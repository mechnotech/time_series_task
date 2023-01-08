from settings import config

import dash
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output

from app_layouts.layouts import make_layout
from helpers import isolation_forest, get_prepared_data, hist_detection

app = dash.Dash(__name__)



