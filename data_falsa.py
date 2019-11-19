import pandas as pd
from datetime import datetime, timedelta
import random
import pickle

n = 1000
data = []
ini_time_for_now = datetime.now()
for _ in range(n):
    temp = []
    fecha_futura = ini_time_for_now + timedelta(minutes=5)
    temp += [fecha_futura]
    ini_time_for_now = fecha_futura
    temp += [random.uniform(1000, 2000)]
    temp += [random.uniform(400, 900)]
    data.append(temp)

df = pd.DataFrame(data, columns=["FECHA", "INGRESOS", "GASTOS"])
df.to_pickle("data_falsa.pkl")

