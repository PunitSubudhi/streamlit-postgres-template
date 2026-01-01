# db/operations.py
from .connection import get_db_connection
import logging

logger = logging.getLogger(__name__)

def log(cpu_temperature: float):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO cpu_temperature (temperature) VALUES (%s)",
                (cpu_temperature,)
            )
            conn.commit()
            logger.info(f"Logged CPU temperature: {cpu_temperature}")
            # get the last inserted id
            cursor.execute("SELECT LASTVAL()")
            last_id = cursor.fetchone()[0]
            return {
                "status": "success",
                "data": {"id": last_id}
            }
        except Exception as e:
            conn.rollback()
            logger.error(f"Failed to log CPU temperature: {e}")
            return {
                "status": "error",
                "message": str(e)
            }
            raise e
        
def get(parameter: str, limit: int = 1):
    if parameter != "cpu_temperature":
        logger.warning(f"Unknown parameter requested: {parameter}")
        return None
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT temperature, recorded_at FROM cpu_temperature ORDER BY recorded_at DESC LIMIT %s", (limit,))
        result = cursor.fetchall()
        if result:
            temperatures = [{"temperature": row[0], "logged_at": row[1]} for row in result]
            logger.info(f"Retrieved {len(temperatures)} CPU temperature records.")
            return {
                "status": "success",
                "data": temperatures
            }
        else:
            logger.info("No CPU temperature records found.")
            return {
                "status": "error",
                "message": "No records found"
            }