import requests
import json

def get_company_reviews_indeed(company_id,wex_token, language="en",page_no=0):
    """
    Fetches reviews from Indeed (implementation would be similar to Glassdoor).
    """
    url = "https://wextractor.com/api/v1/reviews/indeed" 
    params = {
        "id": company_id,
        "language": language,
        "auth_token": wex_token,
        "offset": page_no,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        # with open('indeed_response.json', 'w') as f:
        #     json.dump(data, f, indent=4)
        reviews = data.get("reviews", [])
        return reviews
    else:
        print(f"Failed to fetch reviews. Status Code: {response.status_code}")
        print(response.text)
        return []
