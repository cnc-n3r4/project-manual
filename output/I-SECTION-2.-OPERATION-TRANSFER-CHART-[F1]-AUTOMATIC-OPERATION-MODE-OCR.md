# I SECTION 2. OPERATION TRANSFER CHART [F1] AUTOMATIC OPERATION MODE OCR

*Converted from PDF: I-SECTION-2.-OPERATION-TRANSFER-CHART-[F1]-AUTOMATIC-OPERATION-MODE-OCR.PDF*

---


# Operation Transfer Chart

(1) Automatic Operation Mode (1/2)



F1 PROGRAM Used to select a part pro-



SELECT gram in the directory-



based selection mode



F2 ACTUAL POSIT. Used to display coordi-



nates of the actual position



F3 PART Used 10 display list of a



PROGRAM part program



BLOCK DATA Used IO display the data in



one block



SEARCH Used for page search in



check data display



ATC/APC Used to display ATC/APC



status



F7 CHECK DATA Used to display check



da1a



F8 [EXTEND] Extensive functions



F1 LIBRARY P. SET Used to register library



programs



F2 PARAM F1 SET Used to select Ft-digit



feed (parameter type)



F3 TOOL DISPLAY



F4 PERSONAL Used to display print data



F5 DIAGNOSIS Used to change display



page for the other axes



F6 AXIS CHANGE Used to display messages



F7 MESSAGE Used to set new data



FB [EXTEND] Extensive functions



F1 NUMBER Used to execute sequence



SEARCH number search



F2 RESTART Used to execute sequence



restart



F3 NUMBER STOP Used to execute sequence



stop



SP SELECT Used to selec! schedule



program in the directory-



based selection mode



SPNO. Used to execute schedule



SEARCH program number search



F6 NEW SP ENTRY Used to register new



schedule program in the



directory-based selection



mode



4203-E P-13



SECTION 1 FOREWORD



To the mode in the program



~ operation mode



F1 SET Used to set new data



F2 ADD Used to add the inplll da1a



to the currently stored data



F7 QUIT Used to quit the data set-



ting mode



F4 POT SEARCH Used to execute search



by a pot number



F5 TOOL SEARCH Used to execute search



by a tool number



F7 QUIT Used to quit the tool dis-



play mode



To the mode in the program



operation mode



FB [EXTEND] Extensive functions 7


