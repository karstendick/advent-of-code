inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip().split())

# print(inp)

shape_to_scores = {'X': 1,
                   'Y': 2,
                   'Z': 3}
def shape_score(my_shape):
  return shape_to_scores[my_shape]

def score_round(opp_shape, my_shape):
  if opp_shape == 'A': #rock
    scores = {'X': 3, #rock
              'Y': 6, #paper
              'Z': 0} #scissors
    return scores[my_shape]
  if opp_shape == 'B': #paper
    scores = {'X': 0, #rock
              'Y': 3, #paper
              'Z': 6} #scissors
    return scores[my_shape]
  if opp_shape == 'C': #scissors
    scores = {'X': 6, #rock
              'Y': 0, #paper
              'Z': 3} #scissors
    return scores[my_shape]

total_score = 0
for opp_shape, my_shape in inp:
  total_score += shape_score(my_shape) + score_round(opp_shape, my_shape)

print(total_score)
