from process.process import Process
import pandas as pd

class GroupByValue(Process):

    def do(self, data):

        delim = self.get("delim")

        if delim == True:
            data = pd.Series(data)
            data = data.str.split(";").apply(pd.Series, 1).stack()

        out = data.groupby(data.iloc[:,0]).size()
        out.columns = ["Index", "GroupedCounts"]



        return out

class SubsetByIndexName(Process):

    def do(self,data):

        out = data
        axis = self.get("axis")
        subset = self.get("subset")

        if axis in ["col", "c"]:
            out = data.ix[subset]
        elif axis in ["row", "r"]:
            out = data.ix[:, subset]

        return out