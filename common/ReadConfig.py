import configparser
import os
def getbrowsername(name):
    cf=configparser.ConfigParser()
    cfpath=os.path.dirname(os.path.abspath('.'))+'\\config\\config.ini'
    cf.read(cfpath)
    browsername=cf.get('browser',name)
    return browsername

# print(getbrowsername('BrowserName'))