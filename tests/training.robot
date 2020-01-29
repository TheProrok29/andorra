*** Settings ***
Library  SeleniumLibrary
Resource    common.robot

Suite Teardown    Close All Browsers

*** Test Cases ***
Training functionality
  Open Chrome
  Click Element    xpath://*[@id="training"]
  Element Should Contain    xpath://*[@id="character-title"]    Character training
  Sleep    1
  Click Element    css:.btn-success
  Click Element    xpath://*[@id="stop_button"]
  Sleep    22
  Element Should Contain    xpath://*[@id="number_session"]    1
  Click Element    xpath://*[@id="exit_button"]
  [Teardown]  Close Browser
