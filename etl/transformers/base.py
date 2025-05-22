from abc import ABC, abstractmethod

class BaseTransformer(ABC):
    def __init__(self, db=None, **kwargs):
        self.db = db

    @abstractmethod
    def transform(self, data, **kwargs):
        """Transform the extracted data according to business logic."""
        pass
