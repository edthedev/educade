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

Confirm this by running `python -V`.

```sh
$ python -V
Python 3.11.0
```

> Tip: If the result is not Python 3.11.0, double check the `PyEnv` was added to your profile correctly.

## Create a virtual environment for Ansible


It's a good idea to make sure `pip` is up to date.

```sh
pip install --upgrade pip
```

Now create a Virtual Environment for Ansible.
This will take a couple of minutes.

```sh
mkdir ~/venvs
cd ~/venvs
python -m venv ansible
```

Now activate the virtual environment and install Ansible.

source ~/venvs/ansible/bin/activate
pip install ansible
```

When creating a new shell to use thse commands in the future, activate the Ansible virtual environment first.

```sh
source ~/venvs/ansible/bin/activate
```