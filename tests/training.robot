*** Settings ***
Library  SeleniumLibrary
Resource    common.robot

Suite Teardown    Close All Browsers

*** Test Cases ***
Training functionality
  Open Chrome
  Click Element    xpath://*[@id="training_start"]
  Element Should Contain    xpath://*[@id="character-title"]    Character training
  Wait Until Page Contains Element    css:.btn-success
  Click Element    css:.btn-success
  Click Element    xpath://*[@id="stop_button"]
  Sleep    21
  Element Should Contain    xpath://*[@id="training_done_counter"]    1
  Click Element    xpath://*[@id="exit_button"]
  [Teardown]  Close Browser
