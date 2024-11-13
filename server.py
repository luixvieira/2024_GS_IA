from flask import Flask, request, jsonify
import joblib
import numpy as np

#Para instalar as dependencias coloque no terminal o seguinte codigo:
#pip install -r requirements.txt

# Carregar os modelos
modelo_regressao = joblib.load('modelo_regressao_co2.pkl')
modelo_classificacao = joblib.load('modelo_classificacao_progresso.pkl')
modelo_clusterizacao = joblib.load('modelo_clusterizacao_paises.pkl')

# Inicializar o aplicativo Flask
app = Flask(__name__)

# Endpoint para o modelo de Regressão Linear (previsão de emissões de CO2)
@app.route('/prever_co2', methods=['POST'])
def prever_co2():
    dados = request.get_json()
    # Supondo que os dados incluam 'primary_energy_consumption', 'population', 'gdp'
    X = np.array([[dados['primary_energy_consumption'], dados['population'], dados['gdp']]])
    previsao = modelo_regressao.predict(X)[0]
    return jsonify({'previsao_co2': previsao})

# Endpoint para o modelo de Classificação (progresso em eficiência energética)
@app.route('/classificar_progresso', methods=['POST'])
def classificar_progresso():
    dados = request.get_json()
    X = np.array([[dados['primary_energy_consumption'], dados['population'], dados['gdp']]])
    classe = modelo_classificacao.predict(X)[0]
    return jsonify({'classe_progresso': int(classe)})

# Endpoint para o modelo de Clusterização (identificar o cluster de um país)
@app.route('/cluster_pais', methods=['POST'])
def cluster_pais():
    dados = request.get_json()
    X = np.array([[dados['primary_energy_consumption'], dados['population'], dados['gdp']]])
    cluster = modelo_clusterizacao.predict(X)[0]
    return jsonify({'cluster': int(cluster)})

# Executar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
