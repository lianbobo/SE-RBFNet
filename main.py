# -*- coding: utf-8 -*-
import sys
sys.path.append('./apps')
import SERBFNet 
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


if __name__ == '__main__':
    file = 'DATA/Armadillo.ply'
    sample_num = 40000
    batch_size = 10000
    save_path = 'results'
    seed = 0
    SERBFNet.SE_RBFNet(file, sample_num, batch_size, save_path, seed=seed)
