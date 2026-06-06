def listar_computadores(lista_computadores):
    if not lista_computadores:
        print("\nNão há cadastro de computadores!")
        return
    print("\n" + "=" * 100)
    print("📋 INVENTÁRIO DE COMPUTADORES")
    print("=" * 100)
    print(f"{'ID':<5} {'Nome':<22} {'Modelo':<22} {'Status':<16} {'Localização':<22}")
    for comp in lista_computadores:
        print(f"{comp.get('id'):<5} {comp.get('nome',''):<22} {comp.get('modelo',''):<22} {comp.get('status',''):<16} {comp.get('localizacao',''):<22}")
    print(f"Total: {len(lista_computadores)}")

def listar_computadores_resumido(lista_computadores):
    if not lista_computadores:
        print("⚠️ Nenhum computador cadastrado!")
        return
    print(f"{'ID':<5} {'Nome':<25} {'Status':<15}")
    for comp in lista_computadores:
        print(f"{comp.get('id'):<5} {comp.get('nome',''):<25} {comp.get('status',''):<15}")

def exibir_detalhes_computador(computador):
    for chave, valor in computador.items(): print(f"{chave}: {valor}")
