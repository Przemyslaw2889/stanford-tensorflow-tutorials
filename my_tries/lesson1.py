#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:24:25 2018

@author: przemyslaw
"""

#First tries with tensorflow
import tensorflow as tf

a = tf.add(3, 100)
with tf.Session() as sess:
    print(sess.run(a))
    
x=2
y=3
add_op = tf.add(x,y)
mul_op = tf.multiply(x,y)
useless = tf.add(x, add_op)
pow_op = tf.pow(add_op, mul_op)

with tf.Session() as sess:
    z, not_useless = sess.run([pow_op, useless])
    print(not_useless)
    
