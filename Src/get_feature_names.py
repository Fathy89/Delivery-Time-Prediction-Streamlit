from category_encoders import HashingEncoder


def get_feature_names(column_transformer):
    output_features = []

    for name, transformer, cols in column_transformer.transformers_:
        # Skip passthrough and drop
        if name == 'remainder':
            continue

        # Handle OneHotEncoder (category_encoders)
        if hasattr(transformer, 'get_feature_names_out'):
            output_features.extend(transformer.get_feature_names_out(cols))

        # Handle OrdinalEncoder and Scaler (same names)
        elif hasattr(transformer, 'transform'):
            output_features.extend(cols)

        # Handle HashingEncoder (no names, so create custom)
        elif isinstance(transformer, HashingEncoder):
            for i in range(transformer.n_components):
                output_features.append(f"{cols[0]}_hash_{i}")

    # Add remainder columns (passthrough)
    if column_transformer.remainder == 'passthrough':
        passthrough_indices = column_transformer._remainder[2]
        output_features.extend(passthrough_indices)

    return output_features
