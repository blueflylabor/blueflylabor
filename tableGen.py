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

![Map](https://rf.revolvermaps.com/h/m/a/0/ff0000/128/0/5h6pyj9unzd.png)

## Website
- [new site](https://www.cnblogs.com/blueflylabor)
- [old site](https://www.cnblogs.com/Carrawayang)
- [blueflylabor.github.io](https://blueflylabor.github.io)

Hi guys, welcome!

Here is blueskylabor.

![](https://komarev.com/ghpvc/?username=blueflylabor)

### Languages

![中文](https://img.shields.io/badge/%E4%B8%AD%E6%96%87-%E2%98%85%E2%98%85%E2%98%85%E2%98%85%E2%98%85-green?style=flat-square)
![English](https://img.shields.io/badge/English-%E2%98%85%E2%98%85%E2%98%85%E2%98%86%E2%98%86-green?style=flat-square)
![Deutsch](https://img.shields.io/badge/Deutsch-%E2%98%85%E2%98%86%E2%98%86%E2%98%86%E2%98%86-green?style=flat-square)

### Programming Languages

![Programming Languages](https://skillicons.dev/icons?i=c,c++,matlab,python3,bash,java,cuda,latex)

### Tools

![Tools](https://skillicons.dev/icons?i=linux,mysql,docker,nginx,pytorch,git,numpy,matplotlib)

### Learning

![Currently Learning](https://skillicons.dev/icons?i=cpp,cuda,pytorch,ml,dl)

### Stats

<a href="https://github.com/blueflylabor">
<img height="190" src="https://github-readme-stats-psi-amber.vercel.app/api?username=blueflylabor&count_private=false&show_icons=true&include_all_commits=false" />
</a>
<a href="https://github.com/blueflylabor">
<img height="190" src="https://github-readme-stats-psi-amber.vercel.app/api/top-langs/?username=blueflylabor&layout=compact&langs_count=8" />
</a>

## Markdown Table 

"""

rd = open('./README.md', '+w', encoding="utf-8")
rd.write(rd0)
rd.write(title)
for i in mdline:
    rd.write(i + '\n')
rd.close()
print(">>>Info : Success gen table")
