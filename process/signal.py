from process.process import Process
import scipy.fftpack as fftpack
import scipy.signal as signal
import pandas as pd
import numpy as np

class FFT(Process):

    def do(self, data):
        out = data

        out = abs(fftpack.fft(data))

        bins = np.arange(0,len(out))
        data_dict = {"x":bins,"FFT":out}
        out = pd.DataFrame(data_dict)
        out = out[["x", "FFT"]]
        return out

class FFT_2D(Process):

    def do(self, data):
        out = data

        out = abs(fftpack.fft2(data))
        print(out)
        print(out.shape)
        bins = np.arange(0,len(out))
        data_dict = {"x":bins,"FFT":out}
        out = np.log(out)
        #out = pd.DataFrame(data_dict)
       # out = out[["x", "FFT"]]
        return out


class Periodogram(Process):

    def do(self,data):
        out = data

        out = signal.periodogram(data)


        data_dict = {"fq":out[0],"PSD":out[1]}
        out = pd.DataFrame(data_dict)
        out = out[["fq","PSD"]]

        return out
