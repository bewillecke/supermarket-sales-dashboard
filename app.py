# --------------- IMPORTS -------------------

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

import pandas as pd
import numpy as np

import plotly.express as px

# ---------------------- DATA ----------------------

# Carrega o dataset em um DataFrame e converte a coluna 'Date' para o tipo datetime
df_data = pd.read_csv("./dataset/supermarket_sales.csv")
df_data["Date"] = pd.to_datetime(df_data["Date"])

# ---------------------- APP -----------------------

# Inicializa a aplicação Dash e configura o tema externo do Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
server = app.server  # Configuração do servidor para deployment

# ---------------------- LAYOUT ----------------------

# Carrega o tema do layout dos gráficos como 'flatly'
load_figure_template('flatly')

# Define a estrutura do layout do aplicativo
app.layout = html.Div(children=[
    dbc.Row([

        # Coluna lateral com filtros e opções de análise
        dbc.Col([
            dbc.Card([
                html.H2('SUPERMARKET SALES DASHBOARD', style={'font-size': '30px'}),
                html.Hr(),

                # Filtro para selecionar as cidades
                html.H5('Cidades:'),
                dcc.Checklist(
                    df_data['City'].value_counts().index,  # valores das opções
                    df_data['City'].value_counts().index,  # valores iniciais selecionados
                    id='check_city',  # ID para uso no callback
                    inputStyle={'margin-right': '5px', 'margin-left': '20px'}
                ),

                # Opção para selecionar a variável de análise
                html.H5('Variável de análise:', style={'margin-top': '25px'}),
                dcc.RadioItems(
                    ['gross income', 'Rating'],  # opções para seleção
                    'gross income',  # valor inicial
                    id='main_variable',  # ID para uso no callback
                    inputStyle={'margin-right': '5px', 'margin-left': '20px'}
                )
            ], style={'height': '90vh', 'margin': '20px', 'padding': '20px'})
        ], sm=2),  # Define a largura da coluna

        # Coluna principal com gráficos
        dbc.Col([
            dbc.Row([
                # Gráficos menores em uma linha com 3 colunas
                dbc.Col([dcc.Graph(id='city_fig')], sm=4),
                dbc.Col([dcc.Graph(id='gender_fig')], sm=4),
                dbc.Col([dcc.Graph(id='pay_fig')], sm=4)
            ]),

            # Gráficos maiores em linhas únicas
            dbc.Row([dcc.Graph(id='income_per_date_fig')]),
            dbc.Row([dcc.Graph(id='income_per_product_fig')])
                 
        ], sm=10)  # Define a largura da coluna principal
    ])   
])

# ---------------------- CALLBACKS ----------------------

# Define o callback para atualizar todos os gráficos quando os filtros são alterados
@app.callback([
    Output('city_fig', 'figure'),
    Output('gender_fig', 'figure'),
    Output('pay_fig', 'figure'),
    Output('income_per_date_fig', 'figure'),
    Output('income_per_product_fig', 'figure')
], [
    Input('check_city', 'value'),
    Input('main_variable', 'value')
])
def render_graphs(cities, main_variable):
    # Define a operação de agregação com base na variável selecionada
    op = np.sum if main_variable == 'gross income' else np.mean
    
    # Filtra o DataFrame com base nas cidades selecionadas
    df_filtered = df_data[df_data['City'].isin(cities)]
    
    # Agrupamentos dos dados para cada gráfico
    df_city = df_filtered.groupby('City')[main_variable].apply(op).to_frame().reset_index()
    df_gender = df_filtered.groupby(['Gender', 'City'])[main_variable].apply(op).to_frame().reset_index()
    df_payment = df_filtered.groupby('Payment')[main_variable].apply(op).to_frame().reset_index()
    df_date_income = df_filtered.groupby('Date')[main_variable].apply(op).to_frame().reset_index()
    df_product_income = df_filtered.groupby(['Product line', 'City'])[main_variable].apply(op).to_frame().reset_index()

    # Criação dos gráficos com Plotly Express
    fig_city = px.bar(df_city, x='City', y=main_variable)
    fig_gender = px.bar(df_gender, x='Gender', y=main_variable, color='City', barmode='group')
    fig_payment = px.bar(df_payment, y='Payment', x=main_variable, orientation='h')
    fig_date_income = px.bar(df_date_income, x='Date', y=main_variable)
    fig_product_income = px.bar(df_product_income, x=main_variable, y='Product line', color='City', orientation='h', barmode='group')

    # Ajusta o layout dos gráficos menores
    for fig in [fig_city, fig_gender, fig_payment, fig_date_income]:
        fig.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=200, template='flatly')

    # Ajusta o layout do gráfico maior
    fig_product_income.update_layout(margin=dict(l=0, r=0, t=20, b=20), height=500)

    # Retorna todos os gráficos para os respectivos Outputs
    return fig_city, fig_gender, fig_payment, fig_date_income, fig_product_income
    
# ----------------- RUN APP -----------------

# Executa o servidor em localhost na porta 8050
if __name__ == '__main__':
    app.run_server(port=8050, debug=False)