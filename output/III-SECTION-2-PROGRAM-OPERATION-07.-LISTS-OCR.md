# III SECTION 2 PROGRAM OPERATION 07. LISTS OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-07.-LISTS-OCR.PDF*

---


## 7. List

4203-E P-262



SECTION 2 PROGRAM OPERATION



The list function outputs the list of a file to the display screen, printer, or other external device.



This section describes the details of the list function using the screen for the output device.



The operating procedure is indicated below.



(1) Press function key [F6J (LIST).



;:::



MJLTI


#### DATE DIR PIP EDIT PIP LIST CONDENS [EXTEND]

@J (ill



Press [F6] (LIST).



The screen changes to the directory-selection-



based file operation screen and the following is displayed on the screen.



LIST


#### PROGRAM OPERI\TION

LIST


#### INDEX DISPLAY PROCEDURE

[F2]-+ llll:*.MIN



[F3] - FOO:*.MIN



197/07/15 14:10:00


#### OVER'tfl IT E

TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl] •



INPUT THE DEVICE NAME ANO FILE NAIE, THEN PRESS [WRITE] KEY.



DEFAULT DEVICE NAME



= M)l:


#### DEFAULT FILE NAME= *.MIN

>XL



W'll: FOO: COMMAND OVERWR/ CHAR.



INDEX INDEX INDEX HI STORY INSERT DELETE CANCEL



@J @J@ @J @J @J@


```text


                                                                                               ───       •
                                                                         ┌───────┐───┐─────────░░░───────░─┐
                                                                         │░░░░░░░│ ░ │░░░░░░░░░ •░░░░░░░░•░│
             ──────     ─────────────────────────────────────────────────┘───────┘── └─────────      •
          ┌─┐         •
          │░└───── ┌── │
          └─┘      │░░─┘
                ┌──     ──┐─┐──┐──┐─┐──┐────┐──┐─┐─────┐─┐────┐─┐────┐──────────┐────┐────────────┐
                │░ ░ ░░ ░░│░│  │░░│░│ ░│░ ░░│░ │░│ ░░ ░│ │░░░░│ │  ░░│  ░░░   ░ │░   │ ░   ░ ░    │
                │         └─ ──┘  └┐┘ ┌┘ • ─┘  │  │     •   ┌─  │    └─    ─┐  •    ─┘           ─┘
                │░░░ ░░░░ │ │░░░░░░│ ░│ •░░░░│ ░ ░│ •░ │░░░░│  │░░│ ░░ ░  ░░│ │░ ░░ ░ ░░  ░░░░░┌─
                │         └─┘      └─    ──  └──  └─ ─┐┘────┘──┘──┘─────────┘─┘────────────────┘
                │ ░  ░░░░░ ░░░ ░░░░░░│ ░  ░░░│░░░░░░░░│
                └┐ ┌─┐  │  ─┐    ┌─┐ │ ┌──   └─ ┌─────┘
                 │ │ │░ │░│ │░░░░│ │░│ │ ░ ░ ░░░│
                 └─┘ └─┐┘┐┘─┘────┘─┘─┘─┘────────┘
                       │ │                                                                 ┌─┐
                       │ │                                                                 │ │
                       │ │                                                                 │ │
                       │ │  ┌─┐─── • ───── ────────────────         ─────                  │ │
                       │ │  │░│     •     │                 ┌───  ─┐                       │ │
                       │ │  └─┘─┐ │   ┌─┐ │          ┌┐     │░  ┌─░│  ┌─ ┌───────    ──┐─┐ │ │
                       │  ──┘░░░└─┘ ──┘░└─┘ ────────┐┘┘───  └───┘    ─┘░ │░░░░░░░• ──  │░└─  │
                        •    ───┘       │           │       │   │   •     │   │ •       •   ─┘
                         ──     │     ──      ──      ─┐── ─┘┐─  ──┐ ┌─┐ ─┘░ ─┘   │░░─┐   ──
                               ░    ░ ░   ░   ░   ░░ │ │ ░ ░ │░│ ░ │ │░│ ░░ ░ │ ░ │ │░│ ░│
                            ─────  • ──── ─── ──┐ ── └─┘─────┘─┼───┘  ┌┘ ── ──┘ ──┘ └─┘ ─┘
                                 ── •    •   •  └─  •          │    •░│ •  •   •   •   •
                                                         ░░ ░░░░ ░    │
                                                       ──────────── ──


                           •  ──  •  ───     • • ─────   ────
                      ─────░░░░░──░░•░░░ ──── ░░░░░░░░ •░░░░░───┐──────┐─┐──┐──┐─────┐
                      ░░░░░────░░░──░───░░░░░──────────░───── ░ │░░░░░░│ │░ │░ │░░░░░│
                      •        ───  •   ────           •     ───┘──────┘─┘──┘──┘─────┘
                       │░─┐
                       └─░│
                         ─┘  ──                 ────────────────────
                            •  ──┐──────────────                    ──                  •
                           │  •  │░░░░░ ░░░░ ░░ ──                    ───── •   ─────    │
                           │ •   │  ┌──────────                        ░░░░░░ ░░░░ ░░│   │
                           │  •  │░░│           ───────────   ───────────────░░░────┐┘ │ │
                           │ │   └──┘─────                 ───               ───    │  │ │
                           │ │                                                      │  │ │
                           │ │                      ────────────────────────────────┘  │ │
                           │ │   ┌──┐──┐────┐──  ░•                                    │ │
                           │ │   │░░│ ░│▒░░ │░░ ── │                                   │ │
                           │ │   │░•  ─┘░• •▒░░    │  ┌───   ──                        │ │
                           │ │   │░░ ░░░• •░░─┐───░└┐ │░░░──░░░───────┐─┐─┐──┐──┐─     │ │
                           │ │   │░░░ •░ •░░░░│░▒░ ░│  ── ░░░──░░░  ░░│ │░│ ░│ ░│      │ │
                           │ │   │▒░░ ░ ░░░░ │▒┌─ │░░     ──    ─── ──┘─┘─┘──┘──┘─     │ │
                           │ │   └───────────┘─┘  └──                                  │ │
                           │ │                        •                                │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │  ┌─┐                                                    │ │
                           │ │ ─┘ └─         •                         ──────── ────── │ │
                           │ │  │      ──┐ ── ──┐  ┌───────────┐──┐──          │       │ │
                           │ │   ──┐   ░ └─    ░└┐ │░░▒░░   ░░▒│  │░░──┐ ┌──── └──    •  │
                           │    •░░│   •░│    • └┘  ┌───── ───┐┘ ─┼── ░│ │░ ░  │
                            ── •      •          │  │         │   │      │     └─────
                              •  ░░   ░ ░░   ░ ░░   │░░░    ░░░    ░░░    ░ ░    ░░  │
                               ───────────── ───────┘──────────────────── ────── ── ─┘
                                                                         •      •  •

















```

