#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
이 코드는 인사이트 출판사에서 출판된 책 <파이썬으로 만드는 OpenCV 프로젝트> 로 부터 정리하였습니다. 
이 코드는 MIT 라이센스를 따르고 아래의 Github 주소에서도 받을 수 있습니다.

GitHub : https://github.com/dltpdn/book_opencv_prject_using_python
Author : Lee Sewoo(이세우, dltpdn@gmail.com)
'''


# In[ ]:


import cv2

img_file = "../img/2.1.jpg" # 표시할 이미지 경로
img = cv2.imread(img_file)  # 이미지를 읽어서 img 변수에 할당

if img is not None:
    cv2.imshow('IMG',img)   # 읽은 이미지를 화면에 표시
    cv2.waitKey()           # 키가 입력될 때까지 대기
    cv2.destroyAllWindows() # 창 모두 닫기
else:
    print("No image file.")

