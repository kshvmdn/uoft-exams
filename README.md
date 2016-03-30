# U of T Exams
A scraper for semesterly exam timetables.

#### Setup / usage

+ Clone, install requirements

  ```
  git clone https://github.com/kshvmdn/uoft-exams.git && cd uoft-exams
  ```

  ```
  pip install -r requirements.txt
  ```

+ Run `main.py` to generate a list of exams (check ./sample for sample output)

  ```
  usage: main.py [-h] -c COURSES [COURSES ...] -ln LAST_NAME [-s SEMESTER]
               [-f {table,json}]

  arguments:
    -h, --help        show this help message and exit
    -s, --semester    semester (S), year (YY) to get schedule for (defaults to W16)
    -c, --courses     courses separated by space, dash for lecture code (eg csc148-l0101 csc165)
    -ln, --lname      last name
    -f, --format      optional output format (one of <table|json>)

  example: 
    ./main.py -s W16 -c csc165 csc148 eco100-l0401 mat137 -ln madan -f json
  ```

#### Contribute
Feel free to open an [issue](https://github.com/kshvmdn/uoft-exams/issues) or make a [pull request](https://github.com/kshvmdn/uoft-exams/pulls). All contributions are welcome.
