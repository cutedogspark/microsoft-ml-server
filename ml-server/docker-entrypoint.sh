#!/bin/bash
set -e

echo "ml-server(${MODE,,}) initial"
if [[ ${MODE,,}  = 'computenode' ]]
then
    echo "-- computenode initial"
    az mlserver admin node setup --computenode
    az mlserver admin node list --computenode
fi

if [[ ${MODE,,}  = 'webnode' ]]
then
    echo "-- webnode initial"
    echo "---  config"
    python config_web_node.py
    echo "---  setup"
    az mlserver admin node setup --webnode --admin-password $PASSWORD --confirm-password $PASSWORD --uri $COMPUTENODE_URI
    echo "---  list webnode"
    az mlserver admin node list --webnode
fi
echo "ml-server(${MODE,,}) finish"
sleep infinity
