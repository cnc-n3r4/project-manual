# III SECTION 2 PROGRAM OPERATION 06. MULTI FILE TRANSFER (MPIP) OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-06.-MULTI-FILE-TRANSFER-(MPIP)-OCR.PDF*

---


## 6. Multi-file Transfer (MPIP)

4203-E P-248



SECTION 2 PROGRAM OPERATION



The MPIP command is used to transfer multiple part program files at a time using the RS232C interface.



The following sub commands are provided.



Item Command Function



Multi-file read MR Reads multiple part program files from an external device



and stores them to the memory.



Multi-file punch MP Outputs multiple part program files, stored in the memory, to



a tape punch.



Multi-file verify MV Verifies multiple part program files, in an external device,



against those in the memory.



Multi-file transfer end Q Quits the multi-file transfer mode.


## NOTICE

: During file transfer processing, do not turn off the power supply. If the power supply is turned



off during file transfer, the contents of file might be destroyed.



6-1. Multi-file Read



The multi-file read function reads multiple part programs from the external device and store them ln the NC



memory.



The operation procedure is indicated below:



(1) Press function key [F5] (MULTI PIP).



MULTI



DATE DIR



PIP EDIT PIP LIST CONDENS [EXTEND]



"=MPIP



>" is displayed.



Press [F5] (MULTI PIP).



The function key names change as indicated in item (2).



(2) Press function key [F1] (MULTI READ).


#### MULTI MULTI LULTI

READ PUNCH VER I FY



Press [F1) (MULTI READ).



"MR" is displayed on the console line.



M-PIP



QUIT


```text


                                                                                               ──
                                                                         ┌───────┐───┐─────────░░────────░─┐
                                                                         │░░░░░░░│ ░ │░░░░░░░░░ •░░░░░░░░•░│
             ─────            •                     ─────────────────────┘───────┘── └─────────      ──
          ┌─┐      ─── • ────  ┌──           ──────
          │░│ ──── ░░  ░│ ░░░│ │░  ┌───░•   ░░░░ ░░
          │░│     ┌──░░─┼────┘ └───┘░░░•░• ─────────
           ─┘   ┌─┘     │                           ──┐──┐─┐─┐─────────┐─┐─────┐─┐─┐─────┐──┐──────────────
                │░  ░░░░│ ░░  ░░ ░ ░ ░░░░ ░ ░░░░░░  ░░│░░│ │░│   ░░░░░ │░│ ░ ░ │░│ │░░░ ░│  │░░ ░░   ░░░  ░│
                │            │                         ──┘─┘─┘─────────┘─┘─────┘─┘─┘─────┘──┘──────────────┘
                 ░░ ░░░░░░ ──┘░│ ░░   ░░░──────────░░│
                ─┐ ┌───────    └───────┐─          ──┘                     ┌──┐────┐                        │
                 │░│       │░░ │       │  │░░── ░ │  │                     │░ │░░░░│                      │░│
                 │░└───────┘┐─┐┘       │ ┌┘─┐░░┌──┘┐─┘──── ───┐────────────┘        ───────────────────   │░│
                 │░│        │░│        │ │  └──┘   │  ░░░░•   │░ ░ ░░░ ░ ░░ ─────┐ ░ ░░ ░ ░░░░░ ░ ░░ ░░   │░│
                 │░│          └─       │░│     │    │░░░ ░░░░░ •░░░ ░ ░░░ ░░░░░░░│                       ─┼─┘
                 │░░░░░░░░   ░ ░  ─────┼─┘   │░│    │░░░░ ───░ ░░░│ │░░ ░░░░░░┌─░░░  ░  ░░░░ ░░   ░────  ░│░│
                 │░│           │ •     │ └── │ │    │░ ░░│ ░  ────┘─┘─────┐───┘ ───  ── ──   ──  ┌─     • │░│
                 │░└──────  ───┘       │ │   └─┘    │░ ░░│ ░──            │               ───  ──┘  •  │  │░│
                 │░│░░░ ░░──░ ░│       │ └── ░░░    │░░░░░│ ░ ░░░░ ─── ───░░░░  ░░░──────░░░░ ░░ │░ ░░─┘  │░│
                 │                     │ │   │ │    │░░░──┘ ────── ░░░ ░░░░──     │      ───────  ────    │░│
                 └──────────────┐────┐─┼─┼───┼─┼────┘░░    •      •   │       ────┼─                      │░│
                 │░░░░░░░░░░░░░░│ ░░░│ │░│   │░│    │░░░▒░░░░░░░░░░░░░│▒░░░│ │░░░░│                       └─┘
         ┌──┐────   ┌─────┐ ────   ──  │ │   │ └───  ──┐────────── ───┘────┘┐┘──┐─ ──┐─────────────────┐──  │
         │  │░░ ░░░░│     │░ ░░  ░│ ░░ ░░│ ░   ░      ░│        ░ ░         │░ ░│  ░░│   ░░░ ░  ░░     │░░░•
         │░ └─────░─┘ ░  ┌┘     ──┘      └──┐ •    ────┘┐── ── ┌──┐    ┌────┘── └────┘─────────────────┘──┐ │
                  •     ░└┘──░──░░░ ░░░░░░░░│ ░░░ ░░░░░░│ ░ ░░ │░░│  ░ │░░░░░░░░│                         │ │
          ┌─       ───── │   •    ──────────┘───────────┘──────┘──┘────┘────────                           ─┘
          │░ ░•   •░░░░ •░│ │░░░░│
          └───            │ └────┘─┐─┐──┐──┐───────────────────────────────┐─┐──┐─────────────────┐───┐────┐
                ┌─────░░ ░│ │░░░░  │░│░ │░░│ ░░░░░░ ░░░ ░░░░ ░ ░ ░░░ ░ ░ ░░│ │░ │░░ ░ ░ ░░░░░░ ░░░│   │░░░░│
                │ ░░ ░── ─┘─┘───   └─┘──┘      ─── ────────────────────────┘─┘──┘─────────────────┘───┘────┘
                │       •       ───      ┌─────   •
               •░ ░ │░░░░░░  ░░░░░░• ░ ░ │░░░░░│ │░░░░│
                ─┐─┐┘┐          ───       •    │ └┐  ┌┘
                 │ │ │░        ░   ░░  ░ ░ ░░ ░ ░ │░ │
                 └─┘ └─┐─┐────────────────────────┘──┘
                       │ │                                                                 ┌─┐
                       │ │                                                                 │ │
                       │ │   ┌────                                                         │ │
                       │ │  ┌┘▒░   ─┐───── ──────────────        ────────   ─────          │ │
                       │ │ ┌┘░────  │     │              ┌──┐───┐                ┌─┐       │ │
                       │ │ │░     │ │  ─┐ │ • ─┐ ─┐      │  │░  │        ┌──────┐┘ │ ────┐   │
                       │  ┌┘ ░░ • │  ┌─ │ │  │ └─ │  │  •   └───┘        │   ░ ░│        └─  │
                        • │░ │   ─┘  │  └─   │   •  ┌┘          │   │   • │                  │
                         ─┼─ └──░░ ──┘ ─┘░┌─┐░┌─  ──┘░─┐───┐─┐─┐ ──┐┘┐─  ─┘  ─┐     ┌─┐  ┌──
                          │  │ ░•   ░ │ │ │ │ │   ░    │ ░ │ │░│ ░ │ │░│  │ │░│ ░ ░ │░│ ░│
                          │  │  ░│ ───┘ │ └─┘ │░│ ──  ─┘ ░─┘ │ │ ░ └─┘─┘  └─┘─┘──── └─┘──┘
                         ┌┘ •░░  │     ─┘─   • ─┘─  ──  ──  ─┘─┘   │               •
                         │   •░ ░░░░░░                          ──░░░  ░ ░░      │
                              ────────                             •   ──────────┘
                     ─┐─┐─────        ────┐──────┐──┐─┐─────┐───┐─┐ ┌─┐
                      │░│  ░░░░░ ░░• •░░ ░│ ░░░░░│ ░│ │░░░░░│ ░ │░│ │░│
                 ┌─┐─┐ • •        • • •  • ┌─   │  ─┘─ ┌────┘───┘─┘─┘─┘
                 │░│ │ ░░░   ░░░   │░░ ░   │░│░░│ │░░░░│
                 └─┘─┘─────────────┘───────┘─┘──┘─┘────┘
                                                                                           ┌─┐
                       │ │                                                                 │ │
                       │ │      •                                                          │ │
                       │ │  ┌──┐░                                                          │ │
                       │   ─┘░▒│  ──     ──    • ────────┐─┐────┐─┐───── ──   • ── ──────  │ │
                       │  •░ ░ ░│   ┌── │  ┌─┐─ │        │ │    │ │     │  ┌─┐ │  │        │ │
                       │   ─┐░░ │   │░  │  │░│  │ ───────┘ └────┘ └─    │  │ │ └─ │       ┌┘ │
                            └───┘   └───┘  └─┘ ░└┐       │ │    │ │     │  └─┘─   │      ─┘  │
                        ┌─░ │    •  │   │        │ ┌─────   ──┐┐   ───┐─   │   •   •  ┌─┐   •
                        │ • │       │ ──  ┌─  ── │ │     ─┐  ░└┘  •   │ ─── ░░  ─┐  ──┘ └───
                        │  │        ░  ░• │░   ░ └─┘─░   ░│   ░   ░ │░│ ░ ░ ┌─  ░│ ░ ▒  │
                       │   │      ░ │      ──                ───────┘─┘─────┘   ─┘──────┘
                       │ ──┘        │  ───       ── ┌─────┐─                  ──
                           ░░   ───░░┌─     ┌──░ ░  │░ ░  │░ ░│
                     ┌───    ┌──     │  ────┘         ┌───┘───┘
                     │░░░│ ░ │░░░░░░│ ░ ░ ░ │░ ░ ░ │░░│
                     └───┘───┘──────┘───────┘──────┘──┘









```

*Figure from page 1 (2346x3317 px)*


---



4203-E P-249



SECTION 2 PROGRAM OPERATION



{3) Following ">MR", enter the file name of the file to be read using the keyboard and press the



WRITE key.



The machining programs are read and stored in the NC memory.



While the program ls being read, "M-READ" and the file name are displayed at the upper right area



of the screen.



After the start of program reading, "Valid information reading" is displayed on the console line.



At the completion of reading, ">" appears on the console line.


#### POOGRAN OPERATION M-PIP


#### BOX-1350.MIN

tile exist overwrite? (Y/N) !Y



varid information reading



MULTI



MULTI



MULTI



READ PUNCH VEfl I FY



{4) Press function key [F7] {M-PIP QUIT).



MULTI MULTI MULTI



READ PU/\tH VERIFY



">Q" is displayed.


#### M--READ


#### M-PIP

QUIT


#### M--PIP

QUIT



Press [F7]



(M-PIP QUIT),



The function key names return to those as displayed in item (1).



[Supplement]



Command format



>MP <input-device:><input-file-name><,<output-device:>><;option>WRITE


