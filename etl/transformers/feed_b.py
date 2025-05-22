import logging
from etl.transformers.base import BaseTransformer

class FeedBTransformer(BaseTransformer):
    def __init__(self, db=None, **kwargs):
        super().__init__(db=db, **kwargs)

    def transform(self, data, **kwargs):
        try:
            logging.info("Transforming Feed B data...")
            result = [x + 5 for x in data["data"]]
            logging.info(f"Transformed Feed B data: {result}")
            return result
        except Exception as e:
            logging.error(f"Error transforming Feed B data: {e}")
            raise
