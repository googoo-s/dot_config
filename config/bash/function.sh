
function galg {
    echo "git config --get-regexp alias | grep $1"
    git config --get-regexp alias | grep $1
}


function tree {
    pwsh -Command tree $1
}

function virc {
    vim ~/dot_config/
}

function nvrc {
    nvim ~/dot_config/
}

function corc {
    code ~/dot_config/
}

function src {
    source ~/.bashrc
}

function psp {
    netstat -ano | grep $1
}

function kill {
    pwsh -Command kill $1 -F
}

function gcl {
    golangci-lint run ./...
}

function cap {
    echo 'export https_proxy="http://127.0.0.1:7890"'
    echo 'export http_proxy="http://127.0.0.1:7890"'
    echo 'export all_proxy="http://127.0.0.1:7890"'
    export https_proxy="http://127.0.0.1:7890"
    export http_proxy="http://127.0.0.1:7890"
    export all_proxy="socket5://127.0.0.1:7890"
}