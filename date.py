import datetime
import tushare as ts
start = datetime.date(2022, 5, 20)
end = datetime.date(2022, 6, 10)
for day in range(start.toordinal(), end.toordinal()):
    print(datetime.date.fromordinal(day))
