A = input("Room A: ").strip().upper()
B = input("Room B: ").strip().upper()
pos = input("Position (A/B): ").strip().upper()

rooms = {'A': A, 'B': B}

if rooms[pos] == "DIRTY":
    print("SUCK")
    rooms[pos] = "CLEAN"


other = 'B' if pos == 'A' else 'A'


if rooms[other] == "DIRTY":
    print("MOVE RIGHT" if pos == 'A' else "MOVE LEFT")
    pos = other
    print("SUCK")
    rooms[pos] = "CLEAN"

print("Final State:", rooms)