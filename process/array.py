from process.process import Process

class Slice(Process):

    def do(self, data):

        axis = self.get("axis")
        set = self.get("slice")

        sli = [slice(None) for r in range(0, len(data.shape))]

        sli[axis] = slice(set[0], set[1] + 1, 1)

        out = data[sli]

        return out

class Squeeze(Process):

    def do(self,data):

        axis = self.get("axis")
        out = data.squeeze(axis=axis)

        return out

class Project(Process):

    def do(self,data):

        out = data
        axis = self.get("axis")
        func = self.get("function")

        if func == "var":
            out = data.var(axis=axis)
        elif func == "mean":
            out = data.mean(axis=axis)


        return out
