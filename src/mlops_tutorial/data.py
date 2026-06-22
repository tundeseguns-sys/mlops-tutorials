# import library
import pandas as pd

from mlops_tutorial.config import RAW_DATA_FILE

def load_data():
    """
    load raw data set
    """
    df = pd.read_csv(RAW_DATA_FILE)
    
    return df

if __name__ == "__main__":
    data = load_data()
    
    print(data.head)