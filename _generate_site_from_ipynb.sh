#! /bin/bash

# Convert notebooks to markdown
jupyter-nbconvert --to markdown  _ipynb/*ipynb
wait
# Move all the generated files to the main dir
mv -v _ipynb/*_files .
mv -v _ipynb/*.md .

# Copy additional "figures" we use in the notebooks
cp -v _ipynb/fig/* fig/

# Render the site from markdown to html.
Rscript --vanilla siterender.R

#Everything without a leading _ will be added, so remove copied stuff you don't want.
rm -rf docs/data

# Update the zip files and then go upload these to cloudstor.
# zip -r _additional/data.zip data
# cd _ipynb; zip -r ../_additional/notebooks.zip *; cd -
