#! /usr/bin/env python3 

from operator import itemgetter

class getTop3FileName():

    def __init__(self,urllist):
        self.URLList = urllist

    def getTop3FileName(self):
        FileNameDict = {}
        for i in self.URLList :
            FileName = i.split("/")[-1]
            if FileName not in FileNameDict:
                FileNameDict[FileName] = 1
            else :
                FileNameDict[FileName] += 1
        SortedFileName = sorted(FileNameDict.items(),key=itemgetter(1),reverse=True)
        for i in range(3) :
            print (SortedFileName[i][0],(SortedFileName[i][1]))
                





if __name__ == "__main__":
    URLList = [
            "http://www.google.com/a.txt",
            "http://www.google.com.tw/a.txt",
            "http://www.google.com/download/c.jpg",
            "http://www.google.co.jp/a.txt",
            "http://www.google.com/b.txt",
            "https://facebook.com/movie/b.txt",
            "http://yahoo.com/123/000/c.jpg",
            "http://gliacoud.com/haha.png"
    ]
    myGetTop3FileName=getTop3FileName(URLList)
    myGetTop3FileName.getTop3FileName()
