import logging
from etl.feed_process import FeedProcess
from etl.utils import Database

# Map string names to actual classes
from etl.extractors.feed_a import FeedAExtractor
from etl.transformers.feed_a import FeedATransformer
from etl.loaders.feed_a import FeedALoader
from etl.extractors.feed_b import FeedBExtractor
from etl.transformers.feed_b import FeedBTransformer
from etl.loaders.feed_b import FeedBLoader

EXTRACTOR_MAP = {
    'FeedAExtractor': FeedAExtractor,
    'FeedBExtractor': FeedBExtractor,
}
TRANSFORMER_MAP = {
    'FeedATransformer': FeedATransformer,
    'FeedBTransformer': FeedBTransformer,
}
LOADER_MAP = {
    'FeedALoader': FeedALoader,
    'FeedBLoader': FeedBLoader,
}

def run_etl_from_db(connection_string):
    db = Database(connection_string)
    configs = db.get_feed_configs()
    for config in configs:
        feed_name = config['feed_name']
        extractor_cls = EXTRACTOR_MAP[config['extractor']]
        transformer_cls = TRANSFORMER_MAP[config['transformer']]
        loader_cls = LOADER_MAP[config['loader']]
        params = eval(config['params']) if config['params'] else {}
        process = FeedProcess(
            extractor=extractor_cls(db=db.conn),
            transformer=transformer_cls(db=db.conn),
            loader=loader_cls(db=db.conn),
            db=connection_string
        )
        logging.info(f"--- Running ETL for {feed_name} ---")
        try:
            process.run(feed_name=feed_name, **params)
        except Exception as e:
            logging.error(f"ETL failed for {feed_name}: {e}")
    db.close()

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s %(message)s',
        handlers=[logging.StreamHandler()]
    )
    # Example connection string, replace with your actual values
    conn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=your_server;'
        'DATABASE=your_db;'
        'UID=your_user;'
        'PWD=your_password'
    )
    run_etl_from_db(conn_str)
