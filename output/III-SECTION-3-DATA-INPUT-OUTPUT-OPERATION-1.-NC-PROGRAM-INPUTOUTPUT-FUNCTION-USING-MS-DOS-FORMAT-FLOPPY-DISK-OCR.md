# III SECTION 3 DATA INPUT OUTPUT OPERATION 1. NC PROGRAM INPUTOUTPUT FUNCTION USING MS DOS FORMAT FLOPPY DISK OCR

*Converted from PDF: III-SECTION-3-DATA-INPUT-OUTPUT-OPERATION-1.-NC-PROGRAM-INPUTOUTPUT-FUNCTION-USING-MS-DOS-FORMAT-FLOPPY-DISK-OCR.PDF*

---


## SECTION 3

4203-E P-304



SECTION 3 DATA INPUT/OUTPUT OPERATION


## DATA INPUT/OUTPUT OPERATION


## 1. NC Program Input/Output Function Using MS-DOS Format Floppy


### Disk

The MS-DOS format 1/0 function enables input and output of NC part programs using MS-DOS format



3.5-inch floppy disks.



(1) Program input and output using this function is possible with the following MS-DOS formats:

- 3.5-inch 2DD floppy disks (640 KB/720 KB)

- 3.5-inch 2HD floppy disks (1.20 MB)

- 3.5-inch 2HD floppy disks (1.23 MB)

- 3.5-inch 2HD floppy disks (1.44 MB)



[Supplement] 1. "MS.DOS" is a trademark of the Microsoft Corporation.


## 2. Even if a 3.5-inch floppy disk can be read and written to at an MS-DOS-compatible

personal computer, it may not be possible to read and write to the disk using this



function if its format is not a regular one conforming to published MS-DOS



literature.



1-1. Operation Overview



The MS-DOS format 1/0 function indicates the operation (1) and (2) in the illustration given below.



(1)



3.5-inch floppy



Memory (MD1)



disk



(2)



Fig. 3-1 Operation Overview



(1) In the program operation mode, part programs and other NC data stored in the NC memory are



copied to a floppy disk using the copy command.



(2) In the program operation mode, part programs and other NC data saved in the floppy disk are



copied to the NC memory using the copy command.



1-2. Specifying MS-DOS File Names



MS-DOS file names are specified in the way shown below.



FOO: \PATH1\PATH2\ABC.MIN


# T 'J

Device name Directory File name



Path name



[Supplement] 1. The reverse slash "\" is used as the delimiter between directory names (the "\'



following the device name can be omitted).


## 2. It is not normally necessary to specify a device name when handling NC files but it

is essential to specify one for MS-DOS files.


```text


                                                                                                •
                                                               ┌──┐──────┐─┐─────┐──┐───────────░░───────┐░│
                                                               │░░│░░░░░░│ │░░░░ │░░│ ░░░ ░░░  ░──░░░░░░ └─┘
                                                                •     •
           ┌─ • • ───   •                 ──        •   ─── •    ──     ─┐─              •                 │
           │▒ ▒░░░░▒ ░░░░▒│ │░┌───── │░•░ ░░░│ ┌───░░░──░░ •░░──░░ ░░░──░│ ┌─┐──────────░░ ───── ──────────┘─
           └──────────────┘ │▒│      │░░░▒──▒│ │▒░▒▒•░░░──░░░▒▒░░──┐┐▒░░─┘ │░│▒░▒▒░▓▒░▒▒│ ▒▒░▒▓▓│
                                       ───  ─┘─ ──── ───  ───────  └┘───   └─┘──────────┘───────┘

           ─┐       ── ────
          │░│      │░░│ ░░ ░────────────────────────────────────────────────────────────────┐───┐────┐────┐
          │ │      │░░└─ ┌──░▒  ░ ░   ░▒░░░ ░░░░░▒░░░ ░ ░░░░░░░░░░ ░░▒░░░▓░░▒░▒░░░░░░▒ ░ ░░░│▒▒▒│ ▒░░│▒▒▒░│
                   │░░░░░│  ── ─── • ─────── ───────   ─────────────────────────────────────┘───┘────┘────┘
                   └─────
                         •   •   ─┐──┐─┐────┐───────┐─┐──────────────────┐─┐─────┐───────┐────┐────────────┐
                 ┌───░░ ░ ──  ░──░│ ░│ │░░░░│  ░ ░░░│ │░   ░ ░ ░ ░░░  ░ ░│ │░  ░ │░ ░░░  │░ ░ │░░░░░░ ░ ░ ░│
                 │░ ░░────░░───░░░└──┘─┘────┘───────┘─┘──────────────────┘─┘─────┘───────┘────┘────────────┘

                 │ │ │░        •        •░ •  •  │     ─── • ─────────┐─┐   ──────────────────────────┐─
                 └─┘ └─┐   │  •        •    •   ─┘─  •      •         │ │ •           ░ ░           ░░│
                       │░ ─┘─┐░ │░  ░  ░  ──░   ░░░•░░  ░  ░░░┌─────── ─┘    ─────────────────────────┘
                       │     │  │     ──┐                ─────┘
                       └┐ •░•░░ │░  ░ ░░│ │░░│    ░ ░░░│
                       └┘  •  • └─────  └─┼──┘ ──┐───┐─┘
                       │              ──┘ │  │   │   │ │
                       │░  ░ ░░ ░░░ ░░░░└─┘░─┘───┘┐─░░▒│
                ┌──────┘    ┌───┐─┐─┐   │         │     ─────────┐─────────────────┐
                │░ ░░░░░░░░░│   │ │ │░░• ░░░• ░   │░ ░ ░░ ░ ░ ░░ │░     ░        ░ └─
                └───────────┘  •    │      •            │    ─┐  └──    •            •
                                    └─────┐  ┌──────░───┘  ── └─      •  •            •  ─── ──── •    ────┐
                                ──  │     │  │        ░  •    │ •   ──░──    •    • ── ─┐        • ────░  ░│
                                    │   •       ░  ░    │░░  ░  ░ ░░░░░░░ ░ │░░░ ░ ░ ░ ░│ ░ ░░ ░░░  ░░░░ ░░│
                                    │░░░░░░ ░─┐┐──░░ ░┌─┘── ░──────░░────░──┘───░───░───┘── ──░─────────░░─┘
                                    └──────┐─ └┘  ────┘    ──      ──    •      •   •      •  •         ──
                                           │
            • │   ────┐─────┐─────┐─┐──
             ─┘  •  ░ │ ░ ░ │    ░│ │░░•
                │     │ •            ── ──────────────────┐──┐───────┐─────┐────┐────────┐─┐───┐─┐────┐
                │     │    ░     ░      ░ ░░░  ░░ ░░░ ░ ░ │░░│░░░    │░ ░ ░│   ░│ ░░░░░░░│ │░░░│ │░░░░│
                 ─────┘─────────────────┐───────────────┐─┼──┘───  ┌─┘──   │      ──  ───┘┐┘───┘─┘────┘
                                        │               │ │        │      │   ────  ──    │
                                        │ │ ┌────────   │ │ ────   └──  │ │   ░    ░░   │ │
                                        │ │ │           └─┼─     •    ──┘ │ ─────────── │ │
                                        │ │    ──       │░│     •░│     │ │             │ │
                                        │        ───────   ─────  └─────┘ └┐              │
                                         ───────   ░  ░  •░ ░ ░░    ░     ░│
                                                  ┌──     ─────── ────── ─┐
                 ──┐─ • ┌┐─────── ─┐────────────┐ │  ─────       •      │ │ ───────────────────────── ───
                •  │ │ ─┘┘ ░ ░░░░• │░░░░░░░ ░░ ░│ │░░   ░░ ░ ░•  ░  ░   │░   ░░  ░       ░  ░            │
                 ──┘ │        ───   ─── ──     •   •    │       ────────┘────────────────────────────────┘
                     │                                  └──
                 │ │ │        •                                    ─────────┐─┐─┐───────┐───┐─────┐─┐───┐
                 │ │ │ ───┐─  ░• ──      ──   • ───░  ░──░ ░────── ░  ░  ░  │░│ │░░░░ ░ │░░ │░░ ░ │░│ ░░│
                     │░░ ░│ ──┐ • ░──────░░░• ░•░░░── •░░─── ░░░░░┌─────────┘─┘─┘───────┘───┘─────┘─┘───┘
         ┌────    ┌──┘        │            │ │       • ──   ──────┘
         │        │░  ────┐───┼─░ ─────────┼─┼───────
         └────  ┌─┘       │ ░ │ │          │ │       •
                │░    ░  ░└─┐   │         ░│ │        ──────┐──────
                └───┐       └── │ ── ──┐───┘─    │          │
                    │ ░░│  │░░░   ░░•░░│ ░░░  ░ ░└────── ───  ─────
                     ┌──┼┐ └───────┐░┌─┘─────────
                     │  └┘┐        └─┘           •   ┌────────
                     │░░░░│ │  ░│          ┌── ── │  │░
                     └────┘─┘───┘─         │      └── ─────────
                                           └──┐─── ░
               ┌───────────┐        ┌─ ─┐──   │      ───── ──┐─  ──    • •  •
               │░░  ░░    ░│       ┌┘ │ │  ──   ───┐      •  │     • │  •  │  ──────────────────────────
               └───────────┘       │  │ │      │   └──────   │       └─   ─┘──                    ░  ░
                                   └──┘─░──────┘─┐─░░ ░░ ░ ──┘ ── •  │░──
                               ┌── │             │                       ────┐────┐───┐─────┐────┐──┐──────┐
                               │   └─░ ─────░░ ░░└──░░░░░░░───┐─░░░──░ ░•░ ░ │░ ░ │░░░│ ░░░░│ ░ ░│ ░│░ ░  ░│
                               └── │░──░░░ ░───── ░░░───── ░░ │░─── ░ •░ ┌───┘────┘───┘─────┘────┘──┘──────┘
                                       ─────     ────      ─── •   ─── ──┘









```

*Figure from page 1 (2329x3294 px)*


---



4203-E P-305



SECTION 3 DATA INPUT/OUTPUT OPERATION



[Supplement} 3. The total length of the sequence "device name:path-name\file name" must not



exceed 64 characters.


## 4. The length of the path-name must not exceed 47 characters.


## 5. The file name consists of a main file name (with a maximum length of 8 characters)

and an extension name (with a maximum length of 3 characters), and a period"." is



used as a delimiter between the main file name and extension. The file name must



begin with a letter of the alphabet and the characters that follow it can only be



numerals, letters of the alphabet, "." or"-".



1-3. Command List



The list of commands used for the MS-DOS format 1/0 function are given below.



Item Command Function Outline



Directory DIR Displays an MS-DOS format directory.



Copying* COPY Copies files from MS-DOS format to OSP format and vice versa.



Renaming* RENAME Used to change specified file names in the MS-DOS format.



Deletion* DELETE Used to delete specified files in the MS-DOS format.



Remaining FREE Indicates the remaining memory capacity in the MS-DOS format.



capacity



File protection* PROTECT Prohibits updating the information of specified files in the MS-



DOS format.



Program im- IN Program Input Work program files are input from the MS-DOS



put* formatted floppy disk to the memory disk while deleting any "%"



codes.



Program out- OUT Work program files are output from the memory disk to an MS-



put* DOS formatted floppy disk. If option "E" is selected, only the "%"



record will be added at the beginning and end of the output files.



MS-DOS Quit QUIT Used to quit MS-DOS.



The commands indicated by an asterisk (*) are executed on the directory-selection-based file operation



screen. The following explanation gives basic information on using these commands. In addition to the



basic information given below, there are various functions including the function to display the registered



part program files in batch. For details of the functions, refer to Section 2, 15. "Directory-selection-based



File Operation Function".



Operation for the commands is described below.



Since all of these commands are executable in the MS-DOS mode, the procedure to set the MS-DOS



mode is explained first. Description of the individual commands is given assuming that the MS-DOS has



been set.



Procedure used to set the MS-DOS operation mode:



(1) Press the EDIT AUX mode selection key to select the PROG OPERATION



mode.


```text


                                                                                                •
                                                               ┌──┐────────┐───┐─┐──┐────┐─┐────░░─────────┐
                                                               │░░│ ░░░░ ░ │░░░│ │░░│ ░░░│ │░  ░──░░░░░░ ░░│
           ┌────   •         ──── ───   •          •     ────── ──┘  ─── • └───┘─┘──┘ ───   ──
           │     ── ┌───────┐    •   ─── ┌────────┐ ┌───┐           •   • •          │   ───               •
           └────┐░  │       └───┐ ┌─     │        │ │   │ │              │           │      │       │       •
                └───┘───────┘   └─┘  ────┘        └─┘── │ │       ───    │ •       • │░     │ ─┐  ──┘┐  │  │
                                    │░░░░│░──┐─┐── ░░░ ─┘                                 ──┘─ └──   └──┘──┘
                                ┌─┐ │        │ │        └┐─┐──────┐─┐──┐────┐─┐──┐────────
                                │░│ │░░│ ░ ░░│ │ ░░ ░░░│ │░│ ░ ░ ░│ │░ │░░░░│ │  │░░ ░░░ ░│
                                │ │ │  │               │ │          │       │             └────────────────
                                │░│  │░└──────────░░░•░└─┘ ───░│ ───┘─░░░──░│ ░ ░░░───────  ░░ ░ ░░░░ ░ ░░ ░
                                └─┘  └─           ─── •       ─┘                 ──         •           ──  │
                                    •          ─┐         •        •  ─┐ ───       •       ░ ───── ────     │
                                     ───┐ ┌─░ ░░└───░ ░░•░░░───── ░░░ ░└─░░░░ ░ ░ ░░░ ░░ ░ •░ ░ ░░ ░░ ░  ░░░
                                    │ ░░│ │░░ │░ ░░░  ░ ░── ░░░░░░┌─░ ░ ░ ─── •░░░─────░──░░░░─────░───░────
                                    └───┘ └── │░░ ──    •   • ░ ──┘ ──────   • ───     •  ────     •   •
                                         •    └───  ────  ── ───
          ┌───┐    ──────────┐─┐──┐
          │   │    ░ ░░░░░░░ │ │░░│
          └───┘  ┌─  ┌────── │ │  └┐──────┐─┐──┐─┐─┐────┐──┐────────┐──┐────┐───┐─┐────┐
                 │░░ │░ ░ ░░░░ │░░░│ ░░░ ░│ │░ │░│ │░░░ │░ │░ ░░  ░ │░░│ ░  │░ ░│ │░░ ░│
                 │ ┌─┘─     ── │                 └─┘────┘  └─     ──┘┐                ─┘ ──────────────────
                 │░│   ┌───┐    ┌──────░░░░░│ ┌─┐        ──          └────────────░ │                       •
                 │░    │   └────┘░     ─────┘ │░└────── •  ┌─── • ┌─ │  ░░░░░░ ░ ░──┘ ───────────────────── ░│
                  •░───┘░░░│    │  │░░░       │░░░░░░░░│ ░ │░░ ░░─┘ •░──░ ░░░░░░                           │░│
                 │░  ░░ ░ ░│ ───┼─ │  ░──┐    │░       └── ░•    ░│   ░ ░         ┌─┐──────────────────────┘░│
                 │░ ░│░░ ░ └┐   │░ │░░░  └─┐  │░ ░•░░░ │░░ ░ ░ ──░░░░░░░░░░ ░░ ░  │░│ ░░░░░ ░░░ ░░░ ░░░░░  │░│
                 │░░░└────░░│   │  │░░░░░░░│   │ •░───┐┘────░│ ░░──────────┐───░ ░│░░ ░░────── ░░•░░┌────  │ │
                 │░░       ┌┘ ──┼─ │ ░  ──░│ ─┐┘      │      │             │    ──   ░         ── ──┘      │ │
                 │░ ─┐──── │    │░ │░░ ░  ─┘  │░░░░░░░░ ░░░░░ ░░░░░░░ ░░░░  ░░░ ░░░ ░ ░ ░░░░░░•  •   ────  │ │
                  │░░│ ░░ ░░ ───┘ ─┘──────    │ ┌───────────────────────────────── ░───────── ░░░░░░░░░░░  │ │
                  │ ─┼───░│     │          • ─┘░│                                  •          ──  •   ───  │ │
                 │░░░│    └─────┘░  ───  ░    │░└─────── ────────── ─── ───── ┌─ ── ───────  •  ── ───       │
                 │░┌─┘─┐──░░░░░ └─   ░░───────┘ ░░░░░░░░ ░░░░░ ░ ░░ ░░░ ░░░░░ │░ ░░░░░░░ ░░░ ░• ░░ ░░░   ─┐┐ │
                 │░│   │      •    │           │░░░░ ░░ │░•                                      │        └┘ │
                 │░░── ░░░ ░░│  │  │░│         │░░│ ░░│ │ ░───░────────┐──────────────┐─┐────────┘─────┐    •
                 │░│ ░┌──────┘─ │ │ ─┘─ ───────┼──┘░░░│  │░   •░ ░ ░ ░░│ ░  ░      ░  │░│ ░  ░ ░     ░░│ ─┐
                 │░│  │        ─┼─┘            │   ░░─┘  └───       ───┘┐   •  • ─────┘─┘───────       └─ │
                 │░  • ───────  │░  ────       │░░░░│             ─┐    │       •                   ┌──   │ │
                 │░░░░░ ░░  ░░──┼─ │░    ────── ░░░░│ ───────┐────░└┐──░░  ░─── ░░┌─ ─┐──────┐──────┘░░│  │ │
                  •░──────────  │ ─┘────       •░░░│ ░░ ░░░░ │░ ░ ░ │░░──░  ░░  •░│   │░░░   │   ░ ░   └┐ │ │
                 •              └─       ─────┐  ──┘──────── │ ░░• ░ ┌┐    ░░░░│ │░   ░░  ░░░│   ░   ░  │ │ │
                  ─────────────┐┘ ─┐───┐      │░             ░ │  • ─┘┘────────┘─┘───────────┘──────────┘ │░│
                  ░░░░░░░░░ ░░░│   │░░░│        ░░░░░░░ ░░ ░░░─┼──░│                                      │ │
                                   │     •  ────               │  ─┘──────────────┐────────────────────┐──┘ │
                ┌────── ─┐░────────┘░──── ── ░░░░░░┌────┐░ •░░ │░░    ░░  ░░░░ ░░ │░░░░░░ ░░░░░░ ░░ ░░░│░░░│
                │░░░░░  ░│░ ░░░ ░░░░•░░░░ ░░░░────░│ ░░░└─░░── │░────── ░░───┐────┼───────░───── ░─────┘── │
                │ ──── ░  • ──┐ ──── ───── ─── ░  • ────   │    •      •     │    │              │         │
                │             │ ░             •            │      ──                   ──  ░   ──┘        ░│
                │░░   •░░░░  ░░░   ░░ ┌───░ •░░░░• ░  ░ •░░░░ ░┌─┐░░░ ░ │░░░░│ ░─┐┐───░░░░░ ░•░░░░░░░──░░░░│
                └────┐░────┐──────────┘        ──    •   ──────┘ └──────┘────┘── └┘   ─────── ───────  ────
                │    │     │           ──┐──┐─┐  ───┐ ┌──
                │ ░░ │░░  ░░ ░░ ░░░░ ░░ ░│ ░│░│░░░░░│ │░░░░
                │                        │                  • ─── ────  ───   ──      •              ──  ──
                └──────┐──────░──── ░░░──┘──── ░░░──░░░─────░░ ░░  ░ ░•░░░░───░░──────░──────┐░─────┐░░•░░░│
                │░ ░░ ░│░░░░░░•░ ░░────░░░░░░░────░ ───░░░░ ░────░ ── ░────░ ░• ░░░░░░•  ░░░ │░ ░░░ └──░───┘
                └──────░┌─────  ───    •   •      ──    ─────    ──  ──     •   ── ──    ────  ─── •   •
                │       │          ───┐ ┌──  ──┐     •
                │░ ░░░░ ░  ░░  ░ •░░ ░│ │░░░ ░░│ ░ ░ ░░░     ░│
                └──┐─┐            ┌─┐─  └──  ──┘              └───── ──────────────────
                   │ │░───┐    ░  │ │  ░           ░                  ░       ░        │  ─────
                 ──┘ │    │ ──────┘─┘──────────────────────────────────────────────────┘ │     │ ┌─┐
                      │ ░░└─                                                             │░    │ │ │
                      └───┘                                                              │ ───  ─┘┐
                                                                                           ░░  ░░▒│
                                                                                          ────────┘















```

