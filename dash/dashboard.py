import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly
import plotly.express as px

df = pd.read_csv("final_data.csv")

mark_values = {2000:'2000',2001:'2001',2002:'2002',2003:'2003',
               2004:'2004',2005:'2005',2006:'2006',2007:'2007',
               2008:'2008',2009:'2009',2010:'2010',2011:'2011',
               2012:'2012',2013:'2013',2014:'2014',2015:'2015',
               2016:'2016',2017:'2017',2018:'2018',2019:'2019',2020:'2020'}
mark_values1 = {2000:'2000',2001:'2001',2002:'2002',2003:'2003',
               2004:'2004',2005:'2005',2006:'2006',2007:'2007',
               2008:'2008',2009:'2009',2010:'2010',2011:'2011',
               2012:'2012',2013:'2013',2014:'2014',2015:'2015',
               2016:'2016',2017:'2017',2018:'2018',2019:'2019',2020:'2020'}

app = dash.Dash(__name__)

#---------------------------------------------------------------
app.layout = html.Div([
        html.Div([
            html.Pre(children= "Dashboard of Spotify feature",
            style={"text-align": "center", "font-size":"100%", "color":"black"})
        ]),

        html.Div([
            dcc.Graph(id='the_graph')
        ]),

        html.Div([
            dcc.RangeSlider(id='the_year',
                min=2000,
                max=2020,
                value=[2000,2020],
                marks=mark_values,
                step=None
                )
        ],style={"width": "70%", "position":"absolute",
                 "left":"5%"}),
html.Div([
            html.Pre(children= "",
            style={"text-align": "center", "font-size":"100%", "color":"black"})
        ]),

        html.Div([
            dcc.Graph(id='the_graph1')
        ]),

        html.Div([
            dcc.RangeSlider(id='the_year1',
                min=2000,
                max=2020,
                value=[2000,2020],
                marks=mark_values1,
                step=None
                )
        ],style={"width": "70%", "position":"absolute",
                 "left":"5%"})

])
#---------------------------------------------------------------
#call back danceability relation
@app.callback(
    Output('the_graph','figure'),
    [Input('the_year','value')]
)

def update_graph(years_chosen):

    dff=df[(df['year']>=years_chosen[0])&(df['year']<=years_chosen[1])]

    scatterplot = px.scatter(
        data_frame=dff,
        x="danceability",
        y="popularity",
        hover_data=['popularity'],
        title="Relationship between danceability and popularity",
        height=550
    )

    scatterplot.update_traces(textposition='top center')

    return (scatterplot)

#call back loudness relation
@app.callback(
    Output('the_graph1','figure'),
    [Input('the_year1','value')]
)

def update_graph1(years_chosen1):

    dff1=df[(df['year']>=years_chosen1[0])&(df['year']<=years_chosen1[1])]

    scatterplot1 = px.scatter(
        data_frame=dff1,
        x="loudness",
        y="popularity",
        hover_data=['popularity'],
        title="Relationship between loudness and popularity",
        height=550
    )

    scatterplot1.update_traces(textposition='top center')

    return (scatterplot1)

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=False, dev_tools_props_check=True)