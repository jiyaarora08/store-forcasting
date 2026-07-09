def fill_missing(df, key, cols):
    """
    Fill missing values in specified columns with a given value.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to fill.
    key : any
        The value to fill missing entries with.
    cols : list of str
        Column names to apply the fill to.

    Returns
    -------
    pd.DataFrame
        DataFrame with missing values filled.
    """
    for col in cols:
        df[col] = df[col].fillna(key)
    return df