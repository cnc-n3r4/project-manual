# III SECTION 3 DATA INPUT OUTPUT OPERATION 2. OSP FORMAT I O FUNCTION OCR

*Converted from PDF: III-SECTION-3-DATA-INPUT-OUTPUT-OPERATION-2.-OSP-FORMAT-I-O-FUNCTION-OCR.PDF*

---


```text


                                                                                =--.- =.--.
                                                     :+=-=-=--.:-==:-=-:-:::--:+%%@#%=**@@-
                                                     :#*===+++:-+++=+*==-=+===+=.+=+=*===*:
         .==-==-::-:::::::--------:::::----------::.::..::..........::::::::....:..::.:::.
               :=. -:.-:::::.:.:::=::::::..::.:-::--.--=-:.::-::--:::::::.::::.:...:::::::
               =#. =++***#*#=*=%#*##++#**-+##*=#++%#:+**+--+=%*++#+=*+#*+.*++#-*#+-++%#*#+
                   ==#*=+#****-**=*=+***+=*=#+-*+=++*-++=#*+: +=-#*+*+=-=+*++##=++-%+
                   #%*##@%:=:*%*++*+:*++#==+*=-****#+.##****-:*=*+-#+****=*=+*==+++*+-=+=
                   =+++#++**+#++-#*++=#+*#+=#*+****%*:**=**#+*#=+++*#**+*=++**+=*+*%=++#-
                   %**::::--:-::.-.:-.--:--.------::-:--:--====:::=-=:=.:-==+=--=-:+:+--
                   ::-
               =*  ++---=:==+--==:-==::::-==:-+=-----:-=:-.
               -+  +*+=-*-=-==-==-+*= -.-==*.-=+=+=-+=++-+.
                   ++*       =##= - =++.-.- +*==+.#=*=.++=*-+*==+=-*#====+#=++=:-+=++
                   *#=++*: . .-:--=-#+--=:+-=*=+#=+==+=+==+-===+===+---=-++=**=-+=-++:..::
                   --:-.-. . :#+#@%%*%##%+#%%#-++==+=+*==+=-=*=*=+++.-:=.#+++**-+=-*=#*+#*.
                   ... . .:  -=+--==::+-==.=+:
                  .*#%+##++. .=:*%#*#%+#*-#**#+#@%***#%###*-*#*%****-=:=-###%%#+@++#*#*+%@.
                             =*%***+:+*+#*-+*-                                     . ..
                  .**%*-     .-.=+=+*+-*=:+==+-+#=====+====:-+=+--=-::.::---==--+::---::-=
                   ::..      =%#@@@#+%%%@**%@*:---=--==-==-.-+-+-==-.-.:.++====-+--*=+=-++.
                             .:::.:. .-.::.:-.





















































```

*Figure from page 1*

4203-E P-323

SECTION 3 DATA INPUT/OUTPUT OPERATION

(5)

If a directory is specified when using the DIR, COPY, or DELETE function, all the files contained

in that directory will be subject to the specified operation. If a directory is specified for the

RENAME or PROTECT function the message "directory" will be displayed on the console lines

and the operation will be aborted because it is only possible to rename or protect one file at a

time.

Meaning of the wild card "*" under different functions

(6)

DIR

Both"*" and"*·*" specify all file names with and without extension names.

DELETE

: "*" specifies file names without extension names and"*·*" specifies file names with

extension names only.

PROTECT; "*" specifies file names without extension names and"*·*" specifies file names with

extension names only.

COPY

"*" specifies file names without extension names and "*.*"specifies file names with

extension names only.


---


