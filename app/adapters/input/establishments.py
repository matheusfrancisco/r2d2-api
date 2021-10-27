# This file will have the necessary code for bringing data from the database to the r2r2 engine
# Temporarily, it will pull data from a local database (excel sheet)

# This file must output a pandas dataframe containing all the establishment data.
# Also, it must output a list of all possible genres (similar to the one in the local database)

import pandas as pd

# gets the establishment data (from local database)
def get_establishments() -> pd.DataFrame:
    db_path = "./resources/data/[mock]establishments.xlsx"
    df_estab = pd.read_excel(db_path, index_col=0, sheet_name="establishments")

    return df_estab


def get_establishment_categories() -> pd.DataFrame:
    db_path = "./resources/data/[mock]establishments.xlsx"
    df_genres = pd.read_excel(db_path, sheet_name="characteristics_categories")

    return df_genres
