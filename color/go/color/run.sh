#!/bin/zsh

# you should only need to do this once when creating a package
function init
{
  go mod init
}

function test
{
  go test ./...
}

function run
{
  go run main.go
}

function build
{
  go build
}

function usage
{
  format="%4s %-7s : %-40s - %s\n"
  printf "${format}" "Flag" "Options" "Description" "Value"
  printf "${format}" "----" "-------" "-----------------------------" "--------"
  printf "${format}" "-b" "" "Build application" ""
  printf "${format}" "-h" "" "this help message" ""
  printf "${format}" "-i" "" "initialize the module, just once" ""
  printf "${format}" "-r" "" "Run application" ""
  printf "${format}" "-t" "" "Test code" ""
}

while getopts bhirt opt ; do
    case "${opt}" in
        #A) account=${OPTARG} ; remote_path=/home/$account/Shared ;;
        
        b) build ;;
        i) usage ;;
        i) init ;;
        r) run ;;
        t) test ;;
        *) usage ; exit 1 ;;
    esac
done