```text


                                                                               ---:: -.--.
                                                    .=::::-::.:-:::--:::::.:-.-+*#**-+=**:
                                                    .+-::---:.:---:-=:::--:::-: ----=-:--.
         ::::::::...:..:::::::::::.:::..:..::::::..::..:::..:::.......:::::::::::.....::.
         -     :--:-.-:.....:.:-::= ...:...          ..  ...   .      .............. ....
        -@.    +%@@#:%*@#%#@%=#%++%###%@%%#.

             .==-=*+=+=+*-+-=====--=++=-+=-+=+=--=+=-=+=-===-==:===-=:=++-=--=--=--=-+--=.
             :+*: .  ...... ............:....::.....:::.:.-:....:::::.... :..:.....:..::-.
             .::
        .:..   .:.:.::...-..:.::.
        :+::   :+++=*+=-:====-=++
             :-: ::-....::.:.:..:.:.::::..::.::.: :..: :.....:...:..:.:.:.......
             .-=.:-=::-:==:=:-=-=--.-==--:+=-+=-=:-:-=.=--=-:+-::=-:--=-+=-:==-=
                            .      .    .      .      .... .      ..........  .
                           .-           ::    .-  .    ..  .:     :           .:
                           .- -+=---*=- .:    .-  *#++===  .:     :  -=::-=-  .:
                           .:  .  ..... .:    .- .--=.     .:     :  .:. .:.  .-
                            :.. --..:...:.     :.....=:....:.     -:......  ..::
                               :-:  :.:              =.:.               -...
                              :+-   :-*.             ::*-               :.=-
                                ..  :          :.. . :. ...:.           :
                                ..  :.........=: .:.:::--- .:           -
                                .:...:........:: +#=::.:=- .+.......:::::
                                  ......      .- ...       ..
                                               :...........:
                                         ..  .. .       .
                                         -+-:==.+*+=*==-+=+==+-

              ::  :.:-:::::::.:.:::: ::..:.::.:::.-:::..:...::.::.::.:.::..: .....:.
              ::  ++**-+=*++=-=-+*++=#+=-+==+-+++-==+=+-==-=====+=-++*-=#+-*-+*+*=*=...
                  -+-+:-----=-:-:=-:=-.-=-+=-:--== =--=:-:======:-=-:==:-=-=:==-=====+-
                  -===.
               .                        .   .        .
              =+  =-++-+=*=+-:+=:*--+*+=-=+-+=-==-=+-==**-+*=-==+-+*+-=-==:=-+=++:=-*+
                  ===+==-=+==+:
                   .   ..    .
                ++ =-+=-=-++=--+===::--==-==-==++:++=:+=:+:-+++-====+:-:-=+=-==-=:=:====
                   ---:-+=+-++=-+:=+=-==-+=++==-+===+===:++-+*-==++-+++-++*++-+**+*+++*.
                   +==+.... ... . .... .. ....  ....:... ..    ..:...... .... .........
                   ...:
                +- =-:-==.::=-:---:=::=---:::---.--:=---.-==.=-:=:--=-:-=---:-::--==:-:
                :. =++*==-==++=-+*++==-=+=-+=-=+=-==++*+=:-:.-:.-.:---:::-:-::.:-:--.:.
                   .:-- .::::::.:.-.:: -:--::.::. ::::-::
                -: :-.:- ::::..:.::.:.:.:: ::::...........-:::.--..:.::.:-:::-::-::..
                -: -++=+-=++*+==+*++*+*=**==+=*+-==-==-=+-=*#+-+*-=+-=-:-==-:=--=--:-.
                   -:-- :.:--=::::----::::= --:=:--.=-=---:--.:::----.
              :-  :.. ...... .....  :. ... . .... :. .. .  . . .  ... .:.:... ::... ...
              -= .=+=++*#=++-+==+---+=-*+==+===++-*+-*+-*=+***+=+====--=-=+++:=+=:+:==+=
                  --.=--:.--=-==-::-=::=.:--+:--=-:=+-=:==+====-+=-=-*.
              ..  ...    ..  .. ...  .     ..     .                       ...  ..
              =+ .=+=++*#+==-+==+==-=-+++=-=++++-=*-+*-=+-+*++==-+=:++-==-==+=-*-=+:+=+=
                  +=:=++-.-======-:-+--*--===:=-+=-++=+-=+++++==+--+=+.






















```

