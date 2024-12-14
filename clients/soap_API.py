import requests
from xml.dom.minidom import parseString

# URL da API SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# Função para enviar uma requisição SOAP
def send_soap_request(action, payload):
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': action
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.text

# Função para fazer o parse do XML usando xml.dom.minidom
def parse_soap_response(xml_response, tag_name):
    dom = parseString(xml_response)
    elements = dom.getElementsByTagName(tag_name)
    return elements[0].firstChild.nodeValue if elements else None

# 1. Descobrir a capital da Nova Zelândia
def get_capital_nz():
    payload = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                <sCountryISOCode>NZ</sCountryISOCode>
            </CapitalCity>
        </soap:Body>
    </soap:Envelope>"""
    response = send_soap_request("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso#CapitalCity", payload)
    return parse_soap_response(response, "m:CapitalCityResult")

# 2. Testar outras 3 funções da API

# Função para obter a moeda de um país
def get_country_currency(country_code):
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
                <sCountryISOCode>{country_code}</sCountryISOCode>
            </CountryCurrency>
        </soap:Body>
    </soap:Envelope>"""
    response = send_soap_request("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso#CountryCurrency", payload)
    return parse_soap_response(response, "m:sName")

# Função para obter o código de telefone de um país
def get_country_phone_code(country_code):
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <CountryIntPhoneCode xmlns="http://www.oorsprong.org/websamples.countryinfo">
                <sCountryISOCode>{country_code}</sCountryISOCode>
            </CountryIntPhoneCode>
        </soap:Body>
    </soap:Envelope>"""
    response = send_soap_request("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso#CountryIntPhoneCode", payload)
    return parse_soap_response(response, "m:CountryIntPhoneCodeResult")

# Função para obter os idiomas oficiais de um país
def get_country_languages(country_code):
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <CountryLanguages xmlns="http://www.oorsprong.org/websamples.countryinfo">
                <sCountryISOCode>{country_code}</sCountryISOCode>
            </CountryLanguages>
        </soap:Body>
    </soap:Envelope>"""
    response = send_soap_request("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso#CountryLanguages", payload)
    return parse_soap_response(response, "m:CountryLanguagesResult")

# Demonstração das tarefas solicitadas
if __name__ == "__main__":
    # 1. Capital da Nova Zelândia
    print("===== CAPITAL DA NOVA ZELÂNDIA =====")
    print(f"A capital da Nova Zelândia é: {get_capital_nz()}\n")

    # 2. Testes com outras 3 funções
    print("===== MOEDA DA AUSTRÁLIA =====")
    print(f"A moeda da Austrália é: {get_country_currency('AU')}")
    
    print("===== CÓDIGO DE TELEFONE DO BRASIL =====")
    print(f"O código de telefone do Brasil é: {get_country_phone_code('BR')}")
    
    print("===== IDIOMAS DA ESPANHA =====")
    print(f"Os idiomas oficiais da Espanha são: {get_country_languages('ES')}")
