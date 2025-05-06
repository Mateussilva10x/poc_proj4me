import mysql.connector
from mysql.connector import Error

def get_data(host, port, user, password, database, mock=False):
    if mock:
        print(f"[MOCK] Conectando a {user}@{host}:{port}/{database}")
        return [
            {"id": 1, "nome": "Produto A", "valor": 100},
            {"id": 2, "nome": "Produto B", "valor": 200}
        ]
    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        if conn.is_connected():
            print("[OK] Conectado ao banco de dados.")
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT NOW() as data_hora_atual;")
            resultado = cursor.fetchall()
            return resultado

    except Error as e:
        print(f"[ERRO] Falha na conexão: {e}")
        return []

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("[OK] Conexão encerrada.")