import sys
def arithmetic_arranger(problems, result=False):
  if len(problems) > 5:
    return "Error: Too many problems."
    sys.exit()
  else:
    arranged_problems = ""
    first = ""
    second = ""
    lines = ""
    sumx =""
    string =""
    ops = {
      '+': lambda pair: str(pair[0] + pair[1]),
      '-': lambda pair: str(pair[0] - pair[1])}
    print (ops.keys())
    for problem in problems:
      chunks = problem.split()
      operator = chunks [1].strip()
      first_num = chunks[0].strip()
      second_num = chunks[2].strip()
      line_len = max(len(first_num), len(second_num)) + 2
      top = first_num.rjust(line_len)
      bottom = operator + second_num.rjust(line_len-1)
      line_dec = "-" * line_len
      
      if not all([i.isnumeric() for i in chunks[::2]]):
        return "Error: Numbers must only contain digits."
      elif chunks[1] not in ops.keys():
        return "Error: Operator must be '+' or '-'."
      elif len(max(chunks)) > 4:
        return "Error: Numbers cannot be more than four digits."
      sum= ""
  
      if (operator == "+"):
        sum = str(int(first_num) + int(second_num)).rjust(line_len)
      elif (operator =="-"):
        sum = str(int(first_num) - int(second_num)).rjust(line_len) 
        
      if (problem != problems[-1]):
        first += top + '    '
        second += bottom + '    '
        lines += line_dec +'    '
        sumx += sum + '    '
      else:
        first += top
        second += bottom
        lines += line_dec
        sumx += sum
      
  if result:
    arranged_problems = first+'\n' + second + '\n'+ lines + '\n' + sumx
  else:
    arranged_problems = first+'\n' + second + '\n'+ lines

  return arranged_problems