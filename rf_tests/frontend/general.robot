*** Settings ***
Library    RequestsLibrary
Documentation    Very basic test of frontend to determine if app responds
Suite Setup    Create Global Session
Suite Teardown    Delete All Sessions


*** Keywords ***
Create Global Session
    Create Session   global_session    http://${AUT}    max_retries=${0}

*** Test Cases ***
Redirect to Welcome Page
    [Documentation]    Accessing root url of application should redirect
    ...                to welcome page of notebook app
    ${response}=    Get Request    global_session    /
    Should Contain    ${response.text}    Main block

