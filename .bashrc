#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
source ~/.sudo.plugins.sh
#Welcome
RED='\033[0;31m'
END='\033[0m'
echo -e ${RED}
echo """
██╗  ██╗ █████╗ ██████╗ ██╗███╗   ███╗██████╗ ███████╗██╗   ██╗ █████╗  ██████╗ 
██║ ██╔╝██╔══██╗██╔══██╗██║████╗ ████║██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝ 
█████╔╝ ███████║██████╔╝██║██╔████╔██║██║  ██║█████╗  ██║   ██║╚██████║███████╗ 
██╔═██╗ ██╔══██║██╔══██╗██║██║╚██╔╝██║██║  ██║██╔══╝  ╚██╗ ██╔╝ ╚═══██║██╔═══██╗
██║  ██╗██║  ██║██║  ██║██║██║ ╚═╝ ██║██████╔╝███████╗ ╚████╔╝  █████╔╝╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═════╝ ╚══════╝  ╚═══╝   ╚════╝  ╚═════╝
"""
echo -e ${END}

#Alias
alias grep='grep --color=auto'
alias tree='tree -C'
alias bash-edit="vim ~/.bashrc"
#alias zsh-edit="vim ~/.zshrc"
alias plug='nvim ~/.config/nvim/lua/plugin.lua'
alias bat='bat --theme gruvbox-dark'
alias activate="source ./*/bin/activate"
if [ -x "$(command -v ccat)" ]; then #install ccat
	alias cat='ccat -G Plaintext="darkred" -G Keyword="blue" -G String="darkyellow" -G Punctuation="darkred" -G Comment="white" '
fi
function pipenv_activate(){
	export R_env=$(pipenv --venv)
	. "$R_env/bin/activate"

}
alias peactivate=pipenv_activate
if [ -x "$(command -v python)" ]; then
	alias py="python"
fi
if [ -x "$(command -v exa)" ]; then # install exa
	alias ls='exa --group-directories-first'
  	alias li="exa --long --all --group --icons"
  	alias la="exa --long --all --group"
	alias tree="exa -T --icons"
fi
if [ -x "$(command -v grep)" ];then
	alias grep="grep --color=auto"
fi

function sudo {
printf '\x1b]11;rgb:4040/2020/3030\x1b\\'
/usr/bin/sudo "$@"
printf '\x1b]111;\x1b\\'
}

export -f sudo

