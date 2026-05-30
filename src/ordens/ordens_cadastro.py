from utils import obter_data_atual, calcular_diferenca_horas
from computadores import buscar_computador_id
from funcionarios import buscar_funcionario_id, listar_funcionarios_resumido
from .ordens_repo import gerar_novo_id_os, salvar_ordens
from .ordens_sla import calcular_sla


def criar_ordem(lista_ordens, lista_computadores, lista_funcionarios):
    """Cria uma nova ordem de serviço vinculada a um computador e a um funcionário."""
    print("\n" + "=" * 50)
    print("🔧 ABRIR NOVA ORDEM DE SERVIÇO")
    print("=" * 50)

    if not lista_computadores:
        print("\nNenhum computador cadastrado! Cadastre um computador antes de abrir uma OS.")
        return lista_ordens

    if not lista_funcionarios:
        print("\nNenhum funcionário cadastrado! Cadastre um funcionário antes de abrir uma OS.")
        return lista_ordens

    # Mostra os computadores disponíveis de forma resumida.
    print("\nCOMPUTADORES DISPONÍVEIS:")
    for computador in lista_computadores:
        print(f"ID: {computador['id']} | Nome: {computador['nome']} | Status: {computador['status']}")

    try:
        id_computador = int(input("\nDigite o ID do computador da OS: ").strip())
    except ValueError:
        print("❌ ID de computador inválido!")
        return lista_ordens

    computador = buscar_computador_id(lista_computadores, id_computador)
    if not computador:
        print("❌ Computador não encontrado!")
        return lista_ordens

    # Mostra os funcionários para o usuário escolher o técnico responsável.
    listar_funcionarios_resumido(lista_funcionarios)

    try:
        id_funcionario = int(input("\nDigite o ID do funcionário responsável: ").strip())
    except ValueError:
        print("❌ ID de funcionário inválido!")
        return lista_ordens

    funcionario = buscar_funcionario_id(lista_funcionarios, id_funcionario)
    if not funcionario:
        print("❌ Funcionário não encontrado!")
        return lista_ordens

    # Coleta dos dados principais da ordem.
    tipo_manutencao = input("Tipo de manutenção (Hardware/Software/Rede/Limpeza): ").strip().title()
    descricao = input("Descrição do problema: ").strip()
    prioridade = input("Prioridade (Crítica/Alta/Média/Baixa): ").strip().title()
    tecnico_responsavel = funcionario["nome"]
    data_abertura = obter_data_atual()

    # A nova funcionalidade monetária usa início e fim para calcular o custo depois.
    data_inicio_manutencao = input("Data e hora de início (AAAA-MM-DD HH:MM:SS): ").strip()
    data_fim_manutencao = input("Data e hora de fim (AAAA-MM-DD HH:MM:SS): ").strip()

    try:
        tempo_total_horas = calcular_diferenca_horas(data_inicio_manutencao, data_fim_manutencao)
    except Exception:
        print("❌ Datas de manutenção inválidas!")
        return lista_ordens

    # O custo é calculado usando o salário por hora do funcionário.
    custo_manutencao = round(funcionario["salario_por_hora"] * tempo_total_horas, 2)

    # Tupla com status válidos, usada como referência didática.
    status_iniciais = ("Aberta", "Em Andamento")
    status = status_iniciais[0]

    nova_ordem = {
        "id_os": gerar_novo_id_os(lista_ordens),
        "id_computador": computador["id"],
        "nome_computador": computador["nome"],
        "tipo_manutencao": tipo_manutencao,
        "descricao": descricao,
        "prioridade": prioridade,
        "tecnico_responsavel": tecnico_responsavel,
        "id_funcionario": funcionario["id_funcionario"],
        "nome_funcionario": funcionario["nome"],
        "data_abertura": data_abertura,
        "data_inicio_manutencao": data_inicio_manutencao,
        "data_fim_manutencao": data_fim_manutencao,
        "tempo_total_horas": tempo_total_horas,
        "status": status,
        "sla_previsto": calcular_sla(prioridade),
        "data_conclusao": None,
        "solucao_aplicada": None,
        "custo_manutencao": custo_manutencao,
    }

    lista_ordens.append(nova_ordem)
    salvar_ordens(lista_ordens)

    print("\n✅ Ordem de serviço criada com sucesso!")
    print(f"OS: {nova_ordem['id_os']}")
    print(f"Computador: {nova_ordem['nome_computador']}")
    print(f"Funcionário: {nova_ordem['nome_funcionario']}")
    print(f"Custo estimado/registrado: R$ {nova_ordem['custo_manutencao']:.2f}")

    return lista_ordens
