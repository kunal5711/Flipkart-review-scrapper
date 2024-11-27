# Flipkart Review Scraper

This project is a **web application** built using **Flask** and **Selenium** to scrape product reviews from Flipkart based on a user-provided search query. The application extracts key review details such as rating, title, content, and author and displays them in a user-friendly format.

---

## Features
- **Dynamic Search**: Enter any product name, and the application fetches relevant reviews from Flipkart.
- **Review Details**: Scrapes ratings, titles, content, and author names of reviews.
- **Pagination Handling**: Supports navigating multiple pages of reviews.
- **Interactive Interface**: Simple and user-friendly UI built using Flask templates.
- **CORS Support**: Ensures cross-origin requests are handled seamlessly.

---

## Requirements
### Software
- Python 3.7 or above
- Google Chrome Browser
- ChromeDriver (compatible with your Chrome version)

### Python Libraries
- Flask
- Flask-CORS
- Selenium

Install the required Python libraries:
```bash
pip install flask flask-cors selenium
```

---

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/flipkart-review-scraper.git
   cd flipkart-review-scraper
   ```

2. Place the **ChromeDriver** executable in the system PATH or the project directory.

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

5. Enter a product name in the search bar and hit "Search" to view reviews.

---

## File Structure
- **app.py**: Main Flask application.
- **templates/index.html**: Front-end page for the search query input.
- **templates/result.html**: Front-end page to display scraped reviews.
- **static/**: Folder for any static assets (e.g., CSS, JavaScript).