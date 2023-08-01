from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open("text.txt", encoding='utf8') as file:
    data = file.read()

wordcloud = WordCloud().generate(data)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
