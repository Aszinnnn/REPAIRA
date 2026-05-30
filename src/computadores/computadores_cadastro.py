from utils import obter_data_atual
from .computadores_repo import gerar_novo_id, salvar_computadores


def cadastrar_computador(lista_computadores):
    """Cadastra um novo computador no sistema."""
    print("\n" + "=" * 50)
    print("📝 CADASTRO DE NOVO COMPUTADOR")
    print("=" * 50)

    # Coleta das informações principais do computador.
    nome = input("Digite o nome do computador: ").strip()
    tipo = input("Tipo (Desktop/Notebook/All-in-One): ").strip()
    modelo = input("Modelo (ex: Dell OptiPlex 3080): ").strip()
    processador = input("Processador (ex: Intel Core i5-10400): ").strip()
    memoria_ram = input("Memória RAM (ex: 8GB, 16GB): ").strip()
    armazenamento = input("Armazenamento (ex: 256GB SSD, 1TB HD): ").strip()
    sistema_operacional = input("Sistema Operacional (ex: Windows 11 Pro): ").strip()
    localizacao = input("Localização (ex: Laboratório - Sala 201): ").strip()
    departamento = input("Departamento (ex: TI, Administrativo): ").strip()

    # Geração do novo ID para manter a ordem dos registros.
    novo_id = gerar_novo_id(lista_computadores)

    # Dicionário com todos os dados do novo computador.
    novo_computador = {
        "id": novo_id,
        "nome": nome,
        "tipo": tipo,
        "modelo": modelo,
        "processador": processador,
        "memoria_ram": memoria_ram,
        "armazenamento": armazenamento,
        "sistema_operacional": sistema_operacional,
        "localizacao": localizacao,
        "departamento": departamento,
        "status": "Operacional",
        "data_cadastro": obter_data_atual(),
        "ultima_manutencao": None,
    }

    # Inclusão do registro e salvamento no arquivo.
    lista_computadores.append(novo_computador)
    salvar_computadores(lista_computadores)

    print("\n" + "=" * 50)
    print("✅ COMPUTADOR CADASTRADO COM SUCESSO!")
    print(f"ID: {novo_id}")
    print(f"Nome: {nome}")
    print("=" * 50)

    return lista_computadores