*Figure from page 2*

4203-E P-324

SECTION 3 DATA INPUT/OUTPUT OPERATION


## 2.


## OSP Format 1/0 Function

The OSP format 1/0 function makes input/output of the part programs using an OSP format 3.5-i nch floppy

disk.

2-1.

Operation Overview

The "OSP format 1/0 function" means operations {1) (2) (3) and (4) in the illustration below.

Tape punch/

Tape reader

Memory(MD1)

printer

-~

(2)

(1)

(4)

(3)

,_

3.5-inch floppy

disk

Fig. 3-2 Operation Overview

(1)

A part program on paper tape can be read directly into a 3.5-inch floppy disk by using the

READ command in the PIP (transfer) mode, which is accessed from the PROG OPERATION

mode.


#### A part program can be output from the 3.5-inch floppy disk to the tape punch or printer in the

(2)

following manner:

(a) A part program stored in a 3.5-inch floppy disk can be output directly to a tape punch to punch

out a paper tape by using the PUNCH command in the PIP mode of the PROG OPERATION

mode.

(b) Similarly, a part program stored in a 3.5-inch floppy disk can be output directly to a printer to

create a process sheet by using the LIST command.

(c) The file names of part programs stored in a 3.5-inch floppy disk can be output directly to a

printer to create a directory of file names by using the DIR command.

(3)

Part programs stored in the memory of the NC can be copied to a 3.5-inch floppy disk by using

the COPY command in the PIP mode of the PROG OPERATION mode.

(4)

Part programs stored in a 3.5-inch floppy disk can be copied to the memory of the NC by using

the COPY command in the PIP mode of the PROG OPERATION mode.


---


