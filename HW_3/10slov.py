import requests
from collections import Counter
import re

url = "https://ru.wikipedia.org/wiki/Космическое_пространство#Межзвёздное_пространство"
response = requests.get(url)
text = response.text

words = re.findall(r'\b\w+\b', text, re.IGNORECASE)

word_count = Counter(words)
top_ten = word_count.most_common(10)

print("10 самых часто встречающихся слов в текстовой строке:")
for word, count in top_ten:
    print(f"{word}: {count}")