import zipfile

obj=zipfile.ZipFile('1.zip','r')
f= open('word.txt','r')
for password in f.readlines():
    password=password.strip('\n').strip('\r')
    try:
        obj.extractall(pwd=password)
        print("Password Found: " + password + "   <<<<<<<<<<")

    except:
        print("Trying.......")
