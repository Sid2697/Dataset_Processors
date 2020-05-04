"""This file downloads IAMDB data and saves in ssd_scratch
"""
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--save_directory', default='/Volumes/Storage/Document_Analysis/IAM_Data/', help='Path to the folder where the downloaded data is to be saved.')
parser.add_argument('--user_id', help='User ID for downloading the data')
parser.add_argument('--password', help='Password for downloading the data')
args = parser.parse_args()

links = ['http://www.fki.inf.unibe.ch/DBs/iamDB/data/ascii/ascii.tgz', 'http://www.fki.inf.unibe.ch/DBs/iamDB/data/forms/formsA-D.tgz', 
'http://www.fki.inf.unibe.ch/DBs/iamDB/data/forms/formsE-H.tgz', 'http://www.fki.inf.unibe.ch/DBs/iamDB/data/forms/formsI-Z.tgz', 
'http://www.fki.inf.unibe.ch/DBs/iamDB/data/lines/lines.tgz', 'http://www.fki.inf.unibe.ch/DBs/iamDB/data/sentences/sentences.tgz', 
'http://www.fki.inf.unibe.ch/DBs/iamDB/data/words/words.tgz', 'http://www.fki.inf.unibe.ch/DBs/iamDB/data/xml/xml.tgz']

assert args.user_id, '[ERROR] Please provide the User ID'
assert args.password, '[ERROR] Please provide the Password'
if not os.path.exists(args.save_directory):
    print('[ERROR] The directory for saving the downloading data does not exists!\n[INFO] Please enter the correct path.')
    quit()

for link in links:
    print("[INFO] Downloading {}".format(link))
    command = 'wget -c --retry-connrefused --tries=0 --timeout=5 -P {} --user={} --password={} {}'.format(args.save_directory, args.user_id, args.password, link)
    os.system(command)
