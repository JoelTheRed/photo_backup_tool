import shutil, os
from difPy import dif

#difPy pkg link:https://pypi.org/project/difPy/https://pypi.org/project/difPy/

source = input('Input source folder:').rstrip('/\\')
dest = input('Input backup \ destination folder:').rstrip('/\\')
ext = ('.jpg','.jpeg','.gif','.png')

# Use the correct path separator to 
# ensure correct matching with dif results:
if os.sep == '/':
    source = source.replace('\\', os.sep)
elif os.sep == '\\':
    source = source.replace('/', os.sep)

#difPy duplicate check
search = dif(source, dest)

dupes = list(value['location'] for value in search.result.values())

srcfiles = []
copied = []
failed = []
skipped = []

for dirpath, subdirs, files in os.walk(source):
    for file in files:
        if file.lower().endswith(ext):
            srcfile = os.path.join(dirpath,file)
            srcfiles.append(srcfile)
            if srcfile in dupes:
                print('File not copied (duplicate) - '+srcfile)
                skipped.append(srcfile)
            else:
                try:
                    destfile = os.path.join(dest,srcfile[len(source)+1:])
                    os.makedirs(os.path.dirname(destfile), exist_ok=True)
                    shutil.copy(srcfile,destfile)
                    print('File copied successfully - '+srcfile)
                    copied.append(srcfile)
                except Exception as err:
                    print('File not copied (error %s) - %s' % (str(err),srcfile))
                    failed.append(f)

print(len(copied), 'files backed up!')
print(len(failed), 'files failed to copy!')

delete = input('Do you want to delete files backed up from the source folder? (Y/N)')

if delete.lower() == 'y':
        src_copied = list(set(copied) - set(failed))
        removed = []
        for f in src_copied:
                os.remove(f)
                print(f,'removed')
                removed.append(f)
        print(len(removed), 'files removed from source folder!')
                
else:
        print('Okily Dokily! No files have been removed')

input('operation complete')

