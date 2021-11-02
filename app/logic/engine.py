try:
    import unzip_requirements
except ImportError:
    Exception("there was a problem with imports")
import pandas as pd
import numpy as np
import json
from scipy.spatial.distance import euclidean, pdist, squareform
from app.models.models import *

from app.logic.users.preprocessing import get_preprocessed_user_prefs
from app.logic.establishments.preprocessing import get_preprocessed_establishments, get_preprocessed_establisment_categories

#these functions have type hints, check all of them

#TODO write test to all this functions
# get the similarity matrix between the user vector and all the establishments
def similarity_matrix(df: pd.DataFrame) -> pd.DataFrame:
    # dists = pdist(df, metric='euclidean')
    dists = pdist(df, metric='cosine')
    df_sim = pd.DataFrame(squareform(dists), columns=df.index, index=df.index)

    return df_sim


# get the ten most similar establishments given a user preference vector
def get_ten_most_similar(df_estabs: pd.DataFrame, user_vector: pd.Series) -> pd.DataFrame:
    index = user_vector.name
    df_estabs_with_usrvector = df_estabs.append(user_vector)

    df_sim = similarity_matrix(df_estabs_with_usrvector)
    most_similar = df_sim[index].sort_values(ascending=True)
    most_similar = most_similar.head(11)[1:]

    return most_similar


# returns the user preference vector (for explanation please view r2d2 explanation google doc)
def get_user_vector(df_user_prefs: pd.DataFrame, df_estabs: pd.DataFrame, estab_categories: dict) -> pd.Series:
    df_estabs_user_prefs = df_user_prefs.join(df_estabs, on="establishment_id")
    df_estabs_user_prefs = df_estabs_user_prefs.drop(["user_id", "establishment_id"], axis=1)

    # vectors that will contain each rating, condensing overall rating, liked category and disliked category
    user_vectors = pd.DataFrame(columns=df_estabs_user_prefs.drop(["overall_rating", "likes", "dislikes"], axis=1).columns)

    for ind in df_estabs_user_prefs.index:               # iterate over a single rating of a user
        rating_vector = df_estabs_user_prefs.loc[ind]    # vector that contains this rating's values AND this establishment's characteristics
        base_vector = rating_vector.drop(["overall_rating", "likes", "dislikes"])   # vector that contains the establishment's characteristics
        overall_rating, like, dislike = rating_vector["overall_rating"], rating_vector["likes"], rating_vector["dislikes"]  # values of this rating

        overall_rating_vector = base_vector.mul(overall_rating, axis=0)                 # vector of the overall rating
        like_vector = base_vector[estab_categories[like]].apply(lambda x: x * 0.3)        # vector of the liked category
        dislike_vector = base_vector[estab_categories[dislike]].apply(lambda x: x * -0.3)  # vector of the disliked category

        all_ratings_vector = pd.concat([overall_rating_vector, like_vector, dislike_vector], axis=1)    # concatenates overall, liked and disliked into a dataframe
        all_ratings_vector = all_ratings_vector.fillna(0)
        all_ratings_vector = all_ratings_vector.sum(axis=1).rename(ind)     # sums the values of overall rating, liked and disliked into a series, which is one user vector
        all_ratings_vector = all_ratings_vector.clip(-1, 1)

        user_vectors = user_vectors.append(all_ratings_vector)      # appends this user vector (one rating from this user) to a dataframe with all user vectors

    user_vector = user_vectors.mean(axis=0).round(3)    # takes average of all user rating vectors to get the final user vector
    return user_vector


# get the establishment recommendations given a user ordered by relevance (descending)
def recommendations(user_id: float, answers: Answers) -> List[str]:
    # TODO: implement the user answer in the recommendation engine

    df_estabs = get_preprocessed_establishments()
    dict_categs = get_preprocessed_establisment_categories()
    df_user_prefs = get_preprocessed_user_prefs(user_id)

    user_vector = get_user_vector(df_user_prefs, df_estabs, dict_categs)
    user_vector = user_vector.rename(f"User_{user_id}_vector")
    # print(user_vector)

    ten_most_similar = get_ten_most_similar(df_estabs=df_estabs, user_vector=user_vector)
    ten_most_similar = list(ten_most_similar.index)

    return ten_most_similar

