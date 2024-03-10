import logging
import pandas as pd
from zenml.steps import step

@step
def train_model(df: pd.DataFrame) -> None:
    '''
    Trains the model on ingested data.
    
    Args:
    df: the ingested data
    
    '''
    pass