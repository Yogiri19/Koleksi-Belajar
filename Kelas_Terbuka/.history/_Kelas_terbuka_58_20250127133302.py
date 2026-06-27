import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now : {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"hari : {data_waktu.strftime('%A')} ")

from collections import Counter

data = ["a", "b","c","d","a","d","e"]