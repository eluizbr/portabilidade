#!/bin/bash
set -e
LOGFILE=/var/log/cdrport/gunicorn_port.log
LOGDIR=$(dirname $LOGFILE)

bash /usr/share/portabilidade/config/celery.sh

# The number of workers is number of worker processes that will serve requests.
# You can set it as low as 1 if you’re on a small VPS.
# A popular formula is 1 + 2 * number_of_cpus on the machine (the logic being,
# half of the processess will be waiting for I/O, such as database).
NUM_WORKERS=1
ADDRESS=0.0.0.0:7000

# user/group to run as
USER=root
GROUP=root

source /usr/share/portabilidade/bin/activate
cd /usr/share/portabilidade

test -d $LOGDIR || mkdir -p $LOGDIR

#Execute unicorn
exec gunicorn portabilidade.wsgi:application -b $ADDRESS -w $NUM_WORKERS --timeout=300 \
    --user=$USER --group=$GROUP --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE -D