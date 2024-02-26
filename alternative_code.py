import PyPDF2
import re

def extract_unit_info_from_pdf(pdf_path):
    units_info = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        unit_pattern = re.compile(r'Apartamento: (\d+)\nCoeficiente Unidade: ([\d,.]+)\nQuantidade de Moradores: \d+\n(?:Proprietário: (.+)\nCPF/CNPJ: ([\d./-]+)\n)?Data de Entrada: (\d{2}/\d{2}/\d{4})\nData de Saída: (\d{2}/\d{2}/\d{4})?\nEndereço: (.+)\nComplemento: (.+)\nBairro: (.+)\nCEP: (\d{8})\nCidade: (.+)\nEstado: (.+)\n')
        owner_pattern = re.compile(r'Proprietário: (.+)\nCPF/CNPJ: ([\d./-]+)')
        for page_num in range(num_pages):
            page_text = reader.pages[page_num].extract_text()
            print("Texto da página:", page_text)  # Depuração
            matches = unit_pattern.findall(page_text)
            print("Correspondências:", matches)  # Depuração
            for match in matches:
                unit_info = {
                    "apartamento": match[0],
                    "coeficiente_unidade": match[1],
                    "inquilinos": [],
                    "proprietarios": []
                }
                if match[2]:  # Se houver proprietário
                    owner_matches = owner_pattern.findall(page_text)
                    print("Correspondências do proprietário:", owner_matches)  # Depuração
                    for owner_match in owner_matches:
                        unit_info["proprietarios"].append({
                            "nome": owner_match[0],
                            "cpf_cnpj": owner_match[1]
                        })
                unit_info["data_entrada"] = match[3]
                unit_info["data_saida"] = match[4]
                unit_info["endereco"] = match[5]
                unit_info["complemento"] = match[6]
                unit_info["bairro"] = match[7]
                unit_info["cep"] = match[8]
                unit_info["cidade"] = match[9]
                unit_info["estado"] = match[10]
                units_info.append(unit_info)
    return units_info


pdf_path = "C:\\Users\\Pointer 01\\OneDrive - PointCondominio\\Documentos\\Importação Fator\\Cadastro de unidades\\Allegro\\ALLEGRO CADASTRO DE UNIDADE.pdf"
informacoes_unidades = extract_unit_info_from_pdf(pdf_path)
for info in informacoes_unidades:
    print(info)
