from services.metadata_service import MetadataService

file_path = "data/raw/sales.csv"

file_hash = MetadataService.generate_file_hash(file_path)

print("File Hash:")
print(file_hash)

print("\nRow Count:")
print(
    MetadataService.get_row_count(
        "data/raw/sales.csv"
    )
)