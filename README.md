---
title: "SIH Python for Geoscience"
---
# Readme

All of the jupyter notebooks are in the `_ipynb` notebook.

Python for Geoscience SIH materials

Rendered at: https://sydney-informatics-hub.github.io/geopython/

- All notebooks go into `notebooks` folder
- Edit `index.qmd` to change the main landing page.
- Edit `setup.qmd` to change the Setup instruction pages.
- Edit `_quarto.yml` to change the dropdown menu options.
- Add additional `*.md` files to the root dir to have them converted to html files (and add them to `_quarto.yml` to make them navigable).
- Run the below commands to render the notebooks into markdown files and copy everything to the `/docs` folder, which will be what is hosted on the github pages.
- You will need to have jupyter and quarto installed to convert the notebooks and render them for the web.

```
quarto render
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
