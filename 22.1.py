from queue import Queue


def play_round(deck1, deck2):
    card1 = deck1.get()
    card2 = deck2.get()

    if card1 > card2:
        deck1.put(card1)
        deck1.put(card2)
    else:
        deck2.put(card2)
        deck2.put(card1)


def get_deck(data):
    q = Queue()
    for x in (int(x) for x in data.splitlines()[1:]):
        q.put(x)
    return q


def main():
    data = open("input/22.txt").read().split("\n\n")

    decks = [get_deck(x) for x in data]

    deck1 = decks[0]
    deck2 = decks[1]

    while not deck1.empty() and not deck2.empty():
        play_round(deck1, deck2)

    winner = next(deck for deck in decks if not deck.empty())

    score = 0
    for i in range(1, len(winner.queue) + 1):
        score += winner.queue[-i] * i

    print(score)


if __name__ == "__main__":
    main()