# III SECTION 2 PROGRAM OPERATION 01. LIST OF PROGRAM COMMANDS OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-01.-LIST-OF-PROGRAM-COMMANDS-OCR.PDF*

---


# SECTION 2

4203-E P-182



SECTION 2 PROGRAM OPERATION


# PROGRAM OPERATION

Thls section describes the program operation procedure and the contents of the commands used in the



program operation.



The NC unit has commands for DATE entry, initializing, program deletion, etc. in addition to reading in and



punching-put of a program tape and program editing.



In this system the file names can also be interchanged as individual programs are assigned a file name for



managing the programs.


## 1. List of Program Commands

Item Command Functions Remarks


#### Date DATE Sets the date.


#### Directory DIR Displays file directory.

Transfer* PIP Transfers program file. Sub commands provided



Edit* EDIT Edits program file. Sub commands provided



(Supplement 1)



Multi-file transfer MPIP Transfers multiple files between Sub commands provided



the NC and an external device



uslng the RS232C interface.



List* LIST Lists file contents.


#### Arrangement CONDENS Arranges the stored data.


#### Time TIME Sets the time.


#### Initializing INIT Initializes the memory, floppy

disks and other data storage de-



vices.



Deletion* DELETE Deletes the specified file.



Operation guide GD Displays the operation state of



(Supplement 2) the selected file.



Free area



FREE



Displays the free area in the



memory.


#### Renaming* RENAME Changes the specified file name.

File protection



PROTECT Prohibits writing to or renewing of



the specified file.



MS-DOS* MSDS Transfers the program files in the Sub commands provided



MS-DOS format.


