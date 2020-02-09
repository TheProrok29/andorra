*** Settings ***
Library  SeleniumLibrary
Resource    common.robot

Suite Teardown    Close All Browsers

*** Test Cases ***
Journey test
    Open Chrome
    Element Should Contain    xpath://*[@id="journeys"]   Journeys
    Click Element    xpath://*[@id="journeys"]
    Wait Until Page Contains Element    xpath://*[@id="form-id"]
    Click Element    xpath://*[@id="form-id"]/button
    Wait Until Page Contains Element    xpath://*[@id="countdown-1"]
    Element Should Contain    xpath://*[@id="countdown-1"]    You'll have to wait another:
    Sleep   20
    Element Should Not Be Visible    xpath://*[@id="countdown-1"]
    [Teardown]
