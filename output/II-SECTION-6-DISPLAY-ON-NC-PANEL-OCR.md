# II SECTION 6 DISPLAY ON NC PANEL OCR

*Converted from PDF: II-SECTION-6-DISPLAY-ON-NC-PANEL-OCR.PDF*

---



4203-E P-114



SECTION 6 DISPLAY ON NC OPERATION PANEL


# SECTION 6 DISPLAY ON NC OPERATION PANEL

This section describes the contents of NC STATUS lamps on the NC operation panel, contents of the



information displayed on the operation mode screen, and the information displayed on the special screen



such as NC HOUR METER screen.


## 1. Status Indicating Lamps

On the NC operation panel, the following six NC status indicating lamps are arranged, and the current NC



operating status can be confirmed from the lamp which is lit.



RUN S.T.M



~gm ,



c~R:::Rf~n'f:::M:::, L I M I T ALARM



Lamp Name Function



RUN This lamp lights when NC is computing the axis position.



S.T.M This lamp lights while the NC is executing the processing for the S



(spindle function), T (tool function), and/or M (miscellaneous function)



command.



SLIDE HOLD This lamp lights when the SLIDE HOLD switch on the machine operation



panel is pressed.



PROGRAM STOP This lamp lights when the NC ls in the program stop or the optional stop



status. It flickers while the dwell command is being executed.



LIMIT This lamp lights if the calculated axis position is on or beyond the soft-limit



position.


#### ALARM This lamp lights when an alarm comes on.

This lamp does not light when a warning message comes from an opera-



tion mistake.


```text


                                                                                                 ──
                                                              ┌─────┐─┐───┐───┐──┐─┐──┐─┐─┐──────░░• ──────┐
                                                              │░░░░░│░│ ░ │░░░│ ░│ │░░│░│ │░░░░░░──░• ░░░░░│
                                                                            ──         ─┘  ── •            │
                ──────────            •     ──                                  •                           │
           ┌┐░─┐░░░░░░░░░░│  ─┐      │░ ───░░░───░─┐  ┌───┐─┐───┐ ┌─┐─░ ───────░░ ───── ───────────┐ ───────┘
           └┘▒▒│░░───▒•░•░│░ ▒│      │░░▒▒▒▒•░▒░▒▒ └─░│▒▒░│ │▒▒▒│ │░│▒░░▒░▓▒░▒▒░ │▒░▒▓▓ ░▒░▒▒▒▒▒▓▒▒│
             ──┘──   • • ─┘───┘       ────── ──────┘  └───┘─┘─── ─┘─┘────────────┘─────────────────┘
                   •           ─────                                                                    ──
                 │░░• •░ ░  ──    ░ • ┌──   ░  ░┌─  •░• •░░   ░ │  ─┐ ┌─ ┌─ │ │ ─── ──   ┌───┐ │   ──  │   │
                 │                    │         │               │   └─┘ ─┘ ─┘ └─ ░    ───┘   └─┘ ──  ┌─┘── └┐
                 │      ░     ░  ░░───┘──  ░░  ░░  ░  ░░ ░░░░░  ░ ░ ░░ ░░░ ░░░   •░░░░░░░ ░░ ░░ ░░░░░│ ░░░░└┘
                 │ ░• •░ ░• •░░ ░• ░░ ░░░ ░░░░░────────────────────────────────── ───────────────────┘─────┘
                  •                       •
           ┌─┐     ┌───┐───┐─┐──────────── ┌───────┐
           │░│     │▒▒░│▒▒▒│ │▒▒▒▒▒░▒▒▒▒░▒ │░▒░░░▒░│
           └─┘     └───┘───┘─┘──────────── └───────┘
                 │                                         ───    ──────┐────────┐─────┐──┐─┐────┐──────────┐
                 └─── ───  • ░   •   ░  ────── ░░░ ░ ──────░░░────░░░░░░│ ░░░░░ ░│ ░ ░ │░░│ │ ░ ░│ ░ ░░░░ ░░│
                 │░░░░░ ░ ░░░ ───░│ ───░░░░░░░░──░───░░ ░░░░──░░░ ──────┘────────┘─────┘──┘─┘────┘──────────┘
                  ────────────   ─┘    ────────  •       ───
                                                      ──      ───       ───  •  ────
                            │░│ ───────────────── ────░░──   •░░░──  ┌──░░ ─┐  │░░░░──   ─┐
                            └─┘  ░░░░░░░  ░░░░░░░   ░░░░░░   ░░•░░░  │░░   ░│  │░░░░░   • │
                                 ───────── ─────  ────────        •   ──────┘   ────     ─┘
                  ─────                                                               •
                ┌─     ──────────┐                                   ┌───────┐────────   ──────────────────
                │ ┌─     ░░░ ░░░░│     •                             │░ ░░░░░│                             │░│
                │░│  • ──┐ ░ ░───┘──    ─────────────────── ────  ───┘       │  ──    ──           ────────┘░│
                │ └──    │  ░░░     ─── ░░ ░░░░░░░░░░░░ ░░░• ░░ ── ░░░──░────┼──░░────░░┌──┐               │░│
                │ │      └──────────   ─┐░░░─┐─┐─── ░░• •░░░  ░ ░░  ░ ░░░░░░░│░░░ ░░░░░░│░ └───────────    │░│
               │ •                      │ ░│ │░│   ───░  ────────── ░ ───────┘────░──░░░└─░░ ░ ░   ░   • ──┘░│
               │  ────             ─────┘ ░│ │░░ ░                                •  ───  ──   ──          │░│
               │      ─────────────     │░░     ──┐───  ───  ────────  ────   ───            ──   ──────── │░│
               │ │     ░ ░░░ ░░░░░    ── ░ ░  ░•░ │░░░─┐░░░  ░░ ░░ ░░░ ░░░░░ ░░░░──┐ ──────░•░░░ ░░░░░░    │░│
               │ │ ─┐──      •    ──┐─  │░░ ░  ░•░░░░░░│   │    │                  │                       │░│
               │░│  │░░░░░░░░░░░░░░░│   │░░░│░░░░ │░░░│ ─┐─┼─┐─┐┘─┐────────────────┘──┐    • ───────────┐  │░│
               │░│  └─────   ───────┘   │ │░│   ░ │░░─┘  │░│ │░│ ░│ ░    ░ ░  ░ ░  ░░░└────░• ░    ░   ░│  │░│
               │ │        ┌──           └─┘░└── ░ │░░░ ░ ░░░░░░│ ░░░░ ░░░░ ░░░░│░ ░░░░ ░░░░░░░│     ──  └─ │░│
               │ └─    • ┌┘░░░░    ─── │░░░░│ ░ ┌─┘────────────┘───────────────┘──────────────┘─┐┐ │ ░ ░░░ │░│
               │ │ ────  │    ───     ─┘░░░░░░┌─┘                                               └┘─┘─────  │░│
               │░│       ░░ ░░░░        ┌──┐──┘ └─┐────────┐ ── ──  ────────                               │░│
               │░└──────────────        │  │      │░       └─   ░            ┌──────┐─┐─────────┐─┐─┐────┐─┘░│
               │░│                      └─░░ │░───░░┌──────░░┌────────────░──┘ ░░░░░│ │ ░░░   ░ │░│ │░░ ░│ │░│
               │░└────────────          ░░ • │░░░░░┌┘      ──┘            •   ──────┘ └─────────┘─┘ └──── ─┘░│
               │                        ─── ─┘─────┘                                                       └─┘
                 ───────────────────────            ───────────────────────────────────────────────────────



































```

*Figure from page 1 (2346x3317 px)*


---


## 2. Actual Position Display

4203-E P-115



SECTION 6 DISPLAY ON NC OPERATION PANEL



When function key [F2] (ACTUAL POSIT.) is pressed in the operation mode, the actual position data



screen is displayed.



The actual position data is displayed in the following three absolute position data display modes and also in



the relative position data display mode. The display screens can be changed by using the page keys.



2-1 . Actual Position Display



For page [1] of actual position data display, two display modes are provided, double extension mode and



four-fold extension mode. Which of the display mode should be used can be set using NC optional



parameter (bit) No. 4, bit 6.



(1) Page [1] (Double Extension)



Main program name currently selected



Last sequence name executed in main program



File name currently selected Block counter



AUTO OPERATION



39.500 0 TST9


### -Y 185.850 N

-1100.000 F 0.0 H 0



0 D 0



A-Mtd



CHECK



SEARCH DATA [EXTEND]



The symbol "-" appears before axis address



on which the mirror image function is active. Running method currently selected



Fig. 6-1 Actual Position Display-Page [1] (Double Extension)



The following display data items are in common to the two actual position data display screens I1]



(double extension and four-fold extension) and also to actual position display screen [2].



X X-axis actual position on active block



Y Y-axis actual position on active block



Z Z-axis actual position on active block



CO Work coordinate system number



O Currently active program name


```text


                                                                                               │ •
                                                             ┌──┐─┐────┐─┐───┐──┐─┐─┐──┐─┐─────┘   ─┐─────
                                                             │░░│ │░░░ │ │░░░│░░│ │░│ ░│ │░░░░░░───░│ ░░░░░•
             ──────                               ─────────── ──┘─┘────┘ └───┘──┘─┘─┘──┘─┘─────        ────
           ──       ──── ───────────────────                                                               │
          •░  ─────░░ ░░•  ░░░  ░░░░  ░ ░░░ ──░  │ ────────────────────────────────────────────────────────┘
           ──      ─────░─────┐──────┐─────░░░──░└┐
                 ┌─           │      │            └────┐────────┐───┐───┐──────┐───┐─┐─┐──┐────┐─┐────┐─┐───┐
                 │░────░░░────┘─── ░░│ │░░░ ░░│ │░░░ ░ │░ ░░░░░░│ ░ │░  │░░ ░░░│ ░ │░│ │░ │░░░░│ │░░░░│ │░░░│
                 └─    ───░       ───┘─┘──  ──┘ └────   • ──────┘  ─┘─ ─┘────── ── └─┘ └──┘────┘─┘────┘─┘───┘
                •     │                   ──   •     ─── •       ──   •        •  │   •
                 │░• ─┘ ░░░ ░░░ ░ ░░• ░ •░ ░░░ ░  ░ │░ ░ ░  • ░    ░  ░   •   ░   │░│ ░  ░ •
                 └─ │             •    •          ┌─┘      •░│                      │          │    │    ┌┐─
                 │░ │     ────     ──   ────┐──   │ └─  • ░  │         │░──  ──░  ░░│ ░  ░░ ░ ─┘ │░░│ │░░└┘
          ┌───┐   ┌─┘─────    ┌─┐─    •     │  ───┘   ── ──── ─────────┘─  ──  ───── ───────── └─┘──┘─┘──┘
          │░ ░│   │░░░░░░ ░░░░│▒│░│ ░•░░░░░│
          └───┘  ─┘┐              │    ─── └──┐───────────────── ────────────────────────────────────── ───
                │ ░│░░─┐ ┌─────░░░░ ──░░░░•░░░│ ░░░░░  ░░ ░░░░░░│░░░░░  ░░ ░  ░░░   ░░░░░ ░░░░ ░ ░ ░  ░│ ░ •
                │    • │ │     ───┐    ──┐  ──┘  ────      ┌─── │ │    ┌─ ┌─┐  ┌─   •  •   ─┐        │ │    •
                │ ──              │      └──         ──    │   ─┘─┘    │ ─┘ │  │ • • ── │ • │   ┌────┘░ •  •
                │░░░░░░░░ ──────┐ ░ ───░│              ────┘       ────    • ──   •    ─┘─ • ───┘     ── ──
                └┐─┐──   •      └───    └──────┐
                 │░│  │░│░│░  │░░░░░│ ░░░░ ░░░░│
                 └─┘  └─┘─┘───┘─────┘──────────┘        ┌────────────── ────────────
                                                        │░░░░░░░░░░░░░░•░░░░░░░░░░░░─┐ ───────────
                                •  ──  ────   ────      └────────░───░ ░  ──░   ░  ░░└┐   ░     ░
                              ──░──  ──    ───    ─┐             •   ─────  │░       ░│ ──────────
                             │                     └──                      └┐  ──────┘─
                          ┌──┘                        ────           ────    └──
                          │    ┌─   ──   ─┐           ░░  ──    ──  •   ░──┐     ──┐  •
                         │  ───┘░│ ░░░░• ░│          ─────░░      ┌┐░░░░░░░│     ░░│   │
                         │ │   └─┘  ┌── ──    •   ──       ────── └┘    ┌──┘─  ────┘ │ │
                         │ │      │░│        ░░  ░ ░│                  ┌┘    ──      │ │
                         │ │      └─┘        ───────┘    ──       ─────┘             │ │
                         │ │      │ │               │                                │ │
                         │ │     ─┘─┘      ────┐────┘    ─┐              ──┐────     │ │
                         │ │        │        ░░│ ░░░     ░│              ░░│  ░░     │ │
                         │ │    │  │                │    ─┘              ──┘────     │ │
                         │ │   ┌┘  └┐   ──┐──┐─┐─┐──┘   │ │        ┌───┐─       ─┐   │ │
                         │ │   │  │░│     │░ │░│ │░░│   │░│        │░ ░│ ░│    │░│   │ │
                         │ │  │  ─┘─┘   ──┘──┘─┘─┘──┘   └─┘        └───┘──┘    └─┘   │ │
                         │ │ ┌┘ │                                                    │ │
                         │ │ │  │                         │            ┌──┐      │   │ │
                         │ │ │            ┌────           │          • │ ░│      │   │ │
                         │      │         │  ░░                          ─┘          └─┘
                         │     ░│         └──── │                                    │ │
                         │     ░│               └┐                                   │ │
                         │    │  ──── ─────     └┘─  ─┐──      ─┐────┐─  ─┐──┐       │ │
                         │░│ ┌┼──░░  •░░░ ░─────┘ ░──░│  ────┐─ │    │ ┌─░│  └┐────┐   │
                        ┌┘░│ └┘ ░──  ░░░•   ░░░░░  ░░░│   ░░░│  │   │  │░░│   │   ░│   │
                        │ │  │       ──      ────  ───┘  │   │   •  │  │      │  ──┘  •
                       │  │        •                  ░──┘ ┌─   │ ┌─   │  │ • │ •    •
                       │    • •░   ░• •░│ │░ ░░     ░┌─░ ░ │▒ ░ │ │▒│  │░ │ ░• │░│ ░•
                      │      │     │ •  │ │          │   ░─┘──  └─┘─┘   ──┘    └─┘
                     ┌┘  ────┘░ ┌──┘░░░░└─░░░──░░  ░░ ░┌──    ──     ──    ────   ────┐
                     └┘  ░░░░░░░│ ░░────░░░•░░░░────░░░│  • •░░░░░░ •░░░░ ░░░░░░░░░░░░│
                      └─ ───────┘───    ─── ────    ───      ──────  ─────  ──  ──────
                                     │     │      •    ────┐─      ┌─     ──  ─┐      ────┐
                                     │ ░   │░░░│  ░░░░░░ ░ │░░░•   │░│ ░│ ░░░░░│ ░ ░│ ░░░░│
                      ┌─                     ──┘  •  ───  ─┘───   ─┘─┘─ │   ───┘   ─┘──
                      │ • ┌──────  ───── ┌───   ──                     •  ──     ──     ─┐───  ──  ─────────
                      └─ ─┘      ──    ░─┘░       ────────┐  ─┐───    │ ──   ────    ─── │   •  ░•░  ░
                      │░  ░░ ░░░░░░░┌──░░ ─────░░ ░░░░░░░░└──░│ ░░░•░ │░░░░ ░░░░░░──░░░░░│ ░░░░• ░░────────
                      └─┐──────┐    │                            ── ── ───────────  ───── ───── ───
                      │ │      │░─┐░└─┐░░░────┐░░   │ │░░░░  ░░─┐
                      │ │      │  └─┘ │ •     └──   │ └───      │
                      │ │      │  │ │ └─ •    │  ── └─┘   ────  │
                      │░│      │░ │░└─┘░░░░ ░ │░ ░ ░│ │ ░•░ ░  ┌┘
                        └┐     │      │             │ │     ┌──┘
                       │░│     │░░░• │░░ │░░░• •░░░░│ │ ░░░░│
                       └─┘     └─── ─┘ │ │  • • │   │ │    ┌┘
                                 ░ ░░ ░│ │░ ░ ░ │░ ░│ │░░░░│
                                ───────┘─┘──────┘───┘─┘────┘









```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-116



SECTION 6 DISPLAY ON NC OPERATION PANEL


#### N Currently active sequence name


#### F Actual feedrate {overridden programmed F value)

S Actual spfndle speed {overridden programmed S value)



H Tool length offset number



D Cutter radius compensation number



[Supplement] Actual position display of additional axes



In the double extension display mode:



1st additional axis data is displayed below "Z-axis".



2nd and 3rd additional axis data are displayed in the next page, which is accessible



