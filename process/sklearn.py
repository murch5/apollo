from process.process import Process

import sklearn as skl
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA as sk_PCA, SparsePCA as sk_sparsePCA
from sklearn.preprocessing import StandardScaler

class PCA(Process):

    def do(self, data):
        out = data

        data = data.set_index("MuiseLabID", drop=True)

        pca = sk_PCA()

        X_std = StandardScaler().fit_transform(data)

        out = pca.fit_transform(X_std)

        out = pd.DataFrame(out)
        print(out.index)
        out = out.set_index(data.index)
        print(out)

        return out


class SparsePCA(Process):

    def do(self,data):
        out = data

        data = data.set_index("MuiseLabID", drop=True)

        pca = sk_sparsePCA()

        X_std = StandardScaler().fit_transform(data)

        out = pca.fit_transform(X_std)

        out = pd.DataFrame(out)

        out = out.set_index(data.index)


        return out
