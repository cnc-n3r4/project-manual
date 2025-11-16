# III SECTION 2 PROGRAM OPERATION 04. FILE TRANSFER OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-04.-FILE-TRANSFER-OCR.PDF*

---


## 4. File Transfer

4203-E P-189



SECTION 2 PROGRAM OPERATION



This is the command to transfer a program, with the following sub commands:



Item Command Functions


#### Read READ

Registers a part program after reading it through the tape



reader.



Punch PUNCH Punches out the part program stored in the memory.


#### Verify VERIFY

Verifies the program in the memory with the program on



the paper tape.


#### Copy COPY Copies the program file on memory.

Forward FAST FORWARD Tape reader rapid forward feed motion


#### Rewind FAST REWIND Tape reader rewinding


#### PIP quit QUIT

Ends transfer mode and restores the program operation



mode.


#### Macro


#### MACRO LOADING

Copies files with extension .LIB from 3.5-inch floppy disk



program loading drive to MD1 :.


#### NOTICE


# I :

Never turn off power supply during the execution offiletransfer or file editing. If it is turned off,



the file contents will be unreliable.



4-1. Read



This is the operation to read a part program from program reading device such as tape reader and to store



it in the memory.



The following explanation is given assuming a taper reader.



(1) Set the program tape in the tape reader.



Set this portion rn the



tape reader.



oc><>Oooooooo ---------... --00 000000 -



Tape feed holes



~rogram



Tape feed



file name holes



(2) Press function key (F3J (PIP).



Program name (number) and



machining program



Tape feed holes



The functfon names on the screen wfll change to those given in item (3) below.



::PIP



DATE DIR



"PIP>" is displayed.



MULTI


#### PIP EDIT PIP LIST CONDENS [EXTEt,0]

Press [F3] (PIP).


```text


                                                                                                ───
                                                                          ┌─────┐─┐───┐──┐─┐────░░░░───────░│
                                                                          │░░░░ │░│ ░ │░░│░│░░░░ ───░░░░ ░░─┘
              ─────     •           ──────────────────────────────────────┘─────┘─┘   └──┘─┘────     ───
           ┌─┐     ┌───  ┌────────                                                                          │
           │░└─────┘▒░░  │░░  ░  ░─┐────────────────────────────────────────────────────────────────────────┘
           │░│     └─────┘────────░│
            ─┘   ┌─                 ──────┐─┐─┐───────┐─┐─┐─────┐───────┐─┐─┐──────┐─┐
                 │ ░│ ░ ░• ░░░░ ░░░░░░ ░░ │░│ │ ░ ░░░░│ │░│ ░ ░ │░░░░░  │░│ │░░ ░░ │░│
                 └┐ │  ──       ──  ┌─             ──    ─┘ ────┘────── └─┘ │          ────────────────────
                  │░│    ┌───     ┌─┘ • ─────────░   ┌──                    └────────┐                     │░│
                  │░│    │░░░ ────┘░│     ░░░░░░░────┘░ ──   ──┐   ─────────   ░░░░░░└──         ──────    │░│
                  │░└───  ──      │  ──   ───────    │  ░░───░░│   ░░  ░  ░░  ───┐───░░░  ░ ░░  ░░ ░░░ ░ ░ │░│
                  │░░░░░•         │  ░ ░░          ──┘    ░░░│ │          ──     │   ──────  •       ───── │ │
                  │░     │        │    │  ─┐         │░ │░░  └┐ ─────── •   ───  └─┐─      ┌─ ─┐  ──┐      │░│
                  │░│░ ░░│       ─┘    └──░│        ─┘  │░░──░│ ░ ░░░░ ░░░── ░░ ░│ │░░░ ── │░  │░░░░└┐─   ─┘░│
                  │░└─   │        │░───┘   │         │  │░░░░░ ░    •░ ── ░ ░░───┘ └─── ░░ │░  └─    │ ──  │░│
                  │░░░•░│         │░ ░░░░░░│         │  └┐ •░   ░ ░  ░•     •           ───       ░  │   • │░│
                  │░    │         │░      │          │░ └┘─░░░░░ ░░░    ┌──┐  ─────    │    ─────────┘───  │░│
                  │░░───┘         │ ───── │          │  │░░░───── • ░░░░│ ░│ •░ ░░░░░ ░│                   │░│
                  │░  ░ └───   ───┘░  ░░░ ░────────┐  ░ │           •░     └─   •     ─┘─┐────      •    ──┘░│
                  │░ ░ ░│ ░ ───   │░ ░░░│ │ ░░░░░░░│ ┌─ │░░░ │░░░│ │░░░ ░░░░░░░░░░│ ░░░░░│    ──────       │░│
                  │░░───┘─┐        ─────┘ │░░░░░░┌─  │  └────┼───┘─┘─── ░── ┌─ ───┘                        │░│
                  │░      │       │░      └──────┘   │       │              │ •    ────────────────────── ─┘░│
                  │░░░  ░░└───────┘  ░░ ──           │  ──┐─ ░───── ─────── ░ ░░░░░░  ░░ ░ ░░░░░ ░░░░░░░░│ │░│
                  │░     ┌┘       │                  └─ ░░│░•      •           •                         └─┘░│
                  │░░─── │        │  ───────────────┐┘░ │ │░░──────░░░ │░░░░░░│ ░░░ │░───┐░│░─┐ ┌───┐ ┌─░│ │░│
                  └──     ────────┘─░░░ ░   ░ ░░ ░░░│ • │░░    ░░  ────┘──────┘  ───┘─   └─┘  └─┘   │ │ •  │░│
                  │░░ ░┌─    ░░░ ░  ──────  ───  ───┘  ─┘─────────                                          ░│
          ┌──┐─┐─┐┘──┐ │ •                     ──                  │  ────  ───     ──────         •         │
          │░ │▒│ │▒░▒│ ░   ┌─┐ ░│░░ ──░•░░░░   ░░░─────░│ ░░ ░░░░░░└─ ░░░░  ░░░░─── ░░ ░░░ ░┌─── • ░░ ░░░░░  │
          └──┘─┘─┘───┘───  │░│ ░│    ░ ░  ┌┐   ─┐       └──────────┘ ───────────   ─────────┘   • ─────────┐ │
                           └─┘──┘──────── └┘─── │ ────░─┘                                                  │ │
           ┌───┐   ┌────┐ •              •     • •    •  ──────────────────────────────────────────────────
           │   │  ─┘ ░░░│
           └───  │         ──────────┐───────┐───────┐───┐───┐───┐───────────────┐─┐─┐──┐─┐─┐───┐───────┐───┐
                ┌┘   •   ──░░░ ░   ░ │░░░  ░░│ ░░░░░░│  ░│ ░ │░ ░│ ░░░░░░░░░░░ ░ │░│ │░ │░│ │░░░│ ░░░ ░ │░░░│
                │░ ──░░──░░░•░──      ───   •  •  ──    ─┘   └──     ────────────┘─┘─┘──┘─┘─┘───┘───────┘───┘
                └┐   │          ─────┐   ──┐ ─┐ ┌─  ┌───  ┌──   ────┐
                 │ ░ │░░░░• ░ ░░░░░░░│  ░ ░│░░│ │░░░│░ ░│ │░░░│ ░░░░│
                 │  ┌┘┐    •        • ──┐ •    •  ┌─┘   │ └───┘─────┘
                  │ │ │░░░░░│ ░ │░░░░ ░░│ ░ ░│░ ░░│ │░░░░│
                  └─┘ └─────┘   └───────┘────┘────┘─┘────┘
                             ───
                      ┌──░░──░░░│  │░│
                      │░░ ░░░░──┘──┘ │
                      └──  ───     └─┘ ────────────────────────────────   ──────────────────────────
                     │           ──┘░│                                 ───                          ┌─┐
                     │                                                │   │                         │ │
                     │              ─┐────────┐─         ─┐───────────┘   └───────────┐─           •  │
                                ─── ░│        │ ┌─      │░│              ─┘           │░┌────────── •
                     ┌─┐─┐─┐─┐──   ┌─┘        └─┘     ──┘ │                 ───┐─── • └─┘
                     │░│ │░│ │░░│  │░ ┌─ ░──┐ │░  ──┐ ░░│░│   │ •░────░────  ░░│  ░• ─┘ │ ──────┐─┐──┐
                     └─┘─┘─┘─┘──┘─ └──┘░──░░│ └── ░░│ ──┘─┘── └─░• ░░ • ░  ────┘───   │ │   ░  ░│ │░ │
                                      │                            ──   ───         ──┘─ ───────┘─┘──┘
                  ──┐─┐─────────────── ──── ────
                    │ │ ░░░   ░ ░░░  ░░         │
                  ──┘ │  ──     ──     │     •  └─────────────┐────────────┐───┐─┐─────────┐
                      └─┐         │   ░│    │     ░░  ░    ░ ░│      ░░ ░ ░│   │░│  ░  ░ ░░│
                        └─┐───────┘────┘────┘─────────────────┘────────────┘───┘─┘─────────┘ ─┐
                        │ │                                                                 │ │
                        │ │   ───                                                           │ │
                        │ │ ┌─░   ─────────────────────────      •  ┌────   ──              │ │
                        │  ┌┘ ───                          ────   ┌─┘    ┌─┐      ──        │ │
                        │  │░•    • ┌─    • │     │ •     │  ░ ─┐ │      │ │     •    ──  │ │ │
                        │     ───   │ ────  │ ░ ░ │  ┌─── │░─┐░░│ │  ───┐  └───── • ┌─  ──┼─┘ │
                        └─ ░ │   │                │  │    │  │  │       │ •  ░  ░   │    ░│   │
                             │ ┌─┘ ────┐─┐─ ────┐─ ──┘┐─┐─ ──┘┐─┼───────┘─         ┌┘ •  ─┼───
                         •  •  │░  ░ ░ │ │ ░   ░│   ░ │ │ ░ ░ │░│    ░░░ ░ ░ │ ░ ░ │ ░░│  │
                        │    ──┘───────┘─┘ ──     ─┐─ └─┘ ──┐─┘─  ──┐ ── ░•░─┘───┐─┘ ──┘ │
                        │ ──             └─  ───░• │        │    •  └─  ── •     │ └─   ─┘
                        │       │ ░░░   │       •  │ ░░ ░    ░──
                        └───────┘───────┘         ─┘──────────









```

*Figure from page 1 (2346x3317 px)*


---



(3) Press function key [F1] (READ).



=PIP



4203-E P-190



SECTION 2 PROGRAM OPERATION



[EXTOO]



®@@J@@J@@J@J



\ Press [F1] (READ)



The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.



PIP:READ R


#### PROGRAM OPERATION

PIP :READ



RII]



INDEX DISPLAY PR:lCEDURE



[F2] - Wl:*.MIN



[F3] - FDO:*.MIN



I 97/07/15 14:10:00



OVERWRITE



TO DISPLAY OTHER ltf)EXES, AFTER PRESSING [Fl] ,



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS [WRITE] KEY.


#### DEFAULT DEVICE NAME= Wl:


#### DEFAULT FILE NAME= *.MIN

>XR



l.01: FDO: COMMAND 01/ERWR/ CHAR.



INDEX INDEX INDEX HI STCflY INSERT DELETE CANCEL


```text


                                                                                              ┌──        ─┐
                                                                        ┌──┐──────┐─┐─────────┘ ░░───────░│
                                                                        │░░│ ░░░░ │ │░░░░░░░░░░───░░░░░░░─┘
          ┌──────  ──                    ──       ────────────────────── ──┘──────┘ └─────────      ────
          │      ──  ┌───────────────────  ──────┐
          └────── ░│ │                 ░    ░ ░  │
                 ──┘ └─┐─┐───────────────────────┘
                       │ │                                                                 ┌─┐
                       │ │                                                                 │ │
                       │ │  ┌───┐                                                          │ │
                       │ │  │░ ░│                                                          │ │
                       │ │  │ ──┘─┐─┐─────┐─┐─ ── ─┐─   ───   ── ──      ──────┐─ ─┐───    │ │
                       │ │  │     │ │     │ │    • │      ░• │ ░│  • ┌──┐ ░  ░ │   │       │ │
                       │ └─  ───┐ └─ ┌──┐    ─┐──  │ ┌── •  ─┘░ │   ┌┘░░│   │       ┌──┐─┐ │ │
                       │   ──░░░│ │  │░░└─ • ░│      │░   • ░│░░░   │░░░│   │░     ─┘░ │░│   │
                        ──            │   │ ┌─      │        │  • ─┐┘   │  ┌┘           ─┘ ──
                          ──┐  ░│     └── │ │ ───── │ ──  ┌─ └─┐ • │  •    │  ░     ┌──  │
                            │  ░│  ┌─ ░ ░ │ │ ░ ░ ░    ░│ │░ │ │ ░ │ │░│ ░    •     │ ░ ░│
                            └──┐░│ │     • ─┼─   ┌──────┘ └─  ─┘───┘─┘─┘ ─────   ───┘────┘
                               └─┘ ░ ░░ ░   │░░ ─┘       •  •           •      ──
                                   ──  ─────┘───
                           ────      ──         ───────┐──────┐─┐───┐─┐──┐───┐──┐─┐────┐─┐─────┐─┐─────────┐
                     ┌─────░░░░───░░░░░──░ ░░│ │░░░░░░ │░░░░░░│ │░░░│ │░ │░░░│░░│ │░░░░│ │░░  ░│ │░░░░░ ░ ░│
                     │░░░░░ ░• ░ ░─────░░ ───┘─┘───────┘──────┘─┘───┘─┘──┘───┘──┘─┘────┘─┘─────┘─┘─────────┘
                     │                 ───
                     │░░ ░░░░░ ░░░░•
                     └─────────                ────────────────────────────────────   ─┐
                                ┌────┐─────────                                        └┐
                          │  •  │░░░░│ ░░░░░░░          ─────────────           ────┐─  │
                          │ │ • │ ┌──  ┌──────                       │░ ░░ ░░░░░░░░░│   │
                          │ │   │░│ ░░░│       ─────────────────    ─┘───────░▒─────┘   │
                          │ │  ┌┘─┘────                         ────         ──      │  │
                          │ │  │                                                   │ │  │
                          │  •                 ────────────────────────────────────┘ │  │
                          │ │   ┌──┐────┐─────░░ ░                                   │  │
                          │ │   │░░│ ░ ▒│   ░░─────                                   │ │
                          │ │   │░•    ░│  •░░        ──     •                        └─┘
                          │ │   │░  ──┐░ ──░• ────────░░│ ┌─░░ ─┐─┐──┐  ┌───┐─┐─┐     │ │
                          │ │   │░░░  │░░░░░░•▒▒░ ░░   ─┘░│▒───░│ │░░│  │░ ░│ │░│     │ │
                          │ │   └┐░░░░│░░──┐░▒░─────░ •  • •   • • ──┘  └───┘─┘─┘     │ │
                          │ │    └──── ──  └───     ──                                │ │
                          │ │                                                         │ │
                          │ │                                                         │ │
                          │ │                                                         │ │
                          │ │  ┌──                                                    │ │
                          │ │  │  • • ──   ──             •            • •            │ │
                          │ │  │       ░──┐   ──┐───┐─────  ───┐────┐ • • ─┐          │ │
                          │  • │     • ░  │  •░ │   │░░░░░• ░░░│  ░░│      └┐ ─┐      │ │
                           •   └────   │░ │   │ └─  └────┐  ───┘──┐  •   •  │  │        │
                            ── │  ░ ──┐┘░│ ───┘ │ •      └─       │ │   │    ──┼──┐── ──
                              │     ░ │░ │ ░░ │ │    │ │  ░ │░ │ ░ ░│ ░ │ ░│ ░ │ ░│ ░│
                              └───────┘─ │ ───┘─┘─── └─┘─── └─ └────┘ ──┘──┘───┘──┘──┘
                                        • •         •      •  •      •





























```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-191



SECTION 2 PROGRAM OPERATION



(4) Enter the file name of the file to be punch and press the WRITE key.



Example: TESTS.MIN


#### PROGRAM OPERATION

197/07/15 14:10:00



PIP :READ



R TEST9. Ml NII]



INDEX DISPLAY ~IJlE



[F2] - MD1:*.MIN



[F3] .... FOO:*.MIN



TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl) .



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS



DEFAULT DEVICE NAME = MD1:



DEFAULT FILE NAME= *.MIN



>XR



OVERWRITE



[WRITE]



KEY.



INDEX



tl>l:



INDEX



FOO: COMMAND OVERWR/ CHAR.



INDEX



HI STORY



INSERT DELETE CANCEL



@J @J @J @ @J @ @J @



.._WR_I_TE_,



Pressing this key starts the tape reader. The commands on the tape are read and stored in memory.



While the tape is being read, the screen displays "READ" along with the "file name" on the first line.



When the first EOB code appears after the start of the tape reading-in, the message "VALID



INFORMATION READING" is displayed.



At the completion of the tape reading-in, the tape is then rewound and read in the reverse order to



verify the read and stored program against the program on the tape.



When the tape reading-in and verification is completed, ">" appears on the console line.


```text


                                                                                                ──         │
                                                                          ┌─────┐─┐───┐─────────░░────────░└─
                                                                          │░░░░ │░│ ░ │░░░░░░░░░ •░░░░░░░░─┘
           ┌──────   ──           •             ───            ──   •     └──   └─┘─  └─────────     ────
           │      ┌─┐  ─────────── ─────────────   ─────────┐──  ─── ────┐   ─┐─                            │
           └──────┘░│ │░  ░     ░                           │            │░   │    ─────────────────────────┘
                  └─┘ │         │ ───   ┌── ┌───────────────┘────────────┘────┘── •
                      │░░░░░░░┌─┘┐░ ░   │░░┌┘                                    •
                      └───────┘  └──────┘──┘
                                                                                 •
                      │   ───────────────┐───────────────────────  •              •
                      │     ░▒░▒▒░░░░▒░░░│                       ── ──     ────┐   │
                      │ │ • ┌───    ─────┘─      ───────    ───  ░░░░░░───┐░░░▒│   │
                      │ │   │░ ░▒░░          ────       •      ────────░░▒└────┘   │
                      │ │ • └────── ░────────            ────          ───      •  │
                      │ │  │        •                                            │ │
                      │ │  │                                                     │ │
                      │ │    ─────┐┐─┐─ ──────                                   │ │
                      │ │   │▒░   └┘░│ •░░░░░░                                   │ │
                      │ │   │░│   ░░  │▒│        ───    ──                       │ │
                      │ │  │░ │ ░ ░░ ░│▒│ ─────┐─░░░─┐─┐░ ░─────── ┌─┐─────┐     │ │
                      │ │  │░░└─ ░░ ░░ ░ ░░▒ ░░│ ─── │░└──░░ ░░░░  │░│ ░  ░│     │ │
                      │ │  │░░░░  │░░ ░ ░░┌──┐░ │   • •     ─────  └─┘─────┘     │ │
                      │ │  └───── └────░──┘  └─░│                                │ │        ┌──────┐
                      │ │              •       ─┘                                │ │        │      │
                      │ │                                                        │ │       │        │
                      │ │                                                        │ │       │ ─┐─┐── │
                      │ │  ──┐                                                   └─┘       │  │░│   │
                      │ │   ░│       ──                           • ────┐─┐───── │░│      ─┘ ─┘ └─  │
                      │ │   •    ┌──   ───     ────┐────── ────  │ │    │ │      │ │    • ░░ ░░░ ░  │
                      │ │    ─┐  │░ ─┐─  ░──┐  ░▒░░│  ░░░░   ░░──┘─┘┐──┐  │      │ │   •  ────────  │
                      │   ┌─░░│  └┐░░│  ──░░│  ───░│ ─────░  •░░ ░  │░░│  │     ─┘ │    •
                       • ┌┘  │    │ •     ──┘                    ──  ─┐┘   ─────  •
                         │   │    ░░     ░      ░░   │ ░░ │ │ │░   │  │         ┌─
                           ─┐  ─────┐ ── ──   • ─────┘ ── └─┘ │░ ──┘ ─┼── │  ░ ░│
                      ┌───  │       │   •  ─┐        └─     │      │  │   │     └──────────────────────────┐
                      │░░ ░░   ░   •   • ░ ░│ •    ░ │░│         •   ░│  │░ •                              │
                      └──        •   ─┐      •         └┐─┐─────  ┌───┘  │   •  │  │       │               │
                      │░░ ░ ░░░░░░─── └─┐  ░░░──── ░░ ░░│ │░░░░░  │░░░│ ─┘ │  •░│ ░│  ─┐ │░│ ──┐──░░ ░ ░ ░░│
                      │                 │                  • ┌─  • ─┐      └─  │ •     │ │ │   │  ┌─┐ │    │
                       ┌─ ░──────────┐──┘────┐ │░░░─────░░  ░│ •░░│ │  ░│ │░░│ │░░░│  ░│ │░│ │ ░░░│░│ │░░ ░│
                       │░──░ ░░░░░░░ │░ ░ ░░░│ └───  ░░ ─── ─┘  ──┘    ─┘ └──┘ └───┘─    └─┘ └────┘─┘ └────┘
                      │                                    •  ──   ───┐  •    •      ──┐─   │        •
                      └──░┌── ░░░░░░── ░ ░──░░░──░░░░░░ ──░░░ ░░░ ░ ░░│  ░░░░  ░ ░ ░ ░░│   ░│  ░ ░ ░   ░░   │
                      │  ─┘ ░ ──┐───   ───   •    ────┐    •   •     ─┘ ┌────     ─────┘────┘───────────────┘
                      │         │   •                 │            ░• │ │
                      │░░░░   ░ │ ░   ░░  │   ░     ░  ░░           ░ │          │                 │
                      └─────────┘─────────┘───────────────────────────┘  ────────┘─────────────────┘


































```

