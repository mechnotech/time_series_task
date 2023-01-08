import numpy as np
from dash import Dash

from settings import config

app = Dash(__name__)
np.random.seed(config.random_state)
