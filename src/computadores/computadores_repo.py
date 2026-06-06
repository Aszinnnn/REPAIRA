from utils import carregar_dados, salvar_dados
ARQUIVO_COMPUTADORES = "computadores.json"
def carregar_computadores(): return carregar_dados(ARQUIVO_COMPUTADORES)
def salvar_computadores(lista_computadores): return salvar_dados(lista_computadores, ARQUIVO_COMPUTADORES)
def gerar_novo_id(lista_computadores): return 1 if not lista_computadores else max(comp.get("id", 0) for comp in lista_computadores) + 1
def buscar_computador_id(lista_computadores, id_computador):
    for computador in lista_computadores:
        if computador.get("id") == id_computador:
            return computador
    return None