*Figure from page 3 (2346x3317 px)*


---



4203-E P-192



SECTION 2 PROGRAM OPERATION



[Supplement} Tape rewinding with or withouttape verification is selectable by setting bits 4 and 5 of NC



optional parameter (bit) No. 1.


#### PROGRAM OPERATION TRANSFER READ

TEST9.MIN



file exist overwrite? (Y/N) !Y



varid information reading



TEST9.MINI



97/07/15 14:10:00



PIP



QUIT [EXTEND]



(5) Press function key [F7] {PIP QUIT).



TEST9.MIN



file exist overwrite? (Y/N) !Y



varid information reading



FAST FAST PIP



READ PUNCH VER IF Y COPY FORWARD REW IN D OU tT [EXTEND]



The screen returns to the one displayed in item (1). Details and precautions on this operation are



given in 4-3-1. "Precautions for Tape Reading-in, Punching-out, and Verifying Operations". Be sure



to read this item.



[Supplement] If an error occurs during tape reading, 31 characters preceding the error character are



displayed on the console line of display screen.


```text


                                                                                                 •
                                                                         ┌───────┐─┐─┐─────────░░░────────░│
                                                                         │░░░░░░░│ │ │░░░░░░░░░ ── ░░░░░░░─┘
          ┌─────             ───                  ───         ──       ──┘────  ─┘   └─────────      ──
          │     ┌───────────┐   ┌─────────────────   ──┐─────┐  ───────       ──  ───          │           │
          └─────┘          ░└───┘░                    ░│     │ │  ░                            │           │
                └───────────┘   │  ──── ────────┐────  │  ───┘─┘──────────── ───    │░ │ •     │     •  ───┘
                                │░░░░ ░ ░░ ░░░░░│ ░░░•░│                    •       └──┘─ ─────┘───── ──
                             ───┘─             ─┘────            ────────
                            •      ────────   │       ─────────┐         ──  ────────┐   │
                           │  ── •░░░░░ ░░░░  └────   ░░░░░░ ░░│ ────┐┐       ░░░░░░▒│   │
                           │ │    ────────────┘    ────────────┘     └┘░ ──  ────────┘   │
                           │ │                                         ──  ──          │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │   ┌──                                                   │ │
                           │ │  ┌┘░ ─────────┐─┐─ ────┐──┐                             │ │
                           │ │  │  ░ ░ ░ ░░░░│ │ •    │  │                             │ │
                           │ │  │    │ ┌─────┘ │    ┌─         ──       ──   ─┐─       │ │
                           │ │ •     │ │            │ ┌─┐ ┌───┐  ─┐───┐─  ┌─┐ │ • ──   │ │
                           │  • │   ─┘─ ──┐ ──┐   ──  │ │ │ ░░└─  │░░ │   │ │ │  •  ───┘ │
                            │   │         │   │         │  ───░   └── │   │     •   ░   ─┘
                            └── └─────  •    • ───┐─┐─── •              ──┘ ───       ┌─
                                 ░░░    ░░░  ░ ░░ │ │ ░░ ░ ░ ░░ ░ ░░░░ ░  ░░░    ░░░  │
                               ───────────────────┘─┘─────────────────────────────────

                 ┌─┐  ────┐──────┐─┐─┐───────────────
                 │░│    ░░│   ░░░│ │░│ ░ ░ ░ ░  ░░
                 └─┘  ────┘──────┘─┘─┘───────────────

                            ┌─┐  ┌─────                                                ┌─┐
                            │ │  │░ ░ ░─┐  ┌─       ──┐                                │ │
                            │ │ │    ░  └──┘ ─────── ░│                                │ │
                           │ │  │         ░     ░░  ░─┘               ───    ─── ────  │ │
                           │ │  │ │ ─┐   ───── ──────     ┌───┐   •      ─┐─    •      │ │
                            │ •   └─ │  │             ──┐ │ ░░└─┐  │░─┐   │ •    ┌────┐┘ │
                            │   │░      │░           •  │ └──░░░│  │░ └┐  │      │  ░░│  │
                             ── │      │                 •      │      │ │   ─┐ │     └──
                               ─┘  │   │ ░░           ┌─┐    │░     │░ │ │  ░ │ │ │░  │
                                │  │ ──┘─── ──      ──┘ │ ── │ ──── │░─┘ │ ┌┐ └─┘ │░ ░│
                      ┌─┐─────┐   ─┘              •     │              │   └┘   │ │   │    ┌┐─    ───  ───
                      │░│ ░ ░░│  │░  ───   ───   │ ──░   ──── • ┌─┐ ──░ ─┐ ░  ──┘─ ──  ────┘┘ ────   •    │
                     │        │  └──           ┌─┘ ░  ░ •    │  │ └─     │   │      ░                     │
                     │░  ──     •             ─┘ └─░───░    ░│  └─  ───    • │ ───░ •░ ░ • ░░  ░  ─── ░  ░│
                      ───░░• ░░ ░░ ░   ──                •                                •   •
                ┌────       ┌──┐     ──   ── ─┐───  ────   ─────  ─────────── ───────────┐ ┌── ─┐───────┐──┐
                │░░░░│░ ░░░░│  └┐────░ ──┐░░ ░│ ░ ──░ ░░│ │░░░░░──░  ░░░░░░░   ░░░░░░░░ ░│ │░ ░ │░░░░░░ │░░│
                └────┘──────┘   │  ░     └───░└─    ░───┘ └───  ░     ──┐────────────────┘─┘────┘───────┘──┘
                                 ────────    •   ────         ───────   │
























```

*Figure from page 4 (2346x3317 px)*


---


### 4-2. Punching Out Stored Program Data

4203-E P-193



SECTION 2 PROGRAM OPERATION



This is the function to punch out the program data stored in the memory.



The procedure is as follows:



(1) Press function key [F3] (PIP).



The function names on the screen will change to those given in item (2) below.



=PIP



DATE DIR



"PIP>" is displayed.



WLTI



PIP EDIT PIP LIST



COtl>ENS [EXTEND]



Press [F3] (PIP).



(2) Press function key [F2] (PUNCH).



=XP



FAST RAST PIP



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEtl>]



Press [F2] UNCH).


```text


                                                                                               ┌─
                                                                         ┌──┐──────┐─┐─────────┘░░─────────┐
                                                                         │░░│ ░░░░░│ │░░░░░░░░░░──░░░░░░░░░│
               ────   •                         •        ──────────────── ──┘──────┘─┘─────────
           ┌───    ─── ─────┐─┐─────┐─────────── ─┐─────┐                                                  │
           │   ── │░        │ │    ░│     ░░      │     │ ┌────────────────────────────────────────────────┘
           └───  ┌┘         ░ │ ┌───┘───────  ░┌──┘   ░ └─┘
                 │ │            │              │       │  └─────────────────────┐
                 │ │ ┌─         │   ─────  │ ──┘ │  ░ ┌┘─              ░        │
                 │ │ │                   │ │   └─┘────┘  ───────────────────────┘
                 └┐┘ │                   └┐  ──
                  │                       └──  ─┐
                  └─  │               •         └─  •   •
                      │         │      │ •   │    ─┐ ┌─┐  ────┐ • ┌────────────────┐───────┐
                      └─────────┘──────┘─ ───┘───  └─┘ └──   ░└─  │             ░  │      ░│
                                                 ──       ────  •   ─────── ─────── • ─────
                        ┌─┐                                                                 ┌─┐
                        │ │   ──┐                                                           │ │
                        │ │  │  │                                                           │ │
                        │ │ ─┘   ─────────── ─────┐───────       ──┐───── ─────── ─┐──────  │ │
                        │  •░ •             │     │         ────   │     •       │ │        │ │
                        │      ─┐      ─┐   │ ┌─┐ │  ┌─┐  │  ▒░    │  ──┐  ──────┘  ┌────── │ │
                        │    │░ └─   ── └── └─┘ │    │░└──┘  ───   │ • ░│ │ ░░▒░░░│ │░░░░░░   │
                         │ ░ └─                      └─          •      │ └───────┘ └┐  ───  •
                         │ │   ──┐     ┌─┐   ──┐─  │   ─┐   ┌─┐─┐ ──────┘          • └─
                        ┌┘ │   ░░│   ░ │░│ ░   │░│ │ ─┐░│ │ │ │░│ ░   ░░│ ░░ │ │ ░ ░ │░│ ░│
                        │ │   ───┘    ─┘─┘ ────┘░│ │  └─┘ │ └─ ┌┘ ──────┘ ── └─┘ ─── └─┘ ─┘
                        │ └─┐     ────    •    └─┘─┘      │ │░ │ •       •  •   •   •   •
                        │ ░░│   ░░░░░░░░•          └──────┘─┘──
                           ─┘   ────────
                 ┌─┐  ┌───┐  ───        ───┐──┐────┐
                 │░│  │░░░│ │░░░░░░ ░│ ░░░ │░ │░░░░│
                 └─┘  └┐─┐┘─┘────────┘─────┘──┘────┘
                       │ │
                       │ │                                                                   │
                       │ │   ───                                                             │
                       │ │    ░░ •   ─────── ─────  ─────                                    │
                       │ │   ───  ┌─        │     ──     ─┐   ──  ─┐  ──┐─── ┌─────          │
                       │ │  •     │ •       │  ──    ┌──┐ └───░░── └┐─░░│   ┌┘░░  ░──────┐   │
                       │  ── ░ ░• └─ ┌┐───   ──  •   │░░│    ░░░░   │ ░ │   │  ───       └┐  │
                        •    ──   │  └┘              └─      ───  │ │       │           ░ │ ─┘
                         ────   ─┐┘──   ───── ───────┘ ────     ┌─┘ │ ┌─┐─┐─┘  ───        └─
                             │░ ░│      ░░ ░ ░ ░░░   ░ ░░     │░│ ░ │ │░│ │ │ ░      ░ ░ ░│
                             └───┘ ───  │░┌─── •   ░ ░ ──  ┌─ └─┘ │ │ │ │ ░ │  ┌────   • ┌┘
                                      ──┘░│   •            │ •   ─┘─┘─ • ───┘─ │    ─── ─┘
                                         •    ░░ ░░░░  ░░░│                   • •
                                           ───────────────┘



































```

*Figure from page 5 (2346x3317 px)*


---



4203-E P-194


#### SECTION 2 PROGRAM OPERATION

The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.


#### PIP:PUNCH P


#### PROGRAM OPERATION

197/07/15 14:10:00



PIP :PUNCH



Pll]



IN:lEX DISPLAY PROCEDlRE



[F2] - MDl:*.MIN



[F3] - FD0:*.MIN



TO DISPLAY OTliER INDEXES, AFTER PRESSING [Fl) ,



OVERWRITE



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS [WRITE) KEY.



DEFAULT DEVICE NAME = MD1:



DEFAULT FILE NAME = *.MIN


#### K>l : FOO:

COMMAND OVERWR/ CHAR.



J tflEX INDEX INDEX



HI STORY INSERT DELETE CANCEL



@ @J @J


# CED

@J @J@@



(3) Enter the file name of the file to be punch and press the WRITE key.


#### Example: BOX-1350.MIN

This step is unnecessary for a program without a file name, i.e., A.MIN.


#### PROGRAM <PERATION

I 97/07/15 14:10:00



PIP :PUNCH


#### P BOX-1350.MIN[I]

INDEX DISPLAY PROCEDURE



[F2] _,. MD1:*.MIN



[F3] _,. FDO:*.MIN



TO DISPLAY OTHER l~ES. AFTER PRESSING [Fl] ,


#### INPUT THE DEVICE NME AND FILE NAME. THEN PRESS

DEFAULT DEVICE



NAME= Jl.l1:


#### DEFAULT FILE NAY:= *.MIN

>XP



wn:



FOO: COMMAND OVERWR/ CHAR.



OVERWRITE



[WRITE] KEY.



ltllEX INDEX INDEX HISTORY INSERT DELETE CANCEL



.,_WR_I_TE...,


```text


                                                                                                •
                                                                         ┌──┐─┐────┐─┐────────── ░───────┐─┐
                                                                         │░░│ │░░░░│ │ ░░░░░░░░░──░░░░░░ │░│
           ┌──────────    •              •                     ──         ──┘      │  ─────────       •
           │          ┌─── ──┐──────────┐ ────┐─┐───────┐──────  ────┐────   ───┐── ──          │       •
           └──────────┘░ ░   │          │    ░│ │       │            │          │       │       │        │  │
                      │  ────┘ •  │ │ ░  •   ─┘─┘───────┘────────────┘─────  ───┘───┐   │ │  ───┘ •      │  │
                      │░░░ ░░ •   │ │ ░  ░ ──                              ──       └───┘ └──    • ──────┘──┘
                      └─── • │     │ ┌─────
                          • ─┘──── └─┘
                                             •  ─────────────────────────  ─────────── ──
                                  ┌────────── ─┐                         ──           •  •
                            │  •  │░░░░░ ░░░░ ░│                               ─────      │
                            │ │   │░│ │░░░│   ─┘                      │ ░ ░ │░░░▒░░░│   • │
                            │ │   │░│ └───┘           ─────       ────┘─────┘───────┘  │  │
                            │ │  ┌┘─┘─     ───────────     ───────                   │ │  │
                            │ │  │                                                   │ │  │
                            │ │       •     •   ─────────────────────────────────────   │ │
                            │ │   ┌─── ───── ┌──░░░░                                    │ │
                            │ │   │░░   ░░ ░ │░░────┐                                   │ │
                            │ │   └─┐   •░• │░│     │  ──    ───                        │ │
                            │ │  •░ │ ░░░  ─┘░│ ────┘┐─░ ────░░░░──────┐─┐─┐───┐─┐─     │ │
                            │ │   │░└┐ •░ •░│░░•░░  ░│  •░ ░░────░░ ░░░│ │░│ ░ │░│      │ │
                            │ │   │░░│  ░░░░░ ▒░┌──┐░│ • • ──    ────── ─┘─┘───┘─┘─     │ │
                            │ │   └──┘─ ────────┘  └─░                                  │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            └─┘                                                         │ │
                            │ │  ┌─┐                                                    │ │
                            │ │ ─┘ │ ──                                 • ──  ┌───────  │ │
                            │ │  │  │   ───┐─────┐  ┌───────────┐──┐─┐ • •    │         │ │
                            │ │  └┐ │ • ░░ │    ░└┐ │ ░░░░   ░░▒│  │░│  •   ─┐         • ┌┘
                            │    └┘ └┐  • ░│   │░ │ │  ──── ─┐──┘  │░│    ── └┐ │        │
                             ── •    └─┐   │ ──┘ ┌┘          │  │  ░   │ │    │ └─┐───┐──
                               •   │ ░ │  │ │░ ░ │ │  │░   ░ │░ │ ░ │░ │ │ ┌┐ │ │ │░ ░│
                                ───┘───┘──┘─┘────┘─┘──┘──────┘──┘───┘──┘─┘─┘┘─┘─┘─┘───┘

                   │  ────┐──┐─── ┌───── • • ──────────────────────────────  ──┐─┐
                   │ │    │  │   ─┘   ░ • │░•      ░       ░ ░ ░ ░░  ░░   ░  ░ │░│
                     │       └──┐░  ┌─┐░░ │   ┌───────────────────────────── ──┘─┘
                     │       │  └───┘ └───┘── │
                      │      │ •     •        └────────────────── ─────────┐──┐──────
                      └─── │ │             │  │     ░ ░                  ░ │  │  ░
                           └─┘        ─────┘       ───── ─── ───   • ──────┘── ─────
                      ──                    •  ────     •   •   ──  •
                     │   ───────────────┐                                        ─┐
                     │  │  ░░░▒▒░░░░░░ ░│                       ┌───        ─── • │
                     │  │  ────  • ──  ┌┘                       │░ ░░░░ ── ░░░░•   │
                     │  │  ░░░ ░░░│    │ ────────  ─────     ───┘──────░░▒┌────  │ │
                     │  └─┐───────┘─░ ─┘─        ──     ─────          ───┘    • │ │
                     │ •  │         ──                                           │ │
                     │  • │                                                    │  │
                     │ │   ┌─┐──────┐─┐──────                                  │  │
                     │ │   │░│  ░░░░│ │░░░ ░░                    ────────────── │ │
                     │ │   │░│   •░░ •▒░     │ ┌───   ───                       │ │
                     │ │  │░ └┐░│░░ ░░░• ────┘┐┘░ ░───░░ ░──────┐─┐─┐───┐─┐     │ │
                     │ │  └─░░│ │░ ░░ ░ •░▒  ░│ ─── ░░────░  ░░░│ │░│ ░ │░│     │ │
                     │ │  │░░░░░ │░░░▒ ▒▒┌──┐░│      •     ─────┘─┘─┘───┘─┘     │ │
                     │ │  └──────┘───────┘  └─┘─                                │ │
                     │ │                                                        │ │          ─────┐
                     │ │                                                        │ │        ┌─     │
                     │ │                                                        │ │        │░│     │
                     │ │  ┌─┐                                                   │ │        │ └─┐─┐░│
                     │ │ ─┘ └─      •                           ───────┐─┐───── │ │        │  ░│ │ │
                     │ │  │    ────  ┌────    ──────────┐───┐─         │ │      │ │        └┐─  •  │
                     │ │  └──┐   ░ ─┐┘  ░░─┐  ░░░░░  ░░░│   │░───┐─┐──┐ ─┘      │ │    ┌─── │▒│ ░  │
                     │    │░░│   │░░│   │░░│  ┌─────────┘░• │░░░░│ │░░└┐ │      │ │    │  ░ └─┘───┐┘
                       • ─┘ • ── │  │   │     │             │   •  │ • └─ ─────  •     └─ ──      │
                        •░ ░░ ░ │░░░    ░░░ ░  ░░░    ░░     ░░   ░ ░░ ░ ░ ░░ ░│              ────
                         ───────┘─────────────────────────────────────── ──────┘
                                                                        •











```

*Figure from page 6 (2346x3317 px)*


---



4203-E P-195



SECTION 2 PROGRAM OPERATION



This starts the tape punching out operation, during which the screen displays "PUNCH" along with



the "filename".



When tape punching-out is completed, the message "file-end" is given on the console line and ">"



appears in the following line.



>P BOX-1350.MIN



file end



FAST RAST PIP



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



(4) Press function key [F7] (PIP QUJTI,



>P BOX-1350.MIN



file end



[EXTEM>)



@J@J@)@@®~@



Press {F7] (PIP QUIT)



This completes the tape punching out operation and the display returns to the mode as in step (1 ).



[Supplement] 1. That tape punching speed will be slowed down while machine operation is carried



out simultaneously.


## 2. Tape Punching Out Format

Feed holes File name Feed holes



(1) (2) (3) (4)



1-----..::.--1 Program name



Machining program



(5)



(1) 600 tape feed holes are punched in the tape leader section.



Feed holes



{6}



The number of feed holes to be punched out can range, as needed, from 1 to 10000 with a



parameter.



For details, refer to IV "PARAMETER", Section 4, 5. "NC Optional Parameter (Word)".



(2) The file name is punched out following the "$" code. (Program data is punched out in the ISO



coding system.)



(3) 50 tape feed holes are punched out.



The number of the tape feed holes cannot be changed.


