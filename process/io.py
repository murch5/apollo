from process.process import Process

import skimage.io as skimage_io
import skimage.external.tifffile as tff

class Export(Process):

    def do(self, data):
        out = data

        output_file = "./output/" + self.get("file_name") + ".tif"
        #skimage_io.imsave(output_file, data, plugin="tifffile")
        #logger.debug("--- Export: Save image " + self.name + ".tif")

        with tff.TiffWriter(output_file) as tif:
            tif.save(out)

        return out