*** Settings ***
Library  SeleniumLibrary
Resource    common.robot

Suite Teardown    Close All Browsers

*** Test Cases ***
Correct homepage
    Open Chrome
    Element Should Contain    css:.text-muted    Andorra RPG game
    [Teardown]  Close Browser

Nav elements visible
    Open Chrome
    Page Should Contain Element    xpath://*[@id="login"]
    Page Should Contain Element    xpath://*[@id="signup"]
    Page Should Contain Element    xpath://*[@id="journeys"]
    Page Should Contain Element    xpath://*[@id="training_start"]
    Page Should Contain Element    xpath://*[@id="statistics"]
    Page Should Contain Element    xpath://*[@id="login"]
    [Teardown]  Close Browser

Journeys page
    Open Chrome
    Click element                   xpath://*[@id="journeys"]
    Wait until element is visible   xpath://*[@id="journey-title"]
    Element Should Contain          xpath://*[@id="journey-title"]   Available journeys
    Submit Form                     xpath://*[@id="form-id"]
    Wait until element is visible   xpath://*[@id="countdown-1"]
    Element Should Contain          xpath://*[@id="countdown-1"]    You'll have to wait another:
    [Teardown]  Close Browser

Statistics page
    Open Chrome
    Click Element                   xpath://*[@id="statistics"]
    Element Should Be Visible       xpath:/html/body/main
    Wait until element is visible   xpath://*[@id="statistics-title"]
    Element Should Contain          xpath://*[@id="statistics-title"]    Character statistics
    [Teardown]  Close Browser
