#-----fn user defined-----
#------variable arg_------------

def fn_vararg(arg1,*vartuple):
    #-formal arg is arg1
    print "output is", arg1
    
    for var in vartuple:
        print var
    return;
    
#calling fn in diff ways

fn_vararg(10)

fn_vararg([34,4,45,4544,47])    #---we r providing a list here

fn_vararg(34,4,45,4544,47) 