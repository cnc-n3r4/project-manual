# III SECTION 2 PROGRAM OPERATION 15. DIRECTORY SELECTION BASED FILE OPERATION FUNCTION OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-15.-DIRECTORY-SELECTION-BASED-FILE-OPERATION-FUNCTION-OCR.PDF*

---



4203-E P-277



SECTION 2 PROGRAM OPERATION


## 15. Directory-selection-based File Operation Function

Operations such as writing files (part programs, etc.) to the NC and outputting files from the NC to floppy



disks are collectively called "file processing". In order to execute a file processing operation, a command



that describes the details of the intended processing must be created and the created command must be



given to the NC.



15-1. File Processing



15-1-1. Procedure for Executing File Processing



(1) Calling Up the Command Creation Screen



Press one of the file processing function keys - for example COPY or READ - to display the



command creation screen.



(2) Creating the Command



Create and editthe command on the command creation screen. Since the first part of the command



(which specifies the command function) is entered automatically, the user has only to input the file



name(s) and option codes.


```text


                                                                                                ───
                                                                          ┌───────┐───┐──┐──────░░░──────────
                                                                          │░░░░░░░│ ░ │░░│░░░░░░───░░░░░░░░░
               ────             •                          •           ───┘─ ─────┘   └──┘──────      •
            ┌─┐     ───────────┐    •  ───            ────  ───                                             │
            │░│    │░░░        └─┐── ── ░ ──┐ ┌──────┐ ░ ░│  ░ ──────────┐ │ ─────────┐─────────────────────┘
           ─┘─┘    └───────────┘ │░░•░░ ──░░│ │░▒░░░░└────┘░───▒░▒░░░░░░░│ │░░░░░░░░░░│
                  ─┘                        │ │                ┌──      •    •     ──  ────────────┐───────
                 │░░───░│░░────────░┌────░░┌┘─┘░░─────░░ ░• ── │░ ░░ •░• ────░───┐─  ──░░ ░    ░░ ░│ ░ ░   ─┐
                 │░    ─┘─  ░  ░    │   ░ ┌┘   •       │      │       •          │              │           │
                 │                  │     │      •     │ ───  │ ───    ─────            ──░     └───        │
                 │ ░ ░░░░ ░░░ ░ ░ ░░░░│ ░ │░ ░░░ ░░░ ░ ░░░░░░░│ ░░░ ░░ ░░░░░░ ░░░ ░░•  │░░░• ░░░░░░░░ ░ ░░ ░│
                 │░────────────── ────┘───┘───────────────────┘───────────────────── ──┘─── ────────────────┘
            ┌───  •              •
            │░ ░│  │░░│ │░░  ░░  ░░•
            │ • └┐ │  │ └─          ──────────────────
           │░  │ │ │         ░  ░          ░  ░       ─┐
           └───┘─   ──┐                  ── ┌─         │
                      │        │           ─┘       •  └────
                      └─       │     │ │    │    ░   │      ───           •     ─────  • •
                      │░       │    ░│ │░            │    │    ──      ──  ──┐─┐  ░  ┌─ │ ──┐  ─── ─────── ─┐
                      │      • │     │ │ ───   ──────┘────┘────    ──     •  │ └─────┘  └─  │               │
                      │ ─── • •   ░░•░ └─ ░░░──                         ── ── •                     ────── ─┘
                  ┌─┐ │    •    │          ┌─
                  │░│ │  ░░░ ░ ░│   ░ ░░░ ░│
                  └─┘ │               │        ───      ── ───    ───         ┌─── •   ─── ──  ────     ───
                       ───────────────┘───────┐░  ──────░░  ░░────░░░──────░──┘░ ░░ ░──░░░ ░░──░ ░░─────░░░│
                      │░░░░░ ░░░░░░░░ ░░ ░░░░░└── ░░░░░░──────░░░░───░░░░░░•░░░──────░░──────░░ ── ░░░ ░──░│
                      └──░• ░░──────  ───────┐┘  ───────      ────   ── ─── ───      ──      ───  ──  •   •
                         • ───      ──       │




















































```

*Figure from page 1 (2346x3317 px)*


---



4203-E P-278



SECTION 2 PROGRAM OPERATION



(3) Executing the Command



With the command creation screen still displayed, press the WRITE key.



The created command is given to the NC and executed.



Any.screen



88[



lfm08BG



(1)



71/1,



Command creation screen



tlC0:019\.AY~



tF2l -> Ji01:•.1i1nt



!'3)



l'l:O:•,MIK



TO OISf"I.A'f '1ffER UUXE$.Wl'8l :P'FUS~ (Fl].



IIFVT TI-ii: IEVICE .11AE NI> Flt.£ M£, '71iEN Pre$ !WRITEl ID.



OS:Ml!,.'T QEVUl: -. a 11'1:



CE:FM.11..T F~U ME • •.lilN



IIOO(



O'§ffll{l



(2)



IPAO!JWI Of'ER,\Tltw.



_,,.



'/EAl;\'IO)PY



T!UIISFffl



ur:a: ot!PL.l'f



[F.e) 101:•~11•



(Fl] F00:•.111•



rt OISA.A'f 01lER IG.XES.AFTE'.A PAESSftG (Fl),



INPUT 1lE O£Vla: 1WiE" NO FILE IW£. nB !'fESS (lif'llf] m',



lEFAUlT 1):\/'tQ. 1WtE = lCIJ;



DE:F""1.T Fil..E IW£ • •.MIM



Fig. 2-2 Procedure for Executing File Processing


```text


                                                                                                ──
                                                                         ┌──┐─┐────┐─┐──────────░░─────────┐
                                                                         │░▒│ │░░░ │ │░░░░░░░░░ ──░░░░░░░░░│
          ┌───────   •                     ────────────────────────────── ──┘─┘────┘ └─────────
          │       ──  ─────┐──┐──┐─────────                                                                │
          └──────  ░┌─     │░ │  │            •                   •                   ─────────────────────┘
                  ──┘ │ •       ─┘─┐        ── ───────┐──────────┐ ┌─────────────────┐
                      │░░• ──   ░░░└─      ░      ░░  │░  ░      │ │        ░░  ░░   │
                      │      ───      ──      ───    •           └─┘    ┌────────────┘
                      │░    ░░░░│ │░ ░░░   ░ │░░░ ░  ░░ ░░   ░ ░░░░ ░░░┌┘
                      │      ───┘─┘──────────┘─────────────────────────┘
                      └─
                      │ ─────────────────────────────────── ─────────────────────────────────────
                        ░░░░░░░        ░░░                 │  ░░░░░░░        ░░░░                │
                     │ ┌────────────────────────────────┐  │ ┌─────────────────────────────────┐ │
                     │ │                                │  │ │                                 │ │
                     │ │                                │  │ │                                 │ │
                     │░│                                │  │ │                                 │░│
                     │░│                                │ │  │                                 │░│
                     │░│                                │ │  │                                 │░│
                     │ │                                │ │  │                                 │░│
                     │ │                                │ │  │                                 │ │
                     │ │                                │ │  │                                 │ │
                     │ │                •             • │ │  │ ────  ──         • •         •  │ │
                     │  ┌───────────── • │ ┌─┐ ─┐────┐    │   │ ░░░░░░ ──────    │ │ ── ──   ──  │
                     └┐ │░   ░░  ░░  ░│  └─┘ └┐ │ ░  └── │    └────────░░  ░     │ └─   ░   •   ┌┘
                      └┐ • ░ • ░     ░└─ ░░ │░│ │     ░  │             ──────┐─┐        ───  ───┘
                       └─ ─── ──────┐ ░ ░───┘─┘─┘────────                    │▓│   ──┐
                                    └──▒│                                    │▓│  │▒░│
                                ────   ▒│                                    │▓│  │░•
                       ┌────────   ░──┐░░─────────     ──┐    ───────┐ ───── │▒└──    ───    ───
                       │░░░░░░░       │░░░         ───   │   │░░░░░░░└─      │░│░         ──    ─┐
                    │  │▒─────────────┘─────────── ░░░•  │   │░──────░░┌─────┘─┘──────── ░░░───  │
                    │  │                           ─── ─┐┘   └─        │                 ───     │
                    │     ──────┐                       │            ──┘                     │   │
                    │  │▒│ ░░░░▒│                 ───── │ │  │░• │░ •░░│                ─────┘─┐ │
                    │  │░│ •░░ ░└──────────┐─────┐      │ │  │░  │░  ░┌┘─────────┐──┐──┐       │ │
                    │  │░░░░░░ ▒░░░░ ░░░░ ░│     │      │ │   ░░░░░░░░│░░░░░▒░░ ░│  │  │       │ │
                    │  └─▒───░▒────────────┘─────┘      │ │   ─────░░─┘──────────┘──┘──┘       │ │
                    │ │  •   ──                         │ │ │      ──                          │ │
                    │ │                                 │ │ │                                  │ │
                    │ │    ──  ──    •      │           │ │ │              •  ──              │ │
                    │   ──  ░──  ░│ ░░────┐ └─────── ───┘ │  ──── ──── ───░░──░░───░────── ───┘ │
                    └─   ░ ──░░──░│ ──░░ ░└─┘░░  ░░        │   ░   ░░  ░░ ──░  ░░░ •░░ ░░░    │ │
                      ─────  ──  ─┘   │▓░•   ─────────────┐┘┐──────────  •  •░▓│    ──────  ──┘
                                      └┐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│▒│▒▒▒▒▒▒▒▒▒▒░░░░░▒▓─┘
                                       └──────────────────┘─┘──────────┐──────
                                         ░       ░                     │       ──────
                                         ──  ──────────────────── ─── ─┘─────
                                                                 •   •       ────────
































```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-279



SECTION 2 PROGRAM OPERATION



15-1-2. Method for Creating Commands



To delete the File "PROGRAM.MIN":



The procedure used for deleting the file by directly entering the file name



(a) Press function key [F3] (DELETE) in the PROG OPERATION mode.



The command creation screen will be displayed.



"DEL", which indicates the DELETE function, will automatically appear on the command line.



!DEL l!i1



{b) Key in the file name "PROGRAM.MIN".



DEL PROGRAM.MIN.



(c) The command is now completed; press the [WRITE] key.



The created command "DELPROGRAM.MJN" will be given to the NC and the file



"PROGRAM.MIN" will be deleted.



Copying the File "PROGRAM.MIN" from a Floppy Disk to the NC Memory under the File Name



"S01.MIN":



The procedure used for copying the file by selecting the file name from the directory



(a) Press function key [F4] {COPY) in the PROG OPERATION mode.



The command creation screen will be displayed.



"CO", which indicates the COPY function, will automatically appear on the command line.



co r,~



(b) Enter the device name "FOO:" and the file name "PROGRAM.MIN".



Do this either by keying in "FOO:" and "PROGRAM.MIN" or by displaying the directory for device



"FD0:" and selecting the file name "PROGRAM .Ml N" from it.



For details on selecting files from directories, see 15-4, "Selecting Files From Directories {OSP



Format)" or 15-5, "Selecting Files From Directories (MS-DOS Format)".



FDO:PROGRAM.MIN



(c) Key in the rest of the command", S01.MIN".


# I co

FD0:PROGRAM.MIN,S01.MIN1i!I



(d) The command is now completed; press the [WRITE] key to execute it.



The created command, "CO FD0:PROGRAM.MIN,S01 .MIN" will be given to the NC and file



"PROGRAM.MIN" in the floppy disk will be copied to the memory under the file name "S01.MIN".



Copying the File "S01.MIN" in the NC Memory to a Floppy Disk under the File Name



"PROGRAM.MIN":



The procedure used for copying the file by selecting the file name from the directory



(a) Press function key [F4] (COPY) in the PROG OPERATION mode.



The command creation screen will be displayed."CO", which indicates the COPY function, will



automatically appear on the command line.



IJj



(b) Key in the file name "S01.MIN" and a comma",".



CO S01.MIN,


```text


                                                                                                ───
                                                                          ┌─────┐─┐─┐─┐──┐─┐────░░░─────────┐
                                                                          │░░░░ │░│ │ │░░│░│░░░░ ──░░░░░░░░░│
                 ──          •      ──          ──────────────────────────┘─────┘─┘─┘ └──┘─┘────      ──
            ┌─  •  ┌────────┐ ──────  ─────────                                                             │
            │░   • │░░ ░   ░│     ░            │                                             ── ────────────┘
            └───┐  │            │░│ ░       ░ ░└────                                           •
                └──┼────────────┘─┘────░─┐───── ░ ░                                  ─────────┐ │
                │  │                     │          ───────────────────────────────┐          │ │
                │  │░ ░ ░──░──────░░───┐ │░░░░ ░ ░│ ░░ ░░ ░░░░░░ ░░░░░░ ░ ░ ░░  ░░░│ ─────────┘ │
                │  └┐ ┌─┐              │ │        │             •                  │            │
                  • │░│ └──░──────────░└─┘┐───────┘─░░ ░ ── ────░░ ░░░░░░░░░░░ ░░░░└──────────
                    └─┘ │  │              │                •      ┌────────────────┘
                        │ ─┘░░░░░░░░• ░░░░│░ ░░░░░░ ░░ ░░ •░░░░░░░│
                        │    •    ┌─                          ─── └───────────┐─┐────┐───┐─┐─┐───────────┐
                        │░░│  ────┘  ──┐░░░░ ░░ ░░░ ░ ░ ░ ░ ░░░  ░░ ░░░░░░░░░░│ │░░░░│ ░ │░│ │░░░░░░░ ░░░│
                        └──┘─  ░  └──  └──────────────────────────────────────┼─┘────┘───┘─┘─┘───────────┘
                                ░░│  •░│                                      │
                    ┌─┐───┐───┐    ──  └─ ───────────────┐
                    │░│ ░░│ ░ │ • ░░  • ░•   ░  ░  ░░ ░ ░└─
                    └─┘───┘─── ░░│   ░    •░░░ •░   ░┌───  ────
                               •░│   ──── ░───┐ ────░│          ────
                    ┌─┐ │ ───   •         •   └─    •          • ░  ─────┐
                    │ │ │                        │    ──────┐── ─┐─      └─   ──  ──    ─── •
                     •  │       ░             ░  └──   ░  ░ │░ │ │     │        ┌─   ──    •  │
                        │                             ┌─────┘──┘ └─────┘┐── ────┘ ──   ───┐ • │
                 •  ──  │       ░ ░ ░░   ───┐────░░░░ │                 │                 │    •
                │   ░  ─┘── │  ░░░ ░░░░   ░ │░░░░░      •   ──  ░ •    ░└─┐   ░───────────┘───  ───────
                │ ┌──── ░ ░ │░░─────────────┘─────────  ░───░ ──── ──── ░ └────░    ░ ░  ░ ░ ░──   ░░ ░  │
                │ │       │                            │                                         ─────── │
                │ └─   •░─┘░░░ ░░ ░│ ░░┌─── ─┐────░ ░• └┐ ┌─ •░░░░ ░ ░░░ ░░ ─────░ ░░ ░░ ░ ░░░░         ─┘
                │   ┌─  │          │   │   • │     •    │ │ •                    ┌───────────────
                    │░│ └─┐░───────┼──░░│░ ░ └─┐─┐─    ─┘─┼─░─────░░░░░░ ░░░ ░ ░░│
                    └─┘   └─       │    │      │ │  ┌─    │       ┌──────────────┘
                        │░│ │░░░ •░    │░•   ░░│░│  │░•░░ │░░░░░░░│
                        └─  └┐    •    │  •   ─┘  • │             └───────────────┐───────┐───────────┐
                        │    │░┌─┐ ░░• ░░░░ ░░ ░░░░  ░░ ░░   ░░░ ░░  ░░░░░░░ ░░░░░│ ░ ░ ░ │░ ░░░ ░ ░ ░│
                        └─── │ │ │ ─┐ ┌────────────────────────────────────┐─┐────┘───────┘───────────┘
                                    │░│                                    │ │
                    ┌───┐────     ──  └┐───┐ ───┐───────┐──┐─┐─────────────┘─┘────┐
                    │   │        ░   • │░  │    │  ░   ░│  │ │░           ░ ░ ░   │
                    └─ │   ░│              │   │        │ ░     ░    • ─┐─── │ │  └─────────────────────────┐
                       │░   │ ┌─┐────────── ┌──┘ ┌─┐─  ░     ░     ░•   │    │ │    ░ ░       ░        ░    │
                       └────┘ │ │ ░░ ░░░ ░ ░│ ░│ │░│░ ── ░────────── ───░    │
                       │        │ │            │    │                         ───   ──────────────────┐─────
                       └┐───────┘┐┘ ─── ┌──┐───┘─┐──┼────  ──────────────────░░░ ───░░░  ░░░   ░░░░  ░│  ░░
                       └┘░░░░░░ ░│ ░ ░  │░░│ ░ ░ │░░│   ░  ░░░░░░ ░░ ░░░░░░░░┌─── ░░░─────────────────┘─────
                         ────┐─  └─── • └──┘     └─   │ ┌──────────────────┐─┘    ───
                             │  •     ░   ░ ─────┘ │░░│░│                  │ │
                    ┌─────┐─ │    ──               └──┘ │ ┌──┐             │ │
                    │    ░│  │░───░░─── ┌────────┐─   ░░│ │░ └┐              │
                    └─────┘─    ░ ─┐░░  │░░   ░ ░│ ░•  ░│ │  ░└──┐         ┌─┘
                            │ ──── └────┘───░░░──┘─░░─┐─░ │░░░░░░│         │ │
                    │ │ │ ┌─┘               ──┐       │    ── ── └─ ───────  └───────┐
                    └─┘ │ │ │                 │░      └───                 ──     ░  │
                        │ │ └─────┐ ┌┐      │ │   •     ░     ░░   ░        ░│        ┌─ • ─┐ │  ─── ─── ──┐
                        │ ░ │     │ └┘      └─┼───  ──                       └──  ────┘   │ └┐┘──   •   •  │
                 ───── │         │    │ ─── ░ │░░ • ░░──── ░   ░░░░   ░░   ░░░ ░ •  ░░  ░ │░ │░  ░  ░  ░░░┌┘
                │      └────┐─ │░│ ░░ │ ░░░│  │░│ ░  ░  ░       •░                  •    ░    ──────┐─┐───┘
                │ ┌────░░░░ │░ │░│  ░░ ────┘──┘─┘─────────────── ───────────┐─────── ────────░      │ │
                │ │            │                                            │                 ──    │ │
                │ │   │░ ░   ──░──┐──░─┐──┐ •░░•░░░░░░────┐──░░░░░────┐──░  │░░░ ░  ░ ░░ ░░░░░░░• ──┘ │
                │   ──┘           │  │ │  └─ │            │           │          ┌──────────────    │ │
                    ░░   ─────────┘──┘░░ ░ ░ └───── ░───┐─┼───┐ ───░──░ ░ ░  ░ ░░│
                    ───┐                     │          │ │   └─   •  ──┐        └─┐─┐─────┐───┐─┐──┐──┐─┐──┐
                       └┐───────────────░│░░─┘──────────┘─┘─░░░░░░  ░░░ │░ ░░░  ░░ │░│ ░ ░ │░░░│ │░ │░ │ │░░│
                       └┘     ░  ░       └─                 ───────────  ──────────┘─┘─────┘───┘─┘──┘──┘─┘──┘
                         ────┐    •   ───  ── ──────────────
                             │  ░  │░•                                       │
                   ┌────┐─┐─┐┘    ┌┘  ──┐─┐─┐─┐──┐─┐─────────────┐           │
                   │░   │░│ │  ░ ░│  ░░░│ │░│ │░░│ │ ░     ░  ░  │           │
                   └────┘─┘─┘┐   ┌┘ •   └─┼─  └──┘─┘─────────────┘         ┌─┘
                             │ ░░│ │░│ │░░│ │░│                            │ │
                             └───┘ └─┘─┘──┘─┘─┘                            └─┘
                                  •            ────────────────────────────







```

*Figure from page 3 (2346x3317 px)*


---



4203-E P-280



SECTION 2 PROGRAM OPERATION



(c) Enter the device name "FOO:" and the file name "PROGRAM.MIN".



Do this either by keying in "FOO:" and "PROGRAM.MIN" or by displaying the directory for device



"FD0:" and selecting the file name "PROGRAM.MIN" from it.



For details on selecting files from directories, see 15-4, "Selecting Files From Directories (OSP



Format)" or 15-5, "Selecting Files From Directories (MS-DOS Format)".



j co



S01.MlN,FD0:PROGRAM.MINM



(d) The command is now completed: press the WRITE key to execute it.



The created command, "CO S01.MIN,FD0:PROGRAM.MIN" will be given to the NC and file



"S01.MIN" will be copied to the floppy disk under the file name "PROGRAM.MIN".



If Input Error is Found:



If an error is found in the created command, move the edit pointer to the location of the error and



correct the character.



(a) Assume that the following erroneous command has been keyed in instead of "CO


#### PROGRAM. MIN,S01.MIN" due to a typing error:

PROGTAM.MIN,S01.MIN if!i



{b) Using the cursor keys, move the edit pointer \\'M' to the character to be corrected, "T".



~,;p, I


#### PROG]f,AM.MIN,S01 .MIN

iii



(c) Key in "R".



For details on editing commands, see 15-2, "Creating and Editing Commands".


# I co

PROGRl!Vl.MIN,S01.MIN~I



{d) The command has now been corrected; press the WRITE key to execute it.



Executing a Command Similar to the Command Previously Executed:



When executing the command "CO PROGRAM.MIN,FD0:S02.MIN" after the execution of the similar



command "CO PROGRAM.MIN,FD0:S01.MIN", the new command can be created following the



procedure indicated below using the previously executed command.



Create the required command by editing the previous command.



(a) Press function key [F4] (COPY) in the PROG OPERATION mode.



The command creation screen will be displayed.



"CO", which indicates the COPY function, will automatically appear on the command line.



co El~



(b} Key in the file name "PROGRAM.MIN" and a comma",".



PROGRAM.MIN,



(c) Enter the device name "FOO:" and the file name "S01.MIN".



Do this either by keying in "FOO:" and "S01.MIN" or by displaying the directory for device "FD0:"



and selecting the file name "S01.MlN" from it.



For details on selecting files from directories, see15-4, "Selecting Files From Directories (OSP



Format)" or 15-5, "Selecting Files From Directories (MS-DOS Format)".



PROGRAM.MIN,FD0:S01


## .MIN iti


