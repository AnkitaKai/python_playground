from etl.extractors.base import BaseExtractor
from etl.transformers.base import BaseTransformer
from etl.loaders.base import BaseLoader
from etl.utils import Database

class FeedProcess:
    def __init__(self, extractor: BaseExtractor, transformer: BaseTransformer, loader: BaseLoader, db=None):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader
        self.db = db
        # Optionally inject db into transformer/loader if needed in future

    def run(self, feed_name=None, **kwargs):
        # Update feed status to 'running' before ETL
        if self.db and feed_name:
            Database(self.db).update_feed_status(feed_name, 'running')
        try:
            # Step 1: Extract
            raw_data = self.extractor.extract(**kwargs)
            # Step 2: Transform
            transformed_data = self.transformer.transform(raw_data, **kwargs)
            # Step 3: Load
            self.loader.load(transformed_data, **kwargs)
            # Update feed status to 'success' after ETL
            if self.db and feed_name:
                Database(self.db).update_feed_status(feed_name, 'success')
        except Exception as e:
            # Update feed status to 'failed' if ETL fails
            if self.db and feed_name:
                Database(self.db).update_feed_status(feed_name, 'failed')
            raise
