# My-First-Repo-RPS-Game-
 

## Prerequisites

Install python version 3.x (for example using Anaconda).

## Setup

some instructions here

1. Clone the repo from GitHub
2. Navigate to the local repo from the command line
3. Make sure the Anaconda base environment is active.


Create a virtual environment (establishes environment needed to run including required installments):

```sh
conda create -n My-First-Repo-RPS-Game-env python=3.11
```

Activate the virtual environment:

```sh
conda activate My-First-Repo-RPS-Game-env 
```

Install package dependencies within the virtual environment:

```sh
pip install -r requirements.txt
```





## Usage

some commands here to run our file(s)

### Command Line App

    Run the example script:

    ```sh
    python app/my_script.py

    # alternatively:
    python -m app.my_script
    ```


    Run the example script:

    ```sh
    python app/rps.py

    # alternatively:
    python -m app.rps



    ## Testing

    to run tests:

    ```sh

    pytest





### Web App


Run the web app (then view in the browser at http://localhost:5000/):

```sh
# if we have the FLASK_APP=web_app env var in the ".env" file:
flask run

# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
`