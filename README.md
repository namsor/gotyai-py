# gotyai-client
Gotyai API : the Spartan explainable AI 

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

First, install the Gotyai client library with 

```sh
pip install git+https://github.com/namsor/gotyai-client-py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/namsor/gotyai-client-py.git`)

Then install the requirements,
```sh
pip install -r requirements.txt
```

Then import the package:
```python
import gotyai_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gotyai_client
```

## Getting Started
Check the server URL and the API Key in gotyai/model.py, then run the demo:
```sh
python main.py
```

## Author

contact@namsor.com


