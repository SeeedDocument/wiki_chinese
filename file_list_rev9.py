#!/usr/bin/python
#coding:utf-8
import os
import re
import string
import linecache
import shutil

#Get file name  from given directory
directoryPath = "C:\\Users\\xyu6\\Desktop\\Document\\Wiki\\SeeedDocument\\wiki_chinese"
file_extension = ".md"


#Get file name  from given directory

def productListGen(productCategory):
    urlList = []
    pattern = re.compile(productCategory)

    for fileName in os.listdir(directoryPath):
        if(fileName.endswith(file_extension)):
            with open((directoryPath + '\\docs\\' + fileName), 'r') as f:
                for eachLine in f:
                    if eachLine.find('category:') != -1:
                        category = pattern.search(eachLine, pos = 8)
                        if category:
                            #print fileName
                            fileNameNew = fileName[:-3]
                            tempurl = linecache.getline((directoryPath + '\\docs\\' + fileName), 7)
                            url = tempurl[8:]
                            url = url.strip()
                            url = "* ["+fileNameNew + "](" + url +")"
                            #print url
                            urlList.append(url)
                                        
        #print fileList
        urlListStr = '\n'.join(urlList)   
        os.chdir(directoryPath + "\\docs\\template")
        shutil.copy2((directoryPath + "\\docs\\template\\"+productCategory+".md"), directoryPath + "\\docs")
        with open(directoryPath + "\\docs\\"+productCategory+".md" , 'a') as fd:
            fd.write(urlListStr)


if __name__ == '__main__':
    for fileTemplateName in os.listdir(directoryPath+"\\docs\\template"):
        if(fileTemplateName.endswith(file_extension)):
            fileTemplateName = fileTemplateName[:-3]
            print fileTemplateName
            productListGen(fileTemplateName)
#    retval = os.getcwd()
#    print retval
#    os.chdir(directoryPath) 
#    retval = os.getcwd()
#    print retval
#    os.system("mkdocs serve")     




