from dotenv import load_dotenv
import os
from module_upbit import get_vol_top_tickers, get_pyupbit_bb
import telegram
import pyupbit
import sys

"""
detect_bb_exceed_upbit.py
* Date: 2022. 1. 23.
* Author: Jeon Won
* Func: 업비트 차트의 %B 0 값을 상향돌파 시 텔레그램 메시지 전송
* Usage: 15분봉 기준 조사 명령어는 `python3 detect_bb_exceed_upbit.py minute15` (minute1~240, day 등 사용)
"""

load_dotenv()

INTERVAL = sys.argv[1]  # 차트 종류
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")      # 텔레그램 봇 토큰
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")  # 텔레그램 봇 아이디
BB_COUNT = 20      # 볼린저 밴드(BB)의 길이
BB_MULTIPLIER = 2  # 볼린저 밴드(BB)에서 상하한선을 정하기 위해 사용하는 곱(승수)

bot = telegram.Bot(TELEGRAM_TOKEN)
tickers = get_vol_top_tickers(10)
# tickers = ["KRW-BTC", "KRW-ETH", "KRW-XRP"]

# 각 ticker 조사
for ticker in tickers:
    # pyupbit로 ticker의 BB_COUNT+1개 만큼의 DataFrame을 얻어옴
    # 0 ~ BB_COUNT 범위의 DataFrame은 직전 볼린저밴드 계산용
    # 1 ~ BB_COUNT+1 범위의 DataFrame은 현재 볼린저밴드 계산용
    df = pyupbit.get_ohlcv(ticker, INTERVAL, BB_COUNT+1)

    prev_df = df[0:len(df)-1]   # 직전 기준 BB_COUNT개의 데이터프레임
    current_df = df[1:len(df)]  # 현재 기준 BB_COUNT개의 데이터프레임
    
    prev_bb = get_pyupbit_bb(ticker, prev_df, 2)        # 직전 기준 볼린저밴드 값
    current_bb = get_pyupbit_bb(ticker, current_df, 2)  # 현재 기준 볼린저밴드 값
    
    prev_per_b = prev_bb['per_b']        # 직전 기준 %B 값 
    current_per_b = current_bb['per_b']  # 현재 기준 %B 값

    # 직전 -> 현재 %B값이 0을 상향돌파 했을 때 텔레그램 메시지 전송
    if(prev_per_b < 0 and current_per_b > 0):
        message = f"Upbit {ticker} {INTERVAL} 차트 볼린저밴드 %B 값 0 상향돌파 (현재가: {current_bb['current']})"
        bot.sendMessage(TELEGRAM_CHAT_ID, text=message)