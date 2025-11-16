# III SECTION 2 PROGRAM OPERATION 08. DATA ARRANGEMENT IN MEMORY OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-08.-DATA-ARRANGEMENT-IN-MEMORY-OCR.PDF*

---


## Data Arrangement in Memory

4203-E P-266



SECTION 2 PROGRAM OPERATION



When the program stored in the memory is edited repeatedly, the unusable area in the memory will



increase. This decreases the available capacity of the memory and restricts the number of programs to be



stored.



This function is used to arrange data in the memory so that it can be used effectively.



The operating procedure is as indicated below.



(1) Press function key [F7] (CONDENS).



"=CO" is displayed on the console line.



MULTI



DATE DIR PIP EDIT PIP



"=CO" is displayed.



(2) Press the WRITE key.



Arrangement of data in the memory will start.



LIST CONOENS [EXTEND]



Press [F7)



(CONDE NS).



After the completion of arrangement, the prompt "=" will appear on the command line.


```text


                                                                                                ──        •
                                                                         ┌──┐─┐────┐─┐──────────░░░──────┐░│
                                                                         │░░│ │░░░░│ │░░░░░░░░░░───░░░░░ └─┘
                                                   ────────────────────── ──┘─┘────┘ └─────────       •
           │                                                                                               │
           │       ┌────┐ ┌─┐  ──────────────── ┌───────┐─┐────────────────────────────────────────────────┘
           │░      │░░░░│ │░└─░░░░▒▒░░░▒░░░ ░░░ │▒▒▒░░░░│▒│
                 ┌─             ───   ─┐───      ──── ──┘─ ┌─  ─┐───────┐ ┌┐┐     ──┐┐ ┌─  ───┐┐┐─┐─────  ┌─
                 │░────░│  ──┐──░░ ░──░│ ░  ──── ░   • ░   │░── │   ░  ░│ └┘┘─────░ └┘ │ ──   └┘┘ │     │ │░│
                 └─     └─┐  │                             │    │                  ░│           └─┘     │   │
                 │ •   ─┘ └──┘──       ──        • ──░   •  ──  │░•   ░ ░   •   ────░  ░░      ░  ░ ░ ░ ░ ░│
                 │░░░░•                               •          •    •                     ───────────────┘
                 └───   ───┐────────────────────────── ──────┐─┐─ ┌──┐ ──┐─┐──┐──┐─┐───────┐
                 │       ░░│ ░  ░░░   ░░░░░░  ░░░ ░  ░ ░░░░ ░│ │░ │░░│ ░░│ │░ │░░│ │░░░░░░░│
                 │ • │         ───     ───┐─             ┌───┘─┘──┘──┘───┘─┘──┘──┘─┘───────┘
                 └─  │░░─────┐─   ───┐    │ │   ░        │
                 │  ┌┘┐      │ ┌──   │ ─┐   │    ┌─┐── ──┘
                  ┌┐┘ │ ░░•  ░ │░░• •░│ │      ░░│░│░░│
                  └┘ ─┘─── │ ──┘   •  │            │  └─┐
                          ┌┘┐  │ ░░░░       ░  ░ ░ ░ ░ ░│
                       ─┐ │ └──┘────────────────────────┘                                   ┌─┐
                        │ │                                                                 │ │
                        │ │                                                                 │ │
                        │ │   ┌─┐                                                           │ │
                        │   ┌─┘░└─────────┐─┐─────┐───────       •   ────┐─┐───── ─┐──────┐ │░│
                        │  ─┘             │ │     │       ┌───┐─┐ ┌──    │ │     │ │      │ │░│
                        │       •  ─┐   │   │ ─── └─ ┌─┐  │  ░│ └─┘   ──┐   ┌────┘  ┌─────┘ │ │
                        │     ░  ┌┐ │ ──┘┐─  │░      │░└─ └───┘─  │  • ░│   │░░░░░• │░░░░░░   │
                         ─┐░     └┘      │   │   •  │    •      ──           ─────  │  ──┐─ ──
                          │    ░░  •   │    •  •  ──┘ ┌─  ─── ──     ┌──          │  ──  │
                         │     ░   ░ ░ │░  │░ ░ ░ ░ ░ │ │ ░    ░   ░ │ ░ ░   ░   ░│ ░ ▒│ │
                         │ │ ──────────┘─  └──────────┘─┘──────── •  │ •  │ ─┐░│ ─┘────┘─┘
                         │ │              •                      • ──┘─ ──┘  └─┘─
                         │  ───────────┐                          •░░░░ ░ ░│
                          •            │                           ────────┘ ──
                 ┌─┐  ┌───             └┐                                   •
                 │░│  │░ ░│ ░   ░░░── ░ └┐
                 └─┘  │  ─┘      •   ┌─  └─┐───┐────┐─┐─┐─┐─┐─
                      │░ ░│ ░ │░•  ░ │░│ ░ │░░ │░ ░░│ │░│ │░│
                      │  ┌┘   └┐ ────┘─┘   │ ──┼─┐  └┐       ─┐─┐───┐─┐─┐────┐───────┐───────────┐
                      │░░│ ░░  │░░░░░░░│ ░ │░░░│░│░░░│ │░░ ░  │░│   │░│ │░░░░│ ░ ░ ░ │░ ░░░ ░ ░ ░│
                      └──┘─────┘───────┘───┘───┘─┘───┘─┘──────┘─┘───┘─┘─┘────┘───────┘───────────┘








































```

*Figure from page 1 (2346x3317 px)*
