"""
This file contains code for processing and loading images
"""
import os
import cv2
import glob
import numpy as np
from tqdm import tqdm


class word_loader():
    def __init__(self, path):
        self.path = os.path.join(path, '*')
        self.level_1 = glob.glob(self.path)
        self.level_2 = dict()
        for folder in self.level_1:
            self.level_2[folder.split('/')[-1]] = glob.glob(os.path.join(folder, '*'))
        self.level_3 = dict()
        for value in self.level_2.values():
            for image_folder in value:
                self.level_3[image_folder.split('/')[-1]] = glob.glob(os.path.join(image_folder, '*'))
        self.final = dict()
        for all_paths in self.level_3.values():
            for ind_path in all_paths:
                word_img_id = ind_path.split('/')[-1].split('.')[0]
                self.final[word_img_id] = ind_path

    def img_paths(self):
        return self.final
    
    def load_image(self, image_path, height=32):
        try:
            img = cv2.imread(image_path)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ratio = height/img_gray.shape[0]
            img_resized = cv2.resize(img_gray, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_CUBIC)
            _, img_thresh = cv2.threshold(img_resized, 0, 1, cv2.THRESH_OTSU)
        except:
            # There are 2 corrupted images in the data.
            return np.zeros((32, 100))
        return img_thresh

    def with_images(self):
        self.image_dict = dict()
        for key, value in tqdm(self.final.items(), desc='Loading Images '):
            self.image_dict[key] = self.load_image(value)
        return self.image_dict
