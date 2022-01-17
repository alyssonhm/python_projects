# ALYSSON MORANDI
# DESAFIO 4 - CONSUMO DE APIS
# DATA: 10/01/2022

import requests
import sys


def main():
    url = "https://61c5c0edc003e70017b798d5.mockapi.io/produto"
    operacao = int(input('Qual operacao deseja? (1=Consultar Produto / 2=Incluir Produto): '))

    if operacao == 1:

        id_produto = input('Digite o codigo do produto: ')
        response = requests.get(url+'/'+id_produto)

        if response.status_code != 200:
            print('Erro na consulta: ', response.text, 'Status code:', response.status_code) 
            sys.exit()       
        
        produto = response.json()

        print("O produto ", produto['descricao'] ," esta localizado em ", produto['localizacao'] ," e seu estoque é ", produto['estoque'])
        print("Veja o produto atraves do link ", produto['foto'])

    elif operacao == 2:

        print('*** Digite abaixo as informações do produto ***')
        descricao = input('Descricao: ')
        foto = input('LInk da foto do produto: ')
        localizacao = input('Localizacao: ')
        estoque = int(input('Estoque: '))

        data = {"descricao": descricao, "foto": foto, "localizacao": localizacao, "estoque": estoque}         
        
        response = requests.post(url, data=data)
        
        if response.status_code != 201:
            print('Erro na inclusao: ', response.text, 'Status code:', response.status_code) 
            sys.exit()            
        
        print('Cadastrado com sucesso', response.text)

    else:
        print('Operacao invalida, escolha entre (1=Consultar Produto / 2=Incluir Produto)')


main()
