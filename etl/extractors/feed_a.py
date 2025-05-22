import logging
from etl.extractors.base import BaseExtractor

class FeedAExtractor(BaseExtractor):
    def __init__(self, db=None, **kwargs):
        super().__init__(db=db, **kwargs)

    def extract(self, **kwargs):
        try:
            logging.info("Extracting data from Feed A API...")
            # Simulate extracting data from Feed A's API
            data = {"feed": "A", "data": [1, 2, 3]}
            logging.info(f"Successfully extracted data: {data}")
            return data
        except Exception as e:
            logging.error(f"Error extracting data from Feed A API: {e}")
            raise
