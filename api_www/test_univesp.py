from urllib.request import urlopen, Request
from html.parser import HTMLParser

class MyParser(HTMLParser):
  def __init__(self):   # Método de inicialização, que vai chamar método de incialização do HTMLParser
    HTMLParser.__init__(self)
    self.n_polos = 0  # Set o numero de polos

  def handle_starttag(self, tag, attrs):  
    if tag == 'p':  # Se a tag for <p>
      for attr in attrs:
        if attr[0] == 'class' and attr[1] == 'item-polos':  # Se a class == item-polos, tras o texto de dentro da tag
          self.n_polos += 1
  
  def num_polos(self):
    return self.n_polos  # Retorna o número de polos

def getSource(url):  # Esse código tem que informa o headers por questão de segurança do Servidor, para assim ele aceitar a requisição
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
  req_url = 'https:XXXX0000'
  req = Request(url = url, headers=headers)
  html = urlopen(req).read()
  return html.decode()


req_html = getSource('https://univesp.br/cursos/bacharel-em-ciencia-de-dados')
parser = MyParser()
parser.feed(req_html)
print('Número de polos:', parser.num_polos())