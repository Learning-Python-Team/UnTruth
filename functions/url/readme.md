# url

Takes title from article, searches nouns and searches if subjects are currently talked about.

## Setup

1. `cd functions/url`
2. `virtualenv env`
3. `source env/bin/activate`
4. `pip install -r requirements.txt`

## Parameters
You can get an API key by visiting [google console](https://code.google.com/apis/console) and clicking "API Access". You will then need to switch on the custom search API on the "Services" tab.

Inside `config.py` file the following parameters are **necessary** 
- `api_key`
- `cse_id`

The following parameters are **customizable**:
- `url`
- `language`

***Do not change the value of other parameters***
