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

<figure class="video_container">
  <iframe src="results/v1/rakugo_v1.mp4" frameborder="0" allowfullscreen="true">
</iframe>
</figure>

### After
<figure class="video_container">
  <iframe src="results/v1/rakugo_v1_final.mp4" frameborder="0" allowfullscreen="true">
</iframe>
</figure>
