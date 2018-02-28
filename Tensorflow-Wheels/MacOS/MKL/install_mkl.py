import os
import pathlib
from distutils.sysconfig import get_python_lib
import shutil
from io import BytesIO
from zipfile import ZipFile
import tarfile
from urllib.request import urlopen

"""
This script installs MKL dylibs.

Usage 1.
Install from local copy
TF_MKL_ROOT=~/Downloads/mklml_mac_2018.0.1.20171227 python install_mkl.py

Usage 2.
Install from bundled zip (requires internet connection)

python install_mkl.py

Usage 3.
Install from zip, local or remote
TF_MKL_ROOT=<URL or Path to zip> python install_mkl.py

"""

def download_and_install(url, destFolder):
  with urlopen(url) as response, ZipFile(BytesIO(response.read())) as zipfile:
    extractZipfile(zipfile, destFolder)

def extractZipfile(zipfile, destFolder):
  for zipInfo in zipfile.infolist():
    zippedfilePath = pathlib.Path(zipInfo.filename)
    if zippedfilePath.suffix == ".dylib" and not zipInfo.filename.startswith("__MACOSX"):
      zipInfo.filename = zippedfilePath.name
      zipfile.extract(zipInfo, destFolder)
      print("Extracted:", zippedfilePath)

def copy_dylibs(sourceFolder, destFolder):
  srcPath = sourceFolder + "/lib/"
  srcPath = os.path.expanduser(os.path.expandvars(srcPath))

  for file in ["libmklml.dylib", "libiomp5.dylib"]:
    shutil.copyfile(srcPath + file, destFolder + file)
    print("Copied ", file)


# Dummy zip with 0 size dylibs (for debugging)
# downloadURL = "https://github.com/anton-matosov/tensorflow-wheels/raw/e932cff97113bb22af9fd8c5830be55277bf37a9/Tensorflow-Wheels/MacOS/MKL/dummy/mkl-lib.zip"

# MKL copy used to build the wheel
downloadURL = "https://github.com/anton-matosov/tensorflow-wheels/raw/master/Tensorflow-Wheels/MacOS/MKL/mkl-lib.zip"

mklRoot = os.environ.get('TF_MKL_ROOT') or downloadURL

mklFileExt = pathlib.Path(mklRoot).suffix
isZip = mklFileExt == ".zip"
isTar = mklFileExt == ".tgz"
isURL = mklRoot.startswith("http://") or mklRoot.startswith("https://")

tfPkg = get_python_lib() + "/tensorflow/"

if isZip and isURL:
  print("Downloading MKL from:", mklRoot)
  download_and_install(mklRoot, tfPkg)
elif isZip and not isURL:
  print("Extracting MKL from:", mklRoot)
  srcPath = os.path.expanduser(os.path.expandvars(mklRoot))
  with ZipFile(srcPath, 'r') as zipfile:
    extractZipfile(zipfile, tfPkg)
# elif isTar and not isURL:
#   print("Extracting MKL from:", mklRoot)
#   srcPath = os.path.expanduser(os.path.expandvars(mklRoot))
#   with tarfile.open(srcPath, 'r:*') as zipfile:
#     extractZipfile(zipfile, tfPkg)
elif not isZip and not isURL:
  print("Copying MKL from:", mklRoot)
  copy_dylibs(mklRoot, tfPkg)

print("MKL Installed successfully to ", tfPkg)
