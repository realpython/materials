from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import (Static, Button, ContentSwitcher, 
DataTable, Markdown, Sparkline)

HARRY_POTTER_BOOKS = [
# Title, Publication date, Pages, Words, Sales

    ("Harry Potter and the Philosopher's Stone", 1997, 223, 76944, "120 million"),
    ("Harry Potter and the Chamber of Secrets",  1998, 251, 85141 , "77 million"),
    ("Harry Potter and the Prisoner of Azkaban", 1999, 317, 107253, "65 million"),
    ("Harry Potter and the Goblet of Fire", 2000, 636 , 190637 , "65 million"),
    ("Harry Potter and the Order of the Phoenix", 2003, 766, 257045 , "65 million"),
    ("Harry Potter and the Half-Blood Prince", 2005,  607,  168923 , "65 million"),
    ("Harry Potter and the Deathly Hallows", 2007, 607 , 198227 , "65 million"),
]


def markdown_example() -> str:
    example =  """
# Harry Potter

Harry Potter is a boy wizard in a series of adventures created by JK Rowling.

| Title | Publication Date | Pages | Words | Sales |
| --- | --- | --- | --- | --- |
"""
    for book in HARRY_POTTER_BOOKS:
        example += f"| {book[0]} | {book[1]} | {book[2]} | {book[3]} | {book[4]} |\n"
    return example

class HarryPotterApp(App[None]):
    CSS_PATH = "simple_layout.tcss"

    def compose(self) -> ComposeResult:
        with Horizontal(id="buttons"):  
            yield Button("Publication Dates", id="pub-dates")  
            yield Button("Statistics", id="stats") 
            yield Button("Words per Book", id="words")   
        with ContentSwitcher(initial="pub-dates"):
                with Static(id="pub-dates"):  
                    yield DataTable(id="pub-dates-table")
                with VerticalScroll(id="stats"):
                    yield Markdown(markdown_example())
                
                with Vertical(id="words"):
                    yield DataTable(id="wordcounts-table")
                    words_per_book = [book[3] for book in HARRY_POTTER_BOOKS]                    
                    yield Sparkline(words_per_book, summary_function=max, )



    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one(ContentSwitcher).current = event.button.id  

    def on_mount(self) -> None:
        pub_dates_table = self.query_one("#pub-dates-table")
        pub_dates_table.add_columns("Book", "Year")
        pub_dates_table.add_rows((book[0].ljust(35), book[1]) for book in HARRY_POTTER_BOOKS)
        word_counts_table = self.query_one("#wordcounts-table")
        for title in [book[0] for book in HARRY_POTTER_BOOKS]:
            short_title = ' '.join(title.split()[4:])
            word_counts_table.add_column(short_title)
        word_counts_table.add_row(*[book[3] for book in HARRY_POTTER_BOOKS])


if __name__ == "__main__":
    HarryPotterApp().run()