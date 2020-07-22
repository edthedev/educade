.PHONY: test deploy

test:
	cd peanut;python3 player.py

deploy:
	./deploy.ps1
