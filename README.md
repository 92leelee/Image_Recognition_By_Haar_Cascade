# Image_Recognition_By_Haar_Cascade
The purpose of this project is to allow the camera to detect the target

![Detection Result](result.png)

## Demo
[Click here to watch the demo video](https://youtu.be/wNfMEHVkqjk)


## How to run
![Detection Result](https://github.com/user-attachments/assets/4ccf4446-ade0-45c3-9250-4e9e603a254f)
```bash
直接跑run.py的程式碼即可完成
```

## How to Train
```bash
1.繪出正樣本:"C:\opencv2\opencv\build\x64\vc15\bin\opencv_annotation.exe" --annotations=annotations.txt --images=D:\你的路徑\cat\p
2.產生vec檔 :"C:\opencv2\opencv\build\x64\vc15\bin\opencv_createsamples.exe" -info annotations.txt -vec positives.vec -num 100 -w 24 -h 24
3.準備bg.txt檔(負樣本清單) :dir /b /s "C:\Users\你的名字\Desktop\cat\n\*.jpg" > bg.txt
4.開始訓練 :opencv_traincascade -data classifier -vec positives.vec -bg negatives.txt -numPos 1000 -numNeg 500 -numStages 10 -w 24 -h 24

```