*Figure from page 1 (2346x3317 px)*


---



4203-E P-263



SECTION 2 PROGRAM OPERATION



(2) Enter the file name of the file for which the list should be displayed and press the WRITE key.



Example: BOX-1.MIN



Note that it is not necessary to inputthe file name for the program for which file name is not specified.



In other words, for outputting the list of A. MIN, input of the file name is not required.



PROORAM OPERATION



197/07/15 14:10:00



LIST



L BOX-1. Ml NII]



INDEX DISPLAY PROCEDURE



[F2] - M01:*.MIN



[F3] -+ FOO:*. MIN



OVERWRITE



TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl] ,



INPUT THE DEVICE NAME /HJ FILE NAME, THEN PRESS



DEFAULT DEVICE NAME= t.01:



[WRITE] KEY.



DEFAULT FILE NAME= *.MIN



>XL



1,01: FOO: COMMAND OVERl'IR/ CHAR.



lll>EX INDEX INDEX HI STORY INSERT DELETE CANCEL /9-WR-ITE___,,



The list of file BOX-1.M IN is output to the screen.


#### PROGRAM CPERt.TION LIST


#### LIST MD1 :BOX-UIIN

>;;!IDOOO



N100 GOO X300 Y300 $250



N101 G56 Z-55



Nl03 G41GOI X400 Y200 F100



N104 G03 X500 Y300 10



N105 XlOO Y300 1-200



N106 X200 Y200 1100



N107 G01 X400



N108 G40 X300 Y200



Nl09 GOO 2100



NllO



=XL



=L BOX-1.MIN



DATE



DIR PIP EDIT



