#!/usr/bin/python
# programmer : zhangll
# usage:fasta split by miRNA

import sys
import string
import re
import numpy as np
import argparse

def Seq_find_miRNA(file):
    with open(file, 'r') as fin:
        with open('Consensus_Rdir.fasta','w') as fout:
            lines = fin.readlines()
            for line in lines:
                line = line.rstrip()
                if line.startswith('>'):
                    fout.writelines(line+'\n')
                else:
                    pos = line.find('CTGTAGGCACCATCAAT')
                    pos_rev = line.find('ATTGATGGTGCCTACAG')
                    if pos == -1 and pos_rev == -1:
                        fout.writelines(line+'\n')
                    elif pos != -1 :
                        ret = []
                        while pos != -1:
                            ret.append(pos)
                            pos = line.find('CTGTAGGCACCATCAAT', pos+1)
                        if len(ret)==1:
                            fout.writelines(line[ret[0]:]+line[:ret[0]]+'\n')
                            #print line[ret[0]:]+line[:ret[0]]
                        else:    
                            ret0=ret[:-1]
                            ret1=ret[1:]
                            aa=np.array(ret1)-np.array(ret0)
                            aa=aa.tolist()
                            seq_length=max(aa)  
                            index_pos=aa.index(seq_length)
                            if len(line[ret[index_pos]:ret[index_pos+1]]) >= len(line[ret[-1]:]+line[:ret[0]]):
                                fout.writelines(line[ret[index_pos]:ret[index_pos+1]]+'\n')
                                #print line[ret[index_pos]:ret[index_pos+1]]
                            else:
                                fout.writelines(line[ret[-1]:]+line[:ret[0]]+'\n')
                                #print line[ret[-1]:]+line[:ret[0]]
                    else:
                        ret_rev = []
                        while pos_rev != -1:
                            ret_rev.append(pos_rev)
                            pos_rev = line.find('ATTGATGGTGCCTACAG', pos_rev+1)
                        if len(ret_rev) == 1:
                            fout.writelines(line[ret_rev[0]:]+line[:ret_rev[0]]+'\n')
                            #print line[ret[0]:]+line[:ret[0]]
                        else:    
                            ret_rev0 = ret_rev[:-1]
                            ret_rev1 = ret_rev[1:]
                            aa = np.array(ret_rev1)-np.array(ret_rev0)
                            aa = aa.tolist()
                            seq_length = max(aa)  
                            index_pos = aa.index(seq_length)
                            if len(line[ret_rev[index_pos]:ret_rev[index_pos+1]]) >= len(line[ret_rev[-1]:]+line[:ret_rev[0]]):
                                fout.writelines(line[ret_rev[index_pos]:ret_rev[index_pos+1]]+'\n')
                                #print line[ret[index_pos]:ret[index_pos+1]]
                            else:
                                fout.writelines(line[ret_rev[-1]:]+line[:ret_rev[0]]+'\n')
                                #print line[ret[-1]:]+line[:ret[0]]
                     

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file",type=str, default = None)
    args=parser.parse_args()
    Seq_find_miRNA(args.file)

if __name__=="__main__":
    main()
