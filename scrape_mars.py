from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)


# create empty dictinary
mars_info = {}

# NASA Mars News
def scrape_news():

    # visit NASA Mars news site
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)

    time.sleep(1)

    # Scrape page into Soup
    news_html = browser.html
    news_soup = bs(news_html, "html.parser")


    # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.
    try:
        news_title = news_soup.find_all('div', class_="content_title")[1].text
        news_p = news_soup.find_all('div', class_="article_teaser_body")[0].text

    except:   
        return None
    return news_title, news_p


# JPL Mars Space Images
def scrape_image():

    # Read HTML from website and create a Beautiful Soup object
    image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(image_url)

    browser.click_link_by_partial_text('FULL IMAGE')

    time.sleep(1)

    # Scrape page into Soup
    image_html = browser.html
    image_soup = bs(image_html, 'html.parser')

    
    image_url = image_soup.find('img', class_='fancybox-image')['src']

    featured_image_url = f"https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{image_url}"

