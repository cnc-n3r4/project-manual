# III SECTION 2 PROGRAM OPERATION 05. PROGRAM EDITING OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-05.-PROGRAM-EDITING-OCR.PDF*

---



4203-E P-211



SECTION 2 PROGRAM OPERATION


## 5. Program Editing

In the program edit mode, modification, insertion, deletion, and others can be conducted for on programs



stored in the memory.



(1) Programs are edited in units of file.



(2) Program editing-related terms are defined as follows:



(a) Edit Line



This is the line on which program edit operation is carried out.



On the display screen, the symbol ">>" appears at the left-most posrtion of the edit line. One line



on the display screen contains a maximum of 63 characters.



(b) Edit Pointer



This refers to the identifier indicating the character to be edited. On the display screen, such a



character is displayed in the reversed display mode.



{c) Record



This is so called a block in the program. The record consists of several commands beginning with



a character right after the "LP' code and ending with the next "LF" code. If commands in a block



cannot be displayed in one line on the display screen, they are displayed on multiple lines with the



2nd and subsequent lines preceded by"&", indicating that the commands are continuous.



(d) The extract buffer means the buffer where commands are temporarily saved for copy or



transfer operation. The buffer capacity is 64 character x 23 lines.



Edit line



Edit pointer



1 record



(one block for



a machining



program)



PR:JG OPERATION



GOl



G40



GOO



=E WHEEL100.MIN



tile end



EDIT



X300 Y300



Y200



Y300



Y300



Y200



Y200


#### P MODE WHEELlOO. MIN

97/ 7/15 14:10:00



S250


#### Z-55 M09 M03

F100 011



10 J100



1-200 JO



llOO JO



2100



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELETE INSERT DELETE DELETE ERASE OU IT [EXTEND]



16 lines


```text


                                                                                                 ──
                                                                          ┌───────┐─┐─┐──────────░░░─────────
                                                                          │░░░ ░░░│ │ │░░░░░░░░░ ───▒░░░░░░░░
                                          ────────────────────────────────┘───────┘─┘ └─────────      ──    │
           ┌─       ────   ─────┐───────                                                                    │
           │▒│ ────┐▒░ ░░░   ░░ │░ ░░░   │ ─────────────────────────────────────────────────────────────────┘
           └─┘     └────────────┘────────┘
                                          ─┐─┐────┐─┐──────┐─┐─────┐─┐─┐─┐───┐─┐─────┐──────────┐───────────┐
                 ┌─────░░░░░░ ──░── ░░░│ │░│░│░░░░│ │░░░░░░│ │░░░░░│ │░│ │░░░│ │░ ░░ │░ ░░░░░░ ░│       ░░  │
                 │░   ░──────   •   ───┘─┘─┘─┘────┘ └──────┘─┘─────┘─┘─┘─┘───┘─┘─────┘──────────┘───────────┘
                 │   •
                  │ │ •░  ───┐ ───┐ ───── ────────  │
                  │ │        └─   │                 │
                  │ │        │  │ │     ───     ──┐  ─────┐───┐──────┐
                  │       ░──┘  │░  ░  ░░░░  ░  ░ │ │ ░░░ │░ ░│  ░ ░░│
                  │  ─┐  ─┐  └┐ └─────────────────┘─┘─────┘───┘──────┘
                    │░│ │ │   │░│
                    └─┘ └─      └───────────────────────┐───────┐─────────────┐
                       •   ░ ░ │░ ░ ░ ░  ░░░  ░░░░░░  ░░│ ░░░░░░│░ ░ ░░ ░░░ ░░│
                        │      │          ┌─                            │ │   └────────────┐─┐─┐─┐─┐─┐────┐─┐
                        │    ░ │      ────┘ ┌─────    ────── ░░░── ░ ───┘─┘─ ░░ ░ ░░░░  ░ ░│ │░│ │░│ │  ░ │░│
                        │░─────┘──░│ ░░░░░░ │░░░░░░──  ░░░░ ──── ░░ ░░░░░░░ ───────────────┘─┘─┘─┘─┘─┘────┘─┘
                    ┌─┐ │         ┌┘────────┘──────  ──────      ───────────
                    │░│ │░░ ░░░░░░│
                    └─┘─┘                ─────   ──────  ──   ─────┐ ──────┐───┐─┐───────┐───┐──────┐─┐──┐──┐
                        └─────░░░ • ─────░░░░░──░░░░░░ • ░░───░░░░░└─░░ ░░ │░░░│ │░░ ░ ░ │░░░│  ░░░░│ │░░│  │
                        │░░ ░░──── ░░░░░ ─────░░ ─────░░░──░ ░ ──── ░──────┘───┘─┘───────┘───┘──────┘─┘──┘──┘
                     ── │          ── ───     ──      ──   ────     •
                        │░
                    ──  │     ─┐──────────────────── ────  ┌────────   ──── ──  ─────  ─────────     •    •
                       ┌┘ ░ ──░│  ░░░  ░ ░░░   ░░ ░ •    ──┘░       ───   ░• ░──    ░──       ░ ───── ┌─── │
                       │  ──      ──    ░      • ──  ░•                                   │       ░   │░   └┐
                         •          ───     ──        ░──────────── •  ─── ───  ──────────┼───────────┘ ░░░░│
                        │░░  ░ ░ ░░░░░░░░   ░░░ ░──   ░░ ░░░░░░ ░░░░░  ░░░ ░░░ ░░░░░░░░ ░ │░░░░░ ░░░░ ░░░───┘
                        └─┐─┐─────────┐──────────░░─┐───┐─────────────────────────────────┘───────────┐──
                    ┌─    │ │         │             │   │                                             │
                    │░│ ┌─┘─┘░░░─────░│ ░ ──────────┘─┐─┘░────────── ────  ┌─────                    │
                    └─┘ │     ─┐     ─┘ ──     ░░     │                  • │      ┌────────────── • ─┘
                        └─ ──  └┐─     │       ─── │░░│  ░   ────┐  ░• │   └─── ░░│              • •
                                │ •  ┌─┘─────      └──┘──┐──     └──┐  └──                ─┐
                                     │░░ ░░░░  ░│        │░░░       │  ░░░───────░───────  └─┐
                               │ │ ──┘──────────┘────────┘──────────┘────░ ░░░░░▒░░░░░░░░    │
                               │ │                                       ────────────────┐   │
                      ────   ──┘ └─ ░───░   ┌─       ┌─┐     ┌─┐     •                   │   │
                     │░░░░──┐  │ │  │░░░│   │░─┐     │░│     │░│   ┌─░│    ┌┐    ┌──     │   │
                     │░    ░│  │ │  │░░░│   │░░│     │ │    │  │   │░░│   ┌┘┘┐   │░      │ ┌─┼──┐
                     │  ────┘  └─┘ ─┘░──┼── └──  ────┼─┘┐   └──┘   │   • ─┘ ░│ • └──    ─┘ │░│  │
                               │ └─░│░░▒│            │░░│   │░░│   │░░░░  │░░│  •   ──── │ └─┼──┘
                       ───     │ │ ─┘░░▒└──          │░░│   └──┘ ──┘────  └──┘──        ─┘   │
                     ┌─░░░┌────┘ └─ │░░░│   │░│      │░│                 •               │   │
                     │░  ░│░ ░   │  │░░░│   │░│      └─┘                                 │  ░│
                     │░░░░░░───  │  │░░│    └─┘                    ────                  │   │
                     └──────   │░│  └──┘                                                 └─  │
                               │░│                                                       │ │ │
                               └─┘                                                         │ │
                               │ │   ┌───  ────┐                                           │ │
                               │ │  ─┘ ░░░ ░░ ░│                                           │ │
                               │ │ │   ─── •  ─┘                                           │ │
                               │ │ │        ┌┐  ── •     ──          •        •  ┌─┐       │ │
                               │ │ │ ───   ─┘┘─   │░──  •░░─┐  ┌────┐ ┌──┐   │░  │░└┐────┐ │ │
                               │ └─┘ ░░░   ░ ░    │░░░   ░•░│  │░ ░░│ │░░│   │   │  │░ ░░│  │
                                •  │      │                    │   •     │          │  ──┘  │
                                 ─┐┘ •  ──┼───        ─┐  •  │  │      ──┘     │ │ │ ┌─  │
                                  │░  │ ░ │  ░  ░   │ ░│ │ │ │░ │░     ░░│  ░ ░│ │ │ │░ ░│
                                  └───┘ ──┘─────────┘──┘─┘─┘─┘──┘────────┘─────┘─┘─┘─┘───┘
                                       •
















```

*Figure from page 1 (2337x3305 px)*


---


## NOTICE

4203-E P-212



SECTION 2 PROGRAM OPERATION



When program edit operation has been completed, press function key [F7] {PIP QUIT).



Otherwise, edited data cannot be stored in the memory.


#### PROO ~TION

>::milOOO



NlOO GOO



N101 G56



N103 G41G01



N104 003



N105



N106



N107 GOl



N108 G40



N109 GOO



N110



Nl 11



=E WHEEL100.MIN



file end



X300



X400



xsoo



X100



X200


#### X400

X300


#### EDIT p MOOE WIEEL100.MIN

97/07/15 14:10:00



Y300 $250



Z-55 M09 M03



Y200 FlOO 011



Y300 10 JlOO



Y300 1-200 JO



Y200 1100 JO



Y200



2100



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELETE INSERT DELETE DELETE ERASE OU IT [EXTEND]



@@)@@@]@~@



Press [F7] (EDIT QUIT).



Program edit operation is complete, and the display screen as indicated to the right will be



displayed on the command line.



PROO OPERATION EDIT



>:iIDOOO


#### N100 GOO X300 Y300 $250


#### N101 G56 Z-55 M09 M03


#### N103 G41G01 X400 Y200 F100 D11

N104 G03 X500 Y300 10 JlOO



N105 X100 Y300 1-200 JO



N106 X200 Y200 1100 JO



N107 GOl X400



N108 G40 X300 Y200



N109 GOD ZlDO



N110



N111



file end



DATE DIR PIP EDJT ~Tl UST



CONDENS



[EXTOO)


```text


                                                                                               ───
                                                                         ┌───────┐───┐─────────░░░─────────┐
                                                                         │░ ░░░░░│ ░ │░░░░░░░░░ ── ▒░░░░░░░│
                        ───  ─────                                                                         │
         ┌──┐───────────   ┌─ ░░░░────────────────────────────────────┐──────────────────────────── ───    └┐
         │░ │░░░░░░ ░ ░  ┌─┘░  ░ ░   ░    ░░ ░░░ ░░  ░ ░ ░░░░ ░    ░░░│   ░░░ ░░ ░░      ░░░ ░░░░   ░   ──  │
         │░ │░ ── ░ ──┐  │                             │ │   │        └── ─┐────────────────────────────  │ │
         └── ──  ───  └┐   ░░░░ ░░░░ │░░░░ │░░  ░░░ ░ ░│ │ ░░│   │░  ░░░ ░ │                              │ │
                       └─  ──────────┘─────┘───────────┘─┘───┘───┘─────────┘                              └─┘
                         •                                                               ─────────────────
                             •  ─┐──┐─┐──┐───┐────────┐─┐──────────┐───     ─────────   •
                            │    │▒▒│░│▒▒│░░░│        │▒│░         │░▒░─────▒▒░░░░ ▒░│   │
                            │ • •  ─┘─┘──┘───┘────────┘─┘──────────┘──┐░░░░░─────░░──┘   │
                           │ │   ┌─                                   └─────     ──  │ │ │
                           │ │   │░░│    ┌┐       ┌─┐    ┌──    ┌──┐                   │ │
                           │ │  ─┘░░│   ┌┘┘──┐   ┌┘ │    │      │ ░│   ┌─┐    ░        │ │
                           │ │   │░░│   │░░░░│   └┘░│    │ •   •░░─┘   │░└─   ──       │ │
                           │ │   │░░│   └────┘   │░░│    │░░│   │░ │   │░│             │ │
                           │ │   │░─┘            │░░│    │░░│   │ ░│   │░│             │ │
                           │ │   │░░│            └┐░│    │░│    └──┘   └─┘             │ │
                           │ │   │░░│   │░│       │░│    └─┘    │  │                   │ │
                           │ │   │░░│   │░│        ─┘    │ │    │ ░│                   │ │
                           │ │   │ ┌┘                           └──┘                   │ │
                           │ │   └─┘                                                   │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │     ┌── ─────┐                                          │ │
                           │ │  ┌─ │░░│ ░ ░ │                                          │ │
                           │ │  │   •░│    • │                                         │ │
                           │ │  │    • • ─┐  └─       ──                ┌──            │ │
                           │ │ • ┌──    •░└┐   ┌───  │░░──┐────┐───┐──┐ │░░│     ──────┘ │
                           │     │░░░   ░░░│   │░░░  │░░░░│ ░░░│   │░░│ └─░│   ──░░░░░   │
                            •   • ──       │             │     │     │      ┌─      ──┐ •
                             ─┐  ░░     │░   • │░ │   ── │ ┌───   │ ░│     ─┘ │  ┌─┐  │
                              └┐  │  •  │ │ •░ │  │ │  ░ ░ │  ░ ░ │  ░ ░    │ └┐ │ │ ┌┘
                               └──┘ • • └─┘  ──┘──┘─┘ ─────┘──────┘─────  ──   │ └─┘ │
                                   •                                    •    ──      └┐
                                                                     ░ ░░ ░  ░░░• │  ░│
                                                                        •    ───  │
                              •     ──  ─────        ────┐─┐─┐─┐──┐────┐ ┌───   ┌─ ┌───────────┐─┐─┐───┐──┐
                          ┌───░────░░░──░░ ░░────────░░░░│ │░│ │░ │░░░░│ │░░░░│ │░ │░░░░░░ ░  ░│ │░│  ░│ ░│
                          │░░░•░░░░ ──░░──── ░ ░░  ░ ────┘─┘─┘─┘──┘────┘─┘────┘─┘──┘───────────┘─┘─┘───┘──┘
                           ──
                                 ────────────── ──── ──────────────────    ─────────   ──
                           │     ░▒░░░░▒░░░▒░         ░░░        ░ ▒▒▒░─── ▒▒▒░░░░░░│    │
                           │ │       ─────────────   ─────────────────┐░░░░───────░▒└─   │
                           │ │  ┌───┐             ──                  └────       ──   │ │
                           │ │  │▒░░│   ┌──      │  │    • │   ┌───┐                   │ │
                           │ │  └─░░│   │░░──    │  │   │  │   │░░░│   │░•   │░│       │ │
                           │ │  │░░░│   │░░░░    └──┘   └┐─┘   └───    │  •  └─┘       │ │
                           │ │  │░░░│   └─┐──    │░░│    │░│   │░  │   │ │             │ │
                           │ │  │░░░│   │ │      │ ░│    └─┘    │░░│   │░│             │ │
                           │ │  │░░░│   └─┘      │░░│    │ │    └──┘   └─              │ │
                           │ │  │░░░│   │░│      └──┘   ─┘░│   ┌┘  │                   │ │
                           │ │  │░░░│   └─┘              └─    │░░░│                   │ │
                           │ │  │░┌─┘                          └───┘                   │ │
                           │ │  └─┘                                                    │ │
                           │ │                                                         │ │
                           │ │    ─────┐                                               │ │
                           │ │ ┌─    ░░│                                               └─┘
                           │ │ │  ┌────┘                                               │ │
                           │ │  │ │     ───┐─ ────────────       • ───┐─ ───────────── │ │
                           │ │  │          │ │            ───── │ │   │ │              │ │
                           │ │    │     ┌─   │ ┌─  • ┌─     ░░  │ │ ┌┐  └┐────┐ ┌────┐ │ │
                           │   ┌──┘─    │░•  └─┘░│  ┌┘░──  ───  │  ─┘┘ • │░░░░│ │░░░▒│   │
                            ── │    ── •         └──┘         ┌─┘    │   │  ──  │   ─┘  •
                              │  ░│   ░ ░░   ░  ░   │  ░    │░│    ░░│    ░░░    │░  │
                              └───┘── • ──── ──── ░ │ ────  │ │  ─── │ ── ░── •  │░  │
                                     • •    •    ─── •     • • ──   • •  ──  • •  ───┘













```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-213


#### SECTION 2 PROGRAM OPERATION

5-1 . Commands Used in the Program Edit Mode



Item Command Functions



Insert line INSERT LINE Inserts a blank line right after the present edit line.



Delete line DELETE LINE Deletes the line including the edit pointer.


#### Insert character INSERT

Inserts a blank space (for one character) right before the edit pointer.


#### CHARACTER


#### Delete character DELETE

Deletes the character identified by the edit pointer.


#### CHARACTER

Delete DELETE Deletes the specified number of records (blocks) in a program.



Erase line ERSE LINE Erases the commands in the line which contains the edit pointer.



The line remains as a blank line.


#### Quit QUIT Ends the program edit mode.

Find FIND Searches the specified character-string.



Shifts the edit line by the specified number of lines.



Change CHANGE Replaces the specified character-string with the newly specified char-



acter-string.



Copy COPY Duplicates program data in the specified number of lines to the ex-



tract buffer. The original program data remains as it is.



Move MOVE Duplicates program data in the specified number of lines to the ex-



tract buffer. The original program data is deleted.



Extract XTRACT Inserts program data in the extract buffer before the edit pointer.



Page mode PAGE MODE Replaces the character located by the edit pointer with the keyed-in



character.



Insert mode INSERT MODE Inserts the character which has been keyed i through the keyboard



before the character located by the edit pointer.


```text


                                                                                               ┌───        │
                                                                         ┌──┐──────┐─┐─────────┘   ──── ───┘
                                                                         │░░│ ░░░░ │ │░░░░░░░░░ ───░░░░•░░░│
            ──────── •         •    ─────  •                      ───────┘──┘──────┘ └─────────      ──   ─┘
          ┌─        • ────────┐ ┌───     ──  ─────────────┐─┐─────                                         │
          │░  ┌────           │ │        ░   ░         ░  │ │░    ┌─               ──────       ──────
          │   │               │ │   │  │   ░    │░ ░ │ •  │ │   ░ │ ───          ──      ───────      ──────┐
          │  •   ┌── ┌─────┐──  │ • └──┘ ┌─    ─┘────┘─ ──┘─┘─────     ────┐─┐──┐                           │
          │░│    │░░ │     │   │░•░░ ░░  │ │ │                        │  ░ │░│░░│                          │░│
          │░└──     ┌┘      ┌──┘   │    │  │░└──── • ──────┐─────────┐┘         └───────┐                  │░│
          │░░░░─────┘       │░░░░░─┘────┘  │ ░░░░░• •░░░   │░ ░░░░ ░░│ ░──░░•░•░░ ░░░ ░░│                  │░│
          │░░░░░░ ░░░│    ─┐░░░• ░░░  ░░░┌─┘ ░░░░░░ ░  ░░│ ░░░ ░░░░ ░│ ░░░   •░─┐───────┘  •        •    ──┘░│
          │░         └───  │░       ┌────┘ │░   ─────   ─┘─ ──────░─┐  ─┐─      │        ─┐ ────┐─── ────  │░│
          │░┌────────░░░░• └┐░──────┘      │                     ░│ │ • │  │      │       │ ░   │        ──┘░│
          │░│               │░░░░░░░│░░░░┌─┘                      │ │      │  •   │      ─┘───          •  │░│
          │░└────────────┐  │░░• ───┘────┘ └──────┐─────┐─────────┘─┼──┐──┐ ── ┌──  ────┐     ──────────   │░│
          │░│            │  │░░ •░       │ │░░░░░░│ ░ ░ │░░░░░░  ░░ │░░│ ░│  ░ │░░•░░ ░░└┐                 │░│
          │░    •  ──────   │░•░░░░░──░░░│ │░     │     │           └┐─       • ┌┐ ─── • └───────┐─┐       │░│
          │░░░░░░•          │░░──░•░    ─┘─┘ ──░──┘ ░ ░ │░░░░░░ ░░ ░░│ │░ ░░░░░─┘┘░░░░•  │    ░░ │░│       │░│
          │░░     ───       │    ░   ─┐     │░    │    │             │ │                         │ └┐      │░│
          │░• ──┐─░░  ──  ─┐░────┐ •░░│     │░─┐──┘┐───┘─────────────┼─┘┐  ░ ░• •░ ░░ ░•░ ░ │░──░ ░░└─     │░│
          │░    │ ────     │░    │  ──┘       ░│ ░ │ ░ ░░░░ ░░ ░░░░░░│░ └───── • ────── ────┘─  ────┘      │░│
          │░────       ──── ░────┘       ──┐─░┌┘┐──┘──░░░░░┌─░░░─────░│                               ─────┘░│
          │░     ──────    ─┐░   │ ──────  │░░│ │         ░│ │        └──┐─────┐                           │░│
          │░┌────        ── └────┘       ──┼─░│░│░░░░ │░ ░░░░│░░░ ░░░░░░░│ ░ ░░└─                          │░│
          │░│              │               │ ─┼─░  ─┐─┘─  •        ─────░ ░   •  • ──────┐                ─┘░│
          │░└─────┐        │░─────────      │░│  ── │        ░░           ░  ░    │      └───────────────┐ │░│
          │░│░░░░░│     ───┘ ░░░░░░░░    ──┐┘░░•░░░─┘─░┌──░──────────────────────░│ ────░░░░ ░░░░ ░░░ ░ ░│ │░│
          │      ─┘─────   │      ──   ──  └┘░•░──┐░░░░│                                │              ──┘ │░│
          │░│ ─┐           │░•░ ░░          │░  ░ │░░░│░──┐──────┐─────┐────────────────┘───────░░░░ ░░    │░│
          │░│  │           │      │        │░░•░░ └─░░│ ░░│ ░  ░░│ ░   │ ░ ░ ░   ░  ░░           ──┐──┐    │░│
          │░└─  │          │░─────┘        │░░░───┘░░│   •░──░░░░│ ░─┐─┘░ ─┐░─┐ ░░░░░░ ░░  ░░ ───  │  │    │░│
          │░░░ ░│          └─░░░░░│         │░ ░░░░░░│ ░░░░░░───░│ ░ │░└─░░│░░│░    ░░░ ────── ░░ ░░ ░│ •  │ │
          │░       ────────                 └────────┘  ░───┐░ ░─┘ ░─┘─░░┌─┘──░ ░ │░──░░              │  ──┘░│
          │░───────         ┌────────       ░         ──    │ ░          │    ░───┘     ─────────────      │░│
          │░░░░░░░ ──┐┐──── │░░░░░░  ───┐───┐░•░────┐░░░░ ░ ░░░░░░░░░░░░░░│ │░░░░░░░░░░  ░░░░░ ░░░░░░ ── ┌─┘░│
           ─────── ░░└┘     └───────┐░░░│   └─░•░░░░│ ────────────────────┘─┘────────────────────────░ ░┌┘ │░│
          │░           ─── │        │      •   ░ ───┘                                                   │ ─┘░│
          │░┌─────────┐    │░┌────── ─────  │        │   ──────  •      • ─── ───    ───────────────────┘  │░│
          │░│░░░░ ░░ ░│    │ │░░░░░  ░░  ░──┘░░░░░░──┘───░░░░░░──░────── •░░░•░░░────░  ░░░  ░░ ░░░░ ░░░│  │░│
          └─┘───────── ────┘  •      ───    │░░░░░ ░░░ ░░░░░░░ ░░░░░░░░░ ░░░░░░░░░░░░░──────────────────    ░│
                                             ───────────────── ───────────────────────                      •








































```

*Figure from page 3 (2328x3293 px)*


---



4203-E P-214



SECTION 2 PROGRAM OPERATION



5-2. Fundamental Operations Necessary for Program Editing



5-2-1. Readout of a Program File from the Memory



(1) Press function key [F4] (EDIT).



MULTI



DATE DIR PIP EDIT PIP LI ST CONDENS [EXTEND]



Press [F4) (EDI1)



The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.



EDIT E



PAOGRUM OPERATION



EDIT



El]]



INDEX DISPLAY PROCEDURE



