# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 23:18:53 2019

@author: SW501
"""

import sys, os
sys.path.append(os.pardir)
import numpy as np
from keras import models
from keras import layers
from keras import callbacks
import matplotlib.pyplot as plt

f = open("C:\\Users\\SW501\\Desktop\\Deep-Learning-scratch-study-master\\book-code\\input2.txt", 'r')

ft = open("C:\\Users\\SW501\\Desktop\\Deep-Learning-scratch-study-master\\book-code\\test.txt", 'r')
#(x_train, t_train), (x_test, t_test)
x_train=[] 
t_train=[]
x_test=[]
t_test=[]
while True:
    line = f.readline()
    if not line: break
    arr=line.split(' ')
    x=arr[0:12]
    answer = [0,0,0,0,0]
    answer[int(arr[12])-1]=1
    x_train.append(x)
    t_train.append(answer)
while True:
    line = ft.readline()
    if not line: break
    arr=line.split(' ')
    x=arr[0:12]
    answer = [0,0,0,0,0]
    answer[int(arr[12])-1]=1
    x_test.append(x)
    t_test.append(answer)    
x_train = np.array(x_train)
t_train = np.array(t_train)
x_test = np.array(x_test)
t_test = np.array(t_test)
x_train = x_train.astype(np.float32)
t_train = t_train.astype(np.float32)
x_test = x_test.astype(np.float32)
t_test = t_test.astype(np.float32)

model = models.Sequential()
model.add(layers.Dense(20, activation='relu', input_shape=(12,)))
model.add(layers.Dense(30, activation='relu'))
model.add(layers.Dense(10, activation='relu'))
model.add(layers.Dense(30, activation='relu'))
model.add(layers.Dense(20, activation='relu'))
model.add(layers.Dense(5, activation='softmax'))

#categorical_crossentropy #binary_crossentropy
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])
results = model.fit(x_train, t_train, validation_split=0.1, epochs=100)

test_loss, test_acc = model.evaluate(x_train, t_train)
print('test_acc', test_acc)

model_json = model.to_json()
with open("DNN_epoch100.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("DNN_epoch100.h5")
print("Saved model")

plt.plot(results.history['acc'])
plt.plot(results.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(results.history['loss'])
plt.plot(results.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()