```text


                                                                                               ┌───
                                                                         ┌──────┐─┐───┐───┐────┘░░░───────░│
                                                                         │░░░░░ │░│   │░░░│░░░░░───░░░░░░░─┘
           ┌──────   •        ──     ──                ──      ──────────┘────  └─┘   └───┘─────      •
           │      ┌─┐ ┌───────  ─────  ─────────┐─────┐  ──┐──┐               ──   ───                      │
           └──────┘░│ │░ ░  ░     ░░░          ░│     │   ░│  │                                         ────┘
                  └─┘ │  ░  │ ┌─  ─── ──────────┘─────┘────┘──┘──── ─── ───                          •░│
                       │ ┌─┐┘ │░│                                               ───────────────────── ─┘
                       └─┘ │   ─┼──────┐───────┐───────────────────────────────┐
                       │ └─┘ ░  │░ ░   │░     ░│   ░  ░   ░ ░░     ░ ░░   ░ ░░░└─
                       │░ ░ ──         └─         ┌─    ░  ┌─              ────  ───────────────────────────┐
                       │  │    ──  ────  ────░•  ─┘ ───────┘ •  ──      •░ ░      ░  ░   ░ ░   ░░   ░░   ░░░│
                      │░ ░│░ ░ ░░░•                                                            ──    •   ───┘
                      │   └─── │    ────────────────  ┌────┐───────────────┐────┐──────────┐───  ───┐ ┌──
                      │   │  ░─┘░░  ░   ░░ ░  ░░░░░░• │░░░ │░░░ ░░░░  ░░░░ │ ░  │░░░░░░    │░  ░░░░░│ │░░│
                      │    │   └──   ┌───┐     ────┐ •     └───       ─┐─┐  ┌───┘──────────┘────────┘─┘──┘
                       ─── └───┘░    │   │         │░ ░░        ░    ░ │ │ ░│
                          ─┘    ──                  •     ────┐      ──┘ └─            ──
                                   ░░░░   ░                   └────┐    •  ───┐──────┐   •
                            │ ┌── ──░░░░ •░░• ░•     ─┐░ ───  │░░░░│ ─┐ ░ ░ ▒▒│░░░░▒▒│    │
                            │ │     ───── ── ──  ──── └──   ── ────   └───────┘──────┘─ │ │
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
                            └─┘                                                         │ │
                            │ │                                                         │ │
                            │ │  ┌─────────             ──                              │ │
                            │ │  │░░ ░░░░ ░────────┐─     •                             │ │
                            │ │  └──░░────░░ ░  ░  │░ ────                              │ │
                            │ │ ─┘          •     ┌┘─┐    ┌─┐───┐──────┐─  ──────────── │ │
                            │ │  └──┐─░ ┌──┐   ──░│  │    │ │   │      │  • ░░          │ │
                            │  • │░░│   │░░│   ░░    │    │ │   │ •    │  ░  ───┐      •  │
                                  ──┘   └──┘            ──  │   │  •      •     │        •
                             ──┐ •     │      │  │ •  ┌─     ┌─┐    ┌─┐     │ ┌─┼─┐─── ──
                               │  ░│ ░ │ ░│   │░ │ ░│ │░│ │░ │░│    │░│    ░│ │ │ │▒ ░│
                               └───┘───┼──┘───┘──┘──┘─┘─┘─┘──┘─┘────┘─┘─────┘─┘─┘─┘───┘
                   •  ┌────────┘       │
                   ░  │               • ░      ░  │░   │
                  ──  └─┐─────────────  ──────────┘────┘
                        │                                                                   ┌─┐
                        │                                                                   │ │
                        │                                                                   │ │
                        │                                                                   │ │
                        │   ───┐   ┌─     ──      ──┐─────┐─┐─────┐─┐──────        ┌──────┐ │ │
                        │      └┐  │  ┌─    ─┐─ ─┐  │     │ │     │ │      • ┌──┐──┘      │ │ │
                        │    •▒░└─┐   │░─┐   │░• │  │    ─┘ └─    │ │    ─┐  │░░│  │ ─────  │ │
                        │ │   •░░░│   │░░│   │░░    │     │ │     │ │     │  │░ │  │      ──  │
                         ┌┘░    ── │     │        │  •   •   •  ──      ─┐      │   •   •    •
                         │         └── ┌─     ┌─┐─┘ │ ┌── ─── ──  ┌─ ┌─┐ └──     ──┐ ┌─┐ ┌───
                         │ • ░ ░ • │ ░ │░│ ░  │ │ │ │ │░░ ░   ░░│ │░ │░│ ░ ░ │ ░ ░ │ │▒│ │
                        ┌┘    ───     ─┘─┘ ───┘─┘─┘─┘─┘─────────┘ └──┘─┘──── │░•   │ └─┘─┘
                        │ ─┐─    ────     •                      •          ─┘┐ ───┘─
                        │  │░ ░ ░░░░░░•                                  ┌─   │░ ░░ ░░  •
                                ──────                                   │    └────────
                      ┌─────────      ┌───┐─┐───┐───┐───┐───┐──┐───────┐─┘─
                ──────┘ ░  ░░░░░• │░│ │░ ░│ │░ ░│ ░ │░░░│ ░ │░░│░░░░   │░ ░ ░░•
                       ──   ────  └─┘ └───┘─┘───┘ ──┘───┘───┘──┘───────┘──────
                ──┐             ─┐               •                            ──────────────────────────
                  │░│  ░ ░░░░ ░ ░│ ░░•                                                                   │
                  │░│ •                                            •                       ─────  ─────┐░│
                  │░└─  ░░ ──░░░░░ ░░░░░ •░░░░░ ░░ ░░  ░─── ░░░░░░ ░░░░░─────░░░░░ ░░░░ ░┌─     ──     │░│
                  │░    ───  ───────────  ──────────────    ────────────     ────────────┘             │░│
                    ───    •                             ──              ──               ─────────────












```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-250



SECTION 2 PROGRAM OPERATION



(a) input-device:



TT:, CN0:, CN1:, CN2:, CN3:, CN4:



If no input-device name is specified, the default device set for optional parameter (word) No. 57 is



selected. (If "0" is set for this parameter, CN0: is selected.) ,



(b) input-file-name



Main file name: Alphanumerics (max. 16 characters), beginning with an alphabetical letter.



Wild card<"*"·"?") can be used.



Extension Alphanumerics (max. 3 characters}, beginning wrth an alphabetical letter. Wild