```text


                                                                                ---:- -.--.
                                                     :=-:-:-::.::-:.---:::::--.=##%##-*+%@:
                                                     -*+--=+=-.-+==-++=--===--=- =-==+==-+:
          :::::-::::::::::::::::::::---:::::::::::--:....::.::::::::..........::::.:......
         .:..  .::....:...:.......:.........     .........................................
         -*++   =%#*+%%*+-******#*%#
                   .
               -*. =+=-**+=+++-*+++:=*++#+-*++=:++==*==-*-=+:=++-+#-=*+*-=+=++=*===*=++=
                   +==----==-=-=*+==+====-----------=---=------=-+-:---=--===+++=------=--:
                  :+.:::-::..   +**@%##++   .-:::.  ::=-:.=-:--:.+--:.-:::--:-:  -::-:. ..#
                  :-       .::::  -*+++=-   =@#**-  -:-*#**###-+.=-***++**+=#-.  =#*%##   *
                  .+=++==++:   ..:::::..=   :==-=-  -:  .==-=:   =   -=-=+   ::  .+=-+-   *
                  :%#+=*#+-:........:::-+.--::....:.=-....:::::::+:.......:::==:::-::::..:#
                  :%+=-**-.....:::::....=.+*+=......-:...........=.......:...=-..=##%*=...*
                  :+     .++-.#@*#+.....=.+=*+*:....-:...+%##:..:=...   ...:.=-...    ....+
                  :=     .++=.**##*+:...=.++*+-::::.-:...:---::::+...=-===:..=-..........:*
                  :+......*==.--=+==::::+-##*-.....:=-:::.   ....+.::+*#**...-:..::::::..:*
                  :*+++*-.+-: :----:   .=.==*++.    -:   ::::   .+ .         -:  ....... .*
                  :=     .=:- -=-=::    = ====      -.   -+==    =           :.           *
                  :-      ==-:--==-....:=-***=-=--::=-..:....:...+....:::::::=-.......:::-#
                  :+::::::+*+.**#+=....:=+**+.-**#*==-...........=....::.....-:..........:*
                  .##+:*#@@- .     ....:=:+*+=.   ..-:...........=...........=:..=##%*=...*
                  :#*=.-+*-.....:::.....=:+++=::::::=-..........:=....   ....+-:.=***+-...+
                  -#*=.+##-::::::.......=:***=......-:...........=.....::::::=:..-**#*=..:+
                  -#+=.#*+..............=:*+#**.....-:...........=...........=:..      ..-*
                  :#*=.+*=#*#-.:........=:*+#*+::...-:......::::.=...........=:..........-*
                  -#++:####*#+.........:*:*+#++.....-::::.:.....:+..:::..:...-:..........:*
                  :#+=.##**%%*.........:+:*+#++.....=-...........+...........-:..........:*
                  :%*=-###*##*+.....:::-=-#+%*+.....*-::::......:=:::::......=:...:::::::-#
                   --::-=+===-:..::::::--:==+=-....:--::::::....:-:::::::::..-:..::::::---=
              =+-+===+=+   :=--+-:===*=-:=-+::--=-=-+..=+:-:==-=-:-:=+==++=+=-+++=+=-=+.
              :::-::.:.:    .:.::.-::-:..:.::::.::-::. :-::::=---.: :------=-:--=--:---
               =+  ===+==+==+-=-:====+-+=-.=-:-+=---+=--
               ::  :::-:::::::::.:----:--:.-:::---:-=-::
                   #*++:-*=++=
                      ==-:  .. .:::.:::::.
                      *%+-  :: :+#+:+++++= ...
                      =+*-  :. :==-==.==++-**+
                      -+=.  :. .===++-++*+-**+
                   ---.:---:.--:--:..  ... ...
                   -++--++++-=+=-=:
                      -+:   .  .+==:=+=+:
                      -+*-  :. .+*+:=+++::-:--=-:---====-.---:-:-
                      =*+-  :. .**+:=++*-=+=+++*=+=+****+:++*=+==
                      -*=:  :. .*++:=++*:=+=+=++-==+++**+:+++=+-:
                      =+*-  .. .+*=.=++*:-====++-==+*++*+:+++=+-=
                      =+*-  .. .+*+-+***:=++++*+=+=+#**#*:++*=+=+
                   -::::--.::..:-=-:.:.. ......:......::...::.:..
                   =#*-+-==+===*=-=-
                      -+*:  ..  ===:=--+:--=-===-=:+++++=:===-=--
                      =++-  :. .**+-+==+-+==++++-+-*****=-+++=+--
                      =*+-  :. .**+-+===:===++++-+-**+**=-+++=+::
                      =+#-  :. .+++-+===:=====++-+-****+=-+===+-=
                      =+*=  :. .**+-++++:+++++*+-*=##*+*=-+++++-+
                                 .. .    .  .... .  ....   ....




















```

*Figure from page 3*

4203-E P-325

SECTION 3 DATA INPUT/OUTPUT OPERATION

2-2.

Operation Commands

(1)

The table given below indicates which command can be used with which input/output devices.

~

Sector

Tape Reading

Tape Punching

Printing

e

Device

Device

Device

Device

d

F2 DIR

Input

Output

F1

READ

Output

Input

Input

F2 PUNCH

Output

Output

F3PIP

F3 VERIFY

Input

Input

F4 COPY

Input Output

F5 FREE

Input

Output

F6 LIST

Input

Output

F2 INIT

Output

F3 DELETE

Output

F4 RENAME

Output

F1 PROTECT

Output

[Supplement]

For the operation of the commands, refer to Section 2 "PROGRAM OPERATION".

(2)

Peripheral Device Classification and Abbreviations

Sector devices

__..,


#### MD1:

User memory

FD0:

__..,

3.5-inch floppy disk

_,.

3.5-inch floppy disk

FD1:

Tape reading devices

TR:

Tape reader

----

_,,.

