def listar_ordens_abertas(lista_ordens, lista_computadores=None):
    abertas = [o for o in lista_ordens if o.get("status") in ["Aberta", "Em Andamento"]]
    if not abertas:
        print("\nNenhuma ordem aberta ou em andamento."); return
    print("\n" + "=" * 125); print("📑 ORDENS ABERTAS / EM ANDAMENTO")
    print(f"{'OS':<5} {'Computador':<18} {'Tipo':<12} {'Prioridade':<10} {'Funcionário':<25} {'Status':<15} {'SLA':<12}")
    for o in abertas: print(f"{o.get('id_os'):<5} {o.get('nome_computador',''):<18} {o.get('tipo_manutencao',''):<12} {o.get('prioridade',''):<10} {o.get('nome_funcionario',''):<25} {o.get('status',''):<15} {o.get('sla_previsto',''):<12}")

def listar_ordens_por_funcionario(lista_ordens, lista_funcionarios):
    if not lista_funcionarios: print("Nenhum funcionário cadastrado."); return
    print("\n📌 ORDENS POR FUNCIONÁRIO")
    for func in lista_funcionarios:
        ordens_func = [o for o in lista_ordens if o.get("id_funcionario") == func.get("id_funcionario")]
        if ordens_func:
            pendentes = [o for o in ordens_func if o.get("status") in ["Aberta", "Em Andamento"]]
            concluidas = [o for o in ordens_func if o.get("status") == "Concluída"]
            print(f"{func.get('nome')} | Total: {len(ordens_func)} | Pendentes: {len(pendentes)} | Concluídas: {len(concluidas)}")
