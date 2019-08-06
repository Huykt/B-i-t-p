import pandas as pd
from collections import Counter

movies = pd.read_csv("movies.csv")
stopWords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

movieTitles = movies.title.str[:-7] #loại year ra khỏi tiêu đề film
movieTitles = movieTitles.str.lower() #chuyển tiêu đề phim về dạng chữ thường để đồng bộ
movieTitles = movieTitles.str.strip() #bỏ khoảng trắng ở đầu và cuối

wordList = []
for title in movieTitles:
	words = title.split(' ') #tách chữ
	for word in words:
		if word not in stopWords:
			wordList.append(word)
counter = Counter()
for word in wordList:
	counter[word] += 1
wordFrequency = pd.Series(counter) #đếm số lần xuất hiện

wordSeries = pd.Series(wordFrequency).sort_values(ascending=False) #sắp xếp theo thứ tự

print(wordSeries.nlargest(10)) #in kết quả