*Figure from page 2 (2346x3317 px)*


---



(2) Press the function key [FB] (EXTEND) twice.



4203-E P-306



SECTION 3 DATA INPUT/OUTPUT OPERATION



DATE



DIR



PIP



EDIT



~~Tl



LIST lcoNDENS



[EXTEND]



@ @@J @@] @J @J@



Press [F8) (EXTEND} twice/



The function names on the screen will change to those given in item (3) below.



(3) Pr s the function key [F2] (MS-DOS).


#### PROTEC US-DOS DNC-B [EXTEM:l]

@@@J@@J@J@J@



\ Press [F2] (MS-DOS).



is displayed.



The function names on the screen will change as indicated to the right.



=EX



=MSDS



FILE FILE MS-DOS



DIR COPY RENAME DELETE FREE PROTECT QUIT [EXTEND]



Press function [F8] (EXTEND).



The function names on the screen will change as indicated to the roght



=EX



=MSOS



>EX



The commands are explained below.



M~S



[EXTEND]


```text


                                                                                               ───       ──
                                                               ┌──┐────┐─┐─┐───┐─┐─┐───┐─┐─────░░░───────░░│
                                                               │░░│░░░░│ │ │░░░│ │░│░░░│░│ ░░░░─── ░░░░░░──┘
          ┌───────  ──                   •             ────────┘──┘────┘─┘─┘───┘─┘─┘───┘─┘─────      ──
          │       ─┐  ─────────────────── ────────────┐                                                    │
          └──────┐ └──      ░              ░░  ░   ░  │      ──────────────────────────────────────────────┘
                 └─┘  ─┐───────────────── ────────────┘───  •
                       │                 •                ──                               ┌─┐
                       └─┐                                                                 │ │
                       │ │                                                                 │ │
                       │ │                                                                 │ │
                       │ │  ┌───── ─┐───── ─┐────────────┐─    ────┐─────┐─┐────────────── │ │
                       │ │  │     │ │     │ │            │ ─┐──    │     │ │               │ │
                       │ └─  ┌──┐ │   ┌─┐ │ │    ──  ┌┐  │  │░  ─┐     │ │ └─────  ────────┘ │
                       │   ──┘░░│    ─┘░│ │ └────  ──┘┘──┘  └──  │ ────┘  ░░░▒░░░   ░░ ░▒░   │
                        ─┐   │  │     │          •              •         ────────     ──┐  •
                         └─   ──┘  ┌──┼─┐ ──┐─┐─┐ ─┐  ─┐─ ─┐─┐─┐ │ ┌─┐─┐ •          ┌─   │
                            │  ░│  │░ │░│   │ │░│ ░│ ░ │ ░ │ │░│ │ │ │░│ ░• • │ ░ ░ │░│ ░│
                            └───┘  └──┘─┘───┘─┘─┘ ─┘───┘───┘─┘─┘  ─┘─┼─ •    ─┘     └┐┘──┘
                                 ──              •             └┐    │░ ░  ░  │      │
                      ┌─                                        └────┘─ ──────┼────
                      │ ──────────┐────────┐───────┐──┐─────────              │     ──┐───┐─
                                  │        │       │ ░│     ░░         ░      │░    ░ │░ ░│
                 ┌─┐  │  •      ──┘    ┌───           └┐──────────────────────┘───────┘───┘
                 │ │  │ │░│  ░  ░  ░   │░ ░ ░  ░      ░│                                    ┌─┐
                 └─┘   ─┼─┼──     ─────┘───────────────┘                                    │ │
                        │ │  ┌────                                                          │ │
                        │  ┌─┘░░░░ ─────────┐────────────── ─────────────────────  ───────┐ │ │
                        │  │░░────          │              •                     ┌─       │ │ │
                        │   │     ─┐──────  │     │  ───┐ │ ┌────┐ ┌─────┐ ┌─────┘ •  ──    │ │
                        │ • └┐░░ ░░│ ▒░░░░  │     │  ░░ └┐┘ │    │ │     │ │     │  ──  ────  │
                        └┐ ░└┘── ──┘─── ──   ─────   •   │   •  •  └─   ─┘ │   ──            •
                         │ •    •      •          │ │ ┌─┐     ── ┌─┘ ┌─┐ └─ ──┐░ ──░┌─┐  ┌───
                         │  │  ░   ░  ░ ░│  ░ ░ ░ └─┘ │░│ ░│  ░░ │ │ │░│ ░ │ ░│   ░ │ │ ░│
                        ┌┘  └────  ────┐░│    ─── │ │ └─   │ ─── └─┘ └─┘ ──┘ ─┘  ── └─┘ ─┘
                        │ •      ──    └─┘         ─┘       •   •   •   •   •  ──  •   •
                        │  ┌────   ────   •  ░░░  ░ ░░  ░░░│
                        │  │░   │    ░░░░░░ ───────────────┘
                        │  └────┘  ─────────

                      ──┐─┐────┐─┐────┐─┐───┐─┐────┐──┐─┐────┐─┐───┐────┐─────┐─┐──┐
                       ░│ │░░░░│ │░░░░│ │░ ░│ │░░░░│ ░│ │░░░░│ │░ ░│░░░░│ ░ ░░│ │░░│
                      ─┐┘┐┘────┘─┘────┘─┘───┘─┘────┘──┘─┘────┘─┘───┘────┘─────┘─┘──┘
                       │ │                                                                 ┌─┐
                       │ │    •                                                            │ │
                       │ │  ──░──┐                                                         │ │
                       │░│   ░░░░└──┐─────────────      ─┐───────      ───        ───────┐ │ │
                       │ │    ───┘  │             ── ─┐  │         ─┐┐    ─┐───┐──       │ │ │
                       │ │        │  ┌──   ──────   •░└─┐┘  ┌──┐ ─┐ └┘───  │░ ░│     ───   │ │
                       │ └─ ┌┐░───┘─ │░░──  ░░░░▒   ░  ░│  ─┘░░└─ │░░░░ ░• └───┘─  ┌─ ░░─┐─  │
                        •   └┘       │      ───── ─┐────┘   └┐─┘  └─    •  │      ┌┘   • │  ─┘
                         ──    •  │                │         │    │  ──   ─┘ ░  ──┘ ┌─┐ ┌┘──
                           │  ░ │ │ ░ ░   ░░ ░ ░ │ ░ │░░ ░   │░│  ░ │░░ ░ ░ ░   ░   │░│ │
                           └────┘─┘───────────── └── └──  ─┐ └─┘ ── └── ─── ───────░└─┘░│
                     ┌─────                     •   •   ── └─   •  •   •   •       •  └─
                     │          ──┐──┐ ─────────
                      ──          │  │          ────────────────────────────────  •
                     │░░░   ░░░░  ░ ░░     ░│ │      ░░               ░            │
                     └─┐─┐───  ─────────────┘─┘────────────────────────────────────┘
                       │ │                                                                 ┌─┐
                       │ │  ┌──┐─                                                          │ │
                       │ │  │░▒│░                                                          │ │
                       │ │   ──┘─                                                          │ │
                       │ │ ┌─    ─┐───────  ─────┐─┐──────────── • ─────┐──     ──         │░│
                       │ │ │░░•░░░│ ░░░░░░│      │ │            │░│     │░ ────┐  •        │░│
                       │ │  ─┐░░ ░└─┐░░░░░│      └─┘──   ───────┘ │ ────┼──░░ ░└─  ┌─────┐─┘ │
                       │     └──    │░──   •     │      │       │ │     │  ┌───┘   │   ░░│  │
                           ┌─┘     ─┘       ─────┘──────┘  ───── • ───┐─ ─┐┘           ─┐┘ ─┘
                           │  ░│    │ │░       ░ ░ ░ ░      ░░░ ░ │ ░░│ │ │ ░░      │░ ░│
                           └─ ─┘  ░   │░│ •░   ░ │ │ • │ ──  •░ │ │ •░│ │ │ ─┐  ──  │░ ░│
                             •     ───┘─┘  ──────┘ └─ ─┘─  •  ──┘─┘─ ─┘─┘─┘─ │    ──┘───┘
                     ┌────┐──   ───      ──       •         •                 ──
                     │░ ░ │░ ░ ░ ░░ ░   ░   ░    ░░ ░│
                     └────┘──────────────────────────┘








```

*Figure from page 3 (2346x3317 px)*


---



1-4. DIR (directory)



4203-E P-307



SECTION 3 DATA INPUT/OUTPUT OPERATION



This function is used to display a list of the files and directories saved in an MS-DOS format floppy disk



(FOO:).



The operating procedure is indicated below.



(1) Press function key [F1] (DIR).



"DI" is displayed on the command line.



~DS



>DI



DIR COPY RENAME DELETE FREE PROTECT OU IT



@J@J @J@@ @J @J @J



\ Press [F1] (DIR).



"DI" is displayed.



(2) Enter the device name following ">DI" for the device which stores the files.



Example 1: The following command displays all the directory names and file names in the



MS-DOS format floppy disk designated as device "FOO:".



>DI FOO:



Example 2: The following command displays all the directory names and file names in the·



directory "PATH" of the disk designated as device "FD0:".



>DI FD0:PATH (or alternatively, >DI FD0:\PATH)



Example 3: The following command displays all the directory names and file names under the



directory "PATH1" which is under the directory "PATH" of the disk designated as



device "FD0:".



>DI FD0:PATH\PATH1



Example 4: The following command format displays all the directory names and file names that



start with the character string "FO" in the directory "PATH" of the disk designated as



device "FD0:".



>DI FD0:PATH\FO*



(3) Press the WRITE key.



WRITE


```text


                                                                                                ───
                                                                ┌─┐─────┐───┐───┐─┐─┐─┐─┐────── ░░░──────────
                                                                │░│░░░ ░│ ░ │░░░│ │░│░│ │░░░░░ ░───░░░░░░░░░
             ───────            ────────────────────────────────┘─┘─────┘── └───┘─┘─┘─┘─┘───────     ───
           ┌─       ─────┐──────
           │   ┌─    ░░  │    ░    ┌────
           └── │   ─────  ───      │
              ─┘ ┌─                 ────────────────────────────────────────────────────────────┐────┐─┐─┐──┐
                 │  ──     ───     •       ░             ░  ░                ░    ░           ░ │░   │░│ │░░│
                 │ •░░                   ──             ────────────────────────────────────────┘────┘─┘─┘──┘
                 │     ───────────────┐──  ┌──┐─┐──────┐
                 └─   │░░ ░ ░░░░░░░░░░│ ░  │░░│░│  ░░░░│
                 │  ──┘    ┌─       │  ──┐ │    └──────┘
                  │    ░•░░│ │░░░░░ │░• ▒│░ │░░░│
                  └──  │ ┌┐  └── ─── •  • • │ ──┘┐─┐────┐
                       │ └┘░ │░░░░░░│ ░│ │░ │░░░ │░│  ░░│
                       └─  ┌─┘──────┘──┘─┘──┘────┘─┘────┘
                          ─┘                                                                 ┌─┐
                         │ │                                                                 │ │
                         │ │  ┌────┐                                                         │ │
                         │   ─┘░░  └─┐─────┐─┐───── • ──────────── • ─────   ─────   ──────┐ │ │
                         │  │░░──┐─  │     │ │     • │            • │     ┌──     ┌─┐      │ │ │
                         │  │    │ │   ┌─┐   └────┐  └─────   ┌──   └─────┘   ──  │░└──────  │ │
                         │  │ ░┌─┘ │ ──┘░└──  ░░░░│ │ ░░░░░│ ─┘░░  │ ░░░░░ │ •░░• │ │      ── ┌┘
                         └─ ░ ─┘  ─┘   │ │   ─────┘ └──  ──┘  │    └──   ──┘        │    •    │
                           ──   ┌─  ──┐ ─┘  │          ┌─      ─┐     ┌─┐    ──┐    └───┐ ┌───
                          │  │░ │ │ ░ │ ░░• │░ • │ │ │ │░│ │░ ░░│ ░ │ │░│ ░ │ ░│  ░░ ░ ▒│ │
                          │  └──┘ └── │ ──  │   ─┘─┘─┘─┘─┘ └─ ──┘───┘─┘─┘───┘──┘────────┘─┘
                         ┌┘ •   └─   │    ░│   ░          •  •
                         │   ───   ──┘  │ ─┘── ──
                         │  •░ ░ ░░ ░░░─┼─    •
                  ┌─┐  ┌─┘        ───── │             ───
                  │ │ ┌┘  │             └──────────┐──   ──────┐─────────┐ ────────────┐
                  └─┘ │   └──      ────           ░│           │         └─            └── •        •
                      │░       │ │  ░   ░               •         ░   ░       ──── │ │    │ │   │   ░│
                      └────────┘ │  │ │      ░                ──            ─┐ ░░  │ └────┘─┘───┘────┘
                                  • └─┘────┐   ░  ░░░░ │░│ │░░░░ ░░░  ░ │░  ░└─── ─┘─
                                           │   • ───── └─┘ └─────────── └────┘   •
                      ┌─────────┐  ────────┘─ │ •     │   •            •            ──────────────────
                      │░░░░░░░ ░│ │░░ ░ ░ ░░ ─┘─     ░└──     ──░ ░ │ ░     ───────┐    ░           ░
                      └─────────┘ │    ────┐ ░  •                   │          ░   └───────────────────
                                  │        └─┐── • ─── │   ───░░ ░ ─┘─░        •  ┌┘
                                           │ │         │                          │
                      ┌────┐─┐──┐  ────────  │ ───────┐ ┌───────────┐─┐─────   ───┘   ────   ───   ──────┐
                      │░░░ │░│ ░│ │░░ ░░░ ░░─┘─  ░  ░░│ │░ ░░   ░ ░ │ │░░     │ ░  ───  ░ ┌─┐   ┌─┐     ░│
                      └────┘─┘──┘ │     ───┐ ░  ┌─┐   │ └─    │   •         ░ │░┌─ ░  │   │ │   │ │     ┌┘
                                  │ •    ░ │ ┌──┘ └───┘─  • ──┘─── ──  ───────┘─┘ ────┘ • │ │░ ░░ ░    ░│
                                  │░░ ░────┘░│             •      •  ──                • • • ──────── ──┘
                                   ───       └───────────┐
                       ─────────      ─────  ░  ░   ░░   └─
                      │      ░  • │              • │   ──┘ ─────────┐       ─────── ──    •   • │      ───
                      └─────────  │           ─── ─┘      •     ░   └─┐─────     ░░   ── │ ┌─┐ ─┘──────   ─┐
                                  │░░  ░░░ ░░ ░░░ ░ ░│ ░ ░░┌── ──░•░│ │░░░░░  ──░──░──░ ░│ │░│ ░░░░░ ░░░  ░│
                                  │░──░─────── •    ─┘ ────┘  •  • ─┘─┘───────  •     ───┘─┘─┘─────────────
                                   •  •       • ────  •
                                       •░ │░░░ ░░░░░░░  │
                  ┌─┐─┐────┐──┐─┐─┐──┐─   └─────────────┘──
                  │░│ │ ░░░│ ░│ │░│ ░│ ░░░│                ─┐
                  └─┘─┘────┘──┘─┘─┘──┘────┘         │     │ │
                                                    │ ─── └─┘
                                                    │  ░  │░│
                                                    │ •     │
                                                     │░│    │
                                                     └─┘────


















```

*Figure from page 4 (2346x3317 px)*


---



4203-E P-308



SECTION 3 DATA INPUT/OUTPUT OPERATION



[Supplement] 1. The use of the wild cards"*" and"?" is only valid for files; an error will occur if either



of these symbols is used with a device name or directory name (path name).


## 2. A maximum of 12 file names and directory names can be displayed on each

screen.



If it is not possible to display all the directory and file names on a single screen, the



symbol "=" (the command prompt) will not be displayed on the command line and



the cursor display will remain unchanged. In this condition:



(a) Pressing the BS key will scroll the screen forward one page.



(b) Pressing the WRITE key will scroll the display continuously in page units



until the end of the directory is reached (press BS to stop scrolling part way



through).



{c) Pressing the CAN key will terminate execution of the command and leave



the currently displayed page.

3. "<DIR>" displayed in the sector column indicates that the entry is a directory.


## 4. If a file name includes a character other than those indicated below, such a

character is replaced with "?" to be displayed.



Space,!,",#,$,%,&,',(,),*,+,-,.,/, Oto 9, :, ;, <, =, >, ?, @, A to Z, [, ¥, ], ",_,a to



z, {,I,}, -


## 5. The following options can be specified after the file name. They must be preceded

by a semicolon ";".



;P (file protected state is displayed following the date)



00 Not protected



01 File protected



1-5. COPY (copying)



This function copies files from the MS-DOS format to the OSP format and vice versa.



The operating procedure is indicated below.



(1) Press function key [F2] (COPY).


#### DIR

COPY



RENAME



DELETE



FREE



PROTECT



OU IT


# CED

@ @ @ @


# CED


# CED

\ Press [F2] (COPY).