[F2l - M01:*.MIN



[F3J - FOO:*.MIN



I 97 /07 /15 14: 10:00



~ I TE



TO DISPLAY OTHER lt,DEXES, AFTER PRESSING [Fl] ,



INPUT l'HE DEV I CE NA1E AND FI LE NAME. l'HEN PRESS [WR I TE] KEY.


#### DEFAULT DEVICE NAME= M01:


#### DEFAULT FILE NAME= *.MIN

>XE



MD1: FOO: COMMAND OVEAWR/ CHAR.



INDEX INDEX INDEX HI STORY INSERT DELETE CANCa


```text


                                                                                              ┌───
                                                                        ─┐─┐──────┐─┐─────────┘ ░░────────┐
                                                                         │▒│ ░░░░ │ │░░░░░░░░░░───░░░░░ ░░│
              ────              •           •   ──      ─────            └─┘ ─────┘─┘─────────     ────
         ┌───     ─────────────┐ ┌────────── ───  ──────     ┌──   ────┐─   •                              │
         │   ┌─── ░            │ │                         │ │  ┌──    │       ────────────────────────────┘
          ───┘    │   ─────────┘─┘──┐──────────────────── ─┘─┘─ │░ ░ • │  •  ░│
         │   │ │  └───              │                          ─┘────   ── ───┘
         └┐ ░  │  │░░░░░░  ░    ░░░░│   ░ ░ ░│ •░ │░░░░░░│
          └────┘ │ ┌─┐─           • └───────┐┘─ ┌─┘──────┘
                 │░│ │ ░░░ ░ ░░░░░ │░░░░░░ ░│░░░│
                 └─┘ └────┐────────┘────────┘───┘
                          │                                                                 │
                        • │                                                                 │ │
                       │                                                                    │ │
                       │ │  ┌─┐───   ─────   ──────────────      •  ─────                  • •
                       │ │  │ │   ┌─┐     ┌─┐              ─┐───  ─┐      │       ─┐        •
                        │ │ │  ─┐ │ │  ─┐ │ │ ┌─┐ │      •  │░░    └─    ┌┘─ ─── • │ ────┐ │ │
                        │ └─ │░ │ │ │ • │ │ │ │ │ │  ┌─┐  ──┘────┐─┘ ─── │  •░ ░│   •    └─┘ │
                        │    │   │   │   │      │    │ │         │      │ │  ───┘      •     │
                         ── ┌┘─┐─┘───┘───┘──────┘┐───┼─┘── ───┐──┘┐─┐─┐─┘─┘─      ─────  ───
                           ┌┘ ░│  ░ ░ ░░   ░ ░ ░ │ ░ │      ░░│ ░ │ │░│ ░ ░ ░│░      ░ ░│
                           └┘ ─┘ │░ ░───┐ ── ─── └─┐ │ ┌─┐─  ─┘ ░ ░ └─┘ │ ░──┘────  ── ░│
                             •  ─┘───   └─  •   ─┘ └─┘░│ │ ──   ───   └─┘──       •   ──
                                                     └─    ░░░░░░ ░░ ─┘
                                                        ─────────────
                      ───   ──     •    ── ── • • ───
                     │        ─┐─── ───┐     │ │ •   ─────── ───────┐ │ ───────────────────────────────────┐
                     │ ─────┐  │       └─   ─┘ └─ ───              ░└─┘   ░                          ░     │
                     │░░░ ░░│  ░ │░░ ░ ░░░┌─         ───────   ─────     ──────────────────── ─── ─────────
                     │  ─┐── │ ┌─┘────────┘
                     │ • │   │░│                            ──
                      •      │  ─┐────────────┐─────────────  ───────                 ──
                           │     │░░░░ ░░░░  ░│                      ┌─────        ─┐   │
                           │ •       • ────── │                      │ ░ ░░───────░░│   │
                           │    ░▒░░                                 └──── ░░░▒░░▒  └┐  │
                           │    ─────────────────────────────────────      ────────  │  │
                           │ │                                                     │ │  │
                           │ │                                                     │ │  │
                           │ │    ─┐──       ──────                                │ │  │
                           │ │ • •░│░  ┌─── │░░░░░░              ──────────────────┘─ │ │
                           │ │  │░░│   │░ ░┌┘░                                        │ │
                           │ │  │░ │ ─┐ ░ ░│▒░ ───── ─────┐───────┐───┐─┐───── •      │ │
                           │ │  │░░│ ░│░ ░░ ░  ░▒░░░│ ░ ░ │▒░  ░░ │░░░│ │░      │     │ │
                           │ │  │░░░░  │░░░░ ░░░───▒│ ┌───┘───────┘───┘ └───────┘     │ │
                           │ │  └───── └────░▒──   •░┌┘                               │ │
                           │ │              ──      ─┘                                │ │
                           │ │                                                        │ │
                           └─┘                                                        │ │
                           │ │  ───                                                   │ │
                           │ │   ░ ──     ──                             ────         │ │
                           │ │  ──┐  ────   ───     ─────────── ──┐          ┌─┐───── │ │
                           │ │    └┐   ░░─┐─  ░──┐ •░░▒░░  ░░░░░  └────┐─┐──┐┘ │      │ │
                           │ └─┐─░░│  ──░░│  ──░░│ ░ ─────────░░  │░░░░│ │░░│  │     ─┘ │
                            •  │ ──      ─┘    ──┘                    ─┘  ─┐┘   •  ──   │
                             • └─   ── •      •      ──     │░     ──   │  │ • │ ─┐  ┌──
                               │░   ░░   │ │░ ░   ░  ░░   ░ │░ ░ │  ░ ░ │  │ ░ │░ │ ░│
                              ─┘─────────┘─┘──────── ───────┘────┘──────┘──┘ ──┘──┘──┘
                                                                            •























```

*Figure from page 4 (2346x3317 px)*


---



4203-E P-215



SECTION 2 PROGRAM OPERATION



(2) Enter the file name of the file to be edited and press the WRITE key.


#### WHEEL 100.MIN

When a program has been stored without specifying a file name, that is, when a program is stored



with the file name "A.MIN", this step can be skipped.


#### PROGRAM OPERATION

197/07/15 14:10:00



EDIT


#### E WHEEL100.MIN[l

INDEX DISPLAY PROCEDLflE



[F2] - MD1:*.MIN



[F3] - FDO:*.MIN



TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl] ,



ltf'UT THE DEVICE NAME AND FILE NAME, THEN PRESS



DEFAULT DEVICE NAME = MD1:



DEFAULT FILE NAME= *.MIN


#### OVERM11TE

[WRITE) KEY.



MDl :



FOO:



CCJ.f.lAND



OVERM,/



CHAR.


# I I

INDEX INDEX INDEX HI STORY INSERT DELETE CANCEL



-.WR_I_TE-



Program data of the specified file is searched and read into the editing area. At the same time,



program data is displayed on the display screen.



Program data of the file name "WHEEL 1O D.MIN" is ready for editing.



PROO OPERATION



>:@000



N100 GOO



N101 G56



N103 G41G01



N104 G03



NlOS



N106



N107 001



N108 G40



N109 GOO



N110



N111



=E WHEEL100.MIN



file end



X300



X400



X500



XlOO



X200



EDIT



X400



X300



Y300 S250


#### Z-55 Kl9

Y200 FlOO 011



Y3DO 10 JlOO



Y300 1-200 JO



Y200 1100 JO



Y200



Z100



LINE LINE CHAR. CHAR. LI NE EDIT



INSERT DELETE IN SERT DELETE DELETE ERASE OU 1T



100.MIN



4:10:00



M03



[EXTEND]


```text


                                                                                               ┌───
                                                                          ┌─┐───┐─┐───┐────────┘░░░─────── ┌┐
                                                                          │░│░░░│░│   │░░░░░░░░░───░░░░░░░─┘┘
           ┌──────   •                               •             ──     └─    └─┘─  └─────────     ────
           │      ┌─┐  ────────────────────────┐───┐─ ────┐─┐──────  ────┐  ────                            │
           └───── │░└─┐░ ░                    ░│   │      │ │            │░░░     ┌─────────────────────────┘
                  └─┘ │        •  ───┐─────────┘───┘──────┘─┘────────────┘────────┘
                      │░░░░░░ │░░ ░░░│
                      │       │     │ ─────────────┐────────────────────┐─┐───┐─┐─┐───┐────────────┐────────┐
                       ┌─┐░───┘ ░░░░│ ░░░ ░░░░ ░ ░░│ ░░░░░░ ░░░░░░░░ ░ ░│ │░ ░│ │░│ ░ │░░░        ░│     ░  │
                       │░└─░  ░ ──── ───   ░┌─── ──   ─┐──   •     ┌────┘─┘───┘─┘─┘───┘────────────┘────────┘
                       │                    │        │ │         • │
                            ┌────────────          ──┘ └─      ──               ───
                      │ │   │░░░░  ░░░░ ░│                       ─────        ──   •
                      │ │   │   ░  ───┐  │                        ░░░ ─────── ░  •  │
                      │  │  │░░•      └─                         ──── ░▒░▒▒░░ •   │ │
                      │  │  └─░░░ ░░░▒░░░┌──────────────────────      ──────── │  │ │
                      │  │ •  ───────────┘                                     │  │ │
                      │ │                      ───────────                     │  │ │
                      │ │     ┌──   ─── ──────┐                                │  │ │
                      │ │   ┌─┘  ┌── ░ •░ ░░░░│ ───────────────────────────────┘  │ │
                      │ │   │░░  │░░• │▒ •                                        │ │
                      │ │  •░░░──┘ •░ │░│   ──   ────  ─────                      │ │
                      │ │   ┌─░░░░░ │░░░└──░░░─┐ ░░░░ •░░░░░  ░─── ┌─┐─────┐      │ │
                      │ │   │▒░░ │░ │░░ ░░▒░• ▒│  ───░░──── ░ •░░  │░│    ░│      │ │
                      │ │   │░░░ └─░└─░░▒░── ──┘ •             ── ─┘─┘─────┘      │ │
                      │ │    ────  •  ────      •                                 │ │
                      │ │                                                         │ │         ─── ──
                      │ │                                                         │ │        •      ─┐
                      │ │  ┌─┐                                                    │ │       │  ┌─┐ │ │
                      │ │  │░│                                                    │ │       │  │▒│ │ │
                      │ │  │    ────   ──┐      ───┐ ─── •  • •         ──┐─────  │ │       │ ─┘  │ ░│
                      │ │   ┌─┐─  ░░───  └──┐─ •░▒░│ ░░░•▒── │░┌──┐────┐  │       │ │    ───┘ ░░░ │ ░│
                      │ └─ ─┘░│   •░░     ░░│  ░░•░│  •░░░░  │░│  │  ░ │  │     ── │      ░ ░───── • │
                      │   • └─┘    ┌──   ┌──┘             •  └─░ ┌┘    │  │        │      ───       •
                       ──┐     • ┌─┘     │             │         │      │ └─┐── ┌─            ──────
                         │  ░│ ░ │  ░│ ░ │ │ ░│ │░│ ░░ │░│    │░│  ░ ░│ │ │ │▒ ░│
                           ──┘─  └───┘───┘─┘──┘ └─┘ ───┘─┘┐   └─┘  ───┘─┘ └─┘──
                       ───      •              •   •      └──     │      │       ─────────┐─┐──────────────┐
                      │ ░░• ░│ │░│░•░ ─────┐ ░░░░ ░░────░░ ░ ───░░│ │░░│ │░ │░│ │░░ ░  ░░ │ │░ ░░          │
                      │    ──┘ └─┘  ──     └───────     ────     ─┘─┘──┘─┘──┘─┘─┘─────────┘─┘──────────────┘
                      │          │                  ──       ┌──
                      │  ░  ░░ ░░░  ░ ──────   ░ ─┐░░░│      │░░░      ░         ─┐
                      └───────────            ─── └───┘   ───┘───      •          │
                                  ┌─┐─┐──────┐         ───        ────                 ──
                            │   │ │░│ │░░░░░░│        │░░        │░ ░░░─────┐░░──────┐   │
                            │ │ └┐┘─┘─┘──────┘────────┘──────────┘────  ░ ░░│▒ ░░░░░▒│   │
                            │ │  │                                    ──────┘────────┘   │
                            │ │  └───┐            ┌─┐    ┌─┐     ┌─┐                   │ │
                            │ │  │░░░│   ──┐─     │ │    │ └┐   ┌┘░│   ┌─┐   ┌───      │ │
                            │ │  │░░│   •░░│      └─┘    │ └┘   │ ░│   │▒└─  │░        │ │
                            │ │  │░░│    ──┘─    •░░░│   │░└┘   │░     │░│    ──       │ │
                            │ │  │░─┘             │░░│   │░░│   │ ░░   │░│             │ │
                            │ │  │░░│             │░│    │░─┘    ┌─┐─  └─┘             │ │
                            │ │  │░░│    ──       │░│            │ │                   │ │
                            │ │  │░░░•   ░░       └─┘    •         │                   │ │
                            │ │  │░ │                     •      ──┘                   │ │
                            │ │  └──┘                                                  │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │    ─── ──────┐                                         │ │
                            │ │  ──░░░│ ░░ ░░│                                         │ │
                            │ │ │   ──┘    ──┘            ───────      •               │ │
                            │ │ │        •   └─ •     ──         •      ─┐─┐  ──       │ │
                            │ │   ───  ──░─┐   │░──  •░░──┐ ┌──── ─┐──┐  │░└┐   ──────┐┘ │
                            │  • •░░░   ░ ░│   │░░░  ░░•░░│ │░░░   │░░└─  ░└┘     ░░░░│  │
                            │       ──    ─┘             ─┘ │   ── │                ──┘ ─┘
                             ── ──           •        │      ┌──    ┌─ │ │ ─┐ │ │ ┌─  └─
                               • ░ │ ░│ │ │ │░ │ │ ░│ │░│    │░ │ │ │░ │ │ ░│ │ │░│▒ ░│
                                ───┘ ─┘─┘─┘─┘──┘─┘──┘─┘─┘────┘──┘─┘─┘──┘─┘──┘─┘─┘─┘───┘
                                    •











```

*Figure from page 5 (2346x3317 px)*


---



4203-E P-216



SECTION 2 PROGRAM OPERATION



[Supplement] If the same file as the one selected for large-capacity program operation {method B,



method S, method M) is edited while the selected program is not executed, program



selection is canceled.



5-2-2. Readout of a Program File from the Memory Using Wild Card{"*","*·*")



(1) Key in "E



or «E



*·*"



and press the WRITE key.



(2) The list of names of stored files is displayed on the screen. Move the cursor to the required file



name using the cursor and page keys, then press the WRITE key.



[Supplement]


#### AUTO OPERATION A.MIN

PROGRAM SELECT INDEX



MAIN PAOGRi\M FILE



JW,MIN



B.MIN



O.MlN



KS.MIN



K51.MIN


#### ABCO.MIN

K52.MIN



K53.MIN



P03.MIN



POO.MlN



=PS B



=What is the fl le name tor program select?



PROGRAM ACTUAL PART i BLOCK



SELECT POS l T. PROG!AM



DATA



SEARCH



01 NGm 11



97/07/15 14:10:00



1mm



PAGE 1



CHECK


#### DATA [EXTEttl]


## 1. An asterisk (*) is displayed at the beginning of the file name of the file that has been

created or edited last.



When the PROGRAM EDIT INDEX screen is displayed, the cursor is positioned on



the file name prefixed by an asterisk.


## 2. When there is no file where asterisk should be set, the first page of the PROGRAM

EDIT INDEX screen ls displayed with the cursor at the top of the file names.


## 3. If the same file as the one selected for large-capacity program operation (method

B, method S, method M) is edited while the selected program is not executed,



program selection is canceled.


```text


                                                                                                ───
                                                                         ┌──┐─────────┐───────── ░░────────┐
                                                                         │░░│ ░░░░ ░  │░░░░░░░░░───░░░░░░░░│
           ┌────             ───              •     ──  •          •      ──┘   ───   └────────      •
           │     ───────────┐   ┌──┐────────── ────┐  ── ┌────────┐ ──────   ──┐   ───                     │
           └────┐░    ░  ░ ░│ ──┘░ │░              │     │        │            │                           │
                └───────────┘   │  │        • •    │    ─┘        └─  ┌──── │  └────  ░  •       ──     ───┘
                                 │ ░  ░     ░░░░• ░│ ░ ░░░░│ │░░░ ░ ░ │░░░░░│ │░░░ ░────░░  ░░░  ░░ •░░░░░░│
                                 └──────────────░──┘   ────┘ └───  ── └─────┘─┘─────    ──────────── ──────┘
          ┌─────┐  ┌─────────┐──                    ─┐─     •    ──  •
          │░ ░ ░│  │░░░░░░░ ░│ ░░  ░░• ░░░ ░ ░░ ░░ │░│░ ░  │░░   ░░░ ░░░  ░         │
          └─────┘ │ ┌─┐  ┌───  ──┐──┐ ┌─────       └─┘┐─  ─┘      ──────────────────┘
                  │ │ │░░│   ░   │  │░│              ░│ •░░░
                  │ │ │ ─┘           │                       •    │
                    │ │░   ──    ──  │   ──                ──   │ │ ── •   ┌──  ──────────────────────────┐
                  ──┘ └───   • ──     • •  ┌─┐   ──  •     ░  ──┘  │    ───┘   │              ░  ░░   ░ ░░│
                      │░░░░  ░░░░─────░•░──┘░└───░░──░────────░░░──┘────░░ ░───┘──────────────────────────┘
                      └─────────
                                  ───────────          ────            ──   ────     ─┐  •
                            │  •  ░░░ ░░░░ ░▒───────── ░░░░ ──────────┐░░   ░░░░───┐─░│   │
                            │ │   ───────────            •            └─░░░░────░░░│░ │ │ │
                            │ │               •░   │        ─┐          ────    ───┘──  │ │
                            │ │   ┌────░░░░    ────┘───── ── │                          │ │
                            │  ┌──┘░░░░ ────                                ───         │ │
                            │  │░░│░░░┌─            │                                   │ │
                            │  └──░░░░│  ───────────┘                                   │ │
                            │ │   •░░░└┐                                                │ │
                            │ │  •▒░░░░│                                                │ │
                            │ │   •░ ▒─┘                                                │ │
                            │ │  •░░ ░ │                                                │ │
                            │ │   │░ ▒│                                                 │ │
                            │ │   └───┘─                                                │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │  ┌──                                                    │ │
                            │ │ ┌┘░ ─┐ ─┐── ─┐────────┐──────┐───┐──┐── •     ── ────── │ │
                            │ │ │░░░░│  │░░│ │░ ░░    │░░░ ░ │  ░│  │  │ ─┐──┐  •       │ │
                            │ │ │░░░░░  │░░│ │░░░ •   ░░─┐─┐     └─    │  │░░│   ┌┐───┐─
                            │   └──░──  │░ │ └┐──░░│ │░ ░│ │░░░░░│     │  │░─┘  ┌┘┘ ░░│  │
                             ── │  │  ─┐   └─ │   ─┘ │   └─┘    • ┌──┐─ •      ─┘    ─┘ ─┘
                               •░ ░│ ░ │░ │  ░ ░      │░   ░ │░ ░ │ ░│ │ ░ ░░ ░ │ ░░ ░│
                                ───┘───┘──┘───────────┘──────┘────┘──┘─┘────────┘─────

                ────────────┐              ───         ────┐────┐─┐──┐─────────────┐─┐──────┐─┐──┐─┐─┐─────┐
                  ░░░ ░ ░░ ░│       │ ────░ ░░────────░ ░░░│ ░ ░│ │░░│░░░░   ░░ ░░ │░│  ░ ░ │░│ ░│░│ │░░░░░│
                 ───────────┘       └─░░░░─── ░░░░  ░░──  ─┘─      ──┘  ──          •   ──   ─┘──    └─  ──┘
                                    │                   •     ─────   ──  ──┐──────┐ ─┐─  ───    ────  ─┐  │
                                    └─░░░ ░░•░░░░░░░░░░░░░░──░░░░░░│░░░░│ ░ │░░░░░░│ ░│░ ░ ░░ ░│░░░░░ ░░│ ░│
                                    │░┌─────░──────────────░ ──░───┘────┘───┘──────┘──┘────────┘────────┘──┘
                                ┌─  │ │
                                │   └─┘───────┐──────┐──────────┐─░ • •    •            ┌─── •    ░░     ░
                                └─  │   ░     │      │          │           •           │░             ─────
                                    └─────────┘    ──┘ ─────┐───┘ ─────── ──░────────┐──┘─────── ░░░───
                                ┌─  │                       │                        │                  •
                                │   └─░░─────────┐──────────┘─────┐ ┌─── ░• ░░░──── ░│░░─── ░░░░░░░ ── ░░•░░
                                └─  │░ ░ ░░░░  ░ │░░░░░ ░░  ░ ░░░░└─┘░░░──░░───░░░░──░──░ ░────────░░░───░──
                                    └─    ───    ░ ────┐── ░░  ───   ───        •       ───        ───   •
                                      ────   ──────    │  ─────























```

*Figure from page 6 (2346x3317 px)*


---



5-2-3. Cursor Operations



4203-E P-217



SECTION 2 PROGRAM OPERATION



When the cursor key is pressed, the edit pointer and the edit line can be moved.



(1) Cursor Right Movement



Each time the cursor key is pressed, the edit pointer (reversed display) moves to the right.



The edit pointer moves continuously while the cursor key is held down.



PROG OPERATION



>::©11000



N100 GOO



N101 G56



N103 G41G01



N104 G03



N105



N106



Nl07 G01



N108 G40



N109 GOO



NllO



Nl 11



=E WHEELlOO.MIN



ti le end



EDIT



X300 Y300



X400 Y200



xsoo



Y300



XlOO Y300



X200 Y200



X400



X300 Y200


#### P MODE WHEEL100.MIN

97/07/15 14:10:00



S250



Z-55 M09 M03



F100 Dl 1



10 J100



1-200 JO



1100 JO



2100



LI NE LI NE CHAR. CHAR. LI NE EDIT



INSERT DELETE INSERT DELETE DELETE EAASE OUIT [EXTEND]



(2) Cursor Left Movement



Each time the cursor key is pressed, the edit pointer (reversed display) moves to the left.



The edit pointer moves continuously while the cursor key is held down.


```text


                                                                                                ──
                                                                         ┌──┐───┐─┐───┐─────────░░───────────
                                                                         │░░│░░░│░│   │░░░░░░░░░ •░░ ░░░░░░░
                 ──      •          ─────────────────────────────────────┘──┘───┘─┘─  └─────────     ──    •
           ┌─────   ───── ─────────                                                                         │
           │   ░           ░        │        •                                         ─────────────────────┘
           └──── ─────  │           └───────┐ ───────────────────────────── ───────────
                │░░░░  ░│    ░░ ░   ░ ░     │   ░ ░      ░  ░   ░    ░ ░ ░
                └───┐─┐─┘                 ──┼───────────────────────────────────────────
                    │ │      │░    ░        │
                  ──┘ └──────┘──────────────
                                                          ─┐─
                                                    ┌───── │░──┐
                                                    │░  ░  │  ░│
                                                    │    • │   │
                                                     │    ─┼─ ░│
                                                     │░░•  │░░│
                                                      ── ──┘──┘

                      ┌──┐────┐─────┐─────┐───┐──────────┐─┐─┐─────┐─┐───────┐─┐────┐─┐─────────┐─┐───┐
                      │ ░│░ ░ │ ░ ░ │░░   │░  │░░░░░░░  ░│ │░│  ░░░│ │░░░░░░░│ │░░░░│ │░░░░░ ░ ░│ │░░░│
                      └┐ │ │ ─┘   ─┐ │   • • ─┘  •         └─ │   • │ │ ┌─── │  │ ──┼─┘─────────┘─┘───┘
                       │ ░ │░  ░░░░│ │░░░░• •░ ░│░░░░│ ░░ ░   │ ░░ ░│ │░│ ░ •░• │░░░│
                       └───┘─────             ──┘────┘       ─┘                        ──
                                  ────────────         ───        ──────────┐─┐───────┐  •
                            │  ── ░░░ ░░░░ ░░ ──────── ░░░────────░ ▒░▒     │▒│░░▒░░░▒│   │
                            │ │  │    ────────         ───         ─────░ ░─┘─┘───────┘ │ │
                            │ │  └───┐            ┌──┐    ──┐     •                     │ │
                            │ │  │░░░│   ┌─┐      │░░│   │░░│    •░•          ┌─┐       │ │
                            │ │  │░░░│   │░└──    │  │   │  │   │░ ░│   ┌─┐   │░│       │ │
                            │ │  │░░░│   │░░░     └──┘   └──┘   │░░░│   │░│   └─┘       │ │
                            │ │  │░░░│   └─┐──    │░░│   │░░│   │   │  • ░│             │ │
                            │ │  │░░░│     │      │░░│   └──┘    │░┌┘   ──┘             │ │
                            │ │  │░░░│   ┌─┘      │░░│   │  │    └─┘                    │ │
                            │ │   •░░│   │░│      └──┘   │░░│   ┌┘  │                   │ │
                            │ │  •░░░│   └─┘             └──┘   │  ░│                   │ │
                            │ │   ───┘                           ───┘                   │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │  ───────────┐                                           │ │
                            │ │ │░ ░░░░     │                                           │ │
                            │ │ │             •     •      •     •     ──     ──        │ │
                            │ │   ───   ┌────  ───┐─ ────┐─ ────┐ ┌─┐─┐   ──┐   • ────┐ │ │
                            │ └─ │░░  • │░    •░░░│   ░░░│      │ │░│░│ • ░ │  • │    │   │
                            │    │             │  │  │   │      │ │    • │   •   │   ░│  •
                             ──┐─┘   │ │  │ ─┐─┘   ──┘     • ┌─      •  ┌┘    ──┐     └──
                               │░  │ │ │  │ ░│ ░ │ ░  ░ ░ │░ │░│    │░│ │░ ░│ ░ │ │░ ░│
                                ───┘─┘─┘──┘ ─┘───┘────────┘──┘─┘┐───┘─┘─┘─ ─┘───┘─┘───┘
                               │           •                    │         •
                  ──  ┌────┐───┘ ┌────────
                      │    │    ─┘
                       ──── ───    ──────              •
                                                    ┌── ┌──────┐
                                                    │░  │  ░  ░│
                                                    │░ ░│ │    │
                                                    │░ ─┘ │   ░│
                                                    └─░░│   ░ │
                                                      ──┘─────┘

                      ┌────┐──┐─┐──┐───┐───┐───┐─────┐  ───┐─┐─────┐─┐──────────────┐─────┐───────┐─┐
                      │░░░ │░░│ │░ │░ ░│ ░░│ ░ │░░░░░│ │░░ │░│ ░░░░│ │░░░░░░░ ░░░░░░│ ░ ░░│ ░ ░░░ │░│
                      │    │      • ─┐ └─ ─┘ ──      │ │     │     │ │  ───┐  ┌─┐   └─────┘───────┘─┘
                      │ ░  │░ ░░░ ░│ │░░░░    ░░░ ░ ░│ │ ░│ │░    ░│  ░│ ░ │░░│ │░░░│
                       ────┘───────┘─┘───────────────┘─┘──┘─┘──────┘───┘───┘──┘─┘───┘

















```

*Figure from page 7 (2346x3317 px)*


---



PF03 OPERATION



»010®



N100 GOO



N101 G56



N103 G41G01



N104 G03



N105



N106



N107 GOJ



N108 G40



N109 GOO



N110



N111



e:E WHEEL! 00. MIN



file end



EDIT



X300 Y300



X400 Y200



X500 Y300



XlOO Y300



X200 Y200



X400



P MODE



X300 Y200



S250



Z-55



FlOO



1-200



1100



Z100



4203-E P-218



SECTION 2 PROGRAM OPERATION



l'IHEEL100.MIN



97/07/15 14:10:00



M09 M03



011



J100



LINE LINE CHAR. CHAR. LlNE EDIT



