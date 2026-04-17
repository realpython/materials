import altair as alt
from altair.datasets import data

movies = data.movies()
movies = movies.dropna(
    subset=[
        "Production Budget",
        "Worldwide Gross",
        "IMDB Rating",
        "Major Genre",
    ]
)

brush = alt.selection_interval()

scatter = (
    alt.Chart(movies)
    .mark_point()
    .encode(
        x="Production Budget:Q",
        y="Worldwide Gross:Q",
        color=(
            alt.when(brush)
            .then("Major Genre:N")
            .otherwise(alt.value("lightgray"))
        ),
    )
    .add_params(brush)
)

scatter

bars = (
    alt.Chart(movies)
    .mark_bar()
    .encode(
        x="mean(IMDB Rating):Q",
        y="Major Genre:N",
    )
    .transform_filter(brush)
)

scatter & bars
