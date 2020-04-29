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
# Splits molecule file into N chunks or chunks of size N
#############################################################################

import os
import sys
from openeye import oechem


def main(argv=[__name__]):

    itf = oechem.OEInterface(InterfaceData, argv)

    if not (itf.HasInt("-num") ^ itf.HasInt("-size")):
        oechem.OEThrow.Fatal("Number of chunks (-num) or the size of each chunk (-size)"
                             " must be specified and are mutually exclusive.")

    ifs = oechem.oemolistream()
    if not ifs.open(itf.GetString("-i")):
        oechem.OEThrow.Fatal("Unable to open %s for reading" % itf.GetString("-i"))

    ifs.SetConfTest(oechem.OEIsomericConfTest(False))
    outbase, ext = os.path.splitext(itf.GetString("-o"))

    if ext == '':
        oechem.OEThrow.Fatal("Failed to find file extension")

    if ext == '.gz':
        outbase, ext = os.path.splitext(outbase)
        ext = ext + '.gz'

    if itf.HasInt("-num"):
        nparts = itf.GetInt("-num")
        SplitNParts(ifs, nparts, outbase, ext)
    else:
        chunksize = itf.GetInt("-size")
        SplitChunk(ifs, chunksize, outbase, ext)


def NewOutputStream(outbase, ext, chunk):
    newname = outbase + ('_%07d' % chunk) + ext
    ofs = oechem.oemolostream()
    if not ofs.open(newname):
        oechem.OEThrow.Fatal("Unable to open %s for writing" % newname)
    return ofs


def SplitNParts(ifs, nparts, outbase, ext):
    moldb = oechem.OEMolDatabase(ifs)
    molcount = moldb.NumMols()

    chunksize, lft = divmod(molcount, nparts)
    if lft != 0:
        chunksize += 1
    chunk, count = 1, 0

    ofs = NewOutputStream(outbase, ext, chunk)
    for idx in range(moldb.GetMaxMolIdx()):
        count += 1
        if count > chunksize:
            if chunk == lft:
                chunksize -= 1

            ofs.close()
            chunk, count = chunk + 1, 1
            ofs = NewOutputStream(outbase, ext, chunk)

        moldb.WriteMolecule(ofs, idx)


def SplitChunk(ifs, chunksize, outbase, ext):
    moldb = oechem.OEMolDatabase(ifs)
    chunk, count = 1, chunksize

    for idx in range(moldb.GetMaxMolIdx()):
        if count == chunksize:
            ofs = NewOutputStream(outbase, ext, chunk)
            chunk, count = chunk + 1, 0
        count += 1
        moldb.WriteMolecule(ofs, idx)


InterfaceData = """\
!BRIEF -num|-size [-i] <input> [-o] <output>

!PARAMETER -in
  !ALIAS -i
  !TYPE string
  !REQUIRED true
  !BRIEF Input file name
  !KEYLESS 1
!END

!PARAMETER -out
  !ALIAS -o
  !TYPE string
  !REQUIRED true
  !BRIEF Output file name
  !KEYLESS 2
!END

!PARAMETER -num
  !TYPE int
  !BRIEF The number of chunks
!END

!PARAMETER -size
  !TYPE int
  !BRIEF The size of each chunk
!END

"""

if __name__ == "__main__":
    sys.exit(main(sys.argv))
