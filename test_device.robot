*** Settings ***
Documentation    Test case for adriuno device. How to verify code for adurino
Library         ./SerialCommunication.py
Library       ./SerialCommunication_data.py
#Resource         ./test_input.robot

*** Test Cases ***
Verify Device Version
    ${device_response}     Serial Communication      ${device_VERSION}
    Log to Console      ${device_response}

Verify Device STATUS
     ${device_response}     Serial Communication      ${device_STATUS}
     Log to Console      ${updater_response}

Verify Device RESET is Working Fine
    ${device_response}     Serial Communication       ${RESET}
    Log to Console      ${updater_response}

Verify Updater REBOOT is Working Fine
    ${device_response}     Serial Communication       ${RESET}
    Log to Console      ${device_response}
