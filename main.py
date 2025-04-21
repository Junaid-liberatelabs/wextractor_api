from get_glassdoor_data import get_company_reviews_glassdoor
from get_indeed_data import get_company_reviews_indeed
from get_trustpilot_data import get_trustpilot_data
from get_g2_data import get_g2_data
from get_capterra_data import get_capterra_data
import os
import logging
from datetime import datetime
import rich

from dotenv import load_dotenv
load_dotenv()
if __name__ == "__main__":
    
    WEX_TOKEN = os.getenv("WEXTRACTOR_API_KEY")
    page_no = 0
    
    #glassdoor review link: https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm
    #SO, GLASSDOOR_COMPANY_ID = "9079"
    GLASSDOOR_COMPANY_ID = "13371" 
    #glassdoor_reviews = get_company_reviews_glassdoor(company_id=GLASSDOOR_COMPANY_ID, wex_token=WEX_TOKEN, page_no=page_no)
    
    #indeed review link: https://www.indeed.com/cmp/Google/reviews
    #SO, INDEED_COMPANY_ID = "Google"
    INDEED_COMPANY_ID = "Google"
    #indeed_reviews = get_company_reviews_indeed(company_id=INDEED_COMPANY_ID, wex_token=WEX_TOKEN, page_no=page_no)
    
    #trustpilot review link: https://www.trustpilot.com/review/www.google.com
    #SO, TRUSTPILOT_COMPANY_ID = "www.google.com"
    TRUSTPILOT_COMPANY_ID = "www.google.com"
    #trustpilot_reviews = get_trustpilot_data(company_id=TRUSTPILOT_COMPANY_ID, wex_token=WEX_TOKEN, page_no=page_no)
    
    #google-meet review link: https://www.g2.com/products/google-meet/reviews
    G2_ID = "google-meet"
    #g2_reviews = get_g2_data(id=G2_ID, wex_token=WEX_TOKEN, page_no=page_no)
    
    #if the url for the software in Capterra is https://capterra.com/p/135003/Slack/ the identifier is 135003
    CAPTERRA_ID = 135003
    capterra_reviews = get_capterra_data(id=CAPTERRA_ID, wex_token=WEX_TOKEN, language="en", page_no=page_no)
    
    
    # Print the reviews
    for i, review in enumerate(capterra_reviews, start=1):
      rich.print(review)