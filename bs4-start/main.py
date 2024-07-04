from pprint import pprint

from bs4 import BeautifulSoup
import requests

# Fetch the HTML content
response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()  # Check if the request was successful

hacker_news = response.text
soup = BeautifulSoup(hacker_news, "html.parser")

# Find all span elements with class 'titleline'
titleline_spans = soup.find_all('span', class_='titleline')
#print(titleline_spans)
# Extract the first anchor tag from each span
first_anchors = []
for span in titleline_spans:
    first_anchor = span.find('a')
    first_anchors.append(first_anchor)

# get Title and link:
title_link = []
title_text = []
for text in first_anchors:
    title_text.append(text.text)
    title_link.append(text.get("href"))

# get the score
score = soup.find_all( name="span", class_='score')
title_score = []
for span in score:
    to_score = span.text
    title_score.append(to_score)

score = []
for s in title_score:
    points_list = int(s.split(" ")[0])
    score.append(points_list)

#print(title_text)
#print(title_link)
#print(score)

sorted_score = sorted(score)[::-1]
#print(sorted_score)
index_numbers = []
for scr in sorted_score:
    index_num = score.index(scr)
    index_numbers.append(index_num)

#print(index_numbers)

title_text_final = [title_text[i] for i in index_numbers]
title_link_final = [title_link[i] for i in index_numbers]

print(title_text_final)
print(title_link_final)
#print(index_numbers)
#print(score)
print(sorted_score)


