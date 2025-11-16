# III SECTION 2 PROGRAM OPERATION 05. PROGRAM EDITING OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-05.-PROGRAM-EDITING-OCR.PDF*

---



4203-E P-211



SECTION 2 PROGRAM OPERATION


## 5. Program Editing

In the program edit mode, modification, insertion, deletion, and others can be conducted for on programs



stored in the memory.



(1) Programs are edited in units of file.



(2) Program editing-related terms are defined as follows:



(a) Edit Line



This is the line on which program edit operation is carried out.



On the display screen, the symbol ">>" appears at the left-most posrtion of the edit line. One line



on the display screen contains a maximum of 63 characters.



(b) Edit Pointer



This refers to the identifier indicating the character to be edited. On the display screen, such a



character is displayed in the reversed display mode.



{c) Record



This is so called a block in the program. The record consists of several commands beginning with



a character right after the "LP' code and ending with the next "LF" code. If commands in a block



cannot be displayed in one line on the display screen, they are displayed on multiple lines with the



2nd and subsequent lines preceded by"&", indicating that the commands are continuous.



(d) The extract buffer means the buffer where commands are temporarily saved for copy or



transfer operation. The buffer capacity is 64 character x 23 lines.



Edit line



Edit pointer



1 record



(one block for



a machining



program)



PR:JG OPERATION



GOl



G40



GOO



=E WHEEL100.MIN



tile end



EDIT



X300 Y300



Y200



Y300



Y300



Y200



Y200


#### P MODE WHEELlOO. MIN

97/ 7/15 14:10:00



S250


#### Z-55 M09 M03

F100 011



10 J100



1-200 JO



llOO JO



2100



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELETE INSERT DELETE DELETE ERASE OU IT [EXTEND]



16 lines


```text


                                                                                                ^^^"'".'^'^'.
                                                                          .'`.``...   ''....'  ._--]!]";ii~l"
                                                                          !{-~<_~_[I_.>+[~+-}-?1ll_~[<-_<+<?<
           .""""""""""^`^^^^^^"^"""""^^`````^```````^`'''''''`'`''''''''''''''. ''.'`'..'`'`.''`'''.^'`''''''
            '",,,,,,^`'.''''.'`,^"^^^`^''`":;;;;:;;;;;,,"^",:;;;:,,;III;I;;;I;:::,,,;IIIIII;:,:,,,,:;IIIII,,^
           ^\;     't[~-+_<+?+-`{[<{[}~~~l
           '-!.    `~l>-}r__1+]:__][?}--x{
                 '..                        ..
                 l!;++I_i~]<-i:+-+I>~-?l,<+-}-~[?<>">~__+-<!`--_?__!^]<+l__~<>;<?!<-I!<i<~i++~>_i,<I!>!<<+iil
                 ;]>i<+l!i{<;!i<<>ii^..'  '...''.'.'..''.''..''''``'.^'`'^'^``'^"'`,`^"`^"^^""`"^'"':"^l:;^""
                 `,^`," '.`".'`"`^`:
                  'l;  ~lIll!l!,,!I`I><l!:I^,;il`!;<l`
                  ^",  "^:<ll:l::lI^l!!lI^:`I,li`!^!i"
                  `l:  !:^^^^"'^"I,^`.^"":^``,``" `^'.:,;^^"'"`"^:``^'
                  :+!  l,!-ii!:l~_<l]l<~__+ll?ii+;<_>:-<+l+~;]!!<?>+_I
                     ^^ :`^'  '.
                    :]+.<i-ll!~~
                        ;l"^^^^,,^:""',`^:,^:'^^^^^^"'^":'``^`^"`''`.'`````..`
                        :!il:!;I<,!!>^<"I~><>"<!>-!<i,~++"-~_>-+iI:<,~-l<_i;<_.
                        ::`:;,`I:,:,'""","" :I"'"",:^,''.`'"^^^^^''"^,^`^;^`^`"^'`^,"^`."",`'`""^"`' ^^`'``'.
                        !>;<><I-+-+-!!+i~+>^><~l_<>~<>^;l,:_-+>?+ii~l<+I+-!;i<_l!>~~+<!I<l+~I_-+!_+> i<>~!<_I
                        i>"!<:l~~+<_,~><++!:<<+]-!!;!I<-+_i!il:+I]~:-+_+~<-<i
                     '  ` . '.  .  .                .  .   .  .. ... .'.'.'..
                    !{>.]~[l<>+-]-`
                      . :,'' '"'`''.'`'.''.'^'..'.`..'.  '.  ..   . ..            .
                        i~>!,-+_~:<!l~_^<?>_?_+^<<-<??l_;<+!:~<+~_?-"><;]<l?--?-.^_+,_+~I[_-??I!_<_-<":_<_;il
                        >-_<_~+-"_,~_<+_~~+!<:+<!;_i~<<_~:++___>:~>>~;. .. ...'.  .. ..'.'`^'^`'^'`^'..`^'.`'
                        . '.'''^ ^'^^"^":^^'^.`^"',^"^""^'",l,;;'",":^
                    :~l _+i!!>I
                    `;" ,::",,`
                        <i!;l:ll,i?-~ll!<ii~,!l+~;>!i<!>!, ~!<"!iI!!:lll>><!,<:iIliI<,llIll!l!>"l!lilI;l,li>'
                        i,~<<i>>~l;<_<I<-~l~<!:i<~li<[<l<!;:i<i<<!!<_l+><i+>iil~_!<i_<!;-!i+<<_l<+}<+l!-~~<_`
                       .~l>>~>_<~l;~?>;~<_;l>~^I<:'!<>]:~<+;<!<i~~!<-"i<!"i>~`:>:.>!i_: <,>il>l-!><:!`!:~>i+`
                       .i_llIl!+^>_<!+_i>:I:!>+I~i!;i:~+:i_-i__"~ii<i,^_>~"<<iI_>~+~i>il>">!_~<+I~i~<:~-~I--"
                       .-i~;_>_;_~<__+~_><i_~_I><_~-<]_l<-`~]^l-+_<[?i<!-_?<_~:>+_~~-+!-Ii<+;<~+->>>i<:....'
                        '.  . . .''..`.'    .'.`.'''.''. ^  '  ''.'`'."'.``..` '`''.^^'^.``^ `^^^`""`:`
                    !-l l!<,ii<<i!:l>]>"!iiiil:<I"<:-_I^<<<lI`I!Il:!lI>^i!;:i;ll;;i>i^I!Il!;!l`;:I:`l.
                    ^^'`ii<i]_I!+<>~_i~"`>-+!+l-[iI<~~<I_<i<!~~!~<i~~>_ll>;<]l-_<>!;i"I!IIl";l`Ili!"!'
                       'I!;ll!`"ilIIlII^ `,!:Ill>!.l~ii!;>`i">;"lii;<li; : !!^!lii
                                  `^^. .^''  .' `",^^^^"""^``'`^''^^'``.^',''`'  '""^,^``^`
                                ,:`l;1({!]{{1_<|!::::;;;;l{--iIII;:;;<<|[{I:I;l)[[ii[!_+];lI'
                                I  ^`:ll"Ill>I;i"````""^^"!;:"^^``^^^::_>_~[+[-|x[{[11)f(;:,:
                                ;    ". '                                 ";,::`,',,`:^;,';^:
                     '''..    .`!^";-r)1-'  ^,^.     ,::'   `,:^   '"^'                   ;^"
                    `~_<!_i'^,^"i::""}]{.   ]t~      !>>`   ^!<;   ;[][    I;^   ,!:      :^^
                    `~~i!<>-!'^,>'  `[--.   ]1+<;    ;;l'   ^ll^   l>[}   `\[,   i?!.     :",
                    .Il;II;il,^.;   "[?1,'..[1_l"....{|\;.'.!)(>''.,_!" ..`>~_`..       . ;l~I!>I
                                ; .<!t(fi;;;;I:^,;:::1(\>::,~\f[;I:!]]|]:::){<;;:::::,",l,l,l`^,^
                    .``^`^^    .!,:":|]\:'^`",`'`````[((;''';_]i.''"![{"`'`[~.''`'`^^^''`.I,I
                    '>+]+?_lII;:i.  .1??'   ]1:      ?|\,   ^,:^                          :,!
                     i~<i~>[+~i.:   `{-)^   }/<      ;!!`   ,!i:   "!l!                   ::!
                    "_<}]?-!i: .i   ^1i}`   ,;`                    ^::I                   ;":
                    `I:<;II.   '~   `[l!.                                                ';^"
                               '<                                                          ^,
                               .:                                                          ":
                               .:                                                          ":
                               .I   l!l{]~,+~I-~^                                          ":
                               'l   !I<!-[!'`'^`                                           ":
                               .;  ^l`^``"^''''`^^`````^^`'`^^^^^```^`'`'^^^''''``^```'``. ,:
                               .;  `l<1,':,I_{`'lI?{[``,!-]_',l'....lIIi1:`I;]><"`~`'''..  ":
                                I^  !{?_l'`]~+<l,'_1?-"'!}~~+:"<_l~i`^+?[] `^]iI  I`+<~-->.;`
                                 ",""",,^^":,,,^^^",,:^",::,:"^;l;I:^^::,;^^^I;:^`"^I:,ill:^
                                  .lI>!,l^ll<>;;,!!<iI;,l><!l,:l~~l!^:I<<Il"Il~<l!^II>iIl.
                                  ^<;~<'+l!!--`><l>~?^-i:>_>"<~:-]llIi"_}l;!<,?<^i!>:]1`_"
                                   ":,:;^ ,::;:' ::;;;'.:^^":.';^",: ^:^"::.":^"":.,:,I;,

















```

*Figure from page 1 (2337x3305 px)*


---


## NOTICE

4203-E P-212



SECTION 2 PROGRAM OPERATION



When program edit operation has been completed, press function key [F7] {PIP QUIT).



Otherwise, edited data cannot be stored in the memory.


#### PROO ~TION

>::milOOO



NlOO GOO



N101 G56



N103 G41G01



N104 003



N105



N106



N107 GOl



N108 G40



N109 GOO



N110



Nl 11



=E WHEEL100.MIN



file end



X300



X400



xsoo



X100



X200


#### X400

X300


#### EDIT p MOOE WIEEL100.MIN

97/07/15 14:10:00



Y300 $250



Z-55 M09 M03



Y200 FlOO 011



Y300 10 JlOO



Y300 1-200 JO



Y200 1100 JO



Y200



2100



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELETE INSERT DELETE DELETE ERASE OU IT [EXTEND]



@@)@@@]@~@



Press [F7] (EDIT QUIT).



Program edit operation is complete, and the display screen as indicated to the right will be



displayed on the command line.



PROO OPERATION EDIT



>:iIDOOO


#### N100 GOO X300 Y300 $250


#### N101 G56 Z-55 M09 M03


#### N103 G41G01 X400 Y200 F100 D11

N104 G03 X500 Y300 10 JlOO



N105 X100 Y300 1-200 JO



N106 X200 Y200 1100 JO



N107 GOl X400



N108 G40 X300 Y200



N109 GOD ZlDO



N110



N111



file end



DATE DIR PIP EDJT ~Tl UST



CONDENS



[EXTOO)


```text


                                                                                               ,,""`; "^^^^`
                                                                         '`''`'''' . '''...'.."]--]<}'il+>~i
                                                                         >}<~i<_?[;+.+<?>+]]+}1Ii_<[<?-i>~[i
           `^^^^'''''.'`'''^^^^````''''''``'''''''''.''`''''...''''''''''''''. .. .'....'''..''.''.''''..'..
          `>lI!!l;;l;i!";;I;IIIllII;;;;:::;ll;;I;;;I;::;lllI;lI;:,,",,,IIIIlII;:;::;:::;l;IIll;;;;::IIliili,
          ~:})[-[}1+(:] <^,]+>_>!-<-~__ll~-+!_~~~]~<!i~<;~_~<liii>~_<<~,li~~~!+<i_~iI!<<,+~-!>-_+I_<>>i,"""l
          _!?1_<i-[<["?.<  ;,":^";"i;:;^^;;"^l::,I:"'"I;':I;"`,:"III:;;`;:;Il^;;,llI^,!>"!^::;";^`i!I":.   :.
          ':`.'''''`'^^ ~':-]+?~--->^--]-_;--?!l-<_>]>_~;-~<-?li:?~Il~+>i<~,                               >.
                        ",":,:;""",,"":;I;;;::,,;,,,:;ll;l;:;:,::;II;Il;Il!;"""""",:::;;::""""""":;;;::,^^^I

                             ',:III;I:::",,",::::,,,,:,:;;;:,,,""""^^":;::,"^^"^^^",,,:"
                            'l'"!+fj}_jt/}_){I;,"""","+\_+:;;:","><[\|?;I;;{x\}<}[>)}+.";
                            :, .'.`"``""""^""'''''''''`"`''``''''``"::<]]-{]({i1-}]1\_. l'
                            :,  .I;',`                                .`````'``^''`'`'  I'
                            :, .;/|[)I  `l;'     ^i!l   .;!i'   :Il`                    l'
                            :,   >}]I   ;/|'     `llI    :!i.   ?_(l   :+!.  ._>"       !'
                            :,   ~}?>   :)]_+`   ,>>I   .li>.   _>1I   ])<   .+i"       ;.
                            :,   <?]_   :)+I".   l({?   '?)|`   l<"'   ;~-!             :.
                            :,   <?{_            ;-]}   .-)(^   ,i[?'  :),'             I.
                            "^   <]}<   .:^      ;{1[    l~<'   ^>],   :_               !'
                            `'   <-[<   :(-'     l))]   .l!!.                           !'
                            ^`   >]1-   ;1{`     `::"    ;!l.   l>-:                    ;.
                            :^   _-~i   .`'                     ^^,'                    ;.
                            :^   ~_:"                                                   ;.
                            :^                                                          l.
                            :"                                                          <.
                            :^                                                          !.
                            :^  ^-:{[{~i?:_-i                                           i.
                            :^  ^!:!:-~'                                                I
                            :^ 'lI,,"":"":"^::,""^^,""^"^^;:,,"^^,^^^^^":,^^^`^"^""""^  ;
                            :^  ,I}_`^!I!|+`;I<{1>'I:+]{l'>^'''''l:l]_',>+{<l.,;'''''.  I
                            'I` .]}_~",i}>~-;^:}[-<^'??~_<II]+i+:,I1?}l.I![>, '.I+~<[?:^;
                             .,";,","^";:;;:^^,"","^":::;:,","^,",:I:;;,:":"^"^^I:^";I;,
                               :l++;I:;;~+iI"!I<<I!"Il+~:!"!l_~:l^ii-<;l"!i~<lI:l<_~I:
                               >:_~I:ii:-]!:I+;~-;!ll:_[,<liI-]^<;i!][^<lIi~l^_i;~]-"<
                               .,"":, .:",:" ':"""^ ^:"":^ ^"`^,` ":",:' ,^?<,. ,^^,,.
                                                                     .    ..;^'..    .
                                                                    .<!+~!_i;_]~i,_iii'

                          `"'.''''.'^`..'''`'...'...'.'.'  ...''. .' ..    .  .     ..    .  ..    .   .
                          ;ii+?~~!:+->:<~+!->!;:>"~<i<--]i`?<+l+-I<[]--?,~+<_-i,[>!-__+?_-!<l!+-"~[-il-<l-<
                          :_~+_<~~>;<"--i,i!i<i~i<l><~              .  .              .. .     .  `   .  ..
                          '^"^`:,"``"'^""`"``"^,^"^^",.
                             ^,",:::"::I::;;:,"^",;,""::::;::,,,,::,;I;:,"""^,,:;;,"",,^
                            ,; ::]\/~?||(??t_;;;;;:::,[]+!,;;::;:+i\)|i::::|//?])?[}1l.::
                            ;.       ...'....'`````''.'''''''````''^`"~{?]?+|_?{+)?(1I  !
                            I' ."~l:!'                                '''... .''...... .i
                            l' ';t11-'  I~i      l<<I   ^i<i   'i>!.                   .>
                            l.   ?{?'   ~t{      ":;^   .,;,   `[?(^   _}!   :}<`      .l
                            l'   [}[I   >1[?>.   <]]l   ,__i   "_+_.  .}-;   `I".      .I
                            l.   ?-1I   l_i.     ~}1<   ,[(?    ~!""   l>+"            .I
                            l'   [_)I            <_[>   "{\[   .l-\~   ~[              .I
                            l.  .[~}:   !~:      <))>   .;I:    `:;    :;              .I
                            ;.   [-1;   _\-      <}{l   "~~l                           .I
                            ;   .[+1l   >}~      ...     ``'   '<>]`                   .I
                            ;.   }>i,                                                  .I
                            ;    !"^.                                                  .I
                            ;.                                                         .:
                            ;.   .                                                     ."
                            ;.  I"!Il_<                                                .I
                            ;   ,;.....                                                'i
                            ;.  :<.                                                    '<
                            :  `;`'^^::^^`^^:"^^^",I"^^^^"::l::,,I""^`^:,^^^^"I:"^```' 'i
                            :   '^,` ;: ^^` I`.`^' :.^^`'.:lt-!""> .'".;;`^`^`i"''`''' .!
                            ^;`.!-_I ,^ ><; I.`Ii^ ^ <+l" ,"I<. ^:.;l_ "<_}-[_l'!--]1?^;^
                             '"";",;;",:^^:,^,,"^:"^:"^":"^:"^,l::I:^^,^^:^^^"`^,"";:,:`
                               i;]<"!:iI]_;l;il~+,i:li-<:!:I<]<:::l+]>:;II__>I;;;-[l!:
                               ~:~I^il<;+_"!!>Ii+">Il!<~^ilI<_+,llI>_~:!i:_<;;!!:~[li!
                               .^'`^' '^``^' '`'`". ^`''^. ^^`^"  ^'''"  "^",^ ."``"^













```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-213


#### SECTION 2 PROGRAM OPERATION

5-1 . Commands Used in the Program Edit Mode



Item Command Functions



Insert line INSERT LINE Inserts a blank line right after the present edit line.



Delete line DELETE LINE Deletes the line including the edit pointer.


#### Insert character INSERT

Inserts a blank space (for one character) right before the edit pointer.


#### CHARACTER


#### Delete character DELETE

Deletes the character identified by the edit pointer.


#### CHARACTER

Delete DELETE Deletes the specified number of records (blocks) in a program.



Erase line ERSE LINE Erases the commands in the line which contains the edit pointer.



The line remains as a blank line.


#### Quit QUIT Ends the program edit mode.

Find FIND Searches the specified character-string.



Shifts the edit line by the specified number of lines.



Change CHANGE Replaces the specified character-string with the newly specified char-



acter-string.



Copy COPY Duplicates program data in the specified number of lines to the ex-



tract buffer. The original program data remains as it is.



Move MOVE Duplicates program data in the specified number of lines to the ex-



tract buffer. The original program data is deleted.



Extract XTRACT Inserts program data in the extract buffer before the edit pointer.



Page mode PAGE MODE Replaces the character located by the edit pointer with the keyed-in



character.



Insert mode INSERT MODE Inserts the character which has been keyed i through the keyboard



before the character located by the edit pointer.


```text


                                                                                               :;:;"i.,;"::,
                                                                         '"^`^``^^.` """^^`"^^,+-_[+};i<~<+<
                                                                         I{_<ii>_-;+.~<-~+--_-{::~<+<-_>>!~i
           ```````````````'''``''''````^`'```````^``^^`^```'``````''''''''..''.''.```''''.'...'`^`''''...'..
           `:,:;;;;:,"",""^^^^`"^```",,,,`^`:,,""""""":""`^"^","`":::,,",,,"",,,,:;;;;;;:,,:,,::;;;;;:,,,",^
           +^;`    ilIlIII!ll>i^;!!!l::I`+Il'~!II!l!il'_I_>"_~;i+;
           >"^^    Il>lII;<!!><`I!>>i,,;`!I<':"l>[l<i;'il<l'>i!>~I
           ^""","^'...`^^^^^^^^"^'''''''"^^^,^^^^^^^``^```^"`^`''^:::,,,,^"""""",::,""^",,,::::::"^^^",,,:::`
          ;?""^^`!1??i""",,li^^~-??]??_++,"><^^^^^""^``^`""^^"^^^^"^`^^<??--1_-[:^^''''`^""""""""^^``^""""">~
          :];:,::I<i;,^^^"";><>+?--+li~<>""i+!!lII,",;::III!l::,;:^!il;<i~i~~<<~!,,l;:;l;","""^`'``''^,"","i~
          ,-~-]_>~~-I'`''''"i]-?{+?<;<_[-`';<~+]_-i><+?+~il<-!<}?~i]]];~<!>~<-?<+<[[_~_[i```''`^^^^^^`````'li
          ,?+~-+_!+<~"''''',>i-iI+i[<!-[}l';i<_----!-+i<+~l!~_<]-<~i+<;<_-!<<<~_i``'''..'`````^^^^^^^`````'!>
          ;[!><<~l~<+I:I::"!-+++<<i~;I!i<l,!<Iilll!:;;I;!iI:I;I!!!_lli:ii!li!l;!:`''^^`^^^^^'..''..^`^^^^,"i~
          I-i~__<l__---?}l ,<[[]{]-~'.. .  ^l!llI!"::;l!i:,>IlI:,~I`Ili`ll>lll<l:"i<i;<i<l!,>>I:!~i;!!i<<` I+
          I~               ,~<+_?---+_}[{;':!Iii!l;Ill!<il;_iii!I<i"il<:!I~li!<!;"<+l;>illl:I!l:iil!!ll>i^.l~
          :[~<~+-!i~~~~+_+::<_-~i~<?i"""^,:>>`...''`,"^^"^' ...^"^^"",^""`.''...',^`""^''''``''^^^""^^^`'"^i~
          ;_I><ii,,:llll!i. l][-[]<]!,;;l. "<>___?_I++i,_~_~_~_I;-+l?]_~I+<:~-:~_[I+>!<?l                  :~
          :_'    '`^``````^Ii<+~_+__~<-?]!"i<:"^^^^^"","",:,,^^^`",","::,:;"^^^^"^,;,,,;,"^'``'.''"",,,,,"^l>
          ,]_]-?[i.'```````,>~{i!-i-:    '`;>+?[???l_?<!}--~]--l_~~_-]l!-!__~~]],]]~-]-><ii>>~~]~?[!'`````'Ii
          "]?<~~~i!l:`^^^^^I-_?]]?i<~<~"^^^;~+<+~~_i<!II<>>~<+~+><!i<>;>iIl~_~-<i+<<>i<l<><<_-~_~<><!,`^^,:~~
          ^+<I+~!,<~l      ^~~i<~~"i>-?.   '>[<?_?+;>+I~<~~!_?!]<!i<-+i++!:+li>^l>l>~l!:!<iI>+I;>ll~~^     ;~
          :~.. .''..'''''``I>   ..`''..''`':I>_-I?<~I->>_~~l+];<<_?_-,-+_'' ..'^```'''.'. ....`^```''''''``i~
          ;[-+-<^^^^^`'''`':~_]_]i^^^"^```';-?i-]I--><<<_<_~;>_[!~_~-_'..'''''^^^"""^^```'''`^"^"""""`'''''!~
          :[~<>l`^^^``^^^,:l~-]-+I````^^^,,>][~++!ii!<~>-~-~i+?~i!<>><;;II;IlI:,"^`^^^^"",,,,"""``^^^^^^,,,>~
          ,]il<~ .       ..^ii_?]; .     . :>+_<!!>><:+>,!<~<>__<">>+l~<]!:]<+-l                         . :i
          :<               ^;              "l<!<_:;<!"!<!:!i,!I,i>"Iii!><!i"l;i<>>'ili!ii'                 ,i
          ,[ll,,,",""""^",,l~!!liilIl,^^",,!~}+_]+!<~!]+!!~?<?1<+~>~_+<~+-_~?-~~__!>><><_>l!;lIl:;l,:,I;II:++
          "-~__-~)+        `i+-_?]?+[,     `l_?-<?+~<;<~:+__~+-_<:~i~i~<]I;]i!?!i_-:~+>`~_-[I<_-+~?_~:_+?I.I~
          "i    .^'''''....:i      ..'''''."!-~]_;_<~_-..           ...                ..           .   ...l~
          :[++-+l",,,"""^^^I-+__--!,,,,",^^;<_>i+>~-<+~_<>i><i:~+-!<i~+<I<>>i]>>!<>+_-_>l+i+i~!<+~}-i++I"^^i~
          ;+":i!^          `!:::^`.        ^~+-[+<<{1_;!-}1i-<!?-[l<>i~+i}i?-?+<i<++~-~i><i~<l"":^:;^;:.   :~
          :?"^'.'^^^^^^^^^"l~"""^",,^^^^^^^!]_-_>>+?-<,.l!+;~~{]+]i?>_[>~!,<?]_l?~~-<~;<+I<<+^""","''..`^"^!>
          "})}~?+.........'"<11??}>''......:_-i_]_<]_~l?~~-__i"+-[ii;+?>,[_<>[~?;l!i___;;?i_~]>-->[]l?_"...:!
          :+ . .           ^;              ^>_-]><<?1?"'_?}I+_-+<[I_~~?<?-:_]]iiiI[-?[?_`  .         ''. . l~
          ,[>l!ll!,,",,,,,"I~<~~<>!!!^^",,,l~_-_!<>l>>I!><~i-_}!<i+_!>-_-~++-~{_>!~+_<+<+<l!<_;III!il^`^":,<+
          "}?_<>]~^ ..'```^:<_<~-__il''''``:>_+-__~~~i[_~>II-_-!~!-+l!~~>_~l+<?[<!]-~><:>-!~-[i_-~<?>`'''`'!~
          "[]___;!++[_^'''`"~[]-[1;{[-](+'',i_-~~-<~<l[+;i+-_-+]?!_~_[-+l<~I_]!~-[l~~__?l;?}~!]]<-_~_-l+l''l~
          "i ^;:..'^^'     'I..''' ''.'`.  ';>--<?+[-^`^.''^````^ '`^^^`.'" .`.``''^^''^..''. .`.'^"`` ..  :~
          "?I:":I:;,:;:,:::i-i>>i!>!;i!Il<!l__~+~_i~~;":;;lll!l;;l:;:,:;:;Il!;ll;::,^l;:;Iil!>lIl;,;::;l,",i<
          ,-i+++>:<><]^    ^>>~+_<+!"]~<<?;'<i<]>+i!<~,_~]~__[<,-+_->i?];_]_+l+-_+_i"?>ii<}Il~<,~<<>i~><.  "i
          :-`^^^`^^^^^""^^^:i'`````^"`^^`''I_-[?-[<[[-<}][_?]}i<{-1){]~}>}]~<}{+]}}?1-;^^^^``'`^`^"^^^^^","!i
           "",,,,,:,,,,""^^^^^",::::::,,""^^^^^`"",""",""^^^`^^",,,"""","``^^^`",,""""""""^""""^""",""","""".








































```

*Figure from page 3 (2328x3293 px)*


---



4203-E P-214



SECTION 2 PROGRAM OPERATION



5-2. Fundamental Operations Necessary for Program Editing



5-2-1. Readout of a Program File from the Memory



(1) Press function key [F4] (EDIT).



MULTI



DATE DIR PIP EDIT PIP LI ST CONDENS [EXTEND]



Press [F4) (EDI1)



The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.



EDIT E



PAOGRUM OPERATION



EDIT



El]]



INDEX DISPLAY PROCEDURE



[F2l - M01:*.MIN



[F3J - FOO:*.MIN



I 97 /07 /15 14: 10:00



~ I TE



TO DISPLAY OTHER lt,DEXES, AFTER PRESSING [Fl] ,



INPUT l'HE DEV I CE NA1E AND FI LE NAME. l'HEN PRESS [WR I TE] KEY.


#### DEFAULT DEVICE NAME= M01:


#### DEFAULT FILE NAME= *.MIN

>XE



MD1: FOO: COMMAND OVEAWR/ CHAR.



INDEX INDEX INDEX HI STORY INSERT DELETE CANCa


```text


                                                                                              `"",`"'.,'"`^
                                                                         ''..`... . .''...'...<?-{<-I"<!-!_.
                                                                        ^]1<>~+~]l~"I_-~+_?-_[~;_<?_]_~~>~_.
          `^^^^^^'```````^^^^^^^``^````````^``^``````''''```''''''''''''''``'.''.'''...''''''''''.''.'''`'`
          ^,"":::"^^^^``^""""""",,"^`^^``^"",:""","""^^^,:,,,`^^"""^`^"":"",,:::::,::;III;III;I;::,,:,;III;
          ~Il!    +iI!i<i!llI<>i^!~!i!I<>Il!:;~!lIl!llil""i;'<i;:;;III'~:>>I:;'
          ;::;    ,"i;i>~lI!;!<<`;~_<!l~iil>!">>>i><+<+>>^~<^!;><1>__i"~i-+<!1l
          ^.` ^   ^"..`. . `. `''     ''. '  ' '  ''
          <l~,i.  !]?+-~_ii~liii<?~_~lii-l>~<!;?_;-??+~<+^
                 .    '          .     .   ''.'.
                .>~" l+_]}><~~-]~~!][<<_~-!1+-~_;
                                    ...  ..     .
                        `^                                                                  ":
                        ,:                                                                  :;
                        ::                                                                  ::
                        :,                                                                  I;
                        :,  `>:^^``"^`^^^``^```^``^,""""^^""^.'`^"""""^^^`^``^^"^^````````  ::
                        :,  '    ''i"'   ''>'.  .'^l`'.''`!:~)<<i^~:`''.'^i.  ...,!'        ":
                        `l   i+!i  l. >Ii  ! .l!; .^ i<": :`!-]". l .^;>' !!>_~+~I:.<i!i~i^ I^
                         ";"`:l,:..:'.;,:.':.'":`.`^.l!,^',^^";..':'"IIl`':Il<ii<I"^<>l>__I:,
                           `",`"";`.,:^",:'';""^:^'";,":I^^;;,,I:`^l:,,;"`":"`^".^I:^',' '^.
                            <"-~I^<;i;?-;I;>,~<-^+"<^_+!,!;I>}["<^<"~]+^+"<:-+!;!;;!_}"+"
                            ~:<!!,<I<;>];lI>:<!-"_,<,<_i;!;;I!+`>^<">+?^-;~"i!:I>l:i~{`_:
                            .,`^",  ^"^^"^  "^"^,. ',"}I"`,I;";i;.:!;;",. ^"`","  ""^`,`
                                                       ;^!~+[~_+[~?+i<`
                                                        .    ..  .

                     ;!l;'!;IIl`^!I!Il!;`i`liI.>ilI!Il";l!!Il;;:lIl!l^!i^"I;I;l;;^^I:I;I'";:;,l;'lIl:;:,^^:
                     :><>I~i<~>;;~+~>]~>;+",ll'!llIlli:IilillI;:!i><i`I~":+>!l>l!":~I><>^!>!l,i<`i~><<l<<:>
                     :+i!i~!~"^+,I<!;<;>_i,
                     ;I;!: i I<
                     !>!!".<'i-
                             .'""^^"^`""^'`""''^^^^^^^^^^^^^,"^^^^^^^",:""^^^^"^^":"^^'
                            :,^ll))[{(_-1}{_~1<::::::,,:;;,,::,,:::::::,""",,;:::",^l,";
                           .I  ,:i<<<_!!>>>I!_iII;;;:""""""""",,:::,"I~]<]~<?,<!i~<1-" ;,
                           .; .!~f]_I:;;;:,:I;::::,,",,,,:::;II;:,"",;!il!l{t)n\]x-__, ",
                           ." ';l));^^^^^^^^^^`''''''''''''''``''''''````''""","":"`l" ^^
                           ', .^  .                                                 `' ^`
                           `l ."                                                    ^^ :"
                           `I ."^^"""^"""^"^,::;;;:""",:"""""",:::;;:,"""",:""^^^^^"i" :"
                           `I   .?|[ili?[>]^?(]][}{^           .. ...                  :"
                           `I   `[}? I`\/!>I}}+                                        :"
                           `I   `[i~,-;<]i+<(-ll!!i; `>;<,`!Ii"I: "I"`                 :"
                           `I   .]]_>~{{^}[>)l:/z?-\>I{+|~}x(<>|/l~(1}; i}i!+`:+I      :"
                           `I   ,)([~ll}[?-~![|1>"-f>` "`'Il" .";,',;;^ ;>;,l`"i".     :"
                           ^!   :(]-]<^<i_;-1n>I .ii-~I                                :"
                           `I            .  ..      . .                                :"
                           ',                                                          :"
                           ^!                                                          :"
                           "i                                                          I,
                           ^l   !["                                                    l:
                           ^I .,>,"^"""^^^^"^``````^`'''`""`^'''^''''^^"^`````^``'''`. l,
                           ^I  ''''``I~|~:'`ii}~^.^<_(/{)<~}[1\<i--]i'`<`..''`i``````. l:
                           .l`  !]?< : ^?[_:; ;{]+"i<+?]?i^"}1{_!^]]<~~;"+]~<';       '!'
                            .,"""",,`^^^:II,""":;;,,:^^,""^"",:":^:,:::",I;;I""``'^,^,:'
                              ^li~!;;,li<>l,:l<>!l,;l+<Il"l;<+;l`!l~<Il^!l>i;I^I!<>lI
                              !I__i`~~l<-~^i+:_<>;i>"?[;li-^~{"<;<;?}^<!il~>'~l;<?{`_
                              .:,":;'.;:,,:..;,"":.`:",;: ^:^^," ",^":" ::"":".;,",:^
























```

*Figure from page 4 (2346x3317 px)*


---



4203-E P-215



SECTION 2 PROGRAM OPERATION



(2) Enter the file name of the file to be edited and press the WRITE key.


#### WHEEL 100.MIN

When a program has been stored without specifying a file name, that is, when a program is stored



with the file name "A.MIN", this step can be skipped.


#### PROGRAM OPERATION

197/07/15 14:10:00



EDIT


#### E WHEEL100.MIN[l

INDEX DISPLAY PROCEDLflE



[F2] - MD1:*.MIN



[F3] - FDO:*.MIN



TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl] ,



ltf'UT THE DEVICE NAME AND FILE NAME, THEN PRESS



DEFAULT DEVICE NAME = MD1:



DEFAULT FILE NAME= *.MIN


#### OVERM11TE

[WRITE) KEY.



MDl :



FOO:



CCJ.f.lAND



OVERM,/



CHAR.


# I I

INDEX INDEX INDEX HI STORY INSERT DELETE CANCEL



-.WR_I_TE-



Program data of the specified file is searched and read into the editing area. At the same time,



program data is displayed on the display screen.



Program data of the file name "WHEEL 1O D.MIN" is ready for editing.



PROO OPERATION



>:@000



N100 GOO



N101 G56



N103 G41G01



N104 G03



NlOS



N106



N107 001



N108 G40



N109 GOO



N110



N111



=E WHEEL100.MIN



file end



X300



X400



X500



XlOO



X200



EDIT



X400



X300



Y300 S250


#### Z-55 Kl9

Y200 FlOO 011



Y3DO 10 JlOO



Y300 1-200 JO



Y200 1100 JO



Y200



Z100



LINE LINE CHAR. CHAR. LI NE EDIT



INSERT DELETE IN SERT DELETE DELETE ERASE OU 1T



100.MIN



4:10:00



M03



[EXTEND]


```text


                                                                                               `:""^"" :'^`".
                                                                          ''''`'''... `'....'..i]_?_-<'+I-!-"
                                                                         .?1_i<+<[~>;:---~_-]?[-:~~~____<>~?"
           '''````^^^^^^^^^^^```````^^^^^^^^^```'`'`^``'''''''''''``'`'''''`''.''''`''..''''.''''`..'.''.'''.
           `"""""",",::"""^,"^`"^^"^""",",""",^^"^^"":"^^^`^`^`^``",::^^"`^^"",:,,:;;;;;;:::::::IIIII;,:,",:.
                  l_: ^-!<~"!~!;+l"l>li";l!>l:-!,i"!i"l>~!!,l;l,ll!l^li:;<~+>+I,ll^
                  :;" ',":I'^::'::'"I,l":",;I^ll^l^I!"ll!lI,l:;:lI!!":!;"!;!:l;,i<:
                      `_+~_--,l+~l][_'
                      ."^``^``'^^'^^".
                      `+~i~::I!!i+l~i;<+<I~<>i,_><_>:~+<i><:+~>i_<i~l>i}~;<_i?l;-~+;<'~?<_;!!>!<+i+i,<,~<i<~:
                      '~--l+~!-_!>~+i<"_<>]-?:,?~il_!>:!<!i<ii-<>+<?I^'""'",`:"'^,"','""":`",:^:!^:^',`,,",:'
                      .lI:':;",I".II:l.^::I:;.`;;:^!lI'Il^"i^,!lil!;.
                         '^'     '.   '' .'''^^^^^"^`'`''``.`'.'''''^^^^^^^^",,^^`
                       ^I^l;[1[[[_+{}{_>]<,::;;I:::::,,,,,,,,:;:,""""""":,,;::";:,;.
                       l  ^"!~+~?~>-~-il_i"""""""^^^""",:,,""""";<]~]+>-"I>!<i[<" ",
                       :  ,:]->,`",""^,,",,,,,:,"""""""""":;;""":lil!!1j|xn-|_<i, `:
                       ^  i;]?\}]!?]<)][-^`^^``````````````^^````'''''l>><>;I:';: `,
                       ;  l .."^^''`'^'""                                      `, ";
                       l  l                                                    ^: ";
                       i  l"`'''``^```"^`'`'''^`````````````""^```````````^^```:, `"
                       !  .'!}-~:~<-i_"<}_][_}:'''''''''''''```''''''''''''`''''  `,
                       l    _([";;{|<~;{]~",,:.                                   '"
                       l    -+_.!,i)~!i\]i  ...  .``. ' '. .  .                   ^"
                       l    --_]-[-!i}-f~^{f{[(!")-)~~\|-~)(,I|_+,.^I"^:`':"      ^"
                       l    _/[-:+]<{[-<_-f{l>u_^:l!"+-_.`<<>:+_-! I}<:+:,_!'     ",
                       l   ^\(})],<{-<{?u[_.`~[_<;                                ^,
                       I   .:"^:".'':`^II  .  .:""                                ^,
                       l                                                          ^,          '^''''
                       l                                                          ^,         ;i"^^`;;
                       I                                                          ^,         !,.",`'I
                       "   "?l                                                    ^,         :,<\:;~l
                       ,  'il,'''. .''''.  ''''.    ..     .   .''..''''...'....  :;         :^.:;^,i
                       "  ``  '`;l1>".`I!]+^.`l+)/]{<i-_]1~l+_?_`'l"'...`!^"^^^^. ,;      "<i;])>i_"i
                       ;'  ^+~> "^I+?<:^.!}_<`:_]1}1>::?{|{I,_)~i!;"l~><.:        ;^     ;-_(<>;"^,;!
                       .:,^,!!l":".:!l::^"li!"^,"^:;"^.:;;;:`;illI:"I!ll",'''''`":,     ^! I` "^`^`".
                         .;lllII^lllII,^!!!I;^^III;I^"l;I:;`:l;I:I':IIlII^Il!l!;'
                         '>;-~._l!l??`l~I_--^~>,+]~,<<"-1!;;i"?1!I!<"-+"il>I[)`+'
                         .;I;;;I`lIl!:"^l;Iil"^l;;Il^,ll!!l',I;IIl`;;Il;l^I;;!;!.
                      ..
                      I<!<~>_i"_-_!:_I_<^>+>!+_+iI?+"~`~>+>i>><"+><:i~_<,<_:~_<:+-+!~ll<>+, >+;_<:!~<i>,~!<:
                      ;!!-_~~l:-__I<;<+_<__~~Ii<!~~I>->~_~;<!<<i>^".^",^.^"'`""',"^`;:^"":` ^"'",`";,":',^:^
                      ;;^l,:"`':,:':`::!;;I;:.:^`;;';;!,l!.;,";;^
                      l<!i>!<i,~~_Ilil<I:?!^l~l<;"_+>]i+,;i<,+_~i"<"i>~-;!i"!>+ili.
                      ''^II",^'":;^"``,,'::'":^:^ ""^:^,,^":^::,`.;':;ll,`:':;;,">.
                              `^^^`'",^`'.''',,"^"^^^^^''`^"""","^'' ..'^^``   ''."```"`
                             ;,`l!1([!({{}-[1;:::,::::>1_~:::::::;~~({]"""">){1i~]!?~~`,I
                            'I  ^^:lI^!Ill:ll^````````"!l;"^^^^^^"":i!>+?~-?|t-1[(}(t]' ;"
                            'I   '^ .'                                 ,;::^'^',",:";^. :,
                            'I  :]x]1~  .,"'     .:;;.   ",:'   `""'                    :"
                            'I   :)]_   `)/:     .!i>.   ,i<^   i?1+   'il'   ll"       :"
                            ':   ;1--.  '{{~~,   '!lI    ;Il`   >i[+   lf?.   -+I       ,"
                            ."   ;}]}   `)}<;`   ^))1'   _}(;   ;-,.   "++i             :"
                            ."   I}]}    '^      `?-{`   <{)l   "!<]:  '1!"             :"
                            .^   I}][    `.      '}11`   l--:   `I[~.  `]"              I,
                            '"   ;{]_   '{["     ^))}'   "II'                           ;"
                            `;   ;(}1   `{(;     'l!l.   ;i<`   ,Ii!                    :^
                            `;   I)~?    ,,.                    ""l;                    :^
                            `;   ;{lI                                                   :^
                            `;                                                          :^
                            `;                                                          :^
                            `;                                                          :^
                            `;   i:<]]i:_ii_+.                                          :^
                            `:   i:_I-]I'''''                                           :^
                            '^  "I^^`^,"^^^^^,^'''``^`'''`^^^"^``^``''^""`''````^""^"". :`
                            '^  ";~{''ll!}]'"li-)-',:i?{<.I:.''..!;:>?^^i!]>i`^!```'''  ^'
                            .I'  i1??l^I[<+~I^']1]+"^<}~-+"`_i!~l,:{]}~ ::}!;  :^<<_~_l.I.
                             .:,^,;::":;lIII:"^;;;:,":;:,:"^;::;:""l;:I";:!:"``,"l;;I!l;`
                               'II!I;:"!!iil""l!!Il",lllIl^;;ii;l`;;!!I!^ll>>ll`Il!!I;
                               ,!i~!'_i;>_~`l~,+~>,<I^~?IIi>"-},!;~,-{,<>>:+<'~l:i?)'[.
                               .;:";I^';",::``;"",;'^:,",;.":",::.,;;I:;.::",::';lIl;:












```

*Figure from page 5 (2346x3317 px)*


---



4203-E P-216



SECTION 2 PROGRAM OPERATION



[Supplement] If the same file as the one selected for large-capacity program operation {method B,



method S, method M) is edited while the selected program is not executed, program



selection is canceled.



5-2-2. Readout of a Program File from the Memory Using Wild Card{"*","*·*")



(1) Key in "E



or «E



*·*"



and press the WRITE key.



(2) The list of names of stored files is displayed on the screen. Move the cursor to the required file



name using the cursor and page keys, then press the WRITE key.



[Supplement]


#### AUTO OPERATION A.MIN

PROGRAM SELECT INDEX



MAIN PAOGRi\M FILE



JW,MIN



B.MIN



O.MlN



KS.MIN



K51.MIN


#### ABCO.MIN

K52.MIN



K53.MIN



P03.MIN



POO.MlN



=PS B



=What is the fl le name tor program select?



PROGRAM ACTUAL PART i BLOCK



SELECT POS l T. PROG!AM



DATA



SEARCH



01 NGm 11



97/07/15 14:10:00



1mm



PAGE 1



CHECK


#### DATA [EXTEttl]


## 1. An asterisk (*) is displayed at the beginning of the file name of the file that has been

created or edited last.



When the PROGRAM EDIT INDEX screen is displayed, the cursor is positioned on



the file name prefixed by an asterisk.


## 2. When there is no file where asterisk should be set, the first page of the PROGRAM

EDIT INDEX screen ls displayed with the cursor at the top of the file names.


## 3. If the same file as the one selected for large-capacity program operation (method

B, method S, method M) is edited while the selected program is not executed,



program selection is canceled.


```text


                                                                                               ^"""`^'':.^`"
                                                                          '`'.`'.' . .''...'...<?-]<+l:+l_i?.
                                                                         ^[1+i<~+[!<,;+__+__-_[~;+<?<-_~~++_.
           `^`''```^^^^^^^^^`'```^`^^^``'``````^``````'''``````````'``''''''''.'`'''''..''`'''`''`.'`'`''```
           ",""""``^"""","""^,,,:,,"","^^^^:,,:"::,,:"^`::,,,,,,:,,::,"^^^^",,:"::,"","":;::::,,^",^":,::::"
                 _<;i!<!l<i>i    !,<i^:iIl;">;.!,"!I':;l.:Il;Ill,lI';!;I^";;:I;>',;:;;;I^`:;;:!;;^`;;;!,;"II
                .I::I;;:^I;:;   .iI+]I<++il!<?!+iI_-,<l~I-~~<>--il-Ii<_]i!--~<>?I~>>[<_>ll-~~>_><ll>i+<i~li<.
                                .!><!i<,lI`<<_i!<,__^<">+_<<"!<>?;i~i`+~->~<>,~!<-!~!`<"l~l;<>iI!-~:^~!_+<+>`
                                .<+-_?_-:i>;_~><-+<"                                                    .
                   .           .       ..  .   .  .
           -!_!-.  _]+_-~_+l_!<>~>+_~-;<_?I+~~>I_+I[[-~>~>;<+<<<![<_!i+<~!!II^`!:,l!^
           '.'.'    .`'. .. . '  '^^`..  '....   ' .``.'`` '`'^: '."'`,"^^'`'. `````'
                 .i<^ ;_~!"i`-I,l^i;:{^!^I;^<iiI>!>>,<i:l_~>i_I;>i"
                  `'' '^,:.` ^..' "' : ^'^  :",^:";:^^"^':^^','^;I^
                  !<' ^i:",i!'i;:I:;l^"l"l;:::,<::.:.l:,l,,:;`;^"l,':::::" ^<I":^I;"`:,;:"":^i:^":"":,:^lI'
                 .!!' ^li>l~!I+ll+~><!IiI_ii+<;+~<:+I~~+>?__<:_l!+~l<><_?<,i]<!<:lil,>i<~l;~:_~I!~~>i<+:<-;
                      ,>~i_::_><_l<<"!>i~>'<!<:>+_<:+<<!.ii<"li<<<"+~;l+<~i?;l<+:
                                '    .       .''.`.  .. .    .... .  .      .. ........
                             .;:;Il!i!>>i!I;il;;;;:::::;;llI;:;;;:,,,,,I;:::lII;,:::,;::^
                             I^ il)[[>{|()~_t!",",,,",:-])]!::"""",,::;[]:I;1/{?lll::_; I^
                             ;   ... .    .. .                ......'',~?~]-~1!-[~]-/_` ':
                             ,                !~<<+>"+:ii'">!l.                  . l-,  ^;
                             I    ?!<^<-+~]>;I__i!>!^i:!I.^i!!.             ><>'^       '^
                             !  .`\)1]?llI>I"::^   .                        :lI''       .`
                             !  {-{{/\l^"""",:::;IIl^                                   '"
                             !   ^?_{}I '........'..                                    '`
                             !   '{_>{}^                                                .'
                             !   ')(--1]:                                               ^"
                             I   '{)<{[+`                                               ^,
                             ,   '[}l1-~                                                ^,
                             l   `{)<\[_                                                ^,
                             l   .I>:<l;                                                ^,
                             :                                                          ^,
                             l                                                          ^,
                             l                                                          ":
                             l   `l'^`                                                  :I
                             !   !1<~`"^'!"':""'I>,^l`.,";"I`:I;;"."                    ;I
                             l  l]}{]>~i>}?~!+-~)]l,_<-]{)<]:i<i~<l!,""^I,;ll!:l"`^``^. :;
                             I  !{-[[];:{~+['!_{]:":^,[+], .,"^"`:"     i"~{1_.<',",,,^ ::
                             "I^I->~l ,:<+",'li<+-[["`+>i ^`+-_-~;^ ... l^<>>" l`-_<-{+"I.
                              .^,;;;l;"I::l!"',""^".^!;,;l",:"",,^,!II!l^:;,:I;,II:":"^^
                               ^>!]<'<!!<-_"l<;-->:!!,+]lII!,_};l"<:]}:!Ii:+~,i:!I-}^~.
                               `il!!,i;ii<~:;ll><<I;I;l<l!;!li<Il^!Ii_I!:il>i,i,!Ii_:i.
                                  ...      .  . ..   .      .      .  .   '...   .. '
                ^i,""::,:,"l`   .'  ';^`","^",'```^':^`"^`^"'^^^``^````^^' `^^'`,`.'''`''"^'',^."''^`''`'...
                ;-<++++i>+>[;   ',  :_li?__i~~;><l~!_~~<?_+~<_i~+l+-}>i~<?l<i__!+_l>-!<ii~><>_[>?<->i]_~-_~I
                                    :!<--++,+^<~-+<l<+~.
                                    ^,,^^^,^`,;;",,:":,^^^`"'^^^"^^...... . '. .   . '.       .    ..
                                    ;?<<_:+_!i<_>>+]~+]~_<>i,~_<?<<I+<_-+;-!-????_+?I-?~!~i--i<~_~+-_<<-_i?i
                                    <->I__:!+<<lI~~-~++i~<:_II__~><[:         ' ..  .    .  . ..'..... ....
                                    ..'  `  '.''`''''`` '^ ^..^'^.'".
                                li  ;+>!i,+iii:l,I;;_I,<!ll::iii:!~'iiIl<li>,!<,:iI;!ll,ili:;i!!I;~~!ii~~~->
                                `^  >]~?-I?_-]~ili>l~>:~;_~i<_>+ii+<-!-~>l>~!<<l!l_l;<i!<[[~i!_<iIl>>i>IIl>;
                                    I!I;"^!!I!l^I!;i!:`!^!<~i~iii^i>i,>>;:il><::+^i<"i+;"l,>>"+~"l<ii<i
                                ^^  '^^'...'''."' ' '^' '.  .'' '..''. ..    ... `  .  ....  .  '.   . '^'''
                                ;i  i<~+il?<i?l__I]>i~<;+~_I?-+~-<~i_i;->{+:~?+-i_~;_i-+i-!:}-+<[-+:I~!--><<
                                    >< l!+~I~::i !i~-!~;I},:!.>?]__"~-<],_+>^__-~+_-l><<_>~~:~l:<+,<~~>i++_^
                                    l>i<<~~!l_+~>_<+:<:!~ii+-<~`'`` '..`..'' `````^`."'`;`^`.`'.`^.^`^^^"^^'
                                    ;""i;:;^^I;;:;::':`;l,:lII:























```

*Figure from page 6 (2346x3317 px)*


---



5-2-3. Cursor Operations



4203-E P-217



SECTION 2 PROGRAM OPERATION



When the cursor key is pressed, the edit pointer and the edit line can be moved.



(1) Cursor Right Movement



Each time the cursor key is pressed, the edit pointer (reversed display) moves to the right.



The edit pointer moves continuously while the cursor key is held down.



PROG OPERATION



>::©11000



N100 GOO



N101 G56



N103 G41G01



N104 G03



N105



N106



Nl07 G01



N108 G40



N109 GOO



NllO



Nl 11



=E WHEELlOO.MIN



ti le end



EDIT



X300 Y300



X400 Y200



xsoo



Y300



XlOO Y300



X200 Y200



X400



X300 Y200


#### P MODE WHEEL100.MIN

97/07/15 14:10:00



S250



Z-55 M09 M03



F100 Dl 1



10 J100



1-200 JO



1100 JO



2100



LI NE LI NE CHAR. CHAR. LI NE EDIT



INSERT DELETE INSERT DELETE DELETE EAASE OUIT [EXTEND]



(2) Cursor Left Movement



Each time the cursor key is pressed, the edit pointer (reversed display) moves to the left.



The edit pointer moves continuously while the cursor key is held down.


```text


                                                                                               '"^"^^` ,'^`^.
                                                                          '`'.`'.'.   ''.......l?-]+<~.~l-ii'
                                                                         .[{~<>~+]~>;"-?_~+-?-{?:__~+~_~~<+["
           '^^^`''``````^^^^^^^^```''''``````''`````''''''''..........'''''''' .'.'''...''''''''.'.'^.'''`''.
           ',",^"","^^^^",,""""^"^^^,,,;;;;;;::;;;;;::,,;;;;,,,,,,,,,,:;;;;;;;:::::,:;;II;;II;:::,,,,::;IIII'
           !!!:<'  I>l!ll"i<iil~il!;
           ","^;'  `":,:,'"II:"l:"":
                 _]<~!:_>l;!;i>"!<<"~:><+~<~<'>~i:<+>l><>+~"~<>I~~;l<?;<><"><;I~;;i!l>>"
                 `'."^'`^'.^'"^ .": ^'^`"^"",'^",`:,^:::":;'I::^";^,;;^,:I`Il"^l"^:;:I;`
                  :!" ^>;Ill,l+i>;;+I;lIIl;;
                  ,;" ';I:Il""l~!:,!;;!;;!;;
                                                          .
                                                     Ii><l;<+i!'
                                                     ~<i>i;i>i_`
                                                     I:<!` ;>I!^
                                                     ~!i<i:ii;-`
                                                     i<+<lI_-+<.
                                                      ```"!;~;.
                                                         " .'
                      `,''`'^`'.^'...''''''. '..''...'.'` ...` ................'  .   .        .    .
                      I<_<i;~i-;><i;~<<~l;+-;!!<~~+<~_;!-+:__~l~~+~?;!~+~->__!l-__-?+;<~~~?>>>I+_;i[_<
                      ';^^.^"^.`^^,"'````^''^`":`'`'^^''^^,'"^^'''``'`^`.''```^."^'"`     .  .  .  ^
                      `!>~;+_!i<+>?_"l~<<->:<>>->~i<+_Ii+!-li~>,<<<+<:__>:~:~__:_~+~;
                                                 ..   .    ''.''..     .''.'   .    ...
                             ';,II+_<l>~<>i!<;::::::;;I<>~il;;;:::!Iiii;;I;:>i!:;!;!i<;::
                             I` ::[()![{{1~+)i:::""""":1]-!:""""""~l|)|<~>++fr|}[|?|t/l ,:
                             ;                .            .           i-<_+I+:!_!_<->: 'I
                             ;  `i}><+'                                                 `l
                             ;  .:)-);   ~{!      i_]I   "~?i   "-_+     ..    ..       `I
                             :    ]+-.   -/-""    ^":'   '";^   :?_\'   )1I   i)>'      `l
                             <   .]<[,   ?{--i    -})I   ;])>   ,~~i   '-+I.            `I
                             <   .]~}"   li,      _]{l   :?)~    i;;l   >+>`            ';
                             l   '{_("            _[{l   :{\+   '![|;   ?-              `I
                             I   .[?]`   ~?,      -{|l   .,:^     ''    ^`              `I
                             !   .[?("   [/~      <?[,   "~_l   ."`"                    `I
                             !   '{~},   l_;                    `>!~.                   `I
                             !   '(>i^                                                  `I
                             i    ,''                                                   `I
                             ,                                                          `I
                             ;                                                          `;
                             >   `;^~lI'Il"!I`                                          `I
                             !   >~~[?{<;l,!I`                                          `I
                             !  .I^"',:"      .   ....   ....'....    ....    . .....'. `I
                             !  "li-I`lI,i_,`!;i<~^'l:>_+'^l'.`'':I,:-,`II<<i:^!"''''^' `!
                             !'  I?[<l:,+_+!"l^+{{+,":{][<:,:>,!!^"+_1_."^]_l' I';ll!i, "I
                             ';,`">i!l;,>i;ll:';!!!:`"iIIiI^l~l!!,^i<!+^""i!:^':`!<i~?<:;.
                               ';;:;l:^l;;;l,`I::,;^^I::,;'";,::;^,;,,,I`:;Il!l`:;:,:^''
                               `>I-~.+Ili?_`<>I~_?^<;,~?_"i>,_{l:,!"-1lIl>"_+">!!I])^_`
                               '!lll:!"!!ii:I,lll!I:"lIl!I::ll>il`:;Iill"l;II,!"lll<:!'
                                                                          .  .   .  .
                 .!>. :l,:::"":<,>l::I;;;I.
                 '>>' ,llI!l"Iii"<!li>l>ii'

                                                    .l!<i::i<!;
                                                    ']!>~Il><<_
                                                    ^>;+;.`li:!
                                                    ^+l<>,li>!~
                                                    .]~?+li>~<<
                                                    :!l~^``^^'
                                                   '" "
                      ^^.''''...`. . ......  .  .    ' '.   '.   .             .              .    .
                      <~__i>+i+:~_;!<i_~:i+-,<:~~_~-_-">-<;--!i++~--^>_~+~~_-l~?_<--iI+<<_-I+l+?<!-)"
                      ";^..`,.'''^^''``''`.`'`"^..'.^`.'`^`.^'''..''.^''.'.`''`'"'`"'  .... .. .. .
                      :>~!l+?l+~<>?i"<~><_Il<>-~><<>?]"-~_];~_iI~!__I!_-;~II-~>;-<_~^


















```

*Figure from page 7 (2346x3317 px)*


---



PF03 OPERATION



»010®



N100 GOO



N101 G56



N103 G41G01



N104 G03



N105



N106



N107 GOJ



N108 G40



N109 GOO



N110



N111



e:E WHEEL! 00. MIN



file end



EDIT



X300 Y300



X400 Y200



X500 Y300



XlOO Y300



X200 Y200



X400



P MODE



X300 Y200



S250



Z-55



FlOO



1-200



1100



Z100



4203-E P-218



SECTION 2 PROGRAM OPERATION



l'IHEEL100.MIN



97/07/15 14:10:00



M09 M03



011



J100



LINE LINE CHAR. CHAR. LlNE EDIT



INSERT DELETE INSERT DELETE DELETE ERASE QUIT [EXIDOJ



@ @J@J@ @J @J@J @J



(3) Cursor Downward Movement



Each time the cursor key is pressed, the edrt pointer (reversed display) and the edit line (>>) move



down one line.



The edit pointer and the edit line move continuously while the cursor key is held down.



When the cursor key is pressed with the edit line (>>) placed atthe bottom, the edit line(>>) moves



to the next block (the first line in the next page).



PF03 OPERATION



>~000



N100 GOO



N101 G56



N103 G41G01



N104 003



N105



N106



N107 GOl



N108 G40



N109 GOO



N110



N111



=E WHEELJOO.MIN



file end



EDIT



X300 Y300



X400 Y200



X500 Y300



X100 Y300



X200 Y200



X400



X300 Y200


#### P WOE WHEEL100. MIN

97/07/15 14:1



:oo



S250



Z-55 M09 M03



F100 D11



10 JlOO



1-200 JO



1100 JO



Z100



LI NE LI NE CHAR. CHAR. LI NE ED IT



INSERT DELETE INSERT DELETE DELETE ERASE OUIT [EXTEND]


```text


                                                                                               ^"""','':'^^"
                                                                          ''.'`... . .'....'...~[_]i?l;<!+<-
                                                                         "[_~<>++-l+`i+]-+?]]?1i;~~]+-+<<~-<
           ``''```^^^^^^^`''''`````````''''````````````'''''''..'.'....'''''''.''.'''..'`'`.''`''`.`''''''''
           """"""":::::::,"""",,:::::::"",":;::;;;:;;;:,",;;;:",,","""",;;;;;;:,,:,:IIIIII;;,,::,:;IIIIII:,"
                                              .
                             ':,ll>~~i~~<<il!ll:::::::I<i<!:::;lllilii!;""",;:IIlI,:,;::`
                             l. ll{|)i({()+]1;,,,,,,:,i\]?:,,,:;:;_>f){II;l+uf(?}|-\({^.!^
                            .I                ........    ........ .  "-}_{+>-;_+~]-1<^ ,:
                            'i  `:Il<)^                                       .         lI
                            `!  `i{?|+' ._?,     '~_+.   ;~_;   ;++l                    ;:
                            ';   :1?~   ')\i`.   .,::    `:;`   >-{[   ,1?^   --!       :"
                            ."   ;)-['  ')}__,   ^}}-    <]{;   I~-!   :]_,   ``'       :"
                            ';   ;)-}.  .++"     ^{11'   >1|l   ^<:;"  '+~~             :"
                            'I   I\{)            `[[1`   ~{|i   ^i|1,  '(;              l:
                            'I   ;)?_.  ._<`     `([]'   `,,`   .^:^   .I'              !;
                            'I   I{-[   `((;     ^[]?.   i~_:                           I,
                            ':   :}-{.  '?]"       ..    .''.   :!~>                    :^
                            '"   :1~+                                                   :^
                            ^l   `i:^                                                   :^
                            `:                                                          :^
                            `;                                                          :^
                            `;   ..'^^..^''^`                                           :^
                            `;   ->?[1?i_!<->.                                          :^
                            `;  .l^;.!i"                                                ;^
                            ^I .:I,l,^;""lI^"II!!:^",;;l,"I;:"^^^;:,;l,";,;;I:,I"^^^"". ;`
                            `I  '!?|;^;:i]["^:l1(_"`'~[1_^;"^`'^'!;i_)" lI[<>.'l.`'`^`. I`
                             ;,' ![??:",[<<+l"^_?+<"`>-l~_I,__i~!""?--~ :"_l: .,^__~][!"l
                              `^:;",,"^:":;I,":^"",^":""":"^:"^""^"I::I:^":"";;"",^^;,,^
                               ^!l_l^!;l>_<,l!;++>;I!:~_!lIi:][I!"i;-];!:i!__:i,l!-?:>
                               ">!>l,!l!i~~,i>I<<i;!i:!+!l!<;<?ll,<:~-;!Iil~>^<;!I~]^_
                                .''`^  '..'`  `.''^  ^'.``  "``^' .^..`' '^`^^' ``'.^.
                  ""  ^^'`'''"'''....'`^'...''.'
                 "-_. i><<<i,+<+_i+--~l[_<~+>?~_'

                                                    .:;l:^,l!;'
                                                    ;?~~~Ii<+}+"
                                                    :!l>;':!i?;l,
                                                    :iiiI`;ii!> ,.
                                                    ;-~-~I<+_+i
                                                     ^,;,^^",".
                      ;,,:^"""^,;^`^^"^^^"^'``'^^^^^^.`^'.'^`.'``"`.``''`''`'`^'`'.'.'.`^'..'"``''.. ..'....
                      ~+_~;!i>i>-~;>~i<<;~+iI!<~<~+__;!_+;_-i>~i!--"i~<<~>-_!~_]<_-!i_i<>+>!~]i~__;iIil<<<~l
                      !~!+!"<<lii>,
                      ,:^''^,'''`"^'.''`^^'.'``'`'.''......''.   .'  ''. ''       .     .  .
                      l<~I>_~;+>i<?!:]<~>?_:--~;~_;!<<<~;~>~_i<<i+]ll[<_!~_<:<!>~i,__il_;+_-:<<_+l
                      ,;"^``:"``.`^``"^'`'.````^```^,',^'`^,`"^`'''^.^''``'``"`.^'^^`" "'''`"`^`'.. ..'....
                      ~_<?lI_<!>~>+~:_?~!_i>+_~__l~_+I+_!<_-I~~~I!I!<?-<++l]>>_i~>?-~<,~_<l_}ii<_I<l>;<+<<?!
                      ~:i~<;<~+I<_>_;!?<;ii~:+ii:<"><:l>~i!~__-;
                      ..  . ..''````'^.'. .'.^^^^^``^^''`',":;,^'... ..```'. ... .. ...
                             ",,;!_+il_+__~+>,:::,::,:!<i!"::::::Il!>>I::::i>!!:!II!l!:;'
                            `; 'l>[1_i{?{?<{]"""""""::?(-i"""":,"!i]|)]!i!<{ur1[\1}f/[ 'l
                            ^^                                        I~~<-!><,+l><+-!. ;.
                            ,: .;]\~]!                                                  ;.
                            ;:  '-1[_.  ,{}.     ,_->   'i+-'   ~]};    ..     .        :.
                            ;;   >]-l   :))I:'   `,:^    ",,    -~|> . ~|_   .1-:       !.
                            ""   ~[]_   ;/]_<"   !()_   `?1{`   >~>`   !+<,             i.
                            ^^   <?]~   `!;      I]]-   '~1{`   :lIi'  :?il             ;.
                            "^   ~-[-            I}{?   ._1)`   "+/_.  ;)               i.
                            ,,   <_-!   "[>      I)1~    ^",.    `^    '"               i.
                            :,   <?{-   I){'     ;?]i   '~~_'   '''.                    I
                            I:   >-[-   ,++.                    !!-:                    ;
                            l:   +]~!                                                   ;
                            l;   ,,^'                                                   ;
                            :,                                                          ;
                            ^`                                                          ;
                            ^`   ^.,,^'^:'",^                                           >
                            ;"  ,[l{[(}<_:_+!                                           i
                            !,  ",^,^!!                                                 !
                            !" 'l;!l'^;,,~;':Illi"`:,!!>""i"`^^`"l:;il^:I;l:;"::^^^```  I
                            :,  ^<1];"I!~}~I"^>[1~,;"{]}i";`;^",'l;<[]'`I~?!I ",`"",,". !
                             ;,`.<~>~:,!?!i+:`:~~_!,"_<!~>`:]<i<:,;]~_;':I+;" ""l-+?{}!,,
                              '^:^^,,^":`^"^'^"`'^`'::,,,``"``^,"^,^^^:^^:",,;",;"^^"`^'
                               I,<+;;l!,_-I!I<:~_:i:II_~^>li!]+"i,!!??,i;I<_<;i;;~?<Il
                               !Ii!;l!!;<_;!I>;!_;i;!Ii~">l>!<+,i:i!>_"iIllil:<l;!+>I>
                                `''`'  ^'.`' .`'.`. '`'.^. '`'.`  '`..`  `'`^^  ^'''`






```

*Figure from page 8 (2346x3317 px)*


---



4203-E P-219



SECTION 2 PROGRAM OPERATION



(4) Cursor Upward Movement



Each time the cursor key is pressed, the edit pointer (reversed display) and the edit line (>>) move



up one line.



The edit pointer and the edit line move continuously while the cursor key is held down.



When the cursor key is pressed with the edit line (>>) placed at the top (01000 on the display



screen), the edit line(>>) does not move.



[Supplement]



PROO OPERATION



»01000



N100 GOO



N101 G56



N103 G41G01



N104 G03



mos



N106



N107 GOI



N108 G40



N109 GOO



N110



Nlll



,:E;



WHEELlOO.MIN



file end



X300



X400



X500



XlOO



X200



X400



X300



EDIT



P MOOE



Y300 S250



Z-55



Y200 F100



Y300 10



Y300 1-200



Y200 1100



Y200



2100



LI NE LI NE CHAR. CHAR.



LI NE



WHEEL100. MIN



97/07/15 14:10:00



INSERT DELETE INSERT DELETE DELETE ERASE



M09



D11



JlOO



EDIT



QUIT



M03



[EXTEND]


# CED

® CED



@ @J @J @


## 1. When the cursor key is pressed continuously or held down until the edit pointer

(reversed display) reaches the left-end or right-end position, the edit line (>>)



moves up or down, respectively.


## 2. The edit pointer (reversed display) is placed on the edit line(>>). This means that

the edit line and the edit pointer move together. The edit pointer moves as the edit



line changes.


```text


                                                                                               `,,"^"" ;'"^,.
                                                                          ``''^''`... `'''.''..>?-?_-~`_I_i["
                                                                         .[{+<<+~?<<I`+_+~_]-_}?:<<+_+-+i<>-"
           '^`^``^"""^^^"""^``^^^^^^^^^````^^^`````````'''`````````````''''''`.'`'''.. .''''.'''''..'.'''``'.
           `"""""""",:,,"""``^`''`"",""^^^^""":::::::::,,,;;;;;;;;;;;;:,,,"":;;;;;;;,,,,:;;;;;;::::::;;II;;I'
                  I_, `<;Ii>I,~i>ill:-<I!!l>!i.
                  ,;^ .",":;"`I;;;:,^;;:;;,l;:.
                                                      .'.   ..
                                                    .<+++l:i+i<^
                                                   'i![<i!;><!-^
                                                  .I.;!<!` ;~I:`
                                                     _!<<!;ii!_`
                                                     !~_<l;><i>'
                                                      .'....'.

                      ^l^""^,^"`;"'''`^`'^^`'^.``````^.:^''`,'''```'.''.''''`'^'.`.....''^. .'`.'. .  ...  .
                      ,~~~iI<i+;++!l>!~<:i--:_i+>+++_+^--!i_]>~~~<[>,~+>_i___i[_]--_;-~_>-+I_??l>_<!ilii<~~_^
                      ^~i"<>Ii~-"
                      'l"'''^`'``''.. ..''.  .'.'   .       ..        ..  .
                      '>l~;_->l+-+?-,++~I~-li_[I__~:~><_l!+>?+!~<<-],-?_?;--!I~<<+I>-_:+!i+-~I_>++^
                      '",`^'`"^.`.`''''`' `'.`''''``'^"'`^`.''"'^^'^'''.''.''````"'.`"''``^^^`^'`''.  ..
                      "-~>+I!-+,i~><+,!_?"~!>_~__++,i-~"I<~"~_]"i>+^<Ii,++?~?~"[I--<I_-,>+l<]}>,~:;--"+-[~-]'
                      ,~!>~>>^I?_:_[-l>~:iIlIl]>_ll~>;~<!+:             .             .             .   '..`
                      .`'.`''' .'.``'.'`.`''''```'.`'.``'^'
                              ^","```"^^:^""^,;:;;;;,,,```"""",,,,,,^''^"^",^,",,"^'^^,^
                             ;,.~i/\)i{(\([}/l;:;;;;;,!|--;:::;:::?+f{{:,::if1|-]{<[_["^l.
                             !  ^^:::`:::;":;`'```````^I;:"""^^```""iI~-}_{[1/-1[])1\[" ::
                             l   .''^"                                 ^^`""`"`^`'^'^`. ,:
                             :  ,>]_|<   II^     .li!'   :!i"   `;;:                    ;;
                             ^   ^{-]   .1\i      l!!'   "!i"   !}{1   .+>"   i+;       ;;
                             ^   "{-]'  .{}~-l   .i~~'   ;i<"   !+?]   "\?^   !<:       ,:
                            .;   :)-)'  .{]i"'   '))\"   i))!   ^~:`.  `l>?.            ,:
                            .I   ~v[{.           .-?1"   !1)!   ^!_{!  .->`             ",
                            .I   ,1+1.   :"'     .})}^   "<<,   'I_~   ._:              ::
                            .I   "[+].  .)1;     .{||"   ,I!^                           I;
                            .;   ,[_).  .1)l      :;I.   ";i"   ^>~>                    "^
                            .;   ;{~-.   ""'                    '":,                    ^^
                            .I   "-ll                                                   ;:
                            .I                                                          lI
                            .I                                                          I;
                            .I                                                          ;:
                            .I   <!_1[_;+<!-<`                                          :,
                            .;   >:<,~_:                                                :"
                            .I  ,l:I"`"^^::`^:",,,^""",;:":,"^^``""^,,^^"^^^"^^:,"````. :"
                            .!  '!-|;`!:l])"`l;-1]"`">?{-^;I``.`';;I+),.<I[~~`.>``''''. :,
                             ;,. l]?]l;,}<<?i,`-}1-"'!]><+l;_}>+<""+-?? l,]!l  ;^-~i-{~`l.
                              ^":,^,:^^,,:,:^"I;;;I"":",,:^"::;;;::I,^:,^^:""::"":"^:"::.
                               '!l->,!,l!~~;l:I~+<;l;I+_>I;I;+]ll"lI-?!l:!l__l!"ll~?;<.
                               ^<l~i^>l!l~_">iI+~~,>!:>_~;ii:>-!;;i:~]!lliI_>^iI!:<{^-`
                                `^'^". ^"^^". "^^^"  "`'^" .,`'^^ ."''^" ',^^^^ `^`'"'
                 ^.  .... .'.        '`             .
                ,[__}-?++-~};   ^l  ;-+>~:I_+">ii~<`~__`<:~i+~~+~:i<i-~<<><-~'>^i<-+`->+i^,<?iI-<`>__^<<++_i
                   ..               "<ii<l>~i'+_~<<il^~>>i>~l"++,:+];~<>"~I,_<+;><<;I<<_+l<`!]>"ii]l><+:!lll
                                    I+i!~<!i>`>l-~~]!.i++ii~_;!+:`;:^;:,.:`.;!,^;,:`;;:;;::'^Il':II`,Il`,,^,
                                    "I;;!i`I<`l.;!li;.;!~>ilillll
                                ^"  `,''.':`.^`""' .``''.''.^`'^'``^'',^``^'^'^``'^:``^''''` ."^`''`''`''"'`
                                ;i  :ii>l_[>><<i?i:+~i_i++~;_-[+-?;>!<?-<_<;+;<_>!+]!!i~;i;i^ ;!<;l>~-~~l<<+
                                    i-i:~+>,l<,>!i!-~I<+-;~<<+_,I+ii<i_<-[?-! I~_l!~?I~<~<?i:+<!>+:~<l~<I>__
                                    i~~I!~<~i-~!.'  '.''''`...' ..'''.`"^''`.   `''^''"`''^' '^``^'^^.'^'^^`
                                    ^,,^""::Ii;"






















```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-220



SECTION 2 PROGRAM OPERATION



[Supplement) 3. If there is a record exceeding 63 characters {one block of data is not displayed



within one line) and if the edit data cannot be displayed within the display area (16



lines), a blank line is automatically generated. The symbol of"@" is displayed on



the automatically generated blank line so that it is distinguished from the line



generated by the "one-line insertion" function.



In this processing, a blank line is generated only at the bottom of the screen and not



generated at a middle or the top of the screen.


#### PROG OPERATION EDIT P MODE WHEEL100.MIN

97/07/15 14:10:00



»N098 GOO XlOO YO



N099 000 X200 YlOO


#### NlOO GOO X300 ¥300 $250


#### N101 656 Z-55 M09 M03

N103 641601 X400 Y200 F100 D11



N104 G03 X500 Y300 10 J100



N105 XlOO Y300 1-200 JO



N106 X200 ¥200 1100 JD


#### N107 GOI X400

N108 G40 X300 Y200



N109 GOO 2100



N110 X200



Nlll YlOO



N112 001



x,oo



¥200



N11m X200 Y300



=E WHEEL100. MIN



file end



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELETE INSERT DELETE DELE1E ERASE QUIT [EXTEND]



@@@J@@J@@J@)



The cursor is moved.


#### PROO OPERATlON EDIT p f.llDE WHEEL100. MI N

97/07/15 1 :1



:oo



»N099 GOO X200 Y100



NlOO GOO X300 Y300 S250



N101 G56 Z-55 r.t:l9 U03



N103 G41G01 X400 Y200 FlOO D11



N104 G03



xsoo



Y300 10 J100



N105 X100 Y300 1-200 JO



N106 X200 Y200 1100 JO



N107 001 X400



Nl08 640 X300 Y200



N109 GOO 2100



Nl10 X200



N111 YlOO



Nl12 001 XlOO Y200



N113 X200 Y300



Nl llil GOO X300 Y200



&2400



"E WHEEL100.MIN



file end



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELE1E INSERT DELETE DELETE ERASE OUIT [EXTEND]


```text


                                                                                              `,,,^"^ ;'""".
                                                                         '''''.''... `'.......!]-]+_>`+I]??^
                                                                        '??+>><<__>l"-_?<__-?[_,+-~~_?+><~?^
          .`````^^^^^^^^^^``'''`````^`^`````'``````````''````'''''''```''''''.''''`''..''''''``'`''`'''.''`.
          '"""",""""""""""^^",""^,::,:"^^^"^^^^^`",,::""^",""^""^^^",:,"`""""^^^::,:,::",""^",:;::;:,"^^""^
                >_I>i~<!i!>~    <^  !^!lI!'I^:^:l:;l:^I;;l;i;l`I~""!;:I;iI;"`;:I';l,!,`l'lli"""',l`I!:ll::I"
                ;;;!lII,;::l    ;`  !l~~>iI<I>ii+l<<!l++~<<+++>>-;I>~>~~~~iI>~!-;!~<+!i~:<]?!l+;>+;>_-~_++?:
                                    <+>il"i<>I><<:~Ii:;!<l!<+:<+_!;<<i!<:i>:__-~-~>!:~<<>^~<ii+-+i-"ili!;!+,
                                   .i!++!.>;++i~,+<<;!:+>~>!<[!~->:[>i+>__~i :<<l;+>iii,l~'-_.iI!_<+-<>+!Ii'
                                   .+il`+!~i!>_>>-~^!_<<i!_<+:<+<+!l_il^<;:?!~^~"~;!+_+!<i!-+i>;~>+ll]~:!><^
                                    >~>l~<_<l>_l]-+"?-~i><-i~;~~?ii,><!:-i;<;l',.l.,Il;I~ll;li:';I;`^;l'";!`
                                    ~<;i:li>;^>,ll;.::!":;>';!<l!ll^.!;I<<!,
                                   .I`l;:^,,":::;",."";l,:`I:""^^:",;,I:,`"::^I:I;:;:i:;,":I;,":,;;;`:::,,;'
                                   .il<<<<+i~i_>~!}!~~++<ii~<>>>-]~+_<++<!><+:<Ii~lii~>!;lI!>!;~l~+~:_>iIi~^
                                   .-+!~>~_<>,+"i:<<~_<`~"i<l:><^>I<>l;>I<_>^
                                             ...  ...  ..  .''```'...'''....'''.''.''`'..  .''......
                                           :;;;Ii!l!<>!I;!I,;;;:;:::!!!!;;:;:,,;I!i!I,,::lllI;l;:;I;::
                                          ,: ;l-(|>+|)|-</-,,":,""""[1~i:;;;;;;+>|\|+ll!>fv/}-(){t\_ "I
                                          I'               ....    .     .......    i}+~-i]>!]>?<[_l  !
                                          I` ',>~+"   ;~!      ;li:   ^<'                             !
                                          I` '"[|t!   ~|]      _((<   :}-~                           .<
                                          I'   ?[{l   </[      !][!   ^<{]   .-?["   .`'    ``       .I
                                          !`   ?}[:   i(];:.   `":`   .""^   ._</;   {)<   ^{_"       ;
                                          !`   [}1! . ~t?_!.   ~||~   "{){.  .>+>    <~_"            .~
                                          I'   ]}1!   "l:      <1{<   ^]|}.   !>!<.  I]i,            .<
                                          ,'   ]{(!            i{{~   `-1]    l+|!   >{              .<
                                          ,.   ][?:   i|<      +\/?   .,:,           ''              .l
                                          l'   _-(i   >\[      I~~I   `~-~    ,":'                   .I
                                          l'   ??[l   :~l      ,l!,           iI~"                   .I
                                          l'   [~i"            ,!l:   .lii                           .I
                                          l'   {__l   !?I      Il~I   "[){                           .I
                                          l'   {+1}   .^       <{)<   ^?{-.                          .I
                                          l'   {"I;".^,.""`     .                                    .I
                                          l'  ;?>)[|_I~;_>;                                          .I
                                          l'  ;,""^!!                                                .I
                                          I. ^ll~!",:,I_:"!;l!>"`l:!i<"^!^'"`'^I""i;^I!!>l;^::`'''^^ .I
                                          ;`  "+)-;^"i_)~:,^~1(<^;:[]1!^I^I`,;^:I~{?``;_}i; I:":,,:" .I
                                          'I"''+~>>^'!+l>i,':+~~l,"+i!ii"I[!>+:"I-~-:',l<," ;,!-><{-;:`
                                            ',l":::`:l;I;:`:;,;l;"!I;:;"`:,:,:"^!;;,I"^;;;;l^^l,,::`^.
                                             <,]<^!!>"_?;l!<I-]"<Ill-[`<l!!{?^>:Ii]]^>!I-_<,i!;~}<l>
                                             IlilI!,l;Ii;I"lIli:!"!I!<;l"!Il>:l^li>+II:llI;;;:ll>!!;
                                              .  .   .  .      .   .. . , .  .   .. .    ...  ..
                                                                        ?
                                                                 l!I;>!>l!;l!l<!
                                                                 .```"^",^``^^"^
                                                                        _
                                           .'`'.'''....'''``''`^^^^'.'.`I''''````''``'''.  .'.'`''.'
                                          ":,I!-_<l+<<>i~~:::::;;;;>-><;:II;::I>i_+i;;;:!~~>;!!l>!i";`
                                         `I ':i]}-![?}?i-?^"^"""""^~{>>",""":,l<_t}?>~i~[xx({{1[/)]  i'
                                         ^,                                        :+~i+lI!"<li>i_l. >^
                                         "; .:~??~   ^?+^     "??+   .!<-^                           !`
                                         ": .'_{]~   "({^     "[1[    >[}^   i-]!    ''.   ''.       l'
                                         ''   i}<!   "{[I:'   .`^^    ^"".   ~>1~   lj-.   1?!       I'
                                         .'   l{+?   "|}-~^   :((}   .-)|,   !-<^   I_>;             l'
                                         ''   i]-+   '!!.     ,[[}    ~{{,   "iI>^  `?i!             !`
                                         ^"   !-]]            "[}}.   +11;   ,i)]`  ^("              l'
                                         ""   <?_~   ^[+'     :(|1    ^"".    .'    .^.              l'
                                         ^"   >?]-   :|1,     ^+?+    <__^   ``^^                    l'
                                         ""   i]_?   ^++^     "II"           ll+>                    l'
                                         ""   i_l!            :>i:   ';;I                            l'
                                         ""   ~[ll   `+i.     'IIl   '_}{`                           i^
                                         ^"   ~{!-   ';"      :)|1    _{{:                           >^
                                         ""   <]_/`  '-~'     ,}{-    >-["                           i`
                                         ""   ~}[\_'`;"::,                                           !`
                                         ^"  `]!{_1[l>;>i!                                           i^
                                         ^"  ^I`,'!I'          .      . ... .                        i`
                                         "" ';I!<''I:,~!`:ll<_l'::!<+I'I;"^''`l;,l>`^l;<ll^"I`''``^  l'
                                         ^;  .>{{i";;+_-l,:l1)]!^'_[}-;,"l,:!";;?-1l lI{!i .;';:;;I^ l.
                                          ,,^.l<!<:,:+;I>;"`<<~i^'I!Ili,,~>i~!:,<>>>.:"i,: ';:~>~~?i:,
                                           .^I,"::`^l:;::`^I",,:`"I:::,'",""::^::""::',"",;"`I,"^:'`.
                                            Il>-l^<!:<-<,!~,]?i;l>,-[;!li,{1,l"<I}},!I>:++^+lI!?]^-
                                            ,!i!!;l:l!~>l;!l<<il:l;lili,ll>_ll^!li~;!,il>i;<:lIi~:<
                                             ...''  .....  .....  .. ..  '..'   .  '   '''`  ... '









```

*Figure from page 10 (2346x3317 px)*


---



5-2-4. Page Down



When the page key



4203-E P-221



SECTION 2 PROGRAM OPERATION



is pressed, the next page is displayed.



On the display screen, 16 lines of program data are displayed on one display page. When program data to



be edited is not found on the given page, press the page keys until required data is obtained.



Positions of the edit pointer and edit fine remain unchanged.



When the last part of the file has been reached while the page key is pressed, the remaining blocks are



displayed on the screen. The message "file end" will appear on the command line.



5-2-5. Page Up



When the page key



is pressed, the previous page is displayed.



When the first page has been reached, the display remains unchanged even if the page key is kept



pressed. The message "beginning of file" will appear on the command line.


```text


                                                                                                '``'.`..^.''.
                                                                           ...''..     .        _]_]i-,"<l?~;
                                                                          :}[~>~~_[;?'i_]+__?-]1!;__-~-_+~~_+
            ,,:,"^^^^^"",""""^^^^^^^^^^^^^'`'`^^^^^````'''``''''''''......'``''.''''`...'`'^''`^''^.`'`^''``^
            ^^"^`^^^^'.'""^^``^""",,:::::,"""";;;;;;;;:,,,;;;;;;:::::::,,,:II;II;,::,IIIII;::,:,,;;I;;;:::::"
           ._;+;<   ~<_+Ii<>~~'
            `'`'`....`II`'^^^`      ^"`
                 ,[_<-Il~~;_--_I-_i;[]?^i!><<<<+~,l_+,><~!l~~_;!lI-<<+>i>l
                 ."'`,''`^`,^;^.^^^.I-l'^`"`^"","'.`,'^,"',,I!`^^^::::l::^
                 "~iI~~;<__<_i;~!+-<`.~<~>ii,<iil~~i<l:+<<:!;"i<<lii!i:;::!lI!~><>!;i!i>.:-_ll,IlIil>i:liil!l
                 I_ll>-_<><il_~l~i<>>;<:~~il+i+iI_+<_`l~~~ii-~li?<+~<~!>,i>-l!<+><_<i+]?,;>l~+i~ii[I!I";!!lIl
                 `;`'"^""^`"'"".""""``".`:^:I,:^^;;il':,;;:`;l^,l>>':Ii!^!I~"Ii~!;i>^i>~!ll;~>_l!>!.
                 I<>_+><<Il<i+<:<~~;i~i~+^!ii;!>-"IiI:!iI!>,,Ilili;il!.
                 ''"^'^""'^'."".""^":,`";.,""':"".`:,.,:":;`":;,;l;_I;.
                 ;]>l_,i<>;_-l;~+;I<;<~:~<"i~i^<<>l'>i!;!>!,~!;I:il`I!i>,>iI,i"!I!!lll.<!,:!ll!;!II:!I;!l^;l;
                 "-~+~~<+>:-I!_<I>!ii<;.!-i;i+i<~~!>I+}>;~><>I~<:<>>+~+i!l-_;!i<i<<<<>;~<!"l:;!,I;~,!Illi"!!!
                 `;I;^I;;^';'"::^l";!I` ':I"^li!!i<~^`>i^lI> ;<:,+><ii",<`!>i">ill;~!>I>!<
           ^i;li:  '!I:;`,l'
           `I:II:  '"I+>^:~^         .
                 l?!i>^;!l'!i!;;ii":]{i.l";IlIl!l'l!:^I:,::,:^:;,:^:'I:,::^":'
                 `;`;I^",;,li<;^Il`"!;; I"l;iIl!I':ll:!IlIlll:>+?>^>^>>+>~<i<`
                 I+~li`!<i'<;l'll!>'I>>':I;; ^lI;!I:" <:`'!:;;;..::^;,,.."^,";",,;^:,::':`;,``"""^`,^`'^."^^`
                 I~>~~l>l:!-<!l_+[-l!_<!<<+<I>_~i>~]>:>~i;~__>-l^<>>]<i:l+i>>?i[+~:i!<>^I^>~;!~-}!,++<^~^~-_l
                 i!!i!i!" ";!";i>!>+?+ l~<?li<!-,l^<+:`_i"<-<~_<^i;l~~,!~>>!~><;<i-"


























































```

*Figure from page 11 (2327x3290 px)*


---



4203-E P-222



SECTION 2 PROGRAM OPERATION



5-3. One Line Insertion



(1) This function inserts a blank line right before the edit line.



Press function key [F1] (LINE INSERT) to insert a blank line before the edit line (>>).



(2) Lines following the edit line shift down and the last line on that page disappears from the display



and shifts to the next page.



(3) The edit pointer shifts to the beginning of the inserted blank line.



(4) One line insertion operation at the line which has more than 63 characters differs from ordinary



one line insertion processing. (See the figure.)



N101 GOO



N102



>> &Y100 □



N103 G01



N104



N117 G01



=E WHEEL100. MIN



ti le end



>IL



XB00 2200



X250



Z150



X300



X113



LI NE LI NE CHAR. CHAR. LI NE ED IT



NSERT DELETE I NSERT DELETE DELETE ERASE OU l T



Press F1] (LINE INSERT).



N101 GOO X800 2200



N102 X250



&Y100



N103 G01 2150



N104 X300



(5) The prompt"> IL" will be displayed on the command fine.



(6) This function is effective for inserting lines in the stored program.



F0.3



[EXTEND]



F0.3


```text


                                                                                               .'''.'' "....
                                                                              .                l[__<~>.?;--]^
                                                                         '?[+<>+<-<i!"]?-_??]?[-;+_]]]+~<+_]^
           '`'`'''```````````'''''''''''''................................``''.'`'``'..'``^`'`^^.`'`"'^`'^^^.
           '^^`,,::,,"",::,,":^^^^^^^^,;;;:::;I;;I;II;;;I::;:;IIIIIIIIIIIlI;;::::,:IIIII;;;,,,",;III;I;,,,,,.
           iI:<    l<!!:""l;l`>;;IIl:;;
           ll:>.   :i!~I"!!l+^>l~+>li<i.
                  '`   "'. . . '       '  .'..'...  . '.. '   ..   ..
                  l~: .>>~;<_>~?<~;~-?+?:il~-_-:l>~^~[+I<-]~-i~-~:__+l__i
                      ^I^^^'"'`'"`^'^`..:^^'^`^,`^,":I:,^'`.`'..^.'`'.```'..'.'.. .'   .'..
                      ;~~~+il~i>_+~;<_+;+:~I~!~}!!--]_-~>l];>~?_<!>>--+<l-->~]+~<<l--;-][I__!li!>.
                  '^.       ' .     ..   .'..                                                .
                  +[: :i<~?;~~<~+~++i_<,_-~:i~;_~_<>?+-ll_<<~[_:+-~l<_!i-;[>?!_-]?,_-_]-__-~l>><>;__l>?__-_^
                      ,?<<;]>]<;_:?_!;~~+I~<~-`.   .... .... .' .'. .'.''...''^`:^.''`""^`^''.'`'.'^'`^,"":.
                      '^''.`..^ ^...^.^^'`,,l"
                 .<?^ ^<ll,i+>,iIl~!^!!~_,::;<i,i!!i;ll!"Ili!l"Ill;l;III;II,!;:
                  ::'  `^,^:;,:;""I;.;:I!""""I!^Il<l":;+;;";l!`:ii:ll:;ll;l,lI!
                  :!' ^I::`I::'",:":"^."^:";;"`':`,^':``.",`^'^^^.'`'^.^^''."" ,""^^^"``.,l"^``^`^.''^^'`'
                 .l>^ ">i~;_<<;>~_~~il:_++i_~~l:_I-+I<~+,?<!>lI+-lli><l!<+>:-+,+>]<-~-ii;_]?~>I~~_:i<_-~]_"
                      "<>lI~~:ii_<<~~,~<!<<<~i<- "-_-I!+<,?[~~l:
                         ^,`^^`^"""^^`"^^""^""";""",,"^""^,I"`^,:::,""^""`''`^^":::"""^^^^^"",.
                         ;"       "!;I'         Ii!`        ;!I:....    'i!l" ...............;"
                         :^       "<i~^         "I;'        >?_<        'i!!"                :"
                         :`    .  "i!~I.        '           I>i!                             ;"
                         :`   ^l` ;~:!~"        i:                                           ;"
                         l^       I>l+"         !_l.                    `i>-:        !<l!    ;"
                         I`       :<!~"         ..          i~+i         ..'.        ..'.    :^
                         ;'       .`^`.                     ^:,^                             "'
                         ;'         '                        .                               :`
                         :'       `",^.         ^^`         `"``                             I^
                         ;'       :!;I.         >_l         iI;i                             I`
                         ",^^^":::,""^^^^^"""^^^""","^^^^^^"````,,,"^^^^^^^^`^^^,,"^^^^^^^^^^l'
                                  ..            .....  ... ~`...................''............
                                                           i'
                         :.    . ..   ..                                                     ^`
                         I.  .?+;\}1+!--,}~<                                                 :"
                         ;.  .<^i!:]+; .                                                     ;"
                         >.  .;'                                                             ;"
                         i. ."l~l`^^"`^`'^^^"''''`^^^``'`""""""^^^`^`''.`^^"^'''''```^""""^  ;"
                         ;   "I:)i '!I;~|" ^,!-][" "^<~{]`.i` .   'l":<):',;>]!>,';i'''''..  I"
                         I,   i[[?-"",}_+<_` `_(]_!' ~}<+>::^~lIi~',"{?]['.;:[I!' ";`>!!><!^ l'
                          ::"`:!lll"::il;:I^^`I<!I:"^;iI;::,^!I;:I^,"i!l~^':^i,,'."""<!;i+~l;,
                           .`^l::;ll",l:::;"'I;,;Il^"I",";"'";::,;"^I:^",;`^I,;:;;^:I^^^:'``.
                             I;!-<.l,~"__+`<:i:?_l;!i,~?]'~:_"}}!"i"iI][IIil:~~_^+,i"][+,<
                             ;!i~i:i^!:ii>"i"!:i<I;:I,!i+,~,~:<<i,i"i;i_ll!l;ili`_:>:<++,<
                              ``->^^:,l;I!I^^I>lIiilIi,`'^. .^'``^  ``''^^  "^^^^' ."``^"
                                 "",><+<<>>><>+ii++]+<!.

                                                           I
                         "",,::"^^````^^^"""",::"`'^^^^^^^,[`^","^^^^^^^`'''^",,"^^^^````^^^^`
                         i..... ..:^""       ..';;,        .;;I".. .....`,,,.'''.........''''l
                         <     .  _1-I'```````',]]_"^``''``"_-_l^"^'''''l+++`.''^^`''.''     ;
                         <    :I..[Q)^"^^""",::,^^^,""""""""`^^"",,"""""^``^,:,",,,""""II    I
                         <        +!~_......'```'''.''''''',[}1!.'''''''```^^^^`'''''`'`.    ;
                         !        >!;><                     ...                              ;
                        .l        >!l>^        '>!,                     :;I!.       .!;:'    l
                        .l        ii<>         .I:`        '::;^        ;:Il        .;lI`    i
                        .l        :,I:                     ^>><:                             I
                        .l          .                        .                               ;
                        .!          '                        '                               ;
                        .!^^^^","^^^^^^^^^^^^^^^^",,"^^``````^^^^""^`````^`^^^^^""^`````````^I
                          ....''.......'..'...'''''''''''''.'''''``'''''''''''''``'''''''''''.

                 I[l  <~~:>i>>~+:":i!"l+il_l:-~~<>><i:i,~>l"liii!ili;llI.
                 '^`   .^'"'`',"   '' ','':".,II,;;:^`:.":,'::":,;";'",:
                 ,~; .i>!,IIII!;;^l^l_I"l::^l:`::;,l;:^!,:^,",I,'::",:^^:,,:;:`
                 :i:  ";!,,!llll:`!,i!!llI!"ll"!!<l>!_:>!>l;IIi<:<iii~I!!i?i+!,















