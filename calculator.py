#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_number(prompt):
    while True:
        try:
            s = input(prompt)
            return float(s)
        except ValueError:
            print("קלט לא תקין — אנא הכנס מספר.")

def get_operation():
    ops = {
        '+': 'add',
        '-': 'sub',
        '*': 'mul',
        '/': 'div',
        'add': 'add',
        'sub': 'sub',
        'mul': 'mul',
        'div': 'div'
    }
    prompt = "בחר פעולה (+, -, *, /) או הקלד add, sub, mul, div: "
    while True:
        op = input(prompt).strip().lower()
        if op in ops:
            return ops[op]
        print("פעולה לא מוכרת — נסה שוב.")

def main():
    print("מחשבון אינטראקטיבי — הקש רווח ואז Enter כדי לצאת.")
    while True:
        a = get_number("הכנס מספר ראשון: ")
        b = get_number("הכנס מספר שני: ")
        op = get_operation()
        try:
            if op == 'add':
                res = a + b
            elif op == 'sub':
                res = a - b
            elif op == 'mul':
                res = a * b
            elif op == 'div':
                res = a / b
            print(f"התוצאה: {res}")
        except ZeroDivisionError:
            print("שגיאה: חלוקה באפס אינה מוגדרת.")

        resp = input("הקש רווח ואז Enter ליציאה, או הקש Enter להמשך: ")
        if resp == ' ':
            print("יוצא. להתראות!")
            break

if __name__ == "__main__":
    main()
