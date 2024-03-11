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

https://github.com/howarudo/rakugo/assets/125206676/9bfc0615-44dc-4fb2-a1ad-2b6370996690

### Before
  1. おようで、実はな、拙者は越中の守様の側用人で大槻刑部という者である。
  2. 今、殿が御駕籠でご通行になってあれにかかっている竹の水仙大層御意に召した。
  3. 値はいかほどだ？
  4. 何です?

https://github.com/howarudo/rakugo/assets/125206676/84767ea0-82ad-4e0d-908b-e63bc1756a60


### After
  1. おようで、実は、わたしは越中のお殿様のお世話をしているおおつきぎょうぶという人だ。
  2. いま、おとのがくるまで通りかかって、あの竹の水仙にとても興味を持った。
  3. あたいはいくらですか？
  4. なんです？

https://github.com/howarudo/rakugo/assets/125206676/06b07c67-5276-4b32-9a11-18e14af899c4


