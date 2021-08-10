import cv2
import numpy as np 
import math

# 
# In[137]:
def mask(): 
    net_mask = cv2.dnn.readNet("C:\shifa\sem6\Internship\maskdet\maskapp\yolov3_mask_last.weights", "C:\shifa\sem6\Internship\maskdet\maskapp\yolov3_mask.cfg")
    classes_mask = []
    with open("C:\shifa\sem6\Internship\maskdet\maskapp\coco -1.names", "r") as f:
        classes_mask = [line.strip() for line in f.readlines()]  
        layer_names_mask = net_mask.getLayerNames()
        output_layer_mask = [layer_names_mask[i[0] - 1] for i in net_mask.getUnconnectedOutLayers()]
        while True:
                      
            re,img = video_capture.read()
            img = cv2.resize(img, None, fx=0.4, fy=0.4)
            height, width, channels = img.shape
            blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (416, 416),  swapRB=True, crop=False)
            net_mask.setInput(blob)
            outs = net_mask.forward(output_layer_mask)
            class_ids_mask = []
            confidences_mask = []
            boxes_mask = []     
            for out in outs:
                for detection in out:
                    scores_mask = detection[5:]
                    class_id_mask = np.argmax(scores_mask)
                    confidence_mask = scores_mask[class_id_mask]
                    if confidence_mask > 0.5:
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
                        boxes_mask.append([x, y, w, h])
                        confidences_mask.append(float(confidence_mask))
                        class_ids_mask.append(class_id_mask)                
            indexes_mask = cv2.dnn.NMSBoxes(boxes_mask, confidences_mask, 0.5, 0.4)
            font = cv2.FONT_HERSHEY_PLAIN
            colors = np.random.uniform(0, 255, size=(len(classes_mask), 3))
            for i in range(len(boxes_mask)):
                if i in indexes_mask:
                    x, y, w, h = boxes_mask[i]
                    label_mask = str(classes_mask[class_ids_mask[i]])
                    if(label_mask=='Mask weared partially'):
                        label_mask='No mask'
 
                    c=str(confidences_mask[i])
                    color = colors[class_ids_mask[i]]
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                    cv2.putText(img, label_mask, (x, y -5),cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)
            cv2.imshow("object detection",cv2.resize(img, (800,600)))
            if cv2.waitKey(500):
                break

# In[138]:

# In[139]:
net = cv2.dnn.readNet("C:\shifa\sem6\Internship\maskdet\maskapp\yolov3.weights", "C:\shifa\sem6\Internship\maskdet\maskapp\yolov3.cfg")
# In[140]:
classes = []
# In[141]:
with open("C:\shifa\sem6\Internship\maskdet\maskapp\coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]  
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
# In[142]:
class_ids = []
confidences = []
boxes = []

video_capture = cv2.VideoCapture(0)
'''
def make_1080p():
    video_capture.set(3,1920)
    video_capture.set(4,1080)
def make_720p():
    video_capture.set(3,1280)
    video_capture.set(4,720)
def make_480p():
    video_capture.set(3,640)
    video_capture.set(4,480)
def change_res(width,height):
    video_capture.set(3,width)
    video_capture.set(4,height)
make_720p()
change_res(1280,720)

'''

# In[ ]:
while True:
    re,img = video_capture.read()
    #print(re)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (416, 416),  swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
               
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
             
    
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
   
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    for i in range(len(boxes)):
        if i in indexes:
            x, y , w, h = boxes[i]
            label = str(classes[class_ids[i]])
            if label=='person':
                mask()
            if label=='traffic light':
                #traffic()
                while(1):
                    re,img = video_capture.read()
                    if(re==False):
                        break
                    hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                    red_lower = np.array([136, 87, 111], np.uint8)
                    red_upper = np.array([180, 255, 255], np.uint8)
                    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
                    green_lower = np.array([25, 52, 72], np.uint8)
                    green_upper = np.array([102, 255, 255], np.uint8)
                    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
                    yellow_lower = np.array([25, 50, 70], np.uint8)
                    yellow_upper = np.array([30, 255, 255], np.uint8)
                    orange_lower= np.array([10, 100, 20], np.uint8)
                    orange_upper= np.array([25,255,255],np.uint8)
                    yellow_mask = cv2.inRange(hsvFrame, yellow_lower+orange_lower, yellow_upper+orange_upper)
                    kernal = np.ones((5, 5), "uint8")
                    red_mask = cv2.dilate(red_mask, kernal)
                    res_red = cv2.bitwise_and(img, img, mask = red_mask)
                    green_mask = cv2.dilate(green_mask, kernal)
                    res_green = cv2.bitwise_and(img, img, mask = green_mask)
                    yellow_mask = cv2.dilate(yellow_mask, kernal)
                    res_yellow = cv2.bitwise_and(img, img, mask = yellow_mask)
                    contours, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)         
                    for pic, contour in enumerate(contours): 
                        area = cv2.contourArea(contour)
                        if(area > 300):
                            x, y, w, h = cv2.boundingRect(contour)
                        # print(x,y,w,h)
                            if(w<=110):        
                                imageFrame = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)   
                                cv2.putText(img, "Red Colour", (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255),3)
                    contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
                    for pic, contour in enumerate(contours):
                        area = cv2.contourArea(contour)
                        if(area > 300):
                            x, y, w, h = cv2.boundingRect(contour)
                            if(w<=100):
                                imageFrame = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)   
                                cv2.putText(img, "Green Colour", (x, y - 10),  cv2.FONT_HERSHEY_SIMPLEX,  1.0, (0, 255, 0),3)
                    contours, hierarchy = cv2.findContours(yellow_mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    for pic, contour in enumerate(contours):
                        area = cv2.contourArea(contour)
                        if(area > 350):
                            x, y, w, h = cv2.boundingRect(contour)
                            imageFrame = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)      
                            cv2.putText(img, "yellow Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX,  1.0, (255, 0, 0))
                    cv2.imshow("object detection", cv2.resize(img, (800,600)))
                    if cv2.waitKey(1000):
                        break

            c=str(confidences[i])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                      
            cv2.putText(img, label, (x, y -10),cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)
        cv2.imshow("object detection",cv2.resize(img, (800,600)))
   
    if cv2.waitKey(1) == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()


    