by pressing function key [FBJ (EXTEND) and [F6] (AXIS CHANGE).



In the four-fold extension display mode:



1st to 3rd addition axis data are displayed in the next page, which is accessible by



pressing function key [F8] {EXTEND) and [F6] {AXIS CHANGE).



(2) Page [1] (Four-fold Extension)



AUTO OPERATION TST9.MIN OTST9 N13



97/07/15


# X 39.500


# Y 185.850


# Z -1100.000

:oPR



=PO



=PO


## 33 0 TST9

PAOOW.1 ACTUAL PAAT BLOCK



SELECT POSIT. PROGRAM DATA



SEARCH


## 0.0

CHECK



DATA [EXTEND]



Fig. 6-2 Actual Position Display Page [11 (Four-fold Extension)


```text


                                                                                                 •        •
                                                             ┌──┐──────┐─┐───┐──┐─┐─┐──┐──┐─────   ─┐───── ░
                                                             │░░│░░░░░░│ │░░░│░░│ │░│ ░│ ░│░░░░░───░│ ░░░░░•
           ┌───────────   ──────        •                     ──┘──────┘─┘───┘──┘─┘─┘──┘──┘────        ────
           │           ┌─┐      ──────── ──────┐──────┐─┐────                                              │
           └───────────┘░└──────           ░   │      │ │                    ──────────────────────────────┘
                       │ │      ┌─┐───  ──           ─┘      ──────┐───┐───┐
                       │ │      │░│ ░░ ░░░•░░  ░────░░│  ░ ░░░░ ░ ░│ ░ │░░░│
                       │ │      │                            ─┐    │  ─┘ •  ┌────┐
                       │░│      │░•░░ ┌──░░░──░░░░    ░│░░░░  │░░░░░ ░░░│ ░ │░░░░│
                       │ │      └─   ─┘   •    •      ─┘───── └─────────┘───┘────┘
                       │ │      │ ───  ░            ──       •
                       │        │  ░░────  ────  ─── ░       ░ •
                 ──────┘ ───    │   •     •    •         │      ─────
                │░    ░    ░│   │░ ░ ░    ░   │░  ░│    ┌┘░
                └───────────┘   │             └─┐  │   ─┘     •   ───
                                │  ░┌─ ░ ░░┌┐░░░└──┘░ │░ •░• │░░░
                                └───┘      └┘        ┌┘   • ─┘    ───────┐───┐──┐
                                     •░ ░░░░░░ ░ ░░░ │░─┐ ░•░░░░░░░░ ░░ ░│ ░ │░░│
                                    │                   │   │                      ──────   ────────────────┐
                                    │░ ░ •░ ░────░░── ░░│░░─┘░░────────░░░░░ ░──┐ •░░ ░░░───░░░░ ░ ░░░░░░░░░│
                                     ──── ───    ──░ ──┐ ──░░──░ ░ ░░░ ──────░░░│  ░  ───░░░ ░┌─────────────┘
                                ┌──┐                   │            • •      ─── ─────   ─────┘
                                │  │░ ░   ░░░ ░░░░░░░░ │░░░░░ ░░░░░
                                └──┘                                ────┐─  ─┐─ ──────    ── ───┐───────┐──┐
                                     │░─────░ •░░░░───░░──░░░───────░░░░│ ──░│ •░░ ░░░────░░│ ░ │░░░░░░░│ ░│
                                     └─     ── ────   ──░ ──░ ░░░ ░░────┘ ░    ░░ ░──░ ░░░ ░│ ──┘───────┘──┘
                      ───  ──────  ──               ──  ──  ───── ──     ───  ─────  ───────┘
                   ░     •     ░ ─┐              │
                  ──  ─── ──────  │ ──           └───
                         •      •               •      ─┐────   ──────
                              │   │ │ │ •               │░   ─┐       ┌───┐──┐──── ───   │
                            │ └── │░│ │░░───┐─          └──░░░│       │░░░│░░│      ▒░•  │
                            │ │  ─┘─ ─┘     │ ─────────    •           ┌──   └────────   │
                            │ │         ┌─┐                  ┌─┐──┐  ──┘░░──░│         │ │
                            │ │         │▓│                  │▒│░▒│ •░░░░ ▒░░│         │ │
                            │ │         └─┘                 │░• ─┐┘  │░• ░•░░│         │ │
                            │ │         │                ┌──┘░ ░ │   └─ ┌─ ░ │         │ │
                            │ │         │▒│              │▒ │░▒░░└──┐▒▒░│░│ ▒│         │ │
                            │ │         │ │              │░─┘─ ── ░ └───┘─┘─░│         │ │
                            │ │         │░│        ┌──┐──┼─  ░  ░ │ │ ░    ░ │         │ │
                            │ │         │▒│        │  │░ │▒│▒ ▒│ ▒│ │░ ▒░░▒ ▒│         │ │
                            │ │        •░              ░─┘┐┘─░─┘──┘ └────░───┘         │ │
                            │ │     ┌─  ░         │░   •  │  •     ─┘░   │             │ │
                            │ │     │░• ──    │░│ └────   │ │       │░ │ │             │ │
                            │ │               │▒│         │░│       └──┘░│             │ │
                            │ │  ┌─┐          └─┘          ─┘          └─┘             │ │
                            │ │  │░│                                                   │ │
                            │ │  └─┘                                                   │ │
                            │ │ │   ───  ────  •    ─────┐─       ─────┐── ─┐───       └─┘
                            │   │░░░░░  │░░░ ░│░────  ░░░│ ┌─────┐     │░ │░│░  ──────┐  │
                            │   └─────  └───  │░░░░░  ░──┘ │░░░░░│     │  │░│     ░░░░│  │
                            │                     ───      └─────┘──   │         •  ──┘ ─┘
                             ──    │  │  ─┐─    ┌─   │ ─┐ •         ┌─┐     •     ┌─  │
                               │  ░│  │░ ░│ • │ │░ ░ │  │ ░• │░│    │░│ │░ │      │░  │
                               └───┘  └───┘─  └─┘──  └──┘──  └─┘    └─┘ │ ─┘──────┘──
                                    │       ──     ──      ──    ───     │           ──────┐
                                  │░│ │ │ │░░░░░░░░░░│ │░░░░░░│ │░░░│ │░ │░░  ░░░ ░░░░░░░░░│
                                  └─┘─┘─┘─┘──────────┘─┘──────┘─┘───┘─┘──┘─────────────────┘























```

*Figure from page 3 (2346x3317 px)*


---



4203-E P-117



SECTION 6 DISPLAY ON NC OPERATION PANEL



(3) Page [2]


#### AUTO OPERATION A.MIN N

ACTUAL POSITION LOAD DI SPLAY mm



0 lOO 200 (")


# 0.000


### 0.000 Spindle


# 0.000


# 0.000

Co 0 0 011 z



F O.ON 0%



0 w



0 TOUCH SENSOR 0%



TOUCH PROBE



PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PROGRAM DATA SEARCH DATA [EXTEND]



@ @J@@ @J @J@)@J



Fig. 6-3 Actual Position Display [2]



TOUCH SENSOR Touch sensor status; Reverse display with touch sensor ON



Touch probe status; Reverse display with touch probe ON TOUCH PROBE



LOAD DISPLAY Loaded condition of the spindle and axes



(indicated by graph and percent values)



[Supplement] For the spindle overload monitor specification, the symbol " V" (max. load value) and



the message "LOAD MONITOR(***%)" are displayed on the screen. The message



"TORQUE MONITOR (***%)" is displayed instead of "LOAD MONITOR (***%)"



during torque monitoring for synchronized tapping operation.


```text



                                                             ┌─┐───┐─┐──┐────┐──┐─┐──┐─┐─┐──────░──┐ ─────┐
                                                             │░│░░ │░│  │░░░░│ ░│ │░ │░│ │░░░░░░•░░│ ░░░░░│
          ┌──────   •        ────────────────────────────────┘─┘───┘─┘─ └────┘──┘─┘──┘─┘─┘─────      ────
          │      ┌─┐ ┌───────                                                                              │
          └───── │░└─┘░    ░░┌─────────────────────────────────────────────────────────────────────────────┘
                 └─┘ └───────┘
                              •               ─────────      ─────────   ──────────    ──
                                ─────────────┐          ─────         ┌─┐          ───   │
                                 ░░░░░░░░░░░░└──────────░ ░░  •     • │░│        │   ░│  │
                                ─────┐───────┘          ──┐─┐  •   │  └─┘░──┐░ │ │░░░ │  │
                                     │       │         •  │ └──    │  │░└─  └┐ └─┘─── │  │
                                     │         ┌──┐───┐         ─── │ │░│ │  └─┘      │  │
                                   ░│          │░ │░░░│  ───┐──     └─┘─┘─┘──    ───   │ │
                                   ─┘          │░ │░░░│ │ ░ │░░░─┐─                    │ │
                                  •            │░ │░░░│ └┐─┐┘─┐─ │░                    │ │
                                   │           │░ │░░░│  │ │  │  │ │                   │ │
                                   └┐          │░ │ ░ │  │ │ •   │░│                   │ │
                                  •▒│          │░ │░░░│  │ │  ┌─ │ │                   │ │
                                   ─┘       ── └──┘───┘  │ │  │  │░                    │ │
                                  │░│    ┌─ ░ •        │ │ └─ │  │                     │ │
                                  │░└─   │░•           │ │ │ │   │░                    │ │
                                  │░│ │  │ ░───────    │ │ └─┘   │                     │ │
                                  │░│ │░ └─░░░ ░░▒░    │ │    │ │                      │ │
                                      └──  ───────     └─┘    └─┘                      │ │
                                                                                       │ │
                                                         ──┐──   • ─────      ── ───── │ │
                                ┌──────────┐─┐──┐    ┌──┐  │    • │     ──┐──┐  •      │ │
                                │░░░░     ░│ │░░└──┐ │ ░│   ┌──┐  │    │  │░ │    • ───┘ │
                                └──────────┘ └──░░░│ └──┘  ┌┘░░│  │    │  └──   ┌─ •░░   │
                               │           │     ──┘ │  └─ │   │  └─┐──  │   ── │     ┌──
                               │   │    ░ │  ░ │    ░ │░ ░ │ ░│ ░ │ │░ ░ │  │ ░ │░░│ ░│
                               └───┘ ─────┘────┘──────┘─── └──┘── └─┘─── └──┘───┘──┘──┘
                                    •                     •      •      •
                                              •░░│ ░   │░░░• │ ░░░░│ │░░░░  ░│
                                               ──┘     └─    └─── ─┘ └───   ─┘
                      ┌──────────────┐      ┌──   ─────  ┌───    •  •    ───  ───────────────────┐
                      │ ░  ░  ░ ░░░ ░│      │ ░░░  ░░░░░ │░░░░  ░░ ░ ░░ ░░░ ░  ░░  ░░ ░ ░░░░░  ░░│
                      │    ─────── ─┐┘      │   │  ── │  └───                 │ •              ┌─┘
                      │             │       │ ┌─┼──  ─┘── ░  ─────┐───── ░────┘░               │
                      │░░░  ░░░░  ░│        │ │░│ ░ •   ░ │  ░ ░░ │   ░  •    ░ ┌──────────────
                      └────────────┘        │ └─┘─   •    │  ── │ │  ┌─┐       ─┘
                                           │ •     ─┐     ░┌─ ░─┘ └─ │ └── ──── │
                │ ──────── │   •░    │     └─       │      │ │                   •      ┌─   ───   • •
                │         ─┘    │   ┌┘────  ░ ─── ──┘──────┼─┘─  │ │░ ──────────┐ ──┐ ┌─┘ ───   • • •░──┐─┐
                  ────────      │░──┘░░░░░──── ░░•░░ ░░ ░ ░│   ┌─┘─┘ ░░░ ░░░░░░░│ ░ │░│ ░░░░░•   ░ ░░░░░│░│
                                │░░░░░░░──░░░░░░░░┌───  • ─┘ ░ │░░░░░░• ░ ──────┘   ░░░──░░░░░░│░───────┘─┘
                                │ • ────   ───── ─┘    │ │     └──────              ┌──  ──────┘─
                                └─ •     ──     •  ────┘ └─────       •  •     ─────┘
                                                                       ── ─────
































```

*Figure from page 4 (2346x3317 px)*


---



(4) Page [3]



AlfTQ OPEP.ATJON



ACTUAL POSITION



LOCAL COORDINATES


#### WOP.I( COOROS (M>A)

WOPJ< COOROS



MACHINE C00R0S



FEEDBACK COORDS



TARGET VALUE



DISTANCE REMAINING



MANUAL SHIFT ACTUL



MANUAL SHIFT TOTAL



PITCH ERROR COMP



4203-E P-118



SECTION 6 DISPLAY ON NC OPERATION PANEL


#### TST9.MIN OTST9 Nl3 16

97/07/15 14:10:00



1111



X y



39.500 185.850 -1100.000



39.500 185.850 -1100.000



39.500 185.850 -1100.000



39.500 185. 850 -1100.000



2539.500 2685.650 1400.000



39.500 185.850 -1100. 000



0.000 0.000 0.000



0.000 0.000 0.000



0.000 0.000 0.000



0.000 0.000 0.000



A-Mtd



=PO



~PO



=PO



PAOGRAM ACTUAL PART BLOCK CHECK


#### SELECT POSIT. PROGRAM DATA SEARCH DATA [EXTEND]

@ @J@ @J @J@@ @J



LOCAL COORDINATES



WORK COORDS (APA)



WORKCOORDS



MACHINE COORDS



FEEDBACK COORDS



TARGET VALUE



DISTANCE REMAINING



MANUAL SHIFT ACTUL



MANUAL SHIFT TOTAL



Fig. 6-4 Actual Position Display



PITCH ERROR COMP



[3]



Distance referenced to the origin of the local coordinate system



Distance referenced to the origin of the work coordinate system



Distance referenced to the origin of the work coordinate system



Distance referenced to the machine origin



Output (numerical value) from the position encoder



Target value



Distance remaining to the target point (commanded poirJt)



Axis manual shift amount (current operation) in manual or pulse



handle intervention operation



Axis manual shift amount {total) in manual or pulse handle



intervention operation



Thread pitch error compensation amount


```text


                                                                                               │ ──       ──
                                                             ┌──┐──────┐─┐───┐──┐─┐─┐──┐─┐─────┘  ░─┐───── ░
                                                             │░░│░░░░░ │ │░░░│░░│ │░│ ░│ │░░░░░░───░│ ░░░░┌─
           ┌──────  ──        ─────────────────────────────── ──┘──────┘ └───┘──┘ └─┘──┘ └──────       ───┘
           │      ──   ───┐───                                                                             │
           └────── ░┌─┐   │   ─────────────────────────────────────────────────────────────────────────────┘
                  ──┘ └───┘───
                                   ───┐────── ───────────────  ────────           •    ──┐
                                  │ ░ │░    ░│           ░░░ ░         ─────────   ─┐─┐  └┐
                            │ │ • │░░ ░░░░  ░│  ────     ─── ░• ────── ░▒░░░░░░ ──  │░│   │
                            │ │  ─┘─░░───────┘──    •       ──         ────────░▒ ──┘─┘ │ │
                            │ │                                                ───      │ │
                            │ │          • ────┐     ┌──       ┌┐─        ┌───          │ │
                            │ │   ┌─┐────▒│░░░░│    ┌┘ ░─┐    ┌┘┘ ─┐     ┌┘░░ ──        │ │
                            │ │   │▒│ ░░▒▒│   ─┘    │░ │░│    │░░ ░│     │░░│ ░░│       │ │
                            │ │   │░└─░░•░░──      ─┘░ │░│    │░░ ░│     │░░│ ░░│       │ │
                            │ │   │▒▒▒░• •░▒▒•     ░│░ │░│    │░•░░│     │░░│ ░░│       │ │
                            │ │   └─░░• ░░░┌─ ──┐  ─┘┐ │░│    └┐░ ░│     └─░│ ░░│       │ │
                            │ │   ░ ──░────┘░░ ░│    └─┘░│     └──░│       │░•░•        │ │
                            │ │   │             │    │ │ │     │   │       │    •       │ │
                            │ │   │░▒░ ───░ ┌─░▒│      │░│     └┐─░│       │░ ░│        │ │
                            │ │   └─── ░░░• │░──┘      └─┘     └┘ ░│       │░ ░│        │ │
                            │ │        ───   │   ─┐              •           •          │ │
                            │ │              │  ░░│                                     │ │
                            │ │  │░│         └────┘                                     │ │
                            │ │  │░│                                                    │ │
                            │ │ ┌┘  ─┐─      •          • ──      ─┐──────  • ───       │ │
                            │ │ │░──░│ ────── ─────   ──░│  ────┐─ │      ──░│   ┌────┐ │ │
                            │   │░░░░│  ░░ ░   ░░░ • │░░░└─  ░ ░│  │    •  ░ └── │    └─  │
                             •  │  ──   •      •   ░ │   │  │   │  │   •  •         • │  •
                              •       │  ┌─ ──┐    │ │  │ ──┼───   └─── ──  • ░    • ░ ┌─
                               │░ ░│  │░ │░   │ ░│ │ │ ░│ ░ │░ ░•   ░░░  ░ │ │ ░  │░  ░│
                               └───┘  └──┘────┘──┘─┘ └──┘── └───   ─────── └─┘─── └────┘
                                    ──              •      │     ──       •
                                               │░    • │░░░│░• ░░░░│ │░░░░░  ░│
                                               └───    └───┘─  ────┘ └─────   │
                       ────────────────────┐       ────      ──     •      ──┐ ┌─────────────────────────┐
                      │   ░░   ░░ ░░░░░░ ░░│     │░░░░  ░ ░░░░░ ░░░ ░  ░░ ░░░│ │░ ░░  ░░░ ░░░ ░ ░░  ░░░░░│
                      │    │       • ──    │     │      │ │          │       │ │   │    •         │      │
                      │ ─┐─┘ │  │          │     │ ──┐  └─┼─  ──┐─┐ ─┘  │  │░└─┘   │ │ •  │     ░░│ │  ─┐┘
                      └─ │░└─┘─ └────    ──      └─░░│ ─┘ │ ──  │ └─░│  │ ─┘─┘ └─ ░│ │  ┌─┘       │ │   └┘
                      │         │     ──┐        │      │ │                  └─     •  ─┘  ─────── • ───┘
                      │░░░░░░░┌─░░░░░░░░└┐       │░░░│  │ │░░ ░ ░░░ ░ ░░░  ──░░░░ │░░
                      └─      │  ─────   └┐      │   │                    •   ──  │   ─┐──────┐
                      │ │░ ░░░         ░ └┘      │ •░│░  ──░ ░ │░• ░ ░░ ░ ░│  ░ │ ░░░│ │░░░ ░░│
                      │ └────┐  ░   ░│           │░   │     ── └─ ───   •  │  • └────┘ └─   • │
                      │      └┐   ── └─────┐     │  • │       •  •   ──┐ ┌─ ─┐ │      •  ─── ─┼─┐───┐
                      │░░░░░░░│▒ ░░░░░░░░░░│     └──░─┘░──── ░░░░░ ░  ░│ │░ ░│ │░░│ •░░ ░░░ ░░│ │ ░░│
                      │      ┌┘┐ ─────  ───┘     │                          • • ─┐┘─      ──── ─┘   └┐─┐───┐
                      │░░░░░ │ │░ ░   ░░   ░│     │░─── ░•░░────┐ ░░────── ░ │░│ │░░ ░░  •    │░│ ░• │ │░░░│
                      │   ──         ───   ┌┘     └─ ░░──░── ░░░└──┐░░░░░ ───┘─┘ └───── •    ─┘─┘    │  ──
                      └───  ─┐─┐─────   ───┘     │                 │     │      │      • ─┐─┐    ───┐ ┌─  ─┐
                      │░░░░░░│ │░ ░    ░  ░│     └─░────── ░░───░── ░ ░ ░│  ░░░░│ ░  │░░ ░│ │░ │░░░░│ │░ │░│
                      └──── •             ─┘      ░•░ ░░░░── ░░░•░░░──  •     •      └────┘─┘──┘────┘─┘──┘─┘
                      │    │ ┌─────┐──┐──┐       │                    ── ────┐ ──────
                      │░  ░│ │░░░░░│  │░░│       │░ │░░░ ░░│  ░ │ │░░░░░░░░░░│ ░ ░░░░│
                      └────┘─┘─────┘──┘──┘─      └──┘──────┘────┘─┘──────────┘───────┘

























```

*Figure from page 5 (2346x3317 px)*


---



2-2. RELATIVE ACT POSIT Screen



4203-E P-119



SECTION 6 DISPLAY ON NC OPERATION PANEL



The RELATIVE ACT POSIT screen looks like as follows.



AlJTO OPERATION



D3--CIR.MlN



0 N 21



j 97/07/15 14:10:00:



RELATIVE ACT POSIT 1nm


### 2287.999 A 349.999


### -Y 1540.189


### 2287.989 F 0.0 S 0

A-Mtd



[EXTEND]



(a) Axis name (c) Relative actual position data



(b) Mirror image effective



Fig. 6-5 Relative Act Posit Screen



(a) Axis name



Indicates a basic axis name (X, Y, or Z) or an additional axis name (A, B, C, etc.).



An additional axis name is displayed only when an additional axis has been selected.



(b) Mirror image effective



When mirror image is effective, a minus sign



"_n



is placed preceding the axis name.



When mirror image is not effective, no sign is placed.



{c) Relative actual position data



Relative actual position data calculated using the following equation is displayed in the selected



unit system.



Relative actual position data "' (coordinate value output from the encoder *

- {Reference position 12 ) (Tool length offset value)

- (Machine zero point)



*1 ....... Whether or not the manual shift amount is added can



be set at NC optional parameter (bit) No. 5, bit 7.



*2 . . . . The reference position is the zero point (in the



machine coordinate system) for the relative actual



position. Far the procedure to set the reference



position, refer to (1} "Reference Position Setting".


```text


                                                                                                ──
                                                             ┌─────┐─┐─┐─┐───┐──┐─┐────┐─┐─┐──── ░────────┐
                                                             │░░░░ │░│ │ │░░░│ ░│ │░░░░│ │░│░░░░──░░ ░░░░░│
              ────                                  ─────────┘─────┘─┘─┘ └───┘──┘─┘────┘─┘─┘───        ───┘
          ┌───    ───┐──┐────┐─┐──────────┐─┐───────                                                       │
          │░ ░┌─   ░░│  │░  ░│ │  ░  ░  ░ │ │       • ─────────────────────────────────────────────────────┘
          └───┘ ── ─┐ │ └────┘ │  •     ──┘ └─┐─┐  │
                    │░│     ░│ │ │ ░  ░•   ─┘ │ │  └───┐─┐───────┐
                ────┘─┘──────    │            │ │  │   │ │       └──
                                 └─ ┌───┐─   ─┘─┘──     ─┘───  ──┘  ──    • •         ──
                                │ ░ │░░░│ ──          ░░ ░░ ░░        ──── │░•  ────┐   │
                          │ ┌── │         ░ │      ─────────────    •░░ ░░ │░ │ ░ ░░│ │ │
                          │ │  ─┘░── ░ •░───┘                   •    ──────┘─┐┼─────┘ │ │
                          │ │    │  ─── •    ─┐─┐───┐     ─┐     ┌───        └┘       │ │
                          │ │    │░│     │░░░░│ │░▒░│    │░│     │░░░│ │░░░│          │ │
                          │ │    └─┘     └────┘─┘───┘    └─┘     └───┘─┘───┘          │ │
                          │ │                                                         │ │
                          │ │    ──┐      ────── ────                                 │ │
                          │ │  │   │              ░░                                  │ │
                          │ │  │                                                      │ │
                          │ │ ┌┘  ─┐     ┌──┐─┐─┐───┐    ┌─┐     ┌───┐──┐    ┌─┐      │ │
                          │ │ │   ░│     │░░│░│ │░▒░│    │░│     │░ ░│ ░│    │░│      │ │
                          │ └─┘   ┌┘     └──┘─┘─┘┐──┘    └─┘     └───┘──┘    └─┘      │ │
                          │ │     │              │                                    │ │
                          │                ┌─┐──┐ │ •                                 │ │
                          │    ┌─┐         │ │░░│ │  │                                │ │
                          │ │  │░│         └─┘──┘  • │                                │ │
                          │░│  └─┘                    │                               │ │
                          │░│         ┌─    ─┐─     • └┐ • ──── ─┐────┐─┐───┐─┐       │ │
                         ┌┘          ─┘░───┐ │░────┐   └─ │    │ │    │ │   │ └┐────┐ │ │
                        ┌┘             ░░░░│ │░░░░░│ • │  │    │ │    │ │   │  │   ░└─  │
                       ┌┘  •░• ── ──┐   • ─┘  ┌──── • •░│      │ │   │  └─  │  │   ─┘  •
                       │    │    •  │       • │      │  └─────┐  └──┐┘  │ ─┐ •  ───   •
                      ┌┘    │   │   ░│ │░│ │░ │░ │ │ │░ ░    ░│  │░░│ ░• ░ │ ░  ░░░ ░│
                      │         └─   └─┘─┘─┘──┘──┘─┘─┘──┐  ───    ──┘─   ──┘  • ─────┘
                     •   ──┐──┐─  ───                   └┐    ───     ──    ── •
                       │   │░ │░░░░░░│                   └┐ ░ ░░░░░░░░░░ ░░░░░ ░░│
                    ┌──┘─┐─┘  └── •  └──┐                 └──────────────────────┘
                    │  ░ │░░│ │░░│ ░░░░░│
                     ────┘──┘─┘──┘──────┘      ┌── ── ───   •    ──── ───
                                               │  •    ░ ──  ┌─      •   ─────
                                               └── ──────  • │ ────── ───
                   ┌─┐─┐────┐──                   •                       ───
                   │ │ │    │  •
                   └─┘ │ ┌──┘   ─────────────────┐───────────────────────────┐────┐─────┐─ ─┐
                       │░│ ░  │  ░ ░          ░  │                ░          │░   │░ ░  │ │ │
                      │    ───┘     ── │ ──      └───── ──┐ ───      ────  ──┘    └┐────┘─┘ └────┐
                      │░░ │░░░│░ ░ ░░░─┘─░░░ ░ ░░░░░░░░ ░░│ ░░░░ ░░ ░░░░░  ░ ░░░  ░│ ░░░  ░░░░░  │
                   ┌─┐    └───       │    ┌───────────────┘────────────────────────┘─────────────┘
                   │░│ │░│ ░   ┌─┐ ░░└┐░ ░│
                   └─┘ │ └─┐ │ │ │    │   └┐─────┐─────────┐─┐───┐──┐──────────┐─────┐───┐─┐────┐
                       │░░░│ │░└─┘ ░░░░• ░ │░░░░░│ ░ ░  ░░ │░│   │░ │░░░░  ░░ ░│░ ░  │ ░░│ │░  ░│
                      │    │ │        •   ─┼── ─┐┘── ─┐ • •   ───┘── ┌─────────┘─────┘───┘─┘────┘
                      │░░ ░│ │░ ░  ░░░░│   │░ •░│░░ │ │  │░░ ░ ░░░░░░│
                   ┌─┐   ──┼─ •        └┐─   • ┌┘───┘─┘──┘───────────┘
                   │░│ │░░░│░│ │░ ░░ ░░░│░│ │░░│
                   └─┘ │   │ │ │        │ │ │  └─┐──────┐─┐──────┐─┐─────────────┐───┐────────┐─┐─┐─┐──────┐
                       │░░░░─┘─░│ ░░ ░ ░│   │░░│ │░░░░░░│ │░░░░ ░│ │░░░░ ░ ░░░░░░│   │░░░░░░░░│ │░│ │░░░░░░│
                       └──── ░  └───────┘───┘──┘─┘──────┘─┘──────┘─┘─────────────┘───┘────────┘─┘─┘─┘──────┘
                      │
                      │░ ░ ░   │        ░           │ •   ░           ───┐ • •   •       │
                      └────────┘────────────────    │             ───   ░│        ───  • └─┐─┐────┐
                                                      │ ░░░░░ ░░ ░░░░ ░  └──── ░░ ░░░░• ░░░│ │░░░░│
                                                      │░░───░───────────          ────  ───┘ └────
                                                   ┌─  ──                ──    ──                 ────────┐─
                                                   │ │       │░░░░░──── ░░ ────░░───── • ░░•░░░ ░ ░░░░░ ░░│
                                                     │       │░────░ ░░░───░░░░──░░░░░•░┌─┐░──────────┐──  •
                                                   ┌─┘                                  │ │           │  •
                                                   │░│       ┌──┐─┐░░ ────────░░───────░└─░░── ┌──────┘──░│
                                                   └─┘       │ ░│ └──┐    ░ ░░──  ░    •  ─┐░  │        ░ │
                                                            •        │  │ •  •           │ │ │ │   │  •    •
                                                             │   •   └─ │  │░         ───┘─┘ └─ ░──┘░• ░  │
                                                             │░░░░░• │░░│  └┐┐ •░░░░░░░░ ░░│░░░░ ░░░░░░───┘
                                                              ───── ─┘──┘── └┘─ ───────────┘───────────








```

*Figure from page 6 (2346x3317 px)*


---



(d) Reference position



4203-E P-120



SECTION 6 DISPLAY ON NC OPERATION PANEL



The reference position is the zero point in the machine coordinate system and is used to display



the relative actual position, or, in their words, the zero point in the relative coordinate system. The



reference position is calculated form the equation below and displayed for each axis in the



selected unit system.



Reference position = (output from position encoder *



) - (actual position value "2)

- (tool length offset value} (machine zero point)



*1 ....... Like the actual position display, it is possible to select whether



or not the manual shift amount is included in the output form the



position encoder by setting data at NC optional parameter (bit)



No. 5, bit 7.



*2 ....... Where the actual position is set in the coordinate system is



input.



Refer to (1) "Reference Position Setting".


```text


                                                                                                 ──       ─┐
                                                             ┌──┐─────────┐───┐──┐─┐──┐─┐─┐──────░  │ ────░│
                                                             │░░│░░░░░░░  │░░░│ ░│ │░ │░│ │░░░░░░───┘ ░░░░─┘
           ┌────────   •                ─────────────────────┘──┘─────────┘───┘──┘─┘──┘─┘─┘─────       ──
           │        ┌─┐ ──────────┐─────
           └────────┘░│ ░░░░      │  ░
                    └─┘ │    ─────┘─    ──────────┐─   ───────┐─────────  ────────  ─────────── ──────┐──
                        │░░ •░░░░  ░ ░░░░ ░   ░   │░─── ░░   ░│     ░░  ──   ░  ░ ── ░         •      │  ───
                       •      ─┐                                                       │               • ░  │
                        ┌────  └───────   │  ─────            ┌───     ──        │ ░ ░─┘    ░ ░  ░░      │ ░│
                        │░░ ░  ░  ░░░░░│ ░└─┐░░░░░░  ░ ░┌──░• │░░░░ ░ •░░░░─┐░░• │░░░░░░┌─░────░░───░──░ └┐─┘
                        └──────────────┘░┌┘ └──   ──   ─┘     └─────   ──── └──   ──── ─┘ •    ──   •  ──┘┘
                        │                │     ─┐─  ───  ─────      ──┐        ──     •  │ ┌──   •
                       •░░░░ ░░░░ ░░│░░ │ │  │  │░│ ░░░  ░░░░░•   ░░░░│ │░│ │░ ░░░ ░░░░░░│ │░░│ ░░│
                        ────────────┘───┘ └──┘─┐  │   ──     │ ┌─   ┌─┘ └─┘─┘         ───┼─┘──┘───┘
                                               │░░│ │░░░│ ░░░│ │░ ░░│ │░░░░░│ ░ ░░  ░░░░░│
                                            ┌─ └──┘─┘─┐ │                           │    │ •  ────    ─────
                                            │ │       └─┘───────────────────░───────┘────░•░──░ ░░────░░░░░─┐
                                            └─┘       │ ░ ░░░░ ░░ ░░░ ░░░ ░░•  ░ ░░ ░░░░░░░ ░░   ░░  ░    ░░│
                                                     •   ───       ┌─ │ │              ─┐    •             ┌┘
                                                      │      •  ───┘ ─┘ └───  •      ── │ •   ── ─── • ─── │
                                                      │░ ───┐░┌─             •                            •
                                            │ │       │     │ │ ────────────┐ ──┐─────────┐───────┐─┐──┐─┐ ─┐
                                            │ │       └───┐─  │     ░       │ ░ │░    ░░  │░  ░░░░│ │░░│░│ ░│
                                                      │░░░│     • ── ──     └───   ───   ┌┘───────┘─┘──┘─┘──┘
                                                      └─░•  ░    │░ ░░░░░░ ░  ░░   ░ ░░  │
                                                        •  ──────┘───────────────────────┘























































```

*Figure from page 7 (2346x3317 px)*


---



4203-E P-121



SECTION 6 DISPLAY ON NC OPERATION PANEL



(1) Reference Position Setting



The reference position is the zero point (in the machine coordinate system) which is used to display



the relative actual position, or, in other words, the zero point in the retative coordinate system. The



reference positlon can be obtained by setting the coordinate value of the actual posltion.



The reference position can be set in two different manners: by setting the actual position at "O" and



by setting the actual position at a desired position.



To set the reference position, press function key (F8] (EXTEND) in the automatic, MDI, or manual



operation mode repeatedly until functions "RELATI. ZEROSET" and "RELATI. PRESET" are



assigned to function keys [F2] and (F3], respectively.



=EX



=EX



=EX



RELAT~ RELAT~



ZEROS PRES



(a) Setting the actual position at "O"



[EXTENJ]



Follow the procedure below when setting the actual position at "O" in the relative coordinate



system.



1) Press function key [F2] (RELATI. ZEROSET) in the automatic, MDI, or manual operation



mode.



The prompt";;;; RPZS" will be displayed on the console line of the display screen.



RELAT~ RELAT~


#### ZEROS PRES [EXTENJ)

Press [F2] (RELATI. ZEROSET).


```text


                                                                                              │ ──
                                                            ┌─────────┐─┐────┐─────┐─┐───┐────┘ ░ ─┐ ────░│
                                                            │░░░ ░░░░░│ │░░░░│ ░ ░░│ │░  │░░░░└───░│  ░░░─┘
          ┌────── ───                        ─────────────── ─────────┘ └────┘─────┘─┘───┘────    •   ───
          │      │   ┌────────────┐──────────
          └──────┘ ┌─┘░ ░░        │░      ░
                 └─┘ │               ──     ─────┐  ──────┐─┐─ ───────────────┐  ────────────  ──────────
                     └┐░░ •░░░░  ░  ░░░   ░ ░░ ░░└┐─ ░░ ░ │░│ •  ░░ ░     ░  ░└── ░░   ░ ░   ──    ░ ░   ─┐
                     └┘    ──                     │░      │    •            ░•                         •  │
                       ──       •      •    ──────┘░     ─┘░│      ──  ░──  ░   ░ ░   │░   ░ ░░ ░░░░┌── ──┘
                     │░░░ ──────░──────░┌─┐─ ░░░░ └──┐───░░─┘ ░────░░───░░──┐─ ─────┐─┼───────░─────┘
                     │                  │ │          │                      │       │ │              ─┐─┐──┐
                     │  ░─────░ ░░ •░░░░└─┘── │ •░ ░─┘────░──░── ░░░░░░│  ░ │░░░░░ ░│ │░ ░░ ░░░░• │░  │ │░░│
                     │░─┐░░░░░─────░────░░░░░─┘ ░───░░░░░░•░░•░ ──     │     ───────┘       •    ─┘──   └──┘
                     │  │                                         • ───  ───         •  ───  ───     ───
                     └──┘────┐─┐───░─────────┐ ───░░───────┐─┐───░░░ ░░──░░░───░ │░ ░░░• ░░│  ░░░──── ░░░ │
                     │░░░░░░ │ │░░░░ ░░░░░░░░│  ░░░ ░░ ░░  │ │░░  ────┐░░───░░░──┘  ──┐░  ─┘ ───░░ ░░ ─── │
                     │                      •░      │░ ┌─     •       └──   ───  │ •  └─        ──────
                     └┐  │ ░───┐ │ • •     │ ───    └──┘ •     • ░ │
                      └─┐┘──   └─┘─ •  ────┘    ────      ───── ───┘                       ─┐
                      │ │   ┌─┐                                                           │ │
                      │ │   │░│                                                           │ │
                      │ │   └─┘                                                           │ │
                      │ │  •   ────       ──       ─────┐─┐───── • ─────┐─┐───── • ─────  │ │
                      │ │           ┌─────  ──────┐     │░│     │ │     │ │     │ │       │ │
                      │  •    ───┐─ │░░     ░░░   │    ─┘ └─────┘ │     └─┼─────┘ └┐──┐─┐─┘ │
                       │  ──     │  └──── │ ┌──┐─┐      │ │     │ │     │ │     │  │░ │▒│   │
                       └─   ─────┘  │     │ │  │ │ ─────   ──┐──   ───── • ─────   │   ─┼───
                         ──┐  ░   ┌─┼─┐░      ─┼─┘ ░ ░       │░ ░ • ░░░ • • ░░      ── ░│
                           └─ ─┐  │ │ │░──── ░ │ │ │ ┌┐  ─┐  │░ ░ ░ •░• ░ ░ ┌─ •░•   ░ ░│
                               └─      •    ───  │ └─┘┘─  │  └────── • ─────┘   • ──────┘
                   ┌─────────    ┌────   ───      │        ──                 ──
                   │░  ░░░     │ │  ░░── ░░ ──░│  │
                   └────    │  │ │       ──    │  └─────────────────────────────┐   ┌─  ──────────────────┐
                        │   │ ─┘ │         •   │           ░                   ░└───┘        ░          ░ │
                      │░└─┐ ░                                                                        ─────┘
                  ┌─┐ │   │  ─────┐─┐───────┐─┐───┐─┐─────┐──┐────┐───────┐─┐─┐──┐───────────┐──────┐
                  │ │ │ ░░│   ░ ░░│ │░░░░░░ │░│░░░│ │░░░░░│░░│ ░ ░│  ░░░░ │░│ │░░│ ░  ░░░░░  │░░ ░░░│
                  └─┘ └───░───────┘ └──  ── └─┘───  └─────┘──┘  ──┘   •   └─┘ └──     •      └──────┘
                      │            │   ─┐  •      ──          ──   ──┐ ┌─┐   •   ────┐ ┌────┐
                      │░ ░ ░ ░░░│  │░░░░│ │░│ ░ │░░░░░░░│ ░ ░ ░ ░░ ░░│ │░│ ░ ░│ │░░░░│ │░░░░│
                      └─┐───   ─┘──┘────┘─┘─┘───┘───────┘────────────┘─┘─┘────┘─┘────┘─┘──┐─┼─
                      │ │                                                                 │ │
                      │ │   ┌─┐                                                           │ │
                      │ │   │░│                                                           │ │
                      │ │   │░└─┐──               ──────   ─────   ─────                  │ │
                      │ │   │▒░░│      •  ─────┐        ┌─┐     ┌─┐      ─┐─────┐─┐       │ │
                      │ │   └───┘   ┌──░─┐  ░ ░└── ─────┘ └─────┘ └─────┐ │     │ └─────┐ │ │
                      │  • •     │  │░░ ░│ ─┐─░░ ░•     └─┘     └─┘     └─┘     │      ░└─  │
                       •  •     ─┘  └─   │  │    │     │        │ │     │ │    ─┘      ░   ─┘
                        •    ──┐  ──┘ ─┐   ─┘┐─  │ ┌──┐┘  ──┐─┐─┼─┘─┐─┐─┘─ ──┐─ └──┐─┐  ┌──
                         • │░ ░│  ░ │ ░│   ░ │ │ ░ │ ░│  │░ │░│ │ ░ │░│ ░ ░ ░│   ░ │░│ ░│
                        │  │░ ─┘ │░─┘──░ ░─┐ └─┘ ┌─┘ ─┘  │░ └─┘ └─┐─┘ │ ─── ─┘┐─── └─┘ ─┘
                        │  │     └─     ░│ │     │ │    • │       │  • •   •  │   •   •
                        │  ░ ░  ░░░░░░░┌─┘ │ ░░ ░  ░░░    │░░ ░░ ░│
                        └──────────────┘  ─┘──────────────┘───────┘


























```

*Figure from page 8 (2346x3317 px)*


---



4203-E P-122



SECTION 6 DISPLAY ON NC OPERATION PANEL



2) Key in axis address(es) for which "0" is set through the keyboard. When no axis address has



been keyed in, "0" is set for all axes.



Example: To set "0" for X and Z axes



=EX



=EX



=EX



= RPZSXZ



Key in axis addresses



A-Mtd



=FPZS XZ



RELA~ RELATQ



ZERO PflES



3) Press the WRITE key.



AUTO OPEPATION



RELATIVE ACT POSfT



=EX



=EX



X 0.000



Y 1540.189



Z 0.000



A--Mtd



=FPZS XZ



REL.AT



i.J



RELAT f.



ZEMSE,1 PRESEll



D3--CIR.MIN



[EXTEND]



0 N 2



97/07/15 14:10:00



rrm



349.999



WRITE



[EXTEND]



The reference position with which the actual position of the designated axis is "0" is obtained and



relative actual position data of the designated axis will change to "0".


```text


                                                                                                 ──      ┌──
                                                             ┌──┐──────┐──┐──┐─────┐───┐──┐─────   ──────┘░
                                                             │░░│ ░░░░░│  │░░│░░░  │░ ░│  │░░░░░───░░ ░░░▒░•
           ┌────────  •    ───                       •   ──   ──┘          ──┘   •    ─┘──┘────         ──
           │           ┌──┐   ────────────────┐────── ───  ───   ──────────   ───  ───           ───   •
           └────────┐─ │░░│       ░  ░        │  ░                                  ░           │         ┌─
                    │  │  └┐ ┌─      │     ─┐       ── ┌───────────────────────── ──────────────┘─────────┘
                       │ ░└┘ │░░░░ │ │░    ░│    ░ ░░░░│
                       │       ┌──┐┘ │  ────┘       •  └─┐
                       └─     ┌┘  │  │        •    │ │   │
                         ─────┘     │    ── │  ────┘ └───
                                 │  │   ░ ░░│
                                 │   ─── ┌─┐
                                 └──┐   ┌┘ └┐────────┐
                                 │░░│ ░ │░░ │░░░░░░░░│
                                 └──┘───┘───┘────────┘
                        ┌─┐                                                                 ┌─┐
                        │ │                │  ░                                             │ │
                        │░│   ┌─┐          └────                                            │ │
                        │ │   │░│                                                           │ │
                        │ │   │░└──                                                         │ │
                        │ │   │▒░░ ───    •         ────── • ───────┐────┐─┐─────┐────────┐ │ │
                        │ │   └──── ░ ───┐  ─┐───         │ │       │    │ │     │        │ │ │
                        │ │        ┌─ ░ ░└─┐ │░ ░───      │ │     │ │    │ │    ─┘  ┌─────┘ │ │
                        │  ──      │ ──░░░░│ └┐░░░░░•     │ │ ── ─┘ │    │ │     │  │░░░░░░   │
                         ─┐  ─── ──      ──┘  └───── •   •      •   │   •   •  ──   │  ──┐─ ──
                          └─┐   •      ┌─   •         ┌── ┌─  ┌─   │ ┌─┐ ┌─┐ ─┐  ─┐  ┌─  │
                            │░ ░ ░ ░ │ │░│ │░ │ ░ │ ░ │░  │░ ░│▒   │ │░│ │ │ ░│  ░│ ░│▒│░│
                            └────────┘─┘─┘ └──┘───┘───┘───┘───┘────┘─┘─┘─┘─┘ ─┘───┘──┘─┘─┘
                       ┌──                                                  •
                       │  ────        ░ ───                                           │   ─┐┐
                    ── └──    ─────────                                              ┌┘─   └┘┐
                          ───           ───                                          │  ─┐ │ │
                                                                                     │  ░│   │
                                                                                      ┌─  │  │
                                                                                      │▒│ │  │
                                                                                      └─┘ │ ┌┘
                                                                                            │
                                                                                        ────┘
                             ──┐──        •   ──────────         ───────────          ──
                            │  │  ──────── ───               ──┐            ───   ────  ─┐
                            │   • ░░  ░░░░ ░░     ──────┐   ░░░│     •░      ░  •   ░  • └┐
                            │ │  ────────────░          └─  ───┘       ── ─────░░ ───── │ │
                            │ │              ── ──┐───┐   ┌─     ┌───┐   •     ───      │ │
                            │ │    │░│         │░ │▒░░│   │░│    │░░░│ │░▒░│            │ │
                            │ │    └─┘         └──┘───┘   └─┘    └───┘─┘───┘            │ │
                            │ │    │ │      •                                           │ │
                            │ │    │ │        ─┐──┐  │                                  │ │
                            │ │    └─┘     ───░│  └──┘                                  │ │
                            │ │               •                                         │ │
                            │ │    ┌─┐         ┌──┐───┐                                 │ │
                            │ │    │░│         │░ │▒░░│                                 │ │
                            │ │    └─┘         └──┘───┘                                 │ │
                            │ │                                                         │ │
                            │ │               ┌──┐                                      │ │
                            │ │               │░░│                                      │ │
                            │ │  ┌─────       └──┘                                      │ │
                            │ │  │░░   │                                                │ │
                            │ │        │      •       ──── • ──────────┐─┐────┐──       │ │
                            │ │ •    │  ┌────┐ ┌────┐     │ │          │ │    │  ┌────┐ │ │
                            │  •     └─ │░░░░│ │░░░░│     │ │    •     │      └─ │  ░░│   │
                             │      ─┘  └────┘  ┌───┘─   ─┘ │   •  │   │  ┌─ •   │    │  •
                             └─┐───┐          • │     ───  • ──┐ ──┼──┐ ─┐┘ •     ┌─ ─┘ •
                               │░ ░│  │░ │░  •░ ░│ │ │  ░ ░ │░░│ ░ │░░│ ░│ ░   ░  │░│ ░•
                                 ──┘─ └─ └──  ───┘─┘ └──── ─┘──┘─ ─┘──┘──┘──── ── └─┘─
                        ┌────────       •    •     │      •      •            •        ─┐───┐────┐──────────
                       ┌┘ ░ ░░░░░ ░░ ░░░░┌┐ │░│ ┌──┘─ ────░──────░░──── ░───░░░•░░ ░░ ░░│ ░ │    │░ ░ ░░ ░  │
                       └┘    ──┐         └┘ │ │ │                       •    ┌─ ────────┘───┘────┘──────────┘
                        │  •   └─   •       │     ─── •       •     │ •     ░│ •
                         ── ───  ─── ───   • ───     • ─────── ─────┘─ • ────┘─












```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-123



SECTION 6 DISPLAY ON NC OPERATION PANEL



(b) Setting the actual position at a desired position



Follow the procedure below when setting the actual position at a desired position in the relative



coordinate system.



1) Press function key [F3] (RELATI. PRESET) in the automatic, MDI, or manual operation mode.



The prompt"= RPPS" will be displayed on the console line of the display screen.



=EX



=EX



=EX



=APPS



"RPPS" is displayed.


#### A--Mtd

[EXTEND]



Press [F3] (RELATL PRESET).



2) Key in axis address(es) and numerical value for which the actual position is set at a desired



position through the keyboard. When no axis address has been keyed in, the actual position



is set at a desired position for each axis.



Example 1: To set the actual position of X and Z axes at 200 and 300, respectively



= RPPS X200Z300



Key in axis addresses and numerical values.



Example 2: To set the actual position of all axes at 100



= RPPS 100



Key in a numerical value without specifying axis addresses.



A-Mtd



=EX



