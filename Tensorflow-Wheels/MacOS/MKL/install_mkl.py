import os
from distutils.sysconfig import get_python_lib
import shutil

"""
env TF_MKL_ROOT=~/Downloads/mklml_mac_2018.0.1.20171227 python install_mkl.py
"""

tfPkg = get_python_lib() + "/tensorflow/"

srcPath = os.environ.get('TF_MKL_ROOT') + "/lib/"
srcPath = os.path.expanduser(os.path.expandvars(srcPath))

for file in ["libmklml.dylib", "libiomp5.dylib"]:
  shutil.copyfile(srcPath + file, tfPkg + file)
  print("Copied ", file)

print("MKL Installed successfully to ", tfPkg)