# Shared utility functions (logging, helpers, etc.)

import logging

def setup_logging(log_level="INFO"):
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.StreamHandler()]
    )

class Database:
    def __init__(self, connection_string):
        import pyodbc
        self.connection_string = connection_string
        self.conn = pyodbc.connect(connection_string)

    def get_feed_configs(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT feed_name, extractor, transformer, loader, params FROM FeedConfigs")
        configs = []
        for row in cursor.fetchall():
            configs.append({
                'feed_name': row.feed_name,
                'extractor': row.extractor,
                'transformer': row.transformer,
                'loader': row.loader,
                'params': row.params
            })
        cursor.close()
        return configs

    def update_feed_status(self, feed_name, status):
        cursor = self.conn.cursor()
        try:
            cursor.execute("UPDATE FeedConfigs SET status = ? WHERE feed_name = ?", (status, feed_name))
            self.conn.commit()
        except Exception as e:
            import logging
            logging.error(f"Failed to update status to '{status}' for {feed_name}: {e}")
        finally:
            cursor.close()

    def close(self):
        self.conn.close()