,,,0(



=EX



=RPPS X2002300



RELAT~ RELAT~



ZEROS PRES



3) Press the WRITE key.



[EXTEND]



WRITE


```text


                                                                                              │ ──      ┌─┐
                                                            ┌──┐──────┐─┐─┐─┐─────────┐──┐────┘   ─┐ ───┘░│
                                                            │░░│ ░░░░ │ │░│░│░░░  ░░ ░│  │░░░░░───░│ ░░░░─┘
          ┌────────  •          •                       ──   ──┘──────┘─┘─┘─┘─────────┘──┘────        ───
          │        ┌─  ───────── ───┐─┐──┐──┐─┐──┐──────  ───
          └────────┘   ░░░    ░     │░│  │  │ │  │              │
                   └─ │        │ ───┘─┘     └─   │     ───┐     └──────────────────────────────────────────
                      │ ░  ░ ░░│   ░░ ░│    ░ ░ ░  ░  ░░░ │ ░░   ░ ░     ░   ░   ░   ░     ░      ░     ░  │
                      └── │  • │ │    ┌┘──────────────────┘────────────────────────────────────────────────┘
                      │   └── ─┘ └────┘
                   ───┘ ──      •      ──────────────────────────┐─┐──────┐──┐───┐──┐────┐─┐─┐─┐──┐─┐───┐
                      │ ░░░░ ░░ ░░│ │░░   ░  ░   ░     ░ ░    ░ ░│ │░░░░░░│  │░  │░ │░░░ │ │░│ │░░│ │░░░│
                   ───┘          ┌┘ │     •       ─┐──     │ ─┐   •    ───┘ •  • └──┘ ┌─ └─┘─┼─┘──┘─┘───┘
                       │░░ ░░░ ░┌┘  │░   │ │░░ ░ │░│░░░░│ ░│ ░│  ░░░░░│ ░  │░ │░ │░░░░│ │░ ░░│
                       └─┐──────┘┘──┘────┘─┘─   ─┘─┘────┘──┘──┘───────┘────┘──┘──┘────┘─┘──┐─┘
                       │ │                   ───                                           │ │
                       │ │   ┌─┐          │ │░ ░│                                          │ │
                       │ │   │░│          └─┘───┘                                          │ │
                       │ │   │░│                                                           │ │
                       │ │   │░░───                 ─────┐─┐───── • ────────────   ──────┐ │ │
                       │ │  │░░•░   ┌───   ─┐──          │ │     │ │            ┌──      │ │ │
                       │ │  └── ─── │▒░░─── │░ ────  ────┘ └─    │ │   ─┐ ─┐─   │░ ┌─────┘ │ │
                       │  ─┐        └─░░░░░ └─░░░░░•     │ │  •  └─┘    │  │    │░ │░░░░░░   │
                        •  │░• ───       ──   ─────     •  └─  ──  │   •   │  ──      ────  •
                         •    │   │   │              ┌─┐     ┌─     ┌─┐ │ • ┌─      ┌─     •
                          │  ─┘ ░ │ ░ │░│ ░░ ░│░│░ ░ │░│ ──┐ │░│  ░ │░│ │ ░ │   ░░ ░│▒│ │
                          │         ░ │░│ ┌───┘░│     • •  │ │░│ ┌──    └── └───── ─┘─┘─┘
                          │ ░  │         ┌┘   └─┘    │ │░ ░░  ░│ │░    ┌┘  •      •
                          └────┘─────────┘       ────┘─┘───────┘─┘─────┘

                   ──        ┌─┐─┐─ ─┐─ ──  •   ─── ───┐─ ──   •   ──┐─   •    •     ───  ──     ───
                      ┌──────┘ │ │ • │ •  ──░───   •   │ •  ──  ───  │ ┌─  ┌──   ───     •   ──── ░ ─────
                      │  ░░░░ ░░ ░░░ ░░░ ░░░░░░░░  ░░ ░  ░ ░░░  ░░░░░│ │░░ │░░• │░░░┌──  ░░──░░░░ •░░░░░
                      └───────────────────────────────────────  ───  │ └──  ──  │  ─┘    ──     ── ─────
                      │                                       ──   ── •   ┌─   • ──   ┌──  ────┐
                      │░░░░░░│  │ │░ │░ ░░ ░░░░░ ░░│░░│  ░ ░ ░ ░ ░ ░░│ │░ │░│ ░░ ░░░│ │░░░░░░░░│
                      └──────┘──┘ │ ┌┘──           └──┘──────────────┘─┘──┘─┘───────┘─┘────────┘─
                                 │  │░░░│ │░│░░░░░░
                                 │ ─┘───┘─┘─┘──────
                                 └─                ─────────────────────┐
                                 │ ░│                                   │
                                 └──┘   │ • ───────   ────   •   •  ───┐┘
                      ──────────     ┌──┘  │       ───    ─── ──┐ •    │
                         ░   ░ ░│ │  │   • │   ░ ░ ░░    ░ ░  ░░│ ░   ░│
                      ──────────┘ │          ───────────────────┘──────┘
                                        ░ │░│
                                     ─────┼─┘
                                 ┌──┐     │ └────┐─┐──┐─┐────┐─┐─────────────┐────────┐
                                 │░░│ ░ ░  ░ ░ ░░│ │░░│ │░░░░│ │░░░░░░ ░ ░ ░ │░░░░░░░░│
                                 └──┘────────────┘─┘──┘─┘────┘─┘─────────────┘────────┘
                       ┌─┐                                                                 ┌─┐
                       │░│                │  ░                                             │ │
                       │ │   ──┐          └─────                                           │ │
                       │ │  │░░│                                                           │ │
                       │ │  │░░└┐───────┐                                                  │ │
                       │░│   •░░│ ░░░░░░└─┐─        ─────┐─┐─────┐────────┐───── •         │ │
                       │░│    ──┘──┐░░    │ ┌───┐──      │ │     │        │     │░•        │ │
                       │ │         └┐░░░  ░ │░░░│  ──────┼─┘     └──────┐─┼─    │░  ─────┐ │ │
                       │   •        └──────  ───┘──      │ │            │ │     │  •  ░░░│   │
                        ──  ───────                 ─────  └────┐ ┌───┐─ • ─────  •     ┌┘───
                          ─┐  ░░     ░░░  │░ ░ ░   │ ░░       ░ │ │ ░░│ │ │ ░░     ░░░ ░│
                           └─ ──  ░   ─── │░ │   ░ │ │   ──  │░ ░ │ • │ │ │ ──────  ─┐ ░│
                             •       •     ──┘─────┘─┘─    • └────┘─ • ─┘─┘─      •  └──┘
                  ┌─┐─┐──────   ┌───                        •                            ───
                  │░│ │ ░░░ ░ ░ │░░░░  ░░│                                          ┌─┐     │
                  └─┘─┘─────────┘────────┘                                          │ │   │ │
                                                                                    │ └─┐─┘ │
                                                                                    │  ░│ │░│
                                                                                     ┌─  ─┘ │
                                                                                     │▒│ ░  │
                                                                                     └─┘────











```

*Figure from page 10 (2346x3317 px)*


---



AUTO OPERATION



RELATIVE ACT POSIT



X 200.000



y 1540.189



z 300.000



A-Mtd



=EX



=EX



=flPPS X200Z300



l~~~R~~



4203-E P-124



SECTION 6 DISPLAY ON NC OPERATION PANEL



D3-CIR.MIN 0 N 2



97/07/15



nrn



A 349.999



[EXTEND]



The reference position with which the actual position of the designated axis is a desired position is



obtained and relative actual position data of the designated axis will change to a desired position.



[Supplement] Pressing the WRITE key without keying in address(es) and numerical value(s) does not



set anything.



(c) Data setting range and restrictions



1) Data is input in the unit system (metric or inch) employed for machine operation and the



decimal point position is fixed. For example, when "1" has been input while the 0.001 mm unit



system is selected, it is recognized as 1 mm. The same rule also applies to the inch system.



2) Data can be set within the following range.



For linear axes: -99999.999 mm to +99999.999 mm



(When the inch system is selected, the entered value is converted into a



metric value and checked if it is within the above range.)



For rotary axes: -99999.999° to +99999.999° {for the 0.001 ° unit system)



-9999.9999° to +9999.9999° (for the 0.0001 ° unit system)


```text


                                                                                               │ ──
                                                             ─┐─┐──────┐─┐───┐──┐─┐─┐──┐─┐─────┘░  ─┐───── ░
                                                              │▒│ ░░░░ │ │░░░│░░│ │░│ ░│ │░ ░░░░──░░│ ░░░░░•
                                                              └─┘──────┘─┘───┘──┘─┘─┘──┘─┘────        ────



                             ─────┐─────────┐ ─────────────────  ─────                 •
                            │     │         │           ░   ░  │       ────────   ────  ─┐
                            │ │ • ░░  │  ░  ░┌─  ───────── •░░░│ ─────░ ░ ░ ░░  │   ░ ┌─ │
                            │ │  ──┐─ └─── ─┐┘  │           ───       ─────────░│ ────┘ │ │
                            │ │    │      • │   └─┐───    ┌─      ────         ─┘       │ │
                            │ │    │░│      │░░░│ │░░░│   │░│    │░░░░ │░░░             │ │
                            │ │    └─┘      └───┘─┘───┘   └─┘    └─────┘────            │ │
                            │ │                                                         │
                            │ │    ┌─┐     ───────────                                  │ │
                            │ │    │ │       ░░     ░░                                  │ │
                            │ │    │ │                                                  │ │
                            │░│    └─┘      ┌───┐─┐───                                   │
                            │ │    │░│      │░░░│ │░░░│                                │ │
                            │ │    └─┘      └───┘─┘───┘                                │ │
                            │ │                                                        │ │
                            │ │              ┌───┐                                     │ │
                            │ │              │░░░│                                     │ │
                            │ │  ┌── ─┐────┐  ───┘                                     │ │
                            │ │  │▒░  │   ░│                                           │ │
                            │ │  └─   │       •       ──────┐─── • ────┐─ ──── •       │ │
                            │ │      │░ ┌──┐── ░────┐       │   │░│    │ │    │ ─┐────┐┘ │
                            │ └─     │  │░░│░░•░░░░░│      •    │ │    └─┘    │  │    │  │
                            │   •   ─┘  └──┘┐─  ┌──┐ ┌─  •      │ │    │ └─   │     │ │ ─┘
                             ──┐ ──┐  │     │   │  │ │ ── ──┐─── • ───┐ ─┘ ───    ┌─┘ └┐
                               │  ░│  │░ │░ │ │ ░│ ░ │  ░ ░ │ ░░ ░  ░░│ ░│ ░ ░ ░  │░│ ░│
                                  ─┘  │  └──┘ └──┘─┐ │ ──   └───   ───┘──┘──────  └─┘
                        ┌────────      ──    •     │ │   ─┐─    ───             ──    ───────────────────┐─┐
                       ┌┘ ░ ░░░ ░░░ ───░░ ───░┌────┘─░│ │░│ ░ •░░░░─────░• ░░──░░░░ ─┐░░ ░  ░░░░░░ ░ ░░░ │ │
                       └┘    ───────   ───    │       │ │ └───░───          •  ────  │     ───┐    ░       │
                      │ │   │                 │     ─┐    │                           ───     │ • ──   ───
                ──────┘     │                   │    └──   •                                  │  •   ──   ─┐
                   ░░    ░  │    │    •░  │    ─┘─           │░░     ░   ░   ░  ░          ░  ░ ░░   ░░░   │
                  ──  •          └────░───┘─          ───────┘─────────────────────────────────────────────┘
                    ┌─ ┌──┐──────           ──────────
                    │░ │░░│ ░░░░ ░  ░░░  ░░  ░░░ ░░░  │
                    └┐ │  │                       •   └─┐─────── ───────────────────────────────────┐
                   • │ └──┘────────░ ░────  ░•░•░░ ┌──░░│   ░ ░ •░░░░░░░░░ ░   ░ ░░   ░░░ ░░░  ░░ ░ └─  ──
                    ─┘ │░                 ───░•  │ │  ──     ──    ──────       ──    ░  ──    • ──       │
                       │   •       ───           │                         •   •   ───             ───── ┌┘
                       │░──░───────░░░── ───────░░ ░░───░• •░┌─ ──░ ░░░░░ │░░ ░░░ │░░░░░ │ │░  ░░  ░░░░░─┘
                   ┌─┐ │                •                 •  │    ────────┘───────┘──────┘─┘────────────
                   │░│ │ ░░ ░░│ ░• •░ │░░─┐───┐──░░░░░│ ░•░•
                   └─┘ │ ┌─   │ • • ┌─┘─  │   │   │  ─┘ │   ───┐──────┐
                       │ │ ░ ░│  ░░░│   ░░░░░ ░░░ └──  ─┘░░░░░ │░░ ░░ └┐
                       └─┘────┘─────┘  │ • ┌─                          └─ ─────  ───    ──────────────┐
                                      ─┼─ ─┘ ──────┐── ────────    ┌───     ░  ── ░ ───        ░░     │
                                       │░░░│ ░░░░ ░│░ •░░░░░░ ░┌───┘░░░──┐░ •░░░░ ─┐░░░ ─┐────────────┘
                       ────┐───┐─┐──┐  │   │  │  │             │         │   •     │     │
                         ░ │░░░│ │░░│  │░░•░░ └─░│ ░  ░░░░░░ ░─┘ │░│ │░ ░ │░   │░░│░░░░░░│
                       ────┘───┘─┘──┘─ │   │     │             │ │ │ │    │  │ └┐ └─┐     │
                                        │░░│ │░░─┘      ░     ░└─┘ │ │       └─ │ │ │░░░  │
                                        └──┘─┘──  ─────────────   ─┘─ ───────   └─┘─┘─────┘























```

*Figure from page 11 (2346x3317 px)*


---



4203-E P-125



SECTION 6 DISPLAY ON NC OPERATION PANEL



(2) Precautions



(a) Data is input in the unit system (metric or inch) employed for machine operation and the



decimal point position is fixed. (For example, when "1" has been input while the 0.001 mm



unit system is selected, it is recognized as 1 mm.)



(b) When changing the reference position of all axes including rotary axes, the entered value is



interpreted as length and degree.



(c) The reference position cannot be set for an indexable axis. In this case, the actual position



data is displayed on the RELATIVE ACT POSIT screen.



However, when axis designation was not made with reference position setting, "O" is set at the



indexable axis, causing no error.



(d) When the power is turned off, reference position data becomes "0" since it is not backed up by



turning off of the power. (The machine zero point is employed as the reference position.)



However, when actual position data in the work coordinate system is rounded (parameter (bit) No.



2 bit 1 is ON) with the multi-tum rotary table specification, reference position data is calculated in



reverse order. Therefore, when the work zero point is other than "0", a value other than "0" is set as



reference position data.



(e) Wark coordinate values do not change when the reference position has been changed.



(f) When the relative actual position value is smaller than -99999.999 mm (-9999.9999 inch for



the inch system),"-OVERFLOW' will be displayed on the display screen.



When the relative actual position value is larger than +99999.999 mm (+9999.9999 inch for the



inch system},"+ OVERFLOW' will be displayed an the display screen.



(g) The display of the relative actual position of a rotary axis (rotary table) varies depending on the



rotary axis specification.



1) Rotary table and indexable axis specification



The relative actual position is displayed within 0° and 360°. The reference position is also



displayed within 0° and 360°.



2) Rotary axis with limits and multi-turn rotary table



The relative actual position obtained using the equation on page 23 is displayed as it is. With the



multi-tum rotary table, whether or not relative actual position data is expressed within 0° and 360"



when the NC is reset can be set at NC optional parameter No. 2, bit 1.



When the additional axis is removed with the removable axis specification, "-OVERFLOW" will be



displayed as relative actual position data.


```text


                                                                                                •
                                                             ┌─┐─┐─┐─┐───┐───┐──┐─┐──┐─┐─┐──────░ ────────┐
                                                             │░│░│ │░│ ░ │ ░░│ ░│ │░░│░│ │░░ ░░░──░░ ░░░░░│
          ┌──────   •            ────────────────────────────┘─┘─┘─┘─┘── └───┘──┘─┘──┘─┘─┘────       ─── ─┘
          │      ┌─┐  ──────────┐                                                                          │
          └───── │░│ •░     ░   └────                                       ───────────────────────────────┘
                 └─       ┌──
                     •    │      │       ───  •      ───     ─── ┌──────────   ───   •   ──   ──  ──┐
                   │   ┌──┼──────┘───────   ── ──  ──   ────┐   ─┘ ░  ░     ── ░  ─── ┌──  ─┐─░ ──  └──┐
                   └─  │░░│ ░░ ░░ ░ ░░░░░░ ░ ░░░░• ░ ░ ░░░░ │░  ░░░┌────┐░░ ░░░──┐░░░ │░░• ░│ ░ ░░┌─ ░░│
                       └──┘──────────────┐ ──────  ─── ┌────┘──────┘    └──────  └───  ── ──┘─────┘ ───┘
                      •                  │             │
                   ┌─┐ │     │           │ │                ─────┐  ────────────────────────────────────
                   │ │ │ ────┘─      ───┐  │    ───    • •       │            ░  ░      ░   ░     ░
                       └─░░░░░░──────░░░└── ───░░░░──                      ───   •
                   ┌── │                │            ────       ───── ────┐   ┌─┐ ┌──┐─┐─┐─┐───────────┐
                   │░  └────░░░──────░░░░────░────░──░░ ░┌─┐░───░░░░░• ░░░│ ░ │ │ │░░│ │░│ │░ ░░ ░░░░░ │
                   └── │░░  ───░ ░░  ────░   •░  ░•░░─── │ │░ ░░─────   •     └─┘ └──┘─ ─┘ └───────────
                       │           │                     │ │             ────┐   •     │  •            ────┐
                       │░░░░──┐ │░░│ │░░──░░░░░░░░   ░░░    ░ ░░│ ░░░ ░░░░░ ░│   ░░░   │░░ ░  │░ ░  ░  ░   │
                       └────  │ └──┘─┼──   ─────┐───────────────┘────────────┘─────────┘──────┘────────────┘
                      •       │      │  ──      │
                   ┌── │                    ──┐ │   ──  ──  ────   ───         │   ──       ─── • ──────┐─┐
                   │   │  ░── ░ ░  ░┌─┐───    └─┼─┐─░ ── ░ • ░  • │░ ░───────░─┘ ──░ ───────   ░░░░░  ░ │░│
                   └─  │░──░░ ──────┘ │░░░────░ │ │░──░ ░──░────░ └───░░░░░░░• ░•░░──░░░░░ ░──────────    │
                       │                          │    │                       │                        ──
                      ┌┘───────┐────────────────┐─┘░───┘───────────────────────┘────────────────────────░░──
                      │░ ░   ░ │░░ ░░░ ░░   ░░ ░│   ░░░░ ░░░░ ░░░░░░░░░   ░░░ ░ ░░ ░░░░ ░ ░░░░ ░ ░░░░░░░░
                       ┌──   ──┘────────┐░  ┌───┘─ ┌───  ─────────────    ── ┌───┐  ──     •    │ ─── • •  │
                       │                │ ┌┐┘     ─┘   ──             ────  ─┘   └──   ────   ──┘        ──┘
                       └──────────░  ░ ┌┘─┘┘
                   ┌─┐ │               │   └───────┐────┐─┐──┐─┐──┐────────────────┐──────┐────────┐
                   │░│ │░░░  ░░░░░░░░ •░░░░  ░   ░ │░░ ░│ │░░│ │░ │░░░░░░░ ░░░░░   │░░ ░░░│ ░░░ ░░░│
                   │ │ │                                │                          │    ┌─┘┐ ┌──┐──┘────┐
                   │░  │░░░──────░░░░░ ░░░─────░░░── ░░ ░ ──░──░───░░░──░░░░░──░│  └─── │░░│ │░░│ ░░░ ░░│
                   └── └─── ░  ░ ────┐────░ ░░░───░░───── ░ •  •   ───  ░──── ░─┼─   ░░  ──┘ └──┘─    ──
                                     │                                          │       •   │     ────  ───┐
                       │░░░░───  ░░░░░ │░─── ░░•░░░───░░░───┐░░░░ ░░░• ░░░░░░ │░└─░│   ░░░│░│░░░│  ░░ ░  ░░│
                       └───      ───── │░ ░░─── ───   ──    └─░─────   ──────┐┘─┘  └──────┘─┘───┘──────────┘
                       │   │                       •          •              │
                   ┌─┐ │ │ │   ──        ──                  •    ─┐ │             ───────────────────── ─┐
                   │ │ │ └─      ────────           •           │  │ │                        ░    ░     ░│
                   │   └─░░░──── ░░░░░░░░──                    ─┘──┘─┘────────────────────────────────── ─┘
                   └─ ┌┘   │                ─┐─┐───┐──┐───────┐
                   │  │░ ░░│  ░░░ ░░░ ░░░░░│░│ │░  │░░│ ░ ░░░ │
                   └─ │                    │ │  ── │  │   ┌─ ─┘─┐──┐─┐───┐──┐   ┌─┐─┐───────────┐──┐─┐──┐──┐
                       ┌─────░░░░───░░░░ • ░░└─    │░░░░░░│ │ ░░│ ░│ │░░ │░░│   │░│ │░░░░░░░  ░ │░░│ │  │░ │
                       │░░░░░────░░░┌───░ ───░░    └──────┘ │  ─┘──┘─┘───┘──┘   └─┘─┘───────────┘──┘─┘──┘──┘
                   ┌─ │             │            ─┐        │ ┌─
                   │░ │░░░░   ░░  │░│ ░ ░░ ░ ░ ░ ░│     ░░░│ │░ ░│
                   └─ │           │               │              └───── ──────────────────────┐───┐ ┌─────┐
                       │░── ░░│ ──┘░░░──░ ┌─────░░░ ░───────░ ░ •░ ░░░░•   ░░░ ░░ ░ ░░░░░░░░ ░│  ░└─┘░░░ ░│
                       └─   ──┘─    ─┐░ ──┘░  ░ ─────     ░ ── •   ──       ░        •    •      │  └──   │
                                   • │                        •   •           ░     • ────  •  ──┘─    ───
                      ┌─ ░  ░ ░    ░ │░░░ ░░░  ░ ░░ ░ ░   ░░ ░ ░ ░░ ░░░░░  ────  ░
                      │                                                             ──   ───────────┐─────┐
                       │  ─── │ ░   ── • ░ ─────────        ░      ░    ░    ░    ░░   •            │ ░░ ░│
                       │░░░░░░│ ── ░░░░░░ ░░ ░░░░░░░░───░░───────────────────────────── ──────────── ─────┘
                        ──────┘─  ───────────────────   ──























```

*Figure from page 12 (2346x3317 px)*


---



4203-E P-126



SECTION 6 DISPLAY ON NC OPERATION PANEL


## 3. Program Display

In the operation mode, press function key [F3] (PART PROGRAM) and, the program information screens



are accessed. There are three types of program information display screens such as schedute program,



main program and MDI program. The display screen can be changed by pressing the PAGE key.



(1) Schedule Program



AUTO OPERATION


#### PROGRAM *SCHEDULE*

»N001 VSET vc1,.1



N002 PSELECT GEAP.MIN,0100 0-10



N003 PSELECT SHAFT.MIN



N004 PSELECT WHEEL.MIN



END



ACT POSIT (WORK)



=EX



=EX



=PR



39.500


#### PROGRAM

ACTUAL PART BLOCK



185.850



SELECT



POSIT. PROGRAM DATA SEARCH



N13 1~



97/07/15 14:10:00:



1111Tl


#### DIS X 0.000

y 0.000



z 0.000



0 F



o.o



H= 0 0.000



D= 0 0.000



-1100. 000



CHECK



DATA [EXTOO]



Fig. 6-6 Schedule Program Screen



The following display data items are in common to the CURRENT MAIN PROGRAM, READ MAIN



PROGRAM, and MDI PROGRAM display screens.



DIS X: Remaining X-axis movement distance to the target position



DISY:



DISZ:



Remaining Y-axis movement distance to the target position



Remaining Z-axis movement distance to the target position



Work coordinate system number



Currently active program number



Currently active sequence number



Actual teedrate (overridden programmed F value)



