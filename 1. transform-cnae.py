import json
import csv

# Função para extrair os grupos e suas descrições
def extract_groups(data, results):
    if 'divisoes' in data:
        for div_key, div_value in data['divisoes'].items():
            if 'grupos' in div_value:
                for grp_key, grp_value in div_value['grupos'].items():
                    results.append((grp_key, grp_value['descricao']))

# Carregar o arquivo JSON
with open('cnae.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Lista para armazenar os resultados
results = []

# Iterar de 'A' a 'U'
for key in map(chr, range(ord('A'), ord('U') + 1)):
    if key in data:
        extract_groups(data[key], results)

# Salvar os resultados em um arquivo CSV
with open('grupos_descricao.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Grupo', 'Descrição'])  # Escreve o cabeçalho do CSV
    csvwriter.writerows(results)

print("Arquivo CSV criado com sucesso.")
