from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient
from datetime import datetime
import uuid
from config.settings import PROXYMESH_URL, TWITTER_USERNAME, TWITTER_PASSWORD, MONGODB_URI

def configure_driver(proxy_url):
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    if proxy_url:
        options.add_argument(f"--proxy-server={proxy_url}")
    
    # Specify the path to your chromedriver
    service = Service("C://Users//Dharamveer//Drivers//chromedriver.exe")  # Update to the actual path to chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver

def fetch_trending_topics(driver, twitter_url, username, password):
    try:
        print("Navigating to Twitter login page...")
        driver.get(twitter_url)

        print("Waiting for username input field...")
        username_field = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        print("Entering username...")
        username_field.send_keys(username)

        print("Waiting for 'Next' button...")
        next_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/ancestor::div[contains(@role, 'button')]"))
        )
        next_button.click()

        print("Waiting for password input field...")
        password_field = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        print("Entering password...")
        password_field.send_keys(password)

        print("Waiting for 'Log in' button...")
        login_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']/ancestor::div[contains(@role, 'button')]"))
        )
        login_button.click()

        print("Waiting for trending topics to load...")
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), \"What's happening\")]"))
        )

        print("Fetching trending topics...")
        trends = driver.find_elements(By.XPATH, "//span[contains(text(), \"What's happening\")]/ancestor::div[2]//span")[0:5]
        trending_topics = [trend.text for trend in trends]
        return trending_topics

    except Exception as e:
        print(f"Error during scraping: {e}")
        raise

def save_to_mongodb(data):
    try:
        # Save the scraped data to MongoDB
        client = MongoClient(MONGODB_URI)
        db = client["twitter_trends"]
        collection = db["trending_topics"]
        collection.insert_one(data)
        print("Data saved successfully to MongoDB.")
        client.close()
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

def main():
    proxy_url = PROXYMESH_URL
    twitter_url = "https://twitter.com/login"
    username = TWITTER_USERNAME
    password = TWITTER_PASSWORD

    # Validate proxy URL
    if not proxy_url.startswith("http"):
        print("Invalid proxy URL. Skipping proxy setup.")
        proxy_url = None

    driver = configure_driver(proxy_url)

    try:
        # Fetch the trending topics from Twitter
        trending_topics = fetch_trending_topics(driver, twitter_url, username, password)
        if not trending_topics:
            print("Failed to fetch trending topics. Exiting.")
            return {}

        # Get the proxy IP address
        ip_address = proxy_url.split('@')[-1].split(':')[0] if proxy_url else "127.0.0.1"
        
        # Generate a unique ID and timestamp for the data
        unique_id = str(uuid.uuid4())
        timestamp = datetime.now()

        # Create the data dictionary
        data = {
            "_id": unique_id,
            "trend1": trending_topics[0],
            "trend2": trending_topics[1],
            "trend3": trending_topics[2],
            "trend4": trending_topics[3],
            "trend5": trending_topics[4],
            "datetime": timestamp,
            "ip_address": ip_address
        }

        # Save data to MongoDB
        save_to_mongodb(data)

        return data
    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    print(main())
