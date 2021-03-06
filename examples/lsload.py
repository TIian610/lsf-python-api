from pythonlsf import lsf

def printHostInfo():
    if lsf.lsb_init("test") > 0:
        return -1;

    intp_nhosts = lsf.new_intp()
    lsf.intp_assign(intp_nhosts, 0) 
    all_lsload_data = lsf.ls_load_py(None, intp_nhosts, 0, None)
    nhosts = lsf.intp_value(intp_nhosts)

    print("{} hosts in the cluster.".format(nhosts))

    for i in range(nhosts) :
        host = all_lsload_data[i]
        print('No.{} host name : {}'.format(i, host.hostName))

    return 0

if __name__ == '__main__':
    print("LSF Clustername is : {}".format(lsf.ls_getclustername()))
    printHostInfo()

