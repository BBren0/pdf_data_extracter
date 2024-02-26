import re
import PyPDF2
import pandas as pd

# Função que extrai as informações do PDF e converte para um DF
def extrair_informacoes_pagina(page_text):
    # Expressões regulares para cada tipo de informação
    regex_unidade = re.compile(r'Apartamento: (\d+)')
    regex_proprietario = re.compile(r'Proprietário: (.+)')
    regex_inquilino = re.compile(r'Inquilino: (.+)')
    # regex_cpf_cnpj = re.compile(r'(?:CPF|CNPJ): (\d{3}\.\d{3}\.\d{3}-\d{2}|\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})')
    regex_cpf_cnpj = re.compile(r'(?:CPF|CNPJ): (.+)')
    regex_coeficiente = re.compile(r'Coeficiente Unidade: ([\d,]+)')
    regex_email = re.compile(r'Email de Cobrança: (.+@.+)')
    regex_endereco = re.compile(r'Endereço: (.+)')
    regex_complemento = re.compile(r'Complemento: (.+)')
    regex_bairro = re.compile(r'Bairro: (.+)')
    regex_cep = re.compile(r'CEP: (\d{5}-\d{3})')
    regex_cidade = re.compile(r'Cidade: (.+)')
    regex_estado = re.compile(r'Estado: (.+)')

    # Procura as informações no PDF
    unidades = regex_unidade.findall(page_text)
    proprietarios = regex_proprietario.findall(page_text)
    inquilinos = regex_inquilino.findall(page_text)
    cpfs_cnpjs = regex_cpf_cnpj.findall(page_text)
    coeficientes = regex_coeficiente.findall(page_text)
    emails = regex_email.findall(page_text)
    enderecos = regex_endereco.findall(page_text)
    complementos = regex_complemento.findall(page_text)
    bairros = regex_bairro.findall(page_text)
    ceps = regex_cep.findall(page_text)
    cidades = regex_cidade.findall(page_text)
    estados = regex_estado.findall(page_text)

    # Organiza as informações em uma lista de dicionários
    data = []
    num_unidades = len(unidades)
    index = 0  # índice para percorrer os proprietários e inquilinos

    print("\n\n\nDaddos antes da readequação")
    print(data)

    while index < num_unidades:
        # Verifica se há informações de proprietário para esta unidade
        while index < num_unidades and regex_proprietario.search(page_text):
            # Adiciona as informações do proprietário
            proprietario_info = {
                'Unidade': unidades[index],
                'Proprietário': proprietarios[index],
                'Inquilino':inquilinos[index],
                'CPF/CNPJ': cpfs_cnpjs[index],
                'Coeficiente': coeficientes[index],
                'Email': emails[index],
                'Endereço': enderecos[index],
                'Complemento': complementos[index],
                'Bairro': bairros[index],
                'CEP': ceps[index],
                'Cidade': cidades[index],
                'Estado': estados[index]
            }
            data.append(proprietario_info)
            index += 1

        # Verifica se há informações de inquilino para esta unidade
        while index < num_unidades and regex_inquilino.search(page_text):
            # Adiciona as informações do inquilino
            inquilino_info = {
                'Unidade': unidades[index],
                'Proprietário': None,  # Define como None porque já adicionamos as informações do proprietário
                'Inquilino': inquilinos[index],
                'CPF/CNPJ': cpfs_cnpjs[index],
                'Coeficiente': coeficientes[index],
                'Email': emails[index],
                'Endereço': enderecos[index],
                'Complemento': complementos[index],
                'Bairro': bairros[index],
                'CEP': ceps[index],
                'Cidade': cidades[index],
                'Estado': estados[index]
            }
            data.append(inquilino_info)
            index += 1
        
        return data

# Caminho do arquivo PDF
pdf_path = "C:\\Users\\Pointer 01\\OneDrive - PointCondominio\Documentos\\Importação Fator\\Cadastro de unidades\\Allegro\\ALLEGRO CADASTRO DE UNIDADE.pdf"

# Lista para armazenar os dados extraídos de todas as páginas
all_data = []

# Abre o arquivo PDF em modo de leitura binária
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    # Extrai o texto de todas as páginas uma vez
    all_text = ''.join([reader.pages[page_num].extract_text() for page_num in range(len(reader.pages))])

    # Extrai as informações de todas as páginas de uma vez
    all_data = extrair_informacoes_pagina(all_text)

print(all_data)

# Cria um DataFrame pandas com os dados extraídos
df = pd.DataFrame(all_data)

print(df)

# Exporta o DataFrame para um arquivo Excel
# excel_file_path = "dados_unidades.xlsx"
# df.to_excel(excel_file_path, index=False)

#print(f"O DataFrame foi exportado para o arquivo Excel: {excel_file_path}")
