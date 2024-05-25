# Don't change
# SRC_DIR := app

test: venv  ## 🎯 Unit tests for Flask app
	. .venv/bin/activate \
	&& pytest -v 

# test-report: venv  ## 🎯 Unit tests for Flask app (with report output)
# 	. $(SRC_DIR)/.venv/bin/activate \
# 	&& pytest -v --junitxml=test-results.xml

# test-api: .EXPORT_ALL_VARIABLES  ## 🚦 Run integration API tests, server must be running 
# 	cd tests \
# 	&& npm install newman \
# 	&& ./node_modules/.bin/newman run ./postman_collection.json --env-var apphost=$(TEST_HOST)

# clean:  ## 🧹 Clean up project
	rm -rf .venv
# 	rm -rf tests/node_modules
# 	rm -rf tests/package*
# 	rm -rf test-results.xml
# 	rm -rf app/__pycache__
# 	rm -rf app/tests/__pycache__
# 	rm -rf .pytest_cache
# 	rm -rf .pytest_cache

# ============================================================================

venv: .venv/touchfile

.venv/touchfile: requirements.txt
	python3 -m venv .venv
	. .venv/bin/activate; pip install -Ur requirements.txt
	touch .venv/touchfile
