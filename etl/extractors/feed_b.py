import logging
from etl.extractors.base import BaseExtractor

class FeedBExtractor(BaseExtractor):
    def __init__(self, db=None, **kwargs):
        super().__init__(db=db, **kwargs)

    def extract(self, **kwargs):
        try:
            logging.info("Extracting data from Feed B API...")
            data = {"feed": "B", "data": [10, 20, 30]}
            logging.info(f"Successfully extracted data: {data}")
            return data
        except Exception as e:
            logging.error(f"Error extracting data from Feed B API: {e}")
            raise