```

*Figure from page 12 (2337x3305 px)*


---



4203-E P-223


#### SECTION 2 PROGRAM OPERATION

5-4. One Line Deletion



(1) This function deletes the edit line.



Press function key [F2] (LINE DELETE) to delete the edit Hne.



(2) Lines following the edit line shift up and the first line on the next page shifts to the current page



and displayed on the last line.



(3) The edit pointer shifts to the first character of the line next to the deleted line.



(4) One line deletion operation at the line which has more than 63 characters differs from ordinary



one line deletion processing. (See the figure.)



N101



N102



» &Y100



N103



>DL



ti le end



GOO



G01



xaoo



X250



2200



2150


#### LI NE LI NE CHAR. CHAR. LI NE ED IT

IN SERT DELETE INSERT DELETE DELETE ERASE OU IT



N101



» [f)103



N104



Press [F2] (UNE DELETE).



N117



GOO



G01



G01



xsoo



X300



X113



2200



2150



(5} The prompt ">DL" will be displayed on the command line.



F0.3



[EXTEND]



F0.3



(6) This function is effective for deleting an entire line in the stored program.


```text


                                                                                               '"^^`^" ,'^^"'
                                                                          '''.`'.'.   ''....'  I[-?_~+.<;?[];
                                                                          _}-><<<__!i^_~]~_??-]]:~-___?_~<+]:
           .^^^^^^^"""^````^^^^^^^^^```````''`'''''''````'''''''''''''''..''''..'..''...''''.''''`'.''`'.'''.
           .`^'":::""^``^^``^,,""""^^`^,:::,,:,""""",;;;:,,";;;;;;;;;;;:,,:;;;;;::::::;II;I::::,:;IIII;:,,,:'
           I_^_    :<>i>:I;!>^i<><i>!!;
           "l^I'   `IIll`;:;>`:li!iI!l:
                  `".  :"`.`.`'`.. `''^^`',`''^,`^``
                  li;  li~II<>i~>i:~~_-_<:~_;i~_;+!~
                      'l"",^"""^;""'"^`.l,;'"`;;,`:I",;l:`^^.,,",^',^.^",'^^'
                      '!l><!:<ii~>i,i<+I_;]:>l+-I,<?><!i+;l<,?_+_~:~-:_++:i~<
                  `;` ..'.. `'`..'. ''.  ''''.  '`'      .'  .   ..          ..      ..'    .
                  i?l "!i~?I!++>_<~-i_+:+-+I--li__~I-I<~~!__ii-_i~<-:~il_-;i-_>~-][ii?-{<l+;__lli<~__;~[]]:
                      `-i~:]~_-___~l<;<_<,__!>+~l                              '.'` .   . .  .  .  . .''"`
                      .`   ..^.'^.. '   . `'. .''
                  i}l '+~_:<-<;!>i~+,i_i]!I!;_i,~!~:<<~i>>+i^<l-i;lli"I>i;>;I<l^><><i!;!ll.
                  `^'  .'"'^"`"^^`^, "".,^'^.^:.`^".:";":";" :':,"^":.^;:`;"';;.;lIII;`;,:
                  ;~" `i;:"!:I'!Il!;;^"!:;;l;;.;I,;;';"^^;::l'::,':":;`l":':i^`I"",":",'"!i::^;,,"'^";",,`
                  :!, `>!>;<>>:_+~_i>,!?>i>~<<:il!-<;i_il-i<>;I+i,l!>>:<!>,i~:I!>i+<~<>Ii-~~>;i>>!,!i~l+~>
                      `<li"i-l!?<~~!l;~Ii>~<~l]! >-+_:+_l>]<!+l"
                         .:"""^''''''`",,"^^^`^"^'.^""``^`""`.^,::,""""""`"",""""""",:::,"""":^
                         ":       `!;I^         :<~"        :i!!'       .ii<:                :;
                         ^,       "~!~,         '":'        I_-+'       .;;I"                ,:
                         :;    '. ^<I<!`       .:"          "I!I.                            ,:
                         ::   ';^ "~;l~;       .!!^                      '..         ..      ,:
                         :,       ^>l~,         :~i`                    '<l-;        :~I!    :;
                         ";^^^",,"`'```^`^"""^``''''``^""^`^^````^"""^`````^`^""^````'`^^^^`'!;
                          ....'''''''''..'''''..''''.''```'lI''''`^^^`'''''''`^^^``````'`^^```
                                                           !l
                         ^'                                                                  `^
                         :`                                                                  :I
                         ,`                                                                  ,:
                         :`   I1>                                                            ,:
                         ^'  'il!<I[]~'' .''''   .'.'.   ''..'..''.....  ....   .'. .......  ,:
                         `.  :!;]+^:<l;i1;'"!l~+_;',:i<+],^>;.'`'``>I;!}I`"ll?<<l,:!^`^^'``  ,:
                         :"   l~}+l`,^_~}~;';`_[{~;^^i[+[<,;,;:',;.:^<<)+' :,]!i^ `I."^,","` I:
                         .I,`.^-~~_,,^?_li~:I'<_]+>"^l]i>~<":?]><_:"^_]<[:.:"_ll` ^:^--~_([!"l.
                           `,""^^^^,^^"^^^,,,:;,,":"^"^^^^^^`^^"^"`^^^'``,"`"^^`:;,:;^``".",^
                             '!I-<;l;:l<+_Ii^i:~<<:l"i!~+;>"!I~?+Ii'>;__!Il"i>~~;i^II<_-l<
                             ">;?i:;<!,>_}'<;_'~><'<ll;~]^ll+`~~?'~"+^_}>^?lIi~<'<l<`~_{.}.
                              ",`,;:..;:~[;"";!lIii"'li!:i!':il,,;^ ":^^":'.;:::;: ^:^"";"
                                         ^:`<<+_>-+<<_--l--~~>];
                                          ..        ..  .
                                                           ,.
                         .``````^^^''''`````^^``''''````^^`[;''''''''`^`''''''''``'''''''''``.
                         ;"'''''``",""`'''''^^``",,`````^^^",,,"`````""^^,""^``^^"^````````""!'
                         ;'       l<!>.         i~~'        >-_i        ^~<~^                I'
                         ;'   "l' ][!~^         >_l.                    ,i!_^        <>!I    I'
                         !`       <_i_^         ..          i+~i        ...'         .'`'    I'
                         l'       '`^`.                     ^;,^                             l'
                         I'         .                        .                               >`
                         I'       `""".         `^'         ^^`'                             !'
                         l.       :!:I          i<;         i;i!                             ;.
                         ;,""""""""",^^"""""":::```""^^^"",,"^``^^^^^^",,^^^^^^^^^,"```````^`l.
                                                           .            ..........''..........
                 '~>. ;~l::;:IIl:,:il"^I>;;;^!l;I;:;;^,":l:`",,,:,,::;,:.
                 '!l. ',I;!:;ll>"';Il''ii,Ii^i>~!<>>i,l:I!i"l!lIl>iilli~^
                 .;:  :l"^`^''"'^'^.'I:'"^` :` `"'`''. ` .'^^'.^.  ..". `^'`^''`''''`.
                 ^?+. :>~<:<li~>>;>l>~~~+<~I>~"<]>+i>?;_:<~<-+I+i>;ll]_;+->+_I~<<?<~<!























```

*Figure from page 13 (2346x3317 px)*


---



4203-E P-224



SECTION 2 PROGRAM OPERATION



5-5. One Character Insertion



(1) This function inserts a space before the edit pointer.



Press function key [F3I (CHAR. INSERTI to insert a space right before the edit pointer.



(2} Data following the edit pointer shifts to the right when a space has been inserted.



(3) One character insertion operation at the line which has more than 63 characters differs from



ordinary one character insertion processing. (See the figure.)



» N101 GOO Y200 2200



>IC



LINE LINE CHAR. CHAR. LINE EDIT



INSERT



DELETE INSERT DELETE DELETE ERASE QUIT [EXTEND)



(BJ@ @@@)@@)



Press [F3) (CHAR. INSERT).



>> N101 GOO x■aoo Y200 220



(4) The position of the edit pointer remains unchanged.



(5) The prompt ">IC" will be displayed on the command line.



(6) This function is effective for inserting a character (numeral).


```text


                                                                                               '"""^^" :'^^^.
                                                                          ''.'`'.'..  ''....'. !??]-+_._l??-"
                                                                         .?}<><_<[~>I,--?+_-]-[-,++<___~i~+?,
           '"""^``^^^^"""^""^``^^^^^^^^```^^^```````''''``'''''''''''''''''..'..'''`'. .''''.'`''`..`'''.`''.
           '^"^""""`^^^^,,""``''^"":""^```""":::::::,,":;;:,:,",:,::::;;;;:,",,;;;;;;;::::;III;I;,:,:;IIII:,'
           l<;]    I_>ii"<<!<l>i>i!`~li>!+i!!
           "I"l'   `;;II';:;>;i!Iil lI>>lliiI.
                  `".  ::^.^.''"''.^'''' . ..`'``^^,``',`..'"'.''``'
                  ;i;  I<+;!>l>_<!:<<_<_:>,]__>~:~_<!+;+~;i_-l<~~>-<.
                      '!"",`,,"^:^^':"`'!:;.;,"::: "::I:;I"'^."^^'`''``^`^'^`"^^`,^```,`.'`".''`^`.
                      `;!<il:<i><>I,<~~;+I_:~!I><>'!<~]+<il;_,>~-<;il>++~+;l?~!!+-~<+!?_;~+_;~~++]>.
                  `;` .".`.'`'.... .`. ..^ . ..   `.^    '.  . .  '
                  !_; ^~~[_l_<~_<!}!+?!~_]I<+_~]i;_~}-I+;++>I_}+;___-,<l]_]_+I~]>>??-!!+?-_?_~
                  ..   '          .     .        .     .
                  >}l ^<!~Ili-_~~_?"<>___~~"!++i~?~i^?!~+<l<+li-ii<,>_<"><i>;-+];_?l<<-<~~?<>:-[}_+l?i<i.
                      `>!_I<<!:i<!:~><i>~_:l~+>i><;I!i>i<<ii~`'<~~!I~<I~<!!i:''' .' . '.`'''..`''^`''``'
                      ."^,;!!!,;;;:I;Il!i<,;l!l:;l;>!;!!!!!l+,^i!il:l!,l-!liI^'''''```''......
                         .l.....''. ^^,"'.'.. `",``''......,l;,'' ....''`""`'``````^:::,`````,:
                         `;     ,;  !!!I      :__:         -t-i        ^<<_"        i++!     `;
                         ^l                                                                  ^;
                         'l""""":::"^"""^^^"::,"""""""":::"""^^^^^^^",,"^^^^^^^"""^^^^^^^^,::;"
                                                       ... !l .     ....      ............'''.
                         ..                                ;,
                         ;:                                                                  "I
                         ;"                                                                  "!
                         ;"                                                                  "I
                         ;"   .^:                                                            :l
                         :" .,l>_"^^,^^^^^^^:",""""",^^`^^":::"^^^^"^",^,"^"```^""^^`^^^"^`  ;l
                         ;"  'l;}- .!:I!|l 'I;_])l ,;!+}{, I:     .l:Il)i.`i:-i>I',~.  .     :l
                         ^l.  ;?}]];,"[-~<-:".+[[]+`'l}<+~>"^~?Ii~,;^]?][: !"[ii" `l^?<i~-~: l"
                          ^;:"^;I;:^:";Il;;""`:l!lI,,";,:";,"l>lI;,:^;lli:^;"i;"'.":,<!:i+~!;,
                            .',:",:;'';:::;,.";:;;l"`:::,;,'^;""";^.^:"`"I^'I"",;,'"I^^^;`.'
                             `>"?<^;il:<_]`>:+^?>~^<;!!-[,iI~"~?+`~`~"[}i"<;I!__,>;<"-]?^-
                             `>I<l;ll;Ii<]:i"~:<-<:i"l;!~"l,!,!!_^i.i"!<i:<;!!!i"<;>,>+?"?.
                              .^`^^`  ```'^.  ^`?i":;i<li<i,l>i<"i!!i+i^'^  ^^^^"` .^`^`"
                                                 ^^!<+~!!i<!>!i<Ii__<i!I
                                                           .
                                .. ...         ..        . _,..
                         ";""""^`^":,,^^""""""^"""^^^^^^^^"~:^``^"""""""""`^^^^^^^":"^^^^^^^^:.
                         ;"     :, .<!i,      !~~`        ^Iu)~<.      :<~~.       .>~;      :^
                         ;"     '. .[~'       '^^          `i;""       .",,         ,:`      ,^
                         ::.'..'.'```'.''.''''''.'...'.'''''    ....''''.  .''''''''.  ....'.;^
                  ":. ^I"^":,:I,:";;;:"",I:",:I;,",::,:,""::;,""^","``^"^`^```````^""^^``````^
                 '~+' ^i~>!<<~~<>"~;i~I!~_!>+<i+!^~-<_-ii;i!<<_>---;
                  ''  '`         . .'. ..    .          .       .   ..
                 '][` :~_<<_>+~-i"l~~^~]+i]!![??]?_-<!-l]+<l_~<<>_<+l--+.
                          .                   .                  .
                 '[}` I+>+l-<~_++;<!i)[~-~_li+,!<+_-_+ii;<~~~_~?>`~~!i+>~]"
                  .'     . ...... .....''.'. ' .'``''""''''^`^`^` ^^`'^`^"'

































```

