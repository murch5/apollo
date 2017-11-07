from process.process import Process

import skimage.morphology as morph
import skimage.measure as measure
import pandas as pd

class Skeletonize(Process):

    def do(self, data):
        out = data

        out = morph.skeletonize(data)

        return out


class LabelRegions(Process):

    def do(self,data):
        out = data

        labelled_regions = measure.label(data)

        regions_properties = measure.regionprops(labelled_regions)

        regions_list = [region.bbox for region in regions_properties]

        regions_list = pd.DataFrame(regions_list)

        regions_list.to_csv("process/regions.csv", header=None,index=False)

        out = data

        return out