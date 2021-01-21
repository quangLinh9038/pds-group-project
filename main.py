import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv('data/data.csv')


fig1 = px.scatter(df, x="danceability", y="popularity",
                   color="explicit", size="energy",
                 log_x=True, size_max=60) 

fig2 = px.scatter(df, x="loudness", y="popularity",
                  color="explicit", size="energy",
                 log_x=True, size_max=60)  

app.layout = html.Div(
    dcc.Graph(
        id='danceability-and-popularity',
        figure=fig1
    )
)

if __name__ == '__main__':
    app.run_server(debug=False)