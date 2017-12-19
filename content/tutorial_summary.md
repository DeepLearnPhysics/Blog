Title: Tutorials
Date: 2017-12-19 00:00
Modified: 2017-12-19 00:00
Category: tutorial
Tags: python, larcv
Slug: tutorial_summary
Authors: Kazuhiro Terao
Summary: Summary of tutorial contents

If you are looking for "how to get started" with hands-on experience, you are in the right place.
Below is a summary of tutorials made available voluntarily by our group members.
The most (if not all) of them are written in `python`, and in fact in _jupyter_ `notebook` format.

### **Installing Jupyter Notebook**
Jupyter notebook is not a requirement for using our software, but we share lots of examples in this format. 
So you might want to install it if you don't have one. Installation is same as many other python packages.

1. If you don't have it, install either [pip](https://pypi.python.org/pypi/pip) or [conda](https://conda.io/docs/index.html) python package manager.
2. Either [pip install](https://pip.pypa.io/en/stable/reference/pip_install/) or [conda install](https://conda.io/docs/commands.html) `jupyter`.

You might find a few glitches. Try googling a solution by copy-and-paste the error message (usually "package X not found") in the browser.

**Additional packages**: other extremely useful python packages include `numpy`, `scipy`, `matplotlib`, `scikit-learn`, and `scikit-image`.
**Optional packages**: want more? you can install `tensorflow` and `pyqtgraph`!

## <a name="quickstart"></a>**Quick Start**
Before starting, `git clone` our [tutorial repository](https://github.com/DeepLearnPhysics/larcv-tutorial). All notebooks in this section can be found there (and you can execute/run the notebook by yourself as you follow the tutorial).

* [Jupyter Notebook](tutorials/tutorial-00.html)
	* Introduction, very brief on our end. Features awesome [Brilliantly wrong](http://arogozhnikov.github.io/2016/09/10/jupyter-features.html) blog post by Alex Rogozhnikov)
* [larcv Installation](tutorials/tutorial-01.html)
	* How to install `larcv` software (our C++ framework for file IO and image processing)
* [Opening larcv Data File](tutorials/tutorial-02.html)
	* What's in the file? Shows how to access images as numpy arrays and visualize them.
* [Storing larcv Data File](tutorials/tutorial-03.html)
	* Brief demo on how to store your own data.
* [Reading larcv Data File _Fast_](tutorials/tutorial-04.html)
	* Covers the basics of the tool you will be using for training a network.

## **Training on Open Data**<a name="opendata"></a>
Like [Quick Start](#quickstart), you can find notebooks used for tutorials below in our [tutorial repository](https://github.com/DeepLearnPhysics/larcv-tutorial). But these examples use simulated liquid argon time projection chamber in our [public data](http://deeplearnphysics.org/DataChallenge).

* [Image classification training](tutorials/tutorial-05.html)
	* Train a network to classify an image containing one of 5 particles (e-, gamma, mu-, pi+, proton).
* [Image classification inference](tutorials/tutorial-06.html)
	* Example of how to run an _analysis_ (inference) using the trained network's weights.
* Semantic segmentation training
	* coming soon
* Semantic segmentation inference
	* coming soon

## **LArCV** <a name="larcv"></a>
Coming soon