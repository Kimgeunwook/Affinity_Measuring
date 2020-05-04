# 목차
### 1. 프로젝트 소개 
### 2. Prerequisites
### 3. 시스템 구성도 / 시나리오  
### 4. 프로그램 작동법  
### 5. 실행 결과   
#   
#   
# 1. 프로젝트 소개    
두명의 얼굴이 잡힌 사진에서 각 얼굴을 인식하여, 감정분석 프로그램에서 두명의 감정수치를 추출한다.
두 명의 감정 수치와 그 사진에서의 관계를 바탕으로 직접 제작한 호감도 도출 함수에서 나온 호감도 수치를 DNN을 사용하여 학습시킨다. 
학습이 완료된 뒤에는 두명의 얼굴이 있는 영상 혹은 사진을 입력으로 받고, 각각의 감정 수치와 그에 따른 호감도를 도출해내는 프로그램이다.
#         
#                  
          

# 2. Prerequisites
```

i.	안정적인 실행 환경을 위해 아나콘다에서 독립적인 가상환경 사용을 권장.
1.	conda create -n NAME python=3.7
2.	activate NAME

ii.	필요한 파이썬 라이브러리 설치
1.	conda install numpy
2.	conda install tensorflow
3.	conda install keras
4.	pip install imutils
5.	pip install opencv-python
6.	conda install matplotlib

```            
#         
#                  
# 3. 시스템 구성도 / 시나리오  
>>>>><div> <center><img src="https://user-images.githubusercontent.com/48399897/80967601-99ad7b80-8e51-11ea-8b3c-1417f8fca4bd.jpg" width="50%" height="40%" title="시스템 " alt="실행1"> </img></div>
<br/>
<div>
<img src="https://user-images.githubusercontent.com/48399897/80967639-a7fb9780-8e51-11ea-8b28-8f1b4b977ff2.jpg" width="60%" height="40%" title="시나리오" alt="실행1">     </img>  
</div>    
#         
#

# 4. 프로그램 작동법   

***1. Choice_channel_nation.py 실행***     
***2. 원하는 채널, 국가 선택***         
***3. 'finish' 문구가 뜨면 지정한 폴더에 가서 excel파일 확인***    



#           
#                     
      
# 5. 실행 결과    
## 
>>>>>![실행결과](https://user-images.githubusercontent.com/48399897/80966965-8b129480-8e50-11ea-9921-137b217bf458.gif)


