# REDDprocessor
preprocessor for REDD created as part of thesis at TUM.

##Steps to run:

```
1. python preprocessRedd.py
2. python combinefiles.py
3. vim -O *.txt
:argdo %s/,\+/,/g | update
:argdo %s/^,//g | update
:argdo %s/,\n/\r/g | update
4. python sortintervals.py
5. vim -O *.txt
:argdo %s/,/\ /g | update
```
