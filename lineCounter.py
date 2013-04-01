'''
Created on Mar 14, 2013
@author: Michael Collis (mcollis@seas.upenn.edu)
'''

import sys, os, csv

def main():
    args = sys.argv
    #Set up the output file
    outputFile = open('lineCount.csv', 'wb')
    csvDialect = csv.excel_tab
    csvWriter = csv.writer(outputFile, csvDialect)
    csvWriter.writerow(["Dir1\tDir2\tCount Type\tFiles Changed\tDir2 Lines Added\tDir1 Lines Removed\tTotal Lines Changed\tFiles only in Dir2"])

    for infilename in os.listdir(args[1]):
        #Cycle through the files in the directory
        if '_' not in infilename: continue
        infile = open(args[1]+infilename, 'r')
        total = {"fileType" : "all", "count" : 0, "dir2Added" : 0, "dir1Removed" : 0, "totalChanged" : 0, "totalMod" : 0, "newFiles" : 0}
        cpp = {"fileType" : [".cpp", ".C", ".cxx", ".cc", ".pcc"], "count" : 0, "dir2Added" : 0, "dir1Removed" : 0, "totalChanged" : 0, "totalMod" : 0, "newFiles" : 0}
        c = {"fileType" : [".c", ".pc", ".ec", ".ecp"], "count" : 0, "dir2Added" : 0, "dir1Removed" : 0, "totalChanged" : 0, "totalMod" : 0, "newFiles" : 0}
        h = {"fileType" : [".h"], "count" : 0, "dir2Added" : 0, "dir1Removed" : 0, "totalChanged" : 0, "totalMod" : 0, "newFiles" : 0}
        py = {"fileType" : [".py"], "count" : 0, "dir2Added" : 0, "dir1Removed" : 0, "totalChanged" : 0, "totalMod" : 0, "newFiles" : 0}
        java = {"fileType" : [".java"], "count" : 0, "dir2Added" : 0, "dir1Removed" : 0, "totalChanged" : 0, "totalMod" : 0, "newFiles" : 0}
        shell = {"fileType" : [".sh"], "count" : 0, "dir2Added" : 0, "dir1Removed" : 0, "totalChanged" : 0, "totalMod" : 0, "newFiles" : 0}
        perl = {"fileType" : [".perl"], "count" : 0, "dir2Added" : 0, "dir1Removed" : 0, "totalChanged" : 0, "totalMod" : 0, "newFiles" : 0}
        asm = {"fileType" : [".asm", ".s", ".S"], "count" : 0, "dir2Added" : 0, "dir1Removed" : 0, "totalChanged" : 0, "totalMod" : 0, "newFiles" : 0}
        objc = {"fileType" : [".m"], "count" : 0, "dir2Added" : 0, "dir1Removed" : 0, "totalChanged" : 0, "totalMod" : 0, "newFiles" : 0}
        modules = {"dirString": "/modules/", "fileType" : "modules", "count" : 0, "dir2Added" : 0, "dir1Removed" : 0, "totalChanged" : 0, "totalMod" : 0, "newFiles" : 0}
        extensions = {"dirString": "/extensions/", "fileType" : "extensions", "count" : 0, "dir2Added" : 0, "dir1Removed" : 0, "totalChanged" : 0, "totalMod" : 0, "newFiles" : 0}
    
        #Build the dictionary structures to hold the counts
        fileTypeDiffs = [cpp, c, h, py, asm, java, shell, perl, objc]
        subfolderDiffs = [modules, extensions]
        
        #Parse the version numbers
        dir1 = infilename.split('_')[0]
        dir2 = infilename.split('_')[1]
    
        #Cycle through the lines in each file
        for line in infile:
            if not "files changed" in line and not ".hg" in line and not "README" in line and not "LICENSE" in line and not "LEGAL" in line:
                record = line.split()
                try: extension = record[0][record[0].rindex("."):]
                except ValueError: extension = ""
                #Decide what type of file this is and where it ought to be counted
                typeMatch = None
                if extension != "":
                    for codeType in fileTypeDiffs:
                        if extension in codeType["fileType"]:
                            typeMatch = codeType
                            break
                #Check if the file is in one of the directories we're interested in 
                folderMatch = None
                for folderType in subfolderDiffs:
                    if folderType["dirString"] in record[0]:
                        folderMatch = folderType
                        break
                #Do the counting
                total["count"] += 1
                if typeMatch != None: typeMatch["count"] += 1
                if folderMatch != None: folderMatch["count"] += 1
              
                if record[1] != "|only" and record[1] != "|binary":
                    total["totalChanged"] += int(record[2])
                    total["dir2Added"] += int(record[3])
                    total["dir1Removed"] += int(record[4])
                    # total["totalMod"] += int(record[5])
                    if typeMatch != None:
                        typeMatch["totalChanged"] += int(record[2])
                        typeMatch["dir2Added"] += int(record[3])
                        typeMatch["dir1Removed"] += int(record[4])
                        # typeMatch["totalMod"] += int(record[5])
                    if folderMatch != None:
                        folderMatch["totalChanged"] += int(record[2])
                        folderMatch["dir2Added"] += int(record[3])
                        folderMatch["dir1Removed"] += int(record[4])
                        # typeMatch["totalMod"] += int(record[5])  
                else:
                    total["newFiles"] += 1
                    if typeMatch != None: typeMatch["newFiles"] += 1
                    if folderMatch != None: folderMatch["newFiles"] += 1
    
        #Write the result to the output file in tab-separated format
        csvWriter.writerow([dir1 + '\t' + dir2 + '\t' + 'Total' + '\t' + str(total["count"]) + '\t' + str(total["dir2Added"]) + '\t' + str(total["dir1Removed"]) + '\t' + str(total["totalChanged"]) + '\t' + str(total["newFiles"])])

        for codeType in fileTypeDiffs:
            csvWriter.writerow([dir1 + '\t' + dir2 + '\t' + str(codeType["fileType"]) + '\t' + str(codeType["count"]) + '\t' + str(codeType["dir2Added"]) + '\t' + str(codeType["dir1Removed"]) + '\t' + str(codeType["totalChanged"]) + '\t' + str(codeType["newFiles"])])

        for folderType in subfolderDiffs:
            csvWriter.writerow([dir1 + '\t' + dir2 + '\t' + str(folderType["fileType"]) + '\t' + str(folderType["count"]) + '\t' + str(folderType["dir2Added"]) + '\t' + str(folderType["dir1Removed"]) + '\t' + str(folderType["totalChanged"]) + '\t' + str(folderType["newFiles"])])
    print "Diff count complete. Check lineCount.csv output file."

if __name__ == '__main__':
    main()
