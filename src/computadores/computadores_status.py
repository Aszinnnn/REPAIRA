from utils import obter_data_atual
from .computadores_repo import buscar_computador_id, salvar_computadores
from .computadores_consulta import listar_computadores_resumido

def atualizar_status_computador(lista_computadores):
    if not lista_computadores:
        print("\nNenhum computador cadastrado ainda!")
        return lista_computadores
    listar_computadores_resumido(lista_computadores)
    try: id_busca = int(input("\nDigite o ID do computador: ").strip())
    except ValueError:
        print("ID inválido!"); return lista_computadores
    computador = buscar_computador_id(lista_computadores, id_busca)
    if not computador:
        print("Computador não encontrado!"); return lista_computadores
    print("1 - Operacional\n2 - Em Manutenção\n3 - Inativo")
    mapa = {"1": "Operacional", "2": "Em Manutenção", "3": "Inativo"}
    opcao = input("Novo status: ").strip()
    if opcao not in mapa:
        print("❌ Opção inválida!"); return lista_computadores
    computador["status"] = mapa[opcao]
    if computador["status"] == "Em Manutenção": computador["ultima_manutencao"] = obter_data_atual()
    salvar_computadores(lista_computadores)
    print("✅ Status atualizado!")
    return lista_computadores

def deletar_computador(lista_computadores):
    if not lista_computadores:
        print("\nNenhum computador cadastrado ainda!"); return lista_computadores
    listar_computadores_resumido(lista_computadores)
    try: id_busca = int(input("\nDigite o ID do computador a deletar: ").strip())
    except ValueError:
        print("ID inválido!"); return lista_computadores
    computador = buscar_computador_id(lista_computadores, id_busca)
    if not computador:
        print("Computador não encontrado!"); return lista_computadores
    if input("Digite SIM para confirmar: ").strip().upper() == "SIM":
        lista_computadores.remove(computador); salvar_computadores(lista_computadores); print("✅ Computador deletado!")
    else: print("Operação cancelada.")
    return lista_computadores
