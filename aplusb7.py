import sys

score_dict = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

for line in sys.stdin:
    row = line.split()
    score_list = []
    is_unknown = False
    for e in row:
        score = score_dict.get(e)
        if score is None:
            print('Unknown')
            is_unknown = True
            break
        score_list.append(score)
    if is_unknown is False:
        print(f"{sum(score_list) / len(score_list):.2f}")
