# Movie Ratings Analysis

## 1. Project Description

Movie Ratings Analysis is an academic data analysis project developed as part of the Master's program in Network and Distributed Systems (M1 NDS).

The project collects movie information from Letterboxd, cleans and preprocesses the collected data, performs statistical analysis, applies a Linear Regression model, and visualizes the results.

The dataset contains 100 movies selected from Letterboxd's Top 500 Films list.

## 2. Project Objectives

- Collect movie information using Web Scraping.
- Build a structured movie dataset.
- Clean and preprocess the collected data.
- Explore movie ratings through statistical analysis.
- Apply Linear Regression to study the relationship between release year and movie rating.
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

Note: Letterboxd rankings and ratings may change over time.

## 4. Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Git and GitHub

## 5. Project Structure

```text
Movie-Ratings-Analysis/
├── data/
│   ├── raw/
│   └── processed/
├── figures/
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

### Step 3: Data Analysis

Perform statistical analysis, including:

- Number of movies.
- Average, minimum, and maximum ratings.
- Top 10 highest-rated movies.
- Average rating by decade.

A Linear Regression model is also applied to explore the relationship between movie release year and rating.

### Step 4: Data Visualization

Generate three visualizations:

1. Distribution of Movie Ratings.
2. Average Movie Rating by Decade.
3. Top 10 Highest-Rated Movies.

## 7. Main Results

Dataset size: **100 movies**

- Average rating: 4.445
- Highest rating: 4.68
- Lowest rating: 4.36
- Highest average rating by decade: 1960s (4.471)

### Linear Regression Results

- Regression coefficient: -0.000503
- Mean Absolute Error (MAE): 0.0578
- R-squared: 0.0249

The results indicate a very weak negative linear relationship between release year and movie rating. Release year alone explains only a small proportion of the variation in ratings.

Note: The model was evaluated on the same data used for training, so these metrics represent training performance.

## 8. Visualizations

Generated figures are saved in the `figures/` directory:

- `rating_distribution.png`
- `average_rating_by_decade.png`
- `top_10_movies.png`

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

Note: The scraping module requires `data/raw/movies.csv` as its input file. This file contains the movie URLs collected from the Letterboxd list.

## 10. Author

M1 NDS Student

Université de Médéa

## 11. Academic Project

Data Analysis Project
