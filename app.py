from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="sistema_eventos"
    )
    return conn

# Endpoint para listar eventos
@app.route('/eventos', methods=['GET'])
def listar_eventos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, data_inicio, data_fim, local FROM eventos")
    eventos = cursor.fetchall()
    cursor.close()
    conn.close()

    # Converte os dados para JSON
    eventos_json = [ 
        {"nome": row[0], "data_inicio": row[1], "data_fim": row[2], "local": row[3]}
        for row in eventos
    ]
    return jsonify(eventos_json)

if __name__ == '__main__':
    app.run(debug=True)

    from waitress import serve

if __name__ == "__main__":
    
    serve(app, host='127.0.0.1', port=5000)