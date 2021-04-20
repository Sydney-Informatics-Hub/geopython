---
title: "SIH Python for Geoscientists"
---
# Readme

All of the jupyter notebooks are in the `_ipynb` notebook.

Python for geosciences SIH materials

Rendered at: https://sydney-informatics-hub.github.io/geopython/

- All notebooks go into `_ipynb` folder
- Run the below command to render them into markdown files in the right place

```
bash _generate_site_from_ipynb.sh
#Generally add whatever files you have created
git add docs/*_files/*
git add *_files/*
git commit -am "your comments"
git push
```
You can browse the result locally by exploring the html files created (note: sometimes figures display locally but not on web and the other way around too.)

***

When you want to convert the notebooks to pdf for the students, use the following command:

```sh
jupyter nbconvert --execute --to pdf notebook.ipynb
```
