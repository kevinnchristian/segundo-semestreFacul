def readfile(filename):
  infile = open(filename, 'r')   # Abrindo arquivo em modo leitura
  content = infile.read()   # Fazendo leitura do arquivo e armazenando na variável content
  infile.close()   # Fechando o arquivo
  wordlist = content.split()  # Dividindo o arquivo por tokens ou palavras com função split()
  print(wordlist)   # Imprimindo informações
  return len(wordlist), len(content)   # Retornando quantidade de palavras e caracteres que li do arquivo

n_words, n_chars = readfile('teste.txt')
print('Número de palavras lidas:', n_words)
print('Número de caracteres lidos:', n_chars)