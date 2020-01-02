*** Settings ***
Library  SeleniumLibrary
Suite Setup  Setup chromedriver

*** Variables ***
${LOGIN URL}          http://automationpractice.com/index.php
${BROWSER}      Chrome
@{list} =   There is 1 error

*** Test Cases ***
Valid Login
    Open main page
    Go to login
    Input Username
    Input Password
    Login button
    Assert Successful Login
    [Teardown]  Close Browser

Invalid Login
    Open main page
    Go to login
    Input invalid login
    Input invalid password
    Login button
    Assert invalid
    [Teardown]  close browser

*** Keywords ***

Setup chromedriver
  Set Environment Variable  webdriver.chrome.driver  ${EXECDIR}/chromedriver
Open main page
    Open browser    ${LOGIN URL}   ${BROWSER}
    Title should be     My Store
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
