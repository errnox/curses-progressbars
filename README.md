# Curses Progress Bars

These are two approaches to rendering progress bars using `curses`. Why one would want to do that, though, is anyone's guess... (Just using a loop and escape sequences directly is what a sane person would do.)

## Usage

```
python progressbar.py
python progressbar-centered.py
```

`progressbar.py` produces something that looks roughly like this:

```
Computing: [#####..........................] 5/100
```

Whereas `progressbar-centered.py` centers the percentage indicator text:

```
[#######                5%                       ]
```

## Note

Here is a nice trick:

Write the output to a file...

```
python progressbar.py > output
python progressbar-centered.py > output-centered
```

...then you can "replay" it like so:

```
cat output
cat output-centered
```
