#coding:utf-8

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import mnist_forward
import mnist_backward
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
TEST_INTERVAL_SECS = 5

class TrainThread(QThread):
    logOut = pyqtSignal(str)
    running = False
    def __init__(self):
        super().__init__()
        
    def stop(self):
        self.running = False
    
    def run(self):
        if (self.running):
            return
        self.running = True
        mnist = input_data.read_data_sets("./data/", one_hot=True)

        with tf.Graph().as_default() as g:

            x = tf.placeholder(tf.float32, [None, mnist_forward.INPUT_NODE])

            y_ = tf.placeholder(tf.float32, [None, mnist_forward.OUTPUT_NODE])
            y = mnist_forward.forward(x, None)
    
            ema = tf.train.ExponentialMovingAverage(mnist_backward.MOVING_AVERAGE_DECAY)
            ema_restore = ema.variables_to_restore()
            saver = tf.train.Saver(ema_restore)
    
            correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    
            while self.running:
                with tf.Session() as sess:
                    ckpt = tf.train.get_checkpoint_state(mnist_backward.MODEL_SAVE_PATH)
                    if ckpt and ckpt.model_checkpoint_path:
                        saver.restore(sess, ckpt.model_checkpoint_path)
                        global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                        accuracy_score = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
                        if (self.running) :
                            print("After %s training step(s), test accuracy = %g" % (global_step, accuracy_score))
                        else:
                            return
                        self.logOut.emit("After " + global_step + " training step(s), test accuracy = " + str(accuracy_score) + "\n")
                    else:
                        print('No checkpoint file found')
                        self.logOut.emit("No checkpoint file found \n")
                        return
                time.sleep(TEST_INTERVAL_SECS)

    

