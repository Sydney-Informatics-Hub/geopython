---
title: "SIH Python for Geoscientists"
---
# Readme

Python for geosciences SIH materials

- All notebooks go into `ipynb` folder
- Run the below command to render them into markdown files in the right place

```
conda activate thecorrectenv
cd markdowns
jupyter-nbconvert --to markdown ../ipynb/*ipynb
```

Then open index.Rmd in Rstudio and run:

```r
rmarkdown::render_site()
```

Note: when developing the materials, make sure to create one .Rmd file per jupyter notebook.
