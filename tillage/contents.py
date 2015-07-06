def getREADME(descr):
    name = descr.name
    underline = '-'*len(name)
    return 'README.rst', '{}\n{}\n'.format(name, underline)
