"""
This file is used to download the Something something dataset
"""
import os
import argparse
import multiprocessing

parser = argparse.ArgumentParser()
parser.add_argument('--dest', default='/Volumes/Storage/Egocentric/Datasets/Something_V2', help='Path to the destination folder')
parser.add_argument('--parallel', default=True, help='Use parallel downloading')
args = parser.parse_args()
print(args)

links = list() # Add links from https://20bn.com/datasets/something-something/v2

for count, link in enumerate(links):
    print('[INFO] Link number {}'.format(count))
    if args.parallel:
        command = "axel -n 8 -o {} '{}'".format(args.dest, link)
    else:
        command = "wget -c --retry-connrefused --tries=0 --no-check-certificate --no-proxy --timeout=5 -P {} '{}'".format(args.dest, link)
    os.system(command)

print('[INFO] Files downloaded!')
