# III SECTION 2 PROGRAM OPERATION 09. TIME OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-09.-TIME-OCR.PDF*

---


```text


                                                                               .::::. :.::
                                                             .-::::::. .-::::::=+**+=-==#+
                                                             .+--:-=--.:==-===+=.=--==---=
         .:::::::.:...:::::::::..::::::::::.::::..::::::::::::........:.........:.........
         .:     --...                              ............  . .......................
         +@     *%@%@+

              :==:*--:=--:=--=-::--==-.--:=-----:--=:-==--=:---=:-:----:-+ :=--=--..=--.=-
              -=====-===+-=--+=:===++===---++=+===:: :::..::::::...::::.::  ::::::..:--.--
              ::::.:.:..:.:. ::.::::..::.:.--:---.
         -=+++====:..::=-::--:--::--::.:::-::::.:------::-:::::----=-:--:::::-::..:::::::-.
         ==@#++%*%:-:..+==--=-=-=:=+-=-==--===+=----+--==+==--==:===+=+++:-+=--=+:+=.==-=+.
         -:::.....: -..=+++=:--====-==+.                                                 .:
              :-:.::-+===++++=-=-=-=-=*===--==-=:....:::::::.......:::::.....:::.:.....:::
              .:-.-:.:.--:.:-:::.:.-..::---:=-:-
               ::  -::::::--:.::.-:.:--=-
               ::  ::--.::---.--.:.:.:-=-
                   --:-+=-==:-.====-=:-:-=:-==-=-==----==:--==-:----==:-===:-:=-:---:----:
                    .....:.::...:.:::....:........:.....:.::::..:::.::.:::-.:.::.:-:.:.:::
                        :-
                        -++-=-*--++=+::+:====
                        ==*-===:==*=+- .  ..
                        :.:.......:.:.
                     :                                                        :
                     -   -*.                                                  :
                     :   -=:  ....- ..    :..:::                              :
                     -   =##::=*+:#+#*.   -::--=                             .:
                     : .==:--:==-.--==:... .     ::::-:.:.  ..:::-...:...... .:
                     : .: .:  - ..  ..:..:..:-:-:::*=#= :.-:. ::**: .:        :
                     .:: .=#  :.=-: ..====: -**#+..*=:#-.:*+. ..+-+- .:+++*+.:.
                       =.:. ::::...:.:...:.:.. ...:::::...  ...::::........::
                       .::+=:-:-=+--:--+=:::-+*:-:--*--.--++:-:-==--:--==-:
                      ..-:=-.+---+-:--:==.--:-+:----+--:--+*.+-:+=:----++:=
                      :  . ..-:-:... :-::-..--:.  .....  .. .  ...:. .. ..
                      ::=       .::.-=+=----=++:
                      :=#+=**=*+*+=+=+#-...
                      :----=-::--=.::-====-
               =- .--:-:-:::---:---:-:::-::-:-:-::-:.:.:: :::-: ::.:::::..::..:::::::: .
               -: .:-.:.:::::-:::-:::-:-=::-:------:.-:--.-----.--:-=---::=-::=---=-:=..
                  -==+-+=  =-+--
                       .
               =- :--=--=:==+-=:==.
               :. ..:::.:..::.:.:-.
                  :+==:===:=+=-=-:=+=-=+===-====+=:=--==+=:++==+--+--+:++-.++:-=+-:===.-=-
                  :==-                         . .    . .. ....:. .... .:. .:.. ...... ...
                  .:..
                  ::.-=.-+*::+- -=.=+::==+==.-=-=-+::+-.+-++-.*++++-.==+-.+==.+=*=+=.-+++.
                  .=+==+===*=:++=++:=--=+--=-==-=++.           .  .                   :..
                    .  . .. . .. ..   . .     .  ..
             .*=+===-=+-   -  :=-=.-=-.===.--::=--:-::=.---=--:=-----:.-::==--:-=.== ---=-
                ..            -==+:++-+***+-+=.-++-=**=--=+++=-=+-===--+- ::....: :. ..:::
                              ::.:..: ... . ::  .: .:: ...::::.::.:::.:-:
                           =  :==:+=--=+=+:=-==-:-=-=-=+:
                                   :...  .   :::.....::.
                                   ---.      ::=:-=+.=-
                                   ==:-=     ::=:--=:=-
                                   -::--     .:-:::-.--
                                   -=--=-    ::=---=.==
                           -  :--.:-:::.:-.::::.-::-..:.::.:...::..:.:.:....:....:.......:
                           -  -++-==-++:=+-===+-===+=-=-==-+==----+=----:--:-:---=-:-===-=
                              ---:-::==:---:=:-+:----:===:--=-*-














```

*Figure from page 1*

4203-E P-267

SECTION 2 PROGRAM OPERATION


## 9.


# Time

The NC's clock function contains counting time even when the power is turned off. Therefore, when the

power is turned on, the current time is displayed.

: Sincethistimedataisveryimportantforthefunctions such as MacMan, alarm log, etc., do not


### NOTICE

change it inadvertently.

The operating procedure is as indicated below.

(1)

Press function key [F1] (TIME).

The following is displayed on the console line and the system becomes ready for the lnput of time.

=T

1994.9.30 FRIDAY 15:13:52

enter time (H:M:S)!

=EX

=T

15: 13:52

1994. 9.30 FRIDAY

enter time (H:M:s)

RUN

BLANK

DELETE

RENAME

DEF I NE

FREE

INIT

QUIDE

[EXTEND]

Press [F1J (TIME).

"=T

1994.9:30 FRIDAY15:13:52

enter time (H:M:S)!" is displayed.

(2)

Key in the present time through the keyboard: hours, minute, and second, each delimited by":".

Example: 8:30:5

(3)

Press the WRITE key.

When time data has been entered correctly, the screen displays the set date, day of the week, and

time.

If time data has not ben entered correctly, the screen displays "enter time (H:M:S)!" again,

requesting the operator to enter correct data.

1.

When time data only needs to be checked and does not need to be set, simply

[Supplement]

press the WRITE key. The TIME command will terminate.

2.

The data setting range is as follows.

0through 23

Hour

0 through 59

Minute

0 through 59

Second

3.

After 23-hour 59-minute 59 second, the time changes to 0-hour 0-minute 0-second

and the date and the day of the week change.
