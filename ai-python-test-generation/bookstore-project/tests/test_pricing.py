from decimal import Decimal

import pytest

from bookstore.pricing import (
    member_discount,
    quote_order,
    shipping_cost,
    tax_rate,
    volume_discount,
)


@pytest.mark.parametrize(
    ("quantity", "expected"),
    [
        (1, Decimal("0.00")),
        (9, Decimal("0.00")),
        (10, Decimal("0.05")),
        (11, Decimal("0.05")),
        (49, Decimal("0.05")),
        (50, Decimal("0.12")),
        (51, Decimal("0.12")),
    ],
)
def test_volume_discount_by_quantity_returns_rate(quantity, expected):
    result = volume_discount(quantity)

    assert result == expected


@pytest.mark.parametrize("quantity", [-1, 0])
def test_volume_discount_non_positive_quantity_raises_value_error(quantity):
    with pytest.raises(ValueError, match="^quantity must be positive$"):
        volume_discount(quantity)


@pytest.mark.parametrize(
    ("member_tier", "expected"),
    [
        ("none", Decimal("0.00")),
        ("plus", Decimal("0.05")),
        ("pro", Decimal("0.10")),
    ],
)
def test_member_discount_known_tier_returns_rate(member_tier, expected):
    result = member_discount(member_tier)

    assert result == expected


def test_member_discount_unknown_tier_raises_value_error():
    with pytest.raises(ValueError, match="^unknown tier: gold$"):
        member_discount("gold")


def test_member_discount_empty_tier_raises_value_error():
    with pytest.raises(ValueError, match="^unknown tier: $"):
        member_discount("")


@pytest.mark.parametrize(
    ("country", "expected"),
    [
        ("US", Decimal("0.00")),
        ("GB", Decimal("0.20")),
        ("DE", Decimal("0.19")),
    ],
)
def test_tax_rate_known_country_returns_rate(country, expected):
    result = tax_rate(country)

    assert result == expected


def test_tax_rate_unknown_country_raises_value_error():
    with pytest.raises(ValueError, match="^unknown country: FR$"):
        tax_rate("FR")


@pytest.mark.parametrize(
    ("subtotal", "expected"),
    [
        (Decimal("0.00"), Decimal("4.99")),
        (Decimal("34.99"), Decimal("4.99")),
        (Decimal("35.00"), Decimal("0.00")),
        (Decimal("35.01"), Decimal("0.00")),
    ],
)
def test_shipping_cost_by_subtotal_returns_charge(subtotal, expected):
    result = shipping_cost(subtotal)

    assert result == expected


@pytest.mark.parametrize(
    ("quantity", "unit_price", "member_tier", "country", "expected"),
    [
        (1, "39.99", "none", "US", Decimal("39.99")),
        (1, "20.00", "none", "US", Decimal("24.99")),
        (1, "34.99", "none", "US", Decimal("39.98")),
        (1, "35.00", "none", "US", Decimal("35.00")),
        (1, "0.00", "none", "US", Decimal("4.99")),
        (10, "39.99", "none", "US", Decimal("379.91")),
        (2, "20.00", "pro", "US", Decimal("36.00")),
        (2, "18.00", "plus", "US", Decimal("39.19")),
        (1, "20.00", "none", "GB", Decimal("29.99")),
        (1, "35.50", "none", "DE", Decimal("42.25")),
        (50, "10.00", "pro", "GB", Decimal("475.20")),
    ],
)
def test_quote_order_valid_order_returns_total(
    quantity, unit_price, member_tier, country, expected
):
    result = quote_order(quantity, unit_price, member_tier, country)

    assert result == expected


def test_quote_order_default_tier_and_country_prices_as_us_non_member():
    result = quote_order(1, "20.00")

    assert result == Decimal("24.99")


def test_quote_order_zero_quantity_raises_value_error():
    with pytest.raises(ValueError, match="^quantity must be positive$"):
        quote_order(0, "10.00")


def test_quote_order_negative_unit_price_raises_value_error():
    with pytest.raises(ValueError, match="^unit price must not be negative$"):
        quote_order(1, "-0.01")


def test_quote_order_unknown_tier_raises_value_error():
    with pytest.raises(ValueError, match="^unknown tier: gold$"):
        quote_order(1, "10.00", member_tier="gold")


def test_quote_order_unknown_country_raises_value_error():
    with pytest.raises(ValueError, match="^unknown country: FR$"):
        quote_order(1, "10.00", country="FR")
