from bs4 import BeautifulSoup as soup
import urllib.request
import requests
import pandas as pd
import datetime

months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

# dataframe
df = pd.read_excel('./s_p.xlsx')
df['earning_flag'] = 0
all_dates = {}


def getData(ticker):
    url = 'https://finance.yahoo.com/calendar/earnings?day=2019-06-13&symbol={}&offset=0&size=100'.format(
        ticker)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    response = requests.get(url, headers=headers)
    print(response)
    html = response.text

    page_soup = soup(html, 'lxml')
    table = page_soup.find_all('td')
    dates = []
    for something in table:
        try:
            if something['aria-label'] == "Earnings Date":
                date = something.text.split(',')
                # print(date)
                temp = date[0].split()
                # print(temp)
                month, day, year = months[temp[0]], temp[1], date[1].strip()
                # print(month, day, year)
                if int(year) >= 2017:
                    dates.append("{}/{}/{}".format(month, day, year))
        except:
            print('')

    all_dates[ticker] = set(dates)


# tickers = "AAPL,ABBV,ABT,ACN,AGN,AIG,ALL,AMGN,AMZN,AXP,BA,BAC,BIIB,BK,BLK,BMY,C,CAT,CELG,CL,CMCSA,COF,COP,COST,CSCO,CVS,CVX,DD,DHR,DIS,DOW,DUK,EMC,EMR,EXC,F,FB,FDX,FOX,FOXA,GD,GE,GILD,GM,GOOG,GOOGL,GS,HAL,HD,HON,IBM,INTC,JNJ,JPM,KMI,KO,LLY,LMT,LOW,MA,MCD,MDLZ,MDT,MET,MMM,MO,MON,MRK,MS,MSFT,NEE,NKE,ORCL,OXY,PCLN,PEP,PFE,PG,PM,PYPL,QCOM,RTN,SBUX,SLB,SO,SPG,T,TGT,TWX,TXN,UNH,UNP,UPS,USB,USD,UTX,V,VZ,WBA,WFC".split(
#     ',')

tickers = ["MSFT"]
for c in tickers:
    getData(c)

count = 0
for i in df.iterrows():

    date = i[1][1]
    tick = i[1][2]
    date = date.strftime("%-m/%-d/%Y")
    # print(all_dates[tick])
    # print(date)
    if tick in all_dates:
        if date in all_dates[tick]:
            df.at[i[0], 'earning_flag'] = 1

    count += 1
    # break
df.to_excel('output.xlsx')
# print(df)
print(all_dates)
