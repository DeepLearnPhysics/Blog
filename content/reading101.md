Title: Getting started: paper readings
Slug: reading101
Date: 2017-12-19 00:00
Modified: 2017-12-19 00:00
Category: tutorial
Tags: paper
Authors: Kazuhiro Terao
Summary: List of useful papers for beginners' reading

This is a message I compiled once for myself but also share with my students etc..
You can easily find a similar compilation of papers on people's github: just google it :) 
But here's just one of those for our group's reference.

I list them in an order of history, hoping this allows you to skip some toward the beginning.
I put “**recommended**” next to the paper i think it’s good/important to read.

## **Modern CNN**

* 2012 [Drop-out](https://arxiv.org/pdf/1207.0580.pdf) (**recommended**)
	* A big jump in training technique to avoid over-fitting and improve final accuracy, key technique for AlexNet

* 2012 [AlexNet](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf) (**recommended**)
	* Legendary debut of CNN, first implementation on GPU by Hinton (prof. U. of Toronto), Alex (now Google), and Ilya (now OpenAI), dramatic performance improvement on ILSVRC, annual competition of image recognition from the last year in both accuracy and speed of processing (previous year based on fisher vector machine). First time CNN was applied on 224x224x3 tensor image.

* 2014 [VGG](https://arxiv.org/abs/1409.1556)
	* First systematic approach to understand the effect of network depth using a homogeneous network architectures (all 3x3 kernel convolutions + 2x2 pooling layers)

* 2014 [GoogLeNet](https://arxiv.org/abs/1409.4842)
	* First “Inception” network idea

* 2015 [Batch Normalization](https://arxiv.org/abs/1502.03167) (**recommended**)
	* Another big jump in training techniques to make dependency on initial weights smaller, making training dramatically easier (avoids over-fitting)

* 2015 [ResNet](https://arxiv.org/abs/1512.03385) (**recommended**)
	* First “ResNet” idea, surpassed human average accuracy on ILSVRC data set. Technique allowed to train 1000 layer deep network, jaw-dropping for researchers who have been competing to make network deeper and deeper since GoogLeNet and VGG. This technique development was a huge deal, and ResNet is current default choice for constructing a deep network architecture today.

* 2015 [Faster-RCNN](https://arxiv.org/abs/1506.01497) (**recommended**)
	* First real-time object detection by neural network (I think it was 20~30 Hz, which is > 60Hz today with advanced version). Elegant technique to piggy-back detection network on top of any image recognition network. Region Proposal Network (RPN), part of Faster-RCNN development originally for an object detection (in this paper), is today cooked further and used by the best semantic segmentation network today.

* 2015 [DC-GAN](https://arxiv.org/pdf/1511.06434.pdf) (**recommended**)
	* First generative-adversarial-network which looks like the machine has learned a concept of real world image. Super popular for the network accurately generating images of a bedroom and bathroom (toilet).

* 2016 [FCN](https://arxiv.org/abs/1605.06211) (**recommended**)
	* First solid implementation of CNN for semantic segmentation. > 1500 citations! Still used today as a standard candle of accuracy. Not the best accuracy in the field but extremely fast learning, simple architecture.

* 2016 [R-FCN](https://arxiv.org/abs/1605.06409)
	* Detection network improved by combining FCN with Faster-RCNN to improve the detection (first find pixels, then draw boudning box, makes sense!). First segmentation=>detection=>classification work flow.  … note “Kaming He” :)

* 2016 [Inception-V4, Inception-ResNet](https://arxiv.org/abs/1602.07261) (**recommended**)
	* Hey let’s improve image classification even more… here’s huge network by Google, the latest Inception module, studied by combining with ResNet.

* 2016 [Wide-ResNet](https://arxiv.org/abs/1605.07146) (**recommended**)
	* Empirical study to answer the question of What-is-the-“depth”-in-ResNet? The group found that ResNet actually performs better by making it “wider” rather than “deeper”.

* 2016 [Wider-or-Deeper ResNet?](https://arxiv.org/abs/1611.10080) (**recommended**)
	* Analytical explanation and analysis of the observation made in the previous paper. Very well written. Demonstrated the importance of the width to image classification and semantic segmentation

* 2016 [Instance-sensitive Fully Convolutional Network (IS-FCN)](https://arxiv.org/abs/1603.08678) … (**recommended**)
	* Extension of R-FCN, improved design architecture to win the ILSVRC semantic segmentation competition 2016 … note “Kaming He” :)

* 2016 [Aggregated Residual Transformations: ResNeXt](https://arxiv.org/abs/1611.05431) (**recommended**)
	* Introduces a new dimension, named "cardinality" (the size of the set of transformations), claimed as yet another effective direction to improve the accuracy besides "width and depth".

* 2017 [Mask R-CNN](https://arxiv.org/abs/1703.06870) (**recommended**)
	* Kaming He’s latest work that already beated IS-FCN, our current target to implement for instance-aware semantic segmentation for particle clustering.

* 2017 [Shattered Gradient Problem](https://arxiv.org/abs/1702.08591)
	* If resnets are the answer, what is the question?

* 2017 [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507) (**recommended**)
	* First detailed study for enhancing the "channels" of the tensor to encode image features instead of spatial dimensions (width/height) of images.
