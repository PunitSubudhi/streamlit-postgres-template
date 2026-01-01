import logging
import sys
from db.setup import initialise_database
from db.operations import get
import streamlit as st
import pandas as pd

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

def get_param(parameter: str, limit: int = 1):
    response = get(parameter, limit)
    if response and response["status"] == "success":
        return response["data"]
    else:
        logger.error(f"Failed to retrieve data for {parameter}: {response['message'] if response else 'No response'}")
        return None
    # Further processing can be done here

st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Welcome to My Streamlit App 🚀")

# Initialize database only once
if "db_initialized" not in st.session_state:
    logger.info("Starting application setup...")
    initialise_database()
    logger.info("Database setup complete.")
    st.session_state.db_initialized = True

# Create a Streamlit Chart of CPU Temperatures
st.header("CPU Temperature Dashboard")

@st.fragment(run_every=1)
def display_cpu_temperature():
    temperatures = get_param("cpu_temperature", limit=10)
    if temperatures:
        df = pd.DataFrame(temperatures)
        df = df.rename(columns={"logged_at": "Time", "temperature": "CPU Temperature"})
        st.line_chart(df, x="Time", y="CPU Temperature")
        logger.info("Displayed CPU temperature chart.")
    else:
        st.write("No CPU temperature data available.")
        logger.warning("No CPU temperature data to display.")

display_cpu_temperature()