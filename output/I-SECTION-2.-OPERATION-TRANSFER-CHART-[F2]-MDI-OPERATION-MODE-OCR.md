# I SECTION 2. OPERATION TRANSFER CHART [F2] MDI OPERATION MODE OCR

*Converted from PDF: I-SECTION-2.-OPERATION-TRANSFER-CHART-[F2]-MDI-OPERATION-MODE-OCR.PDF*

---



4203-E P-15



SECTION 1 FOREWORD



(2) MDI Operation Mode (1/2)



F1 DATA INPUT Used for manual data in- F1 SET • Used to set new data



put operation



F2 ACTUAL. POSIT. Used to display coordi• F2 ADD Used to add the input data



nates of the actual position to the currently stored data



F3 PART Used to display list of a F3



PROGRAM part program



BLOCK DATA Used to display the data in F4



one block



SEARCH Used for page search in F5



check data display



ATC/APC Used to display ATC/APC F6



status



CHECK DATA Used to display check F7 QUIT Used to quit the data set·



data ting mode



[EXTEND] Extensive functions FS



F1 LIBRARY P. SET Used to register library F1



programs



F2 PARAM F1 SET Used to select F1 -digit F2



feed (parameter type)



F3 TOOL DISPLAY F3



F4 PERSONAL Used to display print data F4 POT SEARCH Used to execute search



by a pot number



F5 DIAGNOSIS Used to change display F5 TOOL SEARCH Used to execute search



page for the other axes by a tool number



F6 AXIS CHANGE Used to display messages F6



F7 MESSAGE Used to set new data F7 QUIT Used to quit the tool dis-



play mode



Fa [EXTEND] Extensive functions Fa



F1 TOOL LIST Used to select !he tool list FILE SELECT Used to select the tool list



mode



F2 RELATI. Used to zero set the rela- F2 USE TOOL Used to display the tool list



ZEROSET live position data



F3 RELATI. Used to preset the relative F3 DISUSED TOOL Used to display the disuse



PRESET position data tool list



F4 LACK TOOL Used to display the lack



tool list



F5 F5



F6 F6



F7 F7 QUIT Used to quit the tool list



mode



FS [EXTEND] Extensive functions F8


