import cv2
import os


video_path = '0619.mp4'#影片來源
output_dir = 'p'#選擇要放在哪個資料夾
images_per_second = 8 # 每秒擷取8張圖片

# 建立資料夾）
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 開啟影片
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print('無法開啟影片')
    exit()

# 取得影片的 fps
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"影片 FPS: {fps}")

# 計算間隔幀數
frame_interval = int(fps / images_per_second)

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        filename = os.path.join(output_dir, f'p_{saved_count:04d}.jpg')
        cv2.imwrite(filename, frame)
        saved_count += 1

    frame_count += 1

cap.release()
print(f'擷取完成，共儲存 {saved_count} 張圖片（總幀數 {frame_count}）')
