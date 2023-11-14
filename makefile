ensure:
	pipenv sync --dev
	pipenv clean

fmt:
	@isort .
	@black -l 120 .

lint:
	isort --check .
	black -l 120 --check .

install:
	python main.py install

uninstall:
	python main.py uninstall

clean_gen_file:
	python main.py clean_gen_file