```text



                                                                                     ┌─────┐─┐── │░─────────┐
                                                                                     │░░░░ │░│   └─░░░░░░░░░│
              ──────                         •       ────────────────────────────────┘─────┘─┘          •
            •       ──      ──   ─┐──         ───                                                           │
           │░ ──────░░───   ░ •   │░ ─┐─────  ░ ░───░───────────────────────────────────────────────────────┘
           └──      •░░░▒┌────░░──┼─┐▒│░░░░░• ───░▒░│
                     ──┐─┘     •  │ └─  ──       ───┘
                  •    │         │         ░  │
              •     •  └─────────┘────────────┘─────
              ░┌───┐  •
             │ │▒▒▓│  ░░  ────────     ┌───────────┐ ─┐  ──────────────────────────────────────┐
             │░  ──┘ │ │  ░░░░░░       │░░ ░░░░░░░░└┐ │                ░░░░    ░░░░░░░░░  ░ ░  │
             └─┐░    │ └┐─  ───┐  ──┐  │░░░ •░░░───░│    ─────────────┐────  ────────────  ───
               │░┌─  │ ░│  │   │ • ░│  │            └┐─┐              │     │            ──   ───┐───┐
               │░│   │  │  │      ──┘  │░░ ░ ░░░│░░░░│ │              │     │ │         │        │   │
               │░│   │░░░ ┌┘─────      │       ┌┘────┘─┘              │     │ │         └────────┘──┐┘┐─┐
               │░ ─┐─┘░   │░░ ░  ──    │░ ░░░░┌┘                      │     └─┘         │░░░░░░░░░░░│░│░│
                •  │░ ░░  └┐──┐──  │   │     ─┘                       │░    │           └───────────┘─┘─┘
                  ─┘─┐   •░│  │   ─┘   │░░░░░                         │     │
                     │  │ │   │  •     │     ──┐───   │          ────┐┘     │
             ┌───────┘  │ └─ •  │      │░░░░░░░│░░░•  │       │ │    │░     │
             │  ░    │  │ │     │      │   ┌───┘───   │       │ └────┘┐     │
            •       │   └─    ┌─ │     │░░░│          │       │ │     │    │
           │ │      │░     │  │ ─┘──   │  ┌┘         •        │ │     │    │
           │ └──────┘┐──   │  │        │░┌┘         │         │ │     │     │                            ┌───
           │ │       │     │     ──    └─┘ •       ┌┘ ───     │ │     │    ─┘──         ┌───────────┐──┐ │   │
           │ │       │     └─────      │           │ │   │    │ │    │ •                │░░░░░░    ░│  │ └─┐ │
           │ │  • ── │                               │   │    │ │    │   •  ───         └───────────┘──┘   │ │
           │ │ │ │   │    ┌──────────   ┌────────────         │ │     ───░┌─                               │ │
           │ │ │ └──┐ ──  │ ░░░    ░   ┌┘░   ░░░  ░ ░ ──      │ │        ─┘                                │ │
           │ │ │ │  │   ┌─┘         │  │ ░   │       •   ─────┘ │     ┌─  │                                │ │
           │ │ │ │  │   │ │ ░░░   ░ │  │ ░   └──────┐         │ │    ┌┘   └┐                               │ │
           │ │ │ │  │    ░          │ │ ─────       └┐          │    │     │                               │ │
           │ │ │ │  │  │ │ ───────  │ │              └─       ┌─┘    │  ┌─ │                               │ │
           │ │ │ └──┼─ │░│ ░░░░░░  ─┘ │  ░    ░•     ░  ──────┘ │    │  │ ░└─                              │ │
           │ │ │    │░ │ │ ───── •     ┌─       •  ─┐ •       │ │    │ ─┘┐░│   ──────   ┌────────────────┐ │ │
           │ │  ────┼── •       •      │░░│░ ░░░░░░░└─        │ │    │   │ └──          │░░░ ░░░░░░░ ░░  │ │ │
           │ │      │     │        •   └──┘─────────┘         │ └────┼─┐ │ │            └──────────┐───  │ │ │
           │ │      │  ░ ░│                           │       │      │░│░  │            │          │   ──┘ │ │
           │ │      │  ─┐─┼──  ─────                  │         ─────┼─┘── │            │░░░ ░░░░░░░       │ │
           │ │      │   │ │                          •               │     │            └────────────────  │ │
           │ │      │  ░    ─────┐     ─────── ┌── │                 │  • ─┘                               │ │
           │ │      │  │ •       │    •        │   │                 │    ░└──┐            ── ──────────┐─┐┘┐
           │ │      │  └─ ┌──────┘     •        • ┌┘                 │ ┌─┐─┘  │         ┌─░░ •░░ ░   ░ ░│ │░│
           │ │   ┌──┼─    │      └───── ──────── ─┘ ──               │ │ │ └──┘         │░───░──────────┘─┘┐┘
           │ │ │ │  │     │                                          │ └─ ░│                 •             │ │
           │ │ │ └──┘     └┐───  ──────          ─┐────              │  ░                                  │ │
           │ │ │ │  │   ┌─ │░░░─┐      ┌──┐─┐───┐ │░   │               ───                                │ │
           │ │ │ │  │  ┌┘░ │    │      │  │ │░  │ │    │                                                  │ │
           │ │ │ │  │  │  ─┘──░─┘      │░ └─┘───┘  ░  ░│                                                  │ │
           │ │ │ │  │           └───┐  │ ░│            │                                                  │ │
           │ │ │ │  │       │░░• ░ ░│  │░┌┘     ░      │                                                  │ │
           │ │ │ └──┼─┐     └──   ──┘  │░│            ─┘ ─────         ─────       ── ────────┐           │ │
           │ │  ─┘  │░└─┐  ░ ░   │     └─┼──────────░│        ┌─       ░ ░    ░───  ░•      ░ │           │ │
           │ │      └─┘ │      ──┘─    │░│░░  ░░░░░░ │   ─────┘  ──    ────────  ░ ── ────────┘           │ │
              ───── │ └─┘░────┐        │             └┐       │ │              ────  •                    │ │
          │  •  ░ ░  ░│ │  ░░░└┐       │░• ░┌─░░░ ░░░░│       │ │                                         │ │
          │ │ ──────┐   │    • └────┐ •   │ │        ┌┘  ─────┘ │                                         │ │
          │ │       │      ░       ░│  ┌──┘─┘░░───░  │          │                                         │ │
          │ │       │     ┌─────────┘  │░░░░░░░░░░░░░│  ────────                                          │ │
          │ │       │ ─── │           ─┘─────────────┘                                                    │ │
          │ │       │  ░ ░│                                                                               │ │
          │ │       │    ░└──────     •   ────────                                                        │ │
          │ │     ──┘─ ░ ░       ─────             ────                                                   │ │
          │ │  ┌─┐    ──────────       ───────────                                                        │ │
          │ │  │░└───                                                                                     │ │
          │ └──┘░│                                      ──────────────────────────────────────────────────┘ │
          │ │  └─┘                                                                                        │ │
             ──   ──────────────────────────────────────────────────────────────────────────────────────── •












```

