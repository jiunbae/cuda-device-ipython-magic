from os import environ
from IPython.core.magic import Magics, magics_class, line_magic


@magics_class
class CUDADevice(Magics):

    @line_magic
    def CUDA_VISIBLE_DEVICES(self, line):
        environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
        environ["CUDA_VISIBLE_DEVICES"]=str(line)


def load_ipython_extension(ipython):
    ipython.register_magics(CUDADevice)
