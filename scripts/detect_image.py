import cv2
from ultralytics import YOLO

# Load model
model = YOLO("models/yolov8n.pt")

# Image path (SAFE)
img_path = r"E:\SmartCrowdAnalyzer\dataset\test_data\images\IMG_11.jpg"

# Read image
img = cv2.imread(img_path)
if img is None:
    raise FileNotFoundError(f"Image not found: {img_path}")

# Run detection
results = model(img, show=True, save=True)



count = 0
for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        if cls == 0:  # person class
            count += 1

annotated = results[0].plot()
cv2.putText(annotated, f"People Count: {count}", (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Crowd Detection", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
