# Copy without Apple Books Citation

some python scripts to remove citation when copying from Apple Books

## Goal

The goal is to create a keyboard shortcut (like Cmd + Shift + C) in Apple Books that copy texts without the annoying citation info.

Instead of getting this when copying:
```
“Eliminate all other factors, and the one which remains must be the truth.”

Excerpt From
The Sign of the Four
Arthur Conan Doyle
https://books.apple.com/tw/book/the-sign-of-the-four/id395537209?l=en
This material may be protected by copyright.
```

You get this when copying with a customized keyboard shortcut:
```
Eliminate all other factors, and the one which remains must be the truth.
```

The solution I made here is sure to work on macOS Monterey 12.6, released on Sep 12, 2022.

## What I've Tried

I tried some solutions from [Don't want iBooks to always paste the "Excerpt From" of what I have copied - Ask Different](https://apple.stackexchange.com/questions/137047/dont-want-ibooks-to-always-paste-the-excerpt-from-of-what-i-have-copied), and most of them don't work well in 2022.

The solutions with `sed` command somehow doesn't work all the time, so I decided to create my own solution in Python.

## How to Set Up

### Step 1. Download `remove_citation.py` from this repo.

Save it in an easy-to-access path like `~/scripts/remove_citation.py`

### Step 2. Make sure python3 is available.

A way to do this:

1. Install [Homebrew](https://brew.sh/).
2. Install Python3 and pip3: `brew install python3`
3. (not necessary) Install [pyperclip](https://pypi.org/project/pyperclip/): `pip install pyperclip`

There may have been python3 in your mac.

The python3 installed with Homebrew may not be the default `python3` used in automator shell scripts.

### Step 3. Create the Quick Action in Automator

Create a new Quick Action in Automator like this one:

![Quick Action in Automator](https://user-images.githubusercontent.com/6902276/197236129-acaa28ce-f7d7-4722-a61e-8f717eafec1f.png)

The command is

```shell
/opt/homebrew/bin/python3 <path_to_the_dir>/copy_without_citation.py
```

Save it with a name like "Copy without Citation.workflow".

Remember to replace `<path_to_the_dir>` with your own path to the script.

Maybe replace the python3 path too with the result from `which python3` or just `python3`.

### Step 4. Create a Keyboard Shortcut

Go to: System Preferences > Keyboard > Shortcuts > Services > Text > Copy without Citation

Assign a shortcut (like Cmd + Shift + C) to it.

<img width="668" alt="Copy without Citation Shortcut" src="https://user-images.githubusercontent.com/6902276/197206078-eb63081a-3df1-4655-83fd-d2425fbd2ddf.png">

### Step 5. Allow Books.app to access the script

When using the quick action in Books.app, you may encounter an error saying "Operation not permitted".

The reason may be that Books.app is not authorized to access the python script.

<img width="260" alt="Screen Shot 2022-10-21 at 21 11 58 copy" src="https://user-images.githubusercontent.com/6902276/197207287-1fd867dc-d634-476d-bd6f-a7fc05cf59b2.png">

To solve this, you may grant Books.app Full Disk Access.

<img width="668" alt="Screen Shot 2022-10-21 at 21 10 25 copy" src="https://user-images.githubusercontent.com/6902276/197208143-6c1a35ab-0b40-4b45-8d3d-484ccf075184.png">

Then the quick action should be functioning.

### One More Thing to Keep in Mind

When you select texts in Apple Books, a small menu shows up.

![Screen Shot 2022-10-21 at 21 40 15](https://user-images.githubusercontent.com/6902276/197212919-1068de68-d170-4bf5-8259-cdc55bce4f61.png)

The keyboard shortcut and quick action doesn't work when the menu is shown.

You need to click somewhere else to close the menu before using the keyboard shortcut.

## Welcome to Leave a Message

Open an issue to leave any suggestions about this repo.
