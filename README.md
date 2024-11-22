# TDP-M3D

This is the official implementation of "Twin Depth Perception for Robust Monocular 3D Object Detection in Adverse Conditions".

Download the KITTI dataset from [KITTI website](http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d), including left color images, camera calibration matrices and training labels.

Clone this project and then go to the code directory:

    git clone https://github.com/jaysonju/TDP-M3D.git
    cd code

We train the model on the following environments:

    Python 3.6
    Pytorch 1.1
    Cuda 9.0

You can build the environment easily by installing the requirements:

    conda env create -f requirements.yml
    conda activate MonoTDP

Train the model:

    CUDA_VISIBLE_DEVICES=0,1,2,3 python tools/train_val.py

Evaluation:

    CUDA_VISIBLE_DEVICES=0,1,2,3 python tools/train_val.py -e

Citation
    
    If you find our work useful in your research, please consider citing:
