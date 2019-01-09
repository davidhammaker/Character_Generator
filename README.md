# Character Generator

A random character generator.

### Purposes

* _Quickly create unique, randomly generated characters for fantasy adventures._
* _Serve as a practice project for developing my skills with the Python language._

## Usage

The project is still in early development, but parts of the project are functional. You must have Python 3 to use the project. Clone this repository, then `cd` into the "character_generator" package directory.

To instantly generate a character, run the following command:

`$ python app.py`

* By default, evil characters may not be generated. If you would like to include evil characters in the random generation, you may enable evil character generation by passing `--evil-permitted` or `-ep`:
* `$ python app.py --evil-permitted`
* `$ python app.py -ep`

To generate a character in the REPL, start Python in the "character_generator" package directory, then run the following:

```
>>> from app import character_generator
>>> c = character_generator()
```

* By default, evil characters may not be generated. If you would like to include evil characters in the random generation, you may enable evil character generation by passing `evil_permitted=True`:
* `c = character_generator(evil_permitted=True)`

## The Future

I intend to develop the project into a Flask application that will allow users to create, store, and download generated characters. Ideally, users would have the option to select options like character race and alignment, and even level, or permit the application to generate fully-random characters. The end result would be a highly flexible application that would allow users to select the aspects of a character that are important, and leave the rest for the application to generate randomly.

## Copyright
© David J. Hammaker 2019
