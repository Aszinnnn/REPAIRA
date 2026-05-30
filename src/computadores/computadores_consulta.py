def listar_computadores(lista_computadores):
    """Lista todos os computadores cadastrados de forma tabular."""
    if not lista_computadores:
        print("\nNão há cadastro de computadores!")
        return

    print("\n" + "=" * 100)
    print("📋 INVENTÁRIO DE COMPUTADORES")
    print("=" * 100)
    print(f"{'ID':<5} {'Nome':<25} {'Modelo':<20} {'Status':<15} {'Localização':<20}")
    print("-" * 100)

    for comp in lista_computadores:
        print(f"{comp['id']:<5} {comp['nome']:<25} {comp['modelo']:<20} {comp['status']:<15} {comp['localizacao']:<20}")

    print("=" * 100)
    print(f"Total de computadores cadastrados: {len(lista_computadores)}")


def listar_computadores_resumido(lista_computadores):
    """Lista os computadores mostrando apenas ID, nome e status."""
    if not lista_computadores:
        print("⚠️ Nenhum computador cadastrado!")
        return

    print("\n" + "-" * 60)
    print(f"{'ID':<5} {'Nome':<25} {'Status':<15}")
    print("-" * 60)

    for comp in lista_computadores:
        print(f"{comp['id']:<5} {comp['nome']:<25} {comp['status']:<15}")

    print("-" * 60)


def exibir_detalhes_computador(computador):
    """Exibe todos os detalhes de um computador específico."""
    print("\n" + "=" * 60)
    print(f"💻 DETALHES DO COMPUTADOR - ID: {computador['id']}")
    print("=" * 60)
    print(f"Nome: {computador['nome']}")
    print(f"Tipo: {computador['tipo']}")
    print(f"Modelo: {computador['modelo']}")
    print(f"Processador: {computador['processador']}")
    print(f"Memória RAM: {computador['memoria_ram']}")
    print(f"Armazenamento: {computador['armazenamento']}")
    print(f"Sistema Operacional: {computador['sistema_operacional']}")
    print(f"Localização: {computador['localizacao']}")
    print(f"Departamento: {computador['departamento']}")
    print(f"Status: {computador['status']}")
    print(f"Data Cadastro: {computador['data_cadastro']}")
    print(f"Última Manutenção: {computador['ultima_manutencao'] or 'Nenhuma'}")
    print("=" * 60)
