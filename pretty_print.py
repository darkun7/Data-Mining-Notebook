def sep(text = ''):
  if text == '':
    text = "-"
  else:
    text = "["+text+"]"
  print("=-=-=-=-=-="+text+"=-=-=-=-=-=")
def br(line=1):
  for i in range(line):
    print('')