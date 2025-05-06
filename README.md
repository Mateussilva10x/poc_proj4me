# Batch S3 Excel MySQL Processor

Este projeto executa um processamento batch via linha de comando que:

1. Conecta-se a um banco de dados MySQL.
2. Executa uma consulta e gera um relatório `.xlsx`.
3. Conecta-se a um bucket S3 e baixa arquivos.
4. Organiza os arquivos localmente.

---

## ✅ Requisitos

* Python 3.10+
* AWS CLI configurado ou variáveis de ambiente para acesso S3

### Instalação de dependências

```bash
python -m venv venv
venv\Scripts\activate  # No Windows
pip install -r requirements.txt
```

---

## 🚀 Como Executar

```bash
python main.py \
  --db-host localhost \
  --db-port 3306 \
  --db-user root \
  --db-password 1234 \
  --db-name vendas \
  --s3-user admin@empresa.com \
  --s3-bucket relatorios2025 \
  --s3-prefix mensal/
```

---

## 📁 Estrutura do Projeto

```
project/
├── db/
│   └── mysql_client.py
├── excel/
│   └── report_generator.py
├── s3/
│   └── s3_client.py
├── fileops/
│   └── file_manager.py
├── output/
├── downloads/
├── arquivos_organizados/
├── main.py
├── requirements.txt
└── README.md
```

---

## 📦 Dependências

```
boto3
openpyxl
mysql-connector-python
```

---

## 🛠️ Configuração AWS

Configure as credenciais AWS com:

```bash
aws configure
```

ou defina variáveis de ambiente:

```bash
set AWS_ACCESS_KEY_ID=...
set AWS_SECRET_ACCESS_KEY=...
```
