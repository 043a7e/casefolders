import os
import zipfile
import shutil
from pdfminer.high_level import extract_text


username = os.getlogin()
downloadspath =  'C:/Users/' + str(username) + '/Downloads/'
for zipped in os.listdir(downloadspath):
    zippath = os.path.join(downloadspath, zipped)
    if zipfile.is_zipfile(zippath) == True:
        ctname = os.path.splitext(zipped)[0]
        casepath = ('C:/Users/' + str(username) + '/Documents/' + ctname)
        os.mkdir(casepath)
        shutil.move(zippath, casepath)
        zippath = os.path.join(casepath, zipped)
        with zipfile.ZipFile(zippath) as ziptarget:
            ziptarget.extractall(casepath)
        os.remove(zippath)
        ctpdfpath = os.path.join(casepath + '/' + ctname + '.pdf')
        cttext = extract_text(ctpdfpath)
        with open(casepath + '/' + ctname + '.txt', 'w', encoding='utf-8') as ctcopy:
            ctcopy.write(cttext)