```text


                                                                                                ──        •
                                                                         ┌──┐─┐────┐─┐──────────░░───────░░│
                                                                         │░░│ │░░░ │ │░░░░░░░░░░──░░░░░░░──┘
           ┌──────── ───             ────  •     ──────    ───────     •  ──┘   • ─┘ └─────────       •
           │        •   ──────┐──────    ─┐ ────┐      ────        ──── ┌─   ─┐─ •
           └────────         ░│           │  ░  │          │       ░    │     │   │  ───
                    ── │   •    ──┐ ┌─    └┐ ┌─ └──      ─┐┘──────          • │   └─    •   •
                      ─┼┐──░│  •░ │ │      │ │ │    •  • ░│░   ░ ░░  ░ ░┌───         ─── ┌─┐ ─── ──────────┐
                       └┘   └┐─  • ─┘─     │  ─┘   •  │░             ░  │    ────────   ─┘ └─   •          │
                       │ ─── │░ │ │░░   ░ ░│░  │  ░ ░ └─────────────░── ░░ ░│
                       │        │ │          │                              └─── •   ─────── ────────┐─────┐
                       │  • ┌─┐ └─┼─── ░─────┘─┐────┐────┐─────────┐────────░    ░── ░░       ░░░░  ░│   ░░│
                       │ ░░ │░│   │░ ░──░░░░░░░│  ░░│   ░│ ░░░░░░░░│ ▒░░ ░░░░ ░ ──░░░────────────────┘─────┘
                        ────┼─┘  ┌┘┐ │      • ┌┘       │ │       ──┘───────┐─┐──  ───
                            │  • │ │░│  ░ ░• ─┘ ──┐────┘░░ ░░░ ░•          │ │
                    ─── ┌─┐─┘   ─┘┐┘ │   ┌─       │      ┌─┐─    ────┐─────┘─┘──────┐
                    ░   │ │ │░  ░░│  ░  ░│  ░  ░░░░   ░░░│ │░    ░   │░░ ░ ░░░░ ░░ ░│
                    ── •  │ │    •          ┌──── │     •   •                │                ───────┐──────┐
                        ──┼─┘──░  ──────────┘    ─┘────   ──   ─── •░──░░ ───┘ ┌──────────────░░     │░░   ░│
                 ──    │ ░│ ░░░• │░░ ░   ░░░│ ░ ░░ ░░░░░ ░░░   ░░░ ░░ ░░• ░░░│ │ ░░░░░░░░░ ░░░ •     └─────
                │    ──┘      •  │     ─────┘─────────────────────────── ────┘─┘───────────────             •
                │ ── ░ ░──░──┐ ──┘───┐░                                                                      │
                │   ─┐░ ░ ░ ░│ ░ ░░  │ •     ░  ░     ░            ░│ │ ░    ░  ─── ┌─┐─┐░       ┌─┐         │
                │ •  │       ░│  ────┘        ────    ───         ──┘ └─           ─┘ │ │      ──┘ │         │
                │   •         └──       ─────     ────   ┌────────   •         │     •       ──        ──   │
                 ───░░ │░░  ░░ ░ • ┌─  │░ ░  • •         │                     │   │    │      ┌─        ───┘
                    ── └─░         │ │ │     ░│              •   ┌─────────────┘───┘────┘──────┘
                         ───┐░░░░  ░─┘─┘ ─┐─ ░└────   ────┐─┐░ ░ │
                            └───┐───░░    │░░ ░░░ ░│  ░░░ │░└──── ─────────┐─┐
                      ──────┘   │   ─────┐┘─────── └─ ░┌──┘─               │ │ •              ──┐
                            │░    •      │           • │    ┌┐ •         ──┘ └┐  ────┐────────  │
                    ── ──── │  ──   ─────┘──┐─┐────── ┌┘─── └┘─░─────░ ──░ │  └──    │        ──┘
                            │  ░░┌──░░░░░░░░│ │░░ ░░  │░░ ░░│         •   ─┘ │     ── ───────
                    ─┐─┐──┐─┘   ┌┘  ────────┘─┘───────┘─────┘              │ │
                    ░│ │░░│   ──┘
                    ─┘ │ │ ┌─   └─────────────────────────────────────────────┐─────────────┐
                       │ │ │░░•░    ░░░░ ░ ░░ ░ ░░░░  ░░  ░ ░  ░ ░░░ ░ ░░░ ░░░│ ░ ░░░░░░░ ░░│
                       └─┘─┘─┐   •        ┌─┐ ┌─┐  •    •   ┌──────────────┐─┐┘─────────────┘
                             │ ░•  •░░░░░ │▒│ │░│░│░│ │░░░░░│              │ │
                    ┌┐ ┌─────┘   ── ─┐ ┌─ └─┘  ─┘─┘─┘ └──┐─ └─────┐─┐────┐─┼─┘────────────
                 ┌─┐┘┘─┘ ░░ ░░──░░░• │░│ •░░  ░░░ ░░ ░░░░│ • ░░░ ░│ │░░░ │ │░░ ░ ░░░░░░░  ─────────────────
                ┌┘ │         │        •       ──              ░     │          •  ────────                  │
                │  └───┐ ┌───┘   ┌──┐   │  ──┐  ────────┐───┐ ┌─┐───┘─────────░░──                          │
                │  │░░░│ │░░░ ──░│░ └─┐─┘──░░└──░░ ░░░░░│░░░│ │░│ ░░░  ░ ░ ░░░• ░░───░•  ───────────────░░──
                │  │░ ░░ │░│ │░ ░  ░░ │░░░░░ ░ ░ ░░░  ░┌┘┐░░│ └┐┘  │░┌─── ░ •░ ░──      •  ░░░  ░ ░ ░░░  │░░│
                │  │  ───┘─┘ └────────┘────────────────┘ └──┘  │   └┐┘   ───░──┐   • ─── ─────────────── └──┘
                │ ┌┘──     │ │                              │ │   • │          │                            │
                │ │   •░░░░│ └─ ░░░░ ░• ──░░ ░░░  │ │░░░░░░─┘ │░░•░░│ ░ ░░░░░░░│                          │ │
                └─  │  │  ─┘ │    •    │          │ └────┐                     └─                         │ │
                  • │░ │░░░│ │░░░• ░ ░░└─────────┐┘ ░ ░░ └───────░░ ░░░░ ░░ ░░░░░ ────────────────────────┘
                    └─ └──┐  └─── •              │     │ │       ────────────────
                      •   │  │   •     ░░┌─── ┌──┘─── ─┘─┘─░░░──
                       │                 │    │            ──┐   ────────────────────────────────────┐
                       └─── │░ ─┐  │ ░░░░└─── └───────░░░ ░  └─ ░░░░ ░░░░░░ ░ ░░ ░     ░            ░│
                            │  ░│  │░│  •                •     ───  ───────┐ ────────────────────────┘
                   ┌───┐────┘    ─┐ ░└── ──────────────── ───     ──       └─
                   │   │░░   • ░ ░│       ░░░   ░░░░ ░░░  ░ ░           ──
                   └───┘─────  • • ──── ────┐ ┌─ •  ┌───────────────────    ─┐
                             │░░• │░░░░░░░░░│ │░░ │░│                      • │
                   ┌─┐─┐─────┘   ┌┘  •     •    │ │ └────────────────────── ─┘
                   │░│ │░░░  │░ ░│ ░• ┌──── ──░░└─┘░│ ░░ ░░  ░░░░  ░░  ░░░
                   └─┘─               │                │          │ •  •  ───┐──┐─┐─┐──────┐───┐────┐─┐───┐─
                       ┌───────░░░─── ░░░░ ────░░─┐ ───┼─┐░  ░░░░ │░ │  │░░░░│ ░│░│ │░░░░░░│ ░ │░░░░│ │░░░│
                       │    ░ ░──   ░──────░    │░│ ░░░│ └─ ─────    └──┘────┘──┘─┘─┘──────┘──  ────┘ └─── │
                                              │ │      │         ────                         ──     •    ┌┘
                      ─┐ ░•░░░░•   ──░░│░─────┘─┘────┐─┘░ ░•░░• •░ ░ ──┐─┐░░• ░ • ░  │ ░      ░░ ░     ░ ░│
                       └─  ─┐──   │    │             │    │    •       │ │           └────────────────────┘─
                       │ ── │░    │  ──┘░░░ ░░┌─┐ ░── ┌─┐ └──░ ░░ ░  •░│  ── ┌────┐ ─┘
                           ─┘┐  │ └┐ ░   ░ ░│ │░│ ░   │░│ │░░░ ░┌───  •      │    └─
                             └──┘  └────────┘ └─┘─────┘░│ └────░│           ─┘
                                             •         • •     • ───────────











```

*Figure from page 4 (2346x3317 px)*


---



4203-E P-281



SECTION 2 PROGRAM OPERATION



(d) The command is now completed: press the WRITE key to execute it.



The created command, "CO PROGRAM.MIN,FD0:S01 .MIN" will be given to the NC and file



"PROGRAM.MIN" will be copied to the floppy disk under the file name "S01.MIN".



(e) Press function key (F4J (COPY) in the PROG OPERATION mode once more.

• I



(f) Read the previous command.



For details on how to do this, refer to 15-3, "Use of the Previous Command".



I co



PROGRAM.MIN,FD0:S01.MIN~I



(g) Using the cursor keys, move the edit pointer



"tf



to the character to be changed, "1".



PROGRAM.MIN,FD0:S0'IMIN



(h) Key in "2".



l~c__o _



P_R_o_G_RA_M_.M_I_N_,F_o_o-:s_o_2_iM_1_N_ll_'.!------.



(i) The command is now completed; press the WRITE key to execute it.



The created command, "CO PROGRAM.MIN,FD0:S02.MIN" will be given to the NC and file



"PROGRAM.MIN" will be copied to the floppy disk under the file name "S02.MIN".


```text


                                                                                                  •
                                                                          ┌──┐────┐─┐─┐─────────░░░─────────┐
                                                                          │░░│ ░░░│ │ │░░░░░░░░░ ── ░░░░░░░░│
           ┌─────────       •          ─── ──        ─── ──── •       ────┘──┘────┘ │ └─────────      ──
           │         ──  ─── ───────┐──   •  ───────┐   •    │ ┌────┐─             •
           └───────── ░ │           │       •       │        │ │    │       │     │  ┌──── ───────   ─────
                     ── │    │      │  ── ──   ┌─  • ───────┐┘┐┘─   └─┐─┐ ┌─┘─    │  │            ──
                        │░───┘────┐  ──  │░ •  │ │ ░░░   ░ ░│ │░░ ░   │░│ │░ ░•  ─┘  └─────    ──   ┌──── ┌─┐
                        └─        │  ░   │   │   └─         └─          │   │  │  └─   ░   ───    ──┘    ─┘ │
                        │ ────────┘───── └── │ • ░░░────────░░░┌─┐─┐─┐░░│░──┘──┘ ─┘ ░───── ░░░░──    ────  •
                    ┌─┐─┘                     • •              │ │ │ │                      ┌──
                    │░│ │  ░░ ┌───░░░•░░ ░ ░   ░ ░ ░   ░░ ░░░░░░ ░░░ ░░░░░ ░ ░░░░│ │░░│ │░░░│
                    └─┘─┘─────┘   ──┐░┌───────────────────────────────────────┐──┘─┘──┘─┘───┘
                                    │░│                                       │
                     │  ┌─────    ──  └┐──────┐──                            ─┘
                     │  │  ░     •     │      │░
                        │  ─┐ ──┐      │      │    ┌─┐───────┐ ┌─┐─────────────────────────
                        └── └┐░░└─  ┌──┘─────┐░ ┌──┘░│ ░    ░└─┘░│     ░   ░       ░   ░
                             │      │░░   ░░░│ ░│  └─       ░░░ ░│ ──     ─── ┌───────────
                     • ─┐────┘    ── •   ────┘ ┌┘    •░       ┌─░└─           │
                      ░ │ ░  │░                │  ░    ░      │                │     ┌─ ──────
                    ─── └────┘┐ ─┐ │ ────────  └─       ──────┼─ ░──────────   └──── │ •
                              │░░└─┘┐░░░░░░░░│ ░░░ ░░░  ░ ░░░░│ ░│          • │     ─┘─ ─────
                    ┌─┐─┐─┐───  ┌┘  └────────┘────────────────┘──┘            │
                    │░│ │░│ ░ │░│
                    └─┘─┘─┘───┘ └┐ ┌─────┐───┐─┐───────┐──┐───┐──┐          ┌─┐
                              │░░│ │░░░░░│░░░│ │░░░░░░░│░░│▒░░│ ▒│          │ │
                    ┌─┐─┐─┐───┘   ─┘ ───┐ ┌─┐┘ │    ┌─┐  ─┘─  └┐ └──────────┘─┘─────┐
                    │░│ │ │ ░░░──░░░░ ░ │░│ │░ ░░░░░│ └──░░ ░• │░│ ░░ ░░░ ░ ░░░░░░ ░│
                     ─┘ │                                          •                   •       ─┐─┐─┐─┐─┐─┐─┐
                        └─────────┐───░░ ░░░── ┌───  ░ ░░░░░• ░ ░──░░░░░░░░░░░──░░─── ░░•░──── ░│ │░│ │░│ │░│
                        │░░░░░░░░░│ ░░──────░░ │░░░░────────░░───░░────────── ░░ •░ ░ ──░• ░░░░─┘─┘─┘─┘─┘─┘─┘
                         ────────  ───      ─── ────         •   ──           ──  ──    •  ────

















































```

*Figure from page 5 (2346x3317 px)*


---



4203-E P-282



SECTION 2 PROGRAM OPERATION



15-1-3. Command Execution



(1) To Execute a Command



To execute the command that is currently displayed fn lines 4 to 7 of the command creation screen,



press the WRITE key. The screen will revert to its original condition and the command will be



executed.



The created command will be saved as the "command history".



(2) To Abort Execution of a Command



To abort execution of the command currently displayed in lines 4 to 7 of the command creation



screen, press function key [F7] (CANCEL). The screen will revert to its original condition and the



command will not be executed.



The created command wfll not be saved as the "command history".



Command creation screen



lfl9CUWf ~rn1t



I<»-••··~'I!



UU:X O!SPU.Y ~



ff2l -> 11»:•,11n1



CFJl->f't:0!•,1111t



11l O!Sl'\J.Y 01"8< INleliES.lfte> l'<ESSIIIG IF\),



