# This file will have the necessary code for bringing data from the database to the r2r2 engine
# Temporarily, it will pull data from a local database (excel sheet)

# This file must output a pandas dataframe containing all the user preferences.
#TODO check all type hint in this file

import pandas as pd
from typing import Tuple


# gets the user preference data (from local database)
def get_user_preference_data(user_id: float) -> pd.DataFrame:
    db_path = "./resources/data/[mock]user-prefs.xlsx"
    df = pd.read_excel(db_path, index_col=0)
    df_user_prefs = df[df["user_id"] == user_id]

    return df_user_prefs

def get_preference_categories() -> Tuple[pd.DataFrame]:
    db_path = "./resources/data/[mock]user-prefs.xlsx"
    genres = pd.read_excel(db_path, sheet_name="Genres_id", index_col=0)
    reactions = pd.read_excel(db_path, sheet_name="Rating_id", index_col=0)

    return (genres, reactions)