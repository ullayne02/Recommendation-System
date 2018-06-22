import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import pearsonr

class ContentFiltering:
    def __init__(self,animes):
        self.animes = animes
        self.animes.set_index('name', inplace=True)
        genres = self.animes['genre'].apply(lambda x: x.split(', '))

        dic = {}
        for i in genres:
            for j in i:
                dic[j] = 0

        columns = dic.keys()

        content_frame = pd.DataFrame(np.zeros((animes.shape[0], len(columns))),index=self.animes.index,columns=columns)

        for i,val in enumerate(genres):
            for j in val:
                content_frame.iloc[i][j] = 1


        self.content = pd.DataFrame(data=cosine_similarity(content_frame),index=self.animes.index,columns=self.animes.index)


    def top_animes(self,k,anime_index):
        return list(self.content.sort_values(by=anime_index,ascending = False).index[1:(k+1)])
