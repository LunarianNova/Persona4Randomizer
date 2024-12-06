import glob, os, random, time
from shutil import copy2
from shutil import rmtree
print('EX: D:\\Modding\\P4G\\data_e')
odir = input('Unpacked data_e dir: ')
try:
    rmtree('RandomMod')
except:
    pass
os.mkdir('RandomMod')
os.mkdir('RandomMod\\data_e')
with open('RandomMod\\Package.xml', 'w+') as f:
    f.write("""<?xml version="1.0"?>
<Metadata xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <name>Randomized Things</name>
    <id>megiryuu.randomizedthings</id>
    <author>Megiryuu</author>
    <version>1</version>
    <link/>
    <description>Does some random things</description>
    <skippedVersion>all</skippedVersion>
</Metadata>""")


def randomize(dirfrom, filetype):
    files = glob.glob(dirfrom+"\\**\\*." + filetype, recursive=True)
    names = []
    for file in files:
        names.append(file)
    for file in files:
        n = random.randint(0, len(names)-1)
        name = names[n]
        copy2(odir + file.split(odir.split('\\')[-1])[1], os.path.dirname(__file__) + "\\RandomMod\\data_e\\" +
              name.split(odir.split('\\')[-1])[1])
        names.pop(n)


os.mkdir('RandomMod\\data_e\\bustup')
randomize(odir+"\\bustup", 'bin')
os.mkdir('RandomMod\\data_e\\model')
folders = ['field', 'npc', 'npc2', 'persona', 'symbol', 'weapon']
for folder in folders:
    os.mkdir('RandomMod\\data_e\\model\\'+folder)
randomize(odir+"\\model", 'amd')
os.mkdir('RandomMod\\data_e\\model\\pack')
randomize(odir+"\\model\\pack", 'pac')
print('Finished, copy the "RandomMod" directory to the persona 4 golden packages folder.')