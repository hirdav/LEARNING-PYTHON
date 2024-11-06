from pathlib import Path
path=Path('the_advantages_of_DBMS.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines :
    print (line) 