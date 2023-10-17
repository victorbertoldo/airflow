from playwright.sync_api import sync_playwright, TimeoutError
import csv
import pandas as pd

# Initialize Playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the webpage
    # page.goto('https://www.bbc.com/news')

    try:
        page.goto('https://www.bbc.com/news', timeout=60000)
    except TimeoutError:
        # Handle the timeout error (e.g., retry or log a message)
        pass

    # Extract information
    articles = page.query_selector_all('a.gs-c-promo-heading')[:5]  # Assuming headlines are in <a> tags

    data = []
    for article in articles:
        title = article.inner_text()
        url = article.get_attribute('href')
        data.append({'Title': title, 'URL': url})

    # Write to CSV
    # with open('bbc_headlines.csv', 'w', newline='', encoding='utf-8') as csvfile:
    with open('/home/pwuser/downloads/bbc_headlines.csv', 'w', newline='', encoding='utf-8') as csvfile:        
        fieldnames = ['Title', 'URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    # Clean up
    browser.close()

# now lets check the file and see if it is there
df = pd.read_csv('/home/pwuser/downloads/bbc_headlines.csv')
print(df.head())