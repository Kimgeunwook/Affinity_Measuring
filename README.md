# 목차
### 1. 프로젝트 소개 
### 2. Prerequisites   
### 3. 프로그램 작동법  
### 4. 실행 결과   
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
#
i.	안정적인 실행 환경을 위해 아나콘다에서 독립적인 가상환경 사용을 권장.
1.	conda create -n NAME python=3.7
2.	activate NAME
#
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
              
# 3. 프로그램 작동법   
***1. Choice_channel_nation.py 실행***     
***2. 원하는 채널, 국가 선택***         
***3. 'finish' 문구가 뜨면 지정한 폴더에 가서 excel파일 확인***    
#         
#                  
      

>>>>><div> <center><img src="https://user-images.githubusercontent.com/48399897/73320598-2bba4c80-4283-11ea-96e2-525d8f7d8cd3.PNG" width="30%" height="40%" title="Choice_channel_nation.py" alt="실행1"> </img><img src="https://user-images.githubusercontent.com/48399897/73322763-aa65b880-4288-11ea-989d-02b9ed222d41.PNG" width="60%" height="40%" title="저장되는 위치 출력" alt="실행1">     </img>  
</div>    

#           
#                     
      
# 4. 주의사항(파일이 생성되는 위치 바꾸고 싶은 경우)    
## ***(case) TripAdvisor***  

>>>>><div><img src="https://user-images.githubusercontent.com/48399897/73321545-290d2680-4286-11ea-8765-c51f2f830db9.PNG" width="50%" height="40%" title="regular2.py" alt="실행1">     </img><img src="https://user-images.githubusercontent.com/48399897/73321635-6ffb1c00-4286-11ea-87c6-e112573c7cf0.PNG" width="50%" height="40%" title="Ta_csvtoexcel.py" alt="실행1"> </img><p>regular2.py, Ta_csvtoexcel.py 빨간 동그라미친 폴더 설정 부분을 원하는 폴더로 변경</p></div>

## ***(case) MonkeyTravel***
>>>>><div><img src="https://user-images.githubusercontent.com/48399897/73322428-1eec2780-4288-11ea-9560-315067a468a4.PNG" width="50%" height="40%" title="choice_category.py" alt="실행1">     </img><img src="https://user-images.githubusercontent.com/48399897/73322428-1eec2780-4288-11ea-9560-315067a468a4.PNG" width="50%" height="40%" title="monkey.py" alt="실행1"></img><p>choice_category.py, monkey.py 빨간 동그라미친 폴더 설정 부분을 원하는 폴더로 변경</p></div>

## ***(case) Klook***
1. 실행 후 403에러 뜨면 klook사이트가서 봇 체크 풀어주기    
2. csv,excel파일 생성 폴더 변경시 4.주의사항의 tripadvisor, monkeytravel case처럼    
Klook_csv_to_excel.py, Klook_detail.py폴더 부분 수정

## ***(case)Trip Dot com***    
1. csv,excel파일 생성 폴더 변경시 4.주의사항의 tripadvisor, monkeytravel case처럼   
Tripdotcom_csv_to_excel.py, TripDotCom_detail.py폴더 부분 수정

#           
#                     
      
# 5. 실행 결과    
## 
>>>>><div><img src="https://user-images.githubusercontent.com/48399897/73332666-c5e1bb00-42aa-11ea-9d28-cbc88d0e388c.PNG" width="49%" height="40%" title="실행 결과" alt="실행결과"></img><img src="https://user-images.githubusercontent.com/48399897/73332565-7ac7a800-42aa-11ea-90f8-a8233366f3c8.PNG" width="49%" height="40%" title="실행 결과" alt="실행결과"> </img></div>


