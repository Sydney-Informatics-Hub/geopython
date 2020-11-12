#! /bin/bash
jupyter-nbconvert --to markdown  _ipynb/*ipynb
wait
cp -r _ipynb/*_files .
rm -r _ipynb/*files
mv _ipynb/*md .
Rscript --vanilla siterender.R
# run the below to copy the files to root so they are appropriately rendered in the final 
# GitHub website
cp -r docs/*files .
