import re
import PyPDF2
import pandas as pd

def tratando_string(all_text):
    palavras_excluir = ["ALLEGRO","SCI Syndkos v24.02.21.2", "Histórico de Unidades - Sem período definido\n","\n\n"]
    
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
                'Cpf_proprietario': proprietarios[0][1],
                'Proprietario': proprietarios[0][0],
                'E-mail': proprietarios[0][13],
                'Telefone Principal': proprietarios[0][10],
                'Telefone Residencial': proprietarios[0][11],
                'Celular': proprietarios[0][12],
                'Data de entrada': proprietarios[0][2],
                'Data de Saída': proprietarios[0][3],
                'Logradouro': proprietarios[0][4],
                'Número': None,
                'Complemento': proprietarios[0][5],
                'CEP': proprietarios[0][7],
                'Bairro': proprietarios[0][6],
                'Cidade': proprietarios[0][8],
                'Estado': proprietarios[0][9],
            }
            return  dados_proprietario
        
        elif proprietarios[1][3] is '': 
            dados_proprietario = {
                'Cpf_proprietario': proprietarios[1][1],
                'Proprietario': proprietarios[1][0],
                'E-mail': proprietarios[1][13],
                'Telefone Principal': proprietarios[1][10],
                'Telefone Residencial': proprietarios[1][11],
                'Celular': proprietarios[1][12],
                'Data de entrada': proprietarios[1][2],
                'Data de Saída': proprietarios[1][3],
                'Logradouro': proprietarios[1][4],
                'Número': None,
                'Complemento': proprietarios[1][5],
                'CEP': proprietarios[1][7],
                'Bairro': proprietarios[1][6],
                'Cidade': proprietarios[1][8],
                'Estado': proprietarios[1][9],
            }
            return  dados_proprietario
           
        else:
            dados_proprietario = {
                'Cpf_proprietario': proprietarios[2][2],
                'Proprietario': proprietarios[2][0],
                'E-mail': proprietarios[2][13],
                'Telefone Principal': proprietarios[2][10],
                'Telefone Residencial': proprietarios[2][11],
                'Celular': proprietarios[2][12],
                'Data de entrada': proprietarios[2][2],
                'Data de Saída': proprietarios[2][3],
                'Logradouro': proprietarios[2][4],
                'Número': None,
                'Complemento': proprietarios[2][5],
                'CEP': proprietarios[2][7],
                'Bairro': proprietarios[2][6],
                'Cidade': proprietarios[2][8],
                'Estado': proprietarios[2][9],
            }
            print("\n\n\n\n\n ATENÇÃO NA UNIDADE DESSE USUÁIRO \n\n\n{proprietario[2]}\n\n")
            return  dados_proprietario
    
    else:
        dados_proprietario = {
                'Proprietario': proprietarios[0][0],
                'Cpf_proprietario': proprietarios[0][1],
                'Data de entrada': proprietarios[0][2],
                'Data de Saída': proprietarios[0][3],
                'Logradouro': proprietarios[0][4],
                'Complemento': proprietarios[0][5],
                'Bairro': proprietarios[0][6],
                'CEP': proprietarios[0][7],
                'Cidade': proprietarios[0][8],
                'Estado': proprietarios[0][9],
                'Telefone Principal': proprietarios[0][10],
                'Telefone Residencial': proprietarios[0][11],
                'Celular': proprietarios[0][12],
                'E-mail': proprietarios[0][13]
            }        
        return  dados_proprietario
        
  