```text


                                                                                               • ──      ──
                                                               ┌─┐───┐─┐───┐───┐─┐─────┐────── ░░░░──────░░│
                                                               │░│░░ │░│ ░ │░░░│ │░ ░░ │░░░░░░ ─── ░ ░░░░──┘
          ┌─────            ────────   ──            •   ───── └─┘   └─┘   │  ─┘ └──── └──────       ──
          │      ───────────        ┌──  ────┐─┐───── ───     •   ───   ──┐┘─┐  •     •       ──       ─── │
          └─────┐          ░┌────── │░       │░│                          │  │                             │
                └───────────┘       │   ──┐ ┌┘ └─     ┌──┐───    ─── │ ┌──┘  │ ┌──  ──  ───┐─┐──   ───  │  │
                                    └───░░└─┘░░│░─────┘░░│ ░░────░░  └─┘░░ ┌─┘ │░░──░░──░░░│ │░░───░░ ░─┘  │
                                ──  │         │         •          •       │  •                          ──┘
                               •    └───░░░░░░│ ░  │░ ░• •░░░░░ ░░│ │░ ░░░ │ •░░░░• │░  ░• │░░░░░░•    •░░░│
                                ──  │░ ░──── •     └─ •     •     │ └──  ──   ── •  │     ─┘──────      ───┘
                                    │       • ─────  • ────┐ ────┐ │   ──  ───  • ── ────┐        ─────┐   │
                                    └── ──░░ ░░░░░░ ░  ░░░░│ ░░ ░│ │ ░░░░• ░ ░ ░░ ░░ ░░ ░│ ░░░ ░• ░░░░░│ •░│
                                    │  •  ────┐░ •            •  │ │ • •    •         │ ░   •       ─┐─    │
                                    │         │   ─┐              ─┘  •             ──┘  •    ──   • │     │
                                    └── ┌─    └──░░│ ░─────┐─ ───░░░•░░░│ ──────────░░░          ──   ─────
                                       ─┘    ─┘            │ •        • └─               ┌──┐
                                    │░│ │░░░░░ ░│░│ ░░ ░░░ │░ ░     ░│ •░░░░ ░░░░░ ░ ░   │░░│
                                    │ │ │       │ │        │ │       │                       •  ───────┐
                                    │░│ └──────░└─┘─░░░│░░─┘░└──░ ░░░└─░───┐──░─────░░░ ──░──░──░░░   ░└─┐
                                    └─┘ │  ░ ░ •  ░ ──░└──░ •░  • ───  •   │  •    ░───┐  •    ░         └─
                                       •     │  ── •  •   ── ──  •      ─── ── ─────   └── ───────   •
                                        ┌────┘─
                                    ┌─┐ │          •  •     •    ──────┐─┐──────┐──┐─┐─────────┐─────┐───┐
                                    │░│ └─░░░░ ░──┐ ┌─░────┐ ┌──░ ░ ░░░│ │░░░░░░│ ░│░│   ░░░ ░ │ ░ ░ │░░░│
                                    │   ░ ──────░░│ │░░░░░░└─┘░░───────┘─┘──────┘  └─┘─ ───────┘─────┘───┘
                               ┌─┐  └┐──                                         ──    •
                               │░│   │░░░░  │░░░░ ░•   •░  ░░░░   ░ ░░   ░  ░░    ░    ░ ░•           ─┐
                               │ │ │  ──    └──────   │ │ ──  │     •        ─┐          •         ┌─  └┐
                               │ │ └──  ░─┐ │      ───┘─┘   ┌─┘────   ┌─   ░  │                    │    │
                               └─┘ │      └─  • ───      │  │       ┌─┘ ─┐─ ┌─┘───────┐────────────┘──  │
                                    │   ░ ░░ ░ │░░░░░░  ░└── ──░──░ │░░ ░│░ │         │               ──   │
                                    │   ─────┐ └─┐──┐ ┌──┘     •  ──┘────┘─           └─────────────    ───┘
                                   •         │  ░│  │░│                                                    │
                                    ──────                                                                 │
                               ┌─┐ •        ───────────┐─┐─┐──────┐─┐─┐─┐──────┐─┐───  ┌──┐─┐──────────────┘
                               │░│  │░░ ░░──░░░░ ░░░░░ │░│ │░ ░░░ │░│ │░│ ░ ░ ░│ │░░░│ │░░│ │░░░ ░ ░ ░░░░░░│
                               └─┘  │ ────░░──░ ─────  └─┘    ────┘─┘ └─┘ ──  •    ──┘─┘──┘─┘──────────────┘
                                    │                ─┐   ┌───       •   •  ─┐ ┌───
                                    │ │░•  ░░░░ ░░ ░░░│ ░ │░░░░░░│ │░ ░░░ ░ ░│ │░░░│
                                    └─┘  ───┐──            ──────┘─┘─────────┘─┘───┘
                                       ░│   │  │░• ░──░░░•░
                                       ░│   │  └─░── ░───░──
                                                    •
           ───┐   ───────────────┐─┐
             ░│           ░ ░░░░ │░│
            ──┘ ┌──         │    └─┘────────────┐─┐────┐────────┐───────────┐─┐─┐─┐─┐─┐───┐
                │  ░ ░░░░───┘░░░•░ ░░░ ░░  ░░  ░│ │░ ░ │░░ ░ ░  │░   ░  ░░ ░│ │░│ │░│ │░░░│
                │ ──         ───   ──────      •      ┌┘────────┘───────────┘─┘─┘─┘─┘─┘───┘
                └┐  │  ────  ░   ──      ──      •░░ ░│
                 │ ┌┘┐     ───     ┌─┐─           ────┘
                 │ │ └┐ ░░│ ░░ ░░│ │░│   ░       │
                 └─┘  └┐─┐┘──────┘─┘─┘───────────┘                                         ┌─┐
                       │ │                                                                 │ │
                       │ │                                                                 │ │
                       │ │   ┌───                                                          │ │
                       │░│   │▒░░ ───    ┌─              ┌─     ─┐─      ──────  ─┐──────┐ │ │
                       │ │   └───     ── │ • ──       ── │ • •   │ •    •       │ │      │ │ │
                       │ │  │    ─── │   └─ │  ──   ──  │ • │ ── │  ───┐     │  │ │       ─┘ │
                       │   ─┘        └─     │ ░░░  │░   │   │  ░    ░  │  ─┐░│ │  │      •   │
                        ──    ┌─┐─┐─┐  ───         │     • •               │ └─┘─ └───┐─   ──
                           │  │ │ │ │ │░░    ░░░ ░ │ ░░░     │░     ░░░ ░ │ ░ ░   │  ░│  ──
                           └┐   │ │ │ │ ┌──░  •░ ░ ░ ░─┐ ░   │░   ░ ─┐┐ ░ │ ┌───░   │░│ │
                            └─    └─┘─┘▒│   ──  ─────  │ ───  ── ─── └┘───┘─┘   ────┘─┘ │
                              ────     ─┘ ░░░░ ░░░ ░░░░└─   •                 ──
                                         ──────────────┘
















```

*Figure from page 5 (2346x3317 px)*


---



4203-E P-309



SECTION 3 DATA INPUT/OUTPUT OPERATION



The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.



MS-DOS CONVERTER: COPY



PROGRAM OPERATION



MS-DOS CONVERTER: COPY



com



I taX DI SPLAY PROCEDURE



[F2]



MDl :*. *



[F3]



FOO:*.*



MS-DOS CONVERT



197/07/15 14:10:00



OVERWRITE



TO DISPLAY OTHER IOOEXES, AFTER PRESSING [Fl],



INPUT THE DEVICE NAME 00 FILE NAIIE, THEN PRESS [WRITE] KEY.



DEFAULT DEVICE NAME=



DEFAULT FILE NAME= *.*



>XCO



(2) Enter the device name, path name, and file name of the program to be copied.



(a) Use the following command format when copying from MS-DOS format to OSP format:



>CO <device name>:<path name+ file name or path name> <device narne>:<file name>



If a path name is specified as the copying source, all the files (excluding directories) listed in the



directory indicated by that path name will be copied.



(b) Use the following command format when copying from OSP format to MS-DOS format:



>CO <device name>:<file name> <device name>:<path name+ file name or path name>



If a path name is specified as the copying destination, the file (or files) is (are) copied into the



directory indicated by that path name.



Example 1: The following command copies A.MIN in FD0: {MS-DOS) to MD1: (OSP) under



the file name B.MIN.



>CO FD0:A.MlN,MD1 :B.MIN



Example 2: The following command copies all files in the directory "PATH" of FD0: (MS-DOS)



to MD1: (OSP).



>CO FD0:PATH\*,MD1:



>CO FD0:PATH,MD1:



Example 3: The following command copies all FD0: (MS-DOS) files whose main file names



start with the letter C and comprise three characters or less to MD1: (OSP).



>CO FD0:C??.MIN,MD1:


```text


                                                                                                ───
                                                                ┌───────┐───┐─────┐───┐─┐─┐──── ░░░────────░│
                                                                │░░░░░░░│ ░ │░░░░ │░ ░│ │░│░░░ ░───░░░░░░░░─┘
           ┌───────────   ──     •                     ───     ─┘── ────┘    ──   └───┘ └─┘ ───     ────
           │           ───  ────┐ ┌──────────┐─────────   ─────    •     ┌─┐─  ───     •   │   ──           │
           └───────────         │ │          │           │               │ │        │    │ │       │        │
                       ┌──────  └─┘┐──┐────┐ └───────────┘───────────────┘─┘    ─── │    │ │ ───   │        │
                       │░░░░░░• ░░ │░ │░ ░░│                                ────   ─┘────┘─ •   ─── ────────
                       └┐ • │             • ┌┐ ┌── │
                        │   │  ───       •  └┘ │  ─┘
                        │░░ ░┌─   ───────  ─┘   ──
                         ────┘
                                ──┐────┐─┐──┐───┐ ──┐──────┐───┐───────                  •
                            │     │▒▒░▒│░│░▒│░░░│   │▒░▒▒░░│▒▒▒│       ───────    ────┐   │
                            │ │   │   │        • ──  ──────┘───┘──────  ░░░░░░─── ░░░░│ │ │
                            │░│   │░░░│ ░░░░░░░  ░░░•                  ───────░▒▒│░───┘ │ │
                            │ │  ─┘───┘─────────────                          ───┘─     │ │
                            │ │                                                      │  │ │
                            │ │                      ────────────────────────────────┘  │ │
                            │ │   ┌──┐───────────────                                   │ │
                            │ │   │░░│ ░░░░░░ ░░░░░░                                    │ │
                            │ │   │░░   •░•  •      •   ───   ──                        │ │
                            │ │   │░ │ │ • ──░────░░░┌─┐ ░░──░░░ ─┐─┐────┐─┐──┐─┐─┐     │ │
                            │ │   │░─┘ │░ •░ ░░ ░░┌─░│ └───░░▒───░│ │░░░ │░│ ░│ │░│     │ │
                            │ │   │▒░░░░ ░░░░ ░░▒┌┘        ──    • • ────┘─┘──┘─┘─┘     │ │
                            │ │   └──────────────┘                                      │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │  ┌───                                                   │ │
                            │ │  │░░  •    ───     •                   ─┐─────── ────── │ │
                            │ │  └───  ┌──    ─┐─┐  ────── ───┐─ ────   │       │       │ │
                            │ │        │░░ ─┐  │░└┐─  ░▒░░░ ░░│▒│  ░░┌─┐┘ ───── └──     │ │
                            │    ──░┌─ └──░░│  │ ░│   ───░• ┌─┘─┘ ─┐─┘░│  ░░░░  │      •  │
                             ──     │       │      •        │      │   │  ────  └─┐──── ┌─
                               •  ░░   ░ ░░   ░ ░░ ░ │ ░░ ░ ░░░░   │ ░░      ░    │░░  ─┘
                                ──── ──░─────── ── • └─── • ─────░ │ ───░──░ • ── │ • •
                                                         •                       •
                  ┌─┐ ┌───┐──┐──┐─  ┌─┐──   ┌──┐ ┌──┐ │   ┌─┐ ┌────┐───────┐─────  ┌──┐────┐
                  │░│ │░░░│ ░│░ │░░ │ │░░░│ │░░│ │░░│ │░░ │░│ │░ ░ │░░░░░░ │░░░    │░ │░ ░░│
                  └─ • ─┐ │  │  │   └┐ ┌─ └─ ──    • •    └┐┘            ┌─    ────┘──┘ ── └─┐──────┐
                    │░│ │░│ ░│░░│░░░░│░│░   ░░ ░ ░• •░│ ░ ░│ │░ ░░░ ░ ░░ │░░░░░░ ░ ░░░░ ░ •░░│ ░ ░░░│
                    └─┘ │   •    ──     ─┐─┐───┐─┐   ┌┘┐ ┌─ ─┘      ─┐   │  ┌─┐     ──┐    ── •  │  └─┐
                        │ ░• •░░ ░░  ░░░░│ │░░░│ │░ ░│ │░│ •░░░  ░ •░│ ░░░░░│ │░░░░░  │░ ░│  │░│ │░ ░ │
                       │                   │  │                      │ │ ─┐ └─┘    ┌── ─┐ └──┘ └┐┘   ─┼─────┐
                       └─────░┌──░──────░░░ ░░└───░ ░──░░░────░ ─────░ │░ │░│ │░░░░│░░• │░░░░ │░│ ░░░░│ ░ ░░│
                       │░ ░░░─┘ ░•░░░░░░────── ░░░───░░───░░░░──░░░░░──┘─ └─┘ └──  └──   ───  └─┘─────┘─────┘
                    ┌─  │                                                │   •   ──   ┌──   ──
                    │░│ │░│ ░• ░░░░░░ ░ ░░ ░░░░░ ░░ │░ │░░░░ │░ ░ │ ░ │░ │░░│    ░░•  │░░ ░░░░     ░│
                    └─┘ │ │ •      •               ─┼─ │     │ •  └─┐ └─┐ │ │  ──    ─┘──  • ──     └┐─
                        │░░• •░░░░│ •░ ░░   ░░ ░░░░░│ •░░ ░░  │░░░  │░░░│ │░░░│  •░ │░ ░░ ░ │░░• ░░ ░│
                       │          │                           │   ┌─┘ ─┐┘  ── │ •   │ ┌─  ┌─┘ •       ┌─┐──┐─
                       └─────░┌─┐░└──────░░░░•░────░ ───┐░░░░ │░░░│ ░░░│ ░ ░ ░│ ░│ •░░│ ░ │░░│ •░░░░│ │░│ ░│
                        ░░░░░─┘ └─░░░░░░ ────░• ░░░──░ ░└──   └──    ──    •    ─┘   ─┘    ──┘    ──┘─   ──┘─
                       │                                   ──┐   ┌──┐  ───┐ ┌──┐  ─┐─  ─┐─┐   ┌───    ┌─┐
                       │░░░░░░│    ┌─░──░░ ░░ ───░──░░│  ░░░░│   │░░│░ ░░░│ │░░│ ░░│░│ ░│░│ │ │░░░│ ░ │░│
                       └──────┘──  │ • ░────── ░ ░░░──┘ ─────┘── └──┘─────┘─┘──┘───┘─┘──┘─┘─┘─┘───┘───┘─┘
                                    •  •               •        │
                                          │  │ │ ░ ░ •░  ░  │ ░ │░░│
                       ┌──────┐──┐  ── ───┘─ │ └─   •       └─     └─────┐─┐──────┐─┐────┐───┐──┐─┐─┐─┐───┐
                       │░░░░░░│ ░│ │ ░•░ ░░░░ • ░░   ░   ░░░░░ ░░ ░░░ ░ ░│ │░░░░░ │ │░░░░│ ░ │░░│ │░│ │░░░│
                       └──────┘──┘ │ ░░ ──┐───░──── ─────────────────────┘─┘──────┘─┘────┘───┘──┘─┘─┘─┘───┘
                                     ───  │        •
                                          │  │ │░░ ░░░ ░   ░░  │
                                            ─┘─┘───────── ─────┘
                                         •░
                                             │     ░ ░  ───┐
                       ┌─────┐───┐  ──────── │             └───┐─────┐─────┐───┐─────┐────────┐─┐──  ───┐
                       │░░░░ │░ ░│ │ ░ ░░░░░░ ░──    ░░░ │ ░░░ │░  ░░│ ░░░ │░░░│ ░░░ │░ ░░  ░░│ │░ ─┐ ░░│
                       └─────┘───┘ │    • ────   ─┐──────┘───      ──   •  │  •  ──    ──    ─┘ │   └───┘
                                   └───  │        │              •   ──   •    ──   •     ───   │ ──┘
                                         │   │           ░     ┌─                    ────
                                          ───┘─────────────────┘









```

*Figure from page 6 (2346x3317 px)*


---



4203-E P-310



SECTION 3 DATA INPUT/OUTPUT OPERATION



Example 4: The following command copies MAIN files (files without their extension names)



from FD0: (MS-DOS) to MD1: (OSP).



>CO FD0:MAIN,MD1:



When this command is used "MIN" is automatically appended as the extension name



of the destination file, so that the file name is MAIN.MIN.



Example 5: The following command copies A.MIN of MD1: {OSP) to FOO: (MS-DOS) under



the name "B.MIN".



>CO MD1:A.MIN,FD0:B.MIN



Example 6: The following command copies A.MIN of MD1: (OSP) to FOO (MS-DOS) under



the name "C.MIN" under the directory "PATH".



>CO MD1 :A.MIN,FD0:PATH\C.MIN



Example 7: The following command copies A.MIN of MD1: (OSP) to FD0: (MS-DOS) under



the same file name as it had in the copying source.



>CO MD1:A.MIN,FD0:



Example 8: The following command copies all files whose file names start with "A" in MD1:



(OSP) to the directory "PATH" of FD0: (MS-DOS).



>CO MD1 :A*,FD0:PATH



(3) Press the WRITE key.



[Supplement]



WRITE


## 1. The COPY function can only be used to copy between the OSP format and

MS-DOS format. Attempts to copy from OSP to OSP or from MS-DOS to MS-DOS



will result in an error.


## 2. This function has no default device name and it is therefore essential to specify the

device name.


## 3. If no destination file name is specified it is made the same as the source file name.


## 4. Contiguous OSP format files cannot be overwritten. If an attempt is made to do this

the message "file attribute unsame" is displayed.


## 5. If the specified destination file name already exists, the message "file exist

overwrite? (Y/N)" will be displayed. To overwrite the file, enter "Y'; to abort the



writing operation, enter "N".


## 6. If the copied file name contains any characters other than those listed below, these

characters will all be replaced by question marks:



