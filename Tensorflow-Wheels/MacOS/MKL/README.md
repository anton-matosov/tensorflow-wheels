# MKL Optimized build

## How this Wheel was created

1. Create conda env `conda create -n mkl_tflow -y python=3.6 numpy protobuf==3.4.1`
1. Activate it `conda activate mkl_tflow`
1. Download https://github.com/intel/mkl-dnn/releases/download/v0.12/mklml_mac_2018.0.1.20171227.tgz and extract it in temporary location (e.g. `~/Downloads/mklml_mac_2018.0.1.20171227`)
1. Clone Mac ready tensorflow `git clone git@github.com:anton-matosov/tensorflow.git -b v1.5.0-mkl-mac-build tensorflow_mkl_mac`
1. Change folder `cd tensorflow_mkl_mac`
1. And build `env TF_MKL_ROOT=~/Downloads/mklml_mac_2018.0.1.20171227 bazel build --config=mkl --config=opt //tensorflow/tools/pip_package:build_pip_package`
1. Create whell `bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_mkl_mac`
1. Wheel is in `/tmp/tensorflow_mkl_mac` directory
