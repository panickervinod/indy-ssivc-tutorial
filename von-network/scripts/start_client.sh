#!/bin/bash

set -e

if [ ! -z "$KUBERNETES" ]; then
  su -c "generate_indy_pool_transactions --nodes 4 --clients 0 --ips \"${NODE_1_SERVICE_HOST},${NODE_2_SERVICE_HOST},${NODE_3_SERVICE_HOST},${NODE_4_SERVICE_HOST}\"" indy
else
  if [ ! -z "$IPS" ]; then
    echo von_generate_transactions -s "$IPS" -n "$NODE_NUM"
    su -c "von_generate_transactions -s \"$IPS\" -n \"$NODE_NUM\"" indy
  elif [ ! -z "$IP" ]; then
    echo von_generate_transactions -i "$IP" -n "$NODE_NUM"
    su -c "von_generate_transactions -i \""$IP\"" -n \"$NODE_NUM\"" indy
  else
    echo von_generate_transactions -n "$NODE_NUM"
    su -c "von_generate_transactions -n \"$NODE_NUM\"" indy
  fi

  su -c "indy" indy
fi
