import logging
from etl.loaders.base import BaseLoader

class FeedALoader(BaseLoader):
    def __init__(self, db=None, **kwargs):
        super().__init__(db=db, **kwargs)

    def load(self, data, **kwargs):
        try:
            logging.info(f"Loading Feed A data: {data}")
            # Simulate loading
            logging.info("Feed A data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading Feed A data: {e}")
            raise
