import os
import pandas as pd
from src.config import RAW_PATH

def load_csv(filename: str) -> pd.DataFrame:
    path = os.path.join(RAW_PATH, filename)
    return pd.read_csv(path)
