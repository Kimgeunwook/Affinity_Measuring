#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys, os
sys.path.append(os.pardir)
import numpy as np
from keras.models import model_from_json
from keras import layers
from keras import callbacks
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument('-c', '--cascade', required = True)
ap.add_argument('-m', '--model', required = True)
ap.add_argument('-v', '--video')
args = vars(ap.parse_args())
graph_a=[]
graph=np.array(graph_a)
#load face detector cascade
detector = cv2.CascadeClassifier(args['cascade'])
model = load_model(args['model'])
EMOTIONS = ['angry', 'scared', 'happy', 'sad', 'surprised', 'neutral']

if not args.get('video', False):
    camera = cv2.VideoCapture(0)

else:
    camera = cv2.VideoCapture(args['video'])
    #camera= cv2.imread('kids.png')


#json_file = open("DNN_epoch500.json", "r")
json_file = open("DNN_new_epoch100.json", "r")

loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

#loaded_model.load_weights("DNN_epoch500.h5")
loaded_model.load_weights("DNN_epoch100.h5")

print("Loaded model")

loaded_model.compile(loss="binary_crossentropy",
                     optimizer="rmsprop",
                     metrics=['accuracy'])

#     acc = loaded_model.evaluate(x_test,t_test,verbose=0)
#     print("%s : %.2f%%" % (loaded_model.metrics_names[1], acc[1]*100))

p=0
ans=0
xxx=[]
yyy=[]
canvas3 = np.zeros((250, 800, 3), dtype= 'uint8')
white_color = (255,255,255)
red_color = (0,0,255)
ttext='Affinity'
cv2.putText(canvas3, ttext, (200, 40),
        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255,255), 2)
canvas3 = cv2.line(canvas3,(40,240), (780,240),white_color,thickness=1)
canvas3 = cv2.line(canvas3,(40,40), (40,240),white_color,thickness=1)
while True:
    (grabbed, frame) = camera.read()

    if args.get('video') and not grabbed:
        break
# resize the frame and convert it to grayscale
    frame = imutils.resize(frame, width=700)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#initialize the canvas for the visualization, clone
# the frame so we can draw on it
    canvas = np.zeros((220, 400, 3), dtype= 'uint8')
    canvas2 = np.zeros((220, 400, 3), dtype= 'uint8')
    frameClone = frame.copy()


    rects = detector.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    #rects = detector.detectMultiScale(camera)
    
    
#     if len(rects) >0:               
#face area
#         rect = sorted(rects, reverse=True, key = lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
#         (fX, fY, fW, fH) = rect

#         roi = gray[fY:fY+fH, fX:fX+fW]
#         roi = cv2.resize(roi, (48, 48))
#         roi = roi.astype('float')/255.0
#         roi = img_to_array(roi)
#         roi = np.expand_dims(roi, axis = 0)
    count = 0
    flag = 0
    flag2=0
    for(x1,y1,w1,h1) in rects:
        if count==0:
            cv2.rectangle(frameClone,(x1,y1),(x1+w1,y1+h1),(255,0,255),2)
            roi1 = frameClone[y1:y1+h1,x1:x1+w1]
            roi1 = gray[y1:y1+h1, x1:x1+w1]
            roi1 = cv2.resize(roi1,(48,48))
            roi1 = roi1.astype('float')/255.0
            roi1 = img_to_array(roi1)
            roi1 = np.expand_dims(roi1, axis = 0)
            preds1 = model.predict(roi1)[0]
            label1 = EMOTIONS[preds1.argmax()]
        elif count==1:
            cv2.rectangle(frameClone,(x1,y1),(x1+w1,y1+h1),(255,0,255),2)
            roi2 = frameClone[y1:y1+h1,x1:x1+w1]
            roi2 = gray[y1:y1+h1, x1:x1+w1]
            roi2 = cv2.resize(roi2,(48,48))
            roi2 = roi2.astype('float')/255.0
            roi2 = img_to_array(roi2)
            roi2 = np.expand_dims(roi2, axis = 0)
            preds2 = model.predict(roi2)[0]
            label2 = EMOTIONS[preds2.argmax()]
            flag = 1
        count = count+1