*Figure from page 1 (2346x3317 px)*


---


## 4203-E P-14


## SECTION 1 FOREWORD


## Automatic Operatfon Mode (2/2)

F1 TOOL LIST Used to select the tool list F1 FILE SELECT Used to select the tool list



mocle



F2 RELATI. Used to zero set !he rela- F2 USE TOOL Used to display the tool list



ZEROSET tive position data



F3 RELATI. Used to preset the relative F3 DISUSED TOOL Used to display the disuse



PRESET posttion data tool list



F4 F4 LACK TOOL Used to display the lack



tool list



F5 F5



F6 F6



F7 F7 QUIT Used to quit the tool list



mode



F8 [EXTEND] Extensive functions F8



F1 GRAPHIC Used to display the pro- F1 SET Used to set new data



gram in graphic display



mode



F2 TRACE/ Used to select display F2 ADD Used to add the input data



ANIMATE mode between tool paths to the currently stored



and animation data



F3 TOOL KIND Used to switch ON/OFF F3



tool kind display



F4 MATERIAL; Used to display workpiece F4



material shape



F5 GRAPHIC Used to clear graphic dis• F5



ERASE play



F6 DATA ON/OFF Used to switch ON/OFF F6



the display in the graphic



display area



F7 HIGH DRAW Used to switch ON/OFF F7 QUIT Used to quit the data set-



the high-speed drawing ting mode



mode



F8 [EXTEND] Extensive functions F8



F1 GRAPHIC Used to display the pro- F1



gram in graphic display



mode



F2 GRAPHIC DATA Used to select the drawing F2



mode



F3 AUTO SCALE Used to automatic setting F3



of the drawing area



F4 F4



F5 AREA CHANGE Used to select the area FS MAKER Used to change the mark•



change mode er position



F6 ANGLE Used to select the view F6



CHANGE angle change mocle



F7 F7 QUIT Used to quit the area



change/View angle change



mode



F8 [EXTEND] Extensive functions ~ Fa



To PLC check screen mode


