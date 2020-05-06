"""
This file contains the parsers for text files for words lines and sentences
"""
import os
import glob


class word_parser():
    def __init__(self, path, split_folder):
        """Initialise the word parser and load data from text file
        """
        self.path = path
        self.split_folder = split_folder
        with open(self.path, 'r') as file:
            # Not loading the initial meta-data
            self.data = file.readlines()[18:]
    
    def load_ok(self):
        """Load words with segmentation as ok
        """
        self.ok = dict()
        self.err = dict()
        for line in self.data:
            line = line.split()            
            if line[1] == 'ok':
                self.ok[line[0]] = line[-1]
            else:
                self.err[line[0]] = line[-1]
        return self.ok

    def load_all(self):
        """Load all the words without considering the segmentattion information
        """
        self.all = dict()
        for line in self.data:
            line = line.split()
            self.all[line[0]] = line[-1]
        return self.all

    def load_train_test_text(self):
            """This code gives list of train and test splits
            """
            files = glob.glob(os.path.join(self.split_folder, '*'))
            self.train_split_data = list()
            self.test_split_data = list()
            for file_name in files:
                main_file = file_name.split('/')[-1]
                if main_file in ['trainset.txt', 'validationset1.txt', 'validationset2.txt']:
                    with open(file_name, 'r') as file:
                        self.train_split_data.extend(file.readlines())
                else:
                    with open(file_name, 'r') as file:
                        self.test_split_data.extend(file.readlines())
            return [item.rstrip() for item in self.train_split_data], [item.rstrip() for item in self.test_split_data]

    def get_pickle_words(self, correct=True):
        """This code is used to generate the keys according to the split name defined in the split text files
        """
        pickle_words = dict()
        if correct:
            data = self.load_ok()
        else:
            data = self.load_all()
        for key in data.keys():
            pickle_key = '-'.join(key.split('-')[:3])
            if pickle_key not in pickle_words.keys():
                pickle_words[pickle_key] = [key]
            else:
                pickle_words[pickle_key].append(key)
        return pickle_words
