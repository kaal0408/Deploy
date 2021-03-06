#!/bin/bash


_get_repolink () {
    local regex
    regex='(https?)://gitlab.com/.+/.+'
    if [[ $ASTRO_REPO == "ASTRObot" ]]
    then
        echo "aHR0cHM6Ly9naXRsYWIuY29tL2xvdmVyYm95WEQvQXN0cm9VQi8tL2FyY2hpdmUvbWFpbi9Bc3Ryb1VCLW1haW4uemlw" | base64 -d
    elif [[ $ASTRO_REPO == "ASTROBOT" ]]
    then
        echo "aHR0cHM6Ly9naXRsYWIuY29tL2xvdmVyYm95WEQvQXN0cm9VQi8tL2FyY2hpdmUvbWFpbi9Bc3Ryb1VCLW1haW4uemlw" | base64 -d
    elif [[ $ASTRO_REPO =~ $regex ]]
    then
        if [[ $ASTRO_REPO_BRANCH ]]
        then
            echo "${ASTRO_REPO}/archive/${ASTRO_REPO_BRANCH}.zip"
        else
            echo "${ASTRO_REPO}/archive/main.zip"
        fi
    else
        echo "aHR0cHM6Ly9naXRsYWIuY29tL2xvdmVyYm95WEQvQXN0cm9VQi8tL2FyY2hpdmUvbWFpbi9Bc3Ryb1VCLW1haW4uemlw" | base64 -d
    fi
}


_set_bot () {
    local zippath
    zippath="ASTRObot.zip"
    echo "Getting Codes.....!"
    wget -q $(_get_repolink) -O "$zippath"
    echo "  Unpacking Data ..."
    ASTROPATH=$(zipinfo -1 "$zippath" | grep -v "/.");
    unzip -qq "$zippath"
    echo "Done"
    echo "  Cleaning ..."
    rm -rf "$zippath"
    sleep 5
    cd $ASTROPATH
    echo "π­β’Starting Service of Astroβ’π°οΈπΈ"
    echo """
    Β© A S T R O Β©
βββββ¦ββββ¦βββββ¦ββββ¦ββββ
ββββββββββββββββββββββ
βββββββββ¬βββββ£ββββββββ
βββββ βββββββββββββ£ββββ
ββββββββββββββββββ£ββββ
βββββ©βββββββββββββ©ββββ
    """
    
    
    python3 -m astro
}

_set_bot
