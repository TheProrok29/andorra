*** Variables ***
${URL}          http://127.0.0.1:8000/
${BROWSER}      Chrome

*** Keywords ***
Open Chrome
    ${chrome_options}    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}   add_argument    headless
    Call Method    ${chrome_options}   add_argument    no-cache
    Call Method    ${chrome_options}   add_argument    no-sandbox
    Call Method    ${chrome_options}   add_argument    disable-dev-shm-usage
    ${options}    Call Method     ${chrome_options}    to_capabilities
    Open Browser    ${URL}    browser=${BROWSER}    desired_capabilities=${options}