INSERT DELETE INSERT DELETE DELETE ERASE QUIT [EXIDOJ



@ @J@J@ @J @J@J @J



(3) Cursor Downward Movement



Each time the cursor key is pressed, the edrt pointer (reversed display) and the edit line (>>) move



down one line.



The edit pointer and the edit line move continuously while the cursor key is held down.



When the cursor key is pressed with the edit line (>>) placed atthe bottom, the edit line(>>) moves



to the next block (the first line in the next page).



PF03 OPERATION



>~000



N100 GOO



N101 G56



N103 G41G01



N104 003



N105



N106



N107 GOl



N108 G40



N109 GOO



N110



N111



=E WHEELJOO.MIN



file end



EDIT



X300 Y300



X400 Y200



X500 Y300



X100 Y300



X200 Y200



X400



X300 Y200


#### P WOE WHEEL100. MIN

97/07/15 14:1



:oo



S250



Z-55 M09 M03



F100 D11



10 JlOO



1-200 JO



1100 JO



Z100



LI NE LI NE CHAR. CHAR. LI NE ED IT



INSERT DELETE INSERT DELETE DELETE ERASE OUIT [EXTEND]


```text


                                                                                               ┌──
                                                                         ┌──┐────┐─┐─┐─────────┘░░░────────┐
                                                                         │░░│ ░░░│ │ │░░░░░░░░░░───░░░░░ ░░│
           ┌───────────────────────────────────────────────────────────── ──┘────┘─┘ └─────────
           │
           └─────────────────
                                  ───────────         ─── ░        ─────   ───────────
                            │ ┌── ░░▒ ░░░░░░░───────── ░░░───────── ▒░░ ─── ▒▒░░░░░▒░░   │
                            │ │        ─── ──          ──          ────░░░░░──────────   │
                            │ │  ┌───┐            ┌──     ──┐          •  ──             │
                            │ │  │░░░│   ──┐      │░░•   │░░│   ┌──┐    │     ──       │ │
                            └─┘  │░░ │  •░░└──    │ │    │  │   │ ░│   ┌┘─   │░░│      │ │
                            │ │  │░░•    │░░░     └─┘    └──┘   │ ─┘   │░ │  └──┘      │ │
                            │ │  │░░░•   └─┐──   │░░░│   │░░│   │  └┐  │░░│            │ │
                            │ │  │▒░│   •  │     │░░░│   └──┘   └┐░░│  │░┌┘            │ │
                            │ │  │░░│    ──┘     │░░░│   │  │    └──┘  └─┘             │ │
                            │ │  │░░░│  •░░│     └───    │░░│   │                      │ │
                            │ │  │░░░│   ──┘             └──┘   │ ░│                   │ │
                            │ │  │░ │                           └──┘                   │ │
                            │ │  └──┘                                                  │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │   ──── ─────┐                                          │ │
                            │ │  • ░░░│ ░░ ░│                                          │ │
                            │ │ │  ──░│ •  • •           ───────       •     ───┐───── │ │
                            │ │ │        •    ─┐─     ──┐       ┌──     ─────   │      │ │
                            │ │   ──┐   •░─┐   │░──  │░░└─   ───┘  ┌──┐   ░  ── └┐────┐┘ │
                            │    •░░│   ░ ░└─  │░░░  │░•░░• │░░    │░░│  ┌──┐   └┘░░░░│  │
                                •                           │            │  └─  │    ─┘ •
                                ░ ░░    ░░░    ░░░    ░░   ░ ░░ ░ ░ ░░ ░ │ ░░ ░ │  ░  │
                                ──── ──────────────────────░──────────── │ ──── └─────┘
                                                           •            • •    •
                 ───┐ ┌────┐───── ───┐─┐────────
                   ░│ │  ░░│ ░░░░ ░░░│ │░░░░ ░░░│
                 ───  └────┘─────────┘─┘────────┘
                                                    ┌───┐─┐───┐
                                                    │ ░ │ │  ░└─┐
                                                    │   │ │  ░│ │
                                                    │  ░└─┘ ░
                                                    │   │ ░   ──
                                                     ───┼─ ───
                       ──     ───  ────┐─┐─┐─┐──────┐   │ │    ───┐─┐──────┐──────┐────┐────┐──┐─┐─────────┐
                      │ ░•   •░ ░│ ░░ ░│ │░│ │░░░░░░│  ░│ │░  ░  ░│ │░ ░░░░│ ░░░░░│  ░ │░ ░ │░ │░│     ░░░ │
                      │░•░░──░───┘─    │   │   •  ──┘  ─┘ └─    •      ───  ──────┘   ─┘─   └─ └─┼─────────┘
                      │            ─┐── ──┐ ┌─┐ ┌─   ──  │  ──── ┌──┐─┐   ─┐       ┌─┐   ┌─┐  •  │
                      │ • ░░░ ░░ ░░░│░░░ ░│ │░│ │░ ░░ ░│ │░░░ ░░ │░ │░│░ ░░│ ░  ░│ │░│ ░ │░│ •░░░│
                      │  │           │      │       •  │        ─┘─ │ │     ──┐  └┐┘ │  • ─┼─    └────┐────┐
                      │ ░└┐ ┌────────┼─┐────░──░──░ ░─┐┘──░░── ░   │░░░ ░  ░ ░│ ░ │░░│ │░░ │░│ ░│ ░ ░ │░░░░│
                      └──░│ │░░ ░░░░ │░│ ░ ░•░ • ░─── │░░░──░░─────┘──────────┘───┘──┘─┘───┘─┘──┘─────┘────┘
                         ─┘─    •
                                  ───────░──┐         ┌─          ──────  ─┐──┐──────┐   │
                            │ │ ──░░░ ░░░• ░│         │░  ──────── ░░▒░    │▒▒│░░░░▒▒│   │
                            │ │        ──  ─┘          ──          ─────  ─┘──┘──────┘   │
                            │ │  ┌───            ┌──┐    ┌──     •                     │ │
                           │ │   │░░ •  ┌──┐     │░░│    │░░•   •░─┐    •     ─┐       │ │
                           │ │   │░░│   │░░│ •   │  │      │   •░ ░│   │░┌─  │░│       │ │
                             │   │░░│   └┐┐┘     └──┘    ┌─┘    │░░│   │░│   └─┘─      │ │
                           │ │   │░░│    └┘ ──   │░░│    │░░•   │  │   │░│             │ │
                           │ │   │░─┘   │        │░░│    └──    └┐░│   │░│             │ │
                           │ │   │  │   └──      │░░│    │  │    └─┘   └─┘             │ │
                           │ │   │░─┘   │░░•     └──┘    │░░│  │   │                   │ │
                           │ │   │░░│   └──              └──┘  │  ░│                   │ │
                           │ │   │░─┘                          └───┘                   │ │
                           │ │   └─                                                    │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │  ┌───────────┐                                          │ │
                           └─┘  │░ ░░░░ ░ ░ │                                          │ │
                           │░│  │   ───┐   •             ──┐────             ─── ───── │ │
                           │ │    •    └───   ┌──┐── ┌──┐  │    ─┐─ ─┐  ┌────   •      │ │
                           │    • ░┌─ │  ░    │░░│   │░░│   ┌──  │ • │  │ ░   │  ┌─────┘ │
                            •    ┌─┘  │ ───   └──┘   └──┘  ┌┘    │ ░░│   ┌─   │ ─┘░░░░   │
                             ──  │                • •      │      •      │  ──┘  │  ──┐──
                                 ░░     ░░ ░ ░ ░░ ░ ░ ░░ ░ ░░░░   ░░░░    ░░░    ░░░  │
                               ──────────────────── ──────────────────────────────────
                                                   •






```

*Figure from page 8 (2346x3317 px)*


---



4203-E P-219



SECTION 2 PROGRAM OPERATION



(4) Cursor Upward Movement



Each time the cursor key is pressed, the edit pointer (reversed display) and the edit line (>>) move



up one line.



The edit pointer and the edit line move continuously while the cursor key is held down.



When the cursor key is pressed with the edit line (>>) placed at the top (01000 on the display



screen), the edit line(>>) does not move.



[Supplement]



PROO OPERATION



»01000



N100 GOO



N101 G56



N103 G41G01



N104 G03



mos



N106



N107 GOI



N108 G40



N109 GOO



N110



Nlll



,:E;



WHEELlOO.MIN



file end



X300



X400



X500



XlOO



X200



X400



X300



EDIT



P MOOE



Y300 S250



Z-55



Y200 F100



Y300 10



Y300 1-200



Y200 1100



Y200



2100



LI NE LI NE CHAR. CHAR.



LI NE



WHEEL100. MIN



97/07/15 14:10:00



INSERT DELETE INSERT DELETE DELETE ERASE



M09



D11



JlOO



EDIT



QUIT



M03



[EXTEND]


# CED

® CED



@ @J @J @


## 1. When the cursor key is pressed continuously or held down until the edit pointer

(reversed display) reaches the left-end or right-end position, the edit line (>>)



moves up or down, respectively.


## 2. The edit pointer (reversed display) is placed on the edit line(>>). This means that

the edit line and the edit pointer move together. The edit pointer moves as the edit



line changes.


```text


                                                                                               ┌───
                                                                         ┌──┐──────┐──┐───┐────┘░░░─────── ┌┐
                                                                         │░░│░░░░░░│  │░░░│░░░░░───░░░░░░░─┘┘
           ┌──────   ──                       ─────────────────────────── ──┘──────┘──┘───┘─────     ──
           │      ┌─┐  ───────────────────────                                                              │
           └───── │░└─┐         ░    ░░    ░ ░──────────────────────────────────────────────────────────────┘
                  └─┘ └───────────────────────
                                                       ──   •
                                                    ─┐─░░───░──
                                                   • │░ ░     ░│
                                                     │         │
                                                     │  ░     ░│
                                                    ─┘░░──── ──
                                                      ──    •

                        ───    ──┐─────┐─┐─┐─────────┐─┐───┐───────┐─┐──────┐─┐────┐─┐────┐─┐─┐─────────────┐
                        ░░░ ░── ░│    ░│ │░│ ░ ░░░░░░│ │░  │░ ░░░ ░│ │░ ░ ░░│ │░░░░│ │░░░░│ │░│  ░      ░░░░│
                       ──────░░──┘     │  ─┘   •   ──┘ └─  │  ────          └─┘────┘ └────┘ └─┘   ──────────┘
                      │           ─┐─┐─ ─┐  ─── ──┐   •  ── ──    ─┐─┐──┐──┐        •      •   ───
                      │░░│ ░░░ ░░░░│ │░  │░ ░░░ ░░│  ░░• ░░ ░░ ░░ ░│ │░░│ ░│   ░░░ •░• ░ ░░░• ░ ░░•
                      │  │                        │         │  ─┐  │ └── •  ─┐ • ─┐ • │      • ─── ─┐─┐─────┐
                       │░░── ░░──░ ────░┌── ░░░░░░░──░───░│ │░│ │ │ │   │░░░░│ ░│░│░ ░│ │░░│░░│ ░ │░│ │░░░░░│
                      ─┘──░░───░░•░░░  ─┘  ────────░░•░░░─┘─┘─┘─┘─┘─┘───┘────┘──┘─┘───┘─┘──┘──┘───┘─┘─┘─────┘
                               •
                                 ─┐─┐─┐──┐───┐        ┌──┐─  ────┐─┐───    ┌────── ──  ──┐
                            │     │░│ │░▒│░░▒│        │░░│       │░│▒░░────┘▒░░ ░░•░░│   │
                            │ │ ──┘─┘ └──┘───┘────────┘──┘──   ──┘─┘──░ ░░░░── ░░░░░░└── │
                            │ │                             ───       ──────  ───────   │ │
                            │ │  ┌───┐   ┌─       │ │      •     ┌─┐                    │ │
                            │ │  │░░░│   │░──┐    └─┘    │  │   ┌┘░│   ┌──    │ │       │ │
                            │ │  │░░░│  •░░░░│    │░│    │░░│   │░─┘   │░░│   └─┘       │ │
                            │ │  │░░░│   ────┘    │░░│   │░░│   │       •░│             │ │
                            │ │  │▒░░│            │░░│   │░░│     ░░│  │  │             │ │
                            │ │  │░░▒│            │░│    │░░│   ┌──┐┘  │░•              │ │
                            │ │  │░░░│   │░       │░│    │  │   │  │                   │ │
                            │ │  │░░░│   │░       └─┘           │  │                   │ │
                            │ │  │░░│                           └──┘                   │ │
                            │ │  └──┘                                                  │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │    ─── ─────┐                                          │ │
                            │ │  ──░░░│  ░ ░│                                          │ │
                            │ │ │  ░──┘ •  ─┘             ────────             ─────── │ │
                            │ │ │            ──       ┌─          •    ─── •  │        │ │
                            │ │   ───   ─────  ───┐  ─┘░──  ─────┐ ┌──┐ ░ │░  │ ─┐────┐┘ │
                            │  ─┐ ░░░   ░░░░   ░░▒│   ░•░░  ░░ ░░│ │░░│   │   │  │░ ░░│  │
                             ── │      │             •      •                •       ─┘ ─┘
                                │ ░░   │  ░    ░ ░    │ │    ░░     ░░     ░░ │ │ │░  │
                                │  • ░ │  ░ •  ░ │ ── │ │ ── ─── •░ •░   ░ ░┌─┘ │ │░ ─┘
                                └── •   ───  ────┘     ─┘─           •     ─┘   │  ──
                ┌───────────┐         ──          │ ──     ──          ──── │    •    ──  ──────┐ ┌─┐──────┐
                │░░░░░░░░░ ░│       ┌─░░────┐─┐───┘─░░───── ░░░─┐ ┌─ ░•░░░░░░───┐░░░─┐░░──  ░░ ░└─┘░│ ░░░░░│
                └───────────┘       │ ░ ░  ░│ │░ ░   •       ──░│ │░── ─────    └──  └─    ─┐░┌─   •   ────┘
                                    │       │ │ ░   │ │  │      │  •        ────    •  ──── └─┘ ──   ──
                                    │      ─┘  ─────┘ └──┘────
                                ┌── │                            •   ───     • • ───                ───
                                │   └───────────░──┐░ ░•░░──┐░░░░░───░░░────░ ░ • ░░───────────── ░ ░░░░ ░─┐
                                └─  │░░ ░░░  ░ ░ ░ └───░░•░ └────░░ ░ ──░░░░────░───░ ░░░░░░ ░░░░░────────░│
                                    └──────    ┌─ •    ──  •      ───   ────        ──  ─── ──────
                                           ────┘






















```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-220



SECTION 2 PROGRAM OPERATION



[Supplement) 3. If there is a record exceeding 63 characters {one block of data is not displayed



within one line) and if the edit data cannot be displayed within the display area (16



lines), a blank line is automatically generated. The symbol of"@" is displayed on



the automatically generated blank line so that it is distinguished from the line



generated by the "one-line insertion" function.



In this processing, a blank line is generated only at the bottom of the screen and not



generated at a middle or the top of the screen.


#### PROG OPERATION EDIT P MODE WHEEL100.MIN

97/07/15 14:10:00



»N098 GOO XlOO YO



N099 000 X200 YlOO


#### NlOO GOO X300 ¥300 $250


#### N101 656 Z-55 M09 M03

N103 641601 X400 Y200 F100 D11



N104 G03 X500 Y300 10 J100



N105 XlOO Y300 1-200 JO



N106 X200 ¥200 1100 JD


#### N107 GOI X400

N108 G40 X300 Y200



N109 GOO 2100



N110 X200



Nlll YlOO



N112 001



x,oo



¥200



N11m X200 Y300



=E WHEEL100. MIN



file end



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELETE INSERT DELETE DELE1E ERASE QUIT [EXTEND]



@@@J@@J@@J@)



The cursor is moved.


#### PROO OPERATlON EDIT p f.llDE WHEEL100. MI N

97/07/15 1 :1



:oo



»N099 GOO X200 Y100



NlOO GOO X300 Y300 S250



N101 G56 Z-55 r.t:l9 U03



N103 G41G01 X400 Y200 FlOO D11



N104 G03



xsoo



Y300 10 J100



N105 X100 Y300 1-200 JO



N106 X200 Y200 1100 JO



N107 001 X400



Nl08 640 X300 Y200



N109 GOO 2100



Nl10 X200



N111 YlOO



Nl12 001 XlOO Y200



N113 X200 Y300



Nl llil GOO X300 Y200



&2400



"E WHEEL100.MIN



file end



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELE1E INSERT DELETE DELETE ERASE OUIT [EXTEND]


```text


                                                                                              ┌──        •
                                                                        ┌──────┐──┐──┐────────┘░░•░─────░░│
                                                                        │░░░░░ │░░│  │░░░░░░░░░──░•░░░░░ ─┘
          ┌─────            ───┐ ────         •      ──                  ───── └──    ─────────     ───
          │     ────────────   └─    ─┐─────── ┌─────  ────────┐─┐───────     •   ────                     │
          └────  ░   ░ ░     ──┘ ┌─┐░ │        │               │ │             │         │         │       │
                ─────────────  └─┘ │           │      │                     ───┘───   ───┘──┐───── │  ──┐──┘
                                    ────┐─┐────░─── ░─┘──────────┐────░░─── ░░░░░░░░──░░░ ░ │ ░░░░─┘░ ░░│ ░│
                                   •░░░░│ │ ░░ ░ ░░░ ░ ░░░░░░░░░░│ ░░░░ ░░░░ ─────░ ░░░•░░•░░ ┌─┐░░░░░░• ░┌┘
                                    ────  └┐──── ─┐ │ ───────────┼─────────░ ░    ─── │    ── │ └──── │ │ └┘
                                   │       │    ░ │ │           ░│          ──       ─┘────  ─┘ │    ─┘ └─┘
                                   │░  ░ ──░•   ──┼─┘ ░   ░  ░░░─┘      ░░░                                │
                                   │              │                         ───────────────────────────────┘
                                    │   ────      ░──           ░        ── ░    ░               ░░  ░     │
                                   ─┘░ ░░░░░───────░░─────────────────── ░░────────────     ── ────────────
                                    └───────                                           •
                                               ────────────         ───        ───────  ─┐─────────┐  •
                                         │  •  ░▒░ ░░▒░░ ▒░ ─────── ░░░─┐──────░ ▒▒▒░    │▒▒░ ░░░░░│   │
                                         │ │       ───   ──         ──  │      ─────┐░  ─┘─────────┘   │
                                         │ │  ┌───┐    ─┐      ┌──┐    ─┘           └───             │ │
                                         │ │  │░░░│   │░│      │░░│   •░░│     •                     │ │
                                         │ │  │░ ░│   │░│      └──┘    │░│    │░─┐    •    ┌─┐─      │ │
                                         │ │   •░░│   │░│      │  │    │ │    │ ░│   │░─┐  │░│       │ │
                                         │ │  │░░░│   │▒│░     └──┘    └─┘    │░░│   │ ░│  └─┘─      │░│
                                         │ │  │░░░│   └─┘─     │░░│    │▒│    │  │   │░┌┘            │ │
                                         │ │  │░░░│            │░░│    └─┘    └─░│   └─┘             │░│
                                         │ │  │░░░│   ┌─┐      │░░│    │ │      ─┘                   │ │
                                         │ │  │░░░│   │░│      │░░│   •░░│    •  │                   │ │
                                         │ │  │░░░│   └─┘      │  │              │                   │ │
                                         │ │  │░ ░│   │ │      │  │    ┌─┐    ───┘                   │ │
                                         │ │  │░ ░│   │░│        ░│    │░│                           │ │
                                         │ │  │░│░│    •       ─┐░│    └─┘                           │ │
                                         │ │  │░│  ─┐─  ─┐─     └─                                   │ │
                                         │ │  └─ ░░░│   ░│                                           │ │
                                         │ │ │    ──┘      •     •      • ──         •     •         │ │
                                         │ │ │ ──     ──┐─  ┌──┐─ ─┐──┐─ •    ───┐─   ┌──── ──       │ │
                                         │ └─ │ ░░│ │ ░░│   │░░│   │░░│          │░•  │ ░      ────┐ │ │
                                              │  ┌┘ │ ░ │ • └─░│  │░──   ┌────  │░░░• └┐░ │   │░░ ░│   │
                                          ── ─┘  │ ─┘    │ │   │ ─┘   •  │      │  │ ─┘┘  └───┘   ─┘┐──
                                            │░ ░│   ░ │  │ │ ░│ ░ │  ░ ░ │ ░│ ░ │ ░│ ░  ░   ░  │░│  │
                                            └───┘  ── └─ └─┘──┘ ──┘──── • ──┘ ──┘──┘ ──────────┘─┘──┘
                                                 ──  •  •      •       │ │          •
                                                                 ┌─────┘─┘ ┌───┐
                                                                 │   ░   │ │  ░│
                                                                 └─────┐ └─┘───┘
                                                                •      └─┘
                                           ───         •   ─────  • ───┘ └────       ──             ──
                                         │      ───────  │         │            ─────  ──┐─┐──────┐   │
                                         │ ┌─┐ •░░ ░░░░──┼────     │░─── ──────░░▒░░    ░│▒│░░░░▒░│   │
                                         │ │ │    ───    │          •           ─────  ──┘─┘──────┘  ░│
                                         │ │  ┌──┐   ┌──       ┌─┐    ───     ──                    │ │
                                         └─┘  │░░│   │░░│      │░│     ░░    •░░│    │    ┌──┐      │ │
                                         │ │  │░░│   │░░│     •  │    │ │   •  ░│   ┌┘┐   │░░│      │ │
                                         │ │  │░░│    │░░      ──┘    └─┘┐   │░░│   │░│   └──┘      │ │
                                         │ │  │░░│    └───    │░░│    │░░│   │  │   │░│             │ │
                                         │ │  │░─┘            │░░│    └──┘   └─░│   └─┘             │ │
                                         │ │  │░ │   ┌──┐     │░░│    │        ─┘     │             │ │
                                         │ │  │░░│   │░░│      ──┘    │░░│  ┌─  │                   │ │
                                         │ │  │░░░│  └──┘        │       │  │  ░│                   │ │
                                         │ │  │░──┘  │  │     •  │    ┌─┐    ───┘                   │ │
                                         │ │  │░  │  │ │       ──┘    │░│                           │ │
                                         │ │  │░ ─┘  └─┘      │░░│    │░░│                          │░│
                                         │ │  │░•░│  │░░│     └──┘    └──┘                          │ │
                                         │ │  │░░░└┐─┘──┘─┐                                         │ │
                                         │ │  └───░│     ░│                                         │ │
                                         │ │ •    ─┘            •      ───    •                     │ │
                                         │ │  ┌──   ────┐ ──┐──┐  ───┐─     ── ─┐──┐ ─────        │ │ │
                                         │ │  │░░│     ░│   │░░│  ░░░│    ──    │░░│   ░       ───┘┐  │
                                         │   │  ─┘  │   │   └──┘  • ─┘   •   │  │ ─┘  ┌─     ┌─   ░│  │
                                           • │      │      •    ──      •    │ │    │ │  │ ──┘     └─
                                            │   • ░  │ │  ░ │    ░ │░ │ ░ │░ │ │ ░│ │ ░ ░│ ░ │  │ ░│
                                            └─ •  ── │░│ ── └─ ─── └─ └───┘─ └─┘──┘ └────┘ ──┘──┘──┘
                                              • ──  • ─┘─  •  •   •  •      •      •      •









```

*Figure from page 10 (2346x3317 px)*


---



5-2-4. Page Down



When the page key



4203-E P-221



SECTION 2 PROGRAM OPERATION



is pressed, the next page is displayed.



On the display screen, 16 lines of program data are displayed on one display page. When program data to



be edited is not found on the given page, press the page keys until required data is obtained.



Positions of the edit pointer and edit fine remain unchanged.



When the last part of the file has been reached while the page key is pressed, the remaining blocks are



displayed on the screen. The message "file end" will appear on the command line.



5-2-5. Page Up



When the page key



is pressed, the previous page is displayed.



When the first page has been reached, the display remains unchanged even if the page key is kept



pressed. The message "beginning of file" will appear on the command line.


```text


                                                                                                 ──
                                                                          ┌──┐─┐──┐───┐──────────░░░────────┐
                                                                          │░▒│ │░░│ ░ │░░░░░░░░░░───░░░░░ ░░│
                               ─────────────────────────────────────────── ──┘─┘──┘── └─────────
           ┌─────   ──────────                                                                              │
           │░ ░ ░  │░░░░  ░ ░░                                            ──────────────────────────────────┘
           └────  ─┘          ┌───────┐─────────────┐─┐──────────────────
                 │░░ ░│ │░ ░░░│ ░░  ░░│    ░░░░░   ░│ │░          ░  ░   │
                 │    │ │           ──┘─                                 └──────── •     ┌─── ───  ─────────
                 └─  ░└─┘░░░░░│░░░░░  ░ ░░░░───░ ┌──░░ │░░ ░  ░░░░░ ░         ░░  • ─┐─┐ │░░ •   ──         │
                 │ ───░░ ─────┘─────  ─────    ──┘  ┌──┘─  ─┐───  ┌──  │         │ │ │░│      •   ░ ────────┘
                 │                   •            │ │       │     │  • │  ───┐   │░└─┘░│    ░░░  ░──
                 │ ░░░░░░  ░ ░• •░░ •░ ░      ░ ░ └─┘       │   ──┘   │      └─── •   ─┘──────────
                 │                    │    ┌─    •          └──       └┐─ • •       •
                 └┐──────┐ ░░ •░░  ░ ░│ ░░ │░░ ░░░• ░┌─┐ ░░ ░░ ░     ░ │ • │         ────         •  ───┐────
                 └┘      └──── ──  • ─┘──  └─        │ └─┐  ─┐            ░│             • ───────░ •   │
             ───  └─          •  •  •     •  •     │ └─┘ └── │ • │  ░──  ── ░ │░   ░ ░ ░ ░•       •  ─── ───
           ┌┐              │                  ─────┘─   •    └─ ─┘───  ──  ───┘───────────
           └┘───  ──       └─  •    ┌─┐
                 │░   •      ── ┌─ ─┘░│ ┌───────┐ ┌──────────────┐──────────┐
                 │   │     •    │     │ │      ░└─┘            ░░│ ░  ░░ ░░░└─
                 │░░░│  ░░ ░ • •░ • ░ └─     •░       ░         •      ─┐  •  ───  ───────────┐──┐─┐─┐───┐──┐
                 └─     ┌─┐ •    ░                    │ │ ┌─ ──┐        └─  •░ ░░──░       ░  │░░│ │░│ ░ │░░│
                 │     ┌┘ └─  • • ░░░┌──░░░  ░░░│ ─┐┐ │░│ │░░░░│ •░ ░│  ░░░ ░░░•░░░┌───── ────┘──┘─┘─┘───┘──┘
                  ─────┘     • • ────┘  ────────┘─ └┘  ─┘─┘────┘─ ───┘───────── ───┘

























































```

*Figure from page 11 (2327x3290 px)*


---



4203-E P-222



SECTION 2 PROGRAM OPERATION



5-3. One Line Insertion



(1) This function inserts a blank line right before the edit line.



Press function key [F1] (LINE INSERT) to insert a blank line before the edit line (>>).



(2) Lines following the edit line shift down and the last line on that page disappears from the display



and shifts to the next page.



(3) The edit pointer shifts to the beginning of the inserted blank line.



(4) One line insertion operation at the line which has more than 63 characters differs from ordinary



one line insertion processing. (See the figure.)



N101 GOO



N102



>> &Y100 □



N103 G01



N104



N117 G01



=E WHEEL100. MIN



ti le end



>IL



XB00 2200



X250



Z150



X300



X113



LI NE LI NE CHAR. CHAR. LI NE ED IT



NSERT DELETE I NSERT DELETE DELETE ERASE OU l T



Press F1] (LINE INSERT).



N101 GOO X800 2200



N102 X250



&Y100



N103 G01 2150



N104 X300



(5) The prompt"> IL" will be displayed on the command fine.



(6) This function is effective for inserting lines in the stored program.



F0.3



[EXTEND]



F0.3


```text


                                                                                                ───      ──
                                                                         ┌──────┐─┐───┐─────────░░░──────░░│
                                                                         │░░░░░ │░│   │░░░░░░░░░───░░░░░░░─┘
               ────   ────────  ──    ───────────────────────────────────┘──────┘─┘─  └─────────      •
           ────    ───        ──  ────                                                                      │
          │    ┌───         │          ─────────────────────────────────────────────────────────────────────┘
          └─ ──┘   ───░─┐ ─┐┘ ┌─────
            •     │   │ │  └┘─┘     ── ────┐────────────────────┐─┐─┐─┐─┐
                  │ │ │ ░│ │░ │░░│ │░░░░ ░ │░░░  ░░ ░░░ ░░░░░ ░░│ │░│ │░│
                  └─┘ │  └─ •  • │ └┐  •    ──                  │ │  ─┘ └┐──────────┐─┐─┐─┐──────┐
                      └─░░░░ ░░ ░░• │░│   ░ ░ •░  ░░░ ░░  ░ ░░░░│ │░░░░• │░ ░░░░ ░ ░│ │░│ │░     │
                  ┌─┐ │ │             │                       ┌─ • ─┐──  │   • ──┐  └─┘ └─┘    ─┐┘┐──┐─────┐
                  │░│ └─┘░────░░░░░░ ░└──░──── ░░░  ░░░│ ░ ░ ░│ │░│ │░  ░│░ ░ │░░│ │░░░│░░░│ ░ ░│ │░ │░░░░░│
                  └─┘ │░ • ░ ░────────░ ░•   ░─────────┘──────┘─┘─┘─┘────┘────┘──┘─┘───┘───┘────┘─┘──┘─────┘
                      │
                  │░│ │░ │ ┌─          ░░     │ ────  ────  ────────── ───────┐─
                  │ │ │  │ │ •        ───    ─┘   ░                           │
                  │ │ │  │                      •  │           •         ─┐ │  ──────────┐─────┐─┐──┐────┐─
                  └─┘ │  └──────────────────────░ ┌┘───────────░░   ░   ░░│ │░ ░ ░░░░░ ░ │░░░░ │░│  │░░░░│
                      │░ ░ ░░ ░░░░░░░ ░░░░░░░░░░  │░░ ░░░ ░░░░  ──────────┘ └────────────┘─────┘─┘──┘────┘─
                      └─┐─┐───────┐─  ─────────┐   ─────────┐
                        │ │       │            │            └──┐────────     ───────────────┐ │
                        │ │       │   │         ────        │░ │         • ──               │ │
                        │ │       │   │                     └──┘                            │ │
                        │ │       │  ░│         ──┐                     ┌───┐        ┌───┐  │ │
                        │ │       │ ░░└─         ░│         ┌──┐        │ ░░│        │   │  │ │
                        │ │       └───┘         ──┘         │░ │        └───┘        └───┘  │ │
                        │ │                                 └──┘                            │ │
                        │ │        │ │                      │                               │ │
                        │ │        └─┘          ───         └───                            │ │
                        │ └────────             ░░  ──────┐─░  ░────────────────────────────┘ │
                        │ │        ───          ───       │  ───                            │ │
                          └───────    ─────────     ──────┘ │   ──────────────────────────── •
                                                          │ │
                        ┌─┐    ───── ──┐─┐──┐             └─┘                               ┌─┐
                        │ │   │░ ▒░░░ ░│ │ ░│                                               │ │
                        │ │   └────────┘─┘──┘                                               │ │
                        │ │  •                            ─────────              •   •      │ │
                        │ │    ──┐  ┌─ ┌─┐  ┌───┐    ┌──┐          ── ┌┐    ┌──┐  ┌─┐       │ │
                        │ │   │ ░└─ │ ─┘░└┐ │ ░░└─   │░░└─  •   ─┐─  ┌┘┘─   │░ │ ─┘ │ ──┐─┐ │ │
                        │  ── └──┘░ │ ░ • │   ┌─┘░   └──     ┌── │   │░░░│  │░─┘  │     │ └─  │
                         •    │      │     │  │     ┌┘   •   │   │      ─┘        │     │    ┌┘
                          ── ┌┘ ─┐░─┐┘░░─┐ └─┐┘ •░ ─┘  ─┐ ─── ┌─┐ ──────  • ───┐──  ─┐──  ┌──┘
                             │  ░│  │░ │ │ ░ │ │ • ░░ │ │ ░ ░ │░│ ░ ░ ░░│ ░  ░░│ ░ │ │░░  │
                             └┐░ │  └──┘─┘── └─┘─     └─┘ ─── └─┘ ──────┘ ── ──┘───┘─┘── •
                              └──┘─                   │  •   •   •       •  •           •
                                    │░░░      ░   ░░░ │
                                  ──┘─────────────────┘
                                                        ──┐─┐────────────────────────────────
                        │                                 │░│                                 │
                        │ ┌───  •              ─────      │  ──┐        ┌───┐             ──┐ │
                        │ │   ┌─  ┌─┐       ─── ░░░     ── │░░░│        │░░░│          ┌─┐  │ │
                        │ │   │   │▓│  ─────    ────────   │   │        └───           │ │  │ │
                        │ │   └─  └─┘░│     ───            └┐░░│                       └─┘  │ │
                        │ │      •░  ░│         ──          └──┘─  ─────    ─────────       │ │
                        │ │       │  ┌┘        │                        │  │         ┌─┐    │ │
                        │ │       │  │         └───         ───┐        └──┘         │ │    │ │
                        │ │       └┐─┘                         │                     └─     │ │
                        │ │        │ │                      ───                             │ │
                        │ └───────   └─────────────────────     ────────────────────────────┘ │
                        │ │                                                                 │ │
                                                                        ────────────────────┘─
                 ┌─┐  ┌────────┐ ─┐───┐─────────────┐─────── ──────────
                 │░│  │░       │  │   │░     ░      │   ░   •          ─┐
                 │ │  │        │       ──           │                   │
                 │░│  │             │░•                                ─┘──────
                 └─┘  └──────────── └─  • │ ───┐   • ░       • │ │        ░ ░
                                   •   • ─┘─   └─── ───────── ─┘─┘────────────














```

*Figure from page 12 (2337x3305 px)*


---



4203-E P-223


#### SECTION 2 PROGRAM OPERATION

5-4. One Line Deletion



(1) This function deletes the edit line.



Press function key [F2] (LINE DELETE) to delete the edit Hne.



(2) Lines following the edit line shift up and the first line on the next page shifts to the current page



and displayed on the last line.



(3) The edit pointer shifts to the first character of the line next to the deleted line.



(4) One line deletion operation at the line which has more than 63 characters differs from ordinary



one line deletion processing. (See the figure.)



N101



N102



» &Y100



N103



>DL



ti le end



GOO



G01



xaoo



X250



2200



2150


#### LI NE LI NE CHAR. CHAR. LI NE ED IT

IN SERT DELETE INSERT DELETE DELETE ERASE OU IT



N101



» [f)103



N104



Press [F2] (UNE DELETE).



N117



GOO



G01



G01



xsoo



X300



X113



2200



2150



(5} The prompt ">DL" will be displayed on the command line.



F0.3



[EXTEND]



F0.3



(6) This function is effective for deleting an entire line in the stored program.