```text


                                                                                                 ┌─
                                                                                     ┌─┐───┐─┐── │░─────────┐
                                                                                     │░│░░░│░│   └─░░░░░░░░░│
           ┌──────   •                    ──  ───────────────────────────────────────┘─┘───┘─┘          •
           │      ───  ───────────────────  ──                                                              │
           └─        • ░░     ░      ░  ░     ┌─────────────────────────────────────────────────────────────┘
              •     •  ───────────────────────┘
               ┌───┐  │                                                 ───
               │░ ▒│ ┌┘░  ─┐──── ──    ┌───────┐─────┐─               ┌─   ───┐        ┌───┐─┐──────┐
               │ ┌─┘ │     │    •  •   │░░░░░░░│     │                │   •   │        │   │ │     ░│
               │░│   │     │        │  │       └─────┼─┐              │  •    │         ───  │      └───
               │░│   │     │     ── │  │░░ ░░░░░░░░░░│ │             │       ┌┘         ░░░  ░░░░░░░░ ░░
               │▒│   │    ┌┘─────  •   │        ┌────┘─┘             │     ┌─┘         ─────────────────
               │▒└─┐─┘─   │░░░   ─┐    │░░░░░░░┌┘                    │  │  │
               │   │░░    └────   └─   │      ─┘     ─┐─             │  │  │
                  ─┘┐──┐          │    │░░░░░│ ░  ░ •░│         ┌────┼─┐   │
                    │  │ ─┐     ┌─┘    │     │ │     ─┼─      │ │    │░└─  │
             ┌──────┼─ │  │     │      │░░░░░└─┘──┐   │       │ └────┘     │
             │░ ░░  │░│  ░│     │      │          │ ──┘       │ │    │     │
                    │ │ ──┘     │      │░•░───────┘ ░ │       │ │    │     │
           │        │░│   │      ──┐   │  │         ┌─┘       │ │    │  • ░└──┐          •   ─────┐───┐  ──
           │ ┌──────┼─  │ │ ░   •  │   │░░│      ░  │         │ │    │   • │  │         │░───░░   │░ ░│    │ │
           │ │      │  ─┘─┘       ─┘   │ │         ┌┘         │ │    │  • ░└──┘         └─   ─────┘───┘  ──┘ │
           │ │  ────┘ │░░  ░  ░░┌┐     └─┘─     ░  │  ─┐      │ │    └─ ░─┐                ──              │ │
           │ │ │    │ │         └┘───  │           └─  │ •    │ │         │                                │ │
           │ │ │ ┌──┘ └─ ░  ░───       └──┐──        ┌─       │ │    ┌─    │                               │ │
           │ │ │ │  │               │  │░░│░░│       │   ─────┘ │    │     │                               │ │
           │ │ │ │  │  ░   ░      ░ │  │  │ ─┘────┐─┐   •     │ │    │  ░ ░│                               │ │
           │ │ │ │  │         •     │ •░░░░░░░░░  │░│ ──        └────┼─    │                               │ │
           │ │ │ │  │  ─────── ──   │  ───────────┘─┘                │░── ░│                               │ │
           │ │ │ │  │    ░         ─┘                ─┐───────────── └─    └───┐────┐   ───    ──  ─────┐  │ │
           │ │ │  ──┘ ──┐ ┌────────    │      ░  ░  •░│              │ ┌─┐     │  ░ │  │ ░░────░ ─┐ ░░░░│  │ │
           │ │  •   │   │ │            │              │              │ │ │ │   │    │  │░──░░  ──░└─  ──┘  │ │
           │ │      │   │░└────────    └─────────────┐               │ └─┼─┼──┐ ┌───┘┐ │            ──  │  │ │
           │ │      │  ─┘─┘            │░░░░░░░░░░░░░│               │ │ │░│  │ │    │ └─ ░░──░░ •░ ░░░░│  │ │
           │ │      │     │            └─────────────┘               │ │ │░└──┘─┘────┘ │░───░ ───░──────┘  │ │
           │ │      │ ────┘      ───   │              ┌─             │ └─┘░│                              │ │
           │ │      │      ─────       └─   • ░───░  ░│              │  ░ ░└──┐           •   ──   ─────┐─┼─┘
           │ │      │ ┌─┐  ░░░░░┌──    │░──  ░•░  ────┘─             │ ┌─┐    │        ─┐░░ ──░░ ░    ░░│ │░│
           │ │      │ │ │ ┌─────┘            •  •                    │ │ │ ┌──┘         └─── ░──────────┘─┼─┘
           │ │      │ └─┘░│            │  ──  •  •                   │ └─┘░│                ──            │ │
           │ │   ───┘  ░ ░│  ░ ░───────┘░         ─┐ ────┐                 │                              │ │
          │    │     • •  │  ┌──       │           └─    └───────────┐     └───┐───             ──        │ │
          │ │  │ ┌──┐   │ └─ │   │     └──            ┌─┐            │  ░ ░│   │       ┌────────  ─────┐  │ │
          │ │  │ │  │ ──┘ │      │     │░░│           │ └─────────── │     │   │  ┌─   │               │  │ │
          │ │  │ │  │  ░ ─┘─┐──┐─      │  └──┐───┐    │              │░     •  │  │    │               │  │ │
          │ │  │ │  │  ─┐  ░│ ░│       │░•░░░│ ░░│    │              │       • │  └─   │                • │ │
          │ │  │ │  │  ░│░     └─     •         ─┘    │              │     │     •  ─┐ └───┐           │  │ │
          │ │  │ └─ │   └─ ░░░│        │░░░ ░░┌─  ────┘              │     │    •    │ │░░░│           │  │ │
          │ │  │ │  │░ ░  ┌───┘        └──────┘                      │  ░ ░│       •   │   │          ─┘  │ │
          │ │  │ │  │░│   │                                          │     │  ─────    │░░░│         │    │ │
          │ │  │ │  │░└── │                                          │     └──         └───┘─────────┘    │ │
          │ │  │ │  │░    │                                          │░    │                              │ │
          │ │  │ │  │░ ░  │                                          │░ ░  └──┐           ───────────┐    │ │
          │ │  │ │  │     │                                          │ ──  │  │        │░  ░ ░  ░    │    │ │
          │ │  │ │  │    ░└─────┐     ┌───────────┐   •              │░   ░└──┘        └─────────────┘     │
          │ │  │ └──┘  ░       ░└─────┘░░         └─── ──┐           └┐    │                             │ │
          │ │  │          ──────┘      ─────  ───        └─────────── └────                              │ │
          │ │  │ ┌────────       ─────            ───  ──                  ──────────────────────────────  │
          │ │  └─┘        ─────                      ──  ─────────────────                                │ │
          │ │  │░│                                                        ────────────────────────────────┘ │
          │ └──┘░└───────────────────────────────────────                                                 │ │
          │ │  └─┘                                       ─────────────────────────────────────────────────┘ │
            └──   ───────────────────────────────────────                                                 │ │
                                                          ────────────────────────────────────────────────

















```

