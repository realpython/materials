# from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Label, SelectionList, Sparkline, TabbedContent, Tree


class TabbedLayoutApp(App):
    CSS = """

 Sparkline {
 width: 100%;
 margin:1;
 }

 #pi > .sparkline--max-color {
     color: $success;
 }
 #e > .Sparkline--max_color {
     color: $warning;
 } 
 #ln2 > .Sparkline--max_color {
     color: red;
 } 

 Vertical > Label {
    color: yellow;
    align: center middle;
 }
 
 Grid {
 grid-size: 3 2
 }
"""

    def compose(self) -> ComposeResult:
        yield Header("Tabbed Layout")
        with TabbedContent("Options", "Tree", "Sparklines"):
            yield SelectionList(
                (":beer: Beer", 1, True),
                (":wine_glass: Wine", 2),
                (":cocktail: Cocktails", 3),
                (":pizza: Pizza", 4, True),
                (":hamburger: Burgers", 5),
                (":fries: Fries", 6),
                (":hot_dog: Hot Dogs", 7),
                (":taco: Tacos", 8),
                (":burrito: Burritos", 9),
                (":popcorn: Popcorn", 10),
            )
            yield self.build_tree()
            with Vertical():
                with Horizontal():
                    yield Label("Pi")
                    yield Sparkline([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], id="pi")
                with Horizontal():
                    yield Label("e")
                    yield Sparkline([6, 2, 1, 8, 2, 8, 1, 8, 2, 8], id="e")
                with Horizontal():
                    yield Label("ln(2)")
                    yield Sparkline([0, 6, 9, 3, 1, 4, 7, 1, 8, 0, 6], id="ln2")

    def build_tree(self):
        tree: Tree[dict] = Tree("Life")
        domains = tree.root.add("Domains", expand=True)
        domains.add_leaf("Bacteria")

        archaea = domains.add_leaf("Archaea")
        archaea.add_leaf("Proteoarcheota")
        archaea.add_leaf("Euryarcheota")
        archaea.add_leaf("DPANN")
        archaea.allow_expand = True

        eukarya = domains.add_leaf("Eukarya")
        eukarya.add_leaf("Protista")
        eukarya.add_leaf("Plantae")
        eukarya.add_leaf("Fungi")
        eukarya.add_leaf("Animalia")
        eukarya.allow_expand = True
        tree.root.expand_all()
        return tree


if __name__ == "__main__":
    TabbedLayoutApp().run()
