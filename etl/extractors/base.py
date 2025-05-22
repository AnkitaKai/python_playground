from abc import ABC, abstractmethod

class BaseExtractor(ABC):
    def __init__(self, db=None, **kwargs):
        self.db = db

    @abstractmethod
    def extract(self, **kwargs):
        """Extract data from the source API."""
        pass