```text


                                                                                                ───
                                                                          ┌─────┐─┐───┐──┐──────░░░────────░│
                                                                          │░░░░ │░│ ░ │░░│░░░░░░ •░░░░░░░░░─┘
           ┌───────────                        ───  •      ─────────      └───  └─┘   └──┘─   ──     ───
           │           ─────────────┐──────────   ── ───┐──         ┌─────    ──   ───     ───  •          ─┐
           └──────────┐       ░     │                   │░          │░                      ░               │
                      │    ┌─      ─┘───────────────────┘───────────┘────────────────    ────────────      ─┘
                      │░░  │░• ░ ░•                                                                       •
                       │               ──   ── ───────────────────────────────────── ──────┐─────────────
                       └───── ░  ░    • ░───  •     ░ ░░     ░░   ░░   ░ ░      ░ ░      ░ │░ ░ ░ ░ ░ ░░
                       │░░░░░░───── ░░░ ░░ ░ │░┌───────────────────── ─────────────────────┘────────────────
                       └┐─┐───     ──────────┘─┘
                        │ │                                                                 ┌─┐
                        │ │  ┌── ──  ──────┐                                                │ │
                        │ │  │░ •░░── ░░ ░░│                                                │ │
                        │ │  │  ░• ░░┌─────┘ ───── ─────────               ──    ─────────┐ │ │
                        │ │  │ ── ───┘      │     │         │  ──     ┌──┐─   ──┐         │ │ │
                        │ │  │         ── • │ ┌───┘ • ┌─┐   └──░░•   ┌┘░░│   │░ │     ──┐─┘ │ │
                        │  • └┐ ─┐ │  │░░│   ┌┘░ ░ │  │░│  •  ░░░░   │░•░│   │ ─┼─  ┌─  │░└─  │
                         │    │  └─┘  │  └─  │     │ │   •     ──    │   │  │   │   │        ┌┘
                         └── ─┘   ░ ──┘░░░░──┘ ┌───┘─┘ ─┐░┌── │   ───  •  ──┘ ──┘───┘ •   ┌──┘
                            •      ░ ░ │ │ ░   │      │ │ │ ░ │░│     │░│  ░ • ░ ░ ░ │░│ ░│
                             •  ── ░── └─┘ ────┘── ───┘ │ └── └─┘ ─── └─┘ ──  ────── └─┘ •
                                                       • •   •   •   •   •  ──      •   •
                  ┌─┐ ┌────┐──────┐─┐─┐──────── ─────┐
                  │░│ │  ░░│ ░ ░░░│ │░│ ░ ░ ░    ░░  │
                  └─┘  ─┐─┐┘──────┘─┘─┘──────────────┘
                        │ │                                                                 ┌─┐
                        │ │  ┌─────  ──────┐                                                │ │
                        │░│  │░  ░░──░░  ░░│                                                │ │
                        │ │  │   • ░░────── ┌───── ─────── •               ──       ─────── │ │
                        │ │  │    ─┐─       │     │       │ │          ── •   ┌─┐───        │ │
                        │ │    ──  │ ──── •  ┌────┘ • ┌─┐ │ └─────   ┌─░░│   ┌┘░│   ┌─────┐ │ │
                        │  • │░░░• │  ░░░│ │ │░░░    ─┘░└─  ░░░░░░   │░•░│  ┌┘ ─┘   │░░░░░│   │
                         •   └───   • ───┘ │ └──      │ │  ─┐─────── └─  │  └┘  │   │    ─┘  •
                          ──     │ │            •     └─┘   │          •    │    • ┌┘┐─     •
                            │░ ░ │ │ ░ ░░  ░░   ░   ░ │░│ ░ ░ │░│ ░░ ░ ░   ░ │   ░ │ │░│ ░│
                            └─ ──┘ └────── ── ───┐ ── └─┘ ─── └─┘ ────────── │ • ──┘─┘─┘──┘
                              •   •       •  •   └─  •   •   •   •           └─ │
                                                                          ───   └─────────
                                                                             ░ •
                       ┌─┐─┐───────┐──┐─┐─┐──────────┐───────────┐─┐──┐─┐───    ──   ────┐─┐─────────┐─────┐
                       │░│ │░░░░░░░│ ░│ │░│   ░ ░ ░  │░ ░░░ ░░░  │░│ ░│ │░░░░│ •░░│ ░ ░ ░│ │░ ░  ░ ░ │░░   │
                 ──────┘ └─ ┌───┐─┐┘─                            └─  •  └────┘  • │      │  •      ──┘─     │
                │░░░░ ░░░░░░│   │ │   ────────────────       ░     ░ ░   ░ ░   ░ ░              ░           │
                └───────────┘   └─┘ │                 ──────────────────────────────────────────────────────┘
                                    │      ──────── ──
                                ┌─┐ │ ──              ───────
                       ┌────────┘ └─ •░░░ │░ ░   ░   ░  ░ ░░  ─────┐─ ┌┐───────  ────────────┐
                       │        └─┘   ────┘──────────     ──┐      │ ─┘┘                     │
                       │            ┌─                ┌──┐  │      │   │ ─────┐──── ─────
                       │            │░ ░░•        │   │░░│ ░│       │   │     │░░░░│           │
                       │             ───  │ ───── │ │ └──          ─┘───┼───  └─── │           │
                       └─ ──────────    ┌─┼─     • ░│     ────────┐ ░░ ░│ ░░│     ░│       •░  │
                         •░       ░░    │░│       ──┘──── ░    ░ ░│   ░     └──────  ── ──  ──
                          ───   ────   ┌┘─ •     •        ───────┐░   ░• ░░░│      ─┐░░  ░┌─
                             ──     ┌─ │     ───     │ │         └───     ──        └─────┘
                  ──┐─┐──┐───   ────┘  └─────   ─────┘─┘─────────    ─────
                    │ │░ │ ░░• ░░░  ░░░░ ░░ ░│░░░░░░   ░░ ░░░ ░░░░• •░░░░░│
                  ──┘ │    │    ┌── ─┐   •   └────┐┐─┐     ──── ─┐ │ ┌─   │ ┌──┐─────┐─┐──┐────────────┐─┐──┐
                      │ ───┘──  │    │░░• ──░│    └┘ │    ░░     │░│ │░ ░│  │░ │░░░░░│ │ ░│   ░   ░░   │░│ ░│
                      │░░░░ ░░─┐┘     ──                         └─┘    ─┘      ───       │       ─────┘─┘──┘
                      └──      │ ┌──┐   ─────────────────┐─────┐─   ─┐─┐  ───┐──   ──────┐ ┌─────
                          ░░░░ │ │░░│ ░      ░░░░░░ ░░   │░░░░░│ ░ ░ │░│ │░░░│░░ ░ ░ ░░░░│ │░░░ ░•
                  ┌─┐                ───────  │ • ───  ──┘ ─┐ │  ──  │ └─┘  ┌┘┐ ─┐ ──┐   └─ •   • ──┐─┐──┐
                  │░│ ─┐░░───────┐ ░ ░░░░░░░│ │░ │░░░░░░ ░░ │░│ │░░│ │░░░░░░│ │░░│ ░ │░░░░░░ ░░│   ░│ │░░│
                  └─┘  └──      ░│ ─────────┘─┘──┘──────────┘─┘─┘──┘─┘──────┘─┘──┘───┘─────────┘────┘─┘──┘
                      │
                    │ │               •  ┌─┐─      ───
                  • │ │         │        │ │ •        ────────────────
                      │░      ░ │   ░       ░     ░             ░
                      └─────────┘──────────────────────────────────────










```

*Figure from page 7 (2346x3317 px)*


---



4203-E P-196



SECTION 2 PROGRAM OPERATION



(4) "%", and "CR", "LF" codes are punched out.



(5) The part program data is punched out following the program name (number).



(6) The same number of tape feed holes as in (1) are punched out in the tape trailing section.



[Supplement] 1. When the program data is punched out ln the EIA coding system, the "CR" code is



punched instead of the "CR" and "LF" codes.



When the program data is punched out in the EIA code, the presence of a code not



available in the EIA coding system causes an error. Tape punching-out halts and



an error message is given on the display screen.



When the tape delimiting code is the "%" (ER) code, i.e., when bit 3 of parameter



No. 1 of NC optional parameter (bit) is 1, the "%" code is punched out before feed



holes.


## 2. The part program is split and punched out, if it is too long to be contained in one

paper tape roll. Paper tape length may be changed from 1 to 300 meters (3 to 984



feed) using the NC optional parameter (word) No. 2.



As the format, the file name is also punched out, for the second tape and so on.



Since the tape ends with "CR" or "LF", actual tape length is somewhat differentfrom



the tape length set using the parameter.



When designating paper tape punch out operation on more than one paper taper



roll, specify option Din the following format:



P <file-name>, <device-name>:;D

• • • • , , $A.MIN • • • • • • %



~**** \, \. ... __



®_®_•



•..,..•-••.,..•_.I



1st tape


#### Food holes


# f.=


#### Tape length foe parameter seW~

.. {; "·®@n,,,



12nd'1ape



~-----------~\ '1_ ______ ,_


#### Machining program

Refer to 4-3-1, "Precautions for Tape Reading-in, Punching-out, and Verifying Operations" for



details and cautions on this operation.


```text


                                                                                                ──        ─┐
                                                                         ┌──┐──────┐─┐──────────░░────────░│
                                                                         │░░│ ░░░░ │ │░░░░░░░░░ ── ░░░░░░░─┘
          ┌───────  ──   •         •   •                   ──────────────┘──┘──────┘ └─────────    • ──
          │       ──  ┌──  ──────── ──  ────┐─┐────────────                                                │
          └──────┐ ░┌─┘░ ─┐     ░░    ──    │ │             ───────────────────────────────────────────────┘
                 │  │ │   │    ───      │ ──┘ └─  ──── ──
                 │ │  │ ──┘─ ──   ──   ┌┘─            │   ────────────────┐──────────────┐
                 │ │  │     •    ░     │ ░      ───   └───  ░  ░    ░ ░░ ░│  ░  ░      ░ │
                 │ │  │   │  ─┐    ──┐ │  ──┐─┐─   ┌─                     └─             └─┐──┐──────┐
                 │      ░ │  ░│   ░░░│ ░ ░░░│ │░•  │░•░ ░ ░     ░░ ░ ░░░░• ░░    ░░ ░░░ ░░░│ ░│░░░░░░│
                ┌┘  ──┐  ─┘─┐─┘─┐───┐    │    │                            ───┐            └──  ───  └┐──┐──┐
                │░░░░░│  ░░░│   │   │░░░─┘──  ░•░░░░──░░░ ░•░░ •░░──░  ───┐ ░░│ ░░░░░░░░░░░│  ░│ ░ ░│ │░░│ ░│
                └─────┘─────┘   └─  └───░ ░░───░────░ ─────░─── ──░ ───  ░│ ──┘    ──  ────┘  ─┘   ─┘  ──┘  │
                                    │      │                                   ────  ─┐     ──  ───  ──   •
                                    │░─────┘ ░ ┌─────░░░─────────░░ •░ ░ ░░ ░░░ ░░░  ░│ ░░░░░░░░ ░   ░░░ ░ │
                                    └─   ░ └───┘░ ░ ░───         ──     ──   ── ┌─┐      ───           │   │
                                    │                              ────┐  ───   │ └──   •   ──── • ────┘   │
                                    └─┐   ░ ░░░░░░░• ░ ░ ░─────── •░░░░│ • ░░░•      •
                                    │ │  •                           ──┘─  ──   ─┐      ──       ──   ──
                                    │  ░       ░───░ •   ─────┐  ──┐     ░     ░░└────── ░─────┐─░ ───░ ░░─┐
                                    │░    ░ ░┌──░░░ ░░ ░░░░ ░░│  ░░│  •  ────┐───░░ ░ ░ ░░░░░░ │░ ░░░░────░│
                                    └─░░─────┘  ──────────────┘────  •       │   ────── ───── ─┘──────
                                ──  │                               •
                               │    │░──── •   •   •  ─┐ • •  ───  ░ •   •      ──┐   ── ─────    ─────
                               └──  │                  │                    •  •  └─  ░        ──      ───┐┐
                                    └─░    ░    │ ┌─░   ░░ ░ ░ ░  ─┐░│ │░  ░░░░░░ ░ ░ • ░ │   ░░░░░ ░ ░  ░└┘
                                    │░─── ──── ─┘ │░─────────────░░└─┼─┘───────────       │      ──     ──┘
                                    │                                │             ──   ──     •    •
                                    └────────────────────────────────┘──░░─────────░ ───░░─────░────░──┐────
                                    │░░░░░░░ ░░░ ░░░░ ░░░ ░░░  ░ ░░  ░░░ •░░░░ ░░░░░ ░ ░• ░░░░░•░░░░ ░░│  ░
                                    └────────── ───── ───  ── │  ──   ─── ──── ─────  •  ────── ─── • • •
                                    │                         │ •                                          │
                                    │░░░  ░░░░░ ░░ ┌─   ░  │ •   ░•     │    ░           ░                 │
                                    └───   ───┐──  │  ───┐─┘░      •    │░┌────────────────────────────────┘
                                    │         │          │  •   ░│ ░─── └─┘
                                   ┌┘─ ░ ──┐ ─┘ ──┐     ─┘┐  ────┼──   •
                                   │  ───  └─     └──     │      │               ─────
                                   │         ┌───┐       • ──    │          ───┐─     ─┐
                                   │ │       │░ ░│        ░░░│             │░ ░│     •░└───┐
                                   │ │        •  │       ────┘             └──░        │   │
                                   │  ─────┐─  ░░└─ │░│ •      ────────────┘  ───┐▒│   └───┘
                                    •░░░░░░│░░ •░░ ░└─┘░░ ░░░░░░░░░░░░░░░░░░░░░░░└─┘ ──
                                     ──────┘      •     ────────────────────   │
                                   ┌─       ────                            ───┘     ───────
                                   │░│     │░ ░░                           │░░░│ ── │  ░░ ░
                                   └─┘     └─────                          └───┘┐  ─┘ ┌─────
                                      ─────      •    • •    ─────────────      │     │
                                                       •     ░░░░░░░░░░░░      ░
                       ──      ──    ─────── ───    ┌─   ┌─── ─┐──┐─┐──   ─┐─┐─  ┌───┐───┐────┐────────┐─┐─┐
                      │░░────── ░────░░░░░░░• ░ ────┘░░  │░░░░░│ ░│ │░░░░░░│ │░│ │   │░░░│    │░░░░░░░░│ │░│
                      │░░░░   ░  ░ ░  ────── •     ░ ────┘─────┘──┘─┘──────┘─┘─┘─┘───┘───┘────┘────────┘─┘─┘
                        ─────────────         ───────





























```

*Figure from page 8 (2346x3317 px)*


---



4-3. Verifying Punched Out Programs



4203-E P-197



SECTION 2 PROGRAM OPERATION



This is the function for verifying the program transmitted to a target device or medium against the program



stored in the source device between the paper tape and the floppy, the paper tape and the memory, the



floppy and the memory, the floppy and the floppy, the memory and the memory.



The following explanation is given for the verify operation made between the program punched on tape



and the program stored in memory.



The procedure is as follows:



(1) Set the tape to be verified in the tape reader in the same manner as for storing a program from



a tape to memory.



(2) Press function key [F3] (PIP).



The function names on the screen will change to those given in item (3) below.



=PIP



DATE DIR



"PIP >" is dis layed.



MULTI



PIP EDIT PIP . LIST CONDENS [EXTEND]



Press [F3) (PIP).



(3) Press function key [F3) (VERIFY).



=PIP



READ [EXTEND]



@@J@@J@



Press [F3) (VERIFY).



The screen changes to the directory-selection-based file operation screen and the following ls



displayed on the screen.



PIP:VER!FY V


```text


                                                                                                ───
                                                                          ┌─┐───┐─┐─┐─┐──┐─┐────░░░──────────
                                                                          │░│░░ │░│ │ │░░│░│░░░░ ──░░░░░░░░░░
                ───                    •             ─────────────────────┘─┘───┘─┘─  └──┘─┘────     ───
           ┌───┐   ┌─────┐────────────┐ ┌───────  ───                                                       │
           │  ░└─ ─┘    ░│    ░       │ │    ░  ──     ┌────────────────────────────────────────────────────┘
           └───┘ •  ─────┘ ░░       ──┘ │       ░░ ░   │
                                         │                •  ─── •    • • ───  •    ──      ──   • •  ────
                     ──      ────   ────░└─────── ──────── ┌─   • ────░•░• ░░┌─ ──── ░───  •░░─── ░░•░ ░░ ░░
                 │░░░░░   ░░ ░░░░░  ░░░░░ ░░░░░░  ░░ ░░░░░ │░░  ░░ ░░░ ░░░░│ │░ ░░░░│ ░░░• ░──░░░ •░░───────
                 └────── ─────────────────────┐─┐──────────┘───────────────┘─┘──────┘────     ──
                 │                            │ │                                        ──      ───┐ ┌─ •  │
                 │░░ •░░ ░░░──░░░░░░░░░── ── ░│ ░│ ░│ │░░░░ ░░░ ░░░│ │░░│ │░░░░░░ ░ ░ ░ ░░░░│ ░  ░░░│ │░ ░ ░│
                 └───░───── ░  ────────  •░  •  ─┘──┘─┘────────────┘─┘──┘─┘─────────────────┘───────┘─┘─────┘
                 │           │            ───
                 │ ░   ░ ░░──┘────░░░░░░░
                 └──┐──           • ───── ──────────   ───── ─────    •      •                        ──
                    │  ─── ── ┌──  •      ░          ─┐     │     ┌─┐─ •   ─┐ ─┐──────┐──────────────   ───
                  ──┘ │   •   │  •     ────────────── └─────┘─────┘ │ • ─── └─ │      │    ░     ░    ──
                      │░─┐░┌──┘┐ ░•░ ░               •             • •     •  • ──── • • ─────────────  ──
                  ┌─┐ │  │ │   │      ┌─────┐───┐
                  │░│ │░░░░░ ░ ░░░• •░│ ░ ░ │ ░░│
                  └─┘  │ ──     ┌─ •   │ ┌──┼── └───┐────┐────┐───┐───┐─┐──┐───┐───────┐───┐
                       │░░ ░░░░░│ │░░ ░│ │░ │░ │░░░░│ ░░ │░░ ░│ ░ │░░░│ │░░│ ░ │░░░ ░░ │░ ░│
                       └┐─┐─────┘─┘────┘─┘──┘──┘────┘────┘────┘───┘───┘─┘──┘───┘───────┘───┘
                        │ │                                                                 ┌─┐
                        │ │                                                                 │ │
                        │ │  ┌────                                                          │ │
                        │ │ ┌┘    ─── ────┐─────────────── •      ── ────────────           │ │
                        │ │ │ ──     •    │               │ ─────┐  │                       │ │
                        │ │     •  │   •  │ │      • ┌──  │  ▒░  └┐ │  •    ──────┐   ────┐ │ │
                        │  •  ░░░──┘  •░──┘ │ ───── ─┘░░──┘  ── • │ └──░│ │░░░░░░░│ ┌─░░░░│   │
                         ──░ ───┐                                •      │ └───────┘ │    ─┘  ─┘
                           │    │      ┌─      •    │ ┌─┐ • │ ──      ──             ┌─┐░  ──
                         • │  │░ ░ ░ ░ │░│ ░░ ░ ░ ░ │ │░└─░ │ ░░│  ░ ░░░ ░ ░ │ │ ░ │ │░│  │
                              └───    ─┘─┘ ── ─┐░ │ │ └─  ──┘ ┌┐┘ ────────── └─┘───┘ └─┘ ┌┘
                        ┌──┐─     ┌──     •  • └──┘┐  │ ░     └┘ •          •       •   ─┘
                        │  │░   ░ │░░░░░│          └──┘───────┘
                          ─┘──────┘─────┘
                  ──┐─┐───               ───────────
                    │ │         ░   ░   ░ ░  ░ ░ ░  •
                  ──┘─┘─┐─┐─────────────────────────
                        │ │                                                                 ┌─┐
                        │ │                                                                 │ │
                        │ │  ┌───┐                                                          │ │
                        │ │  │░ ░│                                                          │ │
                        │ │ │ ───┘─────  ─┐─             ─┐─      •     ─┐ ── ──┐──┐─────   │ │
                        │ │ │             │ •          ── │░─┐───┐ • ┌──░└┐  │  │  │        │ │
                        │ │ │ ─── ─── ───┐   ┌───     •  ─┘  │ ░░│   │░░  │ ┌┘  └── ┌───┐─┐ │ │
                        │   └┐░░░│   │ ░░│   │   •   •  •  • ░░─┐░• ░└────  │░ •    │  ░│░│   │
                          •  │   └─  │   └─ ─┘    │ │    •      │               •  •    └┐┘ ──
                           ─┐┘  ░  ──┘─░░  │  │░░ │ │ ──      ░░     ──┐ ░   ░    │  ┌─┐░│
                            │░     ░ ░ ┌┐─ │░ │ ░ │ ░ ░ │ ░   ───  ░   │ ░ ░ ┌─ •░│  │▒│ │
                            └──    ────┘┘   ──┘┐░   ──  └── ──   ┌─────┘─────┘   ─┘─ └─┘─┘
                                               └── ░░░░•░░░░░░░░░│                  •
                       ┌─┐─┐───── ──── •  ────┐         •    ──── ─────────────────   ─────────────────── ──
                      ┌┘ │ │ ░░░ •░ ░ •░•    ░│ │░        ░░ ░   ░     ░       ░                       ░ •  │
                      │    │   •      ░    ┌──┘─┘──────────────────────────────────────────────────────── ──┘
                      │    └──  │      •  ┌┘
                      │ ░  ░ ░ ░│   │░• ──┘
                       ── ──────┘───┘─





















```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-198



SECTION 2 PROGRAM OPERATION



PROGRAM OPERATION



197/07/15 14:10:00



PIP :VERIFY



v[l]



INDEX DI SPLAY PROCEDlflE



[F2] - MD1 :*.MIN



[F3] - FOO:*.MIN



TO OIS?LAY OTHER INDEXES. AFTER PRESSING



OVERNRITE



[Fl] ,



ltf)IJT THE DEVICE NAME AND FILE NAME. THEN PRESS [WRITE] KEY.


