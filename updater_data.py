def get_variables(commands):
    Operations = {
                "UPDATER_VERSION": "display_product_version.sh \r\n",
                "UPDATER_STATUS": "config_status.sh \r\n",
                "reset": "uconfig -r",
                "updaterReboot":"reboot"
                 }
    # legacy2Ingelwood is used to upgrade from GG/Halifax to Ingelwood
    legacy2Ingelwood = {
                "1": "cd /",
                 "2": "killall updater-start 2> /dev/null",
                 "3": "killall updater 2> /dev/null",
                 "4": "nv set UPGRADED_FROM PULSE",
                 "5": "umount /flash",
                 "6": "fwupdate -e",
                 "7": "echo ”PR300307” > /BUILD",
                 "8": "echo \"PR300307 version-3.0.1-platform sa@sestvld323 2019-11-04 10:46\" > BUILD",
                 "9": "fwupdate -fd http://rocketfw.s3-eu-west-1.amazonaws.com/PR300307_inglewood_5.0.8-updater_3.0.1-platform.zip",
                 "10": "reboot"
                }
    #Ing507toIng508 used to upgrade from 5.0.7
    Ing507toIng508 = {"BASE_URL": "https://staging-yale.accentra.assaabloy.com/",
                 "username": "xyz",
                 "password": "put stage pass"}

    if commands == 'Operation':
        return Operations
    elif commands == 'GG':
        return legacy2Ingelwood
    elif commands == 'upgrade507_508':
        return Ing507toIng508
