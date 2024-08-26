from factories.strategy_factory import StrategyFactory
from cache.caching_service import CachingService
import time
from config.config import Config

class ScraperService:
    def __init__(self, storage_service, notification_service):
        self.storage_service = storage_service
        self.notification_service = notification_service
        self.cache_service = CachingService()

    def scrape(self, num_pages: int, proxy: str = None):
        strategy = StrategyFactory.create_strategy(
        use_proxy= proxy is not None,
        proxy= proxy
    )
        attempts = 0
        success = False
        scraped_data = []

        while attempts < Config.RETRY_ATTEMPTS and not success:
            try:
                scraped_data = strategy.scrape_data(num_pages)
                success = True
            except Exception as e:
                attempts += 1
                print(f"Scraping failed, retrying in 5 seconds... (Attempt {attempts}/{Config.RETRY_ATTEMPTS})")
                time.sleep(5)
                if attempts == Config.RETRY_ATTEMPTS:
                    print("Max retry attempts reached. Exiting.")
                    raise e

        # Cache validation and storage
        new_data = []
        for item in scraped_data:
            if self.cache_service.has_changed(item['product_title'], item['product_price']):
                self.cache_service.cache_result(item['product_title'], item['product_price'])
                new_data.append(item)


        self.storage_service.save(new_data)
        self.notification_service.notify(f"Scraping completed. {len(new_data)} items were updated in the storage.")

        return new_data
