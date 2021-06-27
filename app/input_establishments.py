# This file will have the necessary code for bringing data from the database to the r2r2 engine
# Temporarily, it will pull data from a local database (excel sheet)

# This file must output a pandas dataframe containing all the establishment data.
# Also, it must output a list of all possible genres (similar to the one in the local database)

import pandas as pd

db_path = "./resources/data_raw/data-places-sp.xlsm"


# gets the establishment data (from local database)
def get_establishment_data() -> pd.DataFrame:
    df_estab = pd.read_excel(db_path, index_col=0, sheet_name="Estabelecimentos")

    return df_estab


# gets list of all the possible genres
def get_establishment_genres() -> pd.DataFrame:
    df_genres = pd.read_excel(db_path, sheet_name="Listas")

    return df_genres
