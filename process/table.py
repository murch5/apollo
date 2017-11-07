from process.process import Process
import pandas as pd

class GroupByValue(Process):

    def do(self, data):

        delim = self.get("delim")

        if delim == True:
            data = pd.Series(data)
            data = data.str.split(";").apply(pd.Series, 1).stack()

        out = data.groupby(data).size()
        out.columns = ["Index", "GroupedCounts"]

        return out

class SubsetByIndexName(Process):

    def do(self,data):

        out = data
        axis = self.get("axis")
        subset = self.get("subset")

        if axis in ["row", "r"]:

            out = data.ix[subset]

        elif axis in ["col", "c"]:
            out = data.ix[:, subset]

        return out

class SortByIndexLabel(Process):

    def do(self,data):

        out = data
        ascending = self.get("ascending")


        out = data.sort_index(axis = 0,ascending = ascending)

        return out

class Reindex(Process):

    def do(self,data):
        out = data

        index_new = self.get("indices")

        out = data.reindex(index_new)
        return out


class Filter(Process):

    def do(self, data):

        out = data

        axis = self.get("axis")
        items = self.get("items")
        like = self.get("like")

        if items:
            out = data.filter(items = items, axis = axis)
        else:
            out = data.filter(like = like, axis = axis)

        return out