*Figure from page 14 (2346x3317 px)*


---



4 2 0 3 - E P - 22 5



S E C T I O N 2 P R O G R A M O P E R A T I O N



5 - 6 . O n e C h a r a c t e r D e l e t i o n



( 1 ) T h i s f u n c t i o n d e l e t e s a c h a r a c t e r l o c a t e d b y t h e e d i t p o i n t e r .



P r e ss f u n c t i o n k e y [ F 4 ] ( C H A R . D E L E T E ) t o d e l e t e t h e c h a r a c t e r l o c a t e d b y t h e e d i t p o i n t e r .



( 2 ) W h e n t h e c h a r a c t e r i s d e l e t e d , c h a r a c t e r s f o l l o w i n g t h e d e l e t e d o n e s h i ft t o t h e l e f t .



( 3 )



O n e c h a r a c t e r d e l e t i o n o p e r a t i o n a t t h e l i n e w h i c h h a s m o r e t h a n 6 3 c h a r a c t e r s d i ff e r s f r o m



o r d i n a r y o n e c h a r a c t e r d e l e t i o n p r o c e ss i n g . ( S ee t h e fig u r e . )



>> N 1 0 1



& O



> DC



L I N E L I N E



I NS E R T D EL E TE



G OO



C HA R . C H AR .



Q9 8 00



I N S E R T D E L ET E D E L E T E


#### Y 2 00

L I N E



ERA S E



E D I T



Q U I T


#### Z2 0

[ E X T E N D ]



@ @J @J � (fil @ @J @


#### P r e ss [ F 4 ] ( C H A R . D E L E T E ) .

> > N 1 0 1 G OO 8 0 0



( 4 ) T h e p o s i t i o n o f t h e e d i t p o i n t e r r e m a i n s u n c h a n g e d .


#### Y 2 00

( 5 ) T h e p r o m p t " > D C " w i ll b e d i s p l a y e d o n t h e c o m m a n d l i n e .


#### Z 2 00


```text
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%B$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$@B@BBBBBBBBBBBBBBBBBBBBBBBBBBBBB%%%%%%%%%%BBBBBBBBBBB%%BBBBBBBBBBBBBBBB%%BBBBB@BBBBBBBBBB%%%%BBBBB$$$$$$$$$$$$
$$$$$$$$$$BoM*aaM*ohko#MMM#oooooooooaaoakakkkkkkkkkhaaooakhoooakkkahaoookaMMMMMMokhaao#oMaoooaao#oakkkhoooaM$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$@$@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@@@$$$$$$$$$$$$$@@@@@$$$$$$$$$$$@@@@$$$$$$$$$$$$@@@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$B8&&&&&&&888%BBBBBB%8888&&&&&%BBBBBBB%%%&&&&%%%%%BBBBB%88&&&&%%8%%%%B$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$@$h#M######MWW8%%%%%%&&&&W####M&%%%%%%%&WWM###WWWW&%%%%%&&M####WWWWWWWb8$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$@$k%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$h&$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$@$k%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$h&$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$@$a*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@8%WWWWWWWWWWWWWWWW&%%%&WWWWWWWM*Wk8$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$B%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%$BBB%%%%%%%%%%%B%%%BBBBB%%%%%%%%8%B$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@$MB$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@$#B$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$M$$$@$@@@@@@@@@@@@@@$$$$@@@@@@@@@@@@@@@@@@@@@@@@@@@@$$$@@@@$$$$$$$@$M@$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$M$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@$MB$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$M@$%8%&&&W&&&88888888BB%8888888888%8888888&8&&&&W&&&%%8&W&888888%B@$WB$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$M$@8W&M#M#owW&&&&&ak&%%&&&oM&&&&&&wW&&&&&#p&MMMM#bdM&&WM#da&W&&&8B@$WB$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$@$a%$$$$$$$$Bh$$$$$$W*$$$$$$WB$$$$$$p@$$$$$Bh$$$$$$W*$$$$$$*W$$$$$$$$@kB$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$@@8h#&888888&a%%%%%%M*%%%%%%*W%%%%%%o%B%%%%&o%%%%%8#*%%%%%%*M8888%%&#aW$@$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$8MM****#W&WWWWWW&&WWWWWW&WWWWWWW&%%&WWWW&WWWWW##WWWWWWW&&#***M#W&@$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$$@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@$B@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$wB$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$@$&#W&888&MMMMMMMMMMMMMMMM88MMMMMMMM0*MMMM#a*#MMMMMMMMMMMMMMM&8&MMMMMMoB$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$@$M%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#B$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$@$WB$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$WB$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$@$#&BBBBBBBBBBBBBBB%88%%BBBBBBBBBBBB%%%%888%BBBBBBBBBBB%8%BBBBBBBBBBBB#B$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$@$8MWWWWWWWW8%%%%%%W***MWWWWWWWW8%%&WWW#***W&%%%%%%%%%8#**WWWWWWW%%%%%&@$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@@@@$$$$$$$@@@@@@@@@@@@@@$$@@@@@@@@@@$$$$$$$$$@@@@@@@@@@@$$$$$@$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
```

*Figure from page 15 (1236x1747 px)*


---



5-7. Deletion



4203-E P-226



(1) Program data in a specified range is deleted.


#### SECTION 2 PROGRAM OPERATION

After specifying the number of lines to be deleted, press function key [F5] (DELETE). The specified



number of lines will be deleted including the edit line (»).



(2) The edit pointer is placed at the first character of the block which follows the final line of the



deleted blocks.



(3) When the number of the specified lines to be deleted is larger than the final block of the file, all



program data up to the end of the file is deleted and the line right after the final line of the file



becomes the edit line. In this case, the message ''file end" will appear.



(4) After program data has been deleted, the message "**RECORD DELETE" appears on the



command line. Here, "**" indicates the number of the deleted lines.



(5) Lines following the deleted range wlll shift up.



Operation:



[F5] (DELETE)-4 [WRITE]



Four lines preceding the edit line (edit line not included) are deleted.



[F5J (DELETE) [WRITE]



Only the edit line is deleted.


```text


                                                                                               ..''.'..^ ...
                                                                                               >?~_>-;"<:-??.
                                                                         ,{?+<_~~]I+"!-[_~-__?[+l---<--~<+_-.
           ````````^^^^^^^`'''''''''''''''''''...'''................     .`^``''``'^.'.`^`^`^^"`'"'`'`"`'^`"
           '^^^"",,""""""""^,:,,,;;;;;;;;;I;;::,:;;;;I;;;II;;;::;III;:;:::,:,,;IIII;Il;,,,",,:;;I;;;I;::,,,"
           ~::;    >>i>i~lII
           l,"^.   ;l>!iiill
                  ^`  '^    '`.^``.'...'...^`.'...   . . ... .
                 'i<" Iii~?<_!,_-]l!:i;-_+i+]_~;+>?]:_;~___-_i
                      ';;,``^`^"^`^.""`'`'^"``.^"^"^'^'`^'`^^``'' .'...'...'  '   `'' ''`..'''  '`
                      ;_+];+?~~<?<>_><~;!><-_~,~l+i~ii!i-I<?_-++i;<~__l<~>+?+l~__l]~}I?_[<]<~-<.l-_<>[_~_[~-^
                      :!li?_~`_l~i_~:+]l~+,?+<]~+!~i<i?~~i+_<:<-!+~~;!IlI       '.  ...  ..  .'   ...^'...''
                      .'                    .  .  .  .' ^` .' '` . '.' ..
                 `?_' :><l;~_!!<<<+>,+:<~<i~I!<i-<,-<>"~!~iii-;^~l_i:i<l<;:~i!<,><>;il:<!"+l!:!ll^;;I!;
                 .^`  :<___~<>_>>~~,."^,",",`",^,:',:,`,,I:;:!^^;^II";I:I",I:l;^;lI;lI";!"l;>:;Ii"l,;i!
                      ^;;llI,";:;II
                 .ll  ,l:^"':"''''^:""',"I,`^""^";^"^"^^'^``^''"^^"'`'''''''."`.''`''^..'''.'..'''..`.   .
                 `<~. l?><_I<<>l<<>~_<^+!++l>[+~~-+~l+<?li>;+!:]__]++I~:?>]-"-+-i;~]l~l]l<_<+i:_!__;<[I'{<
                      >ll_!~!"I]>~^!I;<:<<,!li,i!>!;l_l^i"_ii_<i^+!!;+>:~>~`!-~:>-<;l<+;-i_!~i>^<!_<l>}i.
                      +-~-+~~~I-~!i+}l!<_`,+:-i<,i+<!"]<i;~~+_+<~l>-iI~l+ili+><>~<+i'^:'"^:`^^,','^""`;,
                      '^``"'"".'`'^^^..^: .^."`,',;", ,;^',I;Ili>'.;I^I^: ^l, !iil!;
                 ^<<  ;~<I';,";;l;`Ili,":l^;I,;.,I:;;;" !,'`"^^^^": .`'"ll:",l;"."::^;:!:'^^^^^^".^^`:^.
                 `Il  l<_+l_><]>?i:l?->l>~li+~~I>?<--+!I+>ll<+_<_]-;:ili+_><i+_+:~+<>>;_!'__-+_+~:~i:__"
                      I!Illi+i!,!iI Ii<<I ;Il``<<~l~~~:+>!:!<i~<~^>l<_>,-~_++!;~~+l
                 ."^  .... . ...   .'   ..           ..  ..                      ..
                 ,[~  !!<[~!_<~_~<]!?_I~]~]?-l!}~]?;?[I~_-?:]i
                ^;^^^";^^         '              `.    .   .`.
                :<++i_~>l`
                      Ill":!!I;!Ii;`:"!l!II!:.
                      <I_!!>il!;"il^l,<il!;<!
                            .!:;,"l:;""::,::!::;!:`;ll,I:^";:l";,"`,:",":`:,,^`"".,,,""^'
                            .,:l,^lI!"!I!Ili>!_I!i">>!;i>Il+i>:!!i,i>I!i~!~_<ll~<,+-_~-~:
                     .]<]:>+-i!>!_I"<<<>l<i
                     .;';^:""",^.""':"^"`":.
                            '~>_!!+i,>+~li<;>l!___-<~
                             ``""'`^'""^'^,`^^`,,,:,,














