card("*"·''?") can be used.



(c) output-device:



MD0:, MD1 :, FD0:, FD1 :, FD2:, FD3:



Default device is MD1 :.



(d) option



Y: Unconditional overwrite; if the file of the same file name to be output already exists in the



specified output device, the file is unconditionally overwritten in this operation.



[SupplementJ 1. If the text (tape data} read from the input device does not agree with the specified



input file name, it is skipped and not stored to the output device.


## 2. If input file name is omitted, input file name of"*·*" is assumed and all read texts

are stored to the specified output device.


## 3. If available space in the output device becomes full during reading, an error occurs

and communication is shut off. In this case, the file being read is not stored.


## 4. If the file of the same file name already exists in the output device while no option Y

is specified, the following messages are displayed on the console line.


#### A.MIN

file exist overwrite ? (Y /N) !



If "Y'' is input, the existing file is overwritten, and if "N" is input, the text to be read is



skipped and the next file is read.


## 5. If an output file name is specified, an error occurs.

5213 File name, error 11


## 6. If the read file agrees with the file selected for DNC-B mode operation, the text to be

read is skipped and the next file is read.



5226 Main program file selecting 'A.MIN


## 7. If the read text already exists in the output device and if it is protected, the text to be

read is skipped and the next file is read.



'A.MIN File write protect


```text


                                                                                                •         •
                                                                         ┌──┐─┐────┐─┐──────────░░░───────░│
                                                                         │░░│ │░░░░│ │░░░░░░░░░░───░░░░░ ░░│
           ┌─────────  •    •  ────────────────────────────────────────── ──┘─┘────┘ └─────────
           │         ─┐ ──── ──                                                                            │
           └────────  │            │     •    ──    ──    ─────────────────────────────────────────────────┘
                    ──┘──      ┌──┐┘ ┌──┐  ──┐  ┌──┐  ┌──
                          │    │░░│  │░ │ │ ░└┐ │░ └┐─┘░ │
                       ┌──┘  ──    ──   └─┘   └─┘   │    └─ ── ───────────┐─────────────────────────── ────
                       │  ░ │░░• ░░  ░ ░   ░ ░ ░ ░ ░│   ░│   ░•          ░│                ░░
                       │    │ │ │░•       •              │                  ────────────────────────────────
                        ─── └─┘ └─ ───  ┌─ ─────       ░░└────── ░ │    ░┌─
                   ┌───       │ │ •   ──┘       ─────────┘      ───┘─────┘
                   │░  ┌───░  │ │░░░│
                    ───┘░     │ │ ──┘  ┌──┐───────────┐───┐────────────────────────────────────────────────┐
                       └──      └─     │░░│ ░ ░  ░    │░  │      ░ ░         ░    ░         ░   ░  ░ ░    ░│
                       │  ──────       │  │  ░        │          ░░•     ┌─      │  •  ┌─┐──        ──     └┐
                       │░░░░░░░ •      │░░░░░░  ░░░░ •░░░  ░ ░░░░░░░ ░ │░│░│░░ ░ │░│ ░ │░│░░░░░░░░ │░░│ │░░░│
                       └───────        └─────────────░──── •░░─────────┘─┘─┘─────┘─┘───┘─┘─────────┘──┘─┘───┘
                   ┌───        ────┐                 •    • ──
                   │░  │░ ░░░ ░░ ░░└┐
                    ───┘──┐ ░  ──   └─ ┌──┐─┐──── ──── ┌──┐
                          │            │  │ │          │  │
                       │               │ ┌┘        ──   ──
                       │     ┌─────────┘─┘
                    •  │     │
                       │░    └─   •          ──   •       ──
                      ─┼───    ─── ──   ──  •  ┌─  ── ────   │ ┌─── ┌──  ───    ┌─ ─── •  • •  ───────────┐
                       │   ┌───      ──┐   •   │ │          ┌┘─┘░  ─┘   •░ ░────┘ • ░   ░•  ░░     ░      │
                           │░░░ ░░│ ░░░└───░───┘─┘░─────────┘░░└──░░│░──░──░░░░░└─░──────░──░────  •
                ┌────────── ┌───┐─┘─   │                                                         ┌─ ┌──────┐
                │░░░░░░░░░ ░│   │    ┌─┘───┐ │░░• ░░░░───░──░░ • ░░│░░───░░• ░──░░─────┐░░░│ ░░│ │░ │░░░░░░│
                └───────────┘   │ •  │░ ░ ░└─┘──░ ────░░░•  ─── ──┐┘ •░  ──░──  ──   ░ └───┘───┘─┘──┘──────┘
                                 •                                │
                                    ┌─ ─── ─┐─┐─────  •  ┌── │   ─┘─ • •    │    │            ────┐ ── ────┐
                                ──  │       │ │     ┌─   │   │ ──   │   ┌───┘────┘────────── •    │   •    │
                                    │ ──────┘─┘─────┘░───┘───┘─░░ •░│ •░│                            •
                                ┌── │                                     ──     ──  • ──────         ──────┐
                                │   └── ░░░░░──░░░─── ░░───░░░  ░░░░• ░░── ░░┌───░░──░•░░░░░░░ ░─── ──░░░░ ░│
                                │ •  ░░────── ░───░░░─── ░░─────────░───░░┌──┘ ░░ │░ •░────────░░ ░• ░──────┘
                                └─  │                                     │       │                         │
                                │   │░░░───── ░░• ░░───── ───────┐─────░┌─┘─ ─────┘░─┐ ░──────░───     ░    │
                                └── └──       ──  ─┐             │     ─┘           ░│        •   ┌─────────┘
                                       •    ──  ── └─           │░ │ •   •░  ░  ── ──┘ •     • • ─┘
                                        │░ •░░│                 └──┘─ ──  ──────      • ───── • •
                                        │   • └─────────┐  ┌────
                                    ┌───┘░• ░ ░░     ░  └─ │  ░ ─┐
                                    │                            └────────────     ─────────────────────────
                                    │ ────┐   │     •    ░    ──              ────    ░       ░     ░  ░░
                                    │░░░░░└───┘─────░─┐───────░░─┐                 ─────────────────────────
                               ┌─┐  │  ┌──            │          └┐─┐─────┐─────┐
                               │ │  │ ░│   ░│░ ░│ │░░░│ ░ •░░░░│░ │░│ ░ ░ │░░  ░│
                               └─┘  └──┘─┐ ─┘┐──┘─┘─       ┌─┐─┘┐─┘┐┘─────┘─────┘
                                         │░ ░│      ░░ ░░░░│ │ ░│  │
                               ┌─┐              ───                └───────┐──┐─────┐─┐─┐────────┐──┐──────┐
                               │░│  │░────░░────░░░░░───░░ •░ ░░ ░░░░░░░░░ │░░│ ░ ░░│░│ │░░░░░░  │░ │░░ ░░░│
                               └─┘  └─░░ ░──░░░░───── ░ ─── ───────── ──  ─┘──   ───┘─┘─┘────────┘──┘──────┘
                                      •       ──                        ──    ┌──
                                        •░░░░│     •░░  ░░░░░░  •░ ░░░░░░ ░ ░ │░░│
                                    ┌──┐ │   └─────              │      •     └─ └─────────────────────────
                                    │  │ │░── ░░ ░░───────┐─┐──┐─┘─┐───┐                                   │
                                    │                 ░   │ │  │   │   └───────────────────────────────────┘
                                    └┐     ┌─ ░   │       │ │  │      ─┘
                                     └─ │  │░ ┌───┘┐           │ ┌────
                                        └──┘──┘    └── ────  ──┘─┘
                                                      •    ──
















```

*Figure from page 3 (2346x3317 px)*


---


#### Example 1: >MP *.MIN

4203-E P-251



SECTION 2 PROGRAM OPERATION



[WRITE]



All files with extension ".MIN" are read and stored to MD1 :.



Example 2: >MP BOX1???.MIN [WRITE]



All files beginning wi1h "BOX1" and with extension ".MIN" are read and stored to



MD1 :. Files such as BOX1001.MIN and BOX1002.MIN are read.


#### Example 3: >MP [WRITE]

All input files are read and stored to MD1 :.



6-2. Multi-file Punch



The multi-file punch function outputs multiple part programs, stored in the NC memory, to the punch



device.



The operatlon procedure is indicated below:



(1) Press function key [F5] (MULTI PIP).



=t.FIP


#### WLTI

DATE DIR PIP EDIT PIP LIST CONDENS (EXTEND]



"=MPIP



>" is displayed. Press [F5] (MULTI PIP).



The function key names change as indicated in item {2).



(2) Press function key [F2] (MULTI PUNCH).



MULTI MULTI MULTI



READ PUNCH VER I FY



Press [F2J (MULTI PUNCH).



"MP" is displayed on the console line.



M-PIP



QUIT


```text


                                                                                                ───      ┌─
                                                                          ┌─┐───┐─┐───┐───┐─────░░░──────┘░│
                                                                          │░│░  │░│   │░░░│░░░░░ ──░░░░░░░░│
           ┌───────────       ─────    ──            ─────────────────────┘─┘───┘─┘─  └───┘─────      •
           │           ───────     ────  ┌─┐─────────                                                      │
           └──────────┐░        ───      │ │       ░ ┌─                            ────────────────────────┘─
                      └───── ───    ──   └─┼───── ───┘
                                  │   ── │ │           ┌──┐ ────────────────────────
                      ┌────┐─┐──┐ └──   ─┘ │    ░•  ───┘  └┐      ░  ░            ░
                      │░░░░│░│ ░│ │░░──░░└─┘─────░──░░░░──░│ •   •   •   •
                      └────┘─┘──  │                               ┌─                        ────────────┐
                                  └──░░░ │░•░ ░────░░────░░───────┘░─────────────── ────────   ░ ░      │
                                  │░░──  └─░─── ░   •░░ ░──░  ░░░  •  ░░░░  ░   ░░░  ░   ░░ ────────────┘
                      ┌────┐─┐──  │    │        ───  ── •  ───────   ───────────── ─────────
                      │░░░░│░│ ░│ │░░• │░░░░░░
                      └────┘─┘──┘ │ •  └┐─     ─┐─┐─────┐─┐────┐──┐──┐
                                  │░ ░░░│ │░│ │░│ │░░ ░░│ │░░░░│░ │░░│
           ┌───    ┌─────────┐──── ┌────┘─┘─┘─┘─┘─┘─────┘─┘────┘──┘──┘
           │░ ░│   │░░ ░ ░░░ │░ ░ ░│
           └───┘ ┌─ ──     • └─     ────────── ───────────  ─────  ───               •              •
                 │ •  ░ ░ ░░│     │                        •      •   │ •    │   ┌─── │   ─────────  ──────┐
                •      ┌────┘─────┘──────────────────────── ────── ───┘  ────┘   │   ─┘  •         ──      │
                 │     │                                          •                       ─────      ──────
                 │ ──┐ └───────────────────────────────┐
                 └┐  │        ░               ░        │
                  │ │ │              ──   •        │  │
                  │ │ └┐  ░  ░  ░   │░░   ░  ░     │░┌┘
                   • • └┐─┐─────────┘──────────────┘─┘┘                                      •
                        │ │                                                                 │ │
                        │ │                                                                 │ │
                        │ │   ─── │                                                         │ │
                        │ │ ┌─ ░  │ ─┐──────┐───── ─────────      ┌─┐───── ───────────────┐ │ │
                        │ │ │░ •   │ │      │     •          ──── │ │                     │ │ │
                        │ │     │  │ │ •    │ ┌─┐    ┌──     ▒░   │ │  ─┐  ───────    ────┘ │ │
                        │  •  │░└─ │ └─░── ─┘ │ └─   │░░ ──  ──░• │ └──░│ •░░░░▒▒░────░░░░░   │
                         ─┐░  └─  •       •                      ─┘        ┌──────     ───   ─┘
                          │ •      │   ┌─┐  ─────     ┌─┐     ──      ┌─┐  │          •     •
                         │   • ░ │ │   │░│ │░ ░ ░│  ░ │░│ ░ ░ ░░  ░  ░│▒│░ ░ │ ░ ░   │░│  │
                         │ •  ───┘ └───┘─┘ └─────┘ ───┘─┘──── ░┌─ ────┘─┘────┘───────┘─┘ ─┘
                         │  │             •       •          │░│                        •
                        ┌┘──┘───────┐                        │  ───────────────┐─
                      ┌─┘     ░░░░░░│ ───────────  ─────── ──┘  ░░░ ░░░░░░░  ░░│
                      │░     │  ────┘            •             ───  ─┐ ┌───────┘─
                      └─     └─           •   ─── •    ────────      └─┘
                  ┌─┐ │ ─────  ┌──   • ─── ┌──     ────
                  │░│ │░░░░ ░░ │░░│ │░  ░░ │░░░░░  ░░░░│░░│
                  └─┘ └─┐─┐────┘──┘─┘──────┘───────────┘──┘
                        │ │                                                                 ┌─┐
                        │ │                                                                 │ │
                        │ │      •                                                          │ │
                        │ │   ┌─┐░│        •      ────────   ─────   ───                    │ │
                        │ │   │▓│ │   ┌─    ┌── •         ┌─┐     ┌─┐   ────┐───┐── ──────┐ │ │
                        │  │  │░ ░│   │░ •  │░░│ ── ──────┘ └─────┘ └──     │░░░│ ░│      │ │ │
                        │  │  │░░░│   │░░ │ └─░│ ░ │      └─┘     │ │       │░──┘──┘        │ │
                         • ░• │   └─  │   │        │ │   ─┘  •   ─┘ │    •  │             •   │
                          •   │ •   ┌─┘┐─ ░─── ────┘─┘┐─┐ └── ┌─┐ └─┘─┐─┐ ── ░░░░────┐─┐── ───
                         │   │  ░│  │░ │ • ░ ░ ░   ░  │ │ │ ░ │░│ ░ ░ │░│ ░░ ░ ░ ░ ░ │░│ ░•
                         │  ┌┘░──┘─  ──┘░░ ░ ───░     └─┘ │ ░ └─┘ ─── └─┘ ──  ── ─── └─┘ •
                        ┌┘  │░     •    ──                       •   •  └─  ──  •   •   •
                        │ •  ──  ──░ ───   ────────────     ░  │
                      ┌─┘┐     ──        ─┐            ────────┘
                      │░░│    │░░░░░░    ░│  ░░░░░│ │░│
                      └──┘────┘───────────┘───────┘─┘─┘─



















```

*Figure from page 4 (2346x3317 px)*


---



4203-E P-252



SECTION 2 PROGRAM OPERATION



(3) Following ">MP", enter the file name of the file to be output to the punch device using the



keyboard and press the WRITE key.



The part programs are output to the punch device.



While the program is being output to the punch device, "M-PUNCH" and the file name are displayed



at the upper right area of the screen.



At the completion of output, ''file end" appears on the console fine, then ">" appears.


#### PROGRAM OPERATION M--PIP M-PUNCH BOX-1350.MIN

97/07/15 14:10:00



=!,f>l p



>II" BOX-1350.MJN



BOX-1350.MIN file end



YJLTI



MULTI



MULTI



READ PUNCH VERIFY



(EJ @J@J @J @J @J @J @J



(4) Press function key [F7] (M-Pf P QUIT).



MULTI MULTI MULTI



READ PUNCH VER I FY



">0" is displayed.


#### M--PIP

QUIT



Press [F7]



(M-PIP QUIT).



The function key names return to those as displayed in item (1 ).


```text


                                                                                                ──
                                                                         ┌───────┐───┐─────────░░░─────────┐
                                                                         │░░░░░░░│ ░ │░░░░░░░░░ ──░░░░░░░░░│
          ┌───────  ──        ──    ───   •           ──   • ────────────┘───────┘   └─────────      •
          │       •   ────────  ────   ──┐ ┌───┐ ────┐  ──┐ •                     ───                      │
          └──────┐ ┌─┐░           ░      │ │  ░└─    │    │                   │       │              ──────┘
                 └─┘ │ ────── ───   ──── │ │   ░    ─┘ ───┘ ───── │  │    • ──┘     • │           • │
                      │░░░░░░  ░░░ ░░░░ ─┘░└┐─── ──┐░│            └──┘──── •   ───── • ─────────── ─┘
                      └──                   │      │   ──────────┐
                      │  •    ░  ░ ░ ░ ░   • ░ ░   └──    ░  ░░ ░└┐
                      │                                      •    └── ┌─ ──────────────────────────────────┐
                      │       ──  ░•   •    ░──    ──         •       │          ░    ░  ░  ░ ░ ░   ░░  ░ ░│
                     │░  ░│ ──░░ ──░──░░─────░░ ───░░•                               ───        ───────────┘
                     │    │           ──     │         ┌────────┐─┐────────┐─┐─┐─┐──┐   ┌──────┐
                      │░ ░│ │ ░░░░░░░ ░  ░░░░│ • ░ ░░░ │░░░░░░ ░│ │░  ░ ░░░│ │░│ │░░│   │░░░░░░│
                      └───┘─┘────               ────                                    └──────┘
                                 ──────────────     ────      ─────   ───────────────┐
                           │  ── ░░░░░░ ░░░░░░░     ░░░░░────░░░░▒░ ─┐     ░▒░░░▒▒░░▒│   │
                           │ │   ──────────────     ─────    ──────  └┐░░░░──────────┘   │
                           │ │                                        └────            │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │░│
                           │ │                                                         │░│
                           │ │                                                         │░│
                           │ │  ┌── ──┐──┐────  ┌─                                     │ │
                           │ │  │▒░ ░▒│ ░│     ─┘ • ──┐                                │ │
                           │ │  │   ──┘┐─┘         •  └────┐────┐─┐─────     ───────── │ │
                           │ │  │ •    │ └┐─  ────  ┌─     │    │ │     ─────          │ │
                           │  • │░░ │ │ ░░│   ░░    │    ┌─      ─┘    │░ ░            │ │
                            •   │  ░│ │ │  •  •     │    │     ┌┐ │    │                 │
                             • ─┘  • ┌┘ │    •  │ ┌─┼─┐── ─┐──┐┘┘─┼──┐─┘  ░░───┐─┐─┐── ──
                              │░ ░   │░ │  │ ░ ░│ │ │ │░ ░ │  │ ░ │ ░│ ░│     ░│ │░│ ░│
                              └───── └──┘──┘────┘─┘─┼─┘─ ──┘──┘ ──┘──┘──┘── • ─┘─┘─┘──┘
                                                    │   •      •           • •
                 ┌─┐ ┌────────────────── • ─────────┘──
                 │ │ │  ░           ░░  •
                  ─┘   ┌────────────────  ────── ────                                       ┌─┐
                       │                                                                    │ │
                       │ │                                                                  │ │
                       │ │                                                                  │ │
                       │ │   •    ───     ──     ─── ────────────────────┐─      ─────────┐ │ │
                       │ │  │ ──     ┌─     ──      │                    │  • ──┐         │ │ │
                        │   └┐▒░─┐   │░┌─┐   ▒░ ─┐  │    │ ┌┐────┐ ┌───  │  ▒ ░░│  │     • ┌┘ │
                        │    └──░│   └─┘░│   ──░ │  │    │ └┘    │ │     │  ── •  ─┘      ─┘  │
                        └─┐░•    │                   •  │    •      •   •       •  │   ──    •
                          └─    ─┘ ──┐ ┌─┐     ─┐   • ┌─┘  •  ┌──  │ ┌─┐ ┌─┐ •      ┌─┐  ┌───
                         │  │░ ░ │ ░ │ │░│ │░ │ │ │   │░│ │░ ░│▒ ░ │ │░│ │ │ ░│  ░░ │░│ ░│
                         │  └────┘───┘─┘─┘ └──┘─┘─┘───┘─┘ └─ ─┘────┘─┘─┘─┘─┘┐░│      ─┘──┘
                         │                •              •  •               │  ────
                        ─┘ ───────────┐                                  •   │░░░░░ ░ ──
                                 ░ ░  │                                 │    └────────
                      ┌─┐    ──       └───────────┐────┐──┐─┐──────┐───┐┘────
                      │░│ │░░░░│ │░│ │░░ ░░ ░░ ░ ░│ ░ ░│ ░│ │░░░░░░│ ░ │░░   │
                      └─┘─┘────┘─┘─┘─┘────────────┘────┘──┘─┘──────┘───┘─────┘




















```

*Figure from page 5 (2346x3317 px)*


---



[Supplement] 1.



4203-E P-253



SECTION 2 PROGRAM OPERATION



Command format



>MV <input-device:><input-file-name><,<Output-device:>><;option>WRITE



(a) input-device:



MD0:, MD1:, FD0:, FD1:, FD2:, FD3:



Default device is MD1 :.



(b} input-file-name



Main file name Alphanumerics (max. 16 characters), beginning with an



alphabetical letter. Wild card ("*", "?") can be used.



Extension Alphanumerics (max. 3 characters), beginning with an



alphabetical letter. Wild card<"*"·"?") can be used.



(c) output-device:



TT:, CN0:, CN1:, CN2:, CN3:, CN4:



If no output-device name is specified, the default device set for optional



parameter (word) No. 45 is selected. (Jf "5" is set for this parameter, CN0: is



selected.)



(d) option



P: Only protected files are output.



C: Only files which are not protected are output


## 2. If input file name is omitted, input file name of"*·*" is assumed and all files are

output to the punch device.


## 3. If none of the specified files exists in the input device, file is not output.

File not found


## 4. If an output file name is specified, an error occurs.

5213 File name, error 11


## 5. If only one file is output, it does not cause an error.

Example 1: >MP *.MIN [WRITE]


#### All files with extension .MIN in MD1: are output.


#### Example 2: >MP BOX1???.MIN [WRITE]

All files beginning with "BOX1" and with extension ".MIN" in MD1:



are output. Files such as BOX1001.MIN and BOX1002.MIN are



output.



Example 3: >MP [WRITE]



All files in MD1: are output.


```text


                                                                                                ─── •     •
                                                                          ┌─┐───┐─┐───┐─────────░░░░░────░░│
                                                                          │░│░  │░│   │░░░░░░░░░ ────░░░░░─┘
           ┌─────   •        ┌────────────────────────────────────────────┘─┘───┘─┘─  └─────────      •
           │     ─── ────────┘                                                                              │
           └────  ░          │        ──     ────────── ────────────────────────────────────────────────────┘
                 ──          └───────┐  ┌────          •
                   │ │         ░     └┐ │                               ──────    •       ───────────────
                   │░└──              │                             ────      ┌─── ─┐─────              ░•
                   │░│   ░░░  ░░ ░ ░░ ░─────░─── ░░   ░       •░   │░        ─┘     │░░ ░░│       ─────┐  •
                   │░│  ──── ────────── ░   •░░ ────────       ░   │                └──   └───────     │
                    • ──    •            •   •          ───────────┘────────────────                     •
                                      ┌── ┌─  ──────                                  ───────────────────
                                      │░  │░ ░ ░░░░░ •
                                      └──┐   ┌─┐ ──┐  ───┐┐──── ┌────  ──┐
                                         │░  │ │░  └──   └┘     │  ░     │
                                         └──░│ └─░       │░ ── • ───── ──┘
                                      ───     •        ┌─┘──
                                      ░   │    ░  │    │
                                      ── ┌┘       │   │      • ──  ────  ────  ┌────── ───   ── ──── ─┐─┐──┐
                                         │░░░  ░   ░ ░│     •░│  ──  ░ ┌─ ░  • │░ ░   •   ───  •    • │ │  │
                                         └─── ────────┘    │ ░│ ░      │      •       ░    ░   ░│     │ │  │
                                         │   •             │░░│ ░░ ░   │ ░░   ░    ░    •    • ░│ ░│  ░░│  │
                                         │ ░░░ ░ │         └─░░        │       ░         ────  ─┘ ─┘ ───┘ │
                                         └───────┘         │                │               ░ ░         │ └─
                                                            │  ░░    ░ • ░──┘─░   ░ ░──────────░  ░│ │░░└─
                                      ── ┌───────────┐      └────────── ──    ───────          ────┘─┘──┘
                                         │           └┐   ┌─
                                         └──── ░      │ ┌─┘ │ ┌─░─┐ │ ─┐
                                         │      ───   └─┘   └─┘   └─┘  └───   ───────   ┌───   •       ────
                                         └──░  │░░░░ ░░░░░  │░ ░    ░░░░░░░• │░  ░ ░ ───┘ ░ ─── ───┐─┐─░   •
                                         │     └─┐─┐  •     └┐┐─        ┌─ ░ │                     │ │░ ░   │
                                         └─ ───  │ └── ───── └┘   •  •  │ ───  •  ───────    ░     │ └──────┘
                                         │░•░░░░ └─             ── ── ──        ──       ────────── •
                                     ──┐ │    ───
                                      ░│ │░░░░
                                      ─┘  ┌───       ───   ───  •    ──
                                        • │   │  │ ──     •  ░│ ░ ───░░░───┐──┐─┐────┐
                                          │   │░─┘─░░───── ───┘───░ ░─┐─░░░│ ░│ │░░░░│
                                ┌─┐         •                         │  • │ ┌┘ └──┐  ┌──────┐─────┐─┐─┐────┐
                                │░│ │ ──░ ──░───░ ───  ───░░░ │░░│ ▒│ │░│ ░ ░│   ░ │░ │░░░░░░│ ░░░ │ │░│ ░ ░│
                                └─┘ └─ ░── ░•░░ ──░░░• ░░░─── └──┘──┘ └─┘────┘   ──┘──┘──────┘─────┘─┘─┘────┘
                                │ │ │                        •       •        ───
                                │░│ │    ░┌─░ ░  ░ ░ ░░  ░░      ░   ░        ░   │           ┌─
                                └─┘ │     │ │     ────────────────────────────────┘────────── │ ──
                                   •  ░░ ░└─┘░ ░░│
                                ┌─┐ │        •  ┌┘──────────────────────────────
                                │░│ │  ░ •  • │░│           ░ ░░
                                └─┘ └───┐ ┌─  │  • │       ──────────────────────
                                    │░░ │ │░│ │░│ ┌┘── ░
                                ┌─┐ └──    ─┘ │ └─┘        ─────────────────────┐
                                │ │ │   ░•    │░    ───   ░ ░     ░     ░       │
                                └─┘ │ ─── ─┐  └┐ ──┐   ────┐───┐─ ┌─────────────┘
                                    │░░░░░░│   └┐░░│ • ░░░ │░░░│░░│
                                    └──────┘──  │ • │  ┌───┘─      ─┐──────────────── ──
                                                │░ ░└─ │░    ░  ──  │░░░   ░░            •
                                     ─────────  │        •        ──┘   │ ───────────────
                                              │ │ ░│ ░  •       │   ░   └─
                                    ──────────┘ │ ─┘ ───      ──┘  ─┐─ •  •
                                                        ───         │    │          ────       •     ──
                                                ── ─────░░  ──░ ░  ─┘░ ──┘──── ░░───░ ░░─────── ░─── ░░
                                               │░░░ ░░░░─── ░░  •░• │░ ▒░░░ ░░──░░░░•░──░░░░ ░░░░░░░░•░──
                                               └───┐────   ───── • ─┘─────────   ─── •  ───────────── •
                                    ──────────     │    ───
                                              •  ░░│ ░ ░ ░░•
                                    ──────────    ─┘  ────  •
                                                │   •         ─────────
                                                └──┐░│  ────
                                                   └─┘──     ──────────













```

*Figure from page 6 (2346x3317 px)*


---



6-3. Multi-file Verify



4203-E P-254



SECTION 2 PROGRAM OPERATION



The multi-file verify function verifies multiple machining programs, stored in an external device, against



those in the NC memory.



The operation procedure is indicated below:



(1} Press function key [F5] (MULTI PIP).



=f.PIP



MULTI



DATE DIR PJP EDIT PIP LI ST CONDENS [EXTOO]



"=MPIP



>" is displayed. Press [F5} (MULTI PIP).



The function key names change as indicated in item (2).



(2) Press function key [F3] (MULTI VERIFY).



=f.PlP


#### MULTI MULTI llJLTI

READ PUNCH VERIFY



">MV" is displayed.



Press [F3] (MULTI VERIFY).



"MV" is displayed on the console line.



M-PIP



QUIT


```text


                                                                                                ──
                                                                         ┌──┐─┐────┐─┐─────────░░░─────────┐
                                                                         │░░│ │░░░ │ │░░░░░░░░░ ──░░░░░░░░░│
             • ───   •  •  ───     ────────────────────────────────────── ──┘─┘────┘ └─────────
          ┌── •    ── ─┐ ┌─   ────
          │░   ── │░░  │ │ │ │   ░┌┐────────
          └────   │   ─┘ └─┼─┼─  ░└┘
                 │         │ │     │ ──────────────────────────────────────┐───────┐─┐─┐──┐────────┐─┐──┐──┐
                ┌┘ ───   ──┘─┘   ── •         ░     ░     ░       ░  ░ ░ ░ │░  ░░  │░│ │░░│ ░░ ░░░░│ │░░│░░│
                │ ░░░ ─── ░ ░░───░░░░───               ────────────────────┘───────┘─┘─┘──┘────────┘─┘──┘──┘
                └┐                      ─┐────────┐───┐
                 │░░ │░░░░│░░ ░ ░░░░     │░░░░░░░ │░░░│
                 │ ┌─┘─   │  •    ── ──┐─┘  ─┐    │   │
                 │░│  ░░░░│ │░░░░░░ │░ │░░ │░│░░░ │░░░│
                 └─┘  ────┼─┘───────┘──┘───┘─┘────┘───┘
                          │                                                                 ┌─┐
                        │ │                                                                 │ │
                        │ │  ┌────┐                                                         │ │
                        │ │ ─┘░░  └─ ───────┐──────────────      ── ─────  ──────           │ │
                        │  │░░──┐─  │       │              ─────   │     ┌─                 │ │
                        │  │    │   │  ─┐   │ ┌┐  │  ┌┐   │  ▒░  • │   ─┐┘░───────  ┌─────┐ │░│
                        │  │  ░░└─    • └──  ─┘┘─ │  └┘── │ ─────  │ ──░│ │ ░░░░░   │ ░░░░│   │
                        │    ───┘    │                           •  •     │ •  ───        │  •
                         ─┐          └───     ──      ┌─      ─┐  ──  ─┐ │ │ ──   ──░░── │ ──
                          │  ░ │ │ ░ ░ ░░   ░ ░ ░ ░ ░ │░│ ░░   │   ░ │░│ │ │ ░ │ ░  ░ ░ ░│
                          │  ──┘─┘ ─────── ────── ──┐ └─┘ ── │ └─ ── └─┘ └─┘ ──┘─── ────┐┘
                         │                •      •  └─   •   └─┘                   •    │
                         │   │░───────┐                     │   ─┐───┐─┐───────┐
                         │  ░└─ ░░░░░░│                     │░ │░│░░░│ │░░░░░░░│
                      ┌──┘       ───── ───┐─ ───  •  ──┐── ─┘  └─┘───  └───────┘─
                      │   ─────           │ │░  ── ─┐  │░  ░
                      │                   │ │       └─ │   ────────────
                 │ │  │              │        │          ┌─
                 └─┘  └── • ────── • │ ─── ───┘──────────┘
                         │ •      • ─┘─   •
                       │ │                                                                 ┌─┐
                       │ │      ──                                                         │ │
                       │ │   ┌─┐                                                           │ │
                       │ │  ─┘▒│  ┌─             ──┐─────┐─┐─────┐───────┐─      ── ─────┐ │ │
                       │ │  ░ ░│  │ ─┐─     ── •   │     │ │     │       │    ──┐  │     │ │ │
                       │ │  ─┐░ •    │░──   ░░│ ─┐      ─┘ └───  │ ┌───  │  ░  ░│  │ ────┘ │ │
                       │     └┐░░•   │░░░•  ──┘ ░│ •     │ │     │ │     │  ────   │      ─┘ │
                        ─┐   └┘ │       │           ───┐─   • ─┐─   •   •       •  │   •    •
                         │ •   ░│  ┌─  ─┘   │ ░       ░│ ──┐ │ │ │ │ ┌─┐ ─┐       • ┌─┐ ─┐──
                            │   ░  │░ • ░   │ │ │ ░│   ░ ░ │ │░│ │ │ │░│ ░│   ░ │   │░│ ░│
                        ┌──┐┘─   ──┘ •  ────┘─┘░└──┘────── └─┘─┘─┘ └─┘─┘ ─┘──── └───┘─┘──┘
                        │  │░░ ░░░░░░░┌─      └─          •      │      •      •
                         ──┘──────────┘            ░░ ░░ ░░░    ░░░
                                                 ─────────────────────
                      ┌──────┐──────┐──┐─┐──┐────
                      │░   ░ │░░░░░░│ ░│ │░ │░░░░░│ │░│
                      └──────┘──────┘──┘─┘──┘─────┘─┘─┘






























```

*Figure from page 7 (2346x3317 px)*


---



4203-E P-255



SECTION 2 PROGRAM OPERATION



(3) Following ">MV'', enter the file name of the file to be verified using the keyboard and press the



WRITE key.



The specified part programs are read and compared to those stored in the NC memory.



While the program is being verified, "M-VERIFY" and the file name are displayed at the upper right



area of the screen.



PROGRAM OPERATION



tape end



file end



data match



MULTI



MULTI



MULTI



READ PUNCH VERIFY


#### M--P IP M-VERIFY BOX-1350. IN

97/07/15 14:10:00



M-PIP



QUIT



@J @)@J @J @J @J @J @J



(4) Press function key [F7] (M-PIP QUIT).



LIJLTJ MULTI MULTI



READ PUNCH VER I FY



M-PIP



QUIT



Press fF?]



(M-PIP QUIT).



The function key names return to those as displayed in item (1).


```text


                                                                                                ──       ──
                                                                         ┌──┐─┐────┐─┐─────────░░░───────░░│
                                                                         │░░│ │░░░ │ │░░░░░░░░░ ──░░░░░░░──┘
          ┌───────   •    ──────     ── ────────────  ── ────  ────────  └──┘ └──  │ └─────────      •
          │       ──  ────      ─────  •            ──  •    ──        ──    •   ─┐ •                      │
          └──────  ░•                 │         │                           •     │                      ┌─┘
                 ───  │ ░  ░  ──  ────┘ ────  ──┘ •  ░     ░ •░   ──    • •    ░      ░   ░      ░ ░░░   │
                      │░───── ░░│                                                                  ──────┘
                      │         └────┐──────────┐─────────────────────────────────────────┐────────
                      │ ░  ░░  ░░  ░░│ ░░░░ ░ ░ │░  ░░░ ░░░ ░░ ░░░░░ ░  ░░░░ ░░░░░   ░ ░ ░│ ░░░ ░░░│
                      │              │ ──┐      │    •   │     ──┐─ • •                 ──┘        └──┐─┐──┐
                      │     ┌─   │░ ░│   │        ░ • ── │   •   │   │░      ░   ░   ░░░░░ ░ ░ ░ ░ │░ │ │░ │
                      │░░░ ░│░───┘───┘ • └─       ──      •      └───┘─────────────────────────────┘──┘─┘──┘
                      └─────┘─                  ──  ──       ───
                                ┌────────────── ░░     ─────     ───────      ────────┐─┐
                              │ │ ░▒▒▒▒░░░░░ ░░──────── ▒░░░──── ▒░▒▒░░ ───── ▒░░░▒▒░▒│░│
                              │  ──────────────        ─────    ──────┐░░░░░░░────────┘┐
                              │                                       └───────         │ │
                              │                                                        │ │
                              │                                                        │ │
                              │                                                        │ │
                              │                                                        │ │
                              │                                                        │ │
                              │                                                        │ │
                                                                                       │ │
                                                                                       │ │
                                                                                       │ │
                                                                                       │ │
                                                                                       │ │
                                  • •                                                  │ │
                                 •░│ ┌─┐                                               │ │
                                │  │ │░└┐                                              │ │
                                │░░│ │  └┐         ──────── ──── • ─────      ──┐───── │ │
                                │        │   ┌──           │    │ │     ─────   │      │ │
                                │░░─┐   │░─┐ │░░─── ┌─   │ │ ───┘ │    │  ░   • └──    │ │
                                 •░░│   │░░│ └─░░   │    │ │    │ │    │ ┌── │  │     •  │
                                •    •              └──── ─┘────   ────  │   │ • ───── ──
                                 ░░░ ░  ░░░    ░░░    ░░   ░ ░░ ░ ░ ░░ ░ ░ ░░ ░ │ ░░ ░│
                                ─────░───────────────────────────────────────── └─────┘
                                                                               •
                 ┌─┐  ┌───┐─┐────┐───┐─── ──┐───┐─────┐
                 │░│  │░░░│ │░░░░│  ░│ ░   ░│ ░ │ ░░░ │
                 └─┘  └┐─┐┘─┘────┘───┘──────┘───┘─────┘
                       │ │                                                                 ┌─┐
                       │ │                                                                 │ │
                       │ │                                                                 │░│
                       │ │         •             ── ─────── ───── ───────        ───────── │░│
                       │ │  ───┐  • •     • ── •   │       │     │       ┌─── ───          │ │
                       │ └┐  ▒░└─┐   ┌───┐  ░░│ ── └─────┐ │     │ ┌──   │  ░│ ░   │ ────  │ │
                          │  ─┐░░└─  │░░░│  ──┘ ░░ │     │ │     │ │     │░ ─┘──   │     ──┘ │
                        ─┐    └──┘     ─┐       ─── •   •   •  ──  │   ──              •     │
                         └──            │      •     ┌─┐   • ┌─  • └─┐─       ┌──   ┌─┐ • ───
                            ┌─ ░─┐─── • ░ ░ ░ ░   ░░ │░│ ░ ░ │░│ ░   │░  ░  • │ ░ ░ │░│ ░│
                        ┌── │    │     ── ─────── ── └─┘ ─── └─┘ ────┘── ───  └──   └─┘ ─┘
                        │      │     ┌─  •       •  •   •   •   •       •   •░
                        └──── ─┘   ──┘                                   ──   ░░░░░ ───┐─
                                                                        │  • •░─────░  │
                     ┌─────┐───────┐─┐────┐─┐─┐─────┐──┐──┐─┐──────────┐┘     •     ───┘
                     │░ ░ ░│ ░░ ░ ░│ │░░░░│ │░│   ░ │░░│ ░│ │░  ░ ░  ░ │░│   │
                     └─────┘───────┘─┘────┘─┘─┘─────┘──┘──┘─┘──────────┘─┘───┘






















```

*Figure from page 8 (2346x3317 px)*


---



[Supplement]



4203-E P-256


#### SECTION 2 PROGRAM OPERATION

Command format



>MV <input-device:><input-file-name><,<Output-device:>>WRITE



(a) input-device:


#### TT:, CN0:, CN1 :, CN2:, CN3:, CN4:

If no input-device name is specified, the default device set for optional



parameter (word) No. 57 is selected. (If "0" is set for this parameter, CN0: is



selected.)



(b) input-file-name



Main file name Alphanumerics (max. 16 characters), beginning with an



alphabetical letter. Wild card



Extension



{c) output-device:



("*", "?") can be used.



Alphanumerics (max. 3 characters), beginning with an



alphabetical letter. Wild card ("*", "?'') can be used.



MD0:, MD1:, FOO:, FD1:, FD2:, FD3:



Default device is MD1 :.


## 2. If the text (tape data) read from the input device does not agree with the specified

file name, it is skipped and not verified.



In this case, the following message is displayed.



5210 Input file name not same a '(tape) file name'



a.: Number of unmatched files



If no files match with the tape data, the following message is displayed at the end.



5210 Input file name not same error



Total number of unmatched files


## 3. If input file name is omitted, input file name of"*·*" is assumed and those which

match the read texts are verified.


## 4. If unmatch is found, the corresponding line is displayed on the console line with

unmatch character blinking on and off.



The message "verify continuing (Y/ N) !" is displayed. To continue verify, input "Y'',



then the program verify restarts from the next line. If "N" is input, the file containing



the unmatch is skipped and program verify is executed from the next file.



For each file, the result of verlfy is displayed:



(a) If all data matched, the following message is displayed and the next file is



continuously verified.



tape end . file end . data match .


```text


                                                                                                ───       •
                                                                          ┌─┐───┐─┐───┐─────────░░░░──────░│
                                                                          │░│░░ │░│   │░░░░░░░░░ •░• ░░░░░─┘
           ┌─────            ─────────────────────────────────────────────┘─┘───┘─┘─  └─────────     ──
           │     ────────────                                                                              │
           └────  ░             │     ──              ──── ────────────────────────────────────────────────┘─
                 ──          ───┘────┐  ┌─────────────    •
                   │ │     ░ ░     ░ └┐ │                               ───       ──────────────────────┐
                   │░│ •              └─                            ───    ─┐─┐──┐                      │░
                   │░│   ░░░ ░ ░░░ ░░ ░░──── ░░░ ░░──░░   ───  ░   ░░  ──   │░│ ░│   ──       ───────  ┌┘░│
                   │░│  ──── ───────────    ───────  ────      ░   │       ─┘─┘   ───  ───────       ──┘  │
                   └─┘──    •                            ──────────┘───────    ───                       •
                                      ┌─────────────                               ──────────────────────
                                      │░  ░░ ░ ░░░ ░─┐
                                      └──┐─────  │   │  ┌───┐ ───── ┌───
                                         │     ┌─┘┐──┘──┘   └─      │  ░──┐  •   ─────   ───┐─ • •  •     ─┐
                                         │  ░  │░░│ ░░ ░░  ░░ ░ ── │   ░░ └┐─░• •░░   ┌─┐   │ │ • ░│ ┌───┐ └┐
                                         │     │ ┌┘  •  │   ─┐┐    │░   ┌─ │          │ │    ─┘  ──┘ │░  │  │
                                         └┐ ───┘ │    • └─ • └┘─  ┌┘░• ░│ ─┘────  │   └─┘░░ ░░░░ ░░░  ──░│ ░│
                                         └┘─░░░░─┘     •  •     ──┘ • ──        ──┘───┘  ────────────   • ──┘
                                     ┌─┐ │         ───┐
                                     │░│ └─░░  ░│ │░░░│
                                     └─┘ │      │ │   │      ──            ──  ┌──  ──────────── • ─── • ──┐
                                         │░░   ░│ │░░░│    ─┐░░░────░░ ░──░░░──┘░ •░░░░░░ ░  ░░░ ░░ ░ •░│ ░│
                                         │        └───┘─    └───░░░░────░░───░░░──░───────────────┐───░─┘  │
                                         └────────         │                                      │       ─┘
                                           ░░ ░░░░•        └┐░─────░░░ ░──░░░───────░░░░ ░ •░░░•░ ░░ ░░─┐░░│
                                              ──            │░░░░░░─────░░───░░░  ░░───────░───░───────░└──┘
                                      ─┐─┐──┐─  ─────┐       •  ───     ──   ───                       •
                                     •░│ │░░│ ░│░░░░░│
                                      ─┘ │   │ └── •  ──┐─┐──┐──┐──┐─┐───┐
                                         │░░─┘ │░░•  ░░░│ │░░│  │░░│ │░░░│
                                         └── │ └──    ──   ──┘ ─┘──┘─┘───┘
                                      • •     •      •  ──┐  │
                                ┌─┐  │ •       •          │  └─       ───────┐─┐──┐─┐──┐───┐─┐─┐─┐──┐──────┐
                                │ │ ┌┘  ░ •    ░ ─── ── ░░│    ──────░░░ ░░░ │ │░░│ │░ │░░░│ │░│ │░ │░░░░░░│
                                └─  └┘░───░────── ░░•░░░──░──── ░░ ░░───       └──┘─┘──┘───┘─┘─┘─┘──┘──────┘
                                    │                                   ──┐───┐
                                    │  │░░•░░░• ░── ░░ ░░ ░ ░░░░░░│   ┌┐░░│░░░│
                                    └──┼──                        │   └┘   ──  ─┐───┐
                                       │    ─────┐  ──────────────┘    │░░░   ░ │░░░│
                                        ───░░ ░░░└─┐   ░░░░ ░░ ░░░│     ───     │
                                    ───          │ │                ───┐   ───── ───┐─┐───┐──────┐────┐────┐
                                        ──░• •░░ └─┘░  ░░ ░░░░ ░░░  ░░ │░░░░ ░ ░░░░░│▒│ ░ │░░░░░░│ ░ ░│ ░ ░│
                                     ──┐  •                             ──┐─────────┘─┘───┘──────┘────┘────┘
                                       │    ──    ────    ── ───░─────┐   │
                                       │░───░░░─── ░░░ ───░ •░░░•░░ ░░└─
                                ┌──                                     ─┐─┐──────┐──┐───────────────┐─┐───┐
                                │░  │ •░───░░ ┌──────────░░░────┐ ░│  ░░░│ │      │░ │░░ ░░░░ ░░ ░░░░│ │░░░│
                                └── │  ░   ───┘ ░        ──   ░ └──┘─────┘─┘──────┘──┘───────────────┘─┘───┘
                                │   │                      •
                                │ │ │     ───                     ─────  ──────────────────────────────────┐
                                └─┘  ───┐─    ─────────────┐─                                     ░   ░  ░░│
                                    │░░ │░───░ ░░░░░   ░░░░│ ──── ░ ───           ────             •    ───┘
                                    │   │                  │               ──────      ───     • •
                                      ─┐ ───────────────┐─┐┘───────────────░░░░░░• ────░░░─────░•░───░─────┐
                                     ░░│ ░ ░░░░░░░░  ░ ░│ │░░░░░ ░░  ░░ ░░░░░░░    ░  ░  ░░░ ░░ ░░  ░•░░░░░│
                                    ┌──┘┐─────┐─────────┘─┘───────────────────    ░ ──  ──░───  ░•░┌─ ─────┘
                                    │   │     │                               ──────  ──  •   ─── ─┘
                                   │░ • │░ ░ ░│ •░•  ░░░ ░░ •░░────░░░░░░░─┐
                                   └─┐  │    │   •           ─┐     ────── └─────────────────────────────
                                     │░│ ░───┘─── • ░───┐─░│  │░                                         │
                                     └─┘─┐          •   │  └──┘──────────────────────────────────────────┘
                                         │                │
                                          •       ┌─┐     │  ┌─┐────
                                           ───────┘ └─────┘  │ │    ──
                                                              • • ──















```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-257


#### SECTION 2 PROGRAM OPERATION

(b} If file data remains although text (tape data) has been read to the end, the



following message is displayed on the console line and the next file is



continuously verified.



tape end



data match



(c) If tape data remains although file data has been read to the end, the



following message is displayed on the console line and the next file is



continuously verified.


## 5. If an output file is output, it does not cause an error.

5213 File name, error 11


#### Example 1: >MV *.MIN [WRITE]

Verify is made with the files which have the same file name as the input



files, having extension .MIN.



Example 2: >MV BOX1 ??? .MIN [WRITE]



Verify is made with the files which have the same file name as the input



files, having extension .MIN and beginning with BOX1. The files such



as BOX1001.MIN and BOX1002.MIN are examples of such files.



Example 3: >MV [WRITE]



Verify is made for all input files with the files having the same file name.


```text


                                                                                                  •
                                                                          ┌─┐─────┐─┐─┐─────────░░░──────────
                                                                          │░│░░░░░│ │ │░░░░░░░░░ ── ░░░░░░░░░
           ┌───────────────────────────       ──  ─── ─────   ─────────  ─┘─┘─────┘   └─────────      •
           │                           ─┐────┐  ──   •     ┌──         ┌─                                   │
           └──────────────────────────┐ │ ░  │ │         │ │           │       │                           ─┘
                                      └─  • • ─┘─────────┘ │  ──────      ┌─┐  └──    ░ ───     ────░  │  │
                                          ░░░░░░░░ ░░░░░░░ ░ ░░░░░░░░ ░░•░│ │░░░░░░• ░•░░  ░ • ░░░ ░┌─░└──┘
                                          ──────────┐────░░───────────── ─┘─ ────── ── ─── ── ──────┘ ─┘
                                                    │    ──
                                            ┌──┐ │░─┘─
                                            │░ └─┘─░ ░│
                                       •  ┌─          └─     ──
                                      │ • │ │    ──       ───    •  ──────── ─┐       ────   ┌─ ─┐   •
                                      └─  │ └── •  ──── ──     ── ──         ░└───  ──     • │ │ └── ░──
                                          │░░░░ ░ ░ ░░░░░░ ░ ░░░░░░░  ░░ ── •░ ░░░░ ░░ ░ ░ ░░│ │░│ ░░ ░
                                         ┌┘──────────────────────────────  • ──────────────── • ─┘──────
                                ┌─┐ ┌───┐┘
                                │░│ │░ ░│ ░ ░ ░ ░│ ░   ░     ░ ░
                                └─┘ └───┘───    ─┘ ─┐    •  •      ───────────────
                                            │░░   ░░│ ░░░░┌─░ ░  ┌─
                                ┌─────┐─┐── └┐ •  ─┐┘─   ─┘  • ──┘
                                │░░░░ │░│    │░░•  │░░•░░░░•░░•
                                └─────┘─┘── │                  ────────┐─┐─┐─────┐─┐──────┐────────────────┐
                                            └┐─ ░ ───┐─░░──░──░░ ░░░  ░│ │ │░ ░ ░│ │░ ░░ ░│   ░   ░ ░░     │
                                            └┘ ┌─┐   │ •   •   ──┐  ───┘─┘─┘─────┘─┘──────┘────────────────┘
                                             │ │ │   │░          │
                                 ┌────────┐  │ │ │              ─┘   ──
                                 │        │   ─┘ └───    ───┐─ •     ░
                                  ────────  │          •    │           •    ──             ───     ───   ──
                                            └──┐─┐─────░────┘────┐──┐───░──── ░───────────── ░░─┐───░░ ──░░
                                            │░░│ │░░░ ░ ░░░ ░░░░ │░░│ ░░░ ░░░ ░░ ░ ░░░ ░░░░  •░░│ ░░░──░░───
                                            └──┘─┘────────░───── └──┘  ░░ │░┌────░  •  ───     ─┘────  ──
                                 ─────────  │             •     ─┘   ─────┘─┘    ──   •     ──
                                 ░        │  •░│ ░ ░   ░•
                                 ─────────┘   ─┘ ──── ── •
                                            │        •    ────────────────────────┐─┐─┐──────────┐──┐─┐────┐
                                            └┐  │     ░      ░  ░   ░░░ ░   ░   ░░│ │░│ ░ ░░░ ░░░│ ░│ │░░░░│
                                             └──┘─────────────────────────────────┘─┘─┘──────────┘──┘─┘────┘











































```

*Figure from page 10 (2346x3317 px)*


---



6-4. Quitting Multi-file Transfer



4203-E P-258



SECTION 2 PROGRAM OPERATION



This function is used to quit the multi-file transfer mode and to return to the program operation mode.



(1) Press function key [F7] (MULTI QUIT).



MULTI MULTI MULTI



READ PUNCH VER I FY



">Q" is displayed.


#### M-PIP

QUIT



Press fF7]



(M-PIP au1n.



">Q" is displayed on the console line and the system quits the multi-file transfer mode. The screen



returns to the program operation mode screen and the function key names as indicated below are



displayed.


#### DATE

DIR



PIP



EDIT



~~Tl



LIST



CONDENS



[EXTEND]


```text


                                                                                                ──        •
                                                                         ┌──┐─┐────┐─┐──────────░░────────░│
                                                                         │░░│ │░░░ │ │░░░░░░░░░░── ░░░░░░░─┘
             ──────              •       •   ──────────────────────────── ──┘─┘────┘ └─────────
          ┌──      ─────┐─┐─┐───┐ ┌─┐─┐── ───
          │░  ┌── │    ░│ │ │   │ │ │ │       ────
          └───┘  ┌┘    ─┘ ░ └──┐┘ │ └─┘ ░ •  •
                 │   │     •   │    │ │    ┌─  ──────┐──────────────────────────┐────┐───┐─┐────────┐─┐──┐
                 └─  │  • │    │ ──   │    │       ░ │░         ░ ░ ░ ░  ░    ░ │░ ░ │░ ░│ │░░░░░   │░│░░│
                 │  ─┘   ─┼────┘   ─┐─      ──      •  ┌────────────────────────┘────┘───┘─┘────────┘─┘──┘
                  ┌┐  • ░░│ ░░░░░ ░ │░ ░│   ░░      ░  │
                  └┘   ┌─┐┘─────────┘───┘──────────────┘
                       │ │                                                                 ┌─┐
                       │ │                                                                 │ │
                       │ │                                                                 │ │
                       │ │                •      ──┐─────── ─────── ──────                 │ │
                       │ │  ┌──┐     ┌─    ┌──     │       │       │      ─┐────           │ │
                       │ │  │▒░└─┐   │░──  │░░───┐ │  ───┐ │  ───┐ └─────┐ │▒░ ░   ┌─────  │ │
                       │  ┌─ ─┐░░│   │░░░   •░░ ░│ │     │ │     │ │     │ └─────  │     ──┘ │
                        • │░  └─┐┘     ──    •  ─┘─ ──  │   •  ──  └─   •  │       │   •     │
                         │ •    │                     ┌─┘  •  •  • │ ┌─┐ ──┘░░░  ── ┌─┐ • ───
                         │  ┌─ ─┘ ┌── ░ ░ ░ ░ ░   ░   │░│  ░ │░│ ░ ░ │░│ ░    ░   ░ │░│ ░│
                        ┌┘  │░   ─┘    ── ─── ─── ──  └─┘ ── └─┘ ────┘─┘ ──┐  ┌─ •  └─┘ ─┘
                        │             •  •   •   •  ──   •  •   •       •  └┐░│   •
                        └─────── ─────                                   •  │ ░░░░░░───┐
                                                                        •    ───────░  │
                       ┌─────────────────────────┐─────────────────   •                 ─┐─────    ─┐─ ───┐
                      ┌┘░░ ░ ░░░░░░░░ ░ ░ ░    ░░│ ░░     ░     ░  ───░│ ┌───────┐──── •░│     ─┐ •░│ •   │
                      │      ────        •       │ │                   │ │       │       │      └─         │
                      │ ─────      ─┐   • ─┐    ─┘ │   •     ──░ ──── •     │ │░░ │░ ░░ ░│ ░░░ ░░░ │░░ ░ ░░│
                      │ ░░░░░░┌─ ── └───   └────  • ─── ─────  ──    • ─────┘─┘───┘──────┘─────────┘───────┘
                       ───────┘

                       ┌─┐                                                                 ┌─┐
                       │ │                                                                 │ │
                       │ │                                                                 │ │
                       │ │ ┌────── ──────   ───                                            │ │
                       │ │ │      │      ┌─┐     ┌─┐    ─┐─    ───────  ─┐─                │ │
                       │ │ │  •  ─┘   ┌─ │ │     │░│ ─── │  │░ ░  ░   ─┐ │ ──────░  ────   │ │
                       │ └┐ ┌─ ─┐ │  ┌┘  └─┘   ░ └─ │   ─┘─ │░ ─────   │ │              ─┐─┘ │
                       │  │ │   └─   │              │                  │       ─── •░   ░│   │
                        ──┘  ───┘ ───┘┐─┐──────┐─ ──┘┐────── ┌─┐─────┐─┼──────┐   • ┌─   └───
                            │  ░│ ░ ░ │░│ ░ ░ ░│     │░░ ░ ░ │░│   ░ │░│    ░░│ ░ ░ │░│  │
                            └─░─┘ ░───┘─┘ ─────┘  ── └── ─── └─┘ ────┘─┘ ── ──┘─┐─┐ └─┘ ┌┘
                              •  ──      •      ──  •   •   •   •       •  •    │ │    ─┘





































```

*Figure from page 11 (2346x3317 px)*


---



4203-E P-259


#### SECTION 2 PROGRAM OPERATION

6-5. Notes on Using Multi-file Transfer Sub Commands



Send



(1) Communication Text Format



The text format used in multi-file transfer operation differs from the format used in a single file



transfer operation. The format used in multi-file transfer operation is indicated below.



(a) ISO code



File



% CR



File


#### LF NC program % $ %,CR LF NC program

......



% %



name name



------ First file ---------- Second file Last file



1} The file name is preceded by "$" symbol.



2) The data which follows "% CR LF" is regarded as the machining program.



