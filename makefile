ensure:
	pipenv sync --dev
	pipenv clean

fmt:
	@isort .
	@black -l 120 .

lint:
	isort --check .
	black -l 120 --check .


