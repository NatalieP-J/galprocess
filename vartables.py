from numpy import *
from itertools import product
from loadWMRho import getWM, load
import matplotlib.pyplot as plt
from construction import pklread
import os

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
 
if __name__ == '__main__':       
    WM = array(load('WM04.dat'))[:,]
    names = WM[:,0]
    name = 'NGC 3115'
    rowind = name2row(name,names)
    alpha = (array([float(i) for i in WM[:,5]]))[rowind]
    beta = (array([float(i) for i in WM[:,6]]))[rowind]
    gamma = (array([float(i) for i in WM[:,7]]))[rowind]
    MBH1 = (array([float(i) for i in WM[:,10]]))[rowind]
    MBH2 = (array([float(i) for i in WM[:,12]]))[rowind]
    basicrow = WM[rowind]
    #varvals = array([-0.5,-0.1,-0.005,0,0.005,0.1,0.5])
    varvals = array([-2,-1.5,-1,-0.5,0,0.5,1,1.5,2])
    
    nplist = []
    #nplist.append(varparams(beta,varvals))
    #nplist.append(varparams(gamma,varvals))
    nplist.append(varparams(MBH2,varvals))

    #chinds = [6,7]
    chinds = [12]

    tab = newtab(nplist,chinds,basicrow)

    writefile(tab,'{0}_vartab2.dat'.format(name.replace(' ','')))
'''
    beta += 1
    gamma += 1

    bs = nplist[0]

    os.chdir('/Users/Natalie/Data/Mar12WM')

    plt.figure()
    plt.xlim(1e-4,1-1e-4)
    plt.title('{0} 1st black hole mass estimate, original beta {1}, gamma {2}'.format(name,beta,gamma))
    plt.xlabel('$u^2$',fontsize = 20)
    plt.ylabel('$d\gamma/d\ln r_p$', fontsize = 20)

    for i in range(len(bs)):
        direc1 = 'NukerRhoGals/{0}_1_Rho_a{1}_b{2}_g{3}_MBH{4}/dgdlnrp.pkl'.format(name,alpha,bs[i]+1,gamma,10**MBH1)
        try:
            ratedat = pklread(direc1)
            plt.loglog(ratedat[:,0],ratedat[:,1],label = 'beta = {0}'.format(bs[i]+1))
        except IOError:
            pass

    plt.legend(loc = 'best')

    plt.figure()
    plt.xlim(1e-4,1-1e-4)
    plt.title('{0} 2nd black hole mass estimate, original beta {1}, gamma {2}'.format(name,beta,gamma))
    plt.xlabel('$u^2$',fontsize = 20)
    plt.ylabel('$d\gamma/d\ln r_p$', fontsize = 20)

    for i in range(len(bs)):
        direc1 = 'NukerRhoGals/{0}_2_Rho_a{1}_b{2}_g{3}_MBH{4}/dgdlnrp.pkl'.format(name,alpha,bs[i]+1,gamma,10**MBH2)
        try:
            ratedat = pklread(direc1)
            plt.loglog(ratedat[:,0],ratedat[:,1],label = 'beta = {0}'.format(bs[i]+1))
        except IOError:
            pass

    plt.legend(loc = 'best')

    gs = nplist[1]

    plt.figure()
    plt.xlim(1e-4,1-1e-4)
    plt.title('{0} 1st black hole mass estimate, original gamma {1}, beta {2}'.format(name,gamma,beta))
    plt.xlabel('$u^2$',fontsize = 20)
    plt.ylabel('$d\gamma/d\ln r_p$', fontsize = 20)

    for i in range(len(gs)):
        direc1 = 'NukerRhoGals/{0}_1_Rho_a{1}_b{2}_g{3}_MBH{4}/dgdlnrp.pkl'.format(name,alpha,beta,gs[i]+1,10**MBH1)
        try:
            ratedat = pklread(direc1)
            plt.loglog(ratedat[:,0],ratedat[:,1],label = 'gamma = {0}'.format(gs[i]+1))
        except IOError:
            pass

    plt.legend(loc = 'best')

    plt.figure()
    plt.xlim(1e-4,1-1e-4)
    plt.title('{0} 2nd black hole mass estimate, original gamma {1}, beta {2}'.format(name,gamma,beta))
    plt.xlabel('$u^2$',fontsize = 20)
    plt.ylabel('$d\gamma/d\ln r_p$', fontsize = 20)

    for i in range(len(gs)):
        direc1 = 'NukerRhoGals/{0}_2_Rho_a{1}_b{2}_g{3}_MBH{4}/dgdlnrp.pkl'.format(name,alpha,beta,gs[i]+1,10**MBH2)
        try:
            ratedat = pklread(direc1)
            plt.loglog(ratedat[:,0],ratedat[:,1],label = 'gamma = {0}'.format(gs[i]+1))
        except IOError:
            pass

    plt.legend(loc = 'best')

    os.chdir('/Users/Natalie/Code/galprocess')

'''
