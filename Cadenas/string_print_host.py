#Encuentra e imprime el host del correo en una linea de texto
data = 'alvaro.fandos@gmail.com Sat Jan  5 09:14:16 2008'

arroba_pos = data.find('@')
print(arroba_pos)

fin_email_pos = data.find(' ',arroba_pos)
print(fin_email_pos)

host = data[arroba_pos + 1:fin_email_pos]
print(host)