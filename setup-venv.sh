# set -e stops execution if anything fails
# set -x echos the command that was run to stdout (well, to the console, not sure if it's stdout)
set -ex
virtualenv strategy-venv
# If the above command fails, run `pip3 install virtualenv`

. strategy-venv/bin/activate

pip3 install -r requirements.txt

# Undo set -x
set +x
