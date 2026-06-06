# Sistema de Manutenção de Ativos de TI - Versão 3

## Como executar

Entre na pasta `src` e rode:

```bash
python main.py
```

## Gerente padrão para testes

O arquivo `src/dados/funcionarios.json` já vem com 100 funcionários.
O gerente padrão é o ID 1.

Use:

```text
ID: 1
Senha: carloshenrique1
```

## Correções desta versão

- Mescla das alterações do grupo em `main.py`, `funcionarios.py` e `monetario.py`.
- Autenticação real de gerente via `funcionarios.json`.
- Consulta monetária protegida por autenticação.
- Cadastro/listagem de funcionários protegido por autenticação.
- Correção definitiva do erro de persistência por caminho relativo.
- Agora os JSONs ficam em `src/dados` e são acessados por caminho absoluto usando `__file__`.
- `main.py` continua passando `funcionarios` para `atualizar_status_ordem`, evitando o erro `KeyError: id_funcionario`.
- OS aberta não recebe data final, tempo nem custo antes do fechamento.
- Fechamento da OS calcula tempo e custo automaticamente.
