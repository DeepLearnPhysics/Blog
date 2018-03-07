Title: ThreadProcessor: speed
Date: 2018-03-06 00:00
Modified: 2018-03-06 00:00
Category: larcv
Tags: larcv, thread processor
Slug: 2018-03-06-Threadprocessor
Authors: Kazuhiro Terao
Summary: Here's a report for a naive data rate profiling of ThreadProcessor, larcv's threaded data reader we often use for network training. Measured on my macbook pro early 2013 model (old!) but reproduced similar numbers on dell xps15 (9560).

`ThreadProcessor` is an API to multi-thread data loading from `larcv` files for efficient training of a deep neural network. I recently added a [__wiki page__](https://github.com/DeepLearnPhysics/larcv2/wiki/ThreadProcessor) that describes how the internals work. There are a few notebooks in our [__tutorial__](http://deeplearnphysics.org/Blog/tutorial_summary.html#tutorial_summary) that can be used as a reference. [__One__](http://deeplearnphysics.org/Blog/tutorials/tutorial-04.html) for simple access to data contents, [__another__](http://deeplearnphysics.org/Blog/tutorials/tutorial-05.html) on image classification and [__one more__](http://deeplearnphysics.org/Blog/2018-01-05-TrainingSegmentationData_v0.1.0.html) on semantic segmentation training.

I hope that was enough references to learn about it :) because this blog post is not about how to use it, but instead I share some findings from simple speed profiling test with different configurations. This study was prompted by reports from [__Taritree Wongjirad__](http://sites.tufts.edu/wongjiradlab/people/) after finding some cases where the performance of the code became bad = slow (thanks Tari!).

## Set up
We use [__test_10k.root__](http://www.stanford.edu/~kterao/public_data/v0.1.0/2d/segmentation/multipvtx/test_10k.root) from our [__public data set__](http://deeplearnphysics.org/DataChallenge/) as an input. [__This__](https://github.com/DeepLearnPhysics/larcv2/tree/85f68f5387e6e6ee5531a4b6a502d4fc5b99b2fe) is the version of larcv and a [__script__](https://github.com/DeepLearnPhysics/larcv2/blob/85f68f5387e6e6ee5531a4b6a502d4fc5b99b2fe/larcv/app/ThreadIO/test/dataloader_test.py) I used to produce the results.

Below you see different configurations I compared the results for. The tests were run on my macbook pro (16GB RAM, SSD, early 2013) as well as dell XPS15 (32GB RAM, SSD, model 9560) and show similar results (agreement on each measurement within ~10%). The actual data rate measured strongly depend on a) hardware specs and b) configurations (such as RAID mode). So take numbers as a grain of salt, and try to measure this on your system ([__click here__](#demo) for instructions).

## Thread counts
The reason why we have multi-threaded file reader is so that we can CPU for data read while GPU is busy training a network. However, multi-threading can speed up data read speed even in CPU-only mode because our data is heavily compressed in our file = multiple threads can parallelize decoding of compressed data and file read tasks. Below, you see the comparison of an average data read speed measured every 1 second. The vertical axis shows the amount of data decoded and made available on RAM and the horizontal axis shows time elapsed since the beginning of executing the script. We can see there's almost a linear gain when we increase number of threads to 2, and then still a good fraction of increase but no longer linear when increasing to 3 threads. The increase from 3 to 4 threads is still clear but much smaller. Then finally 5 threads do not help any more.

<center>
<figure>
<img src="imgs/2018-03-06-ThreadProcessor-Threads.png" title="Thread Counts" style="width:75%">
</figure>
</center>

## Data access, copy vs. pointer wrapper

Here we vary two configurations: `RandomAccess` configuration parameter of `ThreadProcessor` and `make_copy` configuration parameter of `dataloader2`, a dedicated python API. For `RandomAccess`, there are 3 possible values: `0` = no random entry access from the input file(s), `1` = completely randomize the entry to access, or `2` = access the random slice of input data. Among these options, `0` is the cheapest since it follows the order of data entries in a file. `1` is the most expensive as it requires a file header to move from one entry to another. The fact that each entry size varies in our data format makes this even slower. `2` is a simple intermediate solution between them by making only the first entry of a particularly sized data slice random.

`make_copy` is a configuration specific to `dataloader2`, a python layer, and does not affect underlying `ThreadProcessor` C++ API. It is `False` by default in which case numpy array of loaded data is a mere pointer wrapper on underlying C array that is owned by `ThreadProcessor`. When set to `True`, `dataloader2` prepares a dedicated `numpy` array buffer to hold loaded data from C++ API and runs an explicit data copy. Although it can be expensive due to copying, it can be useful sometimes when you want to massage `numpy` data without affecting underlying C++ data handling.


<center>
<figure>
<img src="imgs/2018-03-06-ThreadProcessor-AccessMethods.png" title="Access Methods" style="width:75%">
</figure>
</center>

The plot above shows the data-read speed in MB/s (mega-byte-per-second) measured as a function of elapsed time in seconds. The legends show configuration of two parameters. We can clearly see that the biggest slow down is caused by setting `RandomAccess=1`, almost 8 times slower than the two optimal configurations (red and purple). Comparing green (Copy+Random Slice) vs. purple (Wrap+Random Slice), we can see how data copy can affect the speed performance by almost a factor of 2. Finally, from the comparison of red (Wrap+No Random) and purple (Wrap+Random Slice), we see there is virtually no slow down by allowing slicing point to be randomly set. Therefore we see that `RandomAccess=2` and `make_copy=False` (latter is default) seems like a good point to sit.

<a name="demo"></a>
## Do It Yourself
Here's asciinema (loving it!) video for running the test script at a GPU tower I often use.

<script src="https://asciinema.org/a/O5pcRgMSkeq9Woy8nkMjuh6aM.js" id="asciicast-O5pcRgMSkeq9Woy8nkMjuh6aM" async data-theme="monokai"></script>

