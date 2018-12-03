#! /usr/bin/python
# -*- coding:utf-8 -*-
########################################################################
#
# Copyright (c) 2018 Yang Li. All Rights Reserved
#
########################################################################

"""
File: init_param.py
Author: Yang Li
Date: 2018/11/19 20:36:31
Description: param config
"""

import os

data_param = {
    'print_debug': True,

    # path related
    'root_dir': '../',
    'img_root_dir': os.path.join(os.path.abspath('..'), "0_DATASET/origin_img"),
    'model_dir': './model',
    'data_save_dir': './data',
    'normalizer_dir': './model',

    # dataset related
    'landmark_num': 68,
    'img_width': 112,
    'img_height': 112,
    'test_size': 0.3,  # split test size
    'random_state': 0,  # split random state

    # data augment
    'balance_num': 2,
    'mode': 'gaussian',
}

occlu_param = {
    # path-related
    'model_name': 'occlu_detection.h5',

    # dataset related
    'channel': 3,
    'radius': 10,

    # dl-related
    'epochs': 100,
    'init_lr': 1e-3,
    'loss': 'binary_crossentropy',
    'bs': 64,
    'weight_path': os.path.join(os.getcwd(), "weights"),
    'weight_name': "vgg16_weights_tf_dim_ordering_tf_kernels.h5"
}

face_alignment_rough_param = {
    # path-related
    'model_name': 'face_alignment_rough.h5',

    # dataset related
    'channel': 3,

    # dl-related
    'epochs': 100,
    'init_lr': 1e-3,
    'bs': 64,
    'weight_path': os.path.join(os.getcwd(), "weights"),
    'weight_name': "vgg16_weights_tf_dim_ordering_tf_kernels.h5"
}
