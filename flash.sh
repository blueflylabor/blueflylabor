cp ../blueflylabor.github.io/_posts/* ./posts 
git add .
git commit -m "run flash script"
git push
python treeGen.py
