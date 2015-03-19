from numpy import *
import matplotlib.pyplot as plt

plt.ion()

def find2nonzero(vallist):
	MBHs = []
	WMrates = []
	MYrates = []
	for i in range(len(vallist[:,0])):
		if vallist[:,1][i] != 0 and vallist[:,2][i] != 0:
			MBHs.append(vallist[:,0][i])
			WMrates.append(vallist[:,1][i])
			MYrates.append(vallist[:,2][i])
	return array(MBHs), array(WMrates), array(MYrates)

def findnonzero(vallist):
	MBHs = []
	MYrates = []
	for i in range(len(vallist[:,0])):
		if vallist[:,2][i] != 0:
			MBHs.append(vallist[:,0][i])
			MYrates.append(vallist[:,2][i])
	return array(MBHs), array(MYrates)

mass1s = loadtxt('Data - MBH1.tsv')
mass2s = loadtxt('Data - MBH2.tsv')

MBH1,WM1,MY1 = find2nonzero(mass1s)
MBH2,WM2,MY2 = find2nonzero(mass2s)
mMBH1,mMY1 = findnonzero(mass1s)
mMBH2,mMY2 = findnonzero(mass2s)

plt.figure()
plt.plot(MBH1,WM1,'o')
plt.plot(MBH1,MY1,'o')
plt.plot(MBH1,WM1-MY1,'o')

plt.figure()
plt.plot(MBH2,WM2,'o')
plt.plot(MBH2,MY2,'o')
plt.plot(MBH2,WM2-MY2,'o')

plt.figure()
plt.plot(mMY1,'o')
plt.plot(mMY2,'o')
plt.plot(mMY1-mMY2,'o')
