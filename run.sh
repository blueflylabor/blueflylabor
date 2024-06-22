cp ./blueflylabor.github.io/source/_posts/*.md  ./posts/
cd ./blueflylabor.github.io/
hexo d
hexo g
cd ..
python3 tableGen.py
bash ./flash.sh
