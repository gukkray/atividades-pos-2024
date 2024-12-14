from clients.user_wrapper import UserAPI
import json
from colorama import Fore, Style

def print_success(message):
    print(Fore.GREEN + message + Style.RESET_ALL)

def print_error(message):
    print(Fore.RED + message + Style.RESET_ALL)

def detail_user(user):
    print(f"\n{Fore.YELLOW}=== Detalhes do Usuário ==={Style.RESET_ALL}")
    print(f"Nome: {user['name']} ({user['username']})")
    print(f"Email: {user['email']}")
    print(f"Telefone: {user['phone']}")
    print(f"Website: {user['website']}")
    print("\nEndereço:")
    print(f"  Rua: {user['address']['street']}, {user['address']['suite']}")
    print(f"  Cidade: {user['address']['city']} - CEP: {user['address']['zipcode']}")
    print("\nEmpresa:")
    print(f"  Nome: {user['company']['name']}")
    print(f"  Slogan: {user['company']['catchPhrase']}")
    print("")

def list_users():
    try:
        users = UserAPI.list_users()
        print(f"{Fore.YELLOW}=== Lista de Usuários ==={Style.RESET_ALL}")
        for user in users:
            print(f"{user['id']}. {user['name']} ({user['username']})")
        print("")
    except Exception as e:
        print_error(str(e))

def create_user():
    print(f"{Fore.YELLOW}=== Criar Novo Usuário ==={Style.RESET_ALL}")
    name = input("Nome Completo: ")
    username = input("Nome de Usuário: ")
    email = input("Email: ")
    try:
        user = UserAPI.create_user(name, username, email)
        print_success("Usuário criado com sucesso!")
        detail_user(user)
    except Exception as e:
        print_error(str(e))

def update_user():
    print(f"{Fore.YELLOW}=== Atualizar Usuário ==={Style.RESET_ALL}")
    user_id = input("ID do Usuário: ")
    try:
        user = UserAPI.get_user(user_id)
        print(f"Nome Atual: {user['name']}")
        name = input("Novo Nome (ou Enter para manter): ")
        username = input("Novo Username (ou Enter para manter): ")
        email = input("Novo Email (ou Enter para manter): ")
        updated_user = UserAPI.update_user(user_id, name=name or None, username=username or None, email=email or None)
        print_success("Usuário atualizado com sucesso!")
        detail_user(updated_user)
    except Exception as e:
        print_error(str(e))

def delete_user():
    print(f"{Fore.YELLOW}=== Deletar Usuário ==={Style.RESET_ALL}")
    user_id = input("ID do Usuário: ")
    try:
        UserAPI.delete_user(user_id)
        print_success(f"Usuário {user_id} deletado com sucesso!")
    except Exception as e:
        print_error(str(e))

def main_menu():
    while True:
        print(f"{Fore.CYAN}=== JSONPlaceholder CLI ==={Style.RESET_ALL}")
        print("1. Listar Usuários")
        print("2. Criar Usuário")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("0. Sair")
        choice = input("\nEscolha uma opção: ").strip()

        if choice == "1":
            list_users()
        elif choice == "2":
            create_user()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "0":
            print("Saindo...")
            break
        else:
            print_error("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main_menu()