3) The program end code is fixed to"%". (NULL code is not allowed.)



4) The end of communication code is fixed to"%%". (NULL code is not allowed.)



5) Leading and trailing feed holes (NULL or space) are not provided.



(b) EIA code



File File



$ ER EOB NC program ER $ ER EOB NC program



.....



name name



ERi



------ First file



------+1<1-----



Second file Last file



---.J



1) A fife name is preceded by "$" symbol (set for optional parameter (bit) No. 31).



2) The data which follows "ER EOB" is regarded as the part program.



3) The program end code is flxed to "ER". (NULL code is not allowed.)



4) The end of communication code is fixed to "ER ER". (NULL code is not allowed.)



5) Leading and trafling feed holes (NULL or space) are not provided.



(2) Timing Chart



(a) Multi-file read and multi-file verify (CNC: master)



DC1 DC3 DC1 DC3 DC1 DC3 DC1 DC3



(CNC-Hosn



\ t \ t t \ t



Receive Communica- Communica- % Communica-



(HOST -+CNC) tion text 1



tion text 2



) tion text n



%! %fl_



Infinite



1--1



1--1



[Supplement] 1 . The DC3 code ls output in the following cases.



(1) Just after receiving the text file name



1--1



(2) Just before writing text name to output device (every 252 characters)



(3) Just after receiving "%" code at the end of a part program



(4) Just after receiving"%%" code which indicates the end of communication.

2. t1



"t1" indicates the "RS232C ready wait time" set for parameter.



(b) Multi-file punch (CNC: master, DC2/DC4 code output)


```text


                                                                                                ───
                                                                         ┌──┐─────┐───┐───┐─────░░░──────░░│
                                                                         │░░│░░░░░│   │░░░│░░░░░───░░░░░░░─┘
               ────      ──────        •       ────   •     •   ───────   ──┘─────┘───┘───┘────
           ────     ─────      ──────── ─┐── ──    ─── ── •  ┌──       •
          │    ────            ░        ░│            │ ░  │ │          │
          └────    ───┐────── ─── ───────┘───   •░ ░ ░│ • ░│ │  ░ ░ ░ ░ │
                  │   │      •   •            •  ─────┘  ── • ──────────
                  │ │ │ ░░░░░░  ░░░   ░░░░ ░ •░•
                  └─┘ │  │ •   │                 ─┐   ─────     ──    ───        •               ───┐─┐─┐──┐─
                        ░└─░░░ │░──── ░░░──────░• └───░ ░░░───░│ ░────░░░ ───────░──┐───────░──── ░ │░│░│ ░│
                        •░░░──░░• ░░  ───░░ ░░ •░─┘░░░──── ░░ ─┘ • ░░░░───░░░░░ ░•░ │░░░░░░ •░░ ░───┘─┘─┘──┘─
                    ┌─           •   •   ─────     ───     ──      ───     ─── ──  • ── ───    •
                    │░• │░│ • ░│
                  ─┐ •  └─┘  ──┘┐    •      ────────    • ─┐─     ────   • ─┐─   ────────── • ─────┐─ ─────
                 • └┐       •   └─┐─┐ ┌──           ──┐┐ • │ • •      ┌── • │ ──┐          │ │     │ │
                │   │ ░┌──── ───  │ │ │  ┌─────────   └┘  •   │░───┐ ┌┘  •      └─┐────────┘ │     │ │   ───┐
                │   │  │░ ░   ░   │░│  │ │░  ░░░░░░  │  • ░   │░░░░│ │   ░░      ░│ ░░░░░░░  └─────┘  ░  ░  │
                │ ┌─┘  └───────── └─┘  └─┘───────────┘─   ────┘────┘   ───── ┌─ ──┘─────────┐       ┌──────┐
                │ │                    │               ┌─┐         │ ──     ─┘ •            │ ──┐── │      │
                │░│              •  ░  │               │░│          •░░░░░░ ░░•              │░░│ ░░│      ░•
                └─┘───────┐ ┌──                    •         ──       ──  • ──               └──┘───┘ ──────
                          └─┘  ─────────────────── ░────────┐░ ░░─────  ── •  ───────────────
                          │░│ │░ ░ ░░░ ░░░░░ ░░ ░░──░ ░░░  ░└───░░░░░░  ░░ ░░ ░░░░  ░   ░     ░
                          │ │ │ •  ──                      │    │    •                 │   ──
                          │ │ │   •  ───  ─────────────────┘ ───┘     ──   ────── ┌────┘ •   ──────┐
                          │░│ │░ ░ ░░░ ░ ░░ ░░░ ░░░░░░ ░░░░ ░ ░░░░░│ ░ ░ ──░░░░ ░ │░░░ ░  ░ │░░░░░░│
                          │░│  ──░░░• ░  •░ ░•  •░───  ░───░ ──────┘ ░  •   ───   └──  ┌────┘──────┘
                   ┌───┐──┘ └┐   ─── ──── ─── ── •   ───   ──      └──── ───   ───   ──┘
                   │░░ │░░░  │░──
                 •  •    ──                   •          ───                           ── ────────┐─
                • ──   ─┐  ───┐─┐─┐──┐──────── ───┐───┐──    •  ┌──────────┐──┐─         │        │ • ┌─┐ ─┐
               │      │░└──   │░│ │░ │ ░          │  ░│     │░┌─┘          │  │ ──┐───┐  │        │   │ └─ │
               │      └─┘░░  ─┼─┘─┘──┘ ──         │ ─┐┘     └─┘ ░ • •   ───┘      │░ ░│  │ ────── │        │
                ┌─┐      ───  │                      │ │       ───            ────┘───┘──┘       •  ┌──────┘
                │░│ ──      ──┘┐    ──  ─────────────┘ └────      ─┐─       │               │       │      │
                └─┘─  ──       │      •                            │  •    ─┘               │      │     │ │
                            │ ┌┘─   │  •   ┌─  ───┐     │   ───      │  │    •  ──   •  ────┘      │  ───┘─┘
                          │ │ │  ───┘┐  ───┘ ──   │ ────┘┐─┐   ──────┘──┘──┐─ ──░ ─┐─ ──  ░   │ │ │
                          │░│ │ ░░ ░░│ ░░░░  ░░░░░  ░░ ░░│░│ ░ ░░░░ ░░░░░ ░│ ░░░ ░░│░░░░┌─────┘─┘─┘
                          │░│ │░─────┘░░───────────░─────┘─┘─────────░•   ─┼─────┐─┘────┘
                          │ │ └─                                       ──  │     │       ────────────┐
                          │░│ │  ───    •     ░   ░  ─── ░ ───░      ░     │ │ ░  ──┐ ░░ ░  ░ ░░░░░░ │
                          │░    ░░░ ░ ░░  ░│ ░░░░░░░• ░░──┐░░░─────░░░ ░ •░│ └─ ░ ░ │░░──────────────┘
                  ─┐  ────┘      ┌─────────┘──────── ───  └───     ────── ─┘─  ─────┘──
                  ░│    ░ ░│   ░░│
                  • ┌─ ┌─┐ │ •   └───────┐─┐──┐─┐──┐─┐───┐─┐─────┐
                    │░ │▒│░ │░│ ░░░ ░░░ ░│░│ ░│ │░░│ │░░░│ │░░░░░│
                    └──┘─  ─┘─┘──────────┘─       ─┘─┘───┘─┘─────┘ ──┐    ┌─┐               ┌─────┐    ┌─┐
                         ░│                 ░                     •░ │    │░│               │░    └─   │░│
           ┌───┐─┐───┐── ─┘  ─────────────┐ •       ─────────────┐ ┌─  ─┐  │ ────────────── └─┐───  │ │ ─┘
           │░░░│ │ ░ │                    │                      │ │  │░│ ┌┘                  │     │ │   •
           └───┘ └───┘─   •  │            │░│    •  │            │░│  └─┘─┘┘┐ •               │ │ ──  │░┌─
                           │░│  ──────── ─┘ │     •░│  ───────┐─┐┘ │        │  • ───────┐─┐──  ─┘    │  │
           │░░░   ───┐──── │ │ •░ ░░      ░ └────     ░░░░ ░░░│ │░ └──┐─┐──  │░ ░░░░░░░░│ │░     • │ │  └───
           └──░•    ░│    ─┘ └─░  ░┌──── ───     ┌─   ────────┘─┘──   │░│   ─┘  ────────┘─┘──      │ │  │
              •  ────┘───   ░  •  ┌┘        ──── │░░                ──┘─┘──   │                    │ │  └───
                            ┌── ──┘               ──  │                      ─┘──                  └─┘──
                ┌───────────┘     │ ┌────┐─┐─┐──┐─  ┌─┘──────────────────────
                │  ░░    ░  │   │ │ │    │ │ │░ │ ░ │░      ░   ░ ░░░░░ ░░░░░•
                 ───────────    └─  │ ┌─┐  │ │  │               ─┐┐──    ────
                                    └─┘ └┐─┘   ─┘─   ── ░ ─┐ │ │ └┘          ────────────────────────
                                    │░│ └┘ └─┐─░ ░───░   ░ └─┼─┘           •░                        │
                                    └─┘ │  │ │          │    │  •  ──┐   │       ──   ┌─  │ ─────────┘
                                    │░│ │░░│ │░┌─┐░░░░ ░│ │░ │░░░• ░ │░•░│░ ░ ░ ░░░   │░│░│
                                    └─┘ │  │ │ │ │      │ │   ─┐─     │  │            │ │  ─┐───────┐────┐
                                    │░│ │ ░│ ░░░ │░░░ ░░░│ ░   │ │░ │░│░│ │░░ │░│  ░│ ░ ░ ░ │ ░░  ░ │░░░ │
                                ─┐    │ └──┘─────┘───────┘─────┘─┘──┘─┘─┘─┘───┘─┘───┘───────┘───────┘────┘
                                 │  │ │
                                ─┘  │ └─┐───────────┐───────────┐─┐──────┐─┐─────┐────────┐
                                     │  │ ░ ░     ░ │        ░░░│ │░░    │ │░░ ░ │░░░░░░░░│
                   ──────────────────┘    ─┐  ──┐   │          ┌┘ │  ─┐──┘─┘─────┘────────┘
                        ░░  ░░   ░      ░• │ ░░░│           │░░│ │░░░░│
                    ─── ───────────────── ─┘────┘───────────┘──┘─┘────┘








```

