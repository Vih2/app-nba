from flask import Flask, jsonify

app = Flask(__name__)

# Dados fictícios dos resultados dos jogos da NBA
resultados_nba = [
    {"data": "2024-04-26", "time_casa": "Los Angeles Lakers", "pontos_casa": 110, "time_visitante": "Golden State Warriors", "pontos_visitante": 105},
    {"data": "2024-04-25", "time_casa": "Brooklyn Nets", "pontos_casa": 115, "time_visitante": "Milwaukee Bucks", "pontos_visitante": 120},
    {"data": "2024-04-24", "time_casa": "Los Angeles Clippers", "pontos_casa": 98, "time_visitante": "Phoenix Suns", "pontos_visitante": 102}
]

@app.route('/v1/resultados_nba', methods=['GET'])
def get_resultados_nba():
    return jsonify(resultados_nba)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')