import hashlib
import pandas as pd


class MetadataService:

    @staticmethod
    def generate_file_hash(file_path: str) -> str:
        sha256_hash = hashlib.sha256()

        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256_hash.update(chunk)

        return sha256_hash.hexdigest()

    @staticmethod
    def get_row_count(file_path: str) -> int:
        df = pd.read_csv(file_path)
        return len(df)