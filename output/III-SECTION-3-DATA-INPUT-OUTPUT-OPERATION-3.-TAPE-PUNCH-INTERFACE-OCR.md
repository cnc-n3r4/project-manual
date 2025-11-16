# III SECTION 3 DATA INPUT OUTPUT OPERATION 3. TAPE PUNCH INTERFACE OCR

*Converted from PDF: III-SECTION-3-DATA-INPUT-OUTPUT-OPERATION-3.-TAPE-PUNCH-INTERFACE-OCR.PDF*

---



4203-E P-327



SECTION 3 DATA INPUT/OUTPUT OPERATION


## 3. Tape Punch Interface

(1) An RS232C serial interface is provided to allow connection of a tape punch.



Connecting a peripheral device such as a tape reader or tape punch that also has an RS232C serial



interface to this RS232C interface enables bulk transfer of NC part program data.



When the RS232C interface is used for connecting a tape punch, it is necessary to set the



parameters so that communication is possible between the NC and the external device (tape



punch}.



(2) There are two methods for data transfer using RS232C - the normal BTR (behind tape reader)



method and a method using DC code control - and the method for connection to the peripheral



device differs according to which of these is used.



3-1 . Operation Commands



{1) The table given below indicates which command can be used with which input/output devices.



~ Tape Reading Tape Punching Printing De-



Sector Device



Device Device vice



F2 DIR Input Output



F1 READ Output Input



F2 PUNCH Input Output



F3 PIP



Output



F3 VERIFY Input



Input



F5 FREE Input Output



F6 LIST Input Output



[Supplement] For the operation of the commands, refer to Section 5 "PROGRAM OPERATION".



(2) Peripheral Device Classification and Abbreviations



Sector devices



MD1: _,. User memory



FOO: _,. 3.5-inch floppy disk



FD1: _.., 3.5-inch floppy disk



Tape reading devices



TR:



_,.



Tape reader



CN0:



_,.



Tape reader connected at RS232C channel 0



CN1:



Tape reader connected at RS232C channel 1



CN2: -+ Tape reader connected at RS232C channel 2



CN3:



_,.



Tape reader connected at RS232C channel 3



Tape punching devices



CN0: _,. Tape punch connected at RS232C channel



CN1: ..... Tape punch connected at RS232C channel 1



CN2: - Tape punch connected at RS232C channel 2



CN3: - Tape punch connected at RS232C channel 3


```text


                                                                                                ──
                                                                ┌───────┐───┐─────┐─────┐───────░░░───────░──
                                                                │░░░░░░░│ ░ │░░░░ │░░░░ │░  ░░░░───░░░░░ ░•░
              ─────                •           ─────────────────┘───────┘── └─────┘─────┘───────     ───
           ┌─┐     ┌──────────────┐ ┌─────── •                                                              │
           │░└─────┘░░ ░   ░░    ░│ │░░   ░ •░  ────────────────────────────────────────────────────────────┘
           └─┘     └──░───────────┘─┘──░────░───
                  ─┘  │                         ────────────┐──── ─────────┐──  •     ──
                    │ │░  ░░────┐ ┌──    ░ ░                │░             │  ── ─────  •
                  ──┘ │         │ │  •                  │  ┌┘                            •   ────────────────
                       │░ ░░░░░░└─ ░░░───── ░░ ░    ░  ┌┘┐─┘░   ░░ ░    ┌─────  ──  • • │  ──   ░
                       │  ──────   ──┐░    ┌──         │ │ └─   ─┐      │░  ░  │  ── •  │ │  ─┐──────────────
                       │             │ │   │      ░     ░  │ •░• └┐   ──┘─ ─┐─┐┘     ░ ░│ └─░░│
                      │░░       ──    ░│ │ │          ─────       │         │ │    │ ───       ───    ───
                      │    ─────       │ │      ─────      ─────   ──────  ░└─░    │    ─── •     ────   ───┐
                       │░ ░ ░░░ ░ ─┐──░│ │░░░  ░░░░░      ░ ░░░░░ │░░░░░ ── │ ────░    ░  ░░░░ ░─┐░░░░░─┐░░░│
                       └────── •   │  ─┘ └──  •  ────     ──────  └──────  • •    ──   ───────── └───── └───
                  ┌─┐ •       • ──┐ ┌─  •   ─┐ ┌─    ────┐      ──              •   ───                •
                  │░│  │░──░ •░ ░░│ │░░░  ░ ░│ │░░•  ░░░░│ •░   ░░░░░░│  ┌───     ░ ░░░ •   ░       •     │
                  └─┘  └─  ──    ─┘                 •           ──    │  │                │               │
                       │     ┌───  ──    ───      •    ───     •   ┌──┘    •  ─── •   ░   │ •     │░ ░ ░░ │
                       └─────┘░░░░•░░────░░░ ░ │░░░ •░ ░░░│ ░ ░░░░─┘   ──── ──     ───────┘─ ─────┘───────┘
           ┌───┐   ────                    ────┘──── ─────┘───────
           │░  │     ░░  ░░ ░     ░ ░ ░ ░░
           └───┘    ──┐──────  ──────┐─────
                      │      ─┐      │      ─────┐─────────────────────┐─┐──┐─┐─┐─┐─────┐───────────────┐
                      │  ───  │ ░ ░   ░───── ░ ░░│ ░░      ░░ ░░░  ░░ ░│ │░░│ │░│ │░░░  │░░░ ░░░ ░ ░░░ ░└──
                         ░░      ─────┐░░░ ░    ─┘────── ──────             │ └─┘  •       ─┐ ┌─    ─── │    │
                     │░│  ──    •     └─┐░░ │ │                  ░  ─┐─     │       ░    │  │ │            │░│
                     │░│ •     •        └───┘░│   │░░░░ ░░ ░░│  ┌──┐░│ ░░ ──┘   ─┐    ░  └─ │ │ ─── ░• ──  │░│
                     │░└─░░───░░             •   ┌┘──     ───┘ ─┘  └─   ──   ┌─┐ └─┐    ─┘  │ │     •░│    │░│
                     │░    ░ ░ •               │░│    ───     │░│            │░│   └────    │ │  ┌─   └─┐  │░│
                     │░│░• •░░  ─┐  ┌───┐ ─────┼─┘   │░░░─┐   │ │    •       │ │            │ │ ─┘░░│░ ░│  │░│
                     │░└─ • ───┐░│  │░░░└┐     │ └── │░░░░│   └─┼──  ░░░░  ──┼─┼────     ───┼─┼─  ──┘─── ──┘░│
                     │░│       │░│  │    └┐    │░│  •     └───┘░│   ───────  │░│    ────┐   │░│  •      •  │░│
                     │░│       └─┘  └───┐░│    │ │   │░   │   │ │            │ │  │░ ░░░│   │░│            │ │
                     │░└────── │  │ │   │  │   │░│   └─── ░│  │░│    ────    │░│  └─────┘   │░│            │░│
                     │░│       │░░└─┘░░░░ ─┘ ──┘ │  │     ─┘──┼─┼──  ░░ ░ ───┘ └──       ───┼─┼─         ──┘░│
                     │░└─┐─┐───  •  └─────     └─┼──┼────     │ │    ────    └─┘  ────      │ │ ─┐───      │░│
                     │░░░│ │░░░│   •       ────┘░│  │░░░ ░┌───┘░│        ────┘░│      ──────┘░│  │░ ░──────┘░│
                     │░  │    ░└─   ──────     └─┼──┘    ┌┘   └─┼───────     └─┘ ─────      └─┼─ │  │░░    │░│
                      ───┘ • ░┌┘               │ │   •░░ │    │ │            │ │            │ │  │░─┘──┐   │ │
                 ┌──┐─    •  ─┘   ─────────────  └─┐─     ────┘─  ───────────  └────────────┘ └──┘     └┐   ┌┘
                 │░ │░░───░──   ┌─░  ░░ ░░░ ░░░──░ │░──── ░ ░ ░░•░░░    ░░ ░░  ░   ░░ ░░ ░░░  ░░ ░ ░░ ░░│ ──┘
                 │  └─┐      ───┘                                  ─────────────────────────────────────┘
                  │░│ │ ░     ░  ░ ░    ░   ░          ░░░
                  └─┘ └────         ┌───────────────────────────────
                      │░░░░• •░ ░░░┌┘
                      └───    ─────┘   ──┐  ─────┐
                          │░░•     │  │░░└──░░░░ └──┐─
                          └─  │  ┌─┘  └──    ──     │ │
                          │   │  │ │ │         •      │
                         • ░░ │  │ │ │░    ░░ ░░░ ░ ░░│
                       ┌─      ── │ • •  ┌────────────┘
                       │░  •     ░│    ──┘
                       └── ░░│ ──┐┘┐─┐░  │     │
                             │   │ │ │   │     │  ─────── ─── ─────┐──────────
                           ──┘   │ │  │░░│ │░░░│ │░░░░░░░• ░ │░░░░░│  ░░░░░░ ░•
                            ░└─  └─┘  └──┘─┘───┼─┼───░ ░     │░ •░   ─────────
                                 │ │  │        │ │                 •          │
                            ░┌┐  └─┘  │░░░ │░░░│ │░  ░░░░░ ░ │░░░░░░  ░░░░ ░ ░│
                           ──┘┘    │  └────┘──░└─┘ ───────── └─── ── ── ── • ┌┘
                      ┌────   └────┘┐─        ─┘ └─         •    •     •  • ─┘
                      │░░░ ░•░ ░░ ░ │░ ░░░│                                   •
                      └───┐ ░┌─────┐┘─── ┌┘  ┌─┐─        │ ──┐───  │
                          │  │     │    ─┘ ──┘ │ ┌──┐────┼─  │   ──┼─┐──┐───┐
                          │░░│   │ │ •░░░│ ░  ░│ │░░│░░░░│ ░ ░░░░░░│ │ ░│ ░░│
                          └──    │ │  │       ─┘ │  │       ───  ──┘ │      │
                          │  ┌┐  │ │  └─────── │ └──┘    ───   •   └─┘  •    │
                          │░░└┘  │ │  │░░░ ░░░░░ ░░░ ░░░░░ ░ ░░░░░░│ ░ ░░ ░  │
                           ──┘   └─┘  └────────────────────────────┘─────────











```

*Figure from page 1 (2346x3317 px)*


---



4203-E P-328



SECTION 3 DATA INPUT/OUTPUT OPERATION



Printing devices



CN: -+ Console



PN: -,. NC operation panel



CNO: -+ Printer connected at RS232C channel 0


#### CN1: -+ Printer connected at RS232C channel 1

CN2: -+ Printer connected at RS232C channel 2



CN3: -+ Printer connected at RS232C channel 3



(3) If no device name is specified, the following selections are made automatically.


#### For sector devices MD1:

For tape reading devices TR: (This selection can be changed by setting NC



optional parameter {word) No. 57.)



For tape punching devices CNO: (This selection can be changed by setting NC



optional parameter (word) No. 45.}


#### For printing devices PN:

The default device for a tape reading device or tape punching device can be changed by changing



the parameter settings.



(4) If no output NC program name is specified, the same name as the input NC program name is



automatically assigned.



(5) If no input NC program name is specified, the name "A.MIN" wm be automatically assigned



unless a program name is designated on the tape, in which case that name will be used.


```text


                                                                                               ──        •
                                                               ┌─────┐─┐───┐───┐─┐─────┐────── ░░•░────── ░│
                                                               │░░░░░│░│ ░ │░░░│ │░░░  │░ ░░░░░──░•░░░░ ░──┘
          ┌──────────       •       ───────────────────────────┘─────┘─┘───┘───┘─┘─────┘───────     ──
          │           ────── ───────                                                                       │
          └───────────░ ░░    ░     •        ──────────────────────────────────────────────────────────────┘
                      ──── ──┐───┐ │  ──────┐
                          │░░│   └─┘ │░ ░░░░└─
                          └─     │   │        ──    ──
                          │ ──┐  │   └────░░ •░ ──── ░────────┐─┐───────┐
                          │░░░│  │   │░░░░░•░░• ░░░░│ ░ ░░░░░░│ │░░  ░░ │
                          │  ┌┘  │   │    │ │       │   │     │ │  │   ─┘
                          └──┘┘  │   └─  ░│ │░──────┘ ──┘─────┘ └─░└─░│ │
                          │░░░│  │   │░┌──┼─┼─░░░ ░░└─░ ░░░░░░│ │░─┘ ─┘
                          └─ ─┘  │   │ │  │ │       │   │     │ │     │
                          │  ░│  │   │ ░ ░│ └─░░░░░░░ ░ └─────┘ │░░░ ░│
                 ┌─┐ ┌────    └─ └───     │ │  ┌──             ─┘      ─┐─┐──┐──────┐─────┐─
                 │░│ │    ──┐─ ░─┘░ ░•   ░░░ ░░│   ░  ░░── ░ │░░░░░░ ░ ░│ │░░│  ░░░ │░░░░░│
                 └─┘ │░     │ •   ──     ── ───┘───────┐░  ──┘──── •       ──┘  ──  └─────
                     │    ┌─┘  •      ───  •           │  │          ── ──    ──          ─┐ ──┐─┐───┐──┐──┐
                     │░   │░└─░░░─── ░░░░░░░•          └──┘   ┌──────░░•░░────░░───────░░░░└┐ ░│ │░░░│░ │░░│
                     │      │   •     •                │      │░░░░ ░ ░░ ░░░░░• ░░░ ░ ░░───┘┘ ┌┼─┘ ──┘ ─┘  │
                     │░   ──┘─── • ─── ───────         │ ─┐   └──                           │ └┘ └─   • └──┘
                     └┐ ──        •  ░                 └─ │   │   ───░    ────  ────   ░ ░░░│ │░ │░░  ░  ░
                      │      │ │ │      ─────         ┌┘  │   │░░░  ░──░ ░░░░░ •░░  ░───────┘ └──┘─────────
                     ┌┘   ░──┘─┘─┘░░░░──              │░░•    │        ─────     •
                     │    │               ─┐──┐─┐─────┘   ─┐── ┌─┐────      ┌──── ┌─┐──┐─┐───┐─┐───────────┐
                      • ──┘░ ░  •░───────  │░░│ │░ ░░░ ░░  │ ░ │░│░░░░ ░░ ░ │░ ░░ │░│ ░│ │░░ │░│  ░ ░░░░░ ░│
                     │░░ ░░──┐─░░• ░░░░░░░─┘─   └──        │   └─  ───    • │   • │   ─┘─ •  └─ •     ─────┘
                 ┌─┐ │       │               ───   ───────┐ ┌─┐  ──   ───┐ │ ──┐ │ ─┐─   • ┌─  │ ┌───┐
                 │░│ └┐────┐─░── ░ ────░ ░  •░░░│   ░░░░░░│ │░│ │░░░ •░░░│ │░ ░│ │░░│ ░  ░░│░ ░│ │░░░│ ░│
                   │  │░░░ │░•░░───░░░░────  ───┘    •  ──┘  ─┘ └───       │  ─┘ └──┘      └───┘ └───┘──┘
                 ┌─┘ │                     ──    ─┐── ──   ┌─  │    ─────── ──  │    ──────     •
                 │░│ └┐────░░░ •░─── ░░─── ░░ ░ ░ │░░░░░░──┘░░ │░ ░  ░ ░░░  ░░ ░│ ░ ░░░░░░░░• •░░░░░ │
                 └─┘  │    ────     ┌─┐     ─┐     •  ┌──        ──  │ ───             ┌── •       ┌─┘
                      └────     ────┘ │ • •  └───░• ──┘   ─── • │    └─    •  │ ─────  │  • ── •  ─┘
                                                 •             ─┘         • ──┘      ── •     • ──













































```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-329



SECTION 3 DATA INPUT/OUTPUT OPERATION



3-2. Parameter Settings



Set the following parameters before connecting a peripheral device.



