import string

articol = """
România a obținut o mare victorie în meciul cu Irlanda de Nord. Echipa națională s-a calificat în etapa următoare a competiției. 
Acesta este un succes important pentru jucători și pentru fani. Meciul a fost intens, iar golurile marcate în ultimele minute au decis rezultatul final.
"""
# 1
mijloc = len(articol) // 2
prima_parte = articol[:mijloc]
a_doua_parte = articol[mijloc:]

# Procesarea primei părți:
prima_parte = prima_parte.upper().strip()

# Procesarea celei de-a doua părți:
a_doua_parte = a_doua_parte[::-1]
a_doua_parte = a_doua_parte.capitalize()
a_doua_parte = ''.join([char for char in a_doua_parte if char not in string.punctuation])
# 2
rezultat_final = prima_parte + " " + a_doua_parte
print(rezultat_final)