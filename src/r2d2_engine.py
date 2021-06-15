import pandas as pd
import numpy as np
import json
from scipy.spatial.distance import euclidean, pdist, squareform
from src.pydantic_types import *

from src.input_establishments import get_establishment_data
from src.preprocess_establishments import get_preprocessed_establishments
# from src.preprocess_user_prefs import get_preprocessed_user_prefs


def similarity_matrix(df: pd.DataFrame) -> pd.DataFrame:
    dists = pdist(df, metric='euclidean')
    df_sim = pd.DataFrame(squareform(dists), columns=df.index, index=df.index)
    return df_sim


# TODO: switch predefined establishment to user_preference
def get_ten_most_similar(df_estabs: pd.DataFrame, estab_names: pd.DataFrame, name: str) -> pd.DataFrame:
    df_sim = similarity_matrix(df_estabs)
    index = list(estab_names[estab_names == name].index).pop()
    most_similar_similarity = df_sim[index].sort_values(ascending=True).head(10).rename("Euclidian Distance")
    most_similar_indexes = most_similar_similarity.index
    most_similar = df_estabs.loc[most_similar_indexes]
    most_similar = pd.concat([estab_names[most_similar.index], most_similar_similarity, most_similar], axis=1)

    return most_similar


def suggest_some_rolês(user_id: float, answers: Immediate_user_preferences) -> json:
    df_estabs = get_preprocessed_establishments(get_establishment_data())
    estab_names = get_establishment_data()["Nome"]
    df_user_prefs = None

    df_sim = similarity_matrix(df_estabs)
    ten_most_similar = get_ten_most_similar(df_estabs=df_estabs, estab_names=estab_names, name="São Cristóvão Bar e Restaurante")

    return ten_most_similar.index


if __name__ == "__main__":
    suggest_some_rolês(None, None)
