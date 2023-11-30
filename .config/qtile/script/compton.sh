#!/bin/bash

if pgrep -x "compton" > /dev/null
then
	killall compton
else
	compton -b --config $HOME/.config/qtile/conf/compton.conf
fi
