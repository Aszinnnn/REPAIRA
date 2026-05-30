from utils import carregar_dados, salvar_dados

# Constante com o nome do arquivo de computadores.
ARQUIVO_COMPUTADORES = "computadores.json"


def carregar_computadores():
    """Carrega a lista de computadores do JSON."""
    return carregar_dados(ARQUIVO_COMPUTADORES)


def salvar_computadores(lista_computadores):
    """Salva a lista de computadores no JSON."""
    return salvar_dados(lista_computadores, ARQUIVO_COMPUTADORES)


def gerar_novo_id(lista_computadores):
    """Gera um novo ID sequencial para o próximo computador."""
    if not lista_computadores:
        return 1
    ids = [computador["id"] for computador in lista_computadores]
    return max(ids) + 1


def buscar_computador_id(lista_computadores, id_computador):
    """Procura um computador pelo ID e retorna o dicionário encontrado."""
    for computador in lista_computadores:
        if computador["id"] == id_computador:
            return computador
    return None
