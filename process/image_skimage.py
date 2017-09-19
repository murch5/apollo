from process.process import Process

import skimage.morphology as morph


class Skeletonize(Process):

    def do(self, data):
        out = data

        out = morph.skeletonize(data)

        return out