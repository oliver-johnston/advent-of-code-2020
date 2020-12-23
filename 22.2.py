from queue import Queue


def play_game(deck1, deck2):
    seen = set()

    while not deck1.empty() and not deck2.empty():
        if play_round(deck1, deck2, seen):
            return 1

    return 1 if deck2.empty() else 2


def copy(queue, length):
    deck = Queue()
    for x in list(queue.queue)[:length]:
        deck.put(x)
    return deck


def play_round(deck1, deck2, seen):
    card1 = deck1.get()
    card2 = deck2.get()

    if (tuple(deck1.queue), tuple(deck2.queue)) in seen:
        return True

    seen.add((tuple(deck1.queue), tuple(deck2.queue)))

    if deck1.qsize() >= card1 and deck2.qsize() >= card2:
        winner = play_game(copy(deck1, card1), copy(deck2, card2))
    else:
        winner = 1 if card1 > card2 else 2

    if winner == 1:
        deck1.put(card1)
        deck1.put(card2)
    else:
        deck2.put(card2)
        deck2.put(card1)

    return False


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

    winner = play_game(deck1, deck2)

    winner = deck1 if winner == 1 else deck2

    score = 0
    for i in range(1, len(winner.queue) + 1):
        score += winner.queue[-i] * i

    print(score)


if __name__ == "__main__":
    main()
