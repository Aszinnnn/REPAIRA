from computadores import (
    carregar_computadores,
    cadastrar_computador,
    listar_computadores,
    atualizar_status_computador,
    deletar_computador,
)
from ordens import (
    carregar_ordens,
    criar_ordem,
    listar_ordens_abertas,
    atualizar_status_ordem,
    verificar_sla_atraso,
    listar_ordens_por_funcionario,
)
from historico import (
    exibir_historico_completo,
    exibir_historico_por_computador,
    exibir_estatisticas,
    exibir_sla_alerta,
)
from funcionarios import (
    carregar_funcionarios,
    cadastrar_funcionario,
    listar_funcionarios_completo,
    autenticar_gerente,
)
from monetario import menu_consulta_monetaria


def exibir_menu_principal():
    """Exibe o menu principal do sistema."""
    print("\n" + "=" * 50)
    print(" SISTEMA DE MANUTENÇÃO DE COMPUTADORES")
    print("=" * 50)
    print("[1] Gerenciar Computadores")
    print("[2] Gerenciar Ordens de Serviço")
    print("[3] Histórico e Estatísticas")
    print("[4] Registrar Funcionários")
    print("[5] Consulta Monetária")
    print("[0] Sair")
    print("=" * 50)


def exibir_menu_computadores():
    """Exibe o submenu de computadores."""
    print("\n--- GERENCIAR COMPUTADORES ---")
    print("[1] Cadastrar computador")
    print("[2] Listar computadores")
    print("[3] Atualizar status")
    print("[4] Deletar computador")
    print("[0] Voltar")


def exibir_menu_ordens():
    """Exibe o submenu de ordens de serviço."""
    print("\n--- GERENCIAR ORDENS DE SERVIÇO ---")
    print("[1] Abrir nova ordem")
    print("[2] Listar ordens abertas")
    print("[3] Atualizar status da ordem")
    print("[4] Verificar SLA")
    print("[5] Listar ordens por funcionário")
    print("[0] Voltar")


def exibir_menu_historico():
    """Exibe o submenu de histórico."""
    print("\n--- HISTÓRICO E ESTATÍSTICAS ---")
    print("[1] Histórico completo")
    print("[2] Histórico por computador")
    print("[3] Estatísticas gerais")
    print("[4] Alertas de SLA")
    print("[0] Voltar")


def exibir_menu_funcionarios():
    """Exibe o submenu de funcionários."""
    print("\n--- REGISTRAR FUNCIONÁRIOS ---")
    print("[1] Cadastrar funcionário")
    print("[2] Listar funcionários")
    print("[0] Voltar")


def main():
    """Função principal do sistema."""
    computadores = carregar_computadores()
    ordens = carregar_ordens()
    funcionarios = carregar_funcionarios()

    while True:
        exibir_menu_principal()
        opcao_principal = input("Escolha uma opção: ").strip()

        if opcao_principal == "1":
            while True:
                exibir_menu_computadores()
                opcao_computadores = input("Escolha uma opção: ").strip()

                if opcao_computadores == "1":
                    computadores = cadastrar_computador(computadores)
                elif opcao_computadores == "2":
                    listar_computadores(computadores)
                elif opcao_computadores == "3":
                    computadores = atualizar_status_computador(computadores)
                elif opcao_computadores == "4":
                    computadores = deletar_computador(computadores)
                elif opcao_computadores == "0":
                    break
                else:
                    print("❌ Opção inválida!")

        elif opcao_principal == "2":
            while True:
                exibir_menu_ordens()
                opcao_ordens = input("Escolha uma opção: ").strip()

                if opcao_ordens == "1":
                    ordens = criar_ordem(ordens, computadores, funcionarios)
                elif opcao_ordens == "2":
                    listar_ordens_abertas(ordens, computadores)
                elif opcao_ordens == "3":
                    ordens = atualizar_status_ordem(ordens, computadores)
                elif opcao_ordens == "4":
                    verificar_sla_atraso(ordens)
                elif opcao_ordens == "5":
                    listar_ordens_por_funcionario(ordens, funcionarios)
                elif opcao_ordens == "0":
                    break
                else:
                    print("❌ Opção inválida!")

        elif opcao_principal == "3":
            while True:
                exibir_menu_historico()
                opcao_historico = input("Escolha uma opção: ").strip()

                if opcao_historico == "1":
                    exibir_historico_completo(ordens)
                elif opcao_historico == "2":
                    exibir_historico_por_computador(ordens, computadores)
                elif opcao_historico == "3":
                    exibir_estatisticas(ordens, computadores)
                elif opcao_historico == "4":
                    exibir_sla_alerta(ordens)
                elif opcao_historico == "0":
                    break
                else:
                    print("❌ Opção inválida!")

        elif opcao_principal == "4":
            while True:
                exibir_menu_funcionarios()
                opcao_func = input("Escolha uma opção: ").strip()

                if opcao_func == "1":
                    funcionarios = cadastrar_funcionario(funcionarios)
                elif opcao_func == "2":
                    listar_funcionarios_completo(funcionarios)
                elif opcao_func == "0":
                    break
                else:
                    print("❌ Opção inválida!")

        elif opcao_principal == "5":
            autenticar_gerente()
            menu_consulta_monetaria(ordens, funcionarios)

        elif opcao_principal == "0":
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    main()
