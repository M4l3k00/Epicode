euro = input("quanti euro hai: ")
euro = float(euro)
p_oggetto = input("dammi il prezzo di un singolo oggetto: ")
p_oggetto = float(p_oggetto)

print('puoi comprare ', euro//p_oggetto,' unità')
print('il tuo resto è ', euro%p_oggetto)
