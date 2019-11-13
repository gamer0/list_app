#! /usr/bin/python3

'''main app for adding lists and entries'''

import sys
import pickle


with open('favorites_dictionary.txt','rb') as f:
  favorites_dict = pickle.load(f) # deserializes file to dictionary object
for key in favorites_dict.keys():
  favorites_dict[key] =  sorted(favorites_dict[key])
  if "" in favorites_dict[key]: favorites_dict[key].remove('')

categories = tuple(sorted(favorites_dict.keys())) # tuple of categories
options = ('-a','-d','-v', '-h') # tuple of actions that can be taken
cli_params = tuple(sys.argv[1:])


def delete(category, my_dict=favorites_dict):
  my_dict[category[0]] = [entry for entry in my_dict[category[0]] if entry not in category[1:]]
  return {category[0]:my_dict[category[0]]}

def add(category, my_dict=favorites_dict):
  if category[0] in categories:
    my_dict[category[0]].extend(category[1:])
  else:
    my_dict[category[0]] = []
    my_dict[category[0]].extend(category[1:])
  return {category[0]:my_dict[category[0]]}

def usage():
  instructions = 'usage: \npython3 listapp.py -option -arguments\nexample: python3 listapp.py -a shows black_mirror \
  \n-a add, -d delete, -v view'
  return instructions

def view(categories, my_dict=favorites_dict):
  return {category:my_dict[category] for category in categories}

def val_arg(args_list):
  if len(args_list) == 0:
    return True
  if len(args_list) == 1:
    return lambda: args_list[1]  == '-h'
  if len(args_list) >= 2:
    return lambda: args_list[1] in options

def main():
  dispatch_table = {'-a':add,'-d':delete,'-v':view,'-h':usage}

  assert val_arg(cli_params), 'somebody fucked up'

  if len(cli_params) == 0:
    print('A list of categories')
    print(*categories, sep='\n')
    print('\nuse -h option for help menu')
  elif len(cli_params) == 1:
    print(usage())
  else:
    result = dispatch_table[cli_params[0]](cli_params[1:])
    for key in result.keys():
      print(key)
      print(*result[key], sep='||')

  with open('favorites_dictionary.txt','wb') as f:
    pickle.dump(favorites_dict, f) # serializes dictionary object

if __name__ == '__main__':
  main()

