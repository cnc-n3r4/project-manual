# III SECTION 2 PROGRAM OPERATION 01. LIST OF PROGRAM COMMANDS OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-01.-LIST-OF-PROGRAM-COMMANDS-OCR.PDF*

---


# SECTION 2

4203-E P-182



SECTION 2 PROGRAM OPERATION


# PROGRAM OPERATION

Thls section describes the program operation procedure and the contents of the commands used in the



program operation.



The NC unit has commands for DATE entry, initializing, program deletion, etc. in addition to reading in and



punching-put of a program tape and program editing.



In this system the file names can also be interchanged as individual programs are assigned a file name for



managing the programs.


## 1. List of Program Commands

Item Command Functions Remarks


#### Date DATE Sets the date.


#### Directory DIR Displays file directory.

Transfer* PIP Transfers program file. Sub commands provided



Edit* EDIT Edits program file. Sub commands provided



(Supplement 1)



Multi-file transfer MPIP Transfers multiple files between Sub commands provided



the NC and an external device



uslng the RS232C interface.



List* LIST Lists file contents.


#### Arrangement CONDENS Arranges the stored data.


#### Time TIME Sets the time.


#### Initializing INIT Initializes the memory, floppy

disks and other data storage de-



vices.



Deletion* DELETE Deletes the specified file.



Operation guide GD Displays the operation state of



(Supplement 2) the selected file.



Free area



FREE



Displays the free area in the



memory.


#### Renaming* RENAME Changes the specified file name.

File protection



PROTECT Prohibits writing to or renewing of



the specified file.



MS-DOS* MSDS Transfers the program files in the Sub commands provided



MS-DOS format.


