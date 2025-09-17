import os
dir = './posts/'
mds = os.listdir(dir)
mds.sort()
lis = []
url = 'https://github.com/blueflylabor/blueflylabor/blob/master/md/'
for i in mds:
    st = '- [' + i.split('.md')[0] + '](' + url + i + ')'
    lis.append(st)
lis.sort()
lis.reverse()

rd0 = """# Welcome to my homepage

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

![Programming Languages](https://skillicons.dev/icons?i=c,cpp,matlab,python,bash,java,latex)

### Tools

![Tools](https://skillicons.dev/icons?i=linux,mysql,docker,nginx,pytorch,git,numpy,matplotlib)

### Learning

![Currently Learning](https://skillicons.dev/icons?i=cpp,go,pytorch)

### Stats

<a href="https://github.com/blueflylabor">
<img height="190" src="https://github-readme-stats-psi-amber.vercel.app/api?username=blueflylabor&count_private=false&show_icons=true&include_all_commits=false" />
</a>
<a href="https://github.com/blueflylabor">
<img height="190" src="https://github-readme-stats-psi-amber.vercel.app/api/top-langs/?username=blueflylabor&layout=compact&langs_count=8" />
</a>

![Map](https://mapmyvisitors.com/map.png?cl=ffffff&w=a&t=n&d=mDCIvYPIKRouJHRiYO6dqK_22eqhTKe0NbwHcydn2l4)


## Markdown Table 


"""

rd = open('./README.md', '+w')
rd.write(rd0)
for i in lis:
    rd.write(i + '\n')
rd.close()