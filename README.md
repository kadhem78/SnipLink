## Running this project localy

To get this project up and running clone this repository and you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env or python3 -m venv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```
Activate Virtual Enviroment Windows:

```
.\venv\scripts\activate
```

Then install the project dependencies with

```
pip install -r requirements.txt

```
Now you can run the project with this command

```
flask --app app run
```


