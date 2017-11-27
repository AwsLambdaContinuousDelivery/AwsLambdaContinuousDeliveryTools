import re

regex = re.compile('[^a-zA-Z0-9]')

def alphanum(s: str) -> str:
  ''' Removes all non-alphanumeric characters '''
  return regex.sub('', s)