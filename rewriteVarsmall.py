import sys

def LoadData(fname):
    f=open(fname,'r')
    data=[]
    for line in f.readlines():
        data.append(line.replace('\n',''))
    f.close()
    return data

if __name__ == '__main__':
    oldfile = LoadData('runVarsmall.sh')
    modline = oldfile[-1][:19]
    newline = '{0} {1}'.format(modline,sys.argv[1])
    newfile = oldfile
    newfile[-1] = newline
    newfname = open('runVarsmall.sh','wb')
    for i in range(len(newfile)):
        newfname.write('{0}\n'.format(newfile[i]))
    newfname.close()
