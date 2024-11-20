Projeto de Servidor Flask com Modelos de IA para Transição Energética
Este projeto disponibiliza uma API Flask que permite acessar três modelos de IA preditivos desenvolvidos para analisar o impacto da transição energética. Os modelos foram salvos em arquivos .pkl e são carregados pelo servidor Flask para fornecer previsões e classificações.

Estrutura do Projeto
server.py: O script principal que executa o servidor Flask e disponibiliza os modelos através de uma API simples.
modelo_regressao_co2.pkl: Arquivo contendo o modelo de Regressão Linear para prever as emissões de CO₂.
modelo_classificacao_progresso.pkl: Arquivo contendo o modelo de Classificação (Regressão Logística) para categorizar o progresso de um país em termos de eficiência energética.
modelo_clusterizacao_paises.pkl: Arquivo contendo o modelo de Clusterização (K-means) que agrupa os países em clusters de acordo com suas características econômicas e de consumo de energia.
Como Funciona
O servidor Flask possui três endpoints principais para cada um dos modelos. Cada endpoint aceita uma solicitação POST com dados em formato JSON e retorna uma previsão ou classificação.

Endpoints:


/prever_co2

Descrição: Utiliza o modelo de regressão para prever as emissões de CO₂ de um país.
Método HTTP: POST
Dados JSON:
primary_energy_consumption: (float) Consumo de energia primária do país.
population: (float) População do país.
gdp: (float) Produto Interno Bruto (PIB) do país.
Exemplo de solicitação:
json
Copiar código
{
  "primary_energy_consumption": 50000,
  "population": 1000000,
  "gdp": 50000000000
}
Resposta:
previsao_co2: (float) Valor previsto das emissões de CO₂.
json
Deve retornar algo como:

{
  "previsao_co2": 12345.67
}


/classificar_progresso

Descrição: Utiliza o modelo de classificação para categorizar o progresso de um país em eficiência energética.
Método HTTP: POST
Dados JSON:
primary_energy_consumption: (float) Consumo de energia primária do país.
population: (float) População do país.
gdp: (float) Produto Interno Bruto (PIB) do país.
Exemplo de solicitação:
json
Copiar código
{
  "primary_energy_consumption": 50000,
  "population": 1000000,
  "gdp": 50000000000
}
Resposta:
classe_progresso: (int) Classificação do progresso do país (0 = Baixo Progresso, 1 = Alto Progresso).
json
Deve retornar algo como:

{
  "classe_progresso": 1
}

/cluster_pais

Descrição: Utiliza o modelo de clusterização para identificar o cluster de um país.
Método HTTP: POST
Dados JSON:
primary_energy_consumption: (float) Consumo de energia primária do país.
population: (float) População do país.
gdp: (float) Produto Interno Bruto (PIB) do país.
Exemplo de solicitação:
json
Copiar código
{
  "primary_energy_consumption": 50000,
  "population": 1000000,
  "gdp": 50000000000
}
Resposta:
cluster: (int) Cluster ao qual o país pertence (0, 1 ou 2).
json
Deve retornar algo como:

{
  "cluster": 2
}
Como Executar o Servidor
Instale as dependências:

Execute o seguinte comando para instalar as bibliotecas necessárias:
bash
Copiar código
pip install -r requirements.txt
Inicie o servidor Flask:

Execute o seguinte comando para iniciar o servidor:
bash
Copiar código
python server.py
O servidor estará disponível em http://127.0.0.1:5000.

Como Testar a API
Você pode testar a API usando ferramentas como Postman ou enviando solicitações POST diretamente no terminal com o comando curl.

Exemplo de solicitação POST para o endpoint /prever_co2:

bash
Copiar código
curl -X POST http://127.0.0.1:5000/prever_co2 -H "Content-Type: application/json" -d '{"primary_energy_consumption": 50000, "population": 1000000, "gdp": 50000000000}'
Explicação dos Arquivos .pkl
Os arquivos .pkl contêm os modelos preditivos que foram treinados anteriormente e salvos usando a biblioteca joblib. Eles incluem:

modelo_regressao_co2.pkl: Modelo de Regressão Linear que prevê as emissões de CO₂.
modelo_classificacao_progresso.pkl: Modelo de Classificação que categoriza o progresso de um país em termos de eficiência energética.
modelo_clusterizacao_paises.pkl: Modelo de Clusterização que agrupa os países com base em características econômicas e de consumo de energia.
Esses arquivos são carregados pelo servidor Flask no início para que possam ser utilizados nos endpoints da API, permitindo que as previsões sejam realizadas em tempo real com dados fornecidos pelo usuário.