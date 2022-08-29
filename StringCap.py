# Question: You are asked to ensure that the first and last names of people begin with
# a capital letter in their passports. For example, alison heck should be capitalised ecorrectly 
# as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.

#!/bin/python3
# Complete the solve function below.
def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s

if __name__ == '__main__':
    s = input('Enter full name: ')
    result = solve(s)
    print(result)