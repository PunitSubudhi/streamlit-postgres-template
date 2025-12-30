import os
import logging
    
logger = logging.getLogger(__name__)

# Cache loaded queries here so we don't read disk every time
_QUERY_CACHE = {}

def get_sql_query(filename):
    if filename not in _QUERY_CACHE:
        # Construct path relative to this file
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "queries", filename)
        
        with open(file_path, "r") as f:
            _QUERY_CACHE[filename] = f.read()
            
    return _QUERY_CACHE[filename]