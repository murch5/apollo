from process.process import Process
import pandas as pd

class GroupByValue(Process):

    def do(self, data):

        delim = self.get("delim")

        #print(data.shape)
        if isinstance(data, pd.DataFrame):
            data = data.apply(pd.Series,1).stack()

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

class FilterByVal(Process):

    def do(self, data):

        out = data
        axis = self.get("axis")
        index = self.get("index")
        operator = self.get("operator")
        value = self.get("val")

        bool_string = str(index) + str(operator) + str(value)

        out = data.query(bool_string)

        return out

class SortByVal(Process):

    def do(self, data):
        out = data

        by = self.get("by")

        if self.get("axis"):
            axis = self.get("axis")
        else:
            axis = 0

        if self.get("ascending"):
            ascending = self.get("ascending")
        else:
            ascending = True

        if isinstance(data, pd.DataFrame):
            out = data.sort_values(by, axis=axis, ascending=ascending)
        elif isinstance(data, pd.Series):
            out = data.sort_values(axis=axis, ascending=ascending)

        return out

class SortByIndex(Process):

    def do(self, data):
        out = data

        if self.get("axis"):
            axis = self.get("axis")
        else:
            axis = 0

        if self.get("ascending"):
            ascending = self.get("ascending")
        else:
            ascending = True

        if isinstance(data, pd.DataFrame):
            out = data.sort_index(axis=axis, ascending=ascending)
        elif isinstance(data, pd.Series):
            out = data.sort_index(axis=axis, ascending=ascending)

        return out




class Save(Process):

    def do(self, data):
        out = data

        path = self.get("path")
        print(data)

        if not isinstance(data, pd.DataFrame):
            data = pd.DataFrame(data)

        data.to_csv(path)

        return out

class MaskIndex(Process):

    def do(self, data):
        out = data

        axis = self.get("axis")
        new_indices = pd.Series(self.get("val"))

        if axis==0:
            data.index = pd.Index(new_indices)

        return out
