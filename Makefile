.PHONY: test deploy

test:
	cd peanut;python player.py
	cd peanut;python field.py

deploy:
	./deploy.ps1
