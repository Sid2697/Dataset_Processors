"""This file downloads IAMDB data and saves in ssd_scratch
"""
import os

links = ['http://www.fki.inf.unibe.ch/DBs/iamDB/data/ascii/ascii.tgz', 'http://www.fki.inf.unibe.ch/DBs/iamDB/data/forms/formsA-D.tgz', 
'http://www.fki.inf.unibe.ch/DBs/iamDB/data/forms/formsE-H.tgz', 'http://www.fki.inf.unibe.ch/DBs/iamDB/data/forms/formsI-Z.tgz', 
'http://www.fki.inf.unibe.ch/DBs/iamDB/data/lines/lines.tgz', 'http://www.fki.inf.unibe.ch/DBs/iamDB/data/sentences/sentences.tgz', 
'http://www.fki.inf.unibe.ch/DBs/iamDB/data/words/words.tgz', 'http://www.fki.inf.unibe.ch/DBs/iamDB/data/xml/xml.tgz']

save_path = '/Volumes/Storage/Document_Analysis/IAM_Data/'
for link in links:
    print("[INFO] Downloading {}".format(link))
    command = 'wget -c --retry-connrefused --tries=0 --timeout=5 -P {} --user=sid2697 --password=9904768487 {}'.format(save_path, link)
    os.system(command)