```text


                                                                                                ──        •
                                                                          ┌─┐───┐─┐───┐─────────░░────────░─┐
                                                                          │░│░░ │░│   │░░░░░░░░░──░░░░░░░░•░│
               ─────         •                                            └─┘───┘─┘── └─────────     ───
           ┌───     ───┐─┐─── ────────                                                                      │
           │  ░┌──── ░ │ │         ░   ─────────────────────────────────────────────────────────────────────┘
           └───┘    ──┐   ─── ───────
                  │   │ •    •       ──────────────┐
                  │ │  •░•   ░░░░│ │░░░░░ ░░ ░░░ ░ └┐
                  └─┘ │      ─── │ └──┐─   •  │ ┌─  └────────┐───┐─┐──┐─┐─┐─┐─
                      └──       •   ░░│ • • ──┘─┘ ──┘   ░  ░ │░░░│ │░ │░│ │░│
                  ┌─┐ │               │          •        ─┐ └───     └─ │  └─────┐─────┐───┐────┐──┐─┐───┐
                  │░│  ──░░ ──────░░ ░└──░░─────░░│ ░ ░ ░│░│  ░░ ░░│ │░ ░│ │░░ ░░░│  ░░░│ ░ │░   │░░│ │░░░│
                     • ░░┌──░░░░░░──── ░░──░░ ░░──┘──────┘─┘───────┘─┘───┘─┘──────┘─────┘───┘────┘──┘─┘───┘
                  ┌─┐ •  │              •
                  │░│  │░│ │░░    ░┌──░ ░│      ░ ░        •  │░│     •       • •   ──   ─┐
                  └─┘  └─┘ └─┐ │   │     │                    └─┼─                        │
                  │ │ ┌┘ │ │ │ │ • │   •                      │ │   ─┐                  │ └───────────────┐
                  └─┘ │  │ └─┼─┘─ ─┘──┐ ───────   ──┐─────────  │ ── └── ────────┐░     │░ ░           ░ ░│
                      │░ ░ │░│ ░░░░   │░░░░░░ ░│ •░░│ ░░ ░░░░░  │                └───    • ───────────────┘
                       ──┐─ ─┘────┐   └┐───────┘   ┌┘────────   │        ───┐
                         │ │      │ ── │       └┐  │          • └───────    │ ───────────────┐ │
                         │ │      │   │         │ ─┘        │ ░│         ───┘                │ │
                         │ │  ┌─┐ │   └┐                    └──┘                             │ │
                           │  │ │ │    │         ─┐                      ────        ┌───    │ │
                           └──┘ │ │  ░│         │░│                      ░ ░         │   •   │ │
                                   ───┘         └─┘                      ────        └──  ─── │
                                                    ──────┐ ┌───────────     ─────           ─┘
                                                          └┐┘
                        ┌─┐                                └┘                                ┌─┐
                        │ │                                                                  │ │
                        │ │   ┌─┐                                                            │ │
                        │ │   │░└┐─┐─                                                        │ │
                        │ │  │   │ │░── •   ── •   •  ──   •       ──     ─┐───┐──── ──────  │ │
                        │ │  │  •░  ░  •░─┐─  │░──┐ ──░░─┐ ░•     •░ ┌──┐  │ ░░│    │        │ │
                        │  • │  ░│    │░░ │   │░░░│   ░ ░│   ┌─┐─  • │ ░│    ░ └──┐ └┐──┐──┐─ │
                        └┐  • ┌──┘┐   └──     └───   ┌───┘── │░│ •   └──┘   ┌──   │  │░ │░░│  │
                         └─┐  │   │  •       │       │       │    │ │       │   ──   │  └─┐┘ •
                           └─┐░ ░│     ░── ░ │ ░ │   └──┐  ── ┌─┐ │ │ ┌─┐  ┌┘──░     └─┐  │
                             └┐ ░│  ┌─ │ ░ ░ │   │ ░ │  │   ░ │ │ │ ░ │░│ ░│   │   ░ │ │ ░│
                              └──   │ ─┘┐░    •   •  └─   •     └─┘───┘─ ──┘───┘ ──── ─┘──┘
                                  ──    └──  ░░░ ░░ ░░░░ ░░░░░░┌┘               •
                                           ────────────────────┘

                        │                              ───┐░•                ───────────────┐─
                        │ ┌───  ──     ────────           │  ───         ───                │ │
                        │ │   ┌─  ┌───┐         │░│    ─── •░░░░         ░░░         ┌───┐──┘ │
                        │ │   │   │░░░│         └─┘         │  │        ─────        │░  │  │ │
                        │ │   └─  └───┘                     │░ │                     └───┘  │ │
                        │ │                                 └──┘                            │ │
                        │ │        │ │                      │                               │ │
                        │ │       ┌┘─┘          ───         └───                            │ │
                        │ └────── │             ░░  ────────░    ───────────────────────────┘ │
                        │ │       └───          ───         ────                            │ │
                      ┌─                                                 ─────────────────── •
                  ─┐  │ ──────── ────  ─────────────────────────────────┐
                   │  │                          ░ ░                   ░│
                   │  │         ───  ──  •  •   •    ──    ──┐       •  └───────┐────┐
                  ░│  │  ░          ░ ░░░ │ ░│ │░ ░ │░ ░ ░░░░│ ░ ░ │ ░│ │░░░░ ░ │░ ░░│
                  ─┘   ───────────────────┘──┘─┘────┘────────┘─────┘──┘─┘───────┘────┘






















```

*Figure from page 13 (2346x3317 px)*


---



4203-E P-224



SECTION 2 PROGRAM OPERATION



5-5. One Character Insertion



(1) This function inserts a space before the edit pointer.



