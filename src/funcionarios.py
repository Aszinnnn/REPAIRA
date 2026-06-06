from utils import obter_data_atual, carregar_dados, salvar_dados, gerar_senha_padrao

ARQUIVO_FUNCIONARIOS = "funcionarios.json"

# Tupla de tuplas usada para exibir e controlar os cargos disponíveis.
CARGOS = (
    ("1", "Estagiário"),
    ("2", "Júnior"),
    ("3", "Pleno"),
    ("4", "Sênior"),
    ("5", "Gerente"),
)

# Dicionário simples com o mapeamento automático de horas mensais.
MAPEAMENTO_CARGA_HORARIA = {
    "12x36": 180,
    "44h semanais": 220,
    "40h semanais": 200,
    "30h semanais": 150,
    "20h semanais": 100,
}


def carregar_funcionarios():
    """Carrega a lista de funcionários do arquivo JSON."""
    return carregar_dados(ARQUIVO_FUNCIONARIOS)


def salvar_funcionarios(lista_funcionarios):
    """Salva a lista de funcionários no arquivo JSON."""
    return salvar_dados(lista_funcionarios, ARQUIVO_FUNCIONARIOS)


def gerar_novo_id_funcionario(lista_funcionarios):
    """Gera um novo ID sequencial para funcionário."""
    if not lista_funcionarios:
        return 1
    ids = [funcionario.get("id_funcionario", 0) for funcionario in lista_funcionarios]
    return max(ids) + 1


def buscar_funcionario_id(lista_funcionarios, id_funcionario):
    """Busca um funcionário pelo ID usando .get para evitar KeyError."""
    for funcionario in lista_funcionarios:
        if funcionario.get("id_funcionario") == id_funcionario:
            return funcionario
    return None


def existe_gerente(lista_funcionarios):
    """Verifica se já existe um gerente cadastrado no sistema."""
    for funcionario in lista_funcionarios:
        if funcionario.get("cargo") == "Gerente":
            return True
    return False


def obter_cargo_por_opcao(opcao):
    """Converte a opção digitada em um cargo real."""
    for codigo, cargo in CARGOS:
        if codigo == opcao:
            return cargo
    return None


def obter_horas_mensais_por_carga(carga_horaria):
    """Retorna a quantidade de horas mensais conforme a carga escolhida."""
    return MAPEAMENTO_CARGA_HORARIA.get(carga_horaria, 220)


def autenticar_gerente():
<<<<<<< HEAD

    funcionarios = carregar_funcionarios()

    id_digitado = input("Digite o ID do gerente: ")
    senha_digitada = input("Digite a senha: ")

    for funcionario in funcionarios:

        if (
            str(funcionario["id_funcionario"]) == id_digitado
            and funcionario["senha"] == senha_digitada
            and funcionario["cargo"] == "Gerente"
        ):
            return True

=======
    """Autentica o gerente pelo ID e senha cadastrados em funcionarios.json."""
    funcionarios = carregar_funcionarios()

    print("\n" + "=" * 50)
    print("🔐 AUTENTICAÇÃO DE GERENTE")
    print("=" * 50)

    id_digitado = input("Digite o ID do gerente: ").strip()
    senha_digitada = input("Digite a senha: ").strip()

    for funcionario in funcionarios:
        id_funcionario = str(funcionario.get("id_funcionario"))
        senha = funcionario.get("senha")
        cargo = funcionario.get("cargo")

        if id_funcionario == id_digitado and senha == senha_digitada and cargo == "Gerente":
            print("✅ Acesso autorizado!")
            return True

    print("❌ Acesso negado! ID, senha ou cargo inválido.")
>>>>>>> 5f4d35c (Atualização OS e de funcionarios)
    return False


def listar_funcionarios_resumido(lista_funcionarios):
    """Exibe uma lista resumida de funcionários."""
    if not lista_funcionarios:
        print("\nNenhum funcionário cadastrado!")
        return

    print("\n" + "-" * 80)
    print(f"{'ID':<6} {'Nome':<28} {'Cargo':<15} {'R$/Hora':<12}")
    print("-" * 80)
    for funcionario in lista_funcionarios:
        print(
            f"{funcionario.get('id_funcionario'):<6} "
            f"{funcionario.get('nome', ''):<28} "
            f"{funcionario.get('cargo', ''):<15} "
            f"{funcionario.get('salario_por_hora', 0):<12.2f}"
        )
    print("-" * 80)


