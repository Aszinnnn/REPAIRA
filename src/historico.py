from datetime import datetime
from computadores import buscar_computador_id

def exibir_historico_completo(lista_ordens):
    concluidas = [o for o in lista_ordens if o.get("status") == "Concluída"]
    if not concluidas: print("\nNenhuma ordem concluída ainda!"); return
    print("\n📜 HISTÓRICO DE MANUTENÇÕES")
    for o in concluidas: print(f"OS {o.get('id_os')} | {o.get('nome_computador')} | {o.get('tipo_manutencao')} | {o.get('data_conclusao')}")

def exibir_historico_por_computador(lista_ordens, lista_computadores):
    for comp in lista_computadores: print(f"ID: {comp.get('id')} - {comp.get('nome')}")
    try: id_comp = int(input("\nDigite o ID do computador: ").strip())
    except ValueError: print("ID inválido!"); return
    comp = buscar_computador_id(lista_computadores, id_comp)
    if not comp: print("Computador não encontrado!"); return
    ordens = [o for o in lista_ordens if o.get("id_computador") == id_comp]
    if not ordens: print("Nenhuma OS para este computador."); return
    for o in ordens: print(f"OS {o.get('id_os')} | {o.get('tipo_manutencao')} | {o.get('status')} | {o.get('data_abertura')}")

def exibir_estatisticas(lista_ordens, lista_computadores):
    print("\n📊 ESTATÍSTICAS")
    print(f"Total de computadores: {len(lista_computadores)}")
    print(f"Total de OS: {len(lista_ordens)}")
    print(f"Abertas/Andamento: {len([o for o in lista_ordens if o.get('status') in ['Aberta','Em Andamento']])}")
    print(f"Concluídas: {len([o for o in lista_ordens if o.get('status') == 'Concluída'])}")

def exibir_sla_alerta(lista_ordens):
    hoje = datetime.now().date(); encontrou = False
    for o in lista_ordens:
        if o.get("status") in ["Aberta", "Em Andamento"]:
            sla = datetime.strptime(o.get("sla_previsto"), "%Y-%m-%d").date(); dias = (sla - hoje).days
            if dias <= 2: print(f"OS {o.get('id_os')} | SLA {o.get('sla_previsto')} | dias: {dias}"); encontrou=True
    if not encontrou: print("Nenhum alerta de SLA.")
