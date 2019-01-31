import os

imdir = 'C:/Users/abhis/Desktop/car damage/images/'
if not os.path.isdir(imdir):
    os.mkdir(imdir)
print(os.listdir('./images'))
folders = [folder for folder in os.listdir('./images') if '00' in folder]
print("2")
print(folders)
n = 0
folder=folders
#print(os.scandir(folder))
#for folder in folders:
for imfile in folder:
        print("1")
        print(imfile)
        print('{:06}.jpg'.format(n))
        print( os.path.join(imdir, '{:06}.jpg'.format(n)))
        os.rename( os.path.join(imdir,imfile), os.path.join(imdir, '{:06}.jpg'.format(n)))
        n += 1
        print(n)
