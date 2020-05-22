"""
This file is used for extracting frames from videos
Code adapted from: https://github.com/mit-han-lab/temporal-shift-module/blob/master/tools/vid2img_sthv2.py
"""
import os
import pdb
import argparse
import threading
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--videos', default='/Volumes/Storage/Egocentric/Datasets/Something_V2/videos')
parser.add_argument('--frames', default='/Volumes/Storage/Egocentric/Datasets/Something_V2/frames')
parser.add_argument('--num_threads', default=50, type=int, help='Number of threads')
args = parser.parse_args()


def split(videos_list, num_threads):
    for i in range(0, len(videos_list), num_threads):
        yield videos_list[i: i + num_threads]


def extract(video):
    video_path = os.path.join(args.videos, video)
    frame_path = os.path.join(args.frames, video[:-5])
    command = 'ffmpeg -hide_banner -loglevel panic -i \"{}\" -threads 1 -vf scale=-1:256 -q:v 0 \"{}/%06d.jpg\"'.format(video_path, frame_path)
    os.system(command)


def target(videos_list):
    for video in videos_list:
        os.mkdir(os.path.join(args.frames, video[:-5]))
        extract(video)


if __name__ == "__main__":
    if not os.path.exists(args.videos):
        raise ValueError('[ERROR] Download Something-something dataset and set the path as --videos path')
    if not os.path.exists(args.frames):
        os.mkdir(args.frames)

    videos_list = os.listdir(args.videos)
    splits = list(split(videos_list, args.num_threads))
    print('[INFO] Length of splits is {}'.format(len(splits)))

    threads = list()
    for i, split_ in enumerate(tqdm(splits, desc='Processing videos')):
        thread = threading.Thread(target=target, args=(split_,))
        thread.start()
        threads.append(thread)
    
    for thread in tqdm(threads, desc='Ending Threads'):
        thread.join()