```text


                                                                                                •
                                                                         ┌──┐──────┐─┐──────────░░───────┐─┐
                                                                         │░░│ ░░░░ │ │░░░░░░░░░░──░░░░░░ │░│
                                                                           ─┘ ─────┘ └─────────
           │  ─── ─── ───             ───                   •        •                                     │
           └──▒░░░ ▒░░░░░░░ ░░ ───── ░░░░ ─────────────  ┌──░ ░─────░ ░──────┐ ────────────────────────────┘
           │▒░▒───────░•░── ──      ───░░░▒░░░▒░░▒▒▒░▓▒░ │▒▒░ ▓▒▒░▒▒▒ │░▒░▒▒░└─
           └───       • •              ────────────────── ────────────┘──────┘
                  ─┐          ──────                                           •   ───
                 •░│ •░ ░   •░░  ░   ░       ░       ░                 ░        ───   ┌────  ───────────────
                │ •    ┌─       ────────────────────────────────────────────────   ───┘    ──
                │      │ •
                │░        ─┐      •  ┌───   ───────    ──     ──────────────────┐─┐─┐─┐─────┐─────────┐─────┐
                │          │  ───  ──┘    ──        ───  ┌────░    ░ ░   ░ ░ ░  │ │ │ │░░ ░░│ ░ ░░░░░░│  ░ ░│
                │░   ░░░░░░│ ░ ░ ░ ░░ ░──░░░ ────░ ░░░░  │░░░░─┐                      └─           ───┘   ──┘
                │                        •                     └───┐─────┐───┐───────┐  ────────┐──    ───
                │ ─────░   ┌─░ ─────  ░░│ │░ ░ ░  ░ │░░░░ ░│░│  ░░ │░░ ░░│ ░ │░ ░░░ ░│░ ░░░░░░  │░░ ░ ░░░  │
                └┐░░░░░░░ ░│ • ░░ ░░ ───┘─┘─────────┘──────┘─┘─────┘─────┘───┘───────┘──────────┘──────────┘
                 │
          ┌─┐     ┌────┐──┐─┐───────────────────────────
          │▒│     │▒░▒▒│ ▒│ │░░░░▒▒░▒░░░░░░░░░░▒░░░░░▒░░
          └─┘     └────┘──┘ └───────────────────────────
                           •                             ─────┐───────   ─────────   ────────       ──────
                 │░│    •░░░│     ┌──┐─░░░░░░░░░  ┌──         │░ ░ ░░░─┐          ┌─┐      ░░───────      │░│
                 │░└──┐  ───┘─────┘  │    ┌───── ─┘░  ── ─┐ ┌─  ──────░└──────────┘░└────────░░░░░░ ──────┘░│
                 │░░░░└┐          │  └─░ ┌┘        │░•░░•░└─┘░•                   │ │                     │░│
                 │░░░•░└─────     └─ │░░┌┘         │░░    │ │░ ░──────┐         ──┼─┘                     │░│
                 │░░         ─────┘░─┘  │          │░░░░░░└─ ░ │░░░░░ │  ───────  │░└───┐───────── ────── │░│
                 │░ ░░ ░░│  •     │  │░░└┐         │░──┐─░│░───┘░░░┌─░│            │░ ░ │░   ░░ ░  ░  ░░░░│░│
                 │░░─────┘        │░ │  ░│         │░  │ │       ░ │ ─┘            │  │ │                │ ░│
                 │░               │  └───┘ ────── ┌┘┐──┘ └─────────┘            ── └─ │ │░░───░────░ ░░░░└┐░│
                 └─░░░░░░┌──────┐ └─ │   └─      ─┘ │                             •                       │░│
                 │░░• ░ ░│ ░░░░░│  ░ ░░░░│         ░└────┐─────────────────────┐    ──────────────────────┘░│
                 │░│ ────┘──────┘ │  ────┘  ───────┐  ░ ░│        ░      ░░░░░░│ ─┐ ░ ░ ░░░░ ░░░░ ░ ░  ░░░ ─┘
                 │ │              └──      •       │░░  ░│ ░─┐─┐──░░░  ░ ░░ ░──┘  │ ────────────────────── ░│
                 └─┼─┐──          │░ ┌──┐         │░░░░░ └┐░ │░│░░░┌─┐░░░────    ┌┘                       │░│
                 │░│░│  │         │  │░░└┐        │░─────░└─░└─┘───┘ │           │         ──   ─── •  ───┘░│
                 │░ • ──┘─────┐   │  │   └────┐   │       │ │      └┐ ┌──   ─────┘ ┌───────  ───     ──   │░│
                 │░░░░░░▒░░░░░│   │  └───░░░░░│     ────░░░─┼─┐ ░ ░░│ │░░│       │ │                      │░│
                   ─────── ─── ───┘─ │░░░┌────┘──┐─ ░░░ ──░░│░│    ─┘─┘──┘   ────┼─┘          ────────    │░│
                 •        •          │  ┌┘       │░ │          • ──      │       │░└──────────        ────┘░│
                │░  ░░░░░░░│ ────┐───┘░┌┘    ────┼─ └──┐░░░░ ░░  ░░░ ░──░░░░░ ─┐ └─┘           ───────    │░│
                │░│ ───────┘     │   └─┘         │  │░░└──────────────░░───── ░│ │ │                      │░│
                │░└─         ─── │ │      •    • │  └──┘                      ─┘ └─┼──────────────────────┘░│
                │░░░─────┐───    └─┘┐─────░░│ • ─┘ ─┘  └─────────────────        │░│                      │░│
                │░░ ░ ░ ░│    ──  ░ │░░░░░──┘    │ ░░░░░░░ ░░ ░░░░░░░░ ░░──┐──┐  │░│                      │░│
                │░ │░░ ░░░────░░│ ──┘─────        │ ───░░ ░ ░│ │ ┌──────┐░░│  │  │░│                      │░│
                │░ └──────░░░  ─┘             ───┐┘    ───┐  │ │░│      └──┘ ─┘  │ │                      │░│
                │░         ┌───   ░    ───       │░       │  │ │ └─  ───    │    │░│                      │░│
                │░   ░ ░───┘     ┌─ • •░      ───┼─  ─┐───░──┼─┘─┘ ░ ░░ ░  ░│    └─┘                      └─┘
                │░•  ──     │    │   •   ───     │  │░│░░ │  │     │             │ └─────                ─┘░│
                │░ ░•░░──── │    └─ •░░──░░░─┐─  │  └─░░░░└──┘─────┘────────────┐┘ │     ──────────────── │░│
                │░          └──  │░  │    ░ ░│   │    ░┌─░│     ░    ░░ ░░  ░  ░│  └─────                ─┘░│
                │░┌─────────┘ ░  └─┐ └───────┘   │ ░│ ░│░░░── ░ ░ ──────────────┘  │                      │░│
                │░│          •   │ │           ──┼─ └──┼──░░░░ ░░                ──┘                      │░│
                │░░░┌─┐░░│  │    │░ ░░───░       │░    │          ────┐─┐──  ───┐ ░└────┐─────┐────────── │░│
                │░┌─┘ └──┘  │    │  ──           │   ░ ░░░░  •░── ░░ ░│ │░     ░│   ░ ░ │░ ░░░│ ░ ░░ ░ ░░ │░│
                └─┘              │                │░░░░░░░░░░░░░▒┌────┘ └─── ───┘┐░─────┘─────┘────────── │░│
                   ──────────────┘────────────────┘──────────────┘     •    •    └─                        ─┘























```

