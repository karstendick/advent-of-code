from collections import deque

with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

cards1 = deque()
cards2 = deque()

player2 = False
for line in lines:
  if not line:
    continue
  if line.startswith('Player 1'):
    continue
  if line.startswith('Player 2'):
    player2 = True
    continue
  if not player2:
    cards1.append(int(line))
  else:
    cards2.append(int(line))

print(cards1)
print()
print(cards2)

while len(cards1) > 0 and len(cards2) > 0:
  card1 = cards1.popleft()
  card2 = cards2.popleft()
  if card1 > card2:
    cards1.append(card1)
    cards1.append(card2)
  else:
    cards2.append(card2)
    cards2.append(card1)

def score_deck(cards):
  cards.reverse()
  score = 0
  for i, card in enumerate(cards):
    score += card * (i + 1)
  return score

print()
print(cards1)
print(cards2)

total = score_deck(cards1) + score_deck(cards2)

print(total)
