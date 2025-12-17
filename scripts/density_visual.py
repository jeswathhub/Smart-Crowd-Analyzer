from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

model = YOLO("models/yolov8n.pt")
cap = cv2.VideoCapture(0)

# Data storage
time_steps = []
person_counts = []
frame_idx = 0

# Set up plot

sns.set_style("darkgrid")  # Or "whitegrid", "dark", etc.

fig, ax = plt.subplots()
line, = ax.plot([], [], color='crimson', linewidth=2)
ax.set_xlim(0, 100)  # Show last 100 frames
ax.set_ylim(0, 20)   # Max expected people
ax.set_title("Real-time Person Count")
ax.set_xlabel("Frame")
ax.set_ylabel("Count")

def update(frame):
    global frame_idx
    ret, img = cap.read()
    if not ret:
        return line,

    results = model(img, conf=0.4)
    person_count = sum(1 for r in results for box in r.boxes if int(box.cls[0]) == 0)

    # Store data
    frame_idx += 1
    time_steps.append(frame_idx)
    person_counts.append(person_count)

    # Keep last 100 frames
    if len(time_steps) > 100:
        time_steps.pop(0)
        person_counts.pop(0)

    # Update plot
    line.set_data(time_steps, person_counts)
    ax.set_xlim(max(0, frame_idx-100), frame_idx)
    ax.set_ylim(0, max(10, max(person_counts)+2))

    return line,

ani = FuncAnimation(fig, update, interval=200)
plt.show()

cap.release()
