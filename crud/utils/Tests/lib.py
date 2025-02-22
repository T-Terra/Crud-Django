from time import sleep
import requests
from json import loads
from random import randint

class Utils:
    def GetPerson(attPerson):
        url = 'https://www.4devs.com.br/ferramentas_online.php'

        sexRand = randint(0, 1)
        sex = ''

        if sexRand == 0:
            sex = 'H'
        else:
            sex = 'M'

        # Dados enviados no body da requisição
        payload = {
            'acao': 'gerar_pessoa',
            'sexo': sex,
            'pontuacao': 'S',
            'idade': randint(1, 110),
            'cep_estado': '',
            'txt_qtde': 1,
            'cep_cidade': '',    
        }

        # Cabeçalhos para simular navegador real
        headers = {
            'User-Agent': 'Batata',
        }

        # Fazendo a requisição POST
        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            respList = loads(response.text)
            return respList[0][attPerson]
        else:
            print("Erro:", response.status_code)

    def SlowTypes(self, actions, text: str, elementWeb, time=0.5):
        for char in text:
            actions.send_keys_to_element(elementWeb, char).perform()
            sleep(time)