import datetime

data_waktu = datetime.datetime.now()
print(f"datetime nw : {data_waktu}")
print(f"hari : {data_waktu.strftime('%A')} ")

from collections import Counter

data = ["a", "b","c","d","a","d","e"]