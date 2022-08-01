#! /bin/bash
jupyter-nbconvert --to markdown  _ipynb/*ipynb
wait
mv -v _ipynb/*_files .
mv -v _ipynb/*.md .
cp -v _ipynb/fig/* fig/
Rscript --vanilla siterender.R
rm -rf docs/data
# run the below to copy the files to root so they are appropriately rendered in the final
# GitHub website
# cp -r docs/*files .
# zip -r _additional/data.zip data
# zip -r _additional/notebooks.zip _ipynb
#
