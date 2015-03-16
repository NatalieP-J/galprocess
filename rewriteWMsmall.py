import sys
from loadWMRho import getWM

def LoadData(fname):
    f=open(fname,'r')
    data=[]
    for line in f.readlines():
        data.append(line.replace('\n',''))
    f.close()
    return data

if __name__ == '__main__':
    WM,names,dists,rbs,mubs,alphas,betas,gammas,M2Ls,MBH1s,MBH2s = getWM('WM04.dat')
    ind = sys.argv[1]
    name = names[int(ind)]
    oldfile = LoadData('runWMsmall.sh')
    modline1 = oldfile[4][:8]
    modline2 = oldfile[-1][:19]
    newline1 = '{0} {1}2'.format(modline1,name.replace(' ',''))
    newline2 = '{0} {1}'.format(modline2,ind)
    newfile = oldfile
    newfile[4] = newline1
    newfile[-1] = newline2
    newfname = open('runWMsmall.sh','wb')
    for i in range(len(newfile)):
        newfname.write('{0}\n'.format(newfile[i]))
    newfname.close()
