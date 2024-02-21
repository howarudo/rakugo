setup:
	cp .local.env.copy .local.env

install_package:
	@pip uninstall -y rakugo || :
	@pip install -e .
