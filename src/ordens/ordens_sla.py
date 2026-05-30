from datetime import datetime, timedelta


def calcular_sla(prioridade):
    """Calcula a data prevista de SLA a partir da prioridade da ordem."""
    data_atual = datetime.now()

    if prioridade == "Crítica":
        dias = 1
    elif prioridade == "Alta":
        dias = 2
    elif prioridade == "Média":
        dias = 5
    else:
        dias = 10

    data_sla = data_atual + timedelta(days=dias)
    return data_sla.strftime("%Y-%m-%d")


def verificar_sla_atraso(lista_ordens):
    """Verifica e exibe ordens com SLA vencido ou próximo do vencimento."""
    if not lista_ordens:
        print("\n⚠️ Nenhuma ordem de serviço cadastrada!")
        return

    hoje = datetime.now().date()
    atrasadas = []
    proximas = []

    for ordem in lista_ordens:
        if ordem["status"] in ["Aberta", "Em Andamento"]:
            sla = datetime.strptime(ordem["sla_previsto"], "%Y-%m-%d").date()
            dias = (sla - hoje).days
            if dias < 0:
                atrasadas.append((ordem, abs(dias)))
            elif dias <= 2:
                proximas.append((ordem, dias))

    print("\n" + "=" * 60)
    print("⏰ VERIFICAÇÃO DE SLA")
    print("=" * 60)

    if atrasadas:
        print("\nORDENS ATRASADAS:")
        for ordem, dias in atrasadas:
            print(f"OS {ordem['id_os']} - {ordem['nome_computador']} - Atraso: {dias} dia(s)")
    else:
        print("\nNenhuma ordem atrasada.")

    if proximas:
        print("\nORDENS PRÓXIMAS DO VENCIMENTO:")
        for ordem, dias in proximas:
            print(f"OS {ordem['id_os']} - {ordem['nome_computador']} - Restam {dias} dia(s)")
    else:
        print("\nNenhuma ordem próxima do vencimento.")
