##Abhishek Subhash Swami 21 AIML
#Demonstration of simple machine learning program for line y=2x-1


#given list of values of x
X=[-1,-2,-3,-4,-5,6,7,8,9,10]
Y=[]

#generating y values from given equation
for number in X:
    Y.append(2*number-1)
print(Y)

import tensorflow as tf
import numpy as np
from tensorflow import keras

model1=tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
model1.compile(optimizer='sgd',loss='mean_squared_error')
print(model1.summary())

x=np.array(X)
y=np.array(Y)
model1.fit(x,y, epochs=50000)
print(model1.predict([10]))