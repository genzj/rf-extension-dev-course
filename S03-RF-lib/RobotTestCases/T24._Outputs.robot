*** Settings ***
Library           libs/Outputs.py

*** Test Cases ***
Library Outputs
    Run Keyword And Continue On Failure    Should Be Nice    bad
    Run Keyword And Continue On Failure    Should Be Nice Again    bad
    Test Logs

Debug
    Log    step1
    Log    step2
    Comment    PAUSE
    Log    step3
    Comment    PAUSE
    Log    step4
    Log    step5
