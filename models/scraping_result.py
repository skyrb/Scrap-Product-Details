from typing import Optional

class ScrapingResultModel:
    def __init__(self, product_title: str, product_price: float, path_to_image: str):
        self.product_title = product_title
        self.product_price = product_price
        self.path_to_image = path_to_image

    def to_dict(self):
        return {
            "product_title": self.product_title,
            "product_price": self.product_price,
            "path_to_image": self.path_to_image
        }

    @staticmethod
    def from_dict(data: dict) -> 'ScrapingResultModel':
        return ScrapingResultModel(
            product_title=data.get("product_title", ""),
            product_price=data.get("product_price", 0.0),
            path_to_image=data.get("path_to_image", "")
        )
