# Regular Expressions

```
example 

/at/g
```

/ - open
at - text to compare
/ - close
g - global i.e.(compare every "at" word in your string)

### 1. Plus

```
example

/e+/g

this will select all "e" or "ee.." together
```

### 2. Optional

```
example 

/ea?/g

this will select "e" and also "ea" together becuase "a" is optional
```

### 3. start indecator

```
example 

/ea*/g

this is morly like a  combination of ? and + 
which will select "e" and "eaaa"
this is just a example
```

### 4. Match words

```
example

1. /\w/g
matches all words in string

2. /\w{4,}/g
matches all the words which are has equal 4 character or more
```

### 5. Match any characters

```
example

1. /[fc]at/g
this matches example "fat" or "cat"

2. /[a-zA-Z]at/g
this matches example "aat" , "zat" , "Bat" ....
```
### 6. Grouping

```
example 

1. /(t|T)he/g
this matches "the" or "The"
```

### 7. Begining of the line

```
1. /^The/g
this Matches the "The" if it is in begining of the line
```
