import PyPDF2
import pandas as pd

# Lista para armazenar as informações extraídas do PDF
data = []

# Abre o arquivo PDF em modo de leitura binária
with open("C:\Users\Pointer 01\OneDrive - PointCondominio\Documentos\Importação Fator\Cadastro de unidades\Bello Horizonte\BELO HORIZONTE CADASTRO DE UNIDADE.pdf", 'rb') as file:
    # Cria um objeto PDFReader
    reader = PyPDF2.PdfReader(file)

    # Obtém o número total de páginas no documento
    num_pages = len(reader.pages)

    # Loop através de todas as páginas e extrai o texto
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text = page.extract_text()
        
        # Adiciona o texto extraído à lista de dados
        data.append(text)
        print(text)


# Cria um DataFrame pandas com os dados
df = pd.DataFrame(data, columns=['Texto'])

# Salva o DataFrame em um arquivo Excel
df.to_excel('dados_extraidos.xlsx', index=False)
