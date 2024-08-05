import os, time
def t(f):
    ti = os.path.getctime(f)
    til = time.localtime(ti)
    return time.strftime("%Y-%m-%d %H:%M:%S", til)

def t_c(f):
    ti = os.path.getatime(f)
    til = time.localtime(ti)
    return time.strftime("%Y-%m-%d %H:%M:%S", til)

dir = './posts/'
name = os.listdir(dir)
print(">>>File : " + str(len(name)) + " files")
mdline = []
url = 'https://github.com/blueflylabor/blueflylabor/blob/master/posts/'
for i in name:
    link = '[' + i.split('.md')[0] + '](' + url + i + ')'
    mdline.append("|" + t_c(dir + i) + "|" + t(dir + i) + "|" + link)

mdline.sort()
mdline.reverse()

title = """
|created date|lastest modified date|markdown links|
|-|-|-|
"""

rd0 = """# Welcome to my homepage

![blueflylabor's GitHub stats](https://github-readme-stats.vercel.app/api?username=blueflylabor&count_private=true&theme=dark)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs?username=blueflylabor&layout=compact&count_private=true&theme=dark)

![Map](rf.revolvermaps.com/h/m/a/0/ff0000/128/0/5h6pyj9unzd.png)

## Website
- [new site](https://www.cnblogs.com/blueflylabor)
- [old site](https://www.cnblogs.com/Carrawayang)
- [blueflylabor.github.io](https://blueflylabor.github.io)

## Markdown Table 

"""

rd = open('./README.md', '+w', encoding="utf-8")
rd.write(rd0)
rd.write(title)
for i in mdline:
    rd.write(i + '\n')
rd.close()
print(">>>Info : Success gen table")
