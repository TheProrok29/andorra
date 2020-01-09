*** Settings ***
Library  SeleniumLibrary

Suite Teardown    Close All Browsers

*** Variables ***
${LOGIN URL}          http://andorra-ts.herokuapp.com/
${BROWSER}      Chrome
${overview.element}    //a[contains(text(), \${selector})]

*** Test Cases ***
Nav elements visible
    Open Chrome
    Nav Check    log in
    Nav Check    register
    Nav Check    journeys
    Nav Check    trenning
    Nav Check    statistics
    Nav Check    log out
    [Teardown]  Close Browser


*** Keywords ***
Open Chrome
    ${chrome_options}    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}   add_argument    headless
    Call Method    ${chrome_options}   add_argument    no-cache
    Call Method    ${chrome_options}   add_argument    no-sandbox
    Call Method    ${chrome_options}   add_argument    disable-dev-shm-usage
    ${options}    Call Method     ${chrome_options}    to_capabilities
    Open Browser    ${LOGIN_URL}    browser=chrome    desired_capabilities=${options}
Nav Check
    [Arguments]  ${selector}
    ${locator}=  Replace variables  ${overview.element}
    log  locator is ${locator}
