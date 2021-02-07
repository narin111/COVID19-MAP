# 전북 COVID-19 현황

## 프로젝트 소개
전북을 대상으로 코로나19 상황에 필요한 정보를 다음과 같이 제공한다.
ⅰ) 확진자가 다녀간 장소에 대한 정보(노출 일시, 소독 여부, 장소)를 제공
ⅱ) 전라북도 보건소에 대한 정보(주소, 전화번호)를 제공
ⅲ) 지도 API를 통해 지도에서의 보건소 위치를 제공

## 개발 배경
전염성이 강한 코로나 19가 확산됨에 따라 확진자의 이동 경로를 파악하는 것이 중요해져 이를 쉽게 알 수 있도록 지도를 이용한 웹이 요구되었다. 확진자 이동경로를 지도로 확인할 수 있는 광주 코로나맵 등 다른 지역을 대상으로 한 코로나맵 웹은 기존에 있었으나 전북만을 대상으로 한 웹은 없었다. 최근 전주에서의 코로나 확진자의 수가 증가함에 따라 코로나맵의 필요가 증가하여 이 프로젝트를 기획하였다.

## 기대효과
지도와 현황표를 한 곳에서 볼 수 있으므로 전북 지역의 COVID-19 상황을 좀 더 편하게 알 수 있다. 현재는 html을 실행할 때마다 크롤링을 해오도록 구현되어있다. 하지만 사용자가 늘어난다면 부하가 증가할 수 있으므로, DB를 이용해 크롤링을 구현한다면 이용자들이 문제없이 사용할 수 있을 것이다. 이 웹을 앱으로 구현 시, 사용자들의 접근성이 좀 더 편리해질 수 있다.

## 느낀점
본격적인 프로젝트 개발에 앞서 이론들을 공부하면서 HTML의 태그를 필요할 때 검색하는 사소한 방법부터 시작해 CSS의 기능들을 알아갈 수 있었다. 프로젝트 개발에 들어가서 직접 그 이론들을 적용해볼 수 있었고 그 외에도 크롤링에 대해서 적용해 볼 수 있었다. 지도의 경우 우리가 가진 정보를 사용해서 API를 적용하는 것이 어려웠다. ‘코로나 확진자 경로’ 라는 주제를 가지고 시작했지만 소독이 되면 코로나 현황 사이트의 목록에서 상호명이 가려져 맵 위에 표현하는 것이 어려워졌다. 결국 보건소를 위주로 한 맵을 제작하게 되면서 결과물로 처음 의도와는 다른 사이트를 제작하게 되었던 점이 조금 아쉬움으로 남는다. 표 페이지 경우엔 크롤링한 것을 HTML로 적용하는 부분이 어려웠지만 여러 번의 시도 끝에 잘 해낼 수 있었다. 마지막 주에 레이아웃을 전체적으로 정리하면서 사이트를 깔끔하게 만들었다. 
함께 Github를 사용하면서 프로젝트를 협업하면서 관리하는 법을 익혔던 것도 좋았다.


   
      
      
## 세부 기능 설명


### 지도

<div>
  <img width="700" src="https://user-images.githubusercontent.com/45174177/107139344-cd2bb200-695d-11eb-9f4a-3bae96bb68e9.png">
  <img width="700" src="https://user-images.githubusercontent.com/45174177/107139349-db79ce00-695d-11eb-9e45-c9e92cefbcb4.png">
</div>

>- 사이트에 접속했을 때 제일 먼저 보이는 화면이다.
>- 마커에 마우스를 올리면 보건소의 이름을 알 수 있다.
>- 마커는 보건소 위치임을 알기 편하게 하기위해 이미지 마커를 적용하였다.
>- 우측 상단에 보이는 지도/스카이뷰 버튼을 통해 지도의 보이는 방식을 바꿀 수 있다.      
  
<div>
  <img width="800" src="https://user-images.githubusercontent.com/45174177/107139372-fa786000-695d-11eb-9c75-194d7658f2e5.png">
</div>

>- 버튼에 지도의 중심좌표을 변경하고 지도의 확대레벨을 조절하는 OnClick 이벤트를 추가하여 클릭하면 해당지역별로 자세하게 지도를 볼 수 있다.      
    
<div>
  <img width="800" src="https://user-images.githubusercontent.com/45174177/107139383-1976f200-695e-11eb-8f87-ec6483fa6a38.png">
</div>

>- 지도를 축소하면 클러스터를 통해 전북지역에 얼마만큼 보건소가 위치하는지 클러스터를 통해 숫자로 확인할 수 있다.      
   
### 표

>- 전북 확진자 이동 경로 현황을 한눈에 보여주는 페이지
>- 웹 접속 때마다 크롤링한 데이터로 table을 구성

<div>
  <img width="800" src="https://user-images.githubusercontent.com/45174177/107139419-517e3500-695e-11eb-9636-c6d4a8d940b2.png">
  <img width="800" src="https://user-images.githubusercontent.com/45174177/107139431-65c23200-695e-11eb-94ca-6eca11fe7d54.png">
</div>      
   
      
>- 전북의 각 보건소(선별진료 의료기관)를 시군구별로 분류한 표

<div>
  <img width="800" src="https://user-images.githubusercontent.com/45174177/107139439-7a9ec580-695e-11eb-8a1a-2c3b82ae2885.png">
</div>
