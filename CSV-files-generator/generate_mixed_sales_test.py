import csv
from datetime import date, timedelta
from pathlib import Path


output_path = Path("data/raw/sales_mixed_test.csv")
products = (
    ("Laptop", "Electronics", 75000.50),
    ("Mouse", "Accessories", 800.00),
    ("Keyboard", "Accessories", 1500.25),
    ("Monitor", "Electronics", 12000.75),
    ("Headphones", "Accessories", 3500.00),
    ("Office Chair", "Furniture", 14500.00),
)
payment_methods = ("Credit Card", "UPI", "Debit Card", "Net Banking", "Cash")


def valid_row(index: int) -> list[object]:
    product, category, unit_price = products[(index - 1) % len(products)]
    quantity = 1 + (index % 5)
    order_date = date(2026, 1, 1) + timedelta(days=index - 1)
    return [
        500000 + index,
        f"C{index:05d}",
        product,
        category,
        quantity,
        round(unit_price * quantity, 2),
        round((index * 3.5) % 31, 2),
        order_date.isoformat(),
        (order_date + timedelta(days=3 + index % 5)).isoformat(),
        f"customer{index}@example.com",
        f"+91-98765{index:05d}"[-14:],
        payment_methods[(index - 1) % len(payment_methods)],
        index % 4 == 0,
        18 + (index * 7) % 63,
    ]


headers = (
    "order_id",
    "customer_id",
    "product",
    "category",
    "quantity",
    "amount",
    "discount_percent",
    "order_date",
    "delivery_date",
    "customer_email",
    "customer_phone",
    "payment_method",
    "is_returned",
    "age",
)

rows = [valid_row(index) for index in range(1, 101)]

# Issues supported by the current ValidatorAgent.
rows[10][13] = -5
rows[20][13] = 130
rows[30][4] = ""
rows[40][9] = ""
rows[50][2] = ""
rows[60] = rows[0].copy()

# Additional realistic issues for future validator improvements.
rows[70][4] = -2
rows[71][5] = -100.00
rows[72][9] = "not-an-email"
rows[73][7] = "2026/13/45"
rows[74][12] = "maybe"
rows[75][8] = "2025-12-01"
rows[76][1] = "000123"

with output_path.open("w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"Created {output_path} with {len(rows)} data rows and {len(headers)} columns")