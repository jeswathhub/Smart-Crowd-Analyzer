import cv2
import winsound
from ultralytics import YOLO
import threading

# ---------------- CONFIG ----------------
MODEL_PATH = "yolov8n.pt"  # YOLOv8 pre-trained model
ALARM_SOUND = r"E:\SmartCrowdAnalyzer\alarm.wav"
THRESHOLD = 10  # Max allowed people
CAMERA_ID = 0
# ----------------------------------------

# Load YOLO model
model = YOLO(MODEL_PATH)

# Alarm flag
alarm_playing = False

def play_alarm():
    global alarm_playing
    if not alarm_playing:
        alarm_playing = True
        winsound.PlaySound(ALARM_SOUND, winsound.SND_FILENAME | winsound.SND_ASYNC)

def stop_alarm():
    global alarm_playing
    winsound.PlaySound(None, winsound.SND_PURGE)
    alarm_playing = False

# Start video capture
cap = cv2.VideoCapture(CAMERA_ID)
if not cap.isOpened():
    print("❌ Camera not accessible")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    person_count = 0

    # YOLO prediction
    results = model(frame)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if cls == 0:  # Only person
                person_count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display person count
    cv2.putText(frame, f"Person Count: {person_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Alarm condition
    if person_count > THRESHOLD:
        cv2.putText(frame, "⚠ DANGER ⚠", (200, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
        threading.Thread(target=play_alarm, daemon=True).start()
    else:
        stop_alarm()

    cv2.imshow("Smart Crowd Analyzer", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
