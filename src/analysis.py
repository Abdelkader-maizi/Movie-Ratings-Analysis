
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/movies_cleaned.csv")


def basic_analysis():
    print("========== DATASET OVERVIEW ==========")

    print("Number of movies:", len(df))
    print("Average rating:", round(df["rating"].mean(), 3))
    print("Highest rating:", df["rating"].max())
    print("Lowest rating:", df["rating"].min())

    print("\n========== TOP 10 MOVIES ==========")

    top_movies = df.nlargest(10, "rating")

    print(top_movies[["title", "year", "rating"]].to_string(index=False))

    print("\n========== AVERAGE RATING BY DECADE ==========")

    # Group movies by decade
    df["decade"] = (df["year"] // 10) * 10

    decade_analysis = df.groupby("decade")["rating"].agg(
        ["mean", "count"]
    ).round(3)

    print(decade_analysis)


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


def linear_regression_analysis():
    print("\n========== LINEAR REGRESSION ==========")

    # Prepare input and target variables
    X = df[["year"]]
    y = df["rating"]

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict movie ratings
    predictions = model.predict(X)

    # Evaluate model performance
    mae = mean_absolute_error(y, predictions)
    r2 = r2_score(y, predictions)

    print("Regression coefficient:", round(model.coef_[0], 6))
    print("Intercept:", round(model.intercept_, 3))
    print("Mean Absolute Error:", round(mae, 4))
    print("R-squared:", round(r2, 4))

    print("\nInterpretation:")
    if model.coef_[0] > 0:
        print("The model indicates a positive relationship.")
    elif model.coef_[0] < 0:
        print("The model indicates a negative relationship.")
    else:
        print("The model indicates no linear relationship.")


if __name__ == "__main__":
    basic_analysis()
    linear_regression_analysis()