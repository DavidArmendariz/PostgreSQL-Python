from sqlalchemy import create_engine
import pandas as pd

df = pd.read_pickle("data_falsa.pkl")
engine = create_engine('postgresql://zwippe:625632@localhost:5432/kpidb')