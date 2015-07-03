#!/bin/bash
set -e

### crontab -e
# */5 * * * * /usr/share/portabilidade/config/email.sh
###

# user/group to run as
USER=root
GROUP=root

source /usr/share/portabilidade/bin/activate
cd /usr/share/portabilidade
python manage.py send_queued_mail --processes=1 >> cron_mail.log 2>&1
python manage.py cleanup_mail --days=30 >> cron_mail.log 2>&1