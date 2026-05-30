def listar_ordens_abertas(lista_ordens, lista_computadores=None):
    """Lista todas as ordens com status Aberta ou Em Andamento."""
    if not lista_ordens:
        print("\nNenhuma ordem de serviço cadastrada!")
        return

    abertas = [ordem for ordem in lista_ordens if ordem["status"] in ["Aberta", "Em Andamento"]]

    if not abertas:
        print("\nNenhuma ordem aberta ou em andamento no momento.")
        return

    print("\n" + "=" * 130)
    print("📑 ORDENS DE SERVIÇO ABERTAS / EM ANDAMENTO")
    print("=" * 130)
    print(f"{'OS':<6} {'Computador':<22} {'Tipo':<12} {'Prioridade':<12} {'Funcionário':<22} {'Status':<16} {'SLA':<12}")
    print("-" * 130)

    for ordem in abertas:
        print(f"{ordem['id_os']:<6} {ordem['nome_computador']:<22} {ordem['tipo_manutencao']:<12} {ordem['prioridade']:<12} {ordem['nome_funcionario']:<22} {ordem['status']:<16} {ordem['sla_previsto']:<12}")

    print("=" * 130)


def listar_ordens_por_funcionario(lista_ordens, lista_funcionarios):
    """Lista as ordens agrupadas por funcionário, mostrando abertas, andamento e concluídas."""
    if not lista_ordens:
        print("\nNenhuma ordem cadastrada!")
        return

    if not lista_funcionarios:
        print("\nNenhum funcionário cadastrado!")
        return

    print("\n" + "=" * 80)
    print("📌 ORDENS POR FUNCIONÁRIO")
    print("=" * 80)

    for funcionario in lista_funcionarios:
        ordens_func = [os for os in lista_ordens if os.get("id_funcionario") == funcionario["id_funcionario"]]
        if not ordens_func:
            continue

        pendentes = [os for os in ordens_func if os["status"] in ["Aberta", "Em Andamento"]]
        concluidas = [os for os in ordens_func if os["status"] == "Concluída"]

        print(f"\nFuncionário: {funcionario['nome']} (ID {funcionario['id_funcionario']})")
        print(f"- Total de OS atribuídas: {len(ordens_func)}")
        print(f"- Pendentes: {len(pendentes)}")
        print(f"- Concluídas: {len(concluidas)}")