```

*Figure from page 16 (2330x3295 px)*


---



4203-E P-227



SECTION 2 PROGRAM OPERATION



N101 GOO X800 Z200



N102 X250



>> N103 @1 Z150



N104 X300



N105 GOO X310 Z200



N106 X200



N107 G01 Z100



To delete four blocks from N103 to N106



>DEL 4



LINE LINE CHAR. CHAR. LINE EDIT



IN SERT DELETE I NSERT DELETE DELETE ERASE QUIT



Press F5 (DELETE).



Key in "4" through the keyboard.



» N101



N102



IEl107



GOO



G01



Press the WRITE key.



X800 2200



X250



Z100



The command line of the screen will show the followfng message.



>DEL 4



4 RECORD DELETE



ti le end



beginning of file



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELETE IN SERT DELETE DELETE ERASE OU IT



F0.3



[EXTEND]



[EXTEND]


```text


                                                                                               .```''` ".''`.
                                                                              .       .        ;]--_<_ +:-->'
                                                                         .-[_<>~~]+!!"-_?~_---]],~]-___+_+~]"
           .'''''''''''''''......'''''''....'''''''''.....................``''.'``'`'...````'^^^.^''`'^`'``^.
           `,,,"":;;;;;;;;:,,,,",:;::::;:::,;I;;;:::;:,,:I;;:"""::,::::;I:,:::,:,,,:;;;;::;,,,,;lIIlIII;::,:'
                          ,^^^^^^^^l!iI"^^^^^^^^,><l"````^"",II;,^^^^^^^"i<>l^^^^^^^^^^",,^^^^^
                         .I       .?+?<         'i>;      ..:)){! .    ..!_<!........    ....'I
                         .;    ^^ ._>-+        .I<l'        '!li^        """^        ';^".    ;
                         .;    "" .+<+<        .!?i'        ',:,'        l:l;        `!I!'    ;
                         .;       ._i+i         'Il;        :[??;        :l:,                .l
                         .;       '-!]~         ';I"        :[-?I        ;!I:                .l
                         ';       .-i?<         `i!"        ':;I`        :,I;                .;
                         ':        ^^,.         'I:`                     ::l;                .;
                         ';          .                                                       .;
                         .;^^^^^,,,,,"^^^^^^^:;::,"^""^"":,"^"^^^^",,"",""""^^^^^^,,,,"^^^^^^";
                                 ...       . ^+;+-_+!+~:<<_-i<~_l+>]<~!-<]~.......'''''.......
                                                      .    `^ .    . .   .
                                                           li
                         ''                                '`                                .`
                         ,,                                                                  `!
                         ;,                                                                  `l
                         ;"                                                                  ^i
                         ;,  ':?):"< .   .'.      ...     .  ......      ..          .       `;
                         ;"  ,!<1_",i:,!]l^"!:ii+I`,;l<__"';;`^""""!;::_l^,<;<lI;":<,,^^^^^  `:
                         ::   I<)-:.l^_~[i"'I^_}(~:'`;[][i":,^".^".I"<i(_' i,}>i; `<.^`^`^`' ^;
                          ;,'.,-?_-,:^]-!i~;:.!]?>~^`:]><>~,,+[~__I,^_?~]I ;^]!l" `;,[-_+1{!^!'
                           `",""'``"""",,":,"^"`^^""^^^::::,^""^`,,:""```"`^",,,,"`^"`^`^'":".
                              !;_<I;;,i!_+;i^!;_+~Il`iI~~!!";l!_~:i'!l-->I!^il<<!i,,l<<<;i.
                             '~^[i;^<>!;+}`il-`?>-.~;i:+?::!_"i~}'~"+'?[-'?l!I~i^!~!`_<|.?"
                              ";",;I'.;::;;: ^;,;;I" :;,,,;.'l;_];I ";"::I,'IlllI;.^I"":I:
                                                           ^'  .:;~+-_+_]~]{<-<]+.
                                                           i;       ..''^^''``''`'
                                                ;+<,l^i:_!i~~l+>I>><iii.
                                                .'^.. . `'^I:'``'^"^^^:,^,.
                                                           <;         !;;:l
                                                    >>+<l-il+~i+li_;  l{ti!
                                                      .. ..       '.  -_!~i
                           ......... .       .....                    i~!~,
                         ,;^",:,,:,^^^""""""":::"``^"""""",,,^``^^^^^""":^''^""""",::::"^^^"^I"
                         ;"   .;` ^>;l.         l?+,        :<>!.       .>~+,                ;;
                         :"    '. ^<l~,         .``.        !-]+.        ``^.                :"
                         ;"       !1<<,         ";,.        ";;:        ."^,'                :,
                         ;"       l+l:.         :iI'                    '!l<,                :,
                         :"         .                                     .                  :,
                         ;"         '                                     .                  :,
                         ^:^^^^^^"::l!:,::::::::;;;::,",,""""::;,"":",,,",;::""""^"^"",::"^"^l^
                                    ,<<;<>>~+~!!+I!i>+I~<~<:~+;-~~l+~i+<<~<~I<+<+-<.  .......
                         `                                                 .     .           ..
                         l'   :__',I                                                         :^
                         l'   "ll.``.l:[<~[-`~_!i<I                                          :^
                         l.   : ::^i~,.;::;: :I;,"^                                          ,^
                         ;.  `]]_i?---^I: l`i,     ..    .. .......                          :^
                         ^  .,i+{l",!_I-]:";i<i<_:"l;><+>^^!"`","""i::!~:^:;liI!,^Il^^^``^`  :^
                         ;'  '!>)<"',:<>{;^^":_{1!``'<[]-:'I.^'.^^.l">_1! ^;<}i<' ::'^'``''. :`
                         `l^. !}]__^"I{iii~,".i]-+i''>[l<<!",}~>_-^:"??~]^',I-!l. "`l[-~](]I"l
                           ",,`'`'```''``^"""^,^``^"^^^"`^`"""`````^`"^",:"^^^^`",:,,^``"^::,
                             `!l+<l!`Il><<ll'il~>ll:^!>~>;!'!l><!!;'il<<l!""!i<<I!'lIiill;
                             ll;~i.lI?`<-] ~l_`-+!"_l"<<} >;+'-?_.-:<"-(l:+i^~>< -l-'-[].{
                             .ll;IlI."l;l!l:.;lIlll`'l:,:I;.:lIIlI" II;Ill``l:,,:l.;I;IlI;























```

*Figure from page 17 (2346x3317 px)*


---



4203-E P-228



SECTION 2 PROGRAM OPERATION



5-8. One Line Erasing



(1) This function erases program data in the edit line(>>). The blank line remains.



Press function key [F6] (LINE ERASE) to erase program data in the edit line. When data is erased,



a blank line will remain.



(2) The edit pointer is placed at the first character of the erased edit line.



(3) The prompt ">ER" will be displayed on the command line.



(4) One line deletion operation at the line which has more than 63 characters differs from ordinary



one line deletion processing. (See the figure.)



N101 GOO X800 2200



N102 X250



>> &2200 D



N103 G01 2150 F0.3



N104 X300



>ER



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELETE I NSERT DELETE DELETE ERASE OU IT [EXTEND]



@ @J @


# CED CJIJ

@J @J



N101



>> •



N103



N104



GOO



G01



X800



X300



Press [F6] (LINE ERASE)



2200



2150 F0.3



(5) This function is effective when replacing entire program data in a block with new program data.


```text


                                                                                              .,,""`" ,`^":`
                                                                         ....''...   ''.......:]]?]i+.~l__}i
                                                                         >{[~<++-?I~.+-]++]?_?};>~<__--~i<];
           ..'....'''''........''''''''...........'''...........'''......'`''..''.''...'''`'''`'`..`.''.'`''
          .",^;;;I;:::::,,"^""^":::::;I;:,,:,::::;I;I;:::;;IIIIII;I;:,,,:III;II;;:::,,,:;I;II;;I;:,,,,:;I;I^
          '!'>'   'lI":`:^:I";l,I;;,,'
          `_:?:   ^<+i-"<!I-II>!??~i{!
                  .   .'                  .  ... ... . '.   '...  .    ``. .. ...'. ...  ..
                 :<i. l~->!-~<-~-,~~--_~l_>+-~~i:_-];iI<~il_]>>~+:>I!l l<-li]-><I?~iI-~_?!+:
                      "^``'``'`^`''^``'::,'",,:^,:,"",".`''`''' `'`''`' ```.''^'..`"`^''.^,"''.``^.'.'''''^.
                      i!++_l+i~<~<!_+_!+!{!~i_[!-___-}+I_l+<_?+i?i_?~~iI]?-llI~~l~__i_<> ~]+-<I_?[>ii_<--__:
                      <:+?+i;+~~,~?l!-><?>`
                      ^. ''  . . .  .. .'
                 "-<  !~<;!<];i>~<->:<"++i>~:<>><!I+~>;<>~<<<+;l<l<<:~>~<>>;<_il!~:
                 ',^   .^`^""',^"":` "`",,"^.^'.`` `^^'`""^,^,.''.`".,`"::"^::^^^:^
                 `>l  i>l",;;l:l,",<+!`l!,l!^!ili!Il!,;:I>;`:;IIIl;:l;l!'
                 ^!;  `,l"I:;;I!`.";:" l:`:l`I!il!!lI^::,;I^;l,:;l:::,:!^
                 .::  ,:^^'""''",::``'"^,,;,,^.:',^.:"^.,:^:'^,,'`"^"^;,,,^!I';::,:;;:,`Ii;:",;":`",;::;".
                 "+~  l<i<Ii+Ii-<_~>!:~+_>-~+!l-;-_I<~_,_>i~;l_-Il>i<!i<_!,_i,ii+i<i+i!:~i~!!;ii>,!l<!~+<^
                      !<_:+ii^_~_-+~,i>i><<<<>? "___l!~~,+-<_!:
                         :^^""":::,,""^^""""""I:"""""^^"^":"^","""""^^^","",,^^"""^^""^":;;:,,
                         !.       ;;;:         'ii!        .!>!,        ">ii'                !
                         !        ii><          Il;        '_?]l        "III.                l
                         I        li>_^         '          'll>,                             l
                         ;    ,;. l_-i>        `i^                       .           .       i
                         I        Ii!>.        .~~;                     l>~+.       '<!>^    !
                         l        iii<.         .          '~++;                             ;
                         i'..    .^`^^........      ........^""` . ......    ..  ......     .l
                         ,:,,"^^^^^^``^^":,,,"^^"^^^^^^":,,l^``^^^^^",::,^^^^"^^^^,:::,^^^^^""
                                                           -
                         .                                 "                                 '
                         I.                                                                  l'
                         ;.                                                                  ;'
                         ;.                                                                  ;'
                         ;.   ,i:                                                            ;'
                         !. .:_1-:",I;:Il;:;:",:;^^:,:,:I::;^^":::;l""::"^:I;;,:"^::"^"^^"^  i`
                         i   `:l1; '!:;<|, ,:i]{{".;^_+{?' i.   ..'i"I_t, ":!{<>` ;:.  .     i`
                         :;   i}}}-"::[__+_""^]1][i"`][>~_l::{-_~_`,,{]-[`."I[!!. I";-++_{_"`!
                          ";,"^:::"`"`",:,;::";I;,^^`"::,:::,II;"^`^`;;;l^^^"I:"^'"^";:::Il;:.
                            ."!IIII!':!i!ii;^ii>i!!`:!I;!i!`!!i!;!"`!Ii~ii^:il!i!!'li<<<<,.
                             i,l~> i;_`]_+.~ii:+?"l!<`?+{ _:<.-}l`iIlI+1"l~<`+i< [;i"_}i"-
                             "!II!l!`;ll!i;;`!lIil!`,lI;l;l'llIl!l,'!;l};!`^II;;,l.;;:lll,
                                  .                                  ^,<;.'"^'`":'^"^^:^
                                                           .         ;l>+I!<~I!<?I<<<<?~.
                                                           i
                         ::,"^^"""``'`""^^^":,"^`''^""^^^^:["^`^^^^"""^^^""""""""""""^",::,"",
                         <'.      "";:.      . 'Il;         lIl"        ,!I;'            .   >
                         l    ..  -];,         .l!I        '!l!"        ,>!l.                !
                         l    ,;. fj                                                         ;
                         !                                                                   I
                         l        iii+'        '+~;                     l>>+.       .>!!^    !
                         l        !>><.         ..         'i>>;        . .'          ..     l
                         !'.....''",,,'...........''.......':::"'''...........'''............!
                         ^^^^^^^","^''^^^^^^^^^^^","^^^^^^^^````",,^^^^^^^^^^^","^^^^^^^^^^^^^

                 .I:  :I,^"""^:",`,`^l;";""`":",^`,";"","'"";,"'"""""""':::`,`^^;,":`^:l'^""^`,"^,",^`;::'
                 ,?~. ,i~iI<<!<i~,<;i~_<_i~:>>i+I;___+ii?lii+>i;~l--i<!,+_-Ii:il+<>_:i__,I<~!i~!??<~II__-;

























```

*Figure from page 18 (2329x3294 px)*


---



4203-E P-229



SECTION 2 PROGRAM OPERATION



Before executing operations explained in 5-9. "Find», press function key [F8] (EXTEND).



Press function key [FS] (EXTEND). The function names on the display screen will change as shown



below.



>ER



LINE LINE CHAR. CHAR. LINE EDIT



INSERT DELETE INSERT DELETE DaETE ERASE OU IT [EXTEND]



@J@]@ @J@ @J @J



=E WHEEL100. MIN



file end



>EX



Press [FS) (EXTEND).



PAGE INSERT



FIND CHANGE COPY MOVE EXTRACT MOOE MODE [EXTEND]


```text


                                                                                                `^^^'^ "''^^'
                                                                           .. '. .    ..       ^]?_]!~ ~!<_[i
                                                                          <1?~<+__?!_.++?+_??-?}I!_+--?_~+>?I
            ''````````````''''''''````'''''''''''''''''''''''...'.........'`'`.'`''``...'`'^'``^'`'.^'`'.'``'
           .,,:;;;;:;;;""^^^^^``^",,,,"``^,",,,,:,,,"^"^,;:;:,":,"",":"^^",:::::::;:"""^"`"::::,,"^"":,:I;;I"
                   ;   ~<i!l;"!Il:;>I;`!lI;iiII;^III!!Il;,;^I:l i!;;! :;;;,,;::I;;`;;:`>I<";llIil!lI'
                   '   I!lIl;,!l!Il!l+">>!I>i!ll,!<!>>l>l:l,!l>.;Ii>I`<i>i!:>!!iii"!<+;_;-l><iIii<<<:

                       _!<~<i~<>?+<l_->>?]+!]+__]-__i.+<>i~i>_+<ll~<>~>:!;~~il_<<_~I<ii<<I;~-I<<>l>!;<:<<lii,
                      .i!+>_"^^^^^^'^,,^'^"^,^'',^""" .`,`,"":,,`^::";:^"`^,,^:;;;!";:,;;^";:":;I:<;,!"l;;I;^
                       liI;i^
                                                                                             ..
                         l.                                                                  ;,
                         ;.                                                                  l:
                         l.                                                                  ;"
                         I    "+l                                                            ,^
                         ;  .,>}?,^^:^^:;"^,:;;:;,^,,;;;I"^;""""^^"l::::"^,;,:":,:II:,"^","  :^
                         !   ^I;|!.';,!]|,.":!-1{:."`~[1?` l.   ...i";+|, :!i{i<^.l!.. .     :^
                         ,;.  >[}]]","1~!-]""`?{][>`.~]!<~I""]++--^l^{[-{``Il}lI. ,",?-<-}-:'!.
                          ^::"^,"""`"^,""^"^"^:;;:""^,:;,"^"^",:""^:":,,:`^"";"^"^,^^:,":;l;;'
                             `l!<!;l':ll!i!;'!I!lI!^"!l!IIl'I!i>!!,'!IlI;!`"!!><il`IlIlIl".
                             l:>]< !l<'[-_ <!~"]_l,~i^+_{ <;]']}~.+:!,]|;;+>^->+ -;~'?]].[
                             ^!l;II!`:!l!!Il`!lI!ll""!lI!Il'!;:;!I;'!ll>!!,,l;:;;i`!l<?>ll
                                                                                     il
                                                                              I::;"Ill;I:ll;I^
                                                                              ;;!!:;i;!!;;l!!;

                         ^                                                                   ^'
                         ,   .-<lt][!I]~I)__                                                 ;^
                         ;   '+,~>i][:''.`''                                                 ;`
                         ;   .:..   .                                                        ;`
                         l  ."_1+``''`^^^`'``''''''''`^````''''''''''.   ....    .''...'''.  ;`
                         l  '^``.`",>^'''..;l`'. '`I:^'`'^"!.....'`i"<~+~^;l"~-_[~ii`''`^`'  ;`
                         l'  ';:_" .:^l;iil^" :i>: ^ '+li` lll!!I:"; >}{{ "Il11-!^I:`;,::;,' l'
                         'l,`":l]; .`:>i~_>^" l~i:."'"}<~" ;><i~_!:: <?i+.^"_-_>  ;":_+<-{-;::
                           `"^:^'";,^^:^^";"`;"^^:I":I`^`;"'`,^`,;"^;"`^,:"";:::!:^,;,,:"'""'
                             I:~->^<">,[-~,i;!l+_;!:l,-__"<"~;]]l;;:!i-[:>:>;?~+"+^>:_?i;i
                             i;~ii^~:~"-+<^<l!!>+:iI!,<<?^+:+,<_l:i;l!~1:>l+^+!!`?:<,<]<"<
                              ,^"":` ',^"",. ^""",^ .,^^^:' `,^^^,  """":" .:",^:' ^:"",:.











































```

*Figure from page 19 (2346x3317 px)*


---



4203-E P-230


#### SECTION 2 PROGRAM OPERATION

This function searches for a specified character-string. It is also possible to advance or return the edit



pointer by the specified number of lines.



(1) Search for Character-string



Example: To search "X300" in the following program



{a) The character-string specified by keying-in operation is searched for, starting from the



character which is next to the one located by the edit pointer.



(b) When the specified character-string has been found, the edit pointer stops at the first



character of the character-string.



(c) To specify a character-string, key in a character before and after it. Here, the character before



and after the character-string must be the same, and the following characters cannot be used.



+, -, ,, ;, :,



through 9, space, and characters used within the character-string



Example: /X300/



(d) The symbol"?" which specifies an arbitrary character can be used.



Example: /N?01/



This is the command to search for three-digit N codes whose lower two digits are "01 ".



Once a character-string has been specified, it is searched for each time function key



[F1] (FIND) and the WRITE key are pressed.



(e) The symbol



"L.J "



in character-strings represents one character other than numbers and a



decimal point.



Example: /X10



L.J /



With this command, character-strings such as X100, X10.5, and others are not



searched for.



(f) Pressing any key on the operation panel interrupts this function at the point the key has been



pressed.


```text


                                                                                               '^``'^'.".```
                                                                          ....'       .        >]_->]!^_;-]_'
                                                                         ^}]+<<__[;+"i__-+_[?-[_:_~-_-_+__-?.
           '````````````````''''''''''''...'''''''''''....................`''' ''..`.'..''`'''`'.`.'`'`''^``
           '^^`:;;;,,,,";;;::,,,";;;;;;:,:,:;;;;;;;;;;::;III;:::::::::::;I;III;:,,,,:::;IIIIII:,:::;;;;;;:::
           i:!>    ~>l;i
           !Ili.   ::ll!
                 >l:`^"":I,;`:;I::,;,^I"`"^::::i,;^":::,,;"'";:"^ `;^"':"^."^^"::"`,'^,"^"`^''^.^,`^^':^.`^:.
                 !!+il<i<!~~,>~+i><_>:~I;>l?~++_~+:l!+<~>~i`<~i>- "<I>:~<>,~i<~+~~,+,~_~++!_lI~`>?<i!:-_;+~?^
                ^+ii~}:"-;~_<,?i<i___,l~><+~^;<I<<-l
                       .        ..
                 .!~, ;[~_<?>:_;l~>-+-+?>;]i++<
                  ^,..''``..."' ...`^`^"^`"`'""'  ...
                  l-~]~_?]; '[iI[??>-:;]]?];:~I}-;_]?+[--+<_~]<_+i
                                                         .   `
                    i~"'+ll`>!ili!<l^>l!!";lill>ll;!";!Il;;,l.;II;!<;;"l^I;l;lllI;!,.!iliI;"i:;;:>I^
                    ;l^'<><I<<_ii~?>!>>!+><~~<l+~l;_>l__~<]i<:<~]i<+<+;~;~~_iIlil"!;`<~<i!+l!llI;<<"
                       ^ii~!<i<;`~li>'!;^~iI,!^!<,lI+,ii<~<~;>~,<<"i~+!~<!<~!
                    ^^..^`.. .'.     ^..' ' . ..   .                   .    .  ...   .     .'  '  .
                    ??""]><_II>~:?-?><__l!+_i~~??:>+_~[l~]<i]??l>-+~_i!-_I-_-!+_+-];!]~-_;}l]-!++_l
                       ^~i-~+_?i:~!?<:l<~<~~-~,>_<<+. `           .  .    .  ...  . ...'..'  .. ..
                       .'.^.''` .. .' . '.'`'' '``';
                    i~"'<,,~!I!-^I"!;>l>!i:^iI!l:`il:;I";,<!!!l<i^ll~ll""i;::-<I^> ,!lII.<l:,iI!;;ll^;lil;;
                    ,:'`<l<~??<i><I!++<+<_<:<+>+_,~~>>l>>i_~!~~~~::~<<<~i>~!<+~<:i`li<!<;<~!I>~+<~>_:;<<<~!
                       "<l!"i>>'II:"Ill;ll>`I>::+";;l>^>I,li`!<;l! <Ii:<<"!!II>!>i:>lll~!>l:">~i!i;i<"!~~~`
                       ''  .  .. ";ii::,l,,I ;:;:I ";,"^;:::;I::^`;,:",;;;"`l:'";;,"";:'":,"^
                       '"  .''..`,,;l:I!-:;!`+i<!>`li!:I!>i<><<iIl<<<;i<!il,~~:li~!~i~~"<~i<?.
                       l+i<ii<_:  >><>>^
                       `",;"::I` ."";::'
                    ^;.';^..'''^``',` `^^^.''`'",`'.`..`^``'' .`''''''.....'. ...'
                   .<[^'i+i:?il~~>.l';_!_<"~--<_]?il-:<+_~~~+l!<+>_+~_">?~:-+:+?]+'
                       :;^,,";;.  l:;:"'
                       ;>i+!~+_, '!!;!;^
                                 ';`` '`,^'```^^'``^`''```'^`^'^^'''.^'``"...`'..``...'.........' '. ...`''.
                                 '>i+:<!~+Ii<><l<_>!i!i<__i!;~!<->?~:+??i_l><]?iI?+>-~I~-_~"_-i!]+_~I+~:i<;`
                                 ':^`^.` "^""^,,`.,"`^`"^^`"^^^ '`^`,:,^ ^'`'^`^`^`^^"^.'`'".^^`':'`^"``'`'.
                                 "?<<>!+!_~_i+~?<:_~>[-<??l+~+>,~<_ii-+>"i;>I_+_<<~+!i_,<-~<:il_!i>i++~<;+-~
                                 I],>"_l__~,~~~l_+i;]-_!_>l+_:i_il_++<__i
                       '`        ..  ..                     .    ..   .
                   `-_':i<!;-!><<i`""`^>;i++i_~??;<__<[-:_[<<+++__,~~~,~i_<+_?!,_~_<I]~?;i<<~_+~i;->~!l
                    .. :_<<<+?l<>~<,'  . . '.'''' ''..:`.'"''``''`.''`.''^'^`^'.`'^`.`^"''^``^"`^'"^^``
                       ^:"^``:`;,,,.
                       ~_>~>~++' '-<_i`^:`
                       '`^^'"^^. ..  ..
                                 ,_<]^^l!,'!!<ii>l<I !i>!>!<>,i>ll!l.!l!>.I>'Iil~< :<Il;! Illl'iiIIl.;!l.;I!
                                 "~>_Ili<!!~!::,;";" :"l:I:II`I;,;~;.llI:.;i'","ll'"I";,l ;Il:'!;lIl.I!l':!l
                                 ^<l>Il!!;Ii"
                    ^I ,;""""^`'^' `'' .'."'.'^^^`,^`''`^^^'^^``''^'^,`'^.''^''.`'"'..'''.``.'.. '.'.'...
                    I+.Ii~~++i-I+><>--Ii~I_~!l]-<~[<>I~_+_~;>_+ii--ii[-I><>~_~~;}l__>~?_~l>-<!_-l;_?I+?-_,
                       >!<++~+l
                       '..'''..































```

*Figure from page 20 (2346x3317 px)*


---



4203-E P-231



SECTION 2 PROGRAM OPERATION



>> N101



N102



N103



N104



N105



N106



N107



file end



>EX



>F /X300/



[fJ>o



G01



GOO



G01



FIND CHANGE COPY



X800 Z200



X250



Z150 F0.3



X300



X310 Z200



X200



Z100


#### PAGE INSERT

MOVE EXTRACT MOOE MODE [EXTEND]



@J @J@@ @@J @J



Press [F1] (FIND).



Key in "/X300/' through the keyboard.



Press the WRITE key.



N101 GOO X800 Z200



N102 X250



N103 G01 Z150 F0.3



>> N104 1]1300



N105 GOO X310 Z200



N106 X200



N107 G01 Z100


```text


                                                                                                '^``.`.'^.`'.
                                                                              ..      ..       ._?_]!?^;~i]+;
                                                                          ;{-+i>+~[;+'<?[+_-}_-1!!-~-~-__+~+<
            ``````''''''```````'''''''`''...'''''''.......'''........     .```'.'`''`...'`'^```^.'`.^````'^'`
           .::::::,,,,,,:;:;;;;:","^^,:;;,,":;;;:"^",::,,:;;;,",;;;;;,,,,,^^"":;;;;;;;:,:,,:;;:;::::,;IIII;:"
                          `:",",:"^;III:,^^^^^",l~_!"^^^^^^"",:,:""""^^^^"!II,^^"":::"^^^^^^^";.
                          l"   `I` l_?-"        I?{i`       ._1{[....  . ^?+<: .......    ....!"
                          ;`       ;_<?:         ,,,         ;l!l         ^`".        ^^``    :`
                          :'       ;+>?,         :l;.        ^","        `;:>"        ;llI    :`
                          :'       I-<-"         :I;.        +][_        .;::'                :`
                          :'       l_>?:         :l;.        +]+_        '!!l`                ,'
                          ;'       l_~?"         II:         :lI;        ';"I`                ;'
                          l'       '",^          :;,                     `;;!^                I'
                          l'         '                                     .                  I`
                          :,^^^^^^"::;"^^^^^^",,"^^^^^^^,::^"^^":::,"^^^^^^,"""","^^^^^^",,""^l'
                                    .         ..        ....~............................'''..
                          .                                 i
                         ';   '"^:.",,                                                       `l
                         `!   ,;'i`ii!                                                       `l
                         `I   ^i>.                                                           ^!
                         `I   "{~,><+>"                                                      ^I
                         `I  ^Ii,I><]_:^^^^^;::,"^""l::^`^^:;^,""^`:"^;:::,I,:::;;";"::"",:. `:
                         'I   . ''  "^.''''.;. '`` .: .''' ,l.''..';`^-?1i l`<{[]_`l.. .     `;
                          ;". !I_}` ,">_?-}l: `_[<^ " {)-~ '>_~~[-i;' 1[[l ,:)_-^  l.+?~]{]!.l^
                           ",,^^''```"^^^^"""^`^''``"""""",:;"``^"^""";:"^`,";::"``,`:;,,,II;^
                              ^!;l;I;.:llll!"'l;I;;I.,lI;:l:.;ll;;l`'!llIlI."I:;;I:.;I::,I'
                              >"+<> ~I]'[-<.~!ll__^lI~'-_} +l~^}{l^iI;<}1"!i<`_>~.];l;}{l,~
                              ,ll<<:!'!;l!!I;^!!l>li^Il!!>II`>;l>il:^!!l>:i,lI!ll;>^!Ii<!ll
                              ',`><:^'.:""".   ....   ... . ' .....  ... .   '.'''   ...'.
                              :!!<;_lIl!!+~`               '~
                                               ;:^,^,IlI;^:I-";^;:":,,^,,^
                                               ;!;;^"!>i!`Il;i+,!iI><i;~~l
                                                           '+         .,'`l.
                                                    :!ll:!l;_>lIl,l;. ^>(<!'
                                                    `,;;":I^:::,:"ll. "~}>i'
                                                                      ^1>!~
                          ,:::,"^^^"","",:"^^^^^",,:,,"^^^^^^",,"^^^^^^":lI"^```````^"^`````'`'
                         .!........+~_<..'......"_->''......:{{}l.'......>]-+''''''''`''.'''''I
                         .;        +<~_          ^'.        `<<_"        ''''         .       ;
                         .;    '' .-<_~         `~i^       .":`'.        !!>>        `<!>`   .;
                         .;    :: ._<-~         .,,^       ^<|]_I        `"^`                .;
                         .;       ._<__         'i>:        :]__;        I~!l                 ;
                         .;       ._<__         '::^        ^!li^        "^^"                .I
                         .;        :::^         `il"                     I;i!                .;
                         'I          .                                                       .;
                         .I^"^",,^^^""^^^^","^^^^^^^^^":"^^^^^^^^""^``````^"^"^^^^^^^^^"""```";
                           .......... .................'.........''.........''''''''''''``''''



































```

*Figure from page 21 (2346x3317 px)*


---



4203-E P-232



SECTION 2 PROGRAM OPERATION



(2) Edit Line Shifting



Example: When the 4th block is specified in the following program



(a) This function shifts the edit line by a specified number of lines.



(b) The edit pointer is placed at the first character of that line.



(c) On the display screen, the display changes so that the edit line is located on the first line of the



screen.



{d) When the specified number is larger than the last line of the file, the edit pointer is placed in



the line next to the last line. In this case, two lines from the last line are displayed on the



screen, followed by the following message on the command line.



file end



(e) When a negative number is specified, the edit line shifts backward and the edit pointer is



placed at the first character of the specified line.



(f) When a negative number exceeding the first line of the file is specified, the edit pointer is



placed at the beginning of the file. The message "beginning of file" will be displayed on the



command line.



>> N101 GOO [3800 2200



N102 X250



N103 G01 2150 F0.3



N104 X300



N105 GOO X310 2200



N106 X200



N107 G01 Z100



>F 4



FINO



CHANGE



COPY



WVE



EXTRACT


# I ~: l: ~ l

[EXTEND}



~@J@J@@J@J@J@J



Press [F1) (FIND).



» [Mias



Key



N106



N107



in "4" through the keyboard.



GOO



G01



Press the WRITE key.



X310 2200



X200



2100


```text


                                                                                               ^^`^." ^^.``'
                                                                          . ... .    ..       `[]+]i}.>><?[i
                                                                         !)?~<_~_?:+.<+?~_][-[{l>-_]~-++~~?<
           ^^^^^^'`````^^^^``````^`````'''''''''........''''...........'.'`''..''''`...'''`'```'``.^''`''`''
          .::::::"`^","""","^^,'^",,";;:,",;;;;:,,,,,"",:;;;:::;IIIIIIIII;,,,,IIIII:::::;IIII:,:::I;I;;I;::"
                 '+<  ~>~i:;!l,]i_>I!
                 'l;. ,::^^^",`!;:,"<.
                      ~><+!>+>' ;-lii,~+!,]_:~~i_:!;!>>ii_<iI!,~>:<<~i>i!;;ilili>;
                      "^^,':""  ."'"".`"".,,'",::'"^,l::":I:'"',I^,;;;I,;l:;:~Ill,
                    ,: `I^`'^'`:"`''"",.^,' `^^'`'.`. . .. .".'.  ...   ''.
                   .<-.`i<<:~!i-~+:>_<_ii--;_-~l_~!>_;~l]-_<--[!<+~-?];l->?<?i
                    '  '^    '    ..             .  '
                   ^]~.,>-ii][l__++?~,_l]]-_-i~~<]-I[~-I~~?+]_[iI+l--?i?_>
                           .                                        .
                   `-+'I+ll__;-?-_]~;_~_--l,_~;<]--__:~~?~?--;~<;-~_l_+:~_];><!!il~i_-_i;_,<<i!>+>!i<,i!<<<
                    '' !<i>>i^.'^.'^.'''`''..'.''^``".''^':"^'^^.'^^.`^'^^^'`^^`"'"^,,,^`"'`^"'`,"^^,`"'"":
                       ^"`",`
                   '!i ;>l::`!;,,l:;Ii:I":,;I:I^,^;,,::^l::`;:,^:::,",'",,,^,;" I,^`"I^`^"",^'"'",^^"^^^
                   `ii i-i__Iii>![~~>_+<li+<+~+^il>-_-i:~~~:<>~;--!Ii~:<I~<<;<+"+<!I<_Ii<ii_i`~I~_-++!!<
                       lii:i<;I~<!;!^i~"~-~,iii "l,<il^~<>,.+<;;li<:!Ii:I+>"~~<I<>!l+<,-+?>_++~:<!l+~"
                       !~<~~i`!_[<+~_i<+:__l~_?>~~>>:+-~_--?lI_,[+!;><>>i>i~!_<i.........`.'^.. '...'.
                       ""'`^''.^``^`^'':.'^''^^^^^^l'^"",,ll`^"'""^`,"^"^:^,',",
                       <?>i+_i
                        ..  .
                   :]~ <?i_!`<,><~+_i~:<i>_~<'>:!~<i_~<>.~i;;+?;i<~,+>]-:<_~+><>!Il><I<<l:i]!i!<>+>,>`
                   ."` !~~<<>l~I-?!]~+;>+<~+~<+:++-~!I+<!>-<<<_!!":`,^":`,I;,,::"^,::^":,";l"l:;:l;'I'
                       :,l:I;`i',;`::;^:,l;!;>l.I`;;,^<l!;I!l`:Il
                    li ;l,,^." ,`^,:^"'"'^"^" `^`^`^:` '"`.:'"'^``."^,"';,'"'``^`,:^" ,^''`:^'`^`^`'`
                    >> >->_<I~;~-]+_<~;~<>~~~,-_<~-__i{<<+I_<_;i<!:~:!_;+?:>;>-_i_-++^~<i!+]<+<+i->`_"
                       i~<!+i,?,<<:i__~i~i_~I_>_<;_~^ >>_,li-+_??_^i--?<!l<_;+I-]:^-_l<<"?~~_?~~~;+!i?-"
                       i<+<~<_ii;i<; .    .'                 ...`.  .'^    ^    '  '  .. ..^.`"`'.`'.'`.
                       '^I:;l!lI,:;:^``^^"^`````````"""^``^"^''`^^"`''''''''^^^''``''`^^^''.'
                         !....ll..?__i.'''''.'.,-->'```''';_t[[l^^`'''''<]?-^^```''`'`^^^```"l
                        .!       ._~__          `'.        :?_-:        .`'.                .I
                         l       .~<_~         ^_i"         .''.        lI~<        `<!>'   'l
                        .;       .+<-i         .^^'        "?]-;        ```'           .    'l
                        .;        -i-_         `+~I        ,]+_;        >-~i                'I
                        .;       .]~]-         ."^.        ^~~~"        ^^^`                `i
                        .;        l!!"         ^<>"                     >i<i                `!
                        .;                                                                  ';
                        .I^^^",,"^^""^^^^^""^^^^^^^^^^""``^^````^""^`````""^`^"`'''''''`^^^'"I
                          ...''''.'.......''''''''''''`''':l'''''```'''''''''`^''''''''`^^^``.
                                                          :i
                        ';                                                                  '"
                        ';                                                                  `:
                        `I                                                                  `,
                        `I   .I.,.                                                          ^"
                        `;  "!-,~,"::,,^^^^,^^^^^^^,,,^^^^""^^^":,:"^"^^^^,",,^`^^"^^"""^^. ^,
                        ':  .     .;".     l'.  ...,.   ..;l .. .'I^^+]{I.l`+{1[?"I.. ..    ^,
                         I`  :I_]. ,`<+?-{I, `~-~^ " ][__ ^<?+-]_i:.')?{I ,;)-[,  ;.~~<<-_> l^
                         .::"^`",`'"^^""":^"``","``:`""""'^,""^;:^"`'l:;"',,i;:'.^,`II;;ii!;"
                            ':I:;;l^'lI;;;I'"lIl;l"'III;;l''I:;:I;'"!,:,I"';;;Ill``I",,l:..
                            ._']>,'>!!l][^!;-`-<-.-:!"[[I:!~:i?}'~"~^[[]'-:i:-+II>i"+~1'+^
                            .i;i~I;;,iIl+;i"i;!!~;>^i;li;l:I!ii_;<`>;i!~:<">lil"!IlIi!-,<`
                             `"^]:"' `^^^`.  ''`'`  .'...'  '`'.`   `...`  .`''''  ```'^
                             ii~i!<l!>l+_!                l:
                                               ^,^'^',`"^^>>`,^^^`^`^".
                                               ,><,I`l^i!i>>:~>I<~>i<>"..
                                                          l^         "^'",
                                                   I,:,"I,><;:!,,:`  !+[Il
                                                   :;!!,!l"ll:!:Ii;  !-1ii
                                                                     -[l+i
                        .^`````'`'..`^^''''''''''''``````````^`'````'";;,`'.''''''''``'''''''
                        :;''''^;^+}+>;'''''''''l~<:'`''''`':ill^`````''`!><;````````^^``````I^
                        :"    .".!{_}!         ^I;'        i}__.       .;I;^                ,"
                        :,       ,+i]I         :!,.        "lI:        .;"l"                :"
                        :,       ',^^          "l".                    .;:!"                :"
                        ,"        ..                                     .                  "^
                        ::''''''''^`.......''''.'.......''''.............`'.................;^
                        .^```````^"````````^,,^^^^^^^^^^",,"^^^^^^^^^,,"^^^^^^^^^":,^^^^^^^^,.












```

*Figure from page 22 (2346x3317 px)*


---



5-10. Change



4203-E P-233



SECTION 2 PROGRAM OPERATION



Example: To change "Z200" in N 105 block to "221 0" in the following program



(1) This function replaces a specified character-string with another character-string specified.



Press function key [F2] (CHANGE) to select this function.



(2) The edit pointer is placed at the first character of the character-string which has replaced the



previous character-string.



When the specified character-string is not found, the message "no character string" is displayed and



the edit pointer does not move.



(3} The same delimiter as explained in 5-9 is used.



(4) The symbol "?" is used in quite the same manner as in 5-9. "Find" operation.



(5) When program data contains several same character-strings, press function key IF2]



(CHANGE) and the WRITE key. The character-strings will be replaced one by one.



(6) Pressing any key on the operation panel interrupts this function at the point the key has been



pressed. In this case, character-strings are not replaced.



(7) The following option code can be used:



";A" When this option code is designated, global search and replace can be executed. The



character-strings are replaced at one time.


```text


                                                                                               '^""``^ ,'^^^.
                                                                          '...'...    '... ..  ![?]+~<.~I--]"
                                                                         .-[~>i~<[<!I:---<_??-{-;+~---_~i><?"
           '`````^^^^^^^````````````''''````````''''''''''''''...'''''....''''.'''''....''`'''`'.`.'`'''.''`.
           .`^^`^::,,""^^```,,::::::,,",:;;;;;;;,,":;;;;;;;;;:,,,;;;;;:::::,:;IIIII;::;::IIIII:,:,:IIIII;,::'
           i<^!~^  ;<<!>i!!l
           :l',l"  ^;,!>I_~!
                  ^<:;::;!"  l!^llI:;l`;iiii":,:l:!>"!;,l`;^"il:II`:^::^:::",;,^`,"^"","
                  'lI>ll><I  "!"lI>;_+',>>ii.I;,l:><:<i!<"i,`<<;i;^i:l<;I>i>~<<+!~!-<<il
                  ..   '   '                     .
                  !~; 'i~]I>><~_~~:-]-?~_~:~I?-~~?-~;+~]+-~?_:-_~+>l-]!;->_[+~"~>-~_~[_;_~+~>l_~_~}+_;
                      ."'``."'''"'''"''';""'^,^^"^""^''''`^'''^`'`:.'`'.`.'.'' '.`'`'`'.`''^:'"`^`'^^'
                      ">>__>l-+i]+<;__+I-<};_<<+_]-[+;~l!]??_>~__;~<~-]_!.
                  .'   '     .
                  ~}: '~<~,>-<l~<~--,!l+_~>+>l[!__I_+-lii?<-+?_^_<?->I-<_~+++I!_<~-l~[_~>:<-!"___+>_~i[-:
                  ..  ^<<_!<!<;<~<>~<?~;++<~!.'..'..''.'.`'`''' '.''''''^`^``.'`'':^^`^^'.^,^.":",","'",`
                      ^:,,`",:."`,^:::".:"`;;
                      "-~<>,i>>:~ii!_i>;;l>Ii>-l,_<!<i~l>~~+il>>,->li~~>i~>i,i!:~>>!~i~l;_<!>II!l<!<<!!iiili^
                      ,->I<<-!~>?-_!l?<<II~>!<~!i!^`l;,^":"":"":`":"";;::li:.",^::;,l:I,"l;,<^";:;l!!>lI;!:l`
                      ';;';II:!I;I!^^lIi"'I:'::;l^
                  :!' 'I^^.^`"^.`","""^ `" ^^^"`'^"^"';^:^^.^^^^
                  !~^ 'll>,~<!~;I_+!>~_,i_:~~_+~l+<:>,~!~I<:+~~i
                  '^  '"'.   '`.' `'      '     ' ''       .    .. . ..'.' '^' ''     .
                 .>-^ `!i+:-_~]+<^l"l_:+--~l!I{-}i+]-I--~-li+->>_l:]IIl+i?,"~~~-">+-+??<<:
                  ..  ..'             .       .                                   ..           .
                 .-[" :[_<~II~!]-~<l![-?;i><?_i<"~_>+><,~_<?II<__~<_~,!+!<_?`l<<<>:+!!~~>I;~_,i<[~
                      ,_<+-]?_][;~+~l-~l<]]-~]!~~+"`]<~,~+~<~~+<;<+~<<iI~?<-il+~<-i<_!>><I~l!>~I^"
                      .^''''''"`.^"`.`".'^.`.' `,:. '`".^`;^:"," "^""i"':"."".;;"I:;;',":'l,`,::
                  ~_' :>Il!I:I"Il:^ll"`l'i!:`!I:,lIl^";I:l`;;;,":I:`!"":"::l,, ,";:^.:,:",,"^,,`,::^,:::^
                  l!' ,!>~_~!];_>+<+~!!+I!!+l[+<<_>>!_-<>>;~~~i<++~I~ii!~!!<iI^<I!i!I<iil;i>:<+i,i~;l<~<:
                      :!l!!i>! :::+!:,<>+"^i!<>+i~l:?>!~-"><<"><"!-<~<<~I
                  ^,. `,' '''.`'.   '` . ..'.          '.
                 '><^ ^<>>l<ii~<<?,~[-<l"<>?_:_[!I-II+?_<
                      '.:` ;;,^" ;:".'^,^^..'^;''^ "^^```^"^^ '^^`^'.``''" .'''.''`''. ... `. .... ...  '"..
                      'l~^ ~+>_~^~<~^i?_<<^;<>{l,+'-++-}>_+_<.?_+~]:l?_<i?'>~~!"-?~-~~`~]>^_?^<_++>--~, "<~?
                      I+<?~~~?I;[<i_["+<l,?+_-i_>:],<i~I+<?:
                        .. ...  .. `' '.. .'.''...'.'.' ..`.













































```

*Figure from page 23 (2346x3317 px)*


---



» N101



N102



N103



M104



N105



N106



>C /210/200/



file end



file start



>C /2200/2210/



G01



GOO



xaoo



X250



X300



X310



X200



4203-E P-234



SECTION 2 PROGRAM OPERATION



2250



Z150 F0.300



2200



FIND



CHANGE



COPY



~VE



EXIBACT


# I :~ I

~~~



[EXTEND]



@ @J@@ @J CED@ @J



\ Press [F2] (CHANGE).



Key in "/Z200/2210i through the keyboard .



Press the WRITE key.



N101 GOO X800 2250



N102 X250



N103 G01 2150 F0.300



N104 X300



>> N105 GOO X310



l}r.210



N106 X200


```text


                                                                                               `^^^'^.'".^`'
                                                                          .  .. ..   .'.       -]_[!?"I<!-]~
                                                                         ,{]_i<~~]l~`<+[_+]]-_}>;-~_<_?<~<-_
           ``````````````''''``````''''''''''''.''''''''''''''.'.''''....'```'.''''`'. .''`'`'`''`.`''`''^'`
           ,,,,,:::::::::",,,:;:;;:"""""":;;;;:"^":;;;;;;:;;:,"":;;;;;,::"^^",;;;;;;;;:,",:;;;;I;:::::;II;;:
                         `:^^^";:"IlIl"^^^^^,"^;~<!;,,,,,,,,II;;^^^"""``^lI;"````^""""^^^^^^":
                         ;,   ';^ I-~-"        ;_?>^        +1{['       '~<~,     ...      ..;^
                         :"       :+!];         ":"         :!lI         ,",'        ":`:,'  ,^
                         ,`       :-i-!         :!:         ^","        'lI<"        I>;~~"  :^
                         :`       :?<?l         :lI'        +]--'       .:::`                :^
                         :`       l}_{;         ;il'        <]_-.       'iii"                "`
                         :`       `:,:`                     "lI;                             :`
                         :`         .                                                        ;`
                         ",`^^^^`"",:"^``````""""^^^^^^^^^":::"^^^^^^^",,,"^^^^^^^^^"""``````l'
                          ....................'''.........'~"'.''''''''```''''''''''```'''''''
                                                           <'
                        .:       ''. ''.                                                    ';
                        ';   "-,">i+i_-_`                                                   ^i
                        ';   :<"_^<-?'                                                      ';
                        ';   ^>:~I_?-ii'`'                                                  '"
                        ';  ';]II][{}+{+-?"",""^`^""^`^`^``^``^^^```'.. .'``^.   '^'^^^^^`. ^;
                        ';  ..    .:;.     i,`.  '^i'    ',l     .lI`+_[>'i"I{]][:l'..''    `l
                        .l.  :I<?` ""l<<~+:; .!~<` , >]>+ 'ii!!>!;I^ [[{> I^-[1<" " lI;I>!, ":
                         `;"`,"l<`.",I!i!>,,^`l!;^.".!+l>.'!<l;ii",^.-<>;.;,?i<" .:'i<!>--i:I.
                           `^^l;::lI^"I,,"I,^I:";ll`";^""!:',l:""I^`;"""I!",:^";l,`,:::,:`^`
                             IIl?~'i,~^__+^>;i;_-lll!,+~[^~,+^?[i">"iI]}lIll:?++^+"i:][<:i
                             l!!!>,>:>:<__,>:>I>+;lIl,>!-`<,+">~<,>">I>-Ili!;_!i^_,i,>-<,+
                              ^"^^"`  ,^[i^'^,;::!;."l:I:l:.."^^^"  ^"`.`"  ,^"",' '"`^",
                                         :^:+_]+i<?>+~<--?]i
                                          .                ^
                                                           _
                                            !l,,""!!!;I!:I:_I::I,ll";II:::,
                                            ;!;,^^IllIl!,l`"IIl~:li:l><><i:
                                                           +         .I. :.
                                                   :!!i;l!:_<~<<;i!' ^<(?l^
                                                   '`,:"^,`"":":^;l' ^-?~!`
                                                                     '{<i_.
                         ,",,,"^^^:,:,^^^",,"^^^::,^^,::"^^^,"""^^,,,"^,::,,^^"""""^^^^^^^^^""
                         i ....   ++_>.  ..... ^+_<........^[}}i...''...l_-_`.'''''.. .. ...'i
                         !        ~++-.        ."`'        'i<~:        '^'`         ^''`'   >
                         !        +~<_.        '<l,         ^^^.        :;!<.       .>ii-~.  +
                         !    `^  +<<_         .,,"        `?]]l       ^Ii`^                 i
                         !    ":  _<_[         'i>I        `]-+l       ^~[I!.                l
                         ~        "":I                     'li!"                             !
                         >                                   .                               !
                         l^^^^^^^^":,^`````````""^^^^^^^^^^^,:^^```````^""^``````````^^^```'`!
                          ........'''..........'''''''''''''`'''''''''''^`'''''''''''```'''''.



































```

*Figure from page 24 (2346x3317 px)*


---



5-11. Copy, Move, and Extract



4203-E P-235



SECTION 2 PROGRAM OPERATION



These functions are used 10 transfer a group of commands from one program to another or to insert the



same group of commands into several different positions of a program.


#### N101


#### N102

-~---~---·-·-·-·-·-



i N103 i



j \ •



, N121 . .



-·-·-·-·-·-·-·-·-·-



N122



N123



N215



N216



N103



, N121



. .



-----~-·-·---~---·-


#### N217


#### N218

Extract buffer



r·-·-·-·-·-·-·-·-·-·-·-·-·-·,

• N103



To other areas



\ Stored



---·-·-·-·-·-·-·-·-·-·~



Fig. 2-1 Copy, Move, and Extract Functions



Operation sequence:



(1) Save the group of commands into the extract buffer using the COPY of MOVE command.



(2) The EXTRACT command will insert the commands saved in the extract buffer into the specified



sequence.


```text


                                                                                               .```''^ ".''`
                                                                              .       .        :]-?+<- _:?][,
                                                                         ._1->+~>]_ii^--?~_-?-][;~]-?-+___~]:
           '^```'''''''``'``''''.''''''''''.''..................        ..'^`'..'''''..'````'^^^'^''^'``'``^.
           ',:,",,"^^^",,;,"^^"`,:,,,:,,,,,^""IIIIIIIII;:::IIII:::::,,,:::;III;:,,:::III;;;::::,;IIlIII;:::,'
           ;i'I;   :>lII; i~l;:l `!;l:ii;!:l:;
           :>^;;`  "!!+<-'l~!il+`,]!<:i~><i?>l
                 ;!:::`"`:^"^`" ,"..""^^^.'`^^:;"'"',^^"'^:`"^"^""","^;^,'`"^'`^``^^"'^''^`^,``.`'^.``'`^`^`.
                 :!+_-Il<ii>>>~;~<!!__+ii!l<+<~<i"~i]<~+:i!;~ii!<-i~~l~i>:li<l~<i]~-+:<!!~!+<~<^+:+ll<+_>!~_;
                 i~iii;?l>_II<;~>i><_>_-:>_>"~i>~i-;][_>~~il>~--<!<,~iil~i<->~<'
                      ..  .                       .   . . .'......... .''.`^.'..
                            ^"``"""""""^^"""""""".
                            ?,''``'.'"'```^^^^^^<I
                            +'    "~I<I         il
                            >'    I1+1[         i;
                            <.",^`;<!+~"^^^^^"^ l:
                            ~ I^  ;[~}['..   ^I i:
                            ? ;'    :l.    ' ': >:
                            ~ I`  ,_>_I   .;;!i`>^
                            ~ ","^;>!~!^^^^`^;;:]!"^. ,lII^:",I,;,
                            ?     !{~)}         i"^:II~___"l:;>!i;
                            _     I-i?<         >`   .'^,,,'    .^,,,,""","^^`'``'''`""""""""^^
                            <        '          <`       .^:;I;"?"'''^^^``-{{[}+__}{-"^^^^^^,"<l
                            -''''''''"'.......'.-'           .`,]I,^I^'.,:i~<!>I:!!!!^^``^^"  l;
                            ;;;::::::;:,,,,,,,,;;               ~.`,~I;l+]~{>             `l  I:
                                                                -   ; 'i` !'     '+l;I!'  ':  !;
                                                                +   ;     "'     '~<!<~'  `;  !:
                                                                < '"-;I"-?<-,             `I  l"
                           ^~:::::::::::"^^,:::;!            .`,};;"!^.!<,"^''```^^```^^``;;  >,
                           :<     '`^".        '_        .^:II:"+:",,"_-,,,:;:::::::;:::::;"""~^
                           ,!     ]1+]!        'i    '";iI;^'    .'.'~l ...'''''''''''''''''''.
                           I< ''''<}~?!.'..'   '<^:;;:"^]---?l     .<,
                           l< i`^^-~i]I`^``^I?;!],^.              ^~^
                           ;l.I   ;:+i^     ;?'^>                ,<'
                           ;I';   l,>;       : `>               Ii l[]_-+'
                           ll.i`^^+<~+,````^^! ^<              il  .'`'^'
                           l! '.'`]{<<:'''.''' ">            .<;
                           ;;    .[1~],        "!           '~,
                           lI     '^^"'        "!          ;_
                           >l       '          ^;        :~~~]>i^~>><'
                           ;>::::;;:;:,,,;:,,::l,        .:`,!;I`iI!!'
                                 ..      ...`  .
                                           :-+!,~,^"+~_~,_{~<+^!_+>_+-<_~i-<+>__<>!
                                             ^^..   .`^"'.'''`.'``''``'^^' `^^`^```
                ':^^^^;^"'^^^'`^```
                ^>><><-i<"<+++++i<>.
                  ..  .'    '      . '. .......' ... `    .  ..  `        .  ...''. ..... '
                 ^>~^ !?-~<l_+:}~i-~I-I<<<~~?_~}li--:?~l>+?~?+!-<{]!I+]~?!?+l>--]iI;~!)?>~]:<~i+~++__.
                  ..  .'  .. '`` .''                                    '                    .    .
                 `?]` ,><i>~~>>-?+>:l<+<~+_>+;-]li+-->++~:><><>~<i_;>?~~+ii,__!l+_~+~l<<-_i:~_!l+~,_~~i_-~i
                  ..  ;+~~i+i!>' .  ... ..'.. '. .'`'...'.''.'.`''`.'^`'`.'.'`''^`'^`.`^'``.`^^'`"'::"^`""`
                      ^;:I:;":;.






























```

