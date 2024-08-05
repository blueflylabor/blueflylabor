cp ./blueflylabor.github.io/_posts/*.md  ./posts/
python3 tableGen.py
bash ./flash.sh
cd ./blueflylabor.github.io/
bash ./flash.sh
