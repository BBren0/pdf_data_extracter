import re
import PyPDF2
import pandas as pd


def tratando_string(all_text):
    palavras_excluir = ["Allegro","SCI Syndkos v24.02.21.2", "Histórico de Unidades - Sem período definido\n","\n\n"]
    
    for palavra in palavras_excluir:
        all_text = re.sub(palavra,"", all_text)
    
    return all_text


def extrair_dados(data_pages):
    regex_unidade = re.compile(r'Apartamento: (\d+)')
    regex_boxs = re.compile(r'Box: (\d+)')
    regex_coeficiente = re.compile(r'Coeficiente Unidade: ([\d,.]+)')
    
    apartamentos = regex_unidade.findall(data_pages)
    boxs = regex_boxs.findall(data_pages)
    coeficientes = regex_coeficiente.findall(data_pages)
    
    all_data = []
    
    for index, apartamento in enumerate(apartamentos):
        unidade_data = {
            'Unidade': apartamento,
            'Coeficiente': coeficientes[index] if index < len(coeficientes) else None
        }
        all_data.append(unidade_data)
    
    for index, box in enumerate(boxs):
        unidade_data = {
            'Unidade': box,
            'Coeficiente': coeficientes[index + len(apartamentos)] if index < len(coeficientes) else None
        }
        all_data.append(unidade_data)
        
    return all_data


def main():
    pdf_path = "C:\\Users\\Pointer 01\\OneDrive - PointCondominio\\Documentos\\Importação Fator\\Cadastro de unidades\\Donatello\\DONATELLO CADASTRO DE UNIDADE.pdf"

    with open(pdf_path, 'rb') as arquivo:
        reader = PyPDF2.PdfReader(arquivo)
        text = ''.join([reader.pages[page_num].extract_text() for page_num in range(len(reader.pages))])
        all_text = tratando_string(text)
        print(all_text)
    all_data = extrair_dados(all_text)
    
    colunas = ['Unidade', 'Coeficiente']

    df = pd.DataFrame(all_data, columns=colunas)
    print(df)

    excel_file_path = "C:\\Users\\Pointer 01\\OneDrive - PointCondominio\\Documentos\\Importação Fator\\Cadastro de unidades\\Donatello\\Donatello_coeficiente.xlsx"
    df.to_excel(excel_file_path, index=False)
    print("Arquivo exportado com sucesso.")


main()
