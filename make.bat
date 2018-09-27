@ECHO OFF



IF "%1"=="" (
    python gather.py -f config.ini
    GOTO :end
)



IF "%1"=="init" (
    python gather.py -f config.ini --init
    GOTO :end
)



:end
