# Conntributing

## Set up PyEnv

```sh
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

Add `~/.pyenv/bin/` to your PATH.

```sh
mkdir -p ~/.local/bin
ln -s ~/.pyenv/bin ~/.local/bin/pyenv
```

Confirm this worked with `which pyenv`. You may need to restart your shell first.

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