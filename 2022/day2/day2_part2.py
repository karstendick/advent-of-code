inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip().split())

# print(inp)

shape_to_scores = {'X': 0,
                   'Y': 3,
                   'Z': 6}
def shape_score(outcome):
  return shape_to_scores[outcome]

# rock: 1
# paper: 2
# scissors: 3
def score_round(opp_shape, outcome):
  if opp_shape == 'A': #rock
    scores = {'X': 3, #lose
              'Y': 1, #draw
              'Z': 2} #win
    return scores[outcome]
  if opp_shape == 'B': #paper
    scores = {'X': 1, #lose
              'Y': 2, #draw
              'Z': 3} #win
    return scores[outcome]
  if opp_shape == 'C': #scissors
    scores = {'X': 2, #lose
              'Y': 3, #draw
              'Z': 1} #win
    return scores[outcome]

total_score = 0
for opp_shape, outcome in inp:
  total_score += shape_score(outcome) + score_round(opp_shape, outcome)

print(total_score)