MULTI



PIP LIST



97/07/15 14:10:00



P E


#### M09 M03

Dl 1



J100



CONDENS



[EXTEtll]



@ @J @J@ @J @J @J@


```text


                                                                                                ──       ──
                                                                          ┌─┐───┐─┐───┐─────┐───░░───────░░│
                                                                          │░│░░ │░│   │░░░░░│░░░ •░░░░░░░░─┘
           ┌──────   •             •                        •  • ───    • └─┘─ ─┘─┘─  └─────┘───     ──
           │      ┌─┐ ┌───┐──────── ────────┐──┐──┐─┐──────┐ ─┐ •   ───┐ │    •     ──          •           │
           └──────┘░│ │░  │                 │ ░│  │ │      │  │        │ │                   │     │ •   ───┘
                  └─┘ │   └──   │ ──        └──┘──┘─┘──────┘──┘  •   ──┘ │   ░      • │    • │ • ──┘─   │
                      │░    ░░──┘░░ ░   ░ ░─┘                  ── ───   • ────────── ─┘──── • • •    ───┘
                      │     ─┐   ──                  ──
                      │░    ░└──          ──      ───  ────    •     ───────      ────┐─── •    ────────────
                      │         ───          ────           ──┐ ┌─┐       ░   ┌───    │   •░───┐     ░
                       ┌───────░░ ░──────────░░░ ───────────░░└─┘░│ ──────────┘░ ░ ░  │░•░░░░░░└────────────
                       │                                         •             ───────┘─ ──────
                      │   ──┐─────────────
                      │ ┌─  │░░░▒░░░░░░░░                                    ──┐─  │
                      │ │ • └─ ───────────                        ░░░░░░ •░░░░░│   │
                      │  │   ░░           ──         ───────   ────────░░▒─────┘  ─┘
                      │  │ ┌──── •░ ───     ─────────       ───        ───       │ │
                      │ │  │      ──                                          │  │ │
                      │ │  │                   ───────────────────────────────┘  │ │
                      │ │   ┌─┐───┐────┐──────                                └──  │
                      │ │   │░│   │░░░ │░░ ░ ░•                  ─────────────   │ │
                      │ │   └─┘   │░░ │▒░        ───    ──                       │ │
                      │ │  •░ │ ░•░░ ░│░│ ─────┐─░ ░───░░ ░┌─────┐─┐─┐───┐─┐     │ │
                      │ │   •░└─ ░░ ░░ ░└─░▒  ░│ ┌── ░░────┘  ░░░│ │░│ ░ │░│     │ │
                      │ │  │░░░░│ │░░ ░ ▒░┌───░│ │    •     ─────┘ └─┘───┘─┘     │ │
                      │ │  └────┘ └───────┘   ─┘                                 │ │
                      │ │                                                        │ │        ┌─────┐
                      └─┘                                                        │ │       ┌┘     │
                      │░│                                                        │ │       │ │     │
                      │░│  ┌─                                                    │ │       │ └─┐─┐ │
                      │░│ ─┘ • ──                                 • ────┐─────── │ │       │░ ░│ │░│
                      │░│  │     ───┐    ──┐ ─┐─┐───┐─────┐────┐ • │    │        │ │      ─┘┐─  ─┘░│
                      │ │  └──┐   ░ └┐    ░└┐ │ │░░░│ ░░░░│  ░░│   └┐──┐  ┌───   │ │   │ │░ │▒│ ░  │
                      │ │  │░ │   •░░│   │░└┘ └─┘───┘ ────┘─ ┌─┘  │ │░░│  │        │   │ └──┘─┘────
                        │ ─┘ • ──    │ ──┘  │                │    │ │    • ───── •      •
                         •  ░░ ░ ░░░░    ░░░    │░░    ░░     ░░     ░░ ░ │ ░░ ░•
                          ──────────────────┐───┘─────────────────────────┘─────
                       ──                   │
                      │         ░─────── ───┘───────────────────
                      └────────                   ░                                 ──
                                  ─────┐─┐──┐──┐        • ──┐                         ───┐
                            │   ─┐░░░░▒│░│░░│ ░│         │ ░│          ───────    ────   │
                            │ │  └─────┘┐  •   │ ──     ─┘──┘────────┐  ░ ░░░░ │░ ░░░     │
                            │ │     ░   └┐░ ░░░  ░ ┌────             └────────░│▒────── │ │
                            │ │    ──    └─────────┘                            •       │ │
                            │ │                                                         │ │
                            │ │  ┌┐                                                     │ │
                            │ │  └┘──░             ─┐     ┌─┐                           │ │
                            │ │  │░░░│   ┌─┐      │░│    ┌┘░│   ┌──┐    │     ┌─┐       │ │
                            │ │  │░░░│   │░│      │ │    │  │   │ ░│   ┌┘──   │░│       │ │
                            │ │  │░░░│   │░│      └─┘    └──┘   │░  │  │░     └─┘       │ │
                            └─┘  │░░░│   └─       │░░│   │░░│   │ ░░│  │░ •             │ │
                            │ │  │░ ░│            │░░│   └──┘   └───┘  └──              │ │
                            │ │  │░░░│   ┌─┐      │░░│   │  │                           │ │
                            │ │  │░░▒│   │░│      └──┘   │  │   ┌─ │                    │ │
                            │ │  │░░│    └─┘             └──┘   │  │                    │ │
                            │ │  └──┘                             •                     │ │
                            │ │  │   • ────                                             │ │
                            │ │ │   ░░  ░ ░                      ──────   ──── ───────  │ │
                            │ │ │  ──   ───                ┌──┐──             │         │ │
                            │ │   •  │ │       ┌─┐    ┌┐   │ ░│   │  ┌┐ ┌─────┘  ┌────┐ │ │
                            │  ──┐░┌─┘ └────── │░└── ─┘┘── └──┘   └──┘┘ │░░░░░░│ │░ ░░│  │
                             •   └─┘ │        │                ──     │ └─────┐┘ │   ─┘  │
                              ─┐─    │ │      │       ──     │      ┌─┘ │     │   │   │
                               │   │ ░ │  ░      ░      │ ░│ │░│  ░ │░   ░ ░│     │░ ░│
                               └───┘ ──┘ ───────────────┘──┘─┘─┘ ───┘───────┘ ────┘───┘
                                    •   •                                    •














```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-264



