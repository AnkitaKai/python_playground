import logging
from etl.transformers.base import BaseTransformer

class FeedATransformer(BaseTransformer):
    def __init__(self, db=None, **kwargs):
        super().__init__(db=db, **kwargs)

    def transform(self, data, **kwargs):
        try:
            logging.info("Transforming Feed A data...")
            result = [x * 2 for x in data["data"]]
            logging.info(f"Transformed Feed A data: {result}")
            return result
        except Exception as e:
            logging.error(f"Error transforming Feed A data: {e}")
            raise
