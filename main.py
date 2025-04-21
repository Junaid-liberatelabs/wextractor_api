# main.py
import os
import re
import logging
from datetime import datetime

import rich
from dotenv import load_dotenv

from get_glassdoor_data import get_company_reviews_glassdoor
from get_indeed_data import get_company_reviews_indeed
from get_trustpilot_data import get_trustpilot_data
from get_g2_data import get_g2_data
from get_capterra_data import get_capterra_data


load_dotenv()
WEX_TOKEN = os.getenv("WEXTRACTOR_API_KEY")
PAGE_NO = 0

# regex patterns to identify platform & capture the ID/slug
URL_PATTERNS = [
    (
        "glassdoor",
        re.compile(
            r"https?://(?:www\.)?glassdoor\.com/Reviews/[^-]+-Reviews-E(?P<id>\d+)\.htm",
            re.IGNORECASE,
        ),
    ),
    (
        "indeed",
        re.compile(
            r"https?://(?:www\.)?indeed\.com/cmp/(?P<id>[^/]+)/reviews",
            re.IGNORECASE,
        ),
    ),
    (
        "trustpilot",
        re.compile(
            r"https?://(?:www\.)?trustpilot\.com/review/(?P<id>[^/]+)",
            re.IGNORECASE,
        ),
    ),
    (
        "g2",
        re.compile(
            r"https?://(?:www\.)?g2\.com/products/(?P<id>[^/]+)/reviews",
            re.IGNORECASE,
        ),
    ),
    (
        "capterra",
        re.compile(
            r"https?://(?:www\.)?capterra\.com/p/(?P<id>\d+)",
            re.IGNORECASE,
        ),
    ),
]


def parse_url(url: str) -> tuple[str, str] | tuple[None, None]:
    """
    Check each platform pattern and return (platform, identifier).
    Returns (None, None) if URL isn't supported.
    """
    for platform, pattern in URL_PATTERNS:
        m = pattern.search(url)
        if m:
            return platform, m.group("id")
    return None, None


def fetch_reviews(
    url: str, wex_token: str, language: str = "en", page_no: int = 0
) -> list[dict]:
    """
    Given a URL, figure out which get_* function to call and pass in the extracted ID.
    """
    platform, identifier = parse_url(url)
    if not platform:
        raise ValueError(f"Unsupported URL or platform: {url}")

    if platform == "glassdoor":
        return get_company_reviews_glassdoor(
            company_id=identifier, wex_token=wex_token, language=language, page_no=page_no
        )
    elif platform == "indeed":
        return get_company_reviews_indeed(
            company_id=identifier, wex_token=wex_token, language=language, page_no=page_no
        )
    elif platform == "trustpilot":
        return get_trustpilot_data(
            company_id=identifier, wex_token=wex_token, page_no=page_no
        )
    elif platform == "g2":
        return get_g2_data(id=identifier, wex_token=wex_token, page_no=page_no)
    elif platform == "capterra":
        return get_capterra_data(
            id=int(identifier), wex_token=wex_token, page_no=page_no
        )
    else:
        # just in case you add more platforms later
        raise ValueError(f"No handler for platform: {platform}")


if __name__ == "__main__":
    if not WEX_TOKEN:
        rich.print("[red]Error: WEXTRACTOR_API_KEY not set in .env")
        exit(1)

    urls = [
        "https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm",
        
        # _____________________ADD as many urls as you want here________________
        "https://www.indeed.com/cmp/Google/reviews",
        "https://www.trustpilot.com/review/www.google.com",
        "https://www.g2.com/products/google-meet/reviews",
        "https://capterra.com/p/135003/Slack/",
    ]

    for url in urls:
        rich.print(f"\n[yellow]Fetching reviews for:[/yellow] {url}")
        try:
            reviews = fetch_reviews(url, WEX_TOKEN, language="en", page_no=PAGE_NO)
            for i, rev in enumerate(reviews, start=1):
                rich.print(f"[{i}] {rev}")
        except Exception as e:
            rich.print(f"[red]Error fetching reviews for {url}: {e}")
