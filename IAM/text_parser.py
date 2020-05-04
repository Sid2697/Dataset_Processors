"""
This file contains the parsers for text files for words lines and sentences
"""
class word_parser():
    def __init__(self, path):
        """Initialise the word parser and load data from text file
        """
        self.path = path
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
