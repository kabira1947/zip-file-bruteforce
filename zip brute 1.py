import optparse
import zipfile
from threading import Thread


def file_extracter(File,password):

    try:
        File.extractall(pwd=password)
        print("password found: "+password+"\n")
    except:
        pass
def cracker():
    parser = optparse.OptionParser("usage of programme" + "-f <zipfile> -d <dictionary>")
    parser.add_option('-f',dest='zipname',type='string',help ='name the zip file')
    parser.add_option('-d', dest='dicname', type='string',help = 'name the dictionary file')

    (options,args)= parser.parse_args()

    if (options.zipname is None) or (options.dicname is None):
        print(parser.usage)
        exit(0)
    else:
        zipname = options.zipname
        dicname = options.dicname


    File = zipfile.ZipFile(zipname)
    passfile = open(dicname)

    for lines in passfile.readlines():
        password= lines.strip('\n')
        t= Thread(target=file_extracter,args=(File,password))
        t.start()


if __name__ == '__main__':
    cracker()
