import logging
import pandas as pd

logger = logging.getLogger(__name__)

def load_netflix(filepath):
    """Load the Netflix CSV file."""
    df = pd.read_csv(filepath)
    logger.info("Data loaded: %s rows and %s columns", df.shape[0], df.shape[1])
    return df