Tape reader connected at RS232C channel o


#### CNO:

Tape reader connected at RS232C channel 1

--,,.


#### CN1:

Tape reader connected at RS232C channel 2

--,,.


#### CN2:

Tape reader connected at RS232C channel 3


#### CN3:

-,.

Tape punching devices

CN0:

.....

Tape punch connected at RS232C channel 0

CN1:

_,.

Tape punch connected at RS232C channel 1

CN2:

_,.

Tape punch connected at RS232C channel 2

_.,.

Tape punch connected at RS232C channel 3

CN3:


---


```text


                                                                               -==:= -:-=:
                                                    .+=---==::.---:-==----:-=-=*#%#%=*+%@=
                                                     *+-:-==-:.+==-=*==--==-=+= -==-==--+:
         ::-------:::::::::::------:::::::::----:::--::::::::::...:::::::......:::::::::.
                  --:::..:.:::                     ......................................
                  ===+=+-*==+*
                     .=*    .  ====-=
                     :#*.  .:  +*=+++--::.::-.
                     :++:   :  ++:+*=+*+==#=*-......
                     :+**. .:  +=+*=:===+=+=-+=#####==*#++*=-
                     :**-  .:  +=+*=:+=+++++-+-*****--++-=+:.
                     :**+. .:  +==*=:+==+=*+=+=*****--++==+-:
                     :*##. .-  *++#=:++=*=*+=+=#****-=++====-
                     .-==   .  :--=:.=--=-==:=:+*+++--=+===--
              -#: -+=:++==-=+===:-=:-==-+=-==-=.
              .-. ::-:----:-=--=:--.:-----:---=-
                  =-:=*=+-=*==+=             .%*=:
                  -#+--++*===*==++            +*.   -==--==--+-.-=-==-.--:=.-=--===-:==+-:
                   --..::::-.-::::            .:   .%*+#%%##*%%*@#%@*+*%%*#%+#@##=-=-=====
                  :...    ..  .   .           .::   -=.=----:==-=--=::=--=.=::-..
                  -##==*+=+**-#+++*          .+**. .#*++*##+*#+=*#**#*-#*=%=+*%#%**#=*##*+
                                                    **.+**+*=+*+++##-+#*++=#-:#+:
                  +++#=+=#==++               .**.
                  ---:=*-=:---:.:..::::.::::.:--::..:::....::...:.:.....:.:....... ......
                  =*+=#***=+++#++===**+-***=*=*=++-=-#*=++=+==*=#+++-#+-*-++**%*=*=+***++=
                  =*-=++=+**.=**+#=
              .:  ...   .  .:.   ... .... . .. . ...  .
              =#. ++*+=*%#++%-*+****-+*+*=+-*=*#*+##+-*+=**++**#*#-+#=*-+=#*#**+-+=*=
                  =*%+===**+*-
               .  ...  . .:..
              =%. -=*+-#*=-#-+++*++-+#++=+-+==*****:-#-:*++:**+*+*=++-*-==%#*=+***-*:%*.
                  ++****-+**++=+##*%*+===#=+##-=-=#+*-+**=**+=#**-*#=*-+**=
                    ..            ... .  ...:..  .... .:..... :.. ...: .::.
        :+-=   =*++*:-*=*===+:+=++
        .-:-    =+-=::-.:-+-+:::=-
              :-  :::.::.::::.--::
              :-. ==--*===#**==+++:........                . ...            ...
                     +.......+**+.::::::+=*@#*###%#%%#@@##+:+:--#***#+*+=#%%---+-
                     #=++-::::=+=.....::+=-+===-==-=+==+++-.*...-*+*%***+**=...==
                     ****:              -:                  =   .+-*+++=+++-   --
                     *  -*-+++.         -:    :..           -   .+===**++++++  --
                     *  :++:+*.         ::    ++*.          -       .:.......  :-
                     #--+##=++:.......::=.   .*#            =....:..::::.......=-
                     *#*#.              -.   .++--:-=::-    =    *++*****+**=  ==
                     +  =*-+=*.         :.   .=+++==**++.   -   .===++*=++=+-  =-
                     =  :+=-+*          -.                  -    ::.:---:-:::  -=
                     +::=#%-**-:::::::-:+=::::::::----::::::*::::::::........::+-
              .:  :..:-::..   ....................................:::...........
              +*  *+#**==*=
                .. :.   . .:. .... :... .. .::......  .. .       .   .     .      ....
                *+ *+**=*++%==+*##=+%*===*==#%-+++**++=*-+*=*##+++-****+-#++***=+==*#+:+
                   =+=+=-++==----**-+*-++=**-=+**-+#*+-*+##++*=**-=*##*===*==*=+#-+:
                   #+***-=+*++%+               ..            .  .   ..          .
                   .   .    ...
                #=.#*+-++=**:+*#*-***==++++*-+##*+*=+**+=++*:++-*+-++*
                .  ..         .:. ...  ..  . ...... ..    .. .. .  ...
                += ==-=+=+#=:*+=+*.=:**=:++=:+-==-++-++++-*#-:**=+*++--+#+*==+*+-+*++*++:
                ...+++-#+#@:+=*#**#*-++*=*%#++**+=.. .::: ....::..::.. .:.........-:.::.
                   :-..-:=:.:..:::--...::.--:.-:::
                     +--::::.....:::::---=:.::.:-=+++++----::--
                    .+   *=-=-=++--==-   -:.....:**+*#+   ...=*
                     =   ::===:-=:.+=:   -:.:%@%-  -.+##*%%%=-*
                     +:*+-==:==---=:-===.+:.:---:..--:-:--:-:=+
                    .* =--=%++#%**%=-++= =   =**-  :.  +=+=  .=
                    .*-::-:+%%@*=+#=::::-*=--===:::=-::-:----=-
                       ....          ....  ..              ...









```

