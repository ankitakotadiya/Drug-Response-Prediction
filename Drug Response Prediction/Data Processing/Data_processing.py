import numpy as np
import pandas as pd
from Dataset import *

def filter_gene_expression_cn_data():
    gene_exp = load_gene_expression_data()
    gene_cn = load_gene_cn_data()

    # Filter Gene CN data so columns match with Expression data columns
    gene_exp_column_list = gene_exp.columns
    filtered_gene_cn = gene_cn.filter(items=gene_exp_column_list)

    # Same way filter Gene Expression columns with CN columns
    gene_exp = gene_exp.filter(items=filtered_gene_cn.columns)

    # Merge both the CSV files so that we could get common cell lines
    merge_exp_cn = pd.merge(gene_exp,filtered_gene_cn, on='cell_line')

    cell_line_exp_cn = merge_exp_cn['cell_line']

    # Filter gene expression cell lines
    gene_exp = gene_exp[gene_exp['cell_line'].isin(cell_line_exp_cn)]

    # Filter copy number cell lines
    filtered_gene_cn = filtered_gene_cn[filtered_gene_cn['cell_line'].isin(cell_line_exp_cn)]

    return (gene_exp, filtered_gene_cn)


def merge_gene_expression_cn():

    gene_exp, filtered_gene_cn = filter_gene_expression_cn_data()

    gene_exp.set_index('cell_line', inplace=True)
    filtered_gene_cn.set_index('cell_line', inplace=True)

    # Mean of the two DataFrames
    result_df = (gene_exp + filtered_gene_cn)/2

    # Reset index
    result_df.reset_index(inplace=True)

    return result_df