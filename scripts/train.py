from ultralytics import YOLO

# Load YOLOv8 Nano
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data="dataset/data.yaml",   # create this file (given below)
    epochs=30,
    imgsz=640,
    batch=4,
    device="cpu"  # change to 0 if GPU available
)

print("Training Completed!")
