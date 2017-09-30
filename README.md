# SeatAllocator
A table allocator that (roughly) randomises the people on tables.

### Use

1. Install Python 3. Download link [here](https://www.python.org/downloads/ "Python Downloads") if you need to do this.

   ​	This version was developed on `Python 3.5.2`. If future versions break something, try installing this.

2. Open a terminal in the same directory as `seats.py` and run the line:

   ```
   $ python3 seatAllocator.py
   ```

3. As per the prompt, enter the location of your list of names. My csv files are formatted as in the example `example.csv`, that is, (lastname, firstname) (other information is discarded), but you can edit the code to fit yours if you need. See **Modifying**

4. As per the prompt, enter the name of the file you want to save the new lists in. By default, the program will create an output folder called "TableListings", and save into a file called "tables.csv" if no file is entered.

   ###### <u>NOTE: You don't need to add the `.csv` to the file name, the program does this automatically.</u>

5. As per the prompt, enter the number of seats to be on each table. This defaults to 8 people.

6. As per the prompt, enter some text as a seed for the allocation algorithm. The same seed should reproduce the same table allocation every time.

### Modifying

Feel free to modify and reuse this code however you need. The code is fairly flexible IMO, simple changes could be made here:

1. ​

```Python
43 DEF_OUT = "TableListings/"
```

The right hand side here can be changed to wherever you want the output to be (don't stress if it doesn't exist, the program will generate it.)

2.

```Python
96 tableWriter.writerow(["Table Number"] + ["Student"] * MAX_SEATS)
```

This really just makes the header row but if you're not dealing with tables of students, it doesn't make too much sense to make columns with these labels.

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
