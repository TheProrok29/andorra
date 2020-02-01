*** Settings ***
Library  SeleniumLibrary
Resource    common.robot

Suite Teardown    Close All Browsers

*** Variables ***
${ERROR_TXT}    Please enter a correct username and password. Note that both fields may be case-sensitive.

*** Test Cases ***
Correct Login Logout Test
    Open Chrome
    Element Should Contain    xpath://*[@id="login"]    Log in
    Click Element    xpath://*[@id="login"]
    Sleep    1
    Click Element    name=username
    Input Text    name=username   Robot
    Click Element    name=password
    Input Text    name=password    Passw0rd!
    Submit Form    xpath://*[@id="loginForm"]
    Wait Until Page Contains Element    xpath:/html/body/main/div
    Element Should Contain    xpath:/html/body/main/div/div/h2    Welcome Robot
    Sleep    1
    Click Element    xpath://a[@id="logout"]
    Wait Until Page Contains Element    xpath://*[@id="login"]
    Element Should Contain    xpath:/html/body/main/div/div/h2    Welcome to the game!
    [Teardown]  Close Browser

Incorrect Login Test
    Open Chrome
    Element Should Contain    xpath://*[@id="login"]    Log in
    Click Element    xpath://*[@id="login"]
    Sleep    1
    Click Element    name:username
    Input Text    name:username   Robot
    Click Element    name:password
    Input Text    name:password    qwewqe!
    Submit Form    xpath://*[@id="loginForm"]
    Wait Until Page Contains Element    //*[@id="loginForm"]/div[2]/div[2]/ul/li
    Element Should Contain    //*[@id="loginForm"]/div[2]/div[2]/ul/li    ${ERROR_TXT}
    [Teardown]  Close Browser
