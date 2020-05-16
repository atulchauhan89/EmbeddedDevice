*** Settings ***
Documentation    Suite description
Library         ./updater.py
Library       ./updater_data.py
#Resource         ./test_input.robot

*** Test Cases ***
Verify Updater Version
    ${updater_response}     Updater Communication      ${UPDATER_VERSION}
    Log to Console      ${updater_response}

Verify UPDATER STATUS
     ${updater_response}     Updater Communication      ${UPDATER_STATUS}
     Log to Console      ${updater_response}

Verify Updater RESET is Working Fine
    ${updater_response}     Updater Communication       ${RESET}
    Log to Console      ${updater_response}

Verify Updater REBOOT is Working Fine
    ${updater_response}     Updater Communication       ${RESET}
    Log to Console      ${updater_response}
