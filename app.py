from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET'])
def home():
    return render_template("index.html")

@app.route("/search", methods = ["POST"])
def search():
    if request.method == "POST":
        search_query = request.form['inp']

        driver = webdriver.Chrome()
        driver.get(f"https://www.flipkart.com/search?q={search_query}")

        links = driver.find_elements(By.TAG_NAME, "a")
        pages = []
        for link in links:
            if "CGtC98" in link.get_attribute("class"): 
                pages.append(link.get_attribute("href"))

        review_list = []
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
                    review_list.append(data)
                else:
                    break

    return render_template("result.html", review_list = review_list)    


if __name__ == "__main__":
    app.run(debug=True)