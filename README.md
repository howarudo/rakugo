# Rakugo

## Setup
1. pyenv

Install `pyenv`. Check [documentation](https://github.com/pyenv/pyenv)

2. Make new pyenv environment and then set it as a local env
```
pyenv virtualenv <PYTHON_VERSION> rakugo
pyenv local rakugo
```

3. Install packages
```
make install_package
```

4. Create local files and folders
```
make setup_local
```

## Demo Showcase
- We have completed a rough model for transformation.

### Before

![Rakugo original clip](results/v1/rakugo_v1.mp4)

### After
![Rakugo after editting clip](results/v1/rakugo_v1_final.mp4)
