def sep(text='', n=40):
  if text == '':
    text = "="
  else:
    text = "["+text+"]"
  amount = '{:=^'+str(n)+'}'
  text = amount.format(text)
  print(text)
def br(line=1):
  for i in range(line):
    print('')
