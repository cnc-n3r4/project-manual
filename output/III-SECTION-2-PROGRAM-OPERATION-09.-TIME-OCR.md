# III SECTION 2 PROGRAM OPERATION 09. TIME OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-09.-TIME-OCR.PDF*

---


## 9. Time

4203-E P-267



SECTION 2 PROGRAM OPERATION



The NC's clock function contains counting time even when the power is turned off. Therefore, when the



power is turned on, the current time is displayed.



NOTICE : Sincethistimedataisveryimportantforthefunctions such as MacMan, alarm log, etc., do not



change it inadvertently.



The operating procedure is as indicated below.



(1) Press function key [F1] (TIME).



The following is displayed on the console line and the system becomes ready for the lnput of time.


#### 1994.9.30 FRIDAY 15:13:52

enter time (H:M:S)!



=EX

1994. 9.30 FRIDAY



enter time (H:M:s)



15: 13:52



BLANK



INIT DELETE RENAME DEF I NE FREE



Press [F1J (TIME).



"=T



1994.9:30 FRIDAY15:13:52



enter time (H:M:S)!" is displayed.



RUN



QUIDE [EXTEND]



(2) Key in the present time through the keyboard: hours, minute, and second, each delimited by":".



Example: 8:30:5



(3) Press the WRITE key.



When time data has been entered correctly, the screen displays the set date, day of the week, and



time.



If time data has not ben entered correctly, the screen displays "enter time (H:M:S)!" again,



requesting the operator to enter correct data.



[Supplement] 1. When time data only needs to be checked and does not need to be set, simply



press the WRITE key. The TIME command will terminate.


## 2. The data setting range is as follows.

Hour 0through 23



Minute 0 through 59



Second 0 through 59


## 3. After 23-hour 59-minute 59 second, the time changes to 0-hour 0-minute 0-second

and the date and the day of the week change.


```text


                                                                                                • •       •
                                                                         ┌────────┐───┐─┐───────░░░───────░│
                                                                         │▒░░░ ░░░│   │░│░░░░░░░───░░░░░░░─┘
             ──────      ──────────────────────────────────────────────── ────────┘─  └─┘──────       •
           │       ┌───                                                                                     │
           │░┌──── │░░ ──┐ ─────────────────────────────────────────────────────────────────────────────────┘
           │░│     └─┐─░░│
                  •  │     ──┐────────────────────────────────┐─┐───┐─┐─────────────────┐─┐─────────┐───────
                 • ░•░░ ──░░░│ ░░░░░░  ░░░░░░░ ░░ ░░ ░ ░░░ ░ ░│ │░░ │░│    ░░     ░  ░ ░│ │░   ░    │░    ░
                •     ──   ──┘ ───────   ────              ───┘─┘───┘─┘─────────────────┘─┘─────────┘───────
                     │                │                 ░                                                   │
           ───── ┌─┐─┘     ┌──────────┘  ──┐   ───     ──┐ ─┐───────────────────────────────────────────────┘
          •░░▒░░ │▓│▒│  •  │░░░░ ░░ ░░░•░░░└───░ ░  ░░░░░│ ░│ ░░ ░░░░░ ░░ ░░░ ░░ ░░░░░░░ ░░░ ░ ░░ ░░   ░  ░░│
           ──────┘─┘─┘── │ │ ░░   • ──   ──               ──  • ────────────────────────  ─── ─── ───     ──┘
                        ─┘─┘   ░░  •          ░───────────                                                  │
                │░ • │░░ ░░ ───────░░─────────░░░░░░ ░░ ░░ ─────────────────────────────────────────────────┘
                └─┐ ┌┘┐                        • ┌────────
                  │░│ │ ░░░ ░ ░░░░• │░│ ░░│ ░ │░░│
                  └─┘─┘    ┌──   │  │ └── └─┐─┘─┐┘┐─┐────┐─┐────────┐─┐──────┐────────┐────────┐─┐──┐──────┐
                      │░ ░ │░░░░░│ ░ │░░░░░░│ ░ │░│ │░ ░░│ │ ░ ░ ░ ░│ │░░░░░ │░░ ░░░  │░░░ ░░ ░│ │░░│ ░ ░░░│
                      └────┘─    └─  └──   ─┘─  └─┘─┘────┘─┘────────┘─┘──────┘────────┘────────┘─┘──┘──────┘
                             ┌──┐  ──   ───   ┌─
                             │░░│ │ ░ ░░░░░░│ │░ │░ ░│
                             └──┼─┘ ─────░  │ └──┘───┘
                                │ └─     ───┘
                        ┌─┐  •  │                                                           ┌─┐
                        │ │   ┌─┘                                                           │ │
                        │ │   │░└┐       ──       ┌──┐───┐                                  │ │
                        │ │   │░░└───── │░ ────   │░ │░ ░│                                  │ │
                        │ │ ──░──┘    ░ │░ ░ ░ ── └─ └───  ──     ──     ──┐─    ─┐─ ────── │ │
                        │  │       │ │    ─┐     •        •  ┌───┐  • •    │ ┌─┐  │ │       │ │
                        │  │ │ │ │ │ │     │      •   ────   │ ░░│   │ •  │  │ └─   └┐───── │ │
                         │ └─┘ │░│ │  │    │       •   ░░░   │░•░░   │░   │  │░ ░│   │░ ░░    │
                         │ │░└─┘  • ─┐┘  ──┘                │       •    │      ─┘ │ │  ─┐─ ──
                          │    ░     │ ░░     ░░░ ░ │ ┌─┐   │ ░░     ──┐ │   ░ ░  ─┘─┼─  │
                          │  ──┐┐ │░ ░───  ──  ── ░ │ │ │ ░   │░   ░ ░ │ ░ ░ ░┌─ ░   │░  │
                          │    └┘ └───        •     └─┘   ─── └────────┘──────┘  ────┘───┘
                          │ ┌─┐           ────░┌─   ░ ░░│    •                 ──
                         │  │░└───────░░│ ░░░░░│ •  ────┘
                         │  └─░ ░     ──┘──────┘░ ░│
                 ┌─┐  ┌──┘─     •                  └──┐──────┐─┐───┐─┐─────┐─────┐────┐─┐──┐─┐────────────┐
                 │░│  │░░    ░░ ░──░░ │░░  ░░░░ ░░ ░░ │░ ░ ░░│ │░ ░│ │░░░ ░│ ░ ░ │░░░ │ │░ │ │░ ░ ░░░     │
                 └─┘  │  ──┐─ ┌─┐     └───────────────┘──────┘─┘───┘─┘─────┘─────┘────┘─┘──┘─┘────────────┘
                     •░░│░ │░░│ │░░░ ░│
                   •  ┌─┘  │ │ ─┘     └─
                   ░  │  •  ░│  ░░░   │ ─┐
                  ──  │ • •              └─┐──────────────────────────────────────────── ─── ──────────  ──
                      │░░░  ░░░  ░░░     ░░│   ░      ░ ░ ░         ░  ░       ░       ░
                      └── ┌────────────────┘───────────────────────────────────────────────────────────  ───
                     │    │
                     │     │ │ ── • │   │ • •       • ┌───   │ │   ┌────┐ ┌──────   ──┐   ─┐─┐        ─────
                      │   ┌┘─┘  ░   └───┘─   ──      ─┘   ┌─ │ └───┘    │ │ ░     ──  │ ── │ └────────  ░
                      │░░░│   ░ ░ ░ ░░░░░░─── ░ ────   ───┘░─┘                                        │
                ┌─────      ┌───┐───┐          │                  • ─────  •  • ───     ───┐───┐──┐─┐─┼────┐
                │ ░░░░░░ ░░░│   │   │░ ░┌─┐░░──┘──────┐  ░•░░ ───┐ ░░░░░░── ░░░│░░░────  ░░│ ░ │░ │░│ │ ░░░│
                └───────────┘   │   └───┘ └┐─░░░░░░ ░░└───░── ░░░└─ ──░•░ ░────┘░•░  ░░ ───┘───┘──┘─┘─┘────┘
                               ┌┘┐  │      │ │                           •      •  ───
                               │ │  │░░░ │░│ │░░░░│ ░░░• ░ ░░ ░░ ░░│
                               └─┘  └────┘─   ────┘───┐           ─┘
                                          ░─┐         │ ──░░ ░┌─░│
                                          │ │  │       │      │  │
                                          │ └─ └─      │ ┌┐──░│ ░│
                                           ─┘ ─┘        ─┘┘  ─┼─
                               ┌─┐  ┌─────   •   ───────    • │  ────────────────┐─────┐─┐─────────────────┐
                               │ │  │░░░ ░░ │░│ ░░ ░░░░░░ ░░░░   ░░ ░░ ░ ░ ░░░ ░░│ ░ ░ │░│   ░░  ░░   ░  ░ │
                               └─┘  └──  ───┘ │ ───────┐ ┌───░───┐  ┌───    ┌────┘─────┘─┘─────────────────┘
                                        •    • •       └─┘   •   └──┘   •  ┌┘
                                                                         ──┘














```

*Figure from page 1 (2346x3317 px)*
