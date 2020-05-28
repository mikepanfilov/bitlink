# Bitly url shorterer

This script can receive two types of links:

- long weblink to shorten
- short bit.ly link to get a number of clicks on it

## How to install

It is necessary to generate a token in the service bitly.com and put in an environment variable.

- [here you can read how to get token](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-)

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

It is recommended to use [virtual environment](https://docs.python.org/3/library/venv.html)

To run the script, you need to run the following line in the terminal:

```bash
python main.py 'https://youlink.com'
```

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