#preds
    personem = []
    #personem=np.array([])
    for(i,(emotion, prob)) in enumerate(zip(EMOTIONS, preds1)):
        text = "{}: {:.2f}%".format(emotion, prob*100)

        w= int(prob * 300)
        cv2.rectangle(canvas, (5, (i*35) + 5),
        (w, (i*35)+35), (0,0,225), -1)
        cv2.putText(canvas, text, (10, (i * 35) + 23),
        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255,255,255), 2)

        cv2.putText(frameClone, label1, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255,0,0), 2)
        cv2.rectangle(frameClone, (x1, y1), (x1+w1, y1+h1),(255,0,0), 2)
        
        personem.append(round(w/300,4))
#     print("person1")
#     print(person1em)
    if flag==1:
        #person2em = []
        for(i,(emotion, prob)) in enumerate(zip(EMOTIONS, preds2)):
            text1 = "{}: {:.2f}%".format(emotion, prob*100)
            wa= int(prob * 300)
            cv2.rectangle(canvas2, (5, (i*35) + 5),
            (wa, (i*35)+35), (0,0,225), -1)
            cv2.putText(canvas2, text1, (10, (i * 35) + 23),
            cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255,255,255), 2)

            cv2.putText(frameClone, label2, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255,0,0), 2)
            cv2.rectangle(frameClone, (x1, y1), (x1+w1, y1+h1),(255,0,0), 2)
            
            personem.append(round(wa/300,4))
            flag2=1
#         print("person2")    
#         print(person2em)
#     asdf = np.array()
#     asdf.append(personem)
#     asdf.append(personem)
#     asdf.append[personem]
#     asdf.append[0,0,0,0,0,0,0,0,0,0,0,0]

    if flag2==1:
        print(personem)
        personem = np.array(personem)
        personem = personem.reshape((1, -1))
        output = loaded_model.predict(personem, verbose=0)
        count = 0
        #print('%d', i+1)
        print(output)
        #ans = 1*i[0] + 2*i[1] + 3*i[2] + 4*i[3] + 5*i[4]
        pans=ans
        ans = 1.0*output[0][0] + 2.0*output[0][1] + 3.0*output[0][2] + 4.0*output[0][3] + 5.0*output[0][4]
        ans = (ans/4)*100 - 25
        print("답 : "+str(ans))
        # 그래프 그리기
        #markers = {'train': 'o', 'test': 's'}
#         graph=np.append(graph,ans)
#         x = np.arange(len(graph))
#         plt.plot(x, graph, label='train acc')
#         plt.xlabel("love")
#         plt.ylim(0, 100.0)
#         plt.legend(loc='lower right')
        ans=int(ans)
        #xxx.append(p)
        #yyy.append(ans)
        aa=240-(2*ans)
        pp=240-(2*pans)
        p=p+1
        canvas3 = cv2.line(canvas3,(p+40,pp), (p+41,aa),red_color,thickness=1)
        

    cv2.imshow("face", frameClone)
    cv2.imshow("prob", canvas)
    cv2.imshow("prob2", canvas2)
#     for i in range(1,len(xxx)+2):
#         canvas3 = cv2.line(canvas3,(xxx[i-1]+40,240-(2*yyy[i-1])), (xxx[i]+40,240-(2*yyy[i])),red_color,thickness=1)
    cv2.imshow("graph", canvas3)

    
    
        

    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# markers = {'train': 'o', 'test': 's'}
# #np.append(graph,ans)
# x = np.arange(len(graph))
# plt.plot(x, graph, label='train acc')
# plt.xlabel("love")
# plt.ylim(0, 100.0)
# plt.legend(loc='lower right')       
# plt.show()
camera.release()
cv2.destroyAllWindows()


# In[ ]:




