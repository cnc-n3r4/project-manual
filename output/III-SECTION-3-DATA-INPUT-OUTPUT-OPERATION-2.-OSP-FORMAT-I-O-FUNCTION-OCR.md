# III SECTION 3 DATA INPUT OUTPUT OPERATION 2. OSP FORMAT I O FUNCTION OCR

*Converted from PDF: III-SECTION-3-DATA-INPUT-OUTPUT-OPERATION-2.-OSP-FORMAT-I-O-FUNCTION-OCR.PDF*

---



4203-E P-323



SECTION 3 DATA INPUT/OUTPUT OPERATION



(5) If a directory is specified when using the DIR, COPY, or DELETE function, all the files contained



in that directory will be subject to the specified operation. If a directory is specified for the



RENAME or PROTECT function the message "directory" will be displayed on the console lines



and the operation will be aborted because it is only possible to rename or protect one file at a



time.



(6) Meaning of the wild card "*" under different functions



DIR Both"*" and"*·*" specify all file names with and without extension names.



DELETE : "*" specifies file names without extension names and"*·*" specifies file names with



extension names only.



PROTECT; "*" specifies file names without extension names and"*·*" specifies file names with



extension names only.



COPY "*" specifies file names without extension names and "*.*"specifies file names with



extension names only.


```text


                                                                                                ```'.^ "'''`.
                                                                .''.''...   . .'    . .    ... :[-_?!] ~l+]];
                                                                <)]<<_~-]!_.+~??+!]]~<>i<+>+++<_"<?--~?+>~~];
           .^^^^^^^`````````````^^^^`^^^^``''''```'`''`'``'''''''```'.'.''`.''''''''.^.''``'..`..`'.^'``'```'
           '::::::,`^""^^`^'```^",,":""","^`"^","::,",:;,,:"^`":::,:::"""^^""^^^",:::,:;;,,:,""^""::::,:::::`
                  ,-l  i::"+IIilI:"I^iIII<!l:;lIl^`I!;:"iI^l!~^'!lilI."",ii"Ili!^I",II"" ;;,I"`!:"'`^";:,":"
                  ^I, .l:_l+I<~<<~l<,_~+i<i>I+><~Ii<++?;>~l!_+!;!i<I!;>!:i-iiI~<:~<>~+>!"-il__:+-~;>~i__i~_l
                      .<l_<+;~_~>>~_!!+>I_li~~~~>I<l!<i,+!<Iii<lI<i>!]!i: l:i:_>+!>!i'<"_!>><~_;I<,>_>
                      '_?i_<-]]`l":>?<ilii!^I>!l-!!"<i!"i~<>~+_""-~<<~i>;^<<:<>'~<i~~<~<,<!;~i:!i!>!~!;i>_;
                      .i!i;~+;!<+>>-!~,!-ii~,<~>>+<!!+<!<!~<>__I;<>l!>>+>!?ll!li>>_i~l<Ili!<i+I!<il-+;i!<l`
                      '?>~I^:^";:,,;",',;^"I^:;:,:I""l;;l:l;^":,:;I:;I;llIi,::^iIIl,i'I^i;I<!i,IIi^l>"~;i`
                      .l:!I
                  ^l` .:"''`^`.`",,^'^""'``^^`'`.'`^`''",'''```..'`...
                  ![l `--i~i>?!>ii_<,_!~:+_>;'!`;<<~_^l~_~i+<I<<i_-i><
                      'lI+'        I>;i'",^^;:;^:.`"';;,"l:'l:;l"^::,,:`,:I`"",^";;^`"`^":^^"^^'`^^^^^
                      'i!i^'`'. .. !<><'`l'!il!'I";,.~~ii!<"_;I<I^>~I>+">l>"i!i">~<lii;<<_!!_!l,l<i!<~
                      ^+]<>->[l '. .I"`_<~i]+<;~~,i_ii~I!_?>l<i!~_>!<!!;l~i~+l!~il^l'!"I~!ii_<iI~!"l>l~~Ii++`
                                   !___<-~_ll+_l__;<+[>'''..`^'^^^^`^``''"`^,^"^^' ^'" ^I,,"^::'^,`";";;"::,.
                      `ii!:I!;:!^  :,::,;;;l,;;;::"::I;'`^;^'.'''`'''.'.'.'..  ...'   '    .^  .'          .
                      ^!i~!;<iIl^. "<Il{]]~~_]!-_ii]~__!<_-+<<i++-~~+<i;~?>~?>+~+I:i^>">?--_[?-i}_!_?<-?!_]{"
                                   i>__I<i!,^>>I>_"IIi;
                      ,+<?_<"   '. ';'^>!l!+>l:+!^l!;!i:l+_!!!l!i>l!ill"lii!>:I!I:::':":IlIl<I;l<:"lI:::^:!i.
                      .^^".'    .  l?~-}[]->>}_-]_i?+}~^:;::I;,lI!;;!;;^;illi:l!;^`;`;.I<i!I!i!;i!"<<Iii:i><'
                                   ,::I^::,`.I;";I`:,l"


























































```

*Figure from page 1 (2332x3298 px)*


---


## 2. OSP Format 1/0 Function

4203-E P-324



SECTION 3 DATA INPUT/OUTPUT OPERATION



The OSP format 1/0 function makes input/output of the part programs using an OSP format 3.5-i nch floppy



disk.



2-1. Operation Overview



The "OSP format 1/0 function" means operations {1) (2) (3) and (4) in the illustration below.



Tape punch/



Memory(MD1) Tape reader



printer



(4) (3) (2) (1)



3.5-inch floppy ,_



disk



Fig. 3-2 Operation Overview



(1) A part program on paper tape can be read directly into a 3.5-inch floppy disk by using the



READ command in the PIP (transfer) mode, which is accessed from the PROG OPERATION



mode.



(2) A part program can be output from the 3.5-inch floppy disk to the tape punch or printer in the



following manner:



(a) A part program stored in a 3.5-inch floppy disk can be output directly to a tape punch to punch



out a paper tape by using the PUNCH command in the PIP mode of the PROG OPERATION



mode.



(b) Similarly, a part program stored in a 3.5-inch floppy disk can be output directly to a printer to



create a process sheet by using the LIST command.



(c) The file names of part programs stored in a 3.5-inch floppy disk can be output directly to a



printer to create a directory of file names by using the DIR command.



(3) Part programs stored in the memory of the NC can be copied to a 3.5-inch floppy disk by using



the COPY command in the PIP mode of the PROG OPERATION mode.



(4) Part programs stored in a 3.5-inch floppy disk can be copied to the memory of the NC by using



the COPY command in the PIP mode of the PROG OPERATION mode.


```text


                                                                                              '"""^`` :'^^".
                                                               ''.''.''... '... ..'' '.'  .'. !?-]-<<'~I-?-"
                                                               -{<<l<+?~li`-_~<<<[->ii>+~!!~>il^~-+??_~>~<-"
          '^``````^^^`````````^^`^```^^`^`''`''''''''''''''..''''''..'.'''''...''...`.''''..'`.'`. '.''.'''.
          '^::::::""^```,````^"""^,:""":"^^^^`''^```,,;;;;:,,:;;;;;;;;;;;;;;;:::::::;;;II;III;II;;:,:,:;III'
          l[      !]-1+)^]_>ii<>!_!;i_]^[];l!l>_i!lI
          <{,     !]_{-<'?l{}-}]{|<!__["-i{[-{[}[1]+.
                ''
                I>~l<_1~>?+_-}i++>__+_~~l<+]-]~>?_i+_~]-<i!<-_><+]<i~>?+<<_!l--<~i+;<+[<i+>>+~i<~!!>~l-<<<~"
                !<_!...  '..'`... `'''''..'`'`'.^^`''`^"`.'.''`"^"'"``I^^``'`"^`;^^.''^..^``"^`^`''^^'`":,;'
                :;;"
          '`.`     ^.....`'..."' ...'...
          <-,<.   !_[?}~{}-+>;-_~[+~_[}>
                ^`  "``'^.... . ''.' ... ..                 .
                i<];;+_}!I_>>_];~+;_+<+_>>^<__?>~,--_>[?>~+,<>"?_"-_,]i<;_-,>I]~;<<<-<?-~<I__~~~
                                  ..'''''...''`'' ''. ...''''''``'^^'^''.'' ...'''^^^`^^`''```''
                                 ,I^``````^`````:!      ;"``..''`^``^``,,      :^",,,:,,"^^^^^;`
                                 ;^ ..     .'.  `i      l. .;,".,",I'  `I      I              ,,
                                 I" l-~<<<i]-!! `I      >' ^]([?~l!>"  ^;      ;  '+_<Ii___"  :"
                                 ;^             `I      i' `:"";       ^I      I    .   .     l:
                                 ^,^^``-,^^!:""","      ""^^",,:]"^^""":"      :;,""^^":^^^"""I^
                                    .,">.  ;.,"                '>.,^                  ^l.^`
                                    "_<;   :"_-.               .:;?>                  ^;"<>
                                       I   ;            ^^^````^;"^^""^,^             ^I
                                       ;   I"^^''''''``;<. ``'`^^"^^^' ""             'l
                                       l...'^^^````````:>. _]+!<!l<_]l ^],^^^^^^^"::::I;
                                       ^^,::,,,^^^^^^^^`l  I!l         `l..............
                                                        l:"^''"""""""""I"
                                                         .
                                                 :!I':Il^"ill;ll:;^i;;l,;;I'
                                                 ":~":Il`"i+<l<i!!"!lii;!i>`

                 l!^ ^!^!il:!;l!II:^l^:llI!'Iil,"l!^!l^;llI"~IIl!",l!^;"l:I:;;;"l:;;"^i;,^;^`:::"^l:'
                 ::^ ,_--]>!~!?-<<ll>l>-]<+i][~il~~i<+:<~~~Iii_<<~;>>Iil>i>!><<;<<-->;[]~l]>l-_+[!~]l^"^
                     `<~l~!^>!!!l~<>:i"!<i;>_`Ii~>>?<i;>!!++ i~l>>"<^+><~~+~<:>><;!~<:l<~!<lI_!>~+<><~~_
                     "<><_I
                       .  .
                 ~]" ,<:~~;I~i+>><:"<<;i?:i<[+<ii>~<l-~:~!+;><<;->__>"]~~:+,_<li-<<:iIi>>">:!<!_+;!!!-~^
                 ^^. ;<+~+<<<;-_<<>~!^'`"'`",,"`'^^`'^"'^`^'^"`.^,;;:',""','^"^`;;,^,"^,^',':,^,;`^^`,;'
                     ';",:;^i^^;,";l`
                   :l` I'"":',^^,""^`l:::;^,`,":I^,::^I:,:,';l;^^,:^:,'"":",^::"":"','^`,^"`^^^`:`,`'^^^""
                   !+,^<i_+l><l??~<ll+<ii>;i:iiiii<~+!<+<++I~_+Il+~:~-"~-]-~I~~~<<-;~,~i?]_<~+~+-l+>~~_+~l
                      '!!,l,>+<+"!_~+"_i"~_i_:~<;iii_+i>,>>>>!<_>!!;!_~I>+;:+i+],ii~+>l~<+i+Il_+_~--<>~-l
                    . ^_<>]>           .    '.                .              .. ..                    .
                       ..''.
                   +_"`-il><<<'l,!<>"!;iiI<!^~<lii,!`!:!I;:l>Il<i!!::~~>">~:i<:Il~!!lI+iii<"<,;:lii<<,il
                   ::'`<<i_-I~:<!<+>i!!-?<+i!!l>+>I>i>;!~~i;>!i<__+<I;l:^l!^,l",;!ll,,I;l:!"l"::!;;!!`;;
                      `:;!<l`I:l:II!>^!;l<;,<":i!;+;!l^Il!"'l!l!I<!l:
                   ^"' :^'.:^ ```'`. ".'`' `.''.''. `'''^.'..''' ..`.,^``'.^""`'``'^`.''^'`'^^''"'.`..
                   i~,.i~_:--:>_~>-i!~i_[>!->?_~]_>;?<i-_;!:>l!<;Ii+:i~][?;>-]lI~i:<-,i<?~~I+__~-_;?,+^
                      "~>~_>"+:!~+_[liI_i_~-<_;i<![>^~<!+_I_~"~->_l>+ii_[<I>!!<<_i+,
                      .           .  .   ... ..      .  .. .' `. ^`  .     '.   `...
                .+[^ I<+>;>I><<~ii^+il<~;!"+~;,>>!!I>`lil>l:-<^;+l">i^!i>>>:i:;;!;i"!>+;?<~<i"?~_:~l"<~>+`
                 ^^. l<~;+_~]];ii~i~<<>ill!+<l+-~l~i~_I!i+_li?~__-I<?~?[]-]<<-+l>!>+:""',;I;;',,:'::`:,"i'
                     ^:,':":`` "::;,:I,""^:;;`^:.`::,i`;,;;I',;;:l""l,!;;l::;l;^l;I~^
                 ;l' ":,:."^`"","^.:"^",^, ``",`"^"';^"^^ '^:' `^.^" ''``''`'.^^ ``.^^^`',,:"`,:,^"''""^^
                .i~` l>_!>?+}}<~i~;-<i~+l<;+l>-<+>~;~+-~]!i>]<i?-l>]l~-]+-<<~l<_;!+~!>i~,~l~~!!_!I-i;_<>{^
                     l+<"<i_i!^l>>>><+iiI;!+~:i?l:<<>~,il<_i:+~_>-lI_<_~+-<<<-i:+<<_,
                                                                            .    ....























```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-325



SECTION 3 DATA INPUT/OUTPUT OPERATION



2-2. Operation Commands



(1) The table given below indicates which command can be used with which input/output devices.



~ Sector Tape Reading Tape Punching Printing



Device Device Device Device



F2 DIR Input Output



F1 READ Output Input



F2 PUNCH Input Output



F3PIP Output



F3 VERIFY Input



Input



F4 COPY Input Output



F5 FREE Input Output



F6 LIST Input Output



F2 INIT Output



F3 DELETE Output



F4 RENAME Output



F1 PROTECT Output



[Supplement] For the operation of the commands, refer to Section 2 "PROGRAM OPERATION".



(2) Peripheral Device Classification and Abbreviations



Sector devices


#### User memory MD1: __..,

FD0: __.., 3.5-inch floppy disk



FD1: _,. 3.5-inch floppy disk



Tape reading devices



TR:



----



Tape reader


#### CNO:

_,,.



Tape reader connected at RS232C channel



CN1: --,,. Tape reader connected at RS232C channel 1



CN2: --,,. Tape reader connected at RS232C channel 2



CN3: -,. Tape reader connected at RS232C channel 3



Tape punching devices



CN0: ..... Tape punch connected at RS232C channel 0



CN1: _,. Tape punch connected at RS232C channel 1



CN2: _,. Tape punch connected at RS232C channel 2



CN3: _.,. Tape punch connected at RS232C channel 3


```text


                                                                                               .^````" ,.''^.
                                                                  . ..        ..    . .    ..  l[-?-~+ -:-]},
                                                                _1-~>+~]-l<'-_-~<<[]_i>i+~<~+<<>^<?~__-++~<]l
           .'''..'''''''''''''.'....''''''''................... '`''..`''''.`''.''`' ` ''''..'`..`'.`'`'.`'`.
           '^"`",:;:,,:,:,",,,,"""^^"""""",;III;::::,,,:,::IIII:,:,:IIIIIIIIIIIIIII;:,::::;;;I;II;II;I;:::,:'
           ,i^<    ,il:::IiI::`!::;;I;;;;iI
           ;<:+`   :i]<<!--~<l"ii~><>i?>~--'
                  ..   `.     .            ..' ..   .. .   .          .        ..  .  .
                  I~!  i<_;+?--;-i~+l+__~_"><]<-?-l!_~~~"><~i!_+>!;_-"~_,!+~+;+]-"__<_<:~~i<<<>?i~;?~<<<-:
                      ^~!!I;:,:;!;IIII><!!!i!lI;!:::::::;;;;I;;l::;II;:I;I;III>:,,:::lIII!lll>!i!I:;;::;Il;;I
                      l!^,::;;:"^'..  !_-_{[]+]l+....`I""""`...!`!:"^"!""";"^'~:;""`I:^",:""^>'..":^":"`''''}.
                      I:       .`","""'  !-~<+_l!    !)?~_~"   <.>--]l??-?~!-.i;---<<i_~_~>]<;   I++~}<}:   ].
                      ;!lIlII;l:;   .'`"",,"^`'.l    !~~!i<:   >   .<>!i>>    >   .<<ii><    l   '<-<i~_    ].
                      !]+~<+<_-i<^^`^"^^"",:IIIl_`^`'.`""""""^^<^^^^"",",",,,,~"^^^``^^"",,""+,""^^''.''`^`^}.
                      !}__._-[l   .'  ...'`''...>'i<_>~''````''i'''''''''`````>''''''''`^^^^^~^^^,]-[}+~`'''[.
                      i~",^""^"!>i:^<]~~+!,,"^^^<`l>i<ll;^^^^``>`'`':!!l!,""""<```````^,,""",-""""::;l;,````-
                      iI       i!I,'>]~~_l`^^^``<`l<i-_-l"""""^>````;_[]]:^"^^<```''....'^^^^~^^^^'....''''^_
                      >I      .<<-!'_+-}[-];``'`<'i__<>.'^^^^^`>'''''..''^^^^^<```"?~_?__^^^^<^^^``''''''''^]
                      !<;::lI,._":"^^`,"""^"::::_:~?-_!;:`^^^",+,,,,^'''.````^_""",ll!!l;```^<``^,:::::::"^^[
                      !+I<l!>,.>!i: I~!i>!l'    < :l!~i<"      !    ^II,I.    ~              !              ?
                      >I      .i`:" ,I:,;`".    ~ l!ili       .<    `I>l!.    ~              l              ?
                      !;       ii!;,l!!>!;`^^^^"<,~~__>;>lI:",^_``^""^`^`""^`^~````^"",,,,,,,~^^^^^^^^^,,:::[
                      l!^`^^^`^!~+!`+_--<i`^^^^">I_+<<`^+_-[_+^~^^^^`````````^>^^^^^^^^'''```>''``''...'^```]
                      ;]??^>-]1{-.'`... ..'`^^^"~^<~~><'...'.'^!^^^^^````''''^>"""""""^```'``<'`^;-+??~+"```?
                      i-~+':;>~i:`'''"""""""""`^>`!!>i!",,,,,,:<"``'````^"""""<"^''''''''^"^,_""":~<~_ii```^+
                      >-~_'I![+l`^^^^^^^`''''''`>'<+~+i.`^``''`!'''``````^^```i`''''``````^^"~'`':?_]]+_```^+
                      >-<~`!]~-:^^^""""^^``````^<^>+~->~;^^`'`^!```^"""""^^^^^i`````"""""""",i`````^^"^^^"":]
                      >_><';<<!;IIl,"""""``````^>`<+<?~+;""^^`^!````^""""""""^i````'`^^^^^^^"<^^`````````^^:[
                      >-~-`l-?>[?~},````'''''``^+`<~~]~_:``'''`l'```^^^^`````^~'''```^^^````^i'''''''''''``"]
                      >-i_"i[-]--?[_`````````^^,?^>~<?><,`````^i^"""""""`````^~'`^"""""""^'`^!'`'''''`^"""^,[
                      >?>~^l_+~__?+i"`''''`"""",~"<~>]>~,`````,_^^^^^`'''''''^<^^^^^^^^`'```^i```^^""""^^^^,]
                    . i}+~"_-[[-_{-__^^`^^^"""",>"_-_)+-:^^^^^:-^""""^^^`````"i^"^"""^"^^^``^>`^`^^""""""^^,}
                      ',",",,;I;:;::"^^"^",,,,::l,;;I!I:"^^^^":I;:,,,:,:"^^^^^I:::,,,,,,,"``":^`^",,:::,:;;I!
                 <_l><><i>i>!   .ill;<!"lii!<+II`i;ii:"I;!lliIi!."i>!^i^i>I!ll";,:><iIi<<i<<,!>~>ii<!l!<:
                 :"^;I,,^,"",    '^"'";':;;":;,`':`,;,^;`"",I"::.`;;l`I^:!lIIl^:^`:;I;Illl!l^l:I!;!I,;Il^.
                  ;i' ^iIIll;ll!;il:I:`II;:;iI"iI,"^;,,,l;::",:l:,"
                  li" `^;;i;!;;I^Il;l!,;l<i>>il~i!,I>I;:i>!i!l<~!I!^
                      ^_iI!!`l~;!l!;
                      .;I;Il^;!::II:                .
                          "[_II   ^' 'i>-~^i~~i~!>
                          ,_<<I  ';`  >l~I!l!;~ii<:"<!i
                          ,<><I  ':^ .>l<Ii!I"~i<i!,->~
                          'll:^   ,.  !;!li!l,<>+<i:_>~.
                      `~i!l.l!!~i!^<il;I!"
                       :i!!^l!!l;<"ll;I;I^
                          .><"    ".  i>i<:i<<i+:
                          ^!~<l. '"`  l<<<"l>>i<:"::,;:Il;^;::!!ll!I,^I;;,,;";.
                          "~+~!  ."`  >~~~"l<<<~:l>il~><~~;<!!++++_~;I><+!!~;>.
                          ">+I:  ."`  >~<~"l<i<+,;>i!iii>>:>li~<<~~<;;<i<ii<^:
                          "<<~!  ."`  !~<>^I<><+";i!!i>>~>;>l>_~<~~~;;~i<!>+:<.
                          ,<~+i. ',` .i~~<,!>><~"Ii!!ii><i;>l!_~~~+~;:<i<!!<:<.
                          'I;l;   `.  ,i>!^!>>i>^;!!!!ii>!:<l:<>i<<i;;>i<ll<:>.
                      "__+i:i;!i<<iIl-li!>i
                       ^I;,Il;,"^";:^:;:,:,  . '       . .   ''.....  .      .
                          "<+?l   ".  i<~+:+il<_;>!<i>i+<~;~,~_____~:!<_<i<~li
                          ,i<i;  ',' .i~<<:<!lli"!l!lii<>i:~,~+~<~<>,!i<il!>^,
                          ,>+<I  ','  i+<<:<>l!i"!lil>i<<>;_:~_+<+~>,i><i!i>":
                          "i<_l  .,'  i~<>:<illi"ll!l>!<>!;~,~~+~~>>,i>il!>iI!
                          :<~_>  ':'  +_~~:<i<>>">>i><>~~>:-I---~~_~:i<~>><il<
                           '.`'   .   .^"^'^^'`'.^```^^^^`'"..`^^`^'.``"^`^`'`






















```

*Figure from page 3 (2346x3317 px)*


---



Printing devices


#### CN:

4203-E P-326



SECTION 3 DATA INPUT/OUTPUT OPERATION



Console


#### PN:

NC operation panel


#### CNO: -+ Printer connected at RS232C channel 0


#### CN1:

Printer connected at RS232C channel 1


#### CN2: -+ Printer connected at RS232C channel 2


#### CNS:

__,.



Printer connected at RS232C channel 3



{3) The default devices are indicated below.


#### MD1: For sector devices

Tape reading devices TR: {This automatic selection can be changed by setting



NC optional parameter (word) No. 57.)



Tape punching devices CN0 {This automatic selection can be changed by setting



NC optional parameter (word) No. 45.)


#### Printing devices PN:

The default device for a tape reading device or tape punching device can be changed by changing



the parameter settings.



(4} If the output NC program name is not specified, the input program name is assigned to the



output program.



(5) If the input NC program name is not specified, the name assigned will be A.MIN unless an NC



program name is specified on the tape, in which case that name will be used.



2-3. Types of Floppy Disk



{1} 3.5-inch Floppy Disks



Type Recommended Maker Format for OSP



2DD 9 sectors/track



80 track 512 bytes/sector



TDK



135 TPI



2HD 18 sectors/track



Hitachi Maxell



80 track 512 bytes/sector



135 TPI



(2) Supplement



(a} Since the NC creates files in the OSP format (a flle management system exclusive to OSP), it



cannot write to or read the 3.5-inch floppy disks containing files created in the format on



another computer.



(b) New 3.5-inch floppy disks must be initialized before they can be used.



(c) The storage capacity of each type of 3.5-inch floppy disk, expressed in terms of the equivalent



tape length, is indicated in the table below.



3.5-lnch



Floppy Disk Type



2DD 2HD/2HC



Storage Capacity (tape



1840 3770



length) [m]


```text


                                                                                               ^""^`, :``^,'
                                                               .'''''.'. . '.''. ..' '... ''' :-??->].~I+[};
                                                               i1_>i<<-?I~ +_+~_l][+~~i+_>>_]+~^>?~]<--i~+[;
          .```````````^`````''```````````'''''''''''''''''.''''''''..'''''.'...''''.`.''''   `..`'.`'''''''.
          ',",::::::::""^^^^^^`^^^"";;;;;:,,",,"""",::;;;:,,:;;;;;;;;;;;;;::::::;III;II;::,::,::;;IIIIIII;:`
                     ._!;!!!:;<Ill!!
                     .,",;;i!,!;:;ll.
                          i<~.   ^^  l><~~i<l
                         '~~i.   ^"  I~<,ii>!ll;:`;;,l:
                         '!>>^   ^"  I~l,<<>l~><!;+<l~I.^`''''' ..    ...
                         'i<_~`  ^"  ilii<>`!l!!<!><!,+;__----~:><-~!~<!!
                         '>~<I.  ",  !!!i~i^i!ii>!<ii:~,>~~~~~>"l!<!;>!""
                         '><~i'  ^"  !!li~!^!!ll<!><i;~:~~~~<~>"!i<!I<!::
                         '>>_+'  ^"  i<li+l^lill<l><i;~:+~~<<<i"il>i;>ll;
                         '>~_~'  ",  i<<i_!^i>ii~i~<<I_;_?-+__~,<<~ii<ll!
                 ."'  ,^'."^,^'^.^'''''''^''^"``"^^,^'"'''`'`''.'.^''`'''
                 ![i  l!~:<_+<><,[<><~-:?<l!<?<~?-+i__~>+
                     'l""^;,::,'!,,,,:.               .!i;:'
                     `!;:,~iliI,_i!!i<'               .-?il^
                      <]+<`i~~_<<:<_!i<_<              l+>    ;<i~!l~<>ii_+;:<~>!+il"!~:!<"l~<ii+~~<>I~~?>>;
                       ^^'.'```."`'^''``'               ..    <-<I--{_+_<_]-_}+][[l<_-]-<-[~,)?_+:""I^;,:"l:
                     .;^'`.`'''`^'..^''''^             """^   ^l;^Il,l,I"I!;;I:I;i';I::I;`;;`:^'' .     .
                      >[?_;+<i<i___I]~<<~+'           '<+?+   >~><ii__~i~?~ll_-+<__~,~-li[I>~---{-_+-l--{+?!
                                                              i[>^~_]~<-!i-_~<<-]?,+?++_>i]>.~[i:   .     ..
                     "+i!_iiI!-!!li!                  '~+i.              .         .    .  .   .
                     `;::;:!i"!;:;I;  .               ."":
                      >!<"~~_~i;,<!!~iI_"!!_]+<!---_~_l[>><_;~I_[_ii<<>+>!+l-[>~+il]_;-~;_<->--+>_il__-<_i+;
                     "_+!!~<+~~+_+,~_]~<+!..`'..'''..".'''''.' '"`'``'''..,```''`''"` ``'''^';^`'^"`'^"";':^
                     .^:`^:^,'^",^ ,""":l`
                 ;~: `!:I;.;,i:;"i>":;:;,I!,,!Ill^!^:I;:II;I>I!`Il:";;:;"l:;:;I,^I;:;^;^,;:;::::^;`l:"
                 ;!" ^i!+<I><?+~l~_:ilI+!i!,,ilI>"i,:i;I<i!I!>>";!i,!~>l!~l_<><;"<>;<:!:i~><+!<!"<,iil
                     `i>]i~:>;i-!~!,
                 '".  ''.. '. .'`'  '..'''.'.''......'....``.. `........ ... . .  ''. ...''.  .       .
                 >]I `li~-,i]~<,-~:~>i?>~>;l-+i~:+,!~;i~_>_~+i._~I"+~!~"+_+~~<_<:_i:_>,il{-?l>>_+-;~~,[]I
                     "~i<+>->:i+>_!<!l?_++[+~;>!I_<:~++>`~">_<<>:>++ii_~>;~-<+:<-<!~;l~<+;   . ..' ..  .
                     .`.":.^  .^'`.''."``^^"^'"''^"'";,".^'"^^"^`";:^`":^',,`:'":^^;'":::`
          ,I^!    ;i",,:` l:li,^""".;;^I`
          !~:_'   "<[-_?i:[ll!+]?_}"i>+}!
                 ..                 .
                 !<; :_~i;<~lli~?~-:<+-~<
                         "lI;;;Il;I!;:;:I;;;;;;;l!;l;:::IlIIIllIl!l:,,,,;,:;;lI;;;:::",::;l;;;;l`
                         ~:.'.```^`>][]!'````^^^l<"{1]-]-??[_[1{_1){}}!`_``^"-<_+-{>+-:+?{}:^"^<<
                         ~+]][l""""'^"^``````",,i+,"""^"^^^^^^",""",,"^^+^^^^,_!~~-+~<~<<<!^^^^>!
                         ~!l;!"    .            "l                      l    `i">!l!l;!I>!I    ;l
                         _^  i-;>~~~"           :!     :,,"             !    ^<l<,<++~>~~><-I  II
                         +"  "l<::<<'           ^;     l><~.            l     . . '`.'..''.'   ;I
                         _l",>_]<l<~;^^^^^^^^^",!:    .<]i              i^```^``'``^^^`''.'.`^`il
                         ~-]_?`      .........''::    .!>I'^``,^''^'    !....'+?;?++-~__~_~-'''>!
                         <"  !>"I;:!'           ^,    'i<++~<![]-_-:    l    'II;Illi;IlIl!;'  !!
                         i'  l<,!i<~`           ,;                      l    ^!Ii:<~+<i>~!>i^  !!
                         <:`'l_)!I_+^......''''.li..........'.''.......'+....                . >i
                         ^:,:::,:,:::,,,,,:;;;;,;I,,,,,,,,,,IlllI;;::::;i:;:;;IlllI:::::::::::;i"
                 i~" :_!<i~iIl!i`
                 ;I. ';,l;:;^"::
                   :!` i",:`:;"^>i^":;Ill^l!:",^,l,^Iii;,;::,I`;";;^^,,",,:,",,,^,":,,^^:^:^,,"`"^^;I!l."^
                   I<"`+i~_i!>~l-<l!!~~_-l!-_!!Ii><;><?I;~i!<?I-lI+l!<~!+?-_!+!ll?+_~~Ii-<<~->+li>:<~~i:I;
                      `l~Iii;I<!+">;;l`><_:l<i;><;<>+"!<+_+:!__~ll~<~?~<i_I<~_:l>~__+!I;i<>:+iI>?:!>
                    . ^[!<?>_,!><+>>[~"                 ...              '.
                       ' ...' .. '`'.
                   ~+""]+<;i!<I~>i^+>~~i,_~>>:iil~l~>;>+_~<i<il<~<i!I<i>"l>l;<!"l!!>.
                   ^"' ^"^`'``.^^^ '";;,.,""".`^,".""'`":,"",`^:",""`^";',:^':,',:::
                   :l^.i;;`!;:l:l`,l;::!I ;",!;I';::^^!,:;"::l^;::::`:l!" I:;";;:,;^:,!;;I,^!;i:^:;:::I;:I.
                   ;l^`ll<:~~i<)~,i<_~_>_I<;<++<;<?_<I~l><!!!!":l>><:I><;`<>~l>i>ii";,~iIi!:i:>i,!~~!!<>li.
                      "+~>"I~!~<`^~^Ii<l<+<:I";!i^+~+l:~i!<l
                         .^^`^"`"^'^'''^^`^^^^^^^^^`'``'`^''`^```^"""""^^`'
                         ?;,,,,,^^``^^`^,;""",:::l!""^^^",>-?+-_]+,,,,"^^^?'
                         <   .->i<<!!_<]^!<~<^   '!""":;:":l!Ii!<I^^^""::"['
                         <`   .'",::``^". ::^.  ."I``^[{[]`..`l.?_?--1?{i^['
                         +">]<i>>!:><!!!!>:I<iii^l!^^",,"^^^^,i^"^^","^^",]'
                         ] `l:,I~]l!_[~~~]!"!ilI ,;   l-_+^   :   <i!_;   >.
                         -;:,::::][})_+!~]i""^,,;>~;;;Ill;,"":i","::";;:::~.
                          '``````......'. ''``````'````'''''''''''''''````'










```

*Figure from page 4 (2346x3317 px)*
