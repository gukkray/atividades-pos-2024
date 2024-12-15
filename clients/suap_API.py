import requests
import os
import json
from getpass import getpass
from tabulate import tabulate  

API_URL = "https://suap.ifrn.edu.br/api/"
TOKEN_FILE = "token.json"


def auth(api_url):
    user = input("Matrícula: ")
    password = getpass("Senha: ")

    data = {"username": user, "password": password}
    response = requests.post(api_url + "v2/autenticacao/token/", json=data)

    if response.status_code == 200:
        token = response.json()["access"]
        print("\nToken gerado com sucesso!")
        return token
    else:
        print("Erro na autenticação:", response.status_code, response.text)
        exit()


def verify_token(api_url, token):
    response = requests.post(api_url + "v2/autenticacao/token/verify/", json={"token": token})
    if response.status_code == 200:
        return True
    else:
        return False


def boletim_request(api_url, token, ano_letivo):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{api_url}v2/minhas-informacoes/boletim/{ano_letivo}/1", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao buscar o boletim:", response.status_code, response.text)
        exit()


def exibir_boletim(boletim):
    tabela = []
    for disciplina in boletim:
        avaliacoes = disciplina.get("avaliacoes", [])
        notas = [av.get("nota", "N/A") for av in avaliacoes]  
        while len(notas) < 4:  
            notas.append("N/A")

        linha = [
            disciplina['disciplina'],
            notas[0],  
            notas[1],  
            notas[2],  
            notas[3],  
            disciplina.get('media_disciplina', "N/A")
        ]
        tabela.append(linha)

    headers = ["Disciplina", "Nota 1", "Nota 2", "Nota 3", "Nota 4", "Média Final"]
    print("\nBoletim formatado:")
    print(tabulate(tabela, headers=headers, tablefmt="grid"))


def main():
    ano_letivo = input("Digite o ano letivo (ex: 2023): ")

    if os.path.isfile(TOKEN_FILE):
        with open(TOKEN_FILE) as file:
            token = json.load(file)['token']

        if not verify_token(API_URL, token):  
            print("Token expirado. Gerando um novo...")
            token = auth(API_URL)
            with open(TOKEN_FILE, "w") as file:
                json.dump({"token": token}, file)
    else:
        print("Nenhum token encontrado. Gerando um novo...")
        token = auth(API_URL)
        with open(TOKEN_FILE, "w") as file:
            json.dump({"token": token}, file)

    boletim = boletim_request(API_URL, token, ano_letivo)
    if boletim:
        exibir_boletim(boletim)
    else:
        print("Nenhum boletim encontrado!")


if __name__ == "__main__":
    main()
