import json
import os
import unicodedata
from datetime import datetime

# Diretório onde este arquivo utils.py está localizado.
# Isso garante que o sistema encontre a pasta dados mesmo se for executado
# de outra pasta, por exemplo: python src/main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Pasta fixa de dados dentro de src/dados.
DADOS_DIR = os.path.join(BASE_DIR, "dados")


def criar_pasta_dados():
    """Cria a pasta dados dentro de src caso ela ainda não exista."""
    if not os.path.exists(DADOS_DIR):
        os.makedirs(DADOS_DIR)
        print("📁 Pasta 'dados' criada com sucesso!")


def obter_caminho_dados(nome_arquivo):
    """Monta o caminho absoluto de um arquivo dentro da pasta dados."""
    criar_pasta_dados()
    return os.path.join(DADOS_DIR, nome_arquivo)


def carregar_dados(nome_arquivo):
    """Carrega um arquivo JSON da pasta src/dados e retorna uma lista."""
    caminho = obter_caminho_dados(nome_arquivo)

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado. Retornando lista vazia.")
        return []
    except json.JSONDecodeError:
        print(f"Arquivo {nome_arquivo} vazio ou corrompido. Retornando lista vazia.")
        return []


def salvar_dados(dados, nome_arquivo):
    """Salva dados em JSON dentro da pasta src/dados."""
    caminho = obter_caminho_dados(nome_arquivo)

    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print(f"✅ Dados salvos em {nome_arquivo}")
        return True
    except Exception as erro:
        print(f"❌ Erro ao salvar {nome_arquivo}: {erro}")
        return False


def obter_data_atual():
    """Retorna data e hora atual no padrão do projeto."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def converter_texto_para_data(texto_data):
    """Converte texto AAAA-MM-DD HH:MM:SS para datetime."""
    return datetime.strptime(texto_data, "%Y-%m-%d %H:%M:%S")


def calcular_diferenca_horas(data_inicio, data_fim):
    """Calcula diferença em horas entre duas datas em texto."""
    inicio = converter_texto_para_data(data_inicio)
    fim = converter_texto_para_data(data_fim)
    horas = (fim - inicio).total_seconds() / 3600
    return round(max(horas, 0), 2)


def remover_acentos(texto):
    """Remove acentos de um texto."""
    normalizado = unicodedata.normalize("NFD", texto)
    return "".join(c for c in normalizado if unicodedata.category(c) != "Mn")


def gerar_senha_padrao(nome, identificador):
    """Gera senha no padrão nome+id, sem espaço, sem acento e minúscula."""
    nome_limpo = remover_acentos(nome).replace(" ", "").lower()
    return f"{nome_limpo}{identificador}"
