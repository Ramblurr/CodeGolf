1P5: Nested boxes

source: http://codegolf.stackexchange.com/questions/2295/1p5-nested-boxes
Author: Joey http://codegolf.stackexchange.com/users/15/joey
------
*This task is part of the [First Periodic Premier Programming Puzzle Push](http://meta.codegolf.stackexchange.com/q/298/15).*

You get a hierarchy of items in the following format:

    2
    Hat
    1
    Gloves

which need to be put in boxes, like so:

    .------------.
    | Hat        |
    | .--------. |
    | | Gloves | |
    | '--------' |
    '------------'

In the input format the numbers start a box with as many items as the number specifies. The first box has two items in it (the Hat and the box that contains the Gloves), the second one only contains a single item &ndash; the gloves.

As can be seen, boxes can live inside boxes, too. And they are always rounded ... sort of (pointy corners are a wound hazard and we wouldn't want that).

*Below there are the nasty details for those that want to utilize every tiny bit of leeway the specification gives. Mind you, not reading the spec is no excuse for submitting wrong solutions. There is a test script and a few test cases at the very end.*

-----

**Specification**

* Boxes are constructed from the following characters:
  * `|` (U+007C) is used to construct the vertical edges.
  * `-` (U+002D) is used to construct the horizontal edges.
  * `'` (U+0027) are the round lower corners.
  * `.` (U+002E) are the round upper corners.

    A box therefore looks like this:

        .--.
        |  |
        '--'

    <sub>*Note that while Unicode also has round corners and proper box-drawing characters, this task is in ASCII only. As much as I love Unicode I realize that there are languages and environments out there that didn't quite arrive in the second to last decade.*</sub>

* Boxes can contain a sequence of items that are either text or other items. Individual items in a box are rendered from top to bottom. The sequence A, B, C thus renders as follows:

        .---.
        | A |
        | B |
        | C |
        '---'

    This of course applies to nested boxes too, which are an item just like text. So the sequence A, B, Box(C, Box(D, E)), F would render as follows:

        .-----------.
        | A         |
        | B         |
        | .-------. |
        | | C     | |
        | | .---. | |
        | | | D | | |
        | | | E | | |
        | | '---' | |
        | '-------' |
        | F         |
        '-----------'

* Boxes adjust their size to the content and nested boxes always extend to the size of their parent. There is always a space before and after the content, so that neither text nor nested boxes are too close to the outer box' edge. In short, the following is wrong:

        .---.
        |Box|
        '---'

    And the following is correct:

        .-----.
        | Box |
        '-----'

    Looks much nicer, too :-)

* Text items (see *Input* below) have to be reproduced exactly.

* There is always a single top-level box (cf. XML). However, one box can contain several other boxes.

**Input**

* Input is given on standard input; for easier testing likely redirected from a file.

* The input is given line-wise, with each line representing either a text item to put in the current box or opening a new box.

* Every line is terminated by a line break.

* Text items are marked by a line that does not consist of a number (see below). Text uses alphabetic characters, the space and punctuation (`.,-'"?!()`). Text will not start or end with a space and it will always have at least one character.

* A box starts with a single line with a number in it. The number tells the size of the box, i.e. the number of following items that are put into it:

        2
        A
        B

    yields a box with two text items:

        .---.
        | A |
        | B |
        '---'

    A box will always contain at least one item.

* The end of boxes is not explicitly marked with a line; instead boxes are implicitly closed after the specified number of items are put into them.

* A box is always just a single item, regardless how many items are in it. E.g.

        3
        A
        4
        a
        b
        c
        d
        B

    will yield a box with three items, the second of which is another box with four items.

    Nesting also does not affect the fact that a box is just a single item.

**Limits**

* The maximum nesting level is **five**. I.e. there are at most five boxes inside of each other. This includes the outermost one.

* There is a maximum of **ten** items per box.

* Text items have a maximum length of **100** characters.

**Output**

* Output is the rendered box including all containing and nested items according to the rules outlined above.
* Output should be given on standard output and it has to match exactly. No leading or trailing whitespace is allowed.
* Each line must be terminated with a line break, including the last.

**Winning condition**

* Shortest code wins (i.e. gets the accepted answer).

**Sample input 1**

    3
    This is some text!
    Oh, more text?
    Just text for now, as this is a trivial example.

**Sample output 1**

    .--------------------------------------------------.
    | This is some text!                               |
    | Oh, more text?                                   |
    | Just text for now, as this is a trivial example. |
    '--------------------------------------------------'

**Sample input 2**

    4
    Extreme
    nesting
    3
    of
    boxes
    4
    might
    lead
    to
    2
    interesting
    1
    visuals.
    Indeed!

**Sample output 2**

    .--------------------------.
    | Extreme                  |
    | nesting                  |
    | .----------------------. |
    | | of                   | |
    | | boxes                | |
    | | .------------------. | |
    | | | might            | | |
    | | | lead             | | |
    | | | to               | | |
    | | | .--------------. | | |
    | | | | interesting  | | | |
    | | | | .----------. | | | |
    | | | | | visuals. | | | | |
    | | | | '----------' | | | |
    | | | '--------------' | | |
    | | '------------------' | |
    | '----------------------' |
    | Indeed!                  |
    '--------------------------'

**Sample input 3**

    1
    1
    1
    1
    1
    Extreme nesting Part Two

**Sample output 3**

    .------------------------------------------.
    | .--------------------------------------. |
    | | .----------------------------------. | |
    | | | .------------------------------. | | |
    | | | | .--------------------------. | | | |
    | | | | | Extreme nesting Part Two | | | | |
    | | | | '--------------------------' | | | |
    | | | '------------------------------' | | |
    | | '----------------------------------' | |
    | '--------------------------------------' |
    '------------------------------------------'

**Sample input 4**

    3
    Foo
    2
    Bar
    Baz
    2
    Gak
    1
    Another foo?

**Sample output 4**

    .----------------------.
    | Foo                  |
    | .------------------. |
    | | Bar              | |
    | | Baz              | |
    | '------------------' |
    | .------------------. |
    | | Gak              | |
    | | .--------------. | |
    | | | Another foo? | | |
    | | '--------------' | |
    | '------------------' |
    '----------------------'

**Test Script**

Since getting details right can be difficult at times we ([Ventero](http://codegolf.stackexchange.com/users/84/ventero) and me) have prepared a test script you can run your solution with to check whether it's correct. It's available as both a [PowerShell script](http://hypftier.de/dump/CG2295/test.ps1) and a [bash script](http://hypftier.de/dump/CG2295/test). Invocation is: `<test-script> <program invocation>`.