After setting the parameters, press function key (F7J (BACKUP) and on completion of the backup



operation switch the power off and then back on again.



The old parameter settings will remain valid if the power is not switched off and back on.



(1} NC optional parameter (bit) No.1



I\ Bit No.



Paramete \



r No,



bit 7 bit 6 bit 5 bit 4 bit3 bit 2 bit 1 bttO



Special Special Tape Tape Tape Tape TV Automatic Tape



tape tape rewind read delimiter check tape code coding



codes code verify code: recognition system



ignored alarm % (ER)



(a) bit 0 Tape coding system



= 1 Tape code set to ISO code (lnitla! value;;;:: 1)



= 0 Tape code set to EIA code



(b) bit 1 Automatic tape code recognition



= 1 Tape code automatically recognized (Initial value= 1)



;;;:: O Tape code not automatically recognized



The codes used for tape punching and tape verification depend on the combination of the settings



made for bit O and bit 1.



bit 1 bit 0 Contents



1 1 In "READ" and "VERIFY" operations, EIA and ISO tape codes are auto-



matically recognized.



In "PUNCH" operations, program data is punched in the ISO code.



1 0 In "VERIFY" operations, EIA and ISO codes are automatically recog-



nized.



In "PUNCH" operations, program data is punched in the EIA code.



1 In "VERIFY" operations, the control assumes that the coding system is



ISO.



(If the tape code is not ISO, an error occurs.)



In "PUNCH" operations, program data is punched in the ISO code.



0 0 In "VERIFY" operations, the control assumes that the coding system is



EIA.



(If the tape code is not EIA, an error occurs.)



In "PUNCH" operations, program data is punched in the EIA code.


```text


                                                                                                ──       ──
                                                                ┌─┐───┐─┐───┐─────┐───┐─┐───────░░•░─────░░│
                                                                │░│░░ │░│ ░ │░░░░ │░░░│ │░ ░░░ ░──░•░░░░░░─┘─
               ───                      ────────────────────────┘─┘───┘─┘── └─────┘───┘─┘──────      ───
           ┌───    ───────┐──┐─┐─┐─┐──┐
           │░ ░┌─ │░      │░ │ │ │░│  │ ┌──────────────
           └───┘  │ ── │  └──  └─┘─┘ ░ ─┘
                 │ ░  ─┘ │   ┌─          ┌──────┐───────────────────────────┐
                 │ •   └─┘─  │           │      │         ░                 │  •                ───
                 │░░│ │  ░ │ │         ░  •     │    │   ─┐    • ┌─┐ ░    ░•  •  ─┐ ─┐──────── │   ─┐─┐─────┐
                 │  └─┘ ┌─ └─           │  ───  └──  └─── │  ──  │ └───────    ── │  │         └─── │ │    ░│
                 │░░    │ •░ ░    ░ ░░░░│ ░   ░ ░ ░░ │░░  ░ ░░░░░│                                 • • ─────┘
                 └┐───          │ │  ┌─ │ │  ──   ┌─ └┐─   ────  └────────────────────────┐───┐
                 └┘       •  ───┘ └──┘ •  └─┐   ─┐┘   │  ─┐  ░  ░│        ░   ░░    ░   ░░│   │
                 │    │    ──    ─┘         │    │  ┌─┘── └──────┘────────────────────────┘───┘
                      │░│ │░░░░ ░ ░░░░ ░░░  │░│ ░│  │
           │   ┌────┐   └─┘────┐─ ────────   ─┘──┘   ─┐────────┐─┐────────┐─┐───────┐───────────┐─┐────────┐
          ┌┘─  │░ ░░│  │       │░│        │░│       │░│        │░│        │░│       │░          │░│        │░│
          │░ ──    │   │ │   │ │░│  •   ──┼─┘     ──┘ └──    ┌─┼─┼─┐    ──┘ │  •  ┌─┼─┐───  ────┘░└──┐   ┌─┘░│
          │░ ░░░│ ┌┘ ░│  └───┘ │░│        │ │  ───  │ │      │ │ │ └────  │ │ •░• │ │ │   •░    │░│  │░  │ │░│
          │   ──┘─┘ • └─      ─┼─┘─     ──┘─┘      ─┼─┘─     └─┼─┘      ──┘ │     │ │ │        ─┼─┼─     └─┘░│
          │░│        │░░─┐───  │░░░────░   ░│ ┌──   │░   ────  │░ ░──┐    │░└── ──┘ │░ ─────┐─┐ │░│ ───┐   │░│
          │ │        │ ░░│  ░ ─┘░•░░░░ ──┐──  │░░   └─┐── ░░░│ └─ │░░└┐─┐ │  ░░░  │ └┐ ░░░░░│░│ │░│  ░░└┐  │░│
          │░│        │ •░░• │  │░ │░░ │  │    └───    │  │░░░│ │  │░░░│░│   ░─────   │ ░░│   ░│ │░│ │░░░└┐ │ │
          │░│        │  ░░░─┘  │░ │░░░│  │        •   │  └───  │  └─░░│ │ │ •        │ ──┘────┘ ░░│ └───░│ │ │
          │░└────────  ░░░ ░░│ │░ │░░░└──┘─ │       ┌─┼──    • └─ │ │░░░│ │      ────┘          │░│          │
          └─┘        ┌┐ ──┐──┘  •░└─░░░░░░  └──   ──┘ │░░      ░  └─┘───             │░    ░░░░░└─░░░░░░    ┌┘
             ────────┘┘   │   ┌─ •  ─┐  ┌─┐          ─┘───────────       ────────────┘──────────  ──────────┘
                      └───┘───┘      └─ │ └─┐    ────
                                    │  •    │        ┌──────┐──────┐───────────┐────┐
                                    │ │  │  │ ░   │  │ ░    │      │     ░   ░ │    │
                                    │ └┐ │  │   ──┼──┘  │     │ ┌─ │  ─────────┘────
                                    │  │ │   ░░ ░ │░░│ ░│ ░   │ │░░│
                      ┌─┐─┐──┐      └──┘─┘──┐ │ ─┐ │   • ──┐──┘─ ┌─┘
                      │░│ │░ │      │░░░░░ ░│ │░░│ │░░• │░░│░░░  │
                      └─┘─┘──┘       ──┐─┐──┼─┘ ─┘─┼─  ─┘  │    ─┼─┐────────┐─┐─────┐───┐───┐
                                    │  │ │  │░░░░ ░│░│ ░░░ │░░░░░│ │░░░░░░░░│ │ ░░░ │░░░│   │
                                    │  │ │  │      │ │ ┌─  │     └┐┘ ─┐     └─ ┌────┘───┘───┘
                                    │  │ │  │░░░░ ░░░│ │░ • ░░░░░░│░│ │░░░░ ░░░│
                             ──── ──┘     ──┘──      └─ •    ─┐   │ └─ ─┐──┐   └───────┐─┐─┐──┐────────────┐
                        │░───░░░░ ░░░░░──░░░   ░░░ ░░ ░ ░ ░░░ │░░░ ░░ ░ │░░│ ░ ░░  ░ ░ │░│ │░░│ ░ ░ ░ ░░░░░│
                        └─░░ ──────────  ░────────────────────┘─────────┘──┘   ────────┘─┘─┘──┘────────────┘
                        │                                                    •
                     │░│ ░░░░  ┌─┐ ░░░░  ┌──                          ┌─░░───░─┐                           │ │
                     │░│ ─┐─┐──┘░└──  ┌──┘    ──      •    ───     ───┘    ░░░░│ ──────        ────── ───  │░│
                     │░│  │ │  │ │  ──┘  │ ░• ░░░░░░ ░░░• ░░░░░ │ •░░ ░░░ ─────┘░░░ ░░░ ░░░░ ░░░░░ ░░ ░░░│ │░│
                     │░│       │ │        ── ░░───── ── ░░──────┘  •   ──         • ───────── ────    ───┘ │ │
                     │░│       │ │       │                          ───   ───   ── •         │    ───      │ │
                     │░└──┐─┐──┼─┼──┐─┐──┘┐─┐─┐──────────────░ ────░░░░───░░░ ░ ░░ ░░░• • ░• │░░ ░░░░─┐ ───┘░│
                     │░│  │ │  │░│  │░│   │░│ │░░░░░░░           ░     ░ ░ │                          └┐   │░│
                     │░└──┘─┘──┼─┼──┘─┘───┘     ───────────────────────────┘ ───────────────░─── ─── •░│   │░│
                     │░│       │ │        │ ░░░░                                                      ─┘   │░│
                     │░└──   ──┼─┼──── ──    •   ─────────────────────── ────────────────────────────      │░│
                     │░│  ┌─┐  │░│    │   │      ░░░   ░ ░ ░   ░ ░░░░░░ •░░░░ ░░░░░░ ░░    ░ ░ ░ ░░░░────┐ │░│
                     └─┼─ │░└──┼─┼────┘── │░──░░───────────────────────░░────────────── ░┌──░░░──────░░ ░└─┘░│
                     │ │  └─┘  │ │        │░░  │                       │               ──┘  ───      ────┘ │ │
                     │ │       │ │        │ ──░│ ┌─┐ ──        ───┐  │ │                                   │ │
                     │ │       │ │        │    └┐┘ └┐  • ─┐─┐     └─ └─  ┌──      ────┐───┐──┐───          │ │
                     └─┼── ────┼─┼────────┘░  │ │░ ░│  ░░░│░│░   •░░░ ░• │░░       ░  │   │░ │░  ────┐    ─┘ │
                     │░│  │    │░│        │ │ │░    │       │                                │       └───┐ │ │
                     │░└─ └────┼─┼────────┼─┘  ─────┘───────┘──────────░─┐────────░ ░░░ ░░   ░░░░░░░░░░ ░│ │ │
                     │░│       │ │        │░│░                           │        ─┐─────────────────────┘ │ │
                     │░│       │ │        └─┘─░░ ░░░ ░  ░ ░ ░ ░ ░░• ░  ░ ░ •░░ ░   │                       │ │
                     │░│       │ │       │                         •      •       ─┘─────────────────      │ │
                     │░└───────┘ └───────┘ ░  ░ ░░░░░• ░░░ ░░░░  ░░░░░░░ ░░░   ░ ░ ░ ░░ ░  ░ ░░░ ░░░░ ───── │
                     └─                   ───────────  ──────────────────────────────────────────────       │
                        ──────────────────           •                                                ──────















```

*Figure from page 3 (2346x3317 px)*


---



4203-E P-330



SECTION 3 DATA INPUT/OUTPUT OPERATION



(c) bit 2 Tape TV check



The tape TV check is a check on the number of characters of tape data in each block of the



program.



It is checked that the number of codes from the code following one LF (EOB) to the next LF (EOB)



is an even number.



bit2 Contents



0 In "READ" operations, no TV check is performed.



In "PUNCH" operations, the number of characters per block is not adjusted.



1 In "READ" operations, it is checked if the number of characters in each



block is an even number; if it is an odd number, an alarm occurs.



In "PUNCH" operations, a space is added if necessary to make the number



of characters in one block an even number.



(Initial value = 0)



(d) bit 3 Tape delimiter code %/ER



Sets whether or not the %/ER code is used instead of tape feed to mark the end of program



information on the tape.



bit3



[Supplement}



(e) bit 4



Contents



Tape feed is taken to indicate the end of program data.



The % (ER) code is taken to indicate the end of program data.



(Initial value "' 0)



The data up until the second appearance of an CR, and LF or EOB on the tape is



ignored.



Tape reading verification



Sets whether or not the program information is automatically verified when a tape is read.



bit4



[Supplement]



(f) bit 5



Contents



Verification is not performed on completion of a "READ" operation.



Verification is performed on completion of a "READ" operation.



(Initial value = O)



File names are not verified.



Tape rewind



Sets whether or not the tape is rewound after reading (if verification is not performed).



bit5 Contents



0 Operation stops after the tape has been read.



1 The tape is rewound after it has been read.



(Initial value= O}



(g) bit 6 Special code alarm



Sets whether or not special codes ($20 to $5F, HT) trigger an alarm.


```text


                                                                                               ───
                                                               ┌─┐─────┐───┐───┐─┐─────┐────── ░░░─────────┐
                                                               │░│░░░░░│ ░ │░░░│ │░░░░ │░ ░░░  ───░░░░░░░░░│
          ┌───────────  ──  ────────       ──    ──────────────┘─┘─────┘── └───┘─┘─────┘───────     ───
          │           ──  ──        ───────  ────                                                          │
          └───────────        ┌─   │              │                          •             •    •    •     │
                      │ ──    │ ┌──┘   │         ─┼────────────────────────── ─────   ─────  ───  ───  ────
                      │  ░    │ │  │░  │         ░│                                │ │      │    │
                      │       │ └──┘───┘──────────┘──────────────────────────────┐─┘─┘──────┘────┘─── ─────┐
                      └─  ░                                                      │                         │
                      │    •   ─── ┌────────  ─┐─ ──────  ──  ───────────────────┘─ ┌──────────────────────┘
                      │  ─┐ ┌──   ─┘        ── │ •      ──                         ─┘   ░             ░
                      └┐ ░│ │ ░• •░░░░░│                                                                   │
                       └─┐┘─┘┐  • ──┐─┐┘                            ─────┐──┐                              └┐
                         │   └┐░ │  │ │                              ░░░░│ ░│                             │░│
                        │ │   └─┐┘  │░│  ┌────┐──────────┐───────┐── ───┐   └────┐                        │░│
                        │ │   │ │ ──┘ │  │░  ░│   ░ ░░  ░│       │░░  ░ │░░░│ ░░ │                        │ │
                        │ └───      │  • │░ ░░└─ │        • ┌── │    │    •      │ ┌┐─┐────────────────── └─┘
                        │     ┌─┐   │    └───░│  └─────── ░─┘░ ─┘──┐─┘─ •  ┌────░│ └┘ │░░ ░ ░ ░░ ░░░ ░░░  │░│
                        │ ┌───┘ └───┘┐   ░░░░░│ │░░ ░░░░░   ░ │░░░░│░ ░ ░░ │░ ░░░ │░ ░░░░░░░ ░ ░──────────┘░│
                        │ │   └─┘    └────────┘─┘─────────────┘────┘─┐─────┘──────┘──┐─────────           │░│
                        │ │          │                               │               │          •    ┌──┐ │░│
                        │░│          └───────────────────────────────┘┐────┐  ░░░░░░░│ ░  ░░░░ •░ ░░ │░░│ │░│
                        │░└──────────  ░ ░░░ ░░░ ░ ░ ░ ░ ░░░░ ░  ░░░  │░░░░│ ────────┘──────              │░│
                         •            ──────────────────────────────── ────┘                 ░░░ ░  ───── ░ │
                      ┌─      ┌─────┐                                        ───────────────────────░ ░   ──
                      │░   ── │     │░─┐ •░│  ░│ ── ░ ░ ░ •                                           •
                      │ ──   ─┘───── • │   │   └─        • ──────┐───┐───┐────┐────┐─┐──┐─┐────     ── ───┐─
                       ░░░┌─┐░░░░░  • ░ ──░│ ░ ░░░ ░░░░ ░  ░░░   │░░░│ ░ │░ ░ │░░  │ │░░│ │       ░ ░    ░│
                       │░─┘ │ ─────  ───   └─────────────────────┘───┘───┘────┘────┘─┘──┘─┘───────────────┘─
                       │    │       │   •  │
                        │ │    •    │░•                             ┌───────┐                             │ │
                        │░└───┐ ┌───┘░ ──┐─┐─    ─┐───     •  ─┐──┐ │ ░░░░░░│       ─┐                    │░│
                        │░│   └─┘   │ •░░│ │░── ░ │░   ░ ┌─░──░│ ░│ │░─────░░──────┐░└┐      •         ───┘░│
                        │░└── │ └───┘░░         ──┘──────┘       ─┘─┘─    ░ •░     │  └┐─┐───             │░│
                        │░│   │░│   └──░░░░░░░░░░░░░░ ░░░░░░░ ░ ░░░░░░░░░░ ░ ░ ░ ░░░░░░│ │░░░─────────────┘░│
                              └─┘      ────────────────────────────────────────────────┘─┘── ░░░░░ ░░░░ ░░░ │
                 ┌────────┐──     ┌─┐                                                       • ────┐ ──── ──┐
                 │░░ ░░░░░│ ░│    │░│ •░│  ░   ░░    ░      ░  ░        ░     ░    ░  ░   ░  ░    │     │  │
                 └────────┘──┘   │  │   └─────────────────────────────────────────────────────────┘─────┘──┘
                                 │░    │
                     ─── ┌───┐   └── ──┘ ┌───────────────┐
                       ░─┘   └─     •░░░ │░░░ ░  ░  ░░░░ └─
                      │        ──┐── ─── │ ───   ──── ──   ────────────────┐─────────────────────────
                      └─         │  │         │░                      ░    │        ░       ░     ░░ ─────
                        │ │  ┌──    │░        └────      ───── ─────      ─┘  ───     ───────────────     ┌─┐
                        │░└──┘░░┌───┘░────┐ •                       ──────░└─     • •                     │░│
                        │░│  └┐─┘   │ ░░░░└─░──────┐───────░░───────░░░░░░░│ ────┐░ ░─┐─┐────░░░      ────┘░│
                        │░│   │ │    │             │                  ░   ░│     │    │ │░   ─── ─────    │░│
                        │     │ │    │░░░░░░░░░ │░░░░░░░░░│ ░░ │░░░░░░░  ░░│ │░░░░░  ░░░│░ ░•             │░│
                         •    └─┘    └──────────┘─────────┘────┘───────────┘─┘──────────┘──   ───────────┐ ┌┘
                                                                                           ─── ░░  ░░░░  └─┘
                 ────────────┐     ───────────┐────┐──────                                    ──────────
                   ░░░    ░  │           ░  ░ │  ░ │░  ░░
                  ───┐ ──┐   │     • ───       ────┘─────
                     │   │░  │      •░░░─┐░░ ░│
                     └─ •    └───┐── ─── │    └───────────────  ─────────┐────────────────────────
                       │░ │ ░    │          ░░     ░░░   ░ ░ ░• ░░ ░ ░   │░   ░░░  ░ ░░ ░░░░░ ░░  ─────────
                       └┐ └──    └──┐  ───────────────────────  ────   ──┘  ──────────────────────         ─┐
                        │░│  │░ ░│  │                               •░•░░░░•                              │░│
                        │░│  └┐─┐ ──┘───┐─┐────────────┐─┐────────── ░      ┌─ ───        ──────────────  │░│
                        │░└── │ └─   ░ ░│ │░      ░  ░░│ │░░ ░░░ ░░░ ░░░░•░░│░    ────────              ──┘░│
                        │░│   │ │    •░░░ ░░░░ ░ ░░░░ ░░ ░░│ ░  ░░ ░░░░ ░░░─┘                             │░│
                         •            ─────────────────────┘───────────────                  ──────────  │ ┌┘
                     ┌─┐   ──┐───── │                                        ───────────────┐░ ░░  ░░░░  │░│
                     │ │ │  ░│     ┌┘ ░ ░─┐┐─░│ │░░┌┐                                       └──────────  └─
                     │  ─┘   └┐──┐─┘      └┘  │ │  └┘┐──┐───┐─┐─┐────────┐──┐─┐───┐
                      │░░│ │░ │░░│ │  ░░ │░░░░░  ░░░ │░░│ ░ │░│ │░░ ░░░░░│ ░│ │░░ │
                      └──┘─┘──┘──┘─┘─────┘───────────┘──┘───┘─┘─┘────────┘──┘─┘───┘













```

*Figure from page 4 (2346x3317 px)*


---



4203-E P-331



SECTION 3 DATA INPUT/OUTPUT OPERATION



{h) bit 7 Special code store



Sets whether or not special codes are .stored.



bit? bit6 Contents



1 An alarm occurs when a special code is read.



1 0 Special codes are read but not stored.



0 0 Special codes are read normally.



(Initial values: bit 6 = 1, bit 7 = 0)



(2) NC optional parameters (bit) No. 8, 13, 14, 21, 22



NC optional



parameter



(bit) No.



No. 8



No. 13



No. 14



No. 21



Used to set the RS232C data handled by the channels used.



Channel bit 7 bit 6 bit 5 bit4 bit 3 bit2 bit 1 bit 0



CNO: File



DC Standard 8-bit Even/ Parity Ready 1-bit/



CN1:



name code DC code JIS/ odd check signal 2-bit



read/no control control 7-bit parity performed/ setting stop bit



CN2: tread TYPE2 JIS not



CN3:



performed



0 0 0 0 0 0 1 0



Initial



value



Explanation of settings for parameter (bit) Nos. 8, 13, 14, 21, 22



(a) bit O RS232C stop bit check



(b) bit 1



(c) bit 2



(d) bit 3



{e) bit 4



= 0 2 stop bits



= 1 stop bit



Determines whether or not the RS232C interface uses the "EXT-INT' signal as



the ready signal.



The "EXT-INT' signal is used as the ready signal.



= 1 The "EXT-INT' signal is not used as the ready signal.



RS232C parity check (determines whether or not a parity bit is appended to



8-bit data)



= 0 Parity check not performed



= 1 Parity check performed



RS232C even/odd parity



= 0 Odd parity



1 Even parity



RS232C 8-bit/7-bit JIS



= 0 7-bit JIS



= 8-bit JIS


```text


                                                                                                ──
                                                               ┌──┐────────┐───┐─┐─────────┐────░░░────────┐
                                                               │░░│░░░░░░  │░░░│ │░░░ ░░░░ │░░ ░───░░░░░ ░░│
          ┌───────────   •   ────────     ───   •   ─────────── ──┘─────── └───┘─┘─────────┘──
          │           ──┐  ──        ─────   ──┐ ┌──                                                        │
          └───────────  │ │        ─┐          │ │   ┌─  •     ─────────────────────────────────────────────┘
                      │  ─┘   ────┐ │          │ │  ┌┘ ── ┌────
                      └┐ ░░• ░  ░ │            │ └─ │     │    │
                       └──        │           •     │          └──────────          ───────────────────────
                          ░│  │  ┌┘  ┌─┐  │░ ░  │░•                       ┌────────                        ┌─┐
                         │░└──┘░─┼┘──┘░└──┘░────┼─ •  ┌──┐  ────┐         │░░░░░░░░•       ────────        │░│
                         │░│   │ │   │ │  │     │  ░░ │░ └── ░ ░│ ░░   ───┘────────    ░░ │        ─────── │░│
                         │░│   │ └───┼─┘  │ │   │        │                           ─────┘  ──────       ─┘░│
                         │░│   │ │   │ │  │ │   │ ─┐─────┘┐───┐──┐────┐ ────┐──░░░░┌┐                      │░│
                         │░└── │ └───┘░└──┘░│ ──   │░░ ░░ │░░░│ ░│ ░░░│   ░░│░░┌───┘┘──────────────────────┘░│
                         │ │   └─┘   │ │  └─┘   ───┘──────┘───┘──┘────┘─────┘─┐┘                           └┐
                                          │    •                              │    │ │    │     ┌┐──┐   ─┐  │
                      ┌─┐─ ┌───   ────────  ┌─┐ ┌┐                            └────┘─┘─  ─┘─────┘┘  └─── └──
                   ░  │ │ ┌┘░             │ │ │ └┘┐── │░│     • ──                     ──          •
                  ──  │ └─┘          ──   │ │ │   │  ─┘ │ ───  │  ──────────
                      │░░░░───┐░ ░• │░░░░░░  ░░│  ░ │░ ░│    │ │
                       ────   └─── ─┘─────── ──┘ ───┘───┘────┘─┘───────────┐
          ┌────┐───────       │                 •                          └──   ───┐─────────┐   ── •
          │░░  │░░░░░  ──────┐┘ │ ─── │░│ ───  │   ───  │░│ ──── │░─┐─── │░│  ───   │░       ░│ ──  │░│
         │  •░░░░  ░│   ░░░░░│  └─    └─┘ ░░   │ ┌─░  • └─┘  ░   └─ │    └─┼──    ──┼───  • ┌─┘     │░│
         │   │░░ ░░┌┘ ░┌─   ─┘ ─┘     │ │  •   │ │      │ │      │       │ │    •   │       │ │     │░│
         │   │░    │ │░│  •   │░└─    │ └─     │░└──────┘░└┐─      •  ─┐ │░└───┐    │░────┐  ░│     │░│
         │ │  •░┌─░│ │  ┌─░│  │ │░──┐   ░░─┐   │ ░░░ ░░░░  │░┌─ ──┐░── └─┘ │░░░│    │░░░░░│  ░  ──  │░│
         │ └─┐░░│  │ │░ │ ░│  └─ ░ ░└──  ░░└──  │░  •░░┌┐  │░│    │░░░•   │░░░ ░──── │░░░░░• │░ ░░──┘░│
         │ │ │      ─┘──┘  │  │░ ░░░│░    │░░░• └── ░──┘┘  │░│    │░──░   │░░┌──░░░░ └─░░──  │░░░• ░│░│
         │ │ └─┐ ───    │░░│    ┌───┘── ┌─┘── ░    ──   │  └─┘   │ •  ──  │░─┘         ──     ─── ──┘░│
         │  ─┘░│  ░  │░ │ ░░│ │ │       │     │         │      ──┘       │░░░ ░    ░                │░│
          ── └─┘ ─── └──┘───┘ │░│     │░│     │      │  │░│      │░│     │░┌──┐────   │     │░│     │░ ────┐
            •   •            ─┼─┘ │ │ └─┘     │ ┌┐ │ │  └─┘    ┌─┼─┘     │ │  │    │  │     │ └─┐ │ └─  ░░░│
                              │ └─┘ └─┘ └─────┘ └┘─┘ └──┘ └────┘ │ │ • ──┘ │  │ •  └──┘─────┘ │ │ └─┘  │░ ░ │
                              │ │ └─   •                └─┘      │ │     │ │  │               │        └────┘
                      ┌───────                          │             │    │   ─────────────── ────────
                      │             • ░──┐ ── ──── ───┐       ┌─ │  │ │   │ │ │
                      │       ┌────┐  •  └─  •        └─ ┌────┘ ─┘  │ │   │ └─┘
                      │░┌─┐░ ┌┘    └┐░░░░░░ •░   ── • ░ ┌┘                 •
                      └─┘ └──┘      └─┐─┐──        • ┌──┘
                                   │  │░│  │░ │░░ •░░│
                                   │  │ │  └─ │     │
                                   │  │ │  │  │   ░░│
                     ┌──┐─┐───┐      ─┘─┘─ └─       └┐──┐─┐───┐─┐─────┐─┐────────┐─┐──┐──┐──────┐─┐───┐──┐
                     │░░│ │░  │     │░░░░ • ░░──░░░░░│ ░│ │░ ░│ │░░░░░│ │░░ ░░░  │░│ ░│  │░░░ ░░│ │ ░ │ ░│
                     └──┘─┘───┘     │ ───   ──  ─────   └─┘───┘─┘─────┘─┘────────┘─┘──┘──┘──────┘─┘───┘──┘
                                         ──    │     ┌──
                                      │ │  ─┐░░└┐ ░░ │░░• ░  ░     ░   ░ ░      ░     ─┐
                                   │  │ │   │ • │    │ │  │  ─┐   ┌──    •          ── │
                                   │  │ │   │   │ ░  ░░│  │   │   │   ──┐             ─┘──┐
                      ──┐ ┌───┐     ┌─┘─┘── └───      •  ─┘───┘──┐  ──  └─          ──    └────────────
                     │░ │ │░ ░│     │░░░░░░─┘░░░│  ░░ ░ │░░  ░   │ ░░ ░░     │       ░              ░
                     └──┘ └───┘     └─────   ┌──┘───────┘────────┘───────────┘──────────────────────────
                                   •       │ │
                                     ─┐ │ ─┘░  ░┌── ─────────      │
                                   │  │ │   •   │                 ─┘
                                   │  │ │  │░   │                •
                       •   ───      ┌─┘─┘──┘─   │               │
                              │     │░          │        ┌──────┘
                      ─── ────┘     └─┐ ┌── ┌──        ──┘
                                      └─┘  ┌┘░░    ░ ┌─
                                   │  │ │  │  ───    │
                                   │  │ │  │     │   │
                      ──  ┌───┐     ┌─┘─┘──┘  ─┐ │    ──
                      ░   │░  │     │░ ░░     ░│ │     ░│
                      ─── └───┘     └─┐ ┌──┐   │ │ ┌────┘
                                   │  └─┘  └─ ─┘ ░░│
                                   │  │ │  │   │ • │
                                   └─ │ │  │░     ░
                                   │ ─┘─┘  └───────











```

*Figure from page 5 (2346x3317 px)*


---



4203-E P-332



SECTION 3 DATA INPUT/OUTPUT OPERATION



(f) bits 5, 6 Specify the DC code control conditions.



bit6 bit 5 Contents



0 0 No DC code control



1 0 No DC code control



0 1 Standard DC code control



1 1 DC code control TYPE 2



(g) bit 7 Required file name output in DNC-A mode (special specification)



= 0 : Required file name not output



= 1 : Required file name output



(3) NC optional parameter (bit) No. 12



(a) bit 2



bit 2



(b) bit 3



bit3



(c) bit 4



bit4



(d) bit 5



bit5



Specifies whether or not the file name is punched out.



Contents



The file name is punched out.



The file name is not punched out.



(Initial value= O)



Specifies the end of record code when punching in the ISO coding system.



Contents



CR, LF is output.



Only LF is output.



(Initial value = 0)



Specifies the code used for tape feed during punching.



Contents



The NULL code is output.



The SPACE code is output.



(Initial value= 0)



Specifies whether or not feed holes are punched during tape punching.



Contents



Feed holes are punched.



Feed holes are not punched.



(Initial value = 0)


```text


                                                                                                ──
                                                               ┌──┐─┐────┐─┐─────┐──┐─┐────────░░░───────░░│
                                                               │░░│ │░░░ │ │░░░░ │░░│ │░ ░░░ ░░ ── ░░░░░░──┘
          ┌───────────   •     ──────      •      •   ────  ─── ──  └────┘ └─────┘──┘─┘────────
          │           ┌─┐ ┌────      ─────┐ ─┐─┐─┐ ───    ──   •   │
          └────────── │░│ │   ░    ──    ░│  │ │ │    •            │   │            ────── ───────────────
                      └─  │ •    •                     •               └────       •      •               •
                         │░│  ┌──░   │ │  ┌─    │ │     ───   ────────     ░──────┐                         │
                         │░└──┘░ ┌───┼─┼──┘░ ───┘ └───                    •  ░░░ ░│                         │
                         │ │  └──┘   │ │  └─┐   │ ░░░ ─┐─┐──┐─┐─────┐        ─────┘  ────────         ────┐ │
                         │░│     │   │ │  │ │   │░     │ │  │ │     │              ──        ─────────    │ │
                         │░│   │ │  │  │  │░│   │░ ────┘┐ ░░│ │░── ░│                                     │ │
                         │░│   │ └──┘     │ └───┘░ ░░░░░│  ░│ │ ░░• ░────┐ ────       ─────       ────────┘ │
                         │░└── │ │   ─────┼─┘   └─ • ─┐░░│ ░        │░░ ░│     ───────     ───────        │ │
                         │░│     │        │ │   │  ░│ └──┼─── ░     │░ ░                                  │ │
                      ┌─    •       ┌─────┘─┘───┘┐  │    │              ─────────────────────┐              │
                      │░│ ─┐ ───────┘░░░ ░░░ ░░  └──┘────┘────┐───────░░░░ ░ ░░ ░ ░░░░░░░░░ ░└──────────────
                      └─┘─ └─         •  ──                   │       ┌──────────────────────┘
                                       ░│   │░─────┐──┐ │░────┘──░ ░░ │
                                       ─┘   └─░░  ░│ ░└─┘─ ░   ░  ┌───┘
                 ┌──  ┌─┐─┐───────────   ┌─┐               • • ───┘
                 │    │░│ │ ░           ░│ └── ░│   │
                 └──  │ │     ──────     └─   ──┘── └──────────┐───────────────────
                      │░│ ── ░      │░ ░░░░░─┐░░░ ░░   ░ ░ ░░ ░│  ░░          ░░   •
                      └─    •  ───  │ ┌───── └──────           │                    ──────────────────────
                         ┌─┐  │░ ░  └─┘             ──               ░  ░░░░                              │░│
                         │░└─ │ ┌───┘░  ────    •     ──────     ─────────────────────────────────────────┘░│
                         │░│  │ │   │  • ░ ░────░• ░ •░ ░░░░• ░░│                                         │░│
                         │░└──┘   ──┘░ ░                        └───  ──  ────────────────────────────────┘░│
                         │░│  │ •   │░──░░░░░░░░░░░░░░░░░░░░░░░░ ░░░                                       ░│
                             • • ───    ────────────────────────────  ────   ────   •   ─── │              │
                      ──   ┌─       ┌──                             ─┐    ───    ─┐  ┌─┐    │         ┌──  │
                     •░   ─┘ ─┐     │    ░   ░                  │    │ │     ──┐  └─ │ │   •         ─┘
                      ──      └───┐─┘                           │    └─┘────  ░│  │                   │ ──
                         │░│  │░ ░│ │░                              ░░░░░░░░│                             │░│
                         │░└──┼─┐─┘─┘            •   ┌──────────────────────┘─────────────────────────────┘░│
                         │░│  │ │   │ ───────────░─┐─┘                                                    │░│
                         │░└──┘ └───   ░░░  ░ ░   ░│ │ ──────────────────────────────────────     •   ────┘░│
                         │░│    │   ───────────────┘─┘                                        ───  ┌─      ░│
                      ┌─ │    ┌─┘──                                                  ────────┐ ░░░ │░░░─────┘
                      │   ────┘     ┌─░──░─────────░───────┐─┐───  ──     │ ──────┐─┐        └─────┘───
                      └─ │     ───  │ │  •         •       │ │   ──  ─────┘─      │░└───────
                         │░│ •░░ ░│ │ │                            │░░░░░░░░│                             │░│
                         │░│  │ ┌─┘ │░│ ──       ──     •    ┌─────┘────────┘────────────────  ───────────┘░│
                         │░│  │░│   │  • ░───────░░───── ────┘                                            │░│
                         │ └──┘ └───┘░░░░░ ░░░░░░ ░░░    ░░░ └───────────────────────────────          ───┘░│
                         │ │  │     └────────────────────────░                               ──────────    ░│
                      ┌─      └────                                                         •░░░░░  ░ ░   ░┌┘
                      │░  ─┐──┘    ─┐─░░ ░░░─┐░ ░░─────┐ •░───────┐─┐── •   ────────────┐─── ────── ────── │
                      └─   │   ──┐  │ ┌────  └────     └─ •       │ │  │ ┌──            │
                         │   •░░ │  │ │                             │░░│░│░░│                             │░│
                         │ │  ┌─┐┘  │░└─────┐── •  ────────     ────┘──┘─┘──┘─────────────────────────────┘░│
                          ─┘  │ │   │   ░░░ │░░│ ── ░░░░░ ░──                                             │░│
                        •  └──┘░└───  ░░░░░ │░░│ ░░ ░░░ ░ ░░░░░ ─────────────────────────────             │░│
                         │    │ │    ───────┘──┘─────────░─────                              ┌───┐ ┌───    ░│
                         └──── • ────                    •      ─────────────────────────────┘░░░│ │░ ░│  ──
                                                                                             └───┘─┘───┘──

























```

*Figure from page 6 (2346x3317 px)*


---



4203-E P-333



SECTION 3 DATA INPUT/OUTPUT OPERATION



(4) NC optional parameters (bit) No. 27 to 31, 49 to 51



(a) These parameters are used to set special EIA codes.



Parameter No. blt7 j blt6



blt5



blt4



blt3



blt2



blt1 j bit 0



No. 27 Sets the punch holes for the EIA code that represents"=".



No.28 Sets the punch holes for the EIA code that represents"*"·



No.29 Sets the punch holes for the EIA code that represents"[".



No.30 Sets the punch holes for the EIA code that represents"]".



No. 31 Sets the punch holes for the EIA code that represents"$".



No.49 Sets the punch holes for the EIA code that represents"#".



No.50 Specifies an irregular code.



No. 51 Specifies the regular code (ISO) corresponding to the irregular code.



I 0


# I Initial

value



(b) In both the EIA and ISO coding systems, it is possible to have one code treated as another in



program reading and program punching.



(c) Set a code which is to be treated as another code (Le. an irregular code) for optional



parameter (bit) No. 50 and the regular code that corresponds to this irregular code for optional



parameter (bit) No. 51.



The regular code must be set in the ISO coding system.



1) If an irregular code is encountered during reading it is read as the corresponding regular code.



2) If the regular code corresponding to an irregular code occurs during punching, the irregular



code is punched.



(5) NC optional parameters (word) No. 1, No. 2



Parameter Factory Set Setting



Item Contents



No. Initial Value Range



1 Tape feed For punchout in the PIP holes in 600 1 to 10000



holes in (transfer) mode, tape feed hole areas



punching are punched out before and after



program punch out.



The number of feed holes is set by



this parameter.



2 Defaults of A file of machining programs which is 180m 1 to300 m



tape too long to be stored in a roll of paper (590 ft) (3.3 to 984 ft)



lengths in tape is divided into smaller files to be



divided punched out. The lengths of the divi-



punching sions are set by this parameter. The



divisions are closed at the breaks of



each block, so that the actual tape



length is slightly different from the



setting. A divided punchout gives the



beginning of each tape part a file



name. Note that the setting does not



include the lengths corresponding to



the fife name and feed hole.


```text


                                                                                                ───       •
                                                                ┌───────┐───┐───┐─┐─────┐────── ░░░───────░░│
                                                                │░ ░ ░░░│ ░ │░░░│ │░ ░░ │░░░░░░░───░░░░░░░──┘
           ┌──────   •    •                 •      •    ──  •  ┌┘── ────┘── └───┘─┘─────┘───────      ──
           │      ┌─┐  ──┐ ───────────────── ┌────┐ ┌───  ─┐ ┌─┘   │
           └───── │░│  ░░│                   │   ░│ │      │ │     └─────────────────────────────────────────
                  └─   ─┐    • │      │ ───┐ └── ─┘ │        └─ │
                     •  │   • ─┘      │    │ │     ─┘──┐────┐   │ ────┐
                      • └─┐─    ──────┘────┘ │░───  ░  │ ░ ░└───┘─  ░ │
                     •    │                                            ──     ──      ───   ────
                           ────────────┐─  ┌┐┐─    ┌── ───┐───┐┐──┐┐─┐─  ┌───┐  ─┐───┐   ┌──    ┌──────┐
                          │░ ░░░░░░░  ░│  ─┘┘┘ ┌─ ┌┘░ │   │░ ░└┘░ └┘ │   │░  │ ░ │░ ░│   │░     │░    ░│
                          │░┌────┐─░• •  •░░░│ │░ │░░░└─┐─░░•░│ ░░│░░└─┐─┘░ ░░░ │░ ░ └──          •  │░│
                          │░│    │      •░   │  │ │   │ │░ │  │ │  • │ │ ░│   │ │  ░░░ ░│   ──────  ─┘░│
                          │░│  │░│ ┌─    •░│░│ ─┘ ░ ──░ │░░│ ─┼─┘░ ░ │ │░░│ ░░│ └─ ─────┘ ─┐         │░│
                          │░└─ │░│ │░┌───░─┘░│ ░└─    •  ░ │ ░│ ░• ░ │ │ ░│ ░ │         │ ░│ ────────┘░│
                          └─┘  │░│  ░│   ░ ░ ░  │ ░░ ░░   ░│ ░│  ░ ░ │ │ ░░  ░│ ░░░░░░░░│ ─┼─        │░│
                          │░│  │░│ ░│    │░░░░ ░└────── ───┘ ─┘ ─┐─┐─┘─┘──┐───┼─┐───────┘  │         │░│
                          │░└──  │  │ ──┐┘                 │  │  │ │      │   │ │        │░│         │░│
                          └─┘  │░│ ░│   │░░░░░ ░░ ░░░░░ │░░│ ░░ ░░─┘░───░─┘───┘ └────────┼─┘         │░│
                          │ │  │░│ •░•   ┌──── ─────────┘──┼─┐───┐ ░░░ ░░░░ ░░░ ░░░░░░░░ │░│         │░│
                          │ │  │ │  │    │                 │ │   └───────────────────────┘─┘         │░│
                          │ │  └─┼─░│    └──────────┐─┐────┼─┘──░│                                   │░│
                          │ └─┐░░│ ░  ──┐░░░░░░░░░ ░│ │░░░░│  ░░ ░░░░░░•░░░•░ ┌─░───░ ░░ ░░────────░┌┘░│
                          └─┘ └──┘───   │░┌────┐─┐─┐┘ │░─┐─ • ┌── ──┐─┐ ┌─┐ ┌─┘░ ░░ ┌────┐─░░ ░░ ░░░│ ░└────┐
                             •       ───┘░│    │ │ │ • │ │   ─┘  •  │ │ │ │ │ │ ────┘    │ ────┐── • │░░ ░░ └┐
                                        │░│    │ │ │   │ │            └─┘   │ │        •       │     │░ ░░• └┘
                                          │              │              │      •              •       ──── ─┘
                    ┌──    ────── ─── ───                    ┌─  ─────┐  ─┐──┐     ─── ─┐─┐──  ┌────┐
                    │░  ┌──░░░ ░░•░░░•░ ░──░────░░░──░•░░──  │░ ░░░░░░│ ░ │░░│   ░ ░░░│ │ │░░│ │░ ░ │░░│  │
                    └──┐┘      ── ░•░  •   •    ───  • ──  │ └────────┘───┘──┘────────┘─┘─┘──┘─┘────┘──┘──┘
                       │                                   └─
                    │   │      •░     ░         ─── •        ──  ───         ───── ┌───    ───  ──┐
                    └─  │    •            ── • •     •         ──   ────────  ░   ─┘   ────      ░└─┐──────┐
                        │░ ░░░░░  ░░░ ░│ │  ░ ░ •░  │░░░• •░░• ░░░ ░░░░░░░░ ░░── ░░░ ░░░░░░ •░░░  │ │░░░░░░│
                        │░─────────────┼─┘─────     └───   ──  ───     ───────  ──────────── ─────┘─┘──────┘
                                       │       ─────    ┌─┐  ──   ─────
                    ┌─ ┌─ ──░░░────░░░─┘──░░ ░  ░░ ░  ░ │░│ ░░░░ ░ ░░░░░──
                    │  │░•   ──     ──    ──             •   ──   ──────  ───────┐───────────── ────── ────
                    │  │  •            │                                         │            ░│  ░
                    │░ │░ ░│ │░  ░░   ░│    ░     ░        │░         ░                      • │ •      ┌─
                    └─  ── │ └─        └───────────────────┘─────────────────────── ─────── • ─┘─ ── ───┘
                       │  ─┘   ┌─────                                              •       •        •
                  ──┐─┐┘    •  │       ─────────────────┐────┐
                    │ │ • ┌─░──┘── ░░░ ░░░░  ░░░ ░ ░░   │░░  └─
                   •  │  ─┘        ──────────┐─┐──────  └──  │      ─────────────┐──────────┐──┐── ────  ──┐─
                     │░  ░░• ░░░ ░│          │ │      ──    ─┘─┐───┐             │░░░░░░░ ░░│ ░│  │░░░░─┐  │░│
                     │░│ ─┐░─── │░│  •░░░─┐  │ │           •   │░ ░│            │   ░ ░ ░ ░    │  │░░  ░│  │ │
                     │░│  └┐    │░  •     │  │░└─── ───────          ──── ─┐    │░┌──┐   ░ ──  │ │    ░░└─ │░│
                     │░└── └────┘  │░────░   │   ░ │░ ░░░ ░─┐ ┌──────░░░░• │ ──┐  │  └┐░░──  ┌─┘ └┐ ──░░░  │░│
                     │░│           │░░░ ░ ──  │░ ░ │░░• •░░░│ │░░  ░░░  ░░ ░ ░░│  │   └──    │ │  └─  ──── │░│
                     │░│           └──░░░░    │░ ░ ░░│░•░░ ░  ░┌───────────────┘┐ │          │ │           │░│
                     │░│        │ │   ─────   │░ ░░ ░│ ░┌─░░ │░│                │ │          │ │           │░│
                     │░│        │ │           │░░░│░•░░░│ •░─┘─┘ ░ ░         •  │ │          │ │           │ │
                     │░└───   ──┼─┘          ┌┘░░ │ ░ ──┘                       └─┼─       • │ │          ─┘ │
                     │░│    •   │░│ ──────── │░   │     ░  ──── ─────── ─┐──    │░│  ┌────┐  │ │  ───── ─┐ │░│
                     │░└───┐ ───┘  •░░░ ░░ ░─┘░░ •░ ░   ░ ░░░░░•░░░░░░ • │░░───┐ ─┘  │░░  │  │ └─ ░ ░░░ ░└┐  │
                     │░│   └─    • ░░░│    │  │░│   ░░   ░░ ░ ░░░• │░  ░ ░ │░░░│  │  └── ░│  │ ░░ ────░░ ░│ ░│
                     │░│          ─┐░░└── ░│  │░│░│ ░ ░ •░•░░ ──┐░ │░┌─┐░░ └──░│  │     ──┘  └─┐──    ────┘ ░│
                     │░│        │  │ ░░░░─┐   │░ ─┘░     │ │░•░ └─ ░░│ └─░│  ░ │  │          │ │           │░│
                     │░│        │    ───  │   │░│ ░   ░ ░│ │  ░   •░• •░ ░│ •  │  │          │ │           │░│
                     │░│        │ ┌──   ──┘   │░│   │    │ └───  ░ •░  •  │   ░│  │          │             │░│
                     │░│        │░│           │░│ ░─┘  ░   │░░░░░░│ │░   ░░── ─┘  │         │ │            │░│
                     │░│        │ │           │░│   │  ┌───  •░   │ │  •  ░░░│  │ │         │ │            │░│
                     │░│        │ │           │░░─┐─ ░┌┘░░░░• ░░░│░•  ░░• ░░ └─┐┘ │         │ │            │░│
                     │░│        │ │           │░░░│░░ │ •░ │░│ ┌─┘░░ •  ░░░░•░░│  │         │ │            │░│
                     │░│        │ │           │░░│░│ ┌┘─░  │░│ │░░░ ░░│   ░•   │  │         │ │            │░│
                     │░│        │ │           │░░│░│ │░░░  ░• │ ──┐░░ │ ░░░░  ░│  │         │ │            │░│
                     │░│        │ │           │░░│ ░• ─────┐ ░│  ░└─░░░┌────  ─┘  │         │ │            │░│
                     │░└────────┘ └─────────── ░░ ░    ░   │░░ ░░    ░┌┘       │ ─┼─────────┘─┼────────────┘░│
                     │ │        │ │           ─── ─── ──── └── ──░────┘           │          ░│            └─┘
                        ────────┘─┘───────────   •   •    •   •  •     ───────────┘───────────┘────────────










```

