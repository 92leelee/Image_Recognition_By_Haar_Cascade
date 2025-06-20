# Image_Recognition_By_Haar_Cascade
The purpose of this project is to allow the camera to detect the target

![Detection Result](result.png)

## Demo
[Click here to watch the demo video](https://youtu.be/wNfMEHVkqjk)


## How to run
[螢幕擷取畫面 2025-06-20 112824](https://github.com/user-attachments/assets/4ccf4446-ade0-45c3-9250-4e9e603a254f)
```bash

```

## How to Train
```bash
opencv_traincascade -data classifier -vec positives.vec -bg negatives.txt -numPos 1000 -numNeg 500 -numStages 10 -w 24 -h 24
```







