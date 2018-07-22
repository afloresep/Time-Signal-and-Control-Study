#!/usr/bin/python
# coding=utf-8

def programa(age):
 import datetime
 name= raw_input('Whats your name?: ')
 now= datetime.datetime.now()
 year= str(( now.year - age)+100)
 print (name + ' will be 100 years old on ' + year )

  #print sys.argv
if __name__ == "__main__":
      age= input('how old are you?: ')
      programa( int(age))
