from numpy import *
from itertools import product
from loadWMRho import getWM, load
import matplotlib.pyplot as plt
from construction import pklread

plt.ion()

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
name = 'NGC 3115'
rowind = name2row(name,names)
beta = (array([float(i) for i in WM[:,6]]))[rowind]
gamma = (array([float(i) for i in WM[:,7]]))[rowind]
MBH1 = (array([float(i) for i in WM[:,10]]))[rowind]
MBH2 = (array([float(i) for i in WM[:,12]]))[rowind]
basicrow = WM[rowind]
#varvals = array([0,0.005,-0.005,0.1,-0.1,0.5,-0.5])
varvals = array([-2,-1,0,1,2])

nplist = []
#nplist.append(varparams(beta,varvals))
#nplist.append(varparams(gamma,varvals))
nplist.append(varparams(MBH2,varvals))

#chinds = [6,7]
chinds = [12]

tab = newtab(nplist,chinds,basicrow)

writefile(tab,'{0}_vartab.dat'.format(name.replace(' ','')))

'''
beta += 1
gamma += 1

bs = nplist[0]

plt.figure()
plt.xlim(1e-4,1-1e-4)
plt.title('NGC596 1st black hole mass estimate, original beta 2.97, gamma 1.55')
plt.xlabel('$u^2$',fontsize = 20)
plt.ylabel('$d\gamma/d\ln r_p$', fontsize = 20)

for i in range(len(bs)):
    direc1 = 'NukerRhoGals/NGC 596_1_Rho_a0.76_b{0}_g{1}_MBH489778819.368/dgdlnrp.pkl'.format(bs[i]+1,gamma)
    ratedat = pklread(direc1)
    plt.loglog(ratedat[:,0],ratedat[:,1],label = 'beta = {0}'.format(bs[i]+1))

plt.legend(loc = 'best')

plt.figure()
plt.xlim(1e-4,1-1e-4)
plt.title('NGC596 2nd black hole mass estimate, original beta 2.97, gamma 1.55')
plt.xlabel('$u^2$',fontsize = 20)
plt.ylabel('$d\gamma/d\ln r_p$', fontsize = 20)

for i in range(len(bs)):
    direc1 = 'NukerRhoGals/NGC 596_2_Rho_a0.76_b{0}_g{1}_MBH48977881.9368/dgdlnrp.pkl'.format(bs[i]+1,gamma)
    ratedat = pklread(direc1)
    plt.loglog(ratedat[:,0],ratedat[:,1],label = 'beta = {0}'.format(bs[i]+1))

plt.legend(loc = 'best')

gs = nplist[1]

plt.figure()
plt.xlim(1e-4,1-1e-4)
plt.title('NGC596 1st black hole mass estimate, original gamma 1.55, beta 2.97')
plt.xlabel('$u^2$',fontsize = 20)
plt.ylabel('$d\gamma/d\ln r_p$', fontsize = 20)

for i in range(len(gs)):
    direc1 = 'NukerRhoGals/NGC 596_1_Rho_a0.76_b{0}_g{1}_MBH489778819.368/dgdlnrp.pkl'.format(beta,gs[i]+1)
    ratedat = pklread(direc1)
    plt.loglog(ratedat[:,0],ratedat[:,1],label = 'gamma = {0}'.format(gs[i]+1))

plt.legend(loc = 'best')

plt.figure()
plt.xlim(1e-4,1-1e-4)
plt.title('NGC596 2nd black hole mass estimate, original gamma 1.55, beta 2.97')
plt.xlabel('$u^2$',fontsize = 20)
plt.ylabel('$d\gamma/d\ln r_p$', fontsize = 20)

for i in range(len(gs)):
    direc1 = 'NukerRhoGals/NGC 596_2_Rho_a0.76_b{0}_g{1}_MBH48977881.9368/dgdlnrp.pkl'.format(beta,gs[i]+1)
    ratedat = pklread(direc1)
    plt.loglog(ratedat[:,0],ratedat[:,1],label = 'gamma = {0}'.format(gs[i]+1))

plt.legend(loc = 'best')
'''

