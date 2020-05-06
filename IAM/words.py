import pdb
import pickle
import argparse
from text_parser import word_parser
from image_loader import word_loader

argument = argparse.ArgumentParser()
argument.add_argument('--gt_path', default='/Volumes/Storage/Document_Analysis/IAM_Data/ascii/words.txt', help='Path to the text file (ascii/words.txt) containing GT information')
argument.add_argument('--image_folder', default='/Volumes/Storage/Document_Analysis/IAM_Data/words', help='Path to the folder containing word images')
argument.add_argument('--split_folder', default='/Volumes/Storage/Document_Analysis/IAM_Data/iamdb_dataset_splits/', help='Path to the text file containing train split')
args = argument.parse_args()

parser = word_parser(args.gt_path, args.split_folder)
# correct_words = parser.load_ok()
correct_words = parser.load_all()
pickle_corr_words = parser.get_pickle_words(correct=False)


word_img_loader = word_loader(args.image_folder)
train_split, test_split = parser.load_train_test_text()
image_images = word_img_loader.with_images()

def save_pickle(file_name, image_images, pickle_corr_words, train_split, test_split):
    """This function saves the pickle file for the OCR
    """
    final_pickle = {'train': [], 'test': []}

    for train_folder in train_split:
        keys_list = pickle_corr_words[train_folder]
        for key_ in keys_list:
            final_pickle['train'].append((image_images[key_], correct_words[key_]))

    for test_folder in test_split:
        keys_list = pickle_corr_words[test_folder]
        for key_ in keys_list:
            final_pickle['test'].append((image_images[key_], correct_words[key_]))

    print('[INFO] Saving {}'.format(file_name))
    with open(file_name, 'wb') as file:
        pickle.dump(final_pickle, file)


if __name__ == "__main__":
    save_pickle('/Volumes/Storage/Document_Analysis/IAM_Data/IAM_OCR.pkl', image_images, pickle_corr_words, train_split, test_split)
