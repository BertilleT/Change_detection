# take path in input
# split the dataset in train, valid and test
# save the split in a file

import os
import sys
import random
import numpy as np
import pandas as pd

def split_dataset(img_path_2006, img_path_2012, trg_path):
    # load the RGB images form the dataset
    images = os.listdir(img_path_2012)
    images = [x.split('.')[0] for x in images]
    images_2006 = os.listdir(img_path_2006)
    images = np.array(images)
    np.random.shuffle(images)
    # split the dataset
    train = images[:int(0.6*len(images))]
    train_codes = [x.split('-')[2] + '-' + x.split('-')[3] for x in train]
    valid = images[int(0.6*len(images)):int(0.8*len(images))]
    valid_codes = [x.split('-')[2] + '-' + x.split('-')[3] for x in valid]
    test = images[int(0.8*len(images)):]
    test_codes = [x.split('-')[2] + '-' + x.split('-')[3] for x in test]
    # save the train_images in train_foler
    train_2006_images = '../data/HRSCD/train/images/2006'
    train_2012_images = '../data/HRSCD/train/images/2012'
    train_targets = '../data/HRSCD/train/targets'
    for i, image in enumerate(train):
        # check if if train_codes[i] is a substring of one of the elments from images_2006 and store the string containing it
        name_img_2006 = [x for x in images_2006 if train_codes[i] in x]
        os.rename(img_path_2006 + '/' + name_img_2006[0], train_2006_images + '/' + train_codes[i] + '.tif')
        # check if train_codes
        os.rename(img_path_2012 + '/' + image + '.tif', train_2012_images + '/' + train_codes[i] + '.tif')
        os.rename(trg_path + '/' + image + '.tif', train_targets + '/' + train_codes[i] + '.tif')
    # save the valid_images in valid_foler
    valid_2006_images = '../data/HRSCD/valid/images/2006'
    valid_2012_images = '../data/HRSCD/valid/images/2012'
    valid_targets = '../data/HRSCD/valid/targets'

    for i, image in enumerate(valid):
        name_img_2006 = [x for x in images_2006 if valid_codes[i] in x]
        os.rename(img_path_2006 + '/' + name_img_2006[0], valid_2006_images + '/' + valid_codes[i] + '.tif')
        os.rename(img_path_2012 + '/' + image + '.tif', valid_2012_images + '/' + valid_codes[i] + '.tif')
        os.rename(trg_path + '/' + image + '.tif', valid_targets + '/' + valid_codes[i] + '.tif')
    # save the test_images in test_foler
    test_2006_images = '../data/HRSCD/test/images/2006'
    test_2012_images = '../data/HRSCD/test/images/2012'
    test_targets = '../data/HRSCD/test/targets'

    for i, image in enumerate(test):
        name_img_2006 = [x for x in images_2006 if test_codes[i] in x]
        os.rename(img_path_2006 + '/' + name_img_2006[0], test_2006_images + '/' + test_codes[i] + '.tif')
        os.rename(img_path_2012 + '/' + image + '.tif', test_2012_images + '/' + test_codes[i] + '.tif')
        os.rename(trg_path + '/' + image + '.tif', test_targets + '/' + test_codes[i] + '.tif')
    
    print('Dataset splitted in train, valid and test')
        

folder_path = '../data/HRSCD'
images_path_2006 = folder_path + '/2006'
images_path_2012 = folder_path + '/2012'
targets_path = folder_path + '/targets'

split_dataset(images_path_2006, images_path_2012, targets_path)
