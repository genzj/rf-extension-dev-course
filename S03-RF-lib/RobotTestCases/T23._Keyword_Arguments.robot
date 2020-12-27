*** Settings ***
Library           libs/KeywordArgs.py

*** Test Cases ***
Argument Type
    ${x}=    Add as number    1    2
    Comment    Add as number    3.14    6.18
    ${x}=    减法    10    8
    ${x}=    减法    ${3}    ${20.1}
    ${x}=    Multiply    3.14    3
    ${x}=    Multiply    17    3

Advanced Arguments
    ${x}=    Add Many    1    2    3    4
    ${x} =     Add or sub    add1=10    sub1=8    add2=5    sub2=3
