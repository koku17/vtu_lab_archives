# pre-run command :
# mongosh --quiet < lab{1..10}*.js

# edited using vim to only display query,comment and o/p
# can be run on git bash

# archiving command :
# zip -r9 proof.zip out/ assignment.{tex,pdf} run.sh

vim out/*.out
latexmk -pdf -auxdir=tmp/ -shell-escape assignment.tex
rm -rf _minted-*/ tmp/
