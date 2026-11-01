
import pandas as pd

# Load scraped movie data
df = pd.read_csv("data/raw/movie_details.csv")

print("Dataset shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nRating statistics:")
print(df["rating"].describe())

print("\nRating values outside the expected range:")
print(df[~df["rating"].between(0, 5, inclusive="both")])
