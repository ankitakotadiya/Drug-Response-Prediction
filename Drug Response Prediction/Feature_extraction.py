from sklearn.decomposition import PCA
from Data_processing import *

def extract_gene_features():
    result_df = merge_gene_expression_cn()

    data = result_df.copy()
    # Separate features from the target (if applicable)
    X = data.drop(columns=['cell_line'])
    original_columns = X.columns
    # Standardize the data
    # scaler = StandardScaler()
    # X_scaled = scaler.fit_transform(X)
    pca = PCA(n_components=1071)
    gene_pca = pca.fit_transform(X)

    # Get the explained variance ratio of each component
    explained_variance_ratio = pca.explained_variance_ratio_

    # Get the indices of components in descending order of explained variance ratio
    sorted_indices = np.argsort(-explained_variance_ratio)

    # # Get the indices of the retained and removed columns
    retained_indices = sorted_indices[:1071]  # Assuming you want to keep 100 components
    removed_indices = sorted_indices[1071:]

    # # Get the names of retained and removed columns
    retained_column_names = original_columns[retained_indices]

    gene_exp_df = pd.DataFrame(result_df.cell_line, columns=['cell_line'])
    gene_exp_df[retained_column_names] = gene_pca

    return gene_exp_df

def merge_gene_drug_data():
    gene_exp_df = extract_gene_features()
    drug_viability = load_drug_viability_data()

    gene_cell_lines = gene_exp_df['cell_line'].unique()
    merge_drug_gene_df = drug_viability[drug_viability['cell_line'].isin(gene_cell_lines)]

    filtered_data = merge_drug_gene_df[(merge_drug_gene_df['DRUG_ID'] == 1006) | (merge_drug_gene_df['DRUG_ID'] == 1372) | 
                                       (merge_drug_gene_df['DRUG_ID'] == 1004) | (merge_drug_gene_df['DRUG_ID'] == 1003) | 
                                       (merge_drug_gene_df['DRUG_ID'] == 1032) | (merge_drug_gene_df['DRUG_ID'] == 1012) | 
                                       (merge_drug_gene_df['DRUG_ID'] == 1022) | (merge_drug_gene_df['DRUG_ID'] == 1058) | 
                                       (merge_drug_gene_df['DRUG_ID'] == 1494) | (merge_drug_gene_df['DRUG_ID'] == 1057)]
    
    # Select drug features
    drug_df = filtered_data[['cell_line','DRUG_ID','dose','viability']]

    # Merge Drug-Gene data
    merge_drug_gene_df = pd.merge(drug_df, gene_exp_df, on='cell_line')

    return merge_drug_gene_df


