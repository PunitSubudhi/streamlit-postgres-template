import logging
import sys
from db.setup import initialise_database
import streamlit as st

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Capture INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)  # Output to console
        #Could add logging.FileHandler("app.log") here to save to file
    ]
)

# Create a logger for this file
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting application setup...")
    initialise_database()
    logger.info("Database setup complete.")
    # Further application logic would go here

st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
    )

st.title("Welcome to My Streamlit App 🚀")