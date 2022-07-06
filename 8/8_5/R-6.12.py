"""
Aufgabe:
What values are returned during the following sequence of deque ADT operations, on initially empty deque? add_first(4),
add_last(8), add_last(9), add_first(5), back( ), delete_first( ), delete_last( ), add_last(7), first( ), last( ),
add_last(6), delete_first( ), delete_first( ).


@Chaitanya
Lösung:
      Operation         Return Value         Dequeue
      add_first(4)      -                   [4]
      add_last(8)       -                   [8, 4]
      add_last(9)       -                   [9, 8, 4]
      add_first(5)      -                   [9, 8, 4, 5]
      back()            5                   [9, 8, 4, 5]        (Assuming that back returns last element added)
      delete_first()    5                   [9, 8, 4]
      delete_last()     9                   [8, 4]
      add_last(7)       -                   [7, 8, 4]
      first()           4                   [7, 8, 4]
      last()            7                   [7, 8, 4]
      add_last(6)       -                   [6, 7, 8, 4]
      delete_first()    4                   [6, 7, 8]
      delete_first()    8                   [6, 7]

"""