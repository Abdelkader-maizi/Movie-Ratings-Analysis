
"""
Movie Ratings Analysis
Module: Web Scraping
Description: Extract details from 100 Letterboxd movie pages.
"""

import re
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

INPUT_FILE = "data/raw/movies.csv"
OUTPUT_FILE = "data/raw/movie_details.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def extract_movie_details(url, original_title, session):
    """Extract movie information from a Letterboxd page."""

    response = session.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    description_tag = soup.find(
        "meta",
        property="og:description"
    )

    rating_tag = soup.find(
        "meta",
        attrs={"name": "twitter:data2"}
    )

    year_match = re.search(r"\((\d{4})\)", original_title)

    rating = None

    if rating_tag:
        rating_match = re.search(
            r"(\d+(?:\.\d+)?)",
            rating_tag.get("content", "")
        )

        if rating_match:
            rating = float(rating_match.group(1))

    return {
        "title": original_title,
        "year": int(year_match.group(1)) if year_match else None,
        "rating": rating,
        "description": (
            description_tag.get("content")
            if description_tag else None
        ),
        "url": url
    }


def main():
    """Collect details for all movies in the input dataset."""

    movies = pd.read_csv(INPUT_FILE)
    results = []

    with requests.Session() as session:

        for index, movie in movies.iterrows():

            print(
                f"[{index + 1}/{len(movies)}] "
                f"Processing: {movie['title']}"
            )

            try:
                details = extract_movie_details(
                    movie["url"],
                    movie["title"],
                    session
                )

                results.append(details)

                print("Rating:", details["rating"])

            except requests.RequestException as error:
                print("Request failed:", error)

            # Wait between requests to reduce server load
            if index < len(movies) - 1:
                time.sleep(3)

    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_FILE, index=False)

    print("\nScraping completed!")
    print("Successfully processed:", len(df))
    print("Output file:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
