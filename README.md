## rx-fractal

This is a python3/tk written software to generate a fractal between 3 points given random numbers.

Features:

- 500x500 canvas
- Generates 10000 max points for each iteration
- Brazillian Portuguese (pt_BR) interface

Binaries:

- Binaries are provided for Windows 10 - 64bits

Explanation:

- This is better used after watching this video:

[![Numberphile Video](https://img.youtube.com/vi/kbKtFN71Lfs/0.jpg)](https://www.youtube.com/watch?v=kbKtFN71Lfs)

## Screenshot

![Demo on Linux](images/2.gif)
![Main Screen - Windows](images/1.png)

# Install

Check if you've got a least python3.7 installed in your system and pip3.

```
$ python3 --version
...
$ pip3 --version
```

Clone this repo and `cd` into its folder.

Create a virtual environment and source into it:

```
$ python3 -m venv venv
$ source env/bin/activate
```

Install the requirements:

```
$ pip3 install -r requirements.txt
```

Run the app:

```
$ python3 rx-fractal.py
```

Some systems are a more "sensible" about Tk as a built in python package, in this case you might have to install it globally depending on your system. In macOS you might need:

```
$ brew install python-tk
```
