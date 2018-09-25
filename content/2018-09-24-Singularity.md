Title: Singularity container
Date: 2018-09-24 00:00
Modified: 2018-09-24 00:00
Category: container
Tags: singularity, container, software
Slug: 2018-09-24-Singularity
Authors: Kazuhiro Terao
Summary: Long due blog post about our singularity container use!

Recently I gave a DLP workshop/tutorial at Brookhaven National Lab (BNL), and one of the successful outcome was sharing our use of singularity. __[**Brett Viren wrote a blog post**](https://wirecell.github.io/news/posts/singularity-containers-for-wct-and-wcls-running-and-development/)__ about how it can simplify lives of WireCell users! So I decided to write this blog post, which was long due, about our use of a singularity container.

## Singularity-Hub
We use __[singularity](http://singularity.lbl.gov)__ to distribute our software, and we use [the singularity hub](https://singularity-hub.org). We maintain our singularity recipe in __[**the github repository**](https://github.com/DeepLearnPhysics/larcv2-singularity)__, and here is __[**our collection on singularity-hub**](https://singularity-hub.org/collections/459)__ which is set to automatically produce and build container images. Our github repository describes three types of images we produce. Today how to run our work environment is as simple as:
```
singularity exec --nv shub://DeepLearnPhysics/larcv2-singularity bash
```
Though I usually pull an image file and execute locally
```
singularity pull -n local.img shub://DeepLearnPhysics/larcv2-singularity
singularity exec --nv local.img bash
```

## Wiki page
Probably some of us are interested in how to build a container, not just pulling an image from the hub. I wrote __[**a wiki page**](https://github.com/DeepLearnPhysics/playground-singularity/wiki)__ with some example code to build simple containers. This should get you up to speed with writing a container recipe that generates our container images on the singularity-hub. Your contributions to improve this example/documentation would be very much welcome. Let us know and we'll include them or simply give you a permission to update the wiki ;)

## Where to use?
I use singularity and our image to setup a work environment on my laptop, desktop, a dedicated GPU server machine for my group as well as shared GPU resources (cluster and grid). It's great: I managed to start training my deep neural network model within 5 minutes since the delivery of a new GPU server which runs an OS (CentOS) I am not familiar with. I have had successful experience with all summer students jumping straight into machine learning research work thanks to Singularity. 

In fact, I no longer recommend to compile larcv from source, __[a step in our tutorial](http://deeplearnphysics.org/Blog/tutorials/tutorial-01.html)__. It's really important for a short-term students/contributors to be able to get to the core of their project. Yep, we should put aside our fun of teaching them how to compile source and generate/link libraries sometimes. Thanks to the world of awesome people for introducing a container, and the singularity team for a particularly handy software!






