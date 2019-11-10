def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.

    r = ["Mario", "Bowser", "Luigi"]
    purple_shell(r)
     r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0], racers[-1] = racers[-1], racers[0]


r = ["Mario", "Bowser", "Luigi"]
purple_shell(r)
print(r)


def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
        name was fashionably late.
        """
    order = arrivals.index(name)  # index method returns the index of an element in a list
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1


verdict = print(fashionably_late(['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], 'Gilbert'))
