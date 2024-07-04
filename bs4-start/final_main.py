from bs4 import BeautifulSoup
import requests

# Fetch the HTML content
response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()  # Check if the request was successful

hacker_news = response.text
soup = BeautifulSoup(hacker_news, "html.parser")

# Find all span elements with class 'titleline'
titleline_spans = soup.find_all('span', class_='titleline')

# Extract the first anchor tag from each span and their corresponding scores
articles = []
for span in titleline_spans:
    first_anchor = span.find('a')
    title = first_anchor.text
    link = first_anchor.get('href')

    # The score span is not a sibling of the title span directly,
    # it is in the 'subtext' span which is a sibling of the parent 'tr' element of the title span
    parent_tr = span.find_parent('tr')
    if parent_tr:
        subtext_td = parent_tr.find_next_sibling('tr').find('td', class_='subtext')
        if subtext_td:
            score_span = subtext_td.find('span', class_='score')
            if score_span:
                score = int(score_span.text.split()[0])
                articles.append((title, link, score))
            else:
                print(f"No score found for: {title}")
        else:
            print(f"No subtext found for: {title}")
    else:
        print(f"No parent tr found for: {title}")

# Debug: Print all articles found before sorting
print("Articles before sorting:")
for title, link, score in articles:
    print(f"Title: {title}, Link: {link}, Score: {score}")

# Sort the articles by score in descending order
sorted_articles = sorted(articles, key=lambda x: x[2], reverse=True)

# Print the sorted titles and links
print("\nSorted Articles:")
for title, link, score in sorted_articles:
    print(f"Title: {title}, Link: {link}, Score: {score}")
