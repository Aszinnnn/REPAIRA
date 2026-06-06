from utils import carregar_dados, salvar_dados
ARQUIVO_ORDENS = "ordem_servico.json"
def carregar_ordens(): return carregar_dados(ARQUIVO_ORDENS)
def salvar_ordens(lista_ordens): return salvar_dados(lista_ordens, ARQUIVO_ORDENS)
def gerar_novo_id_os(lista_ordens): return 1 if not lista_ordens else max(ordem.get("id_os", 0) for ordem in lista_ordens) + 1
