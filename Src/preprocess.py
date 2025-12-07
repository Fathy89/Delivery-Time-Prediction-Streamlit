from category_encoders import HashingEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer

def preprocessor(min_max_col=None,standard_column=None,robust_col=None ,
                col_to_one_hot_Encoding=None, col_to_label_Encoding=None,
                col_to_hash_Ecnoding=None, n_hash=4):

    # Choose scaler (even though for XGBoost you might just passthrough)
    
    
    # Build transformers list safely
    transformers = []

    # Only add numeric scaling if columns are provided
    if min_max_col is not None and len(min_max_col) > 0:
        transformers.append(('Scaling_Min_Max', MinMaxScaler(), min_max_col))
    
    if standard_column is not None and len(standard_column) > 0:
        transformers.append(('Scaling_Standard', StandardScaler(), standard_column))
    
    if robust_col is not None and len(robust_col) > 0:
        transformers.append(('Scaling_Roubust', RobustScaler(), robust_col))
    # Add categorical transformers if provide
    if col_to_one_hot_Encoding is not None and len(col_to_one_hot_Encoding) > 0:
        transformers.append(('One Hot', OneHotEncoder(handle_unknown='ignore'), col_to_one_hot_Encoding))
    
    if col_to_label_Encoding is not None and len(col_to_label_Encoding) > 0:
        transformers.append(('Ordinal', OrdinalEncoder(), col_to_label_Encoding))
    
    if col_to_hash_Ecnoding is not None and len(col_to_hash_Ecnoding) > 0:
        transformers.append(('Hash', HashingEncoder(n_components=n_hash), col_to_hash_Ecnoding))
    
    pre = ColumnTransformer(
        transformers=transformers,
        remainder='passthrough'  )

    return pre
