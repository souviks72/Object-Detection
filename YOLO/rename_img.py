# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:21:07 2020

@author: Souvik M
"""


import os

imdir = 'images'
if not os.path.isdir(imdir):
    os.mkdir(imdir)

fidget_folders = [folder for folder in os.listdir('.') if 'fidget' in folder]

n = 0
for folder in fidget_folders:
    for imfile in os.scandir(folder):
        os.rename(imfile.path, os.path.join(imdir, '{:06}.png'.format(n)))
        n += 1