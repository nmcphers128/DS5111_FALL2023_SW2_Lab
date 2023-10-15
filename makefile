default:
	@cat makefile

env: 	env/touchfile

env/touchfile: requirements.txt
	test -d env || python3 -m venv env
	. env/bin/activate; pip install -Ur requirements.txt
	touch env/touchfile

run: env
	@. env/bin/activate; python bin/clockdeco_param.py

.PHONY: tests run lint

tests:
	pytest -vv tests

lint: env
	pylint bin/perceptron.py 


clean:
	@echo "Removing files ...."
	rm -rf env





