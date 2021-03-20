from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time

# def init_browser():
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # executable_path = {'executable_path': "chromedriver.exe"}
    # return Browser('chrome', **executable_path, headless=False)

executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)
browser = Browser("chrome", executable_path="chromedriver", headless=True)


# create empty dictinary
mars_info = {}

# NASA Mars News
def scrape():

    # browser = init_browser()

    # visit NASA Mars news site
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)

    time.sleep(1)

    # Scrape page into Soup
    news_html = browser.html
    news_soup = bs(news_html, "html.parser")


    # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.
    news_title = news_soup.find_all('div', class_="content_title")[1].text
    news_p = news_soup.find_all('div', class_="article_teaser_body")[0].text
    print(news_title)
    print(mars_info)

    # Add entries into dictionary
    mars_info['news_title'] = news_title
    mars_info['news_p'] = news_p

    # browser.quit()


# JPL Mars Space Images
# def scrape_image():

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

    # Add entry into dictionary
    mars_info['featured_image_url'] = featured_image_url

    # browser.quit()

# Mars Facts
# def scrape_facts():

    # Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet
    facts_url = "https://space-facts.com/mars/"

    # Use Panda's `read_html` to parse the url
    tables = pd.read_html(facts_url)

    # create dataframe
    facts_df = tables[0]
    facts_df.columns = ['Description', 'Value']
    facts_df.set_index('Description', inplace=True)

    
    # Use Pandas to convert the data to a HTML table string.
    html_table = facts_df.to_html()

    # Add entry into dictionary
    mars_info['html_table'] = html_table


# Mars Hemispheres
# def scrape_hemispheres():

    # Read HTML from website and create a Beautiful Soup object
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemi_base_url = "https://astrogeology.usgs.gov"
    browser.visit(hemi_url)

    # Scrape page into Soup
    hemi_html =browser.html
    hemi_soup = bs(hemi_html, 'html.parser')

    # extract instances of hemisphere information
    hemispheres = hemi_soup.find_all('div', class_="item")
    # hemispheres

    #create empty list to store urls 
    hemi_image_urls = []

    # Loop through hemisphere data
    for x in hemispheres:
        
        # extract enhanced image url and store in empty list
        hemi_image_urls.append(f"{hemi_base_url}{x.find('a', class_='itemLink')['href']}")

    #create empty list to store urls 
    hemisphere_urls = []

    for link in hemi_image_urls:
        browser.visit(link)
        
        time.sleep(1)
        
        hemi_html =browser.html
        hemi_soup = bs(hemi_html, 'html.parser')

        image_url = hemi_soup.find('img', class_="wide-image")['src']
        title = hemi_soup.find('h2', class_="title").text

        # create Python dictionary to store data
        hemisphere_dict = {
            'title':title,
            'img_url': hemi_base_url + image_url
        }

        hemisphere_urls.append(hemisphere_dict)

    # mars_info['hemisphere_dict'] = hemisphere_dict
    mars_info['hemisphere_urls'] = hemisphere_urls

    browser.quit()

    return mars_info