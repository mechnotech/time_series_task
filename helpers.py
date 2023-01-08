import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from pyod.models.hbos import HBOS

from settings import config


def get_prepared_data() -> pd.DataFrame:
    df = pd.read_csv('data/task_data_middle.csv', low_memory=False, parse_dates=["date"])
    df['cnt'] = 1
    df.drop('id', axis=1, inplace=True)
    df = pd.DataFrame(df.groupby([df["date"], "inetnum"])["cnt"].sum())
    df = df.reset_index('inetnum')
    grouper = df.groupby([pd.Grouper(freq='1H'), 'inetnum'])
    df = grouper['cnt'].count().unstack('inetnum').fillna(0)
    top = df.loc[:, df.sum(axis=0) > 5000].copy()
    top = top.resample('1H').sum()
    return top


def scale_ip_data(data: pd.Series) -> pd.DataFrame:
    scaler = StandardScaler()
    np_scaled = scaler.fit_transform(data.values.reshape(-1, 1))
    return pd.DataFrame(np_scaled)


def isolation_forest(data: pd.DataFrame, coll: str, cont: float = 0.01) -> np.array:
    data = scale_ip_data(data[coll])
    model = IsolationForest(contamination=cont, random_state=config.random_state)
    model.fit(data)
    return model.predict(data)


def hist_detection(data: pd.DataFrame, coll: str, cont: float = 0.01) -> np.array:
    detector = HBOS(contamination=cont)
    data = scale_ip_data(data[coll])
    detector.fit(data)
    pred = detector.predict(data)
    return pred

