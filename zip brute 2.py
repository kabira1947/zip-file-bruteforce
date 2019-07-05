import zipfile
Filename=input("input path of zip file: ")
ZFile = zipfile.ZipFile(Filename, "r")
passfile = open('word.txt', 'r')
body= passfile.read()
passwords=body.split()
tried=1

for password in passwords:
    try:
        ZFile.extractall(pwd=password)
        print("found the password: {}".format(password))
        break
    except Exception as e:
        print(" {} is not the password.".format(password))
        print('The number of password tried: {}'.format(tried))
        tried+=1
        continue
