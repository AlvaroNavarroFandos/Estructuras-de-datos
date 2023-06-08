#Coge el número del final del texto y lo convierte a entero
text = "X-DSPAM-Confidence:    0.8475"

pos_dos_puntos = text.find(':')
text_casi = text [pos_dos_puntos + 1:]
text_final = text_casi.lstrip()
num = float(text_final)
print(num)