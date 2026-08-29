import csv
from pathlib import Path


output_path = Path("data/raw/sales_quality_test.csv")
products = ("Laptop", "Mouse", "Keyboard", "Monitor", "Headphones")


with output_path.open("w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(("order_id", "customer_id", "product", "amount", "age"))

    valid_rows = []
    for index in range(1, 901):
        row = (
            300000 + index,
            f"Q{index:05d}",
            products[(index - 1) % len(products)],
            500 + ((index * 173) % 100000),
            20 + ((index * 7) % 61),
        )
        valid_rows.append(row)
        writer.writerow(row)

    # Exact duplicates: detected by DataFrame.duplicated().
    for row in valid_rows[:30]:
        writer.writerow(row)

    # Null values: blank fields are interpreted as null by pandas.
    for index in range(30):
        row = list(valid_rows[30 + index])
        row[index % 3 + 1] = ""
        writer.writerow(row)

    # Out-of-range ages: detected by the validator's 0-120 rule.
    for index in range(40):
        row = list(valid_rows[60 + index])
        row[4] = -1 - index if index < 20 else 121 + index
        writer.writerow(row)

print(f"Created {output_path} with 1,000 data rows")