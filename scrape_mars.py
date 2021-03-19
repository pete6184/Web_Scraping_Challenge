from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
from flask import Flask, render_template
from flask_pymongo import PyMongo

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():





# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    costa_data = scrape_costa.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, costa_data, upsert=True)

    # Redirect back to home page
    return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(debug=True)