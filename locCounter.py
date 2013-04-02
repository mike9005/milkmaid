'''
Created on Mar 14, 2013
@author: Michael Collis (mcollis@seas.upenn.edu)
'''

import sys, os, csv

def main():
    args = sys.argv

    for infilename in sorted(os.listdir(args[1])):
        if not infilename.startswith("firefox"):
            continue
        dict = {}
        count = countdir(0, infilename, dict)
        print infilename, count[0]
    #print 'Dict:'
    #for ext in sorted(count[1], key=count[1].get):
        #print ext, count[1][ext]

def countdir(countSoFar, infile, dict):
    count = countSoFar
    if os.path.isdir(infile):
        result = (None, dict)
        for infilename in os.listdir(infile):
            if infilename.startswith('.'): continue
            result = countdir(countSoFar, infile + '/' + infilename, dict)
            count += result[0]
        return (count, result[1])
    else:
        result = countlines(infile, dict)
        return (count + result[0], result[1])

def countlines(infilename, dict):
    infile = open(infilename, 'r')
    dot = infilename.rfind('.')
    slash = infilename.rfind('/')
    if(dot == -1 or slash > dot):
      return (0, dict)
      #ext = slash
    #else:
    ext = dot

    #if infilename[ext:] not in [".cpp", ".C", ".cxx", ".cc", ".pcc", ".c", ".pc", ".ec", ".ecp", ".h", ".py",".java", ".sh", ".perl", ".asm", ".s", ".S", ".m"]:
    #    return (0, dict)

    #if infilename[ext:] != '.html' and infilename[ext:] != '.css' and infilename[ext:] != '.h' and infilename[ext:] != '.h' and infilename[ext:] != '.in' and infilename[ext:] != '.idl' and infilename[ext:] != '.js'and infilename[ext:] != '.xul' and infilename[ext:] != '.dtd' and infilename[ext:] != '.txt' and infilename[ext:] != '.xhtml' and infilename[ext:] != '.out' and infilename[ext:] != '.exe':
     #   return (0, dict)

    if infilename[ext:] in dict:
        dict[infilename[ext:]] += 1
    else:
        dict[infilename[ext:]] = 1

    count = 0
    comment = False
    for line in infile:
            #if len(line.strip()) > 0:
        if len(line.strip()) > 0 and (not line.strip().startswith("#") or infilename.endswith('.c') or infilename.endswith('.cpp') or infilename.endswith('.h') or infilename.endswith('.css') or
            infilename.endswith('.html')) and not line.strip().startswith("//"):
            if not comment and ((line.strip().startswith('<!--') and not line.strip().endswith('-->')) or
                                 (line.strip().startswith('/*') and not line.strip().endswith('*/')) or
                                  (line.strip().startswith('\'\'\'') and not line.strip().endswith('\'\'\''))):
                comment = True
            elif comment and (line.strip().startswith('*/') or line.strip().startswith('\'\'\'') or line.strip().endswith('*/') or line.strip().endswith('\'\'\'') or line.strip().endswith('-->') or line.strip().startswith('-->')):
                comment = False
            elif not comment:
                                count += 1
    return (count, dict)

if __name__ == '__main__':
    main()
