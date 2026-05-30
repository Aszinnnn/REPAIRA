from datetime import datetime
from computadores import buscar_computador_id


def exibir_historico_completo(lista_ordens):
    """Exibe o histórico completo de ordens concluídas."""
    if not lista_ordens:
        print("\nNão há ordens de serviço registradas!")
        return

    concluidas = [os for os in lista_ordens if os["status"] == "Concluída"]
    if not concluidas:
        print("\nNenhuma ordem concluída ainda!")
        return

    print("\n" + "=" * 100)
    print("📜 HISTÓRICO DE MANUTENÇÕES")
    print("=" * 100)
    print(f"{'OS':<6} {'Computador':<25} {'Tipo':<12} {'Data Conclusão':<20}")
    print("-" * 100)

    for os in concluidas:
        data = os['data_conclusao'][:19] if os['data_conclusao'] else '---'
        print(f"{os['id_os']:<6} {os['nome_computador']:<25} {os['tipo_manutencao']:<12} {data:<20}")

    print("=" * 100)
    print(f"Total: {len(concluidas)} manutenções realizadas")


def exibir_historico_por_computador(lista_ordens, lista_computadores):
    """Exibe o histórico de ordens de um computador específico."""
    if not lista_computadores or not lista_ordens:
        print("\nDados insuficientes!")
        return

    print("\n" + "=" * 100)
    print("HISTÓRICO DE MANUTENÇÕES POR COMPUTADOR")

    for comp in lista_computadores:
        print(f"ID: {comp['id']} - {comp['nome']}")

    try:
        id_comp = int(input("\nDigite o ID do computador: "))
    except ValueError:
        print("❌ ID inválido!")
        return

    comp = buscar_computador_id(lista_computadores, id_comp)
    if not comp:
        print(f"Computador com ID {id_comp} não encontrado!")
        return

    ordens_comp = [os for os in lista_ordens if os["id_computador"] == id_comp]
    if not ordens_comp:
        print(f"\nNenhuma ordem para {comp['nome']}")
        return

    print(f"\n💻 HISTÓRICO: {comp['nome']}")
    print("-" * 60)

    for os in ordens_comp:
        numero_os = os['id_os']
        tipo = os['tipo_manutencao']
        status = os['status']
        data_mostrar = os['data_conclusao'][:10] if os['data_conclusao'] else os['data_abertura'][:10]
        print(f"OS {numero_os} | {tipo} | {status} | {data_mostrar}")
        if status == "Concluída" and os['solucao_aplicada']:
            print(f"Solução: {os['solucao_aplicada']}")


def exibir_estatisticas(lista_ordens, lista_computadores):
    """Exibe estatísticas gerais do sistema."""
    if not lista_ordens:
        print("\nNenhuma ordem cadastrada!")
        return

    total = len(lista_ordens)
    abertas = len([os for os in lista_ordens if os["status"] in ["Aberta", "Em Andamento"]])
    concluidas = len([os for os in lista_ordens if os["status"] == "Concluída"])

    print("\n" + "=" * 50)
    print("ESTATÍSTICAS")
    print("=" * 50)
    print(f"Total de OS: {total}")
    print(f"Abertas: {abertas}")
    print(f"Concluídas: {concluidas}")

    print("\nPor tipo:")
    tipos = ["Hardware", "Software", "Rede", "Limpeza"]
    for tipo in tipos:
        qtd = len([os for os in lista_ordens if os["tipo_manutencao"] == tipo])
        if qtd > 0:
            print(f"{tipo}: {qtd}")

    print("\nPor prioridade:")
    prioridades = ["Crítica", "Alta", "Média", "Baixa"]
    for prioridade in prioridades:
        qtd = len([os for os in lista_ordens if os["prioridade"] == prioridade])
        if qtd > 0:
            print(f"{prioridade}: {qtd}")

    print("=" * 50)


def exibir_sla_alerta(lista_ordens):
    """Exibe alertas de SLA atrasado ou próximo do vencimento."""
    if not lista_ordens:
        print("\nNenhuma ordem cadastrada!")
        return

    hoje = datetime.now().date()
    atrasadas = []
    proximas = []

    for os_item in lista_ordens:
        if os_item["status"] in ["Aberta", "Em Andamento"]:
            sla = datetime.strptime(os_item["sla_previsto"], "%Y-%m-%d").date()
            dias = (sla - hoje).days
            if dias < 0:
                atrasadas.append((os_item, abs(dias)))
            elif dias <= 2:
                proximas.append((os_item, dias))

    print("\n" + "=" * 50)
    print("ALERTAS DE SLA")
    print("=" * 50)

    if atrasadas:
        print("\nATRASADAS:")
        for os_item, dias in atrasadas:
            print(f"OS {os_item['id_os']} - {os_item['nome_computador']} - Atraso: {dias} dias")
    else:
        print("\nNenhuma atrasada")

    if proximas:
        print("\nPRÓXIMAS DO VENCIMENTO:")
        for os_item, dias in proximas:
            print(f"OS {os_item['id_os']} - {os_item['nome_computador']} - {dias} dias restantes")
    else:
        print("Nenhuma próxima do vencimento")

    print("=" * 50)
