# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

module load nvhpc
module load cuda

PATH=$PATH:./
