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
from pymic.util.parse_config import parse_config
from pymic.net_run.net_run_agent import  NetRunAgent
from pymic.net.net_dict import NetDict
from coplenet import COPLENet

my_net_dict = NetDict
my_net_dict['COPLENet'] = COPLENet

def main():
    if(len(sys.argv) < 3):
        print('Number of arguments should be 3. e.g.')
        print('    python train_infer.py train config.cfg')
        exit()
    cfg_file = str(sys.argv[1])
    config   = parse_config(cfg_file)

    stage    = str(sys.argv[1])
    cfg_file = str(sys.argv[2])
    config   = parse_config(cfg_file)

    # use custormized CNN and loss function
    agent  = NetRunAgent(config, stage)
    agent.set_network_dict(my_net_dict)
    agent.run()

if __name__ == "__main__":
    main()
    

