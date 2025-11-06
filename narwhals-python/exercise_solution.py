import narwhals as nw
from narwhals.typing import IntoFrameT


def rowling_books(df: IntoFrameT, lf: IntoFrameT) -> IntoFrameT:
    return (
        nw.from_native(df)
        .join(nw.from_native(lf).filter(nw.col("last_name").str.contains("Rowling")).collect(), on="author_id")
        .select(["book_title", "year_published", "first_name", "last_name"])
        .sort("year_published")
        .to_pandas()
    )
