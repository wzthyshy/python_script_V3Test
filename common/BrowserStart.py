from common.ReadConfig import getbrowsername

import os
def BrowserStart():
    getbrowsername=getbrowsername('BrowserName')
    url=getbrowsername('Url')