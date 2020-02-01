*** Settings ***
Library  SeleniumLibrary
Library  String
Resource    common.robot

Suite Teardown    Close All Browsers

*** Test Cases ***
Register test
    Open Chrome
    Element Should Contain    xpath://*[@id="register"]   Register
    Click Element    xpath://*[@id="register"]
    Sleep    1
    ${low}=    Generate Random String    12    [LOWER]
    Input Text    name:username    ${low}
    Input Text    name:email    thisissorandom@email.com
    Input Text    name:password1    Passw0rd!
    Input Text    name:password2    Passw0rd!
    Submit Form    xpath://*[@id="loginForm"]
    Element Should Contain    xpath://*[@id="loginForm"]/div[1]/div[2]/h2    Log in
    [Teardown]
