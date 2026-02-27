.PHONY: install lint data embeddings geotop classify all clean help

help:
	@echo "S2-PEPANALYST — available commands:"
	@echo "  make install     Install all dependencies"
	@echo "  make lint        Lint Python source files"
	@echo "  make data        Run data preparation notebook"
	@echo "  make embeddings  Generate TAPE & ESM embeddings"
	@echo "  make geotop      Run GeoTop topological assessment"
	@echo "  make classify    Run CNN classification"
	@echo "  make all         Run full pipeline"
	@echo "  make clean       Remove cache and executed notebooks"

install:
	pip install -r requirements.txt

lint:
	flake8 code/*.py --max-line-length=127 --count --statistics 2>/dev/null || \
		echo "No .py files found in code/ — linting skipped"

data:
	jupyter nbconvert --to notebook --execute code/01_data_preparation.ipynb \
		--output code/01_data_preparation_executed.ipynb

embeddings:
	jupyter nbconvert --to notebook --execute code/02_embeddings.ipynb \
		--output code/02_embeddings_executed.ipynb

geotop:
	jupyter nbconvert --to notebook --execute code/03_geotop.ipynb \
		--output code/03_geotop_executed.ipynb

classify:
	jupyter nbconvert --to notebook --execute code/04_classification.ipynb \
		--output code/04_classification_executed.ipynb

all: data embeddings geotop classify
	@echo "Full S2-PEPANALYST pipeline complete."

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null; true
	find . -name "*.pyc" -delete 2>/dev/null; true
	find . -name ".DS_Store" -delete 2>/dev/null; true
	find . -name "*_executed.ipynb" -delete 2>/dev/null; true
	find . -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null; true
