import requests
import argparse
import json


BASE_URL = "https://jsonplaceholder.typicode.com"

def listar_usuarios():
    """Lista todos os usuários."""
    response = requests.get(f"{BASE_URL}/users")
    if response.ok:
        users = response.json()
        print(json.dumps(users, indent=4))
    else:
        print(f"Erro: {response.status_code} - {response.text}")

def listar_tarefas_usuario(user_id):
    """Lista as tarefas de um usuário específico."""
    response = requests.get(f"{BASE_URL}/users/{user_id}/todos")
    if response.ok:
        todos = response.json()
        print(json.dumps(todos, indent=4))
    else:
        print(f"Erro: {response.status_code} - {response.text}")

def criar_usuario(nome, usuario, email):
    """Cria um novo usuário."""
    dados_usuario = {"name": nome, "username": usuario, "email": email}
    response = requests.post(f"{BASE_URL}/users", json=dados_usuario)
    if response.ok:
        user = response.json()
        print("Usuário criado com sucesso!")
        print(json.dumps(user, indent=4))
    else:
        print(f"Erro: {response.status_code} - {response.text}")

def ler_usuario(user_id):
    """Lê as informações de um usuário específico."""
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.ok:
        user = response.json()
        print(json.dumps(user, indent=4))
    else:
        print(f"Erro: {response.status_code} - {response.text}")

def atualizar_usuario(user_id, nome=None, usuario=None, email=None):
    """Atualiza um usuário existente."""
    dados_atualizados = {"name": nome, "username": usuario, "email": email}
    dados_atualizados = {k: v for k, v in dados_atualizados.items() if v is not None}
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=dados_atualizados)
    if response.ok:
        user = response.json()
        print("Usuário atualizado com sucesso!")
        print(json.dumps(user, indent=4))
    else:
        print(f"Erro: {response.status_code} - {response.text}")

def deletar_usuario(user_id):
    """Deleta um usuário."""
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    if response.ok:
        print(f"Usuário com ID {user_id} deletado com sucesso!")
    else:
        print(f"Erro: {response.status_code} - {response.text}")

def main():
    parser = argparse.ArgumentParser(description="CLI para usuários do JSON Placeholder")
    subparsers = parser.add_subparsers(dest="comando")

    subparsers.add_parser("listar", help="Lista todos os usuários")

    tarefas_parser = subparsers.add_parser("tarefas", help="Lista as tarefas de um usuário específico")
    tarefas_parser.add_argument("user_id", type=int, help="ID do usuário")

    criar_parser = subparsers.add_parser("criar", help="Cria um novo usuário")
    criar_parser.add_argument("nome", type=str, help="Nome do usuário")
    criar_parser.add_argument("usuario", type=str, help="Username do usuário")
    criar_parser.add_argument("email", type=str, help="Email do usuário")

    ler_parser = subparsers.add_parser("ler", help="Lê as informações de um usuário")
    ler_parser.add_argument("user_id", type=int, help="ID do usuário")

    atualizar_parser = subparsers.add_parser("atualizar", help="Atualiza um usuário existente")
    atualizar_parser.add_argument("user_id", type=int, help="ID do usuário")
    atualizar_parser.add_argument("--nome", type=str, help="Novo nome")
    atualizar_parser.add_argument("--usuario", type=str, help="Novo username")
    atualizar_parser.add_argument("--email", type=str, help="Novo email")

    deletar_parser = subparsers.add_parser("deletar", help="Deleta um usuário")
    deletar_parser.add_argument("user_id", type=int, help="ID do usuário")

    args = parser.parse_args()

    if args.comando == "listar":
        listar_usuarios()
    elif args.comando == "tarefas":
        listar_tarefas_usuario(args.user_id)
    elif args.comando == "criar":
        criar_usuario(args.nome, args.usuario, args.email)
    elif args.comando == "ler":
        ler_usuario(args.user_id)
    elif args.comando == "atualizar":
        atualizar_usuario(args.user_id, args.nome, args.usuario, args.email)
    elif args.comando == "deletar":
        deletar_usuario(args.user_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
