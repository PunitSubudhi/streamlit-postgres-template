# db/connection.py
from contextlib import contextmanager
import psycopg2
from psycopg2 import pool
from config import Config
import logging

logger = logging.getLogger(__name__)

_pg_pool = None

def get_pool():
    """Get the PostgreSQL connection pool.

    Returns:
        psycopg2.pool.SimpleConnectionPool: The connection pool instance.
    """
    global _pg_pool
    if _pg_pool is None:
        _pg_pool = pool.SimpleConnectionPool(
            minconn=1, maxconn=10,
            # connection url parameters
            host=Config.DB_HOST,
            database=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD
        )
    return _pg_pool

@contextmanager
def get_db_connection():
    """Context manager to get a database connection from the pool.

    Yields:
        psycopg2.extensions.connection: A database connection.
    """
    pool = get_pool()
    conn = pool.getconn()
    try:
        # yield gives control back to the caller (your operation function)
        yield conn
    finally:
        # This runs automatically when the 'with' block ends or crashes
        pool.putconn(conn)