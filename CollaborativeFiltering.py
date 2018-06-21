import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split




class CollaborativeFiltering:
    def __init__(self, animes, rating):
        self.animes = animes
        self.rating = rating
        df = self.animes.merge(self.rating, on='anime_id', suffixes=('_anime', '_user'))

        pvt = pd.pivot_table(df,index='user_id',columns='name',values='rating_user')
        colunas = list(pvt)
        pvt.fillna(0,inplace=True)

        cosine_item_based = cosine_similarity(pvt.T)
        self.item_based = pd.DataFrame(data=cosine_item_based,index=pvt.columns,columns=pvt.columns)


    def top_animes(self,k,anime_index):
        return list(self.item_based.sort_values(by=anime_index,ascending = False).index[1:(k+1)])
