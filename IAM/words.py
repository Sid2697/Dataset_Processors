import pdb
import argparse
from text_parser import word_parser
from image_loader import word_loader

argument = argparse.ArgumentParser()
argument.add_argument('--gt_path', default='/Volumes/Storage/Document_Analysis/IAM_Data/ascii/words.txt', help='Path to the text file (ascii/words.txt) containing GT information')
argument.add_argument('--image_folder', default='/Volumes/Storage/Document_Analysis/IAM_Data/words', help='Path to the folder containing word images')
args = argument.parse_args()

parser = word_parser(args.gt_path)
correct_words = parser.load_ok()

word_img_loader = word_loader(args.image_folder)
image_images = word_img_loader.with_images()
