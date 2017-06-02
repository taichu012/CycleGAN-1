import tensorflow as tf
from Unet import UNet

class Discriminator():
    def __init__(self, image, ini):
        h0 = tf.nn.relu(tf.layers.batch_normalization(tf.layers.conv2d(image, filters=64, kernel_size=[3,3], strides=(2,2), padding='SAME',name=ini+'_h0_conv')))
        h1 = tf.nn.relu(tf.layers.batch_normalization(tf.layers.conv2d(h0, filters=128, kernel_size=[3,3], strides=(2,2), padding='SAME', name=ini+'_h1_conv')))
        h2 = tf.nn.relu(tf.layers.batch_normalization(tf.layers.conv2d(h1, filters=256, kernel_size=[3,3], strides=(2,2),padding='SAME', name=ini+'_h2_conv')))
        h3 = tf.nn.relu(tf.layers.batch_normalization(tf.layers.conv2d(h2, filters=512, kernel_size=[3,3], strides=(2,2),padding='SAME', name=ini+'_h3_conv')))
        self.last_h = tf.layers.dense(tf.reshape(h3, [-1,32*32*512]), 1, name=ini+'_dense_layer')
        self.out = tf.nn.sigmoid(self.last_h,name='out')
