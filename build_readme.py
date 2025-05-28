import os

# Load and increment version numbers

f = open("./merk/data/major.txt","r")
major = f.read()
f.close()

f = open("./merk/data/minor.txt","r")
minor = f.read()
f.close()

f = open("./merk/data/win_major.txt","r")
win_major = f.read()
f.close()

f = open("./merk/data/win_minor.txt","r")
win_minor = f.read()
f.close()

# Build README

x = open("README.txt",mode="r", encoding='latin-1')
readme = str(x.read())
x.close()

x = open("HELP.txt",mode="r", encoding='latin-1')
helpfile = str(x.read())
x.close()

readme = readme.replace("!_VERSION_!",major)
readme = readme.replace("!_MINOR_!",minor)
readme = readme.replace("!_FULL_VERSION_!",major+"."+minor)
readme = readme.replace("!_WIN_VERSION_!",win_major+"."+win_minor)

helpfile = readme.replace("!_VERSION_!",major)
helpfile = readme.replace("!_MINOR_!",minor)
helpfile = readme.replace("!_FULL_VERSION_!",major+"."+minor)
helpfile = readme.replace("!_WIN_VERSION_!",win_major+"."+win_minor)

# !_PYSIZE_!
dist_file_size =  os.path.getsize("./downloads/merk-latest.zip")
file_size_kb = dist_file_size / 1024
file_size_mb = file_size_kb / 1024
readme = readme.replace("!_PYSIZE_!",f"{file_size_mb:.2f} MB")
# !_WINZIP_!
win_latest_file_size =  os.path.getsize("./downloads/merk-windows-latest.zip")
file_size_kb = win_latest_file_size / 1024
file_size_mb = file_size_kb / 1024
readme = readme.replace("!_WINZIP_!",f"{file_size_mb:.2f} MB")
# !_WINEXE_!
win_single_file_size =  os.path.getsize("./downloads/merk-windows-standalone.zip")
file_size_kb = win_single_file_size / 1024
file_size_mb = file_size_kb / 1024
readme = readme.replace("!_WINEXE_!",f"{file_size_mb:.2f} MB")
# !_WINSETUP_!
win_setup_file_size =  os.path.getsize("./downloads/merk_setup.zip")
file_size_kb = win_setup_file_size / 1024
file_size_mb = file_size_kb / 1024
readme = readme.replace("!_WINSETUP_!",f"{file_size_mb:.2f} MB")

os.remove("README.md")
f = open("README.md",mode="w", encoding='latin-1')
f.write(readme)
f.close()

os.remove("HELP.md")
f = open("HELP.md",mode="w", encoding='latin-1')
f.write(helpfile)
f.close()
