## Introduction
```
'jop_scraper.py' is a file in python to scrap data from 'https://techolution.app.param.ai/jobs/'

```
## Download

```
Download the file into your local system

Ensure that you work with python < 3.8
This project has been initially developed with python 3.6

```


Activate your Python virtual environment, and download the required libraries
```
source venv/bin/activate
export PYTHONPATH = '.'
pip install -r requirements.txt
```

## How to run app on local laptop

Follow the guide here to ensure you run correct main file
```
python job_scraper.py
```

Final output will be in the file 'jobs_result.csv'

## Approach towards problem
```buildoutcfg
1. Analysed the html of the website
2. Understood that the site dynamically loads the content from js scripts
3. Analysed the exact request with relevant data
4. Mocked the required request
5. Analysed the result from request
6. Extracted the required data
7. Processed the required data
8. Added Markdowns
9. Created requirements.txt file
10. Created readme.md file
```
