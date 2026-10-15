import pytest

from alien_pet_care.pet import AlienPet


@pytest.fixture
def pet():
    return AlienPet("Zorg")


@pytest.mark.parametrize("times, expected", [(1, 1), (10, 10), (15, 10)])
def test_feed_caps_at_max(pet, times, expected):
    for _ in range(times):
        pet.feed()
    assert pet.fed_level == expected


@pytest.mark.parametrize("times, expected", [(1, 1), (10, 10), (15, 10)])
def test_rest_caps_at_max(pet, times, expected):
    for _ in range(times):
        pet.rest()
    assert pet.rested_level == expected


@pytest.mark.parametrize(
    "fed, rested, expected",
    [(10, 10, True), (9, 10, False), (10, 9, False)],
)
def test_is_happy(pet, fed, rested, expected):
    pet.fed_level, pet.rested_level = fed, rested
    assert pet.is_happy() is expected


@pytest.mark.parametrize(
    "fed, rested, expected",
    [
        (10, 10, "🛸 Happy and thriving!"),
        (4, 0, "👾 Starving! Please feed me."),
        (5, 0, "Doing okay, but still feels a bit empty..."),
    ],
)
def test_get_status(pet, fed, rested, expected):
    pet.fed_level, pet.rested_level = fed, rested
    assert pet.get_status() == expected
