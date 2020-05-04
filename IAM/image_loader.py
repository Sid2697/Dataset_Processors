"""
This file contains code for processing and loading images
"""
import os
import glob


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
