# This file will have the necessary code for bringing data from the database to the r2r2 engine
# Temporarily, it will pull data from a local database (excel sheet)

# This file must output a pandas dataframe containing all the user preferences.

import pandas as pd

db_path = "./test/data_raw/data-user-preferences.xlsm"

# gets the user preference data (from local database)
def get_user_preference_data(user_id: float) -> pd.DataFrame:
    df = pd.read_excel(db_path, index_col=0)
    df_user_prefs = df.loc[user_id]

    return df_user_prefs
