import csv
import getopt
import sys     # sys.argv needed
# argparse
# getopt
# fire

inp = 'cars-original.csv'     # input file name
outp = 'cars-fixed.csv'    # output file name
indlm = '|'  # delimiter
inqt = " "    # "\'" or "'" or ...

def changef(inf, outf, ind, inq):
    #print(f'[changef]: {inf}, {outf}, "{ind}", "{inq}"', file=log)
    
    with open(inf, newline='') as f:
        lines = list(csv.reader(f, delimiter=ind, quotechar=inq)) #, quotechar=inqt)
      
    #print(lines)    
    with open(outf, 'wt', newline='') as o:
        csvwr = csv.writer(o,delimiter=',')
        for row in lines:
            csvwr.writerow(row)
   


if __name__ == '__main__':
    
    #print(sys.argv)
    optlist, args = getopt.gnu_getopt(sys.argv[1:], '', ['in-delimiter=', 'in-quote='])
   
    #print(optlist)
    for par, val in optlist:
        if par == '--in-delimiter':
            indlm = val
        elif par == '--in-quote':
            inqt = val
    #print(f'dlm="{indlm}", quote="{inqt}"')
       
    #print(args)
    if len(args) != 2 : raise ValueError('Two file-arguments are needed!')
    inp = args[0] 
    outp = args[1]
    
    changef(inp, outp, indlm, inqt)
    