# Korbun_internship_2024


## Install

**Clone repo**
```bash
git clone https://github.com/KMkhim/Korbun_internship_2024.git
cd your-repo
```
    
**สร้าง env**
```bash
python3 -m venv env
source env/bin/activate  # macOS/Linux
#or
env\Scripts\activate     # Windows
```
**ติดตั้ง package ต่างๆ**
```bash
pip install -r requirements.txt
```
- ultralytics==8.0.153 ต้องเป็นรุ่นที่เก่า เพราะ ver ใหม่ๆติดบัค ตรง classes = [15] ค่ะ

**รันโค้ด**

ภาพตัวอย่างที่ได้จากวิดีโอ

<img width="450" alt="Image" src="https://github.com/user-attachments/assets/0db525a3-0ff4-4dc5-9b1e-c9ca3f2d799b" />

<img width="450" alt="Image" src="https://github.com/user-attachments/assets/722efa05-8a9b-40d9-ae42-788b4c5433f8" />

## Error ที่เจอ

- แก้ cv -> cv2
- yolov8a.pt -> yolov8n.pt
- prediction -> predict แต่สุดท้ายใช้ track ค่ะ
- read_frame() -> read()
- เคาะ annotator.box_label 1 tab
- เคาะ frame = draw_boxes(frame, result.boxes) 1 tab


## แหล่งอ้างอิงโค้ด

#### detect cat only
- https://github.com/orgs/ultralytics/discussions/10074

#### requirements.txt คืออะไร?
- https://github.com/ultralytics/yolov5/blob/master/requirements.txt

#### วิธีใส่ text
- https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/

- https://stackoverflow.com/questions/53111837/align-text-in-the-puttext-in-opencv

#### เปลี่ยนสีกล่อง
- https://docs.ultralytics.com/reference/utils/plotting/#ultralytics.utils.plotting.Annotator

#### สร้างเส้นติดตาม track line
- https://docs.ultralytics.com/modes/track/#plotting-tracks-over-time
