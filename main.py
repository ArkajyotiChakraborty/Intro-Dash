import pandas as pd
import dash

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px

df = pd.read_excel("Month_data.xlsx")
df3 = pd.read_excel("Dash_Data.xlsx")
df2 = pd.DataFrame({
    "Activity": ["Walking", "Sleeping", "Sitting", "Eating"],
    "Amount": [2, 7, 8, 3]
})
df4 = pd.DataFrame({
    "Activity": ["Walking", "Sleeping","Sitting","Eating","Miscelle"],
    "Amount": [9,48,40,1,2]
})
fig = px.line(df3, x='Week', y='Hours')
fig1 = px.line(df3, x='Month', y='Hours')
fig2 = px.bar(df2, x="Activity", y="Amount")
fig4 = px.pie(df4, values='Amount', names='Activity')
value1 = ''
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
app = dash.Dash(__name__)

activity = df3['ActivityName'].unique()
app.layout = html.Div([
    html.Div([html.H1(children='Activity Log')

              ], style={'text-align': 'center'}),

    html.H3(children='''
         Average Sitting Time: 7 to 10 hours
    '''),
    html.H3(children='''
         Average Walking Time: 1 to 2 hours'''),
    html.H3(children='''
     Average Sleeping Time: 7 to 8 hours'''),
    html.Div([dcc.Dropdown(
        id='activity-select',
        options=[{'label': i, 'value': i} for i in activity],
        value='Fertility rate, total (births per woman)'
    ),
    ], style={'width': '49%'}),
    html.Div([dcc.Dropdown(
        id='week-select',
        options=[{'label': i, 'value': i} for i in months],
        value='Fertility rate, total (births per woman)'
    )], style={'width': '49%'}),
    html.Div([dcc.Graph(
        id="time-series-chart",
        figure=fig
    )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20', 'background': 'grey'}),
    html.Div([dcc.Graph(
        id="example-graph",
        figure=fig1
    )], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20', 'background': 'grey'}),
    html.Div([
        dcc.Graph(
            id="bar-graph",
            figure=fig2
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20', 'background': 'grey'}),
    html.Div([
        dcc.Graph(
            id = "pie-graph",
            figure =fig4
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20', 'background': 'grey'})
], style={'background': '#ececec'})


@app.callback(
    Output('example-graph', 'figure'),
    Input('activity-select', 'value')
)
def update_output(value):
    global value1
    value1 = value
    return px.line(df[df['ActivityName'] == value], x='Month', y='Hours')


@app.callback(
    Output('time-series-chart', 'figure'),
    Input('week-select', 'value')
)
def update_output1(value):
    global value1
    return px.line(df3[df3['ActivityName'] == value1][df3['Month'] == value], x='Week', y='Hours')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
