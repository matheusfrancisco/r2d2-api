# This file will have the necessary code for bringing data from the database to the r2r2 engine
# Temporarily, it will pull data from a local database (excel sheet)

import pandas as pd
from copy import copy
from typing import List
import numpy as np
from src.input_establishments import get_establishment_data, get_establishment_genres

preprocessed_path = "./test/data_preprocessed/data-places-sp-preprocessed.xlsx"
df_genre_lists = get_establishment_genres()
genres = {
    "Gêneros Musicais": df_genre_lists["Gênero Musical: "].dropna(),
    "Gêneros Gastronômicos": df_genre_lists["Gênero Gastronomico:"].dropna(),
    "Genêro de bebidas": df_genre_lists["Gênero de Bebidas:"].dropna(),
    "Gênero de Afinidade": df_genre_lists["Gênero de Afinidade:"].dropna(),
    "Gênero de Atividades": df_genre_lists["Gênero de Atividade:"].dropna(),
}


# Encodes a list of strings containing Music, drink and food genres
# into a multi-hot vector
def encode_genre(genre_list: pd.Series, genre_type: str) -> List[np.array]:
    genre_items = list(genres[genre_type])
    all_encoded_genres = []
    # for each string containing the genres of an establishment, separate it into a list
    for genre_str in genre_list:
        encoded = np.zeros(len(genres[genre_type]))
        if type(genre_str) is not str:
            all_encoded_genres.append(encoded)
            continue
        genre_str_list = genre_str.split(', ')
        indexes = [genre_items.index(i) for i in genre_str_list]
        encoded[indexes] = 1
        all_encoded_genres.append(encoded)

    return all_encoded_genres


# Adds vectorized array of genres to dataframe
def add_genre_list(df: pd.DataFrame, genres: list) -> pd.DataFrame:
    new_df = copy(df)
    for key, value in genres.items():
        if key in df.columns:
            encoded_genre = encode_genre(genre_list=new_df[key], genre_type=key)
            encoded_genre_df = pd.DataFrame(encoded_genre, columns=genres[key], index=new_df.index)
            new_df = pd.concat([new_df, encoded_genre_df], axis=1)

    return new_df


# Removes unnecessary/unused features in data, and vectorizes establishment genres
def get_preprocessed_establishments(df: pd.DataFrame):
    df = copy(df)
    columns_todrop = ["Nome", "Telefone", "website", "Imagens (URLs)", "Observações", "Ativo (Colocar 0 para remover)"]
    indexes_todrop = df[df["Ativo (Colocar 0 para remover)"] == 0].index

    df = df.drop(index=indexes_todrop)
    df = df.drop(columns=columns_todrop)

    ignore_columns = ["Endereço", "Horário de funcionamento", "Descrição"]
    df = df.drop(columns=ignore_columns)

    df = add_genre_list(df=df, genres=genres)
    df = df.drop([key for key, value in genres.items()], axis=1)
    df = df.drop(df[df["Avaliação"] == '-'].index, axis=0)
    df = df.astype(float)

    return df


if __name__ == "__main__":
    df_test = get_establishment_data()
    get_preprocessed_establishments(df_test).to_excel(preprocessed_path, index=False)