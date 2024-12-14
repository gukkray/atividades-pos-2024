import zeep

wsdl_countries = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
wsdl_number_to_words = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"


countries_client = zeep.Client(wsdl=wsdl_countries)
numbers_client = zeep.Client(wsdl=wsdl_number_to_words)

def get_norway_capital():
    """Obtém a capital da Noruega (NO)."""
    country_code = "NO"  
    return countries_client.service.CapitalCity(sCountryISOCode=country_code)

def number_to_words(number):
    """Converte um número em texto por extenso."""
    return numbers_client.service.NumberToWords(ubiNum=number)

if __name__ == "__main__":
    print("===== CAPITAL DA NORUEGA =====")
    norway_capital = get_norway_capital()
    print(f"A capital da Noruega é: {norway_capital}\n")

    print("===== NÚMERO POR EXTENSO =====")
    number = int(input("Digite um número para converter por extenso: "))
    number_in_words = number_to_words(number)
    print(f"O número {number} por extenso é: {number_in_words}")