*Figure from page 7 (2346x3317 px)*


---



4203-E P-334



SECTION 3 DATA INPUT/OUTPUT OPERATION



(6) NC optional parameters (word) No. 6, 39, 40, 41, 42



Set the baud rates for channels CN0: to CN3:.



NC Optional



Parameter Channel Contents



(word) No.



No.6 CN0: Any of the following baud rates can be set: 110, 150,



200,300,600, 1200,2400,4800,9600, 19200,



No.39 CN1:



No.40 CN2:


#### No. 41

Initial Value



600 baud



CN3:



(7) NC optional parameters (word) No. 34, 35, 36, 37, 38



Set the ready completion waiting times for channels CN0: to CN3:.



NC Optional



Setting Range



Parameter Channel Contents Initial Value



(Unit: Seconds)



(word) No.



This is the waiting time between


#### No.34 CNO:

output of DC1 (tape reader start) or


#### No.35 CN1:

the cessation of data reception and



reception of data; or the waiting



1 to 9999 time (when CTS and DSR are ON) 10 seconds


#### No.36 CN2: until the RS232C ready completed

status comes into effect. If there is


#### No.37 CN3:

no response within this time an



alarm occurs.



(8) NC optional parameter (word) No. 45



Used to select the punch channel for data transfer.



Setting for No. 45 Peripheral Device Initial Value



0 CN0: (TT:) [RS232C]



1 CN1: [RS232C]



2 CN2: [RS232C] (This selects CN0:)



3 CN3: [RS232CJ



(9) NC optional parameter (word) No. 57



Used to select the read channel for data transfer.



Setting for No. 57 Peripheral Device lnitial Value



0 TR: [Standard tape reader]



1 CN0: [RS232C]



2 CN1: [RS232C]



3 CN2: [RS232C] (This selects TR:)



4 CN3: [RS232C]



5 CN4: [RS232C]


```text


                                                                                               ───
                                                               ┌───────┐─┐─┐─────┐─┐───────────░░░─────────┐
                                                               │░░░ ░░░│ │ │░░░░ │░│ ░ ░░░ ░ ░░───░░░░░░░░░│
          ┌──────   ──   •                 •     •     •  ─────┘─── ───┘─┘ └─────┘─┘───────────      ───
          │      ───  ──┐ ───────────────── ───── ──┐── ┌─         •                                       │
          └─────    •  ░│   ░                       │   │░ │    │ │ ┌──────────────────────────────────────┘
                 ───  │ └─┐        ──┐     ──  ┌─   └─┐─   └─┐ ─┘ └─┘
                      │░│ │░ ░░ ░──░░│ ── •░░ ─┘░│  ░░│   │░░│
                      │            ──┘     ─┐   ─┘────┘   └──┘────────────────────────────────────────────┐
                      └────┐───────         │ │                                                           └─┐
                     │  ░  │░░░░ ░   ┌──────  └──────────────────┐────┐──┐───────────────────┐─ ┌───┐─┐── │░│
                     │  │░─┘░░░░░•   │░░░░ ░  │                  │░░░░│ ░│                   │  │░░░│ │░░░│░│
                     │░ └┐░░░──░│             │                                     •   •    └─ └───┘─┘── │░│
                     │░│ │░░│ ░┌┘ │ ─┐──────┐─ ────┐──────┐────────────────────────  ──┐ ┌─┐   •          │░│
                     │░│  •░│ ░│ ─┼─ │░░░░  │░ ░░  │ ░  ░░│░░ ░░ ░░░ ░░░░ ░░░ ░░ ░░ • ░│ │░│ ──           └─┘
                     │░│ │░░│ ░│  │   │░░•  │░ ────┘░─────┘─────────░────░───░░────░░░░│  •     ┌──┐─┐─── │░│
                     │░│ │░  • │ ─┼─  │░ ░┌─┘░│     •               •    •   ──    ────      │  │░░│ │░░░ │░│
                     │░└─┘░░  ░│  │  •  ░░│ │░│                                              │   ──┘─┘─── │░│
                     │░│  ── • │  │   │░░│  │ └──────────  • ────────────────────────────────┘ •          │░│
                 ┌─  │ └┐       ──┘   └──┘ ─┘            ─┐ │                                │            │░│
                 │ │  │ │ •               │ │          │  │ │ │      │  •       ─────────────┘────────────┘
                 └─┘  └─┼─            ────┘ │ ───   ── │ •  │ └─    ░└─┐ ┌──┐──
                      │░│ ───          ░ ░│ └┐         │  │ │          │ │  │  •
                     •       │         ──    │      •  │  │            │        ───────────────────────────
                      ─────┐─┘─ ─┐   ┌─     •        ──                  ── ────                           ─┐
                     │░ ░░ │░░░• │   │ ────┐ │ ──────  ────  ┌───────────  •    ─┐───────────┐  ┌──┐─┐────  │
                     │░─┐░░░░░░░┌┘   │░░░░ │ │ ░░ ░ ░  ░ ░░  │           • ░░░░ ░│           │  │░░│ │░░ ░│░│
                     │░ │░──────┘  • │     │     ───░   ───  └─                            ──┼─ └──┘─┘────┘░│
                     │░┌┘┐      │ │░│ ────┐ │░┌──   ────   │░ ░─┐───────────────── ──────    │░│          │░│
                     │░│ │░│ │░│  │ │ ░░░░│ └─┘            │  │ │ ░ ░░░░░░░░░ ░░░ •░░░░░░─┐   ─┼──────────┘░│
                     │░│ └─┼─┼─┘  │░│ ┌───┘ │ │              ─┘░░░░ ░ ░░   ░░•░ ░░░░│ •░░░└─┐  │          │░│
                     │░│   │ │   ─┼─┘ │     │ │            │  │░ ░░░░░░░ ┌─ •░░░ ░░░└─░░  ░░│  │          │░│
                     │░└─┐░│ │░│  │ │    ───┘ │  ┌───┐───┐ │░ ░░░░░░░  ░ │░│  ░ ── ░░░░░░     ─┘──┐────── │░│
                     │░│ │ │ └─┘  │    •    │░│  │ ░ │░░░│ │  │░│ │░░░ ──┘ │ ░──░░░░ ░ ░────   ░  │░ ░ ░░ │ │
                     │░│ │░│ │░│  │ │ •░░┌──┼─┘  └───┘───┘ │  │░│ └┐─┐░░░░░│ •░░░ ── ░░░░░░░│  ┌──┘────── │░│
                     │ │ │ │ └─┘ ─┼─┘    │  │ │            │  │░│  │ └──┐─┐░  │░░░  ░ ░ ░┌──┘ ░│          │░│
                     │ │ └─┘ │ │  │░│ ┌──┘─ │ │            │     ░•   ░░│ │░──┘───░ ─┐──┐┘     │          │░│
                     │ │ │░└─┘ └─ │░│ │░░░ ─┼─┘────────────┘┐ ░  ░ ░       •         │  │    ┌─┘──────────┘░│
                     │ │ └─┘ └─┘  └─┘ └───  │               │░░░░░ ░░░░ ░│                   │░           └─┘
                 ┌─┐ │  │                         │ │        ──── ───────┘────────────── ────┘────────────
                 │░│  ┌─┘──    ──░░•  ░░ ── ░ ── ░└─┘░ ──────    │
                 └─┘  │░░░ ────░░──░───── ░─── ░──░ │░ ░░░ ░░░ ░░│
                                                       •          ─────   ────────────┐─┐───     •      ──
                     ┌─ ░░░░░░ ░░░░░ ░░░ ─┐           •  ░░░░───── ░░░░─┐             │░│   ░░──░░░────   │░│
                     │  ──────  ┌───────┐░│ ┌───   •    ───── ░        ░└─────────────┘░└─────░░───░░░  ──┘░│
                       •      │░│       │ │ │░░░│ │░░ ┌─     ─┐░░░░░░░░│              │ │      •   ───    │░│
                    │ │       │ │       │   └──┐┘ └───┘       └──    • │              │ │                 │░│
                    │ │       │ │       │   │  │              │  ───┐  │              │  ┌──┐─┐──────┐────┘░│
                    │ │       │░│       │   │░░░│             │░░░░░│░░│              │  │░ │ │░░░░░ │░░░ │░│
                    │ └┐──────┘ └───────┘──┐    │  ───────────┘        └──────────────┘  └──┘─┘─    ─┘─── │░│
                     │ │      │░│        ░ │░░░░└─┐           ░░░░░░░░│               │░                  │░│
                 ┌─┐ │ │      │          │  ────  │ │       ──────────┘───────────────┘─────────────────── •
                 │ │ │  •     └──   │ │  │        └─┘ ┌─
                 └─┘ │            ──┘─┘ •  •          │ │ ───  ──
                     │                   •          ──  │                ─────────────┐─┐───           ───┐
                    ┌┘  ┌────────░░│ ░░   │              ░ ──────────────             │░│    ─────────┐   └─┐
                    │   │░░░░▒ ░░░░│ ───┐─┘ ─── ┌─────────░░░░░░░░░░░░░░ ─┐──────── ──┘░└──   ░░░ ░░ ░│ ──┘░│
                    │ │  ─────┐────┘─   │ │  ░ ┌┘         ────┐────────┐░░│  ░░░░░░│  │░│   ──────────┘   │░│
                    │ │       │         │ │ │  │              │        └──┘────────┘──┼─┼───           ───┘░│
                    │ │       └─┐       │   └─░               │ ░░░░░ │               │ │                 │░│
                    │ │       │░│       │   │░──              │░──────┘               │ │                 │░│
                    │ │       │ │       │░│                   │       │               │  ┌──────────┐───┐ │░│
                    │ │       │░│       │ │ │░░│              │░░░░░░░░•              │  │  ░░ ░░░░░│   │ │░│
                    │░│       └─┘       │   └──┘              └───────┐               │  └──────────┘───┘ │░│
                    │░│       │ │       │   │                 │       │               │ │                 │░│
                    │░└───────┘░└───────┘   ░░░░ ──────────── │░░░░░░░░───────────────┘─┘─────────────────┘░│
                    └─        └─┘           ────              └────────                                     │
                      ────────   ──────────      ─────────────          ───────────────────────────────────














```

*Figure from page 8 (2346x3317 px)*


---



4203-E P-335



SECTION 3 DATA INPUT/OUTPUT OPERATION



(10) NC optional parameter RS232C {CN0:)



This screen displays the parameters to be used for the tape punch interface function, which are allocated



to NC optional parameter {bit) and NC optional parameter (word). Note that they are only for CN0: device



and it is necessary to set the parameters for the individual NC optional parameter (bit) and NC optional



parameter (word) screens for other devices.



When the following parameters are set, the corresponding NC optional parameters are set accordingly.



Conversely, if NC optional parameters are set, the corresponding parameters shown below are set



accordingly.



PARAMETER SET



*NC OPTIONAL PARAMETER"



197/07/1~ 14:10:00



Aszn: <CNo:)



NO.



l STOP B IT(l '. lbi t/0:2.bi t) 1



2 PARITY CflECK(l :Yes/0:No) l



3 PARITY(l: Even/0:0dd) 1



4 8 BIT JIS(l:Yes/0:No) 1



5 DC CODE(l :Yes/0:No) l



6 DC CODE TYPE2(1:Yes/O:No) 1



7 FILE NAME REQUEST at DNC--A(l :Yas/0:No) 1



8 MASTER/SLAVE or RS CONT. (I :SLY, Yes/0:MAS, No) 1



9 BAUD RA.TE(bps) 99999



10 BUSY TIME(sec) 99999



ACT POSIT (WORK) 300. 000



SET



100.010



100.000



ITEM t ITEM l [EXTEND]



(a) 1 STOP BIT (1 :1 bit/0:2bit) {NC optional parameter {bit) No. 8, bit O)



RS232C stop bit check



= 0 : Stop bit 2



=1: Stopbit1



(b) 2 PARITY CHECK {1:Yes/0:No) (NC optional parameter (bit) No. 8, bit 2)



RS232C parity check (sets whether or not a parity bit is added to 8-bit data)



= 0 No parity



= 1 Parity check



(c) 3 PARITY (1 :Even/0:Odd) (NC optional parameter (bit) No. 8, bit 3)



RS232C odd parity scheme



"" 0 Odd parity



= 1 Even parity


```text


                                                                                                ───       •
                                                                ┌─────┐─┐───┐───┐─┐─┐───┐────── ░░░░──────░│
                                                                │░░░░░│░│ ░ │░░░│ │░│░░ │░░░░░ ░────░░░░░░─┘
           ┌──────   ──   •      •  ── •  ──       •    ────────┘─────┘─┘── └───┘─┘─┘───┘──────       •
           │      ───  ─── ────── ──  • ──  ──────┐ ┌───
           └─────┐   ──░                          │ │     │
                 │       │ │ ────────            ─┘─┘ •   └─┐─┐┐─ ───    ── ┌──────          ──
                 │       │ │░        •               │ │    │ └┘ •   •  •  ─┘      •    •   │  • ──────────
                 │   │    │    │  │ •   ░        │  ─┘─┘    │                            ── │   •  ░       •
                 └──░│   ─┘┐───┼──┘┐ ─┐ ┌───┐────┘──░░░ ░ ░░ ░░░░░░ ░░░ ░ •░ ░░ ░░ ░ ░░ ░░ •░░ ░░  ░░  ░░ ░░│
                 │░░ ░ ░  ░│░░░│ ░ │ ░│ │░  │░░░░░░░░ ░┌─┐░───░░── ░ •░──░░░░────░░░──░░──░░──░── │░──┐░────┘
                 └───┐───┐─┘───┘───┘──┘─┘───┘──┐─┐─────┘ └─   ──  ─── •  ────    ───  ──  ──  •  ─┘─  └─
                 │   │   │                     │ │      •  ───       │
                 │░░░└───┘ ░░░░ ░░ •░░░ ░░░ ───┘─┘─┐ │░ ░░ ░░░│  ░░░ │░│ │░░░░  • ░  ░ ░  •    • ───    ░ ░─┐
                 └───       ───  •      ┌─┐┐       └─┘ ┌─┐ ┌─░│ ─┐     │ │░                         │ │     │
                 │        │    ── ──────┘ └┘───── ─┘ │ │ │ │ ─┘  │ •     └─ │ •      ░ ────   ───   │ │ ────┘
                 │░░░░░░░░│                      •        •       • ───    ─┘─ ────────    ───   ─── ─┘─
                 └────────┘   •                    ──────     ───      ──
                             │   ┌───────────                                        ──   │
                             │   │ ░░░▒░░░ ░░ ───          •         ─┐   ┌───┐─┐────  •  │
                             │ │    ─────────    │    │     │  ░   ┌─ └─░░│░░░│ │░░░ ░│   │
                             │ │  │░           • │    │ ┌── └──────┘    ──┘───┘─┘───┐─┘ │ │
                             │ │  └─ ┌───░ ┌─── ─┘─ ──┘┐┘  •                        │   │ │
                             │ │    ┌┘░░   │░ ░   ░│  ░│                          │ │   │ │
                             │ │    │░░░░│ │░ ░ ───┼─ •                           │ │   │ │
                             │ │    │░ •░└┐    ░░ ░│░•                            │ │   │ │
                             │ │    │░░ •▒└┐░░│░  ░│  ────   ──                   │ │   │ │
                             │ │    │░ ░ ░└┘ ─┘░░░  ░ ░░ ░ • ░░─────┐──┐          │ │   │ │
                             │ │    └──░░░ ░░░░─┐─░  ░──── ░───░ ░ ░│ ░│         ─┘┐    │ │
                             │ │  │  ░░│ │░░│░░░│ ────    ──   ── ──┘──┘        │░░│    │ │
                             │ │  │ ───┘─┘──┘───                                └──┘    │ │
                             │ │  │                ────       ────       ────           │ │
                             │ │  │   ░      ░                    │          │          │ │
                             │ │  └─────── ────   ──────     ─────┘      ────┘          │ │
                             │ │                                                        │ │
                             │ │                                                        │ │
                             │ │     ─┐─┐────┐─┐─────       ─────┐─┐    ┌─┐    ───      │ │
                             │ │  ──  │ │    │ │      ──────     │ └┐──┐┘ └──┐    ────┐ │ │
                             │ │ │    └─┘    └─┘    ─┐      •    │  │  │ •   └┐       └┐  │
                             │   │                   │   •          │  │      │ │      │  │
                                ─┘ │ ─────┐─┐─┐──┐───┘ ─┐   ─┐─┐────┘─   ───  └─┘     ┌┘─
                               │░ ░│ ░ ░ ░│ │ │ ░│ ░ │  │ ░░ │░│    ░░  ░░ ░    ░ ░░ ░│
                               └───┘──────┘─┘─┘──┘───┘──┘────┘─┘──────────────────────┘

                    ┌─┐ ┌──────┐─┐ ─────────────────┐──────┐───────┐ ─────┐ ──────┐
                    │░│ │      │░│     ░    ░░   ░  │░░░ ░ │░ ░░░░░│  ░░ ░│    ░  │
                    └─ │░     •   │    •    ────────┘──────┘───────┘──────┘───────┘
                       └┐      ── │        •
                        └─┐───┐    ┌── ┌───
                       │  │   │  │ │   │
                       │      └─░│  ░  │
                    ──    ────┘ •    ┌─┼───┐──────┐─┐─┐┐  ────     ───     • ──┐      •
                    ░       ░  • │  ░│ │   │      │ │░└┘──    ─────   ───── │  │ ───── │
                    ──  ──── ─┐ ┌┘─ │  └─┐─┘       •  │                     │  │       └──
                       │░░░░░░│ │░░░└─░░ │ │  ░ ░░░░░     │       ░      │  ░  ░      │
                       └┐────┐ •    │ ┌──┘─┘──────────────┘──────────────┘────────────┘────
                        │    └┐░• ░░│░│
                       │ ──   │  •  │ └──┐
                       │      │ ░░• │░│░░│
                    ┌─┐┘┐──┐─┐┘ ─┐ •  │  └───┐─┐─┐──┐───┐─┐───┐─┐─┐─┐─┐───┐───────┐
                    │ │ │░░│░│░• │ ░░░░ ░ ░░░│ │░│  │░░░│░│░░░│ │░│ │░│  ░│ ░    ░│
                    └─┘ └─      ┌┘┐─   │    •   ┌┘──┘───┘─┘───┘─┘─┘─┘─┘───┘───────┘
                       │░░░░░░• │░│ │░░│ │░░░░░░│
                       └┐─┐─── ┌┘ │ │  └─┘──────
                        │ │   ┌┘░• │░░░│
                         ┌┘   │ •  └┐  └┐
                       │ │    │ ░░│ │░ ░│
                       └─┘    └───┘─┘───┘














```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-336



SECTION 3 DATA INPUT/OUTPUT OPERATION



(d) 4 8 BIT JIS (1 :Yes/0:No) (NC optional parameter (bit) No. 8, bit 4)



RS232C 8-bit JIS



= 0 7-bit JIS



= 1 8-bitJIS



(e) 5 DC CODE (1 :Yes/0:No) (NC optional parameter (bit) No. 8, bit 5)



DC code control



= 0 Controlled by DC code



= 1 Not controlled by DC code



(f) 6 DC CODE TYPE2 (1 :Yes/0:No) (NC optional parameter (bit) No. 8, bit 6)



DC code control type 2



= 0 DC code control type 2 is not executed.



= 1 DC code control type 2 is executed.



6 DC CODE TYPE2 SDCCODE Description



0 0 Controlled by DC code



1 0 Not controlled by DC code



0 1 Standard DC code control



1 1 DC code control type 2



(g) 7 FILE NAME REQUEST at DNC-A (1 :Yes/0:No) (NC optional parameter (bit) No. 8, blt 6)



Request file name output at DNC-A (option)



:a:



0 Request file name is not output



= 1 Request file name is output



(h) 8 MASTER/SLAVE or RS CONT. (1 :SLV, Yes/0:MAS, No)



(NC optional parameter (bit) No. 40, bit 0)



Master/slave station designation or RS control designation



= O : Master station or without RS control



= 1 : Slave station or with RS control



(i) 9 BAUD RATE (bps) (NC optional parameter (word) No. 6)



Selection of baud rate from 110,150,200, 300, 600, 1200, 2400, 4800, 9600, and 19200.



Initial value: 600



u) 1 O BUSY TIME (sec) (NC optional parameter (word) No. 34)



Sets the delay time until data receiving or RS232C getting ready (CTS and DSR ON} after sending



DC1 (tape reader start) or interruption of data receive. If there is no response within the set length



of time, an alarm occurs.



Setting range: 1 to 9999 sec.



Initial value: O


```text


                                                                                               ───        •
                                                               ┌──┐─┐────┐─┐─────┐─┐───────┐───░░░───────░░│
                                                               │░▒│ │░░░ │ │░░░░ │░│ ░░░░░░│ ░░ ──░░░░░░░──┘
          ┌─────────   •      •            ───   ──  ────────── ──┘ └────┘ └─────┘─┘───────┘───
          │         ─── ────── ┌───────────   ──┐  ──          •   │      │                                │
          └─────────       ░   │                │ │    │         │ │ │  │ │  │   ┌─────────────────────────┘
                    ── ┌──   │ │    │ • ──── ───┘ │ • ┌┘ │       │ │ │ ─┘    │  ┌┘
                       │░░  ░│ │    │░ •    •    • • ─┘┘─┘─────── • • •  ────┘──┘
                       └┐─┐──┘     │  │
                        │░│  │  ░┌─┘░┌┘
                        └─┘      │ │ │
                        │ │  │░ ░│ │░│
                    ─┐─┐┘┐┘┐─┘   │ └─┘───────────────────────────────────────────
                    ░│ │ │░│  ░░ │ │  ░  ░ ░   ░░    ░  ░        ░  ░ ░ ░
                    ─┘ └─ • ──    ─┘─ ────────────────────────────────────────────
                       │░• │ ░─┐─░ ░░│
                       └┐ ┌┘── │     └┐─┐───┐─┐──┐─
                      │ │░│   │░  ░░░░│ │░ ░│ │░░│
                      │ └─┘   └─┐ │    •    │ │ ─┘─┐─┐
                          │   │░│ │░ ░ ░│  ░│ │░ ░░│░│
                    ┌──┐─┐┘───┘ └┐ │    │ ── ─┘────  └─┐──┐──────┐───────┐─┐─┐──┐─┐───┐─┐
                    │░ │ │░  ░│░░│ │░░░░░   │░░░░░░  │░│  │░░░░░ │░ ░░░░░│ │░│ ░│ │   │░│
                    └──┘ └──   ──┘ │ ─┐     └────────┘─┘──┘──────┘───────┘─┘─┘──┘─┘───┘─┘
                       │░│   ░░  ░ ░│ │░░░  │
                       └┐ ┌───   •  │  •  ──┘────────┐───┐──────┐
                      │ │░│   │░│ •░░│ ░ ░   ░░░   ░ │░  │░░░░░ │
                      │  •    │ │    │      •        │       ┌──┘
                      └─     ─┘ │ •░─┘───  • ░░░   ░─┘──────░│   ──────────────────          ──────────────
                      │   ───   └┐ │     ──  ─┐────┐         └┐                    ┌─────────               │
                      │░│ ░ ░░ ░░│░└┐  ░ ░░•  │    └┐ ░│ ░░░░░│    │ │             │░░░░░░░░░•            │░│
                      │░│      ──┼─┼┘──────  ░│ ─── └──┘   ┌──┘────┼─┘ ───────────┐      ░ │        ───── │░│
                      │░│     •  │ │       ─┐─┘         •  │       │░│    ░ ░░░░ ░│ ░  ░░░░└── ─────     ─┘░│
                      │░│        │ │        │ │           •        │  │░░• ░░───░░└──░ ░──░░░░│           │░│
                      │░│   ─────┘░└───    ─┼─┘            ┌───    │░┌┘░        •         •   └───      ──┘░│
                      │░└───     └─┘   ──── │░│            │   ────┼─┘┘░░░░░░░░ ░░──░░░│░░░░░─┘   ─────   │░│
                      │░│        │ │        │ │            │       │   •░───┐──┐──░░───┘░───            ──┘░│
                   ┌─┐┘  ────────┘ └────────   ──────────  └───────┼─┐      │  │            ───┐──────┐   │░│
                   │░│ ░ ░░ ░ ░░░░░ ░░░░ ░░░░•░ ░░░░     ──░░░ ░░  │░│ │░░░ ░░ │░ ░░░░│   ░ ░░ │░ ░░ ░└───
                   └─┘ ┌──                  │ │ │  │         ┌─────┘─┘─┘───────┘──────┘────────┘──────┘
                       │░░░░░░ ░░  ░░░░ ░ ░░│ │ │░░│ ░ •░░░ ░│
                       └┐─┐───           │ │   ─┘┐─┘ ── ─┐───┘
                      │ │ │   │░░░░░│ ░│ │░│ ░ ░ │░└─░░│ │
                      │ │ │   │     │  │ │ │     │ │ ┌─┘─┘
                      │      • ░ ░  │ •  │░    ░ │░░░│
                   ┌──   ────          │    •           •  ──────┐──┐────┐
                   │░  ┌─░░░░       ░░░└── ░ ──░ ─┐ ── ░  • ░░░░ │░░│  ░░│
                   └── │░──────────┐─── ░░░──░░──░└─░░────░   ───┘─      │
                       │           │              │         ┌─     ┌─┐───┘┐
                       │░░░░│ •░░│ │░•░░ •░░│▒│░░░│ ░ ░░• ░░│░│ │░░│░│░░░░│
                       └──┐─┘┐  ─┘┐ │  ─┐ ──┘─┘        •    └┐┘─┘──┘─┘────┘
                      •   │  │░░░░│ │░•░│  ░  ░░░─┐  ░│ •░│ ░│
                        ──   └─ ──┘ │  ─┘   ┌─ ─┐ │   │  ┌┘──┘
                      │      │░      ░• │   │ ░ └─┘ •░  ░│
                   ┌─┐┘──────    ─┐    ─┘─┐─ • ─┘  •     └───┐───────┐────┐
                   │░│ ░ ░░ ░│ │ ░│  ░░░  │░• │░░░░░ ░░░░░░░░│ ░░░ ░ │░  ░└┐
                   └─┘┐      │ └── •       •  └─┐─┐─┐ ┌─┐  ──       ┌┘     └───┐─┐──┐─┐───┐─┐─┐─┐────┐
                      │  •  ░ •    ░    ░│    │ │ │ │░│ │ ░  ░░  ░ ░│ │░░│ │░ ░│ │░░│ │░░░│ │░│ │░░░░│
                       ┌─ ┌─┐    ────  ──┘────┘─┘─┘─┘─┘─┘───────────┘─┘──┘─┘───┘─┘──┘─┘───┘─┘─┘─┘────┘
                       │  │ │        ──
                   ┌─┐ │   ─┘ ┌─  ─┐    ────┐──────────────────────────┐─┐──┐
                   │░│ │  •   │ •░░│ •░░  ░ │ ░░░░░░░ ░░░░ ░░░  ░░░ ░ ░│ │░░│
                   └─  │       •         │                                  └──────   • ───  •   ──    ──
                      ┌┘    ───  ───   ──┘── ░ ──░  ── ░────     ───   ░░•░░ ░     ──░     ── ──░░░────░░─┐
                      │░    ░░░  ░░░░  ░░░░ ░ ░░░  ░░░░•░░░░░░ ░░░░░────░░░─── ░ •░░░• ░░•░░░░░ ░──░░░░░░░│
                      └───────┐────────────░│ ───────── ────────────    ───   ─── ─── ─── ──────   ── • ──
                              │             └─
                      │░░░░ • ░ •░│  •░ │░░░│ ░░│
                      └─ ─┐─ ──  ┌┘ │ ┌─┘───┘───┘
                      │░░░│ │░░░ │  │ │
                      └───┘─┘────   └─┘












```

