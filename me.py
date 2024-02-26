import re
import PyPDF2
import pandas as pd

def tratando_string(all_text):
    palavras_excluir = ["ALLEGRO","SCI Syndkos v24.02.21.2", "Histórico de Unidades - Sem período definido\n","\n\n"]
    
    for palavra in palavras_excluir:
        all_text = re.sub(palavra,"", all_text)
    
    return all_text

def dados_proprietarios(data_pages):
    
    regex_proprietario = re.compile(r'Proprietário:(.*?)(?=(?:\n\w|Email de Cobrança:))', re.DOTALL)
    
    proprietario = regex_proprietario.findall(data_pages)

    return proprietario
    

def extair_dados(data_pages):

    regex_unidade = re.compile(r'Apartamento: (\d+)')
    # regex_proprietario = re.compile(r'Proprietário: (.+)\nCPF/CNPJ: (.+)\nData de Entrada: (.+)\nData de Saída: (.*)\nEndereço: (.+)\nComplemento: (.+)\nBairro: (.+)\nCEP: (\d{5}-\d{3})\nCidade: (.+)\nEstado: (.+)\nTelefone Principal: (.*)\nResidencial:(.*)\nCelular: (.*)\nEmail de Cobrança: (.+@.+)')
    # regex_inquilino = re.compile(r'Inquilino: (.+)\nCPF/CNPJ: (.+)\nData de Entrada: (.+)\nData de Saída: (.*)\nEndereço: (.+)\nComplemento: (.+)\nBairro: (.+)\nCEP: (\d{5}-\d{3})\nCidade: (.+)\nEstado: (.+)\nTelefone Principal: (.*)\nResidencial:(.*)\nCelular: (.*)\nEmail de Cobrança: (.+@.+)')
    
    apartamentos = regex_unidade.findall(data_pages)
    data_pages = data_pages.split("Apartamento:")
    print(data_pages)
    index = 0
    data = []

    while index < len(apartamentos):
        unidades = {
            'Apartamento': apartamentos[index],
            'Proprietario': dados_proprietarios(data_pages[index+1]),
        }
        data.append(unidades)
                
        index += 1
    
    return data
    



def main():

    # Caminho Arquivo
    pdf_path = "C:\\Users\\breno\\Downloads\\Dados\\ALLEGRO CADASTRO DE UNIDADE.pdf"

    # Gerencimaneto do arquivo / 'rb' significa o modo de leitura binária
    with open(pdf_path, 'rb') as arquivo:
        # Atribui a variável reader o objeto lido em arquivo
        reader = PyPDF2.PdfReader(arquivo)

        # Extrai o textos das paginas 
        # Isso é uma compreensão de lista que itera sobre todos os números de página e extrai o texto de cada página usando o método extract_text() do objeto reader.pages[page_num]. Isso resulta em uma lista contendo o texto de cada página.
        text = ''.join([reader.pages[page_num].extract_text() 
                            for page_num in range(len(reader.pages))])
        
        all_text = tratando_string(text)
        
    
    # Lista onde serão armazenados todos os dados
    all_data = []

    # Atribuiu a lista all_data todas as informações do PDF
    all_data = extair_dados(all_text)
    #print(all_data)

    # Criando um dataframe pandas com os dados
    df = pd.DataFrame(all_data)

    # Exporta o dataframe para um arquivo excel
    # excel_file_path define o nome do arquivo que será criado ou atualizado
    excel_file_path = "dados_unidades_allergo.xlsx"

    # # Transorma o dataframe em excel e exporta com o nome do excel_file_path e não define o index como uma coluna
    df.to_excel(excel_file_path, index=False)

main()