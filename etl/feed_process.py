from etl.extractors.base import BaseExtractor
from etl.transformers.base import BaseTransformer
from etl.loaders.base import BaseLoader
from etl.utils import Database
from etl.settings import settings
from etl.utils import setup_logging
import logging

class FeedProcess:
    def __init__(self, extractor: BaseExtractor, transformer: BaseTransformer, loader: BaseLoader, db=None):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader
        self.db = db
        # Optionally inject db into transformer/loader if needed in future
        setup_logging(settings.log_level)
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self, feed_name=None, **kwargs):
        # Update feed status to 'running' before ETL
        if self.db and feed_name:
            Database(self.db).update_feed_status(feed_name, 'running')
        try:
            self.logger.info(f"Starting ETL process for feed: {feed_name}")
            # Step 1: Extract
            raw_data = self.extractor.extract(**kwargs)
            self.logger.info("Extraction complete.")
            # Step 2: Transform
            transformed_data = self.transformer.transform(raw_data, **kwargs)
            self.logger.info("Transformation complete.")
            # Step 3: Load
            self.loader.load(transformed_data, **kwargs)
            self.logger.info("Load complete.")
            # Update feed status to 'success' after ETL
            if self.db and feed_name:
                Database(self.db).update_feed_status(feed_name, 'success')
            self.logger.info(f"ETL process for feed {feed_name} completed successfully.")
        except Exception as e:
            # Update feed status to 'failed' if ETL fails
            if self.db and feed_name:
                Database(self.db).update_feed_status(feed_name, 'failed')
            self.logger.error(f"ETL process for feed {feed_name} failed: {e}", exc_info=True)
            raise
