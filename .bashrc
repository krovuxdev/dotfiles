#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
export PATH="$PATH:/home/karimdev/.development/flutter/bin"
export CHROME_EXECUTABLE=/usr/bin/google-chrome-stable
export PATH="$PATH:/home/karimdev/.node.js/bin"

