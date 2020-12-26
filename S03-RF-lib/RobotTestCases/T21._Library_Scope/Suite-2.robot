*** Settings ***
Library           ../libs/T21-Scope/GlobalScope.py
Library           ../libs/T21-Scope/SuiteScope.py
Library           ../libs/T21-Scope/CaseScope.py

*** Test Cases ***
Test-2-1
    Should Be True    ${True}
    GlobalScope.kw
    SuiteScope.kw
    CaseScope.kw

Test-2-2
    Should Be True    ${True}
    GlobalScope.kw
    SuiteScope.kw
    CaseScope.kw
