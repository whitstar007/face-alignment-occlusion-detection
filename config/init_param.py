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
    'img_root_dir': os.path.join(os.path.abspath('..'), '0_DATASET/origin_img'),
    'model_dir': './model',
    'data_save_dir': './data',
    'normalizer_dir': './model',
    'record_dir': './record',

    # dataset related
    'landmark_num': 68,
    'channel': 3,
    'img_size': 112,
    'test_size': 0.3,  # split test size
    'random_state': 0,  # split random state

    # data augment
    'balance_num': 2,
    'mode': 'gaussian',
}

face_alignment_rough_param = {
    # path-related
    'model_name': 'face_alignment_rough.h5',

    # dl-related
    'epochs': 100,
    'init_lr': 1e-3,
    'bs': 64,
    'weight_path': os.path.join(os.getcwd(), 'weights'),
    'weight_name': 'vgg16_weights_tf_dim_ordering_tf_kernels.h5'
}

occlu_param = {
    # path-related
    'model_name': 'occlu_detection.h5',

    # dataset related
    'radius': 10,

    # dl-related
    'epochs': 100,
    'init_lr': 1e-3,
    'loss': 'binary_crossentropy',
    'bs': 64,
    'weight_path': os.path.join(os.getcwd(), 'weights'),
    'weight_name': 'vgg16_weights_tf_dim_ordering_tf_kernels.h5'
}

face_alignment_precise_param = {
    # path-related
    'model_name': 'face_alignment_precise.h5',

    # dl-related
    'epochs': 100,
    'init_lr': 1e-3,
    'bs': 64,
}
