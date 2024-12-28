# Twitter Trending Topics Scraper

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Configuration](#configuration)

---

## Introduction
The **Twitter Trending Topics Scraper** is a Python-based project that automates the process of logging into Twitter, scraping trending topics from the "What's Happening" section, and saving the results to a MongoDB database. The scraper leverages Selenium WebDriver for browser automation and includes support for proxy servers and headless browsing.

---

## Features
- **Automated Login:** Logs into Twitter using the provided credentials.
- **Trending Topics Scraping:** Extracts the top 5 trending topics from the "What's Happening" section.
- **Proxy Support:** Includes optional support for HTTP/HTTPS proxies with or without authentication.
- **Headless Mode:** Runs the browser in headless mode for efficiency.
- **Data Storage:** Saves the scraped data in a MongoDB database with unique IDs and timestamps.

---

## Prerequisites
Before running the project, ensure you have the following:
1. **Python 3.8+** installed on your system.
2. **Google Chrome browser** and a compatible version of **ChromeDriver**.
3. **MongoDB** installed and running locally or on a remote server.
4. A valid **Twitter account** for login.
5. (Optional) A working **proxy server** for network requests.

---

## Installation

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/twitter-trending-scraper.git
cd twitter-trending-scraper
```

### Step 2: Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Step 3: Configure ChromeDriver
Download ChromeDriver from ChromeDriver and place it in the drivers/ folder.

---

## Configuration

### settings.py Example
```bash
PROXY_URL = "http://username:password@proxy_ip:proxy_port"
TWITTER_USERNAME = "your_username"
TWITTER_PASSWORD = "your_password"
MONGODB_URI = "mongodb://localhost:27017/"
```
