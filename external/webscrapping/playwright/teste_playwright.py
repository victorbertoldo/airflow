from playwright.sync_api import sync_playwright
import csv

# Initialize Playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the webpage
    page.goto('https://www.bbc.com/news')

    # Extract information
    articles = page.query_selector_all('a.gs-c-promo-heading')[:5]  # Assuming headlines are in <a> tags

    data = []
    for article in articles:
        title = article.inner_text()
        url = article.get_attribute('href')
        data.append({'Title': title, 'URL': url})

    # Write to CSV
    with open('bbc_headlines.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    # Clean up
    browser.close()
