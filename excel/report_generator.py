from openpyxl import Workbook # type: ignore
import os

def generate_excel_report(data, output_path="output/report.xlsx", mock=False):
    if mock:
        print(f"[MOCK] Gerando relatório Excel em: {output_path}")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        wb = Workbook()
        ws = wb.active
        ws.title = "Relatório Simulado"
        ws.append(["ID", "Nome", "Valor"])
        ws.append([1, "Produto A", 100.0])
        ws.append([2, "Produto B", 200.0])
        ws.append([3, "Produto C", 300.0])
        wb.save(output_path)
        print(f"[MOCK] Relatório salvo em: {output_path}")
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = "Relatório"

    # Cabeçalho
    if data:
        ws.append(list(data[0].keys()))
        for row in data:
            ws.append(list(row.values()))
    else:
        ws.append(["Sem dados"])

    wb.save(output_path)
    print(f"[OK] Relatório Excel gerado em: {output_path}")
