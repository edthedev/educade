include .env

venv:
	python -m venv venv

setup: venv
	./venv/bin/python -m pip install -r requirements.txt

shell:
	source ./venv/bin/activate

new:
	./venv/bin/ansible-playbook ansible/new.yml --ask-become-pass