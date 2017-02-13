# Python & MongoDB

## pyenv 시작
* pyenv and pyenv-virtualenv install ref [link](https://dobest.io/how-to-set-python-dev-env/ "참고링크")

* python 2.7.12 사용 (pyenv virtualenv 2.7.12 적용하기)
```
$ pyenv virtualenv 2.7.12 py_mongo
$ virtualenv versions
$ pyenv shell py_mongo
$ pyenv versions
$ pyenv version
py_mongo (set by PYENV_VERSION environment variable)
```

## pymongo install

```
$ python -m pip install pymongo
$ python -c "import pymongo; print(pymongo.version); print(pymongo.has_c())"
```

### collection 이름들 가져오기
```
$ vim test.py ### source 참조
$ python test.py
```
