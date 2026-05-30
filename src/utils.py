import json
import os
import unicodedata
from datetime import datetime


def criar_pasta_dados():
    """Cria a pasta de dados caso ela ainda não exista."""
    if not os.path.exists("dados"):
        os.makedirs("dados")
        print("📁 Pasta 'dados' criada com sucesso!")


def carregar_dados(nome_arquivo):
    """Carrega uma lista de dados em JSON a partir da pasta dados/."""
    criar_pasta_dados()
    caminho_arquivo = f"dados/{nome_arquivo}"

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            print(f"Dados carregados de {nome_arquivo}")
            return dados
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado. Retornando lista vazia.")
        return []
    except json.JSONDecodeError:
        print(f"Arquivo {nome_arquivo} está vazio ou corrompido. Retornando lista vazia.")
        return []


def salvar_dados(dados, nome_arquivo):
    """Salva uma lista de dados em JSON dentro da pasta dados/."""
    criar_pasta_dados()
    caminho_arquivo = f"dados/{nome_arquivo}"

    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print(f"✅ Dados salvos em {nome_arquivo}")
        return True
    except Exception as e:
        print(f"❌ Erro ao salvar {nome_arquivo}: {e}")
        return False


def obter_data_atual():
    """Retorna a data e hora atual formatada como texto."""
    agora = datetime.now()
    return agora.strftime("%Y-%m-%d %H:%M:%S")


def converter_texto_para_data(texto_data):
    """Converte um texto no formato padrão do sistema para datetime."""
    return datetime.strptime(texto_data, "%Y-%m-%d %H:%M:%S")


def remover_acentos(texto):
    """Remove acentos de um texto para facilitar a criação de logins e senhas."""
    texto_normalizado = unicodedata.normalize("NFD", texto)
    texto_sem_acento = "".join(char for char in texto_normalizado if unicodedata.category(char) != "Mn")
    return texto_sem_acento


def gerar_senha_padrao(nome, identificador):
    """Gera uma senha simples no padrão nome+id, sem acentos e sem espaços."""
    nome_tratado = remover_acentos(nome).replace(" ", "").lower()
    return f"{nome_tratado}{identificador}"


def calcular_diferenca_horas(data_inicio, data_fim):
    """Calcula a diferença, em horas, entre duas datas no formato texto do sistema."""
    inicio = converter_texto_para_data(data_inicio)
    fim = converter_texto_para_data(data_fim)
    diferenca_segundos = (fim - inicio).total_seconds()
    return round(diferenca_segundos / 3600, 2)
