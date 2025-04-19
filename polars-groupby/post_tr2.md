One of the most common tasks you'll encounter when analyzing Polars data is the need to summarize it. This allows you to make sense of its meaning since the summary often reveals insights in the data that were not apparent in its original form. Two standard summarization techniques are **aggregation** and **grouping**  

When you aggregate data, you take a sequence of related values and condense them into a single value. For example, you may take the results of a class examination and work out an aggregation such as their sum, mean, and maximum values. These aggregate values are single values used to help describe the original data.

A concept related to aggregation is grouping. When you group data, you divide it into separate categories according to some criteria and then analyze each category.

For example, you may be processing examination results. While you could perform an aggregation of the complete set, you may prefer to see information about each course or even each class within a course. To do this, you'd first group the data into separate courses and then by class groups within each course. Then you'd aggregate each class group to, for example, see the mean examination mark for each class across different courses.

**By the end of this tutorial, you'll understand how:**

- You can summarize data using **aggregation**.
- You can use `.filter()` to view on **specific data**.
- Using `.group_by()` allows you to summarize **one or more** columns of your data.
- Your **time series** data can be grouped using `.group_by_dynamic()`.
- You can match summarized data with the original data using **windows functions**.
- **Pivot tables** allow you to group and aggregate rows and columns of data.

In this tutorial, you'll learn how to group data in several ways and perform an aggregation on each group.

