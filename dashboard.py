# TODO : - This is my final step create an interactive dashboard to present your findings #DONE
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px


def create_dashboard(df):
    # Load dataset

    # Initialize the Dash app
    app = dash.Dash(__name__)

    # Define the layout of the dashboard
    app.layout = html.Div([
        html.H1("Student Performance Dashboard"),

        # Dropdown for selecting x and y variables
        html.Label("Select X and Y Variables:"),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': col, 'value': col} for col in df.select_dtypes(include=['float64', 'int64']).columns
            ],
            multi=True,
            value=['AGE', 'SCORE'],  # Default selected variables
        ),

        # Scatter plot for selected variables
        dcc.Graph(id='scatter-plot'),
    ])

    # Define callback to update scatter plot based on dropdown selection
    @app.callback(
        Output('scatter-plot', 'figure'),
        [Input('dropdown', 'value')]
    )
    def update_scatter_plot(selected_vars):
        fig = px.scatter(df, x=selected_vars[0], y=selected_vars[1], hover_data=['NAME'], title='Scatter Plot')
        return fig

    # Run the app
    app.run_server(debug=True)