*Figure from page 10 (2346x3317 px)*


---



4203-E P-337



SECTION 3 DATA INPUT/OUTPUT OPERATION



3-3. Tape Format



3-3-1. Input Format



(1) ISO Coding System



rape file name-i (d) Program s;;ction



(,__--_---...__I



$-Filen _ame



_....__l---__._-l~...._l ~,.. .......



~ I



_o Pro_gram_name.........._l



..,..~..... .


# I..____,\

\~-'~Pro_g,am_end .........



~,-~I. _. ,--_--_---_-~



"'1- Program Start block--/ /-Program end block +-tJ- Feed holes -



(e) \



(b) Feed ho/ ""



(c) Tape start Program start



Tape end



Fig. 3-3 Input Format {ISO Coding System)



(2) EIA Coding System



(d) Program s;;ction

- Feed holes_j



(a) -,



Program start block-,



(b) Fe;d holes'/ • '



Program end block..k+- Feed holes - r-



(e) '\;



(c) Tape start



Tape end



Fig. 3-4 Input Format (EIA Coding System)



(a) Feed holes (in ISO coding: NUL or SPACE, in EIA coding: BLANK or SPACE)



(b) Input the file name after the "$" symbol.



If no file name is specified, the same file name as that specified for the output NC program name



will be automatically selected. If no output NC program name is specified, the name set will be



"A.MIN".



(c) Feed holes



(d) Start and end the program section with the% (ER} code.



(e) Always include M02 or M30, or END, or RTS in the program end block.



[Supplement] Codes that cannot be set in the EIA coding system can be replaced by codes that can be



set so that they can be read. For details, see Section 6, 3-3-3, "EIA Special Codes".


```text


                                                                                                ───
                                                                ┌─┐─────┐─┐─┐───┐─┐─┐─┐─┐─┐──── ░░░───────░┌─
                                                                │░│░░░░░│ │ │░░░│ │▒│░│ │░│ ░░  ───░░░░░░░─┘
               ────           ── ───────────────────────────────┘─┘─────┘─┘ └───┘─┘─┘─┘─┘─┘─────      ──
           ┌───    ───────────  •                                                                           │
           │░ ░┌───░     ░       ┌──────────────────────────────────────────────────────────────────────────┘
           │   │   │ ░         ░┌┘
           │   │   └┐          ─┘
           └── │    │░       │
              •   ┌─ ──     ─┘──────────┐
                  │ │  │░    ░░ ░ ░░░░░░│
                  └─┘  └─   ────────────
                          ┌─                                  • ──────┐
                    ┌───┐─┘ ░ ░    ┌─┐──┐─┐─    ─────────── ┌─ •      └──────┐─────────  ────┐─────────┐
                  ┌─┘   │░       ┌─┘░│  │░│ ───┐           ─┘   ┌───┐ │      │          •   ░│         │
                 ─┘     │░│░│   ┌┘ │░└──┘░ │░░░│     ┌──  ░ ░│ ░│   │░ ────┐░│       ┌─ ░ ┌─░│         │
                  ░     │░│ └───┘┘─┘░│  │░ │░░░│     │    •░░│ ░│    ──    │░│       │░── │░░└────     │
                ─┐ ┌────┘ │        │ └─ │   •░  │    │          │          │░             ░ ░│         │
                 │░│     ─┘ ──── ──┘   • ░░│ •░░│ ──░         ──┘────  ────┘─ ░░ │       •░░░└─     ───┘
                ─┘─┘─────       │░ └──  ░┌─┘  ──    ── •  ────               ────┘─────── ───┘  • ──
                               ┌┘     ┌┐─┘            │ ──                                    ── •
                               │      └┘             ░│   •                                 •     │
                               └──────┘                                                      ─────┘
                                            ┌─────┐─┐──────────────┐─┐─┐──┐─┐──────┐
                                            │ ░ ░ │ │░ ░ ░ ░░ ░ ░░░│ │ │░░│ │░░░░ ░│
                  ┌─┐ ┌───────────┐─────┐   └─────┘─┘──────────────┘─┘─┘──┘─┘──────┘
                  │░│ │░░░ ░░░░ ░ │░░░░░│
                  └─┘ └───────────┘─────
                                        ┌┐                 ┌────┐─────┐   ┌───────────────┐─┐
                     ──┐─┐─────────────┐┘┘                 │   ░│     │   │               │░│
                  │    │ │             │                     ───┘──   └───┘┐                └───────
                  │░│  │░│      ┌─┐░│   ──┐─┐            ┌─┐        ┌─┘    └─┐────────┐────┐        ┌─┐
                  │░└──┘░│      │ │░└──┐▒░│▒│            │▒│        │░│    │░│  ░     │▒░░▒│        │░│
              ┌─ ─┘    │ │        │ │  │░ └─┘            │░│        └─┘    │░└─ ───── └────┘ ───── ─┘─┘
              │        │░└──────  │░└──┘░ ░ ░                ───────  └────┘                │     •   │
              └────────┘─┘       ─┘ │  │░┌────── │      │ • •              │░ ░│        │░░░│ •    │   │
                                │   └─  ┌┘      ─┘──────┘                  └───┘────────┘┐── • ────┘───┘
                                └──░  ──┘                                                │░   │
                                   ───                                                   └────┘
                                           ┌──┐─────┐─────────────────┐───────────┐
                                           │░░│ ░ ░ │░░  ░ ░░ ░ ░░░░  │░ ░  ░░░░ ░│
                    ┌─┐─┐────────────┐─┐─┐─┘  │ │   └──┐─     ───    ─┘            ─────────
                    │░│ │░░░ ░ ░░  ░ │░│ │░░░ │ │░   ░ │░░░░░    ░ ░   ░    ░ ░░░│   ░░░  ░
                    │ │ │             ─┼─┘ ┌─   │ │    └─────────────────────────┘──────────
                    │ │ │    ░  ░      │ └─┘ • │ ░│   •
                    └─  │              └─┘ └─  └─  ┌──   ────── ─┐────────────────┐─┐─  ─┐  ──┐ ── ── ─┐─ •
                       ┌┘ ░ ░░  ░░░░ ░ ░░░░░░░  ░│ │░░  ░░   ░░• │  ░░   ░  ░░░   │░│ ──░└──░░└─  •  │ │ • │
                       │ ░      ───     ┌─┐──    └─┘────┐                         │   ░ ░            │ │   │
                       │    ░  •   ─────┘ │   •  │      └┐░•  ────  │ ─── •   •       •░─── │ │░│ • ░│ └┐ ░│
                       └────░•           ─┘─── ──        └─ •     ──┘─     ─── ─────── •   ─┘─┘─┘─ ──┘─┘┘──
                    ┌─┐┘       ──┐
                    │ │ │░░│ ░░░░│
                    └─┘ └──┘    ─┘────────────┐─┐──────┐─┐──┐───┐──┐─┐───┐
                    │░│ │░░│ ░░░ ░░░░░░ ░ ░░░░│ │░░░░  │░│ ░│ ░ │░░│ │░░░│
                    │ │ │  └─ ─┐      ── ─── ─┘┐┘┐─     ─┘─  •  └─   └─── ───────────┐
                    │░│ │░░░░│ │ ░░░░•░░•   •░░│ │   ░┌┐   •░░░   ░               ░  │
                 ───  │ └───┐┘─┘─     │      ──┘   ─┐ └┘     ┌─                       │
                 ░░   ░     │     ─── └──────    ─┐ │░   ────┘ •     • •        ──────┘──────┐─────────   ─┐
                 ───────────┘    │   │       │ ┌─ │             ──    │    ────          ░   │         ──  │
                                 └┐ ░│ │░░  ░│ │░│    ░░ ┌──   │░░░░• │░░ ░░░░░░ ─────────   │░░░ ░ • ░░░┌─┘
                                  └──┘─┘─────┘─┘─┘───────┘  ───┘──── ─┘──────────         ─── ────── ────┘





















```

*Figure from page 11 (2346x3317 px)*


---



4203-E P-338



SECTION 3 DATA INPUT/OUTPUT OPERATION



3-3-2. Output Format



(1) ISO Code



Feed hofes File name Feed holes Part program Feed holes



(a) (b) (c) (d) (e) (t)



Fig. 3-5 Output Format (ISO Code)



(2) EIA Code



..__?---___._--,_ $fllenam_e


#### L--...Jl----1--L...L~,~,

_OProgra-mname .J.::..1-IRI _---J?....__{ ---1...IR...L...------_---- .



Feed holes File name Feed holes Part program Feed holes



(a) (b) {c) (d) (e) (t)



Fig. 3-6 Output Format (EIA Code) (1)



(a) 600 tape feed holes are punched in the tape leader section.



The number of feed holes to be punched out can range, as needed, from 1 to 10000 with a



parameter.



For details, consult III, "PARAMETERS".



(b) The file name is punched out following the"$" code. (Program data is punched out in the ISO



coding system.)



(c) 50 tape feed holes are punched out.



The number of the tape feed holes cannot be changed.



(d) Either of the following is punched out.



%, CR, and LF



ER and EOB



{e) The part program data is punched out following the program name (number).



(f) The same number of tape feed holes as in a} are punched out in the tape trailing sectlon.


```text


                                                                                               ───       •
                                                               ┌─┐───┐─┐───┐───┐─┐─────┐────── ░░░───────░─┐
                                                               │░│░░ │░│ ░ │░░░│ │░░░░ │░ ░░░  ───░░░░░░░•░│
               ───              ───────────────────────────────┘─┘───┘─┘── └───┘─┘─────┘───────     ───
          ┌────   ┌───┐─────────                                                                           │
          │    ───┘  ░│  ░      ───────────────────────────────────────────────────────────────────────────┘
          └────    ──         ┌─
                 │   •        │
                 └──  ────────┘
                │   ──         •
                └─┐     ┌──         ─┐──                        ──────────────  ─────── ──    ─────────
                │░│     │░          ░│  ┌───┐────┐─┐─────┐──┐──               ──       │░ ┌──┐         │
                │ └─────┘  •      ─┐░│  │░▒░│ ░░░│ │     │░ │░░───────────   •░░───    │░ │░░└── ──────┘
                │░      ░   ── ──  │░│  └───┘──┐─┼─┘─────┘──┘──           ─── ──   ──  └──┘──          │
                │ ── •   │ │  •    │ └──┘      │ │                ───┐──┐                    ┌─────────┘
                 │░░░░│ ░│ │░░░░│  │░░░░░░│ │  │░│                ░░░│░░│   •              │░│ ░░░░░░  │
                 └────┘──┘─┘────┘──┘──────┘─┘ ─┘─┘───────────────────┘──┘─── ──────────────┘─┘─────────┘
                                            └─
                                               ──  ────              ── •
                                                 │        •       •    │  ───┐
                                               ──┘ ───────  ────── ────┘──   │
                 ┌─┐ ┌─────────                   •                         •
                 │ │ │       ░
                 │  ─┘         ───── • ──                     ─────────────────  ────────     ─────────┐
                 │░      • ────     │░│   ┌───             • •                 ──          •           │
                │  ─────         ─┐─┘░│   │░░░•           │░• ───── ──────────   │     ── •░•          │
                │░│     │ │       │ │░│ • │░░░▒•          │░░│                │  └─────  •░░░   ───────┘
                │ └───┐ │░│ ┌────   │░└─ │░┌─┐─  ───────  └──┘    ┌──┐──┐     └──         ───┐         │
                │     │ │ │ │    │  │    │░│ │░│                  │  │  │                    │ │    │  │
                └──  ┌┘ │░│ └─┐  │  │░│  │░  │░│                  └─   ┌┘                  │░│ │ ┌──┘   │
                   ──┘ ─┘─┘─  └──┘──┘─┘── ───┘─┘──────────────────  ───┘ ──────────────────┘─┘─┘─┘   ───┘

                                             ──  ──── ───  ──────┐──── ┌───┐ ──┐
                                            •  ──  ░ │   •       │     │   │   │
                                                  ┌┐ │       ──  │  •     ─┘───┘
                   ┌── ┌─┐─┐─── ───────┐──────  ──┘┼─     ───  •  •  ┌───
                   │   │ │ │   •       │ ░         │   ─── ░   ░░ ░│ │░  ┌─               •
                   └─ ─┼─┘     ░ │   │       ┌─ ┌─┐┘       ┌─   ─┐ └─┘   │ ─── ─────┐ ┌──┐ │  │ ┌───┐─┐─┐──┐
                       │ └───── ─┘───┘───────┘ ─┘ └┘───────┘ ─── │ │ │  ░│          │ │  └─┘  │ │   │ │ │  │
                      │░░ ░ ░░░│                                  ─┘  ───┘─ •  ───── • ──        ─── ─┘─ ──┘
                      └┐──┐─ ──┘  ────────┐ ───────   ────
                       │  │               │       ░───
                   ───      │             └─              ─┐───────┐─┐───┐─────┐─┐───┐────────┐─┐──┐─────┐
                         ──░└─────     ░ ░ ░     ░░ ░░░░░░ │ ░  ░ ░│ │░  │░░░░ │░│ ░ │ ░░░░░  │░│  │░ ░░ │
                       ──░░░ ░░░░░───  •  ───      •  ─────┘── ────┘─┘───┘─────┘─┘───┘────────┘─┘──┘─────┘
                   ┌─┐─              ─┐ ─┐   ─────┐ ──
                   │░│ │░ ░░• •░░░ •░░│ ░│ ░  ░░░░│ ░░•
                   └─┘─┘  ── │      ── ──┘      • └─ • ────────────┐──┐
                       │░│ ░ │░░░ ░ ░ ░ ░░│ ░░░░ •░░• •░░░ ░░░   ░░│░░│
                   ┌─┐─┘ └─ │            ─┘            ┌───────────┘──┘
                   │░│ │░░░ │░ ░░ ░░░░░ ░    ░░ ░░░│ ░░│
                   └─┘─┘────┘┐            ┌────────┘───┘
                             └─┐ ░░  ┌── ░│
                             │ │     │  ┌─┘
                            │  │ ░░░ └──┘
                   ┌─┐ ┌────┘       •   └┐────┐───────┐───────────┐───┐───┐─┐───┐─┐──────┐
                   │ │ │ ░  ░  ░ ░░ ░│ │░│ ░ ░│  ░░░  │░ ░░ ░░░░ ░│   │░░░│ │░░░│ │   ░░░│
                   │ │ │   ┌───      │ │  ──┐  ──   ── •      •    ───   ┌┘  ───┘─  ──┐─ └──────────┐
                   │░│ │ ░ │░ ░ ░ ░░░░ │░ ░░│ │░░│ │░░│ │░ ░ ░ │ ░ ░░ ░ ░│ ░│   ░  │░░│ │░░░░░ ░░░░░│
                   └─┘─┘───┘───────────┘────┘─┘──┘─┘──┘─┘──────┘─────────┘──┘──────┘──┘─┘───────────┘






















```

*Figure from page 12 (2346x3317 px)*


---



4203-E P-339



SECTION 3 DATA INPUT/OUTPUT OPERATION



[Supplement] 1. When the program data is punched out in the EIA code, the presence of a code not



available in the EIA coding system causes an error. Tape punching-out halts and



an error message is given on the display screen.



When the tape delimiting code is the "%" (ER) code, i.e., when bit 3 of parameter



No. 1 of NC optional parameter (bit) is 1, the"%" code or "ER" is punched out before



feed holes.


## 2. The part program is split and punched out, if it si

too



long to be contained in one



paper tape roll. Paper tape length may be changed from 1 to 300 meters (3 to 984



feed) using the NC optional parameter (word) No. 2.



As the format, the file name is also punched out, for the second tape and so on.



Since the tape ends with "CR" or "LF'', actual tape length is somewhat difference



from the tape length set using the parameter.



When designating paper tape punch out operation on more than one paper taper



roll, specify option D in the following format:



<file-name>, <device-name>:;D



0 0 0


# $A.MIN

0000 00



o/o~Hf)o*"'** . \ \ ..



000000 1st tape



File I Feed



Feed I



.Feed holes ~-name,



?Oles



Tape length for parameter setting. holes .



. { ·.___-_®_~_-_···._ ,,_·__.I 2nd tape



\ \ \f.)



'------------------



~ ~



0 C



$A.MIN



Machining program



Fig. 3-7 Output Format (EIA Code) (2)



3-3-3. EIA Special Codes



(1) There are some characters, such as"=" and"*"· that are not represented by codes in the EIA



coding system. To make it possible to use these characters when creating an EIA program



tape, other characters are sometfmes temporarily substituted for them.



(2) When a program tape created in this way is read into the NC, the substituted characters must



be converted back to "=" and "*" by using editing functions.



(3) This troublesome procedure is made easier by setting EIA special codes for the characters for



which substitution is necessary in advance; the control then automatically substitutes the



appropriate characters when a program is input from or output to tape.



{a) Setting the EIA special codes



1) Special codes can be set for the following 6 characters:



=, *· [, ), $, #


```text


                                                                                                • •
                                                                ┌───────┐─┐─┐─────┐───┐─┐─┐─────░░░────────░│
                                                                │░ ░ ░░░│ │ │░░░░ │░ ░│ │░│ ░░░░───░░░░░░░░─┘
           ┌─────            ────────    ──  ──────  •    ───── └──  ───┘   │  ── └───┘─┘─┘────       ──
           │     ┌───────────        ┌───  ──      ── ────         ──    ───┼──  •             ─┐           │
           └─────┘           ┌───┐── │░░   ░                                │                   │           │
                 └───────────┘   │   │   ──     •░ ░     ───────        ── •   ┌─  │░───       ─┘  •  ──┐── │
                                     │░░░░░░░   ░░ ░ ░ ░░░░░░ ░░░░░  ░░░░░ ░  ░│░──┘─░░░    ░░░░░  ░  ░░│ ░░│
                                     └─────────────────────────────┐░──────────┘─    ───   ──  ──  •  ──┘
                                     │                             │             •      ───  ┌┐  ── ──   ───
                                     └─░░───── ░░──░░░░░░░─────░ ──┘░ ────░░░│  │░┌──░──░░░• └┘ ░ ░ ░░░░░░░░│
                                     │░──  ░░░░──░  ────░•  ░░ • ░░ •   ░ ───┘─ │░│   ░ ░•        •  ──  ░• │
                                     │        •   •     •  ───  ────    ──       • •  ─── •    • •     ───
                                     │ ┌──
                                 ──  │ │       • ───    •    •     •   • •           ────         ────
                                     └─┘─────── •░░░────░────░────┐░──┐ •░───────────░░░ ──────░──░ ░░───────
                                     │░░░░ ░░░   ░ ░░░░░ ░░░░ ░░░░│ ░░│ ░░ ░░░░░░░ ░░░───░ ░░░ •░░────░░ ░░░
                                     └──── ───  ─┐ ┌──────────────┘───┼── ──┐───── ──    ── ──  ──    ─────
                                     │           │ │                  │     │
                                     │░ ░ ░ ░ ░ ─┘ │░ ░•  ░  ░ │ ░░  ░   ░░─┘─── ░  ░ │ •      ───  ┌── • ─┐
                                     └─    •     │        ┌──  │ ──                   │         ░   │░     └┐
                                     │ •  │ │ •  └────┐   │    │    ─────   ░   • │  ░│      •░░  │ │ •     │
                                     │ ░│ │░│░░┌─ ░ ░░└──░│ ░── ░ ░ ░░ ░░────     └──         •  ─┘    •    │
                                     │  │    │ │         •      │             ──┐─   ┌──┐─┐──┐ ──  ┌──┐ ┌───┘
                                     │  ░ ───┘░░ ───┐──░░░──░░──┘░───────┐░░░ ░░│    │░░│ │░░│ ░░ ░│░░│ │░░░│
                                     └───░░░░░───░░░│ ░───░░──░░ •░░░ ░ ░└──────┘────┘──┘─┘──┘─────┘──┘─┘───┘
                                          •                           •
                                       │ •   •░│ ░░ ░   │░░ ░░  ░░ ░  ░──
                                     • │      ─┘        └────                                  ─────
                                    │░│         ──────         ──┐───┐────             ┌─┐───       ┌─┐──────
                                    │░└────────  ░ ░░░        •░ │░░░│    ────         │░│░░        │░│░ ░░░
                                    │░│        • •              ┌┘───┘                 └─┘──       ─┘─┼──────
                                    │  ────────   ┌───┐ ┌────── │     ──┐──┐─┐──────┐─┐┘      ┌───┐   │
                                       ░░  ░ ░  • │░░░│ │░░░░   │░░│ │░░│ ░│ │░ ░ ░░│ │░░░░   │░░░│   │
                                     ───────────░─┘───┘─┘─────░─┘──┘─┘──┘──┘─┘──────┘─┘───────┘───┘ ──
                                                •
                                    ┌─┐                                                              ┌┐
                                    │░└──  ───┐─────┐──                                 ────┐ ──────┐┘┼─┐─┐──┐
                                    │░│       │░░░░░│                                  │░░ ░│       │░│░│ │░░│
                                    │░└─      └─────┘── ────┐─┐─────            │      └────┘    ─── ░└─┘─┘──┘
                                    └─┘                     │ │      ┌──────────┘────┐       │       •
                                       ─────────────────────┘ │      │░░░░░░░░ ░░░ ░░│     │ └──────
                                                            │ │      └───────────────┘     │ │
                                              ────┐─┐─┐─┐─┐─┘ └───┐──                 ───── •
                                                ░ │ │ │ │░│░ ░  ░░│ ░ ░   │░│ │░│
           ┌────┐  ┌───┐─┐───────┐─┐          ────┘─┘─┘─┘─┘───────┘───────┘─┘─┘─┘
           │░░ ░│  │░░ │░│░░░░ ░ │░│
           └────┘ │ ┌──┘      │ │   ─────────── ┌── ─┐┐┐─ ┌──┐ • ─┐─────┐────┐───────────┐─ ───┐─────────┐
                  │ │  └──────┘─┘░░░░ ░░░░░░░ ░─┘░░• └┘┘ ┌┘░ └─ • │░░  ░│  ░ │░░░░░░░░░░ │ •  ░│ ░ ░    ░│
                  └─┘            • ┌─┐─── ░───           │  •      │            •           ░  │  │   ┌──┘
                       ┌─          │ │        ┌─  •  • ──┘ •     │ └────  ─┐     ──         ───   │░ ░│
                       │░─────── •░░ ░░░░┌─░• │░──░──░░░ ░│░░░───┘─┘░░░░──░│ ───░ ░•
                  ┌─┐  │              │  │ •            │ │        │       │         ────┐─┐─┐─────┐──┐──┐
                  │░│  │░ ░──────░ ░──┘░░░ ░░░░░░   │░░ │░└───────░ ────░ ░░ │░│ │ ░░░░░░│ │░│ ░░░░│ ░│ ░│
                  └─┼─ └───░ ░░░░───░░░─────────────┼─┐░░•░  ░░░░░──░░░ ─────┘─┘─┘───────┘─┘─┘─────┘──┘──┘
                  │ │ •                             │ │
                  │░│  ┌─────┐───┐───────┐────  • ──┘─┘ ┌───┐     ───────┐──    •  •      │ •     ──     │
                  └─┘  │     │   │       │       •    │ │   │    •       │        •      ─┘  ──     │ ───┘
                       └─   ─┘  ░    ────   ░ ░ ░░──┐░  ░  ░   ░   ░░ ░ ░░──░   ░░░ ░░  ░ ░░░░░░░  ░└─
                       │░───░░──┐────░░░░─────────░ │░░░─── ░ ░░ ░ ────── ░░░──░•░──────────────────┘
                    ┌─ │        │                 ──┘───   ────────      ────  • •
                    │░│ │░░░ ░ ░│ ░░░ ░░░░░░ ░░░░•
                    └─┘┐┘┐─┐                      ─┐──┐─┐────┐──┐───────────┐
                       │ │ │░░░░░░ ░░░░  ░░•░│ ░░ ░│ ░│ │░░ ░│ ░│  ░░░░░░░░░│
                       └─┘─┘──────────────┐░ └─────┘──┘─┘────┘──┘───────────┘
                                          └─
















```

*Figure from page 13 (2346x3317 px)*


---



4203-E P-340



SECTION 3 DATA INPUT/OUTPUT OPERATION



2) Special codes are set as bit patterns in NC optional parameters (bit) No. 27 through 31



and No. 49.



Example: Suppose the puncher key



[Supplement]



"[ ]" is determined for punching the "=" code, and



that the arrangement of punched holes by this key operation is as below.



8 7 6 5 4 3 2 1 Channel



0 00



Feed holes



Set this arrangement of punched holes by a "1" and a "O", where "1" indicating a



punched hole and "O" a position not punched. Setting will be as below:



01011011



Set this at the No. 27 of NC optional parameter (bit). Repeating the same



operations, set all the codes used on the NC.


## 1. When inputtlng a program in the EIA coding system, if the special code"$" is input

at the head of the program, the character string immediately following the "$" is



read as the file name {in EIA codes) for the program.


## 2. When outputting a program using the EIA coding system, if the "$" special code is

set the file name will be punched out in EIA codes. If the"$" special code is not set,



the file name will be punched out in ISO codes.


## 3. There is no check to determine whether or not the bit patterns assigned to special

codes already represent characters in the EIA coding system.



Example: If the special code for the character "=" is set as 01100001 (the EIA



code for "A") and "A=B" is output for punching, what will actually be



punched is "AAB". When the tape is read, the data will be



interpreted as "==B".


## 4. Special codes are only converted when commands are executed ln the PIP mode.

They are not converted in the ONG mode.



3-4. Specifications



3-4-1. RS232C Interface



(1) Communication Method



Start-stop synchronization



This is a method in which a pre-determined signal is sent at the beginning and end of a character.



The data for each character comprises the following bits (see Fig. 6-8): (A) start bit (1 bit), (B)



information bits (8 bits), (C} parity bit (1 bit), (D) stop bit (2 bits).


#### LSB MSB

7 1-


# I ·---1

1----



------1



1s -1I ,_.___:


#### L-..J ______________ __.1...-,1.___ _. .,

(A) (8) (C) (D)



Fig. 3-8 Bit Configuration


