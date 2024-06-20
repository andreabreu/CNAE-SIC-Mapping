# CNAE-SIC Mapping

This repository contains a Python script for mapping CNAE (Classificação Nacional de Atividades Econômicas - National Classification of Economic Activities) codes to SIC (Standard Industrial Classification) codes based on their descriptions. The script utilizes advanced NLP (Natural Language Processing) techniques to match activity descriptions across different languages.

## How It Works

The project leverages the pre-trained SentenceTransformer model, `paraphrase-multilingual-MiniLM-L12-v2`, to generate text embeddings and compute semantic similarity between CNAE and SIC code descriptions.

## Project Structure

- `grupos_descricao.csv`: A generated CSV file containing CNAE groups and their descriptions.
- `siccodes.csv`: A CSV file containing SIC codes and their descriptions in English.
- `cnae_sic_mapping.csv`: The resulting CSV file with mappings from CNAE codes to SIC codes.
- `main.py`: The Python script that performs the mapping.

## Requirements

To run the script, you will need Python 3 and the following libraries:
- `pandas`
- `torch`
- `scipy`
- `sentence_transformers`

You can install all required dependencies with the following command:
```bash
pip install pandas torch scipy sentence-transformers
