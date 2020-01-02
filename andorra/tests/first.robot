*** Settings ***
Library  SeleniumLibrary

Suite Teardown    Close All Browsers

*** Variables ***
${LOGIN URL}          http://automationpractice.com/index.php
${BROWSER}      Chrome
@{list} =   There is 1 error

*** Test Cases ***
Valid Login
    Open Chrome
    Go to login
    Input Username
    Input Password
    Login button
    Assert Successful Login
    [Teardown]  Close Browser

Invalid Login
    Open Chrome
    Go to login
    Input invalid login
    Input invalid password
    Login button
    Assert invalid
    [Teardown]  close browser

*** Keywords ***
Open Chrome
    ${chrome_options}    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}   add_argument    headless
    Call Method    ${chrome_options}   add_argument    no-cache
    Call Method    ${chrome_options}   add_argument    no-sandbox
    Call Method    ${chrome_options}   add_argument    disable-dev-shm-usage
    ${options}    Call Method     ${chrome_options}    to_capabilities
    Open Browser    ${LOGIN_URL}    browser=chrome    desired_capabilities=${options}
Go To Login
    click element   class=login
Input Username
    wait until element is visible   id=email
    Input Text  id=email  emailer5k+selen@gmail.com
Input password
    Input Text  id=passwd   12345
Login button
    click element  id=SubmitLogin
Assert Successful Login
    page should contain element  id=center_column
Input invalid login
    wait until element is visible   id=email
    Input Text  id=email  blednylogin@onet.pl
Input invalid password
    wait until element is visible   id=passwd
    Input Text  id=passwd   blednehaslo1
Assert invalid
    wait until element is visible   class=alert-danger
    get text    css=div.alert-danger p
    Should Contain Any   ${list}    There is 1 error
