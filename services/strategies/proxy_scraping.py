import requests
from bs4 import BeautifulSoup
from .scraping_strategy import ScrapingStrategy

class ProxyScrapingStrategy(ScrapingStrategy):
    def __init__(self, proxy: str):
        self.proxy = proxy

    def scrape_data(self, num_pages: int):
        scraped_data = []
        for page in range(2, num_pages + 1):
            url = f"https://dentalstall.com/shop/page/{page}/"
            if page == 1:
                url = f"https://dentalstall.com/shop"
            proxies = {
                'http': self.proxy,
                'https': self.proxy,
            }
            response = requests.get(url, proxies=proxies)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                products = soup.find_all('div', class_='product-card')
                for product in products:
                    title = product.find('h2', class_='product-title').text
                    price = product.find('span', class_='price').text
                    image_url = product.find('img', class_='attachment-woocommerce_thumbnail')['src']
                    scraped_data.append({
                        "product_title": title,
                        "product_price": price,
                        "path_to_image": image_url  # Placeholder, should download and save the image locally
                    })
            else:
                print(f"Failed to scrape page {page} using proxy. Status code: {response.status_code}")
        return scraped_data
