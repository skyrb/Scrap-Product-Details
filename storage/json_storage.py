import json
import os
from .storage_service import StorageService

class JSONStorageService(StorageService):
    def __init__(self, ):
        self.file_path =os.path.join(".", 'scraped_data.json')

    def save(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f)


