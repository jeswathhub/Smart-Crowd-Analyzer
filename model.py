from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # auto-download if missing
print("YOLO loaded successfully")