SECTION 2 PROGRAM OPERATION



[Supplement] 1. The list of a file is displayed in units of 12 lines per page.



If the list cannot be displayed on one page, the"=" code which indicates that the



control is waiting for next command input is not displayed on the command line and



the cursor remains as it was. Possible operations and the results are as indicated



below.



(a) When the BS key is pressed, the display page will advance by one.



(b) When the WRITE key is pressed, the display page will advance



continuously up to the last page. To stop it, press the BS key.



(c) When the CANCEL key is pressed, the command is aborted with the



display page unchanged.



Example: When the list of a file is large



(1) press function key [F6] (LIST) and the WRITE key. This will display



the first page of the list.



(2) press the BS key repeatedly until the required page is obtained.



(3) press the CANCEL key to abort operation.



(4) the next function can be started with the display unchanged.


## 2. When a file name has not been entered, the screen will display the list of the file

"A.MIN". That is, pressing the WRITE key without entering a file name has the



same effect as entry of the file name "A.MIN".


## 3. The device name to which the list of a file is output can be specified following the file

name.



Each output device is provided with a code as specified below.



Display screen on the NC operation pane PN



Printer PR



Teletypewriter TT



Specify the code of the output device folio wing the file name with a delimiter","



placed between them. Key in ":" after the output device code.



When an output device code is not specified, the system selects the display screen



on the operation panel as the output device.



Example 1: = L LJ ,PR: [WRITE]



The list of the file named A.MIN is output to the printer.



Example 2: = LLJ BOX-1.MIN,TT: [WRITE]



The list of the file named BOX-1.MIN is output to the teletypewriter.


