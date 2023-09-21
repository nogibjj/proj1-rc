install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	py.test --nbval project1/*.ipynb
	python -m pytest -vv --cov=project1 project1/*.py

format:	
	nbqa black  \project1/*.ipynb &&\
		black \project1/*.py

lint:
	ruff check \project1/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy

generate_and_push:
	# Create the markdown file (assuming it's generated from the plot)
	python project1/main.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add scatter_mpg.png fitted_mpg.png scatter_acc.png fitted_acc.png desc_stats.md; \
		git commit -m "Add generated plot and report"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi
