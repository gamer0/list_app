#! /usr/python3


import sys
import pickle


def main():
  with open('favorites_dictionary.txt','rb') as f:
    unserialized_dict_obj = pickle.load(f)
  print(unserialized_dict_obj)

if __name__ == '__main__':
  main()
