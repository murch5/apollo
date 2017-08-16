from process.process import Process
import scipy.ndimage.interpolation as interpolation
import numpy as np
import pandas as pd
import logging as logging

class Slice(Process):

    def do(self, data):

        logging.debug("------ Slice: shape: " + str(data.shape) + " , type: " + str(type(data)))

        if isinstance(data,pd.DataFrame):
            data = data.as_matrix()
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

class Retype(Process):

    def do(self,data):
        out = data

        type = self.get("type")

        out= data.astype(type)


        return out

class Transect(Process):

    def do(self,data):
        out = data

        mode = self.get("mode")
        axis_one = self.get("axis_one")
        axis_two = self.get("axis_two")
        line_start = self.get("line_start")
        line_end = self.get("line_end")

        dist = self.get("dist")

        x = np.linspace(line_start[0],line_end[0],dist)
        y = np.linspace(line_start[1], line_end[1], dist)

        val_index = np.arange(0,dist)

        project = self.get("project")

        if project:
            data_accum = []
            for i,slice in enumerate(data):
                slice_interpolate = interpolation.map_coordinates(slice.T, np.stack((x, y)))
                data_accum.append(slice_interpolate)
            val = pd.DataFrame(data_accum)

        else:
            val_interpolate = interpolation.map_coordinates(data.T, np.stack((x, y)))
            val = {"index": val_index, "value": val_interpolate}

        out = val

        return out