*Figure from page 25 (2346x3317 px)*


---



4203-E P-236



SECTION 2 PROGRAM OPERATION



5-11-1. Copy



This function transfers specified program data to the extract buffer.



Press function key [F3] (COPY} after the range (in terms of lines) of program data to be duplicated has



been specified.



Example: To copy blocks from "N103" to "N105" in the following program



(1) Program data in the specified range which starts from the edit line(>>) is transferred to the



extract buffer.



{2) The edit pointer is placed at the first character of the line that is preceded by the last line of the



specified range.



(3) Program data previously registered in the extract buffer is erased.



(4) When the specified number is larger than the last line of the file, program data up to the last line



is transferred.



(5) When a negative number is specified, program data in the blocks preceding the edit line (edit



line not included) is transferred.



When a negative number exceeding the first line of the file is specified, program data up to



the first line of the file is transferred.



(6) Pressing the WRITE key without entering the number of lines causes program data in the edit



line to be transferred.



{7) When an attempt has been made to transfer program data which is larger than the extract



buffer, the message "extract buffer overflow" will appear on the display screen and copy



operation is not executed.


```text


                                                                                               .'``'`` ".''`
                                                                              .       .        !?-?~-+ _;]][^
                                                                         '[1+<<_<}i>I,-]_<_-__[]I__[--_~<~~],
           '^`^``''`````````'''''''''''.....''''''''......................``''.'`''`'..'`'``'`^^'^'`^'^`'``^.
           `,,":",,"^^",;;;;,,,"":;;;;;,,,,,;;;;;;;;::::III;::::::::;;IIII;,",;IIIIII;:::;;;I;,:;::;;lIIlI;:.
           !l"!`:  ;>l!I
           ,:`"'^. ':IlI
                 ~~<l!>!>?<>"i~>i_<ill~>i<-<<;<!>>><!"_~>IiI!~i,i>>i!I!!l<!^
                 ``^^';^",,^ ^,^^"""`"l::,:;:":^;!::``;;:^""`::'I:";:""I"";'
                .<l<<<^ilI!!i,!+~^}<[!!~i<>ll^_]<"!>i`><!_I:+"i<;!>^!I!I!iI^~;>!>>i>l"<~_;i!I~I:<l<<l~<i;l!i`
                '>!~~;!~~i__<>^":`,.:""^`^''^';,:'^":.::;i"":`,:^,;^:'"":;:`:^I"li:I"^Ill,:;"l,"lllII!!l""l!`
                 ;;:, lllII;II
                ._!i>l!>;  ii`I!il,~>!<!:~Ii;"-il~~"!;"~!!~<^l,!iI;!lIl;;I^II;;I!I`
                 :,;I,l::  `,`,:II`;;:;;^::;" ;,"lI I; ;::!I I":ll^!;liI;~:!I!<!<l`
                  '`  ."''`'.' '.'.. '.      ,.    .    .         '                         .       .
                 .i>: :ii_[~?i,--[<>!<+~;_+->[]_Ii?~[?,??~+il[]<_;<>~iI~-;___!?-<l!l!!~!_?<?]+<++l_,_++
                      ,<-?__i<<_]~`                 '                           ... . .  ......'. .. .'
                      .`..'' .'..'
                  >]" '!i;"l~!:!!l~<,<:i~<!<l;~I_i:+i<,!!>!>!<!^iI>i;;!!,+l>,i"Illlli!l,!,;>I^!lI:lI^,l;!;.
                  ,;' ^i<<i?~>!><!<~`:"I:;:;""I^:;^::I^::!;!;l;`I^:I:";l"II!^l,!;ll!lil"il,!i^<<l"li,;;:!i.
                      "_!!!!!!^:!;~i.
                  ";. `"'..''..^``  ````''"`.`''`^'''^`'``'.''`.''`.`"'........'
                  <-^ ;!!--~+!;---i<<<>ii<_-,~--+?~<->iIl<~:_-_+_>~~~}+^+;<i---?"
                  ..  .'`.' ..      '      .   .       .                    .
                 .<]" ;]+<-,i+i:?<-~]-_!i~<~_];l<>]~[?I-~-!>-_;_]<i-+!i~!+_I?-"i+<-+--ll}[-:<+l~;?+I!-+I_>~
                      l<l+_<+_~>~-,      .      . .'^.   .   . .'. ....   ' .'.^''"``'..```'^".`.'`''^`.`'`
                      .'.'''``' ''
                 .++` :_<li^;^;lIlil!";:I!!i";;,!l!!+!i^:i;l!!i::<i>"I,~l:;>Il!:"lI;IIi;;^l;,,;>,l::`I:i,
                 .;;' ;+>!>I<li~]<-i-;!!>>~+i>i!-+l;I!l^l!:<!!!,:i><,;"!l;:i!!iI:i!!ii<l_;Iilli~;iii"~i~;
                      ":l"^i;:IIl:~!<,!,Iii;~~;li!
                      :>!;l`:^,:;Il:;`,,:;;:'^:",:;lI:"I:,lII,:;:';;l;^Il^^"^,,,,I,,'`,^^^^,^`:,,''^`".
                      ^l:ll^l,;l_<iI!`:l;l!i`:il!!!!l+Ilill!~II><"<I~+l!+l:iI-~~>>+~,!+!?~i<lI?_-;i_:~"
                      !>l:~!l,I!,,l!~!;~l`I"l!II>;;;l,
                      ^",',"".^:^,^^::^,I.,`,I,:I;";I"
                 .~~. II,I:l::";;'lliI,i^l::',I;,",^::l:,:";l:^,^,;:;`,:":::`^,^","'"""""""',::^^^^:^.^":
                 .>>' ll<<_<>]Ii+Ii+~>:~Ii<<">ilii!;<!_!:<~I><,!!I><~^iI;!~~:l_>>+<,<i<[i_i,<_+<I!I~~,<~-.
                      ,!i"<:l_,l>~i~_l>~!
                  `^  '''       '    ..  ..  ...  . . ..   .
                 `<~` i]>~+:_+^?}~~_?;!+],>_+i^>>++I!iI~+>+_~:<!<-!-<">[-i:__~~,>;l_<-<:i!_:>~i,<<i~~<
                      !!~?<'I~i"l~>>+>+!"ii~i~~I~>[+;Ii<+[~<~"~_<<-~<>_I!+;-il!_<+++l+i!>~i"<><;>>>!^'
                      l_~~<+i<lll!~_i_]<:<-<>:"',"^:'^,:,",:" ,:^^i;::I'":^::^";Il;!`,:,;l^`I::^:l!:
                      ,>!l;>I;`;:^ll"ll!llil;








































```

*Figure from page 26 (2346x3317 px)*


---



N101



N102



» N103



M104



N105



N106



N107



GOO XB00



X250



G01



X300



GOO X310



X200



G01



4203-E P-237



SECTION 2 PROGRAM OPERATION



Z200



~50 F0.300



Z200



Z170



Move the symbol "»" to N103 using the cursor control keys.



>CO 3



FIND CHANGE



N101



N102



N103



N104



N105



>> ~06



N107



COPY



PAGE


#### WVE EXTRACT MODE

Press [F3] (COPY).



Key in "3" through the keyboard.



Press the WRITE key.



GOO X800 Z200



X250



G01 Z150



X300



GOO X310 Z210



X200



G01 Z170



INSERT



MODE [EXTEND]



F0.300


```text


                                                                                               .^^^`'^ ,''`^'
                                                                          ........    '.       I[--_<+ _;+?<^
                                                                          -}_><~>]_!i"?-?<_]-_??"<_~__-+<+~];
           '^^`'````````````'''''`````'''''''''''``''...''''.'''.......'''`^''..'''``...'''`''``'`'.^'``'```'
           ^::,",,,,::::::::,,,,,;;:::,,::;;;;;;;::::,",;;;::,,",,,::,:;I;::":,,:;;;;;;,,,,:;;;II::;:::;I;;;`
                          ;"^^^^^`^!!!:^^^^^^",,;>>!^^^^^",,"II;,^^^^^^^^:!!;`````^"""^^^^^^^:"
                         .!        <~+l         `~~l        ^][]I        ;~_~.     ...       'I
                          l        ii+~                     '><+,        `.           .       ;
                          l     I;.~>+<         "?~;                    ^1}+~        ^~l<?<  .;
                         .!       .?ii>.                    "+_?:        .              ..   .;
                         .I        <>~>         "__l        ^+~<:        i_~<                .l
                         .;        <!<<                     "?-?;        .'..                .;
                         .;       .~>_i         `<i,        .^""'        !;;I                .;
                         .;        `"".         .:"'                     :",,                .;
                         .;         .                                      .                  ;
                          ;^^^`^"""",^^^^^^^^,,,^^^^^^^^","^^^^^^^^^^^"""^^"````^""^````````^:I
                           ..................''''''..'.''`':!'''''''''```'''''''````''''''''`^.
                                                           ,!
                                      .?+ii!_I!<<~>";;"<;<i>!l+<<!~ll<>~l;i>>l!~<i.
                                       .....'.'`.'' .. '...""'^'"''''^`^''`'`''^"^
                                                           li
                         '`                                ":                                 '
                         :!                                                                  `l
                         ,l                                                                  'I
                         ":                                                                  `l
                         ;I  .:<~`>.                                                         ^i
                         Il  ,Iii"l"i;"^`^",i:,""^^,:"^^,::ll:"^^^^I;;ill:"i:li!ii,l,,"^^^^. ^i
                         ,;   '.'`  l``'``^ l .'^^ ., '`'' ":'``'''I'`+[1! <`>)[?_`~ . ..    ^i
                          l". <i}]. I"+-[11,I :?}~'., {)-+ 'i]--}-l;.`\[}I ;;(?]^  i _[-})1>.!"
                           ,::`^''^^^^^^^^"^"'`'..``^'''""`^^^``^,^:^^""""":":"""",;";;"";lI;^
                              l!<<!!"^!l>>!!';l!ill:'!li!l!^"i>+il!'Il!!l!;`!;l!li""ii>!ll.
                             .~^]!:'~<l;+['il<'[!_._I!:-{::!_"!?1.~"~']?] ?l!:-~^l~I`--) +'
                              ;l;;Il"`!ll>Il';l!{>I:.I:,lll'"lI:I:l.;lllilI'!;,;;!^"llli;l.
                                                ;I^">+->-+_l~__<<,              .
                                                 ',,",:,:^:::::",".
                                                           ;"
                                                ..   ..... +l .
                                                l~<I!,>:_ii<_l+>l+~<~++"
                                                           !^       ..,^^;"
                                                    :^`'`"'~!"",`''.  ;i<;<
                                                   .!!<!;~l;>>I>;!_I  ,-|!!
                                                                      <];~I
                          '''''''''.'``'''''''''''.''''''''''...'''''':lll` ........''''.....
                         :;'`'''`'I-~~,````````^~[[,`^````^^i]-<^^^^^^`'"-][!^^^^^^^^^,"^^^^^i,
                         ;"       "+i+^          .'         i?_~         ^^^.                I,
                         ;"       "<>?:         I!:.        `^^^        'I,l`        :l"lI`  ,^
                         ;"       ;<>~"         ";^         ^::"        ';"l`        "I:i!^  :^
                         ;"       ;<!_^         ",:.        <?++         "`''                :^
                         ;"   .`. <]>]"         ;ii'        >~i>        '<lI,                :^
                         :^   `I` ?)~?"         ''.         Ii<i         ' '                 :^
                         :`       "ii!.         i_l.                    ^~;~:                :^
                         :'         .                                     .                  ;`
                         :".......'`^.....................................^.       ..        I`
                         '"^^^^^^",,"`````````"""^^^^^^^^^,,"^^^^^^^^^^::"""""""""",::""""""":.




























```

*Figure from page 27 (2346x3317 px)*


---



4203-E P-238



SECTION 2 PROGRAM OPERATION



5-11-2. Move



This function extracts program data in the specified range of a file and transfers it to the extract buffer.



Press function key [F4] (MOVE) after the range (in terms of lines) of program data to be transferred has



been specified.



Example: To transfer blocks from "N103" to "N105" in the following program



(1) Program data in the specified range which starts from the edit line(>>) is transferred to the



extract buffer.



(2) The lines transferred to the extract buffer are erased from the display screen.



(3) The edit pointer is shifted to the first character of the line next to the last line of transferred



lines.



(4) Program data previously registered in the extract buffer is erased.



(5) When the specified number is larger than the last line of the file, program data up to the last line



is transferred.



(6) After program data has been transferred, the message "**RECORD DELETE" appears on the



command line. Here,



"**"



indicates the number of the specified lines.



(7) When a negative number is specified, program data in the blocks preceding the edit line (edit



line not included) is transferred.



When a negative number exceeding the first line of the file is specified, program data up to the first



line of the file is transferred.



(8) When an attempt has been made to transfer program data which is larger than the extract



buffer, the message "extract buffer overflow" will appear on the display screen and move



operation is not executed.



(9) Pressing the WRITE key without entering the number of lines causes program data in the edit



line to be transferred.


```text


                                                                                               `^^^'".'".^^^
                                                                          ''.''...    '..  ..  ~?_-i];,<!?]-
                                                                         ,}[_>~++{l_^!+-++-?--}>;__-?]+~~<_~
           ^^^^^`''````````````''''`````''''''''''''...'''''''''''.......'''''.'`''`....''`'''`''`.'''''.`'`
           ^,,,,^,"``^^^:::::::,,,,;;;;:,,,,,,"";;;;,,,;;;;;;;;;;;:;::::;I;IIIII;I;::::;II;I;,,:,,;IIIII;,:,
           ~,;l,>  _-lli
           :^^^^:. ";,":
                 +<<:ili>~ii:~~~~i-l!+>+<>~II-+<I<,]<;l<<i__~<,<>l<::<Il>+;Iili>ii!~<l!li!;l~!"!i!!lI!I!~l`
                 `'"'',^^^"`',"^"":",,"!:,"^^:,,'"'""^^I,":,;: :,;i^`,^"':"^:"""::":;""^^,"^::`;;";;^,;"II
                '>i>>!:i!!<i<"<<<"+!_^+-><<-I:??-,<<l,~i>-"ii:-i!i;:+I~i<>"!;lilili>,!~~i:i:ilIil!i<i;l!;I>i
                "<<+~;>~+i-__<`^,'`."`^```````"^,'`""',";I`,^`:"^""^"`,,:;`"`:,"i:::^";;:^:^::^:;:;:;";;^:lI
                ';;:".l;I;;Il:
                ^+Ii!ii<:  ~i:+iii-~:~iii>;il!>^i<i<_I:i^~~!~-,II;<!,!<ili!l:;lI!ll!:
                .:":,:;,"  `,`;,"":;',":,:^^",,.':";l.`I ,;"Il ",^:l`:lII!;!!I:;-l!l:
                  ``  `,'```'` ^`` ..`'. ....^.'' .  . .^ .  ... .' .  .   .. .      . .. ..' . ..  '
                 `i>^ l!i-_~?!"[??!!;>_+;[-_~+?+l>?<1+:]+~_I>[-<+l?<+I<-+I_-~i_?l!l!!><<-]~-[~!-+!_I}_!
                      ;<?~-+l+_}?>.                 .                            .
                      .'  .   '
                 '_-` I~~<!+>~;!>~i--<>~I!!!_i,<<+<~!l>~]<"<~lI<i~>>lii!l,+i:l~>i>i"!lliil.
                  ^^.   `^''`"'.^"'^,`^^.'`.^^."^^,,'',^", :,`^:";",^`""".",^^;l;;i',:";::
                 .>~. ;~I:"!~::l!l>l`!`ii>!lI;:;!I^!Il'!;:;:;l"'l:i;^l::'::;,;`,:"'I::,,,':I:;;,;I,::,
                 .ll. Ii><I!!,Ill;!l'l^!I;l!;:::li^Ill,!!iIi!<,,!:>i,!l>^lii,!;;!i,~~!I!>,!IIi~!<<l!~l
                      l!!~;
                  ^^  '`. .'''.`''..''.'..`... .''...'..`. .... ... `' .       .
                 `+_. !<~-?+]i:???!+~->~~+[~,+]--[~_-!<l--i!_-<--i_+][_:_;_i?-_-'
                  .     . . .      ..      .  '.                            .
                 ^[-' i?~+~,<_iI?~+~[++:>-~---,>i<_~__:<~];+_<;--!+<-;~i?_>!-~'<<i?~_~;l-__"<>l>l[_I__~;++!
                  ..  !ll~~i~->!+?".... .'..'' .'.`^"' .'`..''.^^.''`.'.''`.`^'"``;^"`'`"^"'"^'^'^"'",^'^"^
                      `'.^,^""^'^"
                 '+>  ;<<!',",;;;;^;i!:"Ii,IlII^I;I:!i;;;l.iI"^:;;;;,:^^"^"iiI;;lii";>i,!;ll^":,"::,'^"`;,`
                 'i!. !~_-I~!<[>+<;;<-~;<~!i<~+l>+->--<>-+"~>il>_~~?}}I`ilii?~!>>+~;l~<i~:!>'i]+>++>:!!:~~:
                      ;i!Ill~l!"l<!  !<~>'.l,;.l><i<~>>;>>I;Il<>_;,<:_~,<_+<>+~<:ii_l
                  ^^  '`' .       '..   .`. ..     .. .                .              .   .
                 "~<. i?i?<^+I<+[]_i_:iii~++^<;i<_~-[_-"?~~}~?_;+??_!~!]~I-<+<-!>+_~~+]~?l+];~-]l+~iI?_[^
                      !i<:!~<l~~_<+~?,~l<_+~]-!~-;     .'  ` .     .    . ......`...''.."..'.''...'''`''
                      ^^,.`^''^`'^"^"'^'^,^"""'^^.
                      i]>~~,>,<<+__!!"i+i~~i'<<i~+__~+_?<!+~<~+~:~i~+><}!ii!_++<-__,i<<?<~~l>-+~:~lil<_ii_<<
                      ~<~;<l~~i~}>lii>~<<-_>i_:````'`,''`..`'''`.`.'``.^`'``,^^'`""'"^^l""^`^,""`;^^^`^"'""^
                      ^`:.^''"" ^^'^'",'",,`,,'
                 ^->  Ii:;;`;:'!!;;;I^;I,"I;;"'IIl!"I,:II,l!:`;,:;:;:`lll""I;:;';`,;,;,^l::'!I"`,;;,:^
                 ^iI  i>~]<^_~I~_~i~+;>~~l+-+i;i~_}!!ll>__<~>;_>~?>~!:+~_il?!ii;~I>~_[i:~++"~~>;<+<~>,
                      l!><i`!<>^!>><~--,'~>>i+!l<!~_"Ii>i+l~;'~i"~__<<_'i!,~_,<?~+_-^<<~+-;l~iiI<>>+'
                      l+~i<-i+"<;l~<!~~~><_~l                                   .  .
                      '`       . ...''`''  .
                 :{+  i!<~<~i>l<i"_<_<~+"~-!;++<ii>l<++ii+;++!Il>>-~<"+iIi~>"i>l<~i;<!!<i~!"~~_,>:><!:>-!
                 .^`  <i+!_l__;>~!<-!!i~;^,"'^``^"``^^,^`;"^"^'^,^":".,'`^:,',:,:;,:;";!:;^'::I^,`"::^;;"
                      ;;l^l^lI^;!;liI:ll,



































```

*Figure from page 28 (2346x3317 px)*


---



4203-E P-239



SECTION 2 PROGRAM OPERATION



N101



N102



>> N103



M104



Nt05



N106



N107



>M 3



FIND



N101



N102



» ~06



N107



>M 3



GOO xsoo 2200



X250



[§01 2150



X300



GOO X310 2200



X200



G01 2170



Move the symbol·»• to N103 using the cursor control keys.



Press [F4] {MOVE).



Key in "3" through the keyboard.



Press the WRITE key.



GOO



xsoo



2200



X250



X200



G01 2170



The following message ls displayed on the command line.



3 RECORD DELETE



F0.300



FIND



CHANGE



COPY



MOVE



EXTRACT



~6E



~:~



[EXTEND]


```text


                                                                                               '"^^`^" "'^^".
                                                                          '...'....   ''.....  l[]]_+~.<I?-1,
                                                                         .?}+ii~~[?>l^_-]+-]--{?"_-____~><<]"
           '^^^^`''````````````'''`````````'''```'''''''''.''''''''''''''.'`''.'`''`'. .'''`''`''`'.`.''.''`.
           ^::::,"",,,,::::;;;::,,:""::;;;;:::;;:"^"";;;;:::,^^"::;;;;;;;,""";I;;;;;:,:,,,:;I;;IIII:,:::::II'
                          :","^^^^^lIl:",""""",";>!;^^^,,^^^"lII"^^^^^",";ll;^^""""^`````````^^
                         .l       .~>+!         `<<I        ,[??;        l_~i                .I
                         'l       .<!~~         ``.         ^>i~"                     '  .   .l
                         ':    ;: ._~<i         _(_:                     ii~<        ^~!>]i  .I
                         ';       .-!i~                     "_--:                            .;
                         ';       .<!~i         "__!        "~i<,        >++>                .;
                         ';       .>I<<                     :?-_,         ..                 .;
                         ':       .~!_l         "+i"        .^^^.        IIi!                .I
                         ';        `^^.         .,^'                     "",,                `i
                         `;         '                                                        'l
                         '!"^`^```^^""""""^^^^^^^^^^^",,,"^^^^^^^^",,"^^^^""^^"""^`````````"":I
                           ......... ................'''''.Il''''.'```'''''''''``''''''''''```.
                                                           :l
                                      ^?i<><+;i<><>,;;,>l~!<lI+<~i~Ili>>;l>+i>!<<!
                                       .......''.'. .. ....'''''".'.''''.''''''`"`
                                                           :;
                                                           ::
                         ^,                                                                  .:
                         ^,                                                                  .;
                         ^,                                                                  '!
                         ^,   '~^:.                                                          `>
                         ^"  ^!(i~I:I;::,^^"l:""""^";,,,,,,::,,"",:;;,:","^:",:::,":^^,,,,^. `>
                         ":       ..l"..  ..!. ..'.'l......",... .'!"`+?{!.!^!{{{["!.  ..    'i
                         .!`  >l][. "`<_][|I; "-[~^ ; }1]- ^~-_-}-ii`.([[l :;1]{,  ;._+<~}_! ;:
                          .::"`^",""::,::::^,`^"^^"",',:::":;::","^:^^l::"'"^;;I"^^"'::":!il;"
                             .;lllI!"^!!i!!l';lliii:'lIl!ii^"i!!;lI'I!l!l!"'l:Il!!`"!IlI!;'.
                             '<`[<,'i!,<-['il_.[~?.~I!,~];;i>^<-}.+^_`}}-.-ll!-~^iii^]])._`
                             .!lllll,"!!!<;!`ll!!>Il`ili}l!^,;,,i;l ;;l!i;l^i;I!;i";li!<:i.
                               . ..       .   .   .   .'i;'l>+_!+_<!?_~++"    ..'   ... .
                                                         ^^,,:;::"lI!I;:;"
                                                           !"
                                                           ~;
                                                !~<:!"~,<!i<+;>>l+_+i_<`
                                                 .'.      .!"  . '`''`:^',`
                                                    ^'...'.~l``^'.    !l!Ii
                                                   .<i+iI+>;+~>+I>+I  I]|!!
                                                           ;'         -_I_!
                          '''''''`'.  ..........   ......'.-:   '.....;l:;'  ................
                         :;^^^^^""!+><"^^^^^^^^^<?];^^^^^^^`!_~+"^^^^^`',-++;","^^^^^^^^^^:::l^
                         ;"       ">!+^         ^::.        >-_<        .lI;'                ;:
                         ;"   '"' _1i?:                     >??+                             l:
                         :"   '"' ~)~-:         ;!I.        ";;:        `!";^                l:
                         ^'       ':;"          :l:.                    ^i"l"                :^
                         :'         .                                     .                  ,^
                         ,:^^^^^^^^^:,"``````````^^""^````````````^""`````"^````^^^``````````I^
                          '''''''''''`'..'...'.''.'``''''''~"'''''```'''''''''''`^^```````````
                                       '. .                +^
                                       !+!l~><>~I!<<~?]l!I_~<_<~l>;>+;<<+i~<>!<>.
                                                .    ..    :...           .    .
                                                           ?^
                         .                                 ".
                         l^                                                                  ,:
                         I`                                                                  :;
                         :'   "i.;                                                           lI
                         ;'   :i:-;[i<[<^_>:!_"                                              ll
                         ;' .^'.,Ii?]~+<:+<<-_!:,^^,:"^^^^^I,^^^^^^;",I:I"";:l!ll;,:^"::,"^  ::
                         :'   `''.  :   .  .:  '`' ", '''' >,.''..'l ,-}{^.l^_)}]+^:.. .   . ""
                         `l'  !!1i  :,?-}1[^: ;?->.'^ (??! I_?~?}_!! l(?]^.;<1][. `^;]_<[1?;'!'
                          '::"'`'^"^"`^```^`^`^^'`^",,""",^,^"``""^;","",^^"";;;:`^`^,"^",I;:'
                             `!!<<!!':lii>!I'!i+>l!""!<~<!i'll><l!;'ilii!!^"!l!il!'l!i>!!:
                             I:>]< !l+'[_- <!<,?~!">i^~-} <;].?}<._:!:?{;:~>`[>~ -;~'+{?.-
                             `!l:IIl':l;IlI;'!l;lll^^!I;lII.;l::;I:.llI!ll^"!I:::!'lll!iI;















```

*Figure from page 29 (2346x3317 px)*


---



4203-E P-240



SECTION 2 PROGRAM OPERATION



5-11-3. Extract



This function inserts program data which is registered in the extra buffer before the edit line (>>).



Press function key [F5] (EXTRACT) and the WRITE key after the edit line has been selected.



Example: When the extra buffer data insert before the block 4 N203"



(1) Data in the extract buffer is inserted before the edit line(»).



(2) Data in the extract buffer is not erased.



(3) The edit pointer remains at the same position.



(4) If no data is registered in the extract buffer when EXTRACT operation is attempted, the



message "extract buffer empty" is displayed and data transfer is not initiated.



(5) To erase program data registered in the extract buffer, proceed as follows.



[F5] (EXTRACT);C [WRITE]



File data is not changed.


```text


                                                                                               .'''.'' ^.'.'
                                                                              .                ![-?~~i'_:___^
                                                                         '[1->>++]~>I:_]-<]?+_[];~-?_-__><+?`
           `^^^^^^^^^`'````'`````````'''''''''''''''''''..................```'.'`''`'..'`'^`'`^^.^''`'^`'`^^.
           '""""":;,"^```^"":;;;;;;;::,,,:;;;;;;;;;;;;;;:::;IIIIIIIIIIlI::::;III;I;;::::,:,:;;;;;;II;I:,,,,:.
           i;:i^>. i<>>>>;
           "^`"`:' `":";:`
                 i>>!I!ii+><,i~+~-!;~i+<<<;I?_<,<<>~lIi:>>><_!li;l:~!I:!i!;l;i->,i!i!l:I!I"I>!;I;^:"",
                 ''``."^^^"^.`""^",","i:::`^;:;^:`",`^,`;>l:!::I'^^:,,^I;,;":;!!'ll:Il,^:I"ll;";I^;;;l.
                .~i<_<l~~i-~~,i<<,[<-"?_<i~~+<l~,>><l<i;l_~~i_lI<i"l_<I,>i"li<"i!::!!"l!!!^:l!l;!l:
                 ^.'``.^''`^"''^,^` ^.,^'' ^^`'''"`"''^`'^'^'``^";^"",``":`,:;^;;:^I!,:l!l`IiIlIll:
                .[~+_<-]<  +}~_~;-+i>+-_>_~_]~^_?_<:<_-~I~?_!<;<_ii+i>~`_+_~_"
                                               ....  ''  .`.'' .`' `'`` '^'^"
                  ;!` ;~i<:;::!!"Ill!!:;,l~l^;`,;;;lI:,;Il":`::^',l^,"^'^'^.
                  "^' ^;ll:""^:!"II:i>,;lI!i`l""!ii!<l:>><i<:!~lI~-;i><,!;i:
                  ;!' "I":`"^::^'"",^^^^',:'.`'`''.''`''.
                  i<^ ;i>_!I:li>,~~>~+I;>~~i`>Il<l><~-__l
                  ^"  ."'  '^. .'..    .     ..'         ..` .
                 .~-^ `i-+l-_!<~+~?+:~~~__~<l}l?+I+}++~l_<]]~+I
                   .  .'                              .. '        . .'.   .
                 '_]^ !!:<"<-_>li,~-~__i~<l>`__l!~]>+>I<>?-l:[~~i:+<<~-__!I'+~<<?~>l">^-]<>__-+;;-~"
                      ,<~++___;l_+__+>i>-}~,<<~<~l,~;]~~~<>~>l~<<;+~<;<<<i>>ii>l+~ii~~>_<<`:,,,^'^,'
                      .'"`^^::. "^``^'`"`^, "`,^:. ,.:;;^l;:,'I":`;;I":;:::;'`;';;',l:!!l;
                 .~~` :<^il!!;,i;;ll!;^!ii^;III!I;l;::^l;'::;:,:":"i:`.,^"",:,':'",:'^`
                 .;I' ';^l:l!:,;,!>;l"`l!!,"!~lI!:l;";,!<:ii!!<!:ii<~:I+l><_~!I-II<<i<~"
                             +~]lI_i<<-~>l>ll:;+>_i<+<
                      ..     "',"^,^`'`"^'.,,^,;:,,";!.
                      ~~]I>]]<:>,i~:<<~i~-+;
                        `.'^^^.^.`^'^`"`I:"`





















































