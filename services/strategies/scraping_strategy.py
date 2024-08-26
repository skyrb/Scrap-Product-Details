from abc import ABC, abstractmethod

class ScrapingStrategy(ABC):
    @abstractmethod
    def scrape_data(self, num_pages: int):
        pass