#### DEFAULT DEVICE NAt.£ = fill:


#### DEFAULT FILE NAME= *.MIN

>XV



MDT: FOO: COWAND OVERNR/ CHAR.



INDEX INDEX I NDEX HI STORY INSERT DELETE CANCEL



(4) Enter the file name of the file to be verify and press the WRITE key.


#### Example: BOX-1350.MIN.

This step ls unnecessary for a program without a file name, Le., A.MIN.



PROGRAM OPERATION



PIP :VERIFY



V BOX-1350.MINII]



INDEX DISPLAY PROCEDURE



[F2] - MOl:*.MIN



[F3J ..... FDO:*.MIN



I 97/07/15 14:10:00



OVERWRITE



TO DISPLAY OTHER INDEXES, AFTER PRESSING [FlJ,



INPUT THE DEVICE NAME ANO FILE NAt.£, THEN PRESS [WRITE] KEY.



DEFAULT DEV I CE NAME = l.t)l :



DEFAULT FILE NAME= *.MIN



11'0EX



f,1)1: FOO:



CCfJMAND OVERWR/ CHAR.



I N[E( I NDEX HI STORY INSERT DELETE CANCEL



'-WR_1_TE_,


```text


                                                                                                ───
                                                                         ┌───────┐───┐─────────░░░░───────░│
                                                                         │░░░░░░░│ ░ │░░░░░░░░░ ── ░░░░░░░─┘
          ┌──────────────────────────────────────────────────────────────┘───────┘── └─────────      ──
          │
          └─────────────────
                            ┌─  ──────┐─┐───────              ─────────         •   •
                           ┌┘ •   ░░░░│ │░░░░░▒ ──────────────         ────       ── │   │
                           │ • • ┌────   ───────                      │░░░░░░░░░ ░░░░│   │
                           │  •  │░░ ░░░        ───────   ────────────┘──────░░▒░───┐┘   │
                           │ │   └─── ───              ───                   ────   │ │  │
                           │ │  │                                                   │ │  │
                           │ │  │                    ───────────────────────────────┘░│  │
                           │ │ │ ┌──┐──┐─┐─────┐───┐                                │ │  │
                           │ │ │ │░░│ ░│░│░░ ░▒│ ░░│                   ─────────────   │ │
                           │ │   │░░ • │░│  •░•         •     •                        │ │
                           │ │   │░ │ ┌┘░ •░░░  ────┐───░────░░┌──────┐ ─┐───┐─┐─┐     │ │
                           │ │   │░░│ │░  ░ ── ░░░ ░│   • ░░▒──┘░░ ░░░│  │░ ░│ │░│     │ │
                           │ │   │░░░░ •░░ ░ ░░▒┌──▒│     ───   ──────┘ ─┘───┘─┘─┘     │ │
                           │ │   └───── ─────░──┘  ─┘░                                 │ │
                           │ │               •       ──                                │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │  ┌─┐                                                    │ │
                           │░│  │ │       ───     •                   ─┐─────── ────── │ │
                           │░│  └─┘   ───┐    ──┐  ──────────── ────┐  │       │       │░│
                           │ │     │   ░░└─┐  ░ └┐─  ░▒░░░ ░░░░│  ░░└─┐  ┌──┐┐ │       │ │
                                ──░└─ ── ░░│  • ░│  ░───── ────┘ ─┐─ ░│  │░░└┘ │      •  │
                            ──            ─┘ •      •             │      │  │  └────── ┌─
                              •  ░░     ░░   ░ ░░ ░ ░ ░░ ░ │ ░░     ░░    ░░░    ░░░  ─┘
                               ───── ───────────────────── └───── ─────░────────── ───
                                    •                     •      •     •          •



                 ┌─┐ ┌─────────┐─ ┌───────┐───┐────┐─┐────┐──┐───────┐─┐─────────┐
                 │░│ │░  ░   ░ │░ │░░░    │░ ░│ ░ ░│ │░ ░ │  │░ ░░░ ░│ │░   ░ ░░░│
                 └─┘ │       ┌─┘   ───  │ │  ─┘────┘─┘────┘──┘───────┘─┘─────────┘
                     │     ░ │  ───   ──┘ └──
                     │       └──    ──   •   ─────────────────────────────────┐────┐
                      │   │ ░░ ░────░░░░░░ ░ ░   ░  ░░░  ░░░░░░ ░ ░░ ░░░░     │  ░░│
                      │ ──┘              ──────  ─────────────────── ────      ────┘
                     │     ┌────░ ──░░ ░                            •        •
                     │ •   │   ░•       •                        ░ ░ ────────░     │
                     │  │  ░░  ░░░░░  •                         ──── ░░░▒▒░░     │ │
                     │  │  • ░┌──░│ ░░▒┌┐──  ─────────       ───    ──────────┐  │ │
                     │  │ • ──┘  ─┘────┘┘  ──         ───────                 │ │  │
                     │ │                                                      │ │  │
                     │ │     ────   ── ───────                                │ │  │
                     │ │   ┌─░░  ┌─┐░ │░░░░░░                  ───────────────   │ │
                     │ │   │░░│  │▒│ ┌┘ ░                                        │ │
                     │ │   │░░│ │ •░─┘▒•░ ────┐─────┐──┐─┐─┐────┐ ┌────  •       │ │
                     │ │   └─░░ │░ ░░░░░ •▒░░░│ ░ ░ │░▒│ │▒│ ░░░│ │░      │      │ │
                     │ │   │▒│░  ░░░░░│▒░▒┌─┐▒│  ┌──┘──┘─┘─┘────┘ └───── ─┘      │ │
                     │ │   └─┘────────┘▒──┘ └─┘ ░│                               │ │
                     │ │              └─       ──                                │ │
                     └─┘                                                         │ │        ─────
                     │ │                                                         │ │      ┌─     ─┐
                     └─┘  ┌─┐                                                    │ │      │     │ │
                     │ │  │░│                                                    │ │      │ ──  │░│
                     │ │  │    ────  ┌────    ───────────┐──┐─          ─┐────── │ │      │      ░│
                     │ │   ──┐   ▒░──┘  ░░─┐ •░░▒▒▒░ ░░░▒│░░│░───┐────┐─ │       │ │    ──┘──     │
                     │  ─┐─░░│   ─┐░░  ──┐░│  ░────────░•░ ─┘░  ░│  ░░│  │     ──  │  • ░░░ ░│    │
                     └─  │ ─┐┘    │ ──   │ │                    ─┘ • ┌┘  └─   •   •     ─────┘────
                       ─┐   │ │ ┌─┘┐   ┌─┘┐     •   │ ┌─     ┌─     ─┘ │ │ ┌─┐ ┌─
                        │ │░│ │ │ ░│ ░ │  │ ░│ │░│ ░│ │░│ │  │░│ │░ ░│ │ │ │▒│░│
                         ─┘─┘ └─┘──┘───┘──┘──┘─┘─┘──┘─┘─┘ └──┘─┘ └───┘─┘─┘─┘─┘─┘
                             •














```

*Figure from page 10 (2346x3317 px)*


---



4203-E P-199



SECTION 2 PROGRAM OPERATION



This starts the tape reader, and program data on the tape is read and compared with the stored



program data.



While verifying operation, the screen displayed "VERIFY" along with the "file name".



PROGRAM OPERATION TRANSFER VERIFY BOX-1350.MIN



tape file name =BOX-1350.MlN



file end



data match



(5) Press function key [F7) (PIP QUIT).



tape file name =B0X-1350.MIN



f lie end



data match



97/07/15 14:10:00



FAST FAST PIP



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



@@J@J@@J@~@



Press [F?J (PIP QUIT).



This completes verification of the punched out program data and the display mode return to the one



in step (1).


```text


                                                                                                ───        •
                                                                          ┌─┐───┐─┐───┐────┐────░░░────────░│
                                                                          │░│░░ │░│ ░ │░░░░│░░░░───░░░░░░░░─┘
                                                           •   ────   ────┘─┘── └─┘   └────┘────     ─────
                        ────┐──┐──┐───────────────────┐───┐ ┌──    ───         •   ─┐─          ┌──         │
           ───────────┐     │░ │ ░│    ░              │   │ │            │      │ │ │           │    │ │    │
                      │      ┌─ • └───────────────────┘───┘─┘────────────┘──────┘─┘─┘─────  ────┘────┘ │    │
                      └┐  ░ ░│ •░░│                                                                   • ────┘
                       │   ┌─    • ────────── ──────────────────   ───    ─────────────────┐───┐
                       └── │ │                       ░      ░░░    ░ ░─── ░░  ░ ░░  ░░   ░ │░ ░│
                          • ─┘───────────────  ─────────────────   ───    ───────────── ───┘───┘

                             •   ───────────────────────────────────────  ────────────   •
                            │     ░▒▒▒▒▒░▒▒▒▒░░▒        ░▒▒▒▒▒░░▒░░░        ▒▒░░░▒░▒░▒│   │
                            │ │  ──────────────────────────────────────┐░░░───────────┘   │
                            │ │                                        └───             │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │   ┌─    ──┐──┐────┐─────┐                               │ │
                            │ │  ┌┘░────  │░ │░░  │░ ░ ░│                               └─┘
                            │ │  │     ░• └──┘────┘─────┘                               │ │
                            │ │  │░  │░ ░                ──            ─┐─    ──┐────── │ │
                            │ │  └───┘──                                │       │       │ │
                            │ │  │       ──┐   ┌──┐┐  ┌─┐   ░───┐─  ───┐   ──    ┌────┐ │ │
                            │   ─┘░┌─   •░░└───┘░░└┘─ │░└─  ░░░░│  ░░░░│   ░░    │░░░░│   │
                             ──    │ ──          •        •     │      │         │   ─┘  •
                               •  ░░ ░ ░ ░░   ░░░░    ░░░ ░  ░░░    ░░░    ░ ░    ░░
                                ───────────── ────────────░──────────── ──────── ──────
                                                          •                     •
                  ┌─┐─┐────┐─┐────  ┌────  ─┐─┐ ┌─┐──
                  │░│ │ ░░░│ │░░░░│ │░░ ░ ░ │░│ │░│ ░•
                  └─┘─┘─┐─┐┘─┘   ─┘─┘──   •    ─┘
                        │ │   ┌─       ┌─┐ ┌──┐  ─┐─┐──┐                                    ┌─┐
                        │ │  ┌┘░┌─┐──┐ │░│ │░░│ │░│ │░░│                                    │ │
                        │ │  │  │ │ ░│ └─┘─┘──┘─┘─┘─┘──┘                                    │ │
                        │ │  │░░│ └─ ░                  ──      ───       •     ─── ─────── │ │
                        │ │  └──┼─┘ ──      │               ──     ───┐  │ • ──┐   •        │ │
                        │ │  │  │ │   ───┐  └┐───┐    ┌─┐  │ ░───┐  ░░│ ─┘   ░░│ •  ┌─────┐ │ │
                        │ └─ │░░└─┘  •░░░│   │░░ └── ┌┘░│  │░░░░░│  ──┘ ░│  ───┘    │ ░░░░│   │
                        │    └──┘      ──    │       │     │   • └┐      │      •        ─┘  •
                         ───    │              •    • ┌─┐ •       └─ ┌─┐─┼───┐─  ─┐──┐─┐  └──
                            │  ░ │ ░ ░ ░░   ░ │ ░ ░ ░ │░│ ░   │░│  ░ │░│ │ ░ │ • ░│  │░│ │
                            └─ ──┘ ─── ─── ── └── ─── └─┘─── ─┘─┘ ── └─┘ └───┘   ─┘──┘─┘─┘
                              •   •   •   •  •   •   •      •    •  •   •    │  │
                                                                          ───┘  └─────────
                                                                            ░  •
                       ────────────────────┐──┐───────────┐────────────────              ───────────────────
                      │░ ░ ░░ ░░░░░  ░ ░░░░│  │░░ ░   ░░░░│ ░    ░░    ░░░ ░░   ░ ░░ ░      ░  ░      ░
                      │ •   ┌──────────────┘──┘───────────┘─────────────────────────────────────────────────
                         ───┘























```

*Figure from page 11 (2346x3317 px)*


---



4203-E P-200



SECTION 2 PROGRAM OPERATION



[Supplement] When a data mismatch is found during tape verification, the block (line) which contains



inconsistent data is displayed on the screen and the inconsistent character flickers.



PROG (J'ERATION



Blinks



>V 8.MIN



tape fi I e=BOX-1350.MIN



N005 GO



verify continuing? (Y/N) !



TRANSFER VERIFY BOX-1350.MIN



97/07/15 14:10:00



FAST FAST PIP



READ PUNCH VERIFY COPY FORWARD REWIID QUIT [EXTEND]



The following message is displayed, asking the operator if he wants to continue



verification.



To continue verification, type "Y'' and press the WRITE key.



To abort verification, type "N" and press the WRITE key.



When no data mismatch is found in verification operation, the following message will be



displayed on the screen.



tape end



file end



data match



If data is left in the file after data on a tape has been read, the following messages will be



displayed on the screen.



tape end



data match



If data is left in the tape after data on the file has been read, the foHowing messages will



be displayed on the screen.



file end



data match


```text


                                                                                               ───
                                                                        ┌──┐─┐────┐─┐──────────░░░──────┐─┐
                                                                        │░░│ │░░░ │ │░░░░░░░░░░───░░░░░ │░│
          ┌─────            ───      ──                 •     ────  ──── ──┘ └─── │  ─────────      ──
          │     ───────────┐    ─────  ───┐──────────┐── ─────    ──    •   •    ─┘──          ──         •
          └────┐░░   ░     └────░         │          │                                        │            •
               └───────────┘    │    ───    ──┐    ──┘──────┐ ┌─ ──░───        ───────     ───┘──  ── •   │
                                │░░  ░░░┌──┐░░└───░░░░░░░  ░└─┘░•░░•░░ ──────── ░░░░░░─────░░░░░░──░ ░░░──┘
                                 ───────┘  │               •   •                                   ─────
                                             ───────────            ───────────   ───────┐───────┐
                                       │  •  ░░░░░░░░░ ░│ ──────── ░░░░░░  ░░░░ ─┐     ░▒│░░░░░░▒│   │
                                       │ │   ───────────┘           ───────────  └─░  ───┘───────┘   │
                                       │ │                                         ───             │ │
                                       │ │                                                         │ │
                                       │ │                                                         │ │
                                       │ │                                                         │ │
                                       │ │                                                         │ │
                                       │ │                                                         │ │
                                       │ │                                                         │ │
                                       │ │                                                         │ │
                                       │ │                                                         │ │
                                       │ │                                                         │ │
                                       │ │               ┌────┐                                    │ │
                                       │ │            ───┘░░░░│                                    │ │
                                       │ │      ──         •                                       │ │
                                       │ │  ┌─── ░──────┐─   ────┐─                                │ │
                                       │ │  │░░░ ░ ▒░░  │░│ │░  ░│                                 │ │
                                       │ │  └───░░ ░•     │ │  ░┌┘   •              ──   ─┐─       │ │
                                       │ │      ┌┐░     ─┐    ─┐┘  │  ┌───┐ ────── •  ┌─┐ │ •      │ │
                                       │    │   └┘       │ ─┐  │  ─┘  │ ░░└─   ░░ •   │ │ │  ────┐─┘ │
                                        │   │░       ░  • • │  │ │  •  ┌──░░  ┌── ░•  │ │ │ •░  ░│   │
                                        └─ ─┘    ──             ─┘──   │      │     ──  └─┘      └┐──
                                          •  ░░   ░ ░░ ░ ░ ▒░ ░ ░ ░░ ░ ░ ░░ ░ ░░░░    ░░░    ░░░  │
                                           ───────────────────────────────────────────────────── •
                                ┌─   •
                               ┌┘ • │ ────── ┌───────   ┌───────┐ ────── ─── ───────   ────────  ─────────┐
                               └┘  ─┘        │    ░     │    ░  │      ░         ░    •     ░         ░   │
                               │░░ ░░░│ ─┐         │                               ┌─  ───────────────────┘
                               │ │ ───┘  │ ────────┘ ─── ──  ───────┐──────────────┘
                               │ │    │   •     ░  │ ░░░│   •░   ░░░│ ░░  ░ ░   ░░░│
                               │░    ─┘─        │     ──┘ ┌─ ──  ───┘ •   ───   ───┘
                               │ ──     ┌─      │       │ │     •    •       ──     ───────  ───       ──
                               │░░      │                                      │                ────┐    ─┐
                               │        └─         • ┌─────────────────────────┘─────────── ────   ░└──── │
                               └─    ░    ┌─ ░ ░  ░ ─┘                                     •    ────     •
                                 ────┐  │ │ ────────
                                     │  └─┘
                                     │░• ░ ────┐
                                     └─░┌──░░░░│
                                        │  │   └─ ─────────────┐─┐──┐─────────────┐────────┐────────┐─┐───┐
                               ┌───────░   └─┐   •░░   ░░░     │░│  │░ ░░░░ ░░░  ░│ ░░ ░░ ░│ ░░░░░░░│ │░ ░│
                               │░░░░░░░┌── ░░│ ░░░░────────────┘─┘──┘─────────────┘────────┘────────┘─┘───┘
                               └─────  │     │ ────
                                     ┌─┘─────┘
                                     │░░░ ░░░░──
                               ┌────       ──   ────┐─ ───────────────┐─────┐─┐──┐─┐───────────┐──────┐─┐─┐
                               │  ░ ───────     ░░░ │ │  ░░░     ░ ░  │░ ░░░│ │░░│ │░ ░░ ░░░░░ │░░░░░░│ │░│
                               │░ •░░░░░░░ ░░─┐┐─── ░░└───────────────┘─────┘─┘──┘─┘───────────┘──────┘─┘─┘
                                ── ──         └┘   ───
                                      ──┐ ░───
                                     •░░│ ░░░░│
                                      ──┘─────┘




















```

*Figure from page 12 (2346x3317 px)*


---



4203-E P-201



SECTION 2 PROGRAM OPERATION



Example 1: Verifying A.MIN in TR: (paper tape} against A.MIN in FD0: (floppy disk)



I...J



TR:A.MIN,FD0:A.MIN



Example 2: Verifying A.MIN in TR: (paper tape) against A.MIN in MD1: (memory)



VLJ TR:A.MIN,MD1:A.MIN



Example 3: Verifying A.MIN in FD0: {floppy disk} against A.MIN in MD1: (memory}



1....1


#### FD0:A.MIN,MD1 :A.MIN

Example 4: Verifying A.MIN in FOO: (floppy disk) against B.MIN in FOO: (floppy disk)



Vu FD0:A.MIN,FD0:B.MIN



Example 5: Verifying A.MIN in MD1: (memory) against B.MIN in MD1: (memory)



Vu MD1 :A.MIN,MD 1: B.MIN



Note that the underlined device name MD1:, which is the default device name, can be omitted.



4-3-1. Precautions for Tape Reading-in, Punching-out, and Verifying Operations



(1) There are two tape coding systems, EIA and ISO. The selection of a coding system can be



conducted by:



(a) Parameter setting



Bit 1 and bit 0 of NC optional parameter (bit) No. 1 are used to determine the tape coding system:



bit 1 for tape code parity discrimination and bit O for tape code. The tape coding system is



determined by the combination of these bits.



Refer to IV "PARAMETER", Section 4, "DESCRIPTION OF PARAMETER AND SETTING



PROCEDURE" for the procedure to set parameters.



(b) ISO or EIA designation for READ, VERIFY, and PUNCH operations



Follow the steps below when conducting READ, VERIFY, and PUNCH operations. This will allow



the operator to directly select the coding system regardless of the coding system set by the



parameter.



Example: To punch out stored program data in the EIA code



Key in the following command in step (3) of the punch-out procedure of a stored



program.



Indicates EIA.



BOX-1350.MIN;E



Key in ";E" following the file to be punched out.



Designation of EIA ISO, and Verifying



;E ..... EIAcode



;I ...... ISO code



;V . . . . . Verifying


```text


                                                                                                ───
                                                                          ┌───────┐───┐─────────░░░──────────
                                                                          │░░░░░░░│ ░ │░░░░░░░░░ ──░░░░░░░░░
           ┌───────         ──               •    •                        ──    ─┘   └─── ─────    ────
           │       ┌────────  ───────┐─────── ──── ┌─────┐─────────────┐───  ───┐  ───    •                 │
           └───────┘░     ░  •    ░  │ ░ ░ ░    ░  │     │             │░░    ░ │ │    │     ───────────────┘
                   └───────── │ ───  └─ ┌── ───  ──┘──┐──┘─────  ──────┘────────┘─┘──  └─── •
                              │    •░ ░ │░░ ░░░   ░░░░│                                    •
                   ┌──────┐───┼────  │                └┐─┐───────┐─────┐─────┐─┐─┐─┐───────
                   │░░░░░░│ ░ │░░ ░░░│ ─┐░░░ ░  ░░ ░░░░│ │░░░ ░░░│░░ ░ │░░░  │░│ │ │░░   ░ │
                   └──────┘───┼─┐──┐─┘  │    ─┐       ┌┘─┘───────┘─────┘─────┘─┘─┘─┘───────┘
                              │ │  │░ ░ │░░ │░└─ ░ ░░░│
                   ┌──────┐─── ─┘┐─  │  │   └─  │ ┌─┐ └────┐─┐─┐────────┐─┐───┐─┐─┐─┐───────┐
                   │ ░░░░░│ ░ │░░│░░░│ • ░•░   ░│░│ │░░░░░ │░│ │░░░░░ ░ │░│░  │░│ │ │░░░ ░░░│
                   └──────┘───┼──┘── │  ─┐ │ ┌─ │  ─┘  ┌───┘─┘─┘────────┘─┘───┘─┘─┘─┘───────┘
                              │     ░░ ░ │░│ │░░░•░ │░░│
                   ────────── │   • │    │ └─┘─── ┌─┘  └───────┐───────────────────┐────┐─┐──┐
                      ░   ░   │   ░─┘─   └─┘     ─┘ └─░░   ░ ░ │░░ ░░   ░░  ░    ░ │░░░░│ │░░│
                   ┌──────────┘   •      │ │          ─────────┘──────  ─────  ────┘────┘─┘──┘
                   │          └───   │  ─┘ │ ──┐─                     ──     ──
                   │        ░ │   ░• │ ░ ░ ░   │░─┐        •  ──        ░         ┌───────┐
                   └───────── │ ──┐ ─┘  │  ┌───   └──── ┌── •   ───────────────── │       │
                              │   │░░│  └─┐┘░░░•    ░░░ │
                   ┌───┐─┐────  ──┘    •  │  │         ─┼──┐───┐───┐──┐────┐─┐───┐─┐───┐─┐────┐─┐─────┐
                   │░░░│ │░ ░ ░ ░ ░░░░░░░─┘┐░└───░•░ │░░│  │░ ░│ ░ │░ │░░░░│ │░ ░│ │░░░│ │░░ ░│ │░░░  │
           ┌───┐   └───  └─      •         │     │   └──┘   ───┘       ───    •     ───┘─┘────┘─┘─────┘
           │░  │   │ ░░ •   ░     │    ░░░ ░•    │░      ┌──    •    ░     ░
           └───┘  │  ─┐     •     │    ─────          ─┐ │    •   ──┐ ┌─
                  │   │   ─┐    ──                     │ │     │ │  │ │ │            ───────────────────
                  └──  │   └───     ────────── • ───── └─┘  ───┘─┘  └─┘ │       ──       ░
                       │░── ░ ░───░             •     •   ──           ─┘───────  ─────────────────────
                    ┌─┐ │          ────┐
                    │░│ │░░░░░░░░ •░░░░└─
                    └─┘    •             • ── ──  ────  •  ─── •     • ──   ──  • ───  •   ───   ────     •
                        ┌── ──┐─┐─┐──┐──┐ │░░• ░──░░░░──░──░ ░•░────┐░• ░░• ░  ░░│  ░ ░ ░──░░░───░░░░─┐─░░ ─┐
                        │░ • ░│ │░│░ │ ░│ │░░░│ ░░░  ░░░░ ░  ░ ░ ░░ └─░───░░─────┘───────░░───░ ░ ───░│░───░│
                        └─░ ░─┘─┘─┼──┘──┘ └───┘──── ───── ──────  •       ──             ──   •  •     •    │
                        │         │                             ── ────┐─    ┌─   ───────   •  ──   ┌─    ──┘
                        │░░░──────┘─ ░░░░░░▒░░░░░──┐░░░░░──░──░░░░░ ░░░│ │░│ │░│ │░░░░░░░   ░ │░░░│ │░   ░░░│
                        └───  ░ ░ ░░────────────   └┐───┐      ──  ────┘─┘─┘─┘─┘─┘────────────┘───┘─┘───────┘
                                  ──                │   │
                    ┌── ┌─┐          •     │  │ ── ─┘  │  ──      •   ─────────────┐
                    │   │ └┐───────   ░ ░  └──┘─     ──┘    ─┐─░│  ───░    ░░ ░░  ░└┐            │
                     • │░ ░│  ░            │           │    ░│  │ │  ░•░     ───    └─    ───   ┌┘── ── ───
                       │         •         │    ──        ░•  ┌─┘─┘    ──────           ──   ───┘   •  │    │
                        │░ •░ ░░░░┌── •░░░░░  ░░░░  ░│ • •░ ░ │░░░░• │░░░░░░░░   ─┐░   ░░░┌─┐░░░░░  ░░ │░─┐┐┘
                        │░░░──────┘    ───── ─────  ─┘     ──   ───  └─────── ┌── └───────┘ └───────── └─ └┘
                       │           ─┐──     •     ──  ─────  ┌─┐   ─┐        ─┘
                       │░░░░░░░│  │ │░░ ░░ •░ │░ ░░░ ░ ░░░░│ │░│  │░│ •░│ ░░░░│
                        ───────┘  │          ┌┘     ─┐─ ┌─ │  ─┘ ┌┘ │  ┌┘     └┐────────┐────┐────┐────┐────┐
                                  │░─────░░ ░│░░░░░│ │░░│ ░░░│ ░ │░│ │░│   ░ │ │░░ ░ ░  │░ ░ │░░░ │░ ░ │░░░░│
                                  └─     ┌───┘─────┘─┘──┘────┘───┘─┘─┘─┘─────┘─┘────────┘────┘────┘────┘────┘
                                    ─────┘
                                                              ┌───────┐─┐─┐
                                                             ─┘░ ░░░░░│ │░│
                                                           ┌─  ───────┘─┘─┘
                                          ┌─────┐───┐────┐ │░ •
                                          │░░░  │░░ │░░░░│  ──
                                          └─────┘───┘─── │
                                                          •
                                                 • ───   ░  ───────  ─────────────────────┐
                                                  •     ┌─        ░                       │
                                  ┌─────┐──┐─┐───   ──┐ │ │        │ ──  ─────────────────
                                  │░░░░ │░░│ │░░░• •░░│ │░│ │░░░░░ │
                                  └───┐  ──┘─┘──         ─┘─┘──────┘
                                      │░│       ┌──────┐
                                      └─┘       │░    ░│
                                      │ │      •       │
                                      │ │       •░  ░ ░│
                                      └─         ──────┘












```

*Figure from page 13 (2346x3317 px)*


---



4203-E P-202



SECTION 2 PROGRAM OPERATION



(2) There are two different methods to operate the machine with stored programs.



(a) When one main program is stored in the memory



In this case, it is necessary to assign a file name to the program. In the memory, however, the



program is assigned the file name "A.MIN".



(b} When more than one program is stored in the memory



In this case, a program can be executed in two different ways.



1) One file for one program



Only one program is registered in one file.



2) One file for several programs



More than one program is registered in one file.



In both cases, it is advisable to create the program by assigning a file name on the tape. If the file



name is not assigned on the tape, follow the steps below and assign a file name when storing a



program in the memory.



Press function key [F1J (READ).



Key in the file name following a comma.



",file-name"



@ Press the WRITE key.



With the steps above, the file name is specified and the program on the tape is stored in the



memory.



To simplify program tape management, it is recommended to register one program in one file.



(3) To store program data following the program data already stored in the memory, follow the



steps below.



Press function key [F1J (READ)



Key in the file name and ";A".



",flle-name;A"



@ Press the WRITE key.



When the program is long and cannot be punched on one tape, the second and subsequent tapes



should be read following the above steps.


```text


                                                                                                ──
                                                                         ┌─┐─────┐───┐─────────░░░───────░░│
                                                                         │░│░░░░░│ ░ │░░░░░░░░░ ──░░░░░░░──┘
          ┌──────   ──     •              •                            • └─┘─────┘   └─────────    ────
          │       ──   ──── ───────┐────── ─────┐───┐─────────┐─┐────── │         ───                      │
          └──────┐  ──             │░░          │   │         │ │       │                  ────────────────┘
                 └─    │  │        └────    ────┘   │        ─┘ └──┐────┘───────────    • •
                     │ │  │       │     ┌──     │ ──          │ │  │                ──── •
                     │ │   │  ──┐ │░    │   ────    •          ─┘ ─┘ •
                       │ │░│    │                                   •  ────────┐  │   ───────── ┌─────── ───
                       └─┘ └─    ──────          ───  ░ ──  │        •   ░  ░  │  └──           │   ░
                       │░ ░░░░─── ░░░░░░┌─┐──── •░░░─── ░░──┘           ──  ───          ─────── ──────   ──
                   ┌─┐ └─   •    •    • │ │                 └─┐─┐──────
                   │░│ │░░░│ │░░│ ░░░│ ░ ░ ░ •░░░│ ░ ░░░░│ ░ ░│ │░░░░░░│
                   └─┘ └───┘ └──┘ ─┐ └┐─┐   │ ┌─ │      ─┘   • │ ┌───  └─────┐
                       │  ░  │░░│  │░░│░│░• │░│ │░ │░░░░░░│   ░│ │░░░░░│ ░░░░│
                       │ ─┐  └─ │   ─┐ ┌┘─ ┌┘ │ └──┘──────┘────┘─┘─────┘─────┘
                      │ │ │░ ░ •░ ░• │░│ ░░│░░░•
                      └─┘─┘───┐   • ─┘  ─┐─ ─┐─ ─┐───────────┐──┐─┐
                              │░░• •░░ ░ │░░░│ ░ │░░░░░░░ ░  │░ │░│
                      ┌─┐─┐──┐      ─┐   └─  └───┘──┐────────┘──┘─┘
                      │░│ │░░│ •░ ░• │░ ░ ░ •░░░░░ ░│
                      └─┘─┘──┘┐ • • • ┌─          ┌─┘─┐──────────┐─┐───┐
                              │░░• ░░░│ • ░░░ ░░░░│ ░ │░░░░░░  ░ │░│ ░░│
                          ──  │                                          ── ──       •       ── •       ──┐
                       ┌──░ ──┘─────────────░░• ░ ──░░░•░ ░ • ░░──░ ░──░░░░• ░ ───┐─░░░░ ░───░ │░─────── ░│
                       │░░░░ ░ ░  ░░░░░░░░ ░┌─░░•░░░───░░───░───░░──░░░────░───░░░│ ░•░───░░ ──┘─░░ ░░░░ ░└─
                       └── ──────────────── │ ── ───   ──   •   ──  ──         ───        ──       • ── •
                       │                        │    •
                       │░┌─┐   │        ░ │ ░   │░░ ░ •
                       │ │ │   └───────   │  ───       ──────┐
                       │░│ │░│ ░ ░ ░ ░░  ░░░ ░░░░░░ ░  ░ ░░░░│
                       └─  └─┘       ────────────────────────┘
                           │  •  ░ ░
                       │   │          ░  ┌─┐─┐
                       └──   ──────┐     │ │ │ ─┐──┐──┐───┐──────┐─┐──┐─┐────────┐─┐──┐────────────────────┐
                       │░░┌─┐░  ░░░│ │░░ │ │░│ ░│  │░ │ ░ │░░░░░░│ │  │░│    ░░  │ │  │░  ░ ░ ░  ░         │
                       └──┘ │   ───┘ └───   •  ─┘──┘──┘ ──┘──────┘─┘──┘─┘────────┘ └──┘────────────────────┘
                              ─┐    •    ──   •        •                          │
                       •░──── ░│         ░     ░        •               ░     ──  └┐    ─────
                 ┌─┐  │      ──┘         •           ───                           │                  ───
                 │░│  │  ────   •         ░                                      │
                 └─┘  └──        ───────────────────── ── ───────  ──  • ────── ─┘── •    ┌┐ ── │  • │
                      │░░░─────░•                     •  •       ──  ── •      •    • ────┘┘─  ─┘── ─┘
                      └┐─         ──┐──┐─┐────────────
                     │ │ │ •░░░ • ░░│  │░│ ░ ░ ░ ░ ░
                     │░│ └┐  ── ░───   │ │  │  ┌──┐───
                     └─┘  │          │  •  ─┘──┘  │
                     │ │  └──  ░░░░ ░│
                     └─┘ ┌┘        │ └──────┐
                     │░└─┘░ •░░ ░──┘░░  ░ ░░└─
                     │     • •                ──          ───────────────────────┐──────────┐──────────┐───┐
                      │ ──      ──░  ─────      ───   ───              ░   ░     │░ ░   ░ ░ │  ░░░ ░ ░ │░░░│
                      │░░░░  ░ │░░░ ░░░░░░░ ░│ ░░░░░ ░░░░────────────────────────┘──────────┘──────────┘───┘
                      └────────┘─────────────┘───────────



























```

*Figure from page 14 (2346x3317 px)*


---



4203-E P-203



SECTION 2 PROGRAM OPERATION



(4) When the file name is already registered in the memory and when it is necessary to store a



program with the same file name, follow the steps indicated below to erase the previous



program and to store a new program.



Press function key [F1] (READ), key in the file name and press the WRITE key.



The following message will be displayed on the display screen.



file exist overwrite? (Y/N)



PROO OPERATION



tape file name= TEST9.MIN



TESTS.MIN



file exist overwrite? (Y/N)



TRANSFER VERIFY TEST9.MIN



97/07/15 14:10:00



FAST FAST PIP



READ PUNCH VERIFY CIYY FORW.ARO REWIND QUIT [EXTEND}



@ Type



uy»



and press the WRITE key.



Data in the specified file is erased and new data is read from the tape reader and stored in the



memory.



{Supplement] If data does not need to be stored, type "N" and press the WRITE key.



When a file name is not given on the tape while the name of the file stored in the memory



is "AMIN" (that is, the file is not assigned a file name), it is not necessary to specify the



file name after pressing function key [F1J (READ).



(5) File names can be specified and changed as required by inputting the following.



[F1] {READ) "input file name", "output file name"



When an input file name has not been specified, the file name given on the tape is taken as the input



file name. If no file name is given on the tape, the program is assigned the file name "A.MIN."



When an inputfile name is specified, it is necessary to check that the specified flie name agrees with



the file name on the tape. If the specified file name agrees with the file name on the tape, an error is



generated. (An error message is displayed on the display screen.)



When an output file name has been specified, the specified file name is created in the memory.



When an outputfile name has not been specified, the inputfile name is used as the output file name.



In this case, the delimiter"," can be omitted.



To specify an output file name without entering an input file name, be sure to enter the delimiter",".


```text


                                                                                               ┌───       ─┐
                                                                         ┌────────┐───┐───┐────┘░░░───── │░│
                                                                         │░░░░░░░░│   │░░░│░░░░░──░░░░░░─┘─┘
           ┌──────   •            •                       •            •  ───  ───┘    ── └─────     ───
           │      ┌─┐  ───────┐──┐ ┌────────────┐─┐─────── ────┐─┐───── ──   ──    ──┐─  •      •           │
           └──────┘░└──░░    ░│ ░│ │            │ │   ░        │ │                •  │       │         ┌────┘
                  └─┘  │         │ │            └─            ┌┘─     ────    ────   └─      └────     │
                      ┌┼─░░ ░│ │░│ │░ ░░ ░░ ░░  ░░░  ░░░░░ ░│ │░░░ ░ ░░░░░░ ░░░░░ ░ ░░░░  •░ ░░░░░ ┌───┘
                      └┘░────┘ └─┘─┘───────────────────── ──┘ └──  •   ──── ──    •  ──     •   ───┘
                      │                                  •   │   ─┐ ┌─┐    •  ───┐ ┌─  ────┐ ───
                      │ │ │░ ░░░ ░░░░ • ░░░ ░ ░ •░░░░│░ ░░   │░│ ░│ │░│░░ ░░░ ░░░│ │░ │░░░░│ ░░░│
                      │ │ │          │           ┌─┐─┘ •  ─── ─┘    └┐  ── •     └─┘──┘────┘────┘
                      │ │   ░░──░ ░░ └────░░░░──░│ │░ │░░ ░░░│  ░  │ │░░░░│ │░░░░│
                       ─┘ │░ •   ───     ░──── ░┌┘─┘──┘──────┘─────┘─┘────┘─┘────┘
                          └── ───   ──────     ─┘
                                                 ──────              ──────             ──
                             │   ┌────────────          ────────────       ────────────   │
                             │ │ │░░░░ ░░░░░░░           ░░░░░░ ░░░░ ─┐     ░░░░░░ ░  ░│  │
                             │ │  ────────────          ────────────  └─░ ░░────────░░┌┘  │
                             │ │                                        ────        ──┘ │ │
                             │ │                                                        │ │
                             │ │                                                        │ │
                             │ │                                                        │ │
                             │ │                                                        │ │
                             │ │                                                        │ │
                             │ │                                                        │ │
                             │ │                                                        │ │
                             │ │                                                        │ │
                             │ │                                                        │ │
                             │ │                                                        │ │
                             │ │                                                        │ │
                             │ │                                                        │ │
                             │ │  ┌─┐     ┌─┐  ───────                                  │ │
                             │ │  │░└─┐─┐ │░└─  ░░░ ░ ─┐                                │ │
                             │ │  └─┘ │ │       ──┐──  └───     ─┐─      ──     • ───── │ │
                             │ │  │  ─┼─┘     ░•  │  ┌┐    ┌─┐─  │ • •  •   •  • │      │ │
                             │ │      │   • ┌─┐   │  └┘ ─┐ │ │░──┘  │░──   │ │   └──────┘ │
                             │   │░      •░ │ │        •░│   │░░░░  │░ ░   │░│       ░░
                                 │   ────    ─┘      ──             │     ─┘  ──  •   ┌─
                                  ░░ ░ ░ ░░    ░░░    ░░░    ░░░    ░░░    ░░ ░ ░ ░░ ░│
                                ───────────── ────────────────────────────────────────
                      ┌─┐─ ┌──┐              •
                      │░│ ┌┘░░│ ░──░ ░ ░░░│ │░┌─░░░•░ ░░░│
                      └─┘ └┘    │   •     │ │ │ ──┐      └┐─┐────┐─┐───┐─────────┐─┐─┐──┐───┐──┐─┐──────────┐
                            ░░──┘░ ░ •░░ ░░░ ░░ ░ │░░░░  ░│ │░░  │░│ ░ │░░ ░ ░░ ░│ │░│  │░░░│ ░│ │░░░░     ░│
                           ───░░░──   •    • ──    ──── •   └────┘─┘   └── •    •  └─┘   ─── ──┘─┘──────────┘
                ┌────┐─┐───   ──   ┌─┐ ┌──┐ •  ────    │ ┌──        ┌─┐   • ───┐ ┌─   ───   •
                │░░░░│░│░░░░│   │░ │░│ │░░│ ░  ░░░░ ░ ░│ │░░ ░  ░ ░ │░│ ░░░ ░░░│ │░ ░░░░░• •░ │
                └────┘─┘────┘   │      │                                                •     └────────────
                                │░│ ───┘░░───── ░───┐─────────────── ─────────░░░──░░░ ░░────░ ░  ░░  ░░░ ░│
                                │░└─ ░░░░ ░  ░   ░  │░ ░               ░      ┌──  ─────          •    ░   │
                                │░│ │ ┌─  │ │            │         │  │░│   ──┘          •  ── ─── ────────┘
                                └─┘ └─┘  ─┘─┘ ──────░─── └─────────┘ ─┘─┘───
                  ──  ──── ────     │   •   └─          •           •        ─┐─────────────┐
                  ░░    ░  ░░░░───── ░ •░░░ ░░░ ░░•  ░──░░┌─── ░░░ ░░│ ░ │░ │░│░░░ ░ ░ ░░░ ░│
                  ──    ─┐░ ──       ─┐  ───┐─     ───   ─┘         ─┘───┘──┘─┘─────────────┘
                      ┌─ │░        •  │     │ •░            ──  ░
                      │░     ┌─┐  • ─┐              • ─┐        ┌┐  │   ──────      ────── ───── ───    ────
                      │    ──┘ │░│   └─ ┌──────────  • │   ┌─   └┘  └───      ────── ░   ░│   ░ │ ░ ───
                      │ ░  ░ ░─┘─┘ ░ ░░ │░░░ ░ ░░░░──░ └───┘░── ░░•░ ░░░░─────░░░░ ░░─────┘┐─░• └── ░░░──  │
                      │           │                              │                         │             ──┘
                      └─ ─────────┘────────┐────┐──────────┐─────┼─┐──────────┐── ░░░░ ░░  └──░ • ░░ ░░░ ░░│
                      │░░ ░░ ░░ ░ ░░ ░░ ░░░│ ░ ░│ ░░░░░░░ ░│  ░░ │ │░░░░ ░░░ ░│ ░░─────────░ ░•░░░─────────┘
                      └─┐────┐── ──────────┘────┘──────────┘─────┼─┘─── ┌─────┘───         ──  ──
                      │ │    │  •                                │      │               ───        ┌──
                      └─┘░░ ─┘ │░░░  ░│ │░ ░░ ┌──░░░░ ──░░░░░░ •░│ • ░░░░░ ░░ •░• • ░ │░░░░│     │ │░ ░  │
                      │      │ │      │ │     │  │   •        •  └─            │   ┌──┘    └┐ ┌─ └─┘ │  ─┘─┐
                      │░░░  ░│ │░░░░ ░░ │░░░ │░│ │░ ░░• │░░░░░░│ ░ ░│ ░░ ░│ │░ │░│ │░░░░░░ ░│ │░░░░ ░│ │░░░│
                      └──     • ─┐ │ ┌──┘── ─┘─┘  •  • ─┘   ┌──┘────┘─────┘─┘──┘─┘─┘────────┘─┘──────┘─┘───┘
                      │░ ░░  •░│ │░│ │░░░░░│   │░░ •░ •░░░░░│
                      └─ ┌─┐  ┌┘  • • ────┐┘┐── • • •  ───  └─────┐───┐─┐─┐─┐─┐─┐──┐─┐──────┐─────┐─┐───┐──┐
                      │  │░│ ░│ ░│ │░░ ░ ░│ │░░│ │░░░ ░ ░ ░░░░░ ░ │░  │░│ │░│ │ │░ │░│ ░ ░ ░│ ░░░ │░│ ░░│  │
                      └──┘─┘──┘──┘─┘──────┘─┘──┘─┘────────────────┘───┘─┘─┘─┘─┘─┘──┘─┘──────┘─────┘─┘───┘──┘









```

*Figure from page 15 (2346x3317 px)*


---



4203-E P-204



SECTION 2 PROGRAM OPERATION



Example 1: [F1] {READ) BOX-1.MIN, BOX-2.MIN [WRITE]



A program assigned the file name "BOX-1.MIN" is stored in the memory with its file



name changed to "BOX-2.MIN".


#### Example 2: [F1] (READ), BOX-2.MIN [WRITE]

The program is stored in the memory assigned the file name "BOX-2.MIN" regardless



of the current file name.


#### Example 3: [F1] (READ) BOX-2.MIN [WRITE]

The control first checks whether or notthe file name given on the tape is "BOX-2.MIN".



Then, the program is stored in the memory assigned with the file name "BOX-2.MIN".


#### Example 4: [F1J (READ) [WRITE]

The program is stored in the memory with a file name assigned on the tape. If not file



name is given on the tape, the program is assigned the file name "A.MIN".



Example 5: [F1] (READ) BOX-1.MIN, BOX-2.MIN;AI [WRITE]



/ I



Stored in succession with a file name Designates the ISO code.



which is already stored in the memory.



The ISO-coded program data which has the file name "BOX-1.MIN" is stored following



the file which is already stored in the memory with the file name "BOX-2.MIN"



{6) The following command reads a tape which contains wrong codes up to the end while replacing



them with"!".



[F1] (READ) file-name;C [WRITE]



The number of read wrong codes is counted and displayed after the completion of tape read



operation. Correct them in the program edit mode.



(7) Reading of a Tape which has a File Name Punched in the EIA Code



The file name punched in the EIA code can be read if an EIA-coded character which corresponds to



$ has been set at NC optional parameter (bit) No. 31.



File name in



Feed holes $ Feed holes 0 Significant information



EIAcode



EIA corresponding code



The control recognizes the coding system of the file by the first "$" code.



The coding system employed for NC data within the significant information area is recognized by the



first end-of-program code (EOB).



During tape punch operation, the file name is always punched in the ISO code irrespective of the



coding system which is employed to punch NC data.


```text


                                                                                               ───
                                                                         ┌───────┐───┐─────────░░░─────────┐
                                                                         │░ ░░░░░│ ░ │░░░░░░░░░ ──░░░░░░░░░│
          ┌───────────        ───                      •                  ┌──────┘─  └─────────      ──
          │           ────────   ┌───────────────  ──── ┌──────┐──────────┘                                │
          └───────────░        ──┘░   ░░ ░   ░░ ░   ░░░ │░     │░    ░░ ░░│ ───────────────────────────────┘
                      ────────   └────┐────────     ─┐─ └───   └─   ─── ── •
                                 │    │          ──┐ │      │                ──────────────────────────────┐
                                 └────┘ ─────  • ░░└─┘──────┘ ─┐─── ── •  ──      ░                ░       │
                                 │ ░ ░ ░░░ ░░──░┌──░ ░ ░ ░░░   │   •    ──  ───────────────────────────────┘
                     ┌────────── │ ──      ┌─   │             ─┘
                     │░ ░░░ ░░   │   ────░─┘ ──    ────────░  ░│
                      ────────── │                          •  └──┐───────┐────┐─┐────┐─┐─┐─┐──────┐─┐─────┐
                                 └─ ░ ░ ░░──  │░░ •░─┐ ░•░ •░░░ ░ │░░░░░░░│ ░ ░│ │░░░ │▒│░│ │░░░░  │░│░░░░░│
                                 │░───────░░──┘───░•░│ •    •  ───┘───────┘────┘─┘────┘─┘─┘─┘──────┘─┘─────┘
                     ┌───────┐─┐ │         │          │ ┌─── ──
                     │░░░░░░░│ │ │░ ░ ░░░░░│ •░░░ ░░░░│ │░░░░░░│
                     └───────┘─┘─┘       •    •              ──┘────┐────┐──── ───   ───────┐─── ──────┐──┐
                                 └─   ░░░ ────░──░───────────     ░░│ ░░ │░   •  ░─── ░     │   │░ ░   │░░│
                                 │    ──         •              │        │          ░     │ │ │ │         │
                      ────────── │ │         ┌───    │   ────   │            ░• ░───── ── │░│ └─┘─────── ─┘
                     │░          │░└─  ░ ░   │ ░░  ──┘───    ─── ───────────── ──     •  • ─┘─┘         •
                     └────────── └─┘         └─────
                                 │                   ┌┐───         ───   │  •    ── ───  • • •  •  ────────┐
                                 └────── ──────    ──┘┘   ─────────░  ───┘──░• ──░  ░ ░── │   ──░░       ░░│
                                 │░░░░ ░ ░░░░  ────  ░░░ ░░░ ░ ░░░░░ ░ ░░░░░░░ ░░░ ────░░░│ ░ ░░─── ───────┘
                     ┌─────────┐ │                    │   ──   │            ┌──────    ─── ─────
                     │░ ░░░░░  │ │     ░ ░ ░ ░  ░   ░░│ │░ ░ ░ │░░░░░░░░░  ░│
                      ─────────┘─ •     ────    •    ─┘ └─    ─┘────────────┘
                                      ──     ───    •  •   ──                ─┐─┐─┐
                                   │░░ ░─────░░░────░──░░ •░░░  │░░░ ░░░│ ░  ░│ │░│
                                   └────  ░ ░───░ ░ • ░───░───  └───────┘─────┘─┘─┘
                                         ───    ───  •

                                    ─────  ─────  ──    ──  ───  •  • • ──      ─────  ────   ──     ──────┐
                                 ┌──     ──    ░──░ ─┐─┐░       │ ░• •░• ░ •░ ─┐     ── ░░ ───░░ ───┐ ░░░ ░│
                                 │░░───── ░─────░░─┐░│ └───────┐┘ •░░░░░┌──░──░│░┌─┐ ░░───░░░░░──░░░└─ ── ─┘
                 ┌─┐   • ────────┘                 │ │ │       │        │        │ │ •                •  •
                 │░│  │░• ░░░░░░░░  ░░░ ░ ░ │░░│ ░ │░│ │░░░│ ░ ░░│ │ │░░   │░░░│ │░ ░ │░ ░ ░ ░░░░ │░░░░░░░│
                 └─┘  │  ───░─────  •  •    └──┘   └─  └───┘─────┘─┘─┘─────┘───┘─┘────┘───────────┘───────┘
                       •          ─┐ ─┐ ┌───    ───  ─┐
                        •░░   •░░░░│ ░│ │░░░░░  ░░░░░░│
                       •     •                         ┌── ───┐─ ─┐─┐─────────┐─┐─┐─┐─┐──────┐──┐──┐──┐─┐──┐
                      │░┌────░░░ ────░░───░  ░───░░────┘░ •░░░│ • │ │░░░░░░░  │░│ │ │ │ ░░░░░│  │░ │░░│ │░░│
                      │ │  ░ ───░ ░   •░  ┌───░  ──      • ░──   ─┘─┘─────────┘─┘─┘─┘─┘──────┘──┘──┘──┘─┘──┘
                 ┌──  │          •        │
                 │   •░ ┌┐        ┌──┐ ┌──┼─┐─                   ─┐  ───── • ────┐
                 └──  ──┘┘─       │  │ │  │ │ ───┐ │              └┐             └────────────────────────
                     │░░░ ░•   ░  │   ░░   •░  ░ └─┘  ░    │      ░│  ░ ░   │░                          ░
                     └──  •    •  ░    ┌─       │          │  │     ┌───────┘───────────────────────────────
                    ─┘░ •  •  • ──────┐┘ ─┐─────┘──────────┘──┘─────┘
                  │         ──        │   │                              ──┐────────                    ───┐
                  └── ──────  ──┐ │ ──┘─┐ └────┐─────   │░│    ─────────   │░ ░ ░   ┌───────────────┐───   │
                     │   ░░   ░ │ │  ░  │ │ ░  │░░░  ── └─┘  ┌┐         ┌┐ │░ │  ┌──┘    ░          │   │  │
                  ┌──┘──────  ──┘─┘ │░  │  ░░  ░░░│    ─┘ └──┘┘──       └┘─┘  │  │   │              └─  └─┐
                  │                 └─┐─┘ ────────┘     │░│                │░ │ •    └─                   │
                  └────────────────   │                  ─┘────────────────┘── • ────  ───────────────────┘
                                   │░ ░─┐───────┐────────
                      ┌────────────┘    │       │        ┌─────┐──┐─  ──┐───┐──┐─  •
                      │      ░         │ │               │     │ ░│ ┌─  │   │  │ ┌─ •
                      │         ┌────┐ │ │        ──   •  ┌──     └─┘ • └─   • └─┘   ──────────────────────
                     ┌┘░░   ░ ──┘ ░░░│ ░ │░  ░░   ░░  ░░│ │░░░ ░│     ░   ░ ░░    ░                      ░
                     └┘───────░ └─┐──┘┐──┘   •  ░ ┌─────┘─┘─────┘─────────────────────────────────────┐────
                     │            │░  │           │                                                   │
                     │                 •    •   ░│  ─┐ ─── • ─── • ─────  •     ──   ┌────┐ ┌─────────┘─  │
                     │ •           ────      ────┘ • └─   •   ░         ──  ────  ───┘    │ │           ──┘
                     └┐░░ ░ ░░░░░░ ░░░░░ ░ │░░░░░░░ ░ ░  ░░ │░──┐░░•      ──    ──    ──── • ─────────
                      └────────────────────┘────────────────┘─  └──














```

*Figure from page 16 (2346x3317 px)*


---



4-4. Duplication of Stored Program



4203-E P-205


#### SECTION 2 PROGRAM OPERATION

To duplicate a file in the memory (MD1 :) or a floppy disk (FOO:), follow the steps below.



(1) Press function key [F3] (PIP).



The function names on the screen will change to those given in item (2) below.



=PIP



MULTI



DATE DIR PIP EDIT PIP LI ST CONDENS [EXTEND]



"PIP>" is displayed.



(2) Press function key [F4] (COPY).



=PIP



Press [F3] (PIP).



FAST RAST PIP



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



Press [F4] (COPY}.



"PIP >" is displayed.



The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.



PIP:COPYCO



Enter the device name, MD1: or FOO:. (The default is MD1 :.)



PROGRAM OPERATION



197/07/15 14:10:00



PIP :COPY



CO[I]



INDEX DISPLAY PROCEDURE



[F2] - MD1:*.MIN



[F3] - FDO:*.MIN



TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl] .



OVERWRITE



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS [WRITE] KEY.



DEFAULT DEVICE NAME



1.01:



DEFAULT FILE NAME=



*.MIN



>XCO



f,01 : FOO: COIAIANO OVERWR/ CHAR.



INDEX INDEX INDEX HI STORY INSERT DELETE CANCEL


```text


                                                                                               ┌─          │
                                                                         ┌──┐─┐────┐─┐─────────┘ ░───────░─┘
                                                                         │░░│ │░░░ │ │░░░░░░░░░░──░░░░░░ •░│
            ───────            •             •  •  ────────────────────── ──┘─┘────┘ └─────────      ──    │
           │       ───────────┐ ┌────┐─────── ── ──                                                        │
           │   ── │           │ │  ░ │     ░       ────────────       ─────────────────────────────────────┘
           └───   └─┐ ░  │░┌─ │  ───┐┘───    │░                     ──
                 │  │    │ │        │        └─      ──────────────   ───────────────────────┐
                 │  │  ──┘┐  ─┐    ─┘    │     ─┐───                ──              ░    ░  ░│
                 │  └─┐   │   │ ──   ─── └─     │   ───── ───── ───   •   ───────────────────┘
                  • │ │ •░│  ┌┘─░░ ──░░ •       │
                   ─┘─┘  ─┘  │  ┌─┐    │ • │ │  └──────────────────────────────────────────┐
                      └─     │  │ │    │   │ │    ░        ░ ░          ░ ░     ░      ░  ░│
                        │ ┌── ── ─┘────┘─── ─┘─────────────────────────────────────────────┘ ─┐
                        │ │                                                                 │ │
                        │ │  ┌───┐                                                          │ │
                        │ │  │  ░│                                                          │ │
                        │  ┌─  ──┘ • ─────┐─ ─────┐─┐─────       ──┐───── ─┐─────┐─┐──────┐ │ │
                        │  │░•    │ │     │ │     │ │      ─────   │     • │     │ │      │ │ │
                        │   • ─── │ │ ───   │  •     ┌──  │  ▒░  •    ──┐  └─────┘  ┌─────┘ │ │
                        │    │░░░•   │░ ░•  └── ───  │░ • │  ────  ─── ░└─ ░░░░░░░• │░░░░▒    │
                         │ ░ └──┐    │               │                    ───  ───  │  ──┐─  •
                         │ •    │  ──┘ ┌─┐     •    ─┘┐─┐     ┌─   │ ┌─┐     ──      ┌─  │
                         │  │░ ░   ░ │ │░│ │░ ░ ░ ░ ░ │░│ •░ ░│▒ ░ │ │░│ │ │ ░░│ ░│ ░│▒ ░│
                        │ │ │ ────    ─┘─┘ └──┐░•  ─── ─┘─  • └────┘─┘─┘─┘─┘───┘──┘──┘───┘
                        │ └─┘     ───     •   └─  • ░░░  ░ │░ │
                          ░░│ ░ ░░░░░░░░│          ────────┘──
                  ┌─┐ ┌──  • │ ┌─ ┌─┐── └┐────────
                  │░│ │ ░░│ ░│░│░░│ │░ ░░│  ░░░░ ░│
                  └─┘ └┐─┐┘──┘─┘──┘─┘────┘────────┘
                       │ │                                                                  ─┐
                       │ │                                                                 • │
                       │ │   ┌───                                                           │
                       │ │  ┌┘░                                  ────     ──     ─────────  │
                       │ │  │░──                              ──┐     ──┐─   ───┐           │
                       │ │ │░     •   ┌─  • ─┐┐──┐   ┌──┐ │ ─┐░░│   ┌─░░│   │░ ░│    ──┐─┐ │
                       │  ┌┘ ░ ──    ┌┘░─┐   └┘  │   │░░│ │  └──░   │░──┘   │ ──┘   •░ │░└─┘ │
                        • │░ │   ──┐ │   └─      │   │   •               │  │   │           ┌┘
                         │ • │ •   └─┘ •   ── ┌─┐┘──┐┘─┐─ ┌┐   │    ░──┐░└─┐░░•  ── ┌─┐░ ┌──┘
                         │  │░ ░│  ░  │░│   ░ │ │ ░ │ ░│  └┘ │░│ ░ ░ ░░│ ░ │ ░   ░░ │ │ ░│
                        │ │ │ ──┘ ────┘─┘┐ ── └─┘ ──┘─┐┘     └─┘ ░   ──┘ ──┘ ──┐ ── └─┘ ─┘
                       ┌┘ └─             └─  •   •    │░                •   •  └─  •   •
                       │   ░──   ░░░ ░░░               • ────────── •
                                        │  ───┐─┐─────┐ │          • │ ┌──┐───┐──┐─┐────┐─┐─────┐─┐──────┐──┐
                      ┌─────░░░░  •░░░░░└─░ ░ │ │░░ ░░│ │░░░░░░░ ░░░░│ │░ │░░░│░░│ │░ ░░│ │░░  ░│ │░░░░░░│ ░│
                      │░░░░░───── ░─────░░ ───┘─┘─────┘─┘────────────┘─┘──┘───┘──┘─┘────┘─┘─────┘─┘──────┘──┘
                      │                  ──
                      │░• •░░░   ░░ •░│
                      │  • ─┐─ ┌─     └──┐─┐───┐──────┐──────┐────┐───┐─────┐
                      │░ ░│ │░ │░░░░  │░░│ │░  │   ░ ░│    ░ │░░░░│ ░ │░    │
                      └───┘─┘──┘─                 • ──┘   ───┘────┘───┘───  └──        •
                                 ─────────────────     ───                              •
                            │   │░░▒▒░▒ ▒░░▒░░░                      ─┐─────     ────┐   │
                            │   │ • ──   ┌──────                      │░░░░░░░░░░░░░▒│   │
                            │  •  ░░ ░░░─┘      ──────────────────────┘──────░░▒─────┘   │
                            │ │ ────────                                     ───      │  │
                            │ │                                                     │ │  │
                            │ │                      ───────────────────────────────┘ │  │
                            └─┘    ─┐──   ──  ──────                                │  │ │
                            │ │ • •░│  ──┐░░ •░░░░░░                   ─────────────┘  │ │
                            │ │  │░░│ ░ ▒│  │▒░  │     ───    •                        │ │
                            └─┘  │░ │ ░ ░░ ─┘░• ─┘─────░░░ ──┐░ ───────  ┌─┐───┐─┐     │ │
                            │ │  │░─┘─ ░░ ░░└─ ░░▒ ░▒   ── ░▒└──░░ ░░░░  │░│ ░ │░│     │ │
                            │ │  │░░░░  │░░░░ ░░┌──┐┐ ──  ───   ───────  └─┘───┘─┘     │ │
                            │ │  └───── └────░──┘  └┘░░                                │ │
                            │ │              •       ──                                │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │   ──                                                   │ │
                            │ │   ░░                                   ───────   ───── │ │
                            │ │   ──  ────   ──┐     ────┐────── ──┐─         ┌─┐      │ │
                            │ │     │   ░ ─┐─  │░─┐ •░░▒░│  ░░░░•  │░• ──────┐┘ │   ── │ │
                            │ └─┐┐░░│ ───░░│   │░░│   ───┘────░░░ ─┘░░ ░  ░░░│  │     ─┘ │
                            │   └┘──     ──┘    ──┘                    ──  ──┘   ────┐  ─┘
                             ── │    ── │      •      ──     ┌─ │ │ ┌─   │    • │    └┐─
                               │   │ ░░ │ │ │░ ░   │░ ░      │░ │ │ │░ ░ │      │  ░ ░│
                               └───┘ ───┘─┘─┘──────┘─ ───────┘──┘─┘─┘────┘─   ──┘─────┘
                                    •                                      ───




```

*Figure from page 17 (2346x3317 px)*


---



4203-E P-206



SECTION 2 PROGRAM OPERATION



(3) Enter the file name of the file to be copy and press the WRITE key.



Example: BOX-1350.MIN, BOX-2000.MIN



t t



Input file name Output file name



I PROGRAM OPERATION



I 97/07/15 14:10:00



PIP :COPY



CO BOX-1350.MIN,BOX-2000.MINII]



INDEX DISPLAY PROCEDURE



[F2] -+- MDl :*.MIN



[F3] - FDO:*.MIN



TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl] ,



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS



DEFAULT DEVICE NAME = !,01:



DEFAULT FILE NAME= *.MIN



>XCO



MD1: FOO: COMMAND OVERWR/ CHAR.



OVERWRITE



[WRITE] KEY.



INDEX INDEX INDEX HI STORY INSERT DELETE CANCa



@J @J @J (B@J @J @J@J


#### WRITE

I 7 ______,



The program which has the file name "BOX-1350.MIN" is duplicated and stored in the memory with



the file name "BOX-2000.MIN".



While the file is being copied, "COPY" and ''file name" are displayed at the upper area of the screen.



At the completion of copying, ">" appears on the console line.


#### PROGRAM OPERATION

>XCO



>CO BOX-1350.MIN,BOX-2000.MIN



TRANSFER COPY BOX-2000. IN



97/07/15 14:10:00



@J @J @J (B @J @J @J@J


```text


                                                                                               ──
                                                                         ┌─────┐─┐───┐─────────░░ ─────── ░│
                                                                         │░░░░ │░│   │░░░░░░░░░───░░░░░░░──┘
          ┌──────   •            •                       •   •                  ─┘   └─────────     ───
          │      ───  ─────────── ───────────────────┐──┐ ─── ──────────────────                           │
          └──────    │░ ░░  ░░ ░   ░    ░ ░  ░       │  │              ░        ┌──────────────────────────┘
                 ─── │         • ── │     ───  ┌──── └─ └┐── ┌──────────────────┘
                     │░░░░░░░│  │░░░│  ░• ░░░│ │░ ░ │░░░ │░░┌┘
                     └───────┘  └───┘──┐░┌───┘─┘────┘░┌──┘──┘
                                       └─┘          └─┘
                                 ┌─────   ────     ┌┘  ──────────┐
                                 │░    ░│ ░░  •    │  ░   ░░     └┐
                                        │ ────   •  ───      ────┘┘─────
                      ── ───────────────┘─    ───
                     │     ░░░░░░░░░░░░░                       ┌─────       ──┐   │
                     │ • │         ───                         │░░ ░░░─────░░░│   │
                     │   │ ░░ ░░░░    ─────────────            └──── ░░░▒░░┌─ │   │
                     │  │  • ░░──░░░░ ▒░▒░░░░░░▒░▒░ ───────────      ──────┘   │  │
                     │  │ • ───  ──────────────────                          │ │  │
                     │  │                                                    │ │  │
                     │ │    ─────  ─── ──────                                │ │  │
                     │ │ • •░░░  ─┐ ░ │░░░░░░───       ──────────────────────┘─ │ │
                     │ │  │░░│  │░│  ┌┘░•                                       │ │
                     │ │  │░░└──┘░░░─┘▒•  ──┐  ───────┐────────                 │ │
                     │ │  │░░│ ░│░ ░░░░ ──░░└─┐ ░ ░ ░░│░░░░  ░░   ┌─────┐─┐     └─┘
                     │ │  │░░░░  ░░░░░░░░░│ ░▒│ ┌─────┘──── ────  │     │ │     │ │
                     │ │  └──░▒│ ────┐░▒──┘───░┌┘                 └─  ── •      │ │
                     │ │     ──┘     └──      ─┘                                │ │       ┌──────┐
                     │ │                                                        │ │      ┌┘      └┐
                     │ │                                                        │ │      │  │     │
                     │ │  ──┐                                                   │ │      │  └─┐─┐ │
                     │ │   ░│                                                   │ │      │  │░│ │ │
                     │ │  ┌─   ────   ───    ┌─────────── ──┐─          ─┐───── │ │    ──┘──┘  │  │
                     │ │  │ ─┐  ░░ ─┐─ ░░──┐ │░▒▒░░░░░░▒▒•░░│░─────┐──┐─ │      │ │    ░░▒  ░  │  │
                     │ └──┘░░│  ──░░│  ──░░│ └───── ────░░ ─┘░  ░  │░░│  │     ─┘ │    ────────┘──┘
                     │     ──┘    ┌─┘     ─┘                   ─┐  └┐─┘           │  ──
                       • ──   • ┌─┘   • •       •     ┌─ │ │  • │ │ │  │ ┌─┐─┐ ┌──
                        •   │   │  │ •░ ░ │    │ │  ░ │░ │ │ │░ │ │  │ │ │░│▒│░│
                         ───┘    ──┘  • ──┘    └─┘   ─┘──┘  ─┘──   ──┘─  └─┘─┘
                       •      •                   ───     •      │      │     ─┐──┐────────┐──┐───────┐─┐─┐─
                      │░─── │░ ░│ ┌─░──┐───────┐ ░░░░│ │░░░ •░░│ │░░│ ░ │░░░░░░│ ░│  ░░░░ ░│ ░│ ░ ░░ ░│ │░│
                      └─ ░░─┘───┘─┘░•░ │░░░ ░░░│     └─┘───  ──┘ └──┘   └── ───┘──┘  ── ───┘ ─┘─    ──┘ └─┼─
                      │           │              ───┐      ─┐   •    ───   •       ─┐  •    •   ───┐   •  │
                     │░░░░ ░ ░ ░░  ░░░ ░ ░░░░• •░░░░│ │░ ░ ░│ •░ ░• │ ░ ░░░░░░░  ░ ░│ │░ ░ ░ ░│ ░ ░│ │░░░░│
                     │   ───                  │ ┌──  ─┘    ┌┘  ┌── ─┘   ───┐────────┘─┘───────┘────┘─┘────┘
                     │░ ░ ░ │░ ░░░░░░ ░ ░░░░░░│ │  ░░░░░░░ │  ░│ ░ ░░░░    │
                     └──────┘─┐──             │    ──────      │     •
                              │  ┌─────  ─────┘           ─────┘ ┌───  ──────┐───┐────┐ •
                           │  └─ │░░░░░ ░░░░ ░│           ░░░░░│ │░░  │      │▒░░│░▒░░│  │
                           │ │    ────────────┘           ─────┘─ ── ─┘░░   ░└───┘────┘┐ │
                           │ │                                        └──────          │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │░│
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │   ─┐                                                    │ │
                           │ │  │░└── ─┐────┐─┐   •                                    │ │
                           │ │  │ │  • │    │ └─── ─────                               │ │
                           │ │ │   •   │                •              ──    ──┐──     │ │
                           │ │ │    •  │                  ───┐ ── ┌─┐ •  ┌──┐  │       │ │
                           │ └─ ┌──  ──┘  │ • ┌─     ┌─ ──░░░└┐   │░└─  ─┘  │   ┌────┐─  │
                           │    │  •   │  │  ┌┘ │    │ •  ── ░│   └─┘░ • │░ │   │░ ░░│  │
                            ── ─┘   ──┐┘   ──┘  └────┘  ──  │ │         ─┘  └───     │ ─┘
                              │░ ░│ ░ │ │░ ░ │  ░ ░    │    │░│  ░ │░   ░ ░│   ░ │░ ░│
                              └───┘┐──┘─┘────┘─────────┘ ───┘─┘ ───┘───────┘─────┘───┘
                                   │                    •      •









```

*Figure from page 18 (2346x3317 px)*


---



4203-E P-207



SECTION 2 PROGRAM OPERATION



(4) Press function key [F7] (PIP QUIT).



>XCO



>CO BOX-1350.MIN,BOX-2000.MIN



FAST FAST PIP



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



Press [F7] (PIP QUIT).



The screen returns to the one displayed in item (1).



[Supplement] 1. When the specified file name "BOX-1350.MIN" is not found in the memory, the



message "no file" will be displayed on the command line.


## 2. When the file name "BOX-2000.MIN" which has been specified as the output file

name already exists in the memory, the following message will appear.


#### BOX-2000.MIN

file exist overwrite? (Y/N)



To erase the currently stored program and store the duplicated one, type "Y" and



press the WRITE key.


## 3. The output file name can be omitted when the output file name is the same as the

input file name.


## 4. When the output file name is omitted, symbols "*" and "?" can be used in an input

file name. In this case, all the corresponding files are duplicated. (Refer to Section



5, 3. "DIRECTORY".)


## 5. In addition to the above duplicating functions, the following functions are optionally

available.



(a) [COPY] input file name, output file name ;A



Duplication is executed following the file which is specified as the output file



name.



{b) [COPY] input file name, output file name ;V



The message "copy OK? (Y/N)" is displayed before starting program



duplication.



To start duplication, type «y" and press the WRITE key.



To abort the operation, type "N" and press the WRITE key.



Example 1: Copying A.MIN in MD1: (memory) to MD1: (memory) under the file name of B.MIN



MD1 :A.MIN,MD1 :B.MIN



Example 2: Copying A.MIN in MD1: (memory) to FOO: (floppy disk) under the file name of B.MIN



CO LJ MD1 :A.MIN,FD0:B.MIN



Example 3: Copying A.MIN in FOO: {floppy disk) to MD1: (memory} under the file name of B.MIN



COLJ FD0:A.MIN,MD1:B.MIN


```text


                                                                                               ┌──       •
                                                                         ┌──┐─┐────┐─┐─────────┘░░───────░─┐
                                                                         │░░│ │░░░ │ │░░░░░░░░░ ──░░░░░░░•░│
                    ──                               ──────────────────── ──┘─┘────┘ └─────────
                  ──   ──────────────────────────────
                   ░┌─┐░    ░   ░       ░   ░ ░    ░
                  ──┘ └┐────── ──────────────────────
                       │      •                                                             ┌─
                       │ │   │░░•                                                           │ │
                       │ │   │   ┌───┐─┐─┐────┐─┐──┐───┐                                    │ │
                       │ │   │░│ │░  │░│ │ ░ ░│ │░░│ ░ │                                    │ │
                       │ │  │ ─┘─┘───┘─┘─┘────┘─┘──┘ ──┘── •   ──┐──    • ── ──── • ──────  │ │
                       │ │  │                             │ •    │  ┌─┐  •  │    │░•        │ │
                       │ └─  ───┐ •  ┌───┐  ─┐───    ┌──  │  ────┘  │░└──   │ ─┐ │░ ──────── │
                        │  ──░ ░│    │░░░│   │░  •   │░ • │  ░▒░░░  │░░░░   │░░│ │  ░░░░▒░   │
                        └─    •       │     ┌┘      │        ┌────  │   •  │ │      │  ──┐─ ─┘
                          ──┐  ─┐  ┌──┘── ──┘ ──┐   │ ┌─┐ ┌─ │ ░   │ ┌─┐  ─┼─┘   ─┐─┼─┐  │
                            │░ ░│  │░ ░ ░ ░ │ ░ │ ░ │ │░│ │░ │░░ ░ │ │░│ ░ │ ░   ░│ │░│  │
                            └───┘  └────────┘───┘───┘─┘─┘ └──┘─────┘─┘─┘───┘─┐░│ ─┘─┘─┘─┐┘
                                                         •                   │ │        │
                      ┌────────   • •                                   │     ░│   ░   ░│
                      │          │ •       ──────────────────────       └──────┘────────┘
                       •     ─── └─                ░
                ┌──────   • •      •      │   │               │     •  ─┐────┐       ────┐───┐───┐─────┐─┐─┐
                │  ░░      •        ┌─────┘─┐─┘░░──  ─────────┘────  ─┐░│   ░└───────░░  │ ░ │ ░ │░░░░░│ │ │
                 ──────────         │░░░░░░░│ └┐─░░──░░ ░  ░░░░░░░░ ░ └─┘────░░░░░ ░ ──           ───  │   │
                                ──  │          │      │     │         │                 ───          ── ───┘
                                    └┐──┐ ─────┘─────┐┘░  ░ │░ ──░░  ─┘░░───────░░─────░░░░──────┐ ░░░░░ ░░│
                                    └┘░ │ ░░░░░░ ░░░░│ ──┐┐ │░░░░─── ░░──░░░░░░ ──░░░░░──── ░░░░░│ ────────┘
                                     └── •         •     └┘─ •  •   ───  ───────  ─────     • ───
                                          │   •░░   │░░──     ──
                                          │░──░─────┘─░ ░░    ░░│
                                         •                      └────────────────┐─┐─┐─────┐─┐─┐─┐──┐───┐──┐
                                    ┌─── ░░░ ░────░░░░│ ░░░ ░░░░ ░░░░  ░░ ░░░░ ░░│ │░│░░░░░│ │░│ │░░│ ░ │░░│
                                    │░░░─────░░░░░──┐─┘────────     •       ──  ─┘   └─────┘ │  ─┘──       │
                                ──  │           │   │          ────┐ ───┐─┐─  ──  ───       • ─┐    ─────┐─┘
                                    │ ───┐─┐────┘ ░░ ░  ░░ ░  ░░░░░│ ░░░│ │░ ░ ░░░ ░░  ░░░│ ░ ░│ •░░░  ░ │░│
                                    │ ░░ │░│ ░░░│ •  •        │    └─ ──   • ────  ─────  │       ────── └─┘
                                    │    │ │     │ ┌─  ───    └────      •       •         ──   •
                                    │   • ─┘  ───┘ │ ──   ── ─┘    ── ░── ───────░──────── ░░ ──░│ ──────░│
                                    │░░ ░░░░──  ░░─┘░░░ •░░░• │░ ░░░  •░ ░░░░░ ░ • ░░░░░░░░──░░░░│ ░ ░░░░─┘─
                                    └──────░░░░───░░────          ───   ───── ──   ─── ────   ───  • ───
                               ┌─┐           ──          ─────┐───   ───     •  ───   •    ──     • •   ───┐
                               │ │  ┌──────┐  ░  ░ ░ ░░• ░░░░ │░░░ ░ ░░░  │ │░  ░░░░░│░ ░░ ░ │░ │░  ░░░░░░░│
                                ─┘  │░░░░░░└┐         •   ────┘  •   ──  ─┘ └────────┘───────┘──┘──────────┘
                                    │       └──┐─┐───┐ ┌─┐     ── ──┐  ┌─  •
                                    │░ │░░░│ ░ │░│░ ░│ │░│ │ │ ░░• ░│  │░ │ ░│
                                    └──┘   │   └┐┘  • •  │ │ │  •   └─ └─ │  └──┐───┐──────┐───┐─┐─┐───────┐
                                          ░░░░░░│    ░░░░░░│ │░░░░ │░ ░│ │░ │░░ │ ░ │░░░░░░│ ░ │░│ │░░░░ ░░│
                                       ─────────┘ •  ──────┘─┘─────┘───┘ └──┘───┘───┘──────┘───┘─┘─┘───────┘
                                    ──           • ──                   •
                                   │    •░ ░     ░  ░│     • │ ░   ░░   ░ •  │
                                   └───┐      ─────  │ • •  ─┘─      •  ┌┐  ─┘─────┐─┐────┐─┐──────────────┐
                                       └─░───┐░░░░░░│ │░░ │ ░░░│ │  ░░│ └┘ │░░░░░░░│ │░░ ░│ │░░░ ░       ░░│
                                       │ •   └──────┘ └───┘ ───┘ └────┘ └┘ └────── │ └────┘─┘──────────────┘
                                       │    •        •     •    ─┘     •  •       ─┘─
                                       │░──░ ┌─░  ░    │ ┌─ •    │            │░  ░░   │
                                       │     │        ─┘─┘   ──┐    │         │  ┌─    └──
                                       │░───┐░░ ────░•░░░   │░ │ ── │░░  ░░░ ░│░ │░░ ░░ ░ │
               ┌───────┐───┐─────────┐─┘    └─┐         │   │  │   •      •       •       └─────┐──┐
               │░░░░ ░░│   │░░░░ ░ ░ │░│ ░ │░░│ │░ ░░░░░│ ░ │░│  │░░│ ░░░│  ░░│ ░│░ ░░ ░░ ░ ░ ░ │░░│
               └───────┘───┘────┐  ┌─┘  │  └─ └─┘──   • └── └─┘──┘──┘────┘────┘──┘──────────────┘──┘
                                │░░│  •░│    ░░░░░░───░░│░░
                ──┐──┐─┐────────┘   ─┐  │  │  ────       ─┐  ──┐─┐──────┐─┐───┐─┐─┐─────────┐──┐──┐──┐
                  │░ │░│     ░░░ ░ ░ │░░   │░░   ░ ░░░░░  │  ░░│ │░░░   │░│   │░│ │░ ░░  ░░░│  │░ │░░│
                ──┘──┘─┘────────┐    │    ─┘               ┌───┘─┘──────┘─┘───┘─┘─┘─────────┘──┘──┘──┘
                                │    │ ░│  └─         ░ ░ ░│
                ┌────────┐─┐────┘    │  │  │  ┌─┐      │  │ ─────┐──────────────────────────┐─────────
                │    ░   │ │ ░    •  │   │ │  │ │ ─────┘──┘      │   ░    ░   ░░░  ░  ░  ░░░│   ░ ░
                 ──────── • ────┐  ┌─┘─░ │        ░       ░┌───   ──────────────────────────┘────────
                                └──┘   ──┘────────░░  ─────┘
                                    ──            ────










```

*Figure from page 19 (2346x3317 px)*


---



4203-E P-208



SECTION 2 PROGRAM OPERATION



Example 4: Copying AMIN in FD0: (floppy disk} to FOO: (floppy disk) under the file name of B.MIN



FD0:A.MIN,FD0:8.MIN



Note that the underlined device name MD1:, which is the default device name, can be omitted.



4-5. Tape Reader Operation Fast Forward Feed



To feed the tape rapidly, follow the procedure below.



(1) Press function key [F3J (PIP).



The function names on the screen will change to those given in item (2) below.



=PIP



DATE DIR



"PIP >" is displa ed.



MULTI



PIP EDIT PIP LIST CONDENS [EXTEl\ll]



Press [F3] (PIP).



(2) Press function key [F5] (FAST FORWARD).



=PIP



READ PUNCH VERIFY COPY



FAST RAST



FORWARD REW l ND



Press [F5]



PIP



QUIT



(FAST FORWARD).



[EXTEND]



The prompt"> FF" will be displayed on the command line (21st line). The tape is fast forwarded to



the end of the tape.



By setting corresponding data at NC optional parameter (bit) No. 1, bit 3, it is possible to select



whether the control recognizes the end of a tape by feed holes or by a code. (% for ISO and ER for


#### EIA).


```text


                                                                                               ┌──       ──
                                                                         ┌──┐─┐────┐─┐─────────┘░░────── ░░│
                                                                         │░░│ │░ ░ │ │░░░░░░░░░ ──░░░░░░░──┘
           ┌────                  ──     •            •           •       ──┘ └─      ─────────      ──┐
           │     ──────┐──  ──────  ───── ───────────┐ ┌──┐─────── ┌─────    •  ──┐───           ──    │   │
           └────┐  ░   │ ░           ░░░         ░   │ │  │   ░    │      │       │        │            ───┘
                └──────┘── ─────   • ─┐       ──      ─┘  │  ──────┘─   • └───────┘─────── │  ░  ───────
                                  •░  └─░░   ░░░░ ──┐ ░ ░•░│                                •
                ┌───┐──────┐─┐────  ──┘      │      │  •   └┐────┐─┐──┐─┐─┐───┐─┐───┐ ┌────┐ ┌─────┐
                │░ ░│ ░░ ░░│ │░░░░░░░░ ░░░░░ │░░░ ░░░ • •░░ │ ░ ░│ │░░│ │ │░ ░│ │░░░│ │ ░ ░│ │░ ░  │
                └──     •       ──          ─┘─    ──              └──┘─┘─┘───┘─┘───┘─┘────┘─┘─────┘
          ┌───┐     ───┐ ───────  ─────────┐   ────  ──────────────
          │░  │     ░░ │  ░░░░░░   ░░░░░░░░│    ░░░   ░░░░░░░  ░░░░│
          └───  ┌──┐  │             ┌───  │ ┌─          ─┐     ────┘
                │  └┐░│  ░ ░░ ░  ░░░│  ░ ░│ │░ ░ ░░░░░░│ │░░░░│
                 │  └─               ┌──   ┌┘─  ───────┘─┘────┘
                 │ ░  │ ░░░ ░ ░░░   ░│ ░ ░ │░░░•
                 └──  │         ┌─ ──┘  ───┘─── ───┐─┐────┐───┐───┐──┐─┐───┐───┐────┐─┐────┐
                      └┐░  ░░░░░│ │░░░░░ ░ ░ ░ ░ ░░│ │░░  │░░░│ ░ │░░│ │░░░│ ░ │░  ░│ │░░░░│
                       └┐─┐─────┘─┘────────────────┘─┘────┘───┘───┘──┘─┘───┘───┘────┘─┘────  ─┐
                        │ │                                                                 │ │
                        │ │   ┌──┐                                                          │ │
                        │ │  ┌┘  │                                                          │ │
                        │ │ ┌┘ ── ──────────┐─────┐─┐─────      ───┐───── ─┐─────┐─┐──────┐ │ │
                        │  ─┘               │     │ │     ┌─────   │     • │     │ │      │ │ │
                        │     ┌─┐  ──       │ ┌─     ┌──┐ │  ░░ ── │  ┌─┐  └─────┘   ─────┘ │ │
                        │ │   │░└┐    ───┐─  ┌┘ ───  │░░│  ─────   │ ─┘░│ • ░░░░░░• │░░░░░░   │
                         ┌┘░  │  └─  │   │   │      ┌┘          ┌─      │  ┌──────  │   ───  •
                         │ •   │░  ┌─┘ │░   •  ── │ │ ┌─┐     ──┘     ──┘  │       │ ──
                         │  •░ │   │ │ │ │ ░░   ░┌┘ │ │ │ ░    ░│ │░ ░ ░ ░ ░ ░   ░ │░ ░│ │
                        ┌┘             └─┘ ──  │░│  └─┘ └─┐ ┌─ ┌┘ └────────────  ──┘───┘ │
                        │  ──    ──────   •  ──┘─┘  │░░ ░ │ │░┌┘ •             ──       •
                        │   ░   ░ ░░░░░░│           └─────┘─┘─┘
                 ┌─┐ ┌──┘─┐  ───   │    └──────┐─┐─
                 │░│ │░ ░░│ │░ ░░│ │░░ ░ ░ ░ ░░│ │░░│░░░░░░░│
                 └─┘ └────┘─┘────┘─┘───────────┘─┘──┘───────┘
                                                                                           ┌─┐
                         │                                                                 │ │
                         │  ┌───┐                                                          │ │
                         │  │░ ░│                                                          │ │
                         │  │ ── ───┐  ──┐─┐─  ── ─┐─   ───      ──      ───    ──         │ │
                         │  │       │    │ │     • │       • ┌──┐  ─┐───┐   ┌──┐  •        │ │
                         │   ─── ─── ┌──┐   ┌──┐   │ ─────  ─┘░░│   │░░░│ • │  │   ┌───┐─┐ │ │
                           ─┐░░░│    │░░│   │░░│    │ ░     ░└──┘   ░░──┘┐  │░│    │░░ │░│   │
                            │   └── • • │ │ │  │    │  ───   │           │ •  └───┐     ─┼───
                            └┐ ░│     ░░│ │ │ ░░     ░░░ ░ │ │░│ • ░ │░     ░░░ ░ │ │░│ ░│
                            └┘ ─┘   ░ • │ │ │ ─┐  ──   │ │ │ │ └─░ • │░│ ░──────┐ ░ │ │ ┌┘
                             └─   ┌──  • ─┘─┘─ │ •  ───┘─┘─┘─┘▒│     │ └─       └─── • ─┘
                               ───┘                           •   │░░░ ░░────  │
                                                               •  └──────░░░░░─┘
                      ┌─           ──┐─                                   ────
                      │ • ─┐───┐    ░│ •   ───────────────────────    ───     ───  ┌───────────────────────┐
                     ┌┘  • │   └─┐───┘                                             │   ░░     ░    ░   ░  ░│
                     │░░  ░░  • ░│ ░░│                                          •      ──          •  •    │
                     │ │                ───   ──    •   ────   ┌───  ──   •   •          •  ──   •      ──
                      ─┘──░░░ ─┐─░•░•░  ░░░──┐░░─── ░── ░░░░───┘░ ░░•░░───░┌──░───────░ ░ ──░░░•░░──────░░
                     •░░░░░░──░│ ░░•░──────░ └──░░░░ ░░ ────░░░│░──░░░•░░░─┘ ░•░ ░ ░ ░┌──░  ░──░──░░░ ░░────
                      • ────  ─┘ ── •       •   ───────     ───    ───  •   •  ────  ─┘  ───   •  ──────
                       •























```

*Figure from page 20 (2346x3317 px)*


---



(3) Press function key [F7} (PIP QUIT).



::?JP



4203-E P-209



SECTION 2 PROGRAM OPERATION



FAST RAST P1 P



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



@J @J@ @J @J



Press [F7] (PIP QUITI.



This completes verification of the punched out program data and the display mode return to the one



in step (1).



4-6. Tape Reader Operation - Rewind



To rewind the tape, follow the procedure below.



(1) Press function key [F3] (PIP).



=PIP



WLTI



DATE DIR PIP EDIT PIP



Press [F3] (PIP).



"PIP>" is displayed.


#### LI ST CONDENS [EXTEND]

The function names on the screen will change to those given in item (2) below.



(2) Press function key [F6] (FAST REWIND).



=PIP


#### FAST RAST PIP

READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



@@J@J@@J~@@J



Press [F6]



(FAST RESIND).



The prompt"> FR" will be displayed on the line (21st line). The tape is rewound up to the beginning



of the tape.



By setting correspondfng data at NC optional parameter (bit) No. 1, bit 3, ft is possible to select how



the control recognizes the beginning of a tape; feed holes on a code. {% for ISO and ER for EIA.)


```text


                                                                                                 ──
                                                                          ┌───────┐───┐─────────░░░───────░░│
                                                                          │░░░░░░░│ ░ │░░░░░░░░░ ── ░░░░░░──┘
           ┌──────                 •             •    ────────────────────┘───────┘─  └─────────    ────
           │      ──    ───┐─────── ───────────── ────
           └──────   ──┐   │            ░    ░░    ░
                  ───  └─┐─┼──────────────────────────
                         │ │                                                                 ┌─┐
                         └─┘                                                                 │ │
                         │ │  ┌───┐                                                          │ │
                         │ │  │░  │                                                          │ │
                         │ │ ─┼───┘─┐─ ──── ─┐──────────  • •      ──     ─┐──┐┐─ ── •       │ │
                         │ │  │     │░•    │ │             │ • ┌─┐    ┌─── │  └┘ │ ░•        │ │
                         │ │   ───  │   ──┐┘  ┌──┐     ─── │  ─┘░└─   │░░     │  └─   ─────┐ │ │
                         │   ─┐░░░• │  •░░│ • │ ░│    • ░  │  ░│░░░   │░•░│  │░ ─┘   │  ░░░│   │
                          ──  │  │ •     │   │       •           ─┐─  │  ─┘  │   │   │  ──┐┘  •
                             ┌┘──┘  ┌──┐─┘ ┌─┼─┐─┐ ─┐ ──┐─  │ ┌─┐ │ ┌─┼─┐  │ └── └─┐─┼─┐  │
                             │   │  │░ │ │ │ │ │ │ ░│ ░ │   │ │░│ │ │ │░│ ░│ │ ░ ░ │ │░│ ░│
                             └───┘  └──┘─┘─┘─┘─┘─┘ ─┘───┘───┘─┘─┘ └─┘─┘─┘──┘─┘┐░┌──┘─┘─┘─┐┘
                                  ──              •              •            │ │        │
                                                                                │   ░    │
                                                                                 ───
                            ───────┐─┐────┐──┐──────┐─────┐──────┐───┐─┐──────┐─┐   ───┐─┐───┐─┐───────┐────┐
                         ░── ░░░░░░│ │░ ░ │░░│    ░ │░░  ░│ ░ ░ ░│░ ░│ │░░░ ░░│░│░ │░░░│ │░░░│ │░ ░ ░ ░│░ ░░│
                       ──░░░───────┘─┘────┘──┘──────┘─────┘──────┘───┘─┘──────┘─┘──┘───┘─┘───┘─┘───────┘────┘
                         │ •
           ┌───┐    ─────┘  ────┐───────────┐─ ────────┐
           │  ░│     ░ ░    ░░░░│   ░░░ ░░░░│   ░░░░░░░│
           └───┘ ───┐           │           └───  ───┐ └──┐
                    │░░░░  •░ │░│   ░ ░ ░ ░ ░ ░░░│ ░ │░░░░│
                 •   ─┐   •   └┐ •   •   ─┐     ┌┘───┘────┘
                  │   │░ ░░│   │░░│ │░│ ░ │ ░ ░░│
                  └──  ────┘───┘──┘─┘─┘───┘─────┘
                                                                                              │
                          │                                                                 │ │
                        │ │   ┌───┐                                                         │ │
                        │ │ ┌─┘   │ • ───── ─────────┐────┐─                                │ │
                        │ │ │        │     │         │    │ ─┐─┐─                           │ │
                         │      •  │ │ ┌─  │ │   │ │ └┐─  │  │░│  │    ┌┐ ─┐─────┐  │  • •  │ │
                         │ •  │░ ──┘ └─┘ ──┘ └───┘ │  │░ ─┘  └─┘─ │    └┘─ │░░░░░│  └── ░░│   │
                         └┐░• └─            •         └─     │   •         └─────┘─      ─┘  ─┘
                         └┘     •       •     ─┐    │   │   ┌┘┐─    ────   │       │
                         │ •   ░ ░   ░ ░   ░   │░│ ┌┘ │░└─┐─┘ │░│ ░  ░ ░   ░ ░ │ ░ │ ░░  ░│
                         │    ────    ──── ────┘░│ │  └┐┘ │ │ └┐┘ ───────░── ──┘───┘ ─── ─┘
                        ┌┘───     ┌──     •    └─┘─┘   │░│     │ •       •  •       •   •
                        │  ░░  │░ │░░░░░•           ───┘─┘───
                       ┌┘     ─┘ ┌┘┐     ┌──┐──┐────         ─┐───┐───┐──┐─┐───┐────┐──┐───┐
                       │░│  ░ ░░┌┘ │░░░│ │░ │░ │░ ░░│ ░│ • ░░░│ ░ │░░░│ ░│░│ ░ │░   │░ │░░░│
                  ┌─┐─┐┘ └─     └┘ │  ┌┘ └──┼─┐   │ └──┘─ ┌───┘───┘───┘──┘─┘───┘────┘──┘───┘
                  │░│ │ ░░░│ ░░ ░░│ │░│ ░│▒ │░│░│ │░░░░░░░│
                  └─┘─┘─┐─┐┘──────┘─┘─┘──┘──┘─┘─┘─┘───────┘
                        │ │                                                                 ┌─┐
                        │ │    ──┐                                                          │ │
                        │ │  ┌─  │                                                          │ │
                        │ │  │  ─┘─┐─┐───── ─┐──── • ─────┐─┐     ──┐             • ─────── │ │
                        │ │  │     │ │     │ │    │ •     │ │       │ ┌──     ── • │        │ │
                        │ │   ┌──┐   └──── │ └────┘   ┌── │ └─────  └┐┘░░│   │░░│  │ ────── │ │
                        │  ───┘░░│ •  ░░░░• • ░░    ──┘░░• │░░░▒░░   │▒•░│   │░ │   •░░░░░░   │
                         •    └──┘    •      ──   •   │ │  └────    ─┘─  │   │         ──┐─  •
                          ──┐    │   • ┌─┐  •  ─┐─  ──┼─┼─ │           •       ┌── ──┐─  │
                            │ │░ │ ░ ░ │░│ │░ ░ │ ░ ░ │░│ ░ │ │░│ │░ ░░▒ ░ ░ │ │ ░   │░│ ░│
                             ─┘──┘─────┘─┘ └────┘─────┘─┘───┘─┘─┘ └───┐─  ─┐─┘─┘─────┘─┘ ─┘
                                          •                      •    │    │            •
                                                                      │ ─┐─┘─────
                                                                      │░░│ ░░░   •
                       ┌─  ─────┐───┐─────────┐─    ────── ───  ─── ── ──┼─────   •
                       │ ──     │   │░        │ • •           ──         │         ────────────── ──────────┐
                      │     ┌── └───┘─────────┘  • ───────  ──  ──────── └────┐ ──               •    ░    ░│
                      │  ── │░░•                                              └─
                      │               •   ── ──     ─┐ ┌───   ──   ───  ─────┐   ───     •   ──     ── •  •
                      │   │  •░   ──   ──  ░  ░──░── └─┘ ░ ┌── ░ ── ░░──    ░└───░░ ░    ░░•░░░─────░░░░── │
                      └┐┐ │░░░ • ░░░░░░░░░ ░───░░ ░░░░ └───┘░░░•░░░░──░░░──── ░░░░───┐ ┌───░─── ░ ░░────░░─┘
                       └┘─ ──── ────────────   ────────     ─── ────  ───     ────   │ │   •   ─────    ──









```

*Figure from page 21 (2346x3317 px)*


---



4203-E P-210



SECTION 2 PROGRAM OPERATION



(3) Press function key [F7] (PIP QUIT).



=PIP



FAST RAST Pl P



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



@J @J (ill@ @J @J @J @J



Press [F7] (PIP QUIT).



This completes verification of the punched out program data and the display mode return to the one



in step (1).



4~7. PIP Quit



This sub command quits the transfer mode, and provides a return to the previous program operation



mode.



The operating procedure is indicated below.



(1) Press function key [F7] (PIP QUIT).



;;;pjp



FAST RAST PIP



READ PUNCH VER I FY COPY FORWARD REW I ND OU IT [EXTEND]



"_@J@J@@@J@J ~@J



Q 1s displayed. Press [F7] (PIP QUIT)



The prompt"> Q" will be displayed on the command line. The transfer mode is quit and the previous



program operation mode is restored.



The display screen wHI change as shown to the right with assigned function names also changed.



=PIP



DATE DIR PIP



MULTI



EDIT PIP LIST CONDENS [EXTEND)


```text


                                                                                               ───
                                                                         ┌───────┐───┐─────────░░░─────────┐
                                                                         │░░░░░░░│ ░ │░░░░░░░░░ ── ░░░░░░░░│
          ┌───────  ──                               ────────────────────┘───────┘─  └─────────      ───
          │       ──   ──────────────────────────────
          └──────┐ ░───░    ░          ░    ░░░
                 └──   ─┐─┐──────────────────────────
                        │ │                                                                 ┌─┐
                        └─┘                                                                 │ │
                        │ │  ┌───┐                                                          │ │
                        │ │  │░ ░│                                                          │ │
                        │ │ ─┘ ── • • ──── • ─────┐─┐─────┐───   ───    ──  ─┐──┐── ─────── │░│
                        │ │  │     │ │    • •     │ │     │░  ┌─┐     ┌─  •  │  │  •        │░│
                        │ │   ───┐ │ └───┐   ┌──┐─    ┌── │  ─┘░└┐  ─┐┘░     │  │   ┌─────┐ │ │
                        │   ──░░░│ │  ░░░│   │░░│  • ─┘░   •░░░░░│  ░│▒ ▒│  │░  │   │░░░░░│   │
                         ──     │     │         │   │    •  •   ─┘ ──   ─┘  │   │   │  ──┐┘ ──
                            ┌─ ─┘  ┌──┼─┐ ──┐ ┌─┘ ─┐┘ ┌──  • ┌─      ┌─   ┌─┼── └───┼─┐  │
                            │   │  │░ │ │ ░ │ │   ░│  │▒ ░ ░ │░│ │ │ │░│ ░│ │ ░ ░ ░ │░│ ░│
                            └───┘  └──┘─┘───┘─┘── ─┘──┘──────┘─┘ └─┘─┘─┘──┘─┘┐░ ────┘─┘─┐┘
                                 ──              •              •            │          │
                                                                              ░•   ░    │
                                                                                ───
                            ──────┐─┐────┐─┐───┐─┐──┐────┐──────┐───┐─┐────────┐   ───┐───┐─┐────────────┐─┐
                      │ ░─── ░░░░░│ │░░░░│░│░  │░│ ░│░  ░│ ░░░ ░│░ ░│ │░░░ ░░ ░│░ ░░░░│ ░ │░│ ░░   ░ ░ ░ │░│
                      └──░░░──────┘─┘────┘─┘───┘─┘──┘────┘──────┘───┘─┘────────┘──────┘───┘─┘────────────┘─┘
                         •
          ┌── │   ───┐───  •
          │  ─┘      │  ░ ░
          └──         •    ───────┐──┐─────┐────┐─┐─┐─┐─┐───────┐──┐───┐───┐───┐───┐─────┐─┐─┐───┐─┐───────┐
                │ ───░░░ ░░░░░░░░ │░░│ ░ ░ │░░░░│ │░│░│ │░   ░ ░│░░│ ░ │░ ░│   │ ░ │░░░░ │ │ │░ ░│ │░░░ ░░░│
                │░░░░───    ───    •   ───          └─┼─┘───────┘──┘───┘───┘───┘───┘─────┘─┘─┘───┘─┘───────┘
                │       ────   ──── ─┐─   ┌──┐──────  │
                │ ░  ░░░ ░░░ ░ ░░░░ ░│ ░  │░ │░░░ ░░░░│
                │  ┌─┐    ┌──  • ┌─  │ ┌─ └┐  ┌─    ┌─┘
                 │ │ │░ ░░│   │░░│ │░│ │ ░ │ ░│ ░░░░│
                 └─┘ └────┘───┘──┘─┘─┘─┘───┘──┘─────┘
                                                                                            ┌─┐
                        │ │                                                                 │ │
                        │ │                                                                 │ │
                        │ │  ──   ────────────────   ─────                                  │ │
                        │ └─  ░ │                 ──┐          •       • ─── ┌─┐───         │ │
                        │       │             • ──  │ ┌─┐  ────░──┐ ┌──░• ░  │░│   ─┐─────┐ │ │
                        │     ┌─┘     ┌──┐   │░│     ┌┘░│ •  ░░░░ │ │░░ ░ • │  └─── │     │   │
                        └┐░  ┌┘ └─┐   │  │   │ │    ┌┘          •   │   •   │           • │  │
                         │   │░░░░│ ──┼─░ ──┐┘░└┐───┘ ░░░─── │ │   │░    ───┘   ────┐─┐  ┌┘──┘
                        │   │ │ • ░ ░ │ │ ░ │   │  ░   │ ░ ░ │░│ ░ │  ░   ░ │ ░ ░ ░ │░│ ░│
                        │  ─┘─┘─ ──── │░│  ─┘ •░│ ── ──┘ ─── └─┘  ─┘░•░│░── │   ─── └─┘──
                       ┌┘ •          • ─┘── └─ ─┘─  •   •   •   ──  • ─┘─    •     •
                       │  ░   ░░░░ ░                                     ───   ────    ─┐
                         ────────────                                   │  ░│    ░      │
                      ┌─             ─┐─┐─ ────────────────────────────┐┘   │            │ ───────── ───
                      │░────────┐ ┌─┐ │░│ • ░                          │                 └─         •   ── │
                      │         └─┘ │ └┐       │      ──────────────── └─────────────────  ───────── ──   ─┘
                      │  ░ ░   ░│ │  │ │  ░    │  ░  •
                      │ ┌─┐     │    │    •     │      ────── ┌─── ───  ─────────────────────┐─────────────
                      └─┘ └─   • ──  │ • • •    │   ──       ─┘  ░       ░  ░             ░ ░│ ░       ░░
                            •      ── • •   ────┘───  ────    └─ •  ──  ───────────────────┐─┼─────────────
                       │ │   ┌───                                                          │ │
                       │ │   │░  •                                                         │ │
                       │ │   │░──                                                          │ │
                       │ │         • ───── • ─────┐──────┐──   ── ─┐─────┐─┐─────┐─┐────── │ │
                       │ │  •     • •     │ │     │      │  ┌──  │ │     │ │     │ │       │░│
                       │  •  ┌──┐     ┌─┐ │ │ │ │ └─ ┌─  │  │░   │ │ ─┐┐ │ └─────  └──────   │
                        │  ──┘░ └── ──┘ │   │ └─┘ │  │░  │  └──  │ └─ └┘   ░░░░░░   ░░░░▒░   │
                        └─   │                   •   │          •         ┌──────      ──── •
                          ─┐   ─┐ │ │ ┌─┐ ┌────┐  ── └─┐ ──┐─┐─┐    ┌─┐───┘        ─┐─
                           │  │ │ │ │ │░│ │░ ░ │   ░ │░│   │ │░│ │  │░│ ░ ░ ░ │ ░ │ │▒│ ░│
                           └──┘─┘ └─┘─┘─┘ └────┘─────┘─┘───┘─┘─┘ └──┘─┘───────┘ ──┘─┘─┘ ─┘
                                 •       •                      •              •       •













```

*Figure from page 22 (2346x3317 px)*