```

*Figure from page 30 (2330x3295 px)*


---



Data in the extract buffer



N103 G01



N104



N105 GOO



N210 GOO



N202



» ~3 G01



N204



N205 GOO



X300



X310



X600



X150



X200



X210



4203-E P-241



SECTION 2 PROGRAM OPERATION



2150 F0.300



2200



2200



2150 F0.400



2200



Move the symbol·»• to N103 using the cursor control keys.



FIND



CHANGE



COPY



~VE



EXTRACT


# I :~ I

:~RT



[EXTEND)



@J @J @J@ ~@ @J @J



Press (F5] (EXTRAC1).



Press the WRITE key.



N210 GOO X600 2200



N202 X150



N103 G01 2150 F0.300



M104 X300



N105 GOO X310 2200



IM2o3 G01 2150 F0.400



N204 X200



N205 GOO X210 2200


```text


                                                                                               .```''^ ^.'''.
                                                                            . .       .        ;]___>_ ~;__>^
                                                                          +[_~>~~?_l<`_-]+--_-?[;~+-__?+>~~]I
           .````'`'''``````'''''`''''''..''''''''''''.'....'''............``''.'`''`'...'`'^'``^.^''^'^^'`^`'
           '::::,,"",:;;;;::,:"":::::::""^^::::,:;;;::::,,;;;;::,:;;;I;I;;;;;,,:,:;;;;;:,::,:;:;I;;:,:,::::I^
                          :^^^^llII!l!;:;l;;;Ii>l,,,"^^^^^^"""``````````"""""^^^^^^":::^^^^^^^"
                          !    !<~!!;i!;~~~<I!~_>                       ..         ...........i
                          l         .            ..                                           l
                          ;        ~~~-.        `_+"                     ;i~_.       '+i<->   !
                          I        >i>>                     ^<~+:                      ....   !
                          !        <>~_         `+_i        ^_~~,        I-~i                 l
                          ;IlI;,,,,,,IllI;,"""""":::,;;:,""",:;;;;,,""""":;;l;;,,,,,,,,:I;;,",:
                          l""^^^^^^i_>~:^^^^^^^^:+_<::,^^^^^:+_+l^^^^^^^^l+-+,""""""":;;;,"""":
                          !        i_><          ",^        "-_[:        "I;:                 ;
                          !     ``.{1-~         ';"'        ',^!^        ''^^        .,`^,^  .;
                         .l     :"^{}_~         `<!^        .``'.        ;:i>        .!l>_!  .I
                         .;        >~+i           ..        ,-~_:         .                  .l
                         .l`''''''`+--<''''''''':-?<.'....'':-i!:.......'<[__'.......''......`I
                          ^^```````'^`^^^^`^^`^""^^`^^^^^^^;l""^`^^`^^^^"""^`^^^^^^",,"^^^^^^^`
                                                           "i
                                      ^+lI:I!,;;l;;^""";:!;!:;lI,Il"::;:^,;I;,:;:"
                                      '!:;,,I"l;;;:.,"';";,I,;ll!:l,;III^:lII:;i!:
                                                           "l
                                                           ;!




                         .:                                                                   ;
                         `l                                                                   i
                         `l                                                                  .<
                         `;    ,`                                                             I
                         `I  ^l]>,"",,^""""":"^""""^"^^"^^^",",^^^^",",`'`^^^`'^^``"",,"``^. .;
                         `I  ..   ..::     .!^.  ..'I.    ."l ..  .:;`~?[>';^;[[{1II^'..      ;
                         .!`  l!<{' "">+}]{l:.'~_~" ! +)__ .>_~<?_il^ {{)< :"{}{!' : <>>>+_l ^l
                          .;:"^`"I^`:::;I;I,:^`:,`'',.;!;;`^:::"Il,:^.i!!I',"~!!".`:.l!II>_i;;.
                            .',I,;I!"`l;;III`:l,:I!".II;;!!^`I::,I;`,!:I;l:^I,"";i""l,"^;"``'
                              ~'?<,'ill!??`!;<`-<-'_;!,+[;;l>"+?]'~^<^{]-'_;!;]~:;il"+_1`_`
                             .>;>ll;I,ii>_Ii"i;>i+;>">li+!!;lIi++,<`i;<>_:~"i;!!:!lI;i!-"+`
                               `'```  .'''`.  `'''`  .`'.`'  `'<I".  ""`'"  ```^"'  ``'.`.
                                                           .    ,i~+li<<:_ii>_<!i'
                                                           >,         `"^:^
                                                    '.  .' ~I'''.     iIl,i
                                                   .i!_>!-!l+~!+li_I  l-t!I
                                                           :'         -[!<!
                          ..'''...     ...'.....    ......._:   ..  ..;<;I^     ..
                         "I^"""^^^;~i!I^^","^^^^>+_;^^"::^"^!~<>"^^",:^'"~<+l^^^","^^^^^^^^^,!^
                         :,       "-~<;         ^,:'        >_?-        .llI"                :,
                         ,,       ^_>_:         ^:^         ,^;;        .^'".        ^,'""'  :,
                         ::       "+l+l         ;~;.        '`''        '!;_,        :iI+~,  :,
                         I:       "~i<I          .'         >?-+.         .                  :,
                         :"       !->-:         i??"        l<Il        '__?I        ..      :,
                         ;"   `l^ -|-~:         !<l'                    '>!?;        I~I~_,  l:
                         ;"       :-_~:                     !~_>                             :^
                         ;:.'''''.:-?];.'''.....~]_"...'....~-<+'.......`~~_;.........     ..;^
                         .^`""^^^^^"""^^^":^^^^^",,^^^",^^^^",",^^^","^^",,:"^^^":,"^^^^^^^^";.


























```

*Figure from page 31 (2346x3317 px)*


---



5-12. Page Mode



4203-E P-242



SECTION 2 PROGRAM OPERATION



In the page mode (P mode), displayed screen is fixed and keying in of a character, etc. overwrites the



existing screen data. For the input on the screen, insert mode (I mode) is also provided in which keyed in



characters, etc. are inserted. For details of the insert mode, refer to 5-13. "Insert Mode".



This page mode is used in the following cases:



(1) creating a new file



(2) replacing one character in an existing file



(3) adding a character-string to the end of a line



The operating procedure is as indicated below.



Press function key [F6] (PAGE MODE) "P MODE" will be displayed on the 1st line of the screen.


#### PROG OPERATION

»01000



N100 GOO



N101 G56



N103 G41G01



N104 003



Nl05



N106



N107 G01



Nl08 G40



N109 GOO



N110



Nl 11



=E WHEELlOO.MIN



file end



X300



X400



>EX



xsoo



X100



X200



X400



X300



"P MODE" is displayed.


#### EDIT Pt.ODE WHEELIOO. MIN

97/07/15 14:10:00



Y300 S250


#### Z-55 M09 M03

Y200 F100 D11



Y300 10 JIOO



Y300 1-200 JO



Y200 1100 JO



Y200



2100



@@)@)@@J~@J@J



Press [F6J (PAGE MODE).



(a) When a character is keyed in in the page mode, the cursor-located character is replaced by



the keyed-in character and the cursor moves to the right. In other words, in the page mode,



the cursor is moved to the right and the character (including a space) located by the cursor is



replaced by a keyed-in character each time data is entered. Therefore, if an attempt has been



made to assign a character-string many digits of characters, subsequent character data might



be replaced.



{b) If one line has more than 63 characters, such a line is displayed in two lines on the screen with



the second line preceded by"&''. These lines are processed as one line. In this case, the edit



pointer and the edit line move to the lower line.



(c) Each page has a total of 16 lines for edit operation.



When the WRITE key is pressed while the bottom line is designated as the edit line, 16 lines of data



are shifted by one line each and a blank line is created on the 16th line. The edit line does not



change and the edit pointer is placed at the beginning of that line.


```text


                                                                                               `^^^'".'^'``^
                                                                          .  .. .    .'.      ._]?[!?`;!<_?<
                                                                         ;{[~i<~+[l_'~+?+_?-_?1lI-+__--<<<-~
           ``^^^```^^^``'`````^````'''''''''''''.....''''..'.............''`''.''''`...'''`'''^''`.`''`''`'`
           ^,,"":::""^"^^"'`^"":;;;,,:"";;;;;;;:,,,,,:;;;::;::::::::;IIII;,,,,::;II;IIII:,:::;;IIII;:,:::;I:
          ._":!>   ->iI>,I->Iii`
           >,"!i. .,:+?<,^<!l!<'
                ^l'!:'',:;^.:""l`;>`:::!I''!I,;:,::`:":::`"":I,,"`:""":","^':.":^'^;"""":".':" `^`^^^""^':"`
                "<;+-i!~-[<:><<?I>;"->>]-::__~<__++;_i>_~;i!;+~+!!_i!!+_+i-:+">IiIi_+>+~?-,I[+'l~<<~_!+_;__<
                :_i<_i-;<!!<i,;~+_^`!i,;>>l<i!!;>^<~:!il~>l.il<<>:!li?"l"!>!~+,<"_~i,<!!!>+<;l;~~<<I!_<<+>!l
                "~i~i<_?>~.<-!.++l;>~_~]+l -~~"~--_?:>><-<I~~++;!~>_~`>_-<:_:+;i?^I->_<>>{<<_!`...' .'``''..
                '"`^'`.''`'``` "`' '^"`""' .`^.^^"^^'`..^^`",:^'`"",,'^,,,.,'"'`:. ,";,^^;,,I`.
                `~_-l+]]-:<<<}>I<,---illl_<l_?~>_+_!!__+~:
                   ..`.^.         .'.  ...'.'''''',^'^``^'
                 ">>. !>+_-<+I<:~~~;[?,
                 ...  '.'''.,'^ ''^ '`
                 `+<. ;><<!lIi"!!i^ii<!>i+!:i^<I,i!iill,_>^
                 ':,  ':l":""i,,";'""l:l:l:':.!^'I;I;,<^;!'
                 'il  :;Ii:,^"`l::;:l;^';"":^l.I;^`"",';^'^:;.
                 '!l  I!lil<:l^lI!I!i>,^i;,_I!^;!;,ll:,I:l,l+`
                "<!I">ll;ilI:,l;;lI!:I^!`II^IIi:!iI:;l!:I'
                .^,,.ll:,I";I;:";I;I:I^;`;;^";;;!!I::i;:l`
                l+<~~:l!l!-II:>>;l~+i"_~~<<^++!i<~""<"_>!~]~^i_<I<,I<i><!l!l:!^ii;`!>:li,;>!<l"!ll!!:
                .'",,^',^","^',;:,^,:^"^,::',,,,,:^.^';,,:;^ :I,"l,lI~>i+!l::I^;I:`;;^,l":;:II^!II!!,
                                                                  `!:-!i?,:Il<<><>+
                              '`'.  .'  ..'..'''`^^`''. ..'''````.. I'.''``''......'.'.
                             :::;>++!l++<il<iIIIll!l::i>l!;;;IIIIII~+!;:::,ii!l;i!iiII,;.
                            :: ^:~}(~>}{{->{-:::"""""^])+<;;,""""<!1|(+<!!i1ff)]|){f|i `l
                            ;'                                        ;+~_?i~<!?l+<-?:  ;
                            :` .;!>~?;                                                  i
                            :` .'-_}~'  :]_.     I_?i   '>?~   ._-]^    ..     .        i
                            :`   +~]l   I([:,.   ^",^   .^:"   .}_/;   ](<   `1_,       l
                            :`   +?}>   l|-+<`   ~\\+   "[([   '~_<.   !-<"             !
                            ;`   +_{i   ^lI      i[1~   "]|}.   I!li   ;]i:             !
                            :`   _])<            i[{+   `]1?.   !?)>   i(               !
                            I`   _{}l   l]!      <|\~   .,;:     ..    '^               !
                            l`   +-1>   i\}.     l_-l   `i_~    "^,.                    l
                            ,'   _<?>   ,>l                    .!li`                    :
                            ;'   -~i;                                                   I
                            I'   '''                                                    <
                            I'                                                          ~
                            I'  .,.l;;."I^;,`                                           ~
                            :.  :]i1](_I<;~!:                                           !
                            ".  ^`^''::                                                 l
                            ". .;-+..  '''''....''....'.'..........    .        ......  ;
                            ,. '^,"'^:!`'...!I^''`^i,' .`,i'''.'^;,<~+,,;:~+-~II`'`^^'  l
                            ;"  ,I<I `;;><+<l"'><; ; l_>: :!!liI::.{11`.`~{|_:,"Il;;il'.l
                             ::^":>I.^";ii>i:^^!!;`:`!~!:'"llI<!",'+ii`^:~<~^ :"i_!i?-;;'
                              .,lII;I`,;::;,':;:;lI^!;,,;,`;:I;I^'I^,,I""I;;l!^";;:::''
                               +^]~^!!<"_?:ii<:~-`+!;i[_'+lI!]-`i!I<]-^+i:~ii:~!,_1iIl
                               ;IIll!^;l!>Il^Ill!;I^lll!;I"lII!I:^!<<i;;:llI;l;:!lill"
                                                                   .l
                                                                   .<;I:;li"llI!:l!;ll`
                    .. `^'..   '.   .... .    .. . ..             ..":!;I:i;IIIi:!iIll"
                   l[< --i_i"<:__-<++?,;!i_~~+!I;iII+<:_-+~">!i}>'_>l:I!<~;;<l>_<>^~<<<+~?;:i,~>~+><<;i!
                    . .<iIi<ii>>!;,<<<!<<<:Ii>l~~l"lli>!"_i!l<:>;I~<"i+~i.ll:+-<!">!i<~^II<>!"i~>>:>l!+!
                      .~<l;>+<<!Il:i<<>~i_:++iI>~~:<>><+:Il<>~l!i!l~Ii]l>:II:!i>!,>i!>>;>l><<:-?-l:!!><l,
                      .!>lI<ii<l:i:ii!>>l<Ii~i;~->:<i>;<>l!!<i~><+"!ii!i~<+<!l~~~~~l:>i?-+il-I><!,<!!>!^+'
                      .!_><<<>;l+^<,~<~<~,I`>l<l~!_:"~~i:;-i<`i+<I!I:!i<I><. >!<ii<!+^;!i<'+_<l>_I;i+"i~i<"
                       li~+lI<"~~++_,~l~<-<_+->:?_i~>i~~><,___]:~<li+<<<_~<l^>i+~+<i~~~:<>_~~<_!;-__li~~?<
                      `_<;~~~+!~~l:,.^'^`"^"^"^'"^'::'^"^:'"I,,'"'^`:",",:""':,"::;::""^"";":";^'I;;^^,i;,
                      .;I :>ll;;;'
                   ,l" ;.,^'`"^'`":',,":`:":^"l"^;,,,",""'."`,"'^,"^'"',"^,"'^"```"^``"`^`'^':"''`'``^'`^,.
                   l~I.+;~<<l>+ll+_:!+<<;!<_!!-l>_?+_]_<<l,_i~IIiii<:~:~<+~+_~~:l:~_!:~<?!I~"_+!:~!<~>">_-,
                      '>>:l+>ii~l;!~:>!~<~<<>,il -:  !!>>~:!!<l,?+:>~>+~<~~<I~~,<+il~~I lIi-_;;~~_":<<:<<_'
                    . '<<+~]i;?<ii_+;+~_!-+!i<<~iI<;-+l~+++!!<~l'''`.'''''''.''.'''.''' ...'`''``^'..`.```
                      .^`''". ^.'.'`.``' `".'`'^` `.^"``^^,'.'"`
                   :!,'~l!i"lili"!!!";:li!"!:;>;!Il:Il^,Ii";lII;!;l^
                   "l".;;;"^ll>i'"l!^;";;I`I."I^:,l,"l',lI^I<IIIIIl`
                      '<~!l,llI:+~<!i;"!I^l,l;Ill!,Iil>,>:;;:i!:;^,I:l:!>l!lli~II;l;lI:ll!;ll`'>l!II:"!:!!!'
                      .<>!i~~-~!iiI:!l;<-ili~i+l>~!!>!_i<~l<<<i<I;!>>~i>><>}~~<~~->i!<:!_~!l>!;<<>!i<l>I<~_,
                      '_<;l~><<<:+~">iil<~:l~<i`il>^!;><i<:i!<`>^!i~+~~;;+'i>i i--">!<` ;l_"i+-"~i!^_<+i"><"
                      'il~i_?"<!+!-_;!~?;<<<i-!l~!~?_++:_!<<i;-~->~><?;+l+_-;i~~
                           `.           ..   .  .'..'.. '. .. .'^....,'. .'' ..'.








```

*Figure from page 32 (2346x3317 px)*


---



4203-E P-243


#### SECTION 2 PROGRAM OPERATION

(d) When the WRITE key is pressed while a line other than the bottom line is designated as the



edit line, the edit line is moved to the subsequent line and the edit pointer is moved to the



beginning of that line. This also applies to the insert mode.



(e) When the program cannot be displayed in one page (16 lines), press the page key



@ .



To return the display to the previous page, press the page key



5-13. Insert Mode



In the insert mode {I mode), keyed in characters are added to the data in the displayed file. For the input on



the screen, page mode (P mode) is also provided in which keyed in characters, etc. overwrites the existing



characters. For details of the page mode, refer to 5-12. "Page Mode".



The operating procedure is as indicated below.



(1) Press function key [F7) (INSERT MODE) "I MODE" will be displayed on the 1st line of the



screen.



PROO OPERATION



»01000



NIOO GOO



N101 G56



N103 G41G01



N104 G03



N105



IN)06



N107 GOl



N108 G40



N109 GOO



NllO



N111



=E WHEEL100.MIN



file end



>EX



EDIT



X300 Y300



X400 Y200



xsoo



Y300



X100 Y300



X200 Y200



X400



X300 Y200



"I MODE" is displayed.



I MODE WHEEL100.MIN



97/07/15 14:J



:oo



$250


#### Z-55 M09 M03

FlOO 011



10 J100



1-200 JO



1100 JO



2100



FIND



CHAl\l:iE



COPY



MOVE



EXTRACT



[EXTEND]



@J @J



® ® ®



Press [F7J {INSERT MODE).



(a) Each time a character is keyed in in the insert mode, it is inserted before the edit pointer and



the character-strings following the edit pointer are shifted by one character. When data is



fnserted successively and the currently dlsplayed data has reached the right end, data is



inserted in the next line that is preceded by"&". These lines are processed as one line.



{b) Each page has a total of 16 lines for edit operation.



When the WRITE key is pressed while the bottom line is designated as the edit line, 16 lines of data



are shifted by one line each and a blank line is created on the 16th line. The edit line does not



change and the edit pointer is placed at the beginning of that line.


```text


                                                                                               `"""`,`.:.^^"
                                                                          ....'... . .''.....  i]-[~]i"_l?-?'
                                                                         `[[+ii~~]i~,:_--~_[??{-;~_-_--~~+-]`
           ''''`````^^^`^^^^`'``'`````````''`''''''''````'.'''''''''''''''`'''.'`''`''.'''`'''``'`''`'`'.'''
           ^,",,,,::,",:""""""^`"^"",:,:,"^"^^`^^^``^:,:,,^,^^^,",,,;,,,::"",""^""::::;:;:"^"^",:::;:;""",:,.
                    :<: ~<!!:"i!`>+_lI<`lI;"l`l;;;Il;^!;i,",l;;'Il;;'l;l`:I,";;i";`I;;^I';l::;,II;:^;`l;,
                    :l:.~<_<>I!ii>iii!<l><~Ii!<i<<~~l>-!>i<>>><:<i<+Iii~I!<_l~>++<:><+!+:<~++[i___i![;!il
                       ^>ii">>!'>i;>>>:~ll,<:>I!<<"l;!><,~~<~~~i<>;;+<:!<iI>~ll>+l>i>l-<^~"!!!<~>;<;+~,
                       "+~--<>i};<<~+[Ii+-` >i~l!_~lI?<+]]!ii!_~I~<_~lI~>_]^
                         .`    ''    .         .     '.  .. .      .   ..'.                       '`.
                    >?I'-?<_i>]~;+<~+i_~:<_<<<~!?I!____+<+!ll;~<ll+~+lI~+l+<++":<i<~:!<!I+~~!i<<:l_+-'.
                    `"`.".'`'.`^^,'";'^` `,'`"''^''^:,^:^^..''^^'",I;``'^.^"""'"i>;:``,",Ili,^;l"^_]l..
                       '->:-_>_:>~~,-_<-]lii;<~;<>~i>>~;>--?:;~~+_,+~!l+~]l!<+"l[}>
                                 .'.''`'^`.'..''^.'.'``'^^:^'``'`^''`'^^,:''^,'`;;"
           iI"l>'  ;IllIi">~I;i;
           !!^I~^  ,I<~i!`i~><<i
                 ;^I"`^^","'"`",`,","::"'::^,:,,',","^,""^^""`"":"":^":^',""`^^;^'",`"^'^^^,".'I''"^'``''^'`
                '_I<<<><-+l;><+-l>!<<+}<:~__~~iiI>>_i~>_~i>+~l-<_-><>l<+I_+_iiI~<l<-_++-+~l!_:"<>;~_>!_+>i>i.
                '~+Iiil<>I'>~_+"Iil~I!<,>;!~!"!;~<!l+!i;+~<:l;+>!>;>~ii<I:">!_<_>_<~^<_I^<i<>-<~_>_~>l<~+?<+`
                .><_<~<?<+,^?_>;]_-]_:>l>+i!_+_!l~<_],:+[?;~l<i;_:"]~+-i<?i+-!``.''''''..'''.'.'`''.''````':.
                .:^"^"^"^^'  `..,^,,".".'"`,,;l`.`^":' "":',^"^`:` ^"l>,";:;l'
                .<i_,i+_>--<-I+ii<<+<_I>!l-:i>+i__<<I+_i<;
                   '.`^`.'..:'' '''''..'''^. .''`'`` ``'''
                 .!>^ ;>l>i:Il!i~i!:i<;l_!!,_~+-~+~"+_i~__,:;+_<_?-"l~<;<:;+ii~i!>I,!,<<l^l<;!iI"i;i!^
                 .^"' ,!i~~>:,",,,^`,;,"^'"^:,::""^.,:,::;^.`::,::, :I,^I""IIIlill,";^;l;':l":lI^;^;l^
                      ,>Il>i"
                                                                       ':_-~--^i;~+~~<_!
                                                                     '",.''''' '.'^``^`.
                              ',,"^^^",^``^^`^"",,,,:;;:,,:::""""""""iI;:""'''`""""^^"^^'
                             ^I'!I?)|<-|1)-+1_,;;;;;;;;]]+!,,,,,,:!i/))!"""[1)}<?_<[_;;`I"
                             I' ``^,;^,;;I:,I:`''''``'',:,"^``````^"il!~[~-{{f[_)](}\[I  ;
                             I'  .```,.                                ^"""'.`'`^'"^""' .:
                             !` 'I}[)}"  "!:      ,!!"   `l!;   .;l;.                   .<
                             !'   ?-],   >\[      "l!"   ';!I   ']-|^   !+I   "+i'       >
                             l'   --]l   !)-_>'   ;~~:   ">~i   ^+>}'  .{]l   ^i;.       <
                             l'   -_[l   !1_^'    ~()~   ,[1]   .<l^'   l<+"            .>
                             l'   (]1!            i?}-   "}(}    ;~)_   >].             .I
                             l'  .f}{l   "l"      >}{~   .li!    ">~.   I!              .;
                             l'   ]-};   ~|-      <1)i   `i<l                           .;
                             l'   ]_)i   <(?      `",'   .;I,   '<i-`                   .;
                             l'   }~-l   .`.                     `'^                    .;
                             l'   +l;`                                                  .;
                             l'                                                         .;
                             l'                                                         .I
                             ;.  "+:?-}I!+;->I                                          '>
                             "   ;l!<>}_`^'"`'                                          'i
                             "   ,,"                                                    '!
                             :. 'I?+`^""^^^``,"^^",:::,"^^^,^^`^^",,,^^^^^^^^"""^^^^^^' .l
                             I.  '.''.,:'`'^`;".`^^'I``^``.i'`^'`,l^-}}`;I!11{i;,''''..  ;
                             ^;' ;l}! ^">]]1-"'^__I " <[?! !<~+]<I,.([}.:I}[}^ ,'i~<<[_^:,
                              '"":^^"^^,;,::"^^"^`"``"^``"``"^`",^",,":;::l:,"""";;^:;::^
                                l:<i,l"l;~~II"ll><:!,lI<>;I;l!_iI:"l>+!I:;I~~il";l~_l!^
                                ~:<i"iIi,<_,lIil>-^+i!!+_^i<l!_<"ll;~]_:><,>i,;l>,<};>l
                                ':^":" `"`^"^ ^^^^"' """^,. "^`^,..,^",:.';>"", `,`^""
                                                                          ;.
                                                                    l<~<!->li++~+~I_>~_<'
                                                                     `^^`^ `'```''.^'^^"
                   .,, ;I,:"`,""'^':,,""::^^^^"^^","^^"";"`"""""`^`"" `'^.^```^`^`'`"''.,`''`,''`^^"`.`'^
                   '~~.i+_<!;>i~;<;~_?~~<]!l~I~-~<<iIlii?+:>~_<l;ii+?,>I~I<<-<~_~!~++!~I_~ii__;~~_~?>"-l~.
                       l<<`>!>i<>_!"_i!i?:li!i+<<~Ii<"<_!:<l!i+,;i<"<>-+<:l~'i!!`><il+<_! '-~i<!"~<~:<"
                       :!<>>~<;i!i!i<>i>?~^+!!l+>l;l>!i<~Il-i>_!i~i;-<iI<i!;<>!<<>!<<>,><>:liii`~+-I>l.
                       ;i<<>+<:>!_+>l~><i_l>i+!>i;I<>!>i_>!<>l~]iIi~++_;<~>;!<~!!<ll><;>?<;<ll!:i_~I;,
                       ";!!;i!^:^IiI^i!!^;!;,i>I;Ill!!i!i!;;~.,>  "li><lI;!+">>I,!Iii<~~<Il?,;!~"<!~
                   .," ""''' '`''''`...'^`..` ^'`''..^. .`' .'..^^.
                   `+<.l<~>Ii<-[>:~-;lI<<-;l!^_!i!<_:~~,++>"-+ii]_>i
                       "l;""`;"":;!;Il^^^'^^`"^""^"^","^^:`"^^:`^',""^"^;""`^^:"^`^`""``^,^,^` ^"""^^'^"^""'
                       I_<~~;_~!<~>>l_;~-<!><i+__+~i+~_<!_~><>+<iI>++i~i[+~}~~?-~l_!i~ii+?l~>>`!_i<>_l<!+?]>
                       I<!`il~_<I:+`!!~^~il`~+!i^-l>,I;++!i"!>,:I^!i>-<!'<:I<< ,_];I_<! :!<!:_}ll~<"!>~_"!~>
                       I~<_i_!;~>i+_>;~_~l~<>__,<l!_+><!I+I-<I<~<~ii><l!<i+<i<<<:....''   .'.''..'`.''``.'`'
                       ^^,,,!"`""^^""^:,",,,^,;.,"::;,:^^;`,:^,;!;"""II,"`:I"":;^












```

*Figure from page 33 (2346x3317 px)*


---



4203-E P-244


#### SECTION 2 PROGRAM OPERATION

(c) When the WRITE key is pressed while a line other than the bottom line is designated as the



edit line, the edit line is moved to the subsequent line and the edit pointer is moved to the



beginning of that line. This also applies to the page mode.



(d) When the program cannot be displayed in one page (16 lines), press the page key@ .



To return the display to the previous page, press the page key



@ .



5-14. Power Failure/Shutdown during Editing



The function to avoid the file from being lost is provided even if power failure occurs or power is shut down



by mistake during editing.



5-14-1. In-editing Comment



If power is shut down during editing, the following "in-editing comment'' is attached to the first data block of



the file having been edited.



"THIS FILE NEEDS EDITING AGAIN!'


#### OKUMA MACHINERY WORKS LTD.'

This comment is deleted when the same file is read out from the memory.



Note: This comment is not displayed on the edit screen.


```text


                                                                                               ^^"^'" `^'^`'
                                                                         .''.''...   .'..  .  '?[?]!]'!i>??i
                                                                         l1[~>~~+}I-'<_]~+??-]1!!-<-+_-<~>-~
           `````````^^``````'````^`^`'''''''''```'''''''''''''''''''''''''`'`'.`'''`'..'''^'`'`''`.^''`''`'`
           ,,,,,::::""::^^^^"^",:",,,"^"^^"^^":,,"^^"^^^^"^",,::""":"^",;:,::::,:,,^,",:;,:::"^^"""",;,:;;I,
                    l!."+!;l`li;^<<+li!"!l^;,":IIIII,;lII',";I:^!ll^:iI:'!I^::l!,;^;,,^;'!;::,,l;:","^!;`
                    ;I'"~~<~l<l~>~Ii>>ll~~!l!<!<+_~+:_~!>;~I!~iI+<-!!_+<;~_~>><_+i;ii+l<:-<+?>>-+~;++I~<,
                       I<~Ili+";_<:<<>:!<,lll!i!<i,<^i<;:<~><<~!>!,ll>^<ii:_+,i<_;~<>~[;;<"<>!~~;i;~-+
                       !-_-i<~~-,~l++?!-~~ "~+~,-?-,-]_?_~:+:-]~l_?->:_~~];
                        .'`  . ^              .  '. .`'  .... ..'''" .'''`.                       ''
                   '+]';?~<_;>_<I~!~++_!;+?i<+i>_,+-~+~<~~;<,i><:>~<~,l<>;i<~<'!!>~<l_>:i<<+;!<i^+~_!
                    ^^.'^.`^..`^"^'::`^..""'^"'`".^":^":^^ ''^`"`,:!,.'``.^"",'l>!;;^,:";;i!^"Il';_+,..
                       ,_I!]-i<I?~l!--~~-:-I~~>I++<!>>>:<+--'>+<+>;+~I>~~_;<~i'+1{;
                                     `. ' .  . .' . '....'"'."``^^''^`"^:,'`^, ,,;`.
          .<^;li  '_!IlIl"I!Ii;,I:!~!";I!:;::.l:";:,`!!;!;""`
           ~,,!<.  I;i~>~^":+~i!i>l_!i<>_>+<l^_+ii>]ii~+_<![<
                '!;^"``^"""'" ^``"^""`"I'"`'^^````."^^.' ''`",^"^^^"`"^^^^^`"""`^`.``''^.''''```'`.^^.'``'''
                `!<~l<i~+<<l~l_<>+>~+<!]>l>>iI~~!-~i+~;<i<i><_~>>+<_Iii+~++i;_~<~~I_~<~~I~l+>~__,+!?_<l~+~_l
                :-I;>~<__>"_i<!-:+_-~+>
                 ..         .  '     '`
          `],<i,; '-;++[-~~;_~~<>-<~"
           '  . '' '.`^^``;''^`^'^``. .                    .
                :>><~~~"~I__<!+><_;;<<i<<~_{-~_,]+!+-?<-_+~:~:~+[_~+l+<>>~-~i:_l[--+++_i~I]~i->-!_?]i~<<-li_
                l_+I]?Ii_><ii!+~+;!~}?~+`....'"...  ...'.`" . ''..'".''..'`'. `'^'^`'^`.`.'`'.'^'^^"```^^'`'
                `""'^;`^:"^,;^:::'"::;:"
                .                                               '
                .                                               '
                '        ":",;`:,^,`;;::,:`,"","""".""^"""`     '
                .        "ii~_;i~<<,]-_?<_l_+<ii~_+:+___~+:     '
                .                                               '
                '                                               '
                .    .
                '    .
                .    .
                .             "+-_>][>!}-_<>~-]_]<,~_<?]__!I>+i'
                ..             ^`^`^^`'"^^``^^,^'' `""^"^"''."^
                ;~>_;~~~+<-~+l<:]~+-+~I-__+:-~;!-_~_I[_"~,<+-!I<ii_<+;_+i:<~~>i<!
                     ''...'     ..  .. ' '.  .  '. ` .` . ''`..'.  .`.`^^.`"^`^""
                !?<?l    <_-ll<<<>++~I~,!<lI-~~_<i~!;>"+~l;i_!l!!~>!'
                .^^"`    '`,`^,^^^"""`,`^,`^:I:,I::^^,'","^,:^",";:"'










































```

*Figure from page 34 (2346x3317 px)*


---



5-14-2. Alarm



4203-E P-245



SECTION 2 PROGRAM OPERATION



If the file with the Kin-editing" comment ls run, the following alarm occurs.



2230 Unusable: direct of left side



If this alarm message is displayed, read out the same file from the memory and complete editing.



AlITO OPERATION



2230 Al.ARM


#### A.MIN O N 11

97/07/15 14:10:00



direct of left side 3EOO


#### PROGRAM *CURRENT MAIN PFOORAIH lm

» "THIS FILE NEEDS EDITING AGAIN!"



OKUMA MACH I NERY WORKS LTD.



LOAD MAX 'v



SP I NOLE LOAD



ACT POSIT (WORK) 0.000 0.000



A-Mtd



;Xf'S



PROGRAM ACTUAL PART BLOCK



SELECT POSIT. PROGRAM DATA SEARCH



(1M



DIS X 0.000


#### Y 0.000

Z 0.000


#### W 0.000

0 F 0.0



H:: 0 0.000



D= 0 0.000



z w



0.000 0.000



CHECK



DATA [EXTEND]



To give warning to an operator, the following alarm is displayed on the screen when the power is turned on



after the power was shut down during editing. In this case, an error file name is stored to the file of



"MD0:ERROR.BAK" (or "MD0:ERROR.LOG").



4248 Error File


```text


                                                                                               '^`^'^..".^``
                                                                           ...'..     .        ~]_-i_:,+!__+
                                                                         :]}_<-++[l+^i-]__-?-_{<I_<_~_-<<<__
           '`''''''''''`'''''''..'......'''''''...........................```'.'''.'...'`'`''``'.`.'`'`''`'`
           ^,,^"^,:^`^",;;;;;;;:,:,,,,,,:;;;;;;:::::::III;::;::::::::::,;II;IIII;,,,::;IIIIIII:::,::::;II;;;
           >,"!,!. l~!;l'
           ;"`:"I  ";l,"'
                .+!~i,~i">+]:+~!:~;!~]~li,;>i!!i>i;!;;!!.i<l!>iIi!li"<>>i,,ll;li`
                .^'",`":',"".^,^ :`":,,^l `:,^^^::^:""I:`,I;"I::l;,~"!ll;^"II;Il^
                '~~_]^  I<>i<+<<i l_><<:<ii-il<+!
                ."^^^   '``"^"``` .^^"^'^.^^'`","
                `_>-_I~[~!>,i~++_-[!!>;?<~__~~~.>_-_I<~l>_I!__~~I{+I_<~;++>,~_<i>>ll_<i;<i<__-?:<_[->~.
                   .'.'''....'''`":'''''^^`,"``.'`^'.`^.'^'`^`'^ `^.'^'.'`^.`"`'^`^`"^''"^^;"",'"""""l.
                              ^,::","""",,:"^""""""""""""",""^^^"^^""""",,""^``,,:::^^"^
                             l".!l1{1i)(|)+[|:,"",,,,,l][([;,,,"",,"",;]::,""+_:::,::+^^l.
                            .;  `,!ll":l<<>i!l``^'''..'""","`'.''''^""l[{?{-_1!]__[-1_` ;"
                            .^  .>/tt>i?}}j_"\';<i}-I:{i <-+""-_(,;\]-.'`^,"^^":"^^^:`  :"
                            ."   "+-_?(>..  .    i+<-_?+'?_<;l[][[{-. .^"" '. l[<.^"    :,
                            .:                                        ;!>< iI   <!{fi   :"
                            '!                                        ;    I;   i![\!   :"
                            `!        ^' . . . ''.. .....    ...      l'   _< . il]\!   :"
                            'I  ;;   .I~ii:i~<"1?_<I-i:+{^_[>-;^      I`'  ``   ..''    "^
                            'I              .              .          ;~?' I, .'   .`'. :"
                            'I                                        ;?:     :<   ""_" ;"
                            'I             ;]+):i]~!<]-"~]-_,^<l      :_<. :" ': .!">]` :^
                            'I   "_{[l|]^'`!],I'^:^`^;,.^:,,'.^^    .`,_-' >I    .->\[. :^
                            ';   "-I]-+:;_?`      '          .      ;(;'`        ^.     :^
                            `!   ';,.Il", li>I'   >:"!,     '<^l;.      -":I'    |"::.  :^
                            ^i   '<,'!+I,.<-+>' ;;?-i+I      l:<i.      l,<_"    l:~_^  :^
                            `I   ;<~'           :;I:.                                   !"
                            `;  '!I"'.''.                                               i"
                            `;   !_^ll_~^                                               l^
                            `; .;i^,"",^,;::,:"",^^",""^""::,"^^^"^^^^^^,"^`^`^"^"""^^. ;`
                            `;  ~[}}1};!{>-[^~]1_`."I![_{!;l`'''.i^'''''!"_[]?'!'`'`'.. ;`
                             ;^ +]~?!.,I]-;; l~]?-[?^,]~i ::-]]-l;.     "'-__' :"-+_[?!'l.
                              ""::",,^""""",^""::;l;:II:I:"":"":::""^^"^^^;"::`"":",l;;,.
                               'l!+!:l,!i_<I;:l<~iI::l<~!l"II+_l!^lI~+I!"!l~<li"!!~<;i
                               :>>+l`+>!>-+^i>:<+~">l,<_!;i<,~[;l:i:_1;<i>l->`_!!I_1`[.
                                "^`",. "`'^,. "''`" .,`'^" '"'`^" ':"",^ ^^`^"^ ""^::'
                ';''^`''^^^"^'^^ `'..'`.^'..^''`^`.'`  .'.'....'.'' ... '.`. . . .. .'..'`..............'...
                '<i_++il__!+<]~~;-!l}+<+]+;:<_i+-+<~i->+_+>lii>+-<+-<+ii!l+<I~i>+~!l_><!><<I~>~~~:~l~i!_<l<I
                ,-~-`i~>'iIi~_ !>+,I<I> >!<>`,~!>!<^+_+i<i ,>^~<+^!__+.l-:;>i~:I_>^i+>~l;<"]>i~+:_:>_~^??,l+
                ^]{?~i_+?[_+-!-_]+"i<,<]]+<<_??-~[-:>+_<>, .'..'`.'`^^.'^.``'^..`^.'"`^`'^.^^`^"."''`".`,'`^
                 ^;^"",^"^"^^^;^;^ :;.'l:,,,;,,:::^"",;^"
                "-i+_  '-!li"i~~
                .^`^^   ^``^..^".




































```

*Figure from page 35 (2346x3317 px)*


---



4203-E P-246



SECTION 2 PROGRAM OPERATION



5-14-3. Not-guaranteed Area Indicating Symbol



If the power is shut down during editing, the first character of the program displayed on the screen (16 lines



x 63 columns) where a character was changed or added last is replaced with the not-guaranteed area



indicating symbol"<".



Note that this replacement occurs only when "1" is set for NC optional parameter (bit) No. 16, bit 4.



Example: NC optional parameter (bit) No. 16, bit 4 = 0



Example:


#### PROO OPERATION EDIT P MOOE WHEEL100. MIN

97/07/15 14:10:00



>fi]IOOO



N100 GOO



N101 G56



N103 G41G01



N104 G03



N105



N106



N107 G01



N108 G40



N109 GOO



N110



N111



=E WHEEL100.MIN



file end



X300



X400



xsoo



Y300 S250



Z-55



X100



X200



X400



X300



t.t::l9



Y200 F100 011



Y300 10 JlOO



Y300 1-200 JO



Y200 1100 JO



Y200



2100



LINE LINE CHAR. CHAR. LINE EDIT



I NSSIT DELETE I NS8IT DELETE DELETE ERASE



NC optional parameter (bit) No. 16, bit 4 = 1



M03



PROO OPERATION EDIT P MODE WHEE



>::ls]IOOO



NlOO GOO



N101 G56



N103 G41G01



N104 G03



N105



N106



N107 GOl



N108 G40



N109 GOO



N110



N111



=E Wl-EELJOO. MIN



file end



X300



X400



xsoo



X100



97/07/15



X200



X40D



X300



Y300 S250



Z-55 M09 M03



Y200 FlOO Dl 1



Y300 ID J100



Y300 1-200 JO



Y200 1100 JO



Y200



2100



LINE LINE CHAR. CHAR. LINE EDIT



[EXTEND]



INSERT DELETE INSERT DELETE DELETE ERASE OU IT [EXTEND]


```text


                                                                                               ..''.`'.^ ..'
                                                                              .                >]_-!-l^-;---'
                                                                         ^[]+<<+~]!~,i---_???-}+l--[~?+~-__?'
           ```^`'''''''````'''''''''''''.''''''...........................```'.'`''^...'^`^``^"`'^'^``^``^^^
           ^::",^",^``,,,,,"^^^^":,,,,:"^",,,:::"""^"",::III;;::;IIIIIIIII,,::I;;;;;::;:;IIII;,:,":;II;I;:,,
           >,,i"i' !~!:ll!lll!!ll"iI!;,l!!;ii;::>:;!:l'
           ;"^I"I' ^l;^<lI;l;;I;;^I;lI^;llI<!I>^>l:!;l.
                 ><<;"!I!i;,;:~;!;l;i;"i:l:,,I<~:l'!!:!I!II>!llIll^li~l;I;Ill;;"i!;lI:;;,;,ll:";,;;I^,llI;:;.
                 ;:!-<ii<<i!><i<_i<<>!;_~<<?<_<>>]il+~!l>!ii<<>>+~;<i+<>+l<[<+!l~+<<?_<_l>Ii~il>!<~+l!<~i<~+`
                 :^l_ll>lllI!+^><<~<"!:i!_>+i~:`~><^<>~i]+>:l;,~<>~!;_+:lI:_~<_<<>:_~!"<+,l<>!]!->+l_~<l!>~_`
                .!<]!__l_;+<!+~i.,I.                                                         ..
                 ,^^^`"',^^".````''''''`.'''.'..'`..`'.'.`'..  ..' .'''  ..                 .
                .~~__:<+~I>i;I_~-?~~>_+<:<<i!<ll~-!l}<-<'II`_:-[!++:-]!;+_~<~[l+?<_~+-}~,{]_![~`,[<"]<i!
                .I^^^^^,`  ,;".^^"``^''```^`"^`.^^"'"' ."' ``'`..^      .    . '. . .... '.'  '  .' '...
                ^->-+>-->  <?l;-+~>>?l<?<_~+_]i"--_;_~^"-<,_i!l;:~

                              ":;;::,;;:"","",,,,,,,,::;:;I:,,,,;;""`^^"",::`''```^"^":"
                             I".!!|\|>|{)1+}/;,,,,,::;~j??I:,:::;l[<r\["",;>\))~-}>)[?`^l.
                            .l  '`^,:`"^,,^,:`''''^^^^^;"^'`'^""^^"^l;!_{?{?1\_)[1)1t+' ;"
                            .;  ."l'`"                                 ^""""`^.``'"'"`. :"
                            .I  ,?x?{~   :;^     .ll!'   ,ll^   ^;;^                    :"
                            .I   ^}__   .1tl     .!!i'   "i>"   !]{]   `~!^   !<:       ;,
                            .I   ,1-?'  .{[~~:   .i~>.   I!<"   !<{?   :t?`   >~;       ;,
                            .;   "1?[.  .1[!"'   ')((`   <)/i   :]:`   `<~~             l:
                            .:   ")?[.           ']_1^   >(|i   ,>?{I  '1i`             ,^
                            'I   "1]].   ;,.     '[})^   ,i~:   `;-<   '?:              ,`
                            'I   :}++.  '({,     ^1))'   :li^                           :^
                            'I   ;)]1.  '1|l     .:;;    ,!!^   :!<!                    :^
                            'I   :|~?.   ^^.                    `^""                    :^
                            `l   ,[;I                                                   :^
                            ^>                                                          :^
                            `l                                                          !"
                            ':                                                          ;`
                            ',  .-!_|{_I_<<-<                                           ;`
                            `;   i,>:~_:                                                ;`
                            `; .;l",^`^^^:"`^,":;:^"""""^^,:,:"^^,"^""^""^^^"",:"^^^^"  ;`
                            `I  `!_|,'!:i[]`^;I_1_^":>[{<'I;'''`.I;I-)^'l;[!!'"i''.'.'  ;`
                             ;". <[]-;l:{~~-l"'-{}-"^>]~+_;:]->?i^:-]}+ :;}l: .:`]+]?-l`l.
                              ^,:":I:``""::,^`::;;;,,:""",":I;,;,^":::l;,";"",,:;I""I;;,.
                               ^li+!:!;!>~<;;l;~~!I;I;_+l!;l;~-;l^l;~_I!,!l+~Ii,l!__;i
                               :!><l"<i!i+~,!~;+~>;!>:~-!li>:-];l,<:<[;i!>I~!`+!l!_{^]
                                '`'`^  ''.'`  `..'`  ^'.'^  "``^` '"``"^ `"`^"' "^^":.
                ,!";:,,:` `lI"",:""^"`""^""^,"'`,,`":' ^: ^".`. .'
                ;<i_i>><, ^~<:l-~<<>+l_+i_i_<+:l+~l;-i ;?,l~:l";^^
                              .''.   '    .  ''`''`^```  '`'`'`""`'' .'^^^"^`''`.'`````.
                            .I,,l~))_i{?]->]-:::::::;l_[<>::::::l><+1]<""":+[?_I+<l_<>^;"
                            `" '";<_!;<i<i;>i^^^^^^^^^l~l;^^^^^^^;;<]__--+]}xt[111[ff-  !.
                            ^`                                        `i!ll,,:`I::;;l". I'
                            :, .I}|[{l  ."^.     ',:"    ^",.   '^^.                    I'
                            ,,   +[}<   ,\1.     ^<~i    I<~'   +[)!   `l:.   l;`       l'
                            :,   ~]_>   :1?<<^   ^Il,   .:lI.   ~<|< . ~/~    ]~"       ;.
                            :,   ~??+   :1?!:'   I(1?   '-))`   :+;'   :~_I             ".
                            :,   ~?[+    ''      ;]}]   .+1{^   ;i-?^  "[I^             ,.
                            :,   <?1-   ."'      ;{}-    !_+`   ,~{I   "].              ;.
                            ,"   ~[[i   :1-.     I()-   .:II.                           ;.
                            ,^   +[1_   I(1`     ^!!;   .l<<'   Il!,                    ;.
                            ;"   +?-<   'I,                     :;;^                    ;.
                            :"   <~!I                                                   ;.
                            :"   ..                                                     ;.
                            "`                                                          ;.
                            ,^                                                          ;.
                            :^  `<`+_+;I+"~+l                                           i.
                            :^  "~;_<{]:;^;:^                                           l
                            :" .,:```^".   ..'.. '''''. ''''`''''```..'.'. .''''.'''''  ;
                            :` .!I]_.`,:;}!'IIi>_;.I;+?}:';^....'>ll?_'"I!+i!",:'.....  ;
                            ";  '~[]+"^i?_+i:^:][-!""]---!'"+l!<,::][[: ,!?l; ..,!!l<<^.!
                             ":"^:;;;"":l::;,":I;I:"^;::;I,:<!II,,^lIl;^,,l"^'^"IilI<+l;'
                               ^lIl;I`"Il!l;`;l!I;;';;lII;^lIilI:';;I;I:^l;l!I""!;I::'.
                               <"~+:;<i^_[;;li"_],!l!;?{'<!il[['<;!>1{`<!I~~<`<I"+}_"<
                               ";:::I^"lIl;;':IIl:I';;;lII`I;:I;;'l!l>I:`lI;:;""l!lll,












```

*Figure from page 36 (2346x3317 px)*


---



5-14-4. File Edit Starting Processing



4203-E P-247



SECTION 2 PROGRAM OPERATION



If the first data block of a file, selected for editing, is the "in-editing" symbol (see 5-14-1), the message of



"under repair of error file." is displayed.



If the file includes the "not-guaranteed area" symbol (see 5-14-3), the screen where the "not-guaranteed



area" symbol is included is displayed.



Example: File not including the "not-guaranteed area" symbol


#### PROG OPERA Tl ON EDIT P MODE

>::!ID 000



NlOO GOO X300 Y300 S250



N101 G56 Z-55



Nl03 G41G01 X400 Y200 F100



N104 G03 X500 Y300 10



N105 XlOO Y300 J-200



N106 X200 Y200 1100



Nl07 G01 X400



N108 G40 X300 Y200



Nl09 GOO 2100



N110



Nl 11



=EA.MIN



under repair of error ti le.



Please file maintenance.



LINE LINE CHAR. CHAR. LINE



INSERT DELETE INSERT DELETE DELETE ERASE



Example: File including the qnot-guaranteed area" symbol


#### PROG OPERo\TION EDIT P MOOE

>::@1000



NlOO GOO X300 Y300 S250



N101 G56 2-55



N103 G41G01 X400 Y200 F100



N104 G03 X500 Y300 10



N105 XlOO Y300 1-200



N106 X200 Y200 1100



N107 GOl X400



N108 G40 X300 Y200



N109 GOO 2100



N110



Nl 11



=EA.MIN



under repair of error file.



Please edit because abort editing in the page.



WHEEUOO. MIN



97/07/15 14:10:00



M09 M03



011



JlOO



EDIT



QUJT (EXTEND]



WHEELJOO.MIN



97/07/15 14:10:00



M09 M03



011



JlOO



LI NE LI NE CHAR. CHAR. LI NE ED IT



INSERT DELETE IN SERT DELETE DELETE , ERASE OU IT [EXTEND]


```text


                                                                                                ````.` "'''`'
                                                                              ..      .        "]-_?!- ~l+-~"
                                                                          +1_~<~~_+I+.-_[~_--_-[:<-_--?_~_+];
           .^`^``````````^```''''````''''''''''''''.......................'```..''''`...'`'`'``^.``."'^`'`^`'
           .","^^":"^",,,",:"^^^^,:,,"^"^,,,,;;;;;;:::III;:::::::::::IIIII;,:,:;IIIIII::::;;;;;;::::,;IIlII:`
           ,~^!l;I :~~I!i<i;+i!lII:<IIllIIll;
           `I`::", '`l;";l:`;I;",>",,l;l;IIii
                 li~<"!ii^l~>I^<;l>'i^;:~I :!i>i~il<i"!<+il!'>,>i::!"!>_>l!^IIlil!,IiiI;;,!::I.!I,"IllIII!"::
                 Il<~+!;+l>-<i>i<~~:_~<;i+,__<~<<~iI;`II;;;~'l",l,.:^l!!II~.I>:lll"l>>l:;"l:"l`I!I"!<><<_-:l:
                  ;;:<;.!ili^";^>:l'l+l `!"i!~;!i!i.
                 lIi;`l!^"::;;l;'I;:.,:l^:^:",:;::^;I;I,";;II;",;;,,:`;,:l I;,`,":::`"I:,,`I,"`,""'"`"""",^""
                 li~+iI<il+~~~+<!>+>,>+>>]~~i+!~++;>>i~`I_>i<<:l~<i;i^!ll_`i>i:>!<~~"i~>~~;<<<'><ii[i+>_i_~~!
                 l+i~`"+i>+i,:i:<i~l_>!,!^_i~+-ii!
                 I"^",","  ,;;'``"`"'^`:"^.;"'^"^^'``^^`""^^^```^^''`^^'`
                 <>~_<+<_^ l!?l;~~;>>>~_>?i~+i'<~><[~_<+~?--!~<+]"l]~~_~!

                              ^:::;I;I;l;,:::::::,,,,::"",::,,,:;:::,,,::"":::^""^",:",:^
                             ";.:I[\\~[|{|{~|?:::,"""",1]_i::,,,::-~//t<;;;;\jj]~)_[11l';,
                             I' .' .`.'''^^'`'..'''''''"^''''''''^^',":~{-[[]\-_{-{?\1I  I
                             ;'  ^~!:!`                                '`''.. ''`''.'`. .l
                             ;' .;f)1-^  ,<I      ;<<;   `i~!   '!!!.                   .I
                             ;'   _?]^   i/{.     ^:;^   .:l:   `[-/^   +]!   :?<`      .;
                             !`   [][l   >(--~'   !?-l   ,~+>   ^++].  .{?;   ';".      .;
                             !'   ]]{l   !]>'     +1)<   "]{?    iI""   l~?,            .I
                             l'   ][(!            i]{<   "}\[   .!_)~   ~-              .!
                             l'   ]-[I   ;+:      <1}i   .::"    "Il    ;;              'l
                             l'   ?_];   ~|-      ~{}i   ^<~i                           .,
                             l'   [_1i   !{_      .''.    `^`   '~<-'                   .;
                             l'   {++;                           . .                    'I
                             !'   iI;'                                                  .;
                             l'                                                         ';
                             ".                                                         'I
                             "   "-:!~-~                                                .;
                             ;.  i[{[:;}]~,,?:~!>~^>,>:                                 ';
                             ;.  ;I>>+'::<`<!,!>i>>i                                    ';
                             ;. `I,:"',,^^I^`;,;;I"":,:;:^^:"::,^":^";,,;;;","^:,^^``^' ':
                             I.  :i)~",:!<)l`;,_11l^`,{[],'l'^'^^^;I<1i.::?+>,.l"''``'. 'l
                             ^I`.^+__<:,~-i<<:';]-?l^"}~~<!,!?i<~"^<}_}`^"+>I` ,`>_~?]~"I^
                              .^";^",^`";",:"`,;^^"`^,""",^":""^"^^""",:^^:":;;"","^::,:'
                                !:++,!:il-_ll:ii-_:!,I>-~:l,Ii?<;;:I~->;:I;~~!I::;~_ll"
                                <;<>:il+l~_,i!<l<_"il!l~_"<lli_+,ilI+?+:!>;_i;;ll:~]liI
                                 `''`.  ` .'. .'..`  '' .^  ````^  `.'`"  ""^^^ ."``^^
                .i:;;::I,  IlI^:,:^::"^,,"`,":'"`"^",,"^"'"^^`.^'""`"
                .il~>!~<!  I!+:i!~i<<<>li+'l><I]<~i+>_+~!l~!_:^-<!<<+.

                             .::;,:::,,::,,,:,,,,:;:;::::;:::,,:;::,",,,,,":;,"""""",,,:'
                             I^ !:[\|!11))~-|I",,::::,l|-_;,,,:;;;+>j/);;;;>j|)+?1<11{^'l'
                             !  .   . '.'`'''''''``''''^'''''''''''`"";-}_{?[(i[??{{\-" ,:
                             l  ':!;:I                                 ....'.......'''  ,:
                             l  ^>/{(!   !<;     .i~~^   ,>~,   ,i>;                    ,:
                             :   .{~]    }t< .    :;;'   `;I`   ![1?   ^[+^   ~-!       ,:
                            .!   ^}+]'   ]}-]l   ._?-`   l~]:   l<]<   :{_"   ,:^       ,:
                            .l   ^}-1'   _-I.     })1,   !})!   ^_,"'  'i<~.            ,:
                            .;   ,{-1'            ??}:   !)(i   :>}1:  '(!              ,,
                            .I   "1-['   i!`     .}1{,   `I;^   ':l:   .i^              ::
                            .I   "{+}.   })!     .[{{^   ;++,                           ;;
                            .I   "{+1.   -}i      '''    .""'   :<-~                    ::
                            .I   "1>_.                            ..                    :,
                            .;   'i,:                                                   ;,
                            .;                                                          ;:
                            .I                                                          ;,
                            .I   !>I!-~!    .      .                                    :"
                            .:   ?[[~"~1-!,i+;_l>!;!I~"`''`..'.^' '''                   :"
                            ."  .iI><i^_:^^_i<!>.<_I"`~I";+:"I`<<^_?+'                  :"
                            ."  "I:;^`;"^;!"^",,;:^,:,:;,`,I,,:"`:"^,;",I,;,:^^:^^^`^^. :"
                            .I  .l-1;`IIi_1"`;;_{]:^I!}{_^:;``'"`iI!?1".I;}!i..~.`'`''. :"
                             :,' ;]+_l,"-~<il:.i]__,^!-><~:,_?>+>:,-?-~ :"-ll  i^}+-]1!^;.
                              `",:^::^":",,:^^:"",;,"l::,"`^,"^::",;,^""^";:,;,"",^`:",,.
                               '!!?>">:!i_~;llI~~~;l;I++ilIl;-]ll^!;+?;!:!;+~:>:ll+_:>.
                               ^i!~i^~l!I~_^i>l>i~:i!:>~!;ii:<?ll:<,>[I>i>;<i^~!!l+{"-`
                                `^'`". ^```^  ^'`^"  "''`^ ."`'^^ ."`'"^ `"`^"` `"^^,'











```

*Figure from page 37 (2346x3317 px)*
