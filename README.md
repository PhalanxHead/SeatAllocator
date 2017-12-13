# SeatAllocator
A table allocator that (roughly) randomises the people on tables.

### Use
#### seatAllocator.py
1. Install Python 3. Download link [here](https://www.python.org/downloads/ "Python Downloads") if you need to do this.

   ​	This version was developed on `Python 3.5.2`. If future versions break something, try installing this.

2. Open a terminal in the same directory as `seatAllocator.py` and run the line:
   ```
   $ python3 seatAllocator.py
   ```

3. As per the prompt, enter the location of your list of names. My csv files are formatted as in the example `example.csv`, that is, (lastName, firstName, tableNumber) (Guests with table numbers already given will be ignored), but you can edit the code to fit yours if you need.

4. As per the prompt, enter the name of the file you want to save the new lists in. By default, the program will create an output folder called "TableForm/",  <u>*</u> and save into a file called "Tables.csv" if no file is entered.

    ###### <u>NOTE: You don't need to add the `.csv` to the file name, the program does this automatically.</u>

5. As per the prompt, enter the number of seats to be on each table. This defaults to 8 people.

6. As per the prompt, enter some text as a seed for the allocation algorithm. The same seed should reproduce the same table allocation every time.

#### linearise.py

1. Open a terminal in the same directory as `seatAllocator.py` and run the line:
```
$ python3 linearise.py
```

2. As per the prompt, enter the path and name of the file you gave in step <b>3.</b> of <b>seatAllocator.py</b>  (ie the list of names and tables).

3. As per the prompt, enter the path and name of the file created by <b>seatAllocator.py</b> (ie the one in "TableForm/")

4. Enter a file to write to. By default, creates a folder called "LinearForm/", and writes to "Linear.csv"

5. Any names the program can't find for whatever reason will be on table number 0. This is a good indicator that something went wrong.

<u>*</u> (If no folder is given. Use `./<name> ` to specify the current directory)



### Config

Feel free to modify and reuse this code however you need. Potentially useful changes to be pointed out here in a future update,

### Math

This algorithm effectively uses a probing hash table to allocate all the seats. The hash is generated using a combination of MD5 hash and a random integer salt that starts with the user's input salt.

### License

Released under the Apache License 2.0:

```
Copyright 2017 Luke Hedt (PhalanxHead)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
