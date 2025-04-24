from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import cv2 #เปลี่ยนทุกอันให้เป็น cv2
import numpy as np
from collections import defaultdict

# Load YOLO model
model = YOLO("yolov8n.pt")
# print(model.names)



def draw_boxes(frame, boxes):
    """Draw detected bounding boxes on image frame"""

    # Create annotator object
    annotator = Annotator(frame)


    for box in boxes:
        class_id = box.cls
        class_name = model.names[int(class_id)]
        coordinator = box.xyxy[0]
        # confidence = box.conf

    
        # Draw bounding box
        annotator.box_label(
            box=coordinator, label=class_name, color=(255, 0, 0) #เปลี่ยนเป็น blue
        ) #อันนี้ค้องอยู่ใน loop for ไม่งั้นจะเกิดปัญหา coordinator ใส่ค่าก่อนประกาศตัวแปร

    return annotator.result()


def detect_object(frame):
    """Detect object from image frame"""
    
    # Detect object from image frame
    # results = model.predict(frame,stream=True,classes=[15]) #จับแมว คลาสที่ 15
    results = model.track(frame, persist=True,classes=[15] , device="cpu")

    for result in results:
    # Get the boxes and track IDs
        if result.boxes and result.boxes.id is not None:
            boxes = result.boxes.xywh.cpu()
            track_ids = result.boxes.id.int().cpu().tolist()

            # Plot the tracks
            for box, track_id in zip(boxes, track_ids):
                x, y, w, h = box
                track = track_history[track_id]
                track.append((float(x), float(y)))  # x, y center point
                if len(track) > 30:  # retain 30 tracks for 30 frames
                    track.pop(0)

            # Draw the tracking lines
                points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                cv2.polylines(frame, [points], isClosed=False, color=(230, 230, 230), thickness=10) 

    # Visualize the results on the frame
    frame = draw_boxes(frame, result.boxes) #เคาะเข้ามา 1 tab
    
    return frame


if __name__ == "__main__":
    video_path = "CatZoomies.mp4"
    cap = cv2.VideoCapture(video_path)

    # Store the track history
    track_history = defaultdict(lambda: [])

  
    while cap.isOpened():
        # Read image frame
        ret, frame = cap.read() #read_frame() ไม่มี มีแต่ read()
        frame = cv2.resize(frame, (650, 400)) #ลดขนาดการแสดงผลหน้าจอ
        
        # ใส่ชื่อขวาบน
        
        font = cv2.FONT_HERSHEY_DUPLEX
  
        # Use putText() method for 
        cv2.putText(frame,  
                'Korbun-Clicknext-Internship-2024',  
                (325, 25),  
                font, 0.5,  
                (0, 0, 255),  
                2,  
                cv2.LINE_4) 
        if ret:
            # Detect cat? from image frame
            frame_result = detect_object(frame)

        
            # Show result
            cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
            cv2.imshow("Video", frame_result)
            cv2.waitKey(30) 
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
