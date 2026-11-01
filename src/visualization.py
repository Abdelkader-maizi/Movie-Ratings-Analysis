
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/processed/movies_cleaned.csv")


def plot_rating_distribution():
    """Visualize the distribution of movie ratings."""

    plt.figure(figsize=(10, 6))

    sns.histplot(
        data=df,
        x="rating",
        bins=10,
        kde=True
    )

    plt.title("Distribution of Movie Ratings")
    plt.xlabel("Movie Rating")
    plt.ylabel("Number of Movies")

    plt.tight_layout()
    plt.savefig("figures/rating_distribution.png", dpi=300)

    plt.show()

def plot_average_rating_by_decade():
    """Visualize average movie ratings by decade."""

    # Create a decade column
    df["decade"] = (df["year"] // 10) * 10

    # Calculate average rating for each decade
    decade_ratings = df.groupby("decade")["rating"].mean()

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=decade_ratings.index,
        y=decade_ratings.values
    )

    plt.title("Average Movie Rating by Decade")
    plt.xlabel("Decade")
    plt.ylabel("Average Rating")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("figures/average_rating_by_decade.png", dpi=300)

    plt.show()

def plot_top_10_movies():
    """Visualize the top 10 highest-rated movies."""

    top_movies = df.nlargest(10, "rating").sort_values("rating")

    plt.figure(figsize=(10, 7))

    sns.barplot(
        data=top_movies,
        x="rating",
        y="title"
    )

    plt.title("Top 10 Highest-Rated Movies")
    plt.xlabel("Movie Rating")
    plt.ylabel("Movie Title")

    plt.tight_layout()

    plt.savefig("figures/top_10_movies.png", dpi=300)

    plt.show()

if __name__ == "__main__":
    plot_rating_distribution()
    plot_average_rating_by_decade()
    plot_top_10_movies()