*Figure from page 1 (2331x3296 px)*


---



4203-E P-183



SECTION 2 PROGRAM OPERATION



The commands indicated by an asterisk (*} are operated using the directory-selection-based file



operation screen. For the PIP command, the directory-selection-based type file operation screen is used



only for READ, PUNCH, VERIFY, and COPY commands. Basic operation using the commands indicated



above is explained below, such as the function to display the registered machining programs in batch using



the function displayed on the directory-selection-based file operation screen. For details of the functions,



refer to Section 15, "DIRECTORY-SELECTION-BASED FILE OPERATION FUNCTION".



[Supplement] 1. The file edit command is changed to the I-MAP edit command for the I-MAP



specification. For details and operation procedure of the I-MAP edit command and



sub commands, refer to I-MAP EDIT FUNCTION published separately.


## 2. For details of operation guide commands, refer to II OPERATION, Section 6, 8.

"Run Guide Display".



Details of the commands accessible in the program operation mode are explained below.



The operation to select the program operation mode before starting the command operation is used in



common to all commands. This program operation mode selection procedure is first explained; this step is



not explained for the explanation on the command operation.



Procedure to select the program operation mode:



(1) Press the EDIT AUX key.


```text


                                                                                                ───
                                                                         ┌──┐─────┐───┐───┐─────░░░░───── ░│
                                                                         │░░│░░░░░│   │░░░│░░░░░ ─── ░░░░░─┘
           ┌─────    •          •       •  ──  •       ─────   •       ──┘──┘─  ──┘    ───┘─────     ───
           │     ───┐ ┌───────── ─────── ──  ─┐ ──────┐     ┌─┐ ┌──────       ┌─   ────         •           │
           └─────   │ │                    •  │       │ │   │ │ │        │    │ │ │      │              │   │
                 │  └─┘        │ │ │        ──┘ • │   └─┘ ──┘ │ └───  ┌┐─┘  ──  └─┘──┐  ─┘────┐  ─────  │ ──┘
                 └──┘░└─┐───── └─┘─┼─░░ ───┐░░░•░░└─── ░ ░░░░░░─┘░░░┌─┘┘░└──░░┌─░░░ ░│ │░░ ░░░└─░░░░░    •░░│
                 │░░░░  │░░░░   ░░░│░░ ░░░░│ ░ ░░░ ░░░ ░ ░░░░ ░░░░ ─┘░░░ │░░ ░│░── ░░│ │░─────░ ─────░░░░░──┘
                 │░─── ░└─────  ───┘───────┘─  ────────┐ ─────    ░ └──┐ └────┘─  ──          ──      ──    │
                │      •      •                        │        ░  •   │                 ─────    •        ░│
                │  ─┐   ░ ── ░░░░░░ ──── ░ ░ ░  ░│ ░░░░ ░░  ░░░░░ ░░•░░░ ░░───  ░░│   ░  ░░░░░ ░  ░ ░░ ░ ░ ─┘
                 ┌─░└─────░░░░─────┐░░▒░─────────┘──┐───────────────░──────░░░────┘ ░─────────┐──── ────
                 │          ┌─     └─               │                                         │    │    ───┐
                 │░░░░░░░░░░│   │ │  ░────░───░│ │░░░ ────────░─────┐─┐───  ───░░ ───────── ──┘────┘ • •░░░└─
                 └──────────┘   └─┘  │    •   ─┘ └───┐           ░  │ │         │  ░          ░         ──┐┘
                                     │ │        •    │   │ ┌───░ ░  │  │  ░░   ─┘── ────  ───────── ──── ░│
                                ┌─┐ │░░│ │░░░░░░░░  ░░░  │ │░░░│   ░│  │░░    ░░  ░░░░░░░ ░░░░░░░░░•        │
                                │░│ │░ └─┼─░─────    •░  │  •░┌┘┐  •   │░┌─┐░ ────────░   ░───░┌─┐─  ──  ──┐┘
                                         │             ── ── ─┘ └── ───┘─┘ └──        ─────   ─┘ │ ──  ──  └┘
                 ┌────┐──┐─┐─────────   ─┘ ░░░•   ░ ░░                    •
                 │░░░░│ ░│░│    ░░ ░ ───░░────░░┌─────     ░░      ░░      ░        ░     ░   ┌┐
                 │         │    │               │     •                        •              └┘─────  ─────
                 └─────░░•░└────┘─░░──░░░────░░░└─░░░░░░░  ░░░░ ░░░░ ░ ░│ ░ ░ │░    ░░ ░ ░ ───░░░ ░ ░── ░░ ░│
                 │     ──░•       ── ░───░   ───   ─────     ──  •      └───░ │     ──┐ •                   │
                │                                         ──   •  ──   •    ──     •  └─  • ───  ────  • •  │
                │     ░ ░     ░   ░ ░░ ░░░░░┌─ ░ ░ ░ ░░  ░░░░  ░░ ░░░┌─       ─────      • •   ──    ── • ──
                 │                          │ │       ─┐ ──┐─────────┘
                 └┐                 ░ ░  ░ ░│ │░░      │   │
                  │ ┌─┐                    ─┘ └────────┘───┘                                ──
                  │ │ └┐ ░░   ░    •      ░░│                                             ┌─ ░─────┐
                   • • └─────────── ────────┘                                             │░       │
                                                                                          │ ──░  ──┘
                                                                                          │▒░   │░░│
                                                                                          └─────┘──┘















































```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-184



