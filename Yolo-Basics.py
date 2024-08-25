from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
results =  model("/Users/anahatdeshmukh/Documents/DynamicFlow/Yolo_Running/Images/1.mp4", show = True)
cv2.waitKey(0)

results =  model("/Users/anahatdeshmukh/Documents/DynamicFlow/Yolo_Running/Images/9.jpg", show = True)
cv2.waitKey(5000)

results =  model("/Users/anahatdeshmukh/Documents/DynamicFlow/Yolo_Running/Images/10.jpg", show = True)
cv2.waitKey(5000)

results =  model("/Users/anahatdeshmukh/Documents/DynamicFlow/Yolo_Running/Images/11.jpg", show = True)
cv2.waitKey(5000)

results =  model("/Users/anahatdeshmukh/Documents/DynamicFlow/Yolo_Running/Images/12.jpg", show = True)
cv2.waitKey(5000)