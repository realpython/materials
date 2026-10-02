import pytest

from bookstore.inventory import Inventory


@pytest.fixture
def inventory():
    return Inventory({"A": 5})


@pytest.fixture
def held_inventory():
    inventory = Inventory({"A": 5})
    inventory.reserve("A", 3)
    return inventory


def test_inventory_on_hand_stocked_isbn_returns_count(inventory):
    result = inventory.on_hand("A")

    assert result == 5


def test_inventory_on_hand_unknown_isbn_returns_zero(inventory):
    result = inventory.on_hand("B")

    assert result == 0


def test_inventory_reserved_nothing_held_returns_zero(inventory):
    result = inventory.reserved("A")

    assert result == 0


def test_inventory_available_nothing_held_returns_on_hand(inventory):
    result = inventory.available("A")

    assert result == 5


def test_inventory_no_stock_on_hand_returns_zero():
    inventory = Inventory()

    result = inventory.on_hand("A")

    assert result == 0


def test_inventory_caller_edits_stock_dict_keeps_own_copy():
    stock = {"A": 5}
    inventory = Inventory(stock)
    stock["A"] = 1

    result = inventory.on_hand("A")

    assert result == 5


def test_inventory_reserve_some_copies_returns_available(inventory):
    result = inventory.reserve("A", 2)

    assert result == 3
    assert inventory.reserved("A") == 2
    assert inventory.on_hand("A") == 5


def test_inventory_reserve_again_adds_to_held(inventory):
    inventory.reserve("A", 2)

    result = inventory.reserve("A", 1)

    assert result == 2
    assert inventory.reserved("A") == 3


def test_inventory_reserve_all_available_returns_zero(inventory):
    result = inventory.reserve("A", 5)

    assert result == 0


@pytest.mark.parametrize(
    ("already_reserved", "quantity", "message"),
    [
        (0, 6, "only 5 copies of A available"),
        (2, 4, "only 3 copies of A available"),
    ],
)
def test_inventory_reserve_more_than_available_raises_value_error(
    inventory, already_reserved, quantity, message
):
    if already_reserved:
        inventory.reserve("A", already_reserved)

    with pytest.raises(ValueError, match=f"^{message}$"):
        inventory.reserve("A", quantity)


def test_inventory_reserve_zero_quantity_raises_value_error(inventory):
    with pytest.raises(ValueError, match="^quantity must be positive$"):
        inventory.reserve("A", 0)


def test_inventory_reserve_unknown_isbn_raises_key_error(inventory):
    with pytest.raises(KeyError, match="^'unknown isbn: B'$"):
        inventory.reserve("B", 1)


def test_inventory_release_some_copies_returns_available(held_inventory):
    result = held_inventory.release("A", 1)

    assert result == 3
    assert held_inventory.reserved("A") == 2


def test_inventory_release_all_held_returns_on_hand(held_inventory):
    result = held_inventory.release("A", 3)

    assert result == 5
    assert held_inventory.reserved("A") == 0


def test_inventory_release_more_than_held_raises_value_error(
    held_inventory,
):
    with pytest.raises(
        ValueError, match="^cannot release 4, only 3 reserved$"
    ):
        held_inventory.release("A", 4)


def test_inventory_release_zero_quantity_raises_value_error(inventory):
    with pytest.raises(ValueError, match="^quantity must be positive$"):
        inventory.release("A", 0)


def test_inventory_release_unknown_isbn_raises_key_error(inventory):
    with pytest.raises(KeyError, match="^'unknown isbn: B'$"):
        inventory.release("B", 1)


def test_inventory_commit_some_held_returns_on_hand(held_inventory):
    result = held_inventory.commit("A", 2)

    assert result == 3
    assert held_inventory.reserved("A") == 1
    assert held_inventory.available("A") == 2


def test_inventory_commit_all_held_returns_on_hand(held_inventory):
    result = held_inventory.commit("A", 3)

    assert result == 2
    assert held_inventory.reserved("A") == 0


def test_inventory_commit_more_than_held_raises_value_error(held_inventory):
    with pytest.raises(ValueError, match="^cannot ship 4, only 3 reserved$"):
        held_inventory.commit("A", 4)


def test_inventory_commit_zero_quantity_raises_value_error(inventory):
    with pytest.raises(ValueError, match="^quantity must be positive$"):
        inventory.commit("A", 0)


def test_inventory_commit_unknown_isbn_raises_key_error(inventory):
    with pytest.raises(KeyError, match="^'unknown isbn: B'$"):
        inventory.commit("B", 1)
