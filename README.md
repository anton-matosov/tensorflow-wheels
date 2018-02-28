# Tensorflow Wheels
This repo contains pre-build Tensrflow and friends python wheels for various configurations 

## MacOS + MKL

This is not the final wheel and requires a bit of manual setup.
This wheel depends on [Intel's MKL-DNN](https://github.com/intel/mkl-dnn) which needs to be installed either globally in your system (The standard locations for dynamic libraries are ~/lib, /usr/local/lib, and /usr/lib) or inside the site-packages/tensorflow.

This wheel was built with Conda's Intel MKL optimized numpy and C++ version of protobuf. I have tested this wheel only in the following configuration

1. Create conda env `conda create -n mkl_tflow -y python=3.6 numpy protobuf==3.4.1`
1. Activate it `conda activate mkl_tflow`
1. Install Tensorflow from  wheel `pip install https://github.com/anton-matosov/tensorflow-wheels/raw/master/Tensorflow-Wheels/MacOS/MKL/tensorflow-1.5.0-cp36-cp36m-macosx_10_7_x86_64.whl`
1. Download https://github.com/intel/mkl-dnn/releases/download/v0.12/mklml_mac_2018.0.1.20171227.tgz and extract it in temporary location
1. Install `libmklml.dylib` and `libiomp5.dylib` into the library search path (e.g. `~/lib`) or into your tensorflow's site-package folder `~/miniconda3/envs/mkl_tflow/lib/python3.6/site-packages/tensroflow` (you can get site-package path by running `python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`).<br />You can use `install_mkl.py` script for this. Make sure to run it within the target conda env. This command will download and run the script: `curl https://raw.githubusercontent.com/anton-matosov/tensorflow-wheels/master/Tensorflow-Wheels/MacOS/MKL/install_mkl.py | python -`
1. Check that it all works by running `python -c "import tensorflow as tf`"
1. For maximum performance with MKL build you have to tweek environment variables for your specific CPU. Please refer to [Optimizing for CPU - TensorFlow with Intel® MKL DNN](https://www.tensorflow.org/performance/performance_guide#tensorflow_with_intel_mkl_dnn) page for details.
<br />Make sure to read main [Optimizing for CPU](https://www.tensorflow.org/performance/performance_guide#optimizing_for_cpu)as well. Fine tuning for your CPU is simple and always gives performance boost. In my case it was additional 1.5x on top of 4x provided by MKL, which is **6x total** compared to naive CPU setup.


That's it, Enjoy AI!