*Figure from page 12 (2346x3317 px)*


---



Send



Communica- % j



(CNC-,.HOST) oc



tion text 1



Cornmunica- %



tion text 2



4203-E P-260



SECTION 2 PROGRAM OPERATION



Communication %% I ._I ___



text n DC4



(c) Multi-file punch (CNC: master, DC2/DC4 code not output)



Send



__J



Communica- %



(CNC-HOST) tion text 1



(d) Multi-file punch (CNC: slave)



Send



(CNC-+HOST)



Communica- %



tion text 1



Communica- %



tion text 2



Communica- %



tion text 2



Receive



(HOST-CNC)



1 DC3 DC1



Infinite



Hts



[Supplement] 1. t2



}J Communication



text n ,___ __



I Communica-



) tion text n



\ t \ t



DC3 DC1 DC3 DC1



t2 t2



Hts



"t2" indicates the "RS232C ready wait time" set for parameter.

2. t3



"t3" indicates the "RS232C ready wait time" set for parameter.



(e) Multi-file read and multi-file verify



Receive



_J I



Communica- %



(HOST -CNC) oc



Communica-



tion text 1



tion text 2



JJ Communication %% j



!~--



text n (DC4)


```text


                                                                                                ──        •
                                                                         ┌──┐─┐────┐─┐──────────░░────────░│
                                                                         │░░│ │░░░ │ │░░░░░░░░░░──░░░░░░░░─┘
           ────────────────────────────────────────────────────────────── ──┘─┘────┘ └─────────
          •                                                                                                │
           ──                             •     •          •     ──                      ──────────────────┘
                             • •   ── ──── ─────         ── ─── •  ┌──    ──────       ─┐
             ──────────┐──┐── │ ───░░•░ ░   ░     ───────          │░ ┌───  ░      │ ── └┐─────┐
             ░░░░      │  │   │  ░░•░░────────── •░░ ░░ ░──────────┘─ │░░ ─────────┘     │     │
             ──────────          ── ──            ───────             └──┐          ──┐ ┌┘─────┘
                       ┌───   ┌─   •  ┌──┐──┐────┐       ─┐─┐──┐─┐────   │            └─┘
                   │░  │░░░░ ░│ ░ ░░│ │░░│  │░░░░│ ░░░░░░░│ │░░│ │░   ░ ░ │
                   └───┘──────┘─────┘─┘──┘──┘────┘────────┘─┘──┘─┘─  ─────┘
                                                                   ┌─
             ┌───       ─────   ┌────────   ┌─┐  ┌─────────  ──┐   │░  ──────────  ────
             │░░░ ─────       ──┘ ░░░░░░░   │░│  │ ░░░░░░░     │ ──┘─ │ ░  ░░ ░░   ░ ░
             └───               └────────    ─┘  └────────   ──┘      └──────────  ───
                        ───────          •
                    │   ░ ░    ───          ┌───┐
                    │  ───────    ────────  │   │
                                             ───  •          •                         •
                         ┌── ───────── ──┐─      •  ────────  ┌─┐           ─────────── ──┐       ┌──┐
            ┌─┐──┐────   │  │   ░ ░░░    │      │   ░░   ░░░ ─┘░└─ ─┐─┐────┐       ░░    ░│  ─────┘░░│
            │░│  │░░ ░┌──┘  └────────  ──       │  ────░───── └─    │░│    │  ───░───── ──  │     │ ┌┘
             ─┘  └────┘  │░│              ┌─┐   │░│    •        ┌┐─  ─┘────┘     •        │ └─    │░│
                         └─┘            ┌─┘░└─ ┌┘ │            ┌┼┘░•       │ •           ┌┘   │  •  │
            ░░•░░ ───┐─┐─  └────────────┘     ─┘  └────────────┼┘   ─┐──┐──┘  ┌──────────┼┘ │ └──   └───────
           ───░── ░░░│ │   │            │  •      │            │     │ ░│  │  │          │  │  ░    │
              •  ────┘ │ ──    ─────────┘ •   ┌───┼────────────┘     └──┘──┘──┘──────────┘ •    ┌───┘───────
                      ─┘─  ───┐         └┐ ░ ░│   │            └┐ ░ ░│                    │ ░ ░ │
                     •░ ░ │░ ░│          └───  │  │             └────┘                    └───┐░│  │
                      ─── └───┘               ─┘──┘                                           └─┘──┘
                ┌─────   •          ┌─
                │░░░░░     ░│       │░│
                └───────────┘       │ └─┐─────────┐─┐──────┐─┐────┐───────────────────────┐
                                    │░│ │░░ ░░░░ ░│ │░░░░░░│ │░░░ │ ░ ░  ░  ░░     ░ ░  ░ │
                                ┌─  │ └─┘─────────┘─┘──────┘─┘────┘───────────────────────┘
                                │   │░│
                                └─  │ └─┐─────────┐─┐──┐───┐─┐──┐─┐────┐─┐─┐──────────────┐
                                    │░░ │░░ ░░░░ ░│ │░░│░░░│ │░░│ │░░ ░│ │ │      ░░ ░░░░ │
                   ┌─┐─┐──────┐─────┘   └─────────   ──┘───┘─┘──┘─┘────┘─┘─┘──────────────┘
                   │░│ │░ ░ ░░│ ░░  ░░░   ░░  ░    ░│
                   └─┘─┘──────┘─────────────────────┘
                                                        ──────────────      •          ──
             ┌────────────┐─    ┌─────     │░    ┌──────            ░ ──────  ──   ───┐  ┌──────
             │░░░░        │  ┌─ │░░░░░─────┘──── │░░░ ░  ──────────── ░░ ░  ──  • •   └─ │
             └────────────┘──┘  └─────           └───────             ─────         ─┐  ┌┘──────
                                                                                     └──┘


































```

