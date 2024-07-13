import dataclasses

import pytest
from digitar.stroke import Direction, Velocity
from digitar.temporal import Time


@pytest.fixture
def arpeggio():
    return Time(seconds=0.005)


def test_upstroke(arpeggio):
    stroke = Velocity.up(arpeggio)
    assert stroke.direction is Direction.UP
    assert stroke.delay == arpeggio


def test_downstroke(arpeggio):
    stroke = Velocity.down(arpeggio)
    assert stroke.direction is Direction.DOWN
    assert stroke.delay == arpeggio


def test_should_be_immutable(arpeggio):
    velocity = Velocity(Direction.DOWN, arpeggio)
    with pytest.raises(dataclasses.FrozenInstanceError):
        velocity.direction = Direction.UP
