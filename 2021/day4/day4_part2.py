with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

drawn_nums = [int(n) for n in lines[0].split(',')]
print(drawn_nums)

cards = []
card = []
marked_cards = []
marked_card = []
for line in lines[2:]:
  if line == '':
    print('empty line')
    cards.append(card)
    card = []

    marked_cards.append(marked_card)
    marked_card = []
  else:
    row = [int(n) for n in line.split()]
    card.append(row)

    marked_card.append([False for _ in line.split()])
cards.append(card)
card = []
marked_cards.append(marked_card)
marked_card = []

print(cards)
print(marked_cards)

def mark_cards(cards, marked_cards, drawn_num):
  for i in range(len(cards)):
    for r in range(5):
      for c in range(5):
        if cards[i][r][c] == drawn_num:
          marked_cards[i][r][c] = True
  return marked_cards

def is_card_winning(marked_card):
  for r in range(5):
    row = marked_card[r]
    if all(row):
      return True
  for c in range(5):
    col = [marked_card[r][c] for r in range(5)]
    if all(col):
      return True
  return False

def get_winning_card(cards, marked_cards):
  for i in range(len(marked_cards)):
    if is_card_winning(marked_cards[i]):
      return cards[i], marked_cards[i], i
  return None, None, None

def score_board(card, marked_card, drawn_num):
  s = 0
  for r in range(5):
    for c in range(5):
      if not marked_card[r][c]:
        s += card[r][c]
  return s * drawn_num

winning_card_is = set()
for drawn_num in drawn_nums:
  print(f'Bingo caller: {drawn_num}!')
  marked_cards = mark_cards(cards, marked_cards, drawn_num)
  winning_card, winning_marked_card, winning_card_i = get_winning_card(cards, marked_cards)
  if winning_card:
    if all([is_card_winning(marked_card) for marked_card in marked_cards]):
      print(f'The last card won!')
    
        
      print(winning_card)
      print(winning_marked_card)
      score = score_board(winning_card, winning_marked_card, drawn_num)
      print(f'Score: {score}')
      break
    cards.pop(winning_card_i)
    marked_cards.pop(winning_card_i)
