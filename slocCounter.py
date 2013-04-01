'''
Created on Mar 14, 2013
@author: Michael Collis (mcollis@seas.upenn.edu)
'''

import sys, os, csv

def main():
    args = sys.argv
    #Sets up the output file
#    outputFile = open('sloccount.csv', 'wb')
#    csvDialect = csv.excel_tab
#    csvWriter = csv.writer(outputFile, csvDialect)
    
    for inDir in os.listdir(args[1]):
        #Cycle through the files in the directory
        if 'firefox' not in inDir: continue
        print 'Running sloccount on', inDir
        stream = os.popen("sloccount "+ inDir)
        nextFlag = False
        for line in stream:
            if "SLOC-by-Language (Sorted)" in line:
                nextFlag = True
            elif nextFlag:
                print line


if __name__ == '__main__':
    main()