```text


                                                                                                ┌──
                                                                                    ┌───────┐── │░░░───────┐
                                                                                    │░░░░░░░│   └───░░░░░░░│
          ┌───────────         •                   ─────────────────────────────────┘───────┘         ─────┘
          │           ┌───────┐ ┌────────────┐─┐───                                                         │
          └────   ────┘░      │ │         ░  │ │   ─────────────────────────────────────────────────────────┘
               ┌─      ───────┘─┘────────────┘─┘───
               │░│                                                     ─┐─
               └─┘  ┌──  ─┐──── │     ┌───┐─┐─────────┐              ┌─ │ ─┐───────    ┌───┐───────────┐
               │ │  │  ── │     └─    │░░░│ │         │              │     │       •   │ ░ │          ░│
               │ │  │░ ░ ░└────┐      │   └─┘┐──┐     │ ─────────────┘     │      │     │  │            │
               │ │  │    │░░░░░│      │░░░░░░│ ░│    │               │     │      │     │░•   ░░░   ░   │
               │ │  │    │     └─     │  ─┐  │ ─┘  ┌─┘┐              │░    │      └──┐  │               │
               │ │  │    │░░░░░│      │░░░│░│░│    │░ │              │░    │   ░     │  └──┐ ░░ ░ ░ ░   │
               │ │  │░    ┌────┘      └───┘─┘─┘────┘──┘              │░ │ ░│  ┌─  ┌──┘ │   │          ┌─┘
               │ │  │     │                                          │  │  │░ │   │    │ ░░│ ░  ░    ░│
               │ └─ │░ ──░│                                           ──┘  └──┘───┘    └───┘──────────┘
               │    │  ░ ░│                                          │ ░│  │
               │ ┌─ │  │  │                                          │  │ ─┼─┐
               │ │   ──┼─ │                                          │░─┘ ░│ │         ─────          │  •
               │ │  │  │  └────┐       ┌──────────                   │    ░└─┘          ░░░ ──────────┘   │ │
               │ │  └─░└─ ░   ░└─┐   ┌─┘░    ░    ────┐─┐────────────┘┐░• ░│            ───               │ │
               │ └──┘ •   ┌────  └───┘                │░│             └─░──                          ─────┘ │
               │ │  │     │    •                      └─┘────────────       ─┐         ──────────────       │
               │ └──┘ ┌── ░░   ░┌─────┐───   ░░░    │                │░    ░░│           ░   ░  ░ ░░
               │ │  │ │  │      │     │░░░──────────┘                │ │ │░┌─┘
               │ │  │░│  └─────┐      │                              │░│ │░│ │             ────────────┐
               │ │  │ │  │░░░░░│      └┐░─────┐░░░░░│                │ │ │░│ │         ─┐─┐  ░░░░ ░░░ ░│
               │ │  │ └┐  ┌───┐ │     └┘─░░░░░│ ────┘                │   │ └─┘          │░└────────────┘
               │ │  │░░│ ░│   │ └┐    │     │                        │░•   │             •
               │ └──┘   • │ ──  └┘    │░░░░░│░░│ ───┐                │     │
               │ │  │    •      │     │     │  │    └─┐        ┌──── │░• • │
                  ──┘           │     │░░░░ │░░│      │      │ │     │  │  │
                    │░░░ ┌───── │     │ ┌───┘──┘     │       │ │ ────┘  │  │
                    │    │░░░░  └─┐   │░│            │       │ │     │  │  │
                    │░░░ ░ ───    │   │  ────┐───────        │ │     │  │  │
                    └────░│   ────┘   └──░░░░│ ░░░░░░│       │ │     │ ─┘  │
                    │     │  •        │░ ░ ░░       ┌┘       │ │     │  │ ─┼──                ────  •
                    │ ░  ░│░  ░ ░│    │░░     ───   │        │ │     │░░ • │           ┌──────       ─┐  • •
                    │ │   │ •   ─┘    │  ░┌───░  ───┘        │ │     │ │  ─┼───        │░░░░░░ ────── │   │ │
                    │ └┐  └─ ───      │   │                  │ │     │ └─  │           └──────          ──┘ │
                ────┘  │  ░  ░ ░│ ────  ░            ───┐    │ │     │  ░  │                              │ │
               •     │ │      ──┘     •                 │    │ │     │  │ │                               │ │
              │  ───┐┘ │         ────   │ ──┐───┐───┐─ •     │ │     │  │ │                               │ │
              │ │   │     ┌────┐      ┌─┘ ░ │░░░│░░░│        │ │     │ │   │                              │ │
              │ │    ──┐─ │    └───┐  │ ░ ──┼─┐─┘─── • ──────┘ │     │ └── │                              │ │
              │ │   │ ░│  │        │  │  │  │ │       │        │     │    │                               │░│
              │ │   │  │ ─┼───    ┌┘  │░░│        •   │ ───────      │    │                               │ │
              │ │   │ ░│  │       │   │   ────────    │              │ ░  │                               │ │
              │ │   │     └───────┘   │░░ ░░░░░░░░ ───               │    │                               │ │
              │ └──┐┘─░──             │   •    ───                  │     │                               │ │
              │ │  │░ •   ──────────  └─── ───┐   ──┐  ─────────────┘     └────┐       ───────────────┐─  │ │
                   │                  │░░ ░░░░│     │               │░    │ ░░░│        ░░ ░ ░░ ░     │   │ │
              │ │  │░•   ──────┐────  │        •    │               │    ░└────┘       ───────────────┘─  │ │
              │ └──┼─ ──  ░░░░ │      │░░ ░░│░░░░░  │               │░ ░  │                               │ │
              │ │  │     ┌─────┘      └─────┘───────┘  ─────────────┼─    └──┐                 ── •      ┌┘ │
              │ │  │ ──┐ │                                          │ │ │  ░ │         ┌───░──   • ░───┐ │░ │
              │ │  │   └─┼─────                                     │ │ │ ┌──┘         │░░░  ░───░•   ░│ └┐ │
              │ │  │  ░ ░│     │      ┌───────────       ─────  ─┐  │  • ░│            └──────   •  ───┘  │ │
              │ │  └─────┘─────┘      │                ┌─ ░      └─┐┘  ░ │                                │ │
              │ │                      ───────────     │  ────░ • ░│  ───┘                                │ │
              │ └─────                            ─────          ──┘─      ───────────────────────────────┘ │
              └─                                                                                            │



















```

*Figure from page 2 (2346x3317 px)*
