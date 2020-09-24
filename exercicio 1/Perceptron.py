# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 01:54:19 2020

@author: kelly
"""
INDEX_X1 = 0
INDEX_X2 = 1
INDEX_OUTPUT = 2

#data
padroes_1 = [[0.5, 0.8, 1], [-0.5, 0.4, 1], [0.5, -0.4, 0], [0, 0.2, 0]]
padroes_2 = [[0.5, 0.8, 1], [-0.5, 0.4, 1], [0.5, 0, 1], [0.5, -0.4, 0]]
padroes_3 = [[0.5, 1, 1], [1, 0.5, 1], [1, 1, 1], [0, 0, 0]]
padroes_4 = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]

#bias
bias = 1

#initial weights
w0 = 0.3
w1 = -0.2
w2 = -0.4
