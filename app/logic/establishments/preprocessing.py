try:
    import unzip_requirements
except ImportError:
    Exception("there was a problem with imports")
# This file will have the necessary code for bringing data from the database to the r2r2 engine
# Temporarily, it will pull data from a local database (excel sheet)
#TODO check all type hint in this file
#TODO write test to all this functions

import pandas as pd
from copy import copy
from typing import List
import numpy as np
from collections import defaultdict
from app.adapters.input.establishments import get_establishments, get_establishment_categories


def get_preprocessed_establishments() -> pd.DataFrame:
    df = get_establishments()
    return df


def get_preprocessed_establisment_categories() -> pd.DataFrame:
    df_cats = get_establishment_categories()
    categories = defaultdict(list)
    for characteristic, category in zip(df_cats["name_characteristic"], df_cats["name_category"]):
        categories[category].append(characteristic)

    return categories


#if __name__ == "__main__":
#    print(get_preprocessed_establisment_categories())
