#!/bin/bash

python manage.py setting_info 2> $(date +'%Y-%m-%d').dat 1> /dev/null