def dados_inquilinos(apartamento, data_pages):
    regex_inquilino = re.compile(r'Inquilino:(.*?)\nCPF/CNPJ: (.+)\nData de Entrada: (.*?)?\nData de Saída:(.+)?\nEndereço: (.*?)?\nComplemento:(.+)?\nBairro:(.*)?\nCEP:(.*)?\nCidade: (.*?)?\nEstado:(.*?)?\nTelefone Principal:(.*?)?\nResidencial:(.*?)?\nCelular:(.*?)?\nEmail de Cobrança:(.*?)?\n')
    inquilino = regex_inquilino.findall(data_pages)
    n_inquilino = len(inquilino)
    print(f"{apartamento}: {n_inquilino}")

    if inquilino:
        if n_inquilino > 1:
            if inquilino[0][3] is '':
                dados_inquilino = {
                    'Cpf_proprietario': inquilino[0][1],
                    'Proprietario': inquilino[0][0],
                    'E-mail': inquilino[0][13],
                    'Telefone Principal': inquilino[0][10],
                    'Telefone Residencial': inquilino[0][11],
                    'Celular': inquilino[0][12],
                    'Data de entrada': inquilino[0][2],
                    'Data de Saída': inquilino[0][3],
                    'Logradouro': inquilino[0][4],
                    'Número': None,
                    'Complemento': inquilino[0][5],
                    'CEP': inquilino[0][7],
                    'Bairro': inquilino[0][6],
                    'Cidade': inquilino[0][8],
                    'Estado': inquilino[0][9],
                }
                return dados_inquilino
            
            elif inquilino[1][3] is '':
                dados_inquilino = {
                    'Cpf_proprietario': inquilino[1][1],
                    'Proprietario': inquilino[1][0],
                    'E-mail': inquilino[1][13],
                    'Telefone Principal': inquilino[1][10],
                    'Telefone Residencial': inquilino[1][11],
                    'Celular': inquilino[1][12],
                    'Data de entrada': inquilino[1][2],
                    'Data de Saída': inquilino[1][3],
                    'Logradouro': inquilino[1][4],
                    'Número': None,
                    'Complemento': inquilino[1][5],
                    'CEP': inquilino[1][7],
                    'Bairro': inquilino[1][6],
                    'Cidade': inquilino[1][8],
                    'Estado': inquilino[1][9],
                }
                return dados_inquilino
            
            else:
                dados_inquilino = {
                    'Cpf_proprietario': inquilino[2][1],
                    'Proprietario': inquilino[2][0],
                    'E-mail': inquilino[2][13],
                    'Telefone Principal': inquilino[2][10],
                    'Telefone Residencial': inquilino[2][11],
                    'Celular': inquilino[2][12],
                    'Data de entrada': inquilino[2][2],
                    'Data de Saída': inquilino[2][3],
                    'Logradouro': inquilino[2][4],
                    'Número': None,
                    'Complemento': inquilino[2][5],
                    'CEP': inquilino[2][7],
                    'Bairro': inquilino[2][6],
                    'Cidade': inquilino[2][8],
                    'Estado': inquilino[2][9],
                }
                print(f"\n\n\n\n\n ATENÇÃO NA UNIDADE DESSE USUÁIRO \n\n\n{inquilino[2]}\n\n")
                return dados_inquilino
            
        else:
            dados_inquilino = {
                    'Inquilino':inquilino[0][0],
                    'Cpf_Inquilino': inquilino[0][1],
                    'Data de entrada_inquilino': inquilino[0][2],
                    'Data de Saída_inquilino': inquilino[0][3],
                    'Logradouro_inquilino': inquilino[0][4],
                    'Complemento_inquilino': inquilino[0][5],
                    'Bairro_inquilino': inquilino[0][6],
                    'CEP_inquiino': inquilino[0][7],
                    'Cidade_inquilino': inquilino[0][8],
                    'Estado_inquilino': inquilino[0][9],
                    'Telefone Principal_inquilino': inquilino[0][10],
                    'Telefone Residencial_inquilino': inquilino[0][11],
                    'Celular_inquilino': inquilino[0][12],
                    'E-mail_inquilino': inquilino[0][13]
                }
            return dados_inquilino
              
    else:
        dados_inquilino = {
            'Inquilino':None,
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
    pdf_path = "C:\\Users\\breno\\Downloads\\Dados\\ALLEGRO CADASTRO DE UNIDADE.pdf"

    with open(pdf_path, 'rb') as arquivo:
        reader = PyPDF2.PdfReader(arquivo)
        text = ''.join([reader.pages[page_num].extract_text() for page_num in range(len(reader.pages))])
        all_text = tratando_string(text)
    
    all_data = extair_dados(all_text)
    
    colunas = ['Bloco', 'Unidade','Rateio', 'Tipo de Pessoa Responsável',
               'Cpf_Inquilino','Inquilino', 'E-mail_inquilino','Telefone Principal_inquilino', 'Celular_inquilino', 'Telefone Residencial_inquilino','Data de entrada_inquilino', 'Data de Saída_inquilino', 
               'Logradouro_inquilino','Número', 'Complemento_inquilino', 'Bairro_inquilino', 'CEP_inquiino', 'Cidade_inquilino', 'Estado_inquilino', 
               'Tipo de Pessoa Proprietario','Cpf_proprietario','Proprietario','E-mail','Telefone Principal','Celular', 'Telefone Residencial','Data de entrada', 'Data de Saída', 
               'Logradouro','Número', 'Complemento', 'Bairro', 'CEP', 'Cidade', 'Estado']
    
    df = pd.DataFrame(all_data, columns=colunas)
    print(df)

    excel_file_path = "dados_unidades_allergo.xlsx"
    df.to_excel(excel_file_path, index=False)
    print("Arquivo exportado com sucesso.")

main()
