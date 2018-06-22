import pandas as pd
import numpy as np

class Animes:
    def __init__(self):
        path = 'anime-recommendations-database/'
        self.rating = pd.read_csv(f'{path}rating.csv')
        self.animes = pd.read_csv(f'{path}anime.csv')

        self.animes.set_index('anime_id',drop=True,inplace=True)
        self.animes.dropna(inplace=True)
        self.rating.rating.replace(-1,np.nan,inplace=True)

        self.animes = self.animes[self.animes['type'] == 'TV']

        self.rating = self.rating[self.rating.user_id <= 50000]


    def get_anime(self,anime_id):
        return tuple(self.animes.loc[anime_id])

    def get_k_animes(self,k):
        return list(self.animes['name'][:k])
