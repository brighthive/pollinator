requirements:
	pipenv lock --requirements > requirements.txt

install: requirements
	pip install -e .

reinstall: requirements
	pip uninstall pollinator
	$(MAKE) install

uninstall:
	pip uninstall pollinator 

clean:
	find . -name \*.pyc -delete
	find . -name \__pycache__ -delete

.PHONY: requirements install reinstall uninstall clean 