```text


                                                                                               ''``.^..^ '''
                                                                          '...' .     .        +]-]i[:,~"+]_
                                                                         ,1[~<~~+[I+`!??-+-]--[>!?--~-->+~]-
           ^^^^^^^^^^"^^"""^"^'''''``^^^^^`'``'```'`'```''''''''''''''''''```'..'''`...'`'`'''^''`.`''^''```
           '`''^'^^'"`^"```:"'""""""^`^"^^^^'^``'`^',^^,"^"^^"",,^::,:":,:,"",:,::::;;;II;;::::::;II;;;I:,,"
           {/]t_1?<t]1]-})1.<1.     ^\][)+___]-~)~l{:1]i`-<~}<[_<}II_![<>>!<>I
           }j(j]\{:?lt))\|c'(j'     ;x~\|j||j/rf\j/x\JL?lr|xt+U/xrxfv{\{Y|tnvn
                                           ' .           ''    '. '  '   ^'  '
                ..
                '-i<,!~!<!!`~<<ii-><;><!l>!~i<<;:!i<l-<!:li!!!ii;i">!il+i:;ll>!li,,>liI^:;llIIl:!^^I;;:,"!I,
                ^>i<!~+>I<>!>--<i:,,`^,,;,"i;;;^^;;;,l;:^l;;IIII,l^!Il,l!::!;!i;!:;l:l!"I!l!l<>l>:I~>i;;:><i
                :>:li;l;`!!!"!l,:
                'iII:iI`;;I,II`::IlIll:>:l;,!!iil";II"`;ll;::,:`^;":::;^,I:;;":.":^ "^^,::;"^""'"^^:^`'^'^`^
                `!!<!->I>i>l>]i>><<i+~i+i><Il><<iI<i>~:>i~++~l]l!>l?<<>:l_<_~ii^i~i.II>__<_~!l~;<++_>}!!!+i+
                ,>I,!>l>il!l^!,i:i;~~Ii,^+?~">li;!I![i~i`~~_~~~
                ^,"I"`"":;":"l,`lI`^,""""'""`^"^`""^,,^`"^'`'^,`^`^`"^`"'``'`''''``.''..'''.'.'..^'.. .. '.
                ,il>i!i-<~_<I+~!!-il_i>_~I~-;~~+Ii_Ii~-i<i<<[_<l_<!>?~<-~]i+<<[<?<?!-+<>]-_]<+~i<~?<i__<_I+i
                ,i+<i?]<-I~_l!i>[i_<>!                                        .            .
                     .' '.      `.. ..     .     ..
           `      .    .  '.``           `
           {;.    ;1-rr]ltj:r/1))f/}r|/<+/[|)()|)|\1{ft]
            '      ^^^"..:' ' `":?l^l,,`':"I:,;::!!,IIl;
                  """"^"^.'``"^^' .'.''''..  .  .. '''.'^^^^^`'..   ...'````'''''...'''''''        ........
                 ^?"""",!)-]>"","",i^^>]_--]][?-""I+,::::::::,l[>+<?+__i::::::,""":i::;;;;;_[_~~~++!;;;;;;;+^
                 "[!II;":i!I,'''``"!`li+_+iii!lI``:~I,:",,`'``,Ii!>~~<_!"""`'''``':<""^^^^'l~_<~-+?l^^^^'`'-:
                 "}-_[?'   .'^^^^^,!^?__>]^.  .'``:<][?~>[-I?}}i       '```''````',i^^````'.     ..'``````'-,
                 "{__<i_~~i``""""";~^+_[l'````""^^:<~+>>~i>;+_i+_~<_<il^``'``^""""I<^^`````^",,,,","^```^^^?"
                 ,{_~<>>~>i``^^^^^;~^__?l^^````^"";<__?~+?+l!~l~~_~-_+~'``''''`^^^l~^^''..'..''`'``''... .`-^
                 :-!<_<--+"~``````:!`>_-'.''''``^^:li<+l_-<~l~>_->-<I[]I''''''``^`I_}_+I<~<~~--~[~<_~<~_+_^-^
                 "1_>[";:^","""",,Ii,-><_l^,,,,,:,I~+i-~Ii<<++<++]~;",;:^^^"::::::l<_>~Ii><~~+~>+lii!ii<<~,[^
                 "_l!i.",         ', !IlI'        ">!!><,iI>_!~;^~~,              ^;_>_:!ii>i+~<_ll~i<>-_> -^
                 I_i-<-_-__?~~:+,':!'     ......'.:;                              ""                       -`
                 ;{}<+]i[~!--+~[_;I>,]]_-~^^",",,,!>~!<!>~i!I<!~+>_I>il:ll!!!!i!::l><;!:IIIl!!!!<l;;;;Il;l,}`
                 I+l;:;^!l`:i;Ill.`: i!,l^        `;-~--{-<+Ii!-<<]~<--<![]+---l  ^;+<-:<+<<>~+i]l>>><<]_+ ?`
                 li               :l              `!__Ii<il_~~~};+_]~l<]I-+ii<l   ^"                       <'
                 l_^^"^^""""^^^^^'!<`^`^"""""^```':i_?>]~_+~I__<+-+!l-]]]{-[:..''';I````````'''''....''''''-.
                 ;[<]~Il'`''..''''li^<-]~^''`'.''':+>_]<+}iI~i~_>_~^''``'^"^"^``^`!!^"""""""`````````^""""^{.
                 l?+<i>illl;;I"^^`ll^+~_>lii!I;```I>~~~>!+<!_~i<i<<:,:::;,""^`````l;^""^^^^^^`'````'``"""""{.
                 l]?<+-[(?<-__:``'II"+<~_?}}[}?`''!<-~~]_]?<<?~:?+~]]i[1)-^^`''''';:`^``^^^^``''''''''`^^^^[.
                 ;+_<~+''.....''`';;`>-[[l'''..'''i~?+?!]]<>-i~,'``'`^^^^""^^'''``l;^"""""""""^``````'^""""[.
                 i+!i<<I;I::,:::::!I"><-+;^^"::,,"i><~~!iiiI+<_l:"^^^^'`"``"",,,,,iI``'````''`^""""^^``````[.
                 >_i<___-<[;      ,"`_?<"    .. . :>___[+~_i!+~:~-->+++"[-?~?,..''I,..........'''''''''''''?
                 <;               ""              :l+<+~:]<_;_]<~,_?]!~]<~[]_:_!. :^                       ~
                 <l...      ......:,.        .... ;l-+_-".   ' .. ..'...'.^,'.``  ;"                       ~
                 <[-+~-~iI,:`^^^^`iI,_?<i_<?I^^^^`l<__--~!;il:;;I;I>l!!<!:^``^``^^>I""",,::,^^^^^^^^^,:::::-
                 ~]+~>_~~;:l.''''`>l:-[_~~!_;`````I_-?--__l~~l>__<~]_~l[-^  ' .'`'<I^^^^^`''''''''''``````^?
                 <-+_~i+]><^-~+]<.I",]?>..  .''''';~-<__~iiI+>:!>+<_{~+:--?-;+i'^`+l"""""^``````^^`^"""""^,?
                 i<]-<-]]+<+[~<[^ :`              I<~_>_]1~+_-I][!`""^^.,:,,.".   I'                       ?
                 !]_<~<~+~~>Illi::<I;~><<i^",,:,::_-~~I<<><<?_i?->,,""","",":",:::>:^^^""^^^^":::::::"""^^,]
                 !i:!>"!ii>.      ;'^i!_<i        l~++]<-?iI+<;~>?:+~-~l>l~-I..   ;'          ........... `-
                 _;. ..    ..''```!:.     .  '''''!!<-+~~+i.           .        ..I^..........            `+
                 +?[?_]?-_-!I"''``i";}[[]?[[-'```'Ii-+<~~__I+<!!~<><]+_>?-I!<<<>^`!"^","""""""`````^^```^^:+
                 ___->+~~_-~i;,^"^_;:<++_-[-_!^^^^li~!_+}]_i><ii_<~>>~_!~_ll_>>~"`l"```^"^"""""```````````,<
                 ~~>_I<><?>+_>!,l <`"<<_i<->i+.   :~~i+__~_:-i]~<!+II<,-i+_-++<;]'!^..'''''```'''''''''''':_
                 _^       . .'.'`'<,       .. ..'.l<--,___~[-~!<]>..   .   . `^ . ~'                      "-
                 +]}}!+__}!>:,,,:,+:~[??~]I^^^^,:,<>><i>+<il<+>I<<><iil;>!!;!l<<i;?+>Il:IlllIIIli;l!lliil;I?
                 -lI:`:,,;."      I `l;l,l'       l!~[<_-_?!i~_!-i<+!<:^l>i^I"l<l !l~i!"iii>l_ii~,~i!!>-_I'_
                 ~l,:;::;::",:::::>;,,,,:,:;;;;,,,+-{[~-?_}>-?~]{~^^""",""","^``^"+"'^^"^^^^^^^^^"`'''''``I_
                  .''.''''..........'''```''''''''.  .''.'.''....'``^""^"""""^^^^^`^^""""""""","""^^^""""""'























```

*Figure from page 1 (2331x3296 px)*


---



4203-E P-183



SECTION 2 PROGRAM OPERATION



The commands indicated by an asterisk (*} are operated using the directory-selection-based file



operation screen. For the PIP command, the directory-selection-based type file operation screen is used



only for READ, PUNCH, VERIFY, and COPY commands. Basic operation using the commands indicated



above is explained below, such as the function to display the registered machining programs in batch using



the function displayed on the directory-selection-based file operation screen. For details of the functions,



refer to Section 15, "DIRECTORY-SELECTION-BASED FILE OPERATION FUNCTION".



[Supplement] 1. The file edit command is changed to the I-MAP edit command for the I-MAP



specification. For details and operation procedure of the I-MAP edit command and



sub commands, refer to I-MAP EDIT FUNCTION published separately.


## 2. For details of operation guide commands, refer to II OPERATION, Section 6, 8.

"Run Guide Display".



Details of the commands accessible in the program operation mode are explained below.



The operation to select the program operation mode before starting the command operation is used in



common to all commands. This program operation mode selection procedure is first explained; this step is



not explained for the explanation on the command operation.



Procedure to select the program operation mode:



(1) Press the EDIT AUX key.


```text


                                                                                               '"",^^^ :''"".
                                                                          '`'.`'.'.   '.....'..l-?[_~+.+;l]]"
                                                                         .]}~><_~]<>l"-__~+]--1],_++++-_<><?"
           .''''````````^^^^^^^`'`````````^``^```'''```'.''''''.''''''''''`'''.'`''`''..''``''``'`.'^'``'```.
           `,""":"^`""^"""""""":"^^^^^""::,:;":;"^^^,,::^"::^^^"^^^"^`":;:,:,::,,;,^",""":;,:,:,"^""^^^,:;::.
                 l<!^ IIlI;l;l>'^I!lIi!!`"!^ i" I!i:;!: :"^ lI^ I;;,!l;, ,;:I':iI "<::;;:,`;I!:lI,";;;:;;.i;`
                 ;!+!;+iili<><~;'<+>>?+>!>}l,_l"~_+i!<<^i<!:_~l,<+~>_+_l"<_i]!!++"!_?_><>+I_-_~~+i!>+~+~!"i_I
                 !-+<+<!~I~i<<i~'l!<:i<l<_~:_<><l~<>l:~_;<~+ii>_:!+_~!<il;>~~<~:++<"_+,>+<i<~!l">!i~~^!l:_<~I
                 li<ll<^>]i<<,:ii+-!<:'_~<+~;;"_>!;i>_l;:>!><!<l<_ "[~><"!++l~_<i^i+Iil++l:!!!!i<l~i,!~+i+<~;
                 !_>iili;i~~+iI!il>~!<!">:<Il<!_<!<il<i!;<l!_<<<<i_>l>+~<<+><i!><!+<><~l~l!<i<!!iI;!<i_;i<i<,
                 ++ii>!i_<+i_~!_<!~<l>ll_il<<+l><l!>i_<<!!l!~_><-i?>;!_-<+<!i;;!+ii;!_+<<<_-+~;~>>;>_iil<>l-:
                 ii<;<!!]<!,<<_~-+~~I~ll>+l?>+i><-:+__~>+~li__+_!l-<:+_>>[+>;!~~~~i',ii;!]<+-!:!l<+I<>l~i!!i.
                 l+-~,_"~-+?<+""_:.++~{_iI><+~!l}-i-~!!>>->>?_-}+~;~+<<:+_?_-+_~<~]i~!]-~!i<~]l
                 ..              .   .   .                  .       ..     .    ..   .
                 -[_-_]_<++_~    !'  <<+^I?l'~__^i<>~>~<>;:<.>i~ii_<,;i'[~I`!?_~<.<>]":i!!!!~li`<l.!~i';_-+_^
                 '.`^`''.''.`    .  .!>~!<~l>+!l ><<:<~+>i;<;>;~<-~_i!l,>i!l!<li:;~+~I;_?~_i>i]:l!;i><l!>>>>,
                                    .++~i<i<+~i!"l;!;_~>~il~_~>]-->?-<<>_<~_+~<~;i;>+<;>->~,l<-!!ii!;ii!li!i,
                                    .ili^!!III<ii~: >i~^I!`,+i+I"~!!;`l;i~i":l!~;i!~i<><i^>_~+!<-i~
                                .~' '>:;'>!!i>';I^i!;l<il^;>I<<'IlllI!II~".!><:"i^-::<<~<~<ii!~i ><!<il"!;"<
                                .:' '<-l;i-++-!i+>-_+~_l;^!<I!!^;I:;:lI;>;'ll!,^l^i",l,!;Il::;l!'Iili!l";;"!
                                     "!lI'I!l!<`ll<i<~'
                .i+--+~:_![~Il<i<><_i<l:_i>>><~~Il!I~>:~!i+<_>,i<~i~_ii,<>i?ll<>,<><++i<<!><<i~^
                 ",^"^`.^.^^'`"`^`""`""':"","""""^^'^,^;`:!":^'";"^:,"^'^",:`","'::;::^,:`::"";
                 i>+"I+~i>_ii">^;++i~,<-i:i!<>>~;'~~~l+<i,'i!!_"l>~IlI"~i!~I!"~i,,lIllI<;!'i!iI+i!l^>`l!!>I<'
                 Il>ii>>I<;i~;i>!<i_i<~`;-i><+i>ii-iI><<i~!il!~!~~;<ii!-<il>+!i~<!<!>i-_~!!+_-_~>+Ii_!!_+~;~`
                 i<>!>><i<i<i!<!<>!>i>~I:!>~>!;+<++;:~><i~>>!I!<<>!-!>Ill::l,;IlIl;:;;;;l,!!l!i:!!,;l!,!!>,l`
                 :l;,l~l<;!!;"!'Ill`>!l~i!+!l",!^!lI"!!;I!<l~;><<!+<il'
                .l:;;;;,":^I';:l,::!:^,",:";:`"::",l:,',,":"
                .;"li>lI;l">^!i!ll:!<,>;!+I~l"l-~!<~>i,!>i~>'
                  `"  .;^`^."^'`;",: ;'"^``'                                                ......
                  li, ,!i++!l<>l~i>!"+>>!i+?l                                             '<!<III:!"
                                                                                          ^-`";>:"!I
                                                                                          ^I l<;"^I;
                                                                                          `)[~~:{[}^
                                                                                           ";:"";;,















































```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-184



SECTION 2 PROGRAM OPERATION



(2) The lamp at the upper left comer in the key lights and the screen changes to the program



operation screen. The function names also change as indicated below.



DATE



01R



PIP



EDIT



~~r,



LIST lcoNDENS



(EXTEND]



@ @J @J



@ @) @----.



BLANK RUN



TI ME IN IT DELETE RENAME DEF I NE FREE OU I DE [EXTEND]



PROTEC~ MS-DOS



DNC-A



DNC-B [EXTEND]



These commands are explained below.



The keys change in



this order when



[F8] (EXTEND) is



pressed.


```text


                                                                                              .^""^', ,''^^'
                                                                         .'..`'... . ''... .  "-?-?>_.+;l-]I
                                                                         ~1~<<+_+_I<.-_]+--?-?[:>++-+-_+~~[;
          .^^^^`''```````^^^^^`^````'`^`^``^`''''''````'''''''''''''''''.'`''..'''`''..'`'`'`'`'`''`'''.''''
          '::::,"^^^,,"^^,"""",""^^^^"",":,",,"^"^^:::,","^""`^^^"",,:,,,"""""","^",:::;,,""^",::::::;:,,,:`
                 ,+l  i!!"I!;l`!:>!:^i!I!'l<l";I:l:",^!;^I;:"!llI';;l:!:^";;;;:'II;::ll^I^lI:^;,::;I:
                 "l:  ll+l<-!?:~!><<l>+]_:<+!l_<l<!l!I><:~+~,-[i~:<!<!i<l~~<++i;~+_>-+<:i:;i!IiI_<>>l.
                      i>>l<>!>"!!!><I .li<:<i!~i!,;+<!+<,-~>"ll_i~-:i~"i<_l~<<;!++l~;
                ..                                                                   .
                l,                                                                  ^:
                !:                                                                  ^:
                !:                                                                  ^:
                !:   ".                                                             ^,
                I"  ^I"^^^,>:"^^^::!:,,,,:;I,"^^^^:":l:lI^l,^^^^^^!",:::::I"^,::::  ^,
                ;"   .'`'  >' ''` .i .`'' ^l `''' ;'?/<i; ~`  .`. _.'''''^!.'.'.... ^:
                'l^  <?><  , .<l~  I "ii; ^: ]_!: ,'ll~'  >.,II-^ ~~?11[1i,`]]__}?l`!`
                 .::",:",;,:""^"";,:,:^`^^^"^^^`^^:,:"^""^,^^^^""",,^`'`'^^^","::II;'
                    ^i>_~li`Il><~i!`il<il!":i<>iIi`!!~+ii:'iI>iIi",ii<~!!`l!>>i!;.
                    i;;_i lI_'_~_ _li"?-I:~>`~~{ +;~.?[>.~;!,](::~>`_i+ ]l~'_}-.{^^",,I'
                    'lI:IIl'"l;llI;.ll;!l!`^lI;Ill.I;:I!l,.lI;l;l`"l::;I!.IlI!!l:     :^
                 .                                                                    :`''
                ':                                                                  ,""'!-~i~-l>-~__!<
                ';                                                                  ,""'<[~;][_<}[[:'
                `l   .:l'                                                           ;,:`+_]<}-Ii!<!:l
                `I   :~<`                                                           ;^!"i;lill
                `I  ^;,'^"";:"""^^"l"^""":;l,,"""^:,:,,I;:;:"^^^^^;^:",,,:;"^^",:,  ;';^
                `I    ..'. !; ...' >'.  ''':'`'.'';"-+-)~.!^... ..<`]][ ."!.. .     :!l'
                 I^  ,;[\' ," !-;, :"]>>~?`.~)][\~^^i}<:[i:.`-?[: < ]~I[;.;`?+~?1[!.!i"
                  ":"^`^^^'"`""""``"`"^"^^^^`^^,:",^",`^,""```:I,^,`:,^:^^^`:::IIlI:'
                    "ii~iI!'Il<>>i;`!li!Ii`:!<ill!`!I!<i!^`!liili^:!l!>!l'li!!l!"
                    >,!+~ >I-.?_+ ~i!l_]"!!>'-_[ +I+`]}!^<I;!-1`!!_'?>~ ]Ii,-1<^]^"""";.
                    ^!;;lll';lI!!I:'llIill':l::;;;'llI!!l"'l;:I;!`:llllIl'!;:IIl:     !'
                ..                                                                    l'
                ;"                                                                  `,;'
                ;"   ',:                                                            ^:;'
                I:   l(1.                                                           "I;'
                I:   l>I                                                            ";;'
                ;" .:<:":::l;::::::l:"^^^^,:"^^^",;:""^^^^:"^""",,;^^^^^^^I,::,,,". ^^;'
                ;"  . ..'..i^.. ...l..    `"     .;,......!`......~......^+.. .     `il.
                `l'  ~}?>_>~"t~l[[:".?)!i! '^{};]:^^      i'      !      'i.-_>-}]I l~"
                 ';:"",:":",,;:,:;,,^:,"","^`,"^,`""^^^^`':``'``'^:`'''``,;"ll:;lil;^
                    `!!iili`:>>>iil`!l!!!i""illll!`li<>l!:'!l!!Ii"">iiil!^li!!!!:..
                    ;I:?> !i>`_+? ~;<"?_!"_i^~+{ ~;~'][~.>:<^_(;:~!^_>~ _;~'?[?.[
                    `!I,::I`^;;I!:: ;I;III`'I:"l:;.;:;;I;:.!;:!!!,"!lIl;i`!;;!ill
                     '>!>!l^;!ilIi!I<"!il,!Il!i;!I,I>!!l
                     .":l;l^;I;::!l;i"ll;,i!Il!:!I"lil!!




































```

*Figure from page 3 (2346x3317 px)*
