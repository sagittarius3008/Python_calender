# 要件
# 条件１、その月は何曜日始まりか
# 条件２、その月の日数はいくつか
    # うるう年：4の倍数、100の倍数ではない、400の倍数の年=>2月29日マデ
print("カレンダーの表示年月を指定してください")
year = int(input("何年？"))
month = int(input("何月？"))

# うるう年の判定
def leap_year(year):
    if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return True
    else:
        return False

# 該当月の日数の判定
def month_days(year, month):
    month_with_30days = [4, 6, 9, 11]
    days = 31
    if month == 2:
        if leap_year(year):
            days = 29
        else:
            days = 28
    elif month in month_with_30days:
        days = 30
    return days
    
    
# 1900年1月1日からの経過日数の計算
# 1900年から該当年までの日数を計算
def total_days(year, month):
    total = 0
    for i in range(1900, year):
        if leap_year(i):
            total += 366
        else:
            total += 365
    # 該当年1月から当月までの日数を計算
    for j in range(1, month):
        total += month_days(year, j)
    print(total)
    return total
    
print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")
week_day = total_days(year, month) % 7 + 1
# カレンダーの開始位置を指定
for i in range(week_day % 7):
    print('\t', end='')
# カレンダー
for j in range(1, month_days(year, month) + 1):
    print(j, '\t', end=''),
    week_day += 1
    if week_day % 7 == 0:
      print('')