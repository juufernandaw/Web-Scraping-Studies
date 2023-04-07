from requests_html import HTMLSession
#essa biblioteca possibilita ler códigos em JS

session = HTMLSession()
response = session.get(url='https://pt.wikipedia.org/wiki/The_Football_Association')
response.status_code

parsed_object = response.html

# Obtaining all the (relative) links from the page:
urls = response.html.links
type(urls)  # set

# Obtaining all the (absolute) links from the page:
full_path_urls = response.html.absolute_links
type(full_path_urls)  # set
# both return a set

# searching for elements
links = response.html.find('a')  # Returns a list of elements (it behaves like the 'find_all()' method from bs4)
print(links[4])  # <Element 'a' class=('mw-jump-link',) href='#mw-head'>
links[4].html  # <a class="mw-jump-link" href="#mw-head">Jump to navigation</a>
links[4].text  # 'Jump to navigation'
links[4].attrs  # {'class': ('mw-jump-link',), 'href': '#mw-head'}

# Searching for tags that containing a certain 'string'
# Find all tags that contain the string 'wikipedia':
a_wiki = response.html.find('a', containing='wikipedia')

# Find all text associated with tags that contain the string 'wikipedia', all stored inside a list:
list_of_tags = [tag.text for tag in response.html.find('a', containing='wikipedia')]

paragrafos = response.html.find('p', first=True)  # Similar to method 'find()' from bs4
