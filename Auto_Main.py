
import Auto_Funcs
from Auto_Funcs import *
x = int(input('Enter your limit: '))

while True:
    function = input('What you want to do? ')

    switch_add = True
    switch_sub = True

    if function == 'add':
        switch_add = True
        switch_sub = False
    elif function == 'sub':
        switch_sub = True
        switch_add = False

    while switch_add:
        auto_add(x)

    while switch_sub:
        # switch_add = False
        auto_sub(x)
