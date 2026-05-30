from utils import obter_data_atual
from .ordens_repo import salvar_ordens


def atualizar_status_ordem(lista_ordens, lista_computadores=None):
    """Atualiza o status de uma ordem de serviço existente."""
    if not lista_ordens:
        print("\nNenhuma ordem de serviço cadastrada")
        return lista_ordens

    print("\n" + "=" * 60)
    print("🔄 ATUALIZAR STATUS DA ORDEM DE SERVIÇO")
    print("=" * 60)

    for ordem in lista_ordens:
        print(f"OS {ordem['id_os']} | {ordem['nome_computador']} | Status: {ordem['status']}")

    try:
        id_os = int(input("\nDigite o ID da OS que deseja atualizar: ").strip())
    except ValueError:
        print("❌ ID inválido!")
        return lista_ordens

    ordem_encontrada = None
    for ordem in lista_ordens:
        if ordem["id_os"] == id_os:
            ordem_encontrada = ordem
            break

    if not ordem_encontrada:
        print("❌ Ordem de serviço não encontrada!")
        return lista_ordens

    print("\nOpções de status:")
    print("1 - Aberta")
    print("2 - Em Andamento")
    print("3 - Concluída")

    opcao = input("Digite a nova opção de status: ").strip()

    if opcao == "1":
        ordem_encontrada["status"] = "Aberta"
    elif opcao == "2":
        ordem_encontrada["status"] = "Em Andamento"
    elif opcao == "3":
        ordem_encontrada["status"] = "Concluída"
        ordem_encontrada["data_conclusao"] = obter_data_atual()
        ordem_encontrada["solucao_aplicada"] = input("Digite a solução aplicada: ").strip()
    else:
        print("❌ Opção inválida!")
        return lista_ordens

    salvar_ordens(lista_ordens)
    print("\n✅ Status da ordem atualizado com sucesso!")
    return lista_ordens
