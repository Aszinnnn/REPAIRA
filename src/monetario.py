from collections import defaultdict
from funcionarios import buscar_funcionario_id


def recalcular_custo_ordem(ordem, lista_funcionarios):
    """Recalcula o custo de uma ordem com base no funcionário e nas horas gastas."""
    funcionario = buscar_funcionario_id(lista_funcionarios, ordem.get("id_funcionario"))
    if not funcionario:
        return 0.0
    horas = ordem.get("tempo_total_horas", 0)
    return round(funcionario.get("salario_por_hora", 0) * horas, 2)


def exibir_custo_por_os(lista_ordens, lista_funcionarios):
    """Exibe o custo monetário de cada ordem de serviço."""
<<<<<<< HEAD

=======
>>>>>>> 5f4d35c (Atualização OS e de funcionarios)
    if not lista_ordens:
        print("\nNenhuma ordem cadastrada!")
        return

    print("\n" + "=" * 120)
    print("💰 CONSULTA MONETÁRIA POR ORDEM DE SERVIÇO")
    print("=" * 120)

    for ordem in lista_ordens:
        custo = recalcular_custo_ordem(ordem, lista_funcionarios)
        print(
            f"OS [{ordem.get('id_os')}] - "
            f"FUNCIONÁRIO [{ordem.get('nome_funcionario')}] "
            f"FUNCIONARIO_ID [{ordem.get('id_funcionario')}] - "
            f"CUSTO R$ {custo:.2f}"
        )


def exibir_total_mensal_por_funcionario(lista_ordens, lista_funcionarios):
    """Exibe o total mensal gasto por funcionário, agrupando por mês/ano."""
<<<<<<< HEAD

=======
>>>>>>> 5f4d35c (Atualização OS e de funcionarios)
    if not lista_ordens:
        print("\nNenhuma ordem cadastrada!")
        return

    totais = defaultdict(float)

    for ordem in lista_ordens:
        data_base = ordem.get("data_conclusao") or ordem.get("data_inicio_manutencao") or ordem.get("data_abertura")
        ano_mes = data_base[:7]
        chave = (ordem.get("id_funcionario"), ordem.get("nome_funcionario"), ano_mes)
        totais[chave] += recalcular_custo_ordem(ordem, lista_funcionarios)

    print("\n" + "=" * 120)
    print("📅 TOTAL MENSAL POR FUNCIONÁRIO")
    print("=" * 120)

    for (id_func, nome_func, ano_mes), valor in sorted(totais.items(), key=lambda item: (item[0][2], item[0][1])):
        print(f"Funcionário {nome_func} - {ano_mes} - Total em OS: R$ {valor:.2f}")


def exibir_ranking_custos(lista_ordens, lista_funcionarios):
    """Exibe um ranking simples de custo acumulado por funcionário."""
<<<<<<< HEAD

=======
>>>>>>> 5f4d35c (Atualização OS e de funcionarios)
    if not lista_ordens:
        print("\nNenhuma ordem cadastrada!")
        return

    ranking = defaultdict(float)

    for ordem in lista_ordens:
        chave = (ordem.get("id_funcionario"), ordem.get("nome_funcionario"))
        ranking[chave] += recalcular_custo_ordem(ordem, lista_funcionarios)

    ranking_ordenado = sorted(ranking.items(), key=lambda item: item[1], reverse=True)

    print("\n" + "=" * 90)
    print("🏆 RANKING DE CUSTO POR FUNCIONÁRIO")
    print("=" * 90)

    for posicao, ((id_func, nome_func), valor) in enumerate(ranking_ordenado, start=1):
        print(f"{posicao}º {nome_func} (ID {id_func}) - R$ {valor:.2f}")


def menu_consulta_monetaria(lista_ordens, lista_funcionarios):
    """Menu principal da área monetária. A autenticação é feita no main.py."""
    while True:
        print("\n" + "=" * 60)
        print("💵 CONSULTA MONETÁRIA")
        print("=" * 60)
        print("[1] Custo por OS")
        print("[2] Total mensal por funcionário")
        print("[3] Ranking de custo")
        print("[0] Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_custo_por_os(lista_ordens, lista_funcionarios)
        elif opcao == "2":
            exibir_total_mensal_por_funcionario(lista_ordens, lista_funcionarios)
        elif opcao == "3":
            exibir_ranking_custos(lista_ordens, lista_funcionarios)
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")
