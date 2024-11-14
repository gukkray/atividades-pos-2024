import json

def exibir_imovel(imovel):
    print(f"Descrição: {imovel['descricao']}")
    print("Proprietário:")
    print(f"  Nome: {imovel['proprietario']['nome']}")
    if 'email' in imovel['proprietario']:
        print(f"  Email: {', '.join(imovel['proprietario']['email'])}")
    if 'telefone' in imovel['proprietario']:
        print(f"  Telefone(s): {', '.join(imovel['proprietario']['telefone'])}")
    print("Endereço:")
    print(f"  Rua: {imovel['endereco']['rua']}")
    print(f"  Bairro: {imovel['endereco']['bairro']}")
    print(f"  Cidade: {imovel['endereco']['cidade']}")
    if 'numero' in imovel['endereco']:
        print(f"  Número: {imovel['endereco']['numero']}")
    print("Características:")
    print(f"  Tamanho: {imovel['caracteristicas']['tamanho']}")
    print(f"  Quartos: {imovel['caracteristicas']['numQuartos']}")
    print(f"  Banheiros: {imovel['caracteristicas']['numBanheiros']}")
    print(f"Valor: {imovel['valor']}")
    print("-" * 40)

def main():
    with open('../json/imobiliaria.json', 'r') as f:
        dados_imobiliaria = json.load(f)


    # Acessa a lista de imóveis, que está dentro de 'imobiliaria' -> 'imovel'
    imoveis = dados_imobiliaria['imobiliaria']['imovel']

    # Menu com os IDs dos imóveis
    print("Imóveis disponíveis:")
    for idx, imovel in enumerate(imoveis, start=1):
        print(f"{idx} - {imovel['descricao']}")

    # Solicita ao usuário o ID do imóvel
    try:
        opcao = int(input("Digite o ID do imóvel para saber mais: ")) - 1  # Subtrai 1 para ajustar o índice
        if 0 <= opcao < len(imoveis):
            exibir_imovel(imoveis[opcao])
        else:
            print("ID inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == '__main__':
    main()
