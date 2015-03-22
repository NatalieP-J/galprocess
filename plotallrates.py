from numpy import *
import matplotlib.pyplot as plt
import matplotlib
import os
from scipy.interpolate import interp1d
from scipy.optimize import leastsq
plt.ion()

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 18}

matplotlib.rc('font', **font)


def load(fname):
    f=open(fname,'r')
    data=[]
    for line in f.readlines():
        data.append(line.replace('\n','').split('\t'))
    f.close()
    return data

def getind(vals,val):
	for i in range(len(vals)):
		if abs(vals[i] - val) < 1e-15:
			return i

def quad(p,x):
	a,b,c = p
	return a*x**2 + b*x + c

def fitquad(p,x,y):
	return abs(y-quad(p,x))

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
	from rhomodels import NukerModelRho
	from rhoratefcns import findrho0
	from construction import pklread,displaycheck,existcheck
	WM,names,dists,rbs,mubs,alphas,betas,gammas,M2Ls,MBH1s,MBH2s = getWM('WM04.dat')
	#os.chdir('/Users/Natalie/Data/Mar16WM')
	rho0s = findrho0(rbs,M2Ls,mubs)
	dcheck = displaycheck()
	ilist = arange(0,50)
	colors = plt.get_cmap('spectral')(linspace(0, 1.0, len(ilist)))
	#ilist = delete(ilist,11)
	#ilist = delete(ilist,5)
	#ilist = delete(ilist,5)
	#ilist = delete(ilist,26)
	#ilist = delete(ilist,46)
	plt.figure()
	rs = []
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
		seton,plotdat = existcheck(model1.directory, dcheck)
		if seton['dgdlnrp'] == 'OFF' and i != len(WM) - 1:
			print 'plotting'
			rate = pklread('{0}/dgdlnrp.pkl'.format(model1.directory))
			plt.loglog(rate[:,0],rate[:,1],color = colors[i],linewidth = 3)#,label = '{0}'.format(log10(MBH_Msun2)))
			linslope = (log10(rate[:,1][401]) - log10(rate[:,1][301]))/(log10(rate[:,0][401]) - log10(rate[:,0][301]))
			#ratefn = interp1d(log10(rate[:,0]),log10(rate[:,1]))
			ind = getind(rate[:,0],1e-2)
			#ind = 501
			#ind = getind(rate[:,0],1e-4)
			#slope = copy(linslope)
			slopes = []
			for k in range(ind,len(rate[:,0])-1):
				slope = (log10(rate[:,1][k+1]) - log10(rate[:,1][k]))/(log10(rate[:,0][k+1]) - log10(rate[:,0][k]))
				slopes.append(slope)
			mslope = -1
			for j in range(len(slopes)):
				if slopes[j] == max(slopes):
					mslope = j
			#for l in range(len(slopes)-1):
			#	print (slopes[l+1] - slopes[l])/(log10(rate[:,0][l+1]) - log10(rate[:,0][l]))
			#risefactor = (log10(rate[:,1][mslope]) - log10(rate[:,1][ind]))/(log10(rate[:,0][mslope]) - log10(rate[:,0][ind]))
			risefactor = (slopes[mslope] - 2.0)/(log10(rate[:,0][mslope + ind]) - log10(rate[:,0][ind]))
			rs.append([name1,alpha,beta,gamma,MBH_Msun1,risefactor])

		plt.xlim(1e-1,1)
		plt.ylim(1e-11,1e-3)
		plt.xlabel('$u$',fontsize = 30)
		plt.ylabel('$d\gamma/d\ln r_p$',fontsize = 30)
		plt.title('$\mathrm{Rate\,as\,a\,function\,of\,pericenter}$',fontsize = 20)
		#plt.title('Rates for varying black hole mass')
	#os.chdir('/Users/Natalie/Code/galprocess')
	rsa = array(rs)
	plt.figure()
	plt.plot(rsa[:,1].astype(float),rsa[:,5].astype(float),'.')
	plt.xlabel(r'$\alpha$',fontsize = 20)
	plt.ylabel('rise',fontsize = 20)
	plt.figure()
	plt.plot(rsa[:,2].astype(float),rsa[:,5].astype(float),'.')
	plt.xlabel(r'$\beta$',fontsize = 20)
	plt.ylabel('rise',fontsize = 20)
	plt.figure()
	plt.plot(rsa[:,3].astype(float),rsa[:,5].astype(float),'.')
	plt.xlabel('$\gamma$',fontsize = 20)
	plt.ylabel('rise',fontsize = 20)
	plt.figure()
	for n in range(len(rsa)):
		plt.plot(log10(rsa[:,4][n].astype(float)),rsa[:,5][n].astype(float),'o',color = colors[n],markersize = 12)
	plt.xlabel('$\log_{10}(M_{\mathrm{BH}})$',fontsize = 25)
	plt.ylabel('$\mathcal{S}$',fontsize = 30)
	plt.title('$\mathrm{Rise\,factor\,vs\,black\,hole\,mass}$',fontsize = 20)
	#plt.savefig('/Users/Natalie/Google Drive/AST425/risefactorNGC3115.png')

