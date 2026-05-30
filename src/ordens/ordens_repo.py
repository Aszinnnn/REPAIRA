from utils import carregar_dados, salvar_dados

# Nome do arquivo JSON onde as ordens de serviço serão salvas.
ARQUIVO_ORDENS = "ordem_servico.json"


def carregar_ordens():
    """Carrega as ordens de serviço do arquivo JSON."""
    return carregar_dados(ARQUIVO_ORDENS)


def salvar_ordens(lista_ordens):
    """Salva as ordens de serviço no arquivo JSON."""
    return salvar_dados(lista_ordens, ARQUIVO_ORDENS)


def gerar_novo_id_os(lista_ordens):
    """Gera um novo ID sequencial para uma ordem de serviço."""
    if not lista_ordens:
        return 1
    ids = [ordem["id_os"] for ordem in lista_ordens]
    return max(ids) + 1
