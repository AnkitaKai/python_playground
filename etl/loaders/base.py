from abc import ABC, abstractmethod

class BaseLoader(ABC):
    def __init__(self, db=None, **kwargs):
        self.db = db

    @abstractmethod
    def load(self, data, **kwargs):
        """Load the transformed data into the target system."""
        pass
