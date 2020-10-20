def writefile(filename):
  outfile = open(filename, 'w') 
  content = outfile.write('Olá novo documento!\n')  
  outfile.close()
  return print('Informações adicionadas com sucesso!!!')   

writefile('write.txt')
