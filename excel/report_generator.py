# excel/report_generator.py

import openpyxl
from openpyxl.styles import Font
from datetime import datetime
import os

def generate_excel_report(data, output_path, mock=False): 
    if mock: 
        print(f"[MOCK] Gerando relatório Excel simulado em {output_path}") 
        return
    """
    Gera um arquivo .xlsx com base nos dados do banco.
    Cada dicionário na lista representa uma linha, com chaves como cabeçalhos.
    """
    if not data:
        print("[WARN] Nenhum dado para gerar o relatorio.")
        return

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Relatorio"

    # Cabeçalhos a partir das chaves do primeiro registro
    headers = list(data[0].keys())
    ws.append(headers)

    # Negrito nos cabeçalhos
    for col in range(1, len(headers) + 1):
        ws.cell(row=1, column=col).font = Font(bold=True)

    # Linhas de dados
    for row in data:
        ws.append(list(row.values()))

    # Ajusta colunas para largura automática (simples)
    for col in ws.columns:
        max_length = max(len(str(cell.value)) if cell.value else 0 for cell in col)
        ws.column_dimensions[col[0].column_letter].width = max_length + 2

    # Cria diretório de saida se não existir
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Salva
    wb.save(output_path)
    print(f"[OK] Relatorio gerado: {output_path}")