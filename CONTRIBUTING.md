# Conntributing

## Set up PyEnv

Setup PyEnv per instructions at [PyEnv README](https://github.com/pyenv/pyenv). 

> Tip: Since my Ansible computer is a Raspberry Pi, I use the `git clone` version for Linux.

Confirm this worked with `which pyenv`. You may need to restart your shell first.

## Install modern Python

Install a modern version of Python
```sh
pyenv install 3.11.0
pyenv global 3.11.0
```

## Create a virtual environment for Ansible

```sh
mkdir ~/venvs
cd ~/venvs
python -m venv ansible
source ~/venvs/ansible/bin/activate
pip install ansible
```

When creating a new shell to use thse commands in the future, activate the Ansible virtual environment first.

```sh
source ~/venvs/ansible/bin/activate
```