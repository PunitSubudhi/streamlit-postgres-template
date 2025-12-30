# db/operations.py
from .connection import get_db_connection
import logging

logger = logging.getLogger(__name__)

def list_users():
    # The 'with' statement handles the getting AND releasing
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT user_id, username FROM users")
            rows = cur.fetchall()
            
            # Transformation logic
            return [{"id": r[0], "name": r[1]} for r in rows]

def create_user(username, email):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (username, email) VALUES (%s, %s)",
                (username, email)
            )
            # Commit is still needed for writes
            conn.commit()