from numpy import *
import matplotlib.pyplot as plt
from construction import pklread

def load(fname):
    f=open(fname,'r')
    data=[]
    for line in f.readlines():
        data.append(line.replace('\n','').split('\t'))
    f.close()
    return data

def getWM(fname):
	WM = array(load(fname))[:,]
	names = WM[:,0]
	dists = array([float(i) for i in WM[:,2]])
	rbs = 10**array([float(i) for i in WM[:,3]])
	mubs = array([float(i) for i in WM[:,4]])
	alphas = array([float(i) for i in WM[:,5]])
	betas = array([float(i) for i in WM[:,6]]) + 1
	gammas = array([float(i) for i in WM[:,7]]) + 1
	M2Ls = array([float(i) for i in WM[:,8]])
	MBH1s = 10**array([float(i) for i in WM[:,10]])
	MBH2s = 10**array([float(i) for i in WM[:,12]])
	return WM,names,dists,rbs,mubs,alphas,betas,gammas,M2Ls,MBH1s,MBH2s

if __name__ == '__main__':
	from rhomodels import NukerModelRho
	from rateget import getrate
	from rhoratefcns import findrho0
	WM,names,dists,rbs,mubs,alphas,betas,gammas,M2Ls,MBH1s,MBH2s = getWM('NGC3115_vartab.dat')
	rho0s = findrho0(rbs,M2Ls,mubs)
	ilist = arange(len(WM))
	for i in ilist:
		print 'Working on ',names[i],' galaxy ',i+1,' of ',len(WM)
		alpha = alphas[i]
		beta = betas[i]
		gamma = gammas[i]
		r0pc = rbs[i]
		rho0 = rho0s[i]
		MBH_Msun1 = MBH1s[i]
		MBH_Msun2 = MBH2s[i]
		name1 = '{0}_1'.format(names[i])
		name2 = '{0}_2'.format(names[i])
		GENERATE = False
		model1 = NukerModelRho(name1,alpha,beta,gamma,r0pc,rho0,MBH_Msun1,GENERATE,memo = False)
		model2 = NukerModelRho(name2,alpha,beta,gamma,r0pc,rho0,MBH_Msun2,GENERATE,memo = False)
		try:
			rate1 = pklread('{0}/dgdlnrp.pkl'.format(model1.directory))
			rate2 = pklread('{0}/dgdlnrp.pkl'.format(model2.directory))
			plt.figure(figsize = (9,7))
			plt.title('{0}'.format(names[i]))
			plt.ylabel('$d\gamma/d\ln r_p$',fontsize = 20)
			plt.xlabel('$u^2$',fontsize = 20)
			plt.loglog(rate1[:,0][20000:],rate1[:,1][20000:],label = 'MBH = {0}'.format(log10(MBH_Msun1)))
			plt.loglog(rate2[:,0][20000:],rate2[:,1][20000:],label = 'MBH = {0}'.format(log10(MBH_Msun2)))
			plt.legend(loc = 'best')
			plt.xlim(min(rate1[:,0][20000:]),max(rate1[:,0][20000:]))
			plt.savefig('{0}MBHcomp_MBH{1}.png'.format(names[i],log10(MBH_Msun2)))
		except ValueError:
			print 'No positive values in rate for {0}'.format(names[i])
		except IOError:
			print 'No rate for {0}'.format(names[i])

