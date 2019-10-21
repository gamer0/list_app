#! /usr/python3

'''main app for adding lists and entries'''

import sys
import pickle

  delete = lambda my_dict, category, *entries: my_dict[category] = [entry for entry in my_dict[category] if entry not in entries]
  add = lambda my_dict, category, *entries: my_dict[category].extend(entries)
  usage = lambda: instructions = 'usage: \npython cmd -option arguments\nexample: python3 listapp.py -a shows black_mirror'
  view = lambda my_dict, *categories: for category in categories: {category: my_dict[category]}
  view_all = lambda my_dict: my_dict

def main():
  with open('favorites_dictionary.txt','rb') as f:
    favorites_dict = pickle.load(f) # deserializes file to dictionary object
  categories = tuple(favorites_dict.keys()) # tuple of categories
  options = ('-a','-d','-v') # tuple of actions that can be taken
  cli_params = sys.argv[1:]
  if len(sys.argv) == 1:
    print(usage())
  else:
    assert cli_params[0] in options, 'somebody fucked up, try again'
    if cmdline_parameters in options:
      if cmdline_parameters[0] == '-a': add(favorites_dict, cmdline_parameters)

  # test suite
  add_entry(favorites_dict, 'shows','the rising','the downing')


if __name__ == '__main__':
  main()
