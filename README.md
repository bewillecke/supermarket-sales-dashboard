# Supermarket Sales Dashboard

Este projeto é um dashboard interativo desenvolvido com Python e Dash para visualização e análise de dados de vendas de um supermercado fictício. A interface permite explorar informações como receita bruta e avaliações, filtradas por cidade, gênero e método de pagamento.

## Tecnologias Utilizadas

- **Python 3.7+**
- **Dash** (com Dash Bootstrap Components para estilização)
- **Plotly** para gráficos interativos
- **Pandas** e **NumPy** para manipulação de dados

## Estrutura do Projeto

- `app.py`: Código principal do dashboard, configurado para criar e renderizar gráficos com base nos dados de vendas.
- `dataset/supermarket_sales.csv`: Dataset público utilizado para análise, que deve estar localizado na pasta `dataset`.
- `requirements.txt`: Bibliotecas necessárias para rodar o projeto.

## Instruções de Instalação e Execução

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/bewillecke/supermarket-sales-dashboard.git
    ```
2. **Instale as dependências**:
    Acesse o diretório do projeto e instale as bibliotecas necessárias:
    ```bash
    pip install -r requirements.txt
    ```
3. **Estrutura de Pastas**:
    Certifique-se de que o dataset (`supermarket_sales.csv`) esteja na seguinte estrutura:
    ```
    supermarket-sales-dashboard/
    ├── app.py
    └── dataset/
        └── supermarket_sales.csv
    ```
4. **Execute o aplicativo**:
    No diretório raiz do projeto, execute o comando:
    ```bash
    python app.py
    ```
5. **Acesse o dashboard**:
    Abra o navegador e acesse o endereço [http://localhost:8050](http://localhost:8050) para visualizar o dashboard.

## Observações

- **Porta**: O servidor está configurado para rodar na porta `8050`. Para modificar a porta, altere o valor no arquivo `app.py`.
- **Modo Debug**: Por segurança, o modo debug está desativado para esta versão. Para ativá-lo, altere a linha `debug=False` para `debug=True` em `app.py`.

---

Este projeto foi desenvolvido como parte de um estudo de análise de dados, visualização de dados e construção de webapps utilizando o Dash e pode ser adaptado para outras finalidades.
