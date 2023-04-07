import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Defining the url of the site
base_site = "https://en.wikipedia.org/wiki/Music"

# # Making a get request
# response = requests.get(base_site)
# response.status_code
#
# # Extracting the HTML
# html = response.content
#
# # Checking that the reply is indeed an HTML code by inspecting the first 100 symbols
# html[:100]
#
# # Convert HTML to a BeautifulSoup object. This will allow us to parse out content from the HTML more easily.
# # Using the default parser as it is included in Python
# soup = BeautifulSoup(html, "html.parser")
#
# # It is extremely useful to be able to check this file when searching where some info is located
# # or to see how was the document parsed
#
# # Exporting the HTML to a file
# with open('Wiki_response.html', 'wb') as file:
#     file.write(soup.prettify('utf-8'))
#
#
# # the 'with' statement is shorthand for a 'try-finally' block
# # open is function for opening/creating a file to edit
# # the 'wb' argument signifies the mode in which to edit the file - Writing in Bytes format
# # .prettify() modifies the HTML code with additional indentations for better readability

response = requests.get(base_site)
soup = BeautifulSoup(response.content, "html.parser") #pega o conteudo
div_notes = soup.find_all("div", {"role": "note"})

div_links = []

for div in div_notes:
    anchors = div.find_all('a')
    div_links.extend(anchors)

lista_urls = [urljoin(base_site, l.get('href')) for l in div_links]
par_text = []
i = 0

for url in lista_urls:
    response = requests.get(base_site) #requisita o acesso ao conteudo da pagina
    soup = BeautifulSoup(response.content, "html.parser") #pega o conteudo
    note_parse = soup.find_all("p")
    text = [p.text for p in note_parse]
    par_text.append(text)

page_text = ["".join(text) for txt in par_text]
url_to_text = dict(zip(lista_urls, page_text))
print(url_to_text)
