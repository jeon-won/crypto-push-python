# crypto-bot-python

## 개요
가상화폐 거래 방법을 배워볼 겸 만든 파이썬 코드 입니다. 떡상 가즈아!!!

이 파이썬 코드는 [조코딩 님 유튜브](https://youtu.be/5vofEMqMyGk)와 [위키독스 사이트](https://wikidocs.net/book/1665)를 참고하여 만들었습니다. 거래소는 업비트를 사용합니다.

**여기 있는 코드는 테스트 중이므로 정상적인 실행을 보장하지 않으며, 이 프로그램을 사용하여 발생하는 손해에 대한 책임은 사용자 본인에게 있습니다.**

## cryptofunc.py
업비트 가상화폐 관련 정보를 얻어오기 위한 함수를 모아놓은 모듈

## AutoDetectCross.py
가상화폐 이동평균선이 골든크로스로 변할 것으로 예상될 때 슬랙 메시지를 전송하는 파이썬 코드

## AutoTrade.py
변동성 돌파 전략을 사용하여 가상화폐를 자동 거래하는 파이썬 코드

## AutoDetect3RCandleBinance.py
바이낸스 거래소 차트에 3연속 음봉이 떴을 때 텔레그램 메시지를 전송하는 파이썬 코드

## AutoDetect3RcandleUpbit.py
업비트 거래소 차트에 3연속 음봉이 떴을 때 텔레그램 메시지를 전송하는 파이썬 코드

## AutoDetectBBBinance.py
바이낸스 거래소 차트에 볼린저 밴드 상단 및 하단을 터치한 봉이 떴을 때 텔레그램 메시지를 전송하는 파이썬 코드

## AutoDetectBBUpbit.py
어비트 거래소 차트에 볼린저 밴드 하단을 터치한 봉이 떴을 때 텔레그램 메시지를 전송하는 파이썬 코드

## MultiChartHtml
바이낸스 거래소 차트를 화면 분할하여 보여주는 html