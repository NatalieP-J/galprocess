from numpy import *
from itertools import product
from loadWMRho import getWM, load

def writefile(rows, fname):
    with open(fname,"w") as data:
        for i in range(len(rows)):
            data.write(rows[i])

def varparams(param, varvals):
    nparams = []
    for i in range(len(varvals)):
        nparams.append(param + varvals[i])
    return array(nparams)

def name2row(name,names):
    for i in range(len(names)):
        if name == names[i]:
            return i

def newtab(nplist,chinds,origrow):
    skrow = copy(origrow)
    combos = list(product(*nplist))
    rows = []
    for i in range(len(combos)):
        nrow = copy(skrow)
        srow = ''
        for c in range(len(chinds)):
            nrow[chinds[c]] = combos[i][c]
        for k in range(len(nrow)):
            srow+='{0}\t'.format(nrow[k])
        srow += '\n'
        rows.append(srow)
    return rows
        
WM = array(load('WM04.dat'))[:,]
names = WM[:,0]
name = 'NGC 596'
rowind = name2row(name,names)
beta = (array([float(i) for i in WM[:,6]]))[rowind]
gamma = (array([float(i) for i in WM[:,7]]))[rowind]
MBH2 = (array([float(i) for i in WM[:,12]]))[rowind]
basicrow = WM[rowind]
varvals = array([0.005,-0.005,0.1,-0.1,0.5,-0.5])

nplist = []
nplist.append(varparams(beta,varvals))
nplist.append(varparams(gamma,varvals))

chinds = [6,7]

tab = newtab(nplist,chinds,basicrow)

writefile(tab,'{0}_vartab.dat'.format(name.replace(' ','')))
