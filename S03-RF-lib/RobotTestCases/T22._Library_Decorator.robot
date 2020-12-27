*** Settings ***
Library           libs/MyClassAdd.py
Library           libs/MyDecoClassAdd.py

*** Test Cases ***
Auto Keyword
    ${x} =    MyClassAdd.Add    1    2
    ${x} =    MyClassAdd.To Num    203
    ${x} =    Ad d    1    2
    ${x} =    A dd    1    2
    ${x} =    a D D    1    2

Deco Keyword
    ${x}=    MyDecoClassAdd.Add as number    1    2
    ${x}=    MyDecoClassAdd.Add as number    2
    ${x}=    MyDecoClassAdd.减法    3    2
