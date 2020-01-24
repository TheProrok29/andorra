*** Settings ***
Library  SeleniumLibrary
Resource    common.robot

Suite Teardown    Close All Browsers

*** Variables ***
${LOGIN_URL}          http://127.0.0.1:8000/
${BROWSER}      Chrome


*** Test Cases ***
Correct homepage
    Open Chrome
    Element Should Contain    xpath://*[@id="navbarCollapse"]/div/h4    Main page
    Element Should Contain    css:.text-muted    Andorra RPG game
    [Teardown]  Close Browser

Nav elements visible
    Open Chrome
    Page Should Contain Element    xpath://*[@id="login"]
    Page Should Contain Element    xpath://*[@id="register"]
    Page Should Contain Element    xpath://*[@id="journeys"]
    Page Should Contain Element    xpath://*[@id="login"]
    Page Should Contain Element    xpath://*[@id="training"]
    Page Should Contain Element    xpath://*[@id="statistics"]
    Page Should Contain Element    xpath://*[@id="login"]
    Page Should Contain Element    xpath://*[@id="logout"]
    [Teardown]  Close Browser

Journeys functionality
    Open Chrome
    Click element                   xpath://*[@id="journeys"]
    Wait until element is visible   xpath://*[@id="journey-title"]
    Element Should Contain          xpath://*[@id="journey-title"]   Available journeys
    Submit Form                     xpath://*[@id="form-id"]
    Wait until element is visible   xpath://*[@id="countdown-1"]
    Element Should Contain          xpath://*[@id="countdown-1"]    You'll have to wait another:
    [Teardown]  Close Browser

Statistics functionality
    Open Chrome
    Click Element                   xpath://*[@id="statistics"]
    Element Should Be Visible       xpath:/html/body/main
    Wait until element is visible   xpath://*[@id="statistics-title"]
    Element Should Contain          xpath://*[@id="statistics-title"]    Character statistics
    [Teardown]  Close Browser

*** Keywords ***
