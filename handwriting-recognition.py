{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tensorflow as tf\n",
    "#class defined to handle the callback\n",
    "class myCallback(tf.keras.callbacks.Callback):\n",
    "     def on_epoch_end(self, epoch, logs={}):\n",
    "        if(logs.get('accuracy')>0.4):\n",
    "        print(\"\\nReached 40% accuracy so cancelling training!\")\n",
    "        self.model.stop_training = True\n",
    "\n",
    "mnist = tf.keras.datasets.fashion_mnist\n",
    "\n",
    "(x_train, y_train),(x_test, y_test) = mnist.load_data()\n",
    "x_train, x_test = x_train / 255.0, x_test / 255.0\n",
    "\n",
    "callbacks = myCallback() #instasitate the callback class itself\n",
    "\n",
    "model = tf.keras.models.Sequential([\n",
    "  tf.keras.layers.Flatten(input_shape=(28, 28)),\n",
    "  tf.keras.layers.Dense(512, activation=tf.nn.relu),\n",
    "  tf.keras.layers.Dense(10, activation=tf.nn.softmax)\n",
    "])\n",
    "model.compile(optimizer=tf.optimizers.Adam(),\n",
    "              loss='sparse_categorical_crossentropy',\n",
    "              metrics=['accuracy'])\n",
    "\n",
    "model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
