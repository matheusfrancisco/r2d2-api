import pandas as pd
from app.input_user_prefs import get_user_preference_data, get_preference_categories


def get_preprocessed_user_prefs(user_id: int) -> pd.DataFrame:
    df_user_prefs = get_user_preference_data(user_id)
    df_gen, df_rat = get_preference_categories()

    genres = dict(zip(df_gen["genre"], df_gen.index))
    ratings = dict(zip(df_rat["rating"], df_rat["scale"]))

    df_user_prefs["overall_rating"] = df_user_prefs["overall_rating"].map(ratings)
    # df_user_prefs["likes"] = df_user_prefs["likes"].map(genres)
    # df_user_prefs["dislikes"] = df_user_prefs["dislikes"].map(genres)

    return df_user_prefs