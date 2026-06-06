from datetime import datetime, timedelta

def calcular_sla(prioridade):
    dias_por_prioridade = {"Crítica": 1, "Alta": 2, "Média": 5, "Baixa": 10}
    return (datetime.now() + timedelta(days=dias_por_prioridade.get(prioridade, 10))).strftime("%Y-%m-%d")

def verificar_sla_atraso(lista_ordens):
    if not lista_ordens:
        print("\nNenhuma ordem cadastrada!"); return
    hoje = datetime.now().date(); encontrou = False
    print("\n⏰ VERIFICAÇÃO DE SLA")
    for ordem in lista_ordens:
        if ordem.get("status") in ["Aberta", "Em Andamento"]:
            sla = datetime.strptime(ordem.get("sla_previsto"), "%Y-%m-%d").date(); dias = (sla - hoje).days
            if dias < 0: print(f"ATRASADA | OS {ordem.get('id_os')} | {abs(dias)} dia(s)"); encontrou=True
            elif dias <= 2: print(f"PRÓXIMA | OS {ordem.get('id_os')} | {dias} dia(s)"); encontrou=True
    if not encontrou: print("Nenhum alerta de SLA encontrado.")
