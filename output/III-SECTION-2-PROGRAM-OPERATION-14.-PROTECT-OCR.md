# III SECTION 2 PROGRAM OPERATION 14. PROTECT OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-14.-PROTECT-OCR.PDF*

---


## 14. Protect

4203-E P-275



SECTION 2 PROGRAM OPERATION



This function protects the specified file in the memory (MD1 :) or in a floppy disk (FD0:).



When this function is activated, file operations such as editing, deleting, and renaming cannot be



conducted.



The operating procedure is as indicated below.



(1) Press function key [F1] (PROTECT).


#### PROTEC~ MS-DOS

DNC-B



Press function key [F1]



(PROTEcn.



[EXTEND]



The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.



PROTECT



PROT



PROGRAM CPERU IO N



197/07/15 14:10:00



POOTECT



POOT [I]



INJEX DISPLAY PROCEDURE



[F2] -+MD1:*.MIN



[F3]



FDO:*.MIN



TO DISPLAY OTHER Jl()EXES, AFTER PRESSING [Fl] ,



OVERIRITE



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS [WRITE] KEY.



DEFAlLT DEVICE NAME = W1:


#### DEFAULT FILE NAIi: = *.MIN

>XPROT



MD1: FOO: COMMAND OVERWR/ CHAR. /



INDEX I NDEX I NJEX HI ST<llY I NSERT DELETE



CANCEL


```text


                                                                                                •
                                                                         ┌──┐──────┐─┐──────────░░░────────┐
                                                                         │░░│░░░░░░│ │░░░░░░░░░░───░░░░░░░░│
               ────   •   •  ──────────────────────────────────────────── ──┘──────┘ └─────────
             •     ───     ──                                                                               │
            │░│ ───░░   ░── ░───────────────────────────────────────────────────────────────────────────────┘
            │░│    ──────▒░░•
            └─┘ ┌──           ────────┐─┐─────────┐────┐─┐───────┐──┐───────┐───────┐───────┐
                │░░░ ░░░░░░░ │░░░░░░ ░│ │░░░░░░░░░│   ░│ │░░░░░  │░░│     ░ │ ░░░   │░  ░░░░│
                             │   ┌─  • ─┘    ┌─┐ ┌┘ ── └─┘ ┌─┐   └┐─┘ ───── │ ───── └┐      └──────┐─┐──┐──┐─
                 ┌──────── ░ │░░░│ •  │░░ │░░│ │░│ │░░ ░░░░│ │░░│ │░ │░░░░░│ │░░░░ │ │░░  ░░░░ ░ ░ │░│ ░│ ░│
                 │    ░ ░░   └───┘    └───┘──  └─  └───────┘─┘──┘─┘──┘─────┘─┘─────┘─┘─────────────┘─┘──┘──┘─
                 │   │    ───     ────       ──  ──
                 │░░ │░┌─░░░░ ░░░░░░░░    ░ │ ░ ░░░░ ░░ ░│
                 └─ ┌┘┐┘ ────               │        ─┐──┘
                    │ │     ░   ░       ░   ░░░  ░   ░│
                  ──┘ └─┐─────────────────────────────┘
                        │
                        │ │                                                                 ┌─┐
                        │ │   ──                                                            │ │
                        │ │   ░░                                                            │ │
                        │ │ │              ─┐────────  ───┐─┐────┐─┐─────┐─┐─────┐────────  │ │
                        │ │ │   ──┐──     • │             │ │    │ │     │ │     │          │ │
                        │ │ │     │░ ┌───   │  ───┐  ┌───  ─┘   ─┼─┘     │ │     └─ ┌───────┘ │
                        │  ─┘     │  │   •  │     │  │  ░│  │    │ │     │ │     │  │░░░░░
                         ─┐        │ │       ─────┘ │    └─ └────   • • •   ─────   │  ──┐─
                          └─┐─    ─┘ │ ──         │ │ ┌─      ░░  ── │ │ ┌─┐ ░░   │  ──  │
                            │░ │ │ ░ │ ░░• ░░ ░ ░ │ │ │ │ ░░ ░ │   ░ │░│ │ │ ░┌─ ░│ ░ ▒ ░│
                            └──┘░└─  │    •       │   └─┘ ─────┘─────┘─┘─┘─┘──┘  ─┘──────┘
                               └─┘  •░─── ░│  •░ ░ ░──   •                     ──
                                 │  ░░░ ░░ └── ─────
                                    ───────
                              •             ──┐─┐───────┐──────┐─┐───┐─┐──┐─────────────┐─┐─────┐─┐──────┐──┐
                       ┌──────░────░░░░░──░ ░░│ │ ░ ░░░ │░░░░░░│ │░░░│ │░ │░░░ ░░░  ░ ░░│ │░░░ ░│ │░░░░░░│ ░│
                       │░░░░░░• ░ ░─────░░░───┘─┘───────┘──────┘─┘───┘─┘──┘─────────────┘─┘─────┘─┘──────┘──┘
                                 •      ───
                        ──░░░░•░░
                         ░───┐░──
                             │                   ───────                               ──
                                ───────┐─────────       ───────────────  ──── •          │
                            │ ─┐  ░░░░▒│░░▒░░░▒░                       ──    •   ────┐   │
                            │  │  │  • └────────               ─────── ░░ ░░░░──░░░░░│   │
                            │  │  │░│░░│            ───────────       ───────░░▒─────┘   │
                            │  │ ┌┘─┘──┘      ──────                         ───      •  │
                            │  │ │                                                     │ │
                            │ │                                                        │ │
                            │ │   ┌─────┐──── ┌─────                                   │ │
                            │ │   │░░   │░ ░ ─┘░ ░░░                                   │ │
                            │ │  │░░│   │░  •▒│     │  ───    ──                       │ │
                            │ │  │░ │ ░│░░ ░░▒│ ──░─┘┐─░ ░───░░ ░──────┐─┐─┐───┐─┐     │ │
                            │ │   ┌─┘─ │▒ ░░ ░│ ░▒  ░│ ┌── ░░───░░░ ░░░│ │░│ ░ │░│     │ │
                            │ │   │░░░  │░░░░ ░░┌─ │░│ │  • •     ─────┘─┘─┘───┘─┘     │ │
                            │ │  ─┘──── └────░──┘  └─░                                 │ │
                            │ │              •       ──                                │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │  ┌────                                                 │ │
                            │ │ ─┘    •    •      •                    ───────┐─┐───── │ │
                            │ │  │     ───┐  ────┐  ┌──────────────┐─┐        │ │      │ │
                            │ │   ──┐   ░ └┐     └┐ │ ░▒░░  ░░░░░  │░│    ┌──┐┘ └──    │ │
                            │    │░░│   │ ░│   │░░│ └─────  ─────  │░  ░  │░░└┘ │        │
                                ─┘   ── │    ──┘           •              │   │  ───── ──
                                  ░░ ░  ░░░    ░░░    ░░░    ░░ ░   ░░ ░ ░ ░░ ░ │  ░ ░│
                                ───────────────────░───────────── ────── ───────┘─── ─┘
                                                   •             •      •           •

















```

*Figure from page 1 (2346x3317 px)*


---



4203-E P-276



SECTION 2 PROGRAM OPERATION



(2} Following "PROT', enter the device name, file name to be protected, and option code.



Device name: MD1: or FD0:



The default is MD1 :.



Option code : ;C, ;V, or ;CV



The option code can be omitted.



(3) Press the WRITE key.



[Supplement] 1. When the specified file name does not exist in the storage device, the message "no



file" will be displayed on the command line.


## 2. Symbols "?" and "*" can be used to specify a file name.

Functions of these symbols are the same as explained in 3. "DIRECTORY".



Option codes for file protection:



The code ";C" specified following the file name cancels file protection.



The code ";V" specified following the file name displays the following message on the command line of the



display screen to allow the operator to select whether or not the specified file is protected.



FILE PROTECT OK (Y/N}?



When file protection is desired, type "Y" and press the WRITE key.



When file protection is not desired, type "N" and press the WRITE key.



The code ";CV" specified following the file name displays the following message on the command line of



the display screen allow the operator to select whether or not protection of the specified file is canceled.



FILE PROTECT CANCEL (Y/N)?



When file protection needs to be canceled, type "Y" and press the WRITE key.



When file protection does not need to be canceled, type "N" and press the WRITE key.



Example 1: PROT



ABC.MIN or PROT



MD1 :ABC.MIN



This instruction protects the file ABC.MIN registered in the memory.



Example 2: PROT



BCD.MIN;C or PROT



MD1 :BCD.MlN;C



This instruction cancels protection of the file BCD.MIN registered in the memory.



Example 3: PROT



CDE.MIN;V or PROT



MD1 :CDE.MIN;V



When the WRITE key is pressed following the above instruction, the prompt as



indicated below will be displayed on the command line.



CED.MIN FILE PROTECT OK (Y/N)?



Type "Y'' and press the WRITE key to protect the file.



Type "N" and press the WRITE key not to protect the file.



Example 4: PROT



DEF.MIN;CV or PROT



L...I



MD1 :DEF.MIN;CV



When the WRITE key is pressed fotlowing the above instruction, the prompt as



indicated below will be displayed on the command line.



DEF.MIN FILE PROTECT CANCEL (Y/N)?



Type "Y" and press the WRITE key to cancel protection of the specified file.



Type "N" and press the WRITE key not to cancel protection of the specified file.


```text


                                                                                               ──
                                                                         ┌─┐─────┐───┐─────────░░────────░░│
                                                                         │░│░░░░░│ ░ │░░░░░░░░░ •░░░ ░░░░──┘
          ┌───────           ──       •   ──  ──  ────────── ────────────┘─┘─────┘   └─────────      •
          │       •    ──────  ─────── ┌──  ──  ─┐          │                     • •                      │
          └──────┐ ┌──░         ░░     │         │  │ │   │ │                    │      •       • ─────────┘
                 └─┘  ┌──    ┌─   ┌─  ─┘      ──    └─┘   │ └─    │░── │    │    │ │    ░░       │
                      │░░░░░ │░░░┌┘  │░░   • ░░░░ ┌─┘  ───┘─  ────┘─  ─┘────┘────┘─┘─────────────┘
                      │    ──┘   │   └─────░┌──── │░
                      └───┐   ┌─┐    │      │     └──
                      │░░░│   │░│    │░┌─░ ─┘  ░░    ─┐──┐─┐─────┐
                      └──  •  │      └┐┘ •░░░░ •░░░│ ░│ ░│ │░░░░░│
                 ┌─┐  │  ─┐ ┌─ ┌───── │   ───── ───┘──┘──┘─┘─────┘
                 │░│  │░░░│ │░ │░░░ ░ │░•
                ┌┘ └──┘    ─┼──┼─┐──     ──────────────────────────────────┐─┐────────┐────┐─┐─────────────┐
                │░│░░░░░░░░░│  │ │  │░░░  ░░ ░░░ ░░░░░   ░░░░ ░░░░ ░░ ░░░ ░│▒│ ░░░ ░░ │░░░░│ │░   ░░░░ ░   │
                └─┘─────────┘  │ │  └────── ┌──     ─┐  ──┐─┐────      • ──┘─┘ ───────┘────┘─┘─────────────┘
                               └─┘ •        │        │    │ │      •          │
                               │░│  •░ ░░ ░│   • ─┐ •   ░   │     ░ │    ░   ░│     •
                               └─┘ │       └───   └┐  ──    └──     └─     ── └──    ────┐────┐───────┐
                                   │░ ░░░░░ ░ ░ ░░░│ │░░░░░░ ░ ░ ░░ ░░░░ ░░ ░░░░░ ░░ ░ ░ │░░░░│░░ ░░░░│
                ┌──────────────┐───┘      ─┐───────┘─┘───────────────────────────────────┘────┘───────┘
                │░░░░░ ░░░░░ ░ │░░ ░ ░░░░░ │
                └────   ┌──┐─ •      •      ────────────────────────────────┐
                │ ░   ░░│  │ │░░┌──── • ────░  ░  ░  ░░░░ ░░  ░░ ░░ ░ ░░░░░░│
                │       │    │  │                         •                   ────  ──        ───────┐─────┐
                └────   └────┘  └─────  ┌──────    ┌── ─── ░ ─┐ ░    ░ ░░ ───░░░░░░ ░░──────── ░░░  ░│ ░  ░│
                │░░░░│ ░░░░░  ░ │░ ░ ░──┘░░░░░░ ── │░░░ ░░ •░░└────░░ ░───░░░────── ── ░░░░░░░───────┘─────┘
                └────┘─         │  ┌──        ┌─  ─┘─────── ──     ────   ───         • ──────
                          ░   ░│   │  •░    ░ │
                │  ─┐          └┐─   •        └─    ─────────────────────┐
                │   │  │ ░ │ ──┘┘ ──    ┌── ░░      ░     ░░  ░    ░     └─
                └───┘ ░└─┐─┘─   │    ┌┐ │   ─┐─ ──  ──                   │ ──┐
                │      │ │      │ ┌──┘┘ │ ── │ •░ •                          └───     • • •    ───   ──
                │░░   ─┘   ░•    ┌┘░ ░  ░ ░  │    ░•          ░        ░     │   ─────   • │ ──   ───
               •  •     • •  │ ░ │   •      •░│     •        ░   •          ░│  •   ░ ───  └─        ──────
                ──  • ░ ░• │ │   ░  ░ ┌──  • ░│     ░░░• ░  ░ ░┌─  │      ░░░░░ ░•░░ ░░░░ ░░░  │ ░ │░░░░░░░
                      │░•  └─┘ ─────┐┐┘ ░ • ──┘     ───  ──────┘ • └───────────   ─────────────┘───┘───────
                ┌───┐─┘             └┘                  •       │ │            ──
                │░░░│ ░│ ┌─ ░ ░░░  ░  ░             │ │  │ │  │ │ │         ░       │
               │    │  │ │                          └─┘  └─┘──┘ │                 ──┘────┐──
               │░░░░│ ░│ │░░░░░░░ ░░░░ ░ ░ ░░░ ───── ░░ ░░    │░│ •░       ░░░ ░  ░░░  ░ │░
               └─┐─ └─    ───┐     ──                 ┌──     │ │   • ┌──────────────────┘──
                 │ ░░░░░░    │ ░  •  ─┐░│ ░░░░ ────░│ │  │░░░•░░░──░░░│
                 │ ────      │ •      └─┘ ────     ─┘    └──  ░──  ──    ──       │   │  ─┐
                 └─    ─┐──┐ └─      │               ──               ───  ─── ───┘───┘─  │
                 │ ░░ ░░│ ░│ │░░     │░░░ ░░░░░ •░ ░░░░ •  ░░░░ ░░░░ ░░░ ░•
                 │     ─┘  │ │ ──░   └── ──────  ─── ──      ┌──────┐─ ──    ░   ────────    ─────────┐
                 └─────  ──┘ └─         •           •      ┌─┘      │ •   ┌────── ░                   │
                 │ ░░░░░│ ░│ │░░░─┐ ───░░ •░░░• ┌─ │░•░•   │░└───░░░│░░│  │                           │
                 └──────┘──┘ └──░░└─    •░ ─┐─░ │  └┐   ┌──┘┐┘    •  ┌─┘ ─┘──────────────┐───────────┐
                                ░ ░  ░ │ │░ │ ░ │░│ │░░ │ ░ │ ░ ░░ │░│ │ ░ ░░░           │           │
                             ┌─┐      ─┘ │  └───  │   ░ │░ ─┘ ┌────┘─┘─┘───────────────── ───────────┘
                             │░│░ ░░░ ░│ ░ ░░░░ ░░░• │░│ ░░░└─┘
                             └─┘─   ───┘┐ │ │   ──   └─┼─  •  └─   ───
                                 ──┐    └─┘─┘───  ───┘ │  │ ┌─┘ ───  ░────── ┌───┐
                 ┌─          ────░░│ │░•░░░ ░░░░  ░░ │░░ ░│ │░│ ░░ ░•░  ░░░ ░│ ░░│
                 │  ───────┐      ─┘ │  •      │  ───┘───   │      │ │       └───
                 └─        │ ──┐    ─┼─┐ ──────┘ •       ───┘ ── ──┘─┘───────    ─┐─┐──┐─┐───────────┐
                   ────────    │░░•░ │░└─░░░  ▒ •░│ ┌──░░░░░ ░ ░ ░░░░ ░░ ░░░░──░░░│ │░ │ │ ░ ░  ░ ░ ░│
                              │ ──░░░░─┘░───────░─┘ │░░─────────────░░ ░ ─── ░ ───┘─┘──┘─┘───────────┘
                             ┌┘                     │               ─────   ───
                             │░ ── ░    ░──     ░• • ┌──── ┌── ░░               ────────┐────────┐
                              ─┐░░─┐──┐─┐ ░ ─────░   │░░░░░│ ░──── ░  ░                ░│  ░   ░ │
                               │   │  │ │            │    • •        ───      ─────             ─┘──┐─
                                │░░│ │  │░░ ░░░░ ░ ░ ░░     ░░  ░░   ░░░░░ ░░░░░░░░░ ░ ░│ ░░░░░░░░ ░│
                                └──┘─┘──┘───────────────────────────────────────────────┘───────────┘─















```

*Figure from page 2 (2346x3317 px)*