*Figure from page 13 (2346x3317 px)*


---



4203-E P-261



SECTION 2 PROGRAM OPERATION



(3} Parameter Settings



Before connecting an external device, it is necessary to set the following parameters.



For details of parameters, refer to III "PARAMETERS".



(a) Optional parameter (bit} No. 1, 8, 12, 13, 14, 21, 22, 40



[Supplement] 1. In multi-file transfer operation, since the tape delimiter code is fixed to"%" or "ER",



the parameter (No. 1, bit 3) used for this setting is not used.


## 2. Verify in tape reading is effective only when the input device is TR: {tape reader).

Therefore, the parameter {No. 1, bit 4) used to set the device is not used in multi-file



transfer operation.


## 3. The multi-file transfer operation supports only standard DC code. Therefore, if the

parameter setting* is for "DC code control type 2" or "no DC code control", an error



occurs.



Bit 5 and 6 of No. 8, 13, 14, and 15:



Setting should be ON for bit 5 and OFF for bit 6.



5261 Device name error 1 'CN0'



Varies depending on the selected device name


## 4. In multi-file transfer operation, since file name punch is fixed to "yes", the

parameter (No. 12, bit 2) used for this setting is not used.


## 5. In multi-file transfer operation, since feed hole punch is fixed to "no", the parameter

