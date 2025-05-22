import logging
from etl.loaders.base import BaseLoader

class FeedBLoader(BaseLoader):
    def __init__(self, db=None, **kwargs):
        super().__init__(db=db, **kwargs)

    def load(self, data, **kwargs):
        try:
            logging.info(f"Loading Feed B data: {data}")
            # Simulate loading
            logging.info("Feed B data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading Feed B data: {e}")
            raise
