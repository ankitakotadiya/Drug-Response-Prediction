import numpy as np
import pandas as pd


def load_gene_expression_data():

    gene_exp = pd.read_csv('/content/drive/MyDrive/Cancer_Data/OmicsExpressionProteinCodingGenesTPMLogp1.csv')
    gene_exp = gene_exp.dropna()

    gene_exp = gene_exp.rename(columns={'Unnamed: 0': 'cell_line'})
    new_col = [col.split(' (')[0] for col in gene_exp.columns]
    gene_exp.columns = new_col

    return gene_exp

def load_gene_cn_data():
    gene_cn = pd.read_csv('/content/drive/MyDrive/Cancer_Data/OmicsCNGene.csv')
    gene_cn = gene_cn.dropna()

    gene_cn = gene_cn.rename(columns={'Unnamed: 0': 'cell_line'})
    cn_new_col = [col.split(' (')[0] for col in gene_cn.columns]
    gene_cn.columns = cn_new_col

    return gene_cn

def load_drug_viability_data():
    drug_viability = pd.read_csv('/content/drive/MyDrive/Cancer_Data/sanger-viability.csv')
    drug_viability = drug_viability.dropna()
    drug_viability.rename(columns={'ARXSPAN_ID': 'cell_line'}, inplace=True)

    return drug_viability
        



