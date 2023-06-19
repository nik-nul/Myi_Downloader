import pandas as pd
import os
import json
import re
import wget

w = os.getcwd()
dirList = os.listdir()
pre = '^user\_class\_.*'
http = re.compile('http://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
title = re.compile('\'title\':([^},]+)')
ext = re.compile('\'ext\':([^},]+)')

def down(ln):
    with open(ln) as f:
        df = json.load(f)
    df = pd.json_normalize(df)
    dfr = df['file_resources']
    l = len(df)
    if not os.path.exists('data'):
       os.mkdir('data')
    for i in range(l):
     #   os.chdir('./data/'+df['numberSubject'][i])
        os.chdir('./data/')
        nameSubject = str(df['subject'][i])
        if not os.path.exists(nameSubject):
            os.mkdir(nameSubject)
        os.chdir(nameSubject)
        dat = df['date'][i]
        if not isinstance(dat,str):
            dat = 'Unknowndat'
        titl = df['title'][i]
        if not isinstance(titl,str):
            titl = 'Unknowntitl'
        grName = str(dat[0:10] + ' ' + titl)
        if not os.path.exists(grName):
           os.mkdir(grName)
        os.chdir(grName)
        tmpGetTitle = title.findall(str(dfr[i]))
        tmpGetUrl = http.findall(str(dfr[i]))
        tmpGetExt = ext.findall(str(dfr[i]))
        s = len(tmpGetTitle)
        for j in range(s):
            tmpName = str(tmpGetTitle[j][2:-1] + '.' + tmpGetExt[j][2:-1])
            if not os.path.exists(tmpName):
                wget.download(tmpGetUrl[j],tmpName)
                print()
                print(df['title'][i],'/',tmpName,'Download Completed')
        print(i+1,'/',l,'GResource',df['title'][i],'Download Completed')
        os.chdir(w)
    print(ln,'Completed!')

for k in range(len(dirList)):
    if re.match(pre,dirList[k]):
        print('Now downloading',dirList[k],'...')
        down(dirList[k])
print('Downloading All Completed')