Space,!,",#,$,%,&,',(,),+,-,.,/, Oto 9, :, ;, <, =, >, ?,@,AtoZ, [, \,], ",_, atoz, [,



I, 1, -


```text


                                                                                               ──
                                                               ┌─────┐─┐───┐───┐─┐─────┐────── ░░───────────
                                                               │░░░░░│░│ ░ │░░░│ │░░░  │░  ░░ ░──░░░░░░░░░░
          ┌────────────       ─────       ──────────── ───────   •    ─┘   └───┘─┘───  └───────     ──
          │            ───────     ───────            •       ┌── ────  ┌──          ──        •           │
          └───────────┐░        │ │░                          │       │ │                             ─┐───┘
                      └─────────┘ │    │  │  ───    ░   ┌─░      ░│ • │ └─ │ │    ┌── │           │░   │
                                  │░░░ └──┘ •░░ ────────┘░─┐── ░░░└─ ─┘─  ─┘─┘────┘  ─┘───────────┘────┘
                                  │  •                     │   ───
                                   ──   ┌──  ─────────────┐┘┐──                     ────────── ───    •
                                  │░░───┘  ──             │ │░░ ─┐──────────────────          •    ──  • ──┐
                                  │░ ░░ │░░░░░ ───┐░│  ░ ─┘  ░  ░│ ░░░    ░░░░░░░░░  ── ──     ── •     •  │
                      ┌─────────┐ │     │         │ └─     •    • •     •  •     ──    │  ──┐──  •   ──   •
                      │░░░░░░░░░│ │░ ░ ░░░░░░░• ░░ ░░ ░ ░░ ░░░ ░░░░░ ░ ░▒┌─ •░░░│    │░│ │░░│ ░░│░│ ░ ░│
                      └─────────┘ │░──────────░░─┐───────────────────────┘   ───┘────┘─┘─┘──┘───┘─┘────┘─
                                   •          │  │
                                              │░│      • ░        │
                      ┌─────────┐─┐─ ──┐─────   │ ───             └── ──── ─┐─┐─┐──────┐─┐─┐─┐───┐─────┐
                      │░ ░░░░░ ░│ │░│  │░░░░░░ ─┘ ░░░░░ ░░░░░░  ░░░░ ░ ░░   │░│░│ ░  ░░│ │░│ │░░░│  ░░░│
                      └─────────┘ │ └─ └──────░░└─────────────────────  ── ─┘─┘─┘──────┘─┘─┘─┘───┘─────┘
                                  └─          │
                                              │░│ │  ░   ░           │  │
                      ┌──────┐──┐   ───────     └─┘───          ───┐─┘ ─┘─ ─┐───┐────────┐──┐───┐─┐─┐───┐
                      │░ ░░░░│  │ ┌─░  ░░░░  ░ ░░ ░░░   ░░░ ░░ ░░░░│ ░ ░░░• │░░░│ ░ ░░░░ │░░│ ░░│░│ │░░░│
                      └──────┘──┘ │ ░ │ ──────────────────────░ ──┐┘    •   └───┘────────┘──┘───┘─┘─┘───┘
                                   •  └─                      ──  │ ────  ──
                                         │  │ ░░   ░ ░ ░   ░│
                      ┌──────┐──┐─    ───┘─ │            ── └─ ──────  ──── ─┐─┐───┐─┐──┐─┐─┐─┐────┐──┐─
                      │░░░░░░│ ░│ ┌───░░░░░░░░ ░░  ░░ ░ •░░░░ •░ ░░░ ──░░░ │░│ │░ ░│ │░░│ │░│ │░   │░░│
                      └──────┘──┘ │ ░░░─────┐── ────┐───░──── ░  ─── ░░ ── └─┘ └───┘─┘──┘─┘─┘─┘────┘──┘─
                                    ───     │       │                ───  •
                                         • ░│ │░│  ░│ │ ░   ░
                 ┌─┐─┐───────┐─┐─┐─┐─┐──  ──┘─┘─┘───  └────┐────
                 │░│ │░ ░░░ ░│ │░│ │░│                     │
                 └─┘─┘───────┘─┘─┘─┘─┘───          │ │     │
                                                   │ └┐─┐──┘
                                                   │  │░│  │
                                                   │ ─┘ └─ │
                                                    │░░  ░ │
                                                    └──────┘

                ┌──────────┐                      ──        ──      ───     ──   ─────       ──   •  •   •
                │░░░░░░ ░░░│       ┌──────────────░░────────░░──────░░░────░░░───░░░░░───────░░───░──░┌──░┌┐
                └──────────┘       │░░░░░░░░░ ░ ░░• ░░░░░░░░──░░░░ ░░• ░░░░ ──░░░──── ░  ░░ ░░•░ ░ ░░░│░░ └┘
                                   └─────────────  ───── ───  ─────    ────   ───      •   •    ── ─── ───
                                   │
                               ┌─┐ │                  ────────────────────────────────────────────┐────────┐
                               │ │  ┌───   │ ─┐  ░       ░   ░      ░ ░ ░      ░░░      ░░░   ░   │░░  ░  ░│
                               │ │  │░ ░───┘─░└┐ •                      •       •       •  • ──   │  •     │
                               └─┘ │           └┐ ┌──────┐───┐─────┐──── ┌──┐──┐ ┌────── ─┐ •  ─── ─┐ ┌───┐
                               │░│ │░ ░ ░░░░ ░░░│ │░  ░░░│ ░ │░░░░░│ ░ ░ │░░│ ░│ │░░ ░ ░ ░│ ░  ░░░ ░│ │░░░│
                               │ │ │                                           │ └──      │        ─┘ └─  │
                               │░│ └┐ ░░░───── ░░░ ░░────░░░ ──┐──░ ░─┐─────░│░  │ ░ │░░ ░ ░  ░ ░░░   ░ ░ │
                               └─┘ └┘ ───     ┌─── •      ┌─   │  ──  │      └───┘───┘────────────────────┘
                                   │        ──┘           │    └─     └┐───  │
                               ┌─┐ │          └─             │ │   •   │     │  ───┐ ───    ─────┐   │  ──
                               │ │ │  ───────   ─┐─ ┌──── ───┘─┘──  ░░─┘░ •░─┘──░░░└─  ░───░░░░░░└─┐─┼──░░│
                               └─┘  │░░░░░░░    ░│  │░ ░░ ░░░░░░░░░──░ └─░░•░ ░ ─── ░░• ░░░──────┘ │░│░ ──┘
                                   ┌┘────────────┘──┘────┐────────   •   ── ───     ──  ───       ─┘─ •
                               ┌─┐ │                     │                                  •
                               │ │ └────────┐ ┌─────     └─  •   •                       •          ──┐ ──┐
                               └─┘ │        │ │        ┌─         ───      •   ┌─────────  ────────   │   │
                                   │  ░ ░ ░ │ ░  ░┌─░  │░ ░░░• ░  ░░░░ ┌──┐░ ░┌┘
                                   │   ─────┘    ─┘ ─┐─┼───── ─────────┘  └───┘ ── ───────────┐─┐   ────── │
                                   │ ░│     │   •    │ │               │  │         ░   ░     │░│          │
                                   └──┘───   ───  ───  └───────────────┘──┘───────────────────┘─┘──────────┘
















```

*Figure from page 7 (2346x3317 px)*


---


## NOTICE

4203-E P-311



SECTION 3 DATA INPUT/OUTPUT OPERATION



(1) Copying from OSP format to MS-DOS format is possible for ASCII data files but if this



operation is attempted with a binary data file the message "file attribute unsame" is



displayed and the copying operation is terminated.



Both ASCII data files and binary data files can be copied from MS-DOS format to OSP



format, but binary data files may not be copied accurately.



(2) When copying from MS-DOS format to OSP format, if the MS-DOS file has no extension



name, "MIN" is automatically appended to the OSP file name as a default. Similarly,



when copying from OSP format to MS-DOS format, the extension name for the MS-DOS



file will be "MIN" if no extension name is specified.



(3) The following option can be specified. It must be preceded by a semicolon";".



;V Specifies use of the following request for confirmation for each of the files specified



for copying:



copy OK? (Y/N)



To copy the file, enter "Y"; to abort the copying operation, enter "N".



1-6. RENAME (renaming)



This function is used to change the name of an MS-DOS format file. The operating procedure is indicated



below.



(1) Press function key [F3] (RENAME).


#### MSDS

DIR


#### COPV ] RENAt.E

DELETE



FREE



PROTECT



@)@@®@@@]@]



\ Press [F3J (RENAME).


```text


                                                                                                ───
                                                                ┌─────┐─┐───┐───┐─┐─────┐────── ░░░─────────┐
                                                                │░░░░░│░│ ░ │░░░│ │░░░░ │░░░░░░ ───░░░░░░░░░│
                        •                                        ──   └─┘       │ └──
          ┌──────────┐── ────┐─────────────────────────────┐─┐──┐  ───   ─────── •   ─┐──┐──────── ───────  │
          │░ ░░░░░░░░│ ░    ░│    ░░░░      ░░░░ ░░░ ░   ░░│ │░░│ ░           ░       │░░│      ░           │
          │  •░───░░░│ │  ┌──┘─┐           ──    •    ─┐ ┌─    │  ───  │     │   ───┐ │ │  •  ░     ░░      │
          │   •   ───  │  │    └┐░░░░░░│ ░•░░░░░░░░░ ░░│ │ ░░░░│ │░░░ ░│ ░ ░ │░░░░░░│ │░│ │░░░ ░┌──░░░░░░ •░│
                        │ │    └┘───┐──┘──░ ───────────┘ ░─────┘─┘───┐─┘────  ──────┘     └─────┘   ────     │
                        │ │    │    │                                │               • ┌──       ───    ┌──  │
                        │ │    │░ ░ ░░░░░•░░░ ░░░• ░░░░░ ░   ░░░ ░░░─┘░░ ░░  ░░░• ░  ░ │░░░░░░ ░ ░░░░ ░ │░░  │
                        │ │    └────────░ ░──────░ ────────────────  └─┐───  • ░    •  └──  ── ──────── └──  │
                        │  ┌─┐ │                  •                 •  │          ── ──   ──  •        •     │
                        │  │░│ │░░░• ░░──┐░░ ░░  │░──░│░│░ ░░░░   ░░░ ░  │░──░  ░ ░░  ░ ░ ░░ •░│   ── ░      │
                        │  └─┘ └─── ─── ░└──     │    │ │          ┌┐ ┌─ │ ░  •   •        •   │             │
                        │ │                  ──    ░    └──────┐── └┘ │      •  ──   ───  • •    ── │     ░  │
                        │ │    │░░░░──░░░ ──░░░   ░░ ░░ ░░ ░ ░░│ ░  ░ ░ ░░░ ░░░ ░░░ ░░░░ ░░ ░ ░░  ░ │░░░░░░░
                        │ │    └────░ ───┐░░──────┐────────────┘──────────── •  ──────── ──── ──────┘──────┐ │
                        │  ┌─┐ │         │        │                         • ──        •    •             │ │
                        │  │░│ │░░  ░░░░░│░ │░░░░ │░ │░ ░░░░░░░░│   •░░░░• ░ ░░░░░│ ░│ ░ ░░ ░░░░•  │       │ │
                        │ ┌┘─┘─┼──          │     │  │      ┌─  └───    • •   ── ─┘  │ ── •      ─┐┘┐──────┘ │
                        │ │    │░  │░ ░░░░┌─┘░░ ░ │░ │░░░░░░│ │░ ░░░ ░  ░░░│ │░░│  ░│ │░░│ ░  ░ │░│ │░░░░░░░ │
                        │ │    └── └────┐─┘ ░──   └──┘──────┘─┘────────────┘─┘──┘───┘─┘──┘──────┘─┘─┘──────┐─┘
                        │ │        │    │      ┌─┐                                                         │ │
                        │ │        │░░• │░░• •░│░│                                                         │ │
                        │ │        └──      •   • ────────────────────────────────────────────             │ │
                        │         ┌┘  ░░░│ ░░ ░░  ░ ░░     ░ ░░░  ░░  ░░░ ░░ ░░░ ░░░░   ░░  ░░             │ │
            ┌──    ┌────┘───┐──┐──┘┘┐    └────────────────────────────────────────────────────             └─┘
            │░░    │░░ ░░░░░│  │░  ░│ ░┌─┘
           ─┘──   • •  ─────┘  └─ ──┼─ │░└────────────────────────────────  ──
                 •   ░         │    │    │                 ░              │   ──────────────────────────────
                •     ┌────────┘────┘────┘────────────────────────────────┘ ──           ░
                 │ • ┌┘                                                       ──────────────────────────────
                 └┐ ┌┘ ────┐──────┐─┐───────────────┐─
                  │ │   ░░░│ ░░░░░│ │░░░  ░ ░░░░░░░░│
                  └─┘─ ─┐─┐┘──────┘─┘───────────────┘─                                      ┌─┐
                        │ │                                                                 │ │
                        │ │                                                                 │ │
                        │ │  ┌───                                                           │ │
                        │ │  │░░░───┐─     ─┐      • ───── ─┐── ─┐─ ───── ─┐─────┐─┐──────┐ │ │
                        │ │  └───   │     • │     • •     • │    │ │     │ │     │ │      │ │ │
                        │ │       │   ┌──    ┌───┐   ────  ░│ ──┐  └┐────┘   ─┐─┐┘ │  ──── ─┘ │
                        │  ──┐  │ │ ─┐┘░ •   │░░░│  │░░░ •   •░░│ • │░░░░  ─┐░│░│  │      •   │
                         ─┐  │  └─ │ │    •  └─┐ │  └─      •       │       │   │   ───┐─   ┌─
                          └─┐      │ │ ░░      │░ │ │ ┌─      │░   │ ──┐ │ • ░   ─── ░░│ ┌──┘
                            │░ ░│  ░ ░ ─┐─ •░  │░ └─┘ │ • ░   │░   │   │ │   ┌┐─ ░  ░ ░│ │
                            └───┘  ───  │   ───┘░┌┘ └─   •  ┌─   ─┐  ──┘─┘── └┘  ┌─────┘ │
                                 ──   •        └─┘   ░░ ░ ░ │░░░░░│ •       •  ──┘
                                                  ──────────┘─────┘─

































```

*Figure from page 8 (2346x3317 px)*


---



4203-E P-312



SECTION 3 DATA INPUT/OUTPUT OPERATION



The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.



MS-DOS CONVERTER: RENAME



PROGRAM OPERATION


#### MS-OOS CONVERTER: RENAME

All]



INDEX DISPLAY PROCEDURE



[F2] - MD1 :*. *



[F3]



FOO:*.*



MS-OOS CONVERT



197/07/15 14:10:00



OVERWRITE



TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl] ,



INPUT THE DEV IC E NAME ANO FI LE NAME, THEN PRESS [WR I TE] KEY.


#### DEFAULT DEVICE NAME =


#### DEFAULT FILE NME = *. *

>XR



1,01 : FOO: COMMAND OVERWR/ CHAR.



INDEX INDEX INDEX HI STORY INSERT DELETE CANCEL



(2) Enter the file name (including the device name and path name) of the MS-DOS format file



whose name is to be changed and the file name {not including the device name and path name)



that it is to be changed to.



Example: The following command changes the file name FD0:PATH\PATH1\FILE to the file



name FD0:PATH\:PATH1 :FILE,.



>R FD0:PATH\PATH1\FILE,FILE1



(3) Press the WRITE key.



[Supplement]


#### WRITE


## 1. If the specified file (currentfile name) does not exist in the floppy disk, the message

"no file" is displayed on the console lines and the renaming operation is terminated.


## 2. If a file with the same name as that specified for the file after the change already

exists in the floppy disk, the message "file exist" is displayed on the console lines



and the renaming operation is terminated.


## 3. The wild cards"*" and "?" cannot be used in the file names (their use will cause an

error).


## 4. Specify only the file name (with no device name or path name) for the file name

after the change. An error will occur if a device name or path name is specified.


## 5. If the specified file is a directory, the message "directory" is displayed on the

console lines and the renaming operation is terminated.


```text


                                                                                               ───
                                                               ┌───────┐───┐───┐─┐─┐─┐─┐──┐─┐──░░░─────────┐
                                                               │░░░░ ░░│ ░ │░░░│ │░│░│ │░ │░│ ░───░░░░░░░░░│
          ┌───────────   ───    •   ──  ────          ───     ─┘──── ──┘   └───┘ └─┘─┘ └──┘─┘──
          │           ───   ───┐ ┌──  ─┐    ──────────   ─────      •   │       •     •        •           │
          └──────────┐░        │ │     │  ┌─          │                 │ │             │ │ │     │        │
                     │  ─────  └─┘ ──┐─┘──┘ ──────────┘ │    ────┐   ───┘ │   │ •  ┌┐   │ └┐┘──   │     ░  │
                      │░░░░░░░ ░  •░ │░░░░│           └─┘────    └───    • ───┘─  ─┘┘─── ─┘┘   ─── ────────┘
                      └─   •               ┌┐ ────────
                         ─┐ ──┐────   ─────┘┘      ░░
                       ─┐░└─  │    •           ───────
                        └─┘    •                                  ────  ───────────── ──
                                ─┐────┐───────┐─    ──────────────    ┌─             •  •
                           │  │  │░░░░│ ░░░░░░│      ░░░░░ ░░░░░░     │      • ────   •  │
                           │  │  │  ░░ ░░░░░░░  ░░░░ ────────────     │░    ░░░▒░░░│   │ │
                           │  │  │░░░• ──────────────            ─────┘────────────┘   │░│
                           │  │  └───                                               │  │░│
                           │  │ •                                                   │  └─┘
                           │  │      •      ───────┐                  ──────────────┘ •  │
                           │ │ • ┌──┐ ─┐─┐── ░    ░│                                   │ │
                           │ │   │░░│  │░│    ─────┘                                   │ │
                           │ │   │░░    ─┘   │         ───   ──                        │ │
                           │ │   │░ ░░│ ░ ░•░│ ──░░─┐─░ ░░ •░░░┌── ───┐ ┌────┐───┐     │ │
                           │ │   └─┐░ │░ ░░░░░•▒▒┌─░│ ────░░───┘░░ ░░░│ │░░ ░│ ░░│     │ │
                           │ │   │▒│░ │ ░ ░░ ░░┌─┘ ─┘      •    ─── ──┘ └────┘───┘     │ │
                           └─┘   └─┘── ────────┘                                       │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │  ┌──                                                    │ │
                           │ │  │  ┌──      ── •          •             • ──  ─┐────── │░│
                           │ │  │  │  ┌─────  │ ─┐──────── ────┐────┐┐── •   • │       │░│
                           │ └─  ┌─┘  │░░░   ─┘░ │   ░▒░░░  ░░░│ ░ ░└┘      │  │      ─┘ │
                           │    ┌┘ └─   │ • • │  └┐  ───── ┌───┘  │░│ •     └─ │
                            ── ─┘  │ ───┘  │ ┌┘   │ │░  ░  │      │    •       └─┐───┐
                              •░ ░│   ░ │  │ │ │░ │ │  │ ░ │  │ ░ │░ │ ░       │ │░  │
                                 ─┘  ───┘──┘ └─┘──┘─┼──┘──┐┘──┘───┘──┘ ────────┘─┘───┘
                 ┌─┐─ ┌──┐────┐                     │     │                          └────────────┐─┐
                 │░│ ┌┘░░│ ░  └─┐─┐─ ───────────░ ──░░░░──░░░───░░──░░░───░░────░ ░ ░░ ░░░░ ░░ ░░ │░│
                 └─┘ └┘░        │ │ •         ░ •   ────░  ──   ─┐  ──    •     •   ───┐    •       │ ─────
                     │          │     ──     ─── ───    ──    ── └──   ─── ────  ──    └── • ── ────
                     │ ░░       ░   ░ ░░•  ░                                                            ──
                     │       ┌──┐            ──── ─── ──────────────────────────────────────────────────
                     └──     │  └───  ░   ░•     •░  •    ░    ░        ░                          ░  ░
                        ─────   │░░░░──────░•   ░░─┐  ─── ──       ─────── ────── ──── ─────────────────
                                └────              │         ┌────┐
                                        ─┐░░░ ░  ░░░ ░░   ░ ░│ ░░░│
                 ──┐──────┐─┐────────  • └─────────┐ ┌───┐─┐─┘────┘
                 ░ │   ░░░│ │░ ░░   ░ │░│          │ │   │ │
                 ──┘─ ────┘─┘─────────┘─┘          │ └┐─┐┘ │
                                                   │  │░│  │
                                                    ┌─┘  • │
                                                    │░░  ░ │
                                                    └─── •
                ───────────┐   ┌─┐   •   ──── •  •          •  ──     •     ───     • ────  ──  ┌─   ─────
                ░░░░░░░ ░░░│   │ │ ┌┐ •░•░░░ ░░──░───░░ ░░ ░░──░ ────░░─────░░░────░░•░░░░──░░░─┘░───░░░░░│
                ───────────┘   │ │ └┘░ •░─────░░░░░░░──────── ░──░ ░░──░░░░░───░░░░•░░────░░──  │░░ ░░──░─┘
                               └─┘ │                                                                      │
                               │░│ │░────  ────── ─────────┐─┐── ──────┐─────┐ ┌───── ──┐ ░  ─────── ──┐──┘
                               └─┘ │           ░           │ │        ░│     │ │        │           •  │  │
                                   └┐        ─── ░ ░    ── │  ░  ░░░   │  ░ ─┘─  •░░ ░░░│ ░   ░    ░ ░ │░░│
                                   └┘─┐─┐─ ──░░░─────░┌─░░─┘ ░──────░░░└───          ──             •   •
                               ┌─┐ │  │ │             │  •                 ┌───┐─┐───  ┌───┐──┐─┐─── ──┐ ─┐
                               │░│  │░└─░░│ │░ ░│   │░░│ ░ │░░░ ░░│ │░░    │░ ░│ │░░ ░░│░░░│ ░│ │░░ ░ ░│ ░│
                               └─┘  └─  ──┘─┘───┘───┘──┘───┘──────┘─┘──────┘───┘─┘─────┘───┘──┘─┘──────┘──┘
                                   •
                               ┌─┐  ┌─ • │ ──   • ─── ────── ──┐   ─── •     •     ───   ──    ──┐       ─┐
                               │ │  │░│  └─  ─── │  ░│ ░       └───     ────   ────   ┌─  ░───┐  └──────  │
                               │ │  └─┘── ░ • ░ ─┘───┘─────────░░░  ────░░ ░──░░░░░── │░░──░░░│ • ░░░░░░──┘
                               └─┘ │                                                    •                 └┐
                               │░│ │░─────░░──░░░──┐─ ────┐─░░░ ░──────░░░░░░░──┐─┐░░  │ │░ │░░░░░░│  ░ │░░│
                               └─┘ └─    ░──  ──   │░     │ ────        ──────  │ └────┘─┘──┘──────┘────┘──┘
                                     •  ──      ──  ── ───      ─── ────       • •









```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-313



