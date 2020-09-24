from random import shuffle
#function
def deck(cards, repeat):
    count = 1
    #the loop
    while again <= count:
        shuffle(count)
        print("Repeat: ", again)
        print(cards)
        count = count + 1
#output
card_deck = []

index = 1
while index <= 32:
    card_deck.append(index)
    index = index + 1
#return
print(card_deck)

deck(card_deck, 5)