Before you start your learning journey, you should already be comfortable with the basics of working with [Polars DataFrames](https://realpython.com/polars-python/). This could be from any previous Polars experience or any other DataFrame library, such as pandas.

{% alert %}
**Note:** If you're familiar with Polars, you'll know that in addition to DataFrames, Polars also supports something called [LazyFrames](https://realpython.com/polars-lazyframe/). While this is an efficient tool when working with large datasets, and you're certainly encouraged to learn how to use them, DataFrames are sufficient for the examples in this tutorial.
{% endalert %}

In addition, you may consider using [Jupyter Notebook](https://realpython.com/jupyter-notebook-introduction/) as you work through many of the examples in this tutorial. Alternatively, [JupyterLab](https://realpython.com/using-jupyterlab/) will enhance your notebook experience, but any Python environment you're comfortable with will be fine.

To get started, you'll need some data. For the central part of this tutorial, you'll use the student performance dataset freely available from the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/320/student+performance). The data in its original form comes in two files: `student-mat.csv` and `student-por.csv`. These contain data on students taking Math and Portuguese language courses, respectively. You'll use a doctored version in this tutorial.

Both files have been altered to include student identification numbers and the subject indicators `M` and `P` and formatted as `maths.parquet` and `portuguese.parquet`. All data has also been merged into a single `course.parquet` file. These three files are available in your download bundle and will be used throughout your learning experience.

The table below shows the fields used in this tutorial:

| Field Name       | Description                        |
|------------------|------------------------------------|
| `absences`       | Number of absences.                |
| `age`            | Student's age.                     |
| `failures`       | Number of failures                 |
| `G1`, `G2`, `G3` | First, second and final grade.     |
| `internet`       | Students have home Internet access. |
| `reason`         | Reason for taking course           |
| `school`         | School attended                    |
| `sex`            | Student gender (`M`, `F`)          |
| `student_id`     | Student's enrollment number.       |
| `subject`        | Subject studied (`M`, `P`)         |

The dataset is quite extensive, containing over thirty fields. If you want to experiment, the `student.txt` file defines every field. This file is also available as part of the tutorial downloads.

To use Polars, you first need to install the Polars library into your Python environment. To install Polars from a command prompt, you use:

```console
$ python -m pip install polars
```

In a Jupyter Notebook, the command is `!python -m pip install polars`.

With everything set up, you're ready to start using Polars to aggregate and group data.

{% quiz 'aggregating-and-grouping-data-in-polars-groupby' %}

## Aggregating Data

Whenever you want to aggregate data without grouping it, you apply an aggregation function directly to the column or columns you wish to analyze.

Suppose you wanted to find the worst absence of all the students in the mathematics class. You could do this as follows:

```pycon
>>> import polars as pl

>>> math_students = pl.read_parquet("maths.parquet")

>>> (
...     math_students
...     .select(pl.col("absences").max())
... )
shape: (1, 1)
┌──────────┐
│ absences │
│ ---      │
│ i64      │
╞══════════╡
│ 75       │
└──────────┘
```

After installing the Polars library earlier, you `import` it into your code with the conventional alias `pl` to access its functionality. This allows you to use the `read_csv()` function to read the contents of `student-mat.csv` into a Polars DataFrame.

With the data now inside a DataFrame, you use its `.select()` [context](https://docs.pola.rs/user-guide/concepts/expressions-and-contexts/) to select the specific columns you want to work with. In this example, you need data from the `absences` column, so specify it using the `pl.col("absences")` expression. You call the expression's `.max()` method to locate the largest `absences` value. As you can see, the worst absence is `75`.

{% alert %}
**Note:** The `.select()` method is also known as a **context**. A context is a method you pass a Polars expression to which, once the expression is executed, returns a result. Depending on the context, the same Polars expression can produce different output. The contexts you'll use in this tutorial are `.select()`, `.filter()`, `.group_by()` and `.with_columns()`.

Don't confuse Polars' contexts with the more widespread Python [context manager](https://realpython.com/python-with-statement/). They're not the same thing.
{% endalert %}

Although the previous example illustrates that aggregating data produces a single value, it doesn't provide any background as to where that value came from. Suppose, for example, you wanted to know which student, or students, have the worst attendance. You need to know more about where this `75` came from. To do this, you filter the DataFrame:

```pycon
>>> math_students = pl.read_parquet("maths.parquet")

>>> (
...     math_students
...     .select(pl.col("student_id", "absences"))
...     .filter(pl.col("absences") == pl.col("absences").max())
... )
shape: (1, 2)
┌────────────┬──────────┐
│ student_id ┆ absences │
│ ---        ┆ ---      │
│ i64        ┆ i64      │
╞════════════╪══════════╡
│ 10277      ┆ 75       │
└────────────┴──────────┘
```

This time, you use `.select()` to select both the `student_id` and `absences` columns. Although you're most interested in the `student_id` value or values, displaying the associated `absences` column will also give their absence information.

To filter the DataFrame so that only information relating to the worst absence is displayed, you use `.filter()`. As a filter condition, you pass in `pl.col("absences") == pl.col("absences").max()` which displays only the `student_id` and `absences` values of rows with an `absences` value equal to the maximum `absences` value of all students studying mathematics. In this case, only student `10277` has this absence amount.

{% alert %}
**Note:** Although the earlier code you've written to select the maximum value in the `absence` column is correct, it's not the only way you'll see computations like this written.

For example, `pl.max("absences")` will do the same thing. This code is [syntactic sugar](https://realpython.com/syntactic-sugar-python/) for `pl.col("absences").max()` to make it look as though you're using a Polar's function when, in fact, you're calling a method on an expression object.

It's also possible to use an attribute syntax. For example, `pl.col.absences` creates an expression equal to `pl.col("absences")`.

In this tutorial, you'll use the `pl.col("absences").max()` syntax form, which is more technically correct.
{% endalert %}

In the examples so far, you've limited your data aggregations to working out maximum values using the `.max()` method of a Polars expression. Polars, of course, supports a range of [methods](https://docs.pola.rs/api/python/stable/reference/expressions/index.html) that can be used on expressions. It's also possible to mix and match them within the same `.select()` context:

```pycon
>>> math_students = pl.read_parquet("maths.parquet")

>>> (
...     math_students
...     .select(
...         min=pl.col("absences").min(),
...         max=pl.col("absences").max(),
...         mean=pl.col("absences").mean(),
...     )
... )
shape: (1, 4)
┌─────┬─────┬──────────┐
│ min ┆ max ┆ mean     │
│ --- ┆ --- ┆ ---      │
│ i64 ┆ i64 ┆ f64      │
╞═════╪═════╪══════════╡
│ 0   ┆ 75  ┆ 5.708861 │
└─────┴─────┴──────────┘
```

Here, you've displayed the highest, lowest, and average absences of mathematical students using the expression methods shown.

This time, you passed each expression to the `.select()` context by [keyword](https://realpython.com/defining-your-own-python-function/#keyword-arguments). The keyword names the column containing the result. For example, you use `mean = pl.col("absences").mean()` to determine the average of `absences` and assign it to the `mean` column in the output.

Keywords are necessary in this example because each column name must be unique. By default, the output columns are named after the data they contain. So the result of `pl.col("absences").mean()` would be placed into a column named `absences`. Without the `min`, `max`, and `mean` variable assignments, Polars would raise a `DuplicateError` because `absences` is duplicated.

{% alert %}
**Note:** It's also possible to aggregate rows of data. Suppose, for example, you wanted to analyze student results for students studying mathematics:

```pycon
>>> math_students = pl.read_parquet("maths.parquet")

>>> math_students.select(
...     "student_id", "G1", "G2", "G3",
...     total=pl.sum_horizontal("G1", "G2", "G3"),
...     mean=pl.mean_horizontal("G1", "G2", "G3"),
... )
shape: (395, 6)
┌────────────┬─────┬─────┬─────┬───────┬───────────┐
│ student_id ┆ G1  ┆ G2  ┆ G3  ┆ total ┆ mean      │
│ ---        ┆ --- ┆ --- ┆ --- ┆ ---   ┆ ---       │
│ i64        ┆ i64 ┆ i64 ┆ i64 ┆ i64   ┆ f64       │
╞════════════╪═════╪═════╪═════╪═══════╪═══════════╡
│ 10001      ┆ 5   ┆ 6   ┆ 6   ┆ 17    ┆ 5.666667  │
│ 10002      ┆ 5   ┆ 5   ┆ 6   ┆ 16    ┆ 5.333333  │
│ 10003      ┆ 7   ┆ 8   ┆ 10  ┆ 25    ┆ 8.333333  │
│ 10004      ┆ 15  ┆ 14  ┆ 15  ┆ 44    ┆ 14.666667 │
│ 10005      ┆ 6   ┆ 10  ┆ 10  ┆ 26    ┆ 8.666667  │
│ …          ┆ …   ┆ …   ┆ …   ┆ …     ┆ …         │
│ 10391      ┆ 9   ┆ 9   ┆ 9   ┆ 27    ┆ 9.0       │
│ 10392      ┆ 14  ┆ 16  ┆ 16  ┆ 46    ┆ 15.333333 │
│ 10393      ┆ 10  ┆ 8   ┆ 7   ┆ 25    ┆ 8.333333  │
│ 10394      ┆ 11  ┆ 12  ┆ 10  ┆ 33    ┆ 11.0      │
│ 10395      ┆ 8   ┆ 9   ┆ 9   ┆ 26    ┆ 8.666667  │
└────────────┴─────┴─────┴─────┴───────┴───────────┘
```

To compute the sum and mean of student grades, you use the `sum_horizontal()` and `mean_horizontal()` expressions and pass them to the `.select()` context.

To avoid column name clashes, you must pass both expressions by keyword to clearly define the output column headers. For clarity, you also display the columns containing the original grade column data used in each calculation. The `total` and `mean` columns show the sum and average of the data in columns `G1`, `G2`, and `G3`.
{% endalert %}

Just before you move on, try the following exercise:

{% exercise '"Comprehension Check"' %}
The `G3` column in `maths.parquet` contains the students' final grades.

What is the median, most frequent value, and variance of the `G3` results?
{% endexercise %}

{% solution '"Comprehension Check"' %}
One possible solution could be:

```python
┌───────────────┬──────────────────────┬───────────┐
│ middle_result ┆ most_frequent_result ┆ variance  │
│ ---           ┆ ---                  ┆ ---       │
│ f64           ┆ i64                  ┆ f64       │
╞═══════════════╪══════════════════════╪═══════════╡
│ 11.0          ┆ 10                   ┆ 20.989616 │
└───────────────┴──────────────────────┴───────────┘
```

You'll find the code that produced it in the `solutions.ipynb` file in your downloads.
{% endsolution %}

Now that you've been introduced to aggregating data, you'll focus on grouping it.

## Grouping Data for Aggregation With Polars `.group_by()`

Grouping data is often done before performing an aggregation. To group data, you split it into separate categories and then aggregate each. In this section, you'll first see a basic example to introduce the concept, then you'll see a more complex example where you'll appreciate the real power of the Polars expression syntax.

### Grouping Data - Basic Principles

Suppose you wanted to find mathematics and Portuguese language students' minimum, maximum, and mean averages. One way would be to analyze both the `maths.parquet` and `portuguese.parquet` files individually:

```pycon
>>> import polars as pl

>>> math_students = pl.read_parquet("maths.parquet")
>>> portuguese_students = pl.read_parquet("portuguese.parquet")

>>> (
...     math_students
...     .select(
...         min=pl.col("absences").min(),
...         max=pl.col("absences").max(),
...         mean=pl.col("absences").mean(),
...     )
... )
shape: (1, 3)
┌─────┬─────┬──────────┐
│ min ┆ max ┆ mean     │
│ --- ┆ --- ┆ ---      │
│ i64 ┆ i64 ┆ f64      │
╞═════╪═════╪══════════╡
│ 0   ┆ 75  ┆ 5.708861 │
└─────┴─────┴──────────┘

>>> (
...     portuguese_students
...     .select(
...         min=pl.col("absences").min(),
...         max=pl.col("absences").max(),
...         mean=pl.col("absences").mean(),
...     )
... )
shape: (1, 3)
┌─────┬─────┬──────────┐
│ min ┆ max ┆ mean     │
│ --- ┆ --- ┆ ---      │
│ i64 ┆ i64 ┆ f64      │
╞═════╪═════╪══════════╡
│ 0   ┆ 32  ┆ 3.659476 │
└─────┴─────┴──────────┘
```

This code is very similar to your earlier example, except this time, you've applied it to the contents of both your `maths.parquet` and `portuguese.parquet` files. You'll recognize the first set of answers from earlier, but the additional analysis has revealed higher absenteeism in mathematics than in Portuguese. However, some keen students in both classes have never missed a lesson.

While running the same code multiple times certainly gives you the correct answer, it's inefficient for analyzing different data groups.

A better way is to use the `.group_by()` context:

```pycon
>>> all_students = pl.read_parquet("course.parquet")

>>> (
...     all_students
...     .group_by("subject")
...     .agg(
...         min=pl.col("absences").min(),
...         max=pl.col("absences").max(),
...         mean=pl.col("absences").mean(),
...     )
... )
shape: (2, 4)
┌─────────┬─────┬─────┬──────────┐
│ subject ┆ min ┆ max ┆ mean     │
│ ---     ┆ --- ┆ --- ┆ ---      │
│ str     ┆ i64 ┆ i64 ┆ f64      │
╞═════════╪═════╪═════╪══════════╡
│ M       ┆ 0   ┆ 75  ┆ 5.708861 │
│ P       ┆ 0   ┆ 32  ┆ 3.659476 │
└─────────┴─────┴─────┴──────────┘
```

This time, you've computed both result sets using `.group_by()`. When you pass `subject` into the `.group_by()` context, you return a `GroupBy` object that gathers, or groups, the data together according to the different values in the `subject` column. There will be two groups: one for mathematics students, denoted by the letter `M`, and another for Portuguese students, denoted by `P`.

Once you have your GroupBy object, you can use its `.agg()` method to perform an aggregation. In this case, because you want the minimum, maximum, and average values for each of the two groups, you pass in the same expressions as before, again with keywords to avoid name conflicts.

This time, your results show you've applied `.min()`, `.max()`, and `.mean()` to each of the two groups separately and not to the complete dataset as a whole.

### Grouping Data - The Power of Expressions

One of the powerful features of passing expressions into `.agg()` is that any expressions you pass are calculated based on the groups defined within the GroupBy object created by `.group_by()`. Provided you can formulate your aggregation into an expression, you can use it in `.agg()` and apply it to groupings. This makes writing complex grouped aggregations more logical.

For example, suppose you wanted to analyze `absences` a little deeper. You want to find out how many mathematics students with `absences` greater than the mean `absences` for their `age`, still managed to pass the subject. A student has passed if their overall grade, `G3`, is `13` or higher.

To begin with, you need to group the `G3` data by `age`. You decide to write some intermediate code to see how this looks:

```pycon
>>> math_students = pl.read_parquet("maths.parquet")

>>> (
...     math_students
...     .group_by("age")
...     .agg(
...         passes=pl.col("G3"),
...     )
... )
shape: (8, 2)
┌─────┬───────────────┐
│ age ┆ passes        │
│ --- ┆ ---           │
│ i64 ┆ list[i64]     │
╞═════╪═══════════════╡
│ 17  ┆ [6, 6, … 16]  │
│ 21  ┆ [7]           │
│ 20  ┆ [18, 15, 9]   │
│ 15  ┆ [10, 15, … 7] │
│ 16  ┆ [10, 15, … 8] │
│ 22  ┆ [8]           │
│ 19  ┆ [9, 0, … 9]   │
│ 18  ┆ [6, 0, … 10]  │
└─────┴───────────────┘
```

To group the maths students by `age`, you pass this into `.group_by()`, and to specify the data you want aggregated, you pass the `G3` column into `.agg()` since this contains the students' overall grade. The aggregated data for each `age` group is placed into a list because you haven't specified any aggregation computations to be carried out.

Currently, the `passes` column contains all the aggregated data. Since you're only interested in the data of passing students with above average `absences` for their age group, you need to add some filters:

```pycon hl_lines="7-10"
>>> math_students = pl.read_parquet("maths.parquet")

>>> (
...     math_students
...     .group_by("age")
...     .agg(
...         passes=pl.col("G3").filter(
...             pl.col("absences") > pl.col("absences").mean(),
...             pl.col("G3") >= 13,
...         )
...     )
... )
shape: (8, 2)
┌─────┬────────────────┐
│ age ┆ passes         │
│ --- ┆ ---            │
│ i64 ┆ list[i64]      │
╞═════╪════════════════╡
│ 18  ┆ [14, 18, … 13] │
│ 20  ┆ []             │
│ 16  ┆ [15, 14, … 18] │
│ 15  ┆ [15, 13, … 15] │
│ 22  ┆ []             │
│ 21  ┆ []             │
│ 19  ┆ [13, 13, … 13] │
│ 17  ┆ [13, 18, … 15] │
└─────┴────────────────┘
```

The filters you apply ensure only the `G3` figures of `13` or higher and belonging to students with above average `absences` are included. As you can see, the lists now reflect this. However, the specific marks don't interest you. You want to see a count of the successes:

```pycon hl_lines="11-13 17"
>>> math_students = pl.read_parquet("maths.parquet")

>>> (
...     math_students
...     .group_by("age")
...     .agg(
...         passes=pl.col("G3").filter(
...             pl.col("absences") > pl.col("absences").mean(),
...             pl.col("G3") >= 13
...         ).count(),
...         poor_attenders=pl.col("G3").filter(
...             pl.col("absences") > pl.col("absences").mean()
...         ).count(),
...     )
...     .select(
...         pl.col("age", "passes", "poor_attenders"),
...         percentage=pl.col("passes") / pl.col("poor_attenders") * 100,
...     )
...     .with_columns(
...         pl.col("percentage").replace(float("NaN"), 0)
...     ).sort("age")
... )
shape: (8, 4)
┌─────┬────────┬────────────────┬────────────┐
│ age ┆ passes ┆ poor_attenders ┆ percentage │
│ --- ┆ ---    ┆ ---            ┆ ---        │
│ i64 ┆ u32    ┆ u32            ┆ f64        │
╞═════╪════════╪════════════════╪════════════╡
│ 15  ┆ 15     ┆ 32             ┆ 46.875     │
│ 16  ┆ 11     ┆ 39             ┆ 28.205128  │
│ 17  ┆ 8      ┆ 29             ┆ 27.586207  │
│ 18  ┆ 11     ┆ 31             ┆ 35.483871  │
│ 19  ┆ 4      ┆ 10             ┆ 40.0       │
│ 20  ┆ 0      ┆ 1              ┆ 0.0        │
│ 21  ┆ 0      ┆ 0              ┆ 0.0        │
│ 22  ┆ 0      ┆ 0              ┆ 0.0        │
└─────┴────────┴────────────────┴────────────┘
```

Next, you add a column named `poor_attenders` to the aggregation. This column contains a count of all students in each `age` group whose attendance was below the average for their age group.

In addition to the `age`, `passes`, and `poor_attenders` columns, you also define a column named `percentage` that contains the percentage of passes for each student involved in the analysis. You use `.select()` to make sure all four of these columns are displayed.

When `poor_attenders` is zero, your `percentage` column displays `NaN`. To deal with this [unsightly data](https://realpython.com/polars-missing-data/), you pass `pl.col("percentage").replace(float("NaN"), 0)` into `.with_columns()`. This causes the original column to be replaced with a new one, also named `percentage`, but without the `NaN` values.

Finally, you use `.sort()` to sort the column by age. By default, the sort is in ascending order. If you wanted to reverse this, you'd add `descending=True`.

You also conclude that those with high absences don't do well in their examinations. While many may have good reasons for not attending and may be working independently outwith the class, overall pass rates are poor. Sadly, some students never seem to understand this.

{% alert %}
**Note:** On rare occasions, you may wish to display your output such that the order of the data groupings is the same as in the original data. You can pass `maintain_order=True` to `.group_by()` to do this.

In the previous example, removing `.sort()` and using `.group_by("age", maintain_order=True)` would display the grouped data in its original age order as opposed to sorting it. By default, `maintain_order` is set to `False` because setting it to `True` causes a performance hit. Fortunately, this is not something you'll use very often, but it is available if you need it.
{% endalert %}

Now that you've practiced grouping by a single column, you'll learn how to group multiple columns of data.

## Grouping and Aggregating by Multiple Columns

You've grouped your data using a single column in the examples written so far. While this is a widespread thing to do, Polars allows you to group data by multiple columns. This is often known as **sub-grouping**.

Suppose you want to find the average, highest, and lowest `absences` for each `subject` again, but this time you want to analyze them for each student's `reason` for choosing the course. To do this, you can pass both columns into `.group_by()` in a Python list:

```pycon
>>> import polars as pl

>>> all_students = pl.read_parquet("course.parquet")

>>> (
...     all_students
...     .group_by(["subject", "reason"])
...     .agg(
...         min=pl.col("absences").min(),
...         max=pl.col("absences").max(),
...         mean=pl.col("absences").mean(),
...     ).sort("subject")
... )
shape: (8, 5)
┌─────────┬────────────┬─────┬─────┬──────────┐
│ subject ┆ reason     ┆ min ┆ max ┆ mean     │
│ ---     ┆ ---        ┆ --- ┆ --- ┆ ---      │
│ str     ┆ str        ┆ i64 ┆ i64 ┆ f64      │
╞═════════╪════════════╪═════╪═════╪══════════╡
│ M       ┆ course     ┆ 0   ┆ 23  ┆ 3.972414 │
│ M       ┆ other      ┆ 0   ┆ 20  ┆ 5.611111 │
│ M       ┆ home       ┆ 0   ┆ 75  ┆ 7.146789 │
│ M       ┆ reputation ┆ 0   ┆ 56  ┆ 6.647619 │
│ P       ┆ home       ┆ 0   ┆ 30  ┆ 4.456376 │
│ P       ┆ other      ┆ 0   ┆ 16  ┆ 2.777778 │
│ P       ┆ reputation ┆ 0   ┆ 32  ┆ 3.811189 │
│ P       ┆ course     ┆ 0   ┆ 26  ┆ 3.389474 │
└─────────┴────────────┴─────┴─────┴──────────┘
```

This time, the data is first grouped by `subject` and then, within the subject, it's sub-grouped by `reason`. Finally, the various calculations are performed for each `subject` - `reason` combination.

Interestingly, the highest mean `absences` figures for both subjects correspond to those students who chose the course because it was delivered closest to their home.

{% alert %}
**Note:** If you run this code several times, the row order of the `reason` sub-groupings may change. Although this may not matter to you when sub-grouping data, setting `maintain_order=True` provides predictability. However, as mentioned earlier, doing this comes at a cost because the processing is slower than if `maintain_order` was left at its default value of `False`. Using `.sort()` is usually a better solution if reproducibility is needed.

In addition, setting `maintain_order=True` also blocks the possibility of using [streaming](https://docs.pola.rs/user-guide/concepts/_streaming/), which may cause resource problems if your dataset is huge.
{% endalert %}

Before you go any further, it's time for another opportunity to test your skills:

{% exercise '"Comprehension Check"' %}
The `internet` column in `course.parquet` indicates if the student has home Internet access. You've been asked to investigate how many students taking each subject have access and if this affects their pass rates. Remember, if their `G3` score exceeds `12`, a student has passed.

Display details of the total students, number of passes, and percentage of passes for each subject for those who either have home Internet access or don't.

For a bonus credit, see if you can format the percentages using the percentage (`%`) symbol.
{% endexercise %}

{% solution '"Comprehension Check"' %}
One possible solution could be:

```python
┌─────────┬──────────┬───────┬────────┬────────────┐
│ subject ┆ internet ┆ total ┆ passes ┆ percentage │
│ ---     ┆ ---      ┆ ---   ┆ ---    ┆ ---        │
│ str     ┆ str      ┆ u32   ┆ u32    ┆ str        │
╞═════════╪══════════╪═══════╪════════╪════════════╡
│ M       ┆ no       ┆ 66    ┆ 14     ┆ 21.21%     │
│ M       ┆ yes      ┆ 329   ┆ 117    ┆ 35.56%     │
│ P       ┆ no       ┆ 151   ┆ 45     ┆ 29.8%      │
│ P       ┆ yes      ┆ 498   ┆ 231    ┆ 46.39%     │
└─────────┴──────────┴───────┴────────┴────────────┘
```

You'll find the code that produced it in the `solutions.ipynb` file in your downloads.
{% endsolution %}

Next, you'll learn a little about grouping time data.

## Grouping and Aggregating Time Series With `.group_by_dynamic()`

Time series analysis is a large part of everyday data analysis. Polars has its own grouping method, `.group_by_dynamic(),` which is dedicated to grouping data based on time values.

In this section, you'll use a file named `maths_classes.parquet` that contains details of absence rates for a six-month semester of algebra, geometry, and calculus classes. The file, which is part of the downloadable materials, contains the following fields:

| Field                    | Description                              |
|--------------------------|------------------------------------------|
| class_start              | The start date and time of the class     |
| class_subject            | Either algebra, geometry, or calculus    |
| absences                 | The number of absences                   |
| lecturer_initials        | Initials of lecturer teaching class      |

Before you begin, you decide to take a look at a part of the data:

```pycon
>>> import polars as pl

>>> maths_attendance = pl.read_parquet("maths_classes.parquet")
>>> maths_attendance.head()
shape: (5, 4)
┌─────────────────────┬───────────────┬──────────┬───────────────────┐
│ class_start         ┆ class_subject ┆ absences ┆ lecturer_initials │
│ ---                 ┆ ---           ┆ ---      ┆ ---               │
│ datetime[μs]        ┆ str           ┆ i64      ┆ str               │
╞═════════════════════╪═══════════════╪══════════╪═══════════════════╡
│ 2024-01-03 09:00:00 ┆ algebra       ┆ 3        ┆ DH                │
│ 2024-01-04 13:30:00 ┆ geometry      ┆ 4        ┆ PS                │
│ 2024-01-05 10:00:00 ┆ calculus      ┆ 3        ┆ LM                │
│ 2024-01-10 09:00:00 ┆ algebra       ┆ 2        ┆ DH                │
│ 2024-01-11 13:30:00 ┆ geometry      ┆ 7        ┆ PS                │
└─────────────────────┴───────────────┴──────────┴───────────────────┘
```

The file contains a row for each weekly class in the three mathematical subjects `algebra`, `geometry`, and `calculus`. Each class runs once a week, and the semester starts in January and continues through the end of June. You used `maths_attendance.head()` to view only the first five rows.

Suppose you're reviewing the absences from the course. You'd like to see the total and mean absences for each week. You do this using `.group_by_dynamic()`:

```pycon hl_lines="5"
>>> maths_attendance = pl.read_parquet("maths_classes.parquet")

>>> (
...     maths_attendance
...     .group_by_dynamic(index_column="class_start", every="1w", closed="both")
...     .agg(
...         total_absences=pl.col("absences").sum(),
...         mean_absences=pl.col("absences").mean(),
...     )
... )
shape: (26, 3)
┌─────────────────────┬────────────────┬───────────────┐
│ class_start         ┆ total_absences ┆ mean_absences │
│ ---                 ┆ ---            ┆ ---           │
│ datetime[μs]        ┆ i64            ┆ f64           │
╞═════════════════════╪════════════════╪═══════════════╡
│ 2024-01-01 00:00:00 ┆ 10             ┆ 3.333333      │
│ 2024-01-08 00:00:00 ┆ 10             ┆ 3.333333      │
│ 2024-01-15 00:00:00 ┆ 11             ┆ 3.666667      │
│ 2024-01-22 00:00:00 ┆ 10             ┆ 3.333333      │
│ 2024-01-29 00:00:00 ┆ 4              ┆ 1.333333      │
│ …                   ┆ …              ┆ …             │
│ 2024-05-27 00:00:00 ┆ 15             ┆ 5.0           │
│ 2024-06-03 00:00:00 ┆ 12             ┆ 4.0           │
│ 2024-06-10 00:00:00 ┆ 17             ┆ 5.666667      │
│ 2024-06-17 00:00:00 ┆ 6              ┆ 2.0           │
│ 2024-06-24 00:00:00 ┆ 14             ┆ 4.666667      │
└─────────────────────┴────────────────┴───────────────┘
```

The [`.group_by__dynamic()`](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.group_by_dynamic.html) method allows you to group data based on a time value. Here, you use it to calculate the total and mean weekly absences.

First, you set `index_column="class_start"` to tell `.group_by__dynamic()` to use the `class_start` column for grouping. However, you also need to pass some additional parameters.

Next, you pass `every="1w"` to group `class_start` into weekly intervals. The `"1w"` string starts each week, by default, on Monday.

The final parameter you pass in this example is `closed="both"`. This ensures that the first and last weeks are included in the output.

The expressions you pass to `.agg()` are similar to those you used earlier. Once again, you define the column headings for the results to avoid naming conflicts and make the results easy to read.

Your output contains a row for each week's data. Each row of the `total_absences` column contains the total absences for each week, while the `mean_absences` column contains their average.

Suppose you want to dig deeper and find the total absences for each quarter but group the data by `class_subject`. The code you use to do this is as follows:

```pycon hl_lines="7 9"
>>> maths_attendance = pl.read_parquet("maths_classes.parquet")

>>> (
...     maths_attendance
...     .group_by_dynamic(
...         index_column="class_start",
...         every="1q",
...         closed="both",
...         group_by="class_subject",
...     )
...     .agg(pl.col("absences").sum())
... )
shape: (6, 3)
┌───────────────┬─────────────────────┬──────────┐
│ class_subject ┆ class_start         ┆ absences │
│ ---           ┆ ---                 ┆ ---      │
│ str           ┆ datetime[μs]        ┆ i64      │
╞═══════════════╪═════════════════════╪══════════╡
│ algebra       ┆ 2024-01-01 00:00:00 ┆ 56       │
│ algebra       ┆ 2024-04-01 00:00:00 ┆ 44       │
│ geometry      ┆ 2024-01-01 00:00:00 ┆ 35       │
│ geometry      ┆ 2024-04-01 00:00:00 ┆ 40       │
│ calculus      ┆ 2024-01-01 00:00:00 ┆ 41       │
│ calculus      ┆ 2024-04-01 00:00:00 ┆ 39       │
└───────────────┴─────────────────────┴──────────┘
```

Your code, this time, isn't too different from the previous version. You assign `1q` to the `every` parameter to group the output into quarterly intervals.

To specify that you want to group by `class_subject` within each quarter, you assign `class_subject` to the `group_by` parameter of `.group_by_dynamic()`. You also pass the `pl.col("absences").sum()` expression to `.agg()`.

This time, your output contains three rows for each quarter: one for `algebra`, one for `geometry`, and one for `calculus`. The first and second quarters start on January 1st and April 1st, respectively. The final column shows the total absences for each period.

{% exercise '"Comprehension Check"' %}
Using the data in `maths_classes.parquet`, find each lecturer's monthly average student `absences`.
{% endexercise %}

{% solution '"Comprehension Check"' %}
One possible solution could be:

```python
┌───────────────────┬─────────────────────┬──────────┐
│ lecturer_initials ┆ class_start         ┆ absences │
│ ---               ┆ ---                 ┆ ---      │
│ str               ┆ datetime[μs]        ┆ f64      │
╞═══════════════════╪═════════════════════╪══════════╡
│ DH                ┆ 2024-01-01 00:00:00 ┆ 4.0      │
│ DH                ┆ 2024-02-01 00:00:00 ┆ 3.4      │
│ DH                ┆ 2024-03-01 00:00:00 ┆ 4.25     │
│ DH                ┆ 2024-04-01 00:00:00 ┆ 2.5      │
│ DH                ┆ 2024-05-01 00:00:00 ┆ 2.0      │
│ …                 ┆ …                   ┆ …        │
│ LM                ┆ 2024-02-01 00:00:00 ┆ 3.0      │
│ LM                ┆ 2024-03-01 00:00:00 ┆ 3.4      │
│ LM                ┆ 2024-04-01 00:00:00 ┆ 3.8      │
│ LM                ┆ 2024-05-01 00:00:00 ┆ 3.666667 │
│ LM                ┆ 2024-06-01 00:00:00 ┆ 4.6      │
└───────────────────┴─────────────────────┴──────────┘
```

You'll find the code that produced it in the `solutions.ipynb` file in your downloads.
{% endsolution %}

Next up, you'll learn about Polars window functions.

## Grouping and Aggregating Using Window Functions

Window functions allow you to perform more complex aggregations within the `.select()` context.

In the grouping examples you've seen, the resulting output contained a single row for each data grouping. For example, previously, you grouped the records by `reason` within `subject,` so your result contained a separate row for each `subject`-`reason` combination.

Window functions also perform aggregations over groups. However, they apply their results to *each* of the original rows within the group. Hence, the resulting dataframe will contain the same number of rows as the original.

To use a window function, you again use an aggregation function as you did before. However, this time, you apply the function to the column expression within `.select()` before using `.over()` to apply the results over each group member.

This is best understood by example.

To gauge student motivation, suppose you want to see how the actual absence figure for *each student* compares to the mean average for each `reason` within `school` within `subject`. This is where window functions can help:

```pycon hl_lines="17-18"
>>> all_students = pl.read_parquet("course.parquet")

>>> all_students.select(
...     pl.col("subject", "school", "student_id", "reason", "absences"),
...     mean_absences=(
...         pl.col("absences")
...         .mean()
...         .over("subject", "school", "reason")
...     ),
... )
shape: (1_044, 6)
┌─────────┬────────┬────────────┬────────┬──────────┬───────────────┐
│ subject ┆ school ┆ student_id ┆ reason ┆ absences ┆ mean_absences │
│ ---     ┆ ---    ┆ ---        ┆ ---    ┆ ---      ┆ ---           │
│ str     ┆ str    ┆ i64        ┆ str    ┆ i64      ┆ f64           │
╞═════════╪════════╪════════════╪════════╪══════════╪═══════════════╡
│ M       ┆ GP     ┆ 10001      ┆ course ┆ 6        ┆ 4.104839      │
│ M       ┆ GP     ┆ 10002      ┆ course ┆ 4        ┆ 4.104839      │
│ M       ┆ GP     ┆ 10003      ┆ other  ┆ 10       ┆ 6.518519      │
│ M       ┆ GP     ┆ 10004      ┆ home   ┆ 2        ┆ 7.397959      │
│ M       ┆ GP     ┆ 10005      ┆ home   ┆ 4        ┆ 7.397959      │
│ …       ┆ …      ┆ …          ┆ …      ┆ …        ┆ …             │
│ P       ┆ MS     ┆ 10645      ┆ course ┆ 4        ┆ 2.627119      │
│ P       ┆ MS     ┆ 10646      ┆ course ┆ 4        ┆ 2.627119      │
│ P       ┆ MS     ┆ 10647      ┆ course ┆ 6        ┆ 2.627119      │
│ P       ┆ MS     ┆ 10648      ┆ course ┆ 6        ┆ 2.627119      │
│ P       ┆ MS     ┆ 10649      ┆ course ┆ 4        ┆ 2.627119      │
└─────────┴────────┴────────────┴────────┴──────────┴───────────────┘
```

Your code has created a new `mean_absences` column containing the `mean absences` for each `subject`-`school`-`reason` combination. For example, if you look at the highlighted `mean_absences` value in the two `M`-`GP`-`course` rows, they're both `4.104839`. This is useful for easy comparison.

You created your new column using `pl.col("absences").mean()` to indicate you want the mean of the original `absences` values. This time, instead of using it within `.agg()`, you call `.over("subject", "school", "reason")` to calculate the mean of each `reason` within `school` within `subject` grouping and to apply the mean value to each row of the associated original data. In other words, you've applied the corresponding mean value to each student's row.

For example, look at the `mean_absences` figures in the highlighted lines. These both contain `7.397959` because this is the `mean_absences` value corresponding to the `"subject", "school", "reason"` grouping `M`-`GP`-`home`. Students `10004` and `10005` each belong to this grouping.

Similarly, the bottom five rows in the above output also contain identical `mean_absences` values because they all belong to the same grouping. In this case, it's `P`-`MS`-`course`.

Looking at the output, you notice that some students, for example, student `10001`, have a higher than average number of `absences` for students who study that course in the same school for the same reason. If you're only interested in students with these above-average `absences`, you can filter by the new column:

```pycon
>>> all_students = pl.read_parquet("course.parquet")

>>> all_students.select(
...     pl.col("subject", "school", "student_id", "reason", "absences"),
...     mean_absences=(
...         pl.col("absences")
...         .mean()
...         .over("subject", "school", "reason")
...     ),
... ).filter(pl.col("absences") > pl.col("mean_absences"))
shape: (381, 6)
┌─────────┬────────┬────────────┬────────────┬──────────┬───────────────┐
│ subject ┆ school ┆ student_id ┆ reason     ┆ absences ┆ mean_absences │
│ ---     ┆ ---    ┆ ---        ┆ ---        ┆ ---      ┆ ---           │
│ str     ┆ str    ┆ i64        ┆ str        ┆ i64      ┆ f64           │
╞═════════╪════════╪════════════╪════════════╪══════════╪═══════════════╡
│ M       ┆ GP     ┆ 10001      ┆ course     ┆ 6        ┆ 4.104839      │
│ M       ┆ GP     ┆ 10003      ┆ other      ┆ 10       ┆ 6.518519      │
│ M       ┆ GP     ┆ 10006      ┆ reputation ┆ 10       ┆ 6.72          │
│ M       ┆ GP     ┆ 10019      ┆ course     ┆ 16       ┆ 4.104839      │
│ M       ┆ GP     ┆ 10026      ┆ home       ┆ 14       ┆ 7.397959      │
│ …       ┆ …      ┆ …          ┆ …          ┆ …        ┆ …             │
│ P       ┆ MS     ┆ 10645      ┆ course     ┆ 4        ┆ 2.627119      │
│ P       ┆ MS     ┆ 10646      ┆ course     ┆ 4        ┆ 2.627119      │
│ P       ┆ MS     ┆ 10647      ┆ course     ┆ 6        ┆ 2.627119      │
│ P       ┆ MS     ┆ 10648      ┆ course     ┆ 6        ┆ 2.627119      │
│ P       ┆ MS     ┆ 10649      ┆ course     ┆ 4        ┆ 2.627119      │
└─────────┴────────┴────────────┴────────────┴──────────┴───────────────┘
```

The filter expression is similar to those you used earlier. You use `pl.col("absences") > pl.col("mean_absences")` to make sure only those `absences` greater than the `mean_absences` are included in the results.

Before moving on, it's time for an exercise:

{% exercise '"Comprehension Check"' %}
Using the `course.parquet` data, work out the mean values of the first (`G1`) and second (`G2`) period grades for each `reason` within `subject`. The column headings of your output should be: `subject`, `reason`, `G1`, `mean_G1`, `G2`, and `mean_G2` in this order. Also, only those rows with the `G1` and `G2` values above their group's mean value will be displayed.
{% endexercise %}

{% solution '"Comprehension Check"' %}
One possible solution could be:

```python
┌─────────┬────────────┬─────┬───────────┬─────┬───────────┐
│ subject ┆ reason     ┆ G1  ┆ mean_G1   ┆ G2  ┆ mean_G2   │
│ ---     ┆ ---        ┆ --- ┆ ---       ┆ --- ┆ ---       │
│ str     ┆ str        ┆ i64 ┆ f64       ┆ i64 ┆ f64       │
╞═════════╪════════════╪═════╪═══════════╪═════╪═══════════╡
│ M       ┆ home       ┆ 15  ┆ 10.816514 ┆ 14  ┆ 10.743119 │
│ M       ┆ reputation ┆ 15  ┆ 11.457143 ┆ 15  ┆ 11.257143 │
│ M       ┆ home       ┆ 12  ┆ 10.816514 ┆ 12  ┆ 10.743119 │
│ M       ┆ home       ┆ 16  ┆ 10.816514 ┆ 18  ┆ 10.743119 │
│ M       ┆ home       ┆ 14  ┆ 10.816514 ┆ 15  ┆ 10.743119 │
│ …       ┆ …          ┆ …   ┆ …         ┆ …   ┆ …         │
│ P       ┆ home       ┆ 17  ┆ 11.657718 ┆ 18  ┆ 11.785235 │
│ P       ┆ home       ┆ 14  ┆ 11.657718 ┆ 15  ┆ 11.785235 │
│ P       ┆ other      ┆ 14  ┆ 10.694444 ┆ 17  ┆ 10.777778 │
│ P       ┆ course     ┆ 15  ┆ 10.982456 ┆ 15  ┆ 11.147368 │
│ P       ┆ course     ┆ 11  ┆ 10.982456 ┆ 12  ┆ 11.147368 │
└─────────┴────────────┴─────┴───────────┴─────┴───────────┘
```

You'll find the code that produced it in the `solutions.ipynb` file in your downloads.
{% endsolution %}

The final section of your journey through aggregation and grouping will show you how to create pivot tables in Polars.

## Grouping and Aggregating Using Pivot Tables

A [pivot table](https://realpython.com/how-to-pandas-pivot-table/) is a data analysis tool that allows you to take columns of raw data from a Polars DataFrame, summarize them, and then analyze the summary data. This summarization may include several statistical calculations, such as sums, averages, and so on, revealing insights previously hidden within the original data.

{% alert %}
**Note:** Pivot tables will only work on DataFrames, not LazyFrames. This is because all data needs to be available to allow them to determine what columns are required in their output.
{% endalert %}

Suppose you wanted to analyze the average number of failures and absences for each subject at each school to see if there were any patterns between each. One way of doing this would be to reuse the techniques you've already seen:

```pycon
>>> import polars as pl

>>> all_students = pl.read_parquet("course.parquet")

>>> (
...     all_students
...     .group_by(["subject", "school"])
...     .agg(
...         mean_absence=pl.col("absences").mean(),
...         mean_failure=pl.col("failures").mean(),
...     )
... )
shape: (4, 4)
┌─────────┬────────┬──────────────┬──────────────┐
│ subject ┆ school ┆ mean_absence ┆ mean_failure │
│ ---     ┆ ---    ┆ ---          ┆ ---          │
│ str     ┆ str    ┆ f64          ┆ f64          │
╞═════════╪════════╪══════════════╪══════════════╡
│ M       ┆ GP     ┆ 5.965616     ┆ 0.318052     │
│ M       ┆ MS     ┆ 3.76087      ┆ 0.456522     │
│ P       ┆ MS     ┆ 2.619469     ┆ 0.314159     │
│ P       ┆ GP     ┆ 4.21513      ┆ 0.172577     │
└─────────┴────────┴──────────────┴──────────────┘
```

The output shows the data grouped by school within each `subject`. For each grouping, the mean absence and failure figures are shown.

As an alternative, you could create a pivot table of the data using `.pivot()`:

```pycon
>>> all_students = pl.read_parquet("course.parquet")

>>> (
...     all_students
...     .pivot(
...         on="school",
...         index="subject",
...         values=["absences", "failures"],
...         aggregate_function="mean",
...     )
...     .select(
...         pl.col(
...             "subject", "absences_GP", "failures_GP",
...             "absences_MS", "failures_MS",
...         ),
...     )
... )
shape: (2, 5)
┌─────────┬─────────────┬─────────────┬─────────────┬─────────────┐
│ subject ┆ absences_GP ┆ failures_GP ┆ absences_MS ┆ failures_MS │
│ ---     ┆ ---         ┆ ---         ┆ ---         ┆ ---         │
│ str     ┆ f64         ┆ f64         ┆ f64         ┆ f64         │
╞═════════╪═════════════╪═════════════╪═════════════╪═════════════╡
│ M       ┆ 5.965616    ┆ 0.318052    ┆ 3.76087     ┆ 0.456522    │
│ P       ┆ 4.21513     ┆ 0.172577    ┆ 2.619469    ┆ 0.314159    │
└─────────┴─────────────┴─────────────┴─────────────┴─────────────┘
```

To create your pivot table, you pass several parameters to `.pivot()`. By passing `school` as the `on` parameter, you tell Polars to aggregate the data for each `school`. In this dataset, they are annotated by `GP` and `MS`, and each will have a separate set of results. Passing in a list of columns is possible if you want a more atomic analysis. You'll see this later.

The `index` parameter defines the rows of the output. By passing `subject`, you specify that you want each subject's data in a separate row. You've created separate rows for math (`M`) and Portuguese (`P`). This is similar to the grouping functionality you saw earlier. Although not relevant here, it's also possible to specify sub-groupings by passing in a list of columns to use.

The `values` parameter defines the data columns on which you want to perform the aggregate calculation. In this case, you want to do so on both the `absences` and `failures` columns. This gives you results for both of these.

Finally, you need to define which aggregate calculation you wish to perform. In this case, you want to calculate mean values, which you do by setting `aggregate_function` to `"mean"`. One drawback with `.pivot()` is that you can only pass a single aggregation function to the `aggregate_function` parameter. If you use `.agg()`, you can pass in several aggregation functions, as you saw earlier. However, you only need one here.

To make the output more readable so that each school's mean absence and failure figures are next to each other, you use `.select()` to define the order in which the columns are displayed.

The output shows the mean absences and failures for each subject and school. Interestingly, school `GP` appears to fare slightly better than `MS`. Although its absence rate is higher, its failure rate is lower. If any students are reading this, please don't take it to mean less attendance will mean better success. In practice, the opposite is true.

You might wish to sub-analyze your data to determine if it's related to the reasons for attending the schools. This can be done by tweaking your pivot table:

```pycon hl_lines="5 12"
>>> all_students = pl.read_parquet("course.parquet")
>>> (
...     all_students
...     .pivot(
...         on="school",
...         index=["subject", "reason"],
...         values=["absences", "failures"],
...         aggregate_function="mean",
...     )
...     .select(
...         pl.col(
...             "subject", "reason", "absences_GP",
...             "failures_GP", "absences_MS", "failures_MS",
...         ),
...     )
... )
shape: (8, 6)
┌─────────┬────────────┬─────────────┬─────────────┬─────────────┬─────────────┐
│ subject ┆ reason     ┆ absences_GP ┆ failures_GP ┆ absences_MS ┆ failures_MS │
│ ---     ┆ ---        ┆ ---         ┆ ---         ┆ ---         ┆ ---         │
│ str     ┆ str        ┆ f64         ┆ f64         ┆ f64         ┆ f64         │
╞═════════╪════════════╪═════════════╪═════════════╪═════════════╪═════════════╡
│ M       ┆ course     ┆ 4.104839    ┆ 0.33871     ┆ 3.190476    ┆ 0.52381     │
│ M       ┆ other      ┆ 6.518519    ┆ 0.333333    ┆ 2.888889    ┆ 0.222222    │
│ M       ┆ home       ┆ 7.397959    ┆ 0.357143    ┆ 4.909091    ┆ 0.636364    │
│ M       ┆ reputation ┆ 6.72        ┆ 0.25        ┆ 5.2         ┆ 0.2         │
│ P       ┆ course     ┆ 3.928144    ┆ 0.245509    ┆ 2.627119    ┆ 0.449153    │
│ P       ┆ other      ┆ 3.407407    ┆ 0.185185    ┆ 2.4         ┆ 0.244444    │
│ P       ┆ home       ┆ 4.869565    ┆ 0.130435    ┆ 3.058824    ┆ 0.147059    │
│ P       ┆ reputation ┆ 4.166667    ┆ 0.105263    ┆ 2.413793    ┆ 0.068966    │
└─────────┴────────────┴─────────────┴─────────────┴─────────────┴─────────────┘
```

To perform the calculation on `reason` within `subject`, you pass both as a list to the index parameter. You also adjust `.select()` to include `reason`. These small changes have made significant changes to your output. This time, the result is more atomically analyzed.

Again, it appears that, on average, more students seem to be failing mathematics at `MS` despite their better attendance. The same trend is broadly similar for Portuguese (P). This time, you can also see that those who chose either school because it was closest to their `home` have the highest average absence figures. Perhaps they've chosen convenience due to their lack of interest and for an easy life.

There's just time for one final exercise:

{% exercise '"Comprehension Check"' %}
Create a pivot table that contains rows for gender (`sex`) within each `subject`. For each of these combinations, calculate the average of grade `G1`, and the average of grade `G2`, for each school.
{% endexercise %}

{% solution '"Comprehension Check"' %}
One possible solution could be:

```python
┌─────────┬─────┬───────────┬───────────┬───────────┬───────────┐
│ subject ┆ sex ┆ G1_GP     ┆ G1_MS     ┆ G2_GP     ┆ G2_MS     │
│ ---     ┆ --- ┆ ---       ┆ ---       ┆ ---       ┆ ---       │
│ str     ┆ str ┆ f64       ┆ f64       ┆ f64       ┆ f64       │
╞═════════╪═════╪═══════════╪═══════════╪═══════════╪═══════════╡
│ M       ┆ F   ┆ 10.579235 ┆ 10.92     ┆ 10.398907 ┆ 10.32     │
│ M       ┆ M   ┆ 11.337349 ┆ 10.380952 ┆ 11.204819 ┆ 10.047619 │
│ P       ┆ F   ┆ 12.28692  ┆ 10.582192 ┆ 12.50211  ┆ 10.719178 │
│ P       ┆ M   ┆ 11.602151 ┆ 9.7875    ┆ 11.688172 ┆ 10.0875   │
└─────────┴─────┴───────────┴───────────┴───────────┴───────────┘
```

You'll find the code that produced it in the `solutions.ipynb` file in your downloads.
{% endsolution %}

Congratulations on completing this tutorial. You can now look forward to confidently aggregating and grouping your datasets to reveal previously hidden insights.

## Conclusion

This tutorial taught you how to produce summarized data by aggregating and grouping it in several ways.

In this tutorial, you've learned how to:

- Use simple **aggregation** to find summary values
- **Filter** data based on aggregated values
- Subdivide your data into **groups** and perform aggregations on each group
- Apply summarization techniques to **time series**
- Use **window functions** to compare the summarized data to the original data quickly
- Perform more intense summarizations using **pivot tables**.

While you've had a good overview of typical data aggregation and grouping techniques, you're strongly encouraged to practice using your own datasets or those freely available on sites such as [kaggle](https://www.kaggle.com/). It's also worthwhile keeping an eye on the Polars documentation as well. Matt Harrison's [Effective Polars](https://realpython.com/asins/B0D911QH19/) will give you many worked examples to play with.

{% quiz 'aggregating-and-grouping-data-in-polars-groupby' %}