SECTION 3 DATA INPUT/OUTPUT OPERATION



1-7. DELETE (delete)



This function is used to delete MS-DOS format files.



The operating procedure is indicated below.



(1) Press function key [F4] (DELETE).



a=MSOS



DIR



COPY



RENAME



DELETE



FREE



PROTECT



OU l T



Press [F4) (DELETE).



The screen changes to the directory-selection-



based file operation screen and the following is displayed on the screen.



MS-DOS CONVERTER: DELETE



DEL


#### PROGRAM OPERATION MS-DOS CONVERT

I 97/07/15 14:J0:Q0



, I c:M:



DELETE 0VERml TE



DEL[IJ



INDEX DISPLAY PR:JCEDURE



[F2] - MDT:•.*



(F3} - FDO:*.*



TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl] ,



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS [WRITE) KEY.


#### DEFAULT DEVICE NAME =

DEFAULT FILE NAME~ *.*



>XDEL



l,lll: FOO: COMMAND OVERWR/ CHAR.



IM lEX INDEX Ir-DEX Hl STORY INSERT DELETE CANCEL



(2) Enter the file name (including the device name and path name) of the MS-DOS format file that



is to be deleted.



Example 1: The following command deletes the file FILE.MIN in device "FOO:".



>DEL FDO:FILE.MIN



Example 2: The following command deletes the file FILE2.MIN in the directory "PATH" of



device "FOO:".



>DEL FD0:PATH\FILE2.MIN


```text


                                                                                                • •
                                                                ┌─┐─────┐─┐─┐───┐─┐─────┐────── ░░░──────────
                                                                │░│░░░░░│ │ │░░░│ │░░░░ │░ ░░░  ───░░░░░░░░░
            ┌───────         •       ───────────────────────────┘─┘─────┘─┘ └───┘─┘─────┘───────      ──
           ┌┘       ────────┐  ─┐────
           │   ┌──┐  ░      │ │ │     ──────
           └───┘  │ ────────┘ └┐░ ░ ░│
                 │             │  ┌──┘ ───────┐────┐─┐────────┐
                 │    ┌── ───  │ ─┘  │ ░ ░░   │    │ │░  ░  ░░│
                 │    │         •                ──    ┌──────┘
                 └┐  ─┘           ──┐─         ┌─      │
                  │   │             │ ┌───     │     ──
                  │ •  •              │ ░ ░ ░ ░   •░│
                   •    ┌─┐───────────┘─────────── ─┘
                        │ │                                                                 ┌─┐
                        │░│                                                                 │ │
                        │░│                                                                 │ │
                        │░│   ─────────────┐┐─────┐─────── ─────── ───────  ─────┐─ ──────┐ │ │
                        │░│    ░░░         └┘     │       │               ──     │ │      │ │ │
                        │ │  │   ──┐  ┌──┐   ─────   ─────┘   ──┐  ───────   │   │ │ ─────  │ │
                        │  • └┐─   │  │░░│   ░░░░▒   ░░░░░    ░▒│  ░░░░░░░   └───┘ │      ──┘ │
                         •    │   •   │  │   ──────  ──  •    ┌─┘  ──── ───         •   •    •
                          ──    ─┐ ──  ┌─┘             ──   │ │ │ │    │           •  ─┐ │ ──
                            │  │░│     │░│ ░   ░░  ░  │░░   │ │░│ │   ─┘─  ░ ░ ░ ░ ░ ░░│ └┐
                            └──┘─┘ ┌───┘─┘ ─────── ───┘┐─  ┌┘─  └┐  •  ░   • ─────── ──┘ └┘
                                  ─┘      •       •    │   │ ░░ ░│ │░░    │ •       •   •
                                                            ─────┘─┘──────┘
                           ──  •      • •     ─┐─────   ──
                       ┌───░ •░░──────░░░────┐ │░░░░░•░ ░░░░░ ───┐──────┐────┐──┐────┐─
                       │░░░░•░░ ░░░ ░░░• ░░░░└─┘──── ░┌─░───── ░ │░░░░░░│  ░ │░ │ ░░░│
                       │         •          │         │       ───┘──────┘────┘──┘────┘─
                        │░░   ░░   ░░░░░░ ░░│ │░│ ░ ░│
                        │░───┐──────────────┘─┘─┘────┘
                         •   │                                        ────────
                                 ─┐────┐─┐──┐──┐─     ┌────┐─┐───┐────                  ──
                                  │░░░░│░│░░│░░│      │▒░░░│ │░░░│     ─────     • ───┐   │
                            │     │     ─┘  └─   ───── ────┘─┘───┘     ░░░░░┌───░░░ ░ │ │ │
                            │  │  ▒▒░▒│░▒▒▒▒░▒▒░░▒░░░░                 ─────┘░░▒░░░──   │ │
                            │  │  ────┘────────────────────────────────     └──────  │  │ │
                            │  │ │                                                   │  │ │
                            │  │ │                   ────────────────────────────────┘ │  │
                            │  │   ┌──── • ──────────                                └─┘  │
                            │ │    │▒░  •░│░  ░░░░░░                   ──────────────   │ │
                            │ │   │░░  │░▒│ ░░│     │                                   │ │
                            │ │   │░░• │ ─┘ ░░│ ────┘┐─┐─░────────┐────┐─┐─┐───┐─┐      │ │
                            │ │   │░░░ │░ ░░░░░•░▒░ ░│ │░░ ░░▒  ░▒│ ░░░│ │░│ ░ │░│      │ │
                            │ │   │░░░░  ░░ ░ ░░▒─── └─ ──────  ──┘────┘─┘─┘───┘─┘      │ │
                            │ │   └───────── │░──    │                                  │ │
                            │ │             ─┘─    ──┘                                  │ │
                            │ │                                                         │ │
                            │ │                                                         │ │
                            │ │   ───                                                   │ │
                            │ │  •░░░ •     •     ──                   ───────   ─────┐ │ │
                            │ │   ───  ┌──   ──┐─┐   ───────────┐────┐        ┌─┐     │ │ │
                            │ │        │▒░─┐─  │░└┐   ░░░░░ ░░░▒│ ░ ░└──┐ ┌───┘░│   ──  │ │
                                ┌─┐░┌─ └─░░│░  │░░│  ░───── ─┐──┘ ─┐─┘░░│ │░░░  │     ──  │
                             ── │ └┐┘      └─  │ ─┘          │     │   •  └─    └────┐   •
                               │  ░│   │ ░░   │  ░   │ •░    └─     │░     ░░     ░░ └┐──
                               └─ ░└─  │ ── • │  ░ ░ │  │ ── │    • │ • ── ───  ░ •░ └┘
                                 ──             •      ─┘     ──              ──   •
                  ┌─┐─ ───┐ ── •    ──┐ │  ───   ─┐─┐──  ──┐─    ─── ──┐─┐─ ─┐  ┌─  ┌─┐─┐──┐──┐─┐───┐──┐─┐
                  │░│ │  ░└─░░ ░───░░░│ │░░░░░░░ ░│ │░░░░░ │░░░ ░ ░ ░░░│ │░ ░│  │░│ │░│ │░░│ ░│ │░ ░│  │░│
                  └─┘ │  •  ░•░░░░  ┌─  └─────────┘ └───    ───  •  ───┘ │  ─┘ ─┘─┘─┘─┘ └──┘──┘─┘───┘──┘─┘
                      │          │  │ ┌─           •    ┌───   ─┐ ─┐    • ┌─  •        │
                      │░░░░ ░░  ┌┘┐░│ │░░░░ ░   ░░░ ░ │ │░░░░░ ░│ ░│ ░│ ░ │░│    ░     │░ ░│
                      └─────────┘ └─┘─┘   ┌─      ─── └─ ───────┘──┘──┘───┘─┘──────────┘───┘
                                      │░░░│ •░░ ░• ░ •░░•
                      ┌──────┐───     │           ─── ── ────┐──┐──┐──┐──┐─┐─┐─┐─┐─────────┐─┐──┐─┐──┐
                      │ ░░░░░│ ░  ┌─┐─░░░░•░░░  ░░░░░░░ │░░░░│ ░│ ░│ ░│ ░│ │░│ │ │ ░ ░ ░░░░│ │ ░│ │ ░│
                      └──────┘─── │░│ ░───░────  ────   └───   ─┘──┘──┘──┘─┘─┘─┘─┘─────────┘─┘──┘─┘──┘
                                   • •         ──    ───    ───
                                      │░ ░│ │ ░ ░░░  ░░░ ░  ░░░│
                                      └───┘─┘──────────────────┘









```

*Figure from page 10 (2346x3317 px)*


---



4203-E P-314



SECTION 3 DATA INPUT/OUTPUT OPERATION



Example 3: The following commands delete all files in the directory "PATH" of device "FD0:".



>DEL FD0:PATH\*·*



>DEL FD0:PATH



In this case, because a directory has been specified as the file name to be deleted, all



the files contained in that directory ("PATH"), except directories, wlll be deleted.



In order to make this clear, the request for confirmation "delete OK? (Y/N}" is displayed



on the console lines.



(3) Press the WRITE key.



[Supplement]


#### WRITE


## 1. The wild cards "*" and "?" can be used in the file name (wild cards cannot be used

in path names).


## 2. If no option is specified deletion is executed unconditionally (unless rt is a path

name that is specified for deletion).


## 3. Directories cannot be deleted.


## 4. Files protected by the file protection function cannot be deleted.


## 5. The following option can be specified. It must be preceded by a semicolon ";".

. ;V Specifies the use of a request for confirmation when an attempt is made to



delete a file.



To delete the file, enter "Y"; to abort the deleting operation, enter "N".



1-8. FREE (free)



This function displays the available capacity in an MS-DOS format floppy disk.



The operating procedure is indicated below.



(1) Press function key [F5] (FREE).



"FR" is displayed on the command line.



DIR COPY RENAfE DELETE FREE PROTECT QUIT



@@J@)@@@J@J@J



\ Press [F5] (FREE).



"FR" is displayed.


```text


                                                                                               ───
                                                               ┌──┐─┐────┐─┐─────┐─┐───┐───────░░░─────────┐
                                                               │░░│ │░ ░ │ │░░░░ │░│ ░ │░░ ░ ░░─── ░░░░░░░░│
          ────────────        ────           ──────    ──       ──┘ └─     │ ────┘─      ─── ──       •    │
                      ────────     ──────────      ────  ─────┐─  └┐  ──┐──┘─      ──────   │  •   ───     │
          ────────────         ┌──┐    ░                      │  ░ │   ░│                   │      ░    ───┘
                      ─────────┘  └───┐   │           ┌── ────┘────┘────┘──── ── ───────────┘    │ ─────
                                      │   │      ░    │  │                   •  •            ────┘
                                      │ ──┘───────────┘  │
                                      │                ──
                                        ──      ──
                                      │   •  •    ──┐     •    ─┐      ─────── •  •     ───  ───    ────────┐
                                 ┌───┐┘ ░░░──░░░░░░░└──░░•░────░│ ─────░░░░░░░░ ░•░─────░░ ── ░ ────░░░░░ ░░│
                                 │░░ │░░───░░░────┐─░░░──░•░░░ ░│ ░░░ ░───░ •░┌─░░░ ░ ░░░• ░░ ░  ░░░░───  ──┘
                                 │                │ •                         │                         ──
                                 └────░  ───░░  ░ │  ░░   ░  │░ ░░ ░│ │░ ░ ░░░ │  ░░░░░  ░• │  ░  ░ ░░░░░░░│
                                ┌┘░ ░ ───  ░────░░└──────────┘──────┘─┘────────┘────────── ─┘──────────────┘
                 ┌──  ────┐─────┘   │    ┌──    ──
                 │      ░░│  ░    ░ │ │░░│          ┌──    ─┐
                  ──   ───┘───────── ─┘──┘          │  ─┐ │ │
                                                    │ •░│ │ │
                                                     │      │
                                                     │░  │  │
                                                     │ ──┘  │
                                                          ──
                ┌───────────        ┌───────────┐────        ───── ──────────── ────  ───  ──
                │░         ░        │           │                           ░             •  ───      ──┐──┐
                └───────────       │        │   │  ─────────────────────────────────────── ──   ──────  │  │
                                   │  ────  │░──┘
                               ┌─┐ │                  ──   • •     ─┐──────┐─┐───────────┐─┐────┐───────┐──┐
                               │ │  ┌────░░░── ░───░░•░░• ░░•░────┐ │░░░ ░░│ │░░░ ░░░░░░░│ │░░░░│ ░ ░ ░ │░░│
                               └─┘  │░░░░ ──░ ──░░░──░──░───░░░░░░└─┘──────┘─┘───────────┘─┘────┘───────┘──┘
                                    │                          • •
                                    │░ ░ ░░          ░│ │░░░  │
                                    │                 │ │     └──────────     ── ───   ────
                                   •  ░     ░         │ │░    ░          ───┐─  •   ───    │
                                    │                •  │                   │              │           ─┐
                                    │     •      •  │              ── │   •   • │         │  ─────────  │
                                    └┐     ──┐───  ─┘ ───            ─┘    ─── ─┘ ░ ░     │ •         • └──┐
                                     └┐  │░  │ ░   ░│              │             ┌─┐                       │
                                      └─ │     ──   └──────────────┘─────────────┘ └────── ────────────────┘
                                          │░  • ░  ░│
                                          │ ─┐      │ ── ────┐     ─────   ───────────────────────
                                          │  │   ───┘        │ ───      ──         ░             ░  ──
          ┌─┐─┐   ┌──┐──┐─┐─┐──┐              ───       ─────      ─────   ───────────────────────
          │░│▒│   │░░│▒░│ │░│░░│
          └─┘─┘ ┌─┘──┘──   ─┘  └──┐──┐─────┐──┐─┐─────┐─────┐─┐─┐─────┐─┐───┐──┐─┐──┐
                │░░░  ░░░░│ │░░░░░│ ░│  ░░░│░░│ │░░░░░│ ░ ░ │░│ │░░░ ░│ │░░░│░░│ │░░│
                │ ── ──   └─┘     │ ─┘  ──  • └─ •    └─────┘─┘─┘─────┘─┘───┘──┘─┘──┘
                │   │░░░░░░░░░ ░░░│░░│ ░ ░•░ ░░░░ ░░░░│
                └┐ ┌┘┐    ┌──    ┌┘  │     │     ┌────┘
                 │ │ │░ ░░│ ░░░░░│ │░│ ░░░ │░░░░░│
                 └─┘ └── │   │   └─┘ │     └┐─── └┐─┐───┐
                     │░ ░│ ░ │░░░░░░│ ░ ░ ░ │░  │░│ │░ ░│
                     └─┐─┼───┘──────┘───────┘───┘─┘─┘───┘                                  ┌─┐
                       │ │                                                                 │ │
                       │ │                                                                 │ │
                       │ │   ┌───                                                          │ │
                       │ │ ┌─┘▒░░  ───────  ─────────────   ─────────────   ─────────────┐ │ │
                       │ │ │░░─┐─         ┌─             ┌──             ┌─┐             │ │ │
                       │ │  •  │  │  ┌──┐ │ ───── •    ┌─┘  ┌──┐  ┌────┐ │ │      ┌──────┘ │ │
                       │  │  │░│  │  │░░│  •░░░░▒•  │░─┘░   │░░│  │░░ ░└┐   │     │       ─┘ │
                        • │  │ └──┘  │   │  ┌─ ──   │    │      •  •    │   │ ─┐       •     │
                         │  ┌┘─┘  └──┘┐─┐┘──┘ •   ──┘ ─┐─┼─┐░┌─░ ──  ┌─  ───┘░░└────┐─┐ • ───
                         │  │     │ ░ │ │ ░    ░│    │ │ │ │ │░│ ░   │░│  ░ ░ │ ░ ░ │░│ ░│
                        ┌┘ ─┘  ── └── └─┘  •░ •░│ ── └─┘ └─┘ │░│ ────┘─┘ ── ──┘ ┌── └─┘ ─┘
                        │ │              ── ── ─┘─  •   •   ─┘─┘           •    │  •   •
                        │ └───────────                            │░░░░░░ ░ ░░░│
                        │  ░░ ░  ░░ ░░                         ───┘────────────┘
                        └──────────────












```

*Figure from page 11 (2346x3317 px)*


---



4203-E P-315



SECTION 3 DATA INPUT/OUTPUT OPERATION



(2) Enter the device name.



Example: The following command displays the available capacity of device "FD0:".



>FR FOO:



(3) Press the WRITE key.



WRITE



[Supplement] Never specify any more than a device name in the command.


```text


                                                                                                ──
                                                                ┌─────┐─┐───┐───┐─┐─┐────────── ░░──────────┐
                                                                │░░░░ │░│ ░ │░░░│ │░│ ░ ░░ ░░░░ ──░░░░░░░░ ░│
           ┌──────   •              ───  ───────────────────────┘─────┘─┘   └───┘─┘─┘───────────     ───
           │      ┌─┐ ┌───┐─────┐───   ──                                                                   │
           └──────┘ │ │░  │     │          │ •                   •        •                     ────────────┘
                  └─┘ │   └───  │    ───── └─ ─────────────────── ────────  ───── ──────────────
                      │░     ░┌─┘┐   ░ ░  ░               ░          ░     │
                      └───────┘  └─────┐       ┌───────────────────────────┘─────  ─────────────
                                       │░│ ░░░ │
                  ┌─┐─┐─────────┐──────  └─────┘      •
                  │░│ │░ ░░  ░  │░░  ░ │ │           •      •
                  └─┘ └─────────┘──────┘─┘─         │        │
                                                    │ ─┐─┐─┐ │
                                                    │  │░│ │ │
                                                    │ ─┘ └┐  │
                                                    │ ░░░ │  │
                                                     ─────┘──

                 ┌───────────┐   ┌───┐─┐─┐──┐─┐────────┐─┐───┐───┐─┐───────┐───────────┐
                 │░░░░░░ ░░░░│   │░░░│ │░│░░│ │ ░ ░  ░ │░│ ░ │░ ░│ │░░░░ ░ │░  ░░░░░░ ░│
                 └───────────┘   └───┘─┘─┘──┘─┘────────┘─┘───┘───┘─┘───────┘───────────┘




























































```

*Figure from page 12 (2346x3317 px)*


---



4203-E P-316



SECTION 3 DATA INPUT/OUTPUT OPERATION



1-9. PROTECT (protect)



