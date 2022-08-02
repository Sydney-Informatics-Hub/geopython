---
title: "SIH Python for Geoscience"
---
# Readme

All of the jupyter notebooks are in the `_ipynb` notebook.

Python for Geoscience SIH materials

Rendered at: https://sydney-informatics-hub.github.io/geopython/

- All notebooks go into `_ipynb` folder
- Edit `index.Rmd` to change the main landing page.
- Edit `setup.Rmd` to change the Setup instruction pages.
- Edit `_site.yml` to change the dropdown menu options.
- Add additional `*.md` files to the root dir to have them converted to html files (and add them to `_site.yml` to make them navigable).
- Run the below commands to render the notebooks into markdown files and copy everything to the `/docs` folder, which will be what is hosted on the github pages.
- You will need to have jupyter and Rscript installed to convert the notebooks and render them in "Rmarkdown" format.

```
bash _generate_site_from_ipynb.sh
#First time you create the file, add them to be tracked by github, e.g.
git add docs/*
git commit -am "your comments"
git push
```
You can browse the result locally by exploring the html files created (note: sometimes figures display locally but not on web and the other way around too.)

***

When you want to convert the notebooks to pdf for the students, use the following command:

```sh
jupyter nbconvert --execute --to pdf notebook.ipynb
```
