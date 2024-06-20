from sentence_transformers import SentenceTransformer
import torch
from scipy.spatial.distance import cosine
import pandas as pd


model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

def get_embedding(text):
    return model.encode(text, convert_to_tensor=True)

def find_best_match(data, target_embedding):
    best_score = float('inf')
    best_match = None
    for index, row in data.iterrows():
        current_embedding = get_embedding(row['Descrição'])
        score = cosine(current_embedding.cpu().numpy(), target_embedding.cpu().numpy())
        if score < best_score:
            best_score = score
            best_match = row['Grupo']
    return best_match


cnae_data = pd.read_csv('grupos_descricao.csv')
sic_data = pd.read_csv('siccodes.csv', sep=';') 

results = []


for index, row in sic_data.iterrows():
    description_eng = row['Description']
    eng_embedding = get_embedding(description_eng)

    
    cnae_code = find_best_match(cnae_data, eng_embedding)
    if cnae_code:
        results.append({
            "CNAE": cnae_code,
            "SIC Code": row['SIC Code'],
            "Description": description_eng
        })


results_df = pd.DataFrame(results)
results_df.to_csv('cnae_sic_mapping.csv', index=False)

print("Arquivo CSV com mapeamento CNAE-SIC criado com sucesso.")
