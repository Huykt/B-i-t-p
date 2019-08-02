import pandas as pd

movies = pd.read_csv('movies.csv')

movies = movies.join(movies.genres.str.get_dummies()) #tạo các cột với biến giả

cotcantinh = movies.loc[:, "(no genres listed)":"Western"] #chỉ lấy các cột cần tính corr

print(cotcantinh.corr())