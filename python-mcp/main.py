from typing import Any
import asyncio
from mcp.server.fastmcp import FastMCP
from transactional_db import CUSTOMERS_TABLE, ORDERS_TABLE, PRODUCTS_TABLE

mcp = FastMCP("ecommerce_tools")


@mcp.tool()
async def get_customer_info(customer_id: str) -> str:
    """Search for a customer using their unique identifier"""
    await asyncio.sleep(1)
    customer_info = CUSTOMERS_TABLE.get(customer_id)

    if not customer_info:
        return "Customer not found"

    return str(customer_info)


@mcp.tool()
async def get_order_details(order_id: str) -> str:
    """Get details about a specific order."""
    await asyncio.sleep(1)
    order = ORDERS_TABLE.get(order_id)
    if not order:
        return f"No order found with ID {order_id}."

    items = [
        PRODUCTS_TABLE[sku]["name"]
        for sku in order["items"]
        if sku in PRODUCTS_TABLE
    ]
    return (
        f"Order ID: {order_id}\n"
        f"Customer ID: {order['customer_id']}\n"
        f"Date: {order['date']}\n"
        f"Status: {order['status']}\n"
        f"Total: ${order['total']:.2f}\n"
        f"Items: {', '.join(items)}"
    )


@mcp.tool()
async def check_inventory(product_name: str) -> str:
    """Search inventory for a product by product name."""
    await asyncio.sleep(1)
    matches = []
    for sku, product in PRODUCTS_TABLE.items():
        if product_name.lower() in product["name"].lower():
            matches.append(
                f"{product['name']} (SKU: {sku}) — Stock: {product['stock']}"
            )
    return "\n".join(matches) if matches else "No matching products found."


@mcp.tool()
async def get_customer_ids_by_name(customer_name: str) -> list[str]:
    """Get customer IDs by using a customer's full name"""
    await asyncio.sleep(1)
    return [
        cust_id
        for cust_id, info in CUSTOMERS_TABLE.items()
        if info.get("name") == customer_name
    ]


@mcp.tool()
async def get_orders_by_customer_id(
    customer_id: str,
) -> dict[str, dict[str, str]]:
    """Get orders by customer ID"""
    await asyncio.sleep(1)
    return {
        order_id: order
        for order_id, order in ORDERS_TABLE.items()
        if order.get("customer_id") == customer_id
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