```text


                                                                                                ──        •
                                                                         ┌──┐──────┐─┐──────────░░░───────░│
                                                                         │░░│ ░░░░ │ │░░░░░░░░░░───░░░░░░░─┘
           ┌────            ─────────  ──  ──     ─── ─────────────┐───   ──┘──────┘ └─────────
           │     ───────────         ──  ┌─  ────┐   │             │   ┌──                                  │
           └────┐░          ┌───┐─┐─┐    │       │   │          •  │   │          ┌─── ─────────────────────┘
                └──  ───────┘   │ │ │    │ │ │░      └─          ─┐    │          │░░ •
                   ──               │      │ │                    │    │               ──  •  ──────   ──  │
                                    │  ── • ─┘───── ─────┐────────┘────┘───────────────  ─┐ ──   ░░░───░ ──┘
                                     │░ ░• ░ ░░░░░░    ░░│ ░░░░░░░░░ ░░░ ░ ░░ ░░░░░░░░  │░│ ░░░░░░░ ░░░░ ░░░•
                                    ─┘░──░ ░───────░░ │░─┘░░──────░░░──░░░ ░░ ───────░• └─┘ ░──────── ░ ░░ │
                                     │    ┌─       ───┘─  ──      ───  ───────       • •   ──        ──────┘
                                    │     │
                                    │  ─┐ └──────┐ ────────────────────────────────────────────────┐
                                    │ │ └─       │          ░           ░ ░░  ░░░    ░  ░     ░   ░│
                                    │ │ │                                                       ┌──┘
                                    │   │ ░───────  ░   ░░┌───░░░──░░ ░ ░──░░░░░•░░░──░░│░░░─┐ ░│
                                        └──░░░░░░░────────┘ ░░───░░── ───░░───── ─── ░──┘───░└──
                                    ┌─┐ │                                                       ┌───┐
                                    │ │ │░────┐───░░░──░│ ─── ░ │░░░░░│ ░│    ░░░░ ░ ░ ░  ░░  │░│ ░ │
                                    └─┘ └─    │   ──┐  ─┘     ┌─┘─────┘──┘────────────────────┘─┘───┘
                                        │           │     •   │
                                        └─  ░ ░ ┌─  └─░─── ──░│     ░│     ─┐
                                        │  ─┐   │ •          • •  •  │      └┐─┐────────  ┌────────────
                                        │ │ │░ ░░ ░─────░ ┌─┐ ░░│  │░│  ░ ░ ░│ │░░ ░░     │     ░
                                        └─┘ │ │         ──┘░│ • └──┘─┘───────┘─┘───────── └──────────────
                                            └─┘ ── ──┐░•  └─┘  •
                                        ┌─┐ │  •     │   │   ┌─  ──────┐────┐─┐──┐──┐─┐──┐───┐──────┐
                                        │ │ │░ ░░ ░│ └── │░  │░░░░░░░  │░  ░│ │░░│ ░│ │░░│ ░ │░░░░░░│
                                        │ │ │   │ ┌┘    ─┘   └┐  ───┐──     └─┘ ─┼──┘─┘──┘───┘──────┘
                                        │░│ │░░░│ │    ░░░ ░• │░│ ░ │░░░  ░░░░░░ │
                                        │ │ │ ┌─ •        ┌─ • ─┘  ┌┘──┐         └────┐─┐────────┐
                                        │░│ │░│ │░• ░░░░░░│ •░• ░  │░░░│ ░░░ ░ ░ │░░░░│ │░░░░ ░░░│
                                ┌─┐  ┌──   ─┘ │ │                                                 ┌────────┐
                                │░│ ┌┘░░─── ░░└─░░░░ │░─────┐░░░──────░──── ───░░──┐── ░•░░░──░░ ─┘ ░ ░░░ ░│
                                └─┘ └┘ ░░░  ──   ─── └─     └──   ░░░ •        ──  │   • ───  ┌─     │ •   │
                                                    •  │                     ──   • • •     ──┘ •    │   ──┘
                                    │░░ ░ ░░░ ──░ ░ ░░ └─────── ──░░  ░ ────
                                ┌─┐ │                                ─┐     ────┐──┐───────────────────────┐
                                │ │  ┌── ░░  ░ │░ ░ ░ │░░░░░░░ │░ ░ │░│ ░ ░ ░░░ │░ │░ ░░░░░░░░░░░░░░░░░░░ ░│
                                └─┘  │░ ───    └─ •  ─┘─  ──   └─   └─┘   • ──  └─   ─── ──────────────────┘
                                    │      ───┐  • ─┐   ─┐  ┌─┐  ┌─┐   ──┐ •  ┌─  ──┐   •
                                    │░░░│ •░░░│ •░ ░│ ░ ░│░ │░│  │░│  ░░░│ ░│ │░░░░░│ ░░░░░│
                                    └───┘─          └─ ─┐  ┌┘─     └───  │ ─┘ └─────┘──────┘     ┌─┐
                                          │░░░░░  ░ ░░│ │░ │░ │░│ ░░░ ░░│ │░░ │                  │░│
                                          └──── │   ──┘─┘──┘──┘─┘───────┘─┘───┘                  └─┘
                                         •      └───                                               │
                                          ──░░░   ░░░•                                           ░
                                       ───             ──  ───────   •  ─┐─┐─────  ───┐───┐─┐─┐──  ─────┐──┐
                                    ┌──░░░░ ────░░░─── ░░ •░░░░ ░░ •░ ──░│ │░ ░ ░──░░ │░░░│ │░│ ░ │░░░░░│  │
                                    │░░─────░░░░───░ ░───░░ ───────░• ░ •  │░ ──░  ───┘───┘ └─┘   └─────┘
                                    │                                             •       └─   ┌──       ──┐
                                    │░░░• │░────░░ ░░░░░── ░• ░ •░ ░░░░░░░  ░░ ░░░░░  ░░░ ░ ░│ │░░░░░ │ ░░░│
                                    └─── ─┘    ░────────   •     • ──  ───┐──────────────────┘─┘──────┘────┘
                                    │          │             ──┐  •  ──   │
                                    │ ░░░░░┌─  │       ░░ │░░░ │░│
                                    └──────┘ • │ ─────   ─┼─     └──────┐──────┐──┐───┐─┐─┐────┐
                                               │ ░░ ░░   ░│ ─── │░ ░░ ░ │░░ ░ ░│░░│ ░ │░│ │░ ░░│
                                    │ ────────  │   ┌─░   │     └──      •      ──┘─   ─┘ │  ──
                                    └─          └───┘     │        •░       ─┐─┐    ┌──  • ──  ┌──────────┐
                                      ───────   │░░  ░ ░ ░░ │░│ ░░░░░ ░░░░   │░│ ░  │░░│ ░ ░ ░ │░░░░░░░░░░│
                                                └───────────┘─┘──────────────┘─┘────┘──┘───────┘──────────┘




















```

