#!/usr/bin/env python
# coding: utf-8

# In[2]:



# import Splinter and Beautiful Soup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.opera import OperaDriverManager
import pandas as pd


# In[3]:


executable_path = {'executable_path': OperaDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[6]:


print(slide_elem.find('div', class_='content_title'))


# In[7]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # Image Scrapping

# In[9]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # MARS FACTS

# In[14]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[15]:


df.to_html


# # Hemispheres

# In[16]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[17]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
titles = []
html = browser.html
hemisphere_soup = soup(html, 'html.parser')

# 3. Write code to retrieve the image urls and titles for each hemisphere.
main_url = hemisphere_soup.find_all('div', class_='item')


# In[18]:


for x in main_url:
    title = x.find('h3').text
    title_url = x.find('a')['href']
    img_url = url  + x.find('img')['src']
    html = browser.html
    browser.visit(img_url)
    img_soup = soup(html, 'html.parser')
    soup_img_url = img_soup.find('img').get('src')
    img_data = dict({'title':title , 'img_url':soup_img_url})
    hemisphere_image_urls.append(img_data)


# In[19]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[20]:


len(hemisphere_image_urls)


# In[21]:


browser.quit()


# In[ ]:




