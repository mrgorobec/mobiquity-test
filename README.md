# Rest API Test Assignment
[![CircleCI](https://circleci.com/gh/mrgorobec/mobiquity-test.svg?style=svg)](https://circleci.com/gh/mrgorobec/mobiquity-test)



For the Rest API  [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

    
## Tech


- Python 3
- pytest
- requests
- CircleCI


## How to run locally


Install git:
```brew install git```

Install python

```brew install python@3.7```

Clone project 

```git@github.com:mrgorobec/mobiquity-test-assignment.git```

Open Project
```cd ExchangerateTest```

Install and activate virtualenv
```sudo pip3 install virtualenv
virtualenv testenv
source testenv/bin/activate
```

Install requirments
```
pip install -r requirements.txt
```

Run tests:
```
py.test -v tests/ --host=prod
```
and host is prod/staging environment


## Tests connected to the CicrcleCI and could be running there:  [CicrcleCI](https://app.circleci.com/pipelines/github/mrgorobec/mobiquity-test)


