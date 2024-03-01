import re
import PyPDF2
import pandas as pd

def tratando_string(all_text):
    palavras_excluir = ["VILLA DI VERONA","SCI Syndkos v24.02.21.2", "Histórico de Unidades - Sem período definido\n","\n\n"]
    
    for palavra in palavras_excluir:
        all_text = re.sub(palavra,"", all_text)
    
    return all_text


def dados_proprietarios(data_pages):
    regex_proprietario = re.compile(r'Proprietário:(.*?)\nCPF/CNPJ: (.+)\nData de Entrada: (.*?)?\nData de Saída:(.+)?\nEndereço: (.*?)?\nComplemento:(.+)?\nBairro:(.*)?\nCEP:(.*)?\nCidade: (.*?)?\nEstado:(.*?)?\nTelefone Principal:(.*?)?\nResidencial:(.*?)?\nCelular:(.*?)?\nEmail de Cobrança:(.*?)?\n')
    proprietarios = regex_proprietario.findall(data_pages)
    n_proprietario = len(proprietarios)
    print(len(proprietarios))
 

    if n_proprietario > 1:
        
        if proprietarios[0][3] is '':
            dados_proprietario = {
                'CPF/CNPJ Proprietário': proprietarios[0][1],
                'Nome Proprietário': proprietarios[0][0],
                'Email Proprietário': proprietarios[0][13],
                'Telefone Proprietário': proprietarios[0][10],
                'Celular Proprietário': proprietarios[0][11],
                'Comercial Proprietário': proprietarios[0][12],
                'Data de entrada': proprietarios[0][2],
                'Data de Saída': proprietarios[0][3],
                'Logradouro Proprietário': proprietarios[0][4],
                'Número Proprietário': None,
                'Complemento Proprietário': proprietarios[0][5],
                'CEP Proprietário': proprietarios[0][7],
                'Bairro Proprietário': proprietarios[0][6],
                'Cidade Proprietário': proprietarios[0][8],
                'Estado Proprietário': proprietarios[0][9],
            }
            return  dados_proprietario
        
        elif proprietarios[1][3] is '': 
            dados_proprietario = {
                'CPF/CNPJ Proprietário': proprietarios[1][1],
                'Nome Proprietário': proprietarios[1][0],
                'Email Proprietário': proprietarios[1][13],
                'Telefone Proprietário': proprietarios[1][10],
                'Celular Proprietário': proprietarios[1][11],
                'Comercial Proprietário': proprietarios[1][12],
                'Data de entrada': proprietarios[1][2],
                'Data de Saída': proprietarios[1][3],
                'Logradouro Proprietário': proprietarios[1][4],
                'Número Proprietário': None,
                'Complemento Proprietário': proprietarios[1][5],
                'CEP Proprietário': proprietarios[1][7],
                'Bairro Proprietário': proprietarios[1][6],
                'Cidade Proprietário': proprietarios[1][8],
                'Estado Proprietário': proprietarios[1][9],
            }
            return  dados_proprietario
           
        else:
            dados_proprietario = {
                'CPF/CNPJ Proprietário': proprietarios[2][1],
                'Nome Proprietário': proprietarios[2][0],
                'Email Proprietário': proprietarios[2][13],
                'Telefone Proprietário': proprietarios[2][10],
                'Celular Proprietário': proprietarios[2][11],
                'Comercial Proprietário': proprietarios[2][12],
                'Data de entrada': proprietarios[2][2],
                'Data de Saída': proprietarios[2][3],
                'Logradouro Proprietário': proprietarios[2][4],
                'Número Proprietário': None,
                'Complemento Proprietário': proprietarios[2][5],
                'CEP Proprietário': proprietarios[2][7],
                'Bairro Proprietário': proprietarios[2][6],
                'Cidade Proprietário': proprietarios[2][8],
                'Estado Proprietário': proprietarios[2][9],
            }
            print("\n\n\n\n\n ATENÇÃO NA UNIDADE DESSE USUÁIRO \n\n\n{proprietario[2]}\n\n")
            return  dados_proprietario
    
    else:
        dados_proprietario = {
                   'CPF/CNPJ Proprietário': proprietarios[0][1],
                'Nome Proprietário': proprietarios[0][0],
                'Email Proprietário': proprietarios[0][13],
                'Telefone Proprietário': proprietarios[0][10],
                'Celular Proprietário': proprietarios[0][11],
                'Comercial Proprietário': proprietarios[0][12],
                'Data de entrada': proprietarios[0][2],
                'Data de Saída': proprietarios[0][3],
                'Logradouro Proprietário': proprietarios[0][4],
                'Número Proprietário': None,
                'Complemento Proprietário': proprietarios[0][5],
                'CEP Proprietário': proprietarios[0][7],
                'Bairro Proprietário': proprietarios[0][6],
                'Cidade Proprietário': proprietarios[0][8],
                'Estado Proprietário': proprietarios[0][9],
            }        
        return  dados_proprietario
        
  
