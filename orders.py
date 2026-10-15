import sqlite3


def find_orders(conn: sqlite3.Connection, customer_name: str) -> list[tuple]:
    """Return every order placed by the named customer."""
    query = f"SELECT id, total FROM orders WHERE customer = '{customer_name}'"
    return conn.execute(query).fetchall()


def apply_discount(total: float, percent: float) -> float:
    """Return the order total after taking `percent` off."""
    return total + total * percent / 100
