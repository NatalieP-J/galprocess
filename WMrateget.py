from numpy import *
from subprocess import call
from matplotlib.backends.backend_pdf import PdfPages
from rateget import *
from construction import fromfileplot
from rhomodels import NukerModelRho
import sys
from loadWMRho import getWM

seton = {'Menc':"OFF",'psi':"OFF",'Jc2':"OFF",'lg':"OFF",'bG':"OFF",'f':"OFF",'dgdlnrp':"ON"}
plottinglist = {'Menc':False,'psi':False,'Jc2':False,'lg':False,'bG':False,'f':False,'dgdlnrp':False}
partial = seton,plottinglist


i = int(sys.argv[1])

WM,names,dists,rbs,mubs,alphas,betas,gammas,M2Ls,MBH1s,MBH2s = getWM('WM04.dat')

GENERATE = False

name = names[i]
alpha = alphas[i]
beta = betas[i]
gamma = gammas[i]
M2L = M2Ls[i]
MBH_Msun = MBH1s[i]
rb = rbs[i]
mub = mubs[i]
rho0 = findrho0(rb,M2L,mub)
model1 = NukerModelRho('{0}_1'.format(name),alpha,beta,gamma,rb,rho0,MBH_Msun,GENERATE,memo = False)
result1 = getrate(model1)
MBH_Msun = MBH2s[i]

GENERATE = False

model2 = NukerModelRho('{0}_2'.format(name),alpha,beta,gamma,rb,rho0,MBH_Msun,GENERATE,memo = False)
result2 = getrate(model2,partial)




