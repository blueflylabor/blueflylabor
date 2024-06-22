cp ./blueflylabor.github.io/source/_posts/*.md  ./posts/
hexo d
hexo g
python3 tableGen.py
bash ./flash.sh