```text


                                                                                               • •
                                                               ┌─┐─────┐───┐─────┐─┐─┐─┐─┐──── ░░░─────────┐
                                                               │░│░░░░░│ ░ │░░░░ │▒│░│ │░│░░░░ ─── ░░░░░░░░│
          ┌────────────────           ── ────────  ──   ─────  └─┘─  ──┘   └─────┘─┘─┘ └─┘─────       •
          │                ────     ──  •        ┌─  ┌──     ──    ──   ───           •        •           │
          └────────────┐┐ │    ─┐ ┌─  │  │       │   │         │ │                     │ │  │      │   ────┘
                       └┘ │ ░░ ░│ │░ ─┘ ─┘      ─┘───┘───     ─┘─┘───     ░   ─────────┘─┘ ─┘──── ░│ ──
                          └──   └─┘ •                                                                   ──┐
                             ─┐░░░░░░│  │░───░░░─┐───────░┌─┐░────────░░░░ ░ ░░─────┐ ────── ───────────░ │
                              └──────┘  └─░ ░── ░│░░ ░░░░─┘ └─░ ░░░   ─────────   ░ │  ░  ░ •       ░░ ░┌─┘
                                           •      ───────  •  ──────┐          ───── • • ───  ──────────┘
                                                                    │
                                                      ┌─  │   ░    ░│ •░• ░ ░   │ ░  ░│
                                                      │░ ─┘┐           •        └─────┘
                                                      │░│  └─   ──── ─┐ ─────┐ │
                                                      │░│  │ │ │      │  ░  ░│░│
                                                      │░└──  └─┘   ───       │░└────
                                                      │░│                 ── └─┘    ───────┐
                                                      └─┘                   •   •     ░   ░│
                                                                                         │     •
                                        ───────────────────────────┐───────────┐─┐────── └───── ───────────
                                       •       ░  ░░░  ░ ░░     ░░░│   ░░  ░░  │ │  ░    ░░░░      ░░    ░
                                        ───┐     ──── ┌────────────┘───────────┘─┘─────  ─────── ───────────
                                       •   │░ ░       │                                •
                                        ┌─┐┘           │    ┌─┐─┐─ ──────────────── ───  ──────────── ─┐───┐
                                        │░│  ░┌─░   ░ ░└─── │ │ │ •░ ░  ░ ░░ ░░░    ░       ░░░░ ░     │░ ░│
                ┌─                     ─┘─┘───┘ ──────░│  ░ │  ░│ ░░── ░────────┐            ──      • └─ ─┘
                │ ──────────        ┌──       │                                 │ ──      •     • │ │ •  •
                └─         ░•       │  ── ───   ──── ──┐───   ┌─ ───────┐─┐─┐───┘─░ ─────░ ░────░─┘░│   ░  │
                  ────────          │  ░░ ░░░  ░  ░░ ░░│░░░   │░ ░░░ ░░░│ │░│ ░ ░░ ░░░░░░───░░░░░░░ ░░─────┘
                                    └──────────────────┘────░─┘─░░──────┘─┘─┘────────────   ──────────
                               ┌─┐  │                                                                      │
                               │░│  └────────────┐───────┐─────── ───┐───────   ──   ───░   ░│ •    • ───  │
                               └─┘  │            │       │           │          ░         ── │       •   • │
                                    │░        ░    ░   ░  ──        ┌┘      ░░┌───┐░ ───░ ░░░░ ░░░   ░ ░░░─┘
                                    └───────────┐─────┐───░░────────┘░────────┘   │     ──     ────
                               ┌─┐ •            │     │                       └─┐┐ ────┐  ─────    ──┐─────┐
                               │░│  ┌─░─┐ ──────░░────┘░░░ •░░───░░░░░───────░░ └┘  ░░░│ ░ ░░░░ ░░ ░ │░░░░░│
                               └─┘  │ •░│ ░    ░──     ────░──  ░─────     ░ •      ┌─   ──────   •  └─   ─┘
                                    │    •   ─┐                                  │  │           •      ──
                                   •░░░░░░░┌─ │░──┐──░░░── ┌─░░ ───░──┐──────┐───┘──┘─┐░░───░░──░───── ░░│
                                    ───────┘  │ ░░│ ░░•░░  │ ░── ░░ ░ │ ░░░ ░│ ░░░░░░░│  ░░░ ░░░ ░░░░░───┘
                                              │░░░░░░│ ░  ░░░│  │░•░ •░░───░░│░──░░──┐┘ │ ░─────░┌────
                                               ───┐─┐┘── ────┘░░└─    ──   ──    ──  └┘─┘──     ─┘
                               ┌─┐ ┌───────────   │ │              ──┐        ──                  ──┐──────
                               │░│ │░░░░░░  ░░░│ ─┘ └─░    ░░░░░• •░░│         ░ ░       ░     ░  ░░│    ░
                               └─┘  │   • • ─┐─┘      ──         • • └──┐───────────────────────────┘──────
                                    │░░│ │░  │░ ░░░│░ ░░ ░ │░│ │░░│ │░░░│
          ┌───┐  ┌─────┐────────┐   └──┘─┘───┘─────┘───────┘─┘─┘──┘─┘───┘
          │░ ░│  │▒░░░░│░░░░░░ ░│
          │ ┌─┘┐  │    └─┐─┐─   └─┐
          │ │  │  │░░░░░░│ │░░░░ ░│
          └─┘──┘ • ┌─┐───┘  ───   └─┐─────
                   │ │          • │ │░ ░
                 ──┘  ──┐      │  └─    ────┐
                     │░░│  ░ ░ │░░░░  ░░░░░░│
                     └─ │       •             ───  ──   ─────       ┌─  ──   • ─────  • •   ─── ──────────
                       ─┘ ──────  ────────────░ ░── ░─── ░░  ─────┐─┘░─┐ ░──┐ │░░░░░─┐ │░│ │ ░ │ ░ ░░░░░░░│
                     ─┐░░ ░░░  ░  ░░░  ░ ░░░░░  ░  ░░░░░  ░│ ░░░░░│ │ ░│  ░░│ │░────░└─┘─┘ └── └┐────░───░│
                      └── ───── ░░░•░ ░░──────  ░░ ──────┐░│ ────░│  ░•   ░░└─ •    ─┘        ─┘┘    •   ─┘
                         •     ──── ────      ─────      └─┘     ─┘─── ─────
                                        ─────                                 ─┐─
                                  ─┐  ┌─░░░░ │  ┌─┐  ┌─┐─────  ─┐   ─┐──┐───░ ░│ ─────┐─┐──┐─┐───┐─┐
                             ────┐░│  │░ ──┐░│  │░│ ─┘░│   ░ ──░│ ─┐░│  │░   ┌─┘   ░  │░│  │░│   │░│
                                 │░│  │░│░ └─┘  │░│ ░└─┘░ ┌┐ ░ ░│ ░│░│  │░│  │░│ │ ┌──┘─┘──┼─┼───  │
                                 │░│  └─┘  │░│  └─┘  │░│  └┘  │░│  │░│  └─┘  └─┘─┘ │       │ │   ┌─┘
                                 │  ──┘░│  │░│  │░│  │░│  │   │░    ░   │░│   ░  │░└──    ─┘ │   │░│
                                  •    ░│   ─┘  └─┘──┘─┘──┘   └─────────┘─┘────    │   ───   │   └─┘
                                   ─┐░┌─ ──   ──          └─┐─                 ─┐ ┌┘── ░░ ───
                                    └─┘                     │                   └─┘    ───
                                                  ┌──┐─┐────┼─┐──────────┐
                                                  │░░│ │ ░ ░│ │░ ░░░░░░░░│
                                                  └──┘─┘────┘─┘──────────┘









```

*Figure from page 14 (2346x3317 px)*


---



4203-E P-341



SECTION 3 DATA INPUT/OUTPUT OPERATION



(2) Baud Rate (BPS - baud)



110,150,200,300,600, 1200,2400,4800,9600, 19200



(3) Data Configuration



Start bit 1 bit



Data bits 8 bits



Parity bit 1 bit or absent (selected by parameter setting)



Stop bits 1 bit or 2 bits (selected by parameter setting)



(4) Parity Check {character parity)



Odd/even parity or no parity check (selected by parameter setting)



(5) Signal Descriptions



Signal



Direction Details



Name



Protective grounding



TXD Output Send data



Data line from the NC to peripheral devices.


#### RXD Input Send data

Data line from peripheral device to the NC.



RTS Output Request to send



Comes ON when data transmission or reception starts.



Thereafter, it is normally ON.



CTS Input Clear to send



When this signal is OFF, data is not output from the NC.



Used for BUSY/READY control.



If this signal is not used, connect the RTS signal at the NC.



DSR Input Data set ready



Indicates that the peripheral device is in the communication en-



abled status.



If this signal goes OFF during data communication, an error will



occur at the NC.



This signal cannot be used to execute BUSY/READY control.



If this signal is not used, connect it to DTR at the NC side.



SG Connection for signals



RG1 Output Data request (register 1)



This signal is used to execute receive BUSY control at the NC side.



It comes ON when the NC is in the reception enabled status and data



transfer from a peripheral device is requested.



It goes OFF on reception of a start bit from the peripheral device (it



goes OFF once per character).


#### RG1__j\J

High



Low



(output) I


# RXD Fl R High

(input)



Low


# I I

Start bit Stop bit



RG2 Output Register 2



Presently not used.


```text


                                                                                                ───
                                                                ┌─────┐─┐───┐───┐─┐─────┐───────░░░──────────
                                                                │░░░░░│░│ ░ │░░░│ │░░░░ │░  ░░░░───░░░░░ ░░░
           ┌──────   •    •           ──  ── ───────────────────┘─────┘─┘─ ─┘───┘─┘─────┘───────     ───
           │      ┌─┐  ─── ────┐─┐────  ──  •                                                               │
           └──────┘ │ •░       │ │░                                      ───────────────────────────────────┘
                  └─┘  │    │   •    ───┐ •   ───┐─┐──┐─┐───┐────┐─┐────┐
                       │ ─┐ └── ░░• ░░░ │░░│  ░░░│ │░░│ │░░░│ ░░░│ │ ░░░│
                  ┌─┐  │  │ │  •    •  │ ──┘ ────┘─┘──┘─┘───┘────┘─┘────┘
                  │░│ │░░░│ │ •░░░ │░│░│
                  └─┘ │   │    ────┘─┘─┘   •
                       ┌──┼───           ┌─ ──┐
                       │  │   │          │   ░│
                      │       │          │    └────────┐────────────────────┐─────┐
                      │░░░░░ ░│          │  ░ ░  ░░░░░ │░░░░░░░ ░ ░░░░░░░░░ │░░░░░│
                       • ──── │            ────  ── ┌─  ───  •  ─┐       ┌─ └──  ┌┘
                  ┌─┐ │       └──┐─ ──────         ─┘ •     • ── │       │      ┌┘
                  │░│ │░  ░│     │ │      •     •                               │
                  └─┘  ┌───┼──   └─┘        ──   ───┐─┐──┐───┐────────┐──┐─┐──── │
                       │░░░│░░│ ░│░│░────░ ░░░░ ░░░ │ │░░│░░░│    ░░░ │░░│ │░░░  │
                  ┌─┐ │       │          ───────────┘─┘──┘───┘────────┘──┘─┘─────┘
                  │░│ │░░░ ░ •░░░░░░░░ ░•
                  └─┘ │ •      ──         ┌─┐───────────────────────────        ───────────────────────────┐─
                      │  ┌────┐  ┌───────┐┘░│                           ──────┐                            │░│
                     │   │░░ ░│  │ ░ ░░░░│  │                            ░░░░░│                       ─────┘░│
                     │ │ └┐─░┌┘ │      ──┘─┐┘────── ───┐──────┐         ──────┘                            │░│
                     │ │  │ ░│  │  ┌───    │░ ░░░░░•░ ░│  ░░ ░│                                            │░│
                     │ │  │░░│  │░ │░░░░░│ │░░░░ ░░░░┌─┘────                                               │░│
                     │ │     │  │  │   ──┘ │  │░     │      ─────────┐───────────────┐                     │░│
                     │ │  ───┘  │   ┌──    └──┘░░┌──░│   ░  ░░ ░░░░░░│░░░░░░░░░░░░░░░│                     │░│
                     │ └─ ░░░│  │ ──┘░░░• │ ░░░░─┘░░░│      │        │      •   •   ┌┘───────────    ───── │░│
                     │░│  │  │  └─        │░       • └──────┘░ ────── • ── • ─── ── │            ────     ─┘ │
                     │░│  │  │  │  ┌───── │░───              ──░       •  •       ░░                       │░│
                     │░└─ └──┘──┼──┘░░░░░ │  ░░░░───┐ •░░░•                          ───┐─┐──── ───────────┘ │
                     │░│        │  └───── │ ────░░░░│ ░░• ░────────────┐░░░░░│ ░ │░░░░░░│ │░░░░•           │░│
                     │░└─  ─────┘┐        │     ░──┐┘──┐ │        ░   ░└─────┘ ──┘──────┘─┘──── ───────────┘░│
                     │░│   ░     │  ────  │░ ──    │   │ └────────── ┌─┘                                   │░│
                     │ └───────┐─┼─ ░░░░ ─┼─  ░░─── ░░─┘┐            │     ─┐───┐─┐──┐───┐─┐───┐───────────┘░│
                     │ │       │ │  ────  │ ┌─┐░░░░  ░░ └─────────── │░──── │░ ░│░│░ │░░ │░│ ░░│           │░│
                     │░│       │ │        │ │ │   ┌─┐─ ░ ░░  ░░ ░ ░  └─                                    │ │
                     └─┼─      └─┼─      ─┘ │ │░ ░│ │                    ─┐───────────────────────┐ ───────┘ │
                     │░│ ───── │ │  ────  │ └─┘ ░░└─┘░──┐────────────────░│ ░ ░ ░   ░░░ ░ ░ ░░░░░░│        │░│
                     │░│  ░░░░ │ └─ ░░░░ ─┘ ░░░░ ░│ ░░░░│                            ────        •    ─────┘░│
                     │░│ ───── │ │  ────   ─┐─┐  ░│░│    • ░   │   ░                                       │░│
                     │░│       │ │        │ │ │ ░░└─┘░░       ─┼─  ── • ──   •    ───     ────────┐─       │░│
                     │░│       │ │        │ │ │ ──┘ │     ───┐ │     • •  ──┐ ┌───   ─┐───        │ ┌─┐    │░│
                     │░│       │ │        │ │ │   │ └─░░░ ░░░│ └──     ░░ ░░│ │ ░  ░░ │░░    ░  ░░│ │ │    │░│
                     │░│       │ │        │ │ └──░ ─┘░ ░│ ░        •    │ │                       │  ─┘    │░│
                     │░│       │ │        │ │ │ ░░ ░│░░░│░░░░──────░░───┘─┘─────────────────┐─┐──░ ░│      │░│
                     │░│       └─┼──      │ │ │ •░░ └───┘          ┌─    ░  ░   ░░░░ ░ ░  ░░│ │  ┌──┘──────┘░│
                     │░└─ ───┐ │░│       ─┼─┘─┘─  ──┘ ░   ────┐ ───┘ ─────  ── ───── ──    ─┘─┘──┘         │░│
                     │░│  ░░░│ │░│ ─────  │░░░░░░░░░░░ ░ ░░░░░│                                            │░│
                     │░│ ────┘ │ │ ░░░░ ░─┘─░░░────░•░──░░────┘                                 ────┐─ ┌─  │░│
                     │░│       │ │ ──────   ┌──    │                ─┐──┐ │  •                      │ ┌┘ │ │░│
                     │░│       │ │        │ │      └── ░           │░│  │ └─┐ ┌─  •    ──────   ──  └─┘  └─┘░│
                     │░│       │ │        │   │ ───░░░   ───────── │░  • ─┘░│ │░──░─── ░ ░░░░──░░░── ░░──░░│░│
                     │░│       │ │        │   │ ░░░░• ░░ ░  ░░░░░ ░░░ •░░░│ ░ │░░░░░░░░               │   ─┘░│
                     │░│       │ │        │   │  ░░░ ░░ ░ ░░ │░░░░ ░  ░• ░░░──┘────────  ░░│░░░░│ │░░░│ ░│ │░│
                     │░│       │░│         │  └┐░░──░────░░• │░─┐────░░░ ───           ─┐  └────┘─┘───┘──┘ │░│
                     │░│       │░│       │ │   └──  •    ── • • │    ┌───   ┌──         └──                │░│
                     │░│       │░│       │ │                    │░   │      │░  ░│      │░░│               │░│
                     │░│       │ │       │ │             ──┐ ── │ ── └───── │ ──░└────┐─  ─┘               │░│
                     │░│       │ │       │ │            │░░└─                   ░│    │ │ ░│               │░│
                     │░│       │ │       │ │            │         ─┐─                 │ │  │               │░│
                     │░│       │ │       │ │             │░   │  │ │ ┌──── │ │  ────    │░ │               │░│
                     │░│       │ │       │ │             └──┐─┘──┘░  │░    └─┘    ░░┌───┘  │               │░│
                     │░│       │░│       │ │                │     │░ └──░ ┌┘  ──────┘   │ ░│               │░│
                     │░│       │░│       │ │                      │      ░│             └──┘               │░│
                     │░└─      │ │       └─┘                    ──┘ ────┐─┘───       ───    ───────────────┘ │
                     │░│ ───── │░  ─────  ░└──────                ░     │░░ ░                              │ │
                     │ │  ░░░  └── ░░░░░ • │░░░░░░────           ───────┘─────                            ┌┘ │
                     │░│   •   │   ────    │ ──░░░░░ ░── ░──░ ┌─              ────────────────────────────┘  │
                     │                         ───────  ──  ──┘                                             ┌┘
                       ───────────────────────                  ────────────────────────────────────────────┘








```

*Figure from page 15 (2346x3317 px)*


---



4203-E P-342



SECTION 3 DATA INPUT/OUTPUT OPERATION



Signal



Direction Details



Name



SG Grounding for signal



SG Grounding for signal



SG Grounding for signal



DTR Output Data terminal ready



This signal comes ON when the NC is ready for operation.



If data is transferred to the NC while this signal is OFF,



EX-INT



it will not be



read by the NC.



Input External interrupt



This signal is used for BUSY/READY control at the peripheral de



vice side.



When this signal is used, the following applies for transfer of each



character:



{1) When the signal is OFF, the NC cannot start data transfer.



(2) When data transfer starts, this signal temporarily goes OFF; when



it comes ON again the next data is transferred. (It goes through



the sequence ON, OFF, and ON for each character).



High



EX-INT Low



(output)



TXD



~nput)



High



Low



Start bit Stop bit



The EXT-INT signal cannot be used for a peripheral device which has



a buffer, meaning that the ready signal does not switch ON/OFF for



every character. For this type of device, use the CTS signal.


```text


                                                                                               ───
                                                               ┌─┐─────┐─┐─┐─────┐─┐───┐────── ░░░───────░─┐
                                                               │░│░░░░░│ │ │░░░░ │░│░░ │░░░░░░░─── ░░░░░░•░│
          ┌──────────                 ───   •         •    ────┘─┘    ─┘      ── └─┘─         •
          │          ┌──┐─────────────   ──  ───────── ───        ────  ──────  •    ─────────            ──
          └──────────┘░ │░                 ──         •   ───────                               ─────────   │
                     │░ │░░░░░┌─      ░ ─┐                             ─┐░   ─┐──────  ─────────          │ │
                     └─ │░░  ░│   ──   • └──────────────── ──           └─    │                           └─┘
                     │░│ │░░░│ │░│  │    │░░░░░ ░░░░ ░░ ░░│ ░│            ───                             │░│
                     └─┘ │░ ┌┘ └─┼──┘────┼──    │░      │ │  │                ────────────────────────────┼─┘
                     │░│ │░ │  │ │       │     ─┘─────┐─┼─┘─░│                                            │░│
                     │░│ │░░└──┼─┘┐──────┘─ ░░░ ░░░░░░│ │░░ ░│                ────────────────────────────┼─┘
                     │░│ │░░░  │  │░░░░░░ ░  ░░ ──────┘─┘──░┌┘                                            │░│
                     │░│ └─────┘ ┌┘──────┐───┐──            └┘                               ──           │░│
                     │░│       │ │       │   │  ┌──────────░░└──   ░ ░── ░ •░┌────░░─────░░──░░░──┐─┐──── │░│
                     │░│       │ │       │ │  ──┘░░░░   ░ ░░│░░░──────░░───░─┘ ░░░──░░░ ░ •░░─── ░│ │░ ░░ │░│
                     │░└───────┘─┘──── ──┘─┘── ░│░• ░ •░•░░┌┘ ──                                 ─┘─┘──── │░│
                     │░ ░   ░░     ░ ░     ░    └┐ │░  • ──┘                                              │░│
                     │░┌───────┐─┐───────┐───┐░  │ └──      ─┐──┐─┐───┐─┐─┐─┐─┐─┐───┐───────┐────────┐─┐──┘░│
                     │░│       │ │       │   │ ──┘─┘░░┌─── ░░│ ░│ │░ ░│ │░│░│░│ │░ ░│ ░░ ░░ │░░░░░ ░ │░│  │░│
                     │░│       │ │       │ ──┘ ░░  │░─┘    ── • │ │ ──  └─┘─┘   │   │        ┌───  ──┼─┘  │░│
                     │░│       │ │       │  ░ ░  ░ └─░░ ░• ░ │░░│ │  ░ ░ ░░  •░  ░       ░  ░│       │    │░│
                     │░│       │ │        • ░ ░  ░─┘ ────    └──   •   •   •  ─────        ──┘    ───┘    │░│
                     │░│       │ │       •   ┌─┐░• │     ┌─     ──   ──  ──                    │          │░│
                     │░│       │ │        │  │ │   │ ┌───┘░•  ──  ───  ──  ┌─┐─────────────┐───┘──┐    ── │░│
                     │ │       │ │        │ ░│ │░ ░└─┘░░░ ░░──░░ •░░░░ ░░──┘░│░ ░░░░░░░░░░ │░░░ ░░│ ─┐░░░ │░│
                     │ │       │ │       │ ┌─  │ ░ ░░░  ░│ ░░░│ ░ ░ •░░ ░░░░ ░ │░ ░░░ ░░• ░ ░│░░──┘ ░│░── │░│
                     │ │       │ │       │ │   │░░──── ──┘───░│ •░░  ┌─┐─┐░░░░ │░░─┐─░░░░░░░─┘──    • •   │░│
                     │ │       │ │       │ │    ──    •      │░  ─── │ │ │ ┌───┘─┐ │ ─────┐─              │░│
                     │ │       │░│       │ │                 │░┌─    │░│ │░│     │░│      │               │░│
                     │ │       │░│       │ │        ─────    └─┘    ┌┘░│ │░│    │  │   │░•                │░│
                     │         │░│       │ │       │░░░ ░       │   │     │ │   │░│    │  │               │░│
                    │ │        │░│       │ │       │░░┌─      •░└───┘─    │░└───┘ │    │ ░│               │░│
                    │ │        │ │       │ │        ──┘░          ░ ░░─── │░│   ░░└────┘  │               │░│
                    │ │        │ │       │ │           ──     │░┌──┐─┐    └─┘─  ──     │░│                │░│
                    │ │        │ │       │ │                  │ │  │ │        ──       └─┘                │░│
                    │ │        │ │       │ │                  │  │ │  │                                   │░│
                    │ │        │ │       │░└──   ──      ──  │ │ └─ │ └───┐       ─┐───   ──      ──  ──┐ │░│
                    │ │        │ │       │   ░───  ┌─────░░─┐┘░└┐░░─┘─ ░░░└────┐─┐ │░░░───░░┌─────░░── ░│ │░│
                    │ │        │░│        │░ ░░░░  │░░░ ░░ ░│░ ░│  ░░░• •░░ ░ ░│░│ │░ ░░░░░ │░░░░░──░░──┘ │░│
                    │  ────────┘░└─────── │░ ░ ░ ░ ░░░░░• │░░ ░░│ ░░│ ░░ ░░░░│ │░░ ░░░  ░░ ░░░░┌─        ─┘░│
                     ──        └─┘        └─────────────  └─────┘───┘────────┘─ ───────────────┘            │
                       ────────   ────────                                                       ──────────







































```

*Figure from page 16 (2346x3317 px)*


---



3-5. Connection to Peripheral Devices



4203-E P-343



SECTION 3 DATA INPUT/OUTPUT OPERATION



If an RS232C interface is used, a special-purpose cable must be used to connect the signals that are



required by an external device since the signals used for the connection vary according to the external



device.



A typical example is shown below.



3-5-1. BTR System (No DC Codes)



Example 1:



FG FG



Peripheral device



[Supplement]



TXD



RXD



RTS



CT$



DSR



RG1



DTR



1/0 BUSY/



1/0ALARM/



READER START



Fig. 3-9 Connection for BTR System (No DC Codes) (1)



Since no EXT-INT signal is used in this example, bit 1 of NC optional parameter (bit) No.



8 (No. 13, 14, 21, 22) (Ready signals of CN0: to CN4:) should be set to "1" in advance.



(1) Timing Chart for READ



r;;::-,C .._ ~P=e=rip=he_ra_l _,



~ _ device



Ready



DSR



Data request



RG1



Receive data



RXO



n n



\/ \I



11 11



8 bits



Start bit Stnpblt



Fig. 3-10 Timing Chart for READ [BTR System (No DC Codes)]



High



low



High



Low


```text


                                                                                                ───       •
                                                                ┌─┐───┐─┐───┐───┐─┐─┐────────── ░░░░──────░┌─
                                                                │░│░░ │░│ ░ │░░░│ │░│ ░ ░░ ░░░░░────░░░░░░─┘
               ────           ──            ──  ────────────────┘─┘───┘─┘── └───┘─┘─┘───────────     ──
           ┌───    ───────────  ────────────  ──
           │░  ── │                ░                   │      •                   ───         •
           └───  ┌┘   ┌─────┐ ─┐──   │ ░ ░──┐   │    ─┐┘   ──┐  ──┐─ ─────┐   • ──   ────────┐   ─────── ──
                 │ ░│ │░░░░░│  │  ░░ └─ ──░ │   │ ░  ░│ ──┐  │ •  │ •     └─┐─ •  • •        │ ──       │  │
                 │  │ └── ┌─ │ │     │            ░│      │   •   │         │      •         └─         │  └┐
                 └─░ •   ─┘ ─┘ │     │ •   • •  ░──┘  ░░ ░│ │░░   │ ░    ░  ░ ░░│ │░   ░  ░ ░░░ • │   ░░░  ░│
                 │░──░──                 •     ──   ────── ─┘───── ─────────────┘─┘───────────── ─┘─────────┘
                        ────────┐───────┐ ┌───┐
                •  •░░░░  ░░░░░░│ ░ ░░░░│ │░░░│
           ┌──── ──          ┌─  │ ┌─┐─  ─┘ ┌─┘─
           │░░  │  •░ ░ ░│░░░│ │░│ │░│ ░░░░░│
           └────┘ │      └───┘─┘─┘─┘─┘──────┘
                  └┐░   ░│
                   └────  │                     ──                           • •  ───────
                        │░│ ──                 •  ┌─┐                       │░│ ─┐        ─────────────
                        │░│ ░░ ───────────────┐ • │░│ ──────────┐───────────┘░│  └────────   ░░  ░░   ░│
                        │░│ ──                │   │░│           │           ░░│ ┌┘        ───────────┐░│
                        │░│                   └─┐ │░│         ┌─┼─      ──── │  └┘                   │░│
                        │░│                   │ │ │ │         │█│░          ░│  ░│                   │░│
                        │░│                   │   │░│         └─             │   │                   │░│
                        │░│                   │   └─┘          ░▒│          ░│   │                   │░│
                        │░│                   └── │░└───────    ░└───   ── │░│                       │░│
                        │░│                   │   │░│       ──┐┐     ───  ─┘░│   •                   │░│
                        │░│                   │   │ │         └┘─░         │░│  │░│                  │░│
                        │░│                   │   │░│            •         │ │  │ └───┐─             │░│
                        │░│                   │   │░│          ░██│        │░│  │  ░  │              │ │
                        │░│                   │   │░│          ─┐░│        │░│  │ ──                 │░│
                        │░│                   └── │░│           │▓└────────┘░│  └─  ─────            │░│
                        │░│                       │░└─          │▓│        │░│                       │░│
                        │░│                   │   │░│ •                  ──┘░│  ──┐─────             │░│
                        │░│                   │░  │░│                      │░│  ░░│                  │░│
                        │░│                   │   │░│          ─┐          │ │  • └────────┐         │░│
                        │░│                   │   │░│         │█│          └─┘             │         │░│
                        │░│                   │   │░└─    ──  │▒│  ──      │░│  ┌──────────┘         │░│
                        │░│                   └─ ─┘░│ ────  • │▒│ •  ──────┘░│  │                    │░│
                        │░└───────────────────┘   ░░          │█│          │░│  ░░───────────────────┘░│
                        └─┘                   └─────          └─┘─         └─┘  ──                   │░│
                          └──────────┐ ───           ──┐──┐──┐    ──────┐─┐┘ │        ┌─┐────────────
                                     │  ░ ░ ░  ░░ ░░░░░│ ░│ ░│░░ ░░░░░░ │░│ ░│ ░░░░░░ │░│
                ┌───┐───────┐     ── │                                   •              └──────────────────┐
                │░░░│░░░ ░░░│    │░░•  ░ ░░  ░░░ •░░░░────░░────┐░•░┌──░░░─────░░░░ ──░• ░░ ░░░░ ░░░  ░░ ░░│
                └───┘───────┘   ┌┘── ───────────  ░──░    ─┐    └─ ─┘   ──      ────  • ┌─┐┐ ───────      ─┘
                              • │                ──   ──── └─── │ •  ───  •  ───    ── ─┘ └┘─       ──
                  │ │ │░   ─── •       ░                                                 •            ─────
                  └─┘ └────   •       ───
                           ──  ─┐        ─┐──────┐ ─┐
                                │  ░│ ░│  │░░░░  │ ░│
                                └───┘  └─ └──────   └────────────────────────────────────────────────┐──┐
                                     ──┘          │ │                                                │░░│
                                  ┌──░░│          │░└────────────────────────────────────────────────┼──┘
                                  │░░░• ──────────┘░│                                                │  │
                                   ───              │                                                │ ░│
                                                                                                        │
                                                                                   ───               ┌──┘
                                    • ─────┐          │       │                 ┌─┐   ┌─┐            │░░│
                                  ┌┐░│ ░░  │          │ ┌───┐ │                 │░└───┘ │            └──┘
                                  └┘░│ ────┘──────────┘░│   │ └─────────────────┘░│   │ └──────────┐ │  │
                                   └─                 │  ┌┐─  │                 │ │  •  │          │ │ ░│
                                      ──────────────── │░└┘  ─┘─────────────────┘  ┌┐  ─┘─────── ──┘─┘──┘
                                                       │░│░                      │░└┘           •
                                    ────┐──┐           │ ░░│              │      │  ░│           │
                                 ┌──░░  │░░│           │  ░│            │ │       ── └─────────┐ │
                                 │░░░• ─┘── ───────────┘░ ░└────────────┼─┘──┐────   │         │░│
                                  ───                  │  ░             │░   │     ──┘         │░│
                                      ─────────────────┘┐─┐──     • ────┘┐ ┌─┘   ──  └───────── • ──
                                                        │ │  ─── ░░•     │ │  ───  │
                                                        │ │ │░░ ░──      │   │░    │
                                  ┌──┐────┐─┐─────────┐─┘┐ ┌┘ •    ───┐──┘─┐─┼─┐ ┌─┼──┐────┐
                                  │░░│ ░ ░│ │░ ░░ ░░ ░│ ░│ │░░░│ │░░░ │░░░░│ │░│ │░│ ░│░░░░│
                                  └──┘────┘─┘─────────┘──┘─┘───┘─┘────┘────┘─┘─┘─┘─┘──┘────┘








```

