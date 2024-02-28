install_package:
	@pip uninstall -y rakugo || :
	@pip install -e .

setup_local:
	test -f .local.env || cp .local.env.copy .local.env
	mkdir -p local_data

run:
	@streamlit run streamlit/streamlit.py
