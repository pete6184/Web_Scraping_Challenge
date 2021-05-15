# Web Scraping Homework - Mission to Mars

## Requirements & Summary
This assignment utilized Jupyter Notebook, Pandas, Requests/Splinter, Flask, BeautifulSoup, and MongoDB.

We were tasked with scraping different websites to pull specific information and pictures related to Mars and then creating a single website to display the information we scraped.

I wrote a python script to run the scraping code and then created a route ('/scrape') to import the python script and call the scrape function. I then created a new database via MongoDB to store all the scraped data. Lastly, I created an html (and .css) file to display all the data and pictures that we scraped.

To get the website to open properly you need to run app.py in a live server.


![mission_to_mars](Images/mission_to_mars.png)

## Background
In this assignment, I build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Step 1 - Scraping
I completed the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* I then created a Jupyter Notebook file and used this to complete the scraping and analysis tasks. The following outlined what was scraped:

### NASA Mars News
* Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/), collected the latest News Title and Paragraph Text, and assigned the text to variables to reference later.

### JPL Mars Space Images - Featured Image
* Visited the url for JPL Featured Space Image [here](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html).

* Used splinter to navigate the site and found the image url for the current Featured Mars Image and assigned the url string to a variable called `featured_image_url`.

* Made sure to find the image url to the full size `.jpg` image and saved a complete url string for this image.

### Mars Facts
* Visited the Mars Facts webpage [here](https://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. and  convert the data to a HTML table string.

### Mars Hemispheres
* Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* Clicked each of the links to the hemispheres to find the image url to the full resolution image.

* Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.

- - -

## Step 2 - MongoDB and Flask Application
Used MongoDB with Flask templating to create a new HTML page that displays the information that was scraped from the URLs above.

* Started by converting the Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that executed the scraping code from above and returned one Python dictionary containing all the scraped data.

* Next, I created a route called `/scrape` that imported the `scrape_mars.py` script and called the `scrape` function.

* Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` that queried the Mongo database and passed the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that took the mars data dictionary and displayed all the data in the appropriate HTML elements.

![final_app_part1.png](Images/final_app_part1.png)
![final_app_part2.png](Images/final_app_part2.png)
