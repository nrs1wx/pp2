from datetime import datetime

date1 = datetime(2024, 2, 20, 10, 30, 0)
date2 = datetime(2024, 2, 22, 12, 45, 0)

difference_seconds = abs((date2 - date1).total_seconds())

print(difference_seconds)