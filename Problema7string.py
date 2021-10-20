#REZOLVĂ! Elaboraţi un program care citeşte de 
# la tastatură şirul de caractere S şi afişează pe ecran:
#a) numărul de apariţii ale caracterului ’A’ în şirul S;
#b) şirul obţinut prin substituirea caracterului ’A’ prin caracterul ’*’;
#c) şirul obţinut prin radierea din şirul S a tuturor apariţiilor caracterului ’B’;
#d) numărul de apariţii ale silabei MA în şirul S;
#e) şirul obţinut prin substituirea tuturor apariţiilor în şirul S a silabei MA prin silaba TA;
#f) şirul obţinut prin radierea din şirul S a tuturor apariţiilor silabei TO;
#g)scrierea inversă a şirului S;
# h) true dacă şirul S este palindrom şi false în caz contrar;
# i) şirul obţinut prin transformarea tuturor literelor mici din componenţa şirului S în litere mari;
#j) şirul obţinut prin transformarea primei litere a fiecăruia dintre cuvintele din componenţa şirului S în literă mare;
# k) şirul obţinut prin sortarea în ordine alfabetică a caracterelor din şirul S.
sir= str(input('introdu sirul de caractere: \n'))
print("""a) numarul de aparitii a literei A in fraza / propozitia "{sir}" \neste: {numar}""". format(sir=sir, numar=sir.count('A')))
print("""b) Inlocuirea caracterului 'A' prin caracterul '*': """, sir.replace('A', '*'))
print('c) Radierea literei "B" din {sirul_initial}\nSirul obtinut este: {sir_final}'. format(sirul_initial=sir, sir_final=sir.replace('B', ' ')))
print("""d) Aparitia silabei "MA" in \n{sir}\neste : {numar} """.format(sir=sir, numar=sir.count('MA')))
print("""e) Inlocuirea silabei 'MA' prin 'TA'\n{sir_e} """. format(sir_e=sir.replace('MA', 'TA')))
print("""f) sirul obtinut din '{sir}' prin radiearea silabei 'TO'\n{c}""".format(sir=sir, c=sir.replace('TO', ' ')))
print('g) Scrierea inversa a sirului initial este: ')
for i in reversed(range(0, len(sir))):
  print( sir[i], end='')
w=sir[::-1]
if w==sir:
  print("""\nh) '{q}': este polindrom""".format(q=sir))
else:
  print("""\nh) '{q}' nu este polindrom""".format(q=sir))
print("""\ni) formatarea sirului initial: {sir}\ncu litere mari in intregime: {e}""".format(sir=sir, e=sir.upper()))
z=sir.split(' ')
print('Sirul initial: ')
for i in range(0, len(z)):
  print(str(z[i]), end=" ")
print('\nj) convertirea literelor initiale ale cuvintelor in litere mari: ')
for i in range(0, len(z)):
  q=z[i]
  print(q.title(), end=" ")
hg=[]
for i in range(0, len(sir)):
  hg.append(sir[i])
print("""\ni) Sortarea literelor din sirul initial: {joker}\nin ordine alfabetica\n{klk}""".format(joker=sir, klk=sorted(hg)))