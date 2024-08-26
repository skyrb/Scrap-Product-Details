from abc import ABC, abstractmethod

class StorageService(ABC):
    @abstractmethod
    def save(self, data):
        pass


