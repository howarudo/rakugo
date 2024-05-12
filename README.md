# RakuRakuGo

We won **Business Award** for the **Softbank x UTokyo UGIP Data & AI Hackathon**! 

[LINK](https://www.softbank.jp/sbnews/entry/20240418_01)

## System

<img width="479" alt="rakurakugo" src="https://github.com/howarudo/rakugo/assets/125206676/2af00643-80be-46c3-8c0c-b30a84597b21">


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

[UI Showcase Link If Above Fails](https://drive.google.com/file/d/17dy5GVw1CVPWwV1DiJc90YA54MPSvs26/view?usp=sharing)
### Before
  1. おようで、実はな、拙者は越中の守様の側用人で大槻刑部という者である。
  2. 今、殿が御駕籠でご通行になってあれにかかっている竹の水仙大層御意に召した。
  3. 値はいかほどだ？
  4. 何です?

https://github.com/howarudo/rakugo/assets/125206676/84767ea0-82ad-4e0d-908b-e63bc1756a60

[Before Video Link If Above Fails](https://drive.google.com/file/d/1i_2EBc4YcFihXoWBPU8BWlX8DlKxWMJl/view?usp=sharing)

### After
  1. おようで、実は、わたしは越中のお殿様のお世話をしている おおつきぎょうぶ という人だ。
  2. 今、おとの が車で通りかかって、あの竹の水仙にとても興味を持った。
  4. あたい はいくらですか？
  5. なんです？

https://github.com/howarudo/rakugo/assets/125206676/2c235d5e-c5f6-4364-968e-93774bfb7eee

[Afer Video Link If Above Fails](https://drive.google.com/file/d/1GVf-6yaQzZYyH8XossaEWWSM5jwNx_vo/view?usp=sharing)
