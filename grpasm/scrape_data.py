import requests
from bs4 import BeautifulSoup

# Specify the URL of WikiNews
url = 'https://en.wikinews.org/wiki/Main_Page'

# Send a GET request to fetch the content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(response.status_code)



# # Find the section containing news articles
# news_section = soup.find_all('div', class_='mainpage')

# # List to hold scraped data
# news_data = []

# # Loop through articles in the news section
# for article in news_section:
#     # Find all articles (h2 tags for news titles)
#     titles = article.find_all('h2')
    
#     for title in titles:
#         # Extract the title text
#         title_text = title.get_text(strip=True)
        
#         # Extract categories (if available)
#         categories = [cat.get_text(strip=True) for cat in title.find_next('ul').find_all('li')] if title.find_next('ul') else []

#         # Format the output
#         category_str = ', '.join(categories) if categories else 'No categories'
#         news_data.append(f'Title: {title_text}\nCategories: {category_str}\n')
# print("Scraping complete. Preparing to save to file...")


# # Save the data to a text file
# with open('wikinews_articles.txt', 'w', encoding='utf-8') as file:
#     file.writelines(news_data)

# print("Data scraped and saved to wikinews_articles.txt")
