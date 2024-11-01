from flask import Flask, request, render_template
import pymongo.mongo_client
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymongo


# Connecting Database
client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["Review"]

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        search_query = request.form['inp']

        if search_query in database.list_collection_names():
            collection = database[search_query]

        else:
            collection = database[search_query]
            driver = webdriver.Chrome()
            driver.get(f"https://www.flipkart.com/search?q={search_query}")

            links = driver.find_elements(By.TAG_NAME, "a")
            pages = []
            for link in links:
                if "CGtC98" in link.get_attribute("class"): 
                    pages.append(link.get_attribute("href"))

            for link in pages:
                driver.get(link)
                reviews = driver.find_elements(By.CLASS_NAME, "EPCmJX")
                for i, review in enumerate(reviews):
                    if i<3:
                        try:
                            rating = review.find_element(By.CLASS_NAME, "XQDdHH").text
                        except:
                            rating = "No rating found"

                        try:
                            title = review.find_element(By.CLASS_NAME, "z9E0IG").text
                        except:
                            title = "No title found"
                        
                        try:
                            content = review.find_element(By.CLASS_NAME, "ZmyHeo").text
                        except:
                            content = "No content found"

                        try:
                            author = review.find_element(By.CLASS_NAME, "_2NsDsF").text
                        except:
                            author = "No author name found"

                        data = {"Rating": rating, "Title": title, "Content":content, "Author": author}
                        collection.insert_one(data)
                    
                    else:
                        break

        items = collection.find()
        return render_template("index.html", items = items)

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)