IIFIJT H ce.rrce IIME NI) FltE JWE, UiEN PRESS (fRJ TEJ 1(£Y.



OEFMA.'f' DEVICE M.ti1: - 11)1:



OEfMA.T Fil.£ fWIE - "'.MIN



Original screen ,



11;:.:..



'fMiD


# I= l"1: Io:= I

t'MIC8.



l /!~



(!'BU.T~(t(



"""'



Command is executed



:!:!:.S!;~~Hl,R:C!



'- ,;;;;--_,. f '"""'


# I I I

I - •i;.,r



/i~~Ttl'.'1 """""'



Command is not executed



"- l'EAI)



I""°' lvei,FVI-


# I I

PIP



WIT



Fig. 2-3 Command Creation Screen


```text


                                                                                                ──       ──
                                                                         ─┐─┐─┐────┐─┐─────────░░░───────░░│
                                                                          │▒│ │░░░ │ │░░░░░░░░░ ── ░░░░░░──┘
              •  ──                  ──────────────────────────────────── └─┘─┘────┘ └─────────
           ┌── ──  ───────────┐──────                                                                      │
           │     ─┐          ░│      ──────────────────────────────────────────────────────────────────────┘
           └───── │ ┌─  ──  ──┘ ────
                  │ │ │   ─┐   │     ──────┐
                  │   │  │ │  ─┘──┐     ░░ └─
                      │  │        │          ────     ───────────── •       •     ─┐─       •    ─── •  ──
                      │  │        ░ ░░ ┌─┐       ────    ░   ░  ░  •   ───   ────  │ │   •░   • •░ ░•  •░░─┐
                      │░░░░ ░░░ ░░──── │░└───░┌─┐ ░░░• •░• ░ ░──── ░  ░░░░░│ ░░ ░░ │ │   ░ • •░░░░░ ░ •░──░│
                      └────┐───  •      •    ─┘ │  ──       ──       ────  │ ────── ─┘───── • ──────── •  •
                      │    │   ─┐  ─────  ─┐─  │ ┌─  ┌──┐──┐   •  ┌─┐    ─┐ •
                      │░ ░ │░░░░│  ░ ░░░│  │░• │ │░ ░│ ░│ ░│ │░░  │░│  │░░│ ░│
                  ┌─  │  ┌─┘ ─── ──── ┌─┘  └─   ─┘  ┌┘──┘──┘─┘────┘─┘──┘──┘──┘
                  │░│ │░ │░░░░░ ░░░░░░│ ░ ░ ░░░░ │░░│
                  └─┘ │  │            │              │   ───── ┌───────────┐──┐ ┌─┐─────┐─────────────────┐
                      └──┘─┐───────┐──┘───┐──────────┘───░░░░░─┘░░░░░░░░ ░ │░░└─┘░│   ░ │░   ░░░░░ ░ ░░░░░└┐
                      │    │       │      │   ░     ░░░ ░ ───┐  ────░ ── ┌─┘          •      ┌─    │ │  •░ │
                      │                          │   ─────   └──    ──  ─┘ │  ──   ──  •░ ───┘ ────┘ │   ──┘
                      │    │░   ░      ░ ░ ░  ░░░│                                      •     •     • ──
                      │    │              ──┐─┐   ───────────────────────────────
                       ─── └───── ─────  •  │ │           ░                    ░
                     •                               ──────── ── ───────────────
                     ░┌───────────────────────────
                      │░░░░░░░░       ░░░░        ────  ──
                    │  │░             ───          ░░     │
                    │  └─────────────     ─────────────   │
                    │                                   │ │
                    │  ┌───┐────┐                       │ │
                    │  │░  │▒ ░░│      •         ───────┘ │
                    │  │ ── ░░ ░└──░ ░░░  ┌─────┐       │ │
                    │  │░ ░░░░░░ ░░ ──────┘     │       │ │
                    │  └────────────       ─────┘       │ │
                    │ │                                 │ │
                    │ │                             ────┘ │  ┌─
                    │  ┌─┐ ┌─┐──┐───┐── ──┐─┐─┐────┐    │ │  │░ ──────────────────────────────────
                    │  │ │ │░│  │░  │▒░•░▒│ │░│  ░ │      │  │ ░░░░░░░        ░░░                 │
                     • └─┘─┘─┘──┘───┘─┐▒┌─┘─┘─┘────┘     •  │ ┌─────────────────────────────────┐ │
                                      │█│           ─────   │ │                                 │ │
                                      │█│                   │ │                                 │ │
                                   ── └─┘                   │ │                                 │ │
                                  ░░▒ │█└───────────────────┘ │                                 │ │
                                  ─── └─┘░░░░░░░░░░░░░░░░░░▒  │                                 │ │
                                      │█└───────────────────┐ │                                 │ │
                                      │█│                   │ │                                 │ │
                                      │█│                   │ │                                 │ │
                                      │█│                   │ │ ────  ──           •            │ │
                                      │█│                   │  │ ░░ • ░ ─────────── ┌─  ┌───────  │
                                      │█│                   └─ │░───░── ░░  ░      ─┘   │░       ─┘
                                      │█│                     ─┘              ───    •
                                      │█│                   │ ░░░░░░░░        ░░░░             ░ ─┐
                                      │█│                   │ ┌─────────────────────────────────  │
                                      │█│                   │ │                                 │ │
                                      │█│                   │ │                                 │ │
                                      │█│                   │ │                                 │ │
                                  ┌── │█└───────────────────┘ │                                 │ │
                                  │░░ └┐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓│ │                                 │ │
                                  └─── └────────────────────┘ │                                 │ │
                                                            │ │                                 │ │
                                                            │ │                                 │ │
                                                            │ │                  ──────     ────┘ │
                                                            │   ─────┐─────┐─┐──       ─┐─┐─      │
                                                            │  │░   ░│     │░│  │     • │░│ •    ┌┘
                                                               └─────┘─────┘─┼─┐┘      ─┘─┘─    ┌┘
                                              ┌───────┐────────              │ │ ──────     ────┘
                                              │ ░   ░ │░            ░    ░    │
                                              └───────┘───────────────────────┘













```

*Figure from page 6 (2346x3317 px)*


---



4203-E P-283


#### SECTION 2 PROGRAM OPERATION

15-1-4. Operation Transition



Use the file processing function keys (copy, delete, etc.)



AUTO Operation



Program Operation



MacMan



Command Creation


#### Screen

INDEX. Displays "ISO" at the console line.



FolJow;ng the ISO character string. enter the



device name then press the WRITE key.



[II)



MD1: INDEX .......... Displays MD1: Directories.



[ill



FOO: INDEX .......... Displays FDO: Directories.



[EI)



COMMAND HISTORY , . Displays the command log.



[ill



OVERWR/INSERT , , , . Switches the command editing mode,



[ill



CHAR DELETE . , . Deletes the character indicated by the edit point8f.



[1IJ



CANCEL , , . , .. , Cancels the creatoo command.



WRITE •



I ...



Executes the created command.



When ttie device Is OSP formatted:



Directory Selection


#### Screen

I]]]



RETURN .. , ,



III]



CANCEL ... ,



WRITE



. Far device name selection only.



.. Cancels the selection.



. For selection of device name and file name indicated by cursor.



Command H lstory



Screen



CAN



... , . , ........ Same as (F7] (CANCEL).



When the device is MS-DOS formatted:



[II)



RETURN .. , • . . . For selection of device name and current directory only.



CT:IJ



CANCEL . , ... , , , , ..... Cancels the selection.



f WRITE



I .. ,. ..........



If cursor is at the directory name, a directory change occures.



lf cursor is at the file name, selection of the device name,



current directory name. or file name occurs.



CAN Same as [F7] (CANCEL).



III]



CANCEL ... ' ' ' .. ' . . . . . Cancels the selection.



WRITE'



I ....



Selects the command indicated by the cursor.



CAN



I ...



Same as [F7] (CANCEL).


```text


                                                                                                ───       •
                                                                          ┌─┐───┐──┐──┐─────────░░░░──────░•
                                                                          │░│░░ │░░│  │░░░░░░░░░──░•░░░░░░•░
                  •         •         ────────────────────────────────────┘─┘───┘──┘─ └─────────     ───
           ┌──  •  ┌───────  ────────                                                                       │
           │░   ░┌─┘        •        ┌──────────────────────────────────────────────────────────────────────┘
           └─────┘ └──────── ────────┘
                                           ┌┐  ┌─────────────────────┐─┐────┐         ───────┐
                               ─────────┐──┘┘┐ │    ░                │ │    │                │
                            ───         │    │ └─────────────────────┘─┘────┘         ───────┘
                         ┌─   ░░░░ ░░░░░│  │ │                                               │
                         │  • ─────────┐   │ │                                               │
                       ──┘ │ •         │   │ │                                               │
                         │░│           │░│ └─┘                                               │
                       ┌─┘ └───────────┘ └─┘                                                 │
                       │ │             └─┘                                                   │
                       │                   ──────────────────────────────────────────────────┘
                       │
                       │               ──────
                       │         ──────      ┌──┐───────           ┌────────────────
                       │                     │  │░                 │░▒░ ░░ ░░░░░░░░░───     ┌──────
                       │      ─┐ │  ─┐──────┐   │                 ┌┘ • ░ ┌──    ─┐──░  ░──┐ │
                       │       │░│ │ │░░░░  │   └──┐──┐─┐──┐      │░░   ░│       │   ──   └─┼──     │
                       │      ─┼─┘ └─┘──────┘─  │░░│  │ │░ │  ─┐  │ ░    │ •     │       ─┘ │  ─┐   │
                       │       │  •             │ ░│ │░░ ░  •  │  │       •     ░└────┐         │   │
                       │        •               │░░│ │░│ ░ ░░┌─ ──┘░         ░    ░  ░└───┐─────┘   │
                       └─   ────                │░░│ │ │ ░───┘ │░ │           ░     ──    │     │   │
                                             │  │░░│  ░ ┌─     └──┘                │   ───┘     │   │
                             ────────────────┘─ └─░░░───┘         └───────── ──────┘            │   │
                                                  ───                       •                   │   │
                                 ────────────                                       ────────────┘   │
                                •                                                               │ │ │
                               │ │                                                                │ │
                               │ │  │                                                              ─┘
                               │  • └─┐                           ───────                    ──────
                               │ │  │ └──           ┌─ ░ ──┐─┐────░    ░ │    ───    ───────┐
                               │ │  └─┘   ───   ──┐ │  • ░░│ │░   ┌──────┘ ┌──   ────       │
                               │ │    ░• │  ░ ░   │ │ │ ── │ │ •░┌┘        │          •     └──────┐─────────┐
                               │ │  ──┐ ─┘────────┘ │ │   •░─┘  ─┘         │  │  │     •           │░        │
                               │ │    │             │  ┌─  ░░░•   ─────────┘ ─┘──┘─────░───────────┘─────────┘
                               │ │    │ │            • │  ░ •
                               │ │      └──────────── ─┘ • │      ┌──────── ──────   •  ─────────────────
                               │ │                      │░░└──   ┌┘        │      ─── │
                               │ │                      └─░░ ░  ┌┘         │       ░ ░└──────────────────┐─
                               │ │                        ──────┘          │  ░ ░  ░──┘░░  ░░░░ ░░ ░░░░░░│
                               │ │                                         │            ┌────────────────┘─
                               │ │                         ░░              └───  ──     │
                               │ │                      ─────────              ──  ─────
                               │ │     ┌─────────────
                               │ │    ┌┘              │ ┌──   ────           • ──  ──
                               │ │    │            ─┐ │ │░ ───░░           ┌─ •  ─┐░ ──────────────┐
                               │ └────┘ │ ─┐──────┐ │ │ └─░░░░  ──         │      │                │
                               │      │ │  │░░░░  │ │ │   ─────            │ ─────┘─ ░ ────────────┘
                                 ─────┘ │ ─┘──────┘ │ │                     •       ───
                                      │ │           │ │
                                       • ───────────┘


























```

*Figure from page 7 (2346x3317 px)*


---



4203-E P-284



SECTION 2 PROGRAM OPERATION



15-2. Creating and Editing Commands



15-2-1. Command Creation Screen



Lines 4 to 7 The command is created and edited here.



Characters keyed in are entered at the position of the edit pointer. When a character



is entered, the edit pointer moves to the next character space.



The downward-pointing arrow



Lines 9 to 15



'T' indicates the end of the command. Up to 255



characters can be entered.



The character string being entered to create a command can be modified by moving



the edit pointer with the cursor keys.



The procedure for displaying directories is shown below.To display a directory, press



one of the following function keys:



[F1} (INDEX), [F2J (MD1: INDEX), [F3] (FOO: INDEX)



[F2]



MD1: *.MIN



If the [F2J (MD1: INDEX) key is pressed, the directory of MD1 related



files (machining



programs) with an extend name of "MIN" will be displayed.



[F3] _.., FD0: *.MIN



If the [F3] (FD0: INDEX) key is pressed, the directory of the "FD0" floppy



disk



files (machining programs) with an extend name of "MIN" will be



displayed.



PROGRAM OPERATION TRANSFER



COPY OVERl'iRITE jcol



Command created {



and edited here



'EDIT POINTER



INDEX OI S PLAY PROCEDURE



[F2J


#### MOl :*.MIN

[F3]



FOO:*.MIN



TO DISPLAY OTHER INDEXES.AFTER PRESSING [Fl).



INPUT THE DEVICE I/Al£ ANO FILE NAME, THEN PRESS [WRITE) K::c!'.



DEFAULT DEV I CE NAME = Mill :



DEFAULT FILE NAlE



*.MIN



Fig. 2-4 Command Creation Screen



EDIT MODE


```text


                                                                                                •         ─┐
                                                                         ┌──┐──────┐─┐──────────░░───────┐░│
                                                                         │░░│░░░░░░│ │░░░░░░░░░░──░░░░░░ └─┘
               ────         • •          • ────────   ─────────────────── ──┘──────┘ └─────────      ───
           ┌───    ───────── • ──────┐──  │        ───                                                      │
           │   ░┌──               ░ ░│    │           ──────────────────────────────────────────────────────┘
           └────┘  ┌───────────── ───┘──░─┘─     ░   •
           │    │  │             •          ─────────
           │  ░   ┌┘ ░ ░░░ ░   │░░░──░░░░• •
           └───── │    ────────┘───         ──    ────┐─      ───  ─┐
                  │ │ │             ────────░ ────  ░░│ ─────┐ ░ ── └──────  ───  ─── ────┐─┐─┐────────────┐
                  └─┘─┘─────      │░░░ ░░░░░ ░░░░░ ░│░│ ░░░░░│░░░ ░░│░ ░░ ░── ░ ──░░ •░░░░│ │░│       ░ ░ ░│
                                  │░┌───────────────┘─┘──────┘░─────┘─── •    • ░░   ░░───┘  ─┘────  ────  │
                                  │ │                                            │    │    •       ┌─    ┌─┘┐
                                  │░└─────────────────────  ░•     ░░░░░│ │ ─────┘───┐┘ ░░░░ ░░  • │░│ ░ │░░│
                                  │░░░░░░░ ░ ░░ ░░ ░░░░░░░         • ── │ └─         └┘ • •  •  │  └─┘┐  └─┐┘
                                  │░ ─┐─     ░│           ────────      └─           │   •    • │     └──  └┘
                                  │ • │░░  ░──┼─░ ░░░░░ ░░░ ░     │ ────┘    •  ──── │      •  •      │    ░│
                  ┌───┐─┐─┐─┐─┐   │   │       │ │             •  ┌┘─     ─┐─┐ ┌─    •  ────┐      • •
                  │ ░░│ │ │ │░│   │░  │░ ░░░░─┘─┘──┐─░░░•░░ ░•░░░│░░░ ░ ░ │░│ │░░ ░ ░ │░░░░│ ░ ░ ░░░░│ │░░░│
                  └───┘─┘─┘─┘─┘   └──  ──────░░░░░░│░──┐░┌──┐░───           │ │      ─┘────┘─────────┘─┘───┘
                                     ─┐          │     │ │  └┐    ── ───────┘─ ─────
                                      │ ─┐ │  ░──┘ ░ ──░│    └──░    ░ ░ ░      ░ ░ ░•
                                      │░░│ └─┐░░░└── ░░░│               ──        •
                                       ──┘   └── │    •  ┌─  ────────┐─┐  ───────┐ ┌──┐────      ───┐─┐─────┐
                                   ──        │   │ ──  ──┘    ░ ░    │░│   ░░░░░░│ │░ │░░░░──────░░ │ │░░░░░│
                                   ░░────────┘─            ──     ┌── •      │  ─┘─┘  └───░░░░░  ░──┘─┘─────
                                  ───░░░░ ░ ░░░──┐ ░░░──░ •░ ░ ░  │░░• │░ │░ │░░░░░░░•     ──────
                                     ───░────── ░│ ──░░░   •      └──  └─ └─ └─────
                                                 └─     ──┐ ┌─┐──┐   ┌─  •  •      ───────┐─┐──┐───┐─┐─┐───┐
                                  ┌──┐        •░│░ ░░░──░░│ │░│░░│ •░│ ░░░░░░░░  ░░ ░ ░░░░│ │░░│   │░│ │░░░│
                                  │░░│       │  └─┐      •  └┐┘── • • ┌─┐ ┌─┐─── ── ─┐─┐   ┌┘┐─┘┐── ─┘  ┌─ │
                                  │  └────┐  │░░│ │░░░░░░ ░│ │░░░ ░░ ░│ │░│ │░  │░░░░│ │░░░│ │  │░░│  │░│  ░│
                                  │░░░░░░░│  └──┘─┘────────┘─┘────────┘─┘─┘─┘───┘────┘─┘───┘─┘──┘──┘─ └─┘───┘
                                  └───────┘

                                                │  │░░░░░░░░░░░░──────────░ ░░░░░──────────────────────┐  │
                                                │  └────────────▒▒▒▒▒▒▒▒▒▒───────▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │
                                                │  │▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓•▒─────▓─┘  │
                                 ┌──────────┐───   └────────────────────────────────────────── •░    • ░  │
                                 │ ░  ░    ░│                                                             │
                                 └──────────┘──   │      ──        ┌─                       │    ░ ░░│    │
                                                │ │ ┌─┐─┐  •       │                        └────────┘──  │
                                                │   │░│ │  ░• ░░░──┘              ──────────            │ │
                                                │   └─┘ │ │░░ ──░                                       │ │
                                                │  │   ─┘ └─ ░   ─────────────────┐─┐──────┐            │ │
                                                │  │░░  │░ ░░░  ░░ ░░ ░░ ░░░ ░░ ░░│ │░     │            │ │
                                                │  │░    │░ ░ ░░░──┐░  ───────────┘─┘──────┘            │ │
                                                │   • ░• └───┐░──  └─░│                                 │ │
                                                │ │  ── •    └─      ─┘                                 │ │
                                                │ │                                                     │ │
                                                │ │                                                     │ │
                                                │ │                                                     │ │
                                                │ │ •   ───     ──       ── ───    •     ──     ─┐───── │ │
                                                │ │  ┌─┐   ───┐─  ──┐─ ──░░│ ░░───  ────┐  ───┐─ │      │ │
                                                │    │░│    ░░│    ░│  ░░░░│ • ░░░   ░░░│   ░░│ ─┘      │ │
                                                     └─┘   ───┘─  ──┘── ───     ────────┘─────┘─        └─
                                               ──┐───   ───     ──          ──                   ───────
                                                ░│      ░░░░░░ ░  ░░░░░│ │░░░░│
                                              ───┘─────────────────────┘─┘────┘






















```

*Figure from page 8 (2346x3317 px)*


---



15-2-2.



4203-E P-285



SECTION 2 PROGRAM OPERATION



Operation of the Edit Pointer



(1) Moving the Edit Pointer to the Right



The edit pointer will move one space to the right every time the right cursor key is pressed.



When the edit pointer is at the right end of a line, pressing the right cursor key will cause it to move to



the left end of the next line, unless it is on the final (7th} line, in which case it will not move.



(2) Moving the Edit Pointer to the Left



The edit pointer will move one space to the left every time the left cursor key is pressed.



When the edit pointer is at the left end of a line, pressing the left cursor key will cause it to move to the



right end of the next line, unless it is on the uppermost (4th) line, in which case it will not move.



(3) Moving the Edit Pointer Downward



The edit pointer will move one line downward every time the "down" cursor key is pressed, unless it



is on the final (7th) line, in which case it will not move.



(4) Moving the Edit Pointer Upward



The edit pointer will move one line upward every time the "up" cursor key is pressed, unless it is on



the uppermost (4th) line, in which case it will not move.



COPY OVERWRITE



~00


### ,oo,,..,,.,_ .,,_ ,,. ' •

'EDIT POINTER



COPY CVER!IRI TE



Fig. 2-5 Operation of Edit Pointer


```text


                                                                                                ───       •
                                                                          ┌─┐───┐─┐───┐─────────░░░░─────░░│
                                                                          │░│░░ │░│   │░░░░░░░░░ ───░░░░░░─┘
                 ┌─        ───              ───────────────────────────── └─┘───┘─┘───┘─────────     ──
           ┌─────┘ ┌──┐─┐──   ──────────────                                                                │
           │     └─┘  │ │                   ────────────────────────────────────────────────────────────────┘
           └─────┘  •    ──        ──      •
                 │   ─┐─   ┌─ ─────   ────  ──┐───┐───
                  • • │  │ │░│   ░ │      │ ░ │ ░ │░░ │
                   •   │ │ │ │   ──┘ │  ──┘   │   │ • └┐─┐──────┐─┐────────────┐─┐────────┐───────────┐
                       └─┼─┘ └┐──  └─┘     ───┘   │  ─┘┘ │    ░░│ │       ░    │░│        │      ░ ░  └┐
                      │░░│    │       •   •      │  •  │         •        │ │             │       ──   └─────
                      └┐                         │ •            •   ░     │ │░ ───   ──             •
                       │░───────────┐─ ░░• ───── └─░░ •░ ░░ ░░   ░░──░░  ░│ └─ ░░░░  ░░│ ░ ░│ │░ ░░░ ┌──────
                  ┌─┐ ┌┘            │     │          • ────────────  ─────┘─  ─────────┘────┘─┘──────┘
                  │░│ │░░░ │░ ░░ ░ ░ ░ ░░░│ ░ ░ ░  ░│
                  └─┘─┘┐ │ │         │ ┌─       │   └──────┐───┐────┐─┐────────┐─┐───┐─┐─┐──────────┐
                       │░└─┘░░ ░░────┘─┘ •░░░ ░░└┐─░░░░   ░│  ░│ ░░░│ │░░  ░░ ░│ │░░░│ │░│ ░ ░░░░░░░│
                       │                         │                        •                         │ • • ──┐
                       │ │ ── ░    ░   ░ ──    ──┘       ░  ░ ───────░  ░•░░──  ░  •░░░░ ──░░░──   ░░░░•░  ░│
                       └─┼─░ ░────────── ░░────░░░──── │░─┐░• ░░░░ ░░───░░░•░ ────░░─────░░───░░───────░░───┘
                  ┌─┐ │  │                │           ─┘─ └─ ───────    ─── ──     •     ──    •        •
                  │░│ │░░│ │░ ░░ ░ ░ ░░░░░│ ░░░░ ░░░░•
                  └─┘ │  │ │   │     │    │           ──── • • ──────────┐─┐───┐─────────┐─────────┐─┐──────┐
                      │░░░ │░░░└──░──┘░ ░░░░  ┌─── ░ •░░ ░░░░ ░░░░░ ░░░ ░│ │░░░│  ░░░░░ ░│ ░ ░░░░░░│ │ ░░░░ │
                      │░───┘───░ ░• ░░┌───┐───┘░░░───░────────────  ─────┘─┘───┘─────────┘─────────┘─┘──────┘
                  ┌─┐ │               │   │                       ──
                  │░│ └────┐─┐   ░   ░└─  │ ┌─    │
                  └─┘─┘    │░│            └─┘     └┐─ ────┐────────────── ──────────────────────────────────
                      │░ ░ │░└─░ ░░░ ── ░░     ░ ░░│ │ ░  │      ░                                 ░
                      │ ┌─     │                   │ │                ──────────────────────────────────────
                      └─┘ │   ─┘               ░           ░
                        └─┘───  ── ───────────────────────────────────────────┐─────┐─┐
                                  │▓▓▓████████████████████████████████████▓██▓│▓▓▓▓▓│█│
                                  └───────────────────────────────────────────┘─────┘─┘
                                  │                                                    │
                                  │           •  ──┐   •            ┌─┐                │
                                   ──    ──┐   ──  │░│    ──────────┘░│     ┌─── ──────
                                      ┌─░▒▓│       │░│              │░│   │ │▓▒░
                                      │ ░──┘       │░│              │░│   │ └┐───
                                                   │░│              │░│   └─░│
                                                   │▒│              │░│
                                  ┌──┐─────────────┘─┘──────────────┘─┘───────────────┐
                                  │▓▒│▓▓█▓█▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓│
                                  └┐─┘────────────────────────────────────────────────┘
                                 │ │                                                   │
                                 │                 ┌─┐              ┌─┐                │
                                   ──   ┌─┐  ┌─────┘░└──────────────┘▒│ •   ┌─┐
                                     ┌─ │█│  │     │░│              └─┘  ┌─ │█│
                                     │  └─┘  │     │░│              │░│  │░ └─┘
                                       •           │░│              │░│
                                                   │▒│               ░
                                  ┌────────────────┘─┘────────────────────────────────┐
                                  │▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒░▒▒▒▒▒│
                                  └──────────────────────────────────────────────────┐┘
                                 │                                                   │ │
                                 └┐                                                  └─┘
                                  └────────  ── ──────┐─┐─────┐─────┐─┐─────── ──────
                                               │░ ░ ░ │ │░░░░░│ ░ ░ │░│ ░░░░░░│
                                               └──────┘─┘─────┘─────┘─┘───────┘






















```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-286



SECTION 2 PROGRAM OPERATION



15-2-3. Editing Modes



Lines 4 to 7 of the command creation screen have two editing modes, function key [F5J



(OVERWR/INSERT).



Immediately after displaying the command creation screen, the overwrite mode will be effective.



(1) Overwrite Mode



The overwrite mode is used to fix the command displayed in lines 4 to 7 of the command creation



screen in order to overwrite a character or characters in the command.



In the example shown below, ''1" is entered at the position of the edit pointer and the edit pointer



moves to the posrtion of the next character":". Note that in this case none of the characters has



moved.



OVERWRITE MODE



COPY OVERWR 17:



r ""'""""·"" ~



EDIT POINTER



COPY OVERl\"R I TE



Fig. 2-6 Editing Modes (Overwrite Mode)



(2) Insert Mode



The insert mode is used to insert additional characters into the command displayed in lines 4 to 7 of



the command creation screen.



In the example shown below, the character string to the right of the edit pointer - "AM.MIN" moves



to the right to accommodate the character "R" as it is inserted at the left of the edit pointer.



INSERT MOOE



COPY INSERT



,OOC,tU,iM,M" I



"EDIT POINTER



COPY INSERT



Fig. 2-7 Editing Modes (Insert Mode)


```text


                                                                                                ──       ──
                                                                         ┌───────┐───┐─────────░░░───────░░│
                                                                         │░░░░░░░│ ░ │░░░░░░░░░ ── ░░░░░░──┘
                ──             ──────────────────────────────────────────┘───────┘───┘─────────      ──
           ┌────   ───┐──┐─────                                                                            │
           │░     │░ ░│  │░  ░                                               ───        •    ──────────────┘
           └───   │       │    │  ──────────────────────────────────── ──────   ────   •  ───
               •  │░• ┌─┐─┘────┘──           ░        ░            ░  •                 │ ░  │
                │   ░ │ │        ░ ──────────────────────────────────┐ ─────────────────┘ ───┘
                │     │   ┌─┐ ░  •                                   │
                │  │  │   │ │░┌──   ───── • ───  ────────────────────┘──────────────────────────────┐
                └──┘─  ───┘ └─┘         ░      ──                 ░        ░   ░       ░   ░ ░ ░ ░░ │
                │    ─┐   └─┘  ┌──  ┌────     •  ────   ───────────── ──────────────────────────────┘
                 • •  │      ░ │░  ░│
                  •          ──┘     ───      ── ┌─  •  ──────    ──────             ──────┐─────────┐─┐───┐
                      ─────     ──┐     ─────┐  ─┘ ── ──     ░──── ░ ░░  ┌─── ─────┐  ░ ░░ │░ ░░ ░ ░ │░│░░░│
                     │░░ ░░─── •░░│ ┌──░░░░░░└── ░ ░░░░░──────░░░░───────┘  ░•░░░░ └─    •    •  •   │ └── │
                     │            │ │                                                • ──  ─── •   •  •
                      ───┐───░░░░░└─┘──░│  ░░░░ ───────────┐ ░ ░┌─── ░•░───░•░░ •░│ ░░░░░ │░░░ ░───░──░░░░┌┐
                     •░░ │░░ ─────░░░░░─┘────── ░░░ ░ ░░░░░└─── │░░░──░• ░ ░░──░░─┘───────┘─────░░ •░░ ───┘┘
                      ───┘───     ─────        ────────── •      ───     • ──                    •   •
                                                                              ───       ──
                                                                               ░░░• ░ │░░░│
                               ──────────────────────────────────────────────────  ───┘───┘
                              •▒▒▒▓▓▓▓▓▓▓▓▓▒▓▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒│
                               ───────────────────────────────────────────────────┘
                                                                                   │
                                     │    │  ░                                   │ │
                                     └────┘──────     ──        •                │ │
                                                 ────┐  •   │ │  ────────────────
                                                     │ │    └─┘ │
                                                       │      ░─┘
                                                     │░│
                              ┌──────────────────────┘─┘─────────────────┐───┐─┐──┐
                              │▓▓▓█████████████████████████▓▓████████████│▓▒▒│▓│██│
                              └──────────────────────────────────────────┘───┘─┘──┘
                             │                                                     │
                             │                                                     │
                              ────────── ── ──────┐─┐──┐───┐───────────────┐────┐──
                                           │░░░ ░ │ │░░│ ░ │░░░░  ░░░░ ░ ░ │░ ░░│
                                           └──────┘─┘──┘───┘───────────────┘────┘
                 ┌─┐ ┌─────┐─┐──┐
                 │░│ │░░░░░│░│░░│
                 └─┘ │           ───   ────────────┐─────────────────┐─┐──┐─┐────┐────────────┐─┐──┐─┐─────┐
                      │░░ •░░░──░░░░───░░░ ░ ░░░░░ │░░░░ ░░ ░░░░░░░░ │░│ ░│ │░░░ │░ ░░░░░░░░░░│ │░░│ │░    │
                      └─── ───  ────  ░ ───   ░────┘──── ── ──────── └─┘ ─┘ └─── └──────────       └─┘──   │
                     │                                  •  │        •   •  •    •           ┌─────┐     ───
                     │░ ░░ ░░•░░░░ ░░░░░──░░─┐ ░ ░ ░░░░░░░ │░│ ░ ░ ░░  ░░   ░   ░░ • ░░ ─┐ ┌┘░ ░░░└─
                     │ ─────┐ ┌───  •  •     │ ░───        │░│    • •                    │ │  •  •    ──────
                     │      └─┘   •  ── ─────┘──    ───── • • ────   ── •                  │ • │    │
                                                                                 ░     ┌───┘─  └────┘
                                                                             •        ─┘
                                ┌────────────────────────────────────────────▒░░───┐
                                │▒▒▒▓▒▓▓▓▓▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░•░▒▒▒▒└─
                                └────────────        ──────────────────────── ─────
                               •             ░  ░ ░
                                •         ──────────── ┌─┐ ┌─
                                 ─────────             │░└─┘
                                                       │░│ │ ───
                                                       │░│ │ ░ ░
                                                       │░│
                                ┌──────────────────────┼─┼──────────────────────────┐
                                │▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│▓│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓│
                                └──────────────────────┘─┘──────────────────────────┘
                               │                                                     │
                               │                                                   • │
                                ───────────── ──┐────────────────┐─┐──────┐───┐     •
                                             │░░│ ░   ░░░░░ ░░░░░│ │░░░░░░│░░░│
                                             └──┘────────────────┘─┘──────┘───┘













```

*Figure from page 10 (2346x3317 px)*


---



4203-E P-287


#### SECTION 2 PROGRAM OPERATION

(3) Switching between Editing Modes



To change the editing mode, press function key [F5} (OVERWR/INSERT). If the overwrite mode is



currently effective the insert mode will become effective, and if the insert mode is currently effective



the overwrite mode will become effective.



liiiii!fffilt:!!t



l....~---•---



INlEX l'.liSP!..AY ~



tF?i -;:,, 11cn;•.111N



:FJJ -;. FDCr.•.¥1!f



0'.S!f!IU



OVERWRITE MODE



11()£}:; OIP..A1" ~



(P:2! -> l()i:"'.t.llN



(Fl!



;::',.ti:'",lllllt



to or5?!.J.'I' O:H.€R I~. .. ~ F'RESS1HG [!='l,J,



USSEB!



INSERT MODE



i'O O,l~Y 0~ 1flU.X$.k"1c'R ~SStHO; [Fl],



Uf'VfirECEVIQ: ~ N(l ;:Jlf~.MN~ {11Jli7i,~ ~.



t;JEF'JULT O&lai ~ - El;



l!FU1' Tt!C :;E'nt::E fWIE UC Fi LE MME:.ike'H PRESS (J1Rr-:1'.J ,::g,



OEFAIA.T OC.IICE. !WE .,,, 101:



eEFJi!Jl.T FU.I MIIE - •.vnc CEFAI.\J" Fl~:1 ~ - •.itlN



Fig. 2-8 Switching between Editing Modes



15-2-4. Deleting Characters



(1) Function Key [F5] (CHAR DELETE)



Use of this key deletes a single character atthe position of the edit pointer, whereupon the character



string to the right of the deleted character shifts one place to the left to close the space. The edit



pointer remains at the same position.



In the example shown below, the character "A" located by the edit pointer is deleted and the



character string ":PROGRAM.MIN"tothe right of the edit pointer moves one place to the left to close



the space.



CO?Y OVERWRITE



r"·-""



'\_ EDIT POINTER



(CHAA DELm)



C0°Y OVERWR IT£



Fig. 2-9 Deleting Characters {Function Key [F5])


```text


                                                                                                ───       •
                                                                          ┌─┐───┐─┐───┐───┐─────░░░░──────░│
                                                                          │░│░░░│░│   │░░░│░░░░░ ───░░░░░░─┘
           ┌──────   ──       ──                     ─────────────────────┘─┘───┘─┘─  └───┘─────      •
           │      ┌─┐  ───────  ┌─────────┐─────┐────
           └──────┘░│ │░        │       ░ │    ░│                                     ──    ──   •
                  └─┘ │   ──────┘    ─┐   │ ┌─ •    ──────┐───── ─────────────────────  ┌──┐  ─── ──
                      │░ │░ ░   │░░ •░└── ░ │░│ •        ░│     •░    ░ ░░░ ░░ ░  ░   │ │  │        •   ──  │
                      │  └──   •░     │       │                                       └─┘  └──        ──  • │
                      └┐     ░   ░      ░ •░░░    ░░ ─┐  ░ ░  ░ ░░░░░░░ ░░░ •░░ ░░░░░ ░░░░ ░ ░░░░ ░░ ░░░░░░░│
                      └┘░ ░░░░░░░───░░░  ░░ •░░░░────░│░░─────────────────── ───────────────────────────────┘
                       └─────────   ──────── •
                                               ┌─────────────────────────────────────
                                             │▒│░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
                            • •   •   •      │█└────────────────       ─────────  ──▒└─
                         ┌─┐░•░─── ─── ──────                    ──────         ──  ░░ ────    ───┐
                         │░│░░░░░       ░░░░                │   ░░░░░░░░       │░░░        ──┐─   │
                         └─┘────────────────┐        ░░░┌┐  │   ───────────────┘──── │ ─── ░░│     │
                                            └┐  ░░  ────┘┘  │ │                      └┐   ░──┘     │
                         │ ┌─┐────           └──────        │ │   ───────┐            └────   ── │ │
                         │░│ │░  ░──                      │ │   │░ ░░░░░░│                      ─┘ │
                         │░│ │░░ ░░ ─┐─ ─────┐─────┐      │ │   │    ░   └─────────┐──────       │ │
                         │░  │░░ ░░  │ •░   ░│     │      │ │   │░ ░  ░ ░░░ ░ ░░░ ░│      │      │ │
                         └───┘─░░────┘─  ────┘─────┘      │  │  │░│  │░░───────────┘──────┘      │ │
                        │      ──                         │  │ │ ─┘──┘──                         │ │
                        │                                 │  │ │                                 │ │
                        │     •                           │  │ │                                 │ │
                         ┌────░─────────────────┐───┐─────   │  ┌─┐──┐─┐─┐──────────────────────┐  │
                         │░░   ░░  ░░ ░░░░ ░░░ ░│░ ░│      ┌─┘┐ │░│  │░│ │▒░░░░░ ░░░ ░░░ ░░░    │ ┌┘
                         └───┐ ──░ ─── ─┐░ • • ─┘───┘──   ─┘  └─┘─┘──┘─┘─┘───── ░   ░ ──────     ─┘
                             └─  ──     │   ░░•                                  ░░──┐      ─────
                                         ────▒░──────────────────────────────────── █│
                                             ──▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┌┘
                                               ─────────────────────────────────────┘

                                            • ░     │                     ░     ░│
            ─────   ─────  ┌─    ──           ───   └─────────────────── ────────┘
           │     • •     ──┘ ────  ─┐
           └───── │ ┌┐              └┐
                  │ └┘┐              └────────┐─┐──┐──
                  │   │    ┌────░░  ┌┘     ░  │░│  │  •    ──           ──
                      │    │    •   │   │     │         │ •  •  ────── •  • ┌───  ────┐───── •    ┌──   ──
                      └─ •         •    └── ──┘──  ─────┘─    ─┐      •     │         │        ───┘   •   ─┐
                      │░░░░ ░ ░ ░  ░  ░ ░ ░ ░░░░░░ ░░░ ░░░  │░░└──░░ ░░░░ ░ ░ ░ ┌─ ── ░░░  ░• ░░░░└───░──┐░│
                      └──────┐─────┐─┐───────────────────   └──┘  ──     ────  ─┘     ────── ──       •  └─
                      │      │     │ │                   ───         ────    ┌─  ─────         ────  │  •
                      └──────┘── ░░└─┘░───────────── ───░░░░───────░░░░░░────┘░──░░  ░░░░─── ─┐░░░░──┘░  ░ │
                      │░░░ ░░░ ░───┘ └─░░░░░░░░░░░░░ ░ ░───░░░ ░ ░░ •░── ░  ░    ──  ────    ░└──── ░ ──░  │
                      │░┌─  ──┐─    •  ────────────    •   ──── ───      ────  •         ─────     ───  ───┘
                      └─┘ •   │
                           ───   ┌───────────────────────────────────────────────────
                                 │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒
                                 └───────────────────────────────────────────────────
                                │                                                    │
                                │ •      ░░░ │░░░░░│            ──                 │ │
                                 • ──   ─────┘─────┘─── │         ────────────┐    └─┘
                                                        │   ─────  ░ ░░ ░░ ░ ░│ ───
                                                       │ │   ░ ░ ─────────────┘
                                                       │ │     ░
                                                ────── └─┘─
                                 ┌─────────────▒▒▒▒▒▒▒•▒▒▒░─────────────────────────┐
                                 │▒▒▒▓▓▓▓▓▓▒▓▓▒──────▒▒▒──▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒│
                                 └┐────────────           ──────────────────────────┘
                                │ │                                                  │
                                │ │                                                  │
                                   ─────┐──┐─┐───┐───────────────────────────────┐──┐
                                        │  │ │ ░ │░░░░░░░░░░░ ░░░ ░ ░ ░ ░░░  ░░░ │░░│
                                        └──┘─┘───┘───────────────────────────────┘──┘














```

*Figure from page 11 (2346x3317 px)*


---



4203-E P-288



SECTION 2 PROGRAM OPERATION



(2) BS Key (Backspace Key)



Use of this key deletes a srngle character to the left of the edit pointer and causes the character



string that starts at the position of the edit pointer to move one place to the left to close the space.



In the example shown below the character "N' to the left of the edit pointer ls deleted and the



character string ":PROGRAM.MIN" that starts at the position of the edit pointer shifts one place to



the left.



COPY OVERl'lfl I TE



f"-'""""'"''



"EDIT POINTER



COPY OVERWA ITE



[C O ""'8 """"· M< I



Fig. 2-10 Deleting Characters (BS Key)



15-2-5. Notes on Creating and Editing Commands



(1) Maximum Command Length



The downward-pointing arrow symbol



"f'



signifies the end of the command and the maximum



command length of 255 characters is reached when this symbol is at the right end of the seventh



line.



When the "insert" editing mode is effective, it is not possible to key in a character at any position



when this limit has been reached.


```text


                                                                                                •         •
                                                                         ┌──┐──────┐──┐─────────░░░───────░│
                                                                         │░░│░░░░░░│  │░░░░░░░░░───░░░░░ ░─┘
           ┌──────  ──                       ──────────────────────────── ──┘──────┘  └────────      ──
           │      ──  ──────┐─┐─┐────────────
           └──────  ┌─ ░░ ░ │ │░│        ░   │                            •   ──     •      •      •
                  ──┘ │     └─        ─┐     └─ ─┐─ ────── ───┐─ ─┐─┐────┐  ─┐  ───┐┐ ────   ─────┐  ──────
                      │ ░│ ┌┘░░│ ┌─┐ │░│░░•    • │ •  ░  ░│   │░│ │░│   ░│ │ └──  ░└┘     ───     │ •      │
                      │ ─┘ │░ ─┘┐┘ │ └─┘┐─  •   ░       │ │     │        │ │         │   •         •   ─── │
                      │   ░ •   │░░│    │  │   ──  ┌─┐░ └─┘ ░   │ ░ │   ░│ │░ ░░░░ ░ │ ░ ░░── ░ ░░ ░░  ░░░░│
                      │ │░         │ │ •   │     │ │ │              │    │ └─      •      │   │          • │
                      │ │   ──  •  │ │   ░• ░ • ─┘ │      │ ────────  ───┘─  ────░  ──   ░└───┘░  ░ ───── ─┘
                      │░░░░░░░  ░░░░  •░░ ░░•░░░ ░░░░──░│ │░░░ ░░░░░   ░░░░ ░░ ░░ •░░ ░░░░│ ░░░░──── ░░░░░ │
                      │░───░─────────  ───── ───────   ─┘─┘──────────────────────  ─────── ─────    ───────
                       •   •
                                   ┌──────────────────────────────────────────┐─────┐──┐
                                   │▓▓▓███████████████████████████████████▓▓▓▓│▒▒▒▓▒│▓▓│
                                   └──────────────────────────────────────────┘─────┘─┐┘
                                                                                      │ │
                                           │ ░   ░░        ┌─┐ •    ──────────────────┘ │
                                           └───────────────┘░│  ┌──┐                    │
                                                           │░│  │░ │  ┌────────────────
                                                           │░│  │░ ░│ │
                                                           │▒│  │ ──┘
                                                           │▒│
                                   ┌───────────────────────┘▒└────────────────────────┐─
                                   │▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▒▒▒│
                                   └──────────────────────────────────────────────────┘
                                  │                                                    │
                                  │                                                    │
                                   ──────────┐──┐─────────┐────────────┐─┐──┐───┐ ─────
                                             │ ░│       ░░│ ░░   ░░░░░░│ │░░│ ░░│
                                                        ──┘────────────┘─┘──┘───┘
           ┌────── ┌───┐─┐────────┐─┐───────────────────
           │░ ░    │░░░│ │   ░░░░░│ │ ░  ░░ ░   ░ ░░░░ ░│
           └───── │ ──  ┌┘───               ───┐────────┘
                  │░  │░│░░░ ░░  ░░░ ░░░░  ░░░░│
                  └── │                             ───      ─── •  ──        ──    • •             ── •
                      │ ────░░ ░░░░•░░ ░░─┐─────────░░░──────░░ ░░• ░░──────── ░───░░  ░────░────── ░░░░───┐
                      │░ ░░ ──────░░────░░│ ░ ░░░░░░─── ░░░░░─────░ ──░░ ░░░░ ──░ ░─────░░░ •░░ ░ ░░────░░░│
                      └───┐       ──    ──   ──────     ────               ───   ──     ── •   •  ──    ───┘
                      │   └───        ─┐   │         ┌─┐            •  ──      •      •                    │
                      │░░░│ ░ ░ • ░░•  │░░░│ •░░░•   │░│░ ░│ ░ ░ │  ░ ░░░ ░ ░ ░   ░    ░    ░│          ░  │
                      └───┘ •     ──   └─          ┌─┘─┘───┘─────┘───────────────────────────┘─────────────┘
                      │             ──    • •  ── ─┘
                                             ──  •




































```

*Figure from page 12 (2346x3317 px)*


---



4203-E P-289



SECTION 2 PROGRAM OPERATION



(2) Automatic Space Insertion



When a character is keyed in while the edit pointer is located to the right of the downward-pointing



arrow«



f',



spaces are automatically inserted up to the position where that character is keyed in.



When the BS key is pressed while the edit pointer is located to the right of the downward-pointing



arrow"!", the edit pointer moves to the position of the downward-pointing arrow.



,00 ""'""'· ",. J



COPV OVEP.ffl' I TE



'EDIT POINTER



COPY OVERWRITE



COPY OVERIIRITE



L ""',,. .... _" ·-



COPY OIJERIIR I TE



[c o



,oo """''"·



",.1



Fig. 2-11 Automatic Space Insertion


```text


                                                                                               ───       ──
                                                                         ┌──┐─┐────┐─┐─────────░░░───────░░│
                                                                         │░░│ │░░░ │ │░░░░░░░░░ ── ░░░░░░──┘
          ┌──────    •               •      ─────────────────────────────┘──┘─┘────┘ └─────────      ───
          │       ──  ┌─────────────┐ ──────                                                               •
          └──────  ░│ │░        ░   │        ┌─                                                           •
                 ───┘ └───┐     ┌───┘        │ ─┐─── ──┐─ •  ──── • ─┐───┐ ─────── • ──┐─┐────────────────
                      │░ ░│ ░ ░ │ ░ ░│   ░░░░   │░░░│ ░│ │ ──   ░│ • │  ░└─ ░ ░   •░•  │░│                 ┌┐
                      └───┼────┐     │              │    │    │  │                        ───       ──     └┘
                      │   │    │░ ░ ░│    ░    │░  ░░•  ░░ ░  │░•  ░░  ░░ ░ ░ ░ ░ ░  ░░  ░░ ░░░  ░ •░░░░ ░
                      │░  │ ░   ─┐ │           │   ──░•        •                                    •     ──┐
                      │   │      │ └─┐─┐─      └┐      ┌─ ───┐─     ──    ────  ──  ───  ───    ░    ░     ░│
                      │░ ░│ •    ░ │░│ │░──────░└──────┘ •░░░│░─────░ ────░░░░ •░ ░ ░░▒ ░ ░░────────────────┘
                      └───                                                      ────────────
                           ┌───────────────────────────────────────────────────┐
                           │▒▒▒▓▒▓▓▓▓▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▓▓│ ──
                           └┐──────────────────────────────────────────────────    ┌─┐
                          │ │                               ░   ░     ░          ──┘░│
                          └─                        │░│ ──     ┌─────────       •  │░│
                            ────────────────────────┘░│   ┌─┐  │                   │░│
                                                    │░│   │░│  │                   │░│
                                                    │░│   │ │ •                    │░│
                                                    │░│                            │░│
                           ┌────────────────────────┘─┘────────────────────────┐   │░│
                           │▓▓▓▓▓▓▓████████████████▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▒▓▓▓│   │░│
                           └───────────────────────────────┐─┐────────────────┐┘  │ │
                                                           │░│                │ │ │ │
                          •                         ┌─┐    │                  │ │ │░│
                           ─────────────────────────┘░│    └──  ──────────────    │░│
                                                    │░│   │ ░  •                  │░│
                                                    │░│   │ ░──                   │░│   ┌───
                                                    │░│                           │░│ │ │░░░
                            ────────────────────────┼─┼────────────────────────   │░│ │ └────
                           │▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│▓│▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒░░░▒░▒▒▒   │░│
                           └────────────────────────┘─┘────────────────────────   │░│
                                                          ░░                      │░│
                                                                                  │░│
                                                                                  │░│
                                                                                  │░│
                                                                                  │░│
                                                                                  │░│
                                                                                  │░│
                           ┌──────────────────────────────────────────────────┐   │░│
                           │▒▒▓▓▓▓▓▓▓▓▓▓█▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▒▓▓│   │░│
                           └┐────────────────────────────────────────────────┐┘ ──┘░│
                          │ │                                                │  ░  ─┘
                          │                                                    ────
                           ───────────────────┐──┐───┐ ┌─────┐─┐─┐───┐────────
                                              │ ░│   │ │░ ░░░│░│ │░░░│ ░ ░░░░░│
                                              └──┘───┘─┘─────┘─┘─┘───┘────────┘
































```

*Figure from page 13 (2346x3317 px)*


---



15-3. Use of the Command History



4203-E P-290



SECTION 2 PROGRAM OPERATION



The last 5 commands which have been used are stored as the "command log". Previously created



commands can therefore by used again by selecting them from the command log. They can also be



revised before they are used.



{1) At the command creation screen, press function key [F4) (COMMAND HISTORY) to switch to



the command history screen.



(2) Use the cursor control keys to move the cursor to the desired command.



(3) Press the WRITE key.



The system will return to the Command Selection screen, and the selected command will be read



into lines 4 to 7. To execute the command as it is, press the WRITE key.



If reading to the command selection screen is not required, press the [F7] (CANCEL) key at the



command history screen. The system will return to the command selection screen without reading



the selected command.



lltj



~EDIT POINTER



IIUX OISP!.,ic't ~



{F:!l -> ici:•.•••



{Fl) -



FCQ::•, •tN



IBMSAFR



TO Ol::PJ.Y OnER INOt)tES,~ ~SSHC (Fl}.



I~ ll1:: 0£V!Ce«Ai11E Ail0 FH.E.wiE.Til£H PR£5S (MITEJ X.~.



CEFNJ:.r O£Ytt£ fWE : llll;



OEFMT Fll.1 ttM1E • ".IIIUt



l.eiiwi



(ff961'l g;



uax 01SPJ.Y



LF2i fiei1:"',IIUN



(Fll FtQ:f',IUN



TO OISP!..AY 0~ !ta'Xi:S,~ ~ING fFl].



IMPU'T T~E QE\/lce It'll€ All) .CH.i HAIE. 'l"HEN ~ f¥ftm:J x:~.



CEF4U..i ONICc HNI!: - El!



OEFMA.'r F!t.: "'6E - -.lt!l'I'



lf:1!0GW ft5!iljQk JBM!SrTI



CO RXr.f'!'IIIJWI.IIIH.Fol:



mae•~



ii ~)~~,\\'r,W,'~•~=lfJ~SSA/l£.



m 'CURSOR



pr:\0T JDl~TES'T.lfJH~C '


# '~ l._ ______ __,,,J

Fig. 2-12 Use of the Command History


```text


                                                                                                ───       •
                                                                         ─┐─┐─┐────┐─┐──────────░░░──────░░│
                                                                          │▒│ │░░░░│ │░░░░░░░░░░───░░░░░ ──┘
             ───────   •     ──  ──       ──   ────────────────────────── └─┘─┘────┘─┘─────────
           ┌─       ──  ┌────  ┌─  ───────  ───                                                            │
           │    ──┐   • │░ ░ │ │                 ─┐────────────────────────────────────────────────────────┘
           └─  •  │  ░░ └──┐ │ │  ░   ░ ░┌───░   ░│
             ──        │   │             │             ──      ── ─┐     │   •         •   ──── ───     ──
                 ┌─────┘─ ┌┘── ───────── │  ┌─┐────┐ ──░░──────░ │░│ ────┼───  ────────░ •   ░░•░░░░  ┌─░░░│
                 │░░░░░░░░│ ░░ ░ ░░░░░░ ░░  │░│ ░░░│ ░░──░░░░░░░─┘░░░ ░░░│ ░░──░░░░░░ ░• ░  ──░░────  │░──░│
                 └───░────░░────────────────┘─ ──── ───  ───────  ─── ─── ───  ──────── ───   ──       •
                     •                                                       •             •
                       • ░      ───── ──── │      ┌─┐   │ │        ┌─         ░    │   ░   ░   ──────   │
                  ──  │              •     └──   ─┘ └───┘─┘────────┘ ──────────────┘───────────      •  │
                      └── │░─────────░─────░░░░                                                ──────
                  ┌─  │   │                     ─────┐─┐────┐─┐─┐───┐─┐───────────────┐
                  │░  │ ░• ░░ ░ ░░│ │░░░ ░ │░░░░░ ░░░│ │░   │░│ │░ ░│ │░░░░░ ░░░ ░░░ ░│
                  │   │   │    ┌──┘─┘    ┌─┘─────────┘─┘────┘─┘─┘───┘─┘───────────────┘
                  │░│ │░░░│ ░░ │░░░░░ ░░░│
                  └─┘ │                           ─────── ────── ──────   ──     ────────┐───┐─────┐──┐─┐──┐
                        ░ ┌──░░░──░░ ░░ ░─────┐── ░░░░░ ░•░░░░░░• ░░░░░──┐░░░────░░░░░░░ │░  │░   ░│ ░│ │░░│
                      ┌───┘░░─── ░───────░░░ ░│ ░───░░───░░───── ──  ──  └┐─┐░░  ░──  ┌──        ──┘ ─┘ └──┘
                      │                                                   │ │         │  ┌───────   •  │
                      └───░───────────░───░░░░ ░░░ ░── ░░•░░─── │░  ░░░░ ░└─┘░░░  ░• ░ ░ │░░░░░░░• ░░• │ ░ •
                      │   •       ░   │   ─┐─┐░ ────   •   •    └─ ░─────    ───  • │ •      ───    •       •
                      │ │             │    │ └─      ── ─── ────┘ ──     ────   •   └─  ──       •   ─┐    •
                      └─┘ •░───░───── │░───┘                                     ───      ───     ──  └────
                        └─            └─
                            ──────────   ─────────────     ──┐   ┌──────────────────┐─────────   ───┐
                           │░░░░░░░        ░░░         ────  └─  │░░░░░░░        ░░░│         ───   │
                           │░───────────────────────── ░░░░  │    ───────      ─────┘─  ┌─────░░░──  │
                           │░                          ─────  │ •        ──  │░       ──┘     ───    │
                           │  ░───┐─░ ░•                    │ │             ─┘─┐░│ ░░░░░░│         │ │
                           │░  ░  │░┌──                     │ │   ┌─┐─────┐    └─┘ ──────┘─────────┘ │
                           │░• ┌──┘░│  ──────────────┐      │  │  │░│  ░ ░└─  •   •                │ │
                           │░░░│░░ ░░░ ░ ░░░░░░      │      │  │  │ ░  ░░ ░░──░ ░░░   ─────┐       │ │
                           │░│ └─ ░░─┐░┌─────────────┘      │  │  │░  ░░ ░│ ░  ───────     │       │ │
                            ─┘─  ─── └─┘                    │  │  └───────┘ •         ── ──        │ │
                          │                                 │  │                                   │ │
                          │                             ────┘  │ •                             ────┘ │
                           ┌─┐─┐──────────────────┐──┐┐     │  │  ┌─┐──┐─┐─┐──┐─── ────┐─┐────┐    │ │
                           │░│ │░░░  ▒░ ░▒▒ ░░▒  ▒│  └┘─       │  │ │  │░│ │░ │░░░ ░░░ │░│    │      │
                           │   ░ •   •  ───  ──         ░ •  •  ──┘─┘──┘─┘─┘──┘── ─┐──   └────┘    ┌─
                           └─ ─── •       ░    ──  ─────── ──                    │█│            ───┘
                                   ───────┐─┐─   ──                              │▓│   ░│
                                          │▓│                                    │▓│  ──┘
                           ───────────────┘▒└─────────     ──┐    ───────┐────── │▓│      ──       •
                        ┌─ ░░░░░░░░       ░░░░         ────  └┐  │░░░░░░░│       │░│░       ──────  ─┐
                        │  ┌────────     ───────────── ░░░░   │  │░┌─────         ─┘         ░░░░    │
                        │  │                                  │  └─┘       ─────     ──────────────┐ │
                        │  └───────────────────────────────── │                                    │ │
                        │ ░│▓▓▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ┌────────────────────────────────┐  │
                           └─░░░░░░░───────────────┐─────────    │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│  │
                        │  ░░░░░░░░• ░        ░    │             └────────────────────────────────┘  │
                        │  ────  ──    ── ─────────┘        │                                      │ │
                        │ │                         ──      │                                      │ │
                        │ │                                 │                                      │ │
                        │ └── • ──────────   ───────        │                                      │ │
                        │ │  │ │                    ──┐     │                             ──────── │ │
                        │    │ │   ┌─                 │     │                                     •  │
                         •         │   ┌──┐─┐                                    ─┐       ──────   ──
                          ─────────┘─  │█ │█└────────────────────────────────────▒│             ───
                                       └──┘─▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░▒▒▒─┘
                                            ─────────────────────────────────────

                                             │░░ ░  ░ │ ░  ░ ░░        ░  ░░░
                                             └── ─────┘─────────────────────────















```

*Figure from page 14 (2346x3317 px)*


---



4203-E P-291



SECTION 2 PROGRAM OPERATION



15-4. Selecting Files From Directories (OSP Format)



15-4-1. Procedure for Selecting Files from Directories



(1) At the Command Creation screen, press one of the following function keys:



[F1] (INDEX), [F2] {MD1: INDEX), [F3] (FD0:INDEX)



If function key [F1J (INDEX) is pressed, "ISO» will be displayed at the console line. Following the



"ISO'' character string, enter the desired device name and file name, then press the WRITE key.



(2) At the directory selection screen, use the cursor keys to locate the cursor at the file name of the



file to be selected.



(3) Press the WRITE key.



The display will return to the command creation screen and the device name and file name selected



with the cursor are entered at the position of the edit pointer.



Command crea~on screen



r,EDIT POINTER



l~OISP".,AY~



[~) -> lll1:•.lillk



{FJJ -► FtQ:"',l!IIN



ti) 01$1'1.AY OntEl'I !NJe:Xl$,~ PRESS,IHQ (F1j.



l!FVf 'J1,£ DEVICE 1WE M«'.l FILE K.4JI:. ilO fll!lle:SS [¥R11;J XE'(.



CE.F,u.:r ~ce MAJE - en:



CEFAUl.i ,:Cl!.E AA1i1E ,.. ... ii!N



Command creation screen



~eo w1:rcoui1-1NI



'EDIT POINTER



lffll;X 01$Pl..4Y ?!'«£!)!Jq('



['11 -> 11)1:•,"1•



[f'l] -



Foo:•,¥l'1\



10 C1$P'..AY On-ER IJaXES,k"'Te:t PR$€$J!tG [Ft'..



llf\IT iii£ :£,/la! MiE NfJ FI/.Z AA!E. 1'!-EN Pfl£SS ~f:'E} K..r:'f'.



IJEF.U..l' 0£¥1 CE: NA1E = i01:



OEFMLT FILI: l'IAIIE" • '".IIIN



Directory selection screen



I~ co



PX:2.IIIUI



~.il!H



P'X6.1t1N



:p;;xs,¥1,t



POlO,ti:IN



r'Ol2,llfl



P?'lUUft



POlS,¥1M



PJ19.imt



Fig. 2-13 Selecting a File from Directory



OYE:lf!H •



QVi::l!)fil"'=


```text


                                                                                                ───       •
                                                                         ┌──┐──────┐──┐─────────░░░───────░│
                                                                         │░░│░░░░░░│  │░░░░░░░░░───░░░░░░░─┘
              ─────     •         •   ────   ──────────     ── ── •  ──── ──┘──────┘──┘─────────     ──
            ┌─     ───── ─── ─┐─── ───    ───          ────┐  •  •
            │░  ┌──           │     ░                      │       ─┐
            └───┘  ┌───────── └──── • ── ┌──────────┐ ─────┘ •   │░░│
           ┌┘   │  │               • •   │          └─     │  ───┘──
           │░    • │░ │░░░ ░ ░░ ░░░░░░░░  ░░│ ░ │ │░░░░░░░░│
           └───── ┌┘ ─┘                     │ │ └─┘ ─┐─   • ─┐──┐─┐───────────────┐─┐───┐
                  │ │ │░ ░░░ ░░░░ ░░░░ ░░░░░│ │░░░░│ │░░░│ │░│ ░│░│ ░░░░░░░░  ░ ░░│ │░░░│
                  └─┘ └┐ ┌─ ┌─────          │ └────┘┐ ┌──┘ └─┘┐─┘ └── ┌───────────┘─┘───┘
                       │░│░ │░░░░░░──░░░ ░░─┘ │░░░▒░│ │░░│ │░░│ │░░░░░│
                         │ •      │                                    ──── ──  ──┐─ ────── ──         ────┐
                       ┌─┘┐ ░─────┘  ┌──░░░ ░░│ ───░░───── ░░───░░────░░░░░░░░•░ ░│ •░░░░░░•░░─────░ ░•░░ ░│
                       │░░└─┐░░░░░░──┘░░ ─────┘─░ ░──░░░░░ ──░░░──░░ ░────────░───┘─░─────░░░•░░ ░░───░── ─┘
                  ┌─┐ │     │        │                                                                     │
                  │░│ └┐────┘─░──────░░  ░       ░│  ░  ░             ░                                    │
                  └─┘ └┘      •       ┌───────────┘ ───────────────────────────────────────────────────────
                      │    ─── ─┐─┐─  │
                  ──┐ │  ──     │ │   └──┐
                    │   ░░░• ░░ │░│  • ░░└─
                   ─┘──                     ─┐       •    ────  ── •       ─────────┐──┐────────┐────┐─────┐─
                       ──┐           ░  ──── └─── ── ░─── ░░░ ──░░ ░──────░░ ░░ ░░  │░░│ ░ ░  ░ │░ ░ │░░░░░│
                       ░░└──────────░░──░ ░░░░ ░░░ ░ •░░░░─── ░ ──── ░░░░░──────────┘──┘────────┘────┘─────┘
                       │                ───────────── ────   ──
                       │ ──────────────                               ───  ──┐
                       └─              ──┐──┐────────    ───┐     ────       └──────────────    ──┐
                         •░░░░░░░┌─      │░░│        ┌───   │   │░░░░░░░        ░░░         ───   │
                         ░▒──────┘ •  ┌──┘──┘────────┘░░░ │ │   └─────░──────────────────── ░░░░•  │
                        • │           │               ─── └┐┘                               ───  │ │
                       │  │ ───────┐──                     │    │  ─── ──░                       │ │
                       │  │░ ░░░░░░│                ───────┘    │░  ░░ ░░ •                ──────┼─┘
                       │  │░   ░   └─────────┐─────┐       │  ░ │    ░     ───┐─────┐─────┐      │ │
                       │  │░ ░  ░ ░ ░ ░ ░ ░ ░│     │       │  ░ │░ ░ ░░ ░░░░░ │░░░ ░│     │      │ │
                       │  │░░ ░░░░───────────┘─────┘       │    │░│ ──░░──────┘─────┘─────┘      │ │
                       │ │ ───────                         │   ┌┘─┘─  ──                         │ │
                       │ │                                 │   │                                 │ │
                       │ │                •                │   │                               • │ │
                       │  ┌──────┐─┐────── ──────┐──────        ───   ─── ── ┌── ─────────────  •  │
                       └┐ │░░  ░░│ │░░░░░░ ░░░ ░░│  ░░  ┌── ───  ░░   ░░  ░░ │░░  ░░  ░░  ░░   •  ─┘
                        └─┘─┐░ • └─┘─────   •   • ░ • ░ │  •   • ───  ─── ─── ─┐▓┌──     ────   •
                            └─ ░░│        •   ── ─── ───┘──                    │▓│    │▒│
                         ───  │░│                                       ────   │▓│  │ └─┘ │
                              │▒│                              ┌──────── ░░░───┘▒└──┘     │     ──┐
                              │▒│                              │░░░░░░░░       │░░░         ───   │
                              │▒│                            │ └┐──────────────┘─────────── ░░░ • │
                              │▒│                            │  │░                          ───    │
                              │▓│                            │ • ┌──────   ────────            │ • │
                               │▒────────────────────────────┘  ▒│ ░           ░             │░│  •
                               └┐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓│   └────────────┐┐─     ───────┘─┘─┐
                                └────────────────────────────┘ ┌─▒▒▒▒▒▒▒▒▒▒▒▒▒└┘  ┌──┐           │
                                                               │░──┐──────────┘   │░░│           │
                                                               │░ ░│              └─░│           │
                                                               │░ ░│              │░░░•  ────   •
                                                               │░ ░│  ───         │░──       ───
                                                             │  ──┐  •    •        •   ─┐───
                                                             │    │ │  │ │ │   │ •  │ │░│
                                            ┌───────┐─┐──────  ───┘─┘──┘─┼─┘───┘─   └─┘─┘───
                                            │░   ░  │ │░░░ ░     ░░      │░      ┌──
                                            └───────┘─┘──────────────────┘───────┘





















```

*Figure from page 15 (2346x3317 px)*


---



4203-E P-292



SECTION 2 PROGRAM OPERATION



15-4-2. Directory Selection Screen



If the selected device is OSP format, the directory selection screen will take the form shown below.



For its appearance when the selected device is MS-DOS format, refer to 15-5, "Selecting Files From



Directories (MS-DOS Format)".



Lines4 to 7 The command being created is displayed here.



The selected file name is entered at the position of the edit pointer. The edit pointer



cannot be moved by pressing the cursor keys.



Une9 The device name for the displayed directory is displayed here.



Lines 12 to 20 : The directory is displayed here.



Move the cursor to the file name to be selected by using the cursor keys.



If no file name is displayed, it means that the selected device does not contain files.



Up to 18 file names are displayed on each screen. If there are more than 18 registered



files in a directory, the page up/down keys can be used to display other pages.



The command being {



created is displayed



here.



The device name of -



directory is



displayed here.



The directory is



displayed here.



PRO\.."f!A~ OPERA TI ON TRANSFER



COPY OV'"t.RWR ITE



co D



'EDIT POINTER



P003.MIH



P005.MIN



P007.MIN



P009.MIN



POl l .Ml N



P013.MIII



P002. UI N



P015.MIN



P017.MIN


#### P004. MIN

P006.MlN



POOS.MIN



P010.MIN



P012.MIN



P014.MIN



P016.MIN



P018. MIN



Fig. 2-14 Directory Selection Screen


```text


                                                                                                •         •
                                                                         ┌──┐──────┐─┐──────────░ ───────┐░│
                                                                         │░░│ ░░░░ │ │░░░░░░░░░░──░░░░░░ └─┘
                 ──                       ─────────────────────────────── ──┘──────┘ └─────────
           ┌─────  ─────────┐─────────────
           │  ░ ░   ░ ░ ░   │ ░                                      •                     •     •
           └────  ─┐  ┌────            ──  ─────────────────────────┐ ┌───────────┐──────── ┌───┐ ┌───
                │░ │░─┘░░░░░  ░░ ░░   ░░░│ ░   ░  ░  ░         ░  ░ │ │      ░░  ░│ ░       │   │ │   ─┐
                │                        │ • ── ──           •      │ │   │  •    │       ──┘   │ │    └┐───
                 ┌───── ░░░░──░ ───░░░  ░└─ │░░ ░░░ ░░ ░░   ░░░ ░░░░   ░░░│ │░░│ ░│ ░  │ │░ ░  ░│  ░░   │  ░│
                 │      ────░ •     ──  •  ─┘────── ─────   ─── ──────────┘─┘──┘──┘────┘─┘──────┘───────┘───┘
                 │           │  ─┐                 •     ───   •
                 └┐ ░░░ ░ ░ ─┘   └┐░░░ ░░── ░░░ ░░░░   ░░░░░ ░ ░  ░░ ░░    │
                  └─────────      │               •  •                    ─┘─┐───┐─┐─┐──────┐─┐───────┐────┐
                                   ░───░░░░░░──░──░░░░────░░░░░░ ░ ░░ ░░░░░░ │░ ░│ │░│ ░░░░░│ │ ░ ░░░ │░░░░│
                                  ┌─░░ ──────░ •░  ───   ░─────────────────┐    ─┘ └─┘  ────┘─┘───────┘────┘
                  ┌─────┐         │          │                             └┐───  •   ──
                 ┌┘ ░░ ░│         │░░░ ░░░░░ │░│░ ░░ ░ ░ ░░░░░░░░ ░ ░░░░░ ░ │░░░░░░│ │░░│
                 │       ──────   └─          ─┘              ──────────────┘──────┘─┘──┘
                  │  ░│ •    ░    │ ─── ░░░░░• ░ ░░░░░░░░ ───
                  └───┘─ ──────   │     ───     ────  ──┐     │    • ─── ───    ────  • ────┐─ ───
                                  │    │   ──        •  └─    └── • •       ────   ░┌─ •    │ │   ────────┐
                                  └──┐ └─  ░░── ░ ░░░░░░░  ───░░░• ░ ░──────░  ░────┘░   • ─┘ └──       ░░└┐
                                  │  │                   ──                                 └─        ───  │
                                  └──░  ░░░──── ░│ ░░░ ░░░░░░──░• ░░░░ ░ ░░ ──░░░░│ ░ ░──── ░ ░│ ░░░•░░░░░░│
                                  │░░──────░ ░░──┘─────────── ░•░───────────  ────┘────  ░ ────┘ ──  ░┌────┘
                                  └──                                                              ───┘
                                            ┌─────────────────────── ────  ───────────
                                         │  │░▒░░▒░░░▒▒░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒░░░░░░──────░░│  │
                                         │  └──────────────░──────────────────────────▒▒▒▒▒▒▒▒─┘  │
                             ──        ──┘  │▓▓████████████████████████████████████████▓▓▓▒▓▒▓▓│  │
                        ┌───    ░────┐      └──────────────────────────────────────────────────   │
                        │░░░░────░░░░│                                                          • │
                        └────    ────  ──   ─────────────────────────────────────────────┐─────┐  │
                        │     ─┐            █▓▓▓▓▓▓▓▓▓▓██████████████████████████████████│▓▓▓█▓│  │
                        └───░│░│ ░ ░   │    ─────     ─────── ───────────────────────────┘────┐┘  │
                        │ ░░ │    ┌────┘         ─────       •                                │   │
                        └────░░ ░ │      •  │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█│▓▓▓▓│     ┌───┐                │   │
                                ──┘     •   └─┐───┐───────────┘────┘    ┌┘░  │                │ │ │
                         •   ───      ┌─    │░│ ░░│                     │░░ ░│                │ │ │
                        │  ░ ░░ ░│    │     └─┘░ ░│                     │░│ ░░•               │ │ │
                        └──░ ─── │    │    │      │                     │░└─░│                │ │ │
                           ──         │ │  │░░ ───                      │░│ ░│                │ │ │
                                      └─┘  │░│ ░░░────        ───────── │░░│░░────  ──────────┘ │░│
                                        │  └─┘────    ────────          └──┘──                │ │ │
                                        │                                                       │ │
                                        │        │ │      ────┐               ────┐─┐──┐──┐     │ │
                                         •       │ │  ──      │               ░ ░░│ │░░│  │     │ │
                                          ─── ───   ─┐  ──  •           •      ───┘ └──┘─      ┌┘
                                             •       │ │   • •        ─┐    ──           ──────┘
                                              ──░   ─┘ └──░   │ •  ░   │ │   ░│
                                                ────  •   ────┘─ ──────┘─┘────┘






























```

*Figure from page 16 (2346x3317 px)*


---



4203-E P-293



SECTION 2 PROGRAM OPERATION



15-4-3. Cursor and Page Operations



(1) Moving the Cursor to the Right



Each time the "right" cursor key is pressed, the cursor moves to the file name which is adjacent and



to the right, or below and to the left, with respect to the current cursor position. If the cursor is located



at the final file name in the directory, it moves to the first file name in the directory.



(2) Moving the Cursor to the Left



Each time the "left' cursor key is pressed, the cursor moves to the file name which is adjacent and to



the left, or above and to the right, with respect to the current cursor position. If the cursor is located



at the first file name in the directory, it moves to the final file name in the directory.



(3) Moving the Cursor Downward



Each time the "down" cursor key is pressed, the cursor moves to the file name directly below the



current position. If the cursor is located at the final file name in the directory, it moves to the first file



name in the directory.



{4) Moving the Cursor Upward



Each time the "up" cursor key is pressed, the cursor moves to the file name directly above the



current position. If the cursor is located at the first file name in the directory, it moves to the final file



name in the directory.



{5) Changing Pages



Up to 18 file names cam be displayed on the directory selection screen. If there are more than 18



files registered in the drrectory, other pages can be displayed by pressing the page up/down keys.



l?SMM ifEiWfq.



lcrer



co Pf«P,1,11.VtN,I



jl(JEXCCICl"'TliJIII



,oo;



POJ2.:IIIN



POOl.lflN ?OOUIIM



FOl5.WlN ?O)E.Yll!I



PC01.IIUN PCCS.lllk



?X19.¥1N POlitMIN



ron.vm ~12.1111"



Ft]ll.iUH Ptn 1 umi1



POl5.tWt POli.V!ff



P0l7.fillN P018,lillM



co PACGWLli!ft,I



CURSOR



POZl.l,lfN



PC2J.lllltl P0:2"1, W!N



P025:.lllfl ?026, U!N



P027.Mll'I ?Q2fl.WIS.



PC29.MIN



Fig. 2-15 Cursor and Page Operations



OVFR!f!f!'1::


```text


                                                                                                 ──
                                                                          ┌─┐─────┐───┐─────────░░░────────░│
                                                                          │░│░░░░░│ ░ │░░░░░░░░░ ──░░░░░░░░─┘
                 ───     ──                  ─────────────────────────────┘─┘─────┘   └─────────      ──
            ┌────   ─────  ──────────────────                                                               │
            │░    ─┐          ░              ───────────────────────────────────────────────────────────────┘
            └────┐ │ ─┐        ──── ┌─┐───
                 │    │  • ────    ─┘ │       ┌───┐
                  • •  •    ░  ───    └┐      │░░ │
                      │   ┌──       │  │       │    •   ──    •        •           •    ──┐───┐   ──── ──
                      │   │   ──    │  │ ──────┘ ──░ ───  ──── ────── • ──     •  • ────  │   └─── ░░ • ░── │
                      └┐ ░ ░ ░░░ ░ ░░░ ░ ░ ░ ░ ░░ ░░ ░░░ ░░░░░░ ░ ░░░░  ░░  ░ ░░░ ░░░░░░  ░ ░░ ░░░░──░ ░░░░░│
                       └───────┐─░──┐────────┐───░──░░───────────────░ ░─────░ ────────░│░────────   ───────
                  ┌─┐  │       │    │        │   •  ──               ───     ──        ─┘─
                  │░│  │░ ░ ───┘  ░ ░░│ ░ ░ ░└─░•
                  └─┘ •   │           │          ────────┐─┐──────┐─────────────────────────┐───┐───────────┐
                       ┌──┘─░░░ ─── ░░░──░░░• ░░•░ ░ ░░░░│ │░   ░░│  ░  ░░ ░ ░░ ░░ ░░░░ ░░ ░│ ░ │░░ ░   ░░ ░│
                       │    ────     •   ─── ──   ┌─  ───        ░│                      ──                 │
                      │               ─┐       │░ │                   •      • •       ──   ──    ──        │
                      │░ ──── ░─────░░░│  ┌────┘─░░ ░│ ░ │░░░░ ░ ░ ░ ░░░ ░│ │░░░░ ░ ░░ ░░░░░░░┌───  ────────
                  ┌─┐               │    ─┘      ┌───┘───┘────────────────┘─┘─────────────────┘
                  │░│ │░░ ░ ░ ░░  ░ │░░ •░░░░░░░░│
                  └─┘ │                           •     ──  •        •     ───           •      ──   •
                       ┌─────────────────┐────────░─────░░░░░┌────── ░─────░░░───────── │░ ░───░░░───░──────
                       │░░░░░ ░░░░░░  ░ ░│ ░░░░░ ░•░░░░░─────┘ ░ ░ ░──░░░ ░──░░░ ░ ░░░░ └───░░░─── ░ • ░░ ░░
                       └───────────── ░──┘─   • •  ─────      • ────  ─────   ──   ──       • •    ──    ──
                  ┌─┐  │
                  │ │  │      ░│          ────┐
                  └─┘ │        └───   • •     └──  •  ─────  ┌─       • ── •
                      │░           │   •         ── ──     ──┘ • ────┐ │  • • │ ┌─   │ ────   ───── ──   • •
                      │            │ │░ •                       •    └─┘─     └─┘ ── └─    •       •   ──  ░│
                       │      ░  ░ └─┘── ░  ░  ░ ░ ░ ░░░  ░  ░ ░ ░ │░ ░░ ░ ░ ░░ ░░░░░░ ░──░   ░░ ░ ░░ ░ ░ │░│
                       └───────────░░░░░░──────────────────────────┘────────────────────  ────────────────┘─
                  ┌─┐ │              ┌───
                  │░│ │░░░░░░ ░ ░░░░░│
                  └─┘ │               • ─── •   ────────   ─┐─ ──────   ───────┐────   ┌─────────┐──────────┐
                       ── ░────░───░░░░• ░░░ ───░░░░░░░░───░│░•░░░░░ ───░░░░   │░░░░───┘░ ░░  ░░ │░ ░ ░░░  ░│
                       ░░░•░░░░•░░░──── ────░ ░░───────   ░ │  ──────  ░   ──   • •     ───    •       ──  ┌┘
                        ── ────  ──          ───       ───── •       ──────  ──  • ──       ─── ───────  ──┘
                                            •    ───  •                              ┌─┐
                                          ──░░░░░░░░░░░░░░░──────────────────────┐ ──┘▓│
                                         │▓░───────────────░░░░░░░░░░░░░░░░░░░░░▓│  ░└─┘
                          ───────┐────── │▓│                                   │▒▒│
                         │░░░░░░░│       └─┘ ───────────┐─     ─┐─┐────────────┘░░└─  ─────────────
                      │  │░░                         ░░░│       │░│  ░          ░░░                │
                      │  └──────┐───────      ──────────┘─┐     └─┘────┐─────────────────────────┐ │
                      │  │      │                         │     │      │                         │ │
                      │  │░░░░░░│                     │░░ ░     ░░░░░░░│       •             │░│ │ │
                      │  │   ───┘───────       ┌──────┘──┐    ░    ────┘─────── │      ──────┘─┘─┘ │
                      │  └──▒▒▒▒▒▒▒▒▓▒▒▒┌─ ┌───┘         │      ───▒▒▒▒▒▒▒▒▒▒▒▒─┘ ┌───┐          │ │
                      │  │▒░┌───────────┘  │░░░│         │      ░░░┌───────────   │░░░│          │ │
                      │  │░░│              │░░░│         │      ───┘              └───┘          │ │
                      │  │░░░───────────── │░░░│         │    │                                  │ │
                      │  │░░•              └┐░─┘         │    │                                  │ │
                      │   ──                └─  •                                 ─┐──  ───      │ │
                      │       │                 ░                                  │   •           │
                       ─┐   ──┘      ──┐ ┌─                                    ┌─┐ └───░ •░┌┐─── ──┘
                        └───   ────  ░▒│ │▒────────────────────────────────────┘█│     ── ─┘┘   •
                                     ──┘─┘▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░│
                                    •     ──────────────────────────────────────
                                                                                │
                                             │░░│ ░ │░ │░░░░│ │ ░│ │░│ │░░░░░│░ │
                                             └──┘───┘──┘────┘─┘──┘─┘─┘─┘─────┘──┘



















```

*Figure from page 17 (2346x3317 px)*


---



4203-E P-294



SECTION 2 PROGRAM OPERATION



15-4-4. Function Key [F6] (RETURN), [F7] (CANCEL) and Cancel Key



When function key [F6] (RETURN} key is pressed, the command creation screen is displayed and the



device name only is entered at the position of the edit pointer. The file name that was at the cursor position



is not entered.



When function key [F7] (CANCEL) or the Cancel key is pressed, the command creation screen is



displayed and neither the device name nor the file name at the cursor position are entered on it.



Directory selection screen Command creation screen



ESiW1 esa'/'1~ 3iHSS



l~~SFl!lt ~~



Im ..Jlll!lll'l'!l:J



L··•-!



OVEf!Rli=



a,~.lllll.!



-- 'EDIT POINTER



',. ... 1:,..,..1(1,1



--- ....



FOO:



INCO OlsPU't ~



(1=2) - > II01 ;•.kl""



(Fl)



F!X):•.•i,



POOf.lllUI P'001:~lillll' to OISJ>IJY On,e! 1H:EXSS.AFT':R ~ING [Fil.



I P003.UfM P0)4.IU1' 1111"1,JT TI-'£ teVIC£ fWE A/"J Fl:.! ""11;. n-EH mss ~rrt] lit$.



j PCXIS,IUN PC()S.11:!ft /CURSOR



WMl'l.T !k'"VICE H:iA.WE-.. 11)1;



XXlJ,.fN POll.liUI



f'IC(5,Mlli POIO.Mll'J



Ol:FAULT i:'t:.£ iWIE '= •,IUN



?Qlt,Mlli



l"Otl.MIN: P014.¥1li



F(H5.111r. POUUII.N



?0!7.llt/C F"018,UIH



I I


# I I 1-1~.1

'""'


# I "11,.;,,.I ~~!:l~lo:rn!

CAIIC<l.



)BJ



CAN



/,~~l:12!



[':~·•"·FOO'\_ ED!T POINTER



~Ir-::



I folOEX OISP\J,'f ~



(F2l



u;n:•,111N



lFJ) - > P.:X):'+.lltH



TO OiSPu.'f ~ IQXES.AFTER PRESS1NC !}=1].



Ir.PU; "tHE OE\!lcE NMIE" N:o ;;ltE !WE. MK~ tifl:J1'l€ X!I'.



OEFM.U Dell CE MIE - CJl:


#### Of;FMJLTFl1• .EM1411e'-. •,f!N

\., ,,.,;;111;~1 ~EXl=lo::l"of=I ~LI



tm9W! Of"E6lt [Oft EW§ft.B



r~·.,._o:,iF1>t1.Nt•\_E:~~~!NTER_ _



_-I



-----··--·------~--



1ta'X DISPu.Y Pia:~



£F2) -;. 1iD1: 11 .1tlH



[f3] - > Fll);•.tl!N



TO OlsP!..AY On-ii;! 1u:<es, ...-. rm PRIS$!Mt f.C:11.



ltlvl lk!;-CEVIC:f HiolE U/0 File HME.lli£H ~SS )IR!~) K::Y.



DEFMIL.T DEVla ~ - il)1:



Df1='AILT FIU'. ~ • •.fttH



'""'



110,·



I roo·



f""""" I"""'"/ I,_ I I

• 1!0:x I il<e riiSTCRf. IHSefi •



oa.:.-re



CAN:el;L



Fig. 2-16 Function Key [F6] (RETURN) and Cancel Key


```text


                                                                                               ───       •
                                                                         ┌─┐───┐─┐───┐─────────░░░───────░──
                                                                         │░│░░ │░│   │░░░░░░░░░ ──░░░░░░░•░
                ──                          •    •             ──        └─┘───┘─┘   └─────────     ───
           ┌────   ──────────────┐────┐───── ──── ───────┐─────  ────────                                  │
           │░      ░       ░   ░░│ ░ ░│  ░░   ░     ░░  ░│                                          •      │
           └───  •                •  • •    ───  •        •        ───┐  ────────   ────┐── ┌┐─────┐  ─┐─┐┐
                │░│░  ░   ░ ░ ░░  ░── •░░  ░░░░ │░│   •░    • ░       │        ░ ───    │  ─┼┘     │ │ │ └┘┐
                └─┘       • •       ░       ──  │ │   ░     ░        │       │          └─  │      └─┘  •  │
                │    ───   │  ░    ─── ─────  • ░ └──────░ ───  ░ ┌──┘─   ░• │░ ░  │░ ░░░ ░ │░   ░░░   ░░░┌┘
                └──── ░ ──░└┐─   •              ──                │             ── └─ ──  • │     •      ─┘
                │           │     ───┐   ──────┐     •   •  ──         ────   •      •  •    ────   ──┐─┐  │
                │░──────░░░─┘──░──   └─┐ ░░░ ░░└─────░── ░░░░ ──░────┐░░░░░── ░────░░ •░░░───░░░░───  │░│ ░│
                │░░░░░░░───░ ░░•░░░ ░│ │░──░───░ ░ ░░• ░░•░───░░•  ░ │░────░░── ░░░───░──░ ░░░───░ ░──┘─┘──┘
                 ──────          •    ─┘─  •   ─── ── ─── •   ──  ──           ────       ───     ──
                                  ───┐                                   ───
                        ┌─────────░░░└──────────────     ──┐  ┌───────── ░░░───┐───────────    ───
                        │░░░░░░░░       ░░░░         ───   │  │░░░░░░░░   •    │░░         ────   ─┐
                        └┐─── ────────────────── ─── ░░░░• │   │░•  •         ─┘───────    ░░░  │  │
                         │                      •    ────      └─    ──     ──         ─────────┘  │
                        ─┘                                             ──┐   ░ ░ │                 │
                         ▒░ •  ┌──────                 ░   │   ┌─┐─┐───░░└─ ─────┘                 │
                        │    ──┘                           │   │░│ │░░ ░ │ •     │        ───────  │
                        └───┐              ┌──┐            │   │░░░ ░░ ░│░• ░ ░░░  ┌─────┐       │ │
                        │░░▒│              │▒░└───────────┐    │░░ ░░░ ░│ ░ ┌──────┘     │       │ │
                        │░░▒│             •▒▒▒▒▒▒▒▒▒░░░░░░│    └──────── ───┘       ── ──┘       │ │
                        │░ ░│              │░▒┌───────────┘   │                                  │ │
                        └───┘        ─┐─── └──┘               │                              ────┘ │
                              •    ─┐ │                       │ ┌───┐─┐─┐─┐─┐──────┐──┐──┐───      │
                             │      │ │            ░       ───  │   │░│ │▒│ │▒▒  ░▒│ ░│  │        ┌┘
                             └──────┼─┘─┐─┐                                  ─┐░┌──┘──┘──┘──     ┌┘
                            │       │ ░ │█└────────────────────────────────── │▓│           ─────┘
                            │  ┌────┘── │█│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─┘
                            └──┘        │▓└────────────────────   ─────────────  ──────────    ──┐
                                        │▓│                    ░░░░░░░░        ░░░          ──   └┐
                                        │▓│                 │  ──  ───   ──────────────────┐░░░•  │
                                        │▓│                 │     •   ───                  └─── │ │
                                        │▓│                 │                ░░░░░░│            │ │
                                        │▓│                 │  ┌─┐ ┌───┐         ──┘            │ │
                                   ───  │█└─────────────────┘┐ │░│ │░ ░└┐────┐───  └────        │ │
                                     ░░ │▓│▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒│ │░░░ ░░ ░│░░░ │░░░░░      │      │ │
                                   ──── │▒└─────────────────┐┘ │░──── ░┌┘─ ──┘───────────┘      │ │
                                        │▒│                 │  └─    ──┘                        │ │
                                        │▒│                 │ │                                 │ │
                                        │▒│                 │ │                               • │ │
                                        │▒│                 │  ─────────────────────────────── ─┘ │
                                        │▒│                 └─  ░░  ░░░  ░░ ░▒▒  ░░ ░░░  ░░     │ │
                                        │▒│                        │  │  •   •    • ───  │        │
                                        │▒│                  ──┐───┘──┘─       ░░░ •   ──┘────────┘
                                        │▒│                 │  │░         │   ────         ░░     │
                                        │▒│                 │  └──────────┘░•          ──────── │ │
                                       │▒▒│                 │              •        ░░│         │ │
                                  ┌─┐─ │▒•                  │  ┌──────┐─┐   ──────────┘         │ │
                                  │ │░  │▒────────────────┐─┘┐ │░   ░ │░│                 ──────┘ │
                                  └─┘── │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│▒░│ │       ░└───── ──────────┐      │ │
                                         ─────────────────┘─┐┘ │░ ░░░░░░ ░    •          │      │ │
                                                            │  └─────────────  ──────────┘      │ │
                                                            │ │                                 │ │
                                                            │ │                                 │ │
                                                            │ └┐─────────────────────────   ─── │ │
                                                            │  │    ░░  ░░  ░▒░ ░░░  ░    •    •  │
                                                               │    ──  ──────────────┐─── ──── ──
                                     ───┐─────────┐──────┐─────┘─ ──  •               │        •
                                       ░│       ░░│░░░  ░│   ░  ░░   ░░│ │░░  ░░░░│ │░│
                                      ──┘─────────┘──────┘─────────────┘─┘────────┘─┘─┘

















```

*Figure from page 18 (2346x3317 px)*


---



4203-E P-295



SECTION 2 PROGRAM OPERATION



15-4-5. Effects of the Editing Modes



(1) Overwrite Mode



In the overwrite mode, the positions of characters in the character string are fixed and the file name



selected from the directory is written over the part of the character string that starts at the position of



the edit pointer.



(2) Insert Mode



In the insert mode, the part of the character string that starts at the position of the edit cursor shifts to



the right as the file name selected from the directory is inserted to the left of the edit pointer.



If the command length is caused to exceed 255 characters by adding the file name, the 256th and



subsequent characters are deleted.



Directory selection screen



IA'f'<



CO~WHt:t



'\. EDIT l'OINTER



IICEX SEl.ECTIOk



"'°'



P001.IUH



f'OOJ.Ht



!'005.MIN:



PC07.Mltl



?:m . .lll:Oj



PO!t.lll



P01l.lfl:II



P01$,lllti1



POl'.l'.11111'1



Directory selection screen



[Pf01WI ?'§Y;Tl<Ji



o:)~illN;



'\.EDIT POINTER



11()(€ S l<tf



RX);



f'COl.VlN



f'COJ.jilll



POOS.¥111



1'iXl~.1m1



P009.IUII



P01LIIIN



?013.llltf



P015,IIIIN



A:,17,Vlli



/MIE:lIF



OVERWRITE MODE



P0:12.llt ..



?OOC . .lffH



"""1



=::::



/CURSOR



POll'J.IIUt



IWBI



INSERT MODE



POOZ.IIIN'



P(X)¢,IIH



~:::: /CURSOR



P()l(),lilllf



P0'14,li11N



P01G.ltllf



?018.IUH



Command creation screen



l!Gc): DI SlU.Y ~



{F2] -> ll)t:•.llinl



(FJ] -::> ,W:•.•11t



TO 01$1\.A'I' 0~ l,aJCES.AFTER flf£SSUC; [Fl).



!IPJT lHE OE\IICE it.VE Ne Fil.I NAME.MN Pf£SS DIJRltt] K'€!.



,OOFJUl...i CEVICE 1NE • IOI:



tEFillll.T FH..E ~ .., •.MIN



Command creation screen



H()EX D1$P<..,A,Y ~



l.e'2J -> IDJ:<".ltlll



(Fl)-> FO():"',ll!ll'J



1~ C>ISPU't G'l'HER ltcE'(ES.~ PFESSU<I (Fl],



lrf'U'f rt!E.



0£V!C'£



!WE .I.IC) Flt.£ K411e. n£H ~SS



(WR11tl U"'I'.



OCF.Q.T DEVICE IWIIE "" IQi:



OZFAIJI.> FILE fWE'. - ".lillf



Fig. 2-17 Effects of the Editing Modes



!l§ffiT


```text


                                                                                                ───       •
                                                                         ┌──┐────┐───┐──────────░░░──────┐░│
                                                                         │░░│░░░░│ ░ │░░░░░░░░░░───░░░░░ └─┘
            •    ──     ───         ──     ────────────────────────────── ──┘────┘── └─────────
           │ ────  ───┐─   ───────┐─  ─┐───                                                                 │
           │    ░──  ░│           │    │    ────────────────────────────────────────────────────────────────┘
           └─────   ┌─ •   ──  ─┐ └─  ─┘─  •
                  │ │ │  ──  ─┐ │    │   ──
                  │ │ │    ░  │ │ ░──┘
                   ─┘ │          •     ──   • ──┐─    •  ──────      │          ┌── •            ─────   ──
                       ──── ───── ────   ──  •  │ ───  ──   ░   ──── └────────┐─┘░ •░────────────    ░───░░─┐
                       ░░░░░░░ ░░  ░░ ░░░░░░░ ░ ░░░░░  ░░░ ░░ ░░░ ░░░░ ░░░░░░░│ └─░░ ░░░ ░░░░ ░ ░ ░░░░░░░──░│
                      ───────────░░┌────────────────────────────────────────── ─┘ ───────────────────────
                  ──┐            ──┘
                   ░│ │ ┌─  ░░ ░
                  ──┘ │ │ •      ────┐───────────┐────────┐─┐─── ──────────────  ───┐─ ───────┐  ───────────
                      │ ░░░• ░░│ ░ ░░│ ░░ ░░░ ░ ░│  ░ ░░ ░│ │░░ •░ ░ ░░   ░░░  ──  ░│ • ░ ░ ░░└──       ░
                      └───┐  ──┘─ • ─┘ │   ──┐      •   ──  └─                   ░                     ──────
                      │   │░•          │     │░   •                         ░             │░ ░ • ░  ──
                       │░•             │░░   └─    │     │ │ │ ░                       ░│ │   │ │  •░   ───┐
                       │                    •   • ─┘   ──┘─┘─┘────────────── ─────░─────┘─┘  ─┘ └─  ────   │
                       │░ ░░░ ░   •░░░░ ░░  ░░ │░░░░░┌─                     •     •        ──  •  ──    ───
                       └─          ── ─────────┘─────┘
                                  •  │                                ────
                        ░─────────░░░└─────────────     ──┐  ┌──┐───── ░  ─────────────      •
                          ░░░░░░░   •   ░░░░       ─────  │  │░░│░░░░       ░░░░       ────── │
                         ─┐░•   ──    ──────        ░░░░  │   ──┘──  │ ─── ──────       ░░░░  │
                          │░░ •   ────      •      ░─┐───          •░│    │             ────   │
                         ┌┘  ░░░│░░░░░       •       │   ─┐   │       ─┐  │░░░░              │ │
                         │▒░ ───┘─────         ──────┘──  │   └─┐ ───░░└─              ───── │ │
                         │                 ┌─           • │   │░└─ ░ ░ │  ─┐─┐──┐──┐──┐      │ │
                         └───┐             │░─┐           │   │░░░ ░░░▒░░░░│░│░░│  │  │      │ │
                         │░░░│             │░░└───────────┘   │░░───░──────┘─┘──┘──┘──┘      │ │
                         │░░▒│            •▓▒▓│▒▒▒▒▒▒▒▒▒▒░│  │ ──   •                        │ │
                         │░──┘    ───      ───┘───────────┘  │                               │ │
                          •   ────   •                       │   ───      ─── ──┐─── •       │ │
                                      •                       ──   ░•  ░──░░░•░░│ ░░  ───  ──  │
                                        ┌─┐                            ░░ ──░░ ░└──    ░      ─┘
                                     ┌─ │█└───────────────────────────────  •█┌─      ───   ──
                                     │░  •▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒─┘
                                    ─┘──  ───────────────────────────────────
                               • ───
                        ┌──────░•░░░░──────────────   ────┐  ┌──────── ░░░─────────────     ──
                        │ ░░░░░░░  •    ░░░░        ──    │  │░░░░░░░       ░░░░        ──    │
                       │ ─┐░──────   ────────┐     •░░ ──┐   └─────       ───────────── ░░──  │
                       │  └─      ──         └┐    ░──   │         ──░•                  •  •  │
                       │ ─┘  ░░░░░░░░         │  • •   ┌─┘           •░░░ ░░░░░              │ │
                       │  ░ ─┐────────────     ──   ──░│  •   │░   ──░░──              ──────┘ │
                        •    │              •            •    │  ──░ ░   ──┐──┐─┐──┐──┐      │ │
                         ┌───              │░░│               │░░░░░░░░░░░ │░░│░│  │  │      │ │
                         │░░▒│            ┌┘░░└───────────    │░───░░──────┘──┘─┘──┘──┘      │ │
                         │░░▒│            │▓▒▒│▒▒▒▒▒▒▒▒▒▒░│  │ •   ──                        │ │
                         └───            ─┘───┘───────────┘  │                               │ │
                       │     ─┐─┐─┐─                             ─── ─── ──── ────── •  ──   │ │
                       │    │ │ │ │           ░░   ░               ░   ░• ░░░ ░░░ ░░   •   ──  │
                        ── ─┘─┘─┘─┘  ┌──┐─┐                               ── • ──────── ──    ─┘
                          •          │░ │▓└───────────────────────────────  •█│        •    ──
                                     ░░┌┘─▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─┘
                                    ───┘  ───────────────────────────────────

                                              ──┐───── ─────┐───────────────────┐
                                               ░│ ░    ░ ░░░│   ░░   ░░ ░ ░░░░░░│
                                              ──┘──── ──────┘───────────────────┘



















```

*Figure from page 19 (2346x3317 px)*


---



4203-E P-296



SECTION 2 PROGRAM OPERATION



15-4-6. Directory Display Method



(1) To Display NC Memory "MD1:" Directory



Press function key [F2] (MD1: INDEX).



The input examples given below show how to designate which file directory is to be displayed.



[F2]


#### MD1: *.MIN

When function key [F2] (MD1: INDEX) is pressed, the directory {in NC memory) for MD1: related



files with extend names of "MIN" {work programs) will be displayed.



[F2]



MD1: *.SDF



When function key [F2] (MD1: INDEX) is pressed, the directory (in NC memory) for MD1: related



files with extend names of "SDF" (schedule programs) will be displayed.



[F2]


#### MD1: *·*

When function key [F2] (MD1: INDEX) is pressed, the directory (in NC memory) for all MD1:



related files will be displayed.



{2) To Display Floppy Disk "FOO:" Directory



Press function key [F3] (FOO: INDEX).



The input examples given below show how to designate which file directory is to be displayed.



[F3]


#### FOO: *.MIN

When function key [F3] (FOO: INDEX) is pressed, the directory (in floppy disk) for FDO: related files



with extend names of "MIN" (work programs) will be displayed.



[F3] ---;,fOO: *.SDF



When function key [F3] (FOO: INDEX) is pressed, the directory (in floppy disk) for FOO: related files



with extend names of "SDF" (schedule programs) will be displayed.



[F3] _.. FDO:



*·*



When function key [F3] (FDO: INDEX) is pressed, the directory (in floppy disk) for all FOO: related



files will be displayed.



(3) To Display Other Directories



When function key [F1] (INDEX) is pressed, "ISO" will be displayed at the console line. Following



the "ISO" character string, enter the desired device name and file name, then press the {WRITE]



key. The following examples apply when an OSP formatted floppy disk is being used.



>ISO MD1: {WRITE]



The directory for the default file name at the MD1: device will be displayed.



The default file name is indicated at the directory display procedure.



>ISO FOO: [WRITE]



The directory corresponding to device "FOO:" is displayed.


```text


                                                                                                ──        •
                                                                         ┌──┐──────┐─┐───┐──────░░───────░░│
                                                                         │░░│ ░░░░ │ │░░░│░░░░░ ── ░░░░░░──┘
                 •                       ┌───────────────────────────────┘──┘──────┘ └───┘─────
           ┌─────  ──────────────────────┘
           │░ ░  ─┐░                ░    └──
           └───── │ ┌─┐─ │  │  ─┐  │ ┌─  │
                    │ │  └──┘── │  │ │      ┌──┐  ┌───────┐
                  ──  └──   ░  ─┘ • │  ┌──  │  │  │      ░│
                      │   ────      └┐ │░ │ │░•  │      ┌─
                      │            ─┘┘─   └─   ──┘      │ ─────┐─── ───────────── ── ──
                      │ ░   │        ░   ░             │       │   •          ░     •  ─────   ┌────────┐
                      │     │     ┌───    ┌────────────┘       └──    ┌────────────  ──     ── │        │
                      │ ──┐   │░  │   ──  │                         │ │                       ─┘  ──────
                      │   └───┘   └─ │   ─┼─ ┌─   ┌─────┐           │░│ •                        •
                      └┐──   ░ ─┐    │   ░│  │░── │░ ░ ░│                ──      ──┐   ───── ── │ │ ───────┐
                       │      │ │ ─┐       │ └─░ •      └─┐─┐─────┐ ┌──     ─────  └───        ─┘─┘─    ░  │
                      │ ░ ░ │ │ │░░│   ░░░░│   •░ ░• ░░░│ │ │░░░░░│ │░ ░│ │░░░░░░░┌┘   ─────         ──────
                      │  ─┐─┘┐┘ │ ─┼─┐     └─── ─── ────┘─┘─┘─────┘─┼─┐─┘─┘───────┘
                      │ ░░│  │ •░• │ │░ ░░░│                        │ │
                      │   │          │     └─┐─── ──────────────────┘┐ •  ── •    •   ──────┐───┐─┐───┐────┐
                       │░ ░───┐ ┌────┘─────  │░  •░░ ░ ░  ░ ░░░░░░  ░│ ░ ░░░░░────░───░░░░░░│ ░ │░│   │░░░░│
                       │░─┐ ░░│ │░░░░ ░░ ░░│ └─ ░░░• ░░░░░░ ░ ░ ░░░░░░░────── ░░░░░░░░──────┘───┘─┘───┘────┘
                      •   │ •  •  ─┐  │ ┌──┘─  ──── ────────────────┐─┐       ────────
                     •  ░░│   │░░│ │░ │░│                           │ │
                      │   │   │  └─   │  ┌──────────────────────────┘ └┐─┐──────┐─┐───┐──┐─┐──────┐─┐──┐──┐─
                      │░░░░░ ░ ░░░░░•░░░ │ ░  ░░    ░░░░░░ ░ ░ ░░░░░  ░│ │░░░░ ░│ │  ░│  │░│ ░ ░ ░│ │░ │░░│
                       ──────────── ░─── └──  ───┐ ────────────────────┘─┘──────┘─┘───┘──┘─┘──────┘─┘──┘──┘─
                  •   │                          │
                 │ │  │     ─┐  ░          │  │  └───────
                 └─┘  │ ──   └──     │ ────┘  └┐ │
                      │ ░ • ┌┘     • │ ░   ░   │ │░ ░ ░│
                     •     ─┘   ───  │    ─┐ │ │       └─────  ─────────┐──────┐─────────────────────────
                      │ ░ ░░░│ •░░░░░░• ░ ░│ │░░░░ │░ ░   ░░ • ░░░░  ░░ │░░ ░ ░│  ░░ ░
                      │    ──┘┐  ┌─┐── │ ┌─┘─┘─────┘─────────  ─────┐─┐─┘──────┘─────────────────────────
                      │ ──┐   │ ░│ │  ░│░│                          │ │
                      │   └┐──┘  └─┘     └─────┐─┐──────────────────┘─┘───┐─  ─┐────────────────────────────
                      │░░░░│ ░ ░░ ░ ░░░ ░░░ ░░░│ │░░░ ░ ░ ░░░░░ ░ ░   ░  ░│ ── │░       ░ ░  ░ ░        ░
                       ┌───┘─┐ ───┐────────░ ─┐┘┐┘─────    ─────          │   ┌┘────────────────────────────
                      ┌┘     │    │        •  │ │      ─┐░│     ── •    ░ ░░ ─┘
                      │░░─┐ ─┘░ ─┐┘  ────       └──     └─┘────     • ┌──────
                      │░ ░│     ░│ • ░░░ •         ┌───               │
                      └┐──┼─┐  •      ─┐  ─────┐ ░ │░    ──    ─┐ ── ─┘─ ──     ───────────── ─────────────┐
                       │  │ └──        │      ░│   └────┐  ──── └─         ─────                     ░   ░ │
                      ┌┘░│  ░░░░│  ░░░░│ ░ │░ •  ░░ ░░░░│ ░ ░░ ░░░  ░░ ░│ ░░░░░░░────────────  • ──────────┘
                      │  │ ─┐─┐ │ ─┐───┘───┘──  ────────┘───────────┐─┐─┘────────
                      │░ ░│ │ │░░│ │  ░                             │ │
                      │   │      │      ─────────┐──────────────────┘─┘─────┐─┐──┐─┐───┐─┐──┐──┐──────┐────┐
                       │  ░ • ░░░░░──░░ ░ ░    ░ │░ ░ ░   ░ ░░░░   ░░ ░ ░░░░│ │  │░│░░ │░│ ░│ ░│  ░░  │░░░░│
                       └────░──────░░──────    ── ──────────────────────────┘─┘──┘─┘───┘─┘──┘──┘──────┘────┘
                 ┌─┐ ┌─                    ───┐
                 │░│ │░░ ░░░░░░ ░░░░  ░ ░ ░░░░│
                 └─┘ └─                       └───── ───────   ──┐─┐─────────────────────────────┐─┐──────
                       ┌─░░─── ░░───────░────░░░░░░ • ░░░░░░──┐░░│ │░ ░░ ░░░░░░░░ ░ ░░ ░  ░  ░ ░░│ │ ░░░░ ─┐
                      ┌┘░┌─░   ─┐       •░   ────── ░ ──      │           ── ──────  ┌─               ░   ░│
                      │  │ ─┐░• │                    │    │   │   •     ──          ─┘   ───   ── │ ───────┘
                      │░ │  │ ░    ░░ ───── ░ ░│ │░░░│ ░ ░│ ░    │  ░░ ░░░░  ░░░░  ░░│ ░ ░░░░ ░░░┌┘─
                    ┌┐ │  │  │ │  ─┐       ┌───┘─┘───┘────┘──────┘──┐─┐──────────────┘───────────┘
                    └┘ │ ░└─ │░│ │ │░░░░  ░│                        │ │
                     │ │ │  ─┘   └─        └──┐────┐───────────────┐┘─┘─────────┐───────┐
                      •  │ │              ░░ ░│  ░ │░ ░░ ░ ░░ ░    │░░░ ░ ░░ ░░ │░░░░░░ │
                       • │ │                ┌─┘    └───            │             ─┐─────┘
                          │          ─────  │      │ ░           ░ │ ░ ░        ░ │
                    ┌┐ ┌─ └───    • •      ┌┘──────┘───────────────┘──┐───────────┘
                    └┘ │ ░│        •░      │                          │
                     └─┘         │           ───    ──── ░        ────┘──┐
                       └─────  ──┘───── ░ ───   ────    ────────── ░ ░░  │
                             ──        ───    ──    ───           ───────┘














```

*Figure from page 20 (2346x3317 px)*


---



4203-E P-297



SECTION 2 PROGRAM OPERATION



The message "ERROR IN SPECIFIED DEVICE NAME." is displayed on the console line and the



directory selection screen ls displayed.



It is not allowed to use wild card "*" or"?" when specifying a device name.



>ISO FOO:*·* [WRITE]



The directory of all files in floppy "FDO:" is displayed.



The same happens if any of the following are specified as the file name:"*"·"*·","·*"•".".



>ISO FD0:*.MIN [WRITE]



The directory of all files in floppy "FDO:" with the extension name "MIN" is displayed.



>ISO FD0:???.MIN [WRITE]



The directory of all files in floppy "FOO:" whose main file name consists of three or fewer



alphanumeric characters and whose extension name is "MIN" is displayed.



>ISO FD0:ABC.* [WRITE]



The directory of all files in floppy "FD0:" whose main file name is "ABC" is displayed.



The same would happen if the specified file name were "ABC" or "ABC.".



>ISO FD0:ABC.?? [WRITE]



The directory of all files in floppy "FD0:" whose main file name is "ABC" and whose extension name



consists of no more than two alphanumeric characters is displayed.



>ISO FD0:MS*.TXT [WRITE]



The directory of all files in floppy "FD0:" whose main file name starts with "MS" and whose



extension name is "TXT" is displayed.



>ISO FD0:MS??.TXT [WRITE]



The directory of all files in floppy "FOO:" whose main file name starts with "MS" and comprises a



total of no more than 4 alphanumeric characters, and whose extension name is "TXT" is displayed.



>ISO FD0:ABC.MIN [WRITE]



The file "ABC.MIN" in floppy "FD0:" is displayed (assuming this file exists in the device).



>ISO FD0:123.* [WRITE]



>ISO FD0:ABCDEFG123456789.* [WRITE}



The message "ERROR IN SPECIFIED FILE NAME." is displayed.



In the OSP format, main file names must start with a letter of the alphabet and consist of a total of



no more than 16 alphanumeric characters.



>ISO FD0:*.123 [WRITE]



>ISO FD0:*.ABCD [WRITE]



The message "ERROR IN SPECIFIED FILE NAME.» is displayed.



In the OSP format, extension names must start with a letter of the alphabet and consist of a total of



no more than three alphanumeric characters.


```text


                                                                                                ──        •
                                                                          ┌─────┐─┐───┐──┐──────░░•░──────░┌─
                                                                          │░░░░ │░│ ░ │░░│░░░░░░──░•░░░░░░░│
           ┌──────────┐───  ───  ─────── ─────────────────────────────────┘─────┘─┘───┘──┘──────     ──
           │          │░░░──   ──  ░░░░░•░░░░        ░░
           └─────────┐┘─┐ ░    ░░     ░░░  ░│                          │ ───              ──         ────
                     │  │ ░ ─┐─  ──        ░└─┐─┐──────────┐───────────┘    ──────────────  ─────────    ──
                       │  ┌┐░│ ░░░░│ ░░░░░ •  │ │░   ░  ░  │░ ░ ░  ░░░░░│                             │
                       │ ─┘┘─┘─ ─┐░│   ┌─┐─   │ └┐       ┌─┘────────────┘─────────────────────────────┘────
                       │         └─┘   │ │   ░│  │░  ░░  │
                       └─      │ │  • •          │ ┌─────┘  ─┐───┐─┐─────────────────────┐
                       │       │         ────      │         │   │ │░░         ░      ░ ░│
                      │ ┌──────┼───┐─ ───   ░──┐ ──┘         └───┘─┘── ┌─────────────────┘
                     ─┘ │ ░    │░░ │   ░░░░──░ │     ┌──  •            │
                       ─┼───┐   ───┘─  ──┐─    ░───┐─┘░░─┐ ────────── ┌┘
                        │   │            │ •  •  ░ │     │      ░ ░   │    •               •
                        │   │             •  │   ──┘  ░   •        • ░└┐───  │ ░┌─┐───┐ │ │ │
                        │    ──             ─┘      ──────          •  │   ──┘  │ │   │ └─┘─┘
                     ┌┐ └───    ──────░─────░ ┌─┐         ──         │ │             •
                     └┘ │ ░ ─┐─ ░░ ░ ░░   ░░──┘░│ │                  │ │           ──
                       ─┼───░│   ────── ────  └─┘ └┐         ░  ─────   ──────────┐  │ ───────────
                        │                          │        ───                   └──┘─    ░  ░
                     ┌┐─┼──░  ───── ░ ───░──────░  │                   ┌──   ───       ──────────
                     └┘ │ ░│    ░░  •  ░░░ ░░░░░░ ░│     ────          │
                       ─┼──┘   ─── │ │ ───  ─┐────      •      ┌────   └┐ │ │ ┌── │    ─────── ┌───────────┐
                        │          └─┼─   •  │     ────┐ ┌─────┘    ──  │ └─┘ │   └────░       │           │
                       •░░░░░ │░░░ ░ │░░░░░░ ░ ░│ │░░░░│ │░░░░░░░ │░░░ ░│ │░│░ • ░░░░░░░░─────  ─────── ───┘
                     ┌─ │   ┌─┘    ┌─ ┌───┐ ─┐─ │ └────┘─┘────────┘──┐─┐ ─┘─┘── ─────────
                     │  │░░░│ │ ░░ │░░│   │░░│░░░•                   │ │
                     └─ │ │  ─┘    └── ┌─┐┘┐─┘─   ──── ──┐─┐─────────┘─┘┐────────┐───┐───┐───────┐
                       •  │ •░░░░ ░ ░  │ │░│ ░ │░░░░  • ░│ │░░░░░ ░░░  ░│ ░░ ░ ░ │░░░│ ░ │░░░░░░░│
                        ┌─┘  ────     •  │    ─┘ ┌─    • └┐┘┐───        │ │  ┌─┐ └┐  │ ┌─┘───────┘
                        │  •     ┌─ •    └──┐  │ │  ░░   ░│ │░  ░ ░  ░░   │░░│ │  │░ │ │
                     ┌┐ └─   ─┐  │ │ • ──   └┐ │ └────────┘─┘──────────┐──┘──┘─┘─ └──┘
                     └┘ │░░ • │  │ │ ░•   •░░│ │░│                     │
                      │ │░  ░─┘  │  •   ── ─┐    └─ ┌──┐─ ┌───── ─────┐  ──    ┌──  ─────────────────┐──┐───┐
                       │   ── │          ░  │ ──░░░─┘  │  │  ░░ •░░░ ░│ •░░░───┘░░   ░░ ░░ ░░░ ░░░ ░░│  │░░░│
                      ┌┘░░•░░░└─┐┐ ░   ░░ ░░░ ░░──░░░░░ ░░░░    ░░ ░░░│ ░──░░░░░░░───────────────────┘──┘───┘
                     ┌┘ │   ┌─  └┘ ┌─        ──    ┌─────────────────┐┘    ───────
                     │  │░░░│ │░│░ │░░░  ░░ •░░• •░│                 │ │
                     └─      ─┘     •        ── │   •  ─────  ───────┘─┼─┐─┐─┐───┐─┐───┐─┐─┐─┐──┐─┐───┐─────┐
                        │░──┐░░░░░─┐ ──░│ │░░   └───░──░ ░░░  ░░ ░░   ░│ │░│ │░░ │ │░░░│ │░│ │░░│ │░░ │░░░░░│
                        │░░░│░────░│ ░ ░│ └── ░ ░░░░•░░░────  ─────  ──┘─┘─┘─┘───┘─┘───┘─┘─┘─┘──┘─┘───┘─────┘
                      •      •           │    ──     ───
                     •  │░░   │░ • │░──  │░│ │░░░░░                    │
                      │ │   ──┘ │ ┌┘   ──┘ │ └─┐    ─┐───┐─┐────┐─┐────┘┐──── • ───┐─┐─┐─┐─┐       ──────┐─
                      └─░░│ ░░░ │░│ ░ ░░ ░░░ ░ │ ░░│ │░░░│ │░░░░│ │░  ░░│ ░ ░• •░░ │ │░│ │░└───────      │ ─┐
                        ──┘─────┘─┘ ───────  ┌─┘───┘ └──┐   ────┘ └──  •             │   └─┘                │
                      │                      │      •   └─                  •   •  ──┘      ──────  │░  ░│ ─┘
                      │ ┌─────┐░─────┐─────── • ░░•       ──────────── ┌──── ─── ──   ─────       ──┘────┘─
                      │ │ ░░  │  ░ ░░│ ░░░░░░░░░ ░░ ─┐                 │
                       ─┘───  └──────┘───────  │ ─┐  │     ───────────    ── ── ─────────── ────────┐
                                             • │  └──┘    •   ░        ┌─   •                       │
                      ──┐──┐  │ ── ┌────────   │             ──────────┘ ───     ────────── ────────┘
                     │  │░░│  │  ░─┘░░  ░░░░░ ░│                       │
                     │  │  └─    • │░   │       ─────┐─  ┌──── ─┐      │
                     └┐ │ ░      ░ │░  ─┘──░   ░░░  ░│ ──┘░ ░   │      │
                      │ │  │ •     └─░  ░ ░┌─░ │  ░  │    •  │  └────  └─────────┐
                       │ │░│     ░░│ ──────┘ ─┐┘────  •░•  ──┘  ░ ░░   ░  ░░░░░░░└┐
                       │ └─┘ ┌─────        │  │                 │ │   │ │ ─── ──  └─────────────────────────┐
                       └─   ─┘      │ ───┐─┘──┘───────────── ┌─ └─┘ ──┘ └─      │   ░   ░               ░░  │
                      │    •░░░ ░░  └─ ░░│░░░  ░░░  ░░░░░░░░┌┘         •     ───┘───────────────────────────
                      │   • │                 • ────────────┘
                     ┌┘─┐─░░│ ────── ┌────────░•              ──────┐─┐
                     │  │  │ │       │          ──                  │ │
                     └┐ │░░└─┘░░░░┌─ │▒░░░ ░░░░░░░                    │
                      │           │  │            ─────────────────── └──┐───────┐
                      └┐░───░░░░░░└──┘░░───┐────░░░░░░ ░░ ░░░░ ░░░░▒░  ░ │░░░░░░░│
                       │     │             │                    •  ┌─ ─── ──   • └┐─┐─┐──────────┐───┐───┐──┐
                       │░ ┌──┘░░──░░ ── ░░─┘─░░───░░░░───░░•░░░│ │░│ │░░░│  │░│ │░│ │░│ ░░░░░░░░░│ ░ │░░░│ ░│
                       └──┘░░░──░░─── ░───░░░── ░ ────░ ░──░░──┘─┘─┘─┘───┘──┘─┘─┘─┘─┘─┘──────────┘───┘───┘──┘
                            •   ──        • •   •     ──   ──










```

*Figure from page 21 (2346x3317 px)*


---



4203-E P-298



SECTION 2 PROGRAM OPERATION



>ISO FD0:\ABC\*-* [WRITE]



If a path name is specified although the device to be selected is OSP format, the message "PATH



NAME CANNOT BE SPECIFIED IN THIS DEVICE." will be displayed on the console line.


```text


                                                                                                ──       ──┐
                                                                         ┌─┐─────┐─┐─┐──────────░░───────░░│
                                                                         │░│░░░░░│ │ │░░░░░░░░░░── ░░░░░░──┘
          ┌──────────┐┐─── ───   •   ────────     ────────────────────┐──┘─┘─────┘─┘ └─────────      ──
          │          └┘░░░•   ─── ─┐─░░░░░░░ ─────       ░            │
          └──────────┘   ░░   ░ ░  │░░      │░░░░                                        •   •       •
                     └┐     •      └── ───┐─┘░  ░   ─┐────┐─── ──────────────── ────────  ┌── ────    ─────┐
                      │  ░ ░░│  ░ ░     ░ │░ ░ ░░  • │    │░  • ░      ░       • ░░     • │       ───  ░░  │
                       │   ░┌┘       ░ ░│ │ ░       ░   ░ │░                │                        │ ────┘
                       └────┘ ──────────┘─┘──────────── ──┘────────────░• ░ │ ░ ░░ ░  ░ │░    ░░░░ •░│
                                                                       • ───┘───────────┘────────── •







































































```

*Figure from page 22 (2346x3317 px)*


---



4203-E P-299



SECTION 2 PROGRAM OPERATION



15-5. Selecting Files From Directories (MS-DOS Format)



When working with the MS-DOS format-for example in the machining management mode and MS-DOS



file convert - it is possible to display the directories of MS-DOS format floppy disks.



15-5-1. Procedure for Selecting Files from Directories



(1) At the Command Creation screen, press one of the following function keys:



[F1] (INDEX), [F2] (MD1: INDEX), [F3] (FD0:INDEX)



If function key [F1] (lNDEX) is pressed, "ISO" will be displayed at the console line. Fallowing the



"ISO" character string, enter the desired device name, path name, and file name, then press the


#### WRITE key.

(2) At the directory selection screen, use the cursor keys to locate the cursor at the file name of the



file to be selected.



(3) Press the WRITE key.



The display will return to the command creation screen and the device name, current directory



name, and file name selected with the cursor, are entered on it at the position of the edit pointer.


#### Command creation screen

lf'PBYC OPfflATl!!t



ttr



COffilIB :qF(



co 'EDIT POINTER



llaX OlsPI.AY l'A0CEW'E



11'2) -> 11)1:•.•



[Fl)



-> Fm:•. •



¥Hr§ t;gWEffl'



TO DISPV.Y OllER INCaeS,Af!'!I! l'!e$1NG D'l].



llFIIT 1l£ OEV!CE NAIIE Mfl FILE !WE. 1liEII PRESS (Wl!TEJ ID.



Deill.l.Ttli.VICEIWIE •


#### DEFAllt.T FILE ME - •. •

omffllJF


#### Command creation screen

lfBIMI oew.rn•



llllEX Dl9V:f l'ROCBlURE



[F?J -> 11:11:•.•



[1'3) -> RlQ:•.•



lfS::QO§CtlfYffl[



TO DISPLAY OTIER llflEXES,AF!eR l'AES$1/lG !Fl).



llf'UT 11£ ll!:VICE !WE ND FlLE IWE.1181 PIESS (aim)



~LT De'IICE IWIE •



tEFAlll.T FJlE MME - •. •



(3)~



Directory selection screen /~



!l'ROGWI DPERAT lg<


#### OVEfffl IT E


#### PYfflffl)JE


# ':fr

8lftl'fBUiB :wer



'-eorr



DEVICE FORMAT



POINTER


#### I !!Et SELECTUIII

FIJO; DIR's


#### PNefl DIRECTIIIIY

A.001.DIR'



AOO:l.DIR'



Alltli,DIA'.



l'IXl!.llN


#### PIXM.IIM

l'tOl,IJN


#### POCll.llN

>'010.IIH



>'012.MIN



AOO!. DIA'\.



-.DIR'



!'001.IIM



f'OCll.1111,



POC:5.IIN /CURSOR



!'007.IIN



?OO!UIN



Fig. 2-18 Procedure for Selecting Files from Directories


```text


                                                                                               ┌──        •
                                                                         ┌──┐─────┐───┐────────┘░░───────░░│
                                                                         │░░│░░░░░│   │░░░░░░░░░──░░░░░░░░─┘
                 ──                     ──           •          ─────────┘──┘─────┘─  └────────       ──
            ┌───┐  ┌──────────────┐─┐───  ┌─────────  ┌──┐──────                                            │
            │░ ░└─ │░         ░   │ │     │         │ │░ │                ┌─────────────────────────────────┘
            └───  • ─────── ░───  │ │   •          ░│  ──┘───────   ┌─ •░ │
                 │                     │ •                          │ │   │  •     ───    ───────┐──────────┐
                 │   ────        ────  │   ┌────  ─┐─────   •  ──┐──┘─┘─  ░• ░── • ░░░ ──┐ ░  ░░ │   ░░     │
                 │░──  ░░────────░░░░──┘───┘░░░░──░│ ░ ░░───░░•░ │░░░░░░ ░░░ ░░ ░░░───░░░└───────┘──────────
           ┌─────                                           ── ──┘─────────────────   ───
           │░░░    •░ ░░░░ ░ ░  ░░░░░░░░  ░░░ ░░• •░░░░░░░░•
           └───── │ ┌─┐                     ┌─┐  • ───    • ────┐───────────────────────┐
                  │ │ │░ ░ ░  ░░  ░░░░ ░░░░░│ │░░░│   ░ ░│ │ ░  │░░  ░░░░░      ░   ░   │
                  └─┘ └┐    ┌─────          │  ┌──┘─┐    │ └──┐─┘     ┌─────────────────┘
                       │░ ░ │░░░░░│  ░░░ ░░░│  │▒░░░│ ░░░│ ░░░│ │░░░░░│
                                  │                                   └─────────────── ──────┐   ──────────
                       ──────────░│ ░ ──┐░░░░░│ ── ░░•░───░░░───░░─── ░░░░░░░░ ░ ░░  ░•░░░░ ░│ ── ░░░░░░░ ░│
                      • ░░  ░░░ ░•░░──░ └─────┘ ░ ─── •  ░ ──   ──   ────░┌──  ────  •░ ──   │    ┌── •   ─┘
                       ───   •  │ •   ──       • •   •  ──    ──  ───    ─┘   •     • •   ───  ───┘  • ──
                      │    ── ──┘
                  ──┐ │   •          ──────┐─┐────┐─┐─┐────────┐──┐─┐───────────┐─┐───┐─┐──┐───┐─┐────┐────┐
                    │ └┐ ░  │ ░░─────░░░░░ │ │░░░░│ │░│ ░░   ░░│  │░│ ░   ░░░   │ │░ ░│ │ ░│  ░│ │░ ░ │ ░ ░│
                      └┘────┘───░░░░░──────┘─┘────┘─┘─┘────────┘──┘─┘───────────┘─┘───┘─┘──┘───┘─┘────┘────┘
                  ┌─┐ │         │
                  │░│ │ ░░░  ░░ │░░ ░░ ░░•
                  └─┘─┘                       •   ─────────────── ────┐ ─────────────┐─ ────  ───── ───────┐
                       ┌───░░░░░──░┌───░░─────░┌─┐░░  ░░ ░ ░░░░░░• ░░░└─ ░ ░ ░ ░ ░░ ░│ •░░░░──░░ ░░  ░░░░░░│
                       │░   ──── ░░│   •   ░  ░│ │ ░  ────  ──── ░ • ░│  • • ──   ───    ┌─    ┌─┐   ───  ┌┘
               ┌─────             • •    ───    • ──      •                 •  ──     ───┘  ───┘ └───   ──┘
               │░░ ░░─────────░░│                          •░░░░░░░ ░░░░░ •░░┌─
               └─             ──┘ ┌────┐──┐────        ───  ──             ──┘  ───────────────      ──┐
              │  ┌──░░░░░░░─┐     │▒░░░│░░│       ────  ░ •   ┌┐───────────     ░░▒░░▒▒░        ────   │
              │  │▒▒┌──────▒│ ──  └────┘──┘─      ░▒▒░░ •  •  └┘░▒░▒░░░░░░    ──────────────   ░░▒░░    │
              │  └──┘           ──          ────────────      ░└────────────░•              ──────────  │
              │  │   ░─────── ░░                                            •  ░░░ ░░░░░░░            │ │
              │   ── ░░  ░░░░───                         │     ┌─┐──────  •  ─────────────            │ │
              │  │░░  │░                         ─────── │     │░│  ░░ ░                      ────────┘ │
              │  │░░──┘░──────┐─────────┐───┐───┐        │     │░└─────────────┐───┐──┐──┐───┐        │ │
              │  │░░ ░ ░░░░▒░▒│░░ ▒▒░▒░░│  ░│   │        │     │░░░░░░▒░▒▒░▒░░░│▒░▒│░░│ ░│   │        │ │
              │  └┐░┌─░░░ ░┌──┘┐────────┘───┘───┘        │     │░│ ─── ░┌───┐──┘───┘──┘──┘───┘        │ │
              │   └─┘ ─────┘   │                         │     └─┘─   ┌─┘   │                         │ │
              │ │            ──┘                         │░  │        │    ─┘                         │ │
              │ │                                        │░  │                                        │ │
              │ │                ──  │ •                 │░  │          •                        • ── │ │
              │  ─┐──────┐────┐──░░──┘─░────────┐───┐────  •  ────── ───░ ─────────────────────── │  ─┘ │
              └┐  │░░   ░│   ▒│ ░░░░  ░░░  ░░░  │░░ │     │ │   ░░   ░▒░• ░░░ ░░░░ ░▒░  ░░░  ░░░  │   │ │
               └─  •    •            ░      ── ─┘─┐─     ─┘ └────── ────  ──── ──┐─┐─── •   ────── ───
                 │  •    │░ ░░░│ •  • │           │     │                        │█│     ──┐
                 └── ─┐─┐┘──┐░ └─ ── ─┘─────────── ─────┘                        │█│    ░░▒│
                      │ │   └─┐                             ──┐─    ──────────┐  │█│    ───┘ ┌───────
                            │█│                               │░─┐──░░░░ ░░░░ └┐─┘▒└────     │       ──┐
                            │█│                            │  │░░│░░░░░•  ──── │░░░ ░░░             │  └┐
                            │█│                            │░ │░░│░░│░• ░│      •  ────      ──────┐┘  ░│
                            │█│                            │░ └──┘──┘─ ──┘   ┌──        •      ░░░░│ │  │
                            │█│          ┌─┐               │              ───┘           ──┐┐────┐─░┌┘  │
                            │█│          │ │ ┌──┐─┐─┐      │  ┌─┐─────┐ ░░ ░              ░└┘    │ ┌┘   │
                             ▓▒──────────┼─┼─┘▓▓│░│█│ ───┐─┘┐ │▒│░▒░░░│ ────────────    ───┘     │░│    │
                             ─┐▒▒▒▒▒▒▒▒▒▒│▓│ │  └─┘ │ ░▒▒│▓▒│ │░│ ░┌──┘                           •  •  │
                              └──────────┘─┘ │▓│░ │▓▒┌───┘─┐┘ │░└─░│                ┌───┐             │ │
                                           │░└─┘──┘──┘     │░ │▒│░░│                │▒░░│             │ │
                                           │               │░ │▒░▒│                 │▒░▒│             │ │
                                                           │  │▒░░│                 └───┘────────────┐  │
                                                           │  │▒░▒│   •           ──▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒│  │
                                                           │  └──░│ ──  ─┐────────  ─────────────────┘  │
                                                           │ •   •    •  │                            │ │
                                                           │      │ │  │ │  │ │  │     │  ░ ░  │      │ │
                                      ┌─ ──────┐──────────   ─────┘ └┐─┘ └──┘ └──┘     │ ────  │       ┌┘
                                      │      ░ │            ░        │        │        └─    ──┘───────┘
                                      └─ ──────┘───────────────────░─┘────────┘──────  │
                                                                   •                 ──











```

*Figure from page 23 (2346x3317 px)*


---



4203-E P-300



SECTION 2 PROGRAM OPERATION



15-5-2. Directory Selection Screen (for MS-DOS Format Devices)



Lines 4to 7 The command being created is displayed here.



The selected file name is entered at the position of the edit pointer. The edit pointer



cannot be moved by pressing the cursor keys.



Line 8 If the device is MS-DOS format, "MS-DOS" [s displayed here.



Line 9 The device name for the displayed directory, and the current directory name, are



displayed here.



Line 11 Normally, "PARENT DIRECTORY" is displayed here.



To change the directory to the parent directory, locate the cursor at "PARENT



DIRECTORY'' and press the [WRITE] key.



Lines 12 to 20 : The directory is displayed here.



File names and directory names are displayed ("\'' is appended at the end of directory



names).



If no file name is displayed, it means that the selected device does not contain files.



When the cursor is located at a file name and the WRITE key pressed, the selected



file name is entered at the position of the edit pointer.



When the cursor is located at a directory name and the WRITE key pressed, the



directory changes to the selected directory.



The Command being {



created is displayed



here.



The device name of -+



the directory and



the current dlrectory



are displayed here.



The directory is



displayed here.



co!



"EDIT POINTER



/\001. 0 IR'-.



A003. 0 IR'-..



A005. 0 IR'-.



P002.IIIN



P004.IIIH



P006.IIIN



P008.IIIN



P010.IIIN



P012.IIIN



CURSOR



OVER/iRITE



DEVICE FORMAT



A002. 0 I A'-.



A004. DIR'-.


#### POOi.MiN

P003.IIIN



POOS.IIIN



P007.IIIN



P009.IIIN



P011.IIIN



P013.IIIN



Fig. 2-19 Directory Selection Screen (for MS-DOS Format Devices)


```text


                                                                                                ──
                                                                         ┌──┐─┐────┐─┐──────────░░───────░─┐
                                                                         │░░│ │░░░ │ │░░░░░░░░░░──░░░░░░░•░│
                 ──     ────           ─────  •                 ─────┐─── ──┘─┘────┘ └─────────
           ┌─────  ─────    ───────────     ── ┌────────────────     │                                     │
           │                                   │                            ───────────────────────────────┘
           └───── │  ─┐  ─┐  │ ──   •    ┌─────┘  •             ──── ┌─────┐
                  │ ░░│ ░ │  └─  ─┐░ ────┘  ░░░ ──░    ░░░░  ───   ░─┘     │
                  └───┘───┘──     │                        •              ─┘──┐────┐─┐─────┐─ ┌────┐─┐─────┐
                                  └┐── ░░░░░░ •░│ ░░ ░────░░░░░ ░░░░░ ░░░░░░ ░│░ ░ │░│░░░ ░│  │░░ ░│░│░░░░░│
                                  └┘░ ──────── ─┘ ────░   ─────────────────     •  └─┘ ────┘─ └────┘─┘─────┘
                  ┌─┐───┐         │              •                          ──── ──   •
                  │ │░ ░│         │░░░ │░░░ ░ ░ ░░░░░░░ ░│░──┐ ░░░░░░░░│ • ░░░░░░░░ ░░ ░│
                 •  │   │         │    │         ┌─┐──  ─┘   └── ┌─┐   └─  │  ┌─┐       └─┐──────┐─┐───┐─┐──┐
                  │ │░ ─┘         └────┘──░────░░│ │░ •░  │░░░░░░│ │ ░░░░• │░ │ │░   ░ ░░ │░░░░ ░│ │░░░│ │░░│
                  │   •           │░░░░░░░• ░░░•          └──────┘          •   └─────────┘──────┘─┘───┘─┘──┘
                  └──┐  │         │        •    ─── ─────┐        ────────── ───
                  │ ░│  │         │░░░──░•  •░░ ░░   ░░░░│ ░ ░ ░    ░░░░░░░  ░░░─┐
                  └──┘──┘         └─      ─┐ •                        ────    ── └────────┐─────┐─┐ ───────┐
                                  │ ─── ░ ░└─   • ────────┐ ─────░  ──             ░    ░ │░ ░  │░│     ░  │
                                  │░░░░ ── │  • ░░ ░░░░░ ░│ ░░░░░░░ ░░░──────── ──────────┘─────┘─┘  ──────┘
                  ┌──── ┌─────┐   │          │          ──   ──────────
                  │     │     │   │ ──┐────  └────  •░░   ──           ────────────────────────────────────┐
                   ─── •         •░ ░ │░        ░   ░ ──     │                                             │
                                  │   │ ┌─────────────  ─────┘ ────────────────────────────────────────────┘
                                  │     │                     •
                                  └─────┘ │░     ─┐  ░       │░│ ─┐─ ░ ░•       │ ┌── ─┐────┐ •    ───┐  ─┐
                                          │       │    •     │ │  │    │        └─┘    │    └─ │ ┌─   └── └┐
                                  │░ ░░ ░│  ░░░───┘ ░░░░░░ ░ │░░  ░░░░ │░░ ░░ ░░░░░░ ░░░ ░░░░░░│ │░░ ░░░░░░│
                                  └───  ─┘─────░   ─┐────┐───┘── ──────┘──────┐───  ──      ───┘─┘─  ────  │
                                  │             │   │    │                    │   ─┐  ┌────┐       ──    ┌─┘
                                  │░░── ░░░ │ ░░└─░  ░░░░░ •░ ░ ░ ░░░░│ ░░ ░│ │░░ ░│  │░░░░│ ░░  ░░░░░░│ │░│
                                  └──   ─── │░      ──────     ───────┘ ────┘─┘────┘──┘────┘───────────┘─┘─┘
                                     ───   ─┘───────
                                                      ┌──────────────────────────────────────────────────┐
                                                   │  │▓▒▒▒▓▒▓▒▓▓▒▓▓▓▓▓▓▓▓▓▓▓▒▓▒▒▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│ ─┐
                                                   │  │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│ ░│
                                   ─────────────┐──┘  │▒▓▓▒▒▒▒▒▒▒────▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓│  │
                                 ┌─░  ░  ░ ░ ░ ░│  │ ─┘────    ──    ────────────────────────────────────┘┐ │
                                 │░░────────────┘  │        ░ ░ ░ ──                                      │░│
                                 │                    ┌───────────░░─────────────────────────────────────┐ ░│
                                 │   ───────┐    │    │▓▒▒▒▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│ ░│
                                 │░ │░░░░  ░└─   └─┐  │   •                  ┌──────────────────────────┐┘┐░│
                                 │░ │░░░░ ░░░░     │  │▓▓▓▓▓▓▓▓▓▓████████████│                          │ │░│
                                 └─ ░░ ░░░ •░░•  │ │  └─┐───┐────────────────┘    ┌─┐───┐               │ │░│
                                   ──────── ──   │ │  │░│ ░░│           ░ ░░ ░│   │░│ ░░│               │ │ │
                                                 │ │  └─┘ ░░│          ───────┘   │░░ ░│                │ │ │
                                  ┌────░░• │     │ │  │░│ ░│                      │░░ ░│                │ │░│
                                  │░░░░──░ │     │ │  │▒└─░│                      │░│ ▒│                │ │ │
                                   ────  ──      │ │░ │░░ ▒│                      │░│ ▒│ ───────────────┘ │░│
                                                 │ │░ └────┘                      └─┘──┘                │ │░│
                                                 └─┘ │                                                    │░│
                                                   │ │      ─┐    ┌─┐   ┌─┐    ┌─       ─────────         │░│
                                                   │ │     │ │    │ │   │ │    │ │    •   ░   ░░        ──  │
                                ─── ─────────────  │  ─────┘─┘───┐┘ └┐─┐┘┐┘────┘─┘──── • ──   ────         •
                                   │                             │░│ │ │ │                   •    ─────────
                                ───┘ ───────────── ──────────────┘─┘─┘─┘─┘────────   •      │
                                                                                  ─── ──────┘
























```

*Figure from page 24 (2346x3317 px)*


---



4203-E P-301



SECTION 2 PROGRAM OPERATION



15-5-3. Changing the Dfrectory



The directory can be changed by locating the cursor at the required directory name and pressing the



WRITE key.



If the cursor is located at "PARENT DI RECTORY" and the WRITE key pressed, the directory changes to



the parent directory.



lffffflW l'.ffifilTltlf



1tfQ2NYERI83:aer



CURRENT DIRECTORY


# I . .

AX),, 11)11



1§-00Sm,yEF!r



l,00.0IA\.



Xll».Olll'-.



' XOOI.DIR'.



CURSOR



!fflitfflM CPffllTl(W 1§:00S g.;wEffi



lt'f9X6fflIFfl:ffl


#### MFIR!Js


#### Offlll!RIJE !trq>!l'y'f!![Bj:g)P\'

CURRENT DIRECTORY CURRENT DIRECTORY



1§:Mcy,Mffl


#### OYfflfUTF

I ~~~li!::======::iii!IS.oos~==~-q• I ~,~~=~~tllllC:======Al:&iC=::::eiai!L~•



/_ .t {_ •~:'Al:;018'



l«X)l.01"'-



CURSOR



"- .IOC!l.01A'-



' J\004.0IA''-


#### CURSQfi POOi.MiN

P(ll);.¥!N



1'(1)5.MIN



!'007.MIN


#### POJ9.MIN


#### POii.MiN


#### POI .MIN


# ~l...__ _ __ I

Flg. 2-20 Changing the Directory


```text


                                                                                                  •
                                                                          ┌───────┐───┐─────────░░░──────────
                                                                          │░░░░░░░│ ░ │░░░░░░░░░ ──░░░░░░░░░░
                 ───                    ──────────────────────────────────┘───────┘── └─────────      ──
            ┌────   ──────┐───┐─┐───────
            │      │      │  ░│ │       │      •          ──          ─────        ──────
            └───┐ ┌┘      └─ • •      ──┘ ───── ────── ───  ──────────     ────────
                │ │ ──░   ░       ░│ │░             ░   ░           ░     •           │ ┌─  ────────────── ──
                 │     ──  ┌───────┘─┘──────────────────────────────────── ───────────┘ │ ──              •
                 │  ┌──  •░│                                                                                │
                 │ ░│  │        ──────           ┌─      ──   ───────────────────────────────────┐─┐─────┐──┘
                 └─   ─┘────────      ───────────┘ ──────  ── ░           ░              ░ ░ ░   │ │░░░░░│ ░│
                 │░░ ░░░░  ░░░░░░░┌┐                         ──────── ───────────────────────────┘─┘─────┘──┘
                 └────           ─┘┘ ─────────────        •
                      ┌─────────┐  └─ ░░░ ░░░     ─┐───┐─  •
                   │  │░░░░░░░ ░│     ──  ░ •      │░░░│    │
                   └──┘░┌──       ┌───  ──── •   ──┘───┘──┐ │
                   │ ░│░│ ░░░░░ ░░│           ───         │ │
                   │  │░░░░░░                 ░░░ ──  ░░    │
                   │░ └───────────────┐       ────    ───  •
                   │  │▓▓▓▒▒▒▒▒▒▒▓▓▒▒▒│  •               • ░─┐────────────────────
                   │  └───────────────┘──    ┌─           │░ │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
                   │                      ───┘            │ ┌┘──────────────────┐▒│
                   │                ──────                │ │                   │▒│
                   │                      ────           ─┘ │                   │▒│
                   └─                           ─── ───── │ │                   │▒│
                   │                     ┌─┐  ──   •     ─┘ │                   │▒│
                   │            │        │ │   ░          │ │                   │▓│
                    •           │  ┌─┐      ──────────     ─┘                   │▓│
                     ───────────┘  │▓│    ──          ─────                     │▓│    ─┐
                                  ░└─┘ ┌─┐                                      │▓│  ░│▒└─
                                       │▓│                                      │▓│   │░│ │
                       ───────   ──  ┌─░░└┐─┐───────   ────┐   ────────── ──────┘▒░─┐─    └──     ───
                      │░░░░░░░ ──    │░░░░│▒│       ───    │  • ░▒▒░░░░░ •      │░░░│░┌─     ┌───┐   ─┐
                   │  │░──────░░░    └────┘─┘─  ──  ░░░░ •  │   │░┌─░─┐─░░    • └─ ─┘─┘      │░░░│ │ ░│
                   └─ │░                          ──────  │ └── │▒│   │   ─┐──              ─┘───┘─┘ ░│
                   ░░─┘────░░░ ░░            ┌──┐─       ─┘ ░░░░░░└───┘ ░ ░│          ─┐──┐─       │ ░│
                  ─┐  ▒▒░░░░░                │▒░│    │░│ ░  ── ░░│░░░░░                │░░│    │░│ ░  │
                   │  ┌──────┐──────── ──┐   └┐─┘────┘─┘──     ┌─┘──────────────        ──┘────┘─┘┐─┐ │
                   │░░│█▓▓███│▒▒▒▒▒▒▒▒│  │░   │           │    │▓▓▓▓▒▒▒▒▒▒▒▓▒▒▒▒───┐───┐          │ │ │
                   │  └──────┘───────┐┘── ────┘           │    └───┐────────────   │▒ ░│          │ │ │
                   │                 │░░░│                │    │░░░│             • │▒░░│          │ │ │
                   │░│             ──┘───┘                │    │░░░│               │░░▒│          │ │ │
                   │░│                                 ──      │▒░▒│      ──  ───  │▒░▒│        • │ │ │
                   │ │                 ─┐────        ──   │    └───┘──────  ──   • └─┐─┘  ──  ── ─┘ │ │
                   │                  • │    ───  ──┐     │  │                 ──    │   •  ─┐  •   │ │
                   └──── • • │             ──░░░ •░░│     └──┘                •       │ ░░  ░│      └┐┘
                        • • ─┘──       ──                                       ──┐   └──────┘─     └┘
                                │ ──┐  ▒▒─────────────────────────────────────── █│            ─────┘
                                │░ ▒│  ─┐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┌┘
                                 ───┘   └──────────┐────┐────────┐──┐─────────┐──┘
                                                  ░│   ░│  ░░░░░░│ ░│ ░░ ░░░░░│
                                                ───┘────┘────────┘──┘─────────┘





























```

*Figure from page 25 (2346x3317 px)*


---



4203-E P-302



SECTION 2 PROGRAM OPERATION



15-5-4. Function Key [F6] (RETURN), [F7] (CANCEL} and Cancel Key



When function key [F6] (RETURN) is pressed, the command creation screen is displayed and the device



and current directory names are entered at the position of the edit pointer. The file name that was at the



cursor position is not entered.



When function key [F7] (CANCEL) or the Cancel key is pressed, the command creation screen is



displayed and the device name, current directory name and the file name at the cursor position are not



entered on it.



Directory selection screen Command creation screen



I' /"iPffflWI CfFMTfllf _, lf!J9WI rmu.r1m



¥5:-09$tffl¥f8I 1§::00S CQNfflT



\..



Ill• ii!li:J~CTj)llllN~======:::Jl~,,_- _ -.. ::.:::·~•"">GE~::.q,



FU):'-Jl!C.Dl"'-



~~:D!T POINTER



HtOEXt:>tSo1.J.Y~



[FZJ -> Kn:•.•



,,_., DI



J001.0Ul",



JOOl.l)IA'



~-0""


#### AIC2.ltll

Pl'01.llll



[F3J



POOG.lllfl



;:o(l;<a.•


#### TO DISPUY 01",el llo!IE:<e$.AFTER PA!:SSIM: [Fl!.

IIIPVT THI: OOVICE !WE MfJ Fil£ NAIIE, - PRES$ ['!RITE] K!'/,



~F".V.11.J OEVICE HMI£ -



~r FtLE 1WE - • •



\. Ital(


# §1 ....._ ____


# _,,,t

/ IP!3P!JUN OPflWUW l:"ir-0® gN';'ERT



llllE)(DIS'I.AY



{F.2) -> iDt:-•.•



(Fl) -:> FOQ:•.•



Til DISPLAY 0'!\£11 Uill)lcS.JF!Sl P!'£SSIHG [Fl].



IRT H DEVIC:S. MIE Nf) f:lt.e IW£. NEN PRESS (llllTE] KEV,



t:EFMJr..TtEVICEMM:-



CEFAUI.T F"lt.E ~ "'" • *



"YFIEIJE



:gpy "'llffl'ITf I



~N.R»:'veC.OIR\;>OOJ,MIN\EDIT POINTER



INCEC OISPUY ~



[f21 -> 1()1:•.•



[Fl] - > AJO;•,•



Am;



~--------~►,



TOOISPUY l>IIER l!Di>a.AF!DlPRESSIM: [Fl).



lriP\IT TIE a:Y'l<:E ~ ND FILE !WE.. nf9I PfE$S. ttrFtlTI(l KEY.



OOFAl>..TOEl'ICENIIE -



CEFJM.T FIU NME = •. •



, HID



1-:~ I '?'fu 1= lo: lc:m I



c,,o:a.



Fig. 2-21 Function Key [F6] (RETURN) and Cancel Key


```text


                                                                                                ──
                                                                         ┌──┐─┐────┐─┐─────────░░░───────░░│
                                                                         │░░│ │░░░ │ │░░░░░░░░░ ── ░░░░░░──┘
                 •                                        ──────  ──    ┌┘──┘─┘────┘ └─────────       •
           ┌─────  ──────────┐────┐─────────┐─────────────      ──  ────┘
           │░ ░   │░         │ ░░░│ ░░    ░░│ ░                              •                   •
           └───┐ ┌┘         • │        •    └─            ─┐           ─────┐  ───   •   ── ──    ┌─
               └┐┘░     ░ ░   └── ░░░ •░│  ░░░•           ░│ │            ░ │ │   ─── ───  •  ──  │░• ─────┐
                │ •           │    •    │   ──               │    •          ─┘                 ──   •     │
                │   •   • ──      • ┌─ ░│ ░•  •   ░┌─░─── ░ ░ ░ ░  ─┐░ ░ ░ ░░ ░░┌─── ░ ░• │░ ░ •░░ ░░░ ░ ░ │
                │░░•░───░•░░──────░ │░░•░░•     • ─┘          •   • └─      ──  │         └─    ──────   ──
                │                    │      ───┐         ────   •       ───        ── ────  ────      ───
                └───────────┐───░──░ └─┐ •░░ ░░└────┐────░░░░───░┌─────░░░░░  ────┐░░░░░░░──░░░░░───░░░░░ ───
                │░░░░░░░░ ░ │ ░░•░░ ░░ │░░░────░ ░░ │░░░░────░░░─┘ ░░ ░─────  ░░░ │░ ───── ░────░░░ ─────
                └──░────  ──┘─── ────── ───    ───── ────    ──   ─── •          •  •     ──    ────     ───
                   •    ──

                           ───┐────┐                                   ────
                     ┌─────░░░│░░░░└─┐──────┐─────     ───  ─┐────────┐ ░░░───────────────      •
                     │░░░░░░░░   ┌─  │░░░░░░│      ────      │░░░░░░░░│      ░░░ ░░░      ────── •
                     └─░░ ░░░░┌──┘  ─┘──────┘      ░░░░ │     │░░░░░░│░░•     ──────      ░░░░░   │
                       ───────┘  │ •             ───────┘     └──────┘─             ────────────  │
                                ░░  ░░ ░░   ┌───┐       └─             ░░   ░ ░ │               │░│
                      │▒──░▒▒░ ─────────┐   │░░░│   │░░ ░     ┌─┐░───░░─────────┘               │ │
                      │   ─────         │     ──┘ ──┘───      │░│  ░░                           │░│
                   │  │░░•               ┌──░                 │ └─┐░░──────  ░ ─────────┐       │ │
                   │  │░░░┌─             │▒░────────────┐     │░ ░│░░░░░░  ────   ░ ░   │       │ │
                   │  │▒░┌┘              │▓▒▒▒▒▒▒▒▒▒▒▒▒▒│     └───┘─────  •     ────────┘       │ │
                   │  └──┘                ──────────────┘    │                                  │ │
                   │        •  ───   •                       │                                  │ │
                   │ │   ┌─┐ ──   ┌─┐    ────                │    ──  ──   ──   •  ──           │ │
                   └┐┘   │ │      │ │        ──  ──           ───  ░──░░░┌─░░░ •░• ░░─────── ───┘ │
                    └┘            │   │░│    ░░  ░░            ░░ ──░░───┘ ──░ ░░░───░░  ░░ •    ─┘
                      ───      ─┐ └── └─┼────  ──  ────────────  •           •▒▓│    ───────  ───
                         ┌──┐   │ │░░ │█│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓─┘
                         │░░└───┘─┘── │█└─────────────────────        ────────              ──
                         └──          │█│                     ──               ─────────────  ───┐
                                      │█│                     ░░░░•░░░•    • ░░░░░░░             │
                                      │█│                     ───▒▒───░─┐──░───────    ────░░───  │
                                      │█│                  │     •      │  •          │    ──   │ │
                                      │█│                  │  ┌─     ──     ──────────┘         │ │
                                  ┌── └─┼──────────────────┘  │░ ░░░│░  │                ───────┘ │
                                  │░░ │█│░░░░░░░░░░░░░░░░░░   │░   ░│  ─┘─────────┐──┐──┐       │ │
                                  └── └─┼────────────────── ░ │░ ░ ░░ ░ ░   ░░ ░ ░│ ░│  │       │ │
                                      │█│                  │  │░░░░░░▒────────────┘──┘──┘       │ │
                                      │█│                  │ │ ───────                          │ │
                                      │█│                  │ │                                  │ │
                                      │█│                  │ │                                  │ │
                                      │█│                  │  ┌─┐────┐───┐─────░────────┐──┐────  │
                                      │█│                  └─ │░│  ░░│  ░│ ░░░  ░░░ ░░░ │░░│     ─┘
                                      │█│                     │ └─   │  ─┘              └─
                                      │▓│                   ┌─┼─░░───┘─      ▒░░░░░│      ────   •
                                      │▓│                   │ │░ ░░░░ ░         ┌──┘─     ░░░░    │
                                      │▓│                   │  ─────────░░░░░░░▒│    ┌───  ─────  │
                                      │▓│                   │            ─────── ░░│ │░░ ░│     │
                                  ─── │▓│                  │  ┌──────░░░•       ───┘─┘────┘     │ │
                                  ░▒░░│█└──────────────────┘  │░   ░                        ────┘ │
                                  ────┘░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│  │ ───░─────   │ ───────┐──┐       │ │
                                       ────────────────────┘  │░ ░░░░░░ ░ • └─ ░ ░   │  │       │ │
                                                           │  └───────────     ──────┘──┘       │ │
                                                           │ │                                  │ │
                                                           │ │                                  │ │
                                                           │ │   •    •    ──────────           │ │
                                                           │  ┌──  ░── ░── ░▒░ ░░░ ░░•  ───  ───  │
                                                           └─ │░  ──░  •░░ ──────────░──░░░      ─┘
                                                                        ──              ───  ────
                                     ┌──────┐─┐───┐─┐──┐─┐─┐─┐─┐──┐ ───┐  ──  ─── ──┐─┐
                                     │ ░  ░░│ │   │░│  │░│ │░│ │░░│░░░░│ ░ ░ ░░░░ ░ │░│
                                     └──────┘─┘───┘─┘──┘─┘─┘─┘─┘──┘────┘────────────┘─┘─













```

*Figure from page 26 (2346x3317 px)*


---



4203-E . P-303



SECTION 2 PROGRAM OPERATION



15-5-5. Directory Display Method



{1) To Display Floppy Disk "FOO:" Directory



Press [F3] function key {FDO: INDEX).



The input examples given below show how to designate which file directory is to be displayed.



(2) When function key [F1] (INDEX) is pressed, "ISO" will be displayed at the console line.



Following the "ISO" character string, enter the desired device name, path name, and file name, then



press the [WRITE] key. The following examples apply when an MS-DOS formatted floppy disk is



being used.



>ISO FOO: [WRITE]



The directory for the default path name and file name at the FDO: device will be displayed.



The default file name is indicated at the directory display procedure.



The default path name used at the MS-DOS file convert function is route directory"\". The default



path name used at the MacMan mode can be designated as desired at the environment setting



operation.



(3) When a path name is entered before pressing the WRITE key:



>ISO FD0:\ABC\ [WRITE] (Absolute path designation)



The directory for the FOO: device, "\ABC\'' path name, and default file name will be displayed.



If the path "\ABC\" does not exist in the device, the message "SPECIFIED PATH DOESN'T



EXIST." is displayed on the console line.



>ISO FDO:ABC\ [WRITE] (Relative path designation)



A path name which doesn't begin with"\" is interpreted as a relative path from the default path



name.



>ISO FOO:\*-*\ [WRITE]



The message "ERROR IN SPECIFIED PATH NAME." is displayed on the console tine.



The wild cards"*" and"?" cannot be used in any of the directory names that make up a path name.



>ISO FD0:\ABC.1234\ [WRITE]



>ISO FD0:\123456789.ABC\ [WRITE]



The message "ERROR IN SPECIFIED PATH NAME." is displayed on the console line.



The following restrictions apply to the directory names that make up path names: the main



directory name must comprise no more than eight alphanumeric characters and the extension



must comprise no more than three alphanumeric characters.



>ISO FD0:\ABC\123456789.ABC



>ISO FDO:\ABC\ABC.1234



The message "ERROR IN SPECIFIED FILE NAME." is displayed on the console line.



If a path name is specified, the format is taken to be MS-DOS and therefore the main file name



must consist of no more than elght alphanumeric characters and the extension name must consist



of no more than three alphanumeric characters.


```text


                                                                                                ┌──
                                                                          ┌─┐─────┐───┐─────────┘░░─────────┐
                                                                          │░│░ ░░░│ ░ │░░░░░░░░░ ── ░░░░░░░░│
                 ───                      ────────────────────────────────┘─┘─────┘── └─────────    • ───
            ┌────   ──────────────────────
            │░    ──░░  ░     ░     ░ ░   ┌─
            └────   ───── │    │  │ ───   │ ┌─
                          └────┘ ░└─      └─┘ ┌─┐ ┌──────┐
                  ───  │ •     └─┐    •   │   │ │ │      │
                       │  ──── │ │ ───    │     │ │░ ░  ─┘
                       │         │    ─┐ ┌┘─  │ │ │       ────────────┐─────────┐─┐─────────────
                       │░       ░     ░│ │░ ░ │    ──   •       ░     │░  ░    ░│ │             ─────────┐
                       │           ────┘  ──   │  │  ─┐─    │           │       │ └──                    │
                    │  └──┐     ───          ──┘──┘   │  ───┘  │        │  ────  ─┘        ────    ┌─────
                  ──┘ │   └───      ┌─┐            ──   •   └─ │       ─┘── ░ ░ │ │░    ───   ░──┐░│
                      │░ •░   ──┐── │░│          │        ┌─   │            •   │ │              │    ── ───┐
                      │         │    ░│ │        │   ░    │   │    ──     ──              ─────   ───┐  •   │
                       ┌───┐ │░•░┌────┘─┘░───────┘─ ─────░░░  │░──┐░░•░ ░░░░ ░░ ░░─── ░   ░ ░░░░ ░░░░│ ░░░  │
                       │░░░│ │░░░│                 •      ────┘─  └──  ┌──────────   ────────────────┘──────
                       └─     │   ┌─┐──┐─┐─┐                           │
                      •  │░░• │░░░│ │░░│ │░│                         │ │
                       │ │   ─┘    ─┘──   • ─────────────────────────┘─┘───┐────┐─┐─┐──┐─┐───┐─┐───────┐
                       │░ ── ░░░░  ░ ░ ┌── ░░░░░ ░░░░ ░░░░   ░ ░░  ░░░░ ░ ░│░░░░│ │░│░ │ │░ ░│ │░░░░ ░░│
                        ┌─  │          │                                        └┐ ┌┘──┘─┘───┘─┘───────┘
                        │ ░ │░░░ ░ ░░ •░░   ░  ░░░░░░ ░ ░ ░ ░░░•░░░ ░░░░░░ ░ ░░░░│░│
                       •    │                                   │                    • ─────          •   ──
                        ┌──┐┘┐──░░ ░░───░░───┐─────░ ░ ░•  ░ ░ ─┘ ──────── ░░ ░─────░░• ░░░░─────────┐ ┌──░░│
                        │░░│ │░░┌───░░ ░──░░ │░░░░░───░•░░──░──░└─░░░░░░░░─────░░░░░──░ ────░░░ ░░ ░░└─┘░░──┘
                        └──┘ └──┘   • •   •   ────    • ──  •  •  ────────     ─────        ── ─────    ──
                  ┌─┐  │    •
                  │ │  │   │   │ │ •     ─── • ─┐ ── ─┐──────────────     ───┐
                  └─┘      │   │ │            • │     │                ┌─    │
                      ─┐─┐─┘  •░░└──────┐   ──░░░•         ─────────   │  ── └───────────────────┐
                       │░│░    •░░ ░░░░ └─── ░░░░  ░   ─┐─┐            │ •░░ ░ ░░░ ░░░  ░░░░░░░ ░└─
                       └─┘──     ┌──────┘   ─┐─┐─     │ │░│   ┌─┐     │ • ───      │ │  ── •       ──────┐
                       │       │ │       • • │ │    ─┐┘  •    │ │     │            └─┘ •  •    ── ░░  ░  └──
                       └────   │░│ ┌─░• │ │ ─┘ │ ░ │ └┘   ░│  │    ┌─░│         ┌─  ░   ░   ┌─┐░  ──┐  ░
                       │       └─  │   ─┘ │   •    │  │    └──┘────┘ ─┘─────────┘ ──────────┘ └───  └────────
                       │     │ │  • ░ ░░░      ┌─       ░ ░│
                     ┌┐  ───┐┘ │░  │  ░─┐─┐    │   ┌───────┘             ┌───────────┐───────────┐
                     └┘ • ░ └┘ │   └┐░  │ │ ░  │  ░│        •            │░░░░░ ░  ░░│ ░░░░░░░ ░ └┐
                      └┐     │ │    │░░ ░ │        │     │       ──────── • ───    ──   ┌────── • └─────────┐
                       │ ──  └─┘────┘─────┘──────── ─────┘───────              ░░░    ░░│       ░ │░ ░░░  ░ │
                       │░░░─┐┘                                        ─┐────────────────┘─────────┘─────────┘
                     ┌─ │   │ ─┐────┐────┐──────┐                    │ │
                     │  │░░░│  │░░  │ ░  │░░░░░░│                    │ │
                     └─┐    └──┘  ─┐ ┌───  ── │  ────────────────────┘┐ ┌──┐──────┐───┐─┐─┐─────────┐
                       └┐─┐ ░░░░•░░│ │░░ ──░ ░└─░░░░░░ ░░░ ░░░░  ░░░░░│ │░ │░░░░░░│ ░ │░│ │░ ░░░ ░░░│
                        │ │ •     ─┘ └──   ───┘                   ──── ─┘ ─┘      └─┐   │ └── ──    └┐─┐─┐──┐
                          └─░░ ──┐ ░    ░•░    ──┐───░│ ░░░ ░ ░░░ ░ ░░ ░░ ░░░ ░░░░░░│  ░│ │░░│ ░ ░ │░│ │░│ ░│
                     │   •   ──  │  ┌─┐ │  ─┐─┐  │    └────────────────┐────────────┘───┘─┘──┘─────┘─┘─┘─┘──┘
                     │ ─┐░░ │   ░░──┘░│ └──░│ │░░│ │░│                 │
                     │ ░│   │         └─┘   │ │  │ │ └────┐            │
                      ──┼─░─┘   ░░  │░░░└───┘ └┐░│ │░│░ ░░│            │
                        │    ──   • └┐         └┐    │     ───────────  ──┐────────────┐───────┐───┐
                       • ░│ ░░░───░│ └───░░░ ── └───░│ ░░• ░░░  ░░░░░░  ░ │░░░░░░░ ░  ░│  ░ ░░░│ ░░│
                        │ │        │ │                                                         │          •
                        └─┘────────┘┐┘─────────────────┐──┐─────────────────────░░░──────░░┌─┐░└──┐─┐─────░│
                       •░░░░░ ░  ░░░│ ░░ ░  ░░░░░░░  ░ │░░│ ░░░  ░░░  ░░░ ░░░ ░░───░░░░ ░──┘ └─░ ░│ │░░░░░─┘
                        ──────   ┌──┘   •   ──────  ─┐ │  │  •   ───  ──   ─┐───    •  •    •      •   ───
                      │       │  │       │         │ │ └── ──           ─── │
                     ┌┘ │ ──┐ │  │ ┌─────┘─────────┘░│                 │
                     │  │   └─┘ ─┘─┘░    ░░░░░  ░░  ░                  │
                     │  │   │ │    │       ┌─┐   ┌─────                │
                     └─ │ ┌─  │    │░    ░░│ │ ░░│                     │
                       ┌┘─┘   │    └─┐░░░──┘ ░ • ░░───░──────────────  │ ─────────────────────────┐
                       │    │      │ └───   ┌─┐ ──┐                  • └─  ░  ░            ░  ░  ░└─
                       │░   └─░ ┌─┐         │ │   │                                        ─┐   • │  •  ───┐
                       │  ──    │ │           │   └─              ───          • │  •     │ └───   ── ──   └┐
                       └┐ ░░ ░░ ░░        ░░ ░░░ ░░░  ░░ ░░   ░░   ░░░░ ░░░ ░░░░░│ ░░░░░░░│ │░ ░░•░░░ ░  ░░└┘
                       └┘─────────░░░──░░░──░░░•░────░───░──░░───────────────────┘────────┘─┘──── ─────────┘
                                  ───  ───  ─── •    •   •  ──










```

*Figure from page 27 (2346x3317 px)*
