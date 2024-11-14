from xml.dom.minidom import parse
import os

def exibir_menu(pratos):
    print("Cardápio:")
    for i, prato in enumerate(pratos, start=1):
        nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
        print(f"{i} - {nome}")

def exibir_detalhes_prato(pratos, escolha):
    try:
        prato = pratos[escolha - 1]
        nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
        descricao = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue
        ingredientes = [ing.firstChild.nodeValue for ing in prato.getElementsByTagName("ingredientes")[0].getElementsByTagName("ingrediente")]
        preco = prato.getElementsByTagName("preco")[0].firstChild.nodeValue
        calorias = prato.getElementsByTagName("calorias")[0].firstChild.nodeValue
        tempo_preparo = prato.getElementsByTagName("tempodePreparo")[0].firstChild.nodeValue

        print("\nNome:", nome)
        print("Descrição:", descricao)
        print("Ingredientes:")
        for ingrediente in ingredientes:
            print("    " + ingrediente)
        print("Preço:", preco)
        print("Calorias:", calorias)
        print("Tempo de preparo:", tempo_preparo)
    except IndexError:
        print("Opção inválida. Tente novamente.")

def main():
    caminho_arquivo_xml = os.path.join("..", "xml", "cardapio.xml")
    dom = parse(caminho_arquivo_xml)
    cardapio = dom.documentElement
    pratos = cardapio.getElementsByTagName("prato")
    
    exibir_menu(pratos)
    
    try:
        escolha = int(input("\nDigite o número do prato para saber mais: "))
        exibir_detalhes_prato(pratos, escolha)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    main()
