import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

movies = pd.read_csv('movies.csv') #đọc file csv
genreList = []
for movie in movies['genres']:
	genreArray = movie.split('|') #tách thể loại phim
	for genre in genreArray:
		genreList.append(genre)
genreIterator = iter(genreList)
counter = Counter()
for word in genreIterator:
	counter[word] += 1
tan_suat_phim = pd.Series(counter) #đếm tần suất phim


tan_xuat_phim_sort = tan_suat_phim.sort_values(ascending=False) #sắp xếp theo thứ tự
print(tan_xuat_phim_sort)

tan_xuat_phim_sort.plot(kind='bar') #tạo đồ thị
plt.show()

movies['genre'] = movies['genres'].apply(lambda x: x.split('|'))
movies["year"] = movies["title"].apply(lambda x: x[-5:-1]) #tách năm

movies['year']=pd.to_numeric(movies['year'],errors='coerce',downcast='integer')

theloai_drama=movies[movies['genres'].str.contains("Drama")]

theloai_drama.groupby('year').size().plot(kind='line') #nhóm theo năm và vẽ đồ thị line
plt.show()

top3 = tan_xuat_phim_sort.head(3).index.tolist()


no1=movies[movies['genres'].str.contains(top3[0])]
no2=movies[movies['genres'].str.contains(top3[1])]
no3=movies[movies['genres'].str.contains(top3[2])]
print(no1)

no1.groupby('year').size().plot(kind='line', label = 'Drama')
no2.groupby('year').size().plot(kind='line', label = 'Comedy')
no3.groupby('year').size().plot(kind='line', label = 'Thriller') #vẽ các loại đồ thị vào cùng 1 bảng

plt.legend()
plt.show()