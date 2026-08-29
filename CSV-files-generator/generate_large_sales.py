import csv
from pathlib import Path


output_path = Path("data/raw/sales_large.csv")
row_count = 1_000_000
products = (
    ("Laptop", 75_000),
    ("Mouse", 800),
    ("Keyboard", 1_500),
    ("Monitor", 12_000),
    ("Headphones", 3_500),
    ("Webcam", 5_000),
    ("Printer", 18_000),
    ("Tablet", 32_000),
)


with output_path.open("w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(("order_id", "customer_id", "product", "amount"))

    for index in range(1, row_count + 1):
        product, base_amount = products[(index - 1) % len(products)]
        variation = ((index * 37) % 21) - 10
        amount = base_amount * (100 + variation) // 100
        writer.writerow(
            (1_000_000 + index, f"C{1 + ((index - 1) % 250_000):06d}", product, amount)
        )

print(f"Created {output_path} with {row_count:,} data rows")