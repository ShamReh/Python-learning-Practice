from pathlib import Path


#glob find all files in directory/ everything
path= Path()
for file in path.glob('*'):
    print(file)