*Figure from page 17 (2346x3317 px)*


---



4203-E P-344



SECTION 3 DATA INPUT/OUTPUT OPERATION



(a) Data request signal RG1 is output from the NC.



(b) On receiving this signal, the peripheral device transfers serial data.



(c) The data request signal is forcibly set to the "Low" status in the interface circuit by the start bit



in the received data.



(2) Timing Chart for PUNCH and LIST



Ready



DSR



Clear to send



CTS



-~;~d



d_ata



____.I I.___I.__.__._I


# I __._I

_.___I



Character



Since CTS has



gone OFF,



data transfer is



suspended here.



111



Since CTS has



come ON again,



data transfer is



recommenced here.



Fig. 3-11 Timing Chart for PUNCH and LIST [BTR System (No DC Codes)]



{a) While CTS is OFF, no data is sent from the NC.



High



Low



High



Low



{b) If CTS goes OFF during data transfer, data transfer is suspended within two characters from



that point.


```text


                                                                                               ──        •
                                                               ┌─────┐─┐────────┐──────────────░░•░──────░│
                                                               │░░░░ │░│   ░░░░░│░░░ ░ ░░ ░░░░░──░•░░░░░░─┘
          ┌────────   •    •                 ────    ───       └─────┘─┘─ ──────┘──────────────     ───
          │        ┌─┐ ──── ────┐────────────    ────   ───┐───                                            │
          └────────┘ │          │        ░                ░│    ───────────────────────────────────────────┘
                   │ │ │        └─   ──                      ───
                   │ │ │               ──  │ │      ───── ───    ────────────────┐
                   └─┘ │      ───░      ░  │ │░ ░         ░ ░    ░       ░ ░  ░ ░│
                   │ │ │ │                 └─┘         │        │   ────         └─┐──────────┐─┐──┐─────┐
                   │░│  ░└─░░░─────░░░──░ ░░ ░ ░ ░░░  ░│ ░ │░│  │░│ ░░░░│ ░ │░ │░░ │░░  ░ ░░ ░│ │░ │░░░ ░│
                    ─┘ ░•░░───░░░░░───░░── •   ──   ───┘───┘─┘──┘─┘─────┘───┘──┘───┘──────────┘─┘──┘─────┘
                 ┌─┐  •         │         • ───  ┌─┐
                 │░│ │░░░░░ ░░ ░│  ░  ░░░•░   ░  │░│
                 └─┘ └──────    │  •            ─┘─┘
                             ──┐ ─┐ │  ┌───░
                           •░ ░│ ░│ │  │░░░    ░│
                            ───     └── ───   • └────────────────────────────────────────────────┐──┐
                                 ─┐─        │  │                                                 │░░│
                              │░░░│         │ ┌┘─────────────────────────────────────────────────┘──┘
                              └───┘ ────────┘ │                                                     │
                                              │                                                     │
                                                                                                    │
                                              ────────────                   ┌───────────────────┐──┘
                              │  ───┐──                   │                │ │                   │░ │
                              └──   │   ────────────────┐ │                │ └───────────────────┘──┘
                              │░░┌──┘───                │  •  ─────────────┘ │
                              └──┘                      └─  ──             │ │                   ───┐
                                                           •     ──────────┘░│                      │
                                                 ───┐─         ─┐          │ └┐ ────┐  ──┐──┐─   ───┘
                              ────────        ──    │ │ ┌─┐    ░│          │  └┐    └──  │  │ │
                              ░░░  ░░ ────────░░│   │ │ │░└───┐─┘          │   └──┐ │    └──┘ │
                              ───────         •░│ • └─┘─ ░│   │ └─┐────────┘ •░│  │ │    │  │ │
                                      ────────   • ─┘    ─┘   └─  │        └─ ┌┘   ─┘────┘  │ │
                                               ─┐     ───       │ │    ┌──    │           ──┘─
                                                └─────      ┌───┘─┘┐ ──┘  ┌───┘──────┐
                                                            │░░░ ░░└─  │  │░░░ ░  ░░░│
                                                            │░░  ░░░░•░│  │░░  ░ ░░ │ ──┐
                                                            └─────── ░•   └─────────┘ ░░│
                            ┌──┐──┐─┐─┐─────────┐─┐───┐─────           ───┘             └┐─────┐
                            │░░│ ░│ │ │░ ░░░ ░░░│ │░  │░░░░  ░░  │░│ │░░░ │░░░░│  │░ │░│ │░ ░░░│
                   ┌─┐─┐──┐─┘  └─ └┐┘─ ──┐─ ─┐── ┌┘   └─┐─   ┌─ ─┘─┘─┘────┘────┘──┘──┘─┘─┘─────┘
                   │░│ │░░│ ░ │░ ░ │░░• ░│ │░│ ░ │░░ ░ ░│ ░░ │░•
                  │     •     │ │ ┌┘ • ──┘ └─ •        │     └─ ────────────────────────────────────────
                  │░  │  ────░░░│ │░│ │░░░   ░░  ░  ░░░│ ░ ░ ░   ░           ░   ░░░                ░
                  └───┘      ░┌─┘─┘─┘─┘────────────────┘────────────────────────────────────────────────
                      └─    ──┘
                        ────


































```

*Figure from page 18 (2346x3317 px)*


---



4203-E P-345



SECTION 3 DATA INPUT/OUTPUT OPERATION



(c) When CTS comes ON again, data transfer is recommenced.



Example 2:



NC Peripheral device



FG FG



READER START



DATA BUSY/



Fig. 3-12 Connection for BTR System (No DC Codes) (2)



[Supplement] Since an EXT-INT signal is used in this example, bit 1 of NC optional parameter (bit) No.



8 (No. 13, 14, 21, 22) (Ready signals of CN0: to CN4:) should be set to "0" in advance.



(3) The timing chart for READ is the same as that shown in Example 1.



(4) Timing Chart for PUNCH



Ready



DSR



Peripheral



device



----



External interrupt



EX-INT



Send data



TXD



Fig. 3-13 Timing Chart for PUNCH [BTR System (No DC Codes)]



High



Low



High



Low


```text


                                                                                                ───       •
                                                                ┌───────┐───┐─────┐─────┐────── ░░░░──────░─┐
                                                                │░░░░░░░│ ░ │░░░░ │░░░░ │░ ░░░░░────░░░░░░•░│
           ┌────────────     •    ──    •   ──── ──   •  •  ────┘───────┘── └─────┘─────┘───────      •
           │            ────┐ ┌───  ───┐ ┌─┐    │  ─── ┌─ ──               •                                │
           └────────┐       │ │        │ │░│    │      │    │                ───────────────────────────────┘
                    └─ ──   └─   ┌──── │ └─┘  ░┌┘ ── • │    └┐  │           •
                      │░        ┌┘    • •   ───┘ •  • • ────┘┘──┘───────────
                      └────┐────┘
                           │     ───────────────────                             ───────────
                          │ │ ┌─┐                   ┌─┐ ──────────────────────┐─┐            ─────────────┐
                          │ └─┘░└──────────────── • │░│                       │░│ │ ─────────       ░    ░│
                          │ │ └─┘                │  │░░┌─      ──     ──      │░│ └┐         ───────────┐░│
                          │░│                    └──┘░ │ ──────   ┌─┐─  ───── │░│ └┘                    │░│
                          │ │                    │░  ░│           │▓│         └─┘ ░░•                   │░│
                          │░│                   │   │░│           │ │         │░│  │                    │ │
                          │░│                   │░░░│ │           │▒│         │ │ ░│                    │ │
                          │░│                   └── │░└─────   ───┘─┘         │░└─┐┘                    │ │
                          │░│                   │  ─┘░│     ┌─┐        ┌┐──── │░│ └┘                   │ │
                          │░│                   │   │░│     │░│       ┌┘┘     │░│ ░                    │ │
                          │░│                   │ ──┘░│  ┌─┐ ░│       │░ ─┐   │░│ │                    │ │
                          │░│                   │  ░│ │  │▓│ ─┘       └─┐▓│   │░│ │░•                  │ │
                          │░│                       │░│  └─┘  └─── • ─┘ └─┘   │░│ └─                   │░│
                          │░│                       └─┘           │▒│         │░│ │                    │░│
                          │░│                    │ ─┘░│ ──    ────┘─┘         │░│ │                    │░│
                          │░│                   ┌┘┐ │░│   ────        ────────┘░│ └─┐                  │░│
                          │░│                   │░│ │ │                       │░│ │░│                  │░│
                          │░│                   │   │░│          ┌─┐          │ │ │ └──┐─────┐         │░│
                          │░│                   │░░ │ │          │▓│          │░│ │░  ░│ ░ ░░│         │ │
                          │░│                   └── │░└┐   ───── │░│          │░│ └────┘─────┘         │░│
                          │ │                   │   │░└┘───     ─┼─┘ ─────────┘░│ │                    │░│
                          │░│                       └─┘          │▓│          │░│   │                  │░│
                          │░│                 ┌─────┘░│              •        │ │ ──┘─────┐─           │░│
                          │ │                 │░░  ░│░│           │█│         ░░│ ░░ ░ ░░░│            │░│
                          │ └────────               └─┘           └─┘        ───          └────────────┘░│
                          │           ───────   ────  └─────┐────┐   ─┐─┐─┐─┐    ───────┐                │
                             ────   ──░░  ░ ░───░░░░░░░   ░ │░░░ │░░░░│ │░│ │░ ──░░░░  ░│            •
                 ┌──────────┐     ──                             └─       │  │            •   •  ──┐─  ┌───
                 │░ ░░ ░ ░ ░│    •░ •   ──── │░│ ┌──────────────┐  ─────── ┌─┘ ──────────  ─── ── ░│  ─┘   │
                 └──────────┘   │░    •     ─┘─┘ │░  ░          │    ░ ░   │                            •  │
                                │  ──┐ •         └──────────────┘───────   └─  ┌──    •░│ ┌┐─░───── ░ ░ ░░░│
                  ┌─┐  ─────────     │                                   ─┐  ──┘  ┌─── ─┘─┘┘ •     ────────
                  │ │    ░   ░ ░  ░░           ░  │ │░│  │░ ░ │ ░ ░░│   ░ │░ ░░│  │
                  │ │ │   ──                ┌─────┘─┘─┘──┘────┘─────┘─────┘────┘──┘
                  │░│ └┐ │░░  ░░░  ░  ░░░░ ░│
                  └─┘  └─┘───┐      ┌─┐      ───
                             └───┐──┘ └─────░░   ─┐
                             │   │       ░░░•   •░│
                             └───┘ ┌───┐          └────────────────────────────────────────────────┐─┐
                                   │   │ │  ─────                                                  │░│
                              ────    │ ┌┘──     ─────────────────────────────────────────────────┐┘─┘
                               ░░░│ ──┼─┘                                                         │
                              ────┘   │░│                                                         │░
                                   ───┘─┘                                                         │
                                             ┌─────────────────                                   └───┐
                                           │ │                  │      │                    │     │ ░░│
                               ────┐─────┐ │░└────────────────┐ │      │░┌────────────────┐░│     └───┘
                              │░░░░│  ░ ░│ │ │                │░│      │░│                │░│
                              └────┘─────┘   │               ┌┘░└──────┘░│                │░└───┐  ───
                                          ─┐ │               │░│       │  │              │░ │   │
                                           │░│               │░└─────── │░│              │░│ ───┘
                                           └┐░── ───────────┐  │        │░└─┐───────────┐  │
                                 ─┐─┐       │░ ░│           │ │         │ ░░│           │ │
                              ──┐ │░│       │░ ░│      ─────┘ │         │  ░└───────────┘ │
                              ░░│  ─┘───────┘░ ░└──────     └─┘─┐───────┘░  │           └─┘─────
                               ─┘           │░•░│           │░ ░│       │░ ░            │░ ░
                                          •  •                                          │   ┌────
                                  ──┐───┐─ ── ──────────┐──────────────┐────┐─┐─┐──────┐┘───┘
                                    │ ░ │░  ░ ░ ░  ░░  ░│   ░░ ░░ ░  ░ │░░░░│ │░│ ░░   │░░░░│
                                  ──┘───┘───────────────┘──────────────┘────┘─┘─┘──────┘────┘












```

*Figure from page 19 (2346x3317 px)*


---



4203-E P-346



SECTION 3 DATA INPUT/OUTPUT OPERATION



(a) When the external interrupt signal EXT-INT comes ON, data is sent from the NC.



(b) On reading the stop bit, the peripheral device forcibly sets the external interrupt signal to



"Low". It is essential that the external interrupt signal be set to "Low" temporarily.



(c) On completion of processing, the peripheral device switches the EXT-INT signal ON again.



3-5-2. DC Code Control



When DC code control is effective, the NC outputs DC control codes to control data transfer.



The user can select whether or not DC code control is performed by parameter setting.



The available DC control codes are DC1 through DC4, as shown below.



"DC" is the abbreviation for "device control", and these device control characters serve to start peripheral



devices.



DC1



DC2



DC3



DC4



