# SINFO

## Requirements

- [Python3.6](https://www.python.org/downloads/release/python-368/) + [Node.js](https://nodejs.org/en/) + [Yarn](https://yarnpkg.com/en/docs/install)

## Setup

- Clone the repo
- `cd sinfo`
- Open 2 terminal tabs

**1.** Frontend:

- `cd client` to move into the client directory
- `yarn` to install the dependencies
- `yarn start` to launch the development server
- wait for the web page to launch

**2.** Backend (from root):

- If you do not have `pip` for python already installed, install it following this [link](https://pip.pypa.io/en/stable/installing/). Then, install virtualenv as `pip3 install virtualenv`

- `python3 -m venv venv` for a virtual environment within the directory
- `source venv/bin/activate`
- `pip install -r requirements.txt` to install the required packages
- `python3 app.py` to launch the backend server

**3.** Data Science (from root):

- Steps 1, 2, and 3 of the Backend part should have been done previously.
- `cd ds` to move into the data science directory
- `jupyter notebook` to launch the notebook
