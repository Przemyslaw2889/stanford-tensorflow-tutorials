#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 21:12:11 2018

@author: przemyslaw
"""

#Gotta do something with TensorBoard

import tensorflow as tf

#Zeby zwizualizowac program w TensorBoardzie trzeba zapisac log files

a = tf.constant(2, name="a")
b = tf.constant(3, name="b")
x = tf.add(a,b, name="x")
#make sure to create a writer only after you’ve defined your graph, else the graph visualized on TensorBoard would be incomplete.
writer = tf.summary.FileWriter('./graphs', tf.get_default_graph())
with tf.Session() as sess:
    print(sess.run(x))
writer.close()