def listar_funcionarios_completo(lista_funcionarios):
    """Exibe uma lista completa de funcionários cadastrados."""
    if not lista_funcionarios:
        print("\nNenhum funcionário cadastrado!")
        return

    print("\n" + "=" * 110)
    print("👥 FUNCIONÁRIOS CADASTRADOS")
    print("=" * 110)
    for funcionario in lista_funcionarios:
        print(f"ID: {funcionario.get('id_funcionario')}")
        print(f"Nome: {funcionario.get('nome')}")
        print(f"Cargo: {funcionario.get('cargo')}")
        print(f"Carga Horária: {funcionario.get('carga_horaria')}")
        print(f"Horas Mensais: {funcionario.get('horas_mensais')}")
        print(f"Salário Líquido: R$ {funcionario.get('salario_liquido', 0):.2f}")
        print(f"Salário por Hora: R$ {funcionario.get('salario_por_hora', 0):.2f}")
        print(f"Senha Padrão: {funcionario.get('senha')}")
        print("-" * 110)


def cadastrar_funcionario(lista_funcionarios):
    """Cadastra um novo funcionário no sistema."""
    print("\n" + "=" * 60)
    print("👤 REGISTRO DE FUNCIONÁRIOS")
    print("=" * 60)

    nome = input("Digite o nome do funcionário: ").strip()
    if not nome:
        print("❌ O nome não pode ficar vazio.")
        return lista_funcionarios

    print("\nEscolha o cargo:")
    for codigo, cargo in CARGOS:
        print(f"{codigo} - {cargo}")

    opcao_cargo = input("Digite a opção do cargo: ").strip()
    cargo = obter_cargo_por_opcao(opcao_cargo)

    if not cargo:
        print("Favor, digite uma opção válida")
        return lista_funcionarios

    if cargo == "Gerente" and existe_gerente(lista_funcionarios):
        print("\n❌ Já existe um gerente cadastrado no sistema!")
        return lista_funcionarios

    salario_liquido_texto = input("Digite o salário líquido do funcionário: ").replace(",", ".").strip()
    try:
        salario_liquido = float(salario_liquido_texto)
    except ValueError:
        print("❌ Salário inválido!")
        return lista_funcionarios

    print("\nModelos de carga horária disponíveis:")
    cargas = tuple(MAPEAMENTO_CARGA_HORARIA.keys())
    for indice, carga in enumerate(cargas, start=1):
        print(f"{indice} - {carga}")

    opcao_carga = input("Digite a opção da carga horária: ").strip()
    try:
        indice_carga = int(opcao_carga) - 1
        carga_horaria = cargas[indice_carga]
    except (ValueError, IndexError):
        print("Favor, digite uma opção válida")
        return lista_funcionarios

    horas_mensais = obter_horas_mensais_por_carga(carga_horaria)
    salario_por_hora = round(salario_liquido / horas_mensais, 2)
    novo_id = gerar_novo_id_funcionario(lista_funcionarios)
    senha = gerar_senha_padrao(nome, novo_id)

    novo_funcionario = {
        "id_funcionario": novo_id,
        "senha": senha,
        "nome": nome,
        "cargo": cargo,
        "salario_liquido": salario_liquido,
        "carga_horaria": carga_horaria,
        "horas_mensais": horas_mensais,
        "salario_por_hora": salario_por_hora,
        "ativo": True,
        "data_cadastro": obter_data_atual(),
    }

    lista_funcionarios.append(novo_funcionario)
    salvar_funcionarios(lista_funcionarios)

    print("\n✅ Funcionário cadastrado com sucesso!")
    print(f"ID: {novo_id}")
    print(f"Senha padrão gerada: {senha}")
    print(f"Salário por hora: R$ {salario_por_hora:.2f}")

    return lista_funcionarios
