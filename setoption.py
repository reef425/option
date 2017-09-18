'''
Created on Sep 18, 2017

@author: reef425
'''

import time
import json
filename = "option.ini"

  


def readFile(filename):
    data = []
    while(True):
        try:
            with open(filename,"r") as f:
                try:
                    data=json.loads(f.read())
                except:
                    data = None
        except:
            data = None
        finally:
            print(data)
        time.sleep(10)
    

if __name__ == '__main__':
    readFile(filename)
