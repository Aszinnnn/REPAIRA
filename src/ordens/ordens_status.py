from utils import obter_data_atual, calcular_diferenca_horas
from funcionarios import buscar_funcionario_id
from .ordens_repo import salvar_ordens

def buscar_ordem_por_id(lista_ordens, id_os):
    for ordem in lista_ordens:
        if ordem.get("id_os") == id_os: return ordem
    return None

def fechar_ordem_servico(ordem, lista_funcionarios):
    if ordem.get("status") == "Concluída": print("\n⚠️ Esta OS já está concluída!"); return ordem
    funcionario = buscar_funcionario_id(lista_funcionarios, ordem.get("id_funcionario"))
    if not funcionario: print("\n❌ Funcionário responsável não encontrado. Verifique funcionarios.json."); return ordem
    data_fechamento = obter_data_atual(); ordem["data_fim_manutencao"] = data_fechamento; ordem["data_conclusao"] = data_fechamento
    if not ordem.get("data_inicio_manutencao"): ordem["data_inicio_manutencao"] = ordem.get("data_abertura", data_fechamento)
    tempo = calcular_diferenca_horas(ordem["data_inicio_manutencao"], ordem["data_fim_manutencao"])
    ordem["tempo_total_horas"] = tempo; ordem["custo_manutencao"] = round(funcionario.get("salario_por_hora", 0) * tempo, 2)
    solucao = input("Digite a solução aplicada: ").strip(); ordem["solucao_aplicada"] = solucao if solucao else "Solução não informada"
    ordem["status"] = "Concluída"; ordem["tecnico_responsavel"] = funcionario.get("nome"); ordem["nome_funcionario"] = funcionario.get("nome")
    print(f"\n✅ OS fechada! Tempo: {tempo}h | Custo: R$ {ordem.get('custo_manutencao'):.2f}")
    return ordem

def atualizar_status_ordem(lista_ordens, lista_funcionarios):
    if not lista_ordens: print("\nNenhuma ordem cadastrada."); return lista_ordens
    for ordem in lista_ordens: print(f"OS {ordem.get('id_os')} | Computador: {ordem.get('nome_computador')} | Funcionário: {ordem.get('nome_funcionario')} | Status: {ordem.get('status')}")
    try: id_os = int(input("\nDigite o ID da OS: ").strip())
    except ValueError: print("ID inválido!"); return lista_ordens
    ordem = buscar_ordem_por_id(lista_ordens, id_os)
    if not ordem: print("OS não encontrada!"); return lista_ordens
    while True:
        print(f"\nOS {ordem.get('id_os')} | Status atual: {ordem.get('status')}")
        print("[1] Fechar ordem de serviço\n[2] Marcar como Em Andamento\n[3] Marcar como Aberta\n[0] Voltar")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1": fechar_ordem_servico(ordem, lista_funcionarios); salvar_ordens(lista_ordens); return lista_ordens
        elif opcao == "2":
            if ordem.get("status") == "Concluída": print("Não é permitido reabrir OS concluída."); return lista_ordens
            ordem["status"] = "Em Andamento"; salvar_ordens(lista_ordens); print("✅ OS marcada como Em Andamento."); return lista_ordens
        elif opcao == "3":
            if ordem.get("status") == "Concluída": print("Não é permitido reabrir OS concluída."); return lista_ordens
            ordem["status"] = "Aberta"; salvar_ordens(lista_ordens); print("✅ OS marcada como Aberta."); return lista_ordens
        elif opcao == "0": return lista_ordens
        else: print("Opção inválida!")