Press function key [F3I (CHAR. INSERTI to insert a space right before the edit pointer.



(2} Data following the edit pointer shifts to the right when a space has been inserted.



(3) One character insertion operation at the line which has more than 63 characters differs from



ordinary one character insertion processing. (See the figure.)



» N101 GOO Y200 2200



>IC



LINE LINE CHAR. CHAR. LINE EDIT



INSERT



DELETE INSERT DELETE DELETE ERASE QUIT [EXTEND)



(BJ@ @@@)@@)



Press [F3) (CHAR. INSERT).



>> N101 GOO x■aoo Y200 220



(4) The position of the edit pointer remains unchanged.



(5) The prompt ">IC" will be displayed on the command line.



(6) This function is effective for inserting a character (numeral).


```text


                                                                                                ────      •
                                                                          ┌─┐───┐─┐────┐────────░░░░──────░│
                                                                          │░│░░░│░│    │░░░░░░░░ ───░░░░░░─┘
               ────     •          •         ─────────────────────────────┘─┘───┘─┘─ ──┘────────     ──
           ┌───     ──── ┌───────── ─────────                                                               │
           │  ░┌───      │░ ░       ░    ░   ───────────────────────────────────────────────────────────────┘
           └───┘   ───┐  └───────── ───────
                  │   │ •          •       ────────────────────────┐
                  │ │  •░│ ░  ░░░░ ░░░░░ ──░░░░░ ░░░░░ ░░ ░░░ ░░░ ░│
                  └─┘ │  │         ─┐       ───  ┌─┐       ───┐   • ─┐───┐─┐─┐──┐─┐────┐─┐─┐─┐────┐
                      │    │ ░      └─── ──    ──┘ │░┌────┐ ░ │░░•   │░░░│ │░│  │░│ ░ ░│ │░│ │░░░░│
                  ┌─┐ │ ──┐┘      ──┘   •     •  └┐┘─┘    │  │ ┌─ ──┐┘── └─┘ │ •     ┌─ •  └─ ────┘
                  │░│ └─░░│ ░ ░░░ ░ │░ ░░░ ░░░░░• │░░│ ░ • ░ │░│ •░░│ ░ •░░░░│ ░░░░░░│ •░░ ░░•
                  └─┘ │             │                                       • •  • • └─ •   • ┌───┐──┐──┐
                  │░│  │░─────░░•░──┘──────────────────────── ░░────┐░░───── ░░│ ░│ ░░░ ░░░░  │░░░│ ░│ ░│
                  └─┘  └─░  ░  • •   ░  ░░                   ┌─     └─ ░    ───┘──┘───────────┘───┘──┘──┘
                         ┌─ ─── •  ────────────── •  ──────┐░│ ┌────   ┌─
                         │ │                       ──      └─┘ │       │  │ │       ────     │ │
                         │ │    •   │  │      │░░│         │▒│░        └┐░└─┘─    • ░░░      │ │
                         │ └────  ──┘──┘──────┘──┘──────── └─┘  ─────── └─┘   ────  ──── ────┘ │
                         │ │                                                                   │
                            ───────────────────────────────  ─────────────────────────────────
                                                           ──
                        │ │                                                                  ┌─┐
                        │ │                                                                  │ │
                        │ │                                                                  │ │
                        │ │   •     •     ─┐       •      ┌───────┐─      •          ──────  │ │
                        │ │  │ ──┐ │ • ──┐ └──┐──┐  ──┐─┐ │       │ • ┌─┐  ─────   ─┐        │ │
                        │ └┐ │  ░└─┘  │░░└┐┘  │░░└┐   │░└─┘       │  ┌┘░│    ░░ • │ │  ─┐─  ┌┘ │
                        │  └─  ──┘░   │░  │   │░░░│   └─┘  │ ┌────   │░░░│   ───  │  ░• │░──┘ ┌┘
                         •        ─── └─ ┌┘   │  ─┘       ─┘ │     • └───┘        │      •    │
                          ───         │  │ • │    │  │          │ │           ─┐──┘──┐─┐  ┌───
                             ┌┐ ░   ░    ░ ░ │ │ ┌┘──┼───┐────┐░└─┼─┐ ░░  ░   ░│ ░ ░ │░│ ░│
                             └┘ ──  ── ░•░ ──┘ │░│ ░ │░ ░│  ░ └─┘ │ │ ──────  ─┘ ░── └─┘ ─┘
                               •  ──  ── ──   ─┘─┘─┐                        ──  ──  •   •
                                                   └┐░  •  •  ┌┐ │░░ ───
                                                  • └─── ─┐ ┌─┘┘─┘───
                          ┌─────        ─────             │ │               ────────   ─────┐
                        │ │         ────      ───          ░└┐──       ────         ──┐     │
                        │ └─────── •░ ░        ░░           ▒│░░          ░           │ ────┘
                        │ │         ────      ───          ──┘──       ────         ──┘     │
                          │                                          ──                ─────┘
                  ┌─┐ ┌───┘─────┐───────────────────────────────────                        │
                  │░│ │░ ░ ░░░░░│ ░ ░░  ░░ ░░░ ░░ ░░░░░ ░   ░ ░░░░░      ───────────────────┘
                  └─  │         └─┐    •         ──                 ─┐─┐─
                  │░│ │░ ░░░ ░░░│ │░• │░░ ░ •░░░░░░░  ░•░•░ ░░░  ░░░ │░│
                 │  │ │         └─┘  ─┘      ┌─┐─       • ─── ── ─┐  │ └──┐
                 │░░│ │░ ░ │░░░░│   │░░░░░░ ░│ │ ░░░░░ │ │░░ ░░░│ │░  ░░░░│
                 └──┘ └────┘────┘───┘────────┘─┘───────┘─┘──────┘─┘───────┘

































```

*Figure from page 14 (2346x3317 px)*


---



4 2 0 3 - E P - 22 5



S E C T I O N 2 P R O G R A M O P E R A T I O N



5 - 6 . O n e C h a r a c t e r D e l e t i o n



( 1 ) T h i s f u n c t i o n d e l e t e s a c h a r a c t e r l o c a t e d b y t h e e d i t p o i n t e r .



P r e ss f u n c t i o n k e y [ F 4 ] ( C H A R . D E L E T E ) t o d e l e t e t h e c h a r a c t e r l o c a t e d b y t h e e d i t p o i n t e r .



( 2 ) W h e n t h e c h a r a c t e r i s d e l e t e d , c h a r a c t e r s f o l l o w i n g t h e d e l e t e d o n e s h i ft t o t h e l e f t .



( 3 )



O n e c h a r a c t e r d e l e t i o n o p e r a t i o n a t t h e l i n e w h i c h h a s m o r e t h a n 6 3 c h a r a c t e r s d i ff e r s f r o m



o r d i n a r y o n e c h a r a c t e r d e l e t i o n p r o c e ss i n g . ( S ee t h e fig u r e . )



>> N 1 0 1



& O



> DC



L I N E L I N E



I NS E R T D EL E TE



G OO



C HA R . C H AR .



Q9 8 00



I N S E R T D E L ET E D E L E T E


#### Y 2 00

L I N E



ERA S E



E D I T



Q U I T


#### Z2 0

[ E X T E N D ]



@ @J @J � (fil @ @J @


#### P r e ss [ F 4 ] ( C H A R . D E L E T E ) .

> > N 1 0 1 G OO 8 0 0



( 4 ) T h e p o s i t i o n o f t h e e d i t p o i n t e r r e m a i n s u n c h a n g e d .


#### Y 2 00

( 5 ) T h e p r o m p t " > D C " w i ll b e d i s p l a y e d o n t h e c o m m a n d l i n e .


#### Z 2 00


```text
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████┌────────────────────────────────────────────────────────────────────────────────────────────────┐████████████
██████████│████████████████████████████████████████████████████████████████████████████████████████████████│████████████
██████████└────────────────────────────────────────────────────────────────────────────────────────────────┘████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████──────────────███████████████████████████████████████──────────────┐─██████████████████████████
████████████████████████│▓██████████████████████████████████████████████████████████████████│▓│█████████████████████████
████████████████████████│▓┌──────────████████──────────████████──────────██████───────────██│▓│█████████████████████████
████████████████████████│▓│██████████────────██████████────────██████████──────███████████──┘▓│█████████████████████████
████████████████████████│█│█████████████████████████████████████████████████████████████████│▓│█████████████████████████
███████████████████████████─────────────────────────────────────────────────────█───────────┘─██████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████│█│█████████████████████████████████████████████████████████████████┌─┐█████████████████████████
████████████████████████│█│█████████████████████████████████████████████████████████████████│█│█████████████████████████
████████████████████████│█│█████████████████████████████████████████████████████████████████│█│█████████████████████████
████████████████████████│█│█████████████████████████████████████████████████████████████████│█│█████████████████████████
████████████████████████│█│█┌──────┐─┐─────┐─┐────┐─┐─────█•█─────┐─┐───────┐────┐─┐──────██│█│█████████████████████████
████████████████████████│█│█│██████│▓│█████│▓│████│█│█████│▓│█████│▓│██████▓│████│▓│████████│█│█████████████████████████
████████████████████████│█└─██████─┼─┼─────┼─┘███─┼─┼─────┼─┼─────┼─┼───────┼────┼─┘███████─┘█│█████████████████████████
████████████████████████│███──────█│█│█████│█└───█│█│█████│█│█████│█│███████│████│█└───────███│█████████████████████████
█████████████████████████───████████████████████████████████│██████████████████████████████┌──██████████████████████████
████████████████████████████────────────────────────────────█──────────────────────────────┘████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
███████████████████████████████───────────────────────────┐─┐─────────────────────────────────██████████████████████████
██████████████████████████████████████████████████████████│▓│█████████████████████████████████│█████████████████████████
███████████████████████████████───────────────────────────┘─┘───────────────────────────────┐█│█████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████│█│█████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████│█│█████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████│█│█████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
```

*Figure from page 15 (1236x1747 px)*


---



5-7. Deletion



4203-E P-226



(1) Program data in a specified range is deleted.


#### SECTION 2 PROGRAM OPERATION

After specifying the number of lines to be deleted, press function key [F5] (DELETE). The specified



number of lines will be deleted including the edit line (»).



(2) The edit pointer is placed at the first character of the block which follows the final line of the



deleted blocks.



(3) When the number of the specified lines to be deleted is larger than the final block of the file, all



program data up to the end of the file is deleted and the line right after the final line of the file



becomes the edit line. In this case, the message ''file end" will appear.



(4) After program data has been deleted, the message "**RECORD DELETE" appears on the



command line. Here, "**" indicates the number of the deleted lines.



(5) Lines following the deleted range wlll shift up.



Operation:



[F5] (DELETE)-4 [WRITE]



Four lines preceding the edit line (edit line not included) are deleted.



[F5J (DELETE) [WRITE]



Only the edit line is deleted.


```text


                                                                                                •         •
                                                                         ┌──┐──────┐─┐──────────░░───────┐░│
                                                                         │░░│ ░░░░ │ │░░░░░░░░░░──░░░░░░ └─┘
               ────         ───────────────────────────────────────────── ──┘──────┘ └─────────
          ┌───     ──────┐──                                                                               │
          │   ┌────      │  ───────────────────────────────────────────────────────────────────────────────┘
          └───┘     ─────┘
                  │       • ─┐─┐─┐─────┐─┐─┐──┐────┐───┐─────┐
                  │░│ │ ░░░ ░│ │░│   ░ │░│ │░░│ ░░░│ ░ │░░░░░│
                  └─┘ │        │           │           │      •    ─────────┐─┐─┐─┐─────────┐─┐─┐───┐───────┐
                      │ ░░──░░░ ░──░ ░───░ ░░─── ░ ────┘───░░░░────░░░ ░░░░░│ │░│ │░░ ░ ░░░ │░│ │░░░│░░░░░░░│
                      └───░░───── ░┌──░ ░────░░░─┐─░░ ░░░ ░────░ ░ ─────────┘─┘─┘─┘─────────┘─┘ └───┘───────┘
                 ┌─┐  │            │             │                                             •
                 │░│  └┐────░──░░•░│ ░ │░░ ░  ░ ░│ ░ ░   ░      ░ ░             ░         ░ ──  ───  ──
                 └─┘  └┘    •  ── ─┘───┘─────────┘──────────────────────────────────────  ──  •    ──
                      │       •
                  ──  │             •    ─┐─────  ──  ───      ─────     ──         • ──  ──  ───   ── ──┐
                   ░  └────────────┐░────░│ ░░░░──░░──░░ ──────░░░░░─────░░───────── ░░░ •░░░• ░ ┌─ ░░• ░│
                      │░░░░░░  ░░░ │░ ░ ░░ ░   ░ ░ ░░░░ ░ ░░░░░░ ░ ░ ░░ ░ ░  ░  ░░░  ───░ ─── ───┘░ ──░ ─┘
                      └────────────┘─────────────┐ ─┐──────────   • ──────   •     │    ──        •   ──
                  ──  │                          │  │              •      •   • ░  │
                      │░─┐    ───┐ ───   ────── │        │       •               • └────┐─┐─────┐─┐────┐
                 ───  │  └─── ░  │    ──        │░ │ │ ──┘  •  •░░ ───  ┌────   •░░     │ │░░░░░│ │░ ░░│
                      └──░░░░ ──░░ ───░░──┐ ────┘──┘─┘ ░ ░• ░•░░─── ░░░ │░░░░░ ░░░────── ─┘─────┘─┘────┘
                 ┌─┐  │           •       │          │        ──   ─────┘─────────
                ┌┘░│     ░│ ░ ░░ │░ ░│ │░░░░│ │░░░│ │░ │░░│ ░│
                │   ─┐─┐  └──────┘───┘─┘────┘─┘───┘─┘──┘──┘──┘
                └┐░░ │░│░
                 └───┼┐  ─────────┐───┐──────
                     └┘           │   │    ░ │
                            │░               └─  ┌──────────────────────────────┐─┐─────┐
                     ┌──────┘        ─── ──   ░  │         ░            ░  ░░  ░│ │░░░░░│
                     │░ ░ ░ ░░   ░   ░ ░•  │          ──────────────────────────┘─┘─────┘
                     └──────┐              └─────────
                            └┐░░  ░░ │░░  ░    ░░░░
                             └───────┘───────────────














































```

*Figure from page 16 (2330x3295 px)*


---



4203-E P-227



SECTION 2 PROGRAM OPERATION



N101 GOO X800 Z200



N102 X250



>> N103 @1 Z150



N104 X300



N105 GOO X310 Z200



N106 X200



N107 G01 Z100



To delete four blocks from N103 to N106



>DEL 4



LINE LINE CHAR. CHAR. LINE EDIT



IN SERT DELETE I NSERT DELETE DELETE ERASE QUIT



Press F5 (DELETE).



Key in "4" through the keyboard.



» N101



N102



IEl107



GOO



G01



Press the WRITE key.



X800 2200



X250



Z100



The command line of the screen will show the followfng message.



>DEL 4



4 RECORD DELETE



ti le end



beginning of file



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELETE IN SERT DELETE DELETE ERASE OU IT



F0.3



[EXTEND]



[EXTEND]


```text


                                                                                                ──        •
                                                                          ┌─────┐─┐───┐─────────░░────────░┌─
                                                                          │░░░░ │░│   │░░░░░░░░░ •░░░░░░░░░│
           ┌───────────────────────     ─────────   ──────────  ───────── └─────┘─┘   └─────────      •
           │                       ┌───          ───                     •                                  │
           └─────────────┐ ┌──────┐┘   ─────────    ┌──────  ─── ┌──────┐    ┌───────────────  ┌────────────┘
                         │ │      │░ ░│         │  ┌┘      ──░░░ │      └┐─░┌┘               │ │
                         │ │      │░ ░│         └─ │         ───┐        │  │        ┌───    │ │
                         │ │      │░ ░│         │░•         │   │       │   │        │       │ │
                         │ │      │░ ░│         └─ │        └┐░─┘       │   │         ───    │ │
                         │ │      │░ ░│         │  │        └┘░░│        │  │                │ │
                         │ │      └───┘         │  │         └──┘        │  │                │ │
                         │ │                    └──┘                     └──┘                │ │
                         │ └──────                                           ────────────────┘ │
                         │ │                  ────────────────────────────                   │ │
                            ──────────────────░ ░░░░ ░  ░  ░ ░ ░   ░ ░ ░ ░  ─────────────────┘
                                              ─────────────┐─┐─────────────
                                                           │ │
                                                           └─┘                               ┌─┐
                        │ │                                                                  │ │
                        │ │                                                                  │ │
                        │ │     ─┐                                                           │ │
                        │ │  ───░└────     ┌──     ─┐     ──┐─────┐──    • ──   ┌─ • ──────  │ │
                        │ │     ░│    ┌───┐┘  ┌───  └─┐──┐  │     │   ┌─┐ •  ─┐─┘ │░│        │ │
                        │  • │ │░░•   │░░ │   │░░ •   │░░└┐  ┌───┐   ┌┘░│    ░│ │ │░└┐───────┘ │
                         •  ─┘ └──░   └── │   └───░   └── └─ │░░░│   │░░│  ─┐░│ │ │  │░░░░░    │
                          ─┐                 │       │                      │   └─   │  ──┐─ ──
                           └─┐  ░│      ░░ ░ │ ───   │ ░       ░│     ┌── ──┘     ──  ──  │
                             │  ░│  │░  │░   ░ ░ ░   │ │░│ ─┐   │ ░ ░ │░  ░ │   │ ░  ░ ░ ░│
                             └───   └── └────────────┘─┘─┘  └──┐░ ────  ────┘───┘ ┌───────┘
                                  ──   •                       └──░░░░░░░░░░░░░░└─┘
                                                ┌─┐── ────┐────   ──   ─────────┘
                                                │░│     ░ │   ░│ ░ ░ ░░
                                                └─┘─    ──┘   ─┘─  ───
                                                    ───┐  └───   ┌─    ─┐  │
                                                   │░ ░│ ░   ░ ░ │░│  │░│  │
                                                   └───┘─────────┘─┘  │░│  │
                           ───────                                    │      ───────────────┐─┐
                        │ │        ──┐           ───        ───┐        │ ───               │ │
                        │ └────── │  │           ░░          ░░│        │ ░░  ──────────────┘ │
                        │ │       │   │         ┌───        ── │         ┌──┐               │ │
                        │ │       │░  │         │             ─┘         │  │               │ │
                        │ │       └───┘         │ •                      │  │               │ │
                        │ │                     └─                       └──┘               │ │
                        │ └───────   │                                              ────────┘ │
                        │ │          └─────────────────────────────────────────────         │ │
                           ───    ─── ░  ░ ░░░  ░   ░░ ░ ░  ░░ ░░░ ░░  ░ ░ ░  ░░░░  ────────┼─┘
                        ┌─┐    ┌┐    ──     ── ──  ────────────────────────────────         │ │
                        │ │   ┌┘┘┐     ────┐  •  •                                          │ │
                        │ │   │  │  •  ░  ░│  ░  ░│                                         │ │
                        │ │   └──┘──░│  ┌──┘  ────┘                                         │ │
                        │ │  •░░  ░░ │ ░│          ──     ──┐─────┐─            ──┐─┐────── │ │
                        │ │   • ░  ─┐┘  │      ─┐    ┌──┐   │     │ • ┌┐   ┌───┐  │ │       │ │
                        │ └─    ░┌─ │ ──░•  •  ░└─   │░░└─  └┐───┐   ┌┘┘─  │   │     ───────┘ │
                        │   • ──░│░ └┐░░• •   •░│░   └──░░  └┘░░░│   │░░░•  ───┘─    ░░ ░▒░   │
                         ──          └─    │         │           │   │  │               ──┐─ •
                           ──┐─ ░│  •  ┌─┐ │   ┌── •   ── │ │ ┌─┐ │ │ ┌─┘ ─┐     │ │ ┌─   │
                             │   │   ░ │ │ │ ░ │   ░│ ░ ░ │ │ │░│ │ │ │░│ ░│ ░ ░ │ │ │░│ ░│
                             └───┘ ┌── └─┘─┘───┘── ─┘─────┘─┘─┘─┘ └─┘─┘─┘ ─┘─────┘─┘─┘─┘──┘
                                  ─┘  •           •              •       •






















```

*Figure from page 17 (2346x3317 px)*


---



4203-E P-228



SECTION 2 PROGRAM OPERATION



5-8. One Line Erasing



(1) This function erases program data in the edit line(>>). The blank line remains.



Press function key [F6] (LINE ERASE) to erase program data in the edit line. When data is erased,



a blank line will remain.



(2) The edit pointer is placed at the first character of the erased edit line.



(3) The prompt ">ER" will be displayed on the command line.



(4) One line deletion operation at the line which has more than 63 characters differs from ordinary



one line deletion processing. (See the figure.)



N101 GOO X800 2200



N102 X250



>> &2200 D



N103 G01 2150 F0.3



N104 X300



>ER



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELETE I NSERT DELETE DELETE ERASE OU IT [EXTEND]



@ @J @


# CED CJIJ

@J @J



N101



>> •



N103



N104



GOO



G01



X800



X300



Press [F6] (LINE ERASE)



2200



2150 F0.3



(5) This function is effective when replacing entire program data in a block with new program data.


```text


                                                                                               ────
                                                                         ┌───────┐───┐────┐────░░░░──────░░│
                                                                         │░░░░░░░│ ░ │░░░░│░░░░ ──░░░░░░░──┘
            ───────────────── ───────────────────────────────────────────┘───────┘── └────┘────     ───
          ┌─                 •                                                                             │
          │   ┌────        •          ─────────────────────────────────────────────────────────────────────┘
          │░ ░│    •░ • ───░   ─────░│
          └───┘  ┌─ ── •     ──      └─────┐───────────────┐────┐──┐─┐─┐───┐───┐───────────┐
                 │ │  •░░░ ░ ░░░░ ░ ░░░░ ░ │░ ░░ ░░░ ░ ░ ░ │░ ░ │ ░│ │ │ ░ │░░░│ ░░  ░░░░ ░│
                 └─┘ •                      •              │ ─┐ └─┐┘┐┘─  ─┐ ─┐ │ │     ┌─┐─┘┐──┐──┐─┐──────┐
                      │ ░─┐ ░░•░░░ ░░• ░ ░ ░ ░░ ░░░░░░  ░ ░ │░│ ░ │░│░░ │░│  │░│ │░░ ░ │ │░░│  │░░│ │░ ░░░░│
                      └──░└───░──────░──────────────────────┘─┘───┘─┘───┘─┘─  ─┘─┘─────┘─┘──┘──┘──┘─┘──────┘
                 ┌─┐ •                                                      ──
                 │ │  │     ░── ░ ░░   ░       ░   ░     ░      ░         ░  ░   ░│
                 │ │  │ ┌─ ──  ────        ┌─┐       •               ───┐─────────┘
                 │ │  │ │ •        ░░│     │ │ ──────                   │
                 │ │  └─┘          ──┘     │ └┐                 ─── •   │
                 │ │  │                       │   │            │   • •  └───────────────────────────────┐
                 │ │  │ ──────────────────────┘░ ┌┘───────────░│      ──░  ░    ░ ░                   ░░│
                  ─┘  │ ░ ░░░ ░░░░░░ ░░░░░░░░ ░  │░░ ░░░ ░░░░  └──────                        ──────────┘
                       ─┐─┐─────────  ┌────────   ──────────┐  │         ───
                        │ │           │        │            └──         │   ┌───────────────┐ │
                        │ │       │  │         └───         │░ │        └───┘               │ │
                        │ │       └──┘┐        │            └──┘                            │ │
                        │ │       │░░░│        └───                     ┌───┐        ┌──┐   │ │
                        │ │       │░ ┌┘        │░░         ─┐──┐        │░ ░│        │░ │   │ │
                        │ │       └──┘          ──          │░░│        └───┘        └──┘   │ │
                        │ └───────                 ───────   ──┘────────     ────────    ───┘ │
                        │                                 ┌─┐                                 │
                         ─────────────────────────────────┘░└───────────────────────────────
                        │                                 └─┘                               ┌─┐
                        │ │                                                                 │ │
                        │ │                                                                 │ │
                        │ │                                                                 │ │
                        │ │   ┌─┐ ─┐      ──      ┌─      ── ───────                        │ │
                        │ │   │░└┐ └──  │   ── •  │   ──    │       •  •    ──┐             │ │
                        │ │   │░░└┐    ─┘─┐   •░──┘  │░░─── └────┐   ──▒│    ░└┐     ┌───── │ │
                        │  ──  •░░│   ░░░░└─  ░░░░   │░•░░   ░░░░│   ░░░│   •░└┘    ─┘░░░░    │
                         •      ──       ─┘      •        ── ─┐ ─┘   •                  ───  •
                          ──┐          ┌─              •    │ └─    │ │ │ •      │ │ ┌─
                            │  │ ░   ░ │░│ ░ │ ░░│  ░ │ │ │ │ │░│   │ │▒│ ░│ ░ │ │ │ │░│ ░│
                            └─ └── ┌───┘─┘ ──┘───┘ ───┘─┘─┘─┘─┘─┘ ──┘─┼─┘ ─┘───┘ │  ─┘─┘ ─┘
                              •   ─┘      •       •              •    │ │       │ •    │
                                                                      │░│   ░  ░│ ░ ░░░│
                                      ──────────   ───────┐─┐   ───── └─┘  ─────┘──────┘────
                        │          ───           ──       │░└──┐         ──                   │
                        │ ┌───  ──    ──────────   ───────┘─   └─────── │   ────────────────┐ │
                        │ │   ┌─  │  •          • •         • ─┘        │  •                │ │
                        │ │   │   │▒                         •                              │ │
                        │ │   └─    •          ┌──┐                     ┌───┐        ┌─┐─   │ │
                        │ │       │░ │         │░░│         ┌──┐        │░ ░│        │░│    │ │
                        │ │       └─ │         └──┘         │░ │        └───┘        └─┘─   │ │
                        │ └───────     ────────    ──────── └──┘───────      ───────     ───┘ │
                          │                                                                 │ │

                 ┌──  ┌─────────┐─────────┐──────┐────────────────┐───┐──────────────┐──────────┐───────┐─
                 │ ░  │ ░░      │ ░ ░ ░░░░│ ░  ░ │░░░░  ░ ░ ░ ░ ░ │░  │ ░░░     ░░░░ │░░  ░░  ░ │░░   ░░│
                 └──   ─────────┘─────────┘──────┘────────────────┘───┘──────────────┘──────────┘───────┘─
























```

*Figure from page 18 (2329x3294 px)*


---



4203-E P-229



SECTION 2 PROGRAM OPERATION



Before executing operations explained in 5-9. "Find», press function key [F8] (EXTEND).



Press function key [FS] (EXTEND). The function names on the display screen will change as shown



below.



>ER



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELETE INSERT DELETE DaETE ERASE OU IT [EXTEND]



@J@]@ @J@ @J @J



=E WHEEL100. MIN



file end



>EX



Press [FS) (EXTEND).



PAGE INSERT



FIND CHANGE COPY MOVE EXTRACT MOOE MODE [EXTEND]


```text


                                                                                                 ──       ──
                                                                          ┌───────┐─┐─┐─────────░░░───────░░│
                                                                          │░░░░░░░│ │ │░░░░░░░░░ ── ░░░░░░──┘
           ┌───────────          •    •       ──────    ────────     ─────┘───────┘ │ └─────────    • ──
           │           ──┐────┐── ───┐ ───────      ────        ────┐              ─┘ │         •           │
           └───────────  │    │      │         • •                  │ │          │                   ───────┘
                       ┌─┘  • │   ──┐┘ ── ─────   ───────── ──  ────┘ └──────────┘ ──────────────────
                       │  ── • ───  │    •     ┌─          •   •     •                               ───────
                       │ ░░░░ ░░░░│ │░  │░░ ░░ │░░░░│ │      ░      ░░    ░   ░  ░          ░               │
                       │  ────────┘─┘───┘──────┘────┘─┘─────────────────────────────────────────────────────┘
                       │ •
                        │  •
                        │ │                                                                 ┌─┐
                        │ │                                                                 │ │
                        │ │                                                                 │ │
                        │ │   ┌─┐  •      ──              ──┐─────              ──┐──────── │ │
                        │ │   │░└┐  ── ┌┐   ┌─ •     ┌──┐   │     ┌──  •   ───┐   │         │ │
                        │ │    ░▒└──  ─┘┘─┐ │ •░──   │░░└── └┐───┐┘  ──░│    ░│   │  ────── │ │
                        │  ──  •░░░   ░░░░│   ░░░░   └──░░   │░░░│   ░░░│  ───┘      ░░ ░▒░   │
                         ─┐      │        │      ──        • │   │                      ──┐  ─┘
                          └── │  │     ┌─┐ • │     •   ─┐   │ ┌─┐     ┌─┐ •  ┌─┐ │   ┌─   │
                              │░░│     │░│   │ ░░│ ░│ │░│   │ │░│ ░ │ │▒│ ░│ │ │ │ ░ │░│ ░│
                             ─┘──┘  ───┘─┘ ──┘───┘ ─┘─┘─┘───┘─┘─┘ ──┘─┘─┘ ─┘─┘─┘─┘── └─┘──┘
                                  ──      •       •              •       •
                                                                              ┌──────  ┌─ ────
                                                                              │      • │ •
                                                                               ──── • •   ───
                        │ │    ───── ──┐─┐─┐                                                  │
                        │ │   │░ ▒░░│ ░│ │░│                                                │ │
                        │ │   └─────┘ ─┘─┘─┘                                                │ │
                        │ │  │                                                              │ │
                        │ │  │░░─┐         ┌─┐    ───    ───       ──          ────┐─   •   │ │
                        │ │   ── │ │░ ──── │ │ ──┐    ┌──   ────  •  ┌───  ──┐─░░░░│   •    │ │
                        │ └─     └─┘─     │ • │  │   ┌┘   •     •   ─┘░░░──  │░░──   ── ┌─┐─┘ │
                        │   •  │░│        │   │      │░  │ •   ░░• │ └───  ──┘──    • ░ │░│   │
                         ─── ──┘ └────     ───┘ ─────┘   │    •   ─┘─    ──     ── │     ─┼──
                            •  ░░│ ░ ░ ░░░     ░░     │ ░ │ │ ░░     ░│░ ░ ░ •░░ ░ │ │░│  │
                             │  ─┘─┐ │ ─── ░•  ──     │ • │ │ ─── ░─┐ │░   ░  ───┐ │ │ │ ┌┘
                             └──   └─┘─   ── ──  ───── • ─┘─┘─   ── └─ ──────    └─┘─ •  │
                                ───                                          ────










































```

*Figure from page 19 (2346x3317 px)*


---



4203-E P-230


#### SECTION 2 PROGRAM OPERATION

This function searches for a specified character-string. It is also possible to advance or return the edit



pointer by the specified number of lines.



(1) Search for Character-string



Example: To search "X300" in the following program



{a) The character-string specified by keying-in operation is searched for, starting from the



character which is next to the one located by the edit pointer.



(b) When the specified character-string has been found, the edit pointer stops at the first



character of the character-string.



(c) To specify a character-string, key in a character before and after it. Here, the character before



and after the character-string must be the same, and the following characters cannot be used.



+, -, ,, ;, :,



through 9, space, and characters used within the character-string



Example: /X300/



(d) The symbol"?" which specifies an arbitrary character can be used.



Example: /N?01/



This is the command to search for three-digit N codes whose lower two digits are "01 ".



Once a character-string has been specified, it is searched for each time function key



[F1] (FIND) and the WRITE key are pressed.



(e) The symbol



"L.J "



in character-strings represents one character other than numbers and a



decimal point.



Example: /X10



L.J /



With this command, character-strings such as X100, X10.5, and others are not



searched for.



(f) Pressing any key on the operation panel interrupts this function at the point the key has been



pressed.


```text


                                                                                                ──
                                                                         ┌───────┐───┐──────────░░░───────░│
                                                                         │░░░░░░░│ ░ │░░░░░░░░░░───░░░░░░░─┘
               ────     ───────────────────────────────────────────────── ───────┘───┘─────────
          ┌────    ─────                                                                                    │
          │    ── │░░   ┌───────────────────────────────────────────────────────────────────────────────────┘
          └────   └──── │
                 │       ──  ──    •       ──────  ───────┐─┐─────┐──────┐─┐─────┐───┐──────────┐─┐───┐──┐──┐
                 │  ──     ──  ░───░│ ─────░ ░   ──  ░ ░ ░│ │░  ░ │  ░ ░░│ │░░░░░│ ░ │ ░░░░░  ░ │░│ ░ │░ │░░│
                 └──░░─────░░ ──░░░─┘─░░░░░──── ░░░┌──────┘─┘─────┘──────┘─┘─────┘───┘──────────┘─┘───┘──┘──┘
                 │  ┌─      │                  ────┘
                  │░│ │░░░ ░│ ░  ░ ░░░░░│ ░ ░░│
                  │ └─┘   ┌─┘       ──┐ └─    └─┐─┐──────────────┐
                  │░░░░░░░│ │░  ░░░ ░ │░░░░  ░ ░│ │░░░░░░░░░░░░░ │
                  └─────  └─┘      │   ───        └───      ──     •        ──   ──
                        ░─┘ └──────┘───   ───┐────     •  •   ─── • •     •   ──   │ ┌─────────── ─┐
                    ──    │                  │     ┌─   • ░  •       ─────      ───┘ │    ░        │
                       •░•░ ───────── ────░──┘─────┘░───░░•░•░░─┐────░ ░░░┌──
                   ┌───                                       │ │         │  ─────┐─┐───┐────┐────┐
                   │░   │░░────┐ ░░░░░░───░──░ ┌───░░░░│ ░░ ░░│ ░░░ ░░ ░│ │░│ ░░░░│ │░░░│ ░ ░│ ░░░│
                   └───┐┘──░░░░└──────┐░░ •░░──┘░░ ────┘──────┘─────────┘─┘─┘ ────┘─┘───┘────┘────┘
                       │       │      │                                      •                         •
                       └───────┘───┐──┘───┐ ┌───┐ ───   ──      │   ░  •  • •░ │   │   │ ┌┐─    ────  • • │
                    ───┘           │      │ │   │            │  │       •      └─┐─┼───┘─┘┘         │     │
                       │░ ─── ──┐  │      │ │   ░│ │ │  ░  ░ │░░░• ░░░ │░ ░░  ░░░│ │░░ ░░░│  ░░░  │░│ │░░┌┘
                       │        └─               │ └─┘        ───      └─  • ─── │    ┌─┐    ┌────┘─┘─┘──┘
                       └───────   •     ░─── │   │ │ │                    │ │░     ░  │ │   ░│
                       │      ░• •  ░  ──   ─┘───┘─┘─ • ──────────────────┘─┘─────────┘─┘────┘
                          ─────   ─────
                    ┌─  ──     ──┐     ──┐─┐──────┐──────┐────┐──────┐─┐─┐─┐──┐───┐
                    │░ │ ░░ ░░░░░│  ──░ ░│ │░░ ░░░│ ░ ░ ░│░░░ │░░░░░░│ │░│ │░ │░░░│
                    └─ │       ┌─┘    ───┘─┘──────┘──────┘────┘──────┘─┘─┘─┘──┘───┘
                       │      ┌┘ │   •
                        ──────┘  │ ─┐  ─┐──────────────────────────┐─┐─┐──┐────┐─┐─────┐──┐─┐─┐─┐──┐──┐────┐
                                 │ ░│ ░ │░ ░░░░ ░░░ ░ ░░░░░   ░ ░░░│ │░│░░│░░░░│ │░░░░ │░░│ │░│ │░░│ ░│ ░  │
                                 │                                       ─┘    │ │  •   │ │ └┐  └──   └┐  ─┘
                                 └─ ░─┐─── ░ •  ─── ┌──────░░░───░░──░──   ░ ░░░│ ░• ░░ │░░• │ ░ ░ ░░░░│ │░│
                                 │░── │░░░───░──░ ░─┘░░░░░ ───░ ░──░░•░░      ──┘   •   └──         ───┘─┘─┘
                   ┌─┐─     ─────     │                                   ────   ──┐ ┌─┐   ───────┐─
                   │░│ ┌────░ ░░ ──   │  │░░ ░░░│ │░░│░│ │░│░░░░░│ │░│ ░ ░░░░░│ │░░│ │░│ ░ ░░░░ ░ │░░  │
                   └─┘ │░    ░ • ░░    ──┘──────┘─┘──┘─┘─┘─┘─────┘─┘─┘────────┘─┘──┘─┘─┘──────────┘────┘
                       │           ──┐
                       │░░░░░░┌─ │░ ░│   │
                       └──────┘  │   │   │  ─────── ──────────────  • ────   ────  ┌────   ── • ──
                                 │░──┘───┘──                      ─┐ │    │        │    │ │  │ │  ─┐───┐ │ │
                                 │           ───────────────────── └─┘────┘  ───── └────┘─┘──┘─┘── │   │ └─┘
                                 │ ─────────┐
                    ┌──      ─┐──┘          └┐─────┐──┐───┐─┐───────┐─┐───────┐────┐────────────┐──┐─┐───┐
                    │░ │ ░───░│ ░ ░ ░│ │░ ░░ │░░░░░│  │░░░│ │░░  ░░░│░│ ░  ░░░│ ░ ░│ ░░░░ ░░░ ░░│ ░│ │░░░│
                    └─ └──░░░░└──────┘─┘─────┘─────┘──┘───┘─┘───────┘─┘───────┘────┘────────────┘──┘─┘───┘
                          • •































```

*Figure from page 20 (2346x3317 px)*


---



4203-E P-231



SECTION 2 PROGRAM OPERATION



>> N101



N102



N103



N104



N105



N106



N107



file end



>EX



>F /X300/



[fJ>o



G01



GOO



G01



FIND CHANGE COPY



X800 Z200



X250



Z150 F0.3



X300



X310 Z200



X200



Z100


#### PAGE INSERT

MOVE EXTRACT MOOE MODE [EXTEND]



@J @J@@ @@J @J



Press [F1] (FIND).



Key in "/X300/' through the keyboard.



Press the WRITE key.



N101 GOO X800 Z200



N102 X250



N103 G01 Z150 F0.3



>> N104 1]1300



N105 GOO X310 Z200



N106 X200



N107 G01 Z100


```text


                                                                                                 ──
                                                                          ┌──┐─┐────┐─┐──────────░░───────░─┐
                                                                          │░░│ │░░░ │ │░░░░░░░░░░──░░░░░░ •░│
           ┌───────────────────────   ─────────     ──────────────────────┘──┘─┘───   └─────────
           │                       ───          ─┐─                                                         │
           └─────────────┐  ───         ┌──────  │░│ ────────┐── ──────── ───  ──────────────┐ ┌────────────┘
                         │ │   │  • •░• │      ──┘░│         │░░│        •░░░┌─              │ │
                         │ │   └─  │ ░░│         │ │         └──┘         ┌─ │        ───┐   │ │
                         │ │       │ ░░│         │ │         │  │         │  │           │   │ │
                         │ │       │░░░│         │  │        └─░│        │   │        ───┘   │ │
                         │ │       │ ░░│         │  │        │░ │        │   │               │ │
                         │ │       └┐░┌┘         │ │         └──┘         │  │               │ │
                         │ │        └─┘          └─┘                      └──┘               │ │
                         │ └───────                  ────────    ─────────    ───────────────┘ │
                         │ │          │                      │                               │ │
                            ──────────┘────────────────────┐ └───────────────────────────────┼─
                         │ │                               │░│                               │ │
                         └─┘     ──┐──                     └─┘                               │ │
                         │ │  │    │                                                         │ │
                         │ │  │ │                                                            │ │
                         │ │  │░│ ───┐  ───┐───────┐───────                        ────────┐ │ │
                         │ │  └─┘─  ░│     │       │                   •      ───┐─        │ │ │
                         │ │ │     ──  ────┘   ┌──  • ┌──┐ ┌────────  │░│    │░░░│  ─┐─────┘ │ │
                         │  ─┘┐─░┌─   │░░░░   ─┘░░──  │░░└─┘░░░░░░░   │░│    │░──┘   │░░░░░    │
                          •   │  │    └─ ── │  └──    └──   ───  ──┐             │ • └─ ────  •
                           ──       │ │ │   └──          •     ┌─  │     │        •    •
                             │  ░ ░ │ ░ │░│ ░   ░░   ░ ░░░ ░ ░ │░│ ░  ░░░│  ░ ░ ░ ░   ░░  ┌┐
                             └┐──┐─ └───┘─┘ ──────┐ ── ──────┐ └─┘ ──────┘ ── ─────────── └┘
                              │  │                └─  •      └─   •       •  •           •
                              │    ░     ░░│               ┌─┘
                              └────────────┘   ────   ───  │░└───────────
                                                   • •   • │  ░     ░  ░
                                                ─── │      │░•      ───  ──
                                                    │                  •▒  │
                                                    └───────────── •  │    │
                                                                    ──┘▒░ ░│
                                    ──           ──          ┌──      └─   └─                  │
                           ┌────── │ ░│          ░░          │░░  ────  ─┐─░░ ───────     ───┐ │
                           │       │ ░│         │  │         └──┐        │  │        ┌───┐   │ │
                           │      │░░░│         └┐░│        │   │        │ ░│        │  ░│   │ │
                           │      │░ ░│         └┘ │        │░──┘        │  │        └───┘   │ │
                           │      │░ ░░•        │  │        │░░░│        │░ │                │ │
                           │       │ ░│         │  │         ───┘        └┐ │                │ │
                           │       └──┘         └──┘                      │ │                │ │
                           └───────     ────────                           ─┘────────────────┘ │
                           │                                                                 │ │
                            ─────────────────────────────────────────────────────────────────┘─



































```

*Figure from page 21 (2346x3317 px)*


---



4203-E P-232



SECTION 2 PROGRAM OPERATION



(2) Edit Line Shifting



Example: When the 4th block is specified in the following program



(a) This function shifts the edit line by a specified number of lines.



(b) The edit pointer is placed at the first character of that line.



(c) On the display screen, the display changes so that the edit line is located on the first line of the



screen.



{d) When the specified number is larger than the last line of the file, the edit pointer is placed in



the line next to the last line. In this case, two lines from the last line are displayed on the



screen, followed by the following message on the command line.



file end



(e) When a negative number is specified, the edit line shifts backward and the edit pointer is



placed at the first character of the specified line.



(f) When a negative number exceeding the first line of the file is specified, the edit pointer is



placed at the beginning of the file. The message "beginning of file" will be displayed on the



command line.



>> N101 GOO [3800 2200



N102 X250



N103 G01 2150 F0.3



N104 X300



N105 GOO X310 2200



N106 X200



N107 G01 Z100



>F 4



FINO



CHANGE



COPY



WVE



EXTRACT


# I ~: l: ~ l

[EXTEND}



~@J@J@@J@J@J@J



Press [F1) (FIND).



» [Mias



Key



N106



N107



in "4" through the keyboard.



GOO



G01



Press the WRITE key.



X310 2200



X200



2100


```text


                                                                                                ──
                                                                         ┌─┐─────┐───┐─────────░░░────────░│
                                                                         │░│░ ░░░│ ░ │░░░░░░░░░ ── ░░░░░░░─┘
          ┌───────  ──               ────────────────────────────────────┘─┘─────┘── └─────────
          │       ──  ─────────┐─────                                                                      │
          └──────   ─┐░ ░      │ ░   │                                   •       ──────────────────────────┘
                 ─── │     ┌── │     └─────┐───────────────────────────── ─── ───
                     │░ ░░ │░░─┘─░ ░• ░   ░│ ░░          ░        ░      •   •
                       ─── └──    ──       │   ──   ──── ───    • ──  ──    • ────
                    ┌─    │   ───┐  ──────┐ ┌──  ───    │   ──┐  •  ─┐  ── •
                    │░ │ ░│ │░░░░│ •░░░░ ░│ │░░ │░ ░• ░ │░░░░░│ ░░░░░│ │░ ░░░│
                   │   │   ─┘┐       •    └─ •  │    •  │      ┌─  │  ─┘ ┌───┘
                   │░│ │ ░  ░│ ░░░ ░│ ░ ░░░░░ ░░ ░░ •░░ ░░░ ░░░│ ░ │░• ░░│
                   │ │       └┐─   ┌┘ •   ┌─┐ • •    • ──    • │ ┌─ • ┌─ └┐────────────────┐───────────────
                   │░│ ┌───░│ │░░░░│ │░░░░│ │░ │░░░░│ │░░░░░│ ░│ │░│ ░│ │░│         ░░░  ░ │    ░ ░     ░ ░│
                   └─┘ │   ─┘─┘────┘─┘────┘─┘──┘────┘─┘─────┘──┘─┘─┘──┘─┘─┘────────────────┘───────────────┘
                       │
                    │  │░  │  •  ───────   ─── • ─┐───   • •   •   •   ──  •     •    •        • ─── ───┐
                    │  │   │    •░      ───   │   │  ░• • • ──┐ ──┐ ───  ┌─░──┐── ───░ ───────░ │░░░░   │
                       │ ░ ░░  ░░░ ░ ░░ ░░░ ░░│ •░ ░░░ ░░░  ░░│  ░│ ░ ░░ │░ ░░│ ░   ░• ░░░░░░░░─┘───────┘
                       └────────░•░░░•░──────░░ ░░ ░──░░░░░░ ─┘┐┐─┘──░ • │ ░──┘── ──  • ───────
                       │        • ─── •      ───────  ───────  └┘    ── • ──
                      •░░░ ░░•
                   ┌─┐ │      ──────────────┐───┐──────┐  ────────┐────┐─────────────────────────────┐
                   │░│ │░░──── ░░░░░░░ ░░░░░│ ░ │░░ ░░░└──   ░░ ░░│ ░ ░│ ░░ ░         ░    ░     ░   │
                   └─┘ └──      ┌───────      ┌─┘ ░ ──           ─┘────┘─────────────────────────────┘
                       │   ──   │           ──┘       ───────
                    ── │                             •            •     ──   ──  ───    •  ── •  •
                       └────────┐──────────░──── ░░░░ ░──░ ░░────┐ ░─── ░░ • ░░░ ░░░┌─░│░──░ •░• ░────┐
                       │░░░░░ ░ │░ ░░░░ ░░░• ░ ░───────░░────░░░░└──░░░ ───░────────┘ ░└─░░──░░░──░░ ░│
                       └┐─░░░░•░  ───        •                 ──   ──                    •  ───  ────┘
                        │ ┌──┐ ┌──              ──          ──          ────
                        │ │  └─┘  ──░│          ░░          ░░░          ░░░ ───────        │ │
                        │ │      │░ ░│         │  │        ┌───┐        •   │       ┌─── ───┘ │
                        │ │      │░ ░│         │░░│        │   │       •  ░░│       │  ░│   │ │
                        │ │      │░ ░│         │  │        └───┘        ┌─ │        └───┘   │ │
                        │ │      │░ ░│         │░░│        │░ ░│        │░░│                │ │
                        │ │      │░ ░│          • │        └─░─┘        └──┘                │ │
                        │ │      └───┘            │          •         │  ░│                │ │
                        │ └──────┘                 ────────     ───────┘───┘──────────────  │ │
                        │ │                                                               ──┘ │
                         ─┘───────────────────────────────┐ ┌─────────────────────────────   ─┘
                                                          │ │
                        ┌─┐                               └─                                ┌─┐
                        │ │                                                                 │ │
                        │ │                                                                 │ │
                        │ │  ┌───┐────────┐─┐─────────────                        ────────  │ │
                        │ │  │░ ░│        │ │                         ─┐     ───┐─          │ │
                        │ │          ┌────┘ │ ┌─┐    ┌──┐  ───────   │░│   ─┐░░░│  ┌┐─────┐ │ │
                        │  ─── ░░•   │░░░░   ─┘░└─── │░░└──░░░░░░░│  │░│    └───┘  └┘ ░ ░░│   │
                        └─           └─────   └─┘    │  │  ───────┘             │       ──┘  •
                          ──┐  ┌─    │        │ │ │   ┌─┘            │     │
                            │░ │ │ ░   ░░   ░ ░ ░ │   │░│ ░░   ░ ░ │ │░░ │ │ ░│  ░░ ░ ░ ░│
                            └──┘ │ ─────── ── ─── └─┐ └─┘ ── ─── ──┘ └── └─┘ ─┘─ ── ─── ─┘
                            │  │░│           •   •  └─      •   •   •   •   •      •   •
                            │░ ░░ ░ │░ ░░│               │
                            └───────┘────┘     ┌───────┐─┼─┐─┐────────
                                               │ ░     │ │░│ │░ ░░  ░░•
                                               └───      └─┘ └─ ─────  ┌┐
                                                    ─── ─┘  •  •     ┌─┘┘─┐
                                                   •      ──         │ ░ ░│
                         ───────      ─────────   •                  │░───
                        │         •            ┌─┐                   └─   ┌┐───────────────┐─┐
                        │ ────┐  │░── ──────── │ └┐        ┌───        • ─┘┘               │ │
                       │ │    │  │░░░│         │  │        │░░░──────   │  │ ──────────────┘ │
                       │ │     • └───┘         │ │         └───         │  │               │ │
                       │ │                     └─┘                      └──┘               │ │
                       │ │                                              │                  │ │
                       │ └─────────────────────   ──────────────────────    ───────────────┘ │
                       └─                                                                  │ │
                         ──────────────────────────────────────────────────────────────────┘











```

*Figure from page 22 (2346x3317 px)*


---



5-10. Change



4203-E P-233



SECTION 2 PROGRAM OPERATION



Example: To change "Z200" in N 105 block to "221 0" in the following program



(1) This function replaces a specified character-string with another character-string specified.



Press function key [F2] (CHANGE) to select this function.



(2) The edit pointer is placed at the first character of the character-string which has replaced the



previous character-string.



When the specified character-string is not found, the message "no character string" is displayed and



the edit pointer does not move.



(3} The same delimiter as explained in 5-9 is used.



(4) The symbol "?" is used in quite the same manner as in 5-9. "Find" operation.



(5) When program data contains several same character-strings, press function key IF2]



(CHANGE) and the WRITE key. The character-strings will be replaced one by one.



(6) Pressing any key on the operation panel interrupts this function at the point the key has been



pressed. In this case, character-strings are not replaced.



(7) The following option code can be used:



";A" When this option code is designated, global search and replace can be executed. The



character-strings are replaced at one time.


```text


                                                                                                ───      ──
                                                                          ┌─────┐─┐────┐──┐─────░░░──────░░│
                                                                          │░░░  │░│    │░░│░░░░░──░░░░░░░░─┘
                            ───────────────────────────────────────────── └─────┘─┘ ───┘──┘─────      •
           ┌──┐─    ────────
           │  │░┌──┐        •
           └──┘─┘  │     ░ │              •
                  │░      ─┘ │ ───────   • │    ──────────── ┌─── ─────────────────────┐
                  └── ─┐──   │      ░   •  │                 │              ░░ ░   ░░░ │
                  │  • │   ── ───  │ ───    ──────    ──────┐  ─────┐─┐   ┌─ ┌─┐     ─┐ ┌─────┐────┐─┐
                  │ │  │░• ░  ░░░│ │░░░░░• • ░░░░░░│ •░░░░░░│ │░░ ░ │░│ ░ │░░│ │░░ ░ ░│ │░░   │░░░░│░│
                  └─┘ │ • •      │ └┐     • │      └┐ ──┐   └─┘ │     └─┐─┘──┘─┘──────┘─┘─────┘────┘─┘
                      │ ░░░░ ░░░░░• │░░ ░░░ │░░░░░│░│ ░ │░░░░ ░░│ │░░░░░│
                  ┌─┐                           ─┐┘─┘   │     ┌─ ─┘     └───┐─┐─────┐─────┐─┐─┐─────┐───┐
                  │░│  │░───░░ ┌─░░─── ░░──── ░ ░│ ░░░  │░ ░░░│ │░░│░ ░ ░ ░░│ │░░░░ │░░░░ │░│ │░░░ ░│ ░░│
                  └─┘  └─░  ───┘░──  ░───      ──┘ ──── └─────┘ └──┘─ ──────┘─┘─────┘──── └─┘─┘─────┘───┘
                      │                      ──   •    •       •     •                   •               ──
                      │░░░░•░░░ │░░░░░░   ░ ░░░  ░    ░    ░     ░  ░░          ░
                      └───┐ ─── └────── ──┐──┐   ────────────────────────────────────────────────────────────
                      │   └─   ─┘         │  │
                  ┌─┐ │           ───    •  ─┘── ─┐─────────┐──┐
                  │ │ │  ░  ░ ░  ░░ ░ ░ │░ •░░░░░░│ ░ ░ ░ ░ │░░│
                  │ │ │      ─── ───┐   └─┐ ─┐     ─┐          └─┐────────┐────┐─┐────┐──┐
                  │░│    ░ ░░ ░░•   │░ •░░│  │░░░ •░│ ░░░░ ░ ░░░░│ ░   ░ ░│ ░░ │ │░░░░│  │
                  │ │                                                                     ───────┐
                 │░░│  ┌───────░░░── ░░░ ───░░ ───░ ░─┐ │░░────░░░•░───░░•░── ░░░────░░░── ░░ ░ ░│
                 └──┘  │░░░░░░░───   ░───░░░───░  ───░└─┘──   ░─── •   ──░•   ───    ───       ┌─┘
                      │                                             │ •                      │ │
                  ░   │  ───            •░        ──            •   │       │                └─┘────────┐
                  ──  │     •░        ──    ─────   ──     •      ──┘──     │             │░   ░      ░ │
                      │░┌──░░─────── •░░░─── ░░░░── ░░─── ░ ░ ░░─┐░░░░░░────┘─────────────┘─────────────┘
                  ┌─┐ │ │           •                     ────── └──────
                  │░│ │░ ░ ░ ░░░░░──░•░  ░ ░░ ░░  ░  ░░░░•
                  └─                                      ────┐────┐─────┐─┐──┐─┐────┐─┐─┐──┐─┐───────┐─┐───┐
                      ─┐─────░░─── ──░░░░─────░• ──░░░░░ •░░░ │░░░░│ ░░░ │ │ ░│ │░░░░│ │░│ ░│ │░░░ ░░ │ │░░░│
                       │░░ ░░░• ░░•░░ ─── ░░░░•░░ ░ ───── ────┘────┘─────┘─┘──┘─┘────┘─┘─┘──┘─┘───────┘─┘───┘
                       └────── ─── ──    ───── ────













































```

*Figure from page 23 (2346x3317 px)*


---



» N101



N102



N103



M104



N105



N106



>C /210/200/



file end



file start



>C /2200/2210/



G01



GOO



xaoo



X250



X300



X310



X200



4203-E P-234



SECTION 2 PROGRAM OPERATION



2250



Z150 F0.300



2200



FIND



CHANGE



COPY



~VE



EXIBACT


# I :~ I

~~~



[EXTEND]



@ @J@@ @J CED@ @J



\ Press [F2] (CHANGE).



Key in "/Z200/2210i through the keyboard .



Press the WRITE key.



N101 GOO X800 2250



N102 X250



N103 G01 2150 F0.300



N104 X300



>> N105 GOO X310



l}r.210



N106 X200


```text


                                                                                                ──
                                                                         ┌──┐─┐────┐─┐──────────░░─────────┐
                                                                         │░░│ │░░░ │ │░░░░░░░░░░──░░░░░░ ░░│
          ┌───────────────────────     ────────    ──────────   ───────── ──┘─┘───   └─────────      •
          │                       ─── •        ───┐          •                                             │
          └─────────────┐ ┌───┐      │  ──────  ░ │  ──────┐─ ──┐───────┐───  ──────────────┐ ┌────────────┘
                        │ │   └───┐─░└┐─      ──┐░└──      │░░░░│       │░░░┌─              │ │
                        │ │       │ ░░│         └─┘         ┌──┐         ┌─ │        ─────┐ │ │
                        │ │       │░ ░│         │ │         │  │         │ ░│           ░ │ │ │
                        │ │       │░░░│         │ │         │░─┘         │  │        ─────┘ │ │
                        │ │       └┐░┌┘         └─┘         │░░│         │ ─┘               │ │
                        │ │        └─┘                      └──┘          •                 │ │
                        │ └───────   │              ──────┐     ─────────    ───────────────┘ │
                        │ │          │                    │ │ │                             │ │
                           ──────────┘────────────────────┘ └─┘───────────────────────────── •
                                                          │░│
                        ┌─┐          ───┐                 └─┘                               ┌─┐
                        │ │  ┌────┐──░░░│                                                   │ │
                        │ │  │    │░░                                                       │ │
                        │ │  │░   │ ┌────┐──────────┐─────   ─────                          │ │
                        │ │  └────░░│░░░░│          │             ──  ─┐ ─── ───┐───        │ │
                        │ │       ─┐┘    │  •  •      ──┐ • •    •   │░└┐   │░░░│           │ │
                        │ └──┐ │░│ │  ░──┘    •░•    │░ │    ────    │░░│   │░░─┘── ┌─────┐─  │
                        │    │ │ └─  │   │   │       │   │ •     •   └─ │   └─      │     │  •
                         ─── └─┘─┘ ──┘ ┌─┘ ──┘ ┌─┐───┘   │   ─┐─┐ ───   └──    ┌── ─┘┐─   └──
                             │  ░│   ░ │ │ ░ ░ │░│    ░ ░ │ ░ │░│ ░ ░ │░│    ░░│ ░ ░ │░│  │
                             │  ─┘ ░── │░│ ────┘─  ────── │ ──┘─┘ ────┘─┘ ── ──┘─┐─┐─┘─┘ ─┘
                              ──  ──  ─┘─┘               ─┘      •       •  •    │ │    •
                                            │░░░  ░ ░░░░░░░•
                                          ──┘─────────────  │
                                                           ─┘    •
                                            ┌──           │░└──── ┌───────┐
                                            │   ──────────┘ │    ─┘       │
                                                          │░└─      ──┐── │
                                                   │       ░ ░        │▒░│
                                                   └────── ────────  │░  │
                                      ─────────                    ──┘▒░░░│
                        │          •           ┌───          •        ──  └─                  │
                        │ ┌────── │░─┐ ────────┘░░░         │░│         │░░░               ─┐ │
                        │ │       │░░│         │  │         └─┘┐        │  •         ┌───┐  │ │
                        │ │       │░░░│        │  │         │  │        └─ ░•        │░ ░│  │░│
                        │ │   ┌─  │░░░│        │  │         └──┘        │  │         └───┘  │ │
                        │ │   │   │ ░│          │ │         │░░│        │░ │                │ │
                        │░│   └─  └──┘          └─          └──┘         ──┘                │ │
                        │ └───  •     ─────────    ─────────┘                ───────────────┘ │
                        └─┘                                   │                             │ │
                           ───────────────────────────────────┘───────────────────────────── •



































```

*Figure from page 24 (2346x3317 px)*


---



5-11. Copy, Move, and Extract



4203-E P-235



SECTION 2 PROGRAM OPERATION



These functions are used 10 transfer a group of commands from one program to another or to insert the



same group of commands into several different positions of a program.


#### N101


#### N102

-~---~---·-·-·-·-·-



i N103 i



j \ •



, N121 . .



-·-·-·-·-·-·-·-·-·-



N122



N123



N215



N216



N103



, N121



. .



-----~-·-·---~---·-


#### N217


#### N218

Extract buffer



r·-·-·-·-·-·-·-·-·-·-·-·-·-·,

• N103



To other areas



\ Stored



---·-·-·-·-·-·-·-·-·-·~



Fig. 2-1 Copy, Move, and Extract Functions



Operation sequence:



(1) Save the group of commands into the extract buffer using the COPY of MOVE command.



(2) The EXTRACT command will insert the commands saved in the extract buffer into the specified



sequence.


```text


                                                                                                ──        •
                                                                          ┌─┐───┐─┐───┐─────────░░────────░──
                                                                          │░│░░ │░│   │░░░░░░░░░ •░░░░░░░░•░
            ─── ───    ───    ───────   ── • ─────────────────────────────┘─┘───┘─┘─  └─────────
           │   │   ────   ┌───       ┌──  • •                                                               │
           │   └──┐       │   ──     │     •  ──────────────────────────────────────────────────────────────┘
           └───┘  │   ░ ░ │░   ░  ░  └─    ░░•
                                               ─┐                ────  •      ──────┐─────────┐─────────┐─┐─┐
                 ┌─  ░───    ──────────   • ░   └───░─────────── ░░░░──░──────░░░░ ░│ ░  ░░░ ░│ ░ ░   ░░│ │░│
                 │░ ── ░ ░░──░ ░░ ░░░░░░• ░─────░ ░ ░░░░░░░ ░░░░░────░░•░ ░░ ░──────┘─────────┘─────────┘─┘─┘
                 └──  ─────           •   •      ────────────────    ── ──── •

                           │░┌───      ────────┐ │
                           │░│    ┌───┐        │ │
                           │ │    │░ ░│        │ │
                           │ │    │  ░│        │ │
                           │░│ ┌─ └─┐░└────  │ │░│
                           │░│ │  │ │ │    ──┘  ░│
                           │░│ └─ │░│░│ ───    ┌─┼─
                           │░│    │ │ │    ────┘░│ ──────────────┐
                           │░│    │░ ░│        └─┼─   ░ ░        └────────            ───────
                           │░│    │░ ─┘        │░│ ────────    │ │        ┌────┐──┐─┐        ┌─┐
                           │ │     ── │        │░│         │   └─┘        │░░░░│  │░│        │ │
                           │░└────    │ ───────┘░│         └───┘░│ ┌─┐───┐┘  ┌─┘──┘─┘        │ │
                           │                   │ │             └─┼─┘ │  ░│░░┌┘         ───┐  │ │
                             ──────────────────                │░│ │ │ ──┘──┘     ┌────   │  │ │
                                                               │░│ └─┘      │     │       │  │ │
                            • ─────────────────                └─┘─┘░│ ──░░░└─            │  │ │
                           │░│                 │ │        ─────┘░        ───  ─────── ────   │░│
                           │░└────     ────────┘░│             └────   ┌─                  • │░│
                           │░│    ┌───┐        │ └────  ───── •      ┌┐┘  ───────────────── • •
                           │░└─ • │░░░│ ──── ──┼─┘      ░░░░░│     • └┘
                           │░│░│  └──░│     │░ │░└───── ─────┘   ┌─░
                           │ │ │  │ ░─┘     │░─┼─┘              ─┘  ────┐
                           │   └─ │   │     │  │ │             •  • ░░░░│
                           │  ░│  └─┐─      │  │░│           ┌─  • ─────┘
                             ──┘─ │░│   ────┘─ │░│          ┌┘  •
                          │ │     └─┘──        │ │         ┌┘░ │
                          │ │                  │ │       ┌─┘░──┘────
                          │  ────      ────────┘ │       │   ░   ░
                          └──                    │          ──── ───
                             ────────────── ──┐  └─┐───┐─┐─┐    •    ────┐─────────┐
                                           │░░│ ░│ │░░░│ │░│ │ │░░░░░░ ░░│░ ░░░░░  │
                                           └──┘──┘─┘───┘─┘─┘─┘─┘─────────┘─────────┘
                ────────┐─┐────────┐
                  ░░░░░░│ │░░░░░░░ │
                 •  ┌─┐ └─ •      ─┘─────────────┐─┐──┐──────┐──┐─┐──┐──┐──┐─┐───┐─┐──┐───┐─┐────────┐
                  │░│ │░░ ░ ░░ ░░░░░ ░ ░  ░░░░░░ │░│ ░│ ░░░ ░│ ░│░│  │░░│ ░│ │░░░│ │░ │░ ░│ │░ ░░░░░░│
                  │   │          • ──       ──┐  │ └─  • ─┐ ─┘  └─┘ ┌┘  │ •   ── └─┘  └─  │ └─┐  ┌─ ─┘────┐
                 │░░│ └─────░░░░░░│   ░░░ ░ ░ │░ │░░░░ ░│ │░ ░░░  ░ │░░░░ ░│░│  │░ ░│ ░ ░░│ │░│ ░│ │░░░░░░│
                 └──┘ │░    ──────┘───────────┘──┘──────┘─┘─────────┘──────┘─┘──┘───┘─────┘─┘─┘──┘─┘──────┘
                      └─────






























```

*Figure from page 25 (2346x3317 px)*


---



4203-E P-236



SECTION 2 PROGRAM OPERATION



5-11-1. Copy



This function transfers specified program data to the extract buffer.



Press function key [F3] (COPY} after the range (in terms of lines) of program data to be duplicated has



been specified.



Example: To copy blocks from "N103" to "N105" in the following program



(1) Program data in the specified range which starts from the edit line(>>) is transferred to the



extract buffer.



{2) The edit pointer is placed at the first character of the line that is preceded by the last line of the



specified range.



(3) Program data previously registered in the extract buffer is erased.



(4) When the specified number is larger than the last line of the file, program data up to the last line



is transferred.



(5) When a negative number is specified, program data in the blocks preceding the edit line (edit



line not included) is transferred.



When a negative number exceeding the first line of the file is specified, program data up to



the first line of the file is transferred.



(6) Pressing the WRITE key without entering the number of lines causes program data in the edit



line to be transferred.



{7) When an attempt has been made to transfer program data which is larger than the extract



buffer, the message "extract buffer overflow" will appear on the display screen and copy



operation is not executed.


```text


                                                                                                ──        •
                                                                         ┌────────┐───┐───┐─────░░░──────░░│
                                                                         │░░░░░░░░│   │░░░│░░░░░ ──░░░░░░░─┘
                        ───────────────────────────────────────────────── ────────┘─  └───┘─────
           ┌──      ────                                                                                    │
           │  ┌── │                                                  ───   ─────────────────────────────────┘
           └──┘   └──  ┌────────────────────┐─────────┐───────┐─┐────   ──┐
                │░   ──┘ ░       ░        ░░│         │      ░│ │         │
                │  ──      │ • •            │ ┌─    │ │       └─┘          ────────────────────────────────
                 │ ░░│ •░░░└─ ░░│ ░ ░ ░░░░░   │░░  ░│ │░ ░│ ░ ░           │ ░           ░
                 └───┘  ──   ───┘─────────────┘─────┘─┘───┘───────────────┘─────────────────────────────────

                │░      ─────            ░    ░                  •   ────────────┐
                └───┐─┐─         • ────┐───     ───  │   ──┐   ── ───            │
                    │ │   •       •    │   ──┐─┐   ──┼─┐─  └─┐─           ┌─┐    └──────┐────┐──┐──────┐
                    │  ───░░░───░│░░ │░│ │░░ │░│ │░░░│ │░░░│ │░ ░ ░  ░ ░│ │░│ ░░      ░ │░░░░│ ░│ ░ ░ ░│
                       ░░░───░░░─┘───┘─┘ └───┘─┘ └───┘─┘───┘─┘──────────┘ └─┘───────────┘────┘──┘──────┘
                  ──┐ •                 •       •                        •
                   ░│  ───────────░│          ░    ░ ░            ░      ░    ──     ─┐  •  ┌───   ───   │
                  ──┘ │            │ ─────────────────────────────────────────  ───── └──  ─┘   ──    ── │
                      │░───────┐───┘                                                     •   ───   ──
                  ┌─┐ │        │    ───────┐─┐────────┐───┐─┐───────┐─┐─────────┐
                  │░│ │ ░░░ ░░ │░░ ░░░    ░│ │░░░░░░░░│  ░│ │░░░ ░░░│░│ ░ ░ ░░░░│
                  │ │              ───      • ┌───  ─┐ ┌─  ─┘ ─┐─    • • │   ┌─ └────┐──┐─┐─┐─┐─┐─┐─┐─┐────┐
                  │░│ │░░░──┐─┐──░░░░░│ ░   ░░│ ░ ░░░│ │░░  ░│ │░│ ░│  ░ │░ ░│ │░░░░░│  │░│ │░│ │░│ │░│ ░ ░│
                  └─┘ └───░ │░│ ░─────┘───────┘──────┘─┘─────┘─┘─┘──┘────┘───┘─┘─────┘──┘─┘─┘─┘─┘─┘─┘─┘────┘
                      │
                  ░   └────    ┌──  │       •   •   ░  ─┐  ──    ┌─┐   ░  │ ────────────────────────────┐
                  ──  │        │░   │        ───  ───── └─   ─── │ │ ─────┘─                            │
                      │        └─ ░░│ ░ • ░░░░ ░░•                                                    ──┘
                      │                  ────     ─────────────────────────────────┐─┐──┐─────┐─┐─┐─┐─
                      │       │ ░   ─┐─      •  •    ░              ░░       ░░░  ░│ │░ │░░   │░│ │░│ │
                      │░  ░   └─────░│ ░───   ── ─────┐────────────────────────────┘─┘──┘─────┘─┘─┘─┘─┘
                      │              │          •     │
                      │             ░│   ───          └──────────────────────┐────┐───────┐─────────┐─┐─┐
                  ──  │      ░ ┌───    •     • •      ░                   ░░ │░░ ░│ ░  ░ ░│ ░░░░ ░ ░│ │░│
                      │ ─────┐─┘░░░─┐──░──    •                           •    ───     ──   ── •      └─┘
                 ┌───        │      │      ──  ──── ─── ──── • ─────┐ ────  ───   ┌───┐  ─┐─  │ ──────
                 │░░  ┌──────┘─░░───┘──░───░░──░░░░│ ░ •░░░░│ │ ░░ ░└─░░░░ ░░░░ ░ │░ ░│ •░│ ░░│ ░░░░ ░│
                 └──  │░░░░  ░░ •░░░░░░  ░░░ ░░ ──░└───  ░──┘─┘        ─── ────     ──┘   └───┘ │ ────┘
                      │  •    •      │      ┌───  •            • ─── ──   •    ────    •  │     │
                      │   ──── •  ───┘   • ─┘                                                    •
                       ──             ─── •







































```

*Figure from page 26 (2346x3317 px)*


---



N101



N102



» N103



M104



N105



N106



N107



GOO XB00



X250



G01



X300



GOO X310



X200



G01



4203-E P-237



SECTION 2 PROGRAM OPERATION



Z200



~50 F0.300



Z200



Z170



Move the symbol "»" to N103 using the cursor control keys.



>CO 3



FIND CHANGE



N101



N102



N103



N104



N105



>> ~06



N107



COPY



PAGE


#### WVE EXTRACT MODE

Press [F3] (COPY).



Key in "3" through the keyboard.



Press the WRITE key.



GOO X800 Z200



X250



G01 Z150



X300



GOO X310 Z210



X200



G01 Z170



INSERT



MODE [EXTEND]



F0.300


```text


                                                                                                ───
                                                                          ┌─┐───┐─┐───┐───┐─┐───░░░░─────────
                                                                          │░│░░ │░│   │░░░│░│░░░──░•░░░░░░░░
           ┌───────────────────────    ─────────     ─────────────────────┘─┘───┘─┘   └───┘─┘───     ──
           │                       ───┐         ────┐                                                       │
           └─────────────┐ ┌──────┐   │ ────────    └───────     ┌──────┐ ──┐┐─────────────── ─┐────────────┘
                         │ │      │   │         ┌──┐┘        │░░ │      └┐░░└┘               │ │
                         │ │    ──┘  ░│         │  │         └──┐       └┘  │        ┌────┐  │ │
                         │ │   •   • ░│         │░░│        │   │       │░░░│        │░ ░░│  │ │
                         │ │    ──┐░░ │         │  │        └───┘       └┐  │        └────┘  │ │
                         │ │      │░ ░│         │░░│        │░░░│        │░░░•               │ │
                         │ │      │░ ░│         └──┘        └─░─┘        └──┐                │ │
                         │ │       ┌──┘         │  │          •          │  │                │ │
                         │ │       │            └──┘                     └──┘                │ │
                         │ └──────      ────────    ────────────────────      ───────────────┘ │
                         │ │                                                                   │
                          • ──────────                     │ │                     ────────────
                                      ┌───────┐───┐───┐────┘─┘─────────────────┐─┐
                                      │░░ ░ ░ │░ ░│   │░ ░ ░░  ░░     ░░     ░ │░│
                                      └───────┘───┘───┘────┐ ┌─────────────────┘─┘
                                                           │ │
                         ┌─┐                               └─┘                               ┌─┐
                         │ │                                                                 │ │
                         │ │                                                                 │ │
                         │ │                                                                 │ │
                         │ │  ───────┐─────┐─┐───────────────┐────┐──              • ──────  │ │
                         │ │         │     │ │               │    │    •     ┌───┐─ •        │ │
                         │ │ │   │    ┌────┘   ──┐    ┌──┐  ─┘────┘   │░│    │░░░│   ┌────── │ │
                         │ └─┘─ ░└─   │░░░░    ░░└──  │░░└─ ░░░░░░ │  │░│    │░──┘   │░░░░▒░   │
                          •      │    └─┐──      │    │  │  ───  • │   •      •      │  ──┐─  •
                           ──┐  ─┘  ┌─  │   ─── •  ──┐ ┌─┘ │   ─┐       │         •  └─   │
                             │  ░│  │░  │▒│    │ │ ░ │ │░│ │░ │░│ ░   │░│ ░ │ ░│  ░│ │░│ ░│
                             └───┘  └───┘─┘┐───┘░│   │ │ └─  ─┘─┘ ┌───┘─┘───┘──┘─ ─┘─┘─┘──┘
                                   •       │    •    ░░ ░ ░ │░░   │              •
                                                 ── ──────┐─┼─────
                                                          │ │
                                                ┌─┐───────┼─┘──────────┐
                                                │░│     ░ │░░ ░  ░ ░░░░└─
                                                └─┘─    • │ │  ──  ───    ─┐
                                                    ┌──┐ ─┘ └──  ┌─    ───░│
                                                    │ ░│     ░   │░│  │░▒  │
                                                    └──┘────     └─┘  │░•
                         • ─────── ┌─┐ ─────────┐──┐         ──           ──┐─────────────── ─┐
                        │ │       ┌┘░└┐         │░░│        │░░│        │░░░│               │ │
                        │ └────── └┘  │ ────────┘──┘─────── └──┘        └───┘ ───────      ─┘ │
                        │ │       │   │                                 │   │        │ ───  │ │
                        │ │       │  ░│         │ │         ┌──┐        │   │        └─     │ │
                        │ │       │  ░│         │ │         │░ │        │   │          ──   │ │
                        │ │       │░ ░│         └─┘         │   •       │   │               │ │
                        │ │       │░ ░│         │ │         │ ░•        │   │               │ │
                        │ │       └┐─┐┘         │░│          ──         │░ ░│               │ │
                        │ │        │ │          └─┘                     └───┘               │ │
                        │ └───────                  ────────────────────     ───────────────┘ │
                        │                                                                   │ │
                         ───────────────────────────────────────────────────────────────────



























```

*Figure from page 27 (2346x3317 px)*


---



4203-E P-238



SECTION 2 PROGRAM OPERATION



5-11-2. Move



This function extracts program data in the specified range of a file and transfers it to the extract buffer.



Press function key [F4] (MOVE) after the range (in terms of lines) of program data to be transferred has



been specified.



Example: To transfer blocks from "N103" to "N105" in the following program



(1) Program data in the specified range which starts from the edit line(>>) is transferred to the



extract buffer.



(2) The lines transferred to the extract buffer are erased from the display screen.



(3) The edit pointer is shifted to the first character of the line next to the last line of transferred



lines.



(4) Program data previously registered in the extract buffer is erased.



(5) When the specified number is larger than the last line of the file, program data up to the last line



is transferred.



(6) After program data has been transferred, the message "**RECORD DELETE" appears on the



command line. Here,



"**"



indicates the number of the specified lines.



(7) When a negative number is specified, program data in the blocks preceding the edit line (edit



line not included) is transferred.



When a negative number exceeding the first line of the file is specified, program data up to the first



line of the file is transferred.



(8) When an attempt has been made to transfer program data which is larger than the extract



buffer, the message "extract buffer overflow" will appear on the display screen and move



operation is not executed.



(9) Pressing the WRITE key without entering the number of lines causes program data in the edit



line to be transferred.


```text


                                                                                                •         •
                                                                         ┌──┐─┐────┐─┐──────────░░───────░░│
                                                                         │░░│ │░░░ │ │░░░░░░░░░░──░░░░░░ ──┘
                 •      ───────────────────────────────────────────────── ──┘─┘────┘─┘─────────
          ┌──────  ─────
          │        ░░   │                                                  ───         •  •        ────
          └─────  •     └──┐────────────────────────┐────────┐────  ───────   ───────── ── ┌─┐─ ───    ──
                │░░░ ░ ░ ░ │   ░░ ░  ░       ░░    ░│      ░ │    •  ░  ░                  │ │ │   •     ─┐
                │            •  │     │    •   ─┐── │ •       •          │          •  •     │ │          └┐
                 ┌──░░ ───░── ░░│ ░ ░ │░░░░░  ░░│ ░   ░  │ ░  ░░░   ░ ░░░│         ░ │░░│   │░     ░       │
                 │  ──    ░  ───┘ ────┘─────────┘────────┘───────────────┘───────────┘──┘───┘──────────────┘
                │         │      •
                │░     ░──┘─░     ░  ░                   ░  ░░             ──── ───
                └─  ────    • •   ───────       • ─── •   ────   • │ ─── ──    •░  •
                                         ┌─────┐ │   │ ┌─     ──┐ ┌┘┐   │  ─┐ │      ───┐──┐─┐─┐───┐──┐
                  •░•   ──░░░───░░   ░ ░ │░░░░░│ │░ ░│ │░░│ │░░░│ │░│ │░│ │░│ │░      ░░│░ │░│ │░ ░│░░│
                      │░░ ───░░░───  ────┘─────┘ └───┘ └──┘─┘───┘─┘─┘─┘─┘─┘─┘─┘─────────┘──┘─┘─┘───┘──┘
                  ┌─  │            ──           •     •
                  │░  │░ ░ ░░░   ░ ░░       ░    ░     ░░│                ░       •      │
                  │   │  ───        ───               ───┘     │                        ─┘┐
                  │░│ └──                                      │                          └───────────
                  └─┘ │     ────────────────────────── •   • ──┘──── •        ───
                      │ ░░                                                       ─────────────────────
                  ┌─┐ │   ───┐─┐─┐─────────┐─┐─────────┐─┐──┐─────────┐───┐─────┐
                  │░│ │░ •░░░│ │░│ ░ ░ ░░░░│ │░░░░░░░ ░│░│  │░ ░░ ░░░░│ ░ │ ░░░░│
                  │   │      │ │     ─┐─┐  └─ ───┐─  │ │ │ • ── •   ┌─┘ ─┐  ─┐─ └┐───┐─┐──┐─┐─────┐─┐─┐─┐─┐
                 │░│  │░░░┌─┐┘░ ░░░░░░│ │░░░░│ ░ │░ ░│ │░│ ░ ░ │░ ░░│ ░│░│░ ░│ │ │░ ░│ │░░│ │░ ░ ░│ │░│ │░│
                 └─┘  └───┘ │░ ───┐───┘─┘────┘───┘───┘─┘─┘─────┘────┘──┘─┘───┘─┘─┘───┘─┘──┘─┘─────┘─┘─┘─┘─┘
                      │           │
                      └──┐         ───  ───────── ──── ───────  ──────    ┌─── ──── ───── ─┐───────┐──────┐
                  ──  │  └─── ░        •      ░   ░           ─┐░  ░░░┌───┘ ░ •    •    ░• │  ░░ ░░│     ░│
                      └──░░ ░ ───░ ───░░░─────── ──┐░─┐─┐────  └──────┘ ░░░░──░───░░•        │   ──┘    ──┘
                 ┌─┐  │                            │  │ │                •            ───┐───┼─┐─   ────
                 │░│  │░░░──────░░──┐── ┌───────░░░░░░│ │ │░░░│ │░░│ ░ ░• │ ░ ░ ░░░░░ ░░░│ ░ │░│ ░░  ░░░•
                 └─┘  └───░░░░░░──░░│ ░─┘░░░░░░░──────┘  ─┘───┘ └──┘     ─┘─       ──────┘ • └─┘────────
                      │                 │              ─┐      •    ────┐   ────┐─┐       │ │           ───┐
                      │░░░─────░░░░ ░ •░ •░░•░░░░░░░░░░░│ ░░░░ ░ ░ ░░░░░│   ░░░ │░│ │░░░ ░│ │░░│      ░░ ░ │
                      └─┐─  ░  ──┐──── ──░•  ─┐─────────┘───────────────┘───────┘─┘─┘─────┘─┘──┘───────────┘
                  •   │ │        │            │
                      └─     │ ┌─┘              ─── ──  • ──── ───    ─── •  ─┐    ───   • • •   ── •
                 ───  │ ─── ─┘─┘ │ ───    ─────   ░│  •          ░────        └────░ ░ ──░│     │░ ░
                      │ ░░░•  ░ ░░░░░░░  ░░░ ░░ ░ ░│  ░░░░ ░• ┌──░░░░░░──┐ │░ ░░░░░░──░░░░│ ░░░ │░░──
                      └───░░───────────────────  ──┘   ────   │  ──────  │ └────────  ──── ─────┘──
                 ┌─┐  │                        ──   ┌─┐    ─┐─         •  •                         ────┐
                 │░│  └─░░░░ │ ░──┐░░•░░ ░░  │░░░ ░ │░│  ░ ░│     ░░│     ░      ░            ░        ░│
                 └─┘  │ ──── └─   └──  ──────┘──────┘─┘─────┘───────┘───────────────────────────────────┘
                      └─    ─┘ ───



































```

*Figure from page 28 (2346x3317 px)*


---



4203-E P-239



SECTION 2 PROGRAM OPERATION



N101



N102



>> N103



M104



Nt05



N106



N107



>M 3



FIND



N101



N102



» ~06



N107



>M 3



GOO xsoo 2200



X250



[§01 2150



X300



GOO X310 2200



X200



G01 2170



Move the symbol·»• to N103 using the cursor control keys.



Press [F4] {MOVE).



Key in "3" through the keyboard.



Press the WRITE key.



GOO



xsoo



2200



X250



X200



G01 2170



The following message ls displayed on the command line.



3 RECORD DELETE



F0.300



FIND



CHANGE



COPY



MOVE



EXTRACT



~6E



~:~



[EXTEND]


```text


                                                                                                ──       ──
                                                                          ┌─┐───┐─┐───┐─────────░░•░─────░░┌─
                                                                          │░│░  │░│   │░░░░░░░░░──░•░░░░░░─┘
           ┌───────────────────────   ───────────   ────────── ────────── └─┘─ ─┘─┘─  └─────────     ──
           │                       ───           ───                     •                                  │
           └─────────────┐ ┌──────┐     ───────      ──────┐     ┌──────     ┌───────────────┐ ┌────────────┘
                         │ │      │   ┌─       ─┐ ───      │ ░░  │      ─┐──┐┘               │ │
                         │ │      └─ ░│         │           ┌───┐        │  │        ┌────┐  │ │
                         │ │      │░ ░│         │░•         │   │       •   ░│       │░ ░░│  │ │
                         │ │      │░░░│         └─ │        └───┘        │   │       └────┘  │ │
                         │ │      │░ ░│         │░░│        │░░ │        │░░│                │ │
                         │ │      │░ ░│         │ ─┘        └─░─┘        └─ │                │ │
                         │ │      └───┘         │░ │          •                              │ │
                         │ │                    └──┘                     ────                │ │
                         │ └──────     ─────────    ────────────────────      ───────────────┘ │
                         │ │                                                                 │ │
                          ─┘──────────                     │ │                     ──────────┘
                                      ┌─┐─┐─┐─┐───┐───┐────┘─┘─────────┐─┐───────┐─
                                      │░│ │░│ │░ ░│   │░ ░    ░ ░     ░│ │░░ ░ ░ │
                                      └─┘─┘─┘─┘───┘───┘──────┐─────────┘─┘───────┘─
                                                             │
                         ┌─┐
                         │ │                                                                 ┌─┐
                         │ │                                                                 │ │
                         │ │                                                                 │ │
                         │ │  ┌───┐────────┐─┐─────┐─────────────────              ─┐──────  │ │
                         │ │  │░ ░│        │ │     │                   •     ┌───┐─ │        │ │
                         │ │  │       ┌────┘ │ ┌─┐ │  ┌──┐  ┌──────   │░│    │░░░│  └┐────── │ │
                         │ └──┘ ░┌── ─┘░░░▒  └─┘░└─┘  │░░└──┘░░░░░░░  └─┘    │░──┘   │░░░░░    │
                         └┐      │    └────    │ │    └──┘  └───────          •  │   │  ──── ──
                          └──┐  ─┘             └─┘   •                │ │      •  •  └─┐    •
                             │  ░│   ░ ░ ░   ░ │ │ ░   │░│ │░ ░░─┐░ │ │░│ ░   ░░     │░│ ░│
                             └───┘  ─────── ───┘─┘──── │░│ │     └──┘ │ │ ┌─────  ───┘─┘──┘
                                   •       •          ─┘─┘┐┘ ░░ ░ ░ ░  ░└─┘     ──
                                                          │  ───────────┘
                                                          │░│
                                                ┌─┐───────┘░└──────────
                                                │ │   ░ ░ │ ░    ░ ░ ░░•
                                                └─┘─    • │     • ────    •
                                                    ───┐ ─┼────┐ │     ─┐  │
                                                   •░ ░│  │ ░░░│ │░│  │░│  │
                                                    ───┘──┘ │ ─┘ └─┘  └─┘─
                           ───────┐──  ─────────┐──┐      │░└─      • │    ───────────────────
                        │ │       │░░─┐         │░░│      │ │░░•        │░░                   │
                        │ └─── ── │   │ ────────┘──┘──────  │░░ ────── ─┼───┐───────────────┐ │
                        │ │   │   │░ ░│                     │░░│        │   │               │ │
                        │ │   │   │░░┌┘         │ │         └──┘        └┐──┘               │ │
                        │ │       └──┘          └─┘                     └┘  │               │ │
                        │ └──────     ─────────     ──────      ──────── │   ──────         │ │
                        │ │                               ┌─┐                      •        │ │
                          └────────────                   │ │                   ───         └─┘
                                       ┌─────────┐────┐───┼─┘───────┐─┐─────────
                                       │░   ░    │░  ░│ ░ │░ ░░  ░ ░│ │ ░ ░ ░   │
                                       └─────────┘────┘───┼─┐───────┘─┘─────────┘
                                                          │░│
                        ┌─┐                               └─┘
                        │ │                                                                  │
                        │ │                                                                  │
                        │ │   ┌────   •                                                      │
                        │ │   │  ░ ░──░┌───────────┐─┐──── • ────────             ─────────  │
                        │ │   │  ── ░ ─┘    ░      │ │    • │          •      ───┐
                        │ └┐   ──  •    • │    ──┐    ┌──┐  └──────┐ ┌─░│    •░░░│  ───────── │
                        │  └─┐─ ░│    ░░░░│  ──░░└──  │░░│ │░░░░░░ └─┘░░│   ░░░──┘ │ ░░ ░░░   │
                         •   │   │    •  ─┘      │    │    └┐─   ──              │ │    ──┐  ─┘
                          ─── ┌──┘     ┌─  • ┌───┘ ─┐ └─┐   │ ┌─┐     ┌─┐ •    │ │ │ ┌─┐  │
                              │░░│   ░ │░│   │ ░░│ ░│ │░│   │ │░│ ░ │ │░│ ░│ ░ │ │ │ │░│ ░│
                             ─┘──┘  ───┘─┘───┘───┘ ─┘─┘─┘───┘─┘─┘───┘─┘─┘ ─┘───┘─┘─┘─┘─┘──┘
                                  ──              •                      •














```

*Figure from page 29 (2346x3317 px)*


---



4203-E P-240



SECTION 2 PROGRAM OPERATION



5-11-3. Extract



This function inserts program data which is registered in the extra buffer before the edit line (>>).



Press function key [F5] (EXTRACT) and the WRITE key after the edit line has been selected.



Example: When the extra buffer data insert before the block 4 N203"



(1) Data in the extract buffer is inserted before the edit line(»).



(2) Data in the extract buffer is not erased.



(3) The edit pointer remains at the same position.



(4) If no data is registered in the extract buffer when EXTRACT operation is attempted, the



message "extract buffer empty" is displayed and data transfer is not initiated.



(5) To erase program data registered in the extract buffer, proceed as follows.



[F5] (EXTRACT);C [WRITE]



File data is not changed.


```text


                                                                                               ┌───       •
                                                                         ┌──┐─────┐───┐───┐────┘░░░──────░░│
                                                                         │░░│░░░░░│   │░░░│░░░░░───░░░░░░ ─┘
               ────       ─────────────────────────────────────────────── ──┘─────┘───┘───┘─────      •
           ┌───     ─────
           │    ░──  ░                               ───       ───   ──     •      •  •
           └────         ─┐──┐────────────────┐──────   ┌──────   ┌─┐   ────  •     •  •
                │░ ░░  ░ ░│  │░░░░  ░   ░   ░░│ ░       │   ░     │░│  •    ┌─░│ ┌─  ── ───────── ────
                │         └─┐     ┌─  │  ┌──  │     ─── │    │       •      │  │ │               •
                │░ ░░•  ░░░░│ •░• │░░ │░░│░░░│   ░── ░  └┐───┘      ░  ─┐  │ ░           │        ┌───
                └─    ──┐──  • • •           │ ┌──   ┌─  │            • └──┘ ┌───────────┘────────┘
                │░░░░░░░│  │░░░ │░│ ░░░░░░░░░│ │░░•  │░│ │░░░  ░░░░░░░░ │░░░░│
                └───────   └──  └─┘   ───   ─┘ └──    ─┘   ──  ──   •   └────┘
                        ───   ──   ───   ──┐  ─┘  ────  ───  ──  ─── ─┐─
                  │ │ │                    │        ░             ░   │    │
                  │ │ │                    │   │         ─────────────┘────┘
                  │ │ │ ░      ░  ░ ░    ░ │ ░ │░ ░░░░░░│
                  │ │ │    ┌─              └┐──┘     ───┘─┐─┐─┐
                  │░│ │ ░░ │░ ░░░░░░ ░░ ░░░░│░ ░• ░░░░░ ░ │░│ │
                  │ │      │            │                     └─ ─┐────────────────────┐───────────┐
                  │░│ ┌────┘░░░ ───░░░░ └────────░░░░────░── ░░░│ │░░░░░░   ░░░░░░░░ ░ │░░░░░░░   ░│
                  └─┘ │░░░░░──── ░░──── ░░  ░    ────░   •   ── │ │ ─────    ──────     ───────────┘
                      │                                           │                ────
                      │  ░   ─┐      │ │         ┌─                                    ┌─
                  ──  └────── └─ │ ┌─┘─┘     ░  ─┘ ───  │ │    •           ░░  ░   ░ ░░│
                             ░ ░ │░│ ░░░──     ░ ░ ░░ │ └─┘──── ───────────────────────┘
                     ┌────┐──    │ │      • ┌─────────┘
                     │░░░ │░░│ ░  ░ ░ ░░░░░┌┘
                     └────┘──┘─────────────┘





















































```

*Figure from page 30 (2330x3295 px)*


---



Data in the extract buffer



N103 G01



N104



N105 GOO



N210 GOO



N202



» ~3 G01



N204



N205 GOO



X300



X310



X600



X150



X200



X210



4203-E P-241



SECTION 2 PROGRAM OPERATION



2150 F0.300



2200



2200



2150 F0.400



2200



Move the symbol·»• to N103 using the cursor control keys.



FIND



CHANGE



COPY



~VE



EXTRACT


# I :~ I

:~RT



[EXTEND)



@J @J @J@ ~@ @J @J



Press (F5] (EXTRAC1).



Press the WRITE key.



N210 GOO X600 2200



N202 X150



N103 G01 2150 F0.300



M104 X300



N105 GOO X310 2200



IM2o3 G01 2150 F0.400



N204 X200



N205 GOO X210 2200


```text


                                                                                                ──
                                                                          ┌─────┐─┐───┐─────────░░░──────────
                                                                          │░░░░ │░│ ░ │░░░░░░░░░ ──░░░░░░░░░
           ┌─────────────────── ─────────────── ──────────────────────────┘─────┘─┘   └─────────     ──
           │                   •               •                                                            │
           └─────────────┐ ┌──┐          ──      ────────────────────────────────────────────┐ ┌────────────┘
                         │ │  └┐░░ ───░ ░░░   ░░•                                            │ │
                         │ │   └───    ─────────  ─┐                     ┌───┐       ┌────┐  │ │
                         │ │       ┌───         │░░│          •          │  ░│       │░░░░│  │ │
                         │ │       │░░ │        │  │        ─┐░──        └─  │       └────┘  │ │
                         │ └───    └──░└──      └─░└┐        │ ░  ───────┘░──┼──────        ─┘ │
                         │ │   ─── │   │  ───── │   └─  ─── •            │   │      ────     │ │
                         │ └───    └──░└──      │ ░   ──     │░•  ────── │░░░└───       ─────┘ │
                         │ │       │░  │   ─────┼──┐──      ─┘░░┌─      ─┼───┘               │ │
                         │ │    ┌─ │░░│         │  │         └──┘        │            ────┐  │ │
                         │ │    │  │░░│         └─ │            │                       ░░│  │ │
                         │ │    └──   │            │        ┌───┘        ──           ────┘  │ │
                         │ └────   │░░│          ░░  ──────┐┘░            ░░░ ────────      ─┘ │
                         │         └──┘          ───       │  ──         ────                  │
                                                          ─┘░│
                                      │░      •              └─── ───────── ──────
                                      └─────── ────────────      •         •
                                                           │ ┌───         •  ─────
                                                           │ │
                                                           └─



                         ┌─┐                                                                 ┌─┐
                         │ │                                                                 │ │
                         │ │                                                                 │ │
                         │ │ ─┐─┐──────────┐─ ───────────── ───────┐─      ──       ──────── │ │
                         │ │  │░│          │ │                     │   ──┐─   ───┐──         │ │
                         │ │ │   ─┐ │  ────┘ │ ┌─┐ │ ─┐──┐ ───────┐   │░░│   │░░░│     ────┐ │ │
                         │  ─┘┐ │░└─┘ ░░░░░  └─┘░└┐┘  │░░└┐  ░░░░░│   └──┘   │░──┼─  ──  ░░└─  │
                         └┐   └─┘─    ─────    └─ │   │   │ ──   ─┘      └┐      │  │      │  •
                          └──                      • • ┌─     ┌─┐ └─┐─┐─░░└─┐     ─┐┘ ─┐  ┌┘──
                             ┌┐ ░   ░    ░   ░ ░ ░ ░   │░│  ░ │░│ │ │ │░│ ░ │ ░│ │░│ │ │ ░│
                             └┘ ──  ───░──┐┐─  • │ ──┐ └─┘ ── │ └─┘─┘─┘─┘───┘──┘─┘─┘ └─┘ ─┘
                               •  ──   •  └┘ ── ─┘─  └─   •  ─┘┐                    •   •
                                                               └─    ░ ░ ░   ░│ ░│
                                                          │ │      ────   ─┐──┘──┘
                                                   ┌──────┼─┘────┐─    ─┐  │
                                                   │░ ░░ ░│ ░░ ░ │░│  │░│  │
                                                    ──────┘ ┌────┘─┘  │░│
                         ┌────────  •  ─────────────      │░│       • │   ─┐ ───────────────┐─┐
                         │        ┌─ ─┐          ░░       │  ░─┐        │░ │                │ │
                           ────── │   │ ────────┐─┐─────── ─┐ ░│        └──┘┐              ─┘ │
                        │ │       │  ░│         │ │         └──┘        │   │        ─────┐ │ │
                        │ │       │   │         │░│                        ░│           ░░│ │ │
                        │ │       │░  │         │           ┌─░│            │          •  │ │ │
                        │ │   ┌─  └──░│         │░│         │░─┘         │░─┘        ┌─ ──┘ │ │
                        │ │   │   │░░░│         └─┘         │  │         └─░│        │  ░░│ │ │
                        │ │    •  └┐░ │         │ │         └──┘         │  │        └────┘ │ │
                        │ └────    │░│           ░░         │░ │         ░░░               ─┘ │
                        │           ─┘          ───          ──          ────               │ │
                                                                             ───────────────┘─

























```

*Figure from page 31 (2346x3317 px)*


---



5-12. Page Mode



4203-E P-242



SECTION 2 PROGRAM OPERATION



In the page mode (P mode), displayed screen is fixed and keying in of a character, etc. overwrites the



existing screen data. For the input on the screen, insert mode (I mode) is also provided in which keyed in



characters, etc. are inserted. For details of the insert mode, refer to 5-13. "Insert Mode".



This page mode is used in the following cases:



(1) creating a new file



(2) replacing one character in an existing file



(3) adding a character-string to the end of a line



The operating procedure is as indicated below.



Press function key [F6] (PAGE MODE) "P MODE" will be displayed on the 1st line of the screen.


#### PROG OPERATION

»01000



N100 GOO



N101 G56



N103 G41G01



N104 003



Nl05



N106



N107 G01



Nl08 G40



N109 GOO



N110



Nl 11



=E WHEELlOO.MIN



file end



X300



X400



>EX



xsoo



X100



X200



X400



X300



"P MODE" is displayed.


#### EDIT Pt.ODE WHEELIOO. MIN

97/07/15 14:10:00



Y300 S250


#### Z-55 M09 M03

Y200 F100 D11



Y300 10 JIOO



Y300 1-200 JO



Y200 1100 JO



Y200



2100



@@)@)@@J~@J@J



Press [F6J (PAGE MODE).



(a) When a character is keyed in in the page mode, the cursor-located character is replaced by



the keyed-in character and the cursor moves to the right. In other words, in the page mode,



the cursor is moved to the right and the character (including a space) located by the cursor is



replaced by a keyed-in character each time data is entered. Therefore, if an attempt has been



made to assign a character-string many digits of characters, subsequent character data might



be replaced.



{b) If one line has more than 63 characters, such a line is displayed in two lines on the screen with



the second line preceded by"&''. These lines are processed as one line. In this case, the edit



pointer and the edit line move to the lower line.



(c) Each page has a total of 16 lines for edit operation.



When the WRITE key is pressed while the bottom line is designated as the edit line, 16 lines of data



are shifted by one line each and a blank line is created on the 16th line. The edit line does not



change and the edit pointer is placed at the beginning of that line.


```text


                                                                                                ──
                                                                         ┌──┐─┐────┐─┐─────────░░░───────░─┐
                                                                         │░░│ │░░░ │ │░░░░░░░░░ ──░░░░░░░•░│
             ─────             ────────────────────────────────────────── ──┘─┘────┘ └──────────     ──
          ┌──      ────┐─┐─────
          │░    ──┐░   │ │     ┌─  ───
          └────┐  │ ──░│ └─    │  •
               │   ░           │ •   ───┐  ┌─ ───── ────   •  •   •   ───┐─   • •  ── ───   •    ─────   ──
                  ───────┐──    •   │   └─ │ │  ░  •░   ──┐ ──░───░─── ░ │░──┐ • ──░░•░░░─┐─░┌─┐─░░░░ ░──░ ░
                │░░░░░░ ░│░░░  │░░  │░ ░ ░ │░│ │░ ░░ ░░ ░░│ ░ ░░░ ░ ░░ ░  ░ ░│ ░ ░░░ ░░░░░│░ │ │░░─────░░░──
                └────┐───┘─────┘─── └──────┘─┘─┘──────────┘░░░───░  ─── ░┌───┘─┐──┐░ ────░└─░│  •       ──
                │    │                                     ───   ───   ──┘     │  └──    •  ─┘
                │░░│ │░░│ •░░░░ ░ •░░•   ░│ │░░░░░░ │░░░░│
                └┐─┼─┘┐─┘─       • •  ────┘─┘───────┘────┘
                 │ │  │ ░░░░  ░ •░│ ░│
                 │  • │   ──      └──┘────┐─── ┌─ ────  •
                   │   ───                │   ─┘ •    • ░│
                 │ │       ┌─             │              │ │
                 │ │  │  ──┘               ───             └─┐
                ┌┘  ──┘    │                  •              │
                │░ │    ───┘               •                •
                │  └──                ────  ┌─         ────┐ ──────┐─────────────────────────── ───
                │░░░░ ░   ░       ░░░ ░░░░│ │░  ░   ░ ░░  ░│   ░   │           ░               │
                └─────────────────────────┘─┘──────────────┘────── │        ──────  ───────────┘─────
                                                                  •░ ░─────  ░░░░░░•
                             ────            ────────     ───────                     ──
                            •     ──────────┐         ┌──         ─────────┐─────────┐   │
                           │  ── •░░  ░░░░ ░│         │░ ░───────  ░▒░░    │▒▒▒░░░░▒░│ │ │
                           │ │         ─── ─┘         └──          ────░ ░─┘─────────┘ │ │
                           │ │   ───┐            ┌──┐    ┌─┐     •                     │ │
                           │ │  •  ░└─  ┌──┐     │░░│    │░│    •░─┐   ┌─     ─┐       │ │
                           │ │   │ ░│   │░░└─    │  │      │   •░ ░│   │░─┐  │░│       │ │
                           │ │   │░░│   │░░░     └──┘    ┌─┘    ┌─░│   │░░│  └─┘─      │ │
                           │ │  •░░░│   └─┐──    │░░│    │▒│    │  │   │░│             │ │
                           │ │   │░░│     │      │░░│    └─┘    └┐┐┘   │░│             │ │
                           │ │   │░░│   ┌─┘      │░░│      │     └┘    └─              │ │
                           │ │  │░░░│   │░│      └──┘   │░░│    •  │                   │ │
                           │ │  │░ ░│   └─┘             └──┘       │                   │ │
                           │ │   ───┘                           ───                    │ │
                           │ │                                                         │ │
                           │ │                                                         │░│
                           │ │  ┌──┐──┐─────                                           │░│
                           │ │  │░ │░░│   ░                                            │ │
                           │ │  │  └──┘─────                                           │ │
                           │ │  │░░│              ┌─     ──      •           ───       │ │
                           │ │  │  │  ──────┐─ ┌─┐┘ ─┐──┐  ──────  ┌──   ───░░  ─────┐ │ │
                           │  ─┐  ─┘ •   ░░░│  │░│   │░ │          │░░│ │ ░░         └─  │
                            •  │    • •  ──┐┘    │   │  │ •    •   └──┘ │  •    •   ░│  ─┘
                             ─┐  ─┐─ •     │   │  ──┐┘─┐ •  ──  ─┐─    ─┼─  • •      └──
                              │░ ░│   ░ │░ │ │ │░ ░ │ ░│ ░│  ░│  │ │░│ ░│ ░   ░│ │░│ │
                              └───┘  ───┘─ └─┘─┘────┘──┘──┘───┘ ─┘─┼─┼──┘──────┘─┘─┘─┘
                                   ──     •                    •   │ │
                                                                   │░└─  ─────   ───
                   ┌──  ───    ──────    ──────   • ──────┐  ───       ─┐     ───   ──────────┐────────
                   │░░ │░░░────░░░ ░░────░░░░░ ─── •░░ ░░░└──░░░│ ──   ░│░  ░░░░░░ │░░░░░░  ░ │░░░░░░  │
                   └──┐┘  ░   ░░─── ░░ ░░░     ░        ┌─     ─┘ ░  │ ─┘───────┐──┘──────       ───   │
                      │        •               │   │   ░│            │░         │             •        └┐
                       ┌─────┐─      ───      ─┘───┘    └───  ────   └──░•░░ ┌──░───── •░░░┌─┐░ ─────░─┘┘┐
                       │░ ░░░│ ┌─── ░░░░░ ░ ░ ░░░░░  ░░░  ░░░ ░░░     ░░ ░░• │░░ ░░░░   ░░ │░│ ░░ ░░░ ░░░│
                       │ ░░──┼─┘░░░──────░░░░░─────░ ───░ ──░░░───   ░░•░░•  └── ░──░ ░ • ░└─┘ ──┐░──┐  ░│
                      ─┘ ─┐  │  ─┐─      ─────     ──   ──  ───   ───── ──  •   ──  ───  ──   •  └─  └───┘
                          └──┘   │
                   ┌──  │         •          ──────────           •     ─────     ──  ────   ──   ───
                   │   ─┘─────────░──┐──────┐     ░░░░░──┐────┐── ░─────░░░░░░┌───░░──░░░░───░ ──░ ░░┌─┐─┐
                    • •░░ ░░░░░░ ░ ░ │░░░░░░│ │░ ░┌─ ░░░░│ ░ ░│ ░░•░░░░░──────┘ ░ ░•░░───  ░░──░░░───┘ │░└─
                       ──────────────┘──────┘─┘───┘ ─────┘────┘──  ─────       ───  ──    ───  ───
                    • •
                   │   ░    ┌──┐ ┌─┐ •        ░            ┌──── ──┐
                   └─  •  ──┘  └─┘ └─                      │    │  └────┐─   ───   ────   ┌─   • •    ──
                      •░░   │░│ ░░░░░•              ░   ░   •  ─┘       │ ┌──   ─┐─    ───┘ • • • ───   ──┐
                       │    │░│ •                  │                      │░     │   │  ░    •       ──   └┐
                      ─┘      ░  ┌─ ░    ░  ░░  ░  │░  ░░░  ░░ ░──░░░░░  ░ ░ ░ ░░│ ░░└─── ░ ░░░ ░ ░ ░░░░ ░└┘
                       │ ░░░┌──░░│░│ ░ ░•░░░░░• ░░░░░░░───░ ──░░░░░────░•░░░•░ ░─┘───┘   ─────────────────┘
                        ────┘  ── ─┘──── ───── ────────   ──  ─────    • ─── ───








```

*Figure from page 32 (2346x3317 px)*


---



4203-E P-243


#### SECTION 2 PROGRAM OPERATION

(d) When the WRITE key is pressed while a line other than the bottom line is designated as the



edit line, the edit line is moved to the subsequent line and the edit pointer is moved to the



beginning of that line. This also applies to the insert mode.



(e) When the program cannot be displayed in one page (16 lines), press the page key



@ .



To return the display to the previous page, press the page key



5-13. Insert Mode



In the insert mode {I mode), keyed in characters are added to the data in the displayed file. For the input on



the screen, page mode (P mode) is also provided in which keyed in characters, etc. overwrites the existing



characters. For details of the page mode, refer to 5-12. "Page Mode".



The operating procedure is as indicated below.



(1) Press function key [F7) (INSERT MODE) "I MODE" will be displayed on the 1st line of the



screen.



PROO OPERATION



»01000



NIOO GOO



N101 G56



N103 G41G01



N104 G03



N105



IN)06



N107 GOl



N108 G40



N109 GOO



NllO



N111



=E WHEEL100.MIN



file end



>EX



EDIT



X300 Y300



X400 Y200



xsoo



Y300



X100 Y300



X200 Y200



X400



X300 Y200



"I MODE" is displayed.



I MODE WHEEL100.MIN



97/07/15 14:J



:oo



$250


#### Z-55 M09 M03

FlOO 011



10 J100



1-200 JO



1100 JO



2100



FIND



CHAl\l:iE



COPY



MOVE



EXTRACT



[EXTEND]



@J @J



® ® ®



Press [F7J {INSERT MODE).



(a) Each time a character is keyed in in the insert mode, it is inserted before the edit pointer and



the character-strings following the edit pointer are shifted by one character. When data is



fnserted successively and the currently dlsplayed data has reached the right end, data is



inserted in the next line that is preceded by"&". These lines are processed as one line.



{b) Each page has a total of 16 lines for edit operation.



When the WRITE key is pressed while the bottom line is designated as the edit line, 16 lines of data



are shifted by one line each and a blank line is created on the 16th line. The edit line does not



change and the edit pointer is placed at the beginning of that line.


```text


                                                                                               ┌───
                                                                         ┌──┐──────┐──┐─┐─┐────┘░░░────────┐
                                                                         │░░│  ░░░░│  │░│░│░░░░░───░░░░░░░░│
           ┌────────                   •                  •    •   ──  ── ──┘─ ───    └─┘─┘─────      ──
           │        ┌─  ┌───┐────┐────┐ ──┐──────────┐───┐ ┌──┐ ───  ──  •    •   ────          •           │
           └────────┘ • │░  │    │░░  │   │          │   │ │  │    │                                   • ───┘
                    └─  │                  •              ─┘──┘ •  │      ────   ───  ─┐     ░      ░   •
                        │░  ░  • ░ ░ ░ ░ ░ ░ ░ ░░░ ░  ░░ ░░ ░░░ ░░░ ░░ ░ ░ ░░░ ░░ ░ ░ ░│ ──░ ░░░░•░•░┌──
                        └─░────░ ──────────────────────────────┐───────┐───────────────┘─  ──────    │
                    ┌─┐ │                                      │       │                 ──
                    │░│ │░ ░░ ░│ ░░░ ░░│ •░│░ ░ ░│ ░░░░░░░   •░│ •░░░  │░ ░░░   │                 ┌─┐
                    └─┘ │      │       └┐ ─┘  ┌─ │       ──┐─   •     ─┘       ┌┘─ ────────────── │░│
                       │░░ ░░ ░ │ │ ░░░░│  ░ ░│ │ ░░░░░ │░░│  ░░░░ ░░░ ░░░ ░░░ │░░│               └─┘
                       │ •     ┌┘─┘─────┘─────┘─┘───────┘──┘───────────────────┘──┘
           │ ─┐ •  ┌───┘─ ─────┘
           │  │    │  ░       ░│
             •                      ──    ── ───   • ───   ───  ────     ───       ───────  •      ─── •
                 ────────┐ ┌──┐─ ─── ░────░░•░  ┌──░•░ ░───░░ ──░░░ ─────░░░───────░░░░░░░──░────── ░░░░───┐
                │░░ ░░ ░░│ │░░│  ░░░░ ░ ░ ░░░ ░ │░░░░ ░ ░░░ ░ ░░░░ ░░░░░░  ░ ░░░░░░─────── ░░░░░░░░ ░───░░░│
                └┐───────┘─┘──┘─────────────── ─┘──────────░ ────────   ░░   ─────        • ─────── •   ───
                 │                                         ──        ────────
                 │░░ │░• ░░░░ ░░░░░░░░ ░  ░ ░░░░░░┌┐─░░ ──
                 └┐ ┌┘┐   │                       └┘       ─┐───────────────────────────── ─────────
                  │░│ │ ──┘     ░       ░   ░░ ░ ░│ │░  ░   │░░ ░░    ░    ░          ░    ░
                  └─┘ │     ┌─────────────────────┘─┘───────┘────────────  ───────    ────────────────
                      │   ░┌┘                                            ──       ────
                       ────┘                                          ───░░• ░ ░ •░ ░░░│
                                                            ────         ──           ─┘
                             • ───┐─┐─┐───┐──┐────────┐───┐─    ────┐───   ─── ─────    ──
                            │     │░│ │░░░│░░│        │░░░│         │░░ ───░░░│ ░░ ░─┐    │
                            │ │ • └─┘ └───┘──┘────────┘───┘─────────┘─┐ ░░░░•▒│░░░░░░│  │ │
                            │ │      │                                └───── • ──────┘─ │ │
                            │ │  ┌─░░│   ┌─┐              ┌─┐    ┌─┐                    │ │
                            │ │  │░░░│   │░└──    │  │    │ │    │░└┐  ┌───             │ │
                            │ │  │░ ░│   │░│░░    │░─┘    │░│   │░░└┘  │░  •  ───       │░│
                            │ │  │░ ░│   └─┘──    │░░│   │░░│   └┐  │   │ │             │ │
                            │ │  └─░░│            │░░│   │░░│    │ ░│   │░│             │ │
                            │ │  │▒░░│   ┌─┐      │░░│    │░│    └──┘   └─              │ │
                            │ │  └─░░│   │▒│      │░░│    │ │   ┌┘  │                   │ │
                            │ │  │░ ░│   └─┘      └──     └─┘   │░░░│                   │ │
                            │ │  │░  │                          └───┘                   │ │
                            │ │  └───┘                                                  │ │
                            │ │                                                         │ │
                            │ │  │  ─── ──┐─┐─                                          │ │
                            │ │  │░ ░░░  ░│░│                                           │ │
                            │ │  │ ───────┘─┘─                                          │ │
                            │ │  └─           ────────────   ────┐─             ─────── │ │
                            │ │  │░•                             │   •      ────        │ │
                            │ │     │ │ ┌────┐  ┌─┐   ┌──┐ ┌────┐┘  │░│   ──░░   ┌────┐ │ │
                            │  ─┐──░│ │ │░░░░│ ─┘░│   │░░│ │░░░░│   │░│   ░░─┐─  │░░░░│   │
                             ── │    •   ┌──┐      • │ ─┐    │ ─┘         •  │  ─┘   ─┘  •
                               ┌┘ ░│     │░ │ │  ░   │  │    │░     │ │    •░     │░  │
                               │░  │   ░ └─ │ │  ░ ░      ── │ │    │ │ ░•  ┌─  ░ │░  │
                               └───  ┌───  ─┘─┘───────────  • ─┘ ── └─┘    ░│      ──
                                    ─┘                                 ─── • ────┐    ─┐
                                                                    • ░░ ░  •░░░░│ ░ │░│
                                                                     ─────   ──  │   └─┘
                    ┌──   ──         ── ──         •    •   ──    ──       ──  ──  ──   ───    ──  •  ───┐
                    │░ ┌──  ──────┐──░ │ ░─┐─────── ┌─┐─░───░░─┐──░░───────░░░•░░ •░░───░░ ────░░──░──░ ░│
                    └─ │░░ ░ ░░░░░│ ░░░│░ ░│░ ░░░░ ░│ │░░ ░░ ░░│ ░░ ░░░░░ ░░ ░░░ ░░░░░░░░• ░░░░░ ░░░ ░┌──┘
                       └────░┌────┘────┘───┘────────┘─┘───────░│  • ───────      ───────   ──── ──── ┌┘
                       │     │   ░                             ░┌─                                   │
                       │ ────   ──────── ───────────────────░───┘  ──░░   ░░ ░ ░   ░░░░░░  ░   ░ ░ ┌─
                   ┌─┐─┘      ──        •                        •   ──────────────────────────────┘
                   │░│ │ ░░ ░░░░░────┐──░•    ░ ░ ░░ ░┌──░│ ░░ ░░░░•
                    ─┘ │             │                │   │            ───── ───   •   ──────  ┌─────  ────
                       └──────────   └──────┐───────┐─┘───┘──────────── ░░░░•░░░──░ ░░░  ░ ░ ──┘░ ░░░── ░░░│
                       │░░ ░░░░░░ ░ ░░░ ░ ░ │░ ░ ░ ░│ ░░░░░  ░    ░░░░░░ ░  ░░  ░░───────────░░ •░─── ░────┘
                       └─░░ ────── ░░• ░░•  │░─────░░ ─────  ─┐    ─────░ ░  •  ┌─           ─── •   ──
                         ───      ─── ─── ── •     ───     ── └────     ───── ──┘












```

*Figure from page 33 (2346x3317 px)*


---



4203-E P-244


#### SECTION 2 PROGRAM OPERATION

(c) When the WRITE key is pressed while a line other than the bottom line is designated as the



edit line, the edit line is moved to the subsequent line and the edit pointer is moved to the



beginning of that line. This also applies to the page mode.



(d) When the program cannot be displayed in one page (16 lines), press the page key@ .



To return the display to the previous page, press the page key



@ .



5-14. Power Failure/Shutdown during Editing



The function to avoid the file from being lost is provided even if power failure occurs or power is shut down



by mistake during editing.



5-14-1. In-editing Comment



If power is shut down during editing, the following "in-editing comment'' is attached to the first data block of



the file having been edited.



"THIS FILE NEEDS EDITING AGAIN!'


#### OKUMA MACHINERY WORKS LTD.'

This comment is deleted when the same file is read out from the memory.



Note: This comment is not displayed on the edit screen.


```text


                                                                                                ──
                                                                         ┌──┐──────┐─┐──────────░░─────────┐
                                                                         │░░│ ░░░░ │ │░░░░░░░░░░── ░░░░░░░░│
          ┌─────────  •                     ──           • • ───   •   •  ──┘    ──┘ └─────────      •
          │         ──  ───┐──────────┐─────  ──────────┐ • •   ┌── ┌──  •   ────   •                      │
          └─────────  •  ░ │      ░░  │                 │       │   │                                   ┌──┘
                    ── │                                 ────   │   │ ──────    │ ─────      ──░ ──┐─┐  │
                       └┐░   ░  ░░ │░│  ░     ░ ░░ ░│░│  ░░░░░░ ░░ ░ ░ ░░░ ░│ ░░│ ░░░░░  ░ •░░░░ ░ │░└──┘
                       └┘──┐────┐──┘─┘──────────────┘░└──┐──────────────────┘───┘────────── ─────   ─┘
                    ┌─ │   │    │                        │                                        •
                    │░ │░░░│ ░│░│░ │░░░░ ░░  ░ ░░ ░░░░░ ░│ ░ │░   ░ │ ┌─     │ │ ░         ░     │ │
                    └──┘ ─┐ • └┐┘┐ │                   •  ─┐ │      └─┘  │   │ │ • ┌─────────────┘░└─
                       │░ │░░• │░│ └─░░░░ ░ ░ ░ ░░░ ░░• •░░│ │░░░░ ░░ │░ │ ░░│ │░░┌┘              •
                           •    •    •                   ──┘ └────────┘──┘───┘─┘──┘
          │ ─────  ───────  ──── ──── ──────┐────────────   │
          │       │   ░     ░  ░   ░ ░ ░░░░░│ ░ ░ ░░░  ░   ░│
               • ┌┘                         │        │       ───────┐──────┐───────┐───┐──┐────┐───┐───────┐
                ─┘ ░ ──── ─────  ░──── ░░  ░   ░ ░ ░░│ │ ░ ░░░░░ ░░░│  ░░░░│ ░░  ░ │░░░│ ░│░ ░░│ ░ │░░ ░░░░│
                 │ ──░░░░│ ░ ░░──┐░░░░───────────────┘─┘────────────┘──────┘───────┘───┘──┘────┘───┘───────┘
          ┌──┐── │       │       │  ┌─
          │░ │░   │░ ░░░•░• ░░░░ ░░░│
          └──┘─   │                   ──────┐─┐──┐─┐──────┐──────┐──────────────┐────────┐─┐─────┐─┐────┐───┐
                ──░░░░░┌─ ░░•░░•░░ ───░░ ░░░│ │ ░│ │░░░░░░│ ░ ░ ░│ ░ ░░░ ░░░  ░ │░░░░░░ ░│░│ ░ ░ │░│ ░░░│ ░░│
                 ░──── │░ ──  •░──  ░░ ─────┘─┘──┘─┘──────┘──────┘──────────────┘────────┘─┘─────┘─┘────┘───┘
                       └──        ─────


                           ───────────────────────┐───────┐
                         • ░░░  ░   ░░░░ ░ ░ ░   ░│ ░░░░░ │
                          ────────────────────────┘───────┘



                              ┌────┐─┐───────────┐─┐──────────┐
                              │░░░ │░│ ░░░  ░░░░░│ │░ ░░░     │
                ┌────┐────────┘      │ │  │      └─┘   ──      ─────┐─────┐─────┐
                │░ ░ │░░░░░ ░ ░┌┐░░░░│ │░░│ ░░ ░░░░░ ┌─ ░  ░░  ░░  ░│ ░ ░ │░░░░ │
                │  • └───┐  •  └┘   ┌┘ └┐─        ───┘             ┌┘─────┘─────┘
                │░░░│    │░│   ░░░░░│ ░ │   ░░░░░ ░    ░    ░     ░│
                └───┘    └─┘────────┘───┘──────────────────────────┘










































```

*Figure from page 34 (2346x3317 px)*


---



5-14-2. Alarm



4203-E P-245



SECTION 2 PROGRAM OPERATION



If the file with the Kin-editing" comment ls run, the following alarm occurs.



2230 Unusable: direct of left side



If this alarm message is displayed, read out the same file from the memory and complete editing.



AlITO OPERATION



2230 Al.ARM


#### A.MIN O N 11

97/07/15 14:10:00



direct of left side 3EOO


#### PROGRAM *CURRENT MAIN PFOORAIH lm

» "THIS FILE NEEDS EDITING AGAIN!"



OKUMA MACH I NERY WORKS LTD.



LOAD MAX 'v



SP I NOLE LOAD



ACT POSIT (WORK) 0.000 0.000



A-Mtd



;Xf'S



PROGRAM ACTUAL PART BLOCK



SELECT POSIT. PROGRAM DATA SEARCH



(1M



DIS X 0.000


#### Y 0.000

Z 0.000


#### W 0.000

0 F 0.0



H:: 0 0.000



D= 0 0.000



z w



0.000 0.000



CHECK



DATA [EXTEND]



To give warning to an operator, the following alarm is displayed on the screen when the power is turned on



after the power was shut down during editing. In this case, an error file name is stored to the file of



"MD0:ERROR.BAK" (or "MD0:ERROR.LOG").



4248 Error File


```text


                                                                                                ──
                                                                         ─┐─┐──────┐─┐──────────░░░────────┐
                                                                          │▒│ ░░░░ │ │░░░░░░░░░░───░░░░░ ░░│
                 ──    ────────────────────────────────────────────────── └─┘──────┘─┘─────────
          ┌──────  ────
          │             •                ──          ────                ─────
          └─────  ──     ────────────────  ──────────    ────────── ─────     •
                │░ ░ •░│ ░░░ ░       ░░                                     ── │
                │ ─── ─┘ •  ──── • •  │  ──      ────────────────── ────────  ─┘
                 •░░░│  │░░ ░░░░│ │░░─┘── ░░  ░░
                │  • └┐─┘  ─┐   └─┘         ──┐─ ──┐─┐──┐──┐──────┐─┐─┐─────┐─────────────────┐─┐──┐──
                │░ ░│ │░│ ░ │░░░░░░• ░ ░░░░░░░│ │░░│ │░ │░ │░░░░ ░│ │░│ ░ ░ │░ ░░   ░░    ░ ░░│ │░░│  │
                └───┘─┘─┘───┘────             └─┘──┘─┘      ──────┘─┘─   ───┘  ──   ──────────┘─┘──┘──┘
                                 ─┐──────────┐        ┌───┐─           •     ─┐
                            │     │░░ ▒░▒░░░▒│        │░░░│           •░─────░└──────┐   │
                            │ │ •     ──      ┌──       •          ──   ░░░░░░ ░░ ░░░│   │
                            │ │  │▒░▒  ░░░▒• ▒│ ░ ░░───┐ │░│ ──────░░░────────  ──  ─┘   │
                            │ │  └───░░┌─── ──┘──── ░░░│ │░│  ░░░░░░──        │░░        │
                            │ │      ──┘            ─── • • ───────      │  │ └┐  ┌─┐    │
                            │ │                                      │ ┌─┘  │  │  │░│    │
                            │ │       ┌────┐─┐─┐─────┐─┐──┐───┐      │ │   ░│   ──┘─┘    │
                            │ │       │░ ░ │ │ │░░░ ░│ │░ │░ ░│      │ │                 │
                            │ │       └────    └─      └─  ───┘       │ •     ┌─         │
                            │ │            ┌───  ─┐─┐─┐  ──    │      │  │    │ •   •░│  │
                            │ │    •  ─┐   │░░░│░░│ │░│ │░░│  ░│      │ ░│ ── └─ ┌┐─ ░│  │
                            │ │  ┌─░──░│ ── ───┘──┘─┘─┘─┘──┘───┘    ┌─ ──        └┘ ─┐   │
                            │ │  │░ ░░░│ ░░•                        │▒   │      │    │   │
                            │ │  │  •    ─┐ ──   ┌─┐──┐     │░───   └── ░└───   │▒── │ │ │
                            │ │  │ │   ── │░░    │░│  │     │          ── ░     └─ ░   │ │
                            │ │  │░│       ──    └─┘──┘        •         ───       ──  │ │
                            │ │ │   ───┐                                               │ │
                            │ │ └─░ ░ ░└─                 ──────   ────┐─      ─────── │ │
                            │   │        ──┐─ ┌─    ──┐───             │ • ────        │ │
                            │   │░░░░░  │ ░│  │░────  │░░   ┌─────┐  ──┘  │░░░  ──────┐┘ │
                            │   └────── │░┌┘  └─░░░░  └──   │░░░  │    │  └──┐ • ░░░░░│  │
                             •            │      ┌──     •  │    ─┘─  •      │      ──┘ ─┘
                              • ┌─ │   • ░│     ░│           │░     ┌─ │ │ ░░ • ┌─┐   │
                                │  │ ░    │ ── • │ ░• •   ─┐ │░ •   │░ │ │  • ░ │ │░ ░│
                                └──        •               └─ •     └──┘ └── ── └─┘──
                   ─── ───    •      • •     •     •      •      •                      ─── •   •     •
                ┌──░░░• ░░──── ┌─────░•░─────░─────░─────┐     ─┐ ░░•░ ░•  ─── ░░░  ░•░░ ░ •░░░░░•░ •  ░░ ░│
                │░░░ ░░│ │░░░░ │░░  ░ ░ ░░░░ •░░░ ░ ░░░░░└─── •░└───░───░──  ░──── ──░──── ░─────░──░───── │
                └──────┼─┘─── ░│░│ ───┐░░•   ░ ░ ░───────┘     •    •       ──       •     •     •  •
                │      │        ┌┘    └── ────────
                │░░░┌─ │░  ░ │░┌┘
                └───┘  └─────┘─┘




































```

*Figure from page 35 (2346x3317 px)*


---



4203-E P-246



SECTION 2 PROGRAM OPERATION



5-14-3. Not-guaranteed Area Indicating Symbol



If the power is shut down during editing, the first character of the program displayed on the screen (16 lines



x 63 columns) where a character was changed or added last is replaced with the not-guaranteed area



indicating symbol"<".



Note that this replacement occurs only when "1" is set for NC optional parameter (bit) No. 16, bit 4.



Example: NC optional parameter (bit) No. 16, bit 4 = 0



Example:


#### PROO OPERATION EDIT P MOOE WHEEL100. MIN

97/07/15 14:10:00



>fi]IOOO



N100 GOO



N101 G56



N103 G41G01



N104 G03



N105



N106



N107 G01



N108 G40



N109 GOO



N110



N111



=E WHEEL100.MIN



file end



X300



X400



xsoo



Y300 S250



Z-55



X100



X200



X400



X300



t.t::l9



Y200 F100 011



Y300 10 JlOO



Y300 1-200 JO



Y200 1100 JO



Y200



2100



LINE LINE CHAR. CHAR. LINE EDIT



I NSSIT DELETE I NS8IT DELETE DELETE ERASE



NC optional parameter (bit) No. 16, bit 4 = 1



M03



PROO OPERATION EDIT P MODE WHEE



>::ls]IOOO



NlOO GOO



N101 G56



N103 G41G01



N104 G03



N105



N106



N107 GOl



N108 G40



N109 GOO



N110



N111



=E Wl-EELJOO. MIN



file end



X300



X400



xsoo



X100



97/07/15



X200



X40D



X300



Y300 S250



Z-55 M09 M03



Y200 FlOO Dl 1



Y300 ID J100



Y300 1-200 JO



Y200 1100 JO



Y200



2100



LINE LINE CHAR. CHAR. LINE EDIT



[EXTEND]



INSERT DELETE INSERT DELETE DELETE ERASE OU IT [EXTEND]


```text


                                                                                                •         •
                                                                         ┌─────────┐─┐──────────░░░───────░│
                                                                         │░░░░░░░░ │ │░░░░░░░░░░───░░░░░░░─┘
            •    ──    ──       ──  ───      ───      ─────────────────── ─────────┘─┘─────────
          ┌─ ────  ┌──┐  ───────  ──   ┌─────   ──────                                                     │
          │        │  │         │    │ │              │                           ─────────────────────────┘
           ─────  ─┘  └───      │ ───┘ │      ░    ───┼───┐─┐───    ┌─
                •░ ░    ░░    ░ │   ░│ │      ░░ │    │   │░│   ─┐ ─┘░┌───      ─── ────    ──       ┌──── │
                 │          •  • ──  │ │  • •    └┐   └───       └─   │ ░    ───    ░         ──── ──┘     │
                 └──         ──░ ░░│ ░ ░ ░░░░░│ │░│ ░ ░░░░  ░  ░░░░░ ░░   ─┐░░░░░░ │░──░│ ░ ░ ░ ░░░ ░░░ ░ ░│
                 │░░─────────░░────┘    ──────┘ └─┘    ──── ──  •  •  ──   └───  • └─   │    ──────────────
                 │                  ───┐       •   ────    │  ┌─ ─┐ ┌─  ┌──    ┌─ •  ──┐ ┌───
                 │░░░  ░│     ░░░░░░ ░░│ │░  ░  ░░░ ░░░•   │░ │░ ░│ │░│ │░░░ ░ │░ ░░░░░│ │░░ ░│ │░│ │░  │
                │       └──          • └─┘────┐ │    ┌─ ── │  └─┐─┼─┘─┘─┘──────┘───────┘─┘────┘─┘─┘─┘───┘
                └┐░░░░░░│  │░  ░░░ ░• •░ ░░░░░│ │░░ ░│ • ░ │░   │░│
                 └──────┘  └─ ───             └─┘────      └───   │
                                 ─┐─┐─┐──┐───┐       ─┐─┐──    ──┐┘─┐──     ─────  ──   •
                            │  •  │░│ │░░│░░▒│        │▒│░       │░ │▒░ ─── ▒░░ ░──▒░│   │
                            │ │ ─┐┘─┘─┘──┘───┘────────┘─┘─────  ─┘──┘── ░░░░───░░░░░░│   │
                            │ │  │                            ──       ─────   ──────┘   │
                            │ │  │▒──┐   ┌─       │ │            ┌─┐                   │ │
                            │ │  │░░░│   │░───    └─┘       │   ┌┘░│   ┌─┐    ┌─┐      │ │
                            │ │  │░░│   •░░░░     │░│    ┌──┘   │░─┘   │▒└─   │ │      │ │
                            │ │  │░░│    ─────    │░░│   │░░│   │░     │░░░    •       │ │
                            │ │  │░░│             │░░│   │░░│   │ ░░   │░┌─            │ │
                            │ │  │░░░│            │░░│   │░░│   └──┐─  └─┘             │ │
                            │ │  │░░░│   │░       │░│    │ ┌┘   │  │                   │ │
                            │ │  │░░░│   │░       └─┘    └─┘       │                   │ │
                            │ │  │░ │                           ───┘                   │ │
                            │ │  └──┘                                                  │ │
                            │░│                                                        │ │
                            │ │                                                        │ │
                            │ │   ──── ──────┐                                         │ │
                            │ │  • ░░░│  ░░░░│                                         │ │
                            │ │ │   ──┘    ──┘           ─┐─────┐─     •     ───┐───── │ │
                            │ │ │        •   └─ ─┐    ┌─  │     │ •     • •     │      │ │
                            │ │   ───  ──░─┐─  │░└┐   │░──┘  ───┘  ┌───  •░│  │ └┐────┐┘ │
                            │    •░░░   ░░░│   │░░│  ░░░░░  │░░░   │░░░│  ░│  │ └┘░░░░│  │
                             •  │                ─┘         │   •      │    ──      ──┘ •
                                │  │      ░    ░      ░      ░░   │ ░░ │ │  ░   │ │░  │
                                └──┘─░•   ──── ────── ──  •░ ─┐ │ │ •░ │ │ ───░ │ │░ ░│
                                              •            •  └─┘─┘─ ──┘─┘─   ──┘─┘───┘
                ┌───────┐ ┌───┐─────────── ───  ─┐───   ───                  •
                │  ░    │ │   │░░░░ ░ ░░░░ ░ ░  ░│  ░• •░     ────
                 ───────┘  •  └──            ────┘───             ────                 ──
                            │    │░░  ░░░░ ░░          ░            ░░───────────────┐   │
                            │ │ ─┘─────────────────────────────────── ░░░░░░░▒░░░░░░▒│ • │
                              │                                      ────────────────┘   │
                           │ │   ┌──┐             ┌─┐    ┌─┐      •                    │ │
                           │ │   │░░└─  ┌──┐─    ┌┘░│    │░│    ──░│   ┌─┐   ┌──       │ │
                           │ │   │░░│   │░░│     │  │    │ │    ░░░│   │░│   │░        │ │
                           │ │   │░░│   └──┘ •   │░░│    │░│    │░ │   │░│    ──       │ │
                           │ │   │░░│            │░░│    │░│    │ ░│   │░│             │ │
                           │ │   │░░│            │░░│    └─┘    └──┘   └─┘             │ │
                           │ │   │░░│   ┌──      │░░│    │  •      │                   │ │
                           │ │   │░░│   │░░      └──┘    │ •    │  │                   │ │
                           │ │   │░░│    ──               •     └──┘                   │ │
                           │ │   └──┘                                                  │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │      •  ──────                                          │ │
                           │ │  ┌──┐░──   ░                                            │ │
                           │ │  │░ └─░░    ──                                          │ │
                           │ │       •       •        ──         ┌─    •  ──────       │ │
                           │ │   ┌───  ────── ────── │░░─── ─────┘ ──── ──░      ────┐   │
                           │     │░░░ • ░ ░    ░░░   └─ ░   ░  ░   ░░░    ░     •    └─  │
                            •       •                      │   •   • │   │ │   •        ─┘
                             ─┐  │   •  ┌─ •   ┌─   │ ┌─   │ ┌─   │ ─┘   │ └┐─  ─┐─   ┌─
                              │  │ │ ░│ │░│    │░ │ │ │░ ░ │ │▒│  │░░│ ░ │░ │ ░  │░│ ░│
                              └──┘─┘ ─┘─┘─┘────┘──┘─┘─┘────┘─┘─┘──┘──┘───┘──┘─── └─┘──┘
                                    •











```

*Figure from page 36 (2346x3317 px)*


---



5-14-4. File Edit Starting Processing



4203-E P-247



SECTION 2 PROGRAM OPERATION



If the first data block of a file, selected for editing, is the "in-editing" symbol (see 5-14-1), the message of



"under repair of error file." is displayed.



If the file includes the "not-guaranteed area" symbol (see 5-14-3), the screen where the "not-guaranteed



area" symbol is included is displayed.



Example: File not including the "not-guaranteed area" symbol


#### PROG OPERA Tl ON EDIT P MODE

>::!ID 000



NlOO GOO X300 Y300 S250



N101 G56 Z-55



Nl03 G41G01 X400 Y200 F100



N104 G03 X500 Y300 10



N105 XlOO Y300 J-200



N106 X200 Y200 1100



Nl07 G01 X400



N108 G40 X300 Y200



Nl09 GOO 2100



N110



Nl 11



=EA.MIN



under repair of error ti le.



Please file maintenance.



LINE LINE CHAR. CHAR. LINE



INSERT DELETE INSERT DELETE DELETE ERASE



Example: File including the qnot-guaranteed area" symbol


#### PROG OPERo\TION EDIT P MOOE

>::@1000



NlOO GOO X300 Y300 S250



N101 G56 2-55



N103 G41G01 X400 Y200 F100



N104 G03 X500 Y300 10



N105 XlOO Y300 1-200



N106 X200 Y200 1100



N107 GOl X400



N108 G40 X300 Y200



N109 GOO 2100



N110



Nl 11



=EA.MIN



under repair of error file.



Please edit because abort editing in the page.



WHEEUOO. MIN



97/07/15 14:10:00



M09 M03



011



JlOO



EDIT



QUJT (EXTEND]



WHEELJOO.MIN



97/07/15 14:10:00



M09 M03



011



JlOO



LI NE LI NE CHAR. CHAR. LI NE ED IT



INSERT DELETE IN SERT DELETE DELETE , ERASE OU IT [EXTEND]


```text


                                                                                                 ──
                                                                          ┌─────┐─┐─┐─┐─────────░░░──────────
                                                                          │░░░░ │░│ │ │░░░░░░░░░ ──░░░░░░░░░
                                 •        ────────────────────────────────┘─────┘─┘─  └─────────      •
           ┌─────   ───────────── ────────                                                                  │
           │         ░             ░                 •      •             ──    ──────           ───────────┘
           └────┐ ┌─            ──┐   ───┐  ───────── ─────  ─────────────    ──
                │ │░• ░ ░ ░░   ░  └─┐   ░│ │    ░  ░       ┌─  ░       ░  │ ┌─     ┌──     • │ ─────────────┐
                └─┘─              │ │  ─┐ ─┘       ────────┘ ─────────────┘ │ ─────┘  ────  ─┘      ░    ░  │
                     ░     ░    ░ │ │░• │░ │ ░  ░░│
                  │░                              └────  ────────────────────────────┐───┐─────┐──┐─────────┐
                 ┌┘─┐   ────   ───────   ░ ───── │    ░  ░        ░      ░        ░░ │░ ░│ ░ ░ │  │░ ░░░ ░░░│
                 │░░│ •░░░░░ ── ░░░░░░────┐░░░░░─┘                •      ────────────┘───┘─────┘──┘─────────┘
                 └─      ┌─┐    │         │   •    ────────┐────┐─ ─────┐
                 │ ░░ ░ ░│ │ ░│ └─ ░  ░░ ░ ░░• │ ░░░░░░░░░░│ ░ ░│ •░ ░░ │
                 └───────┘  ──┘─┘              └──────     └────┘       │              •
                                 ──────────────       ────┐      ┌──┐───     ────────   ──
                            │     ░▒▒░░▒▒▒▒░▒░         ░░░│      │░ │▒▒ ─── •▒▒░░░░░░│    │
                            │ │       ────────────    ────┘─ ────┘──┘──░▒░░░░───░░░░▒└─ │ │
                            │ │  ┌───┐             ──       │          ─────    ─────   │ │
                            │ │  │▒░░│   ┌──      │  │    • │    ───┐                   │ │
                            │ │  └──░│   │▒░─┐    │  │      │   •░░░│   •░•   │░│       │ │
                            │ │  │░ ░│   │░│░│    └──┘    ┌─┘    ───   •░  │  └─┘       │ │
                            │ │  │░░░│   └─┘─┘    │░░│    │░│   •   │   │ ░│            │ │
                            │ │  │░░░│   │        │░░│    └─┘    │░░│   │░─┘            │ │
                            │ │  │░░░│   └─┐      │░░│    │ │    └──┘   └─              │ │
                            │ │  │░ ░│   │░│      └──┘    │░│   ┌┘                      │ │
                            │ │  │░ ░│   └─┘              └─┘   │░░░│                   │ │
                            │ │  │░ ░│                          └───┘                   │ │
                            │ │  └───┘                                                  │ │
                            │ │                                                         │ │
                            │ │     ───                                                 │ │
                            │ │  ┌──░░░──           ──┐                                 │ │
                            │ │  │░░░  ░░──┐────────  │                                 │ │
                            │ │   ──░░ • ░ │   ░ ░░       ┌───────     ──      ─┐────── │ │
                            │ │ │    ┌─     ───   ┌─   •  │          •   ─┐─┐ • │       │ │
                            │ │ │ ┌──┘  ┌───   │░─┘   │░┌─  ┌───┐  ──░│   │ │    ┌────┐ │ │
                            │     │░░░  │░ ░┌─ └─░░   └─┘░  │░░░│  ░░░│   │  │   │░░░░│   │
                             ── •      │    │ │      │                │      └─  │   ─┘  •
                               │  ░░   │ ░░   │ ░░   │  ░     ░│    ┌─┘    ░      │░  │
                               └───────┘──────┘──────┘─── ░• • │ •  │ │ •░  ┌─ •  │   │
                                                              •      ─┘─ ───┘ • •  ───┘
                 ────────  ┌─────────── ──  ── ┌───────  ────   ────         •
                      ░    │       ░     ░   ░ │░░ ░░░░░  ░ ░  │░ ░░░•
                  ───────   ───                └─    •     ──  └─                      •
                                ───────────────  ──── ─────  ──  ───────    ──────      ─┐
                            │  •  ░▒▒ ▒░▒▒░░▒          ▒░░        ░░▒▒▒ ─── ▒▒░░░░ ░░░   │
                            │ │       ────────────   ────── ─────────── ░░░░────░•░░── • │
                            │ │  ┌───              ─┐      •           ─────    • ──    │ │
                            │ │  │▒░░│   ┌─┐      │ │    │  │   ┌──┐                    │ │
                            │ │  └─░░│   │░└──    │      │  │   │░░│   ┌──    │░│       │ │
                            │ │  │░░░│   │ ░░     └──    └──┘   │ ─┘   │░ │   └─┘       │ │
                            │ │  │░░░│   └────    │░░│   │░░│   │░ └┐  │  │             │ │
                            │ │  │░░░│            │░░│   └─░│   │ ░░│  │░┌┘             │ │
                            │ │  │░░░│   ┌─┐      │░░│   │  │   └───┘  └─┘              │ │
                            │ │  │░░░│   │░│      └──┘   │░┌┘   │                       │ │
                            │ │  │░ ░│   └─┘             └─┘    │░░│                      │
                            │ │  │░░│                           └──┘                   │ │
                            │ │  └──┘                                                  │ │
                            │ │                                                        │ │
                            │ │     ───                                                │ │
                            │ │  ┌── ░░─┐       •   ──                                 │ │
                            │ │  │░░   ░│ ────── ┌──  ───── •  ┌─────                  │ │
                            │ │  └──░░ ─┘  ░░░ ░ │░ • ░   ░  ──┘░ ░░░• ┌─        ───── │ │
                            │ │ •   ┌─     ┌──    ┌─           │   │   │ ─┐┐  ┌─┐      │ │
                            │ │   ──┘   ───┘    ──┘   ────  ┌──    └───   └┘─ │ └─────┐┘ │
                            │  •  ░░░   ░░░    •░░░   ░░░░  │░░ ░  │░░░   ░  •   ░░░░░│  │
                             ── ┌─                          │                       ──┘ •
                                │ ░░ ░   ░░    ░ ░    ░      ░░     │░─┐   │░ ░ │ │░  │
                                └────░ • ── ──   • ────── ── ── │ ░ │░ │ ░ └──┐ │ │░ ░│
                                │    ── •  •  ─── •      •  •  ─┘─── ──┘───   └─┘─┘───┘
                                                                             •










```

*Figure from page 37 (2346x3317 px)*
