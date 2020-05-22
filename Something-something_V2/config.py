# Code adapted from https://github.com/mit-han-lab/temporal-shift-module/blob/master/ops/dataset_config.py

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--root_dir', default='/Volumes/Storage/Egocentric/Datasets/Something_V2/', help='Path to the base directory')
args = parser.parse_args()


def config(modality):
    categories_filename = os.path.join(args.root_dir, 'labels/category.txt')
    if modality == 'RGB':
        root_data = args.root_dir
        train_filename = os.path.join(args.root_dir, 'labels/train_videofolder.txt')
        val_filename = os.path.join(args.root_dir, 'labels/val_videofolder.txt')
        prefix = '{:0.5d}.jpg'
    elif modality == 'Flow':
        root_data = args.root_dir
        train_filename = os.path.join(args.root_dir, 'labels/train_videofolder_flow.txt')
        val_filename = os.path.join(args.root_dir, 'labels/val_videofolder_flow.txt')
        prefix = '{:06d}-{}_{:05d}.jpg'
    else:
        raise NotImplementedError
    return categories_filename, train_filename, val_filename, root_data, prefix

if __name__ == "__main__":
    categories_filename, train_filename, val_filename, root_data, prefix = config('RGB')
    print(categories_filename, train_filename, val_filename, root_data, prefix)
