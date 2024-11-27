from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import (
    Header,
    Label,
    SelectionList,
    Sparkline,
    TabbedContent,
    Tree,
)


class TabbedLayoutApp(App):
    DEFAULT_CSS = """
    Sparkline {
    width: 80%;
    margin:1 2;
    }

    #pi > .sparkline--max-color {
        color: $success;
    }
    #e > .sparkline--max-color {
        color: $warning;
    } 
    #ln2 > .sparkline--max-color {
        color: $error;
    } 

    Horizontal > Label {
        color: black;
        background: orange;
        align: center middle;
        margin: 0 0 2 1;
    }
"""

    def compose(self) -> ComposeResult:
        yield Header("Tabbed Layout")
        with TabbedContent("Transport", "Life", "Transcendentals"):
            with VerticalScroll():
                yield self.build_transport_selector()
            yield self.build_tree_of_life()
            with Vertical():
                yield Label("Pi = 3.1415926535...")
                yield Sparkline([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], id="pi")
                yield Label("e = 2.718281828...")
                yield Sparkline([2, 7, 1, 8, 2, 8, 1, 8, 2, 8], id="e")
                yield Label("ln(2) = 0.6931471806...")
                yield Sparkline([0, 6, 9, 3, 1, 4, 7, 1, 8, 0, 6], id="ln2")
                yield Label("Omega = 0.5671432904...")
                yield Sparkline([0, 5, 6, 7, 1, 4, 3, 2, 9, 0, 4], id="omega")

    def build_transport_selector(self) -> SelectionList[int]:
        return SelectionList[int](
            (":airplane: Airplane", 1,),
            (":ambulance: Ambulance", 2,),
            (":articulated_lorry: Lorry", 3,),
            (":auto_rickshaw: Rickshaw", 4,),
            (":automobile: Automobile", 5,),
            (":bicycle: Bicycle", 6,),
            (":blue_car: Blue Car", 7),
            (":broom: Broomstick", 8),
            (":car: Red Car", 9),
            (":delivery_truck: Delivery Truck", 10),
            (":dromedary_camel: Camel", 11),
            (":elephant: Elephant", 12),
            (":fire_engine: Fire Engine", 13),
            (":flying_saucer: UFO", 14),
            (":helicopter: Helicopter", 15),
            (":minibus: Minibus", 16),
            (":motorcycle: Motorcycle", 17),
            (":motor_scooter: Scooter", 18),
            (":police_car: Police Car", 19),
            (":rocket: Rocket", 20),
            (":sailboat: Sailboat", 21),
            (":ship: Ship", 22),
            (":speedboat: Speedboat", 23),
            (":steam_locomotive: Locomotive", 24),
            (":taxi: Taxi", 25),
            (":tractor: Tractor", 26),
            (":train: Train", 27),
            (":trolleybus: Trolleybus", 28),
            (":truck: Truck", 29),
        )
    def build_tree_of_life(self) -> Tree[dict]:
        tree: Tree[dict] = Tree("Life")
        domains = tree.root.add_leaf("Domains",)
        domains.allow_expand = True
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
        animalia = eukarya.add_leaf("Animalia")
        animalia.add_leaf("Chordata")
        animalia.add_leaf("Arthropoda")
        animalia.add_leaf("Mollusca")
        animalia.add_leaf("Cnidaria")
        animalia.add_leaf("Platyhelminthes")
        animalia.add_leaf("Nematoda")
        animalia.add_leaf("Annelida")
        animalia.add_leaf("Echinodermata")
        animalia.add_leaf("Porifera")
        animalia.add_leaf("Ctenophora") 
        animalia.allow_expand = True
        eukarya.allow_expand = True
        return tree
    

if __name__ == "__main__":
    TabbedLayoutApp().run()