*Figure from page 1 (2346x3317 px)*


---


## 4203-E P-16


## SECTION 1 FOREWORD


## MDI Operation Mode (2/2)

A F1 GRAPHIC Used to display the pro- F1 SET Used to set new data



gram in graphic display



mode



F2 TRACE/ Used to select display F2 ADD Used to add the input data



ANIMATE mode between tool paths to the currently stored



and animation data



F3 TOOL KIND Used to switch ON/OFF F3



tool kind display



F4 MATERIAL; Used to display workpiece F4



material shape



F5 GRAPHIC Used to clear graphic dis- F5



ERASE play



F6 DATA ON/OFF Used to switch ON/OFF F6



the display in the graphic



display area



F7 HIGH DRAW Used to switch ON/OFF F7 QUIT Used to quit the data set-



the high-speed drawing ting mode



mode



FS [EXTEND) Extensive fune1lons F8



F1 GRAPHIC Used to display the pro· F1



gram in graphic display



mode



F2 GRAPHIC DATA Used to selee1 the drawing F2



mode



F3 AUTO SCALE Used to automatic setting F3



of the drawing area



F4 F4



FS AREA CHANGE Used to select the area FS MAKER Used to change the mark-



change mode er position



F6 ANGLE Used to selee1 the view F6



CHANGE angle change mode



F7 F7 QUIT Used to quit the area



change/view angle change



mode



F8 [EXTEND) Extensive functions F8



To PLC check screen mode


