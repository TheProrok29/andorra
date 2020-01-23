*** Settings ***
Library  SeleniumLibrary

Suite Teardown    Close All Browsers

*** Variables ***
${LOGIN_URL}          http://127.0.0.1:8000/
${BROWSER}      Chrome

*** Test Cases ***
Training functionality
  Open Chrome
  Click Element    xpath://*[@id="training"]
  Element Should Contain    xpath://*[@id="character-title"]    Character training
  Click Element    css:.btn-success
  Click Element    xpath://*[@id="stop_button"]
  Sleep    21
  Element Should Contain    xpath://*[@id="number_session"]    1
  Click Element    xpath://*[@id="exit_button"]
  [Teardown]  Close Browser

*** Keywords ***
Open Chrome
    ${chrome_options}    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}   add_argument    no-cache
    Call Method    ${chrome_options}   add_argument    no-sandbox
    Call Method    ${chrome_options}   add_argument    disable-dev-shm-usage
    ${options}    Call Method     ${chrome_options}    to_capabilities
    Open Browser    ${LOGIN_URL}    browser=${BROWSER}    desired_capabilities=${options}
