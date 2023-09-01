# My solution to arithmetic arranger problem by FreeCodeCamp

def arithmetic_arranger(problems, answers = False):

  if len(problems) > 5:
    return 'Error: Too many problems.'
    
  prlist = []
  for p in problems: 
    prlist += p.split(' ')
  prbs = [prlist[x:x+3] for x in range(0, len(prlist), 3)]
      
  nums1 = [list[0] for list in prbs]
  operator = [list[1] for list in prbs]
  nums2 = [list[2] for list in prbs]

  for s in nums1 + nums2:
    for ch in s:
      if ch not in '0123456789':
        return 'Error: Numbers must only contain digits.'
    if len(s) > 4:
      return 'Error: Numbers cannot be more than four digits.'

  top_row = ''
  bottom_row = ''
  dashes = ''
  
  maxlen = []
  for i in range(len(problems)):
    if int(nums1[i]) >= int(nums2[i]):
      maxlen.append(len(nums1[i]))
    else:
      maxlen.append(len(nums2[i]))
  for i in range(len(problems)): 
    top_row += nums1[i].rjust(maxlen[i] + 2) + '    ' 
    bottom_row += operator[i] + ' ' + nums2[i].rjust(maxlen[i]) + '    '
    dashes += '-' * (maxlen[i] + 2) + '    '
  top_row , bottom_row , dashes = top_row[:-4] , bottom_row[:-4] , dashes[:-4]

  result = '{}\n{}\n{}'.format(top_row, bottom_row, dashes)

  solutions = []
  for i in range(len(operator)):
    if operator[i] == '+':
      solutions.append(str(int(nums1[i]) + int(nums2[i])))
    elif operator[i] == '-':
      solutions.append(str(int(nums1[i]) - int(nums2[i])))
    else: 
      return "Error: Operator must be '+' or '-'."

  solution_row = ''
  for i in range(len(problems)):
    solution_row += solutions[i].rjust(maxlen[i] + 2) + '    '
  solution_row = solution_row[:-4]
  
  if not answers:
    return result
  else:
    with_solutions = '{}\n{}\n{}\n{}'.format(top_row, bottom_row, dashes, solution_row)
    return with_solutions

# Testing...
# probs1 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
# probs2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
# print(arithmetic_arranger(probs1, True))