# Blog
A repository for DeepLearnPhysics group [Blog](https://deeplearnphysics.org/Blog) webpage.
The `master` branch holds static HTML files generated by [Pelican](http://docs.getpelican.com/en/stable/) with [flex theme](https://github.com/alexandrevicenzi/Flex). We use [pelican-ipynb](https://github.com/danielfrg/pelican-ipynb) plugin to easily turn a juypyter notebook into a blog.
The `develop` branch holds source code to generate the website.

### Requirement
Besides [Pelican](http://docs.getpelican.com/en/stable/), there are additional [requirements for ipynb plugin](https://github.com/danielfrg/pelican-ipynb). Follow the link and install them if you want to use this plugin.

You also need markdown (pip install markdown) (maybe sudo required).

### How to contribute
For aweome you to help development, follow the following steps
1. Join [web-blog](https://github.com/orgs/DeepLearnPhysics/teams/web-blog) github team
2. Install [Pelican](http://docs.getpelican.com/en/stable/) ... here's [quick start](http://docs.getpelican.com/en/stable/quickstart.html#).
3. Clone the repo: `git clone git@github.com:DeepLearnPhysics/Blog`

You should be on the `develop` branch by default. To generate static website:

4. `make html`

To view the locally generated website (good idea before pushing!):

5. `make devserver` then access `localhost:8000` on your browser.

Finally, to make modification & test:

6. Make modifications you need, then `make html`. If you did step 5., you can check the change in the output in `localhost:8000`
7. Maybe good ide: change `SITEURL` in `pelicanconf.py` to `""` (empty string). This ensures generated static sites to use locally modified js/css under theme dir.

Note that `output` directory holds locally generated static HTML files. `output` directory is excluded from `develop` branch via `.gitignore` intentionally.
Ready to publish? Here are the steps.

8. If you did step 5, `make stopserver`. If you did step 7, `undo` it. Then commit & push your change to `develop` branch. 
9. Make sure `develop` branch has no modifications by `git status`.
10. `git checkout master`, then `cp -r output/* ./` (this simply replaces the old page source with your new ones)
11. `git add .` && `git commit -m "updated"` && `git push`

Done!

---

### Jupyter notebook
The following is an instruction copied from [pelican-ipynb](https://github.com/danielfrg/pelican-ipynb) plugin repository.

Write the post using the Jupyter Notebook interface, using markdown, equations, etc.

Place the `.ipynb` file in the content folder and create a new file with the
same name as the ipython notebook with extension `.ipynb-meta`.
For example if you have `my_post.ipynb` create a `my_post.ipynb-meta`.

The `.ipynb-meta` should have the markdown metadata (note the empty line at the end, you need that)
of a regular pelican article:

```
Title:
Slug:
Date:
Category:
Tags:
Author:
Summary:

```

---

### Copyright and license

It is under [the MIT license](/LICENSE).