```text


                                                                                                 •
                                                                                    ┌─┐───┐─┐── │░░────────┐
                                                                                    │░│░░ │░│   └──░░░░░░░░│
          ┌───────────                       ───────────────────────────────────────┘─┘───┘─┘         ───
          │            ─────────────┐────────                                                               │
          └───────────┐░        ░   │░       ┌──────────────────────────────────────────────────────────────┘
                      └─────────────┘────────┘
                     •
               ┌─┐                    ┌─────────────┐                 •   ───┐         ┌──────────┐─┐
               │ │  │ │   ┌─────      │░░ ░ ░░░░░░░░│                │       │         │     ░    │░│
               │ │  └─┘── │           │ ░           │                │ ─── │ │
               │ │  │░░░ ░└────┐      │  ─────┐─┐───┘─               │ ░   │           ┌──┐────────────┐
               │ │  │ ┌┐ •░░░░░│      │ ░░░░░░│ │░ ░                 │ │  ░└──         │ ░│ ░░░░░░░░░  │
               │ │  │░└┘        ─┐    │  ░ •░ │     ┌─               │ └┐  │           └──┘────────────
               │ │  │ │░•      ░░│    │ ░ ░ │ └┐ ░ ░│                │░░│  │
               │ │  │  │ │      ┌┘    │  ░│ │░░│ •  └─┐         ─────┘  │  │
               │ │  │ ░│ │░ ░░░░│     │ ░ │ │ ░└┐ ░ ░ │      ┌─┐     │ ░│  │
               │ └─ │ ─┘ │     ─┘     │░░ │ │░┌┘┘     │      │ └─────┘  │  │
               └─   │░░│ └─────       │░┌─┘─┼─┘░░   ░│       │ │     │ ░│  │
                 ───┘    │  ░░ ───┐   │░│   │        │       │ │     │  │  │
                    │░░░ ░┌───    │   │ ░───┘───░───┐┘       │ │     │░░│  │
                    │ ┌── │   •   │   │░ ░░░    •░░░│        │ │     │ ┌┘  │
                    │░│   │  • ──┐    │ ░  ░ •               │ │     │ │   └──┐         ───  ─────┐───┐ ────
                      │         ░│    │░░     ──░• ─┐        │ │     │ ░•  │  │        │░░ ░•   ░ │░ ░│     │
                    • │   │     ─┘    │  ░┌───  •░• │        │ │     │     └──┘        └─── ░─────┘───┘ ──┐ │
                     ┌┘┐──┘────┐      │   │                  │ │     │ ──  │               ──             │ │
                 ─── │░│  ░  ░░└───── │ ── ───    •     •    │ │      │ ░ │                               │ │
              │ │    └─┘       │      │                •     │ │      │   │                               │ │
              │ └── │ ░     ░  │      └───────────── •       │ │     │ ░• │                               │ │
              │ │   │     ────        │░░ ░░░░░░░░░░│        │ │     │ •  │                               │ │
              │ │   └────     ─┐───┐  │ ░│       ─┐ └─┐──────┘ │     │  ──┘                               │ │
              │ │   │ ░░  ░ ░░░│   │  │ ░│  ░ ░   │░  │      │ │     │ ░░ │                               │ │
              │ │   │          └─ ┌┘  │░░│        │   │ ─────┘       │    │                               │ │
              │ │   │ ░░  ░   ░ ░ │   │ ░  • • ░─┐░░  │              │ ░░ │                               │ │
              │ │  │     ─────────┘   └──── • ── └────┘              │    │                               │ │
              │ └──┼─────                               ────────────┐┘─░• │                               │ │
              │ │  │░       • •    │  ┌─────┐─┐── ┌─┐               │░ •  └────┐       ┌──────┐───────┐   │ │
                   │     │     ────┘  │░░░░░│░│   │ │               │ │ •      │       │░░░░░░│ ░    ░│   │ │
                │  │░│░│░└────┐      •        └───  │               │░│  ░┌────┘       └──────┘───────┘   │ │
                └──┼─┘─┘  ░░░░│       │░░ ░░░░░░░░ │   ─────────────┼─┘   │                               │ │
                │  │    ░┌────┘─      └────────────┘                │     └───          ──────────────  ──┘ │
                │  │   │ │                                          │  ─┐              │░░░░░░░░░░░░  ─┐  │ │
                │  │  ─┘ └─────┐      ┌──────────┐      •   ┌─┐──┐  │   │ ┌──          └────────────── │  │ │
                │  │  ░░│ ░ ░  │      │          │     │ ┌──┘░│  │  │ ┌─ ░│                               │ │
                │   ────┘──────┘      └──────────┘     │ │       └──┘─┘  ─┘                               │ │
                └──              ─────             ────┘     │         ░│ └───────────────────────────────┘ │
                │                                       ─────┘──────────┘                                   │
                └───────────────────────────────────────                 ──────────────────────────────────


































```

*Figure from page 2 (2346x3317 px)*