(No. 12, bit 4 and bit 5) used for this setting is not used.



(b) Optional parameter (word) No. 6, 34 to 42, 45, and 57



[Supplement] 1. In multi-file transfer operation, if "5" is set in the punch device name designation



(No. 45), it selects "CN0:" instead of "PP:".


## 2. In multi-file transfer operation, if "0" is set in the tape read device name designation

(No. 57), it selects "CN0:" instead of 'TR:".


```text


                                                                                                ───       •
                                                                          ┌─────┐─┐─┐─┐─────────░░░───────░┌─
                                                                          │░░░░ │░│ │ │░░░░░░░░░ ──░░░░░░░─┘
           ┌──────   ──  ──          ─────────────────────────────────────┘─────┘─┘─  └─────────      ──
           │      ┌──   •  ────┐─────                                                                       │
           └──────┘   •        │ ░      │      ───    •                           ──────────────────────────┘
                  └──          │      ░ └──┐───   ┌───                     •
                      │░ ░           • │   │      │    │      • ────┐ ───┐  ┌──┐  ────────────────
                      │     ────      ─┼───    ──      └────── •    └─   │ ─┘  └──
                      └─  •░░ ░░     •░│ ░░ ───░░│ ░     ░░░░░░░   ░░ ─┐     ──   ───────────────
                     ┌┘    ─────    •    ──     ─┘ ┌──  ─┐───────┐──── │
                    ─┘┘ │               │  •  ░    │     │       │     └─
                      │ └───  ──┐  ─┐───┘          │  •         •
                 ┌────┘─     │  │   │            •      •                ──   ─────    •  ────┐──┐──────────
                 │   ░      ─┘  │ │  ──────  ───   ░│  ░░░ ░ ░────░• ┌─ ░░░───░░ ░░────░░   ░░│ ░│ ░  ░   ░
                  ──────────      │ │░ ░░░░──░░░────┘───────── ░░░•░─┘░───░░░ ─────░ ░░──────   •
                                ┌─┘ │                                                        ┌── ┌─────────
                                │░│  │░░░────░░░• │░░────░ ░░░░░░───░┌─┐─░──░─────┐──░───░ ░ │░  │░░░ ░░░░░─┐
                                └─┘  └───     •   └──     ──────┐   ─┘ │    •     │           •    ┌─   ░•░ │
                                     │    │      •    ────      └──   •  ─── • ──  • •      •  •  ─┘ • ── ──┘
                                    │░ ░──┘ •░░░░░░•
                                ┌─┐ │                •   ── ───    ───   ───────────────────    ─────── ───┐
                                │░│  ──────────░──░──░───░░░░░░─┐─ ░░ ───░░░ ░░░ ░░░░ ░░ ░ ░│ ── ░ ░░░░•░ ░│
                                └─┘ •░░░░░░░░░ ░░░•░░•░ ░───░── │░─── ░░  • ────────────── ─┘   ░─────░  •░└─
                                     ────────  ─── ──  •       ─┘─     •   •                 ──        •
                                                     •
                                       │░•          ░ │ ░ • │    • │ ┌─
                                       │  ───         │ ──  └────  └─┘ ──┐────────┐
                                       └┐░░░ ░ ░│  ░ ░│ ░░░ ░ ░  ░ ░ ░  ░│ ░   ░  │
                                        └─┐ ── ─┘       •          │  • ─┘────────┘
                                          │░░░│ │░░░░│ │░│░░ ░ ░   │░░░│
                                          └───┘─┘────┘─┘─┘──────── └─┐─┘
                                                                   │ │  •  ──┐─ • ───── •         •
                                                           •   │ •   └─  •   │ │ •     │ ───────── ─┐
                                ┌─┐  │ ─┐─────┐  ─────┐   •    │    │    ░   │ │       │            └───────
                                │░│ ┌┘─ │ ░░ ░└── ░  ░└─┐─    ─┘─ │ │   │░• ─┘  │ •    │  ─┐  │  •
                                └─┘ │   │         •  •  │░        │     │  •    └─   ─┐  • └──┘──  ─────────
                                     ───┘      ─── ── ──┘─────────┘───  └─     • ░───░│
                                ┌─┐ •                                                  ───┐─┐──┐─┐─────────┐
                                │░│  ──░░░░ │░ ░░ •░───░░░░░────░░░░ ░░░───░ ░░░  ──  ░░░░│ │  │░│ ░░░░ ░░░│
                                     ░░─────┘─────░• ░░─────░░ ░────────░░░────── ░░░─────┘─┘──┘─┘─────────┘
                    ┌─┐─┐───────┐────                                   ───      ────
                    │░│ │░░░░░░ │░ ░ ░░░• ░░░ ░ ░     ░░ ░ ░│ •░   ░░░░
                 ───┘ └─ •  ┌───┼─┐─┐  •                    │  •    •    ───────────────────────────────────
                •░░ ░░░░ ░░░│   │ │ │░•  ┌─ │░─┐────┐ ──── ░└── ──── ────           ░
                 ───────────┘   └─┘ │   ─┘  │  │    │  ░   •           ░  ──────────────────────────────────
                                     ─── │     └────┘ ───── ────   ──────
                                ┌─┐ •        •             •             ───┐─┐─┐─┐──┐──┐────┐────┐─────┐──┐─
                                │ │  ──   • ░░ ┌──░─┐ │░•░░░░───────░ ┌─ ░ ░│ │░│ │░░│ ░│ ░░ │░░░ │░░░░ │░░│
                                └─┘ •░░░──░─── │░░░░└─┘─░────░░░░░ ░──┘░────┘─┘─┘─┘──┘──┘────┘────┘─────┘──┘─
                                     ──   •   • ────         ───────































```

*Figure from page 14 (2346x3317 px)*
