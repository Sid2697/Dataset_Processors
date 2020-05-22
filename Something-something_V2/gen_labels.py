"""
This code is used for 
"""
import os
import pdb
import json
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--frames', default='/Volumes/Storage/Egocentric/Datasets/Something_V2/frames', help='Path to the directory containing all the frames')
parser.add_argument('--labels', default='/Volumes/Storage/Egocentric/Datasets/Something_V2/labels', help='Path to the files containing labels')
args = parser.parse_args()
print(args)

input_files = [os.path.join(args.labels, item) for item in ['something-something-v2-validation.json', 'something-something-v2-train.json', 'something-something-v2-test.json']]
output_files = [os.path.join(args.labels, item) for item in ['val_videofolder.txt', 'train_videofolder.txt', 'test_videofolder.txt']]
with open(os.path.join(args.labels, 'something-something-v2-labels.json')) as file:
    labels = json.load(file)
categories = []
for i, (cat, idx) in enumerate(labels.items()):
    assert i == int(idx)
    categories.append(cat)
category_path = os.path.join(args.labels, 'category.txt')

if not os.path.exists(category_path):
    with open(category_path, 'w') as file:
        file.write('\n'.join(categories))
else:
    raise ValueError('[INFO] {} exists'.format(category_path))

if os.path.exists(output_files[0]):
    raise ValueError('[INFO] {} exists'.format(output_files[0]))

for (input_file, output_file) in zip(input_files, output_files):
    with open(input_file) as file:
        data = json.load(file)
    folders = list()
    idx_categories = list()
    for item in data:
        folders.append(item['id'])
        if 'test' not in input_file:
            idx_categories.append(labels[item['template'].replace('[', '').replace(']', '')])
        else:
            idx_categories.append(0)
    # pdb.set_trace()
    output = []
    for i in tqdm(range(len(folders))):
        current_folder = folders[i]
        current_idx = idx_categories[i]
        dir_files = os.listdir(os.path.join(args.frames, current_folder))
        output.append('{} {} {}'.format(current_folder, len(dir_files), current_idx))
    with open(output_file, 'w') as file:
        file.write('\n'.join(output))
