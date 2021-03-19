# import dependencies
from flask import Flask, render_template, redirect
# import pymongo
import scrape_mars
from flask_pymongo import PyMongo

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
# conn = 'mongodb://localhost:27017/'
# client = pymongo.MongoClient(conn)
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
# mars_data = mongo.db.mars_data

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    mars_info = mongo.db.mars_info
    
    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mars_info.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)