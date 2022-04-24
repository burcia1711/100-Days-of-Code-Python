# ------------------ SECOND PART ---------------
# Scrapping https://news.ycombinator.com/

from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
# print(response.text)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

# ----- Challange ------
# article_tag = soup.find(name="a", class_="titlelink")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_text)
# print(article_link)
# print(article_upvote)

# ---- cont. -----
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().strip("points")) for score in soup.find_all(name="span", class_="score")]
# print(article_texts)
# print(article_links)
# print(article_upvotes)

maxVoted_index = article_upvotes.index((max(article_upvotes)))
# print(maxVoted_index)

maxVoted_article = article_texts[maxVoted_index]
maxVoted_article_link = article_links[maxVoted_index]
print(maxVoted_article)
print(maxVoted_article_link)













# ------------------- FIRST PART -------------------
# from bs4 import BeautifulSoup
# #import lxml
#
# file_path = "website.html"
#
#
# with open(file_path, "r", encoding='utf-8') as f:
#     contents = f.read()
#
# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.class_)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)


