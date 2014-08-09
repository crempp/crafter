#!/bin/bash

echo "Starting server mc-64..."
screen -dmS mc-64 bash
sleep 1
screen -S mc-64 -p 0 -X stuff "/srv/minecraft.64/start.sh
"
sleep 1

echo "Starting server mc-65..."
screen -dmS mc-65 bash
sleep 1
screen -S mc-65 -p 0 -X stuff "/srv/minecraft.65/start.sh
"
sleep 1

echo "Starting server mc-66..."
screen -dmS mc-66 bash
sleep 1
screen -S mc-66 -p 0 -X stuff "/srv/minecraft.66/start.sh
"
sleep 1

echo "Starting server mc-67..."
screen -dmS mc-67 bash
sleep 1
screen -S mc-67 -p 0 -X stuff "/srv/minecraft.67/start.sh
"
sleep 1

echo "Starting server mc-68..."
screen -dmS mc-68 bash
sleep 1
screen -S mc-68 -p 0 -X stuff "/srv/minecraft.68/start.sh
"
sleep 1

echo "Starting server mc-69..."
screen -dmS mc-69 bash
sleep 1
screen -S mc-69 -p 0 -X stuff "/srv/minecraft.69/start.sh
"
