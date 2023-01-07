import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.seasonal import seasonal_decompose


def get_prepared_data() -> pd.DataFrame:
    df = pd.read_csv('data/task_data_middle.csv', low_memory=False, parse_dates=["date"])
    df['cnt'] = 1
    df.drop('id', axis=1, inplace=True)
    df = pd.DataFrame(df.groupby([df["date"], "inetnum"])["cnt"].sum())
    df = df.reset_index('inetnum')
    grouper = df.groupby([pd.Grouper(freq='1H'), 'inetnum'])
    df = grouper['cnt'].count().unstack('inetnum').fillna(0)
    return df.resample('1H').sum()


def scale_ip_data(data: pd.Series) -> pd.DataFrame:
    scaler = StandardScaler()
    np_scaled = scaler.fit_transform(data.values.reshape(-1,1))
    return pd.DataFrame(np_scaled)


def isolation_forest(data: pd.DataFrame, coll: str, cont: float = 0.05) -> np.array:
    data = scale_ip_data(data[coll])
    model = IsolationForest(contamination=cont)
    model.fit(data)
    return model.predict(data)

def create_iso_forest_chart(data: pd.DataFrame, coll: str, cont_factor: float = 0.05):
    result = isolation_forest(data=data, coll=coll, cont=cont_factor)
    data['anomaly'] = result
    return data