[SupplementJ



Example 1:



8 7 6 5 4 3 2 I



Tape reader start



Tape punch start



0 oQ



Tape reader stop -+ 0 0



Tape punch stop -+ 0


## 1. Since DC control codes are automatically generated from the NC, the user does

not have to write them into programs.


## 2. The control codes used are the ones shown above, regardless of whether the ISO

or EIA coding system is used.


## 3. The NC unit cannot be controlled by control codes sent from the peripheral device.

Peripheral device



FG FG



TXD RD



RXD SD



ATS



CTS



1/0 BUSY/



DSR 1/0ALARM/



SG SG



DTR DR



Fig. 3-14 Connection for DC Code Control


```text


                                                                                                ──        •
                                                               ┌──┐─┐──┐─┐─┐───┐─┐─────────────░░░───────░░│
                                                               │░░│ │░░│ │ │░░░│ │░░░ ░░░░░░ ░░ ──░░░░░░░──┘
          ┌─────────        •         ───   ─────────         • ──┘─┘──┼─   ───┘─┘────────────┐
          │         ──────── ────┐────   ───         ──┐────┐─         │ ┌──                  │            │
          └─────────             │                    ░│    │        │ │ │                    └────────────┘
                    •  │ ┌─      │                ░   ─┘ ───┘        └─   •                   │
                   •   │ │  ─┐──                                                              └───┐──┐
                    ── │ └─ ░│    ┌──── ░ ░──────░ •  ░ ░ •░  ─────░ • ░░░ ░ • ░░░░░░ •░──────░░░ │ ░│
                       └─ ░──┘────┘░░░░─┐── ░ ░ ░─┐░──┐───░─── ░░░░──░───────░───┐───┐░•░░ ░░░────┘  │
                   ┌───┘                │         │   │                          │   │             ──┘┐
                   │░░ │░│ •░░░░░░░  ░ ░ ░░░░░░ │ │░ │░░░░ ░░│ │░ ░│ │░ ░░░░│ ░│ ░░│ │░│ │ ░ ░  ░   ░░│
          ┌────┐  ┌┘  ─┘ └┐       ┌─────────────┘─┘──┘───────┘─┘───┘─┘──────┘──┘───┘─┘─┘─┘────────────┘
          │░ ░░│  │░░  ░ ░│ │  ░░░│
          └────┘ ─┘      • ─┘┐ │  └────┐──────┐─┐──┐─┐─┐────┐─┐───────┐─┐────────────────┐───────┐
                │░░░░ ░░• •░░│ │░ ░    │░░░░░░│ │░ │░│ │░░░░│ │░    ░░│ │ ░░░     ░░   ░░│ ░░  ░░│
                │      │   ┌─ ─┘─ ─┐───  ┌─── │ │  │ └─ •   │    ┌─── └─┘  ── ────  ─┐ │ └─  ┌───┘
                │░░░ ░░│ │░│ │░░░• │░░░░░│   ░│ │░  ░░░•  •░│░ ░ │░░░░░░│░ ░ •░░░░░░░│ │░░░░ │
                │      └─┘ │ └─┐─ • ─┐─  └─┐  │ │        │ •  ─┐ │ ─┐    • ┌─  ┌─────┘─┘─────┘
                │  ░ ░░░░░░│ │░│ │░░ │ •░░░│ •░ │░░  ░░  │░ ░░░│ │░ │░░░░ ░│░░░│
                │       ─── ─┘ └┐┘ ─┐   ─┐─   • │        │     └─┘┐  ┌─┐─   •  └─────┐─┐───────┐─┐──────────┐
                └─ ─── ░ ░ ░░░░░│░░░│  │ │░ ░ ░ │░░    ░  │░░░░│ ░│░░│ │░ ░░ ░░░░░░░░│ │░ ░░░  │░│ ░░ ░░░░░░│
                │░░░░░───────── └───┘ ─┘ └──────┘─────────┘┐───┘──┘ ─┼─┘──── ──┐─────┘─┘───────┘─┘──────────┘
                └─────         │     •  │                  │  ░   ░ ░│  ░   •  │
                      │        │░      ░│ │  │             │░┌─────  └─── •    │
                      │   │   │         │ │  │             │░│     │ │     •  │
                      │  ─┘   │░          │  │             │ │     │ │   •    │
                      │   │   │  │      │ │                │ │     │      ───░│
                      │   │   │  │     ░│    │             │░└─┐   │     │   ░│
                      │   │   │  │      │    │             │ │ │   │     │ ─┐░│
                      │   │   │  │      │    │             │░│     │  │  └─ │░│
                      └───┘   └──┘─  ───┘────              │░│  ─── • └──┘  │░│
                                                           │░│              │░│
                ┌──────┐────┐        ─────┐───────┐─ ──── │    ──  ─────────┘  ┌──────┐──┐─┐─┐─┐─┐─────────┐
                │░ ░░░░│ ░░░│       │░  ░ │░    ░░│ │░░░░─┘┐──┐░░•░░░░░░░  ░░│ │░░░ ░░│ ░│ │░│ │░│  ░░  ░░ │
                └──────┘────┘       └─        ──    └───   │  │    ──────────┘─┘──────┘──┘─┘─┘─┘─┘─────────┘
                                    │        •
                                 │ •           │                   │  ─────────────────────────────┐────────
                                 │  │        ──┘   ───    │░• │   ░│    ░  ░      ░░░  ░░░    ░ ░ ░│ ░░
                                    │░───────░░░───░░ ────┘─░░│    │                   •
                               ┌─┐  │                          ───┐ ────────┐─┐─┐────── ──┐─┐────────┐─┐───┐
                               │░│  │░│ │░│ │░ │░│ ░░ ░ ░░ ░ ░░░ ░│  ░ ░ ░ ░│░│ │░░░░ ░ ░░│ │░░░░░░░ │░│░░░│
                  │ ─────       ─┘  └─┘─┘─┘─┘──┘─┘────────────────┘─────────┘─┘─┘─────────┘─┘────────┘─┘───
                  │      • ─────  ──                                                                       •
                    ─┐░                           ┌─┐                         ┌─┐             ──────────  │░│
                     │░│ ─────────────────────┐   │░└──────────────────────── │░│ │ ┌─────────░    ░ ░  ──┘░│
                     │░│                      └─  │░│                         └─┘ │░│         ──────────  │░│
                     │░│                      │   │░│                         │░│ │                       │░│
                     │░│                          │░│           ██▒           └─┘                         │░│
                     │░│                          │░│       •   ──         ──┐┘░└─┐┐┐                     │░│
                     │░│                     ┌──┐ │░└─────── ──   ─┐ ──────  └┘░│ └┘┘                     │░│
                     │░│                     │░░│ │ │           ░•█│          │ │ │░│                     │░│
                     │░│                     └──┘ │░└───     ──   ─┘ ─── ──  ┌┘░└─┼─┘                     │░│
                     │░│                     │    │░│   ─────  ───      •  ──┘┘░│ │ │                     │░│
                     │░│                     │░ ░ │░│           █▓▒           │ │   │                     │░│
                     │░│                      │   │░│              │          │░│ │ └───┐                 │░│
                     │░│                      │   │░│           ░│█│          │ │ │     │                 │░│
                     │░│                          ░░└───── ────  │▒│ ────────┐┘░│ │  ──                   │░│
                     │░│                      ───┐░░│     •    ──┼─┘         └┘░└─┼──  ───┐               │░│
                     │░│                     •░░ │ │            ░│█│          │ │ │       │               │░│
                     │░│                      • ─┘░│             └─┘          │░│ │ ──────┘               │░│
                     │░│                         │░│                          │░│ │                       │░│
                     │ │                      ───┘░└───────────────────────── │░│ └──                     │░│
                    │ │                          │░│                          │ │                         │░│
                    │ │                          │░│                         │ │                          │░│
                    │ │                          │░│                         │ │                          │░│
                    │ │                       ───┘░└────────── ┌─┐ ──────────┘░│ ─┐─┐                     │░│
                    │░└───────────────────────░ ░│ │           │█│░          │ │  │░│                     │░│
                    │░│                        ──┼─┘           └─┘─          └─     └─────────────────────┘░│
                      └────────────────────┐─┐   │  ┌─────────     ─┐──┐─┐─┐─┘  │                           │
                                           │░│ ░  ░ │░░ ░░ ░  │░│ │░│  │░│ │  ░ └───────────────────────────
                                           └─┘──────┘─────────┘─┘─┘─┘──┘─┘─┘────┘










```

*Figure from page 20 (2346x3317 px)*


---



4203-E P-347



SECTION 3 DATA INPUT/OUTPUT OPERATION



[Supplement] 4. Since no EXT-I NT signal is used in this example, bit 1 of NC optional parameter (bit)



No. 8 (No. 13, 14, 21, 22) (Ready signals of CN0: to CN4:) should be set to "1" in



advance.



(1) Timing Chart for READ



r;;7 --



"-""Pe;.;.;rip=he_ra_l-'



~ _device



Ready



DSR



Send data



TXD



Receive data



RXD



Data

- -



D D



C C



1 3



\ \ \



\ \ \



. \ \



Data



Within 100 characters Within 100 characters



Fig. 3-15 Timing chart for READ (DC Code Control)



(a) The NC sends the DC1 code.



(b} On receiving the DC1 code, the peripheral device starts transferring data to the NC.



(c) After reading the program name, the NC sends the DC3 code.



(d) On receiving the DC3 code, the peripheral device suspends transfer of data to the NC. Data



transfer stops within 100 characters after transmission of the DC3 code.



(e) When processing at the NC is completed, the NC sends the DC1 code again.



(f) On receiving the DC1 code, the peripheral device starts transferring the data immediately



following the data sent in the last transfer operation.



(g) The NC sends a DC3 code and a DC1 code during reading of each 256-character section of



the NC program (equivalent to a tape length of 0.65 m).



(h) The peripheral device sends the end of record code and data transfer is terminated.



(i) On completion of data reading, the NC sends the DC3 code.


```text


                                                                                                 ──
                                                                ┌──┐─┐────┐─┐───┐─┐─────────────░░░───────░─┐
                                                                │░░│ │░░░ │ │░░░│ │░░  ░░░ ░░  ░ ──░░░░░░ •░│
           ┌─────             ────────      •            ── ──── ──┘  ────┘  ───┘─┘─    ───────       ──
           │     ─────────────        ─┐──── ───┐─┐─┐─ ──  │    •   ──     ──       ────                    │
           └─────      ░      ───┐ ┌─┐ │        │ │ │ •    │                 ──    •                        │
                 ─────────────   │ │ │     ──       │  ░     ░ ───  ┌────   ░░ ─┐ •   ──      •    ░
                                     │░░   ░░│ • • ┌┘ ────░│ •░░░░░ │░░░░│ ░──░░│ ░ │░░░─── ░░░  ░ •░ ░──────
                                     └───────┘─ •  └┘─    ─┘─ ──────┘────┘──  ──┘───┘───   ──────── ───
                  ┌─┐  ┌──────┐─────┐┘
                  │░│  │ ░░░  │░░░ ░│ •░░░░
                  └─┘  └──────┘─       ───        •
                                ┌─────     ──┐───░░  ┌┐
                                │░ ░░   ░  ░ │░░░ ───┘┘
                                  ──────              └────────────────────────────────────────────┐
                              ┌──       │                                                          │
                              │░░──   │ └──────────────────────────────────────────────────────────┘
                              │░░░  ──┘░│
                              └───    │░│
                                   ───
                                         ┌──┐          ───┐            ┌──┐            ┌── │
                              ┌──────┐   │  └┐           ░│            │  └┐           │░ ░│
                              │░░    └───░  ░└─────────  •░┌───────────┘ │░└───────────┘░   ┌──────┐
                              └──────┘   ── ░│         ░ ░░│           ░ └┐            │░ │░│      │
                                     └──   ──   ─────────┐─┘ ──────────── │   ───────── ──┼─┘  ────┘
                                               │         │                │  │            │
                                            ─┐░└─────────┘ ─┐─┐            │ │ ───────────┘  ┌─┐
                              ┌────────┐     │ │         │░ │░│            └┐░│           │░ │░│
                              │░░░░░ ░░│     │░│ ───     └──┘ │             │░└─── •      │  └─┘
                              │░░ ─────┘─────┘░│    │    │    └─────────────┘░│   •   ░  ─┼─ │ └───┐
                              └───           │ │    └─── │░│  │             └─┘     ───   │░│ ░│   │
                                  ─────────── • ───      │ │        ────────   ─────      │ │  │
                                                   ┌───┐─┼─┘───────┐                 ┌────  └──┘─────┐
                                                   │░ ░│ │░  ░░░ ░ │                 │░░░░  ░ ░ ░░ ░ │
                                                       │     ───                      ───────────────┘
                                        ┌──┐────┐─┐──── ─────   ┌───┐─┐─────┐─┐─┐─────
                                        │░░│ ░ ░│ │░░░░   ░░ ░│ │░░░│ │░░   │░│ │ ░░ ░│
                     ─┐─┐───┐─┐─┐──────┐ • │    │ └───────────┘─┘───┘─┘─────┘─┘─┘─────┘
                    │ │ │   │░│ │     ░│ ░░  ┌──┘─
                    │ │ │ │ └─        •   │  │    •    •     •
                    │ │ └─┘    •  ──      │ ┌┘─┐   ┌─── ───── ──────────┐─────────────────── ─────
                    │ │ │ │  ┌─     ─┐ ───┘ │  │   │                    │          ░
                    │ │ └─┘┐ │ •     └─    •             │   •              ── ────────────  ──
                    │ │ │  │ └─ ───         •    ░       └───░      ░       ░░•
                      │ │              │                                         ───   ───┐────┐─┐─┐ ┌───┐
                      ░ └─────░ ─── ░ ─┘    •░░───░───░░░░• ░ •░ ░░───░░░░ ─┐────░░░─── ░░│ ░ ░│ │░│ │░░░│
                        │ ░ ░░──░░░───░░───░░──░░░•░░░────░░•░░┌───░░░─────░│ ░░░── ░░░ ──┘────┘─┘─┘─┘───┘
                    ┌─┐ │                  •               │   │
                    │░│ │░░░  ░░ ░░░░░░ ░░ ░• ░│ ░ ░░░░░░░░│  ░│ ░│ ░░  ░ ░ ░  ░     ░ │  ░•
                    │ │ │                  •   │ │             │  │                    │    ──────────
                     ░│ └───┐─────────────┐ ───┘─┼──┐──────┐─┐─┼──┘─                    │             │
                     ─┘ │   │             │      │  │      │ │ │      ──────────────────┘─────────────┘
                        └───┼─ ──────────  ──────┘──┼──────┘ └─┘───
                    ┌─┐ │   │ •                     │                  ───────────┐─┐─┐─┐──────┐─┐────┐──┐
                    │░│ │ ░─┘░ ─────── ┌─ ──────── ░└──░─────░│ •  •░ •░░░ ░ ░ ░░░│ │░│ │░░ ░░░│ │░░░░│ ░│
                    └─┘─┼──░░• ░░░░░░ ─┘░• ░░░░░ ░── ░░•░ ░░░─┘─░──░•  ────   ────  └─┘─┘──────┘ └────┘──┘
                        │                   │                        •     ───    ──            •
                    │░│ │ ░ ░░░░░ ░ ░ ░░░ ░ │░░░░ •░ ░░  ░  ░   ░  ░░  ░   ░░    ░░░│   ░   ░ ░░
                    │ │ │                   │      •               •        ┌───────┘─────────────
                    │ │ │░       ░░   ░ ░      ░  │ ░  ░░                  ░│
                    └─┘─┘─────────────────────────┘ ────────────────────────┘





















```

*Figure from page 21 (2346x3317 px)*


---



(2) Timing Chart for PUNCH



r.:::-7 __



Pe~pheral



L..::'.:::.J



device



Ready



DSR



Send data



TXD



O2'



Data



4203-E P-348



SECTION 3 DATA INPUT/OUTPUT OPERATION


# I I

Data


# I I

-_ ------;L_:-t- -



Clear to send



CTS



Fig. 3-16 Timing Chart for PUNCH (DC Code Control)



(a) The NC sends the DC2 code.



(b) If the CTS signal is ON, the data to be transferred is sent immediately following the DC2 code.



(c) When the CTS signal goes OFF, data transfer is suspended.



When the CTS signal comes ON again, the NC starts transferring the data following the previous



transfer data.



(d) When data transfer is completed, the NC sends the DC4 code.


```text


                                                                                                ──        •
                                                               ┌──┐─┐────┐─┐─────┐──────────────░░░───────░│
                                                               │░░│ │░░░ │ │░░░░ │░░░ ░░░░░░░░░ ───░░░░░░░─┘
           ┌──────  ──              •        ────────────────── ──┘─┘────┘ └─────┘────────────
           │      ──  ┌───────────── ───┐───┐                                                              │
           └────── ░│ │░              ░ │  ░└──────────────────────────────────────────────────────────────┘
                  ──┘ └───── ───────────┘───┘
                            •
                             ┌──┐─┐─┐────────┐───┐─┐
                             │  │░│ │ ░ ░ ░░░│ ░ │░│
                             └┐─┘─┘─┘──┐─────┘── │ │
                              │        │        •  └────────────────────────────────────────────────┐
                               ┌───    └─┐                                                          │
                               │░░░    │░│    ──────────────────────────────────────────────────────┘
                               └───  ──┘░│
                                    •   •
                                     ──
                                        ┌──┐         ───────┐─          • ───────   ────┐──
                               ┌────── ┌┘ ░│       ──       │░│        │░│       ───    │░ ┌─
                               │░░ ░░░ │░ │░•    │ ░░──── • │░│        │░│ ─────        │░ │░│
                               └────── │░ └┐ ────┘ ──    • ─┘░└────────┼─┼─         ────┘░ │░└──────┐
                                       └── │                │░│        │░│              │  └─       │
                                     ──                    │ ┌┘───────  ┌┘        ──────┘──      ───┘
                                                         ──┘░│        │ │ ────────            ───   │
                              •    ───── ────────────────  │░│        │░│                           │
                                 ░   ░░░│                ──┘░│        │░└───────────────────────────┘
                              ──────────┘                  │░└────────┘░│
                                                            ─┘
                                      ─┐─┐────┐─┐─────────┐    ┌────┐─  ─┐──┐─┐─┐─────┐
                                       │░│ ░ ░│ │░░░░░ ░░░│ │░ │░░░░│  │░│  │░│ │░░░ ░│
                   ┌─┐─┐─────┐─┐───┐──┐  └──  └─ ─────────┘─┘──┘────┘──┘─┘──┘─┘─┘─────┘
                   │░│ │ ░  ░│ │░░░│ ░│ │░░░ │░░•
                   │ │ │    • │ ─┐    │ └┐ │ │ • ────────────────────────────────────────────────────────
                   │░│ │ ░░   │░ │░░░• ░ │░│ │░ │░░░          ░  ░░       ░    ░ ░ ░ ░ ░ ░        ░      │
                   │ │ │       ──┘ ┌─     •   ┌─┘ ┌─          ─────         ─────────────────────────────┘
                     │ │░░   ░    ░│ ┌───┐ ┌──┘ │░│  ┌─┐            ─── •
                   ──┘ │          ─┘ │   │ │  │   └──┘ │      ─┐─┐──   •   ──────────────────── ───────────
                       │░░░  ░░ • ░░ │░ ░░  ░░░░ ░░  │░░│ │   ░│ │░░░ ░   ░      ░    ░   ░  ░ • ░         │
                       └───  ───  ┌──┘───────────────┘──┘─┘────┘─┘───────────────────────────── ───────────┘
                       │   ──     │
                    ── │           ─────────────────────────┐─────────────┐──┐─
                       └─  │ │     ░          ░░░ ░         │░ ░░  ░    ░ │░░│
                         ──┘─┘──────────────────────────────┘─────────────┘──┘







































```

*Figure from page 22 (2346x3317 px)*


---



4203-E P-349



SECTION 3 DATA INPUT/OUTPUT OPERATION



3-5-3. DC Code Control TYPE2



In the standard DC code control described in 3-5-2, DC codes can only be output from the NC. In TYPE2



control however, DC codes can also be output from the peripheral device.



When this type of control is used, the NC uses the four control codes DC1, DC2, DC3 and DC4, and the



host computer side uses two: DC1 and DC3.


#### DC Code NC Host Computer

DC1 Enables data reading: Enables data reading:



(1) Starts data reading. (1) Responds to DC2.



(2) Cancels temporary stops. {2) Cancels temporary stops.



DC2 Sent to the peripheral device at the be-



ginning of a data transfer operation as a



data reading request.



DC3 Requests temporary stoppage of data Requests temporary stoppage of data



transfer from the peripheral device. transfer from the NC.


#### DC4 Terminates data transfer.

To make TYPE2 control effective, set "1" for both the standard DC code control bit and the DC code control



TYPE2 bit in the NC optional parameter {bit) for the relevant channel.



Example 1:



NC Peripheral device



FG FG



TXD



RXD



RTS



CTS



DSR DTR



DTR



Fig. 3-17 Connection for DC Code Control TYPE2


```text


                                                                                                ──        •
                                                                ┌─┐─────┐───┐───┐─┐─────┐────── ░░░───────░░│
                                                                │░│░░░░░│ ░ │░░░│ │░░░░ │░ ░░░ ░───░░░░░░░──┘
                 ──         ──            ──────────────────────┘─┘─────┘ ──┘───┘─┘─────┘───────     ───
           ┌────┐   ────────  ───┐────────
           │    │ │              │    ░░  │             •    •   ──    •         ───  •        •  ────
           └────  └─ │ │       ──      •  └───┐───────── ┌──┐  •   ┌──┐  ── ─────   ── ───────  ──    ─────
                 │  ░│ │    ░  ░░ ─────       │          │  │ • │ ─┘  │ •          •
                 │  ─┘─┘                  │   │              •  └─     •     •   │  • ────────────  ────────
                 └─        ░  ░       ░░• │░  │░│  ░   ░ ░   ░   ░ ░░ ░░░ ░ •░  ░│
                 │░                    •  │    ─┘   │       ┌─  ┌─┐─   ──    •   │ ───────────────────┐─────┐
                 │ ─┐──────┐─┐─┐───┐──┐ ──┘ ──   •  └─── ───┘ ┌─┘ │ ───  ──── ───┘           ░        │    ░│
                 │░░│ ░░ ░ │░│ │░░ │░░│ ░░  ░    ░░  ░ ░│     │                  │                     ──
                 └┐─┘┐        ┌┘┐──┘──┘───────────   ┌──┘            ┌─┐           ──────────┐─┐            •
                  │  │░░  ░░░░│ │                  ░░│   ──       ───┘ │           ░░░░  ░░  │░│           │░│
                  │░  ─┐░  ┌──  │░░─────  ────────   │               │  ──────────         ──┘─┘           │░│
                  │ │  └───┘   ─┘┐  ░░░░── ░░  ░░░  ┌┘┐ ─────────────┼─   ░░ ░  ░░░•░░░░ ░•      ──────────┼─┘
                  │ │            │ ░┌───░░░──░──────┘░│              │  ─┐─┐────── ░ ─────░                │░│
                  │ └──          │  │                   ───          │   │ │               ┌─────┐         │░│
                 │      ────     └─┐┘───░───────────────░░░────┐───  │ │░│   ░░░░░░ ░░░░ │░│ ░░░░└─────────┘░│
                 │ ┌────░░ ░ ─── │░│░░  •░░ ░░░░░░░ ░ ░░░░░ ░░░│░░░• │░└─┘  ─────────────┘─┘─────┘         │░│
                 │ │    ─────    │░│ ░      ──┐──  ░░░░──── ░░░   ░  └─┘                          ─────────┘░│
                 │ └───      ────┘░░│ │░┌┐ ░  │    ░┌──      •         │                                   │░│
                 │      ────     │░░└─┘░└┘  ░─┘──░░░│  ──       ───  │░ ───────────   •  ────────────────  │░│
                 │ ┌─── ░░░░    ┌┘░░░░░░░│ ░░░░░░░ ░ •░░░░░──── ░░░• │  ░░░ ░░░░ ░░░─┐░── ░░ ░░░░░ ░ ░░░░  │░│
                 │ │   │        └┘░───── ░ ░░ ░│ ──░░░░░───░░░░┌──   │  ─────┐───── ░└─░░   ──────    ─────┘░│
                 │ └───┘────┐───┘░░     ──┐  ──┘   ──          │   ──┘░      │            ──               │░│
                 │ │    ░░░░│    ───░░░░░▒└──▒░▒░░░░░░──             └─ ░────┘─────                        │░│
                 │       ───    │                 ──                                       ────────────────
                 └────┐       ░─┼─  ░──░░   ──────  ░───░░ ░•░ ┌─░░░░░  ───░░│ ░░  ░ ░░ ░ ░░ ░    ░░░░ ░░░░ •
                 │ ░ ░│ •░ ░ ── │░ •░░░─── •░ ░░░░░░ ░░░────░──┘░──────░░░ ──┘ ─────────────────────────────
                •        ────  • •  ───   • ──────── ───    •   •      ────
                 │  ░ ░░•
                 └───┐ │  ───────────────────  ──                                  ─────────            ──┐
                     └─┘  ░                   •  ┌─┐─────────────────────────┐─────          ──────────   │░│
                     │░│ ───────────────────── ──┘░│                         │░░   ──────────░░ ░ ░ ░  ───┘░│
                     │░│                         │░└┐ ───────       •    ────┘░┌┐            ──────────   │░│
                     │░│                     ┌───┘░└┘─       ───┐─┐─ ────    │░└┘──┐                      │░│
                     │░│                     │ ░ │ │            │█│          │░│ ░░│                      │░│
                     │░│                     │   │░└────────────┘   ─────    │░└──┐┘                      │░│
                     │░│                     └───┘░│              ─┐     ────┘░│  │                       │░│
                     │░│                     │   │░│             ▒▓│         │░│                          │░│
                     │ │                     │   │░│    ┌──────────┘────     │░│  │                       │░│
                     │ │                     │   │ │   ─┘               │ │  │ │ ░│                       │░│
                    │ │                      │   │░└┐ │ │               │░│  │░│ ─┘                       │ │
                    │ │                      └───┘░└┘─┘ │               │░└──┘░│   │                     │ │
                    │░│                      │ ░░│ │  └─┘               │ │  └─┘ ░░│                     │░│
                    │░│                      │   │░│    │                •   │░│   └┐                    │░│
                    │░│                      │   └─┘  │ │               │ │  └─┘ ░  │                    │░│
                    │░│                      └───┘░└┐─┘░│               │░└─┐┘░│   ┌┘                    │░│
                    │░│                      │   │░└┘ │░│               │░│ └┘░│ ┌─┘                     │░│
                    │░│                      │ ░ └─┘  │ │               │░│  └─┘ │░│                     │░│
                    │░│                      │  ─┘░└─                     │ ┌┘░└─┼┐┘                     │░│
                    │░│                      └─  └─┘ •  ─────────────────  ─┘┼─┘ └┘                      │░│
                    │░└──────────────────────┘░• │░│                         │░│   ──────────────────────┘░│
                    │░│                       •  └─┘─────────────────────────┘─┘  •                      │░│
                      └──────────────────────   •                               •  ────────────────────── ─┘

                                        ┌───────┐─┐────────────────────────────┐─┐───┐
                                        │░░  ░  │ │  ░░░░░       ░    ░        │ │░░ │
                                        └───────┘─┘────────────────────────────┘─┘───┘





















```

*Figure from page 23 (2346x3317 px)*


---



4203-E P-350



SECTION 3 DATA INPUT/OUTPUT OPERATION



(1) Timing Chart for READ



r;;l _



..__Pe_r_ip-he-r_al _, L.:::.J



device



Send data



TXD



Receive data



RXD



Data



' '



\ '



\ '\ '



\ \



\ \



Data



Within 100 characters Within 100 characters



Fig. 3-18 Timing Chart for READ (DC Code Control TYPE2)



(a) The NC sends the DC1 code.



(b) On receiving the DC1 code, the peripheral device starts transferring data to the NC.



(c} After reading the program name, the NC unit sends the DC3 code.



(d) On receiving the DC3 code, the peripheral device suspends transfer of data to the NC. Data



transfer stops within 100 characters after transmission of the DC3 code.



(e) When processing at the NC is completed, the NC sends the DC1 code again.



(f) On receiving the DC1 code, the peripheral device starts transferring the data immediately



following the data sent in the last transfer operation.



(g) The NC sends a DC3 code and a DC1 code during reading of each 256-character section of



the NC program (equivalent to a tape length of 0.65 m).



(h) The peripheral device sends the end of record code and data transfer is terminated.



(i) On completion of data reading, the NC sends the DC3 code.


```text


                                                                                               ───       •
                                                               ┌──┐─┐──┐─┐─┐───┐─┐─────────────░░░───────░─┐
                                                               │░░│ │░░│ │ │░░░│ │░ ░░ ░░░░░░░░─── ░ ░░░░•░│
          ┌───────────      •       •      ────────────────────┘──┘─┘──┘─┘─┘───┘─┘─────────────
          │            ───── ┌────── ──┐───                                                                │
          └──────┐ ┌──┐      │        ░│   ────────────────────────────────────────────────────────────────┘
                 └─┘  └──────┘─────────┘───

                       ┌─ ┌────┐─┐─   ──────┐──┐
                       │░ │░  ░│ │░│ │░░░  ░│ ░│
                       └─┐   ░┌┘─┘░│ │░░░─── │░│
                         │ ───┘   • ─┘───    └─┘
                                            •



                        ┌─┐ ──┐  ┌───┐               ┌──┐              ┌───┐                    ┌──┐
                        │ └─  │  │  ░│              ┌┘ ▒│              │░ ░│                   ┌┘ ▒│
                        │░░  ─┘ │░ │░│              │░ ░│              │░ ░│                   │░ ▒│
                        └──     │░ │░└──────────────┘░ ░└──────────────┘░│░└───────────────────┘░ ░└────────┐
                            ─── └─┐ ─┘              │░┌─┘              └─┘░                    │░  ░        │
                               ─┘░│  │     •        └─┘ │    ──────────   ─┐     ──────        │░┌──    ────┘
                                │ │  └┐ ──┐ ────────┘ │   ───              └┐ ──┐      ────────┼─┘    ──
                                │░│   └─░░│         │░│    ░                └─░░│              │░│    ▒ │
                        ───┐────┘░│     │░└─── • ───┼─┼─── │░│                │░└─────┐── ────┐┘┐┘────┐░│
                       •░░░│   ░░░│     │░│   │░│   │ │    │░│                │░│     │░░•    │ │     │░│
                     ┌─ ───┘  ──┐ └─────┘ └── └─┘───┼─┼────┼─┼────────────────┘░└─────┘── ────┘ │ ────┼─┼───┐
                     │          │░│     │░│         │░│    │░│                │ │             │░│     │░│   │
                     └──   ─────┘░│ │ • └┐┘───────    │    │░│    ────────────┘─┘──────────   │ │     │░│   │
                                │ │ │  │░│        ───░ ────┘ └───┐                         ┌──┘░└─────┘ └──┐
                                   •  ─┘─┘       •░░░   ░ ░ ░░ ░ │                         │░░░░ ░░ ░░░ ░  │
                                                  ───                                      └──── ──────────┘
                                    ┌─┐────┐──────   ──┐──┐─┐───┐─┐─┐─┐───┐───┐─┐───┐────┐
                                    │░│ ░ ░│   ░░░░ ░░░│ ░│ │░░░│ │░│ │░ ░│ ░░│░│░  │░░░░│
                                    │     ─┘     ──────┘──┘─┘───┘─┘─┘─┘───┘───┘─┘───┘────┘
                   ┌─┐─────┐─┐─────┐ ─┐───  ──┐─┐
                   │░│   ░ │░│ ░░ ░│ ░│ ░    ░│░│
                   │ │ │   │ └─   •  • • │ ┌─ └─ ────────────┐──────┐──┐─┐──────────┐─┐─────────┐
                   │░│ │░ │░░░░░░│ ░│ │░░│ │░░│ │ ░ ░░░░░░ ░ │░ ░░  │░░│ │░░░░░░░ ░ │░│ ░ ░ ░ ░░│
                   │ │ └──┼─┐    │  │ │  └─┘ ─┘ │           │     ┌─ ┌─┘┐┘  ─┐   ┌──┘─┘─────────┘
                   │░│ │░░│ │░░░ ░ ░│  ░░░░░•  •░░░  ░░ ░░  │░ ░░░│░ │░ │░░│ │░░░│
                   │ │ │            │                              •       │      ┌─ ────────────────────
                   │░│ └────░░──── │░─── ░ ──░───────────────────── ───────┼─┐───░│ • ░░░    ░  ░░
                   └─┘ │     •   ░ │    ──   •                             │ │░ ░      ──────────── ─────
                       │   ──   ─── ────                ──┐ ┌────┐───── • ─┘─┘─┐──  •░
                   ┌─┐ │           •    ──                │ │    │     │ •     │  ──  ┌───┐
                   │░│ │  ░      ░░░ ░ ░   ░ ── ░ ░░░░ ░ ░│ │ ░ ─┘ ░░ ░│ ░•      │░░• │░░ │
                   │ │ │              • │                              │ │ ──────┘ •  └┐ ┌┘───────────┐
                   │░│ └─────────░ ─── ░└───░░─── ───░░░ • ░ •░ ░──░░░░│ │░░░░░ ░░░ ░│ │░│   ░ ░░░░░░░│
                    ─┘ │░░░░░░░░ ──░░░ •░ ░░──░░ •░░ ────░──░░───░░────┘ └───────── ─┘─┘─┘────────────
                   │       │             │                              •          •                  ───
                   │░│ │░░─┘─ ─────── │░─┘─┐──────  ┌───  ┌──┐────┐──┐  ░     ░    ░░░  ░    ░
                   └─┘ │              │    │        │     │  │    │░ │ ┌─────────────────────────────────
                   │      •     ─────   ───┼─────  ─┼─┐───┘── ────┘──┘─┘
                   └─┐ │   ┌────     •     │      • │ │                 ─┐──┐──────┐───┐────┐─┐─┐
                   │ │ └── │░   ░░░• ░░  │ │░ ░│  ░ │░│   │░░ ░   │░ ░ ░ │░░│ ░░░░░│ ░ │░ ░ │░│ │
                   │ │ │      ─── │ │  ┌─┘ │ ──┘─  │ ─┼─┐ │     • │     ─┘ ┌┘──────┘───┘────┘─┘─┘
                   │░│ │░ │░ │░░░░│ │░ │░│ │░░░░░│ │░ │░│ │░ ░░ ░│ ░░░░ ░░░│
                   └─┘─┘──┘──┘────┘─┘──┘─┘─┘─────┘─┘──┘─┘─┘──────┘─────────┘























```

*Figure from page 24 (2346x3317 px)*


---



4203-E P-351



SECTION 3 DATA INPUT/OUTPUT OPERATION



(2) Timing Chart for PUNCH



r;;l __



.__P_e_ri-ph_e_ra_i _. CJ



device



......



Send data



TXD



Receive data C



RXD 1



Data


# I I

Data


# I I


# J1J

Within 2 characters



Fig. 3-19 Timing Chart for PUNCH (DC Code Control TYPE2)



(a) The NC sends the DC2 code.



{b) On receiving the DC2 code, the peripheral device sends the DC1 code to the NC.



(c) On reading the DC1 code, the NC starts transferring data to the peripheral device.



(d) If reception processing for the data transfer cannot keep pace with data reception, the



peripheral device sends the DC3 code.



{e) The NC stops data transfer within 2 characters after receiving the DC3 code.



(f) After completing the processing backlog, the peripheral device sends the DC1 code again.



(g) On receiving the DC1 code, the NC starts transferring the data immediately following the data



sent in the last transfer operation.



(h) The NC sends the end of record code at the beginning of the transfer data and the DC4 code



when data transfer is completed.



[Supplement] If the times t1 , t2 and t3 overrun the set values for the ready completion waiting times for



the RS-232C channels set in the NC optional parameters (word), an RS232C device



reading error occurs.


```text


                                                                                                • •
                                                                ┌───────┐───┐───┐─┐─┐─┐─┐────── ░░░───────░│
                                                                │░░░░░░░│ ░ │░░░│ │░│░│ │░░░░░░ ───░░░░░░░─┘
           ┌──────                           ───────────────────┘───────┘── └───┘─┘─┘─┘─┘───────      ──
           │      ──    ────────────  ──────┐                                                               │
           └──────   ──┐              ░  ░  └───────────────────────────────────────────────────────────────┘
                  ───  └───────────── ──────┘

                               ┌────┐ ┌───┐──────┐─┐─
                              ┌┘   ░└─┘░  │░░░░░░│ │░│
                              └┘   ░   ░ ─┘ ─────┘ │░│
                               │ ───────  └─
                                        •

                                    ──┐       ─┐─────   ────────          ─┐───────────────┐─
                         ─────┐   ┌─ ░│      │ │      ──        │░│      │░│               │░────┐
                        │░  ░░│   │░ ░│      │░└──  │    │    • │░│      │░└─────┐    ┌────┘░ ░ ░│
                     ┌─ │░│ ──┘───┘░│▒└──────┼─┘  ──┘    └──── ┌┘ └───── │░│     │   ─┘    │░ ░ ░│ ────────┐
                     │  └─┘       │░└─┘      │░│      ──       │  │     │ ░│      ───      │░ ░ ─┘         │
                     └──    ────── ─┘ └───    ░└──────  ────── │░┌┘──── │░┌┘──────    ───── ────  ─────────┘
                                    │ │     •░│               •░┌┘     │ ┌┘
                                    │ │  │ • ┌┘             ┌─  │     ┌┘ │
                        ┌─────┐─┐   │ │ ┌┘ ░░│             ┌┘ ─┐    │░│▒│
                       ┌┘░ ░  │░│   │ │ │  │░│             │░ ░│    │░│▒│
                       │░░┌───┘─┘───┼─┼─┼─ │░└─────────────┘░░░└─┐──┘░ ░└──────────────────────────────────┐
                       └──┘         │░│ │░  •              └─ •  │  │░ ░│                                  │
                      •    ─────────┘ │ │ │   ─────────────  │      │░┌─ ──────────────────────────────────┘
                                    │ └─┘ │                  └─ ────┘░│
                                    │░ ░ ░│                  │░ ░  ░ ░│
                                     ─────                   └─┐   ──  ──────
                                                               └──

                                    ──┐───┐────────┐───┐──┐───────┐───┐───┐──┐─────────────┐
                                      │ ░ │░    ░ ░│ ░░│ ░│ ░ ░░░░│ ░░│  ░│░ │░░░ ░ ░ ░ ░░░│
                                     ─┘          ──┘───┘──┘───────┘───┘───┘──┘─────────────┘
                    ┌─┐ ┌─┐──────────  ────────┐─
                    │░│ │░│ ░░  ░░ ░   ░   ░  ░│░│
                    │ │ │ │             ──   • └─┼──────────┐─┐───┐─┐──┐───┐────┐─┐──┐─────────┐
                    │░│ │░  ░░░░ ░░ ░░ •░ • │░░│ │░ ░░░░░ ░░│ │░ ░│ │░░│░ ░│░░░░│ │░░│ ░ ░ ░ ░░│
                    │ │ │               ── ─┼─┐ • ─┐─┐─  • • •  • │ └─ │   │     ┌┘  └───      └┐
                    │ │ │░  ░░░ ░░ ░░ ░•   ░│░│ ░│ │░│ •░░• •░ ░░│  │░ │░• ░ ░ ░ │░ ░░░ ░ ░░░░░░│
                    │ │ │                        │         • ┌─┐ │  │ • •     ─┐─             ── ──┐
                    │░  └─────░░░ ────░░░────── │░─┐░░───┐░░░│ │░│ ░ │░░  ░░ ░ │░│   ░      ░    ░ │
                    └── │     ─── ░   ───  ░    │  └──   └───┘─┘─┘───┘─────────┘─┘─────────────────┘
                       •  │                    • │       │
                    ┌─┐ │ │                      │       └───────────────────┐─────────┐───┐
                    │ │ │ │ ──         ░ ── ──░   ──        ░   ░ ░ ░  ░ ░   │  ░    ░ │░░░│
                    │ │ └─┘   •    ──      •   ──   ──────┐   │ ┌──                   •    └───────┐──┐
                    │ │ │░░  •░ ░░░░░│ │░ ░ ░░░░░ ░░ ░░░░░│ │ │ │░ ░░░ ░ •░░ ░░ ░░ ░░ ░│ ░•   ░░░  │░░│
                    │ │ │            │ │              ──   ─┘ └─┘─┐  •  • • ──┐───     └─  ┌──     └── ┌──┐
                    │░  └───░░░░──░──┘─┘─── ░░░─────░░░ │░░░ ░░░░░│ ░░│ ░│ │░░│    ░░░░░░│ │░░░░░░ ░ ░ │░░│
                    └── ░░░ ────░ •░ ░░░░░░ ───░░░  ─── └─────────┘───┘──┘─┘──┘──────────┘─┘───────────┘──┘
                                                       •
                    │   ┌──────────────┐─  ─────────┐  ░░ ░ ░          •              │ ┌──    ──┐  ──── │
                    └── │              │            └──────────────────  ───────────  └─┘  ────  └──    ─┘
                        ░───   ░░──────┘  ───┐─┐───░│
                 ───────     ────            │ │    └─  ──  ─── ─── ───  •       • ─── ───── •       •
                 ░ ░░░░░ ░░░│    ──────────┐─┼─┘───░│░ ░ ░──░░░•░░ •░░░──  ──────░│ ░░•░░░░░░ ┌─────░░ ────┐
                 ───────────┘   •░░ ░░░ ░░░│ │░░░░░░└───── ░ ──░───░░──░░•░░░░ ░░─┘───░───────┘░░░░░── ░░░░│
                                 ┌─  ── ───┘─┘──────           •   ──  •  ──  • •     •          ───     •
                                 │ ──  •





















```

*Figure from page 25 (2346x3317 px)*


---



4203-E P-352



SECTION 3 DATA INPUT/OUTPUT OPERATION



3-5--4. Slave Station Function



If an attempt is made to transfer data between two OSPs, it is normally impossible because both of the



OSPs function as master stations. The slave station function allows communication between two OSPs



by making one of them a slave station.



In the slave station mode, an OSP operates in the same way as a tape reader/punch.



OSP master station l"•lf ,-------•.. ..



l_ _



o_s_P_s_la_v_e_s_ta_ti_o_n _ __,



Master station (not OSP) ------- OSP slave station



Example 1: Example connection to a peripheral device when using the slave station function



Slave station



Peripheral device



Master station



[Supplement}



EX-INT



DATA BUSY/



Fig. 3-20 Example Connection (1)



Since an EXT-INT signal is used in this example, bit 1 of NC optional parameter (bit) No.



8 (No. 13, 14, 21, 22) (Ready signals of CN0: to CN4:) should be set to "0" in advance.



(a) The timing chart for READ is the same as the one shown in 3-5-1 (Example 1).



(b) The timing chart for PUNCH is the same as the one shown in 3-5-1 (Example 2).



(c) When reading, the tape feed data following the program section is ignored.



(d) When punching, the tape feed data following the program section is not punched out.



(e) Notwithstanding c) above, if the end of record code is NULL, one character of NULL data is



punched out.


