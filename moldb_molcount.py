#!/usr/bin/env python3
# (C) 2017 OpenEye Scientific Software Inc. All rights reserved.
#
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of OpenEye products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. OpenEye claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable OpenEye offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED.  OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall OpenEye be
# liable for any damages or liability in connection with the Sample Code
# or its use.

#############################################################################
# Counts molecule in input files
#############################################################################

import sys
from openeye import oechem


def MolCount(fname):

    ifs = oechem.oemolistream()
    if not ifs.open(fname):
        oechem.OEThrow.Warning("Unable to open %s for reading" % fname)
        return 0

    moldb = oechem.OEMolDatabase(ifs)
    nummols = moldb.NumMols()
    print("%s contains %d molecule(s)." % (fname, nummols))
    return nummols


def main(argv=[__name__]):

    itf = oechem.OEInterface(Interface, argv)

    totalmols = 0
    for fname in itf.GetStringList("-i"):
        totalmols += MolCount(fname)
    print("===========================================================")
    print("Total %d molecules" % totalmols)


Interface = """
!BRIEF [-i] <infile1> [<infile2>...]

!PARAMETER -in
  !ALIAS -i
  !TYPE string
  !LIST true
  !REQUIRED true
  !BRIEF Input file name(s)
  !KEYLESS 1
!END

"""

if __name__ == "__main__":
    sys.exit(main(sys.argv))
