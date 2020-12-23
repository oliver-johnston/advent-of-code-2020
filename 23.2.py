class Node:
    def __init__(self, cup):
        self.cup = cup
        self.next = None


def play_round(head, tail, lookup):

    length = len(lookup) + 1
    current_cup = head
    head = head.next

    pick_up = []
    for _ in range(3):
        pick_up.append(head)
        head = head.next
        tail.next = head

    destination = (current_cup.cup - 1) % length
    while destination in [x.cup for x in pick_up] or destination == 0:
        destination = (destination - 1) % length

    destination_node = lookup[destination]

    pick_up[-1].next = destination_node.next
    destination_node.next = pick_up[0]

    if destination_node == tail:
        tail = pick_up[-1]

    tail.next = current_cup
    current_cup.next = head

    return head, current_cup


def get_result(cups):

    result = ""
    index = cups.index(1)
    for i in range(len(cups) - 1):
        result += str(cups[(index + i + 1) % len(cups)])

    return result


def main():

    cups = [int(x) for x in "962713854"] + list(range(10, 1000001))

    head = None
    tail = None
    for cup in cups[::-1]:
        node = Node(cup)
        if head is not None:
            node.next = head
        if tail is None:
            tail = node
        head = node

    tail.next = head

    lookup = dict()
    lookup[head.cup] = head
    cup = head.next
    while cup is not head:
        lookup[cup.cup] = cup
        cup = cup.next

    for i in range(10000000):
        head, tail = play_round(head, tail, lookup)

    one = lookup[1]

    print(one.next.cup * one.next.next.cup)


if __name__ == "__main__":
    main()
