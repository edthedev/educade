.PHONY: test deploy

test:
	cd peanut;python player.py

deploy:
	./deploy.ps1
