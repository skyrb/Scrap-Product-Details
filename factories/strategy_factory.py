from services.strategies.basic_scraping import BasicScrapingStrategy
from services.strategies.proxy_scraping import ProxyScrapingStrategy

class StrategyFactory:
    @staticmethod
    def create_strategy(use_proxy: bool = False, proxy: str = None):
        if use_proxy and proxy:
            return ProxyScrapingStrategy(proxy)
        return BasicScrapingStrategy()
