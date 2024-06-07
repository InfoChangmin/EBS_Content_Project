# Load YOLOv8n, train it on COCO128 for 3 epochs and predict an image with it
from ultralytics import YOLO
import cv2

model = YOLO('yolov8s-world.pt')
model.set_classes(['Man holding a tumbler with yellow in it','black cell phone','lip balm'])

cap = cv2.VideoCapture(1)

while cap.isOpened():
  success, image = cap.read()
  if not success:
    continue

  results = model.predict(image, device='cpu', save=True)

  for result in results:
    result_ploted = results[0].plot()
    cv2.imshow('img', result_ploted)

  if cv2.waitKey(1) == ord('q'):
    break
cap.release()



