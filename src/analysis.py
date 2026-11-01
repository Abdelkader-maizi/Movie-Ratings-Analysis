import numpy as np
import pandas as pd

from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 

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

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    # Train the Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict ratings on unseen test data
    predictions = model.predict(X_test)

    # Evaluate the model
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print("\n========== MODEL PERFORMANCE ==========")
    print("Regression coefficient:", round(model.coef_[0], 6))
    print("Intercept:", round(model.intercept_, 3))
    print("MAE:", round(mae, 4))
    print("RMSE:", round(rmse, 4))
    print("R-squared:", round(r2, 4))

    # Create a baseline model
    baseline = DummyRegressor(strategy="mean")
    baseline.fit(X_train, y_train)

    baseline_predictions = baseline.predict(X_test)

    baseline_mae = mean_absolute_error(
        y_test,
        baseline_predictions
    )

    baseline_rmse = np.sqrt(
        mean_squared_error(y_test, baseline_predictions)
    )

    print("\n========== BASELINE COMPARISON ==========")
    print("Baseline MAE:", round(baseline_mae, 4))
    print("Baseline RMSE:", round(baseline_rmse, 4))

    print("\n========== INTERPRETATION ==========")

    if mae < baseline_mae:
        print("Linear Regression performs better than the baseline.")
    else:
        print("Linear Regression does not outperform the baseline.")

    if r2 < 0:
        print("The model performs worse than predicting the test mean.")
    elif r2 < 0.5:
        print("The model has limited explanatory performance.")
    else:
        print("The model explains a substantial proportion of rating variation.")

def correlation_analysis():
    print("\n========== CORRELATION ANALYSIS ==========")

    # Calculate Pearson correlation
    pearson_corr, pearson_p = pearsonr(
        df["year"],
        df["rating"]
    )

    # Calculate Spearman correlation
    spearman_corr, spearman_p = spearmanr(
        df["year"],
        df["rating"]
    )

    print("Pearson correlation:", round(pearson_corr, 4))
    print("Pearson p-value:", round(pearson_p, 4))

    print("\nSpearman correlation:", round(spearman_corr, 4))
    print("Spearman p-value:", round(spearman_p, 4))


def cross_validation_analysis():
    print("\n========== 5-FOLD CROSS-VALIDATION ==========")

    # Prepare input and target variables
    X = df[["year"]]
    y = df["rating"]

    # Define 5-fold cross-validation
    kf = KFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    # Define the regression model
    model = LinearRegression()

    # Evaluate Linear Regression
    regression_scores = cross_validate(
        model,
        X,
        y,
        cv=kf,
        scoring={
            "mae": "neg_mean_absolute_error",
            "rmse": "neg_root_mean_squared_error",
            "r2": "r2"
        }
    )

    # Evaluate the baseline model using the same folds
    baseline = DummyRegressor(strategy="mean")

    baseline_scores = cross_validate(
        baseline,
        X,
        y,
        cv=kf,
        scoring={
            "mae": "neg_mean_absolute_error",
            "rmse": "neg_root_mean_squared_error",
            "r2": "r2"
        }
    )

    # Convert negative error scores to positive values
    regression_mae = -regression_scores["test_mae"]
    regression_rmse = -regression_scores["test_rmse"]

    baseline_mae = -baseline_scores["test_mae"]
    baseline_rmse = -baseline_scores["test_rmse"]

    # Display regression results
    print("\n========== LINEAR REGRESSION ==========")
    print("MAE scores:", regression_mae.round(4))
    print("RMSE scores:", regression_rmse.round(4))
    print("R2 scores:", regression_scores["test_r2"].round(4))

    print("Mean MAE:", round(regression_mae.mean(), 4))
    print("Mean RMSE:", round(regression_rmse.mean(), 4))

    # Display baseline results
    print("\n========== BASELINE MODEL ==========")
    print("MAE scores:", baseline_mae.round(4))
    print("RMSE scores:", baseline_rmse.round(4))
    print("R2 scores:", baseline_scores["test_r2"].round(4))

    print("Mean MAE:", round(baseline_mae.mean(), 4))
    print("Mean RMSE:", round(baseline_rmse.mean(), 4))

    # Compare both models
    print("\n========== MODEL COMPARISON ==========")

    if regression_mae.mean() < baseline_mae.mean():
        print("Linear Regression performs better in MAE.")
    else:
        print("Baseline performs better or equally in MAE.")

    if regression_rmse.mean() < baseline_rmse.mean():
        print("Linear Regression performs better in RMSE.")
    else:
        print("Baseline performs better or equally in RMSE.")


if __name__ == "__main__":
    basic_analysis()
    linear_regression_analysis()
    correlation_analysis()
    cross_validation_analysis()