*Figure from page 3 (2346x3317 px)*


---



4203-E P-265



SECTION 2 PROGRAM OPERATION



[Supplement] 4. The option code ";H" allows the operator to add a comment at the beginning of the



list page. Key in ";H" following the output device.



Example: LL...J GEAR-1.MIN,TT:;H [WRITE]



When the instructions indicated above are keyed in, the prompt"!" will appear on



the command line, indicating that a comment can be entered.



A comment consisting of a maximum of 60 characters can be entered in through



the keyboard.



When a command has been entered, press the WRITE key. list output will start.



=L GEAR-1. IIIN, TT: ;H



!MAIN PROGRAM GEAR KOUTEll



DATE DIR PIP



Keyed-in comment


#### MULTI

EDIT PIP UST CONDENS [EXTEND]



List output to the teletypewriter is as shown below. The comment is output to on



each list page.



L MD1 GEAR-1. MIN PAGE1


#### M~N PROGRAM GEAR KOUTEI 1

01000


#### N100 GOO X300 Y300 8250

N101 G56 Z-55 H09 M03



N103 G41 G01 X400 Y200 F100 D11



N104 GOO xsoo Y300 I 0 J100



N105 X100 Y300 1-200 JO


```text


                                                                                                ──        •
                                                                         ┌──┐─┐────┐──┐─────────░░░───────░│
                                                                         │░░│ │░░░░│  │░░░░░░░░░───░░░░░░░─┘
           ┌─────  •         ────────   ──  ───────────── ─────────────── ──┘ └────┘ ─┘────────
           │     ── ─────────        ──┐  ──             •               •   •      •                      │
           └─────░           ───┐ ┌──  │                                   │                •              │
                 ──   ───────   │ │  ──┘┐───  ┌─    │ ┌─┐──────────  ──────┘ ─┐        │   •    ░░         │
                   ───          └─┘ │░░ │░░░• │░░── │ │ │░░░░░░░░░░ • ░░░ ░░ ░└────────┘─── ───────────────┘
                                    │░   ──   │     │ │  • ┌───┐───  ──── ──  │
                                      ───   │  ─────┘░└── ─┘   │   ──          ┌─┐─┐────────────────────────
                                    •░░░░░ ░│ ░░░░  ░ ░░ ░░░ ░░│ ░░░ ░•░ ░ │   │ │ │ ░ ░
                                     ───────    ──  ┌──       │   ──── •   └─  │           ─────────────────
                                    │             • │   • ░  ░│  •        │  •░│      ░ ░ │
                                    │░         │         │ ──  │      │   │    │       ┌─ │ ────────   ────┐
                                    │    ──────┘ ┌───────┘─  ──┘──────┘─── ────┘───────┘ ─┘         ───   ░│
                                    │ ░ ░░░░░░░  │                                                         │
                                    │    ──────  └────────────────────────────────────┐─┐  ────┐──┐─────┐──┘
                                    └┐─           ░    ░  ░░░    ░ ░░ ░ ░░░  ░  ░     │░│   ░  │░░│  ░░ │░ │
                                     │ ┌───────────────────────────────────────────  ─┘─┘──────┘──┘─────┘┐─┘
                                     │ │                                                                 │ │
                                     │ │       •                                                         │ │
                                     │ │  ┌────░─────┐─┐────────                                         │ │
                                     │   ─┘░░ ▒ ░░░░░│░│░░░ ░░░░── ────       ────────┐─ ───── • ──────┐ │ │
                                     │  •░ ──────────┘─┘───────┐░      ┌─────┐        │ │     │░•      │ │ │
                                     │                         │   •   │  ░░ └─ •  ┌─┐  └─────┘░ ┌─────┘ │ │
                                     │  •  ░░┌─   •░──── ─────    •░   └────      ─┘░│ • ░▒░░▒░│ │░░░░▒░   │
                                      ─┐░ ── │                               │           ──────┘ │  ──┐─  •
                                       └─   ─┘    │ ┌─  ┌─  ─┐ ┌─┐ ┌─┐ │   ┌─┘    ┌─┐─┐        │  ┌─  │
                                      │  • │░│  ░ │ │░│ │░ │ │ │ │ │░│ │  ░│▒│  ░ │░│ │ ░ │   ░│ ░│▒│ │
                                      │    └─┘─    ─┘─┘ └──┘─┘─┘─┘─┘─┘─┘───┘─┘┐───┘─┘─┘───┘────┘──┘─┘ │
                                      └────    ┌───    •                      │                      •
                                      │ ░░░░░░ │░░░░░•
                                        ──  ───┘────
                                      •   ──        ┌─────────┐──────┐──────┐───┐─┐────┐──────────┐─┐───────┐
                                     │░• ░░░ │ • ░░ │░░░░░░░░░│  ░ ░ │░░░░░ │░░░│ │░ ░ │░░░░░░░ ░ │░│ ░ ░  ░│
                                    ─┘  ──── │░  ───┘─────────┘──────┘──────┘───┘─┘────┘──────────┘─┘───────┘
                                      │       ──
                                      │          ┌──┐     ┌────────┐                     ─────   │
                                      │ ┌───┐──┐ │░░└───  │░░░   ░░│                      ░░░  │ │
                                      │ │   │░░│ └──░░░   └───── • │                     ───── │ │
                                      │ │   │       ────          ─┘                           │ │
                                      │ │   └──┐        ──    ┌──     •                        │ │
                                      │ │   │░░└─ ┌─┐  │░░│   │░░•   │░•   ┌─     ─┐           │ │
                                      │ │   │░░│  │░│  │ ┌┘   │      │░░│  │░─┐  │░│           │ │
                                      │ │   │ ░│  │░│  │░│   ┌┘──┐   │░ │  └─░│  │░│           │ │
                                      │ │   │ ░│  │ │  └─┘   │░░░│   │░ │ •    │ │ ░│          │ │
                                      │ │   │  │  └─┘         │░┌┘   │░░│  │   │ │ ┌┘          │ │
                                      │ │   └──┘              └─┘    └──┘  └───  └─┘           │ │
                                      │ │                                        │ └───────    │ │
                                      │ └──                        ──          ──          ────┘ │
                                      │    ────────────────────────              ─────────     │ │
                                       ───┐                        ┌─────────────         ─────┘─
                                          └────────────────────────┘





























```

*Figure from page 4 (2346x3317 px)*
