**[summary](#summary) | [prerequisites](#prerequisites) | [setup](#setup) | [resources](#resources) | [license](#license)**

# Transform 2021: Inversion for Geologists

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/simpeg/transform-2021-simpeg/HEAD)
[![License](https://img.shields.io/github/license/simpeg/transform-2021-simpeg.svg)](https://github.com/simpeg/transform-2021-simpeg/blob/master/LICENSE)

|         | Info |
|--------:|:-----|
| When    | Tuesday, April 20 • 20:00 - 22:00 UTC |
| Slack   | [Software Underground](https://softwareunderground.org/) channel `t21-tue-inversion-for-geologists` |
| YouTube | https://youtu.be/5MiaebDwWUQ |
| conda environment  | `t21-tue-simpeg` |
| Slides  | [SimPEG Transform presentation](http://bit.ly/transform-2021-slides) |

**Team**
- [Seogi Kang](https://github.com/sgkang) (Instructor)
- [Lindsey Heagy](http://github.com/lheagy) 
- [Doug Oldenburg](http://github.com/dougoldenburg)
- [Dom Fournier](https://github.com/fourndo)
- [Joe Capriotti](https://github.com/jcapriot)
- [Dieter Werthmüller](http://github.com/prisae)
- and the [SimPEG contributors](https://github.com/simpeg/simpeg/graphs/contributors)

## Before the tutorial

Make sure you've done these things before the tutorial on Tuesday:

1. Sign-up for the [Software Underground Slack](https://softwareunderground.org/slack)
1. Join the channel `t21-tue-inversion-for-geologists`. This is where **all communication will happen**.
1. Set up your computer ([instructions below](#usage)). We will not have time to
   solve many computer issues during the tutorial so make sure you do this
   ahead of time. If you need any help, ask at the `t21-tue-inversion-for-geologists` channel on
   Slack.
1. If you have some data you'd like to process, please have it ready and make
   sure you can load it with pandas or numpy. You'll have some time at the end
   of the tutorial to work on your own data.

## Summary

This repo contains the notebooks and tutorial resources for the Transform 2021 tutorial on Inversion for Geologists. 
In this tutorial, we will provide fundamental concepts about the inversion framework. As a motivating example, 
we will use the magnetic data acquired at [Raglan deposits](https://en.wikipedia.org/wiki/Raglan_Mine) in Northern Quebec, Candada. 
About 20 years ago, this magnetic data set was inverted in 3D (sort of the first time), and resulting susceptiblity model 
played an imporant role for spotting a drill hole, which found mineralized zones. 


Starting from field data in a text file we will learn how to
- load those data into SimPEG
- construct a survey object that contains the geometry of the sources and receivers
- set up and run a forward simulation
- define the inverse problem consisting of a data misfit and regularization
- run an inversion and discuss inversion strategies

Then, we will work with a synthetic example to
- demonstrate how to explore aspects of the physics with SimPEG
- explore the role and influence of parameters used in an inversion

## Prerequisites

**Software**

* Some knowledge of Python is assumed.
* All coding will be done in Jupyter notebooks. I'll explain how they work
  briefly but it will help if you've used them before.
* We'll use [numpy](https://numpy.org/), [matplotlib](https://matplotlib.org/), and
  [ipywidgets](https://ipywidgets.readthedocs.io/)
  You don't need to be an expert in these tools but some familiarity will help.

**Geophysical Inversions**

* This tutorial will focus on providing fundamental concepts of the geophysical inversion. 
  I do not assume an extensive background in inversions, but it will help if you have been
  introduced to some concepts. The [Inversion Module](https://curvenote.com/@geosci/inversion-module/inverse-theory-overview)
  provides a nice overview.
* As a motivating example, I will use magnetic mehod. 
  I'll explain the basic principles, but if these are new to you, then I would recommend
  taking a read through the [Magnetics](https://gpg.geosci.xyz/content/magnetics/index.html).

## Usage

There are a few things you'll need to follow the tutorial:

1. A working Python installation ([Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html))
2. The SimPEG *conda environment* installed
3. A web browser that works with Jupyter
   (basically anything except Internet Explorer)

To get things setup, please do the following.

**If you have any trouble**, please ask for help in the
`t21-tue-inversion-for-geologists` channel on the Software Underground slack.

**Windows users:** When you see "*terminal*" in the instructions,
this means the "*Anaconda Prompt*" program for you.

### Step 1: Python

**Follow the general instructions for Transform2021:** https://www.youtube.com/playlist?list=PLgLft9vxdduAW-jmhYqXvtfGYJS6v2FjM

This will get you a working Python 3 installation with the `conda` package
manager. If you already have one, you can skip this step.

### Step 2: Download the SimPEG tutorials

To access the notebooks, there are 3 options (in order of preference):
1. Use git to clone this repository
2. From GitHub, you can use the `download` option to download this repository as a zip file (follow all instructions below, replacing the `git clone` step with download and unzip the zip file with the repository contents.
3. You can run the notebooks online with binder through: https://mybinder.org/v2/gh/simpeg/transform-2021-simpeg/master

To clone this repository, open up a terminal and navigate to where you want this repository stored on your computer.

Then run
```
git clone https://github.com/simpeg/transform-2021-simpeg.git
```
to clone the repository, and `cd` into the `transform-2021-simpeg` directory
```
cd transform-2021-simpeg
```

### Step 3: Create the SimPEG tutorial conda environment

From inside of the `transform-2021-simpeg` repository, create the `t21-tue-simpeg` conda environment
```
conda env create -f environment.yml
```
and activate the environment
```
conda activate t21-tue-simpeg
```

### Step 4: Launching the notebooks

Once you have activated the conda environment, you can launch the notebooks
```
jupyter notebook
```
Jupyter will then launch in your web-browser.

If you are able to open any one of the notebooks and run the first cell, then you should be good to go!
If you run into issues, please post in the #t21-tue-simpeg slack channel.

## Resources

**Resources on Geophysics and Inversions**
- [Geophysics for Practicing Geoscientists](https://gpg.geosci.xyz/)
- [Inversion Module](https://curvenote.com/@geosci/inversion-module/inverse-theory-overview)
- [SimPEG](https://www.simepg.xyz)

**Resources on SimPEG**
- [Docs](http://docs.simpeg.xyz/)
- [Discourse](http://simpeg.discourse.group/)
- [Slack](http://slack.simpeg.xyz/)
- [This Tutorial](https://github.com/simpeg/transform-2021-simpeg/)


## License

All code and text in this repository is free software: you can redistribute it and/or
modify it under the terms of the MIT License.
A copy of this license is provided in [LICENSE](LICENSE).
