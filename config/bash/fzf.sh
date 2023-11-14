export FZF_COMPLETION_TRIGGER='``'
export FZF_PREVIEW_CMD='[[ $(file --mime {}) =~ binary ]] && echo {} is a binary file || (ccat --color=always {} || highlight -O ansi -l {} || cat {}) 2> /dev/null | head -500'


export FZF_DEFAULT_OPTS='--height 90% --layout=reverse --border'