#! /usr/python3

'''
Convert file of lists to dictionary object and serialize dictionary object
'''
import sys
import os
import pickle
import re


def file2dict(file):
  with open(file, 'r') as f:
    f_string = f.read()
  my_list = f_string.split('\n\n')
  my_list = [ item.split('\n') for item in my_list ]
  keys = [ item[0] for item in my_list ]
  values = [item[1:] for item in my_list ]
  my_dict = { category:items for category,items in zip(keys,values) }
  return my_dict

def main():
  my_dict = file2dict('favorites.txt')
  with open('favorites_dictionary.txt', 'ab') as f:
    pickle.dump(my_dict, f)
  print("dictionary object has been serialized")

if __name__ == '__main__':
  main()
