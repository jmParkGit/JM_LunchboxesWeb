# 편의점_도시락_여행 web 기획안
## 1. 프로젝트 이름/간단 설명
- 편의점_도시락_여행
- 몇년 사이 편의점 도시락 품질이 높아졌다. 이로 인해 편의점 도시락을 탐방하는 매니아 층도 생겨났다.
이 매니아분들을 위하여, 여러개 편의점의 도시락 목록을 한곳에서 제공하는 것을 생각하였다.
- 프로젝트에서는 편의점은 3개(GS25, CU, 7-ELEVEN)만 이용하겠다.

## 2. 프로젝트 생김새(레이아웃)
![layout_편의점도시락_211107](https://user-images.githubusercontent.com/84515872/140633433-90542723-42b9-4f64-a124-36edaa578948.JPG)
- [위 layout 원본파일](https://github.com/jmParkGit/JM_LunchboxesWeb/blob/main/layout/%ED%8E%B8%EC%9D%98%EC%A0%90_%EB%8F%84%EC%8B%9C%EB%9D%BD_%EC%97%AC%ED%96%89_page1_211107)


## 3. 개발해야 하는 기능들
- 각 편의점 도시락 page 크롤링
- 크롤링 한 데이터를 mongo DB를 이용하여 관리
- 좋아요 수 관리 및 업데이트
- 편의점 변경시 서버에서 -> fronted로 편의점 도시락 목록을 다시 보내줘야됨.
  - Example: GS25에서 CU로 변경시, 화면 목록 업데이트 필요
  
## 4. 프로젝트에 필요한 데이터소스
- GS25 도시락 tab: http://gs25.gsretail.com/gscvs/ko/products/youus-freshfood
- CU 도시락 tab: http://cu.bgfretail.com/product/product.do?category=product&depth2=4&sf=N
- 7-ELEVEN 도시락 tab: https://www.7-eleven.co.kr/product/bestdosirakList.asp?pTab=mini

## 5. 기타
- 2.프로젝트 생김새의 layout은  diagram.net을 이용해서 작성하였다.