*Figure from page 4*

4203-E P-326

SECTION 3 DATA INPUT/OUTPUT OPERATION


# CN: -

Printing devices


# PN: -

Console

NC operation panel


# CN1: -


#### CNO:

Printer connected at RS232C channel 0

-+

Printer connected at RS232C channel 1


#### CN2:

Printer connected at RS232C channel 2

-+

__,.


#### CNS:

Printer connected at RS232C channel 3

{3)

The default devices are indicated below.


#### MD1:

For sector devices

Tape reading devices

TR:

{This automatic selection can be changed by setting

NC optional parameter (word) No. 57.)

Tape punching devices

CN0

{This automatic selection can be changed by setting

NC optional parameter (word) No. 45.)


#### PN:

Printing devices

The default device for a tape reading device or tape punching device can be changed by changing

the parameter settings.

(4}

If the output NC program name is not specified, the input program name is assigned to the

output program.

(5)

If the input NC program name is not specified, the name assigned will be A.MIN unless an NC

program name is specified on the tape, in which case that name will be used.

2-3.

Types of Floppy Disk

{1}

3.5-inch Floppy Disks

Recommended Maker

Format for OSP

Type

2DD

9 sectors/track

80 track

512 bytes/sector

TDK

135 TPI

3M

2HD

18 sectors/track

Hitachi Maxell

80 track

512 bytes/sector

135 TPI

(2)

Supplement

(a} Since the NC creates files in the OSP format (a flle management system exclusive to OSP), it

cannot write to or read the 3.5-inch floppy disks containing files created in the format on

another computer.

(b) New 3.5-inch floppy disks must be initialized before they can be used.

(c) The storage capacity of each type of 3.5-inch floppy disk, expressed in terms of the equivalent

tape length, is indicated in the table below.

3.5-lnch

Floppy Disk Type

2DD

2HD/2HC

Storage Capacity (tape

1840

3770

length) [m]
