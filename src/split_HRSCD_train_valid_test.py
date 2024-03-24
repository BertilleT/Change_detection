# take path in input
# split the dataset in train, valid and test
# save the split in a file

import os
import sys
import random
import numpy as np
import pandas as pd

def split_dataset(img_path, trg_path):
    # load the RGB images form the dataset
    images = os.listdir(img_path)
    images = [x.split('.')[0] for x in images]
    print(images)
    images = np.array(images)
    np.random.shuffle(images)
    # split the dataset
    train = images[:int(0.6*len(images))]
    valid = images[int(0.6*len(images)):int(0.8*len(images))]
    test = images[int(0.8*len(images)):]
    # save the train_images in train_foler
    train_folder_images = '../data/HRSCD/train/images'
    train_folder_targets = '../data/HRSCD/train/targets'
    for image in train:
        os.rename(img_path + '/' + image + '.tif', train_folder_images + '/' + image + '.tif')
        os.rename(trg_path + '/' + image + '.tif', train_folder_targets + '/' + image + '.tif')
    # save the valid_images in valid_foler
    valid_folder_images = '../data/HRSCD/valid/images'
    valid_folder_targets = '../data/HRSCD/valid/targets'
    for image in valid:
        os.rename(img_path + '/' + image + '.tif', valid_folder_images + '/' + image + '.tif')
        os.rename(trg_path + '/' + image + '.tif', valid_folder_targets + '/' + image + '.tif')
    # save the test_images in test_foler
    test_folder_images = '../data/HRSCD/test/images'
    test_folder_targets = '../data/HRSCD/test/targets'
    for image in test:
        os.rename(img_path + '/' + image + '.tif', test_folder_images + '/' + image + '.tif')
        os.rename(trg_path + '/' + image + '.tif', test_folder_targets + '/' + image + '.tif')
    
    print('Dataset splitted in train, valid and test')
        

folder_path = '../data/HRSCD'
images_path = folder_path + '/images'
targets_path = folder_path + '/targets'

split_dataset(images_path, targets_path)
