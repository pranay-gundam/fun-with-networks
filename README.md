# fun-with-networks

Authors: Pranay Gundam and Anouska Siva

## Introduction

I'm currently reading this book called *The Human Network* by Matthew O. Jackson. It's the first book on networks that I have read and its giving me reminders every now and then that I am actually really interested in networks because of the applications of graph theory and how introductory of a data structure they are which makes it a good teaching tool for beginner coders. This repo is simply a little code I (along with the gf Anouska Siva) was inspired to write and a nice practice in data structures. I'm honestly not sure where I would use this code right now but was just urging to write it so here it is.

## Basic Features

There is some very basic code that builds un-weighted/weighted and un-directed/directed graphs. At their core, graphs consist of a collection of nodes and edges; there is a little additional nuance one can add in the form of weighting edges or directing edges but this is not to difficult of a facility to add.

The functionalities of the objects themselves involve getting and setting the relevant attributes of nodes and edges and there is some in-built protection such that un-directed edges cannot reveal some inherent ordering of the edges. The way graphs are implemented in this code base leaves some room for speed improvements but this is an issue I am leaving up to the analysis part of this codebase.