def dados_inquilinos(apartamento, data_pages):
    regex_inquilino = re.compile(r'Inquilino:(.*?)\nCPF/CNPJ: (.+)\nData de Entrada: (.*?)?\nData de Saída:(.+)?\nEndereço: (.*?)?\nComplemento:(.+)?\nBairro:(.*)?\nCEP:(.*)?\nCidade: (.*?)?\nEstado:(.*?)?\nTelefone Principal:(.*?)?\nResidencial:(.*?)?\nCelular:(.*?)?\nEmail de Cobrança:(.*?)?\n')
    inquilino = regex_inquilino.findall(data_pages)
    n_inquilinos = len(inquilino)
    print(f"{apartamento}: {n_inquilinos}")

    if inquilino:
        if n_inquilinos == 1:
            dados_inquilino = {
                    'CPF/CNPJ Responsável': inquilino[0][1],   
                    'Nome Responsável':inquilino[0][0],
                    'Email Responsável': inquilino[0][13],
                    'Telefone Responsável': inquilino[0][10],
                    'Celular Responsável': inquilino[0][12],
                    'Comercial Responsável': inquilino[0][11],
                    'Data de entrada_inquilino': inquilino[0][2],
                    'Data de Saída_inquilino': inquilino[0][3],
                    'Logradouro Responsável': inquilino[0][4],
                    'Complemento_inquilino': inquilino[0][5],
                    'Número Responsável': None,
                    'CEP Responsável': inquilino[0][7],
                    'Bairro Responsável': inquilino[0][6],
                    'Cidade Responsável': inquilino[0][8],
                    'Estado Responsável': inquilino[0][9],
                }
            return dados_inquilino
        if n_inquilinos > 1:
            index = 0
            while n_inquilinos != index:
                if inquilino[index][3] is '':
                    dados_inquilino = {
                    'CPF/CNPJ Responsável': inquilino[index][1],   
                    'Nome Responsável':inquilino[index][0],
                    'Email Responsável': inquilino[index][13],
                    'Telefone Responsável': inquilino[index][10],
                    'Celular Responsável': inquilino[index][12],
                    'Comercial Responsável': inquilino[index][11],
                    'Data de entrada_inquilino': inquilino[index][2],
                    'Data de Saída_inquilino': inquilino[index][3],
                    'Logradouro Responsável': inquilino[index][4],
                    'Complemento_inquilino': inquilino[index][5],
                    'Número Responsável': None,
                    'CEP Responsável': inquilino[index][7],
                    'Bairro Responsável': inquilino[index][6],
                    'Cidade Responsável': inquilino[index][8],
                    'Estado Responsável': inquilino[index][9],
                    
                    }
                    return dados_inquilino
                  
                index += 1     
    else:
        dados_inquilino = {
            'Inquilino': None,
            'Cpf_Inquilino': None,
            'Data de entrada_inquilino': None,
            'Data de Saída_inquilino': None,
            'Logradouro_inquilino': None,
            'Complemento_inquilino': None,
            'Bairro_inquilino': None,
            'CEP_inquiino': None,
            'Cidade_inquilino': None,
            'Estado_inquilino': None,
            'Telefone Principal_inquilino': None,
            'Telefone Residencial_inquilino': None,
            'Celular_inquilino': None,
            'E-mail_inquilino': None
        }
        return dados_inquilino


def extair_dados(data_pages):
    regex_unidade = re.compile(r'Apartamento: (\d+)')
    apartamentos = regex_unidade.findall(data_pages)
    data_pages = data_pages.split("Apartamento:")
    all_data = []
    
    for index, apartamento in enumerate(apartamentos):
        unidade_data = {
                    'Bloco': "Apartamentos",
                    'Unidade': apartamento ,
                    'Rateio': "S",
                    'Tipo de Pessoa Responsável': None
                    }

        unidade_data.update(dados_inquilinos(apartamento, data_pages[index + 1]))
        unidade_data.update(dados_proprietarios(data_pages[index + 1]))
        all_data.append(unidade_data)
        
    return all_data


def main():
    pdf_path = "C:\\Users\\Pointer 01\\OneDrive - PointCondominio\Documentos\\Importação Fator\\Cadastro de unidades\\Villa Di Verona\\VILLA DI VERONA CADASTRO DE UNIDADE.pdf"

    with open(pdf_path, 'rb') as arquivo:
        reader = PyPDF2.PdfReader(arquivo)
        text = ''.join([reader.pages[page_num].extract_text() for page_num in range(len(reader.pages))])
        all_text = tratando_string(text)
        print(all_text)
    all_data = extair_dados(all_text)
    
    colunas = ['Bloco', 'Unidade','Rateio', 'Tipo de Pessoa Responsável',
               'CPF/CNPJ Responsável','Nome Responsável', 'Email Responsável','Telefone Responsável', 'Celular Responsável', 'Comercial Responsável','Data de entrada_inquilino', 'Data de Saída_inquilino', 
               'Logradouro Responsável','Número Responsável', 'Complemento Responsável', 'CEP Responsável','Bairro Responsável', 'Cidade Responsável', 'Estado Responsável', 
               'Tipo de Pessoa Proprietario','CPF/CNPJ Proprietário','Nome Proprietário','Email Proprietário','Telefone Proprietário','Celular Proprietário', 'Comercial Proprietário','Data de entrada', 'Data de Saída', 
               'Logradouro Proprietário','Número Proprietário', 'Complemento Proprietário', 'CEP Proprietário', 'Bairro Proprietário', 'Cidade Proprietário', 'Estado Proprietário']
    
    df = pd.DataFrame(all_data, columns=colunas)
    print(df)

    excel_file_path = "dados_unidades_VillaDiVerona.xlsx"
    df.to_excel(excel_file_path, index=False)
    print("Arquivo exportado com sucesso.")

main()