SECTION 2 PROGRAM OPERATION



(2) The lamp at the upper left comer in the key lights and the screen changes to the program



operation screen. The function names also change as indicated below.



DATE



01R



PIP



EDIT



~~r,



LIST lcoNDENS



(EXTEND]



@ @J @J



@ @) @----.



BLANK RUN



TI ME IN IT DELETE RENAME DEF I NE FREE OU I DE [EXTEND]



PROTEC~ MS-DOS



DNC-A



DNC-B [EXTEND]



These commands are explained below.



The keys change in



this order when



[F8] (EXTEND) is



pressed.


```text


                                                                                               ───
                                                                         ┌───────┐───┐────┐────░░░─────────┐
                                                                         │░ ░░░░░│ ░ │░░░░│░░░░ ──░░░░░░░░░│
          ┌──────   ──        •          •         ───  •        • ──   ─┘───────┘   └────┘────      ───
          │      ┌─   ────┐──┐ ───┐──┐──┐ ┌────────   ── ──────── │  ──┐          ───          •           │
          └──────┘  ─┐░   │  │   ░│  │  │ │░                      │    │        │     │              ──────┘
                 └── │            └─   ░     ──    ──────┐   │░───      ─────┐  │    ░│   •         •
                      │ ░ ░  ░ ░ ░░░──── ░ ░ ░░░  ░░░░░░ │░• │░░ ░░ ░░  ░░ ░░│  ░░░░──┘─── ─────────
               ┌─┐    └─────────────    ─────────────────┘─ • ───────────────┘──────
               │ │                                                                  │
               │ │                                                                  │
               │ │                                                                  │
               │ │  ┌─┐─── • ─────┐─┐─────┐─┐──── •       • ───── • ─────── ──────┐ │
               │ │  │ │   • │     │ │     │ │    │ ─┐───── │     │ │       │      │ │
               │ └─  ┌┘─    │  ─┐         │  ┌── │  │░░   ░│   │ │░└────── └┐─────┘ │
                │  ──┘░ ─── │ • └── ───── │  │░ ─┘  └─── •░│  ─┘─  ░░▒░░░   │░░░░░
                └─   │                             │    •         ───────┐  │  ──┐  •
                  ──   • •    ┌─  │ │ ┌─┐ ─┐  ─┐── │ ┌─┐ • ┌─┐─┐ •       │ ─┼─┐  │   ┌─
                    │  ░│  │░ │░│ │ │ │░│ ░│ │ │ ░ ░ │░│ ░ │ │░│ ░│ │ ░ │ │ │░│ ░│   │ │
                    └───┘  └──┘─┘─┘─┘─┘─┘ ─┘─┘─┘─────┘─┘ ──┘─┘─┘ ─┘─┘───┘─┘─┘─┘──┘───┘ │
                ┌─       ──              •              •       •                    │ │           ───┐
                │ │                                                                 ┌┘  ┌─┐─┐──────░  │
                │ │                                                                 │   │░│ │░░ ░░░  ┌┘
                │ │  ┌──┐                                                          │    │ ░ ░┌────── │
                │ │  │  └─   ───── • ──────────────      ──┐─────       ─── ─────┐ │    └────┘      ─┘
                │ │  └─   ┌─┐     │ │              • ───   │     ─── ──    │     │ │   │
                │ │    ── │ │ ┌─┐ │ └────┐   ────   │░░░── │ ───    │░░─┐─ └┐────┘─┘─  │
                │  ─── ░▒•    │░└─┘  ░░░░│  │▒░░▒░  │░──░░  •░░░• ░ └─ ░│   │░░░░░    ─┘
                 •     ─┐               ─┘  └────┐       •   ┌─         │ │   ────  ──
                  ─┐  │ │     ┌─┐ ──┐───  ──     │   ┌─┐    ─┘   ┌──┐─┐ └─┼─┐─
                   │░ │░│   ░ │░│ ░ │ ░░│    │░│ │ │ │░│ ░ │░│▒│ │░ │ │ │ │ │░│ ░│   │ │
                   └──┘─┘ ────┘─┘───┘───┘ ───┘─┘─┘─┘─┘─┘ ──┘─┘─┘ └──┘─┘─┘─┘─┘─┘──┘───┘ │
               ┌─┐       •               •              •       •                    │ │
               │ │                                                                   │ │
               │ │   ┌─┐                                                             │
               │ │   │░│                                                            │ •
               │ │  │  │ ───────────┐────────────┐─┐───── • ─────┐  ─────   ──────  │
               │ │  └──┘            │            │ │     │ │     └─┐     ┌──         •
               │ └┐    └─────────┐   ┌───┐   ────┘ │     │ └─────┘ │     │░  ─────  │ │
                │ └─ │░░ ░ ░ ▒░ ░│   │░  └─  ░░ ░  │     │ │     │ │     │░ │░░░░░ ─┘░│
                │    └── ─── ── •    └─      ──  •  •   • ─┼─   •  └─  ─┐   └─────   ─┘
                 ───┐   │      •    │  •       ┌─    ┌─┐ • │ ┌─┐ •   ─┐ │   │
                    │  ░└┐ ┌─ │░│   │ │░• ░░ ░ │ ░ │ │░│   │ │░│ ░│ │ │ ░ ░ │░│ ░│
                    └┐   │ │  └─┘   │ └─      ─┘ │ │ └─┘ ──┘─┘─┘ ─┘─┘─┘─────┘─┘──┘
                     └┐   │ │                    │ │            •
                      └───┘─┘────────────── ─────┘─┘── •
                                           •          •



































```

*Figure from page 3 (2346x3317 px)*