This function establishes, and cancels, write protection for MS-DOS files (it is equivalent to the ATTRIB



function in MS-DOS).



When a file is protected it cannot be renamed, deleted, or overwritten by copying.



The operating procedure is indicated below.



(1) Press function key [F6] (PROTECT).



DlR



COPY



RENAME



DELETE



FREE



PROTECT



OU IT



@]@@@@@@)@



Press [F6] (PROTECT).\



The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.



MS-DOS CONVERTER: PROTECT



PROTif!I



I PROGRAM OPERATION



MS-DOS CONVERTER: PROTECT



PROTJII



INDEX DISPLAY Proel:DlRE



[F2] - MD1 :*. *



[F3] - FOO:*.*


#### MS-DOS CONVERT

I ~7/07/15 14:10:00



OVERl'IR IT E



TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl] ,



INPUT THE DEVICE NAME ANO FILE NAME, MN PRESS [WRITE] KEY.


#### DEFAULT DEV IC E NAA£ =

DEFAULT FILE NAME "'



*. *



t,01:



FOO:



COIIMAND



OVERWR/



CHAR.


# I I

INDEX IN OEX IN OEX HI STORY INSERT DELETE CANCEL


```text


                                                                                               ───
                                                               ┌─────┐─┐───┐───┐─┐─┐─┐─┐────── ░░░─────────┐
                                                               │░░░░░│░│ ░ │░░░│ │░│░│ │░ ░░░░░───░░░░░ ░░░│
               ───                    ─────────────────────────┘─────┘─┘─  └───┘─┘─┘─┘─┘───────     ──
          ┌───┐   ─────────┐─── ┌─────                                                                     │
          │  ░└─   ░░░     │ ░ ┌┘       ┌──────────────────────────────────────────────────────────────────┘
          └───┘  •  ─┐─────┘─  │    ░ ──┘
                     │               │  └──────────┐───────────────────────────┐──────┐─┐─┐──┐─────┐───────┐
                ─────┘     ──  ░     │             │░ ░ ░  ░░  ░              ░│      │░│ │░░│ ░   │ ░   ░░│
               •  ░░░░── •░░░──────                      •                   •         ─┘─┘──┘─────┘───────┘
                │       •          ─┐───────────────────┐ ┌────┐─┐──┐────┐──┐ ┌──┐─────
                │░ ░• ░ ░• ░ •░░──░░│  ░░ ░░░ ░░ ░░░░░░░│ │░░░░│ │░ │░░░░│░░│ │░ │░ ░░░│
                │ ──          ──   • │                ┌─┘─┘────┘─┘──┘────┘──┘─┘──┘─────┘
                └─  │░░  ────   ───  │     ░░░░░  ░ ░░│
                │   └┐  •    ───    ─┘               ┌┘
                 │ │ └┐ ░░░  ░░░░│ │░│ ░ ░ ░ ░░  ░   │
                 └─┘  └┐─┐───────┘─┘─┘───────────────┘
                       │ │                                                                 ┌─┐
                       │ │                                                                 │ │
                       │ │                                                                 │ │
                       │ │  ┌────┐── ────────────────────────────                          │ │
                       │ │  │░░░░│  •                                                      │ │
                       │ │  └────┘┐  ┌──┐  ─┐────            ──┐  ───┐  •         ┌──────  │ │
                       │  ──┘     │  │░░└─  │░░░▒   ────┐   •░░└┐ ░░░└──    ───   │      ──  │
                        •       ──┘  └─     └────       │    ┌─ │ ──       │   │  │   ──    ┌┘
                         ──   ┌─  │                   ─┐ │ ┌─┘   •   ┌─  ──┘░  └── ─┐─  • ──┘
                           │░ │ │ ░ ░ ░   ░    ░   ░ │░│ │ │ │░• ░   │░│  ░ ░   ░ │ │░│ ░│
                           └─ └─┘ ─── ─── ──  •░│ •  └─┘─┘ └─┼─      │░└──░ ──────┘ └─┘ ─┘
                             •   •   •   •  ── ─┘─ •         │       │░│  ──       •   •
                                                      ░░░────┘────░── •
                              •    ────    ──┐─┐────┐                   ┌─┐──────┐─┐────┐───┐─┐───┐─────┐──┐
                      ┌──────░░░•░ ░░░░──░  ░│ │░░░░│ ░ ░░░ ░ ░ │░░░│ │░│ │░░ ░░░│ │ ░░░│ ░ │ │░  │░░░ ░│ ░│
                      │░░░░░░──  ──────░░── ─┘    ──┘ ──────────┘───┘─┘─┘─┘──────┘─┘────┘───┘─┘───┘─────┘──┘
                      │                    │  ────   •
                       │░──░░░│ ░░░░░░░░ ░░│ │ ░░░░░░ ░│
                       └─░░───┘ ───────────┘─┘─────────┘
                          •   │
                                                ────               ───────
                            ─────┐────┐────┐──┐─    ─┐─┐────────┐──                  ───┐
                                 │░░░░│ ░░░│░░│      │▒│░░░ ░░░░│     ┌────       ──┐   │
                           │ •   │   • ── ─┘─ └────── ─┘─── ────┘     │░░░░──────░░░│    │
                           │  │  ▒▒▒▒▒░░▒▒▒▒░▒░░▒▒▒░░      •          └────░░░▒░░┌──   │ │
                           │  └───────────────────────────                 ──────┘  │  │ │
                           │ │                                                      │  │ │
                           │ │                      ──────────────────────────      │ •  │
                           │ │    ─────  ─┐────────┐                                   │ │
                           │ │   │░▒░ ░┌─░│ ░░░░░░░│                                   │ │
                           │ │   │░│  ┌┘▒•░ ░│                                         │ │
                           │ │   │ │ ░│░░ ──░│ ─────┐────────────┐────┐─┐───────┐      │ │
                           │ │  │░░░░ │▒ ░░░░░•░▒░░▒│ ░ ░ ░░▒  ░░│ ░░░│ │░░     │      │ │
                           │ │  │░░░│ │░░░░░ ▒░▒────┘┐───────────┘────┘─┘───────┘      │ │
                           │ │  └─░░└─ ─────┐░──     │                                 │ │
                           │ │    ──        └─    ───                                  │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │  ┌────                                                  │ │
                           │ │  │░░░ •    ─┐                             ─────  ───    │ │
                           │ │  └───  ───  └────     ─────────────┐─┐         ─┐   ──  │ │
                           │ │         ░░─┐┘  ░░─┐  │░▒░░  ░░░░   │░└──┐─┐──┐─ └───   │ │
                           │  ─┐─░░░   •░░│  ──░░│  └──── ───░── ─┘░│░░│ │░░│  │     ─┘ │
                            •  │ ─┐─    ┌─┘    ──┘                    ─┘ └──┘   •  ──   │
                             ─┐┘  │ ──┐─┘     •       •     ┌─     ┌─   •    • │ ┌─  ┌──
                              │   │ ░ │  ░      ░  ░   │ │░ │ │    │░│  ░ ░│   │ │░ ░│
                               ───┘ ──┘────────────────┘─┘──┘─┘┐───┘─┘─────┘ ──┘─┘───┘
                                   •                           │            •

















```

*Figure from page 13 (2346x3317 px)*


---



4203-E P-317



SECTION 3 DATA INPUT/OUTPUT OPERATION



(2) Enter the file name (including the device name and path name).



Example 1: The following command protects the file FILE.MIN in device "FD0:".



>PROT FD0:FILE.MIN



Example 2: The following command protects all files with the extension name MIN in device



"FD0:".



>PROT FD0:*.MIN



Example 3: The following command cancels protection for the file FILE.MIN in device "FOO:".



>PROT FD0:FILE.MIN;C



Example 4: The following command protects all files in the directory "PATH" of device "FOO:".



>PROT FDO:PATH\*·*



{3) Press the WRITE key.



[Supplement]


#### WRITE


## 1. The wild cards "*" and "?" can be used in file names.


## 2. If the specified file is a directory, the message "directory" is displayed on the

console lines and the file protection operation is terminated.


## 3. If the option V (;V) is not specified, files will be protected (or have their protection

canceled) unconditionally.


## 4. The following options can be specified. They must be preceded by a semicolon";".

;C Cancels file protection.



;V Specifies use of a request for confirmation of whether or not the file may be



protected (or have its protection canceled).



If the file may be protected or file protection may be canceled, enter "Y''; to



abort the file protection or protection cancellation operation, enter "N".


```text


                                                                                                ───
                                                                ┌───────┐───┐───┐─┐───┐─┐───────░░░░────────┐
                                                                │░░░░░░░│ ░ │░░░│ │░░░│ │░ ░░░ ░────░░░░░░░░│
           ┌──────   •            •    •                ────   ┌┘────   │   └───┘─┘───┘─┘───────     ───   ─┘
           │      ┌─┐ ┌──────────┐ ──── ────┐──────┐─┐──    ───┘     ┌─┐ ┌──                                │
           └──────┘░│ │░        ░│          │░     │ │         │ •   │ │ │     │             ───────────────┘
                  └─┘ │         │  •   ─────┘     ─┘─    ┌────  •      │ │  • ─┘─────────────
                      │░   ░ ░ ┌┘─┐ ░ ░ ░ ░░   ─┐─░  ──┐ │ ░       ░░ ░ │░ ░░░          ░
                      └────────┘  └────┐        │      └─┘ ─────────────┘────────────────────
                                       │░░░ ░ ░░░  ░   │░░░
                      ┌────┐─┐──┐─ •  ─┘                   ───┐─┐─────┐─┐───┐─┐──┐───┐─┐─┐─────┐───┐────┐
                      │░░░░│░│ ░│ │ ──░░░ ░░ ░  ░ ░░░░░ ░░░░░░│ │ ░░░ │░│  ░│ │░░│░░░│ │░│░░░░░│   │░ ░░│
                      └────┘─┘──┘ │░ ░─── ─────   ───   ──────┘─┘─────┘─┘───┘─┘──┘───┘─┘─┘─────┘───┘────┘
                                   ───   •     ───   ───
                                       │░░░ ░ • ░    ░░░│
                      ┌──────┐──┐ ┌───┐┘     •   ───    └────────────────────┐──┐─┐────┐─┐───┐────┐─┐───┐
                      │░░░░░░│ ░│ │░░ │░░░─┐ ░ ┌─░░░░    ░░░░░  ░░░░░░ ░  ░ ░│ ░│ │░ ░ │░│ ░ │░░░░│ │░░░│
                      └──────┘──┘ └───┘┐   │ • │            ┌────────────────┘──┘─┘────┘─┘───┘────┘─┘───┘
                                       │░░░░• •░░░░░░░ ░░░░░│
                      ┌─────────┐ ┌──── ──   • ┌───         └─┐───────────┐───────┐────────┐──────┐─────┐
                      │░ ░ ░░   │ │       ░• ░ │    ░│  ░░░░░░│ ░  ░░    ░│ ░ ░░░░│   ░    │ ░░░░░│    ░│
                       ─────────   ─────    ┌─     ──┘  ┌──┐──┘───────────┘───────┘────────┘──────┘─────┘
                                         •░┌┘ │       •░│  │
                  ┌─┐   ────────┐─┐ ┌─    ┌┘  └──────  ─┘  └┐
                  │ │ •         │ └─┘░   ░│               • │
                   ─┘   ──────── •   ─────          │  ┌─┐  └┐
                                                    │  │░│   │
                                                    │ ─┘  ┌─ │
                                                     │░░  │  │
                                                     └────  ─┘

                 ┌──────────┐   ┌─┐  ┌─┐─┐────────────       ┌─────────────────────┐
                 │░░░░░░░░░░│   │ │  │░│ │░   ░ ░     ░ ░    │             ░     ░ │
                 └──────────┘   │ │ │ •  │    •      │            │ │           ─┐  •         •         •
                                │ │ │░ ┌─ ┌─── •   ──┘     ┌─     │ │       ───┐ │   ───   ──┐ ────── ──   │
                                └─┘ │ ─┘ ─┘           ┌────┘  │   └─  ──       └─┘      │    └─         ───┘
                                    │ ░└─░ ──────░  •░│  ░░ ──┘───░░  ░░ ──────┘░░──────┘
                                ┌─┐ │                                                    ─┐──┐─┐──┐───┐───┐─┐
                                │░│  ┌─────░░ ─────░───────░░░░░░░│ │░│ ░░  ░ ░ │░░░░│ ░• │░░│ │░░│ ░ │░░░│ │
                                └─┘  │░░ ░░─── ░░ ░•░░  ░░░───────┘ └─┘─── ─────┘────┘──  └──┘─┘──┘ ──┘───┘─┘
                                │ │  │                             •      •             ──         •
                                │░│ │░░│ ░░░░░    ░░  ░  ░  ░ ░   ░░ ░ │░      ░ ░       ░ ░               │
                                └─┘ │ ┌┘┐                   ┌───────── └───────────────────────────────────┘
                                    │░│ │░░ ░░░░ ░░ ░░░░ ░░ │
                                    │ │ │                     ────  ───────── ───┐─────┐───┐────┐──┐─┐─────┐
                                    │░│  │░───░─┐─┐░─┐────░░ ░░░░░──░░░░ ░░░░• ░ │░░░░░│ ░ │ ░ ░│ ░│ │░░ ░░│
                                    └─┘  └─░░ │░│ └─ │░ ░ ─────░• ░ ───░───░   •   ────┘       ─┘    └────┐┘
                                        │     │      │                        │  ─┐     ───────  ───      │
                                        └┐──┐ ░┌─┐░──┘─────░░░░  ░ •░──░ ░░░░░└──░│ ░░ •░░ ░░░░ • ░░    │░│
                                         │  │ ░│ │         ─┐────   •  ┌──┐ •       •   •  ───   ┌─┐  ──┘─┘
                                         └──    • • ──────  │    ─── ──┘  └─ ───── • •   ──   ───┘ └──
                                                                                      ──






























```

*Figure from page 14 (2346x3317 px)*


---



4203-E P-318



SECTION 3 DATA INPUT/OUTPUT OPERATION



1-10. Special Input/Output Function For Work Program Files



1-10-1. Program Input



Work program files are input from the MS-DOS formatted floppy disk to the memory disk while deleting any



"%" codes which may exist within, or at the beginning of the files.



The operation procedure is indicated below.



(1) Press function key [F1] (PROGRAM INPUT)



=EX



=MSDS



>EX


#### PROGRAM

OUTPUT



Press F1 (PROGRAM INPUT)


#### MS-DOS


#### QUIT [EXTEND)

The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.



MS-DOS CONVERTER: PROGRAM INPUT


#### PROGRAII OPERATION US-DOS CONVERT

us..ms CONVERTER: PROGRAM I NPl!T



PROT[I]



INDEX DISPLAY PROCEDURE



[F2] -. llll :*. *



[F31 - Fl)():*.*



I 97/07/15 14:10:00



OVERWRITE



TO DISPLAY OTHER INDEXES. AFTER PRESSING [FT] ,



INPUT 11-lE DEVICE NAME AND FILE NAME, THEN PRESS [WRITE] KEY.



DEFAULT DEVICE NAl,E =



DEFAULT FILE NAME~ *.*



>XIN



l()l: FOO: COt.lfANO OVERWR/ CHAR.



INDEX INDEX I M>EX HI STORY INSERT DELETE CANCEL


```text


                                                                                               ──
                                                               ┌─────┐─┐───┐───┐─┐─┐───┐─┐─────░░──────────┐
                                                               │░ ░░ │░│ ░ │░░░│ │░│░░ │░│░░░ ░──░░░░░░░░░░│
            •  ───                    ──        ───       ── • └─────┘─┘   └───┘─┘─┘───┘─┘─────     ───
          ┌─ ──   ┌───────────────┐───  ┌─┐─────   ───────  • •         ───                                │
          │     ──┘░              │ ░   │░│      │            ░│ ──          ──────────────────────────────┘
          └────┐  └─── ───────────┘─    └─┘  •   └─────────────┘┐░░ ░┌───  ░•
               │  │   •             ────   ── ───               └────┘   ───
          │      │  ░░░ ░░  ░░•
          └─────┐┘             •        •   ────── • ───      ───  ──   ───────┐─┐──────┐─┐─┐──┐─┐─────────┐
                │ │ ░ ──░ ░░──░░ • ░ ──┐ ░── ░ ░ ░   ░  ─────░░░░ •░░░──░░ ░ ░ │ │░░░░░ │░│ │░░│ │░░░░ ░ ░░│
                └─┘─┐─░░─── ░░───░──┐░░└──░░────────────░░░░ ░─── ░───░░───────┘─┘──────┘─┘─┘──┘─┘─────────┘
                │   │               │                   ─── •    ──   ──
                │ ░ │░░░░░░░ ░ ░░░░░░░ ░ • ░░•░•  ░░░░│
                └─ ┌┘┐    │      ┌─  │  • •   │ ┌─  • └┐────┐
                │  │ │░ ░░│ ░ ░░░│ │░│ ░ ░ │ ░│ │░░░░│ │░░░░│
                 ──┘ └──┐─┼───  ─┘─┘─┘─────┘──┘─┘────┘─┘────┘
                        │ │                                                                 ┌─┐
                        │ │  ┌──┐─                                                          │ │
                        │ │  │░▒│░                                                          │ │
                        │ │   ──┘           ────────                                        │░│
                        │ │  │   ──┐─┐─────┐               ─┐────┐─┐─────┐───  ─┐───        │ │
                        │ │  │░░░░░│ │░░░░░│ ─────┐ ┌─────┐ │    │ │     │░ ░░•░│    ───    │ │
                        │ └─ └┐────┘─┼─────┘      └─┘     └─┘     ─┘     └──┐░ ░└─  │   ──┐─  │
                        │     │      │                   •       │ │     │  │ ──    │   ░░│  │
                         ─── ─┘─── ──┘ ─┐   ──┐─┐─┐───┐─┐ ── ─┐──┘─┘─┐─┐─┘  │   ────┘ •  ┌┘──┘
                            │░ ░   ░ ░ ░│   ░ │ │ │ ░ │ │     │░ ░ ░ │░│ ░ ░ ░│     ░│░ ░│
                            └─ │  ┌─────┘┐────┘─┘─┘ ──┘─┘───  └─ ┌── └─┘ ─────┘──────┘──░│
                              ─┘─ │      │         •        ──  ─┘  •   •               •
                                    •░░░ ░─┐░░░ ░░░░──░──┐
                       •   ───── │ •   •   │ ──┐         └──────┐─────┐─┐─┐──────┐─┐────┐───┐─┐─────────┐──┐
                      │░───░░░░░─┘░░░░░░─── ░░ │░ ░░░ ░ ░░░ ░ ░ │░░░░░│░│ │░░ ░░░│ │░░░░│ ░░│ │░  ░░░░ ░│ ░│
                      │      ─┐   ─────     ──   ──     •   ────┘─────┘─┘─┘──────┘─┘────┘───┘─┘─────────┘──┘
                      │ ──    │           ─┐  ───  ────┐ ┌──
                      │░░░░░░░░  ░░░░░░░░░░│ │ ░░░░░░░░│ │░ ░░│
                       ── ░┌───────────────┘─┘─────────┘─┘────┘
                         ──┘                                             ───────────
                                 ┌──── ────┐── •   ── ──── • ───┐─────              ────
                                 │░░░   ░░░│ ░•      •░  ░• •   │      ───              •
                           │      ░░░░░ •░░└─░ ─────┐ ░ ░░░ ░░░░│     │░ ░ ─────── ░     │
                           │  │  │░░░│ ░░░░░░░ ░░░░░│ │░░┌── ───      │    ░░░▒░░░     │ │
                           │  │  │▒░░└──────────────┘─┘──┘        ──── ─────────────   │ │
                           │  │   ───                                               │  │ │
                           │  │                                                     │  │ │
                           │  │   ┌───    ─────────┐                                │  │ │
                           │ │ • ┌┘░░  ┌─┐░  ░░░░░░│ ───────────────────────────────┘  │ │
                           │ │   │░░│  │▒│   ┌─                                        │ │
                           │ │   │░░└── ░░───┘  ────┐───── ──────  ──                  │ │
                           │ │   │░░░░░░ •░░░└──▒░░░│ ░░░░░░▒░░░▒  ░░░  ┌────────      │ │
                           │ │   │░░░ ░░░░░░│░░▒░───┘ ──────────── ───  │░             │ │
                           │ │   │░─┐┐─────░│▒───                       └────────      │ │
                           │ │    • └┘     ─┘─                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │  ┌──┐                                                   │ │
                           │ │  │░░│                                                   │ │
                           │ │ ─┘    ────   ──┐─    ────┐──────  ─┐─         ──┐─────┐ │ │
                           │ │  └──┐─  ▒░───  │░─┐─ ░░▒▒│░░░░░▒──░│░───┐─┐──┐  │     │ │ │
                           │  • │░░│  ──░░░  ─┘░░│  ░───┘ ───░░░  │░   │ │░░│  │     └─  │
                            •    ┌─┘ •  ┌───   ┌─┘                    ─┘ │ ─┘  │        •
                             ─┐  │    │ │    │ │      •   │ │      ┌─┐         │ ┌─── •
                              │  ░│ │ │ │░   │ │░ ░│ │░│ ░│ │░│ │░ │░│ ░  ░│  │  │░ ░│
                              └───┘ └─┘─┘────┘─┘───┘─┘─┘──┘─┘─┘─┘──┘─┘─────┘─ └──┘───┘
                                   •                                         •


















```

