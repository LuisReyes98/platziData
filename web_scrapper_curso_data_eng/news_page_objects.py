from common import config
import requests
import bs4

class HomePage:

  def __init__(self, new_site_uid, url):
    self.__config = config()['news_sites'][new_site_uid]
    self.__queries = self.__config['queries']
    self._html = None
    self._visit(url)

  @property
  def article_links(self):
    link_list = []
    for link in self._select(self.__queries['homepage_article_links']):
      if link and link.has_attr('href'):
        link_list.append(link)

    return set(link['href'] for link in link_list )


  def _select(self, query_string):
    return self._html.select(query_string)

  def _visit(self, url):
    response = requests.get(url)

    response.raise_for_status()

    self._html = bs4.BeautifulSoup(response.text, 'html.parser')