Actual splndle speed (overridden programmed S \(alue)



H Tool length offset number and offset data



D Cutter radius compensation number and compensation data



ACT POSIT (WORK) X Actual X-axis position in the currently active block (work coordinate



system)



ACT POSIT (WORK) Y



ACT POSIT (WORK) Z



Actual Y-axis position in the currently active block (work coordinate



system)



Actual Z-axis position in the currently active block (work coordinate



system)


```text


                                                                                               ┌───       ─┐
                                                             ┌────────┐───┐──┐───┐─┐──┐───┐────┘   •  ──── │
                                                             │░░░    ░│░  │░░│  ░│ │░ │░  │░░░░░───░•  ░░░─┘
                                          ─────────────────── ───  ───┘── └──┘───┘ └──┘── └────        ───
           ┌─      ┌───   ────┐─┐─── ───
           │░│     │▒░░ ░░░░░░│ │░░░  ░░  ───────────────────────────────────────────────────────────────────
           └─┘     └───┐──────┘ └────────┐
                  •    │                 └──────  ┌───────────┐─ ─────────┐───── ──┐───────────────┐────────
                 • ────┘────┐░ ─────────░░ ░  ░░┌─┘░░░░░░ ░░░░│ •░░░░░░░░░│ ░░░ •░ │░░░░░  ░░░ ░░░ │ ░░ ░░ ░
                │░   ░    ░░└─  ░ ░ ░  ░• ░ ░   │ │     │  ──░    ░ ───      •      •  ──   •              ──
                └┐          │ • ┌─           ┌─┐        │     │        │    •                  │░░
                 └┐─┐ ┌─────  ░─┘ ┌──    ░  ─┘ └── • ░ ░│ ░  ░│ │    ░ │ ░ ░░  │░  ░░░░ ░  ░ • └─── ░░┌─
                  │ │ │      ──   │  • ─────      • ────┘─────┘─┘────── ───────┘───────────── •    ───┘
                  │ │ │░░░░░░░░• •░░░░•
                  └─┘─┘────────               ─────────────────────────────     ───     •
                                  ───────────                               ────     ─┐  •
                            │     ░░░ ░░░░░░░░ ────────       • ──────  ────░░░      ░│   │
                            │ │  ─┐──── ┌────               ──        ─┐░░░░──  ░░░ ──┘   │
                            │ │   │    ░│               ────░  │       └────  ─┐─       │ │
                            │ │   └──  │░──────┐ •   ──     ┌──┘       │     │ │  ──┐   │ │
                            │ │  •░░░│ │░░░░ ░░└┐░─── ░│    │         │  • │░│  │░ ░│   │ │
                            │ │   │░░│ │░░░│ │░░│ ░  ──┘────┘         │ •  └─┘  └───┘   │ │
                            │ │   │░┌┘ └───┘ │░─┘ ───                 │    │ │          │ │
                            │ │   └─┘       • •                        │ │   │          │ │
                            │ │                                        │░│     ─┐     │ └─┘
                            │ │                                        │░│ │  •░│   • │ │ │
                            │ │                                        │░│ │ │ •    ░░│ │ │
                            │ │                                        │░│ └─┘      ──┘ │ │
                            │ │   ┌──┐──┐─┐───┐    ┌─┐──┐    ┌────┐       ─┘  •         │ │
                            │ │   │  │░ │ │░░░│    │░│ ░│    │░░ ░│      │░│  ░│        │ │
                            │ │     ─┘──┘─┘───┘    └─┘──┘    └────┘      └─┘───┘        │ │
                            │ │  ┌─┐                                                    │ │
                            │ │  │░│                                                    │ │
                            │ │  │  │                     ── ──────┐──────     ─┐────── │ │
                            │ │ ┌┘──┘─  ────┐─┐──┐    ───┐  •      │      ┌──┐─ │       │ │
                            │ │ │░░░░░  ░  ░│ │░░└── •░ ░│   ┌──┐ ─┘      │░░│   ┌──┐─┐   │
                            │    ────┐  •  ─┘ └┐─░░░• •  │ • │░░│  │      └──┘   │░ │░│   │
                             ── •    └─     │ └┘  ──     └─ •     ─┼──────┘  └───     │  •
                               •  ░ │ ░░ ░░   ░ ░░ ░ │ │░ ░ ░ ░░ ░ │ ░░ ░    │    ░░░ ░•
                                ────┘────────────────┘─┘───────────┘─────────┘─────────

                                                           │ ──    ────   ─────
                                                     • ────┘─  •         •
                          ─┐───────────    • ───   •            ─── │ ┌── ────┐─┐───┐─┐─┐─┐────┐─┐───┐─┐───┐
                      ──── │░░░░░░ ░░░░── │░• ░░───░░ ──── ░░──░ ░ ░│ │░░░ ░░░│ │░░░│ │░│ │░░░░│ │░ ░│ │░░░│
                       ░░  │░ ░ •   ──░░  └─░   ░ ░░•     ──┐      ─┘ └───────┘─┘───┘─┘─┘─┘────┘─┘───┘─┘───┘
                       │     ┌─       •                •    │        •
                       │ ░┌──┘ ─┐░░•░░    ░ │ ┌──── ░░• ┌─  ░        ░│ •        ░
                       │  │  │  │ │ ── │ •  └─┘         │ ┌──┐      │ └─   │      ┌┐
                       │░░│  │  │░│ ░░ └─ • │░│ ░░░ ░░░─┘ │░░│ ─┐ ░ │░│ ───┘ ░░░░░└┘
                       │ ─┘  │  │ │    │    │ │              │  │   │ │    │        •
                       │  │ ┌┘  │░│ ░░ └────┘░░ ────░░░────░░│ ░│ ░ │░│ ░│░│ ░░░░░░│
                       │ ┌┘─┘   └─ ──       │ •     ┌──     ─┘──┘───┘─┘──┘─┘───────┘─
                       │ │      │    ──    •      ──┘     •
                       │░│      │░┌─░░░┌─┐─░░• ░ ░░░░ ────░░│
                       │ │      │ │    │ │                  └─┐
                       │░│      │░└─░░░└─┘──┐░ ░░░ ░─────░░░░░│
                       └─┘      └─   ──┘    │                 └─────┐─ ┌───┐
                                │   ░   ░  ░  ───      │ ──░░     ░░│  │░░░└────
                       │ •      │   •    ──      •   ──┘─░  •       │  │ ──
                       └─       │ ┌─ ───┐   ───    ──      │ ──   ─┐┼──┘─   ─────
                       │ •      │░│░░░░░│ •░░░░─── ░░┌──░░─┘░░░ ──░└┘
                       │        │     │ │  ──        │  •      │    └────────────┐──┐
                       │ • ─────┘ ░░──┘─┘ ░ ░░░░░░░░░└── ┌─ ░░░└─░░░  ░░░░ ░░░░░ │░░│
                       │         ──       ──┐────        │  ───    ────────────   ──┘──────────────────────┐
                       └─────────  ───────  │     ────── ░•                    •░ ░   ░    ░ ░  ░        ░░│
                                            │    │░░░░ ░•                                                  │
                       ┌──┐ │  ───────────  │    │     │ ─────────────────────────┐──────────┐─────────────┘
                       │  └─┼──           • │    └─────┘ ░ ░ ░          ░    ░ ░░ │ ░░░ ░░ ░ │░░░   ░ ░░ ░░│
                          │ │               │    │░░░░ ░                                ────   ──   •      │
                       ┌──┘ └───────────────┘    │     • ┌─┐─┐─────┐───┐──┐─────┐─┐─────    ─┐─  ─┐─ ┌─────┘
                       │  │ │  ░      ░     │    │░────  │░│ │░░░░░│   │░ │░ ░ ░│ │░░░░  ░░│ │░ ░ │░ │░ ░░░│
                       └──   ──────────────      │░░░░ ──┘─┘─┘─────┘───┘──┘─────┘─┘────────┘─┘────┘──┘─────┘
                                                  ─────








```

*Figure from page 13 (2346x3317 px)*


---



4203-E P-127



SECTION 6 DISPLAY ON NC OPERATION PANEL



[Supplement] The DIS data and ACT POSIT (WORK) data of additional axes are displayed in the



following manner.



(2)



For the first additional axis, the data Is displayed below the "Z-axis" data of DIS and right



to the "Z-axis" data of (ACT POSIT) on the screen indicated above. For the second and



third additional axes, the data is displayed on the page accessible by pressing function



key [F8] (EXTEND) and [F6] (AXIS CHANGE).



Current Main Program



AUTO OPERATION A.MIN 0 N 1



97 07/15



PROGRAM * CURRENT


#### MA IN PROGRAM* Jllll

»G15H5 DIS X 0.000



G56XOYOZ500Hl y 0.000



S1000M3



z 0.000


#### GOX100Y100 w 0.000

CALL 0100



GOX200Y150



CALL 0100 0 F 0.0


#### M30 N

Ha: 0 0.000



LOAD MAX LOAD MON ITOR(l 1°") °"' 0 0.000



SPINDLE LOAD 0%


#### X y z w

ACT POSIT (WORK) 0.000 0.000 0.000 0.000



A-Mtd



=f'S A


#### PROGRAM ACTUAL PART BLOCK CHECK


#### SELECT POSIT. PROGRAM DATA SEARCH DATA [EXTEND]

>> Block just read into the buffer



Block being executed.



Fig. 6-7 Current Main Program Screen



[Supplement] For the spindle overload monitor specification, the symbol " V " {max. load value) and



the message "LOAD MONITOR {***%)"are displayed on the screen. The message



'TORQUE MONITOR (*** %)" is displayed instead of "LOAD MONITOR (*** %)"



during torque monitoring for synchronized tapping operation.


```text


                                                                                                ── •
                                                             ┌───────┐─┐─┐───┐──┐─┐─┐──┐─┐──┐───░░• ──────┐
                                                             │░░░ ░░░│ │ │░░░│ ░│ │░│ ░│ │░ │░░░──░• ░░░░░│
          ┌─────            ────            ─────            │      ─┘   └───   │ └─┘ ─┘ └──┘──        ──
          │     ┌───────────    ┌──┐───┐─┐──     ────────────┼──┐──┐  ──┐     ──┘─   •  │                 •
          └─────┘░   ░      ┌───┘░ │   │ │            ░  ░   │░ │░░│ │  │   │           │                  •
                └───────────┘   │  └───┘ └────  ─────────────┘──┘──┘─┘──┘───┘─────────  │     ───  ░ ──────
                                │░░░░░░░  ░░  ░•
                                └──┐            ──┐      •   ─┐─   ─────   ──          •   ┌───  • •     •
                                │  │     ────┐──  └────── ─── │ ───░░ ░░─┐─ ░┌──┐─┐────░• ─┘░░ ─┐ • ─────░─┐
                                └──░░ ───░░░ │░░░ ░ ░░ ░ ░░░░░│ ░ ░ ░░  ░│░  │░░│░│░░░░░░• ░ ░ ░│ ░░░░░░ ░░│
                                │░░ ░░░░░░• ░ ──░───── ░░┌───░ ░░░     ─┐┼─    ─┘─┘  • ░│    • •   ─────  ─┘
                                └── ─────       │     ░  │    ░      │  └┘ ────    ── ──┘ ──  • ───     ──
                                │        ───────┘─   ──── │ ─────────┘  │
                 ──┐  ──────────                  ───     └─          ──
                   │    ░ ░    ░•    ░░░
                  •    ──────                ──────────     ─────────────    ───   •   ─┐
                                 ┌──────────           ─────             ────   ┌── ──  └┐
                           │  ── │░░░ ░░░░ ░░ ──        ░░░         ┌┐     ░ •  │░ • ░   │
                           │ │   └──────────    •       │    │    │ └┘┐░•░──░ ░░ •░░░│   │
                           │ │                   ───────┘░ ┌─┘ ░ ░└─  │  •  ┌───    ─┘ │ │
                           │ │   ────┐ ────┐             ──┘  ────┘  ┌┘     │    ──┐   │ │
                           │ │  • ░░░└┐░░░░│                         │  • │ │  │░ ░│   │ │
                           │ │   │░░░░│  ──┘                         │ •  └─┘  │░ ░░•  │ │
                           │ │   │░░ ░░──                            │    │░│   ────   │ │
                           │ │   │░•░░░░░│                            │ │ └─┘          │ │
                           │ │   │░░┌──░─┘                            │░│ │   ─┐  •   │  │
                           │ │   └──┘                                 │░│ │  •░│   ──░│  │
                           │ │   │  └──┐                ┌─┐─┐────┐────┘░│ │░│ •  • ░░│   │
                           │ │   │░░░░░└─┐┐             │░│ │░  ░│  ░░ ░│ └─┘   │  ──┘   │
                           │ │   │ •   │ └┘──┐   ┌────┐ └─┘┐┘─  ┌┘─────   │ │   │      │ │
                           │ │   │░ •░│ ─┘░░░│  ─┘░ ░░│    │  │░│      │  ░│    │░     │ │
                           │ │    ── ─┘  └───┘   ░ ───┘     ──┘─┘      └───┘    └────  │ │
                           │ │                  ───                                    │ │
                           │ │  ┌─┐  │                                                 │ │
                           │ │  │ │  │             •     ──    ─┐─┐─────      ─┐─────  │ │
                           │ │ ┌┘░└─░ ───────┐──┐ │ ─┐──┐  •    │ │     ────┐─ │       │ │
                           │   │░░░░│  ░░ ░  │░░└─┘  │░░│   ┌─┐  ─┘       ░░│   ┌── ─┐ │ │
                            │  │░──┐┘ ─┐─ │  └┐┐░ └┐ └─ │   │░└─┐ │      │░ │   │░ •░│   │
                            └──┘   │   │  │   └┘  └┘┐┘  │ ┌─┘   │  ─┐──┐ │  │ • │ │ • ┌──
                               │░ ░│ │ │  │ │  ░ │ ░│ │░  │░ │░ │ ░ │░ │ │ ░│ ░ │ │░ ░│
                                ───┘─┘ └──┘─┘────┘──┘─┘───┘──┘──┘───┘──┘─┘──┘───┘─┘───┘
                       ┌─      │      •
                       │       │░  ░ │ │ ┌──┐  ┌┐░│   ░░│
                      │ ┌─     │     │ └─┘  └──┘┘ └─────┘
                      │ │      │░░░░ ░░░ ░ ░░░░░░░│
                      └─┘      └─────────────┐     ┌──────┐────┐────┐─┐────────┐
                                             │ ░ ░ │   ░ ░│ ░░░│    │░│░░ ░░░░░│
                                              ──        ──  ───┘    └─┘ •   •
                ────────────     •      • ──┐                   ────            ──       ──   ┌─   ───
                  ░░░░░ ░░ ░    • ──────░•░░└────────────────░░░░ ░░░░░──┐──────░░───────░░───┘░───░░░─────┐
                 ───────────   •░ ░ ░░░░░░░│░ ░░░░░▒░░░ ░░░░   │  ░  ░░░ │░░░░░░░ ░  ░░ ░  ░░  ░ ░ │░░░░░░░│
                                ┌─ ░░──────┘ ─────── ── ───┐─  │░     ── └─────── • ──   ░░     ░┌─┘ ──────
                                │          │               │  ─┘    ░   •        •    ── ────────┘ │
                                │   ░    ░ └─┐      ░  │ ░░░   ░  ░░  ░░░░ ░ ░░░░░  ┌─
                                └──────────┘ └─────────┘────────────────────────────┘


























```

*Figure from page 14 (2346x3317 px)*


---



(3) Read Main Program



AUTO !J'ERATION



PROGRAM



>>G15H5



G56XOYOZ500H1



S1000M3



GOX100Y100



CALL 0100



GOX200Y150



CALL 0100



1,130


#### LOAD MAX

SP I NOLE LOAD



ACT POSIT (WORK)



=PS A


#### A.MIN

4203-E P-128



SECTION 6 DISPLAY ON NC OPERATION PANEL



0 N 1



97/07/15 14:10:00


#### READ MA IN PROGRAM* 11111

DIS X 0.000



y 0.000



z 0.000



w 0.000



0 F 0.0



H= 0 0.000



LOAD MONITOR(110%)



D= 0 0.000



X y



z w



0.000 0.000 0.000 0.000



A-Mtd


#### PROGRAM ACTUAL PART BLOCK CHECK

SELECT POSIT. PROGRAM DATA SEARCH DATA [EXTEND]



Fig. 6-8 Read Main Program Screen



(4) MDI Program



AUTO OPE~TION



PROGRAM



G90GOXOY0Z0


#### RTI.I) I

TST9.MIN



*MDI PROGRAM*



*CURRENT*


#### ACT POSIT (WORK) 0.000

0.000



A-Mtd



=IN



PROGRAM ACTUAL PART BLOCK



SELECT POS 1T . PROGRAM DATA SEARCH



OTST9 N 1



97/07/15 14:10:00



lllll



DIS X



CO 1



0 TST9 F



N S



H= 0



D= 0



100.000



CHECK



0.000



0.000



0.000



0.0



0.000



0.000



DATA [EXTEND]



Fig. 6-9 MDI Program Screen


```text


                                                                                                 •        •
                                                              ┌─┐───┐────────────┐─┐──┐─┐─┐──────░──░ ────░│
                                                              │░│░░░│░░░  ░░░░░ ░│ │░ │░│ │░░░░░░•░░• ░░░░░│
           ───────   •                   ─────────────────────┘─┘───┘────────────┘─┘──┘─┘─┘─────      ───
                  ┌─┐  ──────────────────
           ───────┘░└──░    ░░   ░       ────────
                  └─┘  ─────────   │             ─────
                                 ──┘ •  ─────         ┌── •  ─────────────             ───
                             •        │░              │  • ─┐              ────       •   │
                            │  ──┐ ░ ─┘ ░░──░•    ────   ░ ░└─────   ─┐┐   ░░░    ──░░    │
                            │ │  └───░░┌──  •  ───░░░░ ░░── ░░░░░░─── └┼──────── •░░░── │ │
                            │ │        │          ───────  ───────     │                │ │
                            │ │  ┌───── ────┐                           ░░ ┌─┐   ───┐   │ │
                            │ │  │░░▒░░│░░░░│                         │ ┌─ │ │  │░ ░│   │ │
                            │ │   │░┌─▒│  ──┘                         │ │  │░│  │░ ░│   │░│
                            │ │   │░│ ░│░░                            │ └┐ │ │  └───┘   │░│
                            │ │   │░│░░ ░░•                            │░│ └─┘       •  │ │
                            │ │   │░└─────                             │░│ │  ┌─┐  •░ │ │ │
                            │ │   └─┘                           ── •  ┌┘░│ └─ │░│ • ──┘   │
                            │░│   │ └──── ─┐             │ │  │     ──┘ ░│ │░│ •    ░░│   │
                            │ │   └─░░░░  ░│             └─┘  │  ─── ░░ ─┘   │   │ ───┘ │ │
                            │ │   │ ─┐ │ •  ──┐   ┌────┐    •   •    ───  ──┐    │    │ │ │
                            │ │  │░░ │░│  │░░░│ ──┘░ ░░│     • │░│      │░ ░│    │  ░│  │ │
                            │ │  └───┘─┘──┘───┘   ░ ───┘      ─┘─┘      └───┘     ───┘  │ │
                            │ │  │              ────                                    │ │
                            │ │  │░│                                                    │ │
                            │ │ ┌┘ └─        •          • ──      ─┐──────  • ───       │ │
                            │   │░•░░░  ───── ──────  ──░│  ────┐─ │      ┌─░│    ────┐ │ │
                            │   └┐ ░──  ░░ ░   ░░     ░░░│      │ •       │░░│   │    └─  │
                            └─   │     ──  │   •     •      │          •  │  │   │  •░│  •
                              • •     │   ─┘       │        │  •   ──── ──┘  └───┘ •   ┌─
                               │  ░ │ │  │░│ │░ │░ │   ┌┐ ░ │ │░   ░  ░ ░ │░ ░ ░  │░│ ░│
                               └────┘ └──┘─┘─┘──┘──┘ • └┘── └─┘──  ────── └───────┘─┘──┘
                                     •              •      ─┘     •      │
                                              │░░  │ │ │░░│ │░░│ ░ ░  ░│ │░  ░ │
                                              └────┘─┘─┘──┘─┘──┘───────┘─┘─────┘
                  ┌─┐ ┌─┐────────┐
                  │░│ │░│░ ░░░░░░│
                  └─┘ └─┘────────                                ───
                                 ─┐─┐─┐────┐─┐────────┐──────┐───   ──     ─────        ─┐
                            │     │░│ │░░░ │░│        │░░░░░░│        ─────░░░░░─────    └┐
                            │ │ ─┐      ┌──┘─┘──  ┌─┐ │      └───────┐  ░░░░░░ ░░░░░░ │   │
                            │ │  └─░░░──┘         │▒│ │░░░░░┌┘       └─────┐───┐──   ─┘ │ │
                            │ │         └─┐   ┌── └─┘  ─────┘              │   │        │ │
                            │ │   ─── ░   │   │  •    •              │   • │ │    │░│   │ │
                            │ │   ░▒▒░ ───┘    ── ──                 │ ┌─ ─┘ │    │░│   │ │
                            │ │   ───                 ───────────────┘ │           ─┘   │ │
                            │ │               ────────               │ └─┐──┐           │ │
                            │ │  ────────────         ───────────────┘ │░│  │ ┌─┐       │ │
                            │ │              ─────────                │  └─ │ │░│   ──┐ │ │
                            │ │                                       │ ░│    └─ │░ ░░│ │ │
                            │ │                                       └──┘ ──    │░───┘ │ │
                            │ │     ──── •                  ┌──      •                  │ │
                            │ │           │ ── ───┐───┐     │░ ──      • ──┐            │ │
                            │ │   ────────┘─      │░  │     └─        │░•  │            │ │
                            │ │                ───┘───        •       └─ ──             │ │
                            │ │                                                         │ │
                            │ │                   ───      ───── ──────                 │ │
                            │ │ ┌─────┐─ ──┐─  •     ────┐─     │      ┌── ──┐          │ │
                            │ │ │░░░░░│ │░░│  │░────  ░ ░│ ┌────┘ ──── │  │░░│  ─┐────┐ │
                            │   └─────┘ └──┘  │░░░░░ ────  │░░░░░•     │  └──┘   │░░░░│  │
                             •                    ──      • •  ── ──┐─┐      └─  │  ──┘ ─┘
                               │  ░│  ┌─ •░ │ │ ░│   ┌───    │      │░│           ┌─  │
                               └┐ ░│  │░ ░  │ │  │ ░ │  ░ ░• │ • ░  │░│ ── ─── ┌┐ │░  │
                                └──┘ ┌┘─────┘─┘──  │ └───     •      •         └┘─ ───┘
                                    ─┘             └─┘    ───   ────   ┌───  ──
                                                 │ ░   │ │░░░│ ░░░░░  ░│ ░░░│
                                                 └─────┘─┘───┘─────────┘────┘














```

*Figure from page 15 (2346x3317 px)*


---



4203-E P-129



SECTION 6 DISPLAY ON NC OPERATION PANEL


## 4. Block Display

In operation mode, function key [F4] (BLOCK DATA) accesses the block data screens.



Under the heading of BLOCK DATA, four screens of block data display are available: CURRENT,



BUFFER, SECOND BUFFER, and THIRD BUFFER.



These display screens are selectable by pressing the PAGE key.



(1) Display of One Block Data Currently Executed



AUTO OPERATION TST9.MIN OTST9 N3 3



97/07/15 14:10:00



BLOCK DATA CURRENT mm



GOO M15 X 2000.000



s 0 Sr 0



G17 M115 y 2000.000 Tc 0 So 0



G23 M131 z -1100. 000 Tn 0


#### G53 M135 M 0 Fm 0.000

G90 M137 H 0 Fr 0.000



G94 M139 D 0



M133 I 0.000 Pr 0



J 0.000 Pe 0



K 0.000 Np 0 Nr 0



F 0.000 Ns



Fd 0.000 He Cr 0



Ft 0 Ce 0


#### Fl BC 3

A-Mtd EMPTY



=Bl



=PR



=BL



PROGRAM ACTUAL PART BLOCK CHECK


#### SELECT POSIT. POOGRAM DATA SEARCH DATA [EXTEND]

Fig. 6-10 Display of One Block Date Currently Executed



The following display data items are in common to the BUFFER, SECOND BUFFER, and THIRD



BUFFER display screens.



X X-axis command value



Y Y-axis command value



Z Z-axis command value



I command value



J J command value



K K command value



F Feedrate command value



Fd Feedrate command value (0.001 mm/6.4 ms)



Ft F command value for dwell



F1 Feedrate (F1-digit command)



S Spindle speed command value



Sr Actual spindle speed



So Actual spindle speed (overridden programmed S value)


```text


                                                                                                 •
                                                             ┌──┐─┐────┐─┐──┐───┐─┐─┐──┐─┐──────░░────────░░
                                                             │░░│ │░░░ │ │░░│ ░░│ │░│ ░│ │░░░░░░──░░░ ░░░░░•
             ─────                  ───────────────────────── ──┘─┘────┘─┘──┘───┘ └─┘──┘─┘────         ──
           ┌─      ┌───────────  ──                                                                        │
           │ ───── │░░  ░░  ░░  • ░─┐ ─────────────────────────────────────────────────────────────────────┘
           └─      └────────┐───░──░└┐
                ┌──         │        └─────┐─────┐─┐───┐─┐────┐─────────┐─┐────┐─┐──┐─┐─────┐
                │░ │░░░░░░  │ ░░░ ░░░░░░  ░│ ░ ░ │░│░░░│ │░░░░│ ░░░░░░░ │░│ ░░░│ │░░│ │░░░░░│
                │  │                       │                    ───    ┌┘┐ │   └─  │   ─┐  ─┼───┐─┐─┐──────┐
                └──┘░─── ░──░░░──┐────░░──░░ ░░░░────░░────░•░│  ░ •░░░│ │░│  ░░░░░│ ░│ │░░░│░░░│ │░│░░░░░░│
                │░ ░│ ░░│ ░░┌─┐░░│ ░░░──░░──░ ─── ░░░• ░ ░░•░─┘      ──  └─┘───────┘──┘─┘───┘───┘─┘─┘──────┘
                │   │   │   │ │                           • │   ┌────  ──
                 │░░░│ •░░░░│ │░░░░•   ░ ░░░ ░░░│ ░░ •░──░░ │░│ │░░░░ ░░ │
                 └┐─┐┘  •   │ └────           ──┘     •  ──   └─┘────────┘
                  │░│ │   ░   ░     ░░  ░   ░          •
                  └─┘ └───────────  ──           ────       ─── │  •
                                  │                   ┌─        └── ──                 ──
                            │     └───┐───            │░│ ░│          ───────┐───   ──┐  │
                            │ │   ░░  │░░   ──  •  │ ─┘░│ ░└─           ░ ░░░│ ░░── ░░│  │
                            │ │  ┌──░░└─────     ──┘ ░░░└─           ──┐─────┘──░░░ ──┘  │
                            │ │  │   •              ────   •           │        ────   • │
                            │ │  └──       ┌───┐          │░────  ┌─┐  │░ │░│        ─┐  │
                            │ │  │░░•      │▒ ░│          │░░ ░░  │░│  │░ │░│         │  │
                            │ │  │░│       │▒ ░│           ─────  │░│  │  │ │    ┌───┐ │ │
                            │ │  │▒│       │▒•░│                  │░│  │   ─┘    │ ░░│ │ │
                            │ │  └─┘       │░ ░│                  └─┘  │ •  │    └──┐  │ │
                            │ │            └───┘      ┌─   ┌────┐      │   ░│       │ │  │
                            │ │                       │ │  │░ ░░│ ┌─┐  │  │░│       │░│  │
                            │ │                       │ │  │░ ░░│ │░│  │  │░│       │ │  │
                            │ │                       │ │  └──┐░│ │░│  └─ │░│       │ │  │
                            │ │                       │░│     └─┘ └─┘  │  │░│       │ │  │
                            │ │                 ┌──┐  └─┘              │   │ ───┐   └─┘  │
                            │ │  │              │░░│                   └─  │ ░░░│      │ │
                            │ │  │░│            └──┘                        ────┘      │ │
                            │ │  │░│                                                   │ │
                            │   │  └──── ── •  •    •  • ──      ───────┐  •  ──       │ │
                            │   │░•░░░░ •░░│ ──░───┐ ┌─░│  ────┐─       └──░•   ─────┐ │ │
                            │   │░ ░──  ░  │ ░░░░░░│ │░░│   ░░░│  │    │  ░░░       ░└┐  │
                            │   │                ──┘─┘──    ───┘  └─   │  ───   •     │ ─┘
                             ──    │   │ ┌─   │         │      │  │ ┌─┐        │ ─┐─  └─
                               │  ░│   │ │░   │░ │ ░  │ │  ░ │░│ ░│ │░│ ░│ │   │░ │░  │
                               └───┘   └─┘──  └──┘─   └─┘    └─┘ •  └─┘──┘─┘─    ─┘──
                                    • •      ┌┘    ─┐    ───┐   │ ┌─         ────     ─┐
                                     •░░│ ░ ░│ •░░░░│ │ ░░░░│░░░│ │░░│ ░  ░░ ░░░░░░░░░░│
                                        │       ────┘ └──── └───┘ │  │        •   •
                            • ──    ────  ──────     •     •     • ── ────────  ── ─────────────────┐──────┐
                      ┌─────  ░░──── ░░░──░ ░ ░░ ░ •    │░░░   ░   ░░  ░    ░   ░    ░░  ░░       ░ │ ░░  ░│
                      │░ ░░░░──░░░░░┌─┐ ░░─── ──    ────┘───────────────────────────────────────────┘──────┘
                      └─┐────  │    │ │      •  ───┐
                      │ │      │░─┐░└─┼─░───░░  ░░ │
                        │      │  │ │ │ •   ───┐   │
                      │ │      │ ─┼─┘ │   •    └─ ─┘
                      │░│      │░ │░└─┘── ░──  │░  │
                      │ │      └┐ │             ───┘
                      │ │       │░ ░ ░░ ░  │░░•
                      │ │      │           │   │
                      └─┘      └─ ┌─░░░• ░ │░──┘
                      │░│      │  │ • • ── └─  │
                      │ │      │ •   •    ─┘  ┌┘──┐───┐
                      │░│      │ ░░░░░░──  └─┐┘ ░ │░ ░│
                      │  │     │      •      │    │   └────┐─┐──┐─┐──┐─┐
                       │ │     │ ░░░░░░ ░ ░┌─░│ ──┘░░░ ░ ░░│ │░ │░│  │░│
                       │ │     │ ──        │  │    │    ───┘─┘──┘─┘──┘─┘
                        │      └─  ───   │ │░─┘─── │░
                       ░│      │      ───┘ └─       ──
                      │ │       ──  •     •    ──      ───┐
                      │░│      │░░•░░• ░░░░░ ──░░░░░░  ░░░│
                      │ │      │           │      ────────┘
                       ░│      │░░░░│ ───┐░│ ░░░░░
                               └┐───┘    └─┘      ─────────────────────┐───┐────┐
                       •       └┘     ░│     ░  ░         ░  ░  ░ ░   ░│   │░░  │
                        •       └──────┘───────────────────────────────┘───┘────┘









```

*Figure from page 16 (2346x3317 px)*


---



4203-E P-130



SECTION 6 DISPLAY ON NC OPERATION PANEL



Tc Active tool number



Tn Next tool number



M M command value



H Tool length offset number



D Cutter radius compensation number



Fm Actual feedrate (mm/min)



Fr Actual feedrate (mm/rev)



Pr Main program repeat count by schedule operation



Pe Main program execution count by schedule operation



Np Hole number in coordinate calculation



Nr Hole number for restart



Ns Sequence specified by the sequence stop



He Work coordinate system number



Cr Number of subprogram to be repeated



Ce Number of subprogram actually repeated



BC Block counter



EMPTY No data in buffer



(EXIST Data existing in buffer)



[Supplement] For the additional axis specification, the data of the additional axes (first, second, third)



is displayed below the "Z-axis" data.



(2} Display of One Block Data in Buffer (to be Executed Next)



AUTO OPERATION TST9.MIN 0TST9 N3 3



97/07/15 14:10:00



BLOCK DATA BUFFER mm



GOO M15 X 2000.000 s 0 Sr 0



Gl7 M115 y 2000.000 Tc 0 So 0



G23 M131



z -1100. 000 Tn



G53 M135 II 0 Fm 0.000



G90 M137 H 0 Fr 0.000



694 M139 D 0



M133 I 0.000 Pr 0



J 0.000 Pe 0



K 0.000 Np 0 Nr 0



F 0.000 Ns



Fd 0.000 He Cr 0



Ft 0



Ce 0



Fl BC 3



A-Mtd EMPTY



=Bl



.,pfl



=BL



PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PROGRAM DATA SEARCH DATA [EXTEND]



@)@J@J@@J@@J@J



Fig. 6-11 Display of One Block Data in Buffer (to be Executed Next)


```text


                                                                                                 ───
                                                              ┌─┐───┐─┐─┐─┐───┐──┐─┐────┐─┐──────░░░ ──────┐
                                                              │░│░░ │░│ │ │░░░│ ░│ │░░░░│ │░░░░░░──── ░░░░░│
           ┌────────────  ──────          • •    ─────────────┘─┘───┘─┘─  └───┘──┘ └────┘─┘────            │
           │            ──       ───────── • ───                                                            │
           └────────────  ┌─────┐░               ───────────────────────────────────────────────────────────┘
                        • │     │          ┌──  │
                       •░ │     │░░░░ ░░   │░░• │
                                │               │
                        ░│      │░ ░░────░░░──░ └─
                        ─┘      │        ┌──  ─┐  ────┐
                                │  ──░  ░│     │ •░  ░└┐────────
                       │ │      │  ░  ─┐ ░   ──   ────░│        │
                       │ └─┐     ──    │   ──  │       └────────┘
                       │░ ░│    │░░─── ░░── ░░ └──────┐┘
                       │ ┌─┘    │      │     │ │      │
                       │ │      └──░░░ │░•░ ░└─┘─── ░░└┐
                         │      │      │  ┌──        • └──┐  ──────┐───────┐
                       │ └─     │ ─── • │░│   ┌─  ░──     └──  ░   │ ░     └───┐
                       │░░      └─░░ •░ │░    │░── ░ •      ░  ────░ ░•     ░  │
                        │ │     │   │   │ │           •       •    ─── ────────┘
                        │░│     │░░░└─┐░└─┘┐   ░░ ░░░░░░ ░░░░░░░░┌─
                        └─┘     │   │ │    │          ───────────┘
                        │░      └───┘─┘─░ ░ ─────░░░░
                        ░       │                ───   •     ───┐────┐
                        │ │     │   │   ───  •          ─┐ •    │   ░│
                        │░│     └───┘───░░░──░░─┐░░░░┌── └─░░│     ──
                        │ │     │             │ │    │       └────┐
                        │░      └──────  ░ ░░░│ │░│░│   ░░ •░░░░░░│
                        │ │     │           ──┘─┘─┘─┘     • ─┐    └─┐
                        │ │     │ ──  ░   •  ░   ░    ░  ░░░ │░ ░░░░│
                        │░│     │░  ──   │  ──    ───────────┘──────┘
                        │ └───┐ └──     ─┘    ───┐
                       •░░░░░ │    │░  ░░░ ░ •░░░│
                        •     │    │          ─┐─ ─┐───┐
                        ░ ░ ░│     │ ░░ ░░░░░ ░│   │░░░│
                 ───────     │          │              └─ ───   ────┐──┐────┐─┐────────┐───────┐────────┐───┐
                  ░░░░░░░░░ ░│   • ░────┘░░░░─── ░░│ │░░░•░░░░──  ░ │░░│ ░ ░│ │░░░░░░░ │░░░ ░ ░│ ░░░░ ░ │░░░│
                 ─┐────          ░──░░░░░────░░ ───┘─┘───░────░░ •  └─    ──┘─┘────────┘───────┘────────┘───┘
                  │    ─────┐─┐──                                 ─┐  ───┐
                  │░│ │░░░░░│ │ ░░ ░░░░░░ ░░░░  │░ │░│ ░  ░ ░░░░░ ░│ │░ ░│
                  └─┘ └─────┘─┘──              ─┘──┘─┘        ─────┘─┘───
                                 ─┐─┐─┐──────┐─       ┌──────┐             ──────    •  ──
                                  │░│ │░░░░░░│        │░░░░░░│         ────░░░░ ░┌───░│   │
                              │ ─┐ • ┌┘┐─ ┌──┘────────┘──┐   └─ ────── ░░░░──░ │░│░ ░░│ │ │
                              │  │░░░│ │░┌┘              │░░░░░•      ─────  ──┘─┘────┘ │ │
                              │  │  ┌┘─┘─┘  ┌─        ┌─  •     │                     │ │ │
                              │   •░│       │░─┐      │░  ░░░─┐░│ │░│  │░│ │░│      │ │ │ │
                              │  •░░│       │░ │      └─  ──░░│░│ │░│  │░│ │ │      │ │ │ │
                              │   │░│       │░░│      │ •   ── ─┘ │░│  │░│ │░│    ┌─░░  │ │
                              │   │░│       │░ │                  │░│  │░│ │ │    │ ──  │ │
                              │   └─┘       │▒░│              ──┐ └─┘  │░             │ │ │
                              │             └──┘      ┌─┐   ┌─ ░│   │   │ ─┐─┐      ┌─┘ │ │
                              │                       │░│   │░ ░│   │   │  │░│      │░│ │ │
                              │                       │░│   │░░░│   │   │  │░│      │ │ │ │
                              │                       │ │   └──░│  ┌┘   │  │ │      └─┘ │ │
                              │                        ░│      •░  │    │  │░│      │ │ │ │
                              │                 ────    │               │  │░ ─┐    └─┘ │ │
                              │  ┌─┐           •                        └──┘─┐░│        │ │
                              │  │░│            ───                          └─         │ │
                              │  └─┘                       ──────  ──────               │ │
                              │ ┌┘ └──┐─ ─────       • ──┐─      ──      ─┐──┐──        │ │
                              │ │░░░░░│ │░ ░   ─────  │ ░│  ─────  ┌───┐  │░░│   ┌────┐ │ │
                                │░────┘ │░ ┌─  ░░░░░│ │░─┘ │░░░░   │   │  └──┘   │░░░░│   │
                                │          │      ──┘     ─┘┐  │    •        │   │   ─┘  •
                                         │           • ──   │ ─┘   │ ┌─   ┌─     │ •   │
                                │     ┌┐ │   •░ ░      ░░ ░ │  ░   │ │░ ░ │  • ░  ░ │ ░│
                                └─  ──┘┘─┘─     ────  ───     ───┐─┘ └─   └┐─  •  ──┘─
                                  ─┐       ─────    ┌─   ──┐ │   │ └┐  ─┐─┘┘ ┌─ ──    ─┐─────┐
                                │░ │ ░│ │ │░░░░░│ ░ │░│ │░░│ │░░│   │░░░│ ░│ │░ ░░░  ░░│ ░░░░│
                                └──┘──┘─┘─┘─────┘───┘─┘─┘──┘─┘──┘───┘───┘──┘─┘─────────┘─────┘











```

*Figure from page 17 (2346x3317 px)*


---



4203-E P-131



SECTION 6 DISPLAY ON NC OPERATION PANEL



(3) Display of One Block Data in Second Buffer



Al.ITO OPERATION TST9.MIN OTST9 N3 3



97/07/15 14:10:00



BLOCK DATA SECOND BUFFER nm


#### GOO 1115 X 2000.000 s 0 Sr 0

G17 M115 y 2000.000 Tc 0 So 0


#### G23 1,1131 z -1100.000 Tn 0

G53 11135 II 0 Fm 0.000



G90 t.1137 H 0 Fr 0.000



G94 t.1139 D 0



t.1133 I 0.000 Pr 0



J 0.000 Pe 0



K 0.000 Np 0 Nr 0



F 0.000 Ns



Fd 0.000 He Cr 0



Ft 0 Ce 0



Fl BC


#### A-I.ltd BPTY

"8L



=PA



"8L



PROGRAM ACTUAL PART BLOCK CHECK


#### SELECT POSIT. PROGRAM DATA SEARCH DATA [EXTEND]

Fig. 6-12 Display of One Block Data in Second Buffer



(4) Display of One Block Data in Third Buffer


#### Al.ITO OPERATION A.MIN

BLOCK DATA THIFO BUFFER


#### GOO M15 X 0.000

G17 M115 y 0.000



G23 M131



z 0.000


#### G53 M135 w 0.000

G90 11137



G94 Ml39



M133 I 0.000



M326 J 0.000



I( 0.000



Fd 0.000



Ft 0



1\-Mtd



0 N



97/07/15 14:10:00



Sr 0



0 So 0



0 Fm 0.000



0 Fr+OVERFLOW



Pr 0



Pe 0



0 Nr 0



5 Cr 0



Ce 0



BC 1



EMPTY



CHECK



DATA [EXTEr-D]



Fig. 6-13 Display of One Block Data in Third Buffer


```text


                                                                                                ───
                                                             ┌─┐───┐─┐───┐──────┐─┐──┐─┐─┐──────░░░───────┐
                                                             │░│░░ │░│   │░░░░ ░│ │░░│░│ │░░ ░░░───░ ░░░░░│
          ┌──────   •       •                ───   •        ─┘─┘───┘─┘───┘──────┘─┘──┘─┘─┘─────      ───
          │      ┌─┐ ──────┐ ────────┐─┐─┐──┐   ─── ──┐─────                                               │
          └───── │░│  ░    │        ░│ │ │  │   ░     │░  ░ ───────────────────────────────────────────────┘
                 └─┘ ──────┘─────           │       • └────┐
                                  ──────────┘        ┌┘    │       ───     •          ──┐
                                 •░░ ░░░░░ ░         │░░───┘          ┌────░── ──────┐  │
                           │ │ ─┐        ┌───       •    ░ ░──      ─┐┘░ ░░░░░ ░   ░░│   │
                           │ │  └───┐─┐░─┘     ────┐░░░░────░░•      └┘───────┐┐─────┘   │
                           │ │  │   │ └─           └─┐ │                      └┘     │ │ │
                           │ │   ──┐       ┌──┐      │░│ ┌─────┐ ┌─┐  │ │ ┌─┐      • │ │ │
                           │ │  •░░│       │░ │      │░│ │░░░░░│ │░│  │░│ │░│        │ │ │
                           │ │   │░│       │░░░•     └─┘ └─────┘ │ │  │░│ │ │   ┌────  │ │
                           │ │   │░│       │░░│                  │░│  │░│ │░│   │░ ░▒• │░│
                           │ │   └─┘       │░░│                  └─┘  │░│ │ │   └────  │ │
                           │ │             └──┘      ┌─┐   ┌───┐          │ │        │ │ │
                           │ │                       │ │   │░ ░│  ──   │  │░│      │ │ │ │
                           │ │                       │░│   │░ ░│  ░░   │  │░│      │ │ │ │
                           │ │                       │░│   │░ ░│  ──   │  │░│      │ │ │ │
                           │ │                       │ │   └───┘       │  │░│      │░│ │ │
                           │ │                ┌─┐─┐─  ─┘               │  │░ ─┐──  └─┘ │ │
                           │ │  ┌─┐           │ │░│                    └──┘─░▒│        │ │
                           │ │  │░│           └─┘─┘─                        ──┘──      │ │
                           │ │  │░│                                                    │ │
                           │ │ ┌┘ └───     •  •    •   • •      ──┐───┐──    ──        │ │
                           │   │░•░░░  ──── ░•░──── ───░│ ─────┐  │   │  ┌──┐ ░──────┐ │ │
                           │   │░░░┌─  ░░ ░   ░░░    ░░░│      │ •    │  │░░└─░      └─  │
                           └┐  └─ ─┘   ───┐  ──   ┌─ • │  ─┐   │      │  │  │   │  • │  •
                            └─ │   │ │    │       │    │   │ │  ──┐─┐─ ──┼─ └── │ •   ┌─
                               │   │ │░ │░│ │░ │░│ •  │░ • │ │░ ░ │ │▒   │  │ ░ │ ░░ ░│
                               └───┘ └──┘─┘─┘──┘─┘   ─┘──   ─┘──  └─┘────┘──┘───┼─────┘
                                    •             ───     •      │              │
                                      • ░    ░ │░░░░░• ░ │░│ │░│░│ │░░░ ░ │░    │░ ░░│
                                       ───     │ ────    └─┘─┘─┘─┘─┘──────┘─────┘────┘
                 ┌─┐─┐─────┐───┐───┐─┐─   ──┐─┐ │    ┌───
                 │░│ │░░░░░│   │░░ │░│ ░ •░░│ │ │░░░ │░░░│
                 └─┘─┘─────┘───┘─            ─┘─┘───     │  ─────        ──      ────
                                 ┌─┐─┐──┐───┐       ┌───┐┘──     ──────    ┌─┐       ───┐
                           │     │░│ │░░│░░░│       │░ ▒│░            ░────┘░│ ──────   │
                           │ │ ─┐     │  ┌──┘─  ──┐┐┘     ─── ──────── ░░░░│░ ░░ ░ ░ │ │ │
                           │ │  │░░░│ │░┌┘     •  └┘░ ░ ░░░░░•        ─────┘─┐░──────┘ │ │
                           │ │  │  ─┘─┘─┘  ┌─┐     └─┐─┐────  ─┐             └─      │ │ │
                           │ │   ──        │░└┐      │░│    ──░│ │░│   •  │░│      │░│ │ │
                           │ │  │░░│       │░░│      │ │   │ ░░│ │░│  │░│ │ │      │ │ │ │
                           │ │  │░░│       │░░│      │▒│   └───┘ │░│  │░│ │░└┐─────░│  │ │
                           └─┘   │░│       │░ │      └─┘         │░│  │░│ └─ │░░░ ░─┘  │ │
                           │ │   └─┘       │░░│               ─┐ └─┘   │     └─────  │ │ │
                           │ │             │░░│      ┌─┐     •░│   │   │  ┌─       │░│ │ │
                           │ │             └──┘      │░│    ░░─┘  ░│   │  │░│      │░│ │ │
                           │ │                       │ │   │   │   │   │░ │░│      │ │ │ │
                           │ │                       │░│   │  ░░  ░│   │░ │ │      └─┘ │ │
                           │ │                 ────  │░│   └──── ──┘   │  │░└───   │░│ │ │
                           │ │                   ░     │               │  │  ░     └─┘ │ │
                           │ │                 ────                    └── ─────       │ │
                           │ │                                                         │ │
                           │ │                            ──────────── •       ──────┐ │ │
                           │ │ ┌─────┐─ ───┐─ •    • ┌──┐─            │  ┌──┐        │ │ │
                           │   │░░░░░│ │░░░│  ░┌───  │ ░│ ┌───┐  │    │  │░░│   ┌────┘   │
                           │   └─────┘ └───┘ ──┘░░░  │░─┘ │░░░│░ │    │  └──┘   │░░░░│  │
                            •              │     ─┐      │ ┌──┘─  ┌──┐┘     └─  │  ──┘  │
                              │         ░░     │░ │ │ ░░ │ │ ░    │  │      │     •   │
                              └┐  •  ─┐ ─┐  •░ │  │ │ ─┐ └─┘ │░ ░ │  ░ ░   ─┘ ── • • ┌┘
                               └──  • │  └─   •  •     └─┘ └─┘     ───   ──          │
                                  ──   │ │  ──    ────    •    ─┐─    ───  ──┐─── ──┐
                                       │ ░ │  │   ░░░░│ ░   ░ │░│░░  ░░░   ░ │░ ░░░░│
                                       └───┘──┘───────┘───────┘─┘────────────┘──────┘














```

*Figure from page 18 (2346x3317 px)*


---



4203-E P-132



SECTION 6 DISPLAY ON NC OPERATION PANEL


## 5. ATC Tool Setting Data Display


## (Memory-Random ATC Specification)

Pressing function key [F8] (EXTEND) changes the key guidance display. Function key [F3] (TOOL



DISPLAY) allows the ATC tool setting page to be accessed.



AUTO OPERATION N 1



19110711s 14:10:oq



ATC TOOL SET (POT REF)



POT TOOL POT TOOL POT TOOL POT TOOL



NO. NO. NO. NO. NO. NO. NO. NO.



1 001 11 011 :SPCY POT NA



2 002 12 012 :ACT TOOL 020



3 003 13 013 :NXT TOOL 007



4 004 14 014



5 005 15 015 :MAGAZINE 10



6 006 16 016



7 007 17 017



8 008 18 018



9 009 19 019



10 010 20 NA



SET



POT



TOOL



SEARCH SEARCH QUIT



@J @J @ @J


# CED

@J@



Fig. 6-14 ATC Tool Set (Pot Reference) Screen


```text


                                                                                                  •       •
                                                             ┌──────┐───────┐─┐───────┐─┐─┐──────░░─┐ ────░│
                                                             │░░░░░░│░░░  ░░│░│░░  ░░ │░│ │░░░░░░──░│ ░░░░─┘
             ──────                      •      •        ────┘──────┘───────┘─┘───────┘─┘─┘────         •
           ┌─       ──── ──┐─ ────  •     ┌── •  ┌──
           │░┌──── │░░░░│ ░│ •  ░░──░──── │░ •░│ │░░───── │
           │░│     │░──░│ •░░░• │░░░░░░░▒• ░░░░│░░│░░░▒░░─┘─   •
                   │░░▒│░░░░░░  │░░░░ ░░░░┌─┐░░░░ │░  ░░ ░░░───░────┐
                   └───┘────────┘─────────┘ └─────┘────┐─ ──░░░•░░  │
                                                       │              ───┐──┐─┐────┐─┐─────┐──┐─┐─┐──┐──────┐
                  ─┐───────░ •░░───┐░░──░░•░░░░░•░░░───┘─░░░─────┐░───░░░│ ░│ │░░░░│ │ ░░░░│  │░│ │ ░│ ░░░░░│
                   │░░░░ ░░• ░ •░  └─ ░░• ░ ────░──  ░ ░ ──      └─░ ░┌──┘──┘─┘────┘─┘─────┘──┘─┘─┘──┘──────┘
                    ─── ──   ──                       ──     •  •   ──┘
                                                                               ────    ───
                                  ───────────┐                 •        ──────┐    ───┐   │
                               ── ░░░ ░░░░ ░░│     │ │        │ │            ░│      ░│   │
                              │   ───────────      │ │ │  ─┐ ░│ │░  │  •░  ░ ─┘ ░ │░░─┘   │
                              │                    │ │ │   │ ─┘ │   │   ─────  ───┘──   │ │
                              │   │░ ┌─┐   ┌─┐ ┌─┐   │░│ │░     ░░  ░░                  │ │
                              │   │░ │░│   │░│ │░│   └─┘─┘──    ── ───     •            │ │
                              │   └─ │░│   │   │░│                      │░│░───    ┌──  │ │
                              │     │░░│    │░ │░│                      │▒│  ░░    │░░  │ │
                              │     │░░│    │░ │░│                      │      │   │ •  │ │
                              │     │ ░│    │  │ │                      │░░░░░░│     ░  │ │
                              │    │ •░│    │░ │░│                      └──────┘    ──  │ │
                              │    │ ░░│    │  │ │                                      │ │
                              │    │  ░│    │░ │░│                                      │ │
                              │    │ ──┘    │░ └─┘                                      │ │
                              │    └─       └─ │                                        │ │
                              │                                                         │ │
                              │                                                         │ │
                              │                                                         │ │
                              │      ─┐─┐────────────    ────    ┌─┐──── ─┐───────────┐ │ │
                              │    ─┐ │ │            ───┐    ┌─┐ │ │    │ │           │ │ │
                              │  ┌┐ │  •              ░░│    │░└┐       │               │ │
                                 └┘─┘─      •    ──  │░░└── •░░░└─ •    │ ┌──┐─           │
                                 │░░  ──┐─── ┌─── ░ ─┼─    • •░ │   ─┐── ─┘  │ │ ┌─┐───┐─
                                •   │ ░ │░   │░ ░    │ │░     │░   ░ │░ │ ░ ░│ │ │ │░ ░│
                                 ───┘ ──┘─── └───── ─┘─┘───── └─── ──┘──┘────┘─┘ └─┘───┘
                                     •                       •    •            └─
                                         │░░│ ░  │ │░░│ │░│ │░ │░ ░░░░░░░░░░│ │░░░░│
                                         └──┘────┘─┘──┘─┘─┘─┘──┘────────────┘─┘────┘─








































```

*Figure from page 19 (2346x3317 px)*


---



4203-E P-133



SECTION 6 DISPLAY ON NC OPERATION PANEL


## 6. Message Display (Option)

In the operation mode, display the function guide and press function key [F7] (MESSAGE) and the



messages in a program can be displayed.



While the display screen is in the message display mode, display page may be switched to the actual



position display, program display, block display, and check display using a proper function key. The NMSG



command in a program automatically returns the display mode from the message display mode to the



original display mode. The message displayed on the display screen is the one specified in the program



last.



Example:


#### N100


#### N101

N102 MOO MSG {CHECK TOOL!) ..... This automatically changes the display mode to



the message mode and "CHECK TOOL!"



appears on the display screen.



N103 NMSG ....................... This restores the display mode to the original



mode.



N104



N110 X100 Y100 (WORK FINISH) ..... Switching the display mode into the message by



pressing function key allows the display screen to



display the comment "WORK FINISH".


#### AITTO OPERATION B.MIN 01 NOOS 31

( 97/07/15 14:10:00



CHECK


## TOOL!

=PS B



OIECK



DATA [EXTEND]



Fig. 6-15 Message Display Screen


```text


                                                                                               ┌──
                                                             ┌──┐─┐────┐─┐───┐──┐─┐─┐──┐─┐─────┘░░────────░░
                                                             │░░│ │░░░ │ │░░░│ ░│ │░│ ░│ │░ ░░░░──░░░░░░░░░•
             ─────                       •           ────────┘──┘─┘────┘ └───┘──┘ └─┘──┘─┘────         ──
          ┌─┐      ┌─────      ────  ──   ─────────
          │░│      │░  ░   ──┐  ░░  • ░──  ░░░ ░░   │
          └─┘      └───────░▒│░─┐───░░│░░ ───────░░─┘
                 •              │     │              ──┐─┐─┐─┐─────┐──────────┐─┐─┐─┐──┐─┐─┐─┐─────┐─┐─┐───┐
                │ ──────░░ ░░░──┼──░│ └─░░░░─┐░─────░░░│ │░│░│ ░ ░ │░░░  ░ ░░░│ │░│ │░░│ │░│░│░░░░░│ │░│ ░ │
                │ ░     ┌─────  │  ─┘   ──── └─     ───┘ └─┘─┘──── └──────────┘ └─┘─┘──┘─┘─┘─┘─────┘ └─┘───┘
                │       │       │░  │                   │         •                                 •
                │░░░░ ░ ░─┐─ ░░  ░░░░•      ░  ░░     │ │  ░ •    ░───    ──── │ • • ────      • ─┐░  ┌────┐
                │ ───     │                          ░│                 │      │                  │   │  ░ │
                │     ── ─┘ ░─── ──   ──────────┐─ ── └─────  ────   ░──┘──  ░░└─ ───┐─┐─ ┌────── └──┐░ │░ │
                │ ░ ░░░░░ ░ ░ ░░░░░░  ░░░░░░░░░░│  ░░░ ░ ░ ░ ░░░░░░ ░ ░░ ░ ░░ ░░  ░░░│░│░ │░░░░░ ░ ░░│ ─┘░░│
                │░ ░ ───░░░░│ ────────░────░•░░─┘ │░░░░░░────────░░░░─── •░░• ──░ ───┘─┘─░└───── ┌───┘   ──┘
                │ ───   ────┘─        •    • ──  ─┘──────        ────   • ── •  ──       ─┘     ─┘    ───
                │
                │     ░
                └────────   ┌───┐
                            │  ░│
                            │   │
                            │░ ░└───────────────────────
                            └──░│ ░░░ ░ ░      ░        ─┐─    ─┐──┐───────┐──────────┐─┐────────────┐─────┐
                            │  ─┘──────────────────────  │      │░ │  ░    │░   ░     │░│  ░░  ░░░░  │░░░  │
                                                                │ ─┘ • ░   ░░• • ─┐─┐ │  ── ───────┐ └─────┘
                            ┌──┐──┐────┐                         •░│░ ░░ ░  ░░ ░░░│░└─░░░░░•       │       │
                            │░ │░ │░░░░│                        •░░░   ░░░░░──┐░──┘─ ░░┌──░ ░│ ░ │░│    ░░░│
                            │ ─┘┐─┘────┘                         ── ░┌──────  └─    ───┘   ──┘───┘─┘───────┘
                            └─  │                                  ──┘
                            │   └────┐─┐──┐─┐───┐─┐───────┐
                            │  ─┘ ░ ░│ │ ░│ │░░░│░│░░░░░░░│     ┌────┐────────────┐─┐──────────┐ ───────┐──┐
                             ──  ────┘─┘──┘─┘───┘─┘───────┘     │ ░░░│  ░   ░░░ ░░│ │░░░░ ░░  ░└─   ░░░░│ ░│
                                                                │░░ ░░ ░░    ░░   ░ │░░░░░ ░ ░░▒░░┌─────┘──┘
                                                                └───────────────────┘─────────────┘

                               •              ───────       ─────
                            ┌─  ─┐───┐───┐──┐─       ─┐───┐─        ──     ──┐
                            │    │░░░│▒░░│ ░│         │░▒░│           ─────░░│ ──┐───┐
                           │  ───┘┐  │   │   ──┐  ────┘───┘──────────  ░░░░──┘░░ │░░░│   │
                           │ │    └┐░▒░░▒│ │░░▒│ │                   ──────   ───┘───┘   │
                           │ │     └─────┘ └───┘ │                                     │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         └─┘
                           │ │                                                         │░│
                           │ │                                                         │ │
                           │ │   ┌────                                                 │ │
                           │ │  ┌┘░               ──      • ────┐─┐────        ┌─────┐ │ │
                           │ │  │ ─────────┐─ •     ─┐──┐─ │    │ │     ────┐──┘     │ │ │
                           │ │ ─┘░░░░    ░░│ │░────┐ │░░│  └┐──┐┘ │    •░ ░░│   ┌────┘─┘ │
                           │    └──────░░░─┘ │░░░░░│ └──┘   │░░│  │       ░─┘   │░░░░░   │
                            ── •       │         ──  │  │   └─     ────      •  │     ┌──
                              • │  ░   │░░░    ░      ░░     ░░ │ ░ ░░ ░ │  ░ ░ │  ░ ░│
                                └─ • ░ │░───── ────────────░ ───┘── ── ──┘ ───┐ │  ░ ┌┘
                                  • ─── •     •                               └─┘────┘
                                               ──┐────┐ ┌──────┐────  ┌──────┐
                                                ░│    │ │░░░░░░│  ░░ ░│ ░░░░░│
                                               ──┘────┘─┘──────┘──────┘──────┘
















```

*Figure from page 20 (2346x3317 px)*


---


## 7. Check Display

4203-E P-134



SECTION 6 DISPLAY ON NC OPERATION PANEL



During operation in automatic, MDI, or manual mode, it is possible to check the NC axis data and the



contents of the system variables by displaying them on the screen.



The following check items can be displayed.



Note that the actual display screens and check items will vary according the selected specifications.


## 1. NC specification codes


## 2. NC axis data


## 3. NC axis data enlarge display


## 4. Diagnostics


## 5. System variables - axis data


## 6. System variables - zero offset


## 7. System variables - tool offset


## 8. System variables system parameter


## 9. System variables home position


## 10. System variables - NC communication


## 11. System variables other data

Select the data to be displayed by an NC optional parameter (bit) No. 5, bit Oto bit 4.



Description of operating procedure:



Ce) @J [ill [ill [El



(1) Press either the MANUAL, MDI



or AUTO key.



(2) Press function key [F7] (CHECK DATA).



(3) Press the page key to change the



screen display one screen at a time.



Fig. 6-16 Displaying the CHECK DATA INDEX Page


```text


                                                                                                 ───
                                                              ┌─┐───┐─┐───┐───┐──┐─┐──┐─┐─┐──────░░░───────┐
                                                              │░│░░ │░│ ░ │░░░│ ░│ │░ │░│ │░░░░░░──░░ ░░░░░│
              ─────                    ───────────────────────┘─┘───┘─┘───┘───┘──┘ └──┘─┘─┘────        •
           ┌─┐     ┌───────┐────  ──                                                                        │
           │░└─────┘░░░  ░░│ ░░░•  ░─┐ ─────────────────────────────────────────────────────────────────────┘
           └─┘     └───░░──┘ ───░───░└─
                 ┌─             •       ───  ┌───    ────── ────┐─ ───────────┐─┐───┐─┐──┐─┐─┐─┐─┐──┐─┐─┐─┐─┐
                 │░─────░░░ ░░ • ░──░░ •░░░──┘▒░ ────░░░░░ •░ ░░│ • ░ ░░░░░░  │ │░░░│ │░ │░│ │░│ │░░│ │░│ │░│
                 └─      ──────   ░ ──   •    ──       ──    ───        ──────┘─┘───┘─┘──┘─┘─┘─┘─┘──┘─┘─┘─┘─┘
                 │                                        ───    ───────
                 └───┐─░ ░░   ░  ░  ░░   •░  ░  ░  • ─┐
                 │   │ •             ───            • └──┐─┐───┐─┐──┐───┐──────────┐─┐───────────────────
                 │░░│ │░│ ░──░░░░░ ░░░░░│ ░░░░░ ░ ░░  ░░░│ │░ ░│ │░ │░░ │   ░░░   ░│ │░░ ░░░ ░ ░ ░  ░
                 └──┘─┼─┼──   ─┐     │  │      ┌─────────┘─┘───┘─┘──┘───┘──────────┘─┘───────────────────
                      │ │  │░│ │░░░░░│░░░  ░░░░│
                      └─┘  │ │ │      ┌────────┘
                      │░│  │░│ │░░ ░░░│
                      └─┘  │ │ │     │ ─┐────┐─┐────┐
                      │░│  │░│ │░░ ░░│  │░░░░│ │░░░░│
                      │ │  │  •      └──┘────┘─┘────┘
                      │ │  │ ░░│  ░░
                      │ │  │ ──┘───┐   ──┐   ┌─┐─┐──┐
                      │ │  │       │  │  │   │ │ │  └┐
                      │░│  │░      │  │ ─┘   │ │ │░• │
                      │ │  │       │  │  │  │  └─┘   │
                      │ │  │░ ░░ ░ │░ │░─┘  │ ░│ │░  │
                      └─┘  │       │  │  │   •  •    └──────┐
                      │░│  │░░░░ ░ │░░░░░│  │░░░░ ░ ░░░░░░░░│
                      │ │  │       │     │  └────       ┌───┘
                      │░│  │░░░░░░ │░ ░░░│  │  ░░ ░░░░░░│
                      │ └┐ │       │     │  │  •     ─── ────┐
                       •░│ │░░░░ ░ │░ ░░░│  │░• •░░ ░░░ ░░░░░│
                        │  │       │     │  │  • •    ───────┘
                  •   ┌─┘─ └─┐░░ ░  ░ ░──┘──┘  ░• │░░•
                 │ ───┘    │ └──   ────        •  │ │  ────────────────────────────────────┐
                 │         │ │  ──     │░  ────   │ │      ░       ░ ░ ░                  ░│
                 │░                ░ │ │       ┌── • ───────────────────────            •  └────┐─┐──┐
                 └─────────   ───────┘─ ───────┘                            •  │░░────── ░ │░  ░│ │░ │
                                                                               └─░░ ░ ░░ ──┘────┘─┘──
                                                             •   ─────────┐─┐         ──             │
                                                              ───         │░│                     ┌──┘
                    │  │                                                  │ │                     │
                    │  │  ┌──                                        • ───┼─┼─────── ─────── •    │
                    │  │  │            •       •    •       ────  ─┐  │   │░│░ ░░ ░░ ░░  ░  │     │
                    │  │   ┌─┐─┐──────  ─────── ──── ───────    •  │  │   │ │               │     │
                    │  │   │ │ │               •    •        │ │ │ │  │ ──┘░└────────────┐ ░│     │
                    │  │   │ │ │                             │ │ │ │  │      ░   ░░░░░░░░│  │     │
                    │  │   │ │ │                             │ │ │ │  │░ ┌─┐─┐░ ░░░░░┌───┼─░│     │
                    │ │    │ │ │                             │ │ │ │  │░ │░│░│░░░░  ░│░░░│░░│    │
                    │ │  │ │ │ │                             │ │ │ │  │░ │░│░│ ░░░░░░░░░┌┘ ░│    │
                    │  ┌─┘ │ │ │                             │ │ │ │  │░░│░░░ ░░░░░░┌┐░░│  ░│    │
                    │  │   │ │ │                             │ │ │ │  │░ │░───┐─────┘┘──┘░░░│    │
                    │  │   │ │ │                             │ │ │ │  │   ░   │            ░│    │
                    │  │   │ │ │                             │ │ │ │   ─────┐ │░ ░─────┐ ┌─░│    │
                    │  │   │ │ │                             │░│ │ │  │░░▒░▒│ │░ ░ ░░ ░│ │░░│    │
                    │  │  ┌┘─┘ │  ──   ────  ─────── • ─── ──┘ └─┘ │  │░░│ ░│ │  ░░ ░ ┌┘ └─░│  │ │
                    │  │  │     ┌─  ┌─┐    ┌─       │ •   │        │  │░░│░░│ │ ─── ░─┘    ░│  │ │
                    │  │  └──░░ │░  │░│    │░│ │░│ ░│  ░│ │░    ───┘   ──┘──┘─┘─   ──   ────┘  │ │
                    │  │ •   ───┘───┘─┘────┘─┘─┘─┘──┘ ─┐┘─┘─────   │  │                     │  │ │
                    │ │                              │ │             ┌┘ │                   └──┘ │
                    │ │                          ─── │ │            ─┘  │                        │
                     │                              │ ┌┘──────────── │  │
                     └─────┐───────┐────────────────┘ │             ┌┘  ░ ───────────────────────────
                     │░ ░░░│ ░░░░░ │░░░░ ░░░░░░ ░░░░  │             └┘ ── ░░░░░ ░░░░░░░░░░░░░ ░░░░░░
                     └─────┘───────┘──────────────────               └─    ──── ──── ───────  ── ────
                                                               ─────    •
                                       │░ ──   │ │ ───────  ──┐  ░       ┌─┐──  •  ───┐
                                       └─   ───┘─┘ ░     ░    └──────────┘ │  ── •  ░░│
                                          ──      ────────  ──            •        ───┘












```

*Figure from page 21 (2346x3317 px)*


---



4203-E P-135



SECTION 6 DISPLAY ON NC OPERATION PANEL



(1) Press either MANUAL, MDI, or AUTO key.



(2) Press function key [F7] (CHECK DATA).



The screen displays a check data indications page.



(3) Press either the



page key to display the check data desired.



Pressing



once advances a page.



Pressing



once returns a page.



The SEARCH command displays the check data by one-touch operation, without repeatedly pressing the



page key.



The explanation of operations (1) and (2) given above is omitted here as they both apply in this case.



(4) Press function key [F5] {SEARCH).



"= F" is displayed on the display screen console line.



{5) Enter the desired page number through the keyboard.



The input data is displayed following "= F



LJ ".



Example: = F



(6) Press the WRITE key.



This will display the desired check data.



When the WRITE key is pressed without inputting data following"= F



LJ ",



the menu display shown



below will be displayed.



AUTO OPERATION



CHECK DATA INDEX



NO. ITEM

* 1 NC SPEX TABLE



2 NC AXIS DATA



3 NC AXIS DATA MAG. DISP.



4 PLC AXIS DATA



5 PLC AXIS DATA MAG. OISP



6 MEMORY DATA



7 MCS DIAGNOSIS



8 SYS. VAA. AXIS DATA



9 SYS. VAR. ZERO OFFSET



10 SYS. VAP.. ZERO OFFSET MSB



11 SYS. VAP.. TOOL OFFSET



12 SYS. VAP.. TOOL OFFSET MSB



I rput a nunber of screen. ! 1



Input a nlJllber of screen. !



NO. ITEM



13 SYS. VAA. SYSTEM PARALETER



14 SYS. VAA. HOME POSJnON



15 SYS. VM. NC COMMUNICATION



16 SYS. VAP.. VAP.IOUS DATA



PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PROGfW.I DATA SEARCH ATC/APC DATA [EXTEND1



Fig. 6-17 Check Display Screen



Input the number for required item and press the WRITE key to display the first page of the required item



screen.


```text


                                                                                                ──
                                                             ┌──┐─┐────┐─┐────┐─┐─┐─┐──┐─┐──────░░────────░
                                                             │░░│ │░░░ │ │░░░ │░│ │░│ ░│ │░ ░░░░──░░░░░░░░░•
          ┌───────  ──     •              •   ────  •     ─── ──┘─┘────┘ └────┘─┘ └─┘──┘─┘────          •
          │       ──   ──── ─────────────┐ ┌──    ── ─────                                                 │
          └──────┐  ┌─┐           ░ ░    │ │░  ──          ┌───────────────────────────────────────────────┘
                 │  │ │  ─┐ ┌┐─ ──────   │ └─ │    •      ┌┘
                      │   │ └┘ •         │    └───┐ ┌──── │
                  ──  │   │ │ •   ────  ┌┘ │      │ │   ░•
                      │  •  │  │       ┌┘  │  │      •    ─────────┐
                      └──  ─┘  │ ┌─┐─  │  ─┘  │  │  │    •         │
                  ──  │  ─┐ └─ │ │ │ ┌─┘    •░░• └──┘  •  • ─────  └┐─┐───┐─┐─┐─┐─────┐
                      │   └─┘   •    │░│     ──  │░░│ ░░│    ░░░░│ ░│ │ ░░│ │░│ │░░ ░░│
                      │        │░┌─  └─┘          ┌─ • ┌┘────────┘──┘─┘───┘─┘─┘─┘─────┘
                      │      │ │░│  •             │  ░░│
                      │░     │ └─┘            │ │ │  ──
                 ┌────┘      └─┘  ──       •  └─┘ │    ────────────────────────────────────────── ────── ──
                ┌┘░░ ░░░░░░░   ░░░ ░░  ░ ░░░│ ░░  │░   ░                          ░              •      •░
                │    ───────────────────────┘─────┘────────────────────────────────────────────── ────── ───
                │  ░
                │░──       ░     ───   ─────────────────── ────┐────── ──  ──────  ───┐─ ────────────────┐
                └┐  ─┐                                         │      •  ──      ── ░ │    ░             │
                 │ │ └┐      ────   ─┐  ──┐──────    ┌───     • •      ──  ──────  ───┘─ ───────── ──────┘
                 │ │  │     •    ─── │    │         ─┘
                  •   └───┐  •      │ ────┘─┐        └──────────────┐
                      │   │   ───   │       └─      •               │
                 ┌─┐  └───┘ •      ─┼─┐──                    │     ─┘┐
                 │ │ •       │ │    │ │░░───    ──     ░     │░░░░░░░│
                      • ──   │ │ ──┐┘ └──             ┌─┐ ┌──┘───────┘
                     │    ───┘ │   │         ─────   ─┘ └─┘
                     │░     ░└─┘───┘ ── ┌────     ───      ──
                      ──  ───┘          │
                 ┌─┐    ──   └──────────┘
                 │░│  │ ░░░ •░    ░ ░ ░░└┐
                 └─┘  └───        •    • └───┐───────┐──┐
                      │       • ── ── ░ •░   │   ░   │░░└─
                     │    ┌─┐  │ ░• ░     •                ─── ─────── ───────         ─────────────────────
                     │    │ │  │    ─────┐ ┌───   ────  ───   • ░     •                 ░        ░  ░    ░
                      │░░░░ │░─┘────░░░░░└─┘   ───    ──   ──  ─────── ───────         ────────────────────
                      └─────┘                 •   •  •
                                  ───────────                              ───────  •   •
                            •    ░░░░ ░░░░ ░░ ─┐              ────────┐──── ░     ──░│   │
                           │ ┌─   ──────── ──  │         │   •        │░░░░ ── ░ ░░░░│   │
                           │ │   │             └─────────┼─ │     ─┐  └─────     ────  │ │
                           │ │   │░•   ──░──             │░░│    │░│        •  ──      │ │
                           │ │   │  ──┐░░  ░──            │  ─┐  │░│ ──────░░── ░│     │ │
                           │ │   │░│▒ │░░ │░░ ──┐ ───┐    │░ ░│  │░ │░▒░ ░░  ░▒  │     │ │
                           │ │   │░│░  ░░░│░░░░░│   ░└─   │░ ┌┘  └┐ │░•░▒▒░░░░│ ░│     │ │
                           │ │   │░ ┌──░░░│░░──░│  • │    └──┘   └┘ └─ ───────┘ ─┘     │ │
                           │ │   │░ │▒░░  │░   •    ─┘                                 │ │
                           │ │   │  ░┌── ░░░░─┐                                        │ │
                           │ │   │░ ░│  │░│ ░░└─┐──┐ •                                 │ │
                           │ │   │░ │░│ │░│ │░│ │░░└┐  │                               │ │
                           │ │   │  │░│ │░│ │░│ │░░░│ ─┘                               │ │
                           │ │   └─ └─┘ └─┘ └─┘─┘─── ░░│                               │ │
                           │ │                       ──┘                               │ │
                           │ │   ──┐                                                   │ │
                           │ │  │ ░│   │░░──   •  ░•                                   │ │
                           │ │  │░ │   │    •       •    ──     ┌─ ────       ──    •  │ │
                           │ │  │ ─┘───┘░─┐┐ ┌──┐ ─┐ ┌──┐  ─────┘ •    ┌┐─┐──┐  ── • │ │ │
                           │    │░░░░  └┐░└┘ │░░└─ │ │ ░│          •   └┘ │░░│    • ─┼─┘ │
                            │   │░ ──   │░ │  │░░░░│ │  │   │  •  │ ──┐┘ ┌┘──   ┌─   │   │
                            └── │          ░  └─ ┌─  │  └───┘   │ │   │  │    │ │     ┌──
                               •   │ ░│   │ │  ░ │ ░  │░   ░ │░ │ │ │░ │ │ ░│ │ │  │ ░│
                                ───┘ ─┘───┘ └────┘────┘──────┘──┘─┼─┘──┘─┘──┘─┘─┘──┘──┘
                                    •      •                      │
                                                ░ •      • ─── • ─┘──── ────
                                                 •        •     •      •
                 ─────┐────────────┐────────────   ──────  ┌─┐─┐            ───────────────────────────────
                │░░  ░│  ░░░░░░░░  │░ ░ ░░░░░░ ░░ ░ ░░░ ░│ │░│ │░│░░    │░░ ░   ░ ░   ░ ░  ░ ░          ░
                │    ┌┘────────────┘─────────────────────┘─┘─┘─┘─┘──────┘──────────────────────────────────
                └────┘










```

*Figure from page 22 (2346x3317 px)*


---



7-1 . Display Screen



4203-E P-136



SECTION 6 DISPLAY ON NC OPERATION PANEL



7-1-1. NC Specification Codes



The NC SPEC TABLE screen has three pages and page selection is possrble using the page keys.



AUTO Cf>ERATION



CHECK DATA NC SPEC TABI..E



NO. data



1 11111011=FB



2 10001010:SA



3 00110000=30



4 11111111=FF



5 00000000=00



6 01000100=44



7 10000000=80



8 10100011=A3



9 00000000=00



10 00110111=37



11 10101000=A8



12 00000000=00



bit7 bit6 bit5 bit4 brt3 bit2 bitl bitO



SDFP SBPR ECAL SYV 0100 011.tC REVF I l'U..



T100 T300 T200 Z050 Z020 3DCR MVOL LSTR



BFUN EPII) PHD3 PH02 PHlN S6AX S5AX S4AX



GSOS G62S G61S G43S G92S G31S G60S HELi



EPSN 0Kl.fA 232C FlPR FlD4 F1DG PAMC



MADS FAPD Bl.SM EC-T AX-T EC-P AX-P



GRTB SYC5 RLn RL TO SYC4 SYCZ SYCY SYCX



EXP4 EXP2 GRP PPC I GF FOF I FDFO COLA



AXCH EXPB EXPA MIR6 MIR5 MJR4 BSP3 BSP2



EI GF EPBI( MSG G22S G28S MAP5 MAP4 MAP2



SSTP RET AXSC MEED PHID AXSL JGNF SFTH



EIML EGCA DNC3 DNC2 DNCl DNCB DNCA NPPC



PROOWJ ACTUAL PART BLOCK CHECK



SELECT POSIT. PROGRAM DATA SEARCH ATC/APC DATA (EXTEND]



Fig. 6-18 NC Specification Codes Screen


```text


                                                                                                ┌──
                                                              ┌──────┐──┐─┐───┐──┐─┐────┐─┐─────┘░░────────░│
                                                              │░░░ ░░│░ │ │░░░│ ░│ │░░░░│ │░░░░░░──░░░░░░░░┌┘
              ──────                ──────────────────────────┘──────┘──┘─┘───┘──┘ └────┘ └─────      ─────┘
           ┌──      ────────┐─┐────                                                                         │
           │░  ┌──── ░  ░   │░│    ─────────────────────────────────────────────────────────────────────────┘
           │ • │    ┌────── └─┘ ───
           │  ─┘┐   │          •    ────┐
           │    │  •░  •░░░░░░░░ • • ░░░│
            ────    •   •   ─┐─┐  │ ──┐─ ─┐───┐────┐─┐───┐─────┐──┐─┐─────┐─┐────────┐─┐─┐───┐─┐──┐─┐───┐
                 ──    │ │   │ └┐░└─  │ ░░│  ░│ ░ ░│ │░░░│ ░ ░ │░░│ │░░░░░│ │░░░░░░░░│ │░│░ ░│ │░░│ │░░░│
                   ────┘─┘───   │               ───┘ └───┘ •   └──┘ └─────             └─┘───┘─┘──┘─┘───┘
                                  ────────────      •     •                ─────     ─┐
                             │ ┌─  ░░░ ░░░░ ░░ ─┐ │        ────────────┐───  ░░ • ── ░│   │
                             │ │  │ ──────┐───  │ └───  ──┐            │░░░░─── ░ ░░░░│   │
                            │ │   │       │            •  └─  •         ───    ───────  │ │
                            │ │   │░  ┌─  └─   ┌──   ──     •  ─┐───┐─┐     ┌─┐         │ │
                            │ │   └──┐┘░ ░│ ─┐ │░░┌──░  ░│  ░│  │░░ │▒│ ──  │▒│         │ │
                            │ │   │  │░───░ ░│ │ ░│ ░░│ ┌┘──┐┘┐─┘░│ │░ •░░│ ░ │         │ │
                            │ │   │  │░░░░│░░│ └─▒│░│▒│ │░░ │░│ ░░│ └┐░ ░░└┐░░│         │ │
                            │ │   │░ │░░░░│░░│ │░░│░│░│ └──┐░░│░──┼─ └─┐░░░│▒░│         │ │
                            │ │   │░ │░░│░│░░│ │░│ ─┘▒│    │░░│ ░ │ ░│ │░░░│▒░│         │ │
                            │ │   │  │░─┼─┼─░│ │░│  │░│ ░│ │░░└─░░  ░│ │░░ │░░│         │ │
                            │ │   │░─┘░░│░│ ░│ │░│ ░│░│ ─┘ │░│  ░│ │░│ │░░ │░░│         │ │
                            │ │   │░ │░░░░└─░│ │░└─┐░▒░│░│ │░└───┼─┘░│░└─┐░└─░│         │ │
                            │ │   │░ │░░░░░░░│ │░▒ │░│ │░│ │▒░░░░│░│▒│ │▒│░│▒░│         │ │
                            │ │   └─ │░░░░▒░░│ └───┘─┘─┘─┘░└─────┘─┘─┘░└─┘─┘──┘         │ │
                            │ │     • ─────── •           •           •                 │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │   •                       ──      ─┐────       ──       │ │
                            │ │  │░─────────┐─┐──┐    ┌──┐  ────┐─ │    ┌──┐──┐  • ───┐ │ │
                            │    │░░░░░ ░ ░░│ │░░└──  │░░│      │  │    │  │░░└─      │   │
                             •   │░─┐─┐ │ ░ │ └─░░░░• │░ │      │ ─┘───┐   └──       ░│   │
                              ── │  │ └─┘  ░│   • ┌─  │  └──     •     │       │ ┌─    ┌──
                                •  ░│ ░ │  │  ░ ░ │ │  │░│    │░   ░ │░ │ ░ ░│ │ │ ░░ ░│
                                 ───┘ ──┘  └──────┘─┘─┐┘─┘────┘──────┘──┘────┘─┘─┘─────┘
                                     •   ──           │
                                             ░ ┌─░    │░          ──  ── ─┐   ───
                                             ──┘ ─────┘───────────      • │ •    │
                                                                              ───┘









































```

*Figure from page 23 (2346x3317 px)*


---



4203-E P-137



SECTION 6 DISPLAY ON NC OPERATION PANEL



7-1-2. NC Axis Data



The NC axis data is displayed in decimal numbers on the display screen, as shown below.



AUTO OPERATION



~~;0711\



14:10:00 1



CHECK DATA NC AXIS DATA P 4 llTlll



y z



RDIF 0.001 0.001 0.001



ODIF 0.000 0.000 0.000



RCON 35999.999 35999.999 28799.999


#### RAPA 35999.998 35999.998 28799.998

RSAPA 0.000 0.000 0.000



RSVPVARl 0.000 0.000 0.000



RSVPVAR2 0.000 0.000 0.000



RLEDATA 00000000 00000000 00000000



RFEDIDC 00000000 00000000 00000000



FIDFR(AK) 0000 0000 0000



PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PROOWA DATA SEARCH ATC/APC DATA [EXTEND]



Fig. 6-19 NC Axis Data Screen



RDIF Difference between calculated value and position encoder output



ODIF Difference between calculated value and position encoder output with acceleration/



deceleration activated



RCON Calculated value



RAPA Position encoder output



RSAPA Position encoder output when contact with the touch setter is detected



RSVPVAR1: Servo data (Designate the content of display with NC optional parameter (word) No. 10.)



RSVPVAR2: Servo data (Designate the content of display with NC optional parameter (word) No. 1 O.)



RLEDATA Absolute scale data



RFEDIDC Position encoder data



FIDFR(AK) : Indicates the inductosyn ON/OFF state.



0000 .... lnductosyn effective. For the axis for which inductosyn on/off is ineffective,



"0000" is always displayed.



8080 .... lnductosyn ineffective.



8000 .... lnductosyn effective/ineffective status is changing from ineffective to effective.



0080 .... lnductosyn effectivenneffective status is changing from effective to ineffective.


```text


                                                                                                ── •
                                                             ┌───────┐─┐─┐───┐──┐─┐────┐─┐──────░░• ──────┐
                                                             │░░░░░░░│ │ │░░░│ ░│ │░░░░│ │░░░░░░──░• ░░░░░│
            •  ───             ──────────────────────────────┘───────┘─┘ └───┘──┘─┘────┘─┘─────        ──
          ┌┐  •    ───────────                                                                             │
          └┘─┐ •   ░           │                                         •      •  •          ─────────────┘
             └─  ──  •       ──┼────────────────────────────────────────┐ ┌────┐  • ┌─────────
                │░ ░ ░│ ░░  ░░░│   ░ ░░       ░    ░      ░     ░       │ │    │ •  │░      ░  │
                └─────┘────────┘             ───────────────  ────     •      ─┘    │ ─────────┘
                                 ────────────
                            │   │ ░░░ ░░░░  ░                            ─────   ────┐   │
                            │ │ │   │      ───  •  •  ──  ┌────────── ┌─ ░░ ░░ ░│░  ░│   │
                            │ │ └──░└──────   ─┐░  ░ •░░ ┌┘           │░───────░└────┘   │
                            │ │    ─┘          └──┐    ──┘            └─       ─┘      │ │
                            │ │      ┌─           └── │      ┌──          •            │ │
                            │ │      │▒─┐         │░ ░│      │░ ──      ┌─ ┌─┐         │ │
                            │ │      │░░│       ──┘░ ░│    ──┘░ ░░│   ┌─┘░ │░│         │ │
                            │ │      │░░│       ░░░░ ░│    ░░░▒ ▒▒│   │░░░ │░│         │ │
                            │ │      │░░└─       ──  ░│     ──  ░░│    ─── │░│         │ │
                            │ │      │░░░░─┐       ░•░│       ░ ░░│        │░│         │ │
                            │ │      │░▒░░░│    ┌───░░│    ┌──░•░░│    ┌──┐┘░│         │ │
                           │ │       │░▒│░░│    │░░░░░│    │░░│░░░│    │░░│░░│         │ │
                           │ │       └──┘░│░    └─────┘    └──┘─░─┘    └──┘░─┘         │ │
                           │ │           ─┘─                    •          •           │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │  ┌──────────   ──    ──    •             ── •  ──       │ │
                           │ │  │░░░░░░░░░░│ │░░───┐ ░──┐  ─┐──┐─┐──────  │░──  ─┐────┐  │
                           └┐   └─ ░• ───░─┘ │░░░░░│ •░░│   │░░│ │ ░  ░   │░░    │░░░ │  │
                            │                   ───┘   •    │ ─┘ └─         │   ┌┘      ─┘
                             ───   │   │  │         │   │ ┌─ │     ─┐─      │ │ │ ┌─  ┌─
                                │ ░│ │ │  │    │ │ ░│ │ │ │░ │░│    │░     ░│ │ │ │▒ ░│
                                └──┘ └─┘──┘────┘─┘──┘─┘─┘─┘──┘─┘─   └──  ───┘─┘─┘─┘───┘
                                    •                            ───   ──
                                                 │░│ ░ ░ •░│ │░░░ ░░• •░░░░░•
                                                 └─┘      ─┘ │    ──   ─────
                ┌───┐        ┌───────┐─────── ───   ──────  • ────  ───     ───┐─┐────┐
                │░ ░│        │░░░░░░░│ ░░░░░░•  ░ ░ ░░░░ ░░░░ ░░░ ░░░░░  ░ ░░░░│ │ ░░ └─
                │░ ░│        │ ░       ──░     ──   •   ┌─┐ • ┌─┐  ───    ┌────┘   ──   ── ── │ ───────────
                └───┘        │       •        •   ── •  │ └─  │ └──    ───┘       •  │        │ ░
                │    │       │░░░░░ ░░░  ░░░░░░░──           •        •    • ─────   └──────── ───────────
                │░ •░│       │ ──────────   ────
                │    │       │            •     ──┐
                │░░░░│       │░░░░┌──┐░░──░│ │░░░░│
                │    └┐      │    │  │     │ │    └─────────────────┐───────────────┐──────┐
                └─░░░░└──    └─░░░░ ─┘░░░──┘─┘── ░ ░░░   ░ ░░░ ░░░ ░│░ ░ ░░ ░░░░  ░ │░░░░░░│
                │ ────   │   │  ───    •            •       ──               │             └┐─ ─────┐─┐─┐─┐
                │      ──┘┐  └─┐   ┌─── ┌─  ░ ──┐  │ │         •░  │ ┌── ┌─┐ └─░────┐░ ░──░░│ │░░ ░ │░│ │░│
                └─┐────░░░│  │░│   │░   │░─┐─  ░│  │ │    │    ░   │ │ ░ │░│        │      ░│ │     │ │ │ │
                │ │      ─┘  │   ──┘   •   │ • ─┘──┘─┘────┘────────┘─┘───┘─┘────────┘──── ──┘─┘─ ───┘ │ └─┘
                │░└┐─░░░│    │░░░░ │░ ░░░• │░░│
                └─ │  ──┘    │                └─┐
                │░ │ • ░└┐   └──░░── •░░░░── │░░└┐  ───────
                │  ░░░  ░│   │   •    ┌───   └─  │ │        ───┐
                └────────┘   └───   • │     •    └─┘       •   └──┐─┐──┐─┐───┐─┐──────────────────────────
                             │░░░┌──  │ ░░░░ ░░  ░░░░░░░      ░ ░ │░│ ░│ │░░ │ │ ░ ░         ░ ░ ░ ░░  ░
                                 │    └─ ──┐───  •            ┌───┘─┘──┘─┘───┘─┘──────────────────────────
                            ┌────┘    │    │        ───      ─┘
                            │░░░░│     ────░ ░─┐────░░░──
                            │    │    │     ── │          ─────────┐─┐─────┐────────┐─┐─┐──┐───┐───┐──────┐
                            │░░•░│    │░░░░░░░░│ │░│░░│░░░░░░░░░░░ │░│░    │░░░░ ░ ░│░│ │░░│ ░░│ ░ │░░░░░░│
                             │  ┌┘    └┐       │ └─┘  │      │     │ │     │        │   │ •         •     │
                             │ ░│      │░░ ░░░░│ │░░░░│░ ░░░░│░░░░ │░│░    │░░░░ ░ ░ ░░ │░░░░░░ ░ │░░░░░░ │
                             └──┘    ──┘───────┘─┘────┘──────┘─────┘─┘─────┘────────────┘─────────┘───────┘
















```

*Figure from page 24 (2346x3317 px)*


---



4203·E P-138



SECTION 6 DISPLAY ON NC OPERATION PANEL



The NC axis data screens also include the following page where ODIF, RAPA, and LOAD values are



displayed in enlarged characters. This page is displayed by pressing the page key from the screen



indicated above.



AUTO OPERATION



CHECK DATA


# NC AXIS DATA

j 97/07/1: 14:10:00



1nm


# ODIF RAPA


# 0.000 35999.998


# 0.000 35999.998


# 0.000 28799.998


# LOAD

PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PflOO'iAM DATA SEARCH ATC/APC DATA [EXrEND]



@J @J @J @J @J @J@J



LOAD Axis loaded status is displayed in %.


```text


                                                                                               │ ──       •
                                                             ┌──┐──────┐─┐───┐──┐─┐─┐──┐─┐─────┘░░░─┐ ────░░
                                                             │░░│ ░░░░ │ │░░░│░░│ │░│ ░│ │░░░░░░───░│ ░░░▒░•
           ┌─────   •       •           •                     ──┘    •     ──┘         └─┘─────        ──
           │     ──┐ ┌─┐─┐─┐ ┌──┐─────── ───┐──────┐────────┐─   ───┐ ────    ────────┐                    •
           └────┐ ░│ │░│ │ │ │  │           │      │    ░ ░ │       │     │ │░    ░   │          │          •
                │  │ │     │ │ • •      ──  │   │  │ ┌──    │  ──── │     └─┘  │ •    └──  •     │ │    ───┐
                │ ░  ░░░  ─┘─  ░░░░• │ ░ ░ ░░ • └─ │ │░░░   │░░░░░░░│ ░  ░░░░░░│ ░░  ░░░░ │░░ │░░│ │░ •░ ░░│
                 ──░░░░── ░░░░───── ─┘────────    ─┘─┘────── ─────── ──────────┘──────────┘───┘──┘─┘ • ────
                   ────  ─────
                                ──┐─┐─┐───┐──┐───────────            •       •         ──
                            │   ░ │░│ │░░░│░░│                        ┌──────░── ────┐   │
                            │ │ ──┘ │   ─┐┘─  │  ───┐──  ───┐── ───── │░░░░░ ░ ░ ░░░░│   │
                            │ │   │░░  ░ │  │▒│ │▒░░│ ░ │░░▒│ ▒•       ───────  ░░┌──    │
                            │ │   └── ───   │░░─┘ ──┘───┘───┘─  ─────         ──  │   ──┐
                            │ │      │      │▒│░│░            ──░▒▒░░───   │░ ░▒▒▒│  •▒░│
                            │ │    │░│      └┐┘┐┘░░•░│    ┌─░░░░░─┐─░░░░│  └───┐─┐┘   ──┘
                            │ │    │ │       │ │ │   │    │  │    │ │   │      │ │       │
                            │ │    │░│       │░│ │▒•░│    │░░└───░│ │░░░│      │░│     │ │
                            │ │    │ │       │░│ │ ░░│    │░░░░  ░│ │ ░░│      │░│     │ │
                            │ │    │░│       │░│ │▒░░│    └─░░•░░░│ │▒▒▒│      └─      │ │
                            │ │    └─┘        •   ───       ── ─── • ───┘      │       │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                                                  ──                           ─────── │ │
                           │    ┌──────────┐─ ──    ────┐                 ┌── •        │ │
                           │    │░░░░░ ░  ░│ │░░───┐ ░ ░│   ┌──┐ ─┐────   │░░│   ┌────┐┘ │
                            │   └─░──────░─┘ │░░░░░│ ┌──┘   │░░│  │░ ░░•  └─░│ • │░░░░│  │
                            └┐                   ──┘ │  │   └─ │             │      ──┘ ─┘
                             └─┐  ░│     ░░   │ ░░   │  ░     ░│    ┌─┐           │   │
                               └─ ─┘ ░ ░ ── • │ ── ░ │  • ░• •   ░  │ │ ──     │░ │░  │
                                              │        •      • ──  └─┘─  •   ┌┘──┘───┘
                ──────       ┌──┐   ───── ─┐──   ──────  ─┐─                ──┘
                    ░        │░░│ │░░░░░ │░│     ░░░░░░░  │ ░│
                ──────       └──┘─┘──────┘─┘──────────────┘──┘











































```

*Figure from page 25 (2346x3317 px)*


---



4203-E P-139



SECTION 6 DISPLAY ON NC OPERATION PANEL



7-1-3. Diagnostics



Any memory content in the memory can be displayed in a designated format on the screen.



The diagnostics function si provided to be used by the machine tool manufacturer.



AUTO OPERATION



BIT


#### PROGRAM

SELECT



-0.001



80000403



FFF807FF



Address displa



-0.001



00000000



00000000



-0.001



00000000



00000000



CHECK



SEARCH ATC/APC DATA [EXTEND]



Decimal code indicatiOn (4 b es)



Decimal code indication (4 bytes or 2 bytes)



Hexadecimal code indication (4 bytes)



Floating decimal point indication (8 bytes)



Bit string indication (1 byte)



Fig. 6-20 Diagnostics Screen



Displayed to the right of the diagnosis data: indicates the cursor key operation enabling



position.



(Once a check address is set in the conventional manner, check address is increased or



decreased in units of the data type being checked by pressing the cursor keys



@ , @ ,



@,@.)



b) W : 2-byte indication of DCM data



L : 4-byte indication of DCM data


```text


                                                                                                ── •       │
                                                             ┌───────┐─┐─┐───┐──┐─┐─┐──┐─┐──────░░• ──────░│
                                                             │░░░ ░░░│ │ │░░░│ ░│ │░│ ░│ │░ ░░░░──░• ░░░░░┌┘
                             ────────────────────────────────┘───────┘─┘─┘───┘──┘ └─┘──┘─┘─────      ─────┘
          ┌────    ──────────                                                                              │
          │        ░         │                                                       ──         ───────────┘
          └────  ──  │       └──┐──────┐─┐─────────────────────────────────────────┐─  ──┐──────
                │░░░─┼────     ░│     ░│ │░░      ░     ░░                    ░    │     │      │
                │    │     ──┐ │  ┌──    │                    ─┐  ──                     └──────┘
                │░ ░ │░░░░░░░│ │░ │░ ░ ░ ░ ░░░░░ ░ ░│  ░░░    ░│  ░░░ ░░ ░░░ ░░░ ░░ ░ ░░│
                └────┘───────┘─┘──┘─────────────────┘────────── ──        ──────────────┘
                                                               ░░░░░ ░░░░│
                               ┌──               ────────  ──  ──────────┘               •
                              ┌┘    ──┐─┐───────         ──░  •                ──      │  ─┐
                              │  •  ░░│ │░▒░░░▒           ░ •     •      ┌─────░    ───┼┐  └┐
                              │ │  ───┘─┘───┐───  ┌─────  ┌─ ───── ──────┘░░░░░░│░░░░░░└┘ │ │
                              │ │           │     │░░   ░─┘              └──────┘──────┘  │ │
                              │ │  ┌──  •  ─┘──    ───┐   │       ┌───┐                   │ │
                              │ │  │░░•░░  ░░░░│      │░ ░│       │░ ░│      •  ░░│       │ │
                              │ │  │  ░        └┐    • ───┘       └───┘       ────┘       │ │
                              │ │   │░░•░─┐────▒└┐                                        │ │
                              │ │   │ •   │░░░░░░│      │                                 │ │
                              │ │   │   ░ │░░░░░░│    ──┘─        ──            •
                              │ │  ┌┘░  ░ │░░░░░░│   │░░░░│      │░░──┐     ┌──░░│       │
                              │ │  │   │░░│░───░░│   └────┘      └──░░│     │░░──┘       │
                              │ │  │░░ │░ │░▒░▒░░│                                       │
                              │ │   ── │  │▒▒▒░▒░│                                       │
                              │ │      │░ │░▒░▒░─┘                                       │
                              │ │   • ─┘──┘─────  ─┐                                     │
                              │ │                  └┐                                    │
                              │ │          •        │                                    │
                              │ │             •     └─      ──     ─┐────┐─      • ──    │
                              │   ┌────────── ░┌──░   ─────┐  •   • │    │ ─┐── • •      │
                              │ • │░░░░░  ░ ░┌─┘░░────░ ░░░│ │ ──┐  └────┘  │░░│   ┌────┐┘
                              │    ┌─────────┘ └┐─░░░░• •░┌┘ │  ░│   ░░ ░░• └─░│   │  ░░│
                                •  │            │ │ ──    │      │         ─┘           │
                                 •  ░░ ░ ░ ░░ ░ │ │░ ░ ░░░└─░  ░░░    ░░░    ░░░    ░░░
                                  ──────────────┘─┘─░░ ───░░ ──────  ────────────────────
                                                    ─┐─
                                                     │         ░░░░░░░░•░░░░░░│ ░ ┌─░┌───  ──
                                                      ─┐       ────────░──────┘   │ ─┘    •  │
                                                       └┐     │                ───    ───   ─┘
                                                        └┐    │░░░░░░░░░░░░░░░░░░░░░░ ░░░•
                                                         └┐   └───── ──     ───     ┌───   ┌─
                                                          └┐  │     •  ────    ──   │   • ─┘
                                                           └─ │░░░░░░░░░░░░░  ░░░─── • • •
                                                               ────── ───────────
                                                 ──────────────      •
                                                   ░        ░░░░ ░░░  ░░░░░•
                •         ┌─ ──  ───────── ──────            •    ──      │  •
                         ┌┘ •  ──     ░          ░            │          ─┼─  ┌─┐───   ───────────┐────────┐
                ──       │        ──────────┐─────────────────┘───  ───── │ ──┘ │   ───           │        │
                         │  ░•░──           │                                                              │
                         │  •     ┌──── ┌───┘─┐   ┌─┐─  ┌─ ──── ──────┐ ┌───── ───────┐─────┐───  ────── ──┘
                         │   ─────┘     │     └─┐─┘ │ ──┘ •    •      │ │░    •   ░ ░ │░░ ░░│ ░ ┌─░ ░░░░• ░│
                         │   ░  ░ ░ ──  ░  ░  │ │              ░  ░    │ │         •  │ ┌──   │ │░┌───┐░  ─┘
                         └┐   ┌─┐      ───────┘─┘──────────────────────┘─┘───────── ── ─┘    ─┘ └─┘   └───
                          │ ░┌┘ └─░ │                                                      ──
               ┌─┐ ┌─┐   ┌┘  └┼─┘   └──┐───────────┐
               │░│ │░│   │░░░░│ ░───░░░│ ░ ░░ ░░░░░│
               └─┘  ─┘   │    │ │   │  │      ──┐  │
                   │ │   │░░│░│ │░░ │░░│    ░ ░ │░░│
                   └─┘   └──┘─┘─┘───┘──┘────────┘──┘



















```

*Figure from page 26 (2346x3317 px)*


---



4203-E P-140



SECTION 6 DISPLAY ON NC OPERATION PANEL



7-1-4. System Variables



The contents of the system variables are displayed on the screen.



Some of system variables (tool offset, etc.} cannot be displayed in one page. For such variables, the next



page can be displayed by pressing the page key.



For details of the system variable names, refer to "System Variables" in the Programming Manual.



[Supplement] On the display screens where axis related system variables are displayed, those for the



first additional axis are displayed to the right of the "Z-axis" data. For the second and



third additional axes, the data is displayed on the page accessible by pressing function



key [F8] (EXTEND) and [F6] (AXIS CHANGE).



(1) Axis Data



AUTO POEAATION



CHECK DATA


#### VRCO"'


#### V1'i'A*


#### VSAPI'


#### VDIW


#### VALA*

VODW


#### VDMPI'


#### VDOA*

VVDA*


#### VDA!r

SYSTEM VARIABLE



35999.999



35999.998



0.000



0.000



000



0.000



5243



256



3880



35999.999



35999.998



0.000



0.000



0.000



0.000



5243



256



3880



28799.999



28799.998



0.000



0.000



0.000



0.000



5243



256



3880


#### PROGRAM ACTUAL PART BLOCK CHECK

SELECT POSIT. PRJGRAM DATA SEARCH ATC/APC DATA (EXTEND]



Fig. 6-21 System Variables Screen -Axis Data


```text


                                                                                                ────
                                                              ┌─┐───┐─┐─┐─┐───┐──┐─┐──┐─┐─┐─────░░ ░ ──────┐
                                                              │░│░░ │░│ │ │░░░│ ░│ │░ │░│ │░░░░░░──░• ░░░░░│
                 ──                ───────────────────────────┘─┘───┘─┘─┘ └───┘──┘─┘──┘─┘ └─────       ──
           ┌─  ─┐  ───────────────                                                                          │
           │  •░│   ░  ░    ░            •                          •      ─────────────────────────────────┘
               • ┌──     │         ─────┐ ┌────────────────────────┐ ┌────┐
                 │░░────░│ ░  ░ ░░ ░ ░░ │ │░░░░░   ░░ ░░  ░ ░     ░│ │    │
                 │                 •   •  │  •      •            ──┘─ •    ─┐─────┐─┐─┐──────┐──────────────┐
                 │░──░•░░░░░░░──┐──░░░░ ──░──░░░░  ░░• ░░ ░░ ░░ ░░░░░░░     │░ ░░ │ │ │ ░  ░ │░ ░░░░  ░░    │
                 └─  • ────┐─┐  │  ────   •   ─── ──        ─────────────  ─┘─────┘─ ─┘──────┘──────────────┘
                 │    •    │ │                                           ──         •
                 └─┐─ ░░░│    ░│ ┌─░│  ─┐    ┌──     ── ░┌─   ░    │ │░  ░  │       ░ ────    ── ░─────┐
                 │ │ ────┘   ──┘─┘ ─┘   │    │    ───   ─┘         │ └─     │       •  ░       ░┌─     │
                 │░ •       │    │      │                          │         ───   │     ────   │       │  •
                 └─   ──────┘    │   ┌─ │ ──────  ─── •  ─────┐ ──  ───┐───── ░ ───┘ ░ ──  ░ ───┘ ───┐──┘── │
                   ───          ┌┘ ──┘░•░•░░░ ░░──░ ░•░░•░░░░░└┐ ░░• ░░│ ░ ░░  ░ ░░░  ░░░  │ ░ ░░ ░░░│░░ ░░ │
                                │░  ░ ░░░░ ░░░ ░░░│ ░░ │░░░── ░│░░░░░ ─┘ ░░──░░░───░░░──── └─ ───░░░░ ── ░ ─┘
                                 │  ─┐ ─── ░  ░░ ┌┘─── │ ──  ┌─┘───     ░┌─  ───   ───    ─┘ •   ─────  ───
                                 │ • └─   ───────┘    • •░ ──┘     ──────┘
                       ─────────

                        ─── ──                   ──────────────────────────       ───  ──┐
                                  ┌────┐──┐──┐                              ── ───   ─┐  │
                            │  ── │░░  │░░│ ░│   ─────────── ┌────────┐ ┌─── ▒│      ░│   │
                            │ │  ─┘─░──┘──┘──┘──┐   ░        │        └─┘░░░ ░│ ░ ░░▒┌┘ │ │
                            │ │     •           │       ────            │ ── • ──────┘  │ │
                            │ │                   ────       ────        │              │ │
                            │ │       ┌───       ▒░░░░─┐    │░░░ ─┐    │░│░ ┌─┐         │ │
                            │ │       │░░░•     ──┐┐░░░│    └─░░ ░│    └─┘░ │░│         │ │
                            │ │       │░░│        └┘ │░│      │░ ░│      │░ ░░│         │ │
                            │ │       │░░│         │ │░│      │░ ░│      │░ ░░│         │ │
                            │ │       │░░│         │  ░│      └┐ ░░•     └┐ ░░│         │ │
                            │ │       │▒▒│          •░░│       │░░•       └┐░░│         │ │
                            │ │       │░░│           │░│        │░░•       └┐░│         │ │
                            │ │       │░░│           └─┘        └──         └─┘         │ │
                            │ │        ──┘                                              │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │  ┌─── • •            • •  ──            ─── •  ──       │ │
                            │ │  │░░░│  ░──┐────────  │ ─┐ ░─┐──┐─────┐─   │░──  ┌────┐ │ │
                            │  • │░ ░│   ░░│   ░░░  │ │░░│   │░░│     │    │░░ │ │   ░│   │
                             •   │ ──┘  ───    ─── ░│  │ │  ┌┘  │ •    •  ┌┘ │ │ │       •
                              ───          │       •   │  │ │ ┌─   │ ┌─ ┌─┘  └─┘─┘───  ┌─
                                 │░ │ ░│ │░│ │░ │░│ •  │░ │ ░ │░   │ │▒ │ │ ░│ ░  ░░░  │
                                ─┘──┘──┘─┘─┘ └──┘─┘    └──  ──┘──┐ └─┘──┼─┘──┘─────────┘
                                                    ───    │     └─     │
                                         │░ ░ │ ░│ │░░░│░  │░░│░│░░ ░│ ░░│ │░░░  ░░░│
                                         └────┘──┘─┘───┘───┘──┘─┘────┘───┘─┘────────┘































```

*Figure from page 27 (2346x3317 px)*


---



4203-E P-141



SECTION 6 DISPLAY ON NC OPERATION PANEL



(2) Zero Offset



(3)



AUTO OPERATION



CHECK DATA



VZ0F*[ 1]



[ 2]



[ 31



[ 4]



[ 5]



[ 6]



[ 7]



[ 8]



[ 9]



[10)



SYSTEM VARIABLE



0.000 0.000



0.000 0.000



-490.212



-361. 042



59.645



-90.355



-25.578



-820.799



-51.000



-1.500



-108.797



-108.797



41.201



-108.799



-389.835



-389.835



-108.800



-388.800



0.000



0.000



-258.854



-258.854



-78.854



-258.854



-250.034



-250.034



-417.216



-260.545



PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PROGRAM DATA SEAACH ATC/APC DATA [EXTE!t)J



Fig. 6-22 System Variables Screen Zero Offset



Zero Offset (for system)



AUTO OPERATION



CHECK DATA SYSTEM VARIABLE nm



X y



VSZO*[ 1] 0.000 0.000 0.000



[ 2] 0.000 0.000 0.000



[ 3) 0.000 0.000 0.000



[ 4] 0.000 0.000 0.000



[ 5] 0.000 0.000 0.000



[ 6] 0.000 0.000 0.000



[ 7] 0.000 0.000 0.000



[ 8] 0.000 0.000 0.000



[ 9) 0.000 0.000 0.000



[10] 0.000 0.000 0.000


#### PROGRAM ACTUAL PART BLOCK CHECK

SELECT POSIT. PROGRAM DATA SEAACH ATC/APC DATA [t/A~]



Fig. 6-23 System Variables Screen - Zero Offset {for system)


```text


                                                                                                ──
                                                             ┌──┐─┐────┐─┐───┐──┐─┐─┐──┐─┐──────░░─────────
                                                             │░░│ │░░░ │ │░░░│░░│ │░│ ░│ │░ ▒░░░──░░░░░░░░░
          ┌───────  ──           ────────────────────────────┘──┘─┘────┘ └───┘──┘ └─┘──┘─┘────          ───
          │       ──   ────┐────                                                                           │
          └──────┐  ──┐░   │░░ ░───────────────────────────────────────────────────────────────────────────┘
                 └──  └────┘────
                                 ─┐───────────────────
                            │  •  │░░ ░░░ ░░░                              ──┐───   ──   │
                            │ │ │ │   │    ────┐┐───────────  ───────┐ ┌─── ░│ ░  • ░░│  │
                            │ │ └─┘░│ │░ ──    └┘░░ ░ ░░ ░░░──       └─┘▒░░░─┘───┐▒┌──┘  │
                            │ │    ─┘─  •       └─     ─────            ─┐──     └─┘   │ │
                            │ │       ── ──       ┌──          •         │             │ │
                            │ │      │░░ ░ ─┐     │░ ┌─┐     ┌─ ──┐      └─ ─┐         │ │
                            │ │      └──┐─ ░│    ┌┘░ │░│     │░ ░░│     ┌┘░░░│         │ │
                            │ │         │ │░│    │░• │░│     │░ │░│     │░░░░│         │ │
                            │ │         │ │░│    └─░ ░▒│     │░ │░│     │░░░░│         │ │
                            │ │         │  ░│    │░░ ░░│     │░ │░│     │░░░░│         │ │
                            │ │         │   │    │░░ ░░│     │░ │░│     │░ ░░│         │ │
                            │ │         │  ░│    │░• │░│    •░░ │░│    •░░░░░│         │ │
                            │ │         │ •░│    └─  └─      ─┐ └─┘     ┌┐ ░░│         │ │
                            │ │          • ─┘                 └─┘       └┘───┘         │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │   ┌───────            ── •                ──    ──       │ │
                            │   │░░░░░░░───┐ ──────┐ ░•░•   ────────────░ ┌──┐  ──────┐  │
                            │   └─░░░   ░░ │ ░░░░  │  ░░░  •░░░░         ─┘░░│      ░ │  │
                            │           •    •     │        •           │ │  └┐  • │  │ ─┘
                             ──    │ │    │   │   • │      •  ── │  ┌─  └─   ░└── ┌┘  └─
                               │  ░│ │ │  │   │░ │ ░│ ░ ░ │░ │░  │░ │░│ │░ ┌┐     │░ ░│
                               └───┘─┘─┘──┘───┘──┘─ │ ────┘──┘── └──┘─┘─┘──┘┘───  └───┘
                                                   • •                          ──
                                         │░│ ░ ░│ │░░░░│ │░░ ░░░│ ░│ ░░│   ░░   ░░  │
                                         └─┘────┘─┘────┘─┘──────┘──┘───┘─ ──────────┘
                 ┌─┐ ┌─────┐───┐──┐─┐────
                 │░│ │░░ ░ │░░░│ ░│ │░░░░ ░
                 └─┘ └─────┘───┘              ─────────         ───   ─────
                                ─┐─┐─┐──┐─┐─┐─         ─────────   ───     ┌─┐         ──
                           │     │░│ │░░│░│░│                          •   │░└──── ──    │
                           │ │ ──┘  ┌┘┐─┼─┘─┘─ ┌─────────── ────       ░░░│ ░│ ░░░ ░░│ │ │
                           │ │   │░░│ │░│     ─┘░░░░  ░░░░░│          ──┐─┘──┘───────┘ │ │
                           │ │   └──    │      └───    ────┘            │              │ │
                           │ │          ░ ┌─┐      ─┐─┐      ┌───┐      │  ┌┐          │░│
                           │ │       ───┐ │░│     │ │░│      │░ ░│      │░ └┘          └─┘
                           │ │          │ │░│     │ │░│      │░ ░│      │░ ░░│         │ │
                           │ │          │ │░│      ─┘░│      │░ ░│      │  │░│         │ │
                           │ │          │  ░│     │ ░░│      │░ ░░│     │░ │░│         │ │
                           │ │           • ░│     │ │░│      │░ ░░│     │░ ▒░│         │ │
                           │ │          •  ░│     │ │░│      │░ ░░│     │░ ░░│         │ │
                           │ │           │ ░│     │ │░│      │░ ░│      │░ ░░│         │ │
                           │ │           └──      └─┘─┘       ───┘       ────┘         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                   ───      ─────────────         ────── │ │
                           │ │ ┌──────────┐─        ─┐── •              ──┐─ ──┐       │ │
                           │ │ │░░░░░  ░░░│  ──────  │ ░│  ────┐─┐─────┐  │░│  └┐───┐  │ │
                                ┌─────────┘  ░░░░░░• └──┘ • ░░░│ │░░ ░░│  └─┘   │▒░░└┐─  │
                                │         │      ──  │      •  │ └─   ─┘ │  │   └──┐ │  •
                                │  │    ──┘ │  ░      │      │░ │   •░ │ │ ░│   │  │ └┐─
                                │ ─┘ ──   │ │░     ── │    ░─┘░ │ •  ░ ░ │ ─┘ ░ │  ░ ░│
                                └─       ─┘    ────   └─      •    ───── │       ───
                                  ───┐──  │ ┌──    ┌──  ──┐─┐  ──┐      • ┌─────    ─────┐
                                    ░│ ░ ░│ │░░░░│ │░░ ░░░│ │░ ░░│  │░    │░░░░░░│ │░░░░░│
                                   ──┘────┘─┘────┘─┘──────┘─┘────┘──┘─────┘──────┘─┘─────┘














```

*Figure from page 28 (2346x3317 px)*


---



(4}



(5)



Tool Offset



AUTO OPERATION



CHECK DATA SYSTEM VARIABLE



VTOFH[N]



NO. NO.



1 1. 000 11 0.000



2 -65.974 12 -92.927



3 -65.629 13 -84.368



4 0.000 14 --85.932



5 0.000 15 --82.647



6 0.000 16 -76.238



7 0.000 17 -72.593



8 -92. 110 18 -79.892



9 -71.620 19 -80.586



10 -68. 702 20 -80.632



4203-E P-142



SECTION 6 DISPLAY ON NC OPERATION PANEL


#### N 1

97/07/15 14:10:00



11111



VTOFD[N]



NO. NO.



1 2.000 11 5.000



2 30. 100 12 30.000



3 0.950 13 3.250



4 0.000 14 3.990



5 0.000 15 4.730



6 0.000 16 5.500



7 0.000 17 6.500



8 1.925 18 6.960



9 1.500 19 51. 500



10 2.000 20 5.000



PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PROGRAM DATA SEARCH ATC/APC DATA [EXTEND]



Fig. 6-24 System Variables Screen Tool Offset



Tool Offset (for system)



AUTO OPERATION



CHECK DATA SYSTEM VARIABLE lllll



VSTOH[N] VSTOD[NJ


#### NO. NO. NO. NO.

1 0.000 11 0.000 1 0.000 11 0.000



2 0.000 12 0.000 2 0.000 12 0.000



3 0.000 13 0.000 3 0.000 13 0.000



4 0.000 14 0.000 4 0.000 14 0.000



5 0.000 15 0.000 5 0.000 15 0.000



6 0.000 16 0.000 6 0.000 16 0.000



7 0.000 17 0.000 7 0.000 17 0.000



8 0.000 18 0.000 8 0.000 18 0.000



9 0.000 19 0.000 9 0.000 19 0.000



10 0.000 20 0.000 10 0.000 20 0.000



PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PROGRAM DATA SEARCH ATC/APC DATA [EXTEND]



Fig. 6-25 System Variables Screen - Tool Offset (for system)


```text


                                                                                                 ───
                                                              ┌─┐─────┐─┐─┐───┐──┐─┐────┐─┐──────░░░───────┐
                                                              │░│░░░░░│ │ │░░░│ ░│ │░░ ░│ │░░░░░░──░░ ░░░░░│
           ┌──────   ──          ─────────────────────────────┘─┘─────┘─┘ └───┘──┘─┘────┘ └─────
           │       ─┐  ┌─────────                                                                           │
           └──────┐░│ ─┘     ░   ───────────────────────────────────   ─────────────────────────────────────┘
                  └─┘  └─────────                                   ───
                                   ────────────────────                                ───
                             │    • ░  ░░░░ ░░                              ───           │
                            ┌┘ ┌─┐ ░   │ ░  ───  ┌────────── ┌────      ░░•░ ░░   ░┌─┐  │ │
                            │ ┌┘ └──░──┘───┐   ──┘░ ░░ ░░░░ ░│         ──┐▒│ ───── │▒└─ │ │
                            │ │     •      │       ────────┐    ──────   └─┘       └─┘  │ │
                            │ │       │░░░░░│    ┌─        │ ┌─   ░░░░•     ─┐          │ │
                            │ │    │░ │     │    │░│    •    │░┌──┐        •▒│    • ─┐  │ │
                            │ │    │ │ ┌───░│    │ │  ┌─ ─┐  └─┘  └──┐─          │ │░│  │ │
                            │ │    │░│ │░░ ░│    │░│ ┌┘░ ▒│  │ │  │░ │░│    │ │  │ │░│  │ │
                            │ │    │░│ └┐░ ▒│    │░│ │░░ ░│  │░│  │░ ░░│    │ │  │░│░│  │ │
                            │ │    │░│  │░ ░│    │ │ │░  ░│  │ │  │░ ░░│    │ │  │░│░│  │ │
                            │ │    │░│  │░░░│    │░│  │░ ░│  │░│  │░ ░░│    │ │  │ │░│  │ │
                            │ │    │ │ ┌┘  ░│    │ │  │░ ░░│ │ │  └─ ░░│    │    │ │░│  │ │
                            │ │    │░│ │░  ░│    │░│  │░ ░░│ │░│  │  ░░│    │░  │░ │░│  │ │
                            │ │    └─┘ └───░│    └─┘ ─┘────┘ └─┘   ────┘    └─  └──┘─┘  │ │
                            │ │            •                •                           └─┘
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │  ┌───┐───            ─┐── ──      •       •             │ │
                            │ │  │░░░│  ░──── ──────┐ │░░│  ─┐──┐─ ─────── ┌───────────┐  │
                            │  • │░ ░│   ░░    ░░░  │ │░░│   │░░│          │░░       ░ │  │
                             •   │ • │  ┌──┐   ─┐─ ░│  ┌─┘  ─┘             │   │ │       ─┘
                              ──        │  │    │  •   │  ─┐  ┌──┐   ┌─  ──    │ │░ •  ┌─
                                 │  │ ░ │░ │ │░ │ │ ░  │░│ │░ │░ │   │░   ░ ┌┐ │ │  ▒ ░│
                                 └──┘───┘──┘─┘──┘─┘─   └─┘─┘──┘──┼─┐─┘──────┘┘─┘ └─────┘
                                                    ───          │ │            •
                                         •░░│ ░ ░│ │░░░░│ │░░│░│░│ ░│ ░░│  │░ ░ ░░░░░│
                                          ──┘────┘─┘────┘─┘──┘─┘─┘──┘───┘──┘─────────┘
                  ┌─┐ ┌────┐───┐─┐──┐─────
                  │░│ │░ ░ │░░░│ │░ │░░░░░
                  └─┘ └────┘───┘ │                    ────────        ──────
                                • ┌───┐────┐─┐────────        ────────      ┌─┐        ───
                            │     │░░░│░░▒░│░│                              │░└───  ──┐   │
                            │ │ ──┘  ┌┘┐─┐─┘─┘─  ────  ───── ─────────  ░░•░ ░│ ░░░ ░ │ │ │
                            │ │   │░░│ │░│     ─┐░░░░ ░░ ░░░•          ───░───┘───┐▒──┘ │ │
                            │ │   │    └─ ─┐    │  ─────────   ─┐─────    •       └─    │ │
                            │ │     •   ░  │    └─┐          │  │ ░░ ░│     ─┐          │ │
                            │ │    │  ──┐ ┌┘┐   │░│   ┌────┐ │░┌┘─┐  ░│    │░│  ┌──┐┐   │ │
                            │ │    │ │  │ │░│    │░│  │░░░░│ │░│  │░•░│    │░│  │░ └┘   │ │
                            │ │    │ │  │ │░│    │ │  │  ░░│ │ │  │░ ░│    │ │  │░ ░░│  │ │
                            │ │    │ │  │ │░│    │░│  │░│░░│ │░│  │░ ░│    │░│  │░ ░░│  │ │
                            │ │    │ │  │ │░│    │░│  │ │░░│ │░│  │░ ░│    │░│  │░ ░░│  │ │
                            │ │    │ │ │  │░│    │░│  │░░░░│ │░│  │░ ░│    │░│  │░ ░░│  │ │
                            │ │    │ │ │  │░│    │░│  │░ ░░│ │░│  │░░░│    │░│  │░ ░░│  │ │
                            │ │   •    │  ░░│    │░│  │  ░░│ │░│  │░ ░│    │░│  │  │░│  │ │
                            │ │    ──   ────┘    └─   └────┘ └─┘  └───┘    │░│   • └─┘  │ │
                            │ │                                             ─┘          │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                   ─┐       • ────────────               │ │
                            │ │ ┌──────────┐────   └──┐──┐─ │            ────           │ │
                            │ │ │░░░░░  ░░░│   ░───┘  │ ░│  └───┐────┐──┐  ░░│   ┌────┐   │
                            │    ┌─────────┘   ░░░░░┌─┼─┐┘ │░░░░│ ░░░│░░│  ──┘   │░░░░│   │
                             ─┐ ─┘                ──┘ │ │  └┐─  │ •    ─┘ │      │   ─┘  •
                              └┐       │ ┌─┐ │  •      •    │ ──     │░   │ ░│     •   │
                               └┐     ░│ │ │ │░ ░  │ ░  ░ ░ │  ░ ░ │ │░ • │  │ ░    │ ░│
                                └──        │    ───┘   ──   │ ──   └─┘──  │    •  ──┘
                                   │  ┌─   │ ┌─    └┐──  ──┐┘   ───     ──┼───  ─┐   ──┐──┐
                                   │  │ ░ ░│ │░░░░│ │░░░░░░│ │░░░░░│ │░░░ │░░░│ ░│ │░░░│ ░│
                                    ──┘────┘─┘────┘─┘──────┘─┘─────┘─┘────┘───┘──┘─┘───┘──┘














```

*Figure from page 29 (2346x3317 px)*


---



(6) System Parameter



AUTO OPERATION



CHECK DATA



VPPL*



VNPL*



VPSL*



VNSL*



VINpl"



VBLCl'



Vl«lF*



VHPI*



4203-E P-143



SECTION 6 DISPLAY ON NC OPERATION PANEL



SYSTEM VARIABLE



lllTl



X y



5000.000 5000.000 5000.000



-5000.000 -5000.000 -5000.000



5000.000 5000.000 5000.000



-5000.000 -5000.000 -5000.000

0. 100 0.100 0. 100



0.000 0.000 0.000



36000.000 36000.000 28800.000



0.020 0.020 0.020



PROGRAM ACTIJAL PART BLOCK CHECK



SELECT POSIT. PROOOAM DATA SEARCH ATC/APC DATA [EXTEND]



Fig. 6-26 System Variables Screen System Parameter



(7) Home Position



AUTO OPERATION



CHECK DATA SYSTEM VARIABLE



VHppl" [ 1l



[ 2]



[ 3)



[ 4]



[ 5]



[ 6]



[ 7]



[ 8]



200.000



200.000



300.000



40.000



0.000



0.000



0.000



0.000



200.000



200.000



300.000



0.000



0.000



0.000



0.000



0.000



PAGE 27 lmn



200.000



200.000



300.000



0.000



0.000



0.000



0.000



0.000



PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PROGRAM DATA SEARCH ATC/APC DATA [EXTEM>]



Fig. 6-27 System Variables Screen - Home Position


```text


                                                                                                ──        ──
                                                             ┌──┐─┐────┐─┐────┐─┐─┐─┐──┐─┐──────░░────────░░
                                                             │░░│ │░░░ │ │░░░ │░│ │░│ ░│ │░ ░░░░──░░░░░░░░░•
          ┌───────   •                 ──────────────────────┘──┘─┘────┘ └────┘─┘ └─┘──┘─┘────         ──
          │       ──  ┌───────────────┐                                                                    │
          └──────┐░░  │░              └────────────────────────────────────────────────────────────────────┘
                 └──  └────────┐──
                               │       ─────                                          ───
                            │     ────┐░░                                           ──   │
                            │ │ │ ░░░ │░░   ─── ┌───────────┐─     ──┐   ── ░░    ──░░•  │
                            │ │ └──░┌─┘─────   ─┘░░░░ ░░ ░░ │ ─────  └──░▒▒ ░•   │░░┌─   │
                            │ │    ─┘           │      ────             ─────  ──┘──┘  │ │
                            │ │                   •░         • •                       │ │
                            │ │      ┌──┐─      ┌─░│ ──┐   ┌─░│ ┌─┐    ┌─░─┐─┐         │ │
                            │ │      │░░│       │░░│ ░░│   │░░│ │░│    │░│ │░│         │ │
                            │ │      │░▒│       └─░│ ░░│    │░│ │░│    │░│ │░│         │ │
                            │ │      │ ▒│         •░ ░░│    └─░ │░│    └─┘ │░│         │ │
                            │ │      │░░│      ┌─  ░ ░░│   │    ░░│   │   ░│░│         │ │
                            │ │      │▒░       │░░│░ ░░│   │░│░ ░░│   │░░░ │░│         │ │
                            │ │      └───      └──┘────    └─┘────┘   └────┘─┘         │ │
                            │ │                                                        │ │
                            └─┘                                                        │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │ │                                                        │ │
                            │   ┌───  •        •    •     •      •      ──    ──       │ │
                            │   │░░░── ───── ──░──── ░───  ────┐─ ──────  ┌──┐  ─┐───┐   │
                            │   │░░░░░  ░░   ░░░░   ─┐░░░   ░ ░│        • │░░│   │ ░░└┐  │
                            │   └─      •          • │   ──┐              │   │ •     │ ┌┘
                             ──┐     │ │  •       •  │ • ░ │░ ─┐    ┌─┐ ┌─    └─  ┌─░ └─┘
                               │  ░│ │ │ │░    ░ ░    ░ │ │░ ░░│    │░│ │░ ░│     │░ ░│
                               └───┘─┘─┘─┘──  ───── ────┘ └────┘ • ─┘─┘─┘───┘─────┘── │
                                            •      •     │      • •                   └┐
                                    • │░  ░│░│ │░░░░│ │░ │░░░│ │░░░░│  │░ ░  ░  ░░  ░░ │
                                     ─┘────┘─┘─┘────┘─┘──┘───┘─┘────┘  └───────────────┘
                 ┌─┐  ┌─┐─┐─┐─────┐
                 │ │  │░│░│ │ ░░░░│
                 └─┘  └─┘─┘─┘────             ──────────       ────────────
                                 ┌────┐──┐──┐─          ───────            ┌─┐         ──
                           │     │░░░ │░░│ ░│                          •   │░└──── ──┐   │
                           │ ┌───┘    └─┐┘──┘─  ───────────            ░░─┐ ░│ ░ ░░░░│ │ │
                           │ │   │░░│ │░│     ─┐░░ ░  ░  ░            ───░└──┘───────┘ │ │
                           │ │   └──┘    •     └─      ────                            │ │
                           │ │       │░ ░ ┌─┐    ┌─┐──┐     ┌─┐───     ┌───┐─┐         │ │
                           │ │       └──┐ │░│    │░│░░│     │░│ ░░│    │░░ │░│         │ │
                           │ │          │ │░│    │░  ░│     └┐┘ ░░│    └┐─ │░│         │ │
                           │ │          │ │░│    └┐░ ░│      │░ ░░│     │  │░│         │ │
                           │ │          │ │░│     │░ ░│      │░ ░░│     │  │▒│         │ │
                           │ │          │ │░│     │░│░│      │░ ░░│     │  │░│         │ │
                           │ │          │ └─┘     └─┘─┘       • ──       ──┘─┘         │ │
                           │ │                                 •                       │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                            • ────   ─────        ─────┐ │ │
                           │ │  ┌───┐────────  •     ┌── • │            ──┐─┐───     │ │ │
                           │ │  │░░░│  ░  ░   │░───┐ │ ░│  └───┐─┐────┐   │░│   ┌────┘ │ │
                           │    └───┘ ────┐   │░░░░│ └─░│   ░░░│ │░░ ░│   └─┘   │░ ░░│   │
                            ─┐  │         │      ──┘ │      •  │ └─      │  │   │   ─┘  •
                             └─┐┘       ──┘ │         ┌── •  │░     │░ │ │ │░   │ ░░  │
                               └┘    ┌─   │ │░      • │    ░ │░ • ░ │░ │ │ └─── │ │░ ░│
                                └─   │ │ ─┘    ──     └──     ──     ──┘ └─     │ └──┐┘
                                  ───  │    ──   ────    ──┐──  ┌───        ────┘─   │
                                       │ │ ░ ░│ │░░░░░  │░ │░░│ │░ ░░│  │░ ░░░ ░░░░░░│
                                       └─┘────┘─┘───────┘──┘──┘─┘────┘──┘────────────┘














```

*Figure from page 30 (2346x3317 px)*


---



4203-E P-144



SECTION 6 DISPLAY ON NC OPERATION PANEL



(8) NC Communication Buffer



(9) Other Data



AUTO OPERATION



CHECK DATA



VNCOM[l]



[2]



[3]



[4]



SYSTEM VARIABLE



00000000



00000000



00000000



00000000



PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PROGRAM DATA SEARCH ATC/APC DATA [EXTEN)J



Fig. 6-28 System Variables Screen - NC Communication Buffer



AUTO OPERATION



CHECK DATA



VPCNT



VOK1



VOK2



VNLM



VINTG



VPITT



VFC1



VFC2



Vt.PT



VTLCN



VINS



SYSTEM VAAIABLE



VINF



00000000=-00



00000000=00



00000000=00



00000000=00



00000000=00



00000000=00



01000010=42



00000000=-00



VFST



VINCH



VSPCO



VSPSB



VMLOK



VACOD



VF[J,IJ(



VFSOV



VTLNN



VSTM



00000000=00



01000010--42



10 001010--SA



00010000= I0



00000000=00



100000



100



00000000---00



PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PROGRAM DATA SEARCH ATC/APC DATA (EXTEND]



Fig. 6-29 System Variables Screen - Other Data


```text


                                                                                                ───
                                                              ┌─────┐─┐─┐─┐───┐──┐─┐────┐─┐─────░░░────────┐
                                                              │░ ░░░│░│ │ │░░░│ ░│ │░░░░│ │░░░░░░──░░ ░░░░░│
           ┌──────   ──                       ────────────────┘─────┘─┘─┘ └───┘──┘─┘────┘─┘────        ──
           │      ┌─┐   ────────────────┐──┐─┐
           └──────┘░└──░░            ░  │░ │░│
                  └─┘  ─────────┐─────  └──┘─┘
                                │            │                                         ───
                             │    ──░──┐───  │                                │           │
                            ┌┘ ┌─┐ ░   │░░░ ░│   ┌──────────        ─── ░─── ░│   ───┐  │ │
                            │ ┌┘ └─┐░│ └─────  ──┘░░░  ░ ░░  ───────   ──░░░ ─┘ ░ ░░░└─ │ │
                            │ │    └─┘                ───────            ────  ──────┘  │ │
                            │ │        ─────     •                                      │ │
                            │ │       │░░░░░│   •░────┐                                 │ │
                            │ │       └───┐░│  •░░░░░░│                                 │ │
                            │ │           │░│   •░░░░•                                  │ │
                            │ │           └─┘    ────                                   │ │
                            │ │                                                         │ │
                            │ │                                                         │░│
                            │ │                                                         └─┘
                            │ │                                                         │ │
                            │ │                                                         └─┘
                            │ │                                                         │░│
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │  ┌───               ── •  ──      •      ── •   •       │ │
                            │ │  │░░░│ ──────────┐──  │ ─┐  ─┐──┐─ ──────  │░──  ┌────┐ │ │
                            │  • │░ ░│ ░ ░░   ░░░│  ┌─┘░░│   │ ░│        • │░░   │  ░░│   │
                             •   └─  │ • ──┐  ──┐   │ │  └┐     │       •  │   │ │    │  •
                              ──           │    │  • • │  └─  ┌─ • │ │ ░░ │  │ └─┼───  ┌─
                                 │  │   │░░│ │░ ░ │ │  │░ │ ░ │░ ░ │ │░ │ │ ░│ ░ │░░░ ░│
                                 └──┘───┘──┘ └─ ──┘─┘──┘──┼─ ─┘──┐─┘─┘──┘ └──┘───┘─────
                                               •          │ │    │       •              ────
                                  │░ ░ ░ ░│ │░░░░│ │░░░░░░│ │░ ░│   │░│ │░░  ░    ░░   ░ ░░
                                  └───────┘─┘────┘─┘──────┘─┘───┘───┘─┘─┘───────────────────
                  ┌─┐─┐─────┐───┐
                  │░│ │░░ ░ │░░░│
                  └─┘─┘─────┘───┘                          ───────────
                                 ─┐────┐──┐──┐─────────────           •                 ──
                             •    │░░  │░░│ ░│                          •   ──┐───  •     │
                            │ ┌───┘  │ │  └──┘   ─────────── ┌────────  ░░─┐ ░│ ░ ░░░░│ │ │
                            │ │   │░░└─┘─┐┘    ─┐░░ ░  ░░░░░ │        ────░└──┘───────┘ │ │
                            │ │    ──┘   │      │  ──────────             •             │ │
                            │ │       ┌─┐                       ┌─         ───────      │ │
                            │ │       │░│       ┌────────┐      │░─┐      │░░░░░░░•     │ │
                            │ │       │░░│      │░░░░░░░░│      │░░│      │░░░░░░░▒│    │ │
                            │ │       │░░│               │     │░░░│      │░░ ░░░ ░│    │ │
                            │ │       │░░│        ──── •░│     │░░░│      └┐░░────┐┘    │ │
                            │ │       └─░│      ┌─░░░░│░░│     │░░░│       └──    │     │ │
                            │ │       │▒│░      │░░░░░│░░│     │░░▒│            ░░│     │ │
                            │ │       └─┘       └─────┘──┘     │░░▒│      ┌────   │     │ │
                            │ │       │░ │      │        │     └───┘      │░░░░░░░│     │ │
                            │ │       │░░│       ░░░░░░ ░│                └───────┘     │ │
                            │ │       └──┘      ─────────┘                              └─┘
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                            ─┐───────────        ──────┐ │ │
                            │ │ ─┐───┐─────┐   ┌─     ┌── • │           ─────┐─       │ │ │
                            │ │  │░░░│  ░░░│   │░───  │ ░│  └┐──┐─┐────┐   ░░│   ┌────┘ │ │
                            │  • └───┘ ───░│   │░░░░│ └──┘   │░░│ │░░ ░│   ──┘   │░░░░│   │
                             ─┐ •                 ──┘ │      │ ┌┘ │    │  │      │   ─┘  •
                              └┐  ░   │  ░░  │  ──     ░    │  │      ░   │  │     •   │
                               └┐  •  │░  ── │░ ░  • • │░ ░ │  ░ ░ • │░ ░    │ ── • │ ░│
                                └──  •  ──       ──    └─── │ ──     └─  ────      ─┼──┘
                                    •      ─────   ────    • •  ────┐  ─┐    ────┐  │
                                         │ ░ ░ ░│ │░░░░░│ │░░░░░ ░ ░│ ░░│  │░░░░ │░░│
                                         └──────┘─┘─────┘─┘─────────┘───┘──┘─────┘──┘














```

*Figure from page 31 (2346x3317 px)*


---



4203-E P-145



SECTION 6 DISPLAY ON NC OPERATION PANEL



7-1-5. PLC Axis Data



The PLC axis data is displayed in decimal numbers on the display screen, as shown below.



RDIF



ODIF



RCON



RAPA



RCOM



RCCON



RCAPA


#### RAWAR1


#### RAWAR2

AUTO OPERATION



CHECK DATA PLC AXIS DATA



1!111


#### MA TS

ROIF 0.000 0.000



OOIF 0.000 0.000



RCON 0.000 359.999


#### RAPA 0.000 359.998

ACOM 0.000 359.999



RCCON 0.000 359.999


#### RCAPA 0.000 359.998

RSWAR1 0.000 0.000



RSWAR2 0.000 0.000


#### PROGRAM ACTUAL PART BLOCK CHECK

SELECT POSIT. PROGRAM DATA SEARCH ATC/N'C DATA [EXTEND]



Fig. 6-30 PLC Axis Data Screen



Difference between calculated value and position encoder output



Difference between calculated value and position encoder output with acceleration/



deceleration activated



Calculated value



Position encoder output



Command value



This is the RCON with the position encoder offset incorporated (applies to systems with



axis switching specifications).



This ls the RAPA with the position encoder offset incorporated (applies to systems with



axis switching specifications).



Servo data (Designate the content of display with NC optional parameter (word) No. 10.)



Servo data (Designate the content of display with NC optional parameter (word) No. 10.)



Crossratl



Magazine



Varies depending on the machine being used. Refer to the Maintenance Manual for the



machine in question.



Varies depending on the machine being used. Refer to the Maintenance Manual for the



machine in question.


```text


                                                                                               ────
                                                             ┌───┐─┐─┐───┐──────┐─┐──┐─┐─┐─────░░░░┌──────┐
                                                             │░░░│ │░│ ░ │░░░░ ░│ │░ │░│ │░░ ░░░───┘ ░░░░░│
               ──              ──────────────────────────────┘───┘─┘─┘───┘──────┘─┘──┘─┘─┘─────      ───
          ─┐  •   ────────────
           │ │░───░            ┌─────
             └─        ──      │
                         ┌─    └──────────────────────────────── ─────────────────┐─────────────┐
                ──  ──   │ │ │       ░  ░           ░      ░         ░░  ░        │░     ░  ░░ ░│
                  ──  ───┘─┘ │                                                         ─────────┘
                                 ───────────    •                          ──┐─     ─┐
                           │  ── ░░░ ░░░░░ ░• ┌─ ┌─       ┌──────────┐ ──── ░│ ────  │   │
                           │ │  ────────────  │  │        │          └┐░░░ ░░│ ░░░░░┌┘ │ │
                           │ │                 ─┐┼─┐── ───            └────── ──────┘  │ │
                           │ │                  └┘░│         ┌──                       │ │
                           │ │       ──┐         └┐ ┌─┐      │░ ─┐                     │ │
                           │ │      │░░└┐         │░│░│      │░ ░│                     │ │
                           │ │      │░░└┘         │ │░│     ┌┘┐ ░│                     │ │
                           │ │      │▒░░│         │ ░░│     │░│ ▒▒•                    │░│
                           │ │      │▒░░│         │ ░░│     │░│ ░│                     │░│
                           │ │      │░░•░│        │ •░│     └┐┘ ░│                     │░│
                           │ │      │░░░░└─       │  ░│      └┘ ░│                     │ │
                           │ │       ───░░        └───┘       └──┘                     │ │
                           │ │          •                                              │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                           ──      • ──────          •   │ │
                           │ │ ┌───── ────┐─────┐    ───┐  ────── │      ─┐─┐    ──  │ │ │
                           │ │ │░░░░░  ░ ░│   ░░└─   ░░░│ •       │  •    │░│   │  ┌─┘ │ │
                           │   └───── ──  │  ┌┐░░░┌┐ •░─┘┐     • • ──░│   │░│ │ │  │░│   │
                            ── │     •    │  └┘┐──┘┼─    │    ░░      │ ─┐  │ └─┘ •   ┌──
                               │     ░  │ │ │░ │   │░ │░ │ │ │░ │ │ ░░ ░ │  │ ░ │  ░ ░│
                               └───  ───┘─┘ └──┘───┘──┘──┘─┘─┘──┼─┼──────┘──┘───┘─────┘
                                   ──      •                    │ │
                                                ░ •    │ ░      │  ──   ─────
                                                ┌─    ─┘ │   ───┘──  • •
                ┌───┐        ┌──┐──────┐─────┐─┐┘  ┌──  ─┼──┐         •  │  ─┐─┐──┐─┐─┐
                │░░░│       ┌┘░░│░░░░░ │░░░░░│ │░• │░░│  │░ │ ░ ░ ░░░░ ░ │░░░│░│ ░│░│░│
                └── │       │          │     │     └┐ └─ └┐ │ ─┐ • ──  ── ─┐ └─ • └─┘ └┐──┐──┐─┐─────────┐─
                │░ ─┘        │ ░───────░░░░░░└──░░  │░░░│ │░│░ │░░│ ░░░░░│ │░ ░ ░░│  │░│░ │░░│ │  ░░░ ░░░│
                             └──░░░░░░░ ─────░░ ────┘───┘─┘─┘──┘──┘──────┘─┘──────┘──┘─┘──┘──┘─┘─────────┘─
                ┌────┐                       ───
                │░  ░│       │ ░──░░░ ──┐─┐
                │    │       │    ──    │ └┐ ─────
                │    │       │ •    •  │   │
                └──░░│       │░░───░░░─┘──░│
                │     ─┐    •              └─ ─┐─ ────────┐─┐───┐─┐─┐───┐──────────────────┐───┐───┐───┐──┐
               │░░░░░░░│     ┌─░───░░───░░░│ •░│ • ░ ░░░░░│ │ ░░│░│ │░░░│  ░░░░░░░░░ ░░░░░░│ ░ │░░░│ ░ │ ░│
               │  •  ─┐┘     │░• ░░── ░░─── ░ ░│ ░──   ──  ─┘── └─┘─┘  ─┘       ───── ─── ─┘  ─┘─  │      │
               └── ── │      │       │         │         ─┐    •     ─┐  ───────     │   •  ─┐   ── ───┐──┘
               │░░░░░░│      └─░ ────┼─░░░░░─┐░└─────░░░░░│ │░ ░░░  │░│░   ░░░░░ ░│  │░░░░░░ │ │░░░│ ░ │░░│
               └── ──        │ • ░░░░│ ──── ░└─┘ ░ ░ ──── │ │       └─┘ •   ─── ──┘─  ── ─── │ └───┘   └──┘
                  •  ───┐   │      │                     • • ──────┐   │ ┌──   •    ┌─  •   │ │     ┌─
                •░░░░░░░│   │░░░ │ │░│ │░•░░░░░│  ░┌─░• ░░│   ░░░░░│ │░│ │░  ░░░░ ░ │░ ░░░░░│ │░  ░ │░│ │░│
               │ •      │   │    │ │ │ └─      │   │ │ │  │      │ │ │ │ │ •        │       │ │     │ │ │ │
               │░ ░ ░░  │    │░──┼─ ░│  ░░░░░░░│  ░│ │░│░░│   ░ ░│░│ │░░ ░░  ░░░░ ░ │░ ░░░░░│ │░░ ░ │░│ │ │
               └┐ ┌─────     │   │ ──┼─────────┘───┘─┘─┘──┘──────┘─┘─┘──────────────┘───────┘─┘─────┘─┘─┘─┘
                │ │          └──  •  │
               •░░│          │░░░░░░░│
                │ │          │        ─────   ───┐─┐──┐─┐──┐─────┐──┐─┐───┐─────┐─┐────┐──────┐────┐──┐───┐
                │░│          └─────░░░░░░░░───░ ░│ │░░│ │░ │░░ ░ │░░│ │░░░│ ░ ░░│ │░░ ░│░░ ░░ │░░░░│ ░│ ░░│
                └┐┘          │░░░░ ───── ──░░ ───┘─┘─   └──┘───── ──┘─┘───┘   ──┘ └──        ─┘─       ───┘
               │ │           │   │                   ───         │         ───   •   ┌─┐──┐──   ───┐──┐   │
               │░│           │░──┘─░░░░░░░░──░░  │ │░░░░ │ │░░ ░ │░░│ │░░░│ ░ ░░░ ░░░│░│░░│░░ ░░░░░│ ░│ │░│
               └─┘           └─░ ░░────░ ──░░ ───┘─┘─────┘─┘─────┘──┘─┘───┘──────────┘─┘──┘────────┘──┘─┘─┘
                                ───    ──  ───














```

*Figure from page 32 (2346x3317 px)*


---



4203-E P-146



SECTION 6 DISPLAY ON NC OPERATION PANEL



Additionally, the machine axis data enlarge display screen displaying ODIF, RAPA and load data in



enlarged characters is provided.



[AUTO OPERATION



CHECK DATA


# PLC AXIS DATA

97/07/1~ 14: 10:od



11m1


# ODIF RAPA


# 0.000 0.000


# 0.000 359.998


# LOAD

PROGFWJ ACTUAL PART BLOCK CHECK



SELECT POSIT. PROOlAM DATA SEARCH ATC/APC DATA [EXTEND]



7-1-6. MCS Diagnostics



AUTO OPERATION



CHECK DATA



MACHINE COORDS

* CH 1



CH 2



CH 3



MCS DIAGNOSIS



CH 4



-0.001



AXIS COM.CODE



N 1



-0.001



97/07/15 14:10:00



-0.001



DATA 10 DATA


#### MIIMMHKM*M~MNNMN


#### M*MMHfflNKMINNMM*


#### MHNNKJ!MM*~MIMNMM


#### RIKMNNKM~KMHMMiN

PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PROGRAM DATA SEARCH ATC/APC DATA [EXTEND]



Fig. 6-31 MCS Diagnostics Screen


```text


                                                                                                 ── •
                                                              ┌─────────┐─┐───┐──┐─┐────┐─┐──────░░• ──────░│
                                                              │░░░ ░░ ░ │ │░░░│ ░│ │░░ ░│ │░ ░░░░──░░ ░░░░░░│
           ┌─────           •   •       •   ──   •      ──  •  ───    ──  └───┘ •  │  •    • ──          ───
           │     ──────────┐ ┌── ──────┐ ┌──  ─── ──────  ── ──   ────  ┌─     •  ─┘─┐ ───                  │
           └────  ░░░░   ░░│ │         │ │     ░               │        │            │      │     │      │  │
                 │          •          └─   •  ───────────── ──┘ ───────┘       ─────┘──────┘   ──┘ ┌─ • │  │
                 │░   ░░│ • ░ ░ ░   ░ ░  ──░░•                           •                   ───   ─┘   ─┘──┘
                 └──────┘─ ──────              ───────   ────────────────  •   ─────   •
                                 ─────────────               ░░           • ┌─┐     ──┐  ─┐
                             • ┌─  ░░░░▒░░░ ░░    •               ─────     │░│ ───  ░│   │
                            │  │ ────────────   ─┐ ─── ┌─┐ ┌──  ─┐     •░ ░░└─┘─░ ░░░░│   │
                            │ │              ░░│░│ ░░▒ │░│ │░▒ │░└─ ──  ────    │  ┌──    │
                            │ │              │▒│ ░░ •   ─┘─┘───┘░░░•░░•     ───┐┘─░│  ┌───
                            │ │     ┌──      └─░     ──┐        ───░│  ───     │░░░│  │░░ │
                            │ │     │▓▒│       │░│ │▒░▒│           ░│ ░░░░•  ── ─┐░│    │ │
                            │ │     └┐░│       │░│ │ ░ │        ┌── ░ │░░ ░•     │░│    │ │
                            │ │      │░│        ─┘ │░░▒│        │░░░│ └┐░▒•      └─┘    │ │
                            │ │       •           • ───         └───┘  └──              │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │░│
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                     •             ─┐────        │  ───  │ │
                            │ │  ┌───┐──────┐─┐──┐   ─┐──┐───    • │    ┌── ─┐──┘ •   │ │ │
                            │    │░░░│  ░ ░░│ │░░└──┐ │░░│    ──┐  └──  │  │░│     ─┐─┘ │ │
                             │   └───┘──┐───  └┐─░░░│ └──┘   • ░│ ─┘░ ──┘  └─┘      │░│   │
                             └── │      │      │   •  │  │      │    •  │  │           ┌──
                                •  ░│ │ │ ░░ ░  ░░░    ░░   ░ │░   ░ ░░   ░ ░░ ░ ░ ░░ ░│
                                 ───┘ └─┘─────────────────────┘────────────────────────┘
                                     •
           ┌────┐  ┌─────────┐────┐
           │   ░│  │░  ░  ░░░│ ░░░│
             ───┘  └─────────┘───             ──────────────────────────        •       •
                                  ─────┐─────                                ─── ──  •   •
                            │  •  ░░░░░│▒░░ ░• •           ┌──────────┐ ─────░     ──░│   │
                            │ │  ───░┌─┘─────   │     •    │          └┐▒░░░ ─┐ ░ ░░░┌┘ │ │
                            │ │     ─┘          └────┐ ┌───            └───── └──────┘  │ │
                            │ │   │   •  ┌───┐       │ │         ─────                  │░│
                            └─┘   │░│ ░│ │░░░│      │   ─┐      │   ░       •░ ░        │░│
                            │ │   └─┘──┘ │ ──  ┌─┐  │  • └──┐───┘ ───┐──┐               │ │
                            │ │          └─   ─┘░│  │  ░░│  │░░ └┐   │░░└─┐─┐─────┐     │ │
                            │ │          │░    └─┘  └─┐─┐┘──┘┐  └┘   └─ ░░│ │░  ░░│     │ │
                            │ │          │░    │░│    │ │    │  │    │  ░   │     │     │ │
                            │ │          │░    │░│    │ │    └──┘    └───░──┘─────      │ │
                            │ │                 •                        •              │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │   •                       ──      • ───  •              │ │
                            │ │  │░──────────────┐┐   ┌──┐  ──────░•    • ───┐──  ── ─┐ │ │
                            │ │  │░░░░  ░░░░   ░░└┘   │ ░│          │      ░░│   │  │ │ │ │
                             │   │   •        ──   ┌┐ │  └┐         └──┐   ┌─┘ │ └─ │░│   │
                             └── │  │      │      ░└┘┐    └─   •░│ │   │ ─┐┘ │ └─┘ •   ┌──
                                │   │ ░  │ │ │░ ░   ░│ ┌┐   ░ │░ │ │ │░ │ │  │ ░ │  │ ░│
                                └─── ────┘─┘ └───────┘─┘┘─────┘──┘─┘─┘──┘─┘──┘─┐─┘──┘ ─┘
                                            •                                  │     •
                                                         ░░ ░        ░•       │
                                               ───────── ───────────── ───────┘
















```

*Figure from page 33 (2346x3317 px)*


---



4203-E P-147



SECTION 6 DISPLAY ON NC OPERATION PANEL


## 8. Run Guide Display

After selecting the EDIT AUX mode, press function key [F7] (RUN GUIDE), and the RUN GUIDE screen is



displayed.



(1) RUNNING FILE



The operation status of the file currently selected is displayed at the left half area on the screen.


#### PROGRAM OPERATION RUN GUIDE

RUNNING FILE



(a) M<\NUAL


#### SELECT taJE


#### MAIN FILE NAMl: MAIN FILE NAME

(b)


#### TST9.MIN RUNNING EIFIY


#### MAIN PROGRAM NAME MAIN PROGRAM NAME

(c)



OTST9 EMPTY



SUB FILE NAME



Et.f'TY



RUNNING METHOD SELECT RUNNING MErnOO



(d) A-Mtd



(e) -----+--------~



TIME



INIT



DELETE



RENAi.iE


# I I

~~~DE



[EXTEND]



Fig. 6-32 Running File Display



(a) File selection method



This field indicates how the file has been selected and is being operated.



Display Contents



EXTERNAL SELECT MODE Operation by external program selection command



SCHEDULE MODE Scheduled program operation



MANUAL SELECT MODE Operation by manual program selection



(b) MAIN FILE NAME



This field indicates the main file name currently selected.



(c) MAIN PROGRAM NAME



This field indicates the main file program name currently selected.


```text


                                                                                                ──
                                                             ┌──┐─┐────┐─┐───┐──┐─┐─┐──┐─┐──────░░──░─────░
                                                             │░░│ │░ ░ │ │░░░│░░│ │░│ ░│ │░ ▒░░░──░░• ░░░░░•
             ─────                          ─────────────────┘──┘─┘────┘ └───┘──┘ └─┘──┘─┘────           ──
           ─┐      ┌─────── ───  ─┐──                                                                      │
          •░│      │░  ░ ░░    ░│ │░  •  ──┐ ──────────────────────────────────────────────────────────────┘
           ─┘      └─░─────░────┘─┘───▒░•░░│
                 ┌─                         ──┐─┐─────────┐─────────────┐──────┐──────┐─────────────────────
                 │░░────┐░░░░ ░│ │░░│ │░░ ░ ░░│ │ ░░░░░░░░│  ░░  ░░ ░░░░│ ░ ░░░│  ░ ░ │░ ░░░░ ░ ░░░ ░       │
                 └─     └──────┘─┘──┘─┘───────┘─┘─────────┘─────────────┘──────┘──────┘─────────────────────┘
                    │
                 │  └─     ─────  ┌─┐
                 └──  │           │ └─   ┌─── ──    • •
                      │           │   ─┐─┘   •  ──── • ───┐────────────────┐────────  ───────────────────┐
                      └──────────      │                ░ │             ░  │                ░          ░░│
                                                                        ───┘─          ──────────────────┘
                          │       ─── ───┐───┐      ─┐  ──┐                    ─────
                          │ ┌── •░░░░  ░░│  ░│     •░│ ░░ │  ───┐ ┌───░───          │  │
                          │ │     ───────┘──░│ ──── │ ────┘─┐░ ░│ │░░▒░░░░┌─ ───────┘  │
               ┌─┐────────┼─┼─               └┐     │       └──   └───────┘ •        │ │
               │░│        │░│  ┌───────────▒░░│     │      •   ┌─┐                   │ │
               │ │        │ │  │▒░░  ░  ░░░ ── ─────   ┌─┐─  ──┘░└─                  │ │
               │ └────────┼─┼─ │░░░ ▒░░  •  ░    ░ ░   │▒│       │ ─┐                │ │
               │ │        │░│  └─░─────── ───   ─┐─┐─  │▒│░     │  ░│                │ │
               └─┘─       └─┼──  •               │ │   │░│ ──┐─░└┐                   │ │
                          │ │     ────┐─┐─┐      │  │  │▒ │  │   └──┐──┐             │ │
               ┌─┐────────┼─┼─  │░░ ░ │░│░│      │  │  └──┘  │░│░│ ▒│░░│             │ │
               │░│        │ │   └─────┘─┘─┘      │  │ │   └──┘─┘─┘──┘──┘             │ │
               └─┘────────┼─┼──                  │  │ │                              │ │
                          │ │                    │ │ ─┘                              │ │
               ┌─┐────────┼─┼──   ───────────────┘ │                                 │ │
               │░│        │░│                      │                                 │ │
               └─┘────────┼─┼─ ──  ────────────────                                  │ │
                          │ │ •░░│                                                   │ │
                          │ │  ──┘  •     •      •       ─────┐─┐──── •      •       │ │
                          │ │    └┐─ ─┐─┐─ ┌────┐ ┌─────┐     │ │    │ ─┐─┐   ──────   │
                          │ │  │░░│   │░│  │ ░░░│ │░░░░░│      ─┘    │  │░└┐      ░ │  │
                          │    │ │         └┐─  │  ┌──── ┌─      •   │  │  └─       │ ┌┘
                           ──┐  ─┘   • ┌──  │ ─┐ • │     │ ┌─┐ ── ┌─┐░     │ │  ┌───┼─┘
                             │  ░│  │  │░ │ │ ░│ ░ │░ │ ░│ │░│  ░ │░│ ░░ │ │ │  │░  │
                             └───┘  └──┘──┘─┘──┘── └──┘─ │ └─┘────┘─┘─── └─ ─┘──┘───┘
                                  ──              •                     •  •
                                                │░░│ ░ ░│ │░  ░   │░│ ░░░░░░│
                                                └──┘────┘─┘───────┘─┘───────┘
                   ┌─┐─┐─┐─┐─────┐───┐─┐──┐
                   │░│ │░│ │░░░░░│  ░│░│ ░│
                   └─┘┐   •    ─┐ ─── ┌┘  └──────┐─┐──────┐─┐────────────────┐─┐─┐─┐──┐
                      │░  ░ ░░│ │░░ ░░│ ░ ░ ░░░ ░│ │░░░░░░│ │░░░░░░ ░░░   ░░░│ │░│ │░░│
                      │ ┌─  ──┘ └─         ──────┘─┘─   ──  └─────────   ───┐         └────────   ────────
                      └─┘          ┌─────┐─          ┌──                    └────┐───┐                    │░│
                      │░│     ───  │  ░░░│ ┌───── ───┘░            ┌───  • ┌┘░  ░│ ░░└───┐  ──────  ┌─────┘░│
                      │░░─────░░░│ │░░░░░│ │░░░░░•    ┌─────────── │░░░┌─░─┘░│░ ─┼──░░░░░│  ░░░░ ░ ░│     │░│
                      │░░░░░░░░  │ └──░┌─┘ └───── •  ┌┘░░░         │   │     │░  │  ─────┼────────── ─────┘░│
                      │░       ░░░•░░░░│ └─        ──┘░ ░ ░░░░░░ ░ │░░░  •░░░░░░│ •      │          •     │░│
                       •░░░░  ░┌─┐░───░│ │░░░░│       │░░░░ ░░░  ░ │ ░  ░ • ░░ ░│ ░░░░░░░│                │░│
                   ┌─┐─        │ │     └─┘────┘       └──────── ───┘────── ─────┘────────┘                │ │
                   │░│ ┌───────┘─ ─┐─░                                                     ───────────────
                   └─┘ │           │   ─┐───┐─┐─┐──────┐─┐─────┐─┐──────┐
                       │░░  ░░░ ░░░└──┐ │░  │░│ │░  ░ ░│ │  ░ ░│ │░░░░░ │
                   ─── │              │ │ ── ─┘─┘──────┘─┘─────┘─┘──────┘
                       │░░░░  ░  ─────┼─┘░░░•
                   ─── │              │   ── ─┐──┐───────────────────────────────
                       │░░ ░░░░ ░░░░░░│ ░│   ░│ ░│    ░  ░     ░          ░░ ░
                       └──────────────┘──┘────┘──┘───────────────────────────────


















```

*Figure from page 34 (2346x3317 px)*


---



4203-E P-148


#### SECTION 6 DISPLAY ON NC OPERATION PANEL

(d) RUNNING METHOD



This field indicates the operation method of the program currently selected.



Display Contents


#### A-Mtd Normal operation


#### B-Mtd Large volume operation


#### S-Mtd Operation without branching and subprogram

(e) Operation status



This field indicates the current operation status of the program selected.



Display Contents



SELECTED Program selection complete, but it is not run.


#### RUNNING Program is being executed.

END Program execution has been completed; this dis-



play is given until the next program is selected or



the next cycle is started.



(2) SELECT ERROR FILE



If an error occurred during automatic program selection, file is displayed at the right half of the



screen.


#### PROGRAM OPERATION RUN GU I OE

2203 ALARM B Schedule program: main program load 1 02



RUNNING FILE SELECT ERROR FILE



SCHEDULE MODE



SCHEDULE PROGRAM FILE


#### TST9. MIN END

MAIN PROGRAM NAME



OTST9



RUNNING METHOD



A-Mtd



=EX



=GD



MAIN FILE NAME



GEAR. MIN ----------t-- (f)



MAIN PROGRAM NAME



~goFILE NAME (g)



EMPTY (h)



SELECT RUNNING METHOD



A-Mtd (i)



TIME l



NIT



DELETE



RENAME



: DE



[EXTEND l



Fig. 6-33 Select Error File Display



(f) MAIN Fl LE NAME



This field indicates the main file name selected if a program selection error has occurred.



(g) MAIN PROGRAM NAME



This field indicates the main file program name selected if a program selection error has occurred.


```text


                                                                                                 •
                                                              ┌─┐───┐─┐───┐───┐──┐─┐──┐─┐─┐──────░░────────┐
                                                              │░│░░ │░│   │░░░│ ░│ │░░│░│ │░░░░░░──░░ ░░░░░│
           ┌─────────  •                   ───────────────────┘─┘───┘─┘── └───┘──┘─┘──┘─┘ └─────        •  │
           │         ── ──────────────────                                                                  │
           └────────┐   ░░ ░░ ░ ░ ░░ ░ ░   │                             •                ──────────────────┘
                    └── │                 ─┘──────────────────────── ───┐ ───────┐────────
                        │ ░  ░░░ ░ ░ ░░  ░   ░ ░ ░    ░░░    ░  ░   •   │       ░│
                       │  ──┐       ────  │                          ░  │ │             ──
                       │░   └──────┐    │ │               • ───────┐────  └──────────┐ │
                       │░┌─ │░░░░░░│    │ │                •░░░░░░░│                 │ │
                       │░│ │░░─────┘     │░──────┐───────┐   ──────┘              ───┘░│
                       │░  │░│      ─────┘       │░  ░   └──┐               ──────   │░│
                       │░░─┘─┘           │ ░░░───░  ┌─┐░░░░░└──┐                     │░│
                        │░░░░░ ───────── ░░░░░ ░░│  │░│  ░░ ░  └────────────────── ──┘░│
                        └─────┐          ──░░░░░░└──┘─┘░░ ░░░░░░░░░░░░░░░░░░░░░░░░   │░│
                    ┌─  │     │    ──┐ •   ──────      ──────────────────────────  ──
                    │░│ │░░░ ░░│ ┌─░░└─
                    └─┘ └──────┘ │ ──  ────────────────────────────────────────────────┐
                       │         │   ░    ░     ░   ░░ ░░   ░░░ ░ ░     ░ ░░░   ░░░░░░░│
                       │  ───┐───┘  ┌──┐  ─────────────────    •    ─────────────────┐ │
                       │     │░░░░─┐┘  │                   │░ │░░░░•                 │░│
                       │░──── ░░░ ░│ ── ┌───────┐──────────┘──┘     ────────────┐   ─┘░│
                       │░░░░░░░ ░░┌┘    │░░░░░░░│ ░░░░░░░░ ░░░░░░░│ ░░ ░ ░ ░░ ░░│    │░│
                       └─░──░░░░░┌┘     │ ░─┐───┘ ───────┐ ░──────┼───               │░│
                       │░   ┌────┘      │   │   │       ░│        │   ───────  •  ── │░│
                       │░  ░│      ─────┘  ─┘░░░└─────┐─┐┘──░░ ░░░└──░░░░░░░░ ░ • ░░ │░│
                      │ ────            │  ░░ ░ ░░░░  │░│ ░░  ░░── ░░───────────░──── ░│
                      │                │  •░ ░░░░ ░░ ░ ░ ░░░░░──                     │░│
                  ┌─┐─┘┐───────────────┼─  ┌──────────────────                       └─┘
                  │░│  │░░░░░░ ░░░░░░░ │░• │
                  └─┘           •          └───────────────────┐─┐──────┐─┐─────┐──────┐────┐────┐─┐─┐─┐────┐
                      ┌─────░ ░│ ░  ░ ░│ │░░ ░ ░ ░░░░░░  ░ ░░░░│ │░░░░░ │ │░ ░  │░░░░░░│ ░ ░│  ░░│ │░│ │░ ░░│
                      │     ───┘───────┘─┘─────────────────────┘─┘──────┘─┘─────┘──────┘────┘────┘─┘─┘─┘────┘
                       ─────
                                        •                                         ──────
                          │    ┌────────░─────┐─────────────             ──────┐        │
                          │ │  │░░░▒░▒▒░░░░░░░│   ░░░░▒ ░░░░ ─── ░ ┌──┐  ░░░░ ░│    ──┐ │
                          │ │ ─┘──────────────┘────────┐─────░ ░   │░░│  ─┐────┘────  │ │
                          │ │                          │     ──── ─┘──┘── │           │ │
                          │ │   ┌───── •░───   ───      •        •                    │ │
                          │ │   │░░░░░  •░░░│     ─┐   │▒┌───────░───           ──────┼─┘   ┌─┐
                          │ │  •░░░ ▒•░░░──░│  ─── │   │▒│░░▒░░░░ ░░░ ──────────      │ └── │ │
                          │ │   ──░── ───   │          │░└────░ ░ ───           ────  │ │   │ │
                          │ │                          │░░   ░──░•                    │ │     │
                          │ │   ┌───────────           │▒░•  │    ─┐─┐──┐             │░│    ░│
                          │ │   │░░░░  ░ ░             └┐░░│ │░│ ░ │░│░░│             │ │   │ │
                          │ │   └──────────         │   └──┘─┘─┘───┘─┘──┘             │ │   │ │
                          │ │                       └─┐                  ─────────────┼─┼─── ─┘
                          │ │                         │                               │ │
                          │ │                                                         │ │
                          │ │                                                         │ │
                          │ │  ┌─┐                                                    │ │
                          │ │  │░│    ────   ────                                     │ │
                          │ │  └─┘  ─┐    ──┐      │    ┌─┐────┐─┐───┐── •   ─┐       │ │
                          │ │     │  │ ┌─┐  └───┐──┘───┐┘ │    │ │   │  │░─┐─░└┐────┐ │ │
                          │  ─┐──░│   ─┘░│   ░░░│   ░░░│  │    │ │   │  │░ │   │░░░░│   │
                           •  │  •     │    ──  │   ───┘  └─  •   •  │  └─ ░│  └────┘  •
                            ── •    ┌─ └─┐ •  ┌─┘ •     │   ┌─   │ ┌─ │ │  ┌┘─ │     ┌─
                              │ ░ • │░ │ │  ░ │ │ ░│ │░ │   │░ • │ │░ │ │  │ ░ │  │ ░│
                              └───  └──┘─┘────┘─┘ ┌┘─┘──    └──  └─┘──┼─┼─    ─┘──┘──┘
                                  ──             ─┘      ┌──   ──     │ │ ────
                                               │░░│ ░ ░│ │░░░░│░ ░│ │░│ │░░░░░│
                                               └──┘────┘─┘────┘───┘─┘─┘─┘─────┘
                    ┌──┐───┐───┐──┐─┐──┐
                    │░ │░░░│ ░ │░ │░│░░│
                    └──┼──┐┘       ─┘──┘──┐─┐──┐──┐─┐────┐────────┐────────┐─┐─┐───┐────┐─┐─┐─┐──────┐
                       │░ │ •░░ ░░░░░░░░ ░│ │░░│ ░│ │░░░ │░░░░░░░ │░░░ ░░░░│ │░│░░░│ ░░░│ │░│ │░   ░░│
                    ┌──┼─┐┘┐        ──┐ ┌─┘─┘┐─┘──┘─┘────┘────────┘────────┘─┘─┘───┘────┘─┘─┘─┘──────┘
                    │░ │░│░│ ░░░░░░░░░│ │░░░░│
                    └──┘ │            │  ┌───┘┐─┐──┐─────┐─┐──────────┐──┐───┐───┐─┐─────┐────┐─┐─┐────────┐
                       │░░░ │░░░ ░░░░░│ ░│ ░ ░│ │░ │░░░░░│ │░░░ ░░░░ ░│ ░│ ░ │░░░│ │░░░░░│ ░ ░│ │░│ ░   ░░░│
                       └────┘─────────┘──┘────┘─┘──┘─────┘─┘──────────┘──┘───┘───┘─┘─────┘────┘─┘─┘────────┘









```

*Figure from page 35 (2346x3317 px)*


---



(h) SUB FILE NAME



4203-E P-149



SECTION 6 DISPLAY ON NC OPERATION PANEL



This field indicates the sub file name selected if a program selection error has occurred.



0) SELECTED RUNNING METHOD



This field indicates the operation method selected when a program selection error has occurred.



The operation method is explained in detail in d) in (1), "RUNNING FILE".


```text


                                                                                                ──
                                                             ┌─────────┐─┐───┐──┐─┐────┐─┐──────░░────────░│
                                                             │░░░ ░░░░ │ │░░░│ ░│ │░░░░│ │░░░░░░──░░░░░░░░─┘
          ┌─────────  •                ──────────────────────┘─────────┘ └───┘──┘─┘────┘─┘────
          │         ── ┌───────────────                                                                    │
          └────────┐  ─┘░ ░ ░  ░ ░ ░░░                            ──      ──      ─────────────────────────┘
                   └── │     •   │    ┌──────────┐────────────────  •  ───  ──────
                       │░░░ •░──░│░•░─┘   ░     ░│              ░     •             •     ──────────
                       │     •   └─                  ───────────────── ───────────── ────
                    │  └───── •░•  ░ ░   ░    ░│  ───                 •                   ─────────
                    │  │     • •               │     ─────── ──    ───
                       │  ░ │ │   ░  ░  ░              ░    •  ────   ── ──────── ───────────── ───────────
                       │    │ │                   ───     ──             ░   ░     ░ ░         •
                       └─░  │░░ ░   • │░ ░    ░░ ░░░░   │░░░░ ░ ░│    ──── ░░░░░░░ ──░───    ── ───────────
                         ───┘─────── ─┘─────────────────┘────────┘────    ─────────  •



































































```

*Figure from page 36 (2346x3317 px)*
