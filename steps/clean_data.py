import logging
import pandas as pd
from zenml.steps import step

@step
def clean_data(df: pd.DataFrame)-> pd.DataFrame:
    pass