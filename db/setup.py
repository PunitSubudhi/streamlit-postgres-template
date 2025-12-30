# db/setup.py
from .connection import get_db_connection
from .utils import get_sql_query
import logging

logger = logging.getLogger(__name__)

def initialise_database():
    """Creates tables if they don't exist"""
    init_query = get_sql_query("init.sql")
    
    with get_db_connection() as conn:
        try:
            cur = conn.cursor()
            cur.execute(init_query)
            cur.close()
            conn.commit()
            logger.info("Database initialized successfully.")
        except Exception as e:
            logger.error("Error initializing database", exc_info=True)
            raise e