```text


                                                                                               ───       •
                                                               ┌─┐───┐─┐───┐───┐─┐─┐───┐────── ░░░───────░─┐
                                                               │░│░░░│░│ ░ │░░░│ │░│░░ │░ ░░░░░───░░░░░░░•░│
                ──           •        ─────────────────────────┘─┘───┘─┘── └───┘─┘─┘───┘───────      ──
          ┌────┐  ─────────── ────────
          │░   │   ░     ░     ░                                   •           •         •       •    ──
          └────   • ─┐─          •    ─────┐┐─── ─┐────── ┌─┐─ ───┐ ────┐─────  ┌───────  ┌┐─   • ───┐
                ┌─░• │░░ ┌─┐    ░░░   ░  ░░└┘ ░░• │ ░░    │ │ •░░ │     │     • │       │ └┘ •       └─────┐
                │    └── │░│    •               ░        │         •           ─┘       │     ───          │
                │   •   •   ┌─┐─       │ ░  ────  ░ •░ ░ │ ░░      ░   ░  ░░     ░  ░ ░░░░ │░░░░░░ │░│ •░░─┘
                └─── ░░░░ ──┘ │ ░ ─────┘───┐░░░░• •      │  •     •      ──           ───  └───────┘─┘─ ──
                │                          │  •    ───┐── ┌─ ┌─┐── ┌─┐───  ┌─┐──┐─────   ──
                │░ ░│ │░░│ │░░░ ░ ░░░░  ░  │░• •░░░░░░│ ░ │░ │░│ ░ │░│ ░   │░│░ │░ ░░░░ ░ ░•
                └───┘─┘──┘─┘───                 ──────┘───┘──┘─┘───┼─┼───    │  └────    ── •
                               ──────────┐─────                    │ │   ┌─── ┌─     ────     │
                                ░░░ ░░░░░│ ░░░  ────░│             │░│   │ ░░ │░         ───┐ │
                            ─── ─── ─────┘          ┌┘─────────────┘┐ • ┌┘─── └─── ──────   │ │
                                                 •  │               │  ─┘                   │ │
                             ┌─────  ──  ──────── │ └┐─────────────┐┘ • │ ────┐────┐────┐ ──┘ │
                             │░░░░  ░░░   ░ ░  ░ ░│ ░│             │░•  └┐░░░ │░░░ │░░░ │   │ │
                            ─┼─────────── ────────┘──              │     └────┘────┘────
                 ┌────────┐  │           •           ────────┐─┐──┐  ──┐                ───┐─┐──────┐
                 │░░░░░░░░│  │░░░ ░░│ ░░░░░░░░ •░ ░ │░░░░░░░ │░│ ░│ │░░│ │░ ░ ░ ░ │░░│ │░░░│ │░░ ░░ │
                 └───  •   ── ──────┘           │  ─┘────────┘─┘──┘─┘──┘─┘───   ──┘──┘ └───       • └─────
                      │ ──┐                     └─┐                          │               ───── ─┘     ─┐
                    │░│   │  ┌───┐─────────┐  ┌─┘░└─────────────────────────┐┘┐─   ┌────────             │░│
                    │░│ •░░  │░░░│         │  │ │ │                         │░│   ░│        │░░░░ ░░░░│  │░│
                    │░│  ────┘───┘          │   │░└┐ ───────       •     •  │  • ─┐┘        └─────────┘─ │░│
                    │░│                     └───┘░└┘─       ── ──┐─ ───── ──┘░│   │                      │░│
                    │░│                         │░│            ▒▓│           ░│                          │░│
                    │░│                     │   │░│            •              │   │                      │░│
                    │░│                     │   │░│             ▒▒          ░ │  ░│                      │░│
                    │░│                     └── │░└┐─      ──── ─────     ──┐░░│  │                      │░│
                    │░│                     │  ─┘▒└┘ ────            ┌────  │░ │ ─┘┐                     │░│
                    │░│                     │░  │ │      │░│        ┌┘      │ │  ░░│                     │░│
                    │░│                     └───┘░└──    │░│        │░      │ │  ┌┐┘                     │░│
                    │░│                     │   │░│   ┌─┐┘░│        │░ ─────┘░│  └┘                      │░│
                    │░│                         │░│   │▓│  │        │  ▒▒   │░│                          │░│
                    │░│                     ┌───┘░│   └─    ────┐───        │░│                          │░│
                    │░│                     │░░ │ │             │▓          │ │   │                      │░│
                    │░│                     └───┘░└┐           ─┘─┐     ────┘░│  ─┘                      │░│
                    │░│                     │   │░└┘───────────   └─────    │░│   │                      │░│
                    │░│                     │ │ │ │                         │ │  ░│                      │░│
                    │░│                     │ │ │░│                         │░│  ─┘                      │░│
                    │░│                     │   │░│            ▒▒           │░│ • │                      │░│
                    │░│                     └── │░│    ──      ┌┐┐─ • ───   │░│                          │░│
                    │ │                     │  ─┘░└────  ─────┐┘┼┘ • •   ── │░│    ──┐                   │░│
                   │ │                      │░░ │ │           │▓│           │ │      │                   │░│
                   │░│                       •  │░└────   ────┘─      ───  ─┼─┘                          │ │
                   │░│                     ── ──┼─┘    ───      ── ───   ── │░│  ────────                │ │
                   │░└─────────────────────     │░│            •▒░          │░│ •    ░ ░ ───────────────┐ │
                   │░                       ──  └─┘──────────── ────────────┘─┘  ────────               │░│
                    ───────────────────────   ──                               •          ──────────────┘─┘

                                               ──┐───────────────────────┐───┐
                                                 │ ░  ░ ░ ░░ ░░░  ░░ ░░░░│   │
                                                      •    ───           │
                ───────────┐    ┌─   • ───   ──  ──      •      •     ──       • ── ──  •   ───────  •   ─┐
                   ░       │   ─┘  •            │░░ ─────░░──── ░──░──░ ──────░  ░ •░░ ░ ░ ░░░░░░░░──░───░│
                 ──   •         └──░┌────── ┌── │░•░░░░ ░──░░░░░ ░ •░░──░ ░░░░░───  ░──────────────░ •░░░─┘
                   ┌─┐ ┌─┐──┐──┐    │      ─┘  •                                                   ──  ──
                   │░│ │░│ ░│░ │ ░ ░│ ░  ░▒░░│ ░ ░░ ░░░░  ░ ░░   ░  ░░░░  ░ ░    │░░░• ░░  •
                   │ │ └─┘ │       ─┘─       │                                   └──┐       ─┐
                   │░│ │░│ │ ░│░ ░ ░░    ░░░░ ░   ░    ░ ░ ░         ░         ░   ░└┐░      │
                   └─┘ │ │  • │    •       •    •  ┌─                                │   ────┘
                   │ │ │░  │ │      ░ ── •   ─── ┌─┘ • ─── •                     ───
                   │ │ │ ──┘ └──        •   •    │ │  •   •                       ░
                   │ │ │   └─┘     ──     ──        •        •       ───   ────     •   ─────┐───┐
                   │   │           ░      ░   ░   •░      ░──░──  ░  ░ ░│ •░   │ ░ │░ ░ ░░░ ░│ ░ │
                   │                    •        •               ┌─     └─ ─┐  │  ─┘────┐── ┌┘─   ┌─┐──┐
                   │░  ░ ░░░░░░░░░░ ░ ░│░│  │ ░ │░ ░ ░ ░ │░░░ ░  │░│ ░ ░░ │ │░ ░ │░░ ░░░│ ░ │░░│  │░│ ░│
                   └───────────────────┘─┘──┘───┘────────┘───────┘─┘──────┘─┘────┘──────┘───┘──┘──┘─┘──┘










```

*Figure from page 26 (2346x3317 px)*


---



4203-E P-353



SECTION 3 DATA INPUT/OUTPUT OPERATION



Example 2: Example connection to a peripheral device when using the slave station function and



DC code control



NC Peripheral device



Slave station



FG FG



Master station



[Supplement]



TXD RD



RXD SD



RTS cs



CTS 1/0 BUSY/



DSR 1/0ALARM/



SG SG



DTR DR



Fig. 3-21 Example Connection (2)



Since no EXT-INT signal is used in this example, bit 1 of NC optional parameter (bit) No.



8 (No. 13, 14, 21, 22) {Ready signals of CN0: to CN4:) should be set to "1" in advance.



(1) Timing Chart for READ



Slave station Peripheral



NC +- device



RXD DC2 Data Data DC4



ATS



Fig. 3-22 liming Chart for READ (Slave Station Function)


```text


                                                                                               ┌──        ─┐
                                                               ┌──────┐─┐──────┐─┐─────────┐───┘░░ ──────░░│
                                                               │░░░░░ │░│   ░░░│ │░░░ ░ ░░ │░░ ░───░░░░░░░─┘
           ┌──────                     ──        ─────         └────   ─┘─  ───  └───  •     •        •
           │      ┌──────┐─── ┌──────┐─  ────────     ─────────┘    ───   ┌─   ─┐    ─┐ ┌───┐ ───      ──   │
           └──────┘░     │    │      │                                  │ │    ░│     │ │   │         │  ───┘
                  └──────┘──  │░░  ░░│ │     ┌──────────────────────────┘ └──  ─┘──── │ └───┘─── •    │ •
                              └──────┘─┘─────┘                           •   ──
                          •                   ──────                               ─────────────            ──
                        ┌─ ┌─┐                      ┌─┐                         ┌─┐             ───────────    │
                        │░ │░│  ┌───┐──────────┐  • │░└─────────────────────────┘░│   ┌────────┐ ░░ ░ ░ ░  ──┐░│
                        │░ └─┘  │░░ │          └──  │ ░                         │ │ │░│        └─░░───░░ ──  │░│
                        │░│  └──┘───┘               │░┌─     ─────     ───   ───┘░│ └─           ──   ───    │░│
                        │░│                       │ └─┘ ─────     ┌─┐ •   ───   └─┘                          │░│
                        │░│                     ──┘ │░│           │█│           │░│  •                       │ │
                        │ │                    │  │ │░│              •          │░│                          │ │
                        │ │                    │░ ░ │ │            ▒██          └─┘                          │░│
                        │ │                    └─── │░└┐──    ───   ─────       │░│ ┌┐                       │ │
                        │ │                    │   ─┘▒└┘  ────    ┌─     ───────┘░│ └┘┐                      │ │
                          │                    │░ │ └─┘           │█•░          └─┘ │░│                      │ │
                       │ │                      • │ │░│  ────── • │  │ ──  ──── │░│ └─                      │ │
                       │ │                        │ └─┘ •      •   ░─┘   ──     │░│ │ ─────                 │ │
                       │░│                      │ │ │░│            ░▓│          └─┘ │                       │░│
                       │░│                      └─┼─┘░│            │ │          │░│ └──  ┌──┐               │░│
                       │░│                      │░│ └─┘            │█│          └─┘ │░ ░ │░░│               │░│
                       │░│                      └─┘ │░└─     ──  • └─┘ ───   ──┐┘░└─┘ ───┘──┘               │░│
                       │░│                      │   │░│ ─────  ──     •   ───  └┘░│ └─                      │░│
                       │░│                          └─┘                         │ │                         │░│
                       │░│                     │    │░│                         │░│ │ •                     │░│
                       │░│                     │  ░ │ │           █▓░           │░│ └─                      │░│
                       │░└─────────────────────┘    │░└────────── ──  ───────── │░└─  ──────────────────────┘░│
                       │ │                          └─┘                         └─┘                         │░│
                         └──────────────────────                                   ─────────────────────────┘
                                                ──┐────┐ ─────────────────┐───┐
                                                  │    │ ░ ░░ ░      ░░ ░ │   │
                                                         │ •
                 ────────────    ┌──  • ───── ──   •     └─      ────  ───     ───── ──  ── ────────  •   │
                     ░   ░      ┌┘░ │  ░         │░  ────░░ ────┐░ ░░░•░░░ ────░  ░ •░░░░░░░░░░░ ░░░ •░• ░└┐
                    ───         └┘──┘─ ───── ─── │░──░░░░░•░░░░░└────░░────░░░░░ ──  ░──────────────░░•░░─┘┘
                  ┌─   ─────────┘     •     •   ─┘   ───── ─────     ──     ─────  •                ── ──
                  │░│ │░ ░░░ ░░ ░  ░ •░░░░│
                  └─┘ └────────          ─┘
                                   ──────        ───────
                              ──░•░░░░░░░       •░░░░░░ ░│
                              ░ •░────────      ░────────┘
                                          ───

                                               • ─────     ───────                       ────── ──
                          ┌───         ┌─ ────┐ │     ────        ┌─┐                ───       │   ────┐
                          │░░░ ────── ─┘▒  ░  │░└────  ░░░        │░└─    ──░┌────── ░░░       │   ░  ░└─
                          └───       │░└── ───┘┐┘     ────        │░░ ┌─┐─ ░░│       ───       │     •░ ░• ─┐
                              ────── │ │       │                  └─┐░│ │  ──                  └─     ── ░│ │
                                     │░│         ────────────────   └─┼─┘░│   ─────────────────         │░└─┘
                            │         ░│                         │  │░│ │░└─                            │░│
                            └─       │░░ ────────────────────────┘░   │ │  ░┌──────────────────────── ─┐░ │
                          •░ ░───────┘░│                         │ │   ─┘ │░│                        │▒│   ─┐
                           ───       └─┘                          ─┘      └─                         └─┘    │
                               ──────                               ──────                               ───┘

                                     ┌───────┐─┐─────────────┐──────────────────────────┐
                                     │░░  ░░░│ │░░   ░░░░  ░ │░░░░  ░░░ ░ ░░░        ░  │
                                     └───────┘─┘─────────────┘──────────────────────────┘




















```

*Figure from page 27 (2346x3317 px)*


---



4203-E P-354



SECTION 3 DATA INPUT/OUTPUT OPERATION



(a) When reading operation is executed at the NC, the RTS signal is switched ON.



(b) The peripheral device outputs the DC2 code.



(c) On reading the DC2 code, the NC starts data input processing.



(d) When the NC needs to stop reading temporarily to execute processing, it switches the RTS



signal OFF. When this signal goes OFF, the peripheral device suspends data transfer to the


#### NC.

(e) On completing the backlog of processing, the NC unit switches the RTS signal back ON.



When the RTS signal comes ON, the peripheral device recommences data transfer to the NC.



(f) The peripheral device outputs the DC4 code to terminate data transfer.



{g) On reading the DC4 code, the NC switches the RTS signal OFF, terminating data reading.



(2) Timing Chart for PUNCH



Recerve data



RXD



Send data



TXD



Request ta send



ATS



DC1 DC3



Data



Clear to send



CTS



Peripheral



device



DC1



Fig. 3-23 Timing Chart for PUNCH (Slave Station Function)



DC3



Data



(a) On reading the DC1 code sent from the peripheral device, the NC executes punch processing



of the data.



(b) On reading the DC3 code sent from the peripheral device, the NC suspends punch



processing.



(c) On reading a DC1 code sent from the peripheral device again, the NC recommences punch



processing.



(d) When all the data has been punched, the NC terminates punch processing on reception of the



DC3 code from the peripheral device.


```text


                                                                                               ───
                                                               ┌───────┐───┐───┐─┐─┐─┐─┐────── ░░░─────────┐
                                                               │░░░░░░░│ ░ │░░░│ │▒│░│ │░ ░░░ ░───░░░░░░░░░│
          ┌────────         •                          ──       ────  ─┘   └───┘─┘─┘─┘ └───────      ──
          │        ┌─   ──── ─────┐────────────┐────┐─┐  ──┐───     ──  ───           •                    │
          └────────┘  ─┐░         │            │    │ │   ░│   │ │   ░           │        │ ┌──────────────┘
                   │ │ └───    ─── │           └──  └─    │   ─┘ └───────┐       │       ─┘─┘
                   │ │ │   ───     │        ──            │     •        └───────┘───────
                   └─┘ │      ─┐ • │                   ──   ░
                   │ │ └─┐     └─ ┌┘                  │  │  ──┐─┐──────┐──────┐
                   │ │ │░│ ░░░░ ░ │░    ░ ░░░  ░░  ░  │░░│ •░░│ │░ ░ ░ │░░░░░░│
                   │ │ │                                                      └──────  ───────────┐───
                   │░│ └─────┐──░░░───░░░───┐░────░░•░░ •░░░•░░ ──────░░░░░──░░░░░░░░── ░░░░░░░░ ░│ ░ ─┐─
                   └─┘ │░░░░ │░░──┐░░░───░░ └─ ░░ ──░───░───░───   ░  ─────  ───     ░  • ────   ─┘─ •░│
                       │░┌─ • ──  └───   • •   ──           •   ─────       •   •  ────  •    ───     ─┘
                       └─┘
                   ┌─┐ │  ───────────────────────────────────────┐─────┐───────────────────┐─┐──────┐
                   │░│ │░•    ░░░░░░ ░░ ░░░░ ░   ░  ░░░░░░░   ░ ░│   ░ │░░░░░░ ░░░     ░░░ │ │░░░   │
                   └─┘ │   ──────  •     ┌─     ─┐ ┌─────         │     ──────           ─┐  │       ─────
                       └───       •  │░  │ │   • └─┘      ─── ──░ └──┐   ░    ┌─░░ ░  ░░│ │░ ░░░    ░░ ░
                   ┌─┐ │    ─┐────   │   │ └┐─┐ │  └──       │   │   └┐─┐ ┌─┐ │   ┌─ ───┘─┘──────────────
                   │░│ │ ░ │░│░░░░ │ │░░ │ ░│░│ │ │░  • ░ │░░│   │░ ░░│░│ │░│ ░░░ │░•
                   │ │ │   │       │ │   │ • ┌┘┐  │ │  ───┘ │ ─┐─┘ ─┐ │ └─ • • ─┐  • ────┐─┐──┐─┐─────┐
                   │░│ │░  │░░░░░ ░│ │░ ░ ░░░│ │░ │░│ │░░░░░│ ░│ ░░░│ │░░░│ │░│ │░  ░░░░░│ │░░│ │░░░ ░│
                 ┌─ •  └───┘─   │  │ │ ─── ┌─┘─┘──┘─┘─┘─────┘──┘────┘─┘───┘─┘─┘─┘────────┘─┘──┘─┘─────┘
                 │░│ │░░░░░░ ░ ░│ │░  │░░░░│
                 └─┘ └──────────┘─┘───┘────┘

                                           ┌─                        •        •
                                          ┌┘  ────────┐──┐───────┐─┐─  ─────── ─┐
                                          │░ │░░░ ░░░ │ ░│░      │░│░ │░░░░░ ░ ░│
                                          └─ └────────┘──┘───────┘─┘─ │░░░░─────┘
                                            •                        • ────
                                                            •                    •
                                      ─────  ─┐           ┌─ ──────       ┌─      •            ┌──┐────┐
                   ┌────────┐        │       ░│           │░      ░│      │░      ░│           │░ │    │
                   │░░░     │ ───────┘ │ ── •░└┐──────────┘░│ ── ┌─┘─ ────┘░│ ── │░│ ──────────┘░│ • │░└─  ─┐
                   └────────┘        │░│      ░│          │ │    │░░░│    │░│    └┐░│          │ │   │  ░ │ │
                             ────────┘─┘    ───┘──────             │ │ ─── •      │░└──────────        ─┐ └─┘
                                           │          ────  ────── │ │           ┌┘ │                   │░│
                       ───┐                └──                    ─┘░│          ┌┘                    •   │
                   ┌──    │                │░░┌──────┐┐─┐────────┐░  │          └┘┐─────── ┌─┐───────┐░│ •
                   │░░ ───┘  ┌─────────────┘─░│      └┘░│        │░│  ──────────  │        │░│       │░│  ──┐
                   └──       │                │       └─┘        └─┘                       └─┘       └─┘    │
                                ────────────   ──────     ───────                              ──────┘      │
                   ┌────┐──────             ┌─                                                              │
                   │░  ░│   ░  │            │ ──────────────────────────────────────────────────────────────┘
                   │░┌──┘─ ────┘───────────┐ •
                   │ │    •                │  ──────────────────────────────────────────────────────────────┐
                   └─┘      │     •        │ │                                                              │
                   │░└─ ────┘ ──── ────────┘ └──────────────────────────────────────────────────────────────┘
                    ─┘                       │
                             ────────────────

                                   ┌──┐─┐──┐─┐─────────┐──┐──┐────┐─┐───┐─┐──┐──────────┐
                                   │░░│ │ ░│ │ ░░░  ░ ░│ ░│  │░░░░│ │░░░│ │░░│░      ░░░│
                                    ──┘ └─   │  ───────┘ ─┘   ──── ─┘─── ─┘──┘       •
                  ┌─── ┌─  ───────┐─   │  ──┐ ┌─        │  ───    │     │     ─┐───── ──┐─┐───┐─┐────────┐
                  │░░  │░──░░░░░░░│ ░░░│ │░░│ │░░ ░ ░│ ░│ │░░░│ ░ │ │░░░│ │░│ ░│  ░░░░░░│ │░░░│ │  ░░░░░░│
                  └───┐┘ ░░──░░───┘────┘ └──┘─┘──────┘──┘─┘───┘───┘─┘───┘─┘─┘──┘────────┘─┘───┘─┘────────┘
                      │                 •
                  │                       • ┌─┐─       ┌──────────────────  ──┐ ───────────────┐
                  └── ┌───── │    ──────── ─┘ │ ───────┘                   •  │                │
                      │░ ░░░─┘───                                                   •
                  ┌───           ───┐───────┐───────┐─┐───────────┐──────┐──┐─┐────┐ ┌─────────────────┐
                  │░  ┌────░░░░░ ░ ░│    ░░ │░ ░ ░░░│░│ ░░░░░ ░ ░ │░░░░ ░│░░│ │░░ ░│ │░░  ░░░░░░░   ░░░│
                  └───┘░ ░░─────────┘───────┘───────┘─┘───────────┘──────┘──┘─┘────┘─┘─────────────────┘
                      │
                      └────    ░•    ─┐         ──    ┌─░           ─────────┐ ──────────────────────   ──
                   ── │               │ ┌─   ───  •   │ ────────────         │ ░                ░     ──
                      └─── ░░░░ ░ ░░ ░│ │░░░░░░░  ░░ ░└─                ─────  ──────────────────────   •
                          ────────────┘─┘─────────────┘










```

*Figure from page 28 (2346x3317 px)*


---



4203-E P-355



SECTION 3 DATA INPUT/OUTPUT OPERATION



Example 3: Example connection between OSPs using the slave station function



Communication between two OSPs is executed by making one the master station and



the other the slave station.



OSP



Signal Name



TXD



RXD



RTS



CTS



DSR



RG1



DTR



EX-INT



NC Parameters OSP



Bit 7



Data 0



Optional



parameter Condition File name



(bit) No. 8 Set read



NC optional Baud Rate



parameter



(word) No. 6



2400



DC code



control



TYPE2



OSP



Signal Name



RXD



TXD



CTS



ATS



DTR



DSR



5 4 3 2



1 * 0 0



Standard 8-bit JIS Even Parity



DC code parity check



control performe



indicates either "0" or "1" can be set.



(1) For the parameters indicated above, set the same values for the two OSPs.



1 0



1 0



No ready 1-blt stop



signal bit



setting



(2) Set the channel used for the peripheral device by setting NC optional parameter (word) No. 45



(designation of punch device) and NC optional parameter (word) No. 57 {designation of read



device) in advance.



(3) Bits O to 4 of NC optional parameter (bit) No. 40 are used to select master or slave status for



each channel: set one of the two OSPs as the master station (set "O") and the other as the



slave station (set "1"),



(4) On completion of the steps above, communication between the two OSPs will be possible.


```text


                                                                                                ──        •
                                                                ┌─────┐─┐───┐─────┐─────┐───────░░•░──────░┌─
                                                                │░░░░ │░│ ░ │░░░░ │░░░░ │░░ ░░░░──░•░░░░░░─┘
           ┌──────        ────        • ─────────    ────     ──┘───  └─┘  ─┘─ • ─┘───  └──────      ──
           │      ┌───────    ───────┐ │         ┌───    ┌───┐      ──   ──   • •     ──                    │
           └──────┘░                 │ │         │     • │  ░│ │             │                           ───┘
                  └───────── ┌─   ───┘─┘────┐────┘┐     ─┘    ─┘    ────    ─┘       ──   ───────────────
                             │░░ ░░░ ░ ░░░░ │░░░░░│ ░░│ ░░░░ ░ ░░░░ ░░░ ░│ ░░░░ ░ ░ ░ ░┌─  ░░░  ░░░   ░  │
                            ─┘ • •   ────┐   ─┐  ─┘┐──┘──────────────────┘─────────────┘ ────────────────┘
                             └─    ──    └─── └──  │
                                                                       •
                              •  ░░│            •                   ┌──░──          ──┐
                             │░ ─┐ └─────────┐    │                ┌┘  │  ┌─────────  │░│
                             │ │ │ ░░ ░░ ░░░░│  │░└────────────────┘░│ └┐░│ ░░ ░░░    │░│
                             │░│  ─────░░┌───┘──┼─┘                │░│  └─┘┐─░░┌────  │░│
                             │░└──      ░│      │░│                │░└──   │  ─┘    ──┘░│
                             │░│      •░░│      │░│     ───────    │░│      │░░│      │░│
                             │░│     │░ ░ ┌─────┘░│ ────       ────┘░│  ─── │ ░  ───  │░│
                             │░└─────┘ ░░░│     └─┘                │░└──   │ ░░│    ──┘░│
                             │ │     │░░──      │░│                │░│     │░ ─┘      │░│
                             │░│     │░   ──────┘░└─       ────────┘░│     │░   •     │░│
                             │░└─────┘░ •░      │░│  ──────        │░└─────┘░──┐      │░│
                             │ │     │░░░│      │░└──              │░│     │░░░│      │░│
                             │░│     └┐ ░│      │░│                │░│      │  │ ─────┘░│
                             │░│      │░ │      │░│                │░│      └┐┐┘      │░│
                             │░└──────  ░│ ─────┘░│                │░│       └┘ ──────┘░│
                             │░│         │      │░└───             │░└──────          │░│
                             │░│     ┌─░░└┐     │░│   ─────────────┘ │                │░│
                             │░└──── │░░░░└───  │░│                │░│ ─── ──░─┐ ──── │░│
                             │░│    ┌┘░   │   ──┘░└────────────────┘░└─     ░•░│     ─┘░│
                             │ │    │░░ ░░│     │ │                │░│                │░│
                             └─┘    └─────┘       │                └─┘                │ │
                     ─┐─                   ──────                     ────────────────
                  ┌── │ ──────────────
             ─────┘                   │ •   ──   ──   •    •   ──   • • ──   ──  ──   ── ─┐───────────   ───
          │ │     └───┐      │        │  ┌─┐  ┌─┐  ┌─┐ ──── ┌─┐  ┌── │ │  ┌─┐  ──  ┌─┐  │ │           ┌─┐   ─┐
          │░│         │   ┌──┘  ──┐─┐ └──┘░│  │░└──┘ │  ░   │░│  │   │ └─ │░│ •    │░│  │ │ │ │  │ │  │░│  │ │
          │░└─────┐   │  ─┘░░└┐─  │ │ │  │ │  │░│  │   │ │  │ │ •  • │ │  └─┘  ──┐ │░└──┘░│ │ │  └─┘  │░│  │░│
           │ ░░░░░└─┐  ┌─   ░ │ │ └─┘ └─ │░└── ─┘─  ┌──┘─┘─┐ ░└─        ──  │ │░░└─┘ │  │░ │  └─  ░│    └─  ░│
           │░░░░░░ ░│  │░░  ──┘ │  ░     │     ░░░  │░░░ ░░│  │  ──────  ░░│ ─┘┐  ░░┌┘  └┐░└┐─░░░ •  ░  ░░•  │
          │░┌───────┘ │ ┌───     ────────┘ ──░░░┌─  │ ──░░┌┘  └──       ───┘   │ ░░░└┘─  │░░│░─┐─┐░┌──────   │
          │░│         │░│      │         │   ───┘  │    ──┘   │      •      ───┘ ░┌─┘  ░  │░│ ░│ │ │       │ │
          │ │        ─┘░└─    ─┘ │ ──      │       │░•        │                └──┘  ─── ─┘─ ──  │░│       │ │
          │        ──  •  ────  ─┘┐   ┌────┘───────┘            ─┐        ┌────         •       • ─┘───────┘
           ────┐───░░─┐░ │░░ ░ ░░░│ │░│            │       ░    ░│ • │ ──┐┘░  ░ ░░│
          │░░░ │░░░░• │░┌┘─┐    ──┘ │░│            └─────────────┘─  └─  └┘───────┘
          │░ ░ ░░ ░• •  │  │░░ ░    │░│
           ──────       └──┼────  ──┘ │
                  │ ┌─┐─┘  │          └────────────────────────────────────── ────────────
                  │ │ │   ─┘─    ─────                                          ░
                  │ │                                                      │               •   ──── ──  ─┐
                  │ │  ─────┐───────────┐ ┌─────░░ ░░ • ░ •░░ ──────░░ • ░░└──░░░░░ ░░ ░───░───░░░░ ░░──░│
                   •  │ ░░░░│░░   ░░░ ░░└─┘░░░ ░─────░░──░░───░ ░░░░───░───░░ ──────────░░░░░░░────░•░░░─┘
                      └─────┘───────────┘  ─── •     ──  ──    • ───   •   ──            ─── ──    • ───
                  ┌─  │
                  │ │ │░───     ┌──── ──░   •      ┌────── ──┐┐ •     ──    ─────────────  ───  ────   │
                  │ │ │         │            ░   • │░  ░  •  └┘  ─────  ───                   •     ─┐ │
                       │░░   ░░• ░ │░░ │ │ ░ ┌┐  ░│ •░ ── ░   ░  ░░░░  ░░░░░─┐░───── ░ ░  ░ •░░░─┐┐ ░└─┘
                      ┌┘────┐──░───┘───┘─┘   └┘   │  •    ── •   ────  ───── └─        •     ─── └┘ ─┘
                  ┌─┐ │     │             ┌──  ┌── │  ────  • ┌─┐    ──     •  ┌──────┐ ─┐──    •  •
                  │░│ │░│   │░░░░│  ░ ░ ░ │░ │ │░░ │ │░░░░░░░░│░│░ │░░░░ ░░ ░│ │░░ ░░░│  │░       ░ ░│
                  └─┘─┘─┘───┘────┘────────┘──┘─┘───┘─┘────────┘─┘──┘─────────┘─┘──────┘──┘───────────┘




















```

*Figure from page 29 (2346x3317 px)*