*Figure from page 15 (2346x3317 px)*


---



4203-E P-319


#### SECTION 3 DATA INPUT/OUTPUT OPERATION

(2) Enter the device name, path name, and file name for the work program which is to be input.



IN <MS-DOS format device name:> <MS-DOS format path name + file name, or file name>,



<OSP format device name:> <OSP format file name>; <option>



With the exception of the following points, operation is identical to the COPY function.

- In order be executed as a work program, the"%" codes within, or at the beginning of the files, are



deleted.

- "FD0:", "FD1 :", "FD2:", and "FD3:" may be designated as the



If no device name is designated, "FD0:" will be adopted.



If any device name other than those shown above is designated, an error will occur.



"MOO:", "MD1 :", and "MD*:"(* = A-H) may be designated as the



If no device name is designated, "MD1 :" will be adopted.



If any device name other than those shown above is designated, an error will occur.



Example:


#### IN ABC.MIN

CP FD0:ABC.MIN, MD1:



+ % codes deleted



IN ABC.DIR\



CP FD0:ABC.DIR\, MD1:



+ % codes deleted



IN FD0:\*.MIN


#### CP FD0:\*.MIN,MD1:

+ % codes deleted



IN ABC.DIR\ABC.MIN, ;V



CP FD0:ABC.DIR\ABC.MIN, MD1: ; V



+ % codes deleted


#### IN MD1 :ABC.MIN

x (Error)



IN FD1 :ABC.MIN,FD0:



x (Error)



1-10-2. Program output



Work program files are output from the memory disk to an MS-DOS formatted floppy disk.



If option "E" is selected, only the"%" record will be added at the beginning and end of the output files.



The operation procedure is indicated below.



(1) Press function key [F2] {PROGRAM OUTPUT)



=EX



=MSDS



>EX


# I MS-DOS

QUIT [ffiEND]



@ @J@J@ @J@@@



\ Press [F2] (PROGRAM OUTPUT)


```text


                                                                                               ┌───
                                                                ┌─┐───┐─┐───┐──────────────────┘░░░ ────── ┌┐
                                                                │░│░░ │░│   │░░░░░░░░ ░ ░░ ░░░░░──░•░░░░░░─┘┘
           ┌──────   •               •    ──    •    ──      ── └─┘    ─┘   └─── ───       ────      ──
           │      ┌─┐ ┌────────────── ────  ┌─── ────  ──────  •   ─┐─┐  ───    │   ───────    ──           │
           └──────┘░│ │░    ░               │ ░                     │ │         │                •     ┌────┘
                  └─┘ │            ─┐─┐    ─┘           ──  • ──  ──┘ │ ──     • ░  │     │       ──── │
                      │░░•░░░ ░░░░  │ │░  •   │ │  ──┐ •░░░  • ░       │ ░│      • ░│     │ │ ░       │
                       │  ─────────   │      ─┘┐┘┐─  │  ──     • ─┐  ┌─┘  └─  ─┐─ ──┘─────┘─┘─────────┘
                      ┌┘─          ─┐          │ │ ──┘    ┌─    •░│  │ │     │ │
                      │░ ░─┐  │     └─┐─  ░           │   │       └─   │     │ └──────── ────────┐
                      └┐ • │ ─┘       │ •           ░ │   │ │    │   ──┘  ───┘                   └─ ───
                       └┐  │ ░│                       │   │ │ │  │           │                         ────┐
                        │ •    ───────────────────────┘───┘─┘─┘──┘───────────┘────────────────░────────    │
                        │░░  ░•                                                               •
                        └─────  ░───┐┐────── ┌─┐─┐──── ┌──────────────────────┐
                        │           └┘      ─┘ │ │    ┌┘          ░ ░         │
                        │  │ ░      │    • │    •   │ │ • │
                        └──┘        │  •  ┌┘  │     └─┘   │              ─────── • ┌─────────────
                        │   │  ░    └┐ ░│ │░ ┌┘────    ░│░ │░│ │  │     ░       │  │             │
                         ───┘   ┌──  └─ │   ─┘      ──  │  │ └─┘  │             │  └─────────── ─┘
                        •░░░│   │░░    ░│░ │░│     │  │  │ │ ░  ──┘░░ ░░░░░░ ░ ░ ░•
                         ──┐  ── ┌─ ─── │  │  ─┐───┘┐ └─ │ │  │   │      ┌────────
                        │ ░│ │░ ░│ •░░░• ░ │░░░│ ░░░│ │░░│  │░│ ░░ •░░─┐░│
                        │  └┐┘    • │   │ ┌┘ ┌─  ┌──┘─  • ──┘┐  ──  •  │ └──────┐──┐─┐──┐─┐──────┐
                         │░ │ •░ ░░ │░░ │ │░░│ │░│ ░ ░░│ │ ░░│ │░░░░ ░ │░░░░░░░░│ ░│ │░ │ │░ ░░░░│
                      ┌┐─┘     ─────┘───┘─┘──┘─┘─┘─────┘─┘───┘─┘───────┘────────┘──┘─┘──┘─┘──────┘
                      └┘░░ ░░░│
                       └──────┘ ┌──────────┐              ──┐── ┌── ───────┐ ──┐───┐──┐
                                │░░ ░░  ░░░│                │░  │░   ░░ ░░░└─░░│  ░│  │
                                 │  │ │    │              ──┘── │ ░    ░───░  ░ ┌─    │
                                ┌┘──┘─┘────┘─                   │            │  │ ┌───┘
                                │░░ ░░   ░ ░                 ░  │░   │░ ░░░──┘░░│ │░ ░│
                                 │  •   ──                •   • └────┼─────░  •  ┌┘───┘
                                 └── ───  ┌──┐             ─┐─  │    │          ┌┘
                                 │░   ░   │░░│              │░  │░•  ░░•   ░░░ ░│░
                                 │                         ─┘── └─░────   ───┐──┘
                                ┌┘──────────────────┐──┐        │        •   │    ─┐─┐──┐─┐─┐────┐─┐
                                │░░ ░░   ░░░░░░  ░░░│ ░│  │ │░│ │░  │░░ ░░░  │░░░░░│ │░░│ │░│    │ │
                                      •     •    ───┘──┘  └─┼─┘ └── └──────░  ░────┘─┘──┘─┘─┘─── └─┘
                                   ─── • ─┐─  •             │ │            ────
                                 ┌─ ░   │░│  │░│ ────     │ └─┘    ░  ░ │
                                 │░ ─── │░│ ░│░│          └─┘░│   ───  ─┘
          ┌──┐───┐ ┌──────┐─┐───   •     • ── • ─────                ──
          │  │░ ░│ │░ ░░░░│ │░░ ░│
          └──┘──┐┘─┘      └─ •   └─┐───┐────┐─┐─────┐──────┐────────┐─┐─────────────┐─────┐─┐──┐
                │░░░│ ░ │░ ░│ │░░ ░│░ ░│░ ░ │░│ ░░░ │░ ░░  │░░░ ░ ░░│░│ ░░░░ ░░ ░░░░│ ░░░░│ │░░│
                │   │  ┌┘ │ │ │ ───  ─┐    • •  ─┐ •        ┌─ ───   •   ── ──   ┌─┐  ─┐  │    └──┐──────┐
                │░ ░ ░ │ ░│ ░ │░░░░░• │░░░ ░│ │░ │░░░░• │░ ░│ │░░░░ ░ ░│░ ░│░░░░░│ │░│ │ ░ ░ ░│ ░ │░░ ░░░│
                └┐  ─┐ └─┐┘┐  └──    ─┘───┐ └─┘─┐      ┌┘───┘─┘────────┘───┘─────┘─┘─┘─┘──────┘───┘──────┘
                 │░• │░░ │░│  ░░░░░░░░  ░ │░░░░░│ │░░░░│
                 └┐ ┌┘┐    │      ┌──  ───┘     └─┘──  └───────┐
                  │░│ │ ░░░   ░ ░░│ ░░░ ░░░ │░░░░░░░░│ │░ ░░░ ░│
                  └─┘─┘─┐─┐───  ──┘─────────┘────────┘─┘───────┘
                        │ │                                                                 ┌─┐
                        │ │  ┌──┐─                                                          │ │
                        │ │  │░▒│░                                                          │ │
                        │ │   ──┘           ─────────────────────────────                   │ │
                        │ │  │   ──┐───────┐                             ┌─────────┐        │ │
                        │ │  │░░░░░│ ░░░░░▒│ ─────┐ ┌─────┐ ┌────┐ ┌─────┘░ ░░░░░ ░│ ─────┐ │ │
                        │ └─ └┐────┼─┐─────┘      │ │     │ │    │ │     └──┐  ──── │     └─  │
                        │     │    │ │                           │       │  │       │    ░│  •
                         ─── ─┘── ─┘─┘  •   ──┐─┐─┐─┐──┐─── ──┐──┘─┐─┐─┐─ ─┐┘─ ─── •     ┌┘──
                            │░ ░   ░ │ ░░   ░ │░│ │ │ ░│      │░ ░ │ │░│ │ │ ░│░    ░ ░ ░│
                            └┐ ── │░ │ ┌─ ────┘ │ └─┼─┐┘┐ ────┘────┘ │ │ └─┘ ─┘────  •░ ┌┘
                             └─   └──┘─┘      └─┘   │ │ └─          • • ─┘ └─      ── ──┘
                               ───     └┐   ░░ ░░░  ░ ░░ ░░      ░│
                                        └─────────────────────────┘














```

*Figure from page 16 (2346x3317 px)*


---



4203-E P-320



SECTION 3 DATA INPUT/OUTPUT OPERATION



The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.



MS-DOS CONVERTER: PROGRAM OUTPUT



OUTfl


#### PROGRAM OPERI\TION MS-DOS CONVERT

MS-DOS CONVERTER: PROGRAM OUTPUT



OUTII!



INJEX DISPLAY PROCEDURE



[F2] .... MD1



:*. *



I 97/07/15 14:10:00



[F3] - FD0:*. *



OVERWRITE



TO DISPLAY OTHER lrflEXES, AFTER PRESSING [Fl] ,



I NP\JT THE DEV I CE NAME AND FI LE NAME, THEN PRESS [WR IT E] KEY.



DEFAULT DEV I CE NAME =


#### DEFAULT FILE NM£ =

*. *



>XOUT



@J @J@J @J@J @J@J @J



(2) Enter the device name, path name, and file name for the work program which is to be output.



OUT <OSP format device name:> <OSP format file name>, <MS-DOS format device name:>



<MS-DOS format file name>; <option>



With the exception of the following points, copying occurs in the same manner.

- "MOO:", "MD1 :", and "MD*:", (*: A to H) may be designated as the



If no device name is designated, "MD1 :" will be adopted.



If any device name other than those shown above is designated, an error will occur.

- "FD0:", "FD1:", "FD2:" and "FD3:", may be designated as the



If no device name is designated, "FDO:" will be adopted.



If any device name other than those shown above is designated, an error will occur.

- Option "E" may be designated. If designated, only the''%" record will be added at the beginning



and end of the output files.


```text


                                                                                               ───       •
                                                               ┌─────┐─┐───┐──┐─┐───────────── ░░░───────░│
                                                               │░░░░ │░│   │░░│ │░░░ ░░░░░░░░ ░──░░░░░░░░─┘
          ┌───────────   ───    •       ───   •      ────── ───┘──── └─┘  ┌┘──┘ └────────────       ───
          │            ──   ──── ┌─────┐   ──┐ ┌─────      •        •   ┌─┘    •             ───           │
          └───────────           │     │     │ │              │         │ │        │                       │
                      ┌───┐──┐ ──┘   ──┘──┐ ─┘─┘──────────────┘──   ┌───┘ │      • │   ┌─   ─── │       │  │
                      │░░ │░░│ ░░│░░ ░░░░░│                      ───┘   └─ ────── • ───┘ ───   ─┘ ──────┘──┘
                      │                    │  ──────────────────┐
                       ░  ───   ──         │       ░  ░░        │
                       •░░░ ▒┌──  ───────── •  ───────────── ───
                        ─────┘
                               ──┐────────────┐──────┐─────────────                    ──
                           │     │▒▒▒▒▒░▒▒▒░░▒│      │▒░░░░ ░▒░░░  ───┐────       ───┐   │
                           │ •  •    ┌─       │ ───── •   │ ─────     │▒░░░│▒──░░░░░░│ │ │
                           │  │  │░░▒│ ░░░░░░░ ░░░▒░▒ ░░░░│      ─────┘────┘▒▒▒•░───┐┘ │ │
                           │  │ ┌┘───┘────────────────────                  ─── •   │  │ │
                           │  │ │                                                   │  │ │
                           │  │                     ────────────────────────────────┘ •  │
                           │ │   ┌────┐┐────────────                                   │ │
                           │ │   │░░░ └┘░░░ ░░░░░░░                                    │ │
                           │ │   │░•  └┘░• •       │  ────    •                        │ │
                           │ │   │░░░░│░• •░░────░░└─ ░░░░ •░░ ┌── ───┐─┐─┐──┐──┐─     │ │
                           │ │   └─░┌─┘─ ░░  ░ ░▒──░░ ────░░▒• │░░ ░░░│ │░│ ░│ ░│      │ │
                           │ │   │░░│   ░░░░ ░░┌─         ──    ─── ──┘─┘─┘──┘──┘─     │ │
                           │ │   └──┘────── │▒─┘                                       │ │
                           │ │             ─┘─                                         │ │
                           │ │                                                         │ │
                           │ │                                                         │ │
                           │ │   ───                                                   │ │
                           │ │  │░░░ •    ─┐                          ───────   ─────┐ │ │
                           │ │  └──┐  ─┐─┐ └──┐─    ─────────── ────         ┌─┐     │ │ │
                           │ │     │   │░└┐┘  │░─┐  ░░▒░░  ░░░▒│   ░┌──┐ ┌──┐┘ └─────  │ │
                           │    ┌┐░│   │░░│░  └─░│  ────── ─┐──┘  ┌─┘░░└─┘░░│  │      •  │
                            ── ─┘┘        └─     │          │     │   •  └─ │  └────┐   •
                              │  ░░ ░ │ ░░   │  ░      ░    │░     │░│    ░░░    ░░ └┐ •
                              └─ ──── │ ──── └─ ░•░──  • ── │ • ── │░│ ── ───    ── └┘
                                       •       ──     •    • •      •               │
                 ┌─┐─┐───┐─┐────┐  ──┐     ──┐   ──┐ │  ───    ─┐──   ┌─┐─   ┌───  │ ┌───┐─────┐──┐────┐
                 │░│ │ ░░│ │░  ░│░░░ │░ ░  ░░│  ░░░│ │░  ░░  ░░░│ ░• ░│ │░░│ │░░░░░│ │░░░│ ░ ░ │░ │░░░░│
                 └─┘ │   │ │                              │    •  •  • ─┘  └─┘      • ───   ┌─┐┘─  ┌─  └──┐
                      ┌──┘─┘──░─────────░░────░░░░───── ░░│ ░ ░ ░  ░• •░░░ │  │░░  ░ ░   ░ ░│ │░ ░░│ │░ ░ │
                     ┌┘░░░░░░░•░░░░░░ ░░─┐░ ░  ───░░░░░•  │       •    ────   └──  ──     ──┘─┘────┘─┘────┘
                     │                   │              ─┐ ┌─────┐ ────    ─┐─   ─┐  ─────
                     │░░• ░•  ░░░░░░│  ░ │░ •░░░░░░░ ░░░░│ │░░░░░│ ░░░ ░  │░│ •░ ░│ │░░░░░│
                     └─┐ •  ┌── • ┌─┘ ──  ┌─ ┌─┐─┐─┐──   └┐ │  ┌─      ───┘ │  •  └┐┘─────┘
                       │░░░░│  │░░│  │░ • │░░│ │ │░│ ░ ░ ░│ │░░│ ░ ░░░░░░░░░│ ░ ░ ░│
                        ──┐─ ──┘ • ──┘ •  │  └─┼─┘ └─┐── ─┘ │           ┌───┘──────┘
                         ░│ │░ ░• •░░░• ░ │░░│ │░░░  │░░•  │░░ ░  ░░░░░░│
                          │ └┐ • │ │   │ │ ─┐┘  ┌─ ──  • ─┐┘ ─┐   ┌───  └───┐──┐──┐────┐─┐──────┐
                         ░░• │░ ░│ │░ ░│ │░░│ │░│ •  ░• ░ │░• │░░░│ ░ •░░░░ │░░│ ░│ ░ ░│ │░  ░░░│
                        •   ┌┘─  └─┘─┐─┘─┼─   └─ • ┌──     │ ┌┘ ┌─┘┐─┐ ─┐─  └──┘──┘────┘─┘──────┘
                       •░░░░│ ░•░│   │░░░│ ░░  ░ ░░│   ░│ ░│ │░░│░ │░│░ │ ░░│
                        •    ──  │ ── ─── │ ── ──  │    └┐─    ┌┘┐    • └───┘
                         ░░ │░ ░• │░  ░ ░ │░░░•░░░•    ░░│ •░ ░│ │░░░░░░│
                            └┐    └┐     •  ┌─  ┌─ ─── • └─ │  └─ ┌───  └───┐──┐─┐──┐───────────┐
                         ░ • │  ░• │░░ ░ ░•░│ │░│ ░  ░• ░░ ░│ •░ ░│ ░ •░░░░ │░░│ │░ │ ░  ░░  ░ ░│
                                              └─┘  │ │ ───  └─ ─┐ └─┐─ ──┐─  ──┘ └── │ ┌────┐─  └──┐───────┐
                       │░░░░───────░ ┌───░░░• ░░░│ │ │░░░░░░░░│ │░│ │░│ ░│ │░░░  │░ ░│ │░░░░│░ ░░░ │░░░░ ░░│
                       │░─── ░ ░ ░ ──┘░░░───░────┘─┘─┘────────┘─┘─┘─┘─┘──┘─┘─────┘───┘─┘────┘──────┘───────┘
                        •    ─────    ──





















```

