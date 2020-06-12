# -*- coding: utf-8 -*-
# Author: Guotai Wang
# Date:   12 June, 2020
# Implementation of of COPLENet for COVID-19 pneumonia lesion segmentation from CT images.
# Reference: 
#     G. Wang et al. A Noise-robust Framework for Automatic Segmentation of COVID-19 Pneumonia Lesions 
#     from CT Images. IEEE Transactions on Medical Imaging, 2020. DOI:10.1109/TMI.2020.3000314.

from __future__ import print_function, division
import sys
import torch
from coplenet import COPLENet
from pymic.net_run.net_run import TrainInferAgent
from pymic.util.parse_config import parse_config

def main():
    if(len(sys.argv) < 2):
        print('Number of arguments should be 2. e.g.')
        print('    python net_run.py config.cfg')
        exit()
    cfg_file = str(sys.argv[1])
    config   = parse_config(cfg_file)

    # parameters of COPLENet
    net_param = {"class_num"   : 2,
                 "in_chns"     : 1,
                 "bilinear"    : True,
                 "feature_chns": [32, 64, 128, 256, 512],
                 "dropout"     : [0.0, 0.0, 0.3, 0.4, 0.5]}
    config['network'] = net_param
    
    net   = COPLENet(net_param)
    agent = TrainInferAgent(config, 'test')
    agent.set_network(net)
    agent.run()

if __name__ == "__main__":
    main()
    

