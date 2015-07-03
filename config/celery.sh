#!/bin/bash
set -e

# user/group to run as
USER=root
GROUP=root

source /usr/share/portabilidade/bin/activate
cd /usr/share/portabilidade
export C_FORCE_ROOT="true"
celery -A portabilidade worker -B -l INFO &