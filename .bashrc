#
# ~/.bashrc
#
# If not running interactively, don't do anything
[[ $- != *i* ]] && return
source ~/.sudo.plugins.sh
PS1='[\u@\h \W]\$ '

#Pyactive
function pipenv_activate(){
	export R_env=$(pipenv --venv)
	. "$R_env/bin/activate"

}
#Alias
#Do not use ccat in nixos
#alias cat='ccat -G Plaintext="darkred" -G Keyword="blue" -G String="darkyellow" -G Punctuation="darkred" -G Comment="white" '
if [ -x "$(command -v exa)" ]; then
    alias ls='exa --group-directories-first'
    alias li="exa --long --all --group --icons"
    alias trex="exa -T --icons"
fi
if [ -x "$(command -v tree)" ]; then
    alias tree='tree -C'
fi
if [ -x "$(command -v bat)" ]; then
    alias bat='bat --theme gruvbox-dark'
    alias cat='bat -p --plain'
fi
if [ -x "$(command -v python)" ]; then
	alias py="python"
    alias peactivate=pipenv_activate
    alias activate="source ./*/bin/activate"
fi
alias grep='grep --color=auto'
alias bash-edit="vim ~/.bashrc"
alias plug='nvim ~/.config/nvim/lua/plugin.lua'
alias lg='$(which ls) --color=auto --group-directories-first -sort'
#SHELL
. ~/.git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1
export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[33m\]$(__git_ps1 "(%s)")\[\033[37m\]\$\[\033[00m\]\n '
#futuros
#export PS1='\[\e[0\][\[\e[0;48;5;36m\]\u\[\e[0;48;5;36m\]@\[\e[0;48;5;36m\]\h \[\e[0m\]\W\[\e[0\]]\[\e[0;97;48;5;88m\]\$ \[\e[0m\]$(git branch 2>/dev/null | grep '"'"'^*'"'"' | colrm 1 2)\[\e[0m\]' 
#Welcome in Terminal
RED='\033[0;31m'
END='\033[0m'
echo -e ${RED}
echo """
██╗  ██╗██████╗  ██████╗ ██╗   ██╗██╗   ██╗██╗  ██╗██████╗ ███████╗██╗   ██╗
██║ ██╔╝██╔══██╗██╔═══██╗██║   ██║██║   ██║╚██╗██╔╝██╔══██╗██╔════╝██║   ██║
█████╔╝ ██████╔╝██║   ██║██║   ██║██║   ██║ ╚███╔╝ ██║  ██║█████╗  ██║   ██║
██╔═██╗ ██╔══██╗██║   ██║╚██╗ ██╔╝██║   ██║ ██╔██╗ ██║  ██║██╔══╝  ╚██╗ ██╔╝
██║  ██╗██║  ██║╚██████╔╝ ╚████╔╝ ╚██████╔╝██╔╝ ██╗██████╔╝███████╗ ╚████╔╝ 
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═══╝   ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝  ╚═══╝                                                                        
"""
echo -e ${END}
function sudo {
printf '\x1b]11;rgb:4040/2020/3030\x1b\\'
$(which sudo) "$@"
printf '\x1b]111;\x1b\\'
}
export -f sudo
#Starship
if [[ -x "$(command -v starship)" ]]; then
    eval "$(starship init bash)"
fi
