#!zsh
# syntactic sugar
function jpcurl {
    curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST -d $2 $1
}
jpcurl http://localhost:31337/alphaville/reflect "{\"text\":\"The reign of Spain mainly affected the plains.\"}"
