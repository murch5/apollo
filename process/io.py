from process.process import Process

import skimage.io as skimage_io

class Export(Process):

    def do(self, data):
        out = data

        output_file = "./output/" + self.get("file_name") + ".tif"
        skimage_io.imsave(output_file, data, plugin="tifffile")
        #logger.debug("--- Export: Save image " + self.name + ".tif")

        return out