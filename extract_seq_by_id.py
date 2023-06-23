#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, csv, sys

'''
    DOC: http://cnvkit.readthedocs.io/en/stable/quickstart.html
    Home: https://github.com/etal/cnvkit

    =============================================================

    Build the reference CNN file for all normal samples

    @@@@ change log
'''

def main():
    '''
        ========================================================
        ========================================================
    '''

    read_id = []

    in_file = sys.argv[1]
    id_file = sys.argv[2]
    out_file = sys.argv[3]

    with open(id_file, 'rb') as in_handle:
        for line in in_handle:
            target_id = ':'.join(line.strip().split(':')[1:])
            read_id.append(target_id)
    print '[INFO]: Found %s seq id from %s' % (len(read_id), id_file)
    read_id = set(read_id)


    flag_to_out = 0
    with open(in_file, 'rb') as in_handle, open(out_file, 'wb') as out_handle:
        for line in in_handle:
            if line[0] == '>':
                flag_to_out = 0
                seq_id = line.strip()
                if seq_id in read_id:
                    print '[INFO]: Output sequence with %s' % seq_id
                    flag_to_out = 1
                    out_handle.write(line)
            else:
                if flag_to_out == 1:
                    out_handle.write(line)


if __name__ == '__main__':
    main()