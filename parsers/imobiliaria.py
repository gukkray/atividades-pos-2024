import xml.etree.ElementTree as ET
import json


tree = ET.parse('../xml/imobiliaria.xml')
root = tree.getroot()

def parse_imobiliaria(root):
    imobiliaria = {"imoveis": []}
    for imovel in root.findall('imovel'):
        descricao = imovel.find('descricao').text
        proprietario_element = imovel.find('proprietario')
        nome_proprietario = proprietario_element.find('nome').text
        emails = [email.text for email in proprietario_element.findall('email')]
        telefones = [telefone.text for telefone in proprietario_element.findall('telefone')]
        endereco_element = imovel.find('endereco')
        endereco = {
            "rua": endereco_element.find('rua').text,
            "bairro": endereco_element.find('bairro').text,
            "cidade": endereco_element.find('cidade').text,
            "numero": endereco_element.find('numero').text if endereco_element.find('numero') is not None else None
        }

        caracteristicas_element = imovel.find('caracteristicas')
        caracteristicas = {
            "tamanho": caracteristicas_element.find('tamanho').text,
            "numQuartos": caracteristicas_element.find('numQuartos').text,
            "numBanheiros": caracteristicas_element.find('numBanheiros').text
        }

        valor = imovel.find('valor').text

        imobiliaria["imoveis"].append({
            "descricao": descricao,
            "proprietario": {
                "nome": nome_proprietario,
                "emails": emails,
                "telefones": telefones
            },
            "endereco": endereco,
            "caracteristicas": caracteristicas,
            "valor": valor
        })

    return imobiliaria

imobiliaria_data = parse_imobiliaria(root)
with open("../json/imobiliaria.json", "w", encoding='utf-8') as json_file:
    json.dump(imobiliaria_data, json_file, ensure_ascii=False, indent=4)

print("Arquivo JSON gerado com sucesso.")
