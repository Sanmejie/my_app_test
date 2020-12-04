#!/bin/bash
#set -x

NUM=1
TIMER=43200
DEVICES=`adb devices | grep "\<device\>" | awk '{print $1}'`
START_TIME=`date +%s`
END_TIME=$(($START_TIME+$TIMER))

for device in ${DEVICES}
do
    adb -s $device logcat -c
    adb -s $device logcat -v time > $device.log &
done

for(( ; ; ))
do
    for device in ${DEVICES}
            do
                echo "模拟语音指令-打开咪咕快游"
                adb -s $device shell am broadcast -a com.baidu.duer.query -e q 打开同桌一百
                sleep 15
                echo "开屏页-点击进入"
                adb -s $device shell input tap 552.6 602.6 
                sleep 15
                echo "最近玩过的游戏，点击开始游戏"
                adb -s $device shell input tap 239.6 470.6 
                sleep 35
                echo "模拟语音指令-退出"
                adb -s $device shell am broadcast -a com.baidu.duer.query -e q 退出 
                sleep 8
            
            done
done