*Figure from page 17 (2346x3317 px)*


---



4203-E P-321



SECTION 3 DATA INPUT/OUTPUT OPERATION



Example:



OUT ABC.MIN - CP MD1:ABC.MIN, FOO:



OUT ABC.MIN;E - CP MD1:ABC.MIN,FD0:



OUT MD1 :*.MIN;V



OUT MD1:*.MIN;VE



+ % codes deleted

- GP MD1 :*.MIN,FD0:;V

- CP MD1 :*.MIN,FD0:;V



+ % codes deleted



OUT ABC.MIN,ABC.DIR\ - CP MD1:ABC.MIN,FD0:ABC.DIR\



OUT ABC.MIN,ABC.DIR\;E - CP MD1 :ABC.MIN,FD0:ABC.DIR\



+ % codes deleted



OUT FD0:ABC.MIN



1-11 . Quitting MS-DOS



x {Error)



This function quits the MS-DOS operation mode.



{1) Press function key [F7] {QUIT).



">0" is displayed on the command line.



"=" will be displayed to indicate the completing of quit.



>(l


#### DIR COPY RENAIE DELETE FREE PROTECT

">Q" is displayed.


```text


                                                                                                ───
                                                               ┌──────┐─┐──┐───┐─┐──┐──────┐────░░░░───────┐
                                                               │░░░░░ │░│  │░░░│ │░░│ ░ ░░░│░░ ░──── ░░░░ ░│
           ┌──────────   ──    ────────────────────────────────┘──────┘─┘  └───┘─┘──┘──────┘───
           │          ┌──  ───
           └──────────┘░      ┌──             ──────────────  ───  •
                      └───────┘   ──┐─ ──   •               ┌─    •
                                 │  │ │    │ │              │ │  │  │  • │░│    │ ┌──┐
                                 └─ │ │ •  │ └──┐         ┌─┘ │ ┌┘ ─┘ •  └─┼────┘─┘  │
                                 │░ │ │░░░ ░░░ ░│         │ │░│ └┘░ │░   │▒│ ░░░░░░░┌┘
                                        ─────             └─     │               │ ─┘
                                  ────┐─     ────┐        │ ┌─┐ ┌┘────    ────── └─  │
                                 │░ ░ │░│  ░ ░░░░└┐       │ │░│ │░░ ░░ ─── ░░░ ░░░░ ░│
                                 │  │ │ │    ┌─── └─      │ │ │ └── │             │  │
                                 │ ─┘ │      │   ─┘         │ │    ┌┼──────────  ░└──┘
                                 │                             ── ░└┘░░░░  ░░░░░──
                                 │    ┌─     ┌─┐   •  │                           ──── ─┐──┐─┐
                                 └──  │░│ ┌─ │ └─┐   ─┼──┐──┐─┐ │ │ ─┐   ┌─┐ ┌─░•   ░ │░│  │░│
                                 │░ ░ │░│ │░░│ │░│  ░░│ ░│  │░│ │░│ ░└── │░│ │░•░░░ ░ │░│   ░│
                                  ──── ─┘─┘──┘  ─┘────┘──┘ •     •               ───── • ────
                                              •               │ │   ──░░░  ░░░░░│
                                 │░   │░░ │░░│ │░░│       │ │░│ │ │░  ──────────┘
           ┌──         ──   ───  │    └───┘──┘─┘──┘       └─┘─┘ └─┘───
           │       ────░ ┌──░  ──┘────
           └──── ──      │░           •   •
                    •      │ │     •   ─── ────────────────┐
                 ─┐─ ─┐──  │ └── ──░ •        ░   ░       ░│
                  │ │ │  ── •                     ─────────┘
                  │ │   ░░░  ┌─ ░   ░░░
                  └─┘──┐───  │       ──┐          ──────┐
                       │    •     ░    │          ░     └─   •   •
                       └─ │   ┌─┐      │          ─┐  │   ──  ─── ── │
                       │ ─┼───┘ └──────┘────────── └──┘──   ──   •   │
                        │ │                              ──   ─── ──                        ┌─┐
                        │ │                                                                 │ │
                        │ │   ┌─                                                            │ │
                        │ │  ┌┘░                                                            │ │
                        │ │ ┌┘   ──────   ─┐──     ──  •  ┌──    ───                        └─┘
                        │ │ │░ ──      ─── │░ ──  │     ┌─┘         •                       │ │
                        │  • •   ──┐──┐   ─┘─   ──┘  ┌─┐┘   • ┌──    ────    ┌──  ──┐──     │ │
                         │  • │    │  │  │    ░░ ░   │░│   •  │░░│ • ░  ░•   │░ │   │     ──  │
                         └┐   └──┐─┘──┘──┘──           └─ • ┌─┼─ └─         ─┘─┐┘┐──┘──┐─┐  │
                         └┘  ┌┘ ░│     ░░░ ░ │ ░░░    ░░░ ░ │ │░│   ░ ░░     ░░│ │ ░ ░░│ └┐─┘
                         │ │ └┘     ────── ┌─┘ ──  ── ─── ┌─┘ └─┘───────┐ ──── │ │ │ • │ └┘
                         └─┘─┘   ───       │ └─   •  •   ─┘ └─          │      ▒ └─┘─ • ─┘
                         │ ░░ ░ ░░░░░░┌─                         │  ░░ ░│  ░ ░░──
                          ────────────┘                          └──────┘──────



































```

*Figure from page 18 (2346x3317 px)*


---



1 ~12. Character Codes



(1)



4203-E P-322



SECTION 3 DATA INPUT/OUTPUT OPERATION



Carriage Return Character



In MS-DOS the carriage return character comprises two bytes for CR and LF ($OD, $DA).



In NC there is only LF ($A).



The NC converts carriage return characters internally.



(2) File End Character



In MS-DOS the character "Z ($1 A) that indicates the end of a file is normally appended at the end of



each file. There are cases in which this character is not appended.



If this character appears part way through a file, all the data following it is ignored.



{3) Treatment of Non-ASCII Characters etc. by NC



Some codes that are not used in ASCII {most significant bit= 1) are used for European languages.



The NC cannot handle non-ASCII codes like these. When a file is read into the NC, any non-ASCII



codes that it contains (including control codes other than the carriage return code) are replaced by



question marks"?".



In addition, since the file end character may appear as the second byte of a two-byte character, the



NC cannot determine whether it is the file end character or a second byte. The file end character is



therefore ignored.



1-13. Miscellaneous Cautions



(1) If the destination file name in a copying operation already exists, the existing file is normally



overwritten. However, if for some reason the copying operation cannot be completed normally



and the copy of the source file cannot be created, this will mean that the existing file (which was



being overwritten) is deleted. If this happens, the error message indicating the cause of the



copying failure is displayed, then the following message is displayed on the console lines:



"<deleted file name> deleted"



Note, however, that-depending on the timing of the deletion of the existing file and the creation of



the new one this message can sometimes be displayed even when the file is successfully



overwritten.



(2) When copying a file from the MS-DOS format to the NC, if the file name specified in the NC is



the same as that of a program that is currently selected for automatic operation, and the



program selection method was B, S, or M, an error will occur.



Similarly, an error will also occur if a tile being processed by the schedule program automatic update



function is specified.



(3) The floppy disk used with the MS-DOS format 1/0 function must be MS-DOS formatted.



An error will occur if a floppy disk that is not MS-DOS formatted is used. {But note that, for copying,



either the source or destination must be OSP format.)



{4) Specifications such as "*A.MIN", where the wild card is used as the first character, are treated



in the same way as "*.MIN".


```text


                                                                                               ───       ──
                                                               ┌──┐─┐────┐─┐───┐─┐─┐───────┐───░░░───────░░│
                                                               │░░│ │░░░ │ │░░░│ │░│ ░░░░░░│ ░░ ── ░░░░░░•░│
            ──  ───   ────   •       ────────────────────────── ──┘─┘────┘ └───┘─┘─┘───────┘───
          ┌─  ──   ───    ──┐ ┌─────
          │     ───         │ │     │
          └─────   ── ──────┘ │  ───┘
                 ┌─  │      └─┘──     ───────┐
                 │ │ │  ░ ░░░░ ░░░   │░░░ ░░░│
                 └─┘ │     ──   • ── │       └─┐──┐──────┐─┐───┐──────┐─┐───┐──┐─────────┐─┐──┐─┐───┐
                      │  ░│    │ ░░░─┘─ ░░░──░░│  │░░ ░ ░│ │░░░│ ░░░ ░│ │░░░│ ░│  ░ ░░   │ │░░│ │░░░│
                      │   └──  │        ──┐  ──┘──┘──────┘─┘───┘──────┘─┘───┘──┘─────────┘─┘──┘─┘───┘
                      │   │    │          │░
                      │     ┌──┘          │ │  ── ── ────────────────
                      │ │ ┌─┘     ─┐    • │░│       •              ░░
                 ───  └─┘ │        └── │ ─┘─┘─       ────────────────
                        └─░      ░ ░ ░─┘
                  •  •    ░             •    ┌────  ───  ────── ───────   ┌─┐   ────────┐──────────────────┐
                      ──       ░  ─┐      ───┘    ──   •      ░•        ──┘ └───    ░░░ │░░  ░░░ ░   ░  ░ ░│
                     •░░░───── ───░└──────░░░░───░░░░──░• ───░•░───░─── ░░░░ ░░░░   ───   •   ─────────────┘
                      ──      •                          •             │          ─┐   ┌─┐ ───
                     •  │░│ ░ ░ │░░ •░░░░░░ │░░ ░░░    ░ ░•   ░│ │  ░│ │░│ ░░░ ░░│░│   │░│ ░░░│
                 ┌─┐    └─┘──  ─┘─ • ─┐     │           ┌─     └─┘───┘─┘─┘───────┘─┘───┘─┘────┘
                 │░│    │░░ ░░•   •░│ │░░░░ │░░░ ░░░░  ░│ •░ ░░│
                 └─┘ •              │       │                   ─┐─┐─  ──     •   ──  •  ── ────  ┌────
                      ┌─────────────┘───────┘───────────────────░│░│░──░░──┐──░───░░──░──░░•░░░░──┘░░░ ────┐
                      │░░ ░░  ░░ ░░░ ░░░░ ░░  ░░░░░ ░ ░░░ ░░ ░ ░░░─┘░ ░░ ░ │░ ░ ░░░ ░░░ ░░ ░░ •░░  ░░  ░░░░│
                      └───────── ───┐  ┌─── ░ ░────   ────── ───░• │  ── ──┘     │ │ ── ── ──   •          │
                     │              └──┘   ────    ───      •   • • ──  •  └─────┘ └─        ─── ──
                     │          ░  •                                                                       •
                     │    │               •     ─────── ─── ─────     ───  • ─── ──  ───     ──  •  ───  ─┐
                      │ ░ └──── ──── ──  • ────        •     ░   ────    │  •    ░ •  ░ •░• ░ ░──  •░ ░──░└┐
                      │░  ░░░   ░░░░ ░░░ ░░░░░░│ ───░│ ░░ ░  •░░░ ░░░│ • │ ░░░░ ░ ░░░──░░░ ┌──░ ░ ░░░░░░░ └┘
                      └────────────────────────┘─   ─┘─────── ───────┘─ ─┘───────────   ───┘  ────────────

          │ ─┐─┐   ┌──────────── • ─────────┐
          └─ │ │   │░     ░  ░ ░ ░   ░     ░│
            • •  ┌─ ──                      │      ───   ───────   ───┐─  • •   •  ───┐────┐    ─────┐
                 │ │  ───────── ░░───────░░░└──────░░░───░░░ ░░ ───░░░│░──░•░──┐░──░░░│ ░ ░└────  ░░░└──
                 └─┘ │░ ░ ░ ░░░ ──░░░░░░░── ░░ ░ ░░   ░░  •░░   ░░  ░   ░ ░░ ░ │░    ─┘      ░░         ─┐
                     │   ─── •      • •       ─┐─┐   ───         • •░ │ │ │  │ │                         └─
                      ┌─       ── ──    • • ── │ └──    ───    ░      │ └─┘──┘    ──────    ░  ── ──── ░ ░
                      │░░░░ ░░░░░ ░░░  ░ ░░░░░░ • ░ ░ ░░░░░ ░  ░░ ░  • ░░░░░░░░•░░░ ░░ ░ ░░ ░░░░░ ░ ░ ┌────
                      └─────────────────────────░░──░┌────── • ──░░░░░┌────░──░░░──────────░───── ░░──┘
                                                ┌─  ─┘      • •  ─────┘    •   ──          •     ───
                         ░░░░░░ ░░ ░░░░░  ░░░░░░│
                      │                          •  •        • ────             ───   ───┐─  • ──    •
                      └───────── ░   ░│  │░────░ ░•░░ ─────░░░ ░ ░░ ────────░─── ░░── ░░░│   ░ ░░ ───░─────┐
                      │░  ░░░ ░░┌─────┘  └─░░░░───░───░  ░░░•░─────░░░░░░░░ •░░░───░░────┘───────░ ░░•░░░░░│
                      └─────░░ ─┘          ────   •   • ────        • ────   •     •             ──    ────
                 ┌─┐ •      ───
                 │ │  │          ── ──┐ ──    ───────  • ──   •   ────┐┐── │ ┌┐    ──  • ────       ────┐
                 └─┘  │   • ───    •  │     ──          •  ───  ──░   └┘  ─┘─┘┘──   ░── •  ░ ───  ░    ░│
                     •░░ ░░ ░░ ░  ░░  ░ •░ ░░ ░• ░░░ ░ ░░   ░░ ░░░░░░░    ░ ░░░░░░──░░░░░░░──░ ░ •░── ──┘
                      ────┐───┐─────────░──────░──────────────────────────────  •   ───────  ──
                     •    │   │                                               ── ┌─┐        •  ─────┐─┐────┐
                      ┌──░│ ░ └───────░░ ░░│ ░░░░ │░ ░░ ░░ ░░░ ░░░░░░░░░ ░│ │░░░ │░│ ░ ░░│ ░ │░░ ░░░│ │░░░░│
                      │░░•░───  ░░░ ░ ─────┘───── └───────────────────────┘─┘────┘─┘─────┘───┘──────┘─┘────┘
                 ┌─┐ │                           •
                 │ │ │░   ░─┐─┐ ──   ──  │   ░• ░ ░    ░     │ │   ─── ──  ─────── ───  │ ───┐────┐
                 └─┘ │      │ └┐  ───  • │                   │ └─        ─┐             │    │    └───  ──
                     │░      •░│      ░  ░──── ░ ░  ┌─┐  •░ ░│ │░•       ░│  │ │  │ │  │ │   ░ ░  │       ┌─
                      •       •     │ • │  ░    ┌── │ │      │       ─────┘──┘─┘──┘ └──┘─┘────────┘─── ───┘
                     │      •░  ────┘  ─┘───────┘  ─┘─┘────── ──────                                      │
                 ┌─┐ │                          └┐                   ───┐───────┐──┐───────────┐─┐─┐─────┐
                 │░│ │░░░░░░•░░░░──░ ░  ░──── ░░░│ │░░░ ░ ░│ │ ░ │░ ░ ░ │░░░ ░ ░│  │░   ░░░░░░ │░│ │░░░░░│
                 └─┘ └──────░────░░░───── ░░░░───┘─┘───────┘─┘───┘──────┘───────┘──┘───────────┘─┘─┘─────┘
                            •    ───     ─────














```

*Figure from page 19 (2346x3317 px)*


---



4203-E P-323



SECTION 3 DATA INPUT/OUTPUT OPERATION



(5) If a directory is specified when using the DIR, COPY, or DELETE function, all the files contained



in that directory will be subject to the specified operation. If a directory is specified for the



RENAME or PROTECT function the message "directory" will be displayed on the console lines



and the operation will be aborted because it is only possible to rename or protect one file at a



time.



(6) Meaning of the wild card "*" under different functions



DIR Both "*" and "*·*" specify all file names with and without extension names.



DELETE : "*" specifies file names without extension names and"*·*" specifies file names with



extension names only.



PROTECT: "*" specifies file names without extension names and "*.*"specifies file names with



extension names only.



COPY "*" specifies file names without extension names and "*.*"specifies file names with



extension names only.


```text


                                                                                                ──        •
                                                               ┌──┐───┐─┐──────┐───────────┐────░░───────░░│
                                                               │░░│ ░ │░│   ░░░│ ░░░░ ░░░░ │░░░░──░░░░░░░ ─┘
           ┌──────   •           ────           ───   •         ──   ─┘─        ────   ──  └───       •
           │       ─┐ ┌──────────    ──────┐─┐──   ─── ──────┐─┐  ───   ┌──────┐    ───  ──
           └────── ░└─┘                  ░ │ │    │          │ │        │      │        │                  │
                  ──┘ │        ────┐         └──┐┐┘─  │                  •     │      ──┼── ─────┐ │   ── ┌┘
                      └────────░░░░└───────░░░░░└┘░ │░└───────┐ ┌─┐─────  ───┐░░──────░ │░░░░░░ ░└─┘─     │
                      │░░░░░░░░ ──░░░░░░░░░ • ░░░░  │░   ░░░░░│ │░│░░░░░──░░ │░ ░░░░░░░─┼── ─┐─┐─ ░░░ ░ ░│
                      └───────┐ ░ •░──────░│ │  • │ └─   ─────┘ └─┘ ───    ── │  ────── │    │ │   ── ───┼─
                      │       └─── •      ─┘ └── ─┘─  ───              ────   └─        └────   ───      │
                      │  •                                                                           ────
                  ┌─┐ │   ──┐───┐────────────────────────────────────┐
                  │░│ │░•░░ │░ ░│░░  ░░░ ░░░     ░░░░ ░░░░░░░ ░░░░░░ └┐
                  └─┘ │   │   ──┘──┐  •                               │     ──  ─────── ──       ──
                      │ • └───     │    ──────┐   ─────  ────   ───░  │ ┌───░ ──░      │░░──────┐░░ ─────┐─┐
                      └┐░•░░░░•    │ ──░░░░░░░└─░ ░░ ░░ ░░░░░░ ░░░░ ░░░ │░░░░ ░  ──────┘░░░░░░░ └───░ ░░ │░│
                       │     •     │░░░───────░░─┐──────────  ───── ── • ────              ───      •   ─┘ │
                        ───── ─┐─  │             │          ─┐     •         ───        ───    ────  ──┐  ─┘┐
                         ░     │   └─────────────┘────┐ ░░░░░│ ░░░░░░░░  ░░░│ ░ ░      │░░░░░░• ░░ │░░░│ │░░│
                             ──    │░░░ ░░░  ░░░░░ ░ ░│      │              └─      •  └───      • │ ──┘─┼─┐┘
                      │  ░ ░│      └───    ░░  ░      │  ░░                        •   │    ░            │ │
                      └─────┘      │  ░░░░░ ░░ ░░    ░└────────────────────────────  ──┘ ─────────────── └─┘
                                   └──────────────────┘                                                 •


























































```

*Figure from page 20 (2346x3317 px)*
