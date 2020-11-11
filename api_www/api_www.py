from urllib.request import urlopen  # Importando a função urlopen da biblioteca
from html.parser import HTMLParser

class MyParser(HTMLParser):
  def handle_starttag(self, tag, attrs):  # tag são as tags do HTML, attrs atributos destas tag's
    if tag == 'a':
      for attr in attrs:
        if attr[0] == 'href':
          print(attr[1])

def getSource(url):
  response = urlopen(url)  # Faz a requisação HTTP pela URL passada
  html = response.read()   # Obtêm a informações que vira da requisição
  return html.decode()     # Vai fazer o decode da informação, enviando para fora 
                           # da função uma string contendo os elementos do HTML da requisição

req_html = getSource('http://www.uol.com.br')
print(req_html)
print('-----------------------------------------------------------------------')
print(' ')

parser = MyParser()  # Instância a class MyParser criada 
parser.feed(req_html)  # Executa método feed() estendido do HTMLParser, imprime 
                       # todos elementos href do HTML requistado


