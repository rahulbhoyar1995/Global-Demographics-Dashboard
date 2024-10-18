import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Hello Dash"),
    dcc.Graph(figure={
        'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'example'}],
        'layout': {'title': 'Basic Example'}
    })
])

if __name__ == '__main__':
    app.run_server(debug=True)