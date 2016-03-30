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

+ Run `main.py` to generate list of exams

  ```
  usage: ./main.py [-h] [-s SEMESTER] -c COURSES [COURSES ...] -ln LAST_NAME [-f {raw,table,json}]

  arguments:
    -h, --help                show this help message and exit
    -s SEMESTER               semester / year to get schedule for (format: SYY) [default: W16]
    -c COURSES [COURSES ...]  courses (separated by a space; use dash for lecture code, eg. csc148-l0101 csc165)
    -ln LAST_NAME             last name
    -f {raw,table,json}       output format (one of <table|json|raw>) [default: raw]

  example: 
    ./main.py -s W16 -c csc165 csc148 eco100-l0401 mat137 psy100-l0101 -ln madan -f json
    # see ./sample for sample json/table output
  ```

#### Contribute
Feel free to open an [issue](https://github.com/kshvmdn/uoft-exams/issues) or make a [pull request](https://github.com/kshvmdn/uoft-exams/pulls). All contributions are welcome.
