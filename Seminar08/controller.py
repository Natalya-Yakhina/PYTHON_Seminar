import imp 
import exp
import inp
import logg

def start():
    if inp.mod == '1':
        info = inp.exp()
        exp.exp(info)
        logg.log_info(info)
    elif inp.mod == '2':
        info = inp.inpp()
        imp.inpp(info)
        logg.log_info(info)