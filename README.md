# Movie Ratings Analysis

## 1. Project Description

Movie Ratings Analysis is an academic data analysis project developed as part of the Master's program in Network and Distributed Systems (M1 NDS) at the University of Médéa.

The project collects movie information from Letterboxd, cleans and preprocesses the collected data, performs exploratory and statistical analysis, applies a Linear Regression model, evaluates its performance, and visualizes the results.

The dataset contains 100 movies selected from Letterboxd's Top 500 Films list.

## 2. Project Objectives

- Collect movie information using Web Scraping.
- Build a structured movie dataset.
- Clean and preprocess the collected data.
- Explore movie ratings through statistical analysis.
- Investigate the relationship between release year and movie rating.
- Apply and evaluate a Linear Regression model.
- Compare the model with a baseline predictor.
- Create visualizations to communicate the results.

## 3. Data Source

**Source:** [Letterboxd – Letterboxd's Top 500 Films](https://letterboxd.com/official/list/letterboxds-top-500-films/)

The project uses the first 100 movies from the selected list.

Collected attributes:

- Movie title
- Release year
- Average rating
- Description
- Movie URL

**Note:** Letterboxd rankings and ratings may change over time.

## 4. Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- NumPy
- SciPy
- Scikit-learn
- Matplotlib
- Seaborn
- Git and GitHub

## 5. Project Structure

```text
Movie-Ratings-Analysis/
├── data/
│   ├── raw/
│   │   ├── movies.csv
│   │   └── movie_details.csv
│   └── processed/
│       └── movies_cleaned.csv
├── figures/
│   ├── rating_distribution.png
│   ├── average_rating_by_decade.png
│   ├── top_10_movies.png
│   └── year_rating_relationship.png
├── notebooks/
├── src/
│   ├── scraping.py
│   ├── check_data.py
│   ├── cleaning.py
│   ├── analysis.py
│   └── visualization.py
├── .gitignore
├── README.md
└── requirements.txt
```

## 6. Project Workflow

### Step 1: Web Scraping

Collect movie information from Letterboxd using Requests and BeautifulSoup.

### Step 2: Data Inspection and Cleaning

Inspect the dataset and apply preprocessing operations:

- Remove duplicate movie URLs.
- Remove unnecessary whitespace from text fields.
- Convert year and rating columns to numeric types.
- Handle missing and invalid records.
- Validate rating values.

The initial dataset contained 100 records without missing values or duplicate rows.

### Step 3: Exploratory Data Analysis

Perform statistical analysis, including:

- Number of movies.
- Average, minimum, and maximum ratings.
- Top 10 highest-rated movies.
- Average rating by decade.
- Distribution of movie ratings.

### Step 4: Correlation Analysis

Use Pearson and Spearman correlation coefficients to investigate the relationship between release year and movie rating.

### Step 5: Machine Learning

Apply Linear Regression using release year as the input feature and movie rating as the target variable.

The model is evaluated using:

- Train/Test Split (80% training and 20% testing).
- Mean Absolute Error (MAE).
- Root Mean Squared Error (RMSE).
- R-squared (R²).
- Baseline comparison.
- 5-Fold Cross-Validation.

### Step 6: Data Visualization

Generate four visualizations:

1. Distribution of Movie Ratings.
2. Average Movie Rating by Decade.
3. Top 10 Highest-Rated Movies.
4. Relationship Between Release Year and Movie Rating.

## 7. Main Results

**Dataset size:** 100 movies

- Average rating: 4.445
- Highest rating: 4.68
- Lowest rating: 4.36
- Highest average rating by decade: 1960s (4.471)

### Correlation Analysis

- Pearson correlation: -0.1577
- Pearson p-value: 0.1171
- Spearman correlation: -0.1111
- Spearman p-value: 0.2710

Both correlation coefficients indicate a very weak negative association. The p-values are greater than 0.05, so the observed correlations are not statistically significant.

### Linear Regression Results

The dataset was divided into 80% training data and 20% testing data.

- Regression coefficient: -0.000579
- MAE: 0.0659
- RMSE: 0.0835
- R-squared: -0.0614

The model did not outperform the baseline on this test split.

### 5-Fold Cross-Validation

| Metric | Linear Regression | Baseline |
|---|---:|---:|
| Mean MAE | 0.0603 | 0.0604 |
| Mean RMSE | 0.0745 | 0.0750 |

Linear Regression achieved slightly lower average errors than the baseline model. However, the improvement was very small.

The average R-squared value for Linear Regression was -0.7291, indicating poor explanatory performance and sensitivity to data partitioning.

### Overall Interpretation

The analysis suggests that release year alone is insufficient to explain or reliably predict movie ratings in the selected dataset.

The limited dataset size and narrow range of ratings may also affect model performance.

## 8. Visualizations

Generated figures are saved in the `figures/` directory:

- `rating_distribution.png`
- `average_rating_by_decade.png`
- `top_10_movies.png`
- `year_rating_relationship.png`

## 9. Installation and Execution

Clone the repository:

```bash
git clone https://github.com/Abdelkader-maizi/Movie-Ratings-Analysis.git
cd Movie-Ratings-Analysis
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project modules in order:

```bash
python src/scraping.py
python src/check_data.py
python src/cleaning.py
python src/analysis.py
python src/visualization.py
```

**Note:** The scraping module requires `data/raw/movies.csv` as its input file. This file contains the movie URLs collected from the Letterboxd list.

The scraping step requires an internet connection. Previously collected data files are also included in the repository.

## 10. Author

M1 NDS Student

Université de Médéa

## 11. Academic Project

Data Analysis Project