

import os
import sys
import matplotlib.pyplot as plt
import subprocess

lev_prec = "HTVS-Cnfgn"

mols_screened = subprocess.check_output(["wc",'-l', 'LOGDATA.txt'])

mols_screened = int(str(mols_screened).split(" ")[0].replace("b'",""))


with open('LOGDATA.txt','r') as f:
        glide_scores = []
        for line in f:
                if line != "":
                        glide_scores.append(-1*float(line.strip('\n')))

print(min(glide_scores))
sortedGlideScores = sorted(glide_scores)[1500000]
print(sortedGlideScores)

plt.hist(glide_scores,bins=100,range=(-13,0))
plt.title('{}  | {} eMols screened'.format(lev_prec,mols_screened))
plt.ylabel('Counts')
plt.xlabel('Gscore')
plt.xlim(-14,0)
plt.ylim(0,500)
plt.show()

