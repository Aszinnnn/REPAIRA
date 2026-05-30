from utils import obter_data_atual
from .computadores_repo import buscar_computador_id, salvar_computadores
from .computadores_consulta import listar_computadores_resumido


def atualizar_status_computador(lista_computadores):
    """Atualiza o status de um computador específico."""
    if not lista_computadores:
        print("\nNenhum computador cadastrado ainda!")
        return lista_computadores

    print("\n" + "=" * 50)
    print("🔄 ATUALIZAR STATUS DO COMPUTADOR")
    print("=" * 50)

    listar_computadores_resumido(lista_computadores)

    try:
        id_busca = int(input("\nDigite o ID do computador que deseja atualizar o status: ").strip())
    except ValueError:
        print("ID inválido! Por favor, digite um número inteiro.")
        return lista_computadores

    computador = buscar_computador_id(lista_computadores, id_busca)
    if not computador:
        print(f"Computador com ID {id_busca} não encontrado!")
        return lista_computadores

    print(f"\nComputador selecionado: {computador['nome']} (ID: {computador['id']})")
    print("Status atual:", computador['status'])
    print("\nOpções de status:")
    print("1 - Operacional")
    print("2 - Em Manutenção")
    print("3 - Inativo")

    opcao = input("Digite o número correspondente ao novo status: ").strip()

    if opcao == "1":
        novo_status = "Operacional"
    elif opcao == "2":
        novo_status = "Em Manutenção"
    elif opcao == "3":
        novo_status = "Inativo"
    else:
        print("❌ Opção inválida!")
        return lista_computadores

    computador["status"] = novo_status

    if novo_status == "Em Manutenção":
        computador["ultima_manutencao"] = obter_data_atual()

    salvar_computadores(lista_computadores)
    print(f"\nStatus do computador '{computador['nome']}' atualizado para '{novo_status}' com sucesso!")
    return lista_computadores


def deletar_computador(lista_computadores):
    """Remove um computador do sistema."""
    if not lista_computadores:
        print("\nNenhum computador cadastrado ainda!")
        return lista_computadores

    print("\n" + "=" * 50)
    print("DELETAR COMPUTADOR")
    print("=" * 50)
    print("\nCOMPUTADORES CADASTRADOS:")
    print("-" * 50)

    for comp in lista_computadores:
        print(f"ID: {comp['id']} | Nome: {comp['nome']} | Status: {comp['status']}")

    print("-" * 50)

    try:
        id_busca = int(input("\nDigite o ID do computador a deletar: "))
    except ValueError:
        print("ID inválido!")
        return lista_computadores

    computador = buscar_computador_id(lista_computadores, id_busca)
    if not computador:
        print(f"Computador com ID {id_busca} não encontrado!")
        return lista_computadores

    print(f"\nATENÇÃO: Você está prestes a deletar:")
    print(f"ID: {computador['id']}")
    print(f"Nome: {computador['nome']}")
    print(f"Localização: {computador['localizacao']}")

    confirmacao = input("\nTem certeza? Digite 'SIM' para confirmar: ").strip().upper()

    if confirmacao == "SIM":
        lista_computadores.remove(computador)
        salvar_computadores(lista_computadores)
        print(f"\n✅ Computador {computador['nome']} deletado com sucesso!")
    else:
        print("\n❌ Operação cancelada!")

    return lista_computadores
