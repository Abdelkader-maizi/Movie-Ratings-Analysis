
import pandas as pd

# Input and output files
INPUT_FILE = "data/raw/movie_details.csv"
OUTPUT_FILE = "data/processed/movies_cleaned.csv"


def clean_data():
    # Load raw dataset
    df = pd.read_csv(INPUT_FILE)

    print("Original dataset:", df.shape)

    # Operation 1: Remove duplicate rows
    df = df.drop_duplicates(subset="url")

    # Operation 2: Clean text columns
    text_columns = ["title", "description", "url"]

    for column in text_columns:
        df[column] = df[column].astype("string").str.strip()

    # Operation 3: Validate and convert data types
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    # Remove invalid records
    df = df.dropna(subset=["title", "year", "rating", "url"])

    # Keep only valid ratings
    df = df[df["rating"].between(0, 5)]

    # Convert year to integer
    df["year"] = df["year"].astype(int)

    # Save cleaned dataset
    df.to_csv(OUTPUT_FILE, index=False)

    print("\nData cleaning completed!")
    print("Cleaned dataset:", df.shape)
    print("Output file:", OUTPUT_FILE)


if __name__ == "__main__":
    clean_data()
