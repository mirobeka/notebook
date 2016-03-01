*** Settings ***
Library    RequestsLibrary
Documentation    Very basic test of REST API to determine if API responds
Suite Setup    Create Global Session
Suite Teardown    Delete All Sessions


*** Variables ***
${DISCOVERY_STRING}    You've discovered notebook api!

*** Keywords ***
Create Global Session
    Create Session   global_session    http://${AUT}    max_retries=${0}

*** Test Cases ***
API Discovery String
    [Documentation]    Tests if root API url responds with API discovery string
    ${response}=    Get Request    global_session    /api/v1/
    Should Be Equal    ${DISCOVERY_STRING}    ${response.text}

