from numpy import *
import matplotlib.pyplot as plt
import os

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
	rates = []
	from rhomodels import NukerModelGenRho
	from rateget import getrate
	from rhoratefcns import findrho0
	from construction import writedata
	WM,names,dists,rbs,mubs,alphas,betas,gammas,M2Ls,MBH1s,MBH2s = getWM('WM04.dat')
	#os.chdir('/Users/Natalie/Data/Mar16WM')
	rho0s = findrho0(rbs,M2Ls,mubs)
	ilist = arange(0,50)
	ilist = delete(ilist,3)
	ilist = delete(ilist,7)
	ilist = delete(ilist,11)
	ilist = delete(ilist,14)
	ilist = delete(ilist,20)
	ilist = delete(ilist,21)
	ilist = delete(ilist,21)
	ilist = arange(48,50)
	#ilist = delete(ilist,21)
	#ilist = delete(ilist,40)
	#ilist = delete(ilist,40)
	#ilist = delete(ilist,44)
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
		model1 = NukerModelGenRho(name1,alpha,beta,gamma,r0pc,rho0,MBH_Msun1,GENERATE,memo = False)
		model1.getrho()
		result1 = getrate(model1)
		if result1[-1] != 0:
			rates.append('{0}\t{1}'.format(name1,log10(result1[-1])))
		#model2 = NukerModelGenRho(name2,alpha,beta,gamma,r0pc,rho0,MBH_Msun2,GENERATE,memo = False)
		#model2.getrho()
		#result2 = getrate(model2)
		#if result2[-1] != 0:
		#	rates.append('{0}\t{1}'.format(name2,log10(result2[-1])))
	writedata(rates,'totalGenrates.dat')
	#os.chdir('/Users/Natalie/Code/galprocess')
