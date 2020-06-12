# COPLE-Net: COVID-19 Pneumonia Lesion segmentation network
This repository provides source code and pretrained model of COPLENet for COVID-19 pneumonia lesion segmentation network proposed by G. Wang et al.[1]. If you use this code or the pretrained model, please cite the following paper:

* [1] G. Wang, X. Liu, C. Li, Z. Xu, J. Ruan, H. Zhu, T. Meng, K. Li, N. Huang, S. Zhang. 
[A Noise-robust Framework for Automatic Segmentation of COVID-19 Pneumonia Lesions from CT Images.][tmi2020] IEEE Transactions on Medical Imaging. 2020. DOI: [10.1109/TMI.2020.3000314][tmi2020]

# Requirements
* [Pytorch][torch_link] version >-1.0.1
* [PyMIC][pymic_link], a Pytorch-based toolkit for medical image computing. Install it by `pip install PYMIC`
* Some basic python packages such as Numpy, Pandas, SimpleITK.

[tmi2020]:https://ieeexplore.ieee.org/document/9109297
[torch_link]:https://pytorch.org
[pymic_link]:https://github.com/HiLab-git/PyMIC

# How to use
1. Download the pretrained model and example CT images.
2. Run `python net_run.py config/cofnig.cfg`. The results will be saved in `coplenet_data/result`.
3. To segment COVID-19 pneumonia lesions from your own images, make sure that the images have been cropped into the lung region, and the intensity has been normalized into [0, 1] using window/level of 1500/-650. Then edit `root_dir`, `test_csv` and `output_dir` in the configure file `config/cofnig.cfg` according to the path of your images. Then return to step 2 to obtain the segmentation results.
