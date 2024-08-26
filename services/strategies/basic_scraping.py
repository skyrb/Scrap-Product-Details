import requests
from bs4 import BeautifulSoup
from .scraping_strategy import ScrapingStrategy

class BasicScrapingStrategy(ScrapingStrategy):
    def scrape_data(self, num_pages: int):
        scraped_data = []
        for page in range(1, num_pages + 1):
            url = f"https://dentalstall.com/shop/page/{page}/"
            if page == 1:
                url = f"https://dentalstall.com/shop"
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                products = soup.find_all('div', class_='product-inner')
                for product in products:
                    thumbnail = product.find('div',class_='mf-product-thumbnail')
                    img_tag = thumbnail.find('img')
                    title = img_tag.get('alt') if img_tag else None
                    url_tag = thumbnail.find('img')
                    image_url = url_tag.get('data-lazy-src') if url_tag else None
                    price = product.find('span', class_='woocommerce-Price-amount amount').text
                    scraped_data.append({
                        "product_title": title,
                        "product_price": price,
                        "path_to_image": image_url  # Placeholder, should download and save the image locally
                    })
            else:
                print(f"Failed to scrape page {page}. Status code: {response.status_code}")
        return scraped_data
