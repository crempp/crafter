#!/bin/bash

MC_64="On"   # BEI Land 
MC_65="Off"  # Land of the Unnamed Wise Turtles
MC_66="Off"  # Empire of the Dying Black Kite
MC_67="Off"  # Kingdom of the Sleepy Castle
MC_68="Off"  # Great Blue Shadow Realm
MC_69="Off"  # Glimmering Mercy Land

if [[ $MC_64 = "On" ]]
  then
    echo "Starting server mc-64..."
    screen -dmS mc-64 bash
    sleep 1
    screen -S mc-64 -p 0 -X stuff "/srv/minecraft.64/start.sh
    "
    sleep 1
fi

if [[ $MC_66 = "On" ]]
  then
    echo "Starting server mc-65..."
    screen -dmS mc-65 bash
    sleep 1
    screen -S mc-65 -p 0 -X stuff "/srv/minecraft.65/start.sh
    "
    sleep 1
fi

if [[ $MC_66 = "On" ]]
  then
    echo "Starting server mc-66..."
    screen -dmS mc-66 bash
    sleep 1
    screen -S mc-66 -p 0 -X stuff "/srv/minecraft.66/start.sh
    "
    sleep 1
fi

if [[ $MC_67 = "On" ]]
  then
    echo "Starting server mc-67..."
    screen -dmS mc-67 bash
    sleep 1
    screen -S mc-67 -p 0 -X stuff "/srv/minecraft.67/start.sh
    "
    sleep 1
fi

if [[ $MC_68 = "On" ]]
  then
    echo "Starting server mc-68..."
    screen -dmS mc-68 bash
    sleep 1
    screen -S mc-68 -p 0 -X stuff "/srv/minecraft.68/start.sh
    "
    sleep 1
fi

if [[ $MC_69 = "On" ]]
  then
    echo "Starting server mc-69..."
    screen -dmS mc-69 bash
    sleep 1
    screen -S mc-69 -p 0 -X stuff "/srv/minecraft.69/start.sh
    "
fi

