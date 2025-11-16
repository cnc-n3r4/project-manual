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


                                                                                               '^``'`..^.`''
                                                                '`''^'.'.. ...'. . '. ' . ...  _-_-i-;^~;]-_.
                                                               `[]+<~-~-i~,;--~_!_}[<>~<_~<<_>~I:-__+-?>><+-'
           ^"^^^""",","",,""^^^````^^^^^^`^`^^`^^^````''''''```'''''.'''''.'''''`'`'''.''`''.``..'.'''`''``^
           .'..``,"^,`^"'''"^.^"^"",,^^^'^```^:"^^^''`,```"'""",^`^'``"^``,^^^^""","",^,``":::,:",:,,:;IIII:
           }r?n])]~t])[]1\1'!\'     '|[l|<1_[] <)[~11],~]},_<+<"+[~[-+^<?- i~i-?<-!-_.+:_+iIiI>;"
           _f}f-1};[l|{{)(r'~n"     "n)\f){}fn^]vxjx?1\{_(lt1tjt?|+Y[/\}1} j1rX1jz(zx\X/t}rr)nuJ_
                                                      '     `  `      ^     ^    ''  ^ '.  .,  '.
                   . .  ...  .          .   ..   .  .               .

           -!.     \|(?^/[+_++~~-~?"<_<~>l[i]?i>+ii;_^{<;llli_ill,:!!I!l::'>-__":<i>!_";_""",,^:;'+l"`''''.
           ;l`     ~-~l !l<]{x-+)_};i-1f[[1~??{11/{[}:]!1]?)[))(}_l)[\1{1U<[c\f__)())x>_]}\})\(u|;\?\\rjr(/
                  .))1{\]                                                '                           .^'`'^
                   !ll~>i                                                         .
                .,^  ^^ '"",^^''''`.`^.'...'.. .. ..                     .
                .!<~:[-i~~!~ll~!!~-:++,<_~~]~I;-<]?--ll++~!<<_:<<?+<l!<l[~,+?~;><>?~<>_l;+_<+l{[>>_~]ii~~i+~
                ,>>i<i_l><-_+:>-__!              .  .  ... . . .'``'... .'.``'.^'':``'`'`"^^I'^``^^`^`'"^^:"
                .'..'`'  .^`^''''.'
                 'ii  +>i<iii;;<>i!;<iI;i~<il"ii!!;_>;lllI<lI^l^IIlIl!l^I!!^!I,IIi:;:,^:i!,:l;l":"""";".
                 '^"  `'"!;:,'`;I;"":,`':Il;^'I;,>^lI:^l:;l;".!:<!iili>^>il"l>I;<<!<!i_I_<l!>i~I!<!!<_<.
                      ''<I!,l>!"+<<:i>i~i^l~i>"l_>>:<-!l<<,<-~
                      ..;;;,:;:"il!"IIlll^I!II";l;!,l>!,:;^:II.
                      '.!ll!!!l:~>_,>i<i~,i~<>I;,;_I!?+>
                      ''ilI;li;,+!~,>>iIi^lii!,:,:<Il~+l
                      .'I;::;I,"iIi^l!i;!^I!!l,:",i:I<<I
                      ``~>!l<~!I-<-;~~__~,<__<:l:I-!~1}>
                 .                   .'''....'         .
                i}i_+_?<~_~['   ;;  :}?-I-~+],<l>li__?>>~+<;_!?+:_]i!i<i];<il<i!~+!i^
                '..``.'.''.`         . . ...' '''..^`^'.^^'.`.^^.`^"'^"^".`"^:"`::,"'
                                iI  +<li:II;l;i";li"+Il!,`i!l^;l,;l`:III^I,:";I!;^""^l^:"lii^llI!^",,:";I;;"
                                ^`  l<><lli+Ii<!!i>!>l-~_l<!<l<_!l+li_]+<<<Ii+i_+ii~l-!?I<+<i~>>_!ii<_~___?!
                                    >~i!+l<i;>>!<ii~;'!,!<_^l~:l~,>!<ii<_"~^:><>"_!>"<!_lI!"~<"!>_:I+~>+;<>;
                                    <>I>_ii <^l-'l~i<-- ~:`<-^ll.--+<]l <i<'l<>~+i>+~-'!>.~i->+~+-II}?i~-<]i
                                    >]+>?ii<                . .. .^`.'. '.' .''.''.'',.''.^`^'`'^^..^`''``^'
                                    .'''"^`^.
          ';'!    "i!;I:!>;;:^iI,;:":,,"
          .;`l'   ^i_i~!__>i!^>!>+>!i_+<
                I!:':I;',",:`:'^`"'`,'^'^^:^^'"^,`""^'"^'.`'`'^^''.^'.'''.^...'`..^..'...
                :!<Ii~~;iii~;~l!i?I!<;>+ii~<!,<>~i_--li~>,[++<[->:,>l!?<~l]l:!!+_;]+--~[__I<[<]<;--_++.
                                         .``^`''.'...'.'`       '^`       '''''.''.'````'. ''       ..
                                         l,`.......  .'^:l`^""^`i>i``````~l``''''''..'`^"!
                                         I' ;;,""^"lI"` ^I.'```'...''''''<" ,l!I!l:><>!  I
                                         ;. IlI;;II>i:, "<''.  .   .   .."" l??:``.`::,  ;
                                         ;`'       ....':-:,,^^^>-!^^^^":>:.''`....    ..l
                                         '``^^^^^`^^""``^       :I^       '`^^^"::"""""^^^
                                                 ,++::>;^"_<+>~-!!,<<i<!ii<^
                                                 ..;"'^'.'"::",:,"`""::"":;'
                  .     .
                 i~; "i"-i;<!!?~<i:;_<>~?+<";ii~+.i<+I!>!<><!<;I<<Il?~+:>-<,~+_;l_>>>l;;!~i:+~:Illllll"ll;
                 '.. "<i<~<<~l+!]~>>_;_+_;!><<i~_!I<<ii;i?<<!~i>I,`^:";'`:"':;;",I;:;"^^";I^;;`":I,;I!"lI;
                     ',;,,:'"^``^;l;I.::;.,l;I!^,l':Ii;^I;,::!;l'
                 l<` ^;`l;'":,:";,.'":"";,".^^';" `",^`^`^^^``.."""^;^"'::,."""''^``^^^'"^'^"'''..^''.''.
                 l>^ "<l<~l<~i{<+<!>++><->>:l!>?+^~-+l~!i]<_i<li~>!i<!_,i~!,+--Ii?++-!~:<-<l?__-i;]+>;_+:
                     ,>_~~~I>:>~>:?<"I>~>>>~"i~>_<~<i,>~+I;>i<<<_<_`
                                                       ... .   ....
          I,<+    +}~__~[~~<_:]-{i!-+<[!<~~~"-<<i><<"
          '',,    ^lI;;::l":~':,:"`,,,;^``:!.;l<Ili>^
               `]-i;<l<lI_I`i<;l!^Il;^!lll<;l"I`l:^`ll,,l;;l;"!;;;I
                ;,,,:":"'I;.ll";I^:::^!;;:::;^;^,l;:><!:l;!iI,<il!>.
                     Ii>_" +~__!l;<+<!i_i>__;i_<+.
                     ^<[l^ Ili!l_{<!}<l>I!ii!>1(+^         .
                      `^         ''^i'         ^'
                     :_+<~~l!+~i~.         >_>>i<ii' '~!<"l>!iI
                     .^"^^"`'"^`,          IlIiii!~  .^^I'"I";:
                                          .+<]<^i~I~i
                                            .'. .` `^
               "}<>~__<i<>?,   ^I  '_!l'l!l!;i":!!!,.!';:'!ll!^i";il'I!!IIi!^;llII;I:'>I;;I::',:;:;;.lI,',:
               ',"::,,"^,^:'   .`  :<~<;<<!l<+:!+<<l":,!iIii<i:_l:i~;++<i;i>`:>l!!ii;^~iii>!>";>il~<`_i<^^:
                                   :iiii>I~,!i:I<ll<>"~<I+:I~i,i<^l!<+_~>
                               '^  .'. . '.'...'` .  .      .     .      .         .   .       . ...
                               ;<  ;i<Il~!!<i>>?]!I+<<_++~~I<;>+?~>_;~!_i<<~:_->-I<-~-!i__>-]<~<->I}_~i_>i<
                                   ;>,_~++i-_:+,l~_~_["i<+I+i;{[<i+~?i!+~>'.  . . . ..  .....'" .. .''.``.'
                                   .`'^^^^'^^.^'`""^`,'^`".^^."^^^"^"^',::









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


                                                                                               '^^^.^'.,.^^^
                                                                .'..'... . ..... ..' .. . ..' ._--]>?I"~;?-_.
                                                               `]}_i>~+[l~,I_-~-l-}-<<~<-+i~+<<l:_+?<-_~<<__.
           '''''`````````````'''''''''``'`''''''''''''''''''''''``''.'`''`''`...'.'.'''`'`''.`'.'`..'''''`''
           ","",,",,","",",,::,,"'"""^,,;,"`""`^^`^,^"",,:"""::::::;:,::::;:,""""^^",:::::::;:^^"^",,:;:;;:"
                .+i;!li!;!li:   '>  .!Il'lli"^i;;<I I,III.lI;"Il,;"`Il::;,.:I;;::;i;":I;I;!!:':;:;;'":^;^^,;'
                'lIlilll"!;I:   'l. '!i~:<+->l~~??i,+Ii>i'>ii!<iI>;.!<ll>l`l~;!!>>~I;I~!<>i>i`l<!<!.;l!~;:i>'
                                    "~ii~<<;+i^>I<!~~_!i
                                 '  .^          ..     .   ..  .  .  .        .' .
                                ^_. ^~<-:-~-[~:]>_->~?]~Ii-~<+;~i?_I~?l-~~?_~:_I;-+]~_~->>.
                                     .   . .        .     .     ..       .  .
                                :]  '~>>!]~:i+!+I!>i<<_+,_l!;~~+,-_Il~>~>:~<<,<;>~<>>!lII+l>{>,<<~!<ii>i-<i>.
                                 .  ^il!:+;!>_!!ii>:!<<>!;i++Ii;li<!!!li;ii!+i;i!~i><~<!><i_:l!!liI>~i<~lI;<.
                                    ^<!!i~l!ii_i~i<ll_<>~l+<>l<II<~il<_I,<!-_I;!llli+><<>iI<l~i<i!!+<!<>^`^~'
                                    ^i~>>l-:>I-+<!~~lI~~~~~i;l><:i~<Il]>;<+!>:~Iil>~~!<!!! `~ill+!"i~!+:!-<~.
                                    ^ii~!`:+?I^l"<_-:'<^~<;`-_>!_<]">!>,!~i^_i_<_i_<>"_~-,--+<<"!,~_:,~~+`~+.
                                    :<~_>i<?i`~--<<Ii!~<!;_i_+-~?;,,,~l,;"'.'.`'`'`''..`` '````.'.^^.'^',.^"
                                    '":`,,:;:',:;,,`:^^:,^I:,,I;I^ . I` ..
           ,.,^   .:"`^```'`'"^''^'
           i"_>   ._~-_~_<[[i]l>>}I
                .,`..'. .. ....'. '. ...'`..`. '`^.````.' .. ..'.'   .
                '<~+I-+"-li~~~i__i]l;_++i<_:~+!i]?!<~>?I<<><-li_ll<!<_~~,+~ii[>+<;_-~>_.
                   ''''`. '.````````..    .. '`.''`'.'.''`'`^````'`'''.. ...``''. ...'`''''''''''''.........
                  ~"""""}[__:::::<;;_<+<~~-+-;,-,,:,""""":::::::::""""-~~__-+~>?+1?<<""",:::::::;;;:"""":;;<!
                  +""^",<+ii"^^``i""<~_l!>_i~:,]:"``^`'^""",::"^^^^^^`lI~~+~~iI>i+>i<```^""^""""`'''````^^^<+
                  -?-~--->+^'`'`'!":-]-. '.'.'^-~-[[?]]ii{l[}[<?~~[![+i_[:___+]<~l   ...'''`''.'...'....'^^>~
                 .]i<~~~~<~:'````i":<i<_~:""^`^>>ii~i<!]+~I~!i!l_-il~>?+_<~<<~i>!+~_>liii!>;iIl,III,;I;II"^<~
                 .]<<_--i?<`"^```i,I_+-i>,""``^>><~_--l-?-l~>>i:__<<~>-<>~<!+~I>:i~]ll-~+-[l[i+;~~+,~[_[?,^<~
                 .]-[~<-~~i[_`'`'!"l}]+[-}{}^'`>!<__!<+;_<}>__,?~_<???<_-iI++i~_:i:]?>>1}l-?<]!-~i>-<''''^^ii
                  ]+~ii+!!i!`'^""_:;_]!~+~_;```i!<~~~<>;<>+<_!i_-+?<+__>>lIi_>i~-?<+?+_+~!>i!>:;lII!l,",^``!!
                 ._<+~+~<<l.`""""+:I]-I~~<-"``"<<+??+i!,?_~_<:[~_<-_+!i~_lII~+~l[-<!_>_!i-~!__`...'..'.  ''l!
                 .~-_<!>_i_->`^^`>^;_]{]~. '''"++~]__}?_l]_;!-~_++_~+l_->~~+I!_-~++}I>I+_>!}[i-}?{___+_-?^`<>
                 .<l-?++__;"`    I.   ''.      < '`'`^^^'`"..`'^^'^"I.^,'^^"^`":",^;`..^"^.""'``'^'.^'^::  l>
                 .--]]~+~?<Ii!!!:<,;>ill!+<<~;I[>I":;:;",;:lIl;::I"^^:,^,:II::,;,""""I:",ll::;;;I::;:,^``""+>
                 .]ll~:~i<_<_<<i'I :<~+>!-~i>  >__-[[[[_;}__?-!]i?_Ii~-~<_{?~i;?l-_?~[]?!~?-><i>]-l{]+`.   !>
                 '?           '''i^    .  .'.`">>-+-!~i!+?<..  '              .  ..                    ....i>
                 '[_~!~~_-i~-!""^>^!{i`^`^"",":<-~i>>><;Ii~i>>}<~<;iiiii<!![~~;~~I!>i!l<l>!!-<l-?_!_+~~^^"^<!
                 ']>i[]:::`^"`   !.`;`         l<><[-1]~i-]+~i>___>->{)-<~<??_i_>+~{~]+??i-~][<_~~>~>+],.  ;I
                 '?;:;           i.            ;i~<_?<l!,,;!ii^I;!^,",!!`:i:,IlI`iil'>li>'<<lilll;il, l:   II
                 ']^^''^`^,,",,,,-;,:^""^^^^^":~~<+?_;   ....'^'''''`.  . .'..'``.''`    .    ..`'.``^'`^^'iI
                 '-++~]<]-l>--:''i`l[_+!.'...'"~-[~-!i-+]+-_!_)]<!]_I<+{__<_>-~i{]!_~_~~i<:--};_l+]l}[}"`^'<!
                 .~-<]>.'. .'.   :  .'        '~<<+]!?<i_]]+~I-~+~-,-?[I'+:>+-i<^]+^~Ii-+->-~<^+i+I-+l:>I' i!
                 .<^'.           ;.           '<>-<~~<i-?<]~!_<][_>_>[]I!+<?-_-_;i]!+>?]i+_-]~:+i[>+<?!-I  i!
                 '_IlI,ll!!;!;l"`i^,l,;!^``^^,;_i+>!il;i!:<ii]>_+>>i":!:l!~lI!i<~!<!;l!!:l;;l!;i<+~iIi+~l:,_l
                 .[{)?>[][[i{]1I">"<1]?+"^^^"":~+-}}___!}]~_{]+?--1!^`.''..'``````'```..''''''`'''``^```^""~I
                `::^^",":::;:;"II!;;;::,,":::IIl;II;:!::;,",,:::;:;:;:;,,,;::;;;::;;;:;:,,:,,,:Ill;;;;;;;;;I.
                ^>>i,><i<>_<><:>i+!+-<I!-"~<^-_~<i_I,>`~~i:~><!<+>l:<"><l:+<+i>ii"~+~>-~>:<+-_~i;+i^_<<!_<>I
                :i!i<+, Ii~:!++l~~>il~><_!<?ii^<~!~l!>~+!^>~i!!~+!>,:l^!+iiI<!>ii"il!i!~i!+" <;Ii~-<ii">:><i
                l+<~<:!~l!ii<i>:<<>-:<++<>:>_>l~l<<:I<>>!!;>i!>->i!,ii!i_!~l+i!<il!~!l!-,~+i;<;l-<I!i!l+!l<i
                :<<~l:!>>i!i_~i;->i>l!+Il-;;i~<!i~ll>_!!~<I>+i~<Il>!!<<l~i-!><:i!>>!>i!<,~<?i<<I<i:!+~~~<!~!
                i_>;!il+<~<:l-_!I;l>-<>'';i:;+>__!,>l>~;!i<<~il<'!~-l:_"~_>-<i:+.I_^'<~<_><li:_-~i+~~:!<_++<
                !i-!I--+i-_<!;i<<>+i>,
                '^``'",`'^"``^.''''^`.'.`.'..`...`...'....
                ;~--i_-<i:_i:-_:i>>~>_-!]I><l}~<>++?iI_-<~~
                ^;^`^.`" "^"^'^`.``^```^^, ^`'.^`'''^^"`.^."^'^::`""",```'^` `^'.'''''^''..' '''''.'^"``^^"`
                I?!i-,_<^_;~<~~i;+><<<->~?,_+!;+<+><+?+-,~^>+iI]-!<~>?l!<>-]`!_+"+i>><-ii>"~"__ll<~;{]<<?<+~
                ,Il<?:i"~>+_->~~i?>< I+~+~++~<~,i>~~<I>~_i+>~<;ii>i<~l_~:~;-i<i,-+<>>~<+I+<_!]+;][_I~~+-!>~l
                !~~+!;_-"'`'`.'' .''..'''`.^'''.'.'''.'''''`^''`''''`'``.`^"'^''^^^^'``:^'^^.`^'`^`'````'`"`
                ^:",.'::
                i~iii>>l~l;+-<;~;i-<>-~;]{>i?<-~:_~~<_<~;l<!~-:
                '.'^"^``'..^`' '.'"`.'^ ^`..''`. :"``^^^ '^`",.
                 ,!:  <IlI;"~!,<>!!"l<l~^IlI~:,i>lI<lI"!l::I`Il>llI<!,><<!<;:~>>>>>~!!ii.  `^^.''^.
                 ^"^ .ll<_~";I^::,^'";::^,;;!,,!Il;!l:^lll"l^ll!I:,Il"",I;l:"!,Il;ll:I;l. >!!ll;,`i
                      I!i~<.                                                              +`'Iil",l
                                                                                          <"^<l:;"~
                                                                                          >1+i;>1{~
                                                                                            ......















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


                                                                                               `^^`', ^''`^'
                                                               ..'.''.'.   . ..  ..' '.   ... "?]_-i] ~I~?}i
                                                               i[]<<+~_[I_'_+-~+l]{<!+~~?~i]~>~">++?<-_>~>?!
           '``````^`''`````````''''''''````''''''''''''''''''..''''......'.''''''.. `..''`.. `. `'.^'``''`''
          ."",::::"",,^^`^":,":"^^^``^",,::^``,,,,,",",::,,"^:II;I;I:,::,":,;IIII;,:,:;IIIII:,:::;I;I;;I;::^
                 `~!  >il!!">l,IIll>II,!!,;<+i"~l!i<!<!,:l;;I
                 ^l;  "";ll";l,,l;IlI;"!>ll;i>:>;;:!;>l;,il!i'
                        .                                                                   '.
                        !^                                                                  :"
                        !^                                                                  :"
                        ;'                                                                  l:
                        ;'   ;.                                                             :^
                        I' .^;``^^^!,"```^:l,,"",,;;,"""",!,!<!<l:i:::^^";i::::::I;":,,,,"  :^
                        l`   '`^'  !  '`' `I .''. ^^ `''' i'](<l: i   '' '!.''''',:.. .   . ;^
                        `l`  -?~<  l ,+_i `l ;!<" ^`.}+!: l'l;~   l ::~_..<+?({[1l^;[?<}|[;`!.
                         .,:,'```^`^'``'`^`"""^^^```^""""":^^^'^"":"::"^`^^^^"""":`^"^^::II:.
                            `!i+<l!`;l!i>!l'iIi!;l""!li!;i'I!<+!l;'il!i!i""i!iil!'I!>i!!:
                            lII-~ ii]`~+] ~l~^-+!"+i">_) <l-.+[+._:>:[)I;_>"+>+ -I~'_[_.-
                            'lI,;Il',!lllI;.IlI!ll^^!;:;:l';lII!;" ;:",;I``I;:;,l ::l-!l;
                                                               .!i<!;<-;<>!<~<>I!>!!ii
                                                              .`"Il!ll>;lI:;l!!li>!l.
                      ii!"l:;I!I:"I!IIl^,;,lI":;;;;;`;I",I::,;^:^^:`^" ""^"'^.":^' ::',:"""
                      ',!`:I:l!I,^Ii;!i^:I^,l,IlI!!I^i;^Ilii~_:!l:<!i~:]<><:l:!?>;"+<^~+!<<.
                 ^!, .l"^,^`:^."^^",`''"^ I;,`',,^^:"":.
                 ;_! 'iI-[>I<~;<<!~_>II~-I?i-!!-<>i~><]!                                    ';
                        .^                                                                  `I
                        `^   '!!I;                                                          `;
                        ^" .:;1]_~                                                          ^l
                        ^, "[i,^'.^,"^^"""";,^^^^^^"",,,,"""``^"^`"^"""^^`""""""^^,","^^^". `:
                        ", ;^.''`'.l^ . ...!'.....':......:;...''.l"'`''''!`````'"+`'.   .  ^I
                        'l'l i[?i?<~.\]![]I"       ':{}:?'`"      :'      <      '!'>ii<~~; I:
                         'i<"^^:^,":,"^^,"":^````.`"`,:":`,,''''``;^...''';..'''.`,^>>ll~->;;
                          ;^';!l!l!"^!ll!!!`:ii>!!,'lll!!i^^!II;il^:!llli,'l;I!i!`"i;;:I"'`.
                          l .i'[<,'<I;<??`i;+']~-'-:!:-[l:ii"i]}.~`_`?[-'_;l;[~"!ii^--1'-`
                         ": '>l>llll,ii>[;i^l;!l<"!'I;!>ll,;lIl+;>'i;i>~:<"ili!:i;l;!l_,~'
                         I'   . .''  .''_! .;II;:i:`I>;,ll: '...'   ''..'  .'''`.  '.. `
                        .l ,;I:;"        ^^;~+_<i>+!+_i!~_]l
                        ,, ,_i!!, ^i!-_<+i~`
                        ;I:^:``'`"":;l!;I::".

                     .:^''`''`''....'.. ...`.  .. .. .' .' .      ...    .. ..    .
                     .><~I__++~~II?_<__:~~l__I_~~+_!I?<,~<-~?]:++I~~[<]_?!~i+-~;_[_>
                                                            '.                . .^
                       .;                                                                   !
                       .I    `^                                                             >
                       'l   "{/<;.                                                          I
                       `>   ^?]_-'                                                          I
                       `i  `I:''.^",^^^"::;:::::,":^"^^"^",^,,"^^^"""^",":"'`^^^`^^^^",,,'  I
                       '!  .   .'.":.  .''!"     .l;<i-; `I..   ."~!!_: .I;\?!1)!:`  ..     l
                        l`  !+-:  :: ~?_I ;"{?]{|",:1+-++"; >}}+ '!-?_?>>;',[<<l.!._~><-+I ^l
                        .::",:;"``,,':;,"`:":;;ll^""!;lIl::.";;:'":IiIll:,' !I"'.;`<<!l>~>;I.
                          .'^l;!!i:.;;:I!!^^I::,::',;,,;l"'l;;Ill`^!;I,;,.,!:lIl^'l:::;,.''
                            <`?~i.~:<^]-l"!!"+~?'~:<`[-+'<;!,?):l:i"~[{'_;+^[+i^_:;i_{^il
                            ll>;!Ii"<li+i!;Il<!_;<"i;!i~;i"ili~;!"Ilii-:~">;!;:;i"li!-;>:
                                 .    .         '   '.''`  .`'.'.  '''.`   `.''`  '``'`'
                     "<i><I>l!!!l;:_!_^+~>!>>~~i'
                     '^":l"^,",":"`;^!`I,:`",II;'
                     "_<i:>!!_<<";~>!i!`i:l~i`i!!><,I__:>i~i><"~!"l>>>_<<!i:i~i"li~<'
                      '^"."^",,,'`::":"`:^`,:`;,"::'^;,^,"I,>I`l:'"::;lII":",II`:>i;.
                       .`                                                                  .^
                       ^:   :]-'                                                           ':
                       ^,   Ijt}?.                                                         `I
                       `"   ;1{"'                                                          ^!
                       '^  ';`.    .....  '''''''`````'''..'''''....'''''.       ........  "i
                       ""  `_[+]-[1<]-?-[[<````^^,!","^``:;``^""`i:^"""""<l]l!__;i^'```''  ">
                       `;   "i1{?[_,~?[]]?!       "      ,,      !^      l"]_<]~^; :","::^ "l
                        ,;^' ^-i!``.I<Ill";'   ..'^. ....,"      ;^     .; `-;;..,`-_><}1<,l.
                         .^",l""":^`""^^,:^,I",,l,^";"";l"`::,,;:,,I,",;,":I`^^,^";^^^:,^""
                            i:?+I,!,>;+_;!"i:<i<"<"<:+~l:I;l>?-,i'i;~-+:~^il-~!l;;I<_?;<^
                           .+^+!l^_l>;<[,I:_"~i]`-I~"~->"<>;i<}`>,~^~-}'[;>,~i";<i,<<).+:
                            `;^:;;' :;,:;: ';:::;` ":^":;. ::,,:" ':,,,;^ ,;,"";..;,,,;"

                     I_>i,>~><<]i_+:_<;!<~>_<i<>!~~>_;
                      .^"'""^^"I",,`:"`":I";"":"";,";^








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


                                                                                               .^^^^'^ "'^^^'
                                                                .'''''.'. . . .'. ..' '... ''. I]?-_i_ <I_]<"
                                                                i1-<i~<+]I+.~+-~+l][<>>>++><_~>>^>_~-+-_<~~?;
            ````````^^^^```''``````````'''''''''''''''''...'''''''''..'..''.'''.''.' ' .''`...`..`. '.''.'''.
           .^"`,:::,"""",^^^'``"",,:;;:,,"";;;;;;;;;;;;;,",;;;;;;;;:::::::,::IIIIIII;,:::,:III;II;,:,:,,::;I^
           .!'~'   "_<?>^><lil<!l;l'
            :^i"   'ilI,">l:<!i>!><'
                 ,>;"`:::;::'"^.,::::,^!;;lI`,";;^,;II";!;:`;,,`l,:,;,::"`:"":,""':^"ll";::I`,^"^,^,^^"^.":,'
                 "~+_!<i!!ii"ll:<<<;;I,>>~<?;!l!<,!;l>!;><>,~l!"<l>i<!i_!:+>i~!Il:+:;~<l>ii+,l>!!-Il>~_-:>_-:
                 :i!<<;
                 ":^`."""^,,^``"^^^""^^'"'^^,^",^^^^"`^.
                 "I<i;]~~>_i-~i+i><<+<>:<"l<_<-?+ii_+i_;
                   .   `.   .'. .       ``.  ''`
                  ;ii .i!+~<;+>>_<-Ii+_:{I>"~~?]!
                       ^,,'^.""`^^'`^```'^`'''''^``'`^`'
                       ;~i'-:~-[-?-~_lil;--;i~<~i_?i>><+,

                         ,:                                                                  ^;
                         ,,                                                                  "I
                         ^,   '!i!l                                                          ^:
                         ,:   lf1<>                                                          ^,
                         Il  _-+l"":l;"^",":!:,"""^,;""":::II:::""^:""""^^^:^":::,:;^^^"::,. ,;
                         ;l .!. ....i^ ..'..i..   .^l    ' l;.'. ..!^     .<.   .."+....'''  :l
                         '!'^"<~?'  I ^_}_^ ;;{_})}`:!1<_?~"`._[[l I~??][<l! ;?!!..!        .l^
                          .,~:","^^",^^,"`^^:",""""`"^::,,:,,"",:^':^";,:"',."l:,^^:'''```^:I^
                           .l.;i>~>>:'!l>>>i`:!l!ll;'l!>il!,"i!ill!.:!iiII;'lIl!!i,^iiil!!`'
                           :" -.]il _!>;[],;!?`+>] ~;>^]]!^<+,![1.<"_`[][ ]:l:[>;"+l"__(.i"
                           l  l!!~iI;.I::!:l`,;:;iIl'!I;Il!",!lI>I!.II;:l;!'!l!l;!:"lI;>I!'
                          ^;   . !>' ili!;~:"!>~; .                            ..       .
                          I'..    .:"li>>!ill<~~<`
                         .!`+[I->[?+?+-;
                           ...'^'``''^'.
                  ;~; '~;>!,ll;`>I;l!";!ll:;li;li;I""!>I:!,;<;^Il;;I:"iI:l`;I:;I^I;::l;:
                  ;>: .:^;l`":I^ilIIl^:i:I:"II;ll:_.`;;^.l"^ll`l!I:!;,!:;I'llIli^:ll"lii
                      '_liiiii^,' :li,III;l:;;`::;,;I:!`illiI:;'i:!;,^<;II!:,'::;;;^^I;:!<:"!!;Il^;"~!:
                      .:"I::I:^'` >+[!>~~-<~~]l+<_i!~i!!~-<+__<I+!~~<;-l_+<i~;i}__-!:!l:,!;^!i:l!":"!lI
                                  ><i;!;I!`lI"I~:ii<>+^<>~`i<<~_I~<~;I_"i+ll>i.II>>`.
                                       `,",;:;.                                          .   .
                                      .;lI,I!i"
                      ^?>_~<_-;~: l~<;!<~Ii!;l^li!l!>i<^<>~i>!l"_;lil,~ii!!ll^!lII!;:<ll<_;,><lii,i^<il
                      ."":"";,`"' l~>i><<ii?_1~?>l+>-~l>+_<_?-~i_>+<~;_l~+><_Ii}~~_!:I,",l,`Il,II^:':I;
                                  llI!!;:I ,:",; ";";l'!;l.!ili~:<~i:,>';i;I;I ;:li'
                                       "!:;!Il"I!!;"',^'!;:^";,":^ '::"iI;^:!;!:;.
                                  .   ';l:^:l!;;!l:,,>"I+<!,!<l!i+',lI:ll>:!!>l;<`
                      :]>-<~+_:_; l<+:l!il<!ll"I;lIIi;i,i>i<iI;^>"+<;^+;!liI: ;iIi~,:!!I!<::!lI!!`;!i~:;+<`
                      .'`"`^,^'`' I<~!<<ill--}~_<Il++>+;+!<~_]il?!l~+!~_+<il[>-[~ii~<-<Ii__,+_i~iI<<<<;!I;.
                                  >+i<~i>_,<>!;;: ,i;il^!":lli;^!l";IliillI.;II"I.,!:i!:!i+^!~><+l<>>,;+^
                                  >-ili> !;<>`
                                       ':'",""^:,:"":,,:^".
                                      .l>lI><~li<!I>~>>il!.
                      "+lilli~"!^ l<i"il!:I,;,`,,:,:;,l";,;;!`;!!Il:;`!,ll:`i;;:;,:`,:,:;"^::,I>,`:;:;;`!:;'
                      `l;l::!!^:` :>+!l~-><~~<l+>!!<_iiI~>l!_<~_-><]>:?!i>~:+l~_~+-!!<<<_!;~<>;?>:>+!~_;~!+^
                                  >~>l"<_iI-_:i>+l~i<<'~l!>>'<<:'l,~<:!+~i+>!l'<>>;~^I~l~+,~~-">_+~_i+~~l;_"
                                  ~]<<+>'+<+~,.                                                    .
                                  .'..... '^` .'.'. ..
                                      `~]l>__->_-?<+__<i
                  .`  .^.   .. .'``'`'...   ...    .  ..
                  <}; :~<+->!~<:]]?<+~:_+<           ";::::;.
                                        .'           !. `^ :"
                                                     i`__,;I`
                                                     <.~_":>^
                                                     lII:!";"
                                                     I}[:!!:^
                                                     ;"`^"^I.
                                                      ''...

















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


                                                                                               "^"^`: :``""`
                                                               ''''''.'. . ..'`. '.` .... ''' :?--?>}.~!+][>
                                                               !{_<ii<?]:_.~+-+_l--~<!i+_<_]_ii`<+>+i-~<<>]i
          .^^^^^^^```````^^^```''''''`````^`'''''```'''''''`'`'.'''''''''`'`'...'.'.`''''`.. `..`'.`'``''^''
          .:::::,^^````^^^"":::,"",,"^^^:,,,^^``^,,,,"^^^";:;:"^^,:;,:,:,::",,"^""^",;:::::","^"",;:::::,,,`
                :-ii<<>!I>l~.   ",  ^>I:`Il"Ilil":ll:,!:l,^:`^l:I^I`I"::;^"l!;;l^Il;^'I",:",`:I:^:,",,:;i;;,
                "II!iII:,l,l'   '^  "<+_!~+I>l<_i>_li!~i~i">;<>!!:I"~iil+ii+>>:_!!<-i;~l~>l>"<<!<ii>>I!~<!<;
                                    :iI<i<~,!+l><i+^i:I<+<,>~~`>"-+il~",~<!!^i`>><i~><;;<<>~"->?+^l_i<_:
                                ''  ..     .     . '. ^                                                   .
                                >i  !!"i~_-+~<~`>i'_>"[?^>]_+-+`-+],<]+_-+_<`+?~+-i^--l"_<`]-?-?-__:I~"I_~-!
                                    l<!<-<,                              . '  .  .. ..  ..  .`.'`.. .. ....
                                    ^,`^"`'
                                    illi!:<_i~>~>~-;~I!__<~?,_~>_>;+l_<~i>,+iii+l:>+>_+Ill:i!~l__,<i>+<!`<>;
                                    I!li~!I"l:!_~:;i>!ii~>>>i!i>>+,>+~li<<>!I_!>~!i<Il~:-<!l<i<_<<<>l<<l;>i<
                                    >?i;iil"I'><+>i>li>!<>>i+lli~+l<~l!>!"+;i_+i>_<><l>,!!;"l:;,;<I;^"l;;i;I
                                    IIi^ili>I^<<<<_>`~l`i>l+<:"Il><_I]?<, >:ii~:lili]~>!
                                     .  ``   '  .'  ^`..    '.      .    .
                                    "?-.!>+++-<?>_-I]}i<_-,_}i<+>~l!__;_>_-~l+_~_-+~I-<>!--{_.
                                     .  ..            '.'`.            .                  .'
                                    "[_.~>+~~+!_;~~,+_+<<-"~~>"+?:+~!-!+>l:->~+_;;<i~<<!!l~<,i"!<<_,:!i_`
                                     .. ";<>i+!!+>~:~!_<:i_<~->>ll>:>>i<<~i!+~<_!>}_I<;+<+l<iii[~_<l>~!>i!"
                                        ~<il;<_:I::^;^;I",;:;:I:;":';;I,Il,;i,II:,lI^I`I;i":l;;!;illl!":!<;
                                        ;lI;!-!I
                                    .^^ ,^'''`..^,^'^":"^^`.'^,`^`^```"'.'''''^''.``^'..'''''''`.'.'''...
                                    "+>.~i<~<~<-l~~:!i~~l+_ll_+:?>>>>-]<I++~<_~<<:+;+~ll<_~<~?<_l->+l-?~+`
                                        __>,<I!?i__,?-~__~-+;~+--`
                                        . '..  .  ' '.`.'`.  '.,`
                                +;  :i]_[~:^__?<~>~~Ii"_<Il_<++:;<_>>+I!<_i>__<;~i~l_<;>i_<:<:i,_!>i<I!"
                                '.   `'`.'  ``;'":^^.' '^^':^^"..^^"^".'^""^,",''",.":'"`,:'"`,."`"";`;^
                                !"  <';.i~:.;l;l^ I:!,~i; l :l;;l;ll `>l;^ i;!^^~;;i"';I!:!!;,^llI;, ;:,<`""
                                ,^  !l<Ii~<Il_!>iI~>><-~+i+"_>_i~+<<l!+~~l,~l>"`!Il>:^I!!l<i!,"ii!!!.!>li`;:
                                    :I!l!l>~'!":<+iiiiI:>+;.,.;!"~!"~ii!~><l
                                    !l,:,"..` i i ;^.> .' ``".' .  '';,^;"  .'`.^.^.l.l!.l":^l`"";^^`'  ^";'
                                    i+~<i>":'^i`+^;l^_^';,;`"^:'^`^,,!lI!i`^"^:`:`;';`<+`i;<;<,!,!Il.^,"!l~,
                                    i.i^"";                                                           .
                                '   ^^.'`''.... . .. .    .       ' .  '  .  ..       .`
                                _,  >>_l~~<>_~+>l?_<<-ii]<;-<i}+_<]?+!]}]I<_<i[i;>?<?:'~~_~;<~<->?i<~-~_++_I
                                   .<i:iI_<>~i__+:,;.   .  .. '..  .  . .   . .. .' ..   '`..''..'.`.''''''.
                                    "I',`,`'^^`^^
                                    !i:?~I!<i_+i~_!>[?];+I<?__?__-I<+<+_~~~~_+:-???`
                                    . '""'`'.'`^"^''^^"'^``^^``"``..''``'^:''^.^^^".
                                      '+~' '   l]<I<ii?~>_+I
                                      `~>  '   !~?l<<>->+?~I
                                       ^'  .   .'"^,"^""","'
          `""!    ,lII>ll`,"",",,"""
          ^;;-`   ;>>>~,i _<<---!+1!
                ,;"'^^'`""`.'`^^`'::"`""`"';^',;;`:,,;^"`^`^``'^^''"":^^```'`.''`.'''..'''.
                "I>i;ii!<i!,!>~~~ll_~lli>i"~<I!_+:>!i+:~<>>]I<!!<~:<~[;i+<i_-;-~+:+<+,+_<-!
                ,l:`^::":I,:`""""::^""^,^,::^:,,",":""
                "Ii:l~il><I+IiIl!>i!l!:!:!>i!<>>;!~<>+^
                 '`.  :'''.^^'.^'' `'.';^^ ^^`""^
                 !i; ^<!<+il-~>++<,+-+!?>-;+<<~I<l.
                        `                                                                   ^
                       'l                                                                  .l
                       .;                                                                  .;
                       '!     ...                                                          .;
                       `<  `;)x11:^^^^^^^`''''''''''`````''''''''''``''''.''`''.....'''''  '!
                       `l  ^^^`^""l!"`''^"!"     ';`''`'',!`.. .`I;'`''''!:"^^`'^!^^,,,,,. 'i
                       .!   ^;i^  ," ;!>" ;^~i!<_'^'i:"Il`; l!>l "llI"::"l. ,'"^ l         'I
                        ^I"';!<,..,"'!~i" :"+<~?}"::]~>i~^: l>?< "!~-!+<;;'`-!;" ;      .'"l`
                         .^"^,^:;!,`":^":I^`""^`^,",:":",^`,"'':;"^"`^`,",:I^^^,^`;I;:;,,:"
                            !;+~>,i^<;-+i;;Il~--:<"!:--+;!"!I]]:!^II<?+:<">:_<<:i"il+_:!"
                            ~"_!>'+;_^<+l,i>:>i-^~I<^_~+`~I!:~[:l;i,!<['_I~`~!l`-!!!<{,II
                            .;",,;` ";l{::.':,":;" ";::,;' ,:"":, .:^``," ^;,::;' :"^^,,
                                       ^;`>~+?i+<-i+~_i~
                                        .^'.'''''`'''.'`
















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


                                                                                               ."""^'^ :`^""'
                                                                '`''`'.'. . ..''..'.' '... ''' ;?]-]i?.~l+?[I
                                                                >[+~i>+_?;+ i__><i}?<<ii+_i>_~i<^<_~]_-~><+?;
           .`'`````````^^^`^`````'``````^''''''''''''````''``````'''..'''`''`'''''...`.'''`'.'`..'..'.'`''`''
           ',",,,,:::::,,",,^^^^^"^"^,,"","^"^`^"`^^",,,:"",,,,,:"^^^^^:",;:,,,"""",""",,:;::::""","^"^"::;:'
                       Il!'"lIIl: ::ll:l!^"l'<i,`>;II!l;^!l!I!lI,I!lII;"~!.:Il;!!:;.,;;;I: ;;;":;:^l;;;l;:':"
                       !<+!><<+<i;!+_i+?+!l~^I!:^!:lIlI!"i!lllll,;!ill;^i>'l<>l<!Il'I!l>>I'i!i":l!^>lli<l+;lI
                       <>ii<<ii`l!^<!"Il,i>;.
                        I!l`:;I!`;;;l;!!i;lIi^.I;l!I,
                        _]_l+i!>,!!i>i>~i;!<i,.l!>l;"
                        l>>;)^
                                ..................... ....             ..         ..
                              ":;:;l;lI::;;IllII;;;::;;Il;;IIIII;;;;;:::,",,"":;;;;;::::"
                             "; ;:_11[))!{[{]!?{"`^^ij+}|+~||(\{:::,:,":;I!!;:"""":,;II :I
                             I' ^,lI:!!:l!lii!i:,l!I",::;I;;;:"^^^^^^^,<{?[{+1~~{~}])];  i
                             >^ !:fj)\1!{()({1)<!){~,,,""",,,""""""":,,,"""",])\x/<]!";  !
                             >` l`I~[,          .      .           ..........       .';  !
                             !` I'                                                    ;  !
                             I` l^..  .   .  .                  ....          ...    .I  !
                             >` ^:;i>>I!;!l;,I<il!li;^^^^^^^^^^^^^"^^^^^^^^^^^",,"^^^",  !
                             !'   I1|_:<~/<?il-~<-+-I                                    !
                             I'   +-{^`,!f-Il;'                                          !
                             l'   <+<>~?i]!_+[}';{_-]I _<+_"_[-~l}, <il..                !
                             l'   !\}]:_|~_)-_{;tx|,{),+l_I[|xi"?(},-}}_.")?I_+`__,      i
                             l'   [t[(-ll|-~[>{/|:"'``'                .  .   . ...      !
                             l'   l>l~l`^,Il^~]i.^ .:"`                                  !
                             l'                                                          !
                             l'                                                          i
                             l'                                                          l
                             l'   ":^                                                    ;
                             I'  :+_l                                                   .I
                             ;. ^!"`^,;l!l:,,I;I;"^^::;I::::IIliI";:,;^^;l,,,"^:,^^"^^` .;
                             !'  .",,'"l{[!:`Il+}>^'I~}x\([,+}{f(l<-{};^;l`"""'l;.....   I
                             `;`.`??-:', l]]~:^ !-]!,iI~_]l, ![]_!""{>~_!"i}}?!""      ';"
                              .",;"::,^^;"",:,;I"","^";""I,,I;,:I"",""","",^^":"^:"":;",`
                                !:-~,l;>:]-Il;>;?+:!:!!]+">;!i[_,l"li__:l;l>~>:I;;<->Il
                                >;_!:!!~I-_;!l~l~~:>;i;~+,~!ii~-"i:!!~-">Il<>!:!!;i_<I<
                                 ^'`^`  ^'`^'  ^''^. '^''"  '`''^  `'.'^  ^^^""  ^`'`^
                  .^' .^'`'.^'..' .   ..     .`    .      ''        ..
                  i[l ,?>]]"-?<;[_~<+:<?<_<"-]1i;-]<-:!]~i<{<;_]>-I~<_[~i->-+__l!~:-_;_-~-_!
                            .  . .         .     .                      ...'`..  .     . ... .
                    l?!.<>?;]?i>-]>+~<-I<><><+<+!++<!?<!+>-!:<~~_<_!<>_>I}]i~+<[!~<>_?+!<:~_[!!-i<<?"
                    ... '^"^ '"'```''`,`^'.''^^`.'`''`.`"'`''^^^^'"^."''.'''..'`'.`''^'.`.'''''`''`".
                       .I>i>^l-_ii_;;?<i-I^l~_-l"~_l-,::]+,i->_i;>:-??,!+<<-l'I-]i<~l:~->~i,:?-!:-~!~>^
                        :'''^,".`^`^'`'''^^";^^'"'"^''``'`^'.'`'^`^.`^`"`':"`.'`'^'',''.^^`'^.```'^`^``'''"'
                       .~!i!__i">-!~;iIi-+<<-_<;]i>~<:<+__>]i>>iii_'<~l_+;-?_:i-~~<~]>?;_~_~_>~__!<-__<!<l?-"
                       .->~~<>+;il?~~?+<l_I!<->i+[_">_>+Ii-~<-!I~~~++"                .
                            . ..         ..    .'.           .   . .'
                    i];.<~_:?+!~_->+_>+:<>><<_~>l<<>!]!![~~!:i+~~<+I~!+i;+_]!i<!i+_l<:[[~l-~-~l~iii_"
                    '^' `",^'`^.``'^^';''`'`""`^..`.','`^`"''^"",`;^.'``'``' ."`^:"'^ "^``^^``."^'^,
                       .I<<<^!-_<~_;l_i<_I"l-];!_++_I'!??i>_l:~_i~I^;<-]>:~_~~:""_+,!-i<>"+,<+[;,~+l_>^
                        "...'^"''`^''``.^'''^"'```'"`''``''^' ^"'^`.'"^' ^^^`"'..'^^`^```.^.^^`'.'^.^`.   .
                       '<:!l+?+`l_+>i'>^]~+~~>_!,_,~+~^>~__<-l!}_]~>]<~i'-+<:-+"+>`+~~_^+,i]<-"i+---+;_[!>?+"
                       '_~~~_<<;>i-><?+<<_;~<-i!+{~:>_<-!.. ..                  .    ..   .. .  .' ..  ..  .
                       .,'``^`"'``^::"^"',^'^,'"""`'^"'"`               .
                       ^->?+>_]:I" :l~I!<-!<~l~,<!!!l-~<!<+_?]li!-{{>>ii<~?,l{{_l_+~[lii!{?>!'_~-]~:ii<]+.
                         .'..'..   <ii>]<;~_i+<-<-]->^''.'``'`'.''''.'.  ''.'`''..''`'''.``...^'''.'^'`"^
                                   ",,`;,`^;',`^'^"^"
                                          ,lii:<i<Ii:+_+l~-~l:_l_-_I
                        `       .  ''  '..",::'^,;::,;;:;;;:"`;"Ill^                .  . .   .
                       ^?<?~+__;-; ;<_;<<+><~>~,>i>!!_!i:i~_+];i~"[_+:+;+_i![~_+-i>^__]+~l"_!++]i^}]]!-+~]~
                          . ..  .  <;~[+>:"_<]}~:'...'.'.'`^''''' .''....'..'.''''^  .'.. .'  '''.`''..'''`
                                   :"";:^'."`"^`'
                                          :ii!:+~+l~+_i~i::-+!!'
                                          :;:,`^:;:":;^:;:"l;"".
                                          i"
                                          ;i>i;<>~l~~+i!I-+!l'
                        .          '.  . .,:;:`";I:,::"::!I",.    .
                       ,]<_~~+[:-: ii~:!i>i~ili,!;I!l~li"li>i<"i+;->_I^]?-;~<>-l;_<>^_<!>?:,>_<:__"I<!<+>.
                        ..'.'''..  !_~>:~~~!?~>i__>:<l<<<i>~<~<~<l:+i<iI<i>i<>+>i:<;i<>l<i>?-_i`<++?_,`"^
                                   I!l,^I:,`::.,:;;.".l",`^:"Il:lI^I:ll^;:i;!;i;l^I'Il!,;,:<l,"'!:!i,^
                                          "ll;;!l!:lI!"!~>lI<!;"
                                         .,;;:"";!;;,"^l>Illil;,.









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


                                                                                              .^^^`'^ "''``.
                                                               ....'....   . ''   .. . .  ... l]--?!> _I+<+:
                                                               ~[_>!~+-]l~.__-?>!{?~~i>_+i>__>>^~__+_-_++~}I
          .'''`````````'''''''```''''.'''''''''''''''''.''''''''```''`''''.''.'''''.^.'''`...^..`'.`.'`''``'
          ',",:;;;;;;::^^^'``^::,;;"^^"^^:,,::::::::,,"""",:::;,,:,::,,:"^^^,"^":::;,:""^"^":::;;;"""""";;;`
                       <ll!IIl:"l 'il,;Ii:I!::',::":I;;:"":II,,>l:!,lll^:<II`:lI,,:,l:I^,:l:":;,^`;;:,,:
                       ;;l!:iI;"I :i<<;__+_i+1~>_~>+?>~I~--_~!!-_-+:Ii<:Iii>"!>ll!!:!!<"!><iI<<!;"<_l><~'
                                  I>i>;Il<! <+~;lil>i"<^i-l;.:<!-~!.
                                          `"^."""'"^"^"'^""'.         .  .                         .
                                         ,!>>;i>+!~-~<?!_?il.
                                  ;-<l!,<!I`::;I;i:I:l`Il;I"_~~<`l:!;llIl~;;!I^>!llIii!I!lIi!:l!>lI!;;"I!Il^
                                  ;]~}]l?][]-?]-++?1<l?+?{-!-[-i_]!?--?~_-_1})}[\|{+lll:ll,;l:lIiII!l;"l>;!"
                       .          ";`"l^I;;I,;I::'^l, l"`"I:`:I'll^"l,;:^:"!;ll^II:"
                      .]<+_>+?><~ "<>i;<_!<+l<^;!>!i-<<!l>i~+l;<>]-+^+i[}iI !<~[_,!ll__-,;}[?!?++]l;+i[+"
                       ..''.`.... !_<:!+<~il]_]-?<^'"'^''`^`^`'```'''^.`^'..^``^'```.'^^.'"^^'```"``"^,".
                                  ";;':l,,^ :',^,'
                                         ^l>i:>-ll,i;__<I>!+l+Ii~<!
                       .          .'  . ."::;`l!:,";"!ll;^^l:l:;!;I
                      .?>__<_[i+< :+>ll<?l>+i+`!ll>l~ii;;i<i<::l!-<~:~![?!i'><_[_;<!!~__"+]]i_+<?_,!i+_l
                       ..''.`'... <~i;i<>+!!_<][]<"i<~-l>__I_<<>~>>:!?++-~:.^''^.'`` .^^'^^^````^"'"`",`
                                  :;:`;l,;` "':",` :^^;``":.:^;::":`.`,`,,.
                                         ^l!!,>-l:,!;~ii:i!<;iiiIlil:<i~"
                       '       .. ''  . .",:;'li:^";,!;I:^:l:,Il,;!I"i!l,
                      '?i?-<][!Il ,i+!l~<i<ll+"l!!>>>l!,l!>!<I;l>]~<^!:_-il >>+?_I~l<>~-"!1[+l-<~[l;!~-_`
                        .'..`..   !><;~~i_I-_>I+_i~:-!>i>+-l<;~<lI><i~><I>lIii!`.'`'..``.`^``'`'`^```^""
                                  "::`l;";'^:' ,:^:.;``'`;:.^`:;,"I!!l;<,l;I,II
                                         ^!!!:_+l;,>:+<<l!i+l
                       '       .  '`  ' '",::'Il,",:,I:I;":I,   ..         .
                      '?<?~~--!_i :~+l>_]><<>+^!lili~!~"I!>>~:l-:]+_:iii<-I!]!;~_<__;_][>I_-i`+>"+;[[~<`
                         .  '.  . l<_[_!i>>?~!_+~>~i~;i---+~;!+><~?:l}]+!?<<]l.``.``.`^^.'`'' '. `.```..
                                  ,,";^^""`",.^^,,,^"^ ^^^'` ,^'":;',lI:^:,:l,
                                         ,!i!;_+!:,>:"~!<!i<~!i:
                                         ^"""';:"`^,"^'^,"^":^"^
                 i[I :?!~+!>+~:-][>~_l+>i           .""^`^"
                 ^,' .'`",^`^".^^`''^',::           l".`^.;:
                                                    !';i,":,
                                                    >`~{":<:
                                                    l"^,I`;I
                                                    :}{Ii~;;
                                                    I:`"""!"
                                                     '''''.
                ",'``"````^^    `   "^' `^^:"`'^''``'. ... '''.''. .'.'.'. ...  ..'.... ''  ''`^.'... .   .
               '__~?+-+>~~~+    !' .!i_^l~~-l;'_i!~~<;.>+> <<~I"+!'>~-?^<l"<-]>.<_++++<.<+~.!~?~'!<il~+'_>_^
                                   "]_>l+!~i!!il+~ ;__~i+~_!<;<~->>~<>;<+]<l<i_?_I!!~><>l[]ii_<+>il+]]I~_<?`
                                   '_~li~>i_I~:_i!>!<l^',^"`"'^":".`"`'``^ '^'`^` ^```^`'"^^`^^"^^^^,"`^^^".
                                   .;".":::"`"'!'`I^,^
                               .!. .:,:^:"":;",":;'""'I;!:;;"l:;:,^::::`:,;;:,"l:,,I,,^^,,,":::""',",^;^::".
                               'i. .i!<ii~>~~~iIi+Ili:<ii<>II+ii<i,<<!~:_i>ilil~<<i~>i!l~<_!i<_l>:?+~i<<i<~`
                                   '-+!<+:,~_i_'
                                '   .             '              '  .
                               `-' "_I-;_?_]~?]<~;<->l]++?l+l]_+<]??>i<~l~_?_l-+I<-_+~>]l_+!><i<~-l[_I+-<_i
                                              .       .  '   '     .   .  . .  ...'    .     ..  .  .  ' ..
                               '_. ^<ii+_<illiI~_~;~!!!_i~-~:I<l!l<><;;lil>i__<;.<!-I>]+i><<>ll<+~<i!:+I~ii'
                                '. "-<Il-_~<~<<,_?I;-_~-!+iI><~>i~iI_:_~~~+><-I'.'^:`",,^^:^""`":,,",`,^"^,.
                                   ':;'';I:Il<l ^l;'l;,;:l"`l;:;,l` l'lI!l!!Il'
                               `I  'I !:' "^^`::^` :^":^",^" `I` '^,`^ ',``^"  ,"";" ^:".'"^"^^^"`.;;^ ^^",.
                               `i. "<^~~i,}-?>_+?>,_+--~-+<~^;?<`i_~~['<->-__>^_++_+^;>+""i~_--][l.l]>.~+_+'
                                   '!iil+>~>".!;~_:.<+"i_`I~]_<-~<< '~I,i<<>~<]"<<>"]_'"-+?~ ;!^"_^~?i_Ii<~'
                                   ^-~]+_l<-~_+}<<^;_<-!^__".. ' .      ...    .  .  .... ..     . .......'
                                    `''.,`'"''^^''  `.^.  .
                               "+  "illI"ll!!I;<!^;l;i,:ll><!!,l!I"!IlI!l>I;"!l!I!<i!;~Ili:>i!!!Il>;!^i>!ll.
                               ':. ^i!<<i+-<<!!_>!<~>>l><<~_<~!<l~I>i_>+!<ii!<!!;:l!l"lIIi:Ii!!;;!!;i"Iii!!.
                                   ^I;>li!<II`<!^<;:>,:~<!i!~l;_:I~i>~l>,"l>iii
                                   '!,:,;.'..;`,:'l l^..'' '    .',:"';    ' ' ^.I`:i.;:;`;`^``"'`  `",^"'^
                                   "<->i>:"'`!:l!^<^>l'";:,,"`^^,"lliI<^^"^;^;^;^:^i?^l!<:i,i";<'^",I>ili,l
                                   ;,I..
















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


                                                                                                ```''" "''''
                                                                .''.''..    . ..   .. .    ..  :]]--i- ~;~<!'
                                                                +{_~i~+[_l~']+-->i}_~>~~+~<--<<i^~?~?+_+<~~[l
            .'''''''''''`'.....''''''.....'..................  .''.' .'''''.`....''. `.''''  .'..`'.'.''.```'
           "!:Il!!l!llil;!!l;;;IIIlll:;:,,;llIIIl;I;;:;:IIIll;;I,:,:::,:IlllI:::,:::lIIII;;;:,:l;;Il;;::;:,:'
           >I|[[?[?--}^i !":+<';<!<><>li>l<,i+-_I~><>_l!:i?-i_++_l>li!<ilIl<><~<iI!i:I<_<+!i<i!;_!>!~ii>ii!!:
           <:|{]~<}[[1^<.I ':: ^!!~+i<<,l!l"ll>;`ii!l_li:Ii>IllIi:!il!?!;!ii!<>!>I,!":+~!!"!_+>"~<>:<<I;,i><l
           ""'`:,:":,";^.;     ^~<<l_<>;`< +_>!>+~>I'>-> !.<l!>~ !-<< <+.>i>'<<+_+_?+ !?+'?{~_i?>.!>++~<_',-i
                        'I     :_~<>~i<!;~<lI~<:>><>i~,I~~>>->~;~:i<i><!<<<l   ....^.     .. .'.' '.''... .^l
                        ^i     ,;;i,!lI:;;:"^"l",;II"i;,!;::;;;'I,:;",;:III"            .                  `I
                        ^i     i_l_^l-_i+^>_-;!__;,_i!!+;~>::->~"-+<^l<!^>!`i~><+;<i>!;{[<~-~]!~<>+_+i~:+-{+;
                        ^l     l~>i<?^<<<<_i~_!;]--I+~~;i~_!:<~!+!:~>~_+I~~>i<_-_<^'........''..`''``'`.`'''I
                        `;     '"^'^:.`"^^"."",':::`^,:`^":".^"':"',;;;:':",:";;,l                         '!
                        `I I[i I->>!,iiiii~il>I!,]?!;~l~i!!Ii>>I::i~-;illl>I.iIllI?-;i~i_l~-;!<>"!;li>>!!>i>i
                        `; '^' :!i!+:"-]]-I~;;<i>>ii_!i-i^~><~>i~ii!i^+<;l_-_:<-i"<>!i;I~"!l!i-<I~^,-~+><~<l!
                        `;     :~_l+;`!il>`I~;+><<<]-<~+_,_]+_+_<?>!_;<<I;i!+"l~!"i~!~:I+"i"!<<>i<..++i!_~+<:
                        "l     I_!<:;~~++!-<+><l;!+<`>l;l-;<"<-i:>i>i;<!!i?"i_iI~_+i_~+i:~+i-I+il<+i[-<I_<+?:
                        "l     i_>:??I_~`?[++`_;+II~__>~<i!:+~>+:<;>+<<~?~~^                               ^l
                        ^: .`. `,`."```'.'... `.`''``"'`'''.^,'".^`^"`^`^``                                "!
                        ^: l[< ;<+i:~]i~_<?I+]-<!"<-I>-;i_-+_]~-^^>:+<+>i-:+~~<+_?_>~+:~I-~>~<++~":;.      "!
                        ^:     .^. ^"'``,^,.'^'.`^"`'^^^`^^`..''..''^^'.'`^"'``"'`^''^.''^'`^^'`^       '. ,!
                        ^:     "~` i?<<<+__;l?+;+l~_l<-?~_~+~:_+<+-<i?!l++~<>+?[~!I?>;_+_!;+<<-l_--l_+_~_]+[!
                        `:         >+:I<<<>!+'              .                                     . .'..  .";
                        ";         .^.'`:;"":'''.                                                          `,
                        :l         l<__;!-+! ii>[<                                                         ^:
                        ":         ^^'^''..^''"` ..''..^`... .....'.      .       .     .  '''             :l
                        ":.'...''''I_l<_]-![?!]{!,?~?+^li,l_:}-~~l+-!l_}-_<[l+_->[[><^<__]l"]>'            ;!
                         `''`""^`^^......`""",""""^^^^^^":::::"^^^`^^":;::";"^"^^"^,,:::""^`^^^^"::::::"""";"
           ;I<].   !?]<?-?[[{;:<~<>->><<+i
           '`,I.   .^,'":"::l'",I,:!",":-;
                 l!i:i!!!!Il">"Il!ll;"iII:iIi~!:!!l>,l!l!:+_!;<i<li!!l!lliI :i!,,!I;;<I;"I::;Il:,::::;!;:!;I`
                .l!~i<l:;:;:"I"Ill:;:";I!;~;:ll"Il:i,I:ll^!l;,I:;,;!I;il:l! `:!;;+il!~l~!<Ili>i!;!I!;i>!i~<<^
                .ii!!>'
                  .`  ';^``'"```"``'^'.`;"".,,,"^"",^.
                 .i~; "i<~-i!~><-++;+_~>?>[I---?_?][_:
                         '                                                                   `
                        'I                                                                  .l
                        `l                                                                  .,
                        ^!                                                                  .;
                        ^l   ~|{}".. ...... ....... ....... .....   ..         .            'I
                        ^i  ',;:;"^;;`'..`^i:^^^`'^l^'^^`^li:,"``^l;`^``^^I,"",""^l^^^^"::' 'I
                        '!   '^:.  :" ,Il^ I^;;;;!'I.:'`^^"! ";:" :;,"""^`l. `.`' l         'l
                         :;`.I>+,  ,^.<]~; :,??[{|",;1+~i_:l !_]> ">_[>-_II.`[>>: ;        `l^
                          '",^:`":l:::;"";I:",`''^^^^"^^";:",^'`::,^"^``,`,:I,^`"`^",^^"^,::'
                             l:~~l,i^>;-+lI";I<_-I<^i;+<iI;,!!--;i`ll<_-I<`l;~<<l!"ii_-li"
                             ~^-i!'+;+`+?;,;<"~i-'-I<^__<`iil;<[`i:~^~_{.-;>`~!l`-ili~)^il
                             `I,,:;^ ,;,:;;..;,!};^ :;"";I' ;,^^,: 'I::;I" :;,:;I` ;;;;I;.
                                                ::`!~+_l_<~!_---][_"
                                                 '"''^^^`'^^``^""^^'

































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


                                                                                              .^^^^'" "'`'`'
                                                               .'`.''... . ' .'  ..' '..  .'. l]]??i] _l+>_I
                                                               >{_<>>~][;_.-_-++l-{+~~!--i_?+i+"~++?~__+<<[I
          .'''''`''''```^`````'''''````````'`'..''''''..'''.'..''.'..``'``'`'.'''.' `.'```'..'..`'.^'``''`''
          ',,,,":,"""::,,:,,,"^^"^^",:,,:::;,"""`",,,,","""""""""^^",::,,;::,""^""""^,,,:;:::"^^^"""::::::"'
                      ill',I:IlI.:!;l:lI`,:'i!"`iIll!I:^lll;lI:",Il;;;,~l.,;;:I>:;';;,;I: ;::`lI"^I;::;::`,"
                      !>+I><!~~!;!_+<+]+!l>^;!:^!lili!i,>ii!!!I,:i<i!l">>`l<il<~!!^iiI<<l'<l!^i>l"iii><!?l!!
                     .>!+!<<!!"Il^ii:I!;<>;
                       I!I`l:;l`::;l:!l!I!I>`.l;IIIl!i`
                       -__i<!!>,!!>~i<>>l<<>".iii~>~-_^
                       <I[_
                         .    .'''   .''..... ..'''''..'..''.    .......'``''......''.
                             ::;I<~><~~!___<!ii;::;;:!<!<<li+<<<l::,,,"":::;::;,,",,;;::
                            :" ,;<[[]{}l{]{?!_]^`^"^,]}>}[!]|(1(<:;:,:l>l!i;!:";,l:i!; ";
                            "  ",~il-+I-_~-_--:i{][1!^^"^^,"^^"",:;I:;<_>~~!|1{n11){<I .l
                            :' !:tx)?_I~_~-<--Il-+-[I"::;;:;;""""^"""^`'^"":+--[_I~,:l `<
                            l' l'`l"                                                '; `~
                            l' l'                                                   .; 'l
                            l' l"'.  '.... '.      .'`^^^^``````````````''''''''````"I .^
                            l' .',_+~,!!+I<:l?__-<[!'`^^^^`````````````^```````^^^^^"' ."
                            l.   !1)i:!_ji_l!>lllIi"                                   'I
                            l'   ><?^,;;|+;!I'         ... .                           'l
                            l.   i]<?-1-~;]+{]._t{?)~.{~{}l{/]+-(;'}~~"'.""'``.``      'I
                            !'   !\[?"_{i-}_~_ir/['[?^;!<^_]1,.<]_:-??+ `{}l+<"?+"     'I
                            i'   (t}}~ll)+~[+\f)^"`^^'                                 'I
                            "    l>I!:``^:"`~_, ' .,"'                                 'I
                            "                                                          'l
                            :.    .                                                    'I
                            "                                                          'I
                            ,   .l!                                                    `!
                            "   ;~i..     ..     ..                                    ^<
                            "  '"  '^Il?+l"^l!_<I^"!!<-<<i<~<>]~l~~<<^`;I`""`^;:"""""^ ^<
                            ;`   !il``"_]_l::"![+l^:+}f)(?<!1}|(i!~(]I;I;:;;l`:`       "!
                            ';"``>~<"^" :~il,' !~_l:l!l!<I: !+!iI""_!>>I,i~<+;"^.....'"I.
                              '";^"":'"I,^,,',;"^;:"II;:l,`I:",:^^I,,":``:"",l",l;:Il^`
                               <,_~"II<"_]:i!<;_-^~IlI_?`~lll]_^i;l<?-^<!;~~>,!l,_}ili
                               ll!!Il,l;!<Il,iIl<;>,!ll<:l:!I!<;l,!><+;l;l!lIII;li+>!I
                      .       .        .  .      .             .      .      .  .  .
                 ~}; ;?l->^~<lI}l:~<l_,i>i!l_iiI_ii:]i!<>^~_><I:_>!I~-i`>>l!~`!Iii!I]?l>~i_;~>!!+Il-!
                 ``. ^<<i><:I>><<:~li:<i"~>~i~??l+~~<++l?~Ii~+i~l~i+i~i!i?i>i<~l;_<!~~;i<>~ll_!>>>~_;;I;;l'
                     "-<<i+I;_i!~;ii<I>il<i<,~l;^l;I^:!^,l"^lI,!^I;;^:I;Il,!I;II^!I;Il^:i;l;:!;::i>;`I>I!<`
                     `;i!'^:,l:;>":li!I+>:;!
                     "!,IlI;I^  !I:`;II":;"^`,,;:,;";^I:::"::,>;^ll^":,:;"l;l:!l!l:li!lI::;;,;":^,I,`l;'
                     "il<!>>i;  l!~l>_?~-~]]<+i>~_[~~l<+_i}+!:~<:l~::>l!~,;l>!l!iII>!<lllliI!<:!ll<<"<_"
                               'l_i~i,l!!I!>>li,l~i!Il:l!l<"
                                      ^`^"^''^`"``^^^^`'^,`.^."`'"'
                                     l+!l<?<>~_<~?_~~i>!~i<~_l><+_l
                 ":' ^l^^"'",^^;;I:I".''             ^^^^``
                 <-, :<i_-!l<<:_~_i>~:+_<           >,'^^'l"
                                                    l.:l"':"
                                                    I`]{^I<^
                                                    I'^,I`,"
                                                    l11:<<;;
                                                    !:^```!^
                :,'`^^`^``^`    `   "^`'''''',`'`,`'^",,,,,"`.'''''.''.'......'''.''.``... .'.. `......
               '?-+__++>-<~l    I. ^_!>~I]_~i~-~!~+I_>>i~<!<_ll_<~-;<~~+Ii<l<+_<lli++!_<-_il?+<`?+l!<+~~_?]`
                                   'l~l_]i,<I+~~-_~_~i+;~~lI>>~><>~_<-l+<<~-~I>~~<><<+I~_+>]_>l!!<_!~>>?--<
                                     .. .  ..'''.^`.. '  '. ` '`''.'.'.`.'.'`.''.^'..;.`'^.^`` ..'`.`.'^``.
                               `+. ^>::i-,:<<:;<!'!>ii,,~!;i^>;"lIi^<i!I~l!;!l`ii^l_I'+~i`il:'<li;!;'ii;Ili.
                               ."  `i!iiiIl>~!;->l<<;~i<I~<<:~>l!>>l-<]>Ii<l<>,i!~l~<!<<+,>!<!<I+>]<I-!<~<-'
                                   `+i>~!;;;i<:>~->i:><_^!~>:l~~<~_}!'i<;lii>`:!"+~<i+i>l,i,;>i^l!l>l>:l!><'
                                   `->i:<+:i~i?<<i];>~+I-+<i:+;-il<>>[+_,
                                .   `             .'    .'.
                               ^-. .<!<:+-_l-?>?:;>"~+_i:>"~?+<>>>-Ii__+!i!-_I]?I<__<_>i]<-!;~_I~]_I~>>-;_+'
                                .  ^<l<<I...''.'  ' '.'.   '`'.''.`.```'...'`..^''^`'^``'`^.'^^'`^'`^^^"'"^
                                   .,.""'
                               '!  'i::,II';:;`!!,,+:';I;I,^;;!^^;`,I,;:,':,,;^",',;i'^,"::^,;^"l:'!I`^,,,,
                               '!. `_]~i~_:ii~I>~>"+-,!_i~i:++<:;~:!_~><~">~l<Il!;<<+^;~>i_!;+;;~~">-;!-<<<.
                                   `+~>"<<<^~i-!++' _>^<l!l"+>^>+<<lIl<,]+i>-:I-~<~"<"<--;:_~>_,<,~__~??><
                                .   ' .       . . '.              .            .        .          .
                               ,_. ,~,_+"I]~<~-+<`_};,~'>.-<<><~~; +<:'<-~~~+]I.<+>i~~><^I+'_~_~-~~_;I+"<-~'
                                   ^ili<i?l~<<~:~!!!]>;!~!+><<<;>_>i_+>>;~;+~~<I<-~~;''^ .' ''"'^"``.'` ''`
                                   ':"":,;`"";I`I",`;;`,;,l::,!";!I,lI;:'I`I:";,l!l;^









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


                                                                                                ^^^`'" "'```'
                                                                ....''..    . ..    ' '..  ''. ;??--i+ ~;+<~I
                                                                <1?<i++-?!~'-+-~~i[?~><>++i~_~i>^>-_[___<~<];
           .``````````'''''''''''''```''.....''''''''''.........'`''..'..''.''''''''.`..''' ..'..`'.^'''.'`'.
           ',:,;;;;:,^^^^^"`^"`'``^,,:;;,,,,,::::::;;;;:::IIIIIII;I;;::,,,,:,;IIIIIII;I;:,,:::;IIIII;I;::::;`
           .l'>.   :~++I><i_!.l+i!!i!;
           .I^:`   ^!i!ii;'!l'<+~!~<~i
                 :l;,^:^,;I,`:^ ":,'"^"l;I!";>>,!l;i,I:,";"l;:^
                 `";!"I,lllI`I;,i>i^I;"~!>~::<i,Illi"ii;l_I<+~!
                 :ll,"l!;;>!!":I:;;ll:l';`;Ii,ll;I::I";`
                 `^::,<I;:!IilI;:Illl:l^;^;llIi!l:,lIIi:
                  `,^  !"""^^:^^;,"'^,`'l,;.,II^":::`
                  ;lI 'iI><<:~i!+<>:i++I-I?:~++!>!I<i'

                         i                                                                   :.
                         ~                                                                   ;.
                         ~                                                                   !.
                         ~    ;_~~"                                                          >.
                         ~  '"<{[[i:l:,"^^"::^^""""l;:::""";"::"^^":^,",,^""^^",,,;,`",,,,'  >.
                         >         'I ..'' ;;.'  ..l^   . .i..'. .^l   . .;;.  .'.>,.'''''.  i.
                         :;. "<<i  .I i]]i ::?}{{fl""{?>~-:; I{{+'.<-}+?_<!, _<;; l'        ^!
                          ";,",,""``"`^^'''^"`"::;",^,,,""":`^":,'`,`;:":^,"';I"`',```'''`";;.
                            .^!lll;I.,l;l!i:'l;lI;!^"llI;II'llIll!^'!II;;l',!;lii;'l!!lli,'.
                             >,<[> <I<'{?~.+I!:]-:I<I`__] <;+'-}!">lll]1^ii<'-!<.?I>"-{<`-
                             ,!!ll;i^lI!iiIl`!ll>l!",ll__;!'I:;l;:"'l;;<;l^IliI;;i^ili~>l!
                               ....   .. ..   .. .   ..;>".<<_~i]_Ii~+>!><` .....   .....
                                                         ``":I;lllII;;;:,l^
                       I;:`"^^""^':""^^"^""^I"',;"^,^"'`"""`"''
                      .li-:+i<+<;I<<_~[+i!~I+_;>-~_-~~<l?-_<_i<, .
                      `<~<<<:>+^>-+i<_>>`~!i<>:Ii!Ili<l+i>+>l_:+:_+__-___l><I~+;<<<-+i'
                       .:;,`"",,^;"":":,:::,;'^::',,:, ...'.."'....`.'^'....  '.''.''.
                       .]?_l_<~~;~~<-~+<_!~~_^i]-l_!_<
                       '<+_,<)
                        '.'''"
                              ',,;:,^,":;:,,:;::III;,,,""^^^"^`^^",,,:;;::,"""",,,,,,:""'
                             ";':;?)(1((~){(]_|{;;:,,,:\]+)]!}()|)!;;;:"""",,":::;::,II`l^
                             :  `:I!i!>iI!!>!;!l,:,,:,:ilIilIii!!I""",;~{+[]<[l_[<[<1_! `>
                             ;. ;;j)-t{i(t))[(\>_j[?}i:,;;:;:^^^^^"",:;IlII;}){x|+)ili> ^>
                             ;. !^-[<(,'`''''^^^```'''.'^^^^'''''''''''''`'.`''`''''.^I ^>
                             ;. l.   .                                               ': 'I
                             ;. !'                                                   ^i ';
                             ;. :,^"",:"",",:,::,,",",,,:,"^^^^^^^^^^^^^^""","^^""^^^:I 'l
                             ;.   I|\?">+(~]I<{]-]_}!                                   'I
                             I.   <[{'^:_f_i!I'                                         .:
                             :.   -~~l~~!}i~+[~.l<>~>` <!~i`<i>lI< .!:"                 ."
                             ^    ;}][l]|i>}-)["\n1i\{"}~1>]tx<!)r~:/|{~.;{~:~,"?>`     ';
                             "    ]/{1?l~(]_[!)/rll.",' '' ^^^  ''`.'"^^ ':^'^`.:^.     `l
                             ;.   +]<[?:;!iI!1\~"` ^;:'                                 `>
                             I.                                                         'l
                             ;.                                                         .;
                             l.                                                         .;
                             !.   `^`                                                   '!
                             l.  :-[_'                                                  `!
                             :. `l"'`^,,:::"^,,:,"^^,",,,::I;III;:,"",^^,,""""":"^^^",` `I
                             :   .``^.";/]!^';;]1l'.l~{f|\?!_1)f{!<_1{"'l:'''^.~,...''. 'l
                             ,;' ^][]"'" <{]>,. -{-l^+i>~]!, <}]_!^I[i<-I">]?[,l`      'I"
                              ',";:;I;:;I:;;"^,::;l,":,"":^":"":,^^::,":^^:"",,^^,,^"",:`
                                !;~>"!,lI++:!:ii+<:l,Ii~<:!;I<-!I;;l~->I:lI_+!!;ll-?li"
                                <:~l^iliI+-"i!<!~_"iIIi<~"<!I>_~;!!;>-~:!>,<>:!i>;_};~;
                                ."`^"` `"^^"` `^``,. "^``"  "^"",  "```" ."`^," '"``^^
                  .'  .. . .'  '.            .
                  ~[, I~!_~"_-;<?I:<]~_:]_+_~]+-!-_!l[~_~~;~_~?I<~-><_)<I+?<?~"+I-+!~1[!_~<?!+><+]!<?li<?!
                  ..  :il~l+>:_+_?<~" ..'...'..^' ...'.... .'.'.'.''`''..'`.``.' '''.''.''''.''.'^'.`'''^'
                      `,'".," ::::;,
                      !+i<>><?^;. i<-;_<~~+i+!l>~<+<+>_;]__+~i;_~:?_;~~!+;[-?!i,<?!><i"?++~:`
                      '`^"`""".'. .'".''``^',,'`````"'`."""",^'^,'^,`'^^"`:""^"'";"":, `",,..
                                      `!<-i'~<+i<<I~;~]+!
                      `^..'.''.^  "^'."::,,^``"""^,:",;":..'. .'  `. `' `..'''.. '.  .       ''.'.'  .
                      l+~-<<~]:_` !><:>_-<_~~<!<<~<<-~<;[-_]?>!~_I]-l<~i-~!}]]i~:__~;[<-+-~_"i+]<<<'_!
                                 .++ii~;:___<I'                                        ....'        .
                                  ^"^`".  `^'
                                      '<_?!'~<-<~-_<<?+~i_~!]??;
                                      '"","''^""``^``,`^:",^,,"`









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


                                                                                               ",,,': ""`"'`
                                                               .''.'`.'' . ...`. '.` '... ''' ,?--[i-`>!~~!i
                                                               l[[~i~~~[;_'+~__+!-}_i!i~_<i~<<<`i_>-~-~><<-<
           ''''''''''```^````````````````'''''````````````''''''''`'.'''``'`'''.'.' `..'''...`.'``.`'''..'.'
          ."",,""""",:,,",,",,:,;:,,,:"""^^^`",,,,,,,,,::,"^`^"":,,":,:,,,:",,,""","^^"^",",""::,:;,:,",:::^
                      >!!ll!lI"l '!lI;i~I!l;!";;IlIlIIi":!ll>",<:<l!^I^il:">;IIl;:`i>>!!:'I"II,;I",>IiI"
                      ;;ll;i;;"; .";l";;,;:">,,:",,I:;I,"lIli:;<"l!>"I"l!I,>I!liIi.:I!;l`^l^!iIl<;`I:i!`.
                                      ^li>"^i!i:!>!ll,, ;
                                      :lll;":Il;:lI:;:I'l.
                                      !;
                                      ,<<<:"~iiIi<i!!.
                                    . ,!l!;^;llI;;l,;         .                      .
                                 I<l__!:<~_,:-~i_i_<l<i_+~-~<ii_?!___+:_+~>~+<il~!_<;~-;!-i<<!iI_II-<+-_~`?_
                                 !__:]__;i~<_+>_-<iI+_-ii?__-_<<I<]-_~_~,!_i<++;]~><-i__+">_<l_;i]~-]-<`' '.
                                 :;"":!I,;";;i:;!::^lIi,:>I:;III:;:l,^::I!IIliI::;lIl!;l>;l;;;>!:I;;i;:"```^
                                 !_;-+]>!~l~?{_+_+-l~~_lI+<:!<_i<~!<!:<i<<l!+~i>^:~~<_~;><;"!!!?::<l_<~_-__>
                                 `<^l!;`!I>>!+:li+~`
                 ';:  I:""^`;"':I!:;;'""`             '''''
                 ,+<  !!<<>;><;i_~<I~,>+-`          '!:::,;;
                                                    "I `"' >
                                                    ^;;|i,i<
                                                    ^" l;^^!
                                                    'i[!!-`:
                                                    `>~;"i"I
                                                    .:^",":"

                !]Ii>>i!!>>_`   :"  ;i>;:>~;:iI<l^;:,il>"!:,!>:ii"I>i>II:i!I+>"l!ll::!i>I;il<I,l!;IlI!I"Ill!
                :;,ll::"";:l'   '`  ;;ii>~!l!~i<<`"`'I:I `."Il^;l"I!!l":":l,;!^:!;;;,!Il:;iI!I:i!;ll,lI,!i!I
                                    :"I<~:';~l!i>;
                                `'  ^''.  .`.. . .'''`,'`.'`^^^''.`.'''..`''..'...'^'.'.^ ...'... '.. . ..^.
                                ~I  ~;!+"<-_~_"<l;?<_<~__^~_+_~+i^?"__-~>-_~:+~~~<+?<_+[}~`-_<_~-,i:_^<;_?1l
                                    I~_>~I-i?;~:]-]>+?+>>?,~?++-i~>                      .
                                    .'. .  .  ' `'.. ... .  '.```'^
                                <l  <_<~<_ii~l,<i!!>!<~"-_+-<~"
                                ''  .''^^^''^'.^``'^'^".^^""^^
                                l,  i><!^l!l~!l!!;iII>I"<>"l;I~!<<iI;I!l>l;^;!;lI!l>;;+<<~l>.
                                ^^  ^^;;`;",I:,II`:;^:;'"l^I,,I::;:^`I::;:,.:I":::"l:"il!!ll
                                I^  :II^II!:;I""';;I:^';;';;`,:;::I:; 'I`,^;",;'",:^,:""^^`."^;::;,:,;`""
                                I,  ^:>,:i!;!l:>^i!l;,^li":>"l<i!;;!! 'i"IIi,I<"iI<li!!i,;>"I">!:!lll!.'.
                                      .>' <l;:l~l:,>!"I!I^i:;"l;;I!l"<;';;!!;;;<II';l;I,"l',<i;;;:,:';!li:!,
                                      ':.._[~+~i<~+<l"Il;^I";"II!Ill^l:^I;;;,:llIl^I;;!::!^;i!l;i::I^Iil!"I"
                                         'l!ll!`;"iI
                                         .i"`!:I!;^!I,~i^`lIlI^l!^:I`!l:l,I;":!;I!;:`;II:l!:;.:Ill^">I'
                                          ;;,>!!>!"!!,i>,"il>!.""^:!^~i!!,;i:I<!>il-"<~iI~<!!`i>i~,'<:.
           ' ^    .""^``` `'  .
          `<;|^   I][1{}-`{_]}{,
                ''    . ... .'.     .                         .   ..       .
                :<<_;+<>-+~;i-__--~I]-!i~+_~[+~:+?_-~-~;<:]l![?i!-<]!+~i~]<~_]+?Ii]]~.
                `^'' ````"^..'"``""''`'``^`"``^'^"^^^'^ ..'  . ..... .'..`. '^^"'.'`'
                :<~!l?-+~[>_~_i<+_-+<~:+:<_?i?++>!?+>-:
                      '    ..          ''   '....
                 I~i '->+~<I_<<]__;___I}~[:-~??__;
                 . .  ^^,^'.'"''^'.'^^`''"'' .''`'...'.
                      i>_:I+;}++-?_-~I_:>~~:_~<i>?i<l~+_'

                        ;                                                                   l'
                        ;                                                                   l'
                        ;    `;:;'                                                          l'
                        ;    _u)-,                                                          :.
                        ;  "}<-i'^",","^^^""^^^^",:"^^""^^,^^^","""^^^^^^""^^","^^^^^""""^  I'
                        l  ;;   ''^l'.  ..;;     .;^     .~'    '^l      ;i'  ''';,''````'  I'
                        ;" ;^~+!  .: !--! ,,+]]-/!.'<<;i~"l ;+__' l+[>~+lI; i!,: "`        .!.
                        .:li"I;,''`:',I,`.^",IlI>,``IlI:;::'":II'':;iI;i,"^.!i:^."`.'''''^,;`
                          I:^I;;I!I^:I":I!"':;,"";'^I,,,l:`;ilI;l"':,"",;'^!:;l!:':!lIli"^`
                          l !:!~>.i"_`]-~`>li;+-:l!!^?__'<,+`[1!">:>;}1;!i!"?i+`+:>,]{>"_
                         "; !l!l!,>"~:i<i,!;>I!+l!Il;<!~,<"<:i_i;!`!;!~,l;I,iIl"~,>;<_<;~
                         I'  `^^^"'  ^``'^  '``'`'  ^'`'^. .^`<~^ ^:;:^ll'"llll". .^`'`^
                        .l                                     ^,^i<++<_+<+i---;
                        ;:,-?I~l++++~_l                          .
                        `^^",^:,:;:;;:,












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


                                                                                               '^""`"" ,.``".
                                                                ....''...   . '' ..'' `.. .''. !]]]+_<'~:_!-"
                                                                -]~>>~<-_l>'__-_<>?]~>~<+<>+~<~I^++-__?~i~i+:
           .```````^``````''''''''''```````''''''.........'''''.''''..''''''`'...... ' ''''. '`.'`.'`.''.'''.
           ^;;;;;;:":;:""^`"^^`"'``^,::,,,,;;;;;:,,",,,,,,;;;;;:::;III;IIIII;II;:::::,:,,,:;;IIIIIII::,,:,,:'
                  :~: '_l<i"I!I`~llll";lll;
                  ;i: ';,;I.`::^iI::I^^I,:;
                      ^-l>!i<<:  Ii!:<<+!i>i>I>iii!>l>:+~<+<i!;<!"iI>-<>~;,i>!>!~:,!:<!Ili^<>>~;^
                      .,,;::I:"  '^:"":,",,,l`"","";":`;;!;l!:^:;^I:IllIl,^liIl;!:",^l;::l."";I^.
                                       I<~Ii<~>.
                                      .^'`^^:::.
                  !]; ,?>~+!>-i:_-?<<+,<>!           ."^``""
                  ":^ '^^::"^",'"""^'"'::I.          ;,.`^'::
                                                     I':i:":I
                                                     !"+),;+;
                                                     !"`,;`";
                                                     ;{|ii~^,
                                                     ;I"^^^;"
                                                      `^`^``
                 ''        ..    '         .
                ._]_]]-_<-__-   '_]~+?,?_?~__:_<<:<><~l~_?,+;--><+I!+~<_;~I__l!~~~~<->?'
                 . .'' . .  .     .... ''.. ' ..'  . .  '. '..'..'..'..' . .'.'''..'`'`




























































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


                                                                                               `^``'^ ,'''`.
                                                               ....''..    . ..   .. ' .  ... ;]?__!~ ?I+!-l
                                                               <{_<<+_]]l<'?+--<i}]+~+i_->_+_><">-___?+i<+}I
          .^``'''''``^`````''''''''''```''.........'''''.......'`'' .'''''.`''''''. ` .''`...`..`..'.''''``.
          '",`",,""^"",,,,"""",^^````,,:;;:,,,,,",,:;;;;::::,,::;I;:::,:;;I;IIII;;::,::,,;III;II:::::;;I;;;`
          `!^-.   "+<_ii><~il>.ilIl<!;i,
          'l"~^   '":ll:^Iil,^ -iI!>~!~I
                "l;,`,",;,".^:;::,:,": ^I::^::,:;: ":II`"::I,I;,^,:`:ll";;,I^;""'"""^^"^"^":^^^"'""`.;;;l:I"
                ;I<~I<ii~i+l>+-??_~!~+"!~i!;~>!<i<^!<>_:<>i-<~<<I;~:i_~l<>!~:i<~:>!i!!__~i_?~>;~;i<~,_i!++[i
                !i!>-!l^I^_~i;>!>_"
                ,;,^`'``I".^.^`^^`:^,"^`^^^`^^"`'^``^^`^'.^``^'^..'.'''''`^''.`......'.
                !~!<>^>:-<"<;+!i~><<>lil_>!!<;_i"_><-i+?!"-+_--_,><:~+-~+<[?~:_+:~++__]<
                :l,``,,,^;;"^`""^":"^^'^'"^,^,"""^^^`^                         .      ..
                ;i>II_i!!_>_>!iii<+<ii:!"i>i>+~+;l+i!_:
                  `.  ,''  '`'.'.. ..  ""^ ^""`'`"`'"
                 !<l ^~i_+>!_~~~~<Ii?+I]<]:-<__>!_~>~i.

                        l                                                                   :
                        !                                                                   I
                       .l                                                                   ;
                       .l    ";,:.                                                          i
                       .l  ';)/{1I";"^^^^^"^^^^^^^^^^""""",^"""^`^,,,,,,,""""^^^",""````^'  <
                        l  .     .:!'.  .':"     .;'   . '>'..  .,i.....'I:'   '`i"`''''`'  l
                        l^  ">i;  ', >[-l :"_}]]|::^]+i<<^l l-]- '+_?>>~l;` ~>!, i'        `l
                        .;:",,"^'.`"':!:,`",;;l!i,:"lII;I,;`,:ll^^;:!;;l::^`il:^'I`''`''^":;'
                          .'^llll!:':lIl!i"`lIl;;l`,l;II!;`IlI;li^'I::,;;`:i;IIl,';I;;I!"^'
                            >"~_<.+,>`[_<`>!lI~?"il>^}--.+;+^?[;:!lIl-)^i;i^}i~'-:!,[{I:<
                            Il<li;<^iI>~<;I:i!!_I>:l;lI>,i^iI!<l;,^lIi};>,i;>;;,~"iI>-!I!
                             ''`'^   `'''`  .``'`.  ^!;Il"II:lllI::;!;]:.  `'''`  .`''``
                                                    "~~+<><+li!<>~_iiI'I
                     .:^` ''`'`` ^```.``.^.'^' '^''`'    .  ' . .    .``.   . .' .   .      . '  . .
                     .<i+`>>>+-l`->_<?--^~I;~_"<-+_--+>i]~_<?+~l+-?--I!{>"++->?_->^+><?~l,]<_,?_Ii_]<-<<-`_,
                     ^]~~_-<~<,>I;>~,_i>->;                                                         ..  ^ .
                      '";^":",`^^`^,`,",,"^` .`'''^'..'
                      ']]<l_~+<I+<-?~[+?!_~-';--?_++_>~.
                      ^+_?<+:1i
                      .''^^'.I"

                             '"""^``^'`^``'^^'`"":::::^"`'``''`'`"""""":::"""":::,^^^^`
                            ":'il1|11)-<)}1?_{_"""",;!j-](-i{{[{[;,:,,,,,;;I::,:I;;:;:,I.
                            :  ",liii<lI!!>;;<l,,""^,:-!i~!l~<i>l"^"^;~]<[_i];~~~-~{~" ",
                            ;  !Iu1{x{<1)))[{{;]/111-;",""""^^",:;,,,;IlIl>)|)c|]t<ii: '"
                            l  :^?1?[]``'``'''''``'``''''''''`^```''''.''.'^^""^`^'.;; ";
                            l  ^                                                    "; ";
                            l  !                                                    `, `"
                            l  I,",,,:;;:^"",:,,",:"":,"""""""""":,"^^^""":,"""""":::^ ^"
                            l    <\(~l_])<},]}-?_]|:                                   ^,
                            l    <1+ I^[f<i;l                                          ^,
                            ;   .]i<:]<>{l<_]l l<i<l '>l>I"<i>;l! .;^.                 ^,
                            ;    +{]_!1/:}(-/+;/X{+r?;1~(i1rf>i(t>I([?i.!{<!~",_!.     ^,
                           .I   ^}}[[l:[1]-[I|tfl:.,,. `^ ,:^  `^"'^,:^ "l,^;'`I".     ^,
                            ;   ^1[_}~^>i~;+{t!l. ::;.                                 ^,
                            I                                                          :;
                           .I                                                          :;
                            I                                                          ,,
                            I    .'..                                                  ,,
                            ;   I_-]i                                                  ,,
                            ^  ^!"^"","""^^^:"^^^^^^^`''`^^`````""^^^``^`^"""^^''`^`'. ,,
                            "  .'```'lit_I''i>[_,'`i<)t}(+>]-[\+i-]1~`'~"''```i''`^``. ,:
                            ;"  ,}-+ :''-[~I: ,[-_"l-+_-?!"'?[]_l`~{__~i:~?-~.I       .I`
                             ","""",^"^^:Il:,^^,,:"",,"",,,",,:,"^,:;::"^:;;l,"^^``""":`
                              .llil,I^ll>>l;"l!i!;:"l!i!I:,I!<II`:Ii>Il";Iii!!^I!~<I!'
                              ^<I~!'+i<i?-`!!;><-^>i:>+<"<<:~[i,;>,_{!l~>"+<"l!i;_1^<^
                               ":",:" :,,::^.:"",:'.;,"";.';",;:.`:"",:.":,:;:.,:",:,


















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


                                                                                               .,,,^^, ,'^`^'
                                                                ''''``''. . '.''...'' '..  `'. l]?]-<~.<;-ii^
                                                                ~}+<i~~_+I<'-__+<i]-+<<>+~i<+<>!`<_<-_-~><<]I
           .```````^^``````````'``````^````''''''''''''````'''''''''..''''''`'...... '.''''..'`.'`'.'..'.'''.
           `::::::,",::^^^`^^`^^`^""",":,","^`^^^^^`^``":,:,`^"^"^^^^^`^,,,,,,:::::::,:::;;III;II;II::,,:,,:'
                  :+; '?I>>,!iI:-I"l!Ii"I!;;:<!l:li;^<lI;l":!!l;^!II,l<<`;llli"
                  ,l: .:^:I'^":`II^;;"l`:,"":I:Il^,:'l:;,I``l;:I`I;::!>I."i:Ii"
                      `?!<ii>~::` ;>~;l<>!><ll,!liiliIi;!;<~l>!^~i"~<,l!!_^+~+;I:I~!!!!^+i<>:'
                      .",;,";:^.' '^;"`"^"""^!`,^^"^"`"`"`"I;;;`:I^,;,^";I^;::^"^,I:,:; ",;;'.
                                       :>+_i>,<<+ii~i>;i?_<
                       `     . .  ^`  `,"^,:`.`"::"^:;",;:;      ..     .
                      ^[<]_~-?I_I i>+;l_]>-<>-;i<>>>+<_l~<+_<__:}>+?_!l]-ll_-:-~]~+_<<:>]<+<~[-_l<,[?>>~I
                         .  .     ;_i?<:... .`... . '...' ..... '  ... .    ' '.'..''. .`.''.......``''`.
                                  .``,"
                                       !-_?i_;<+_~;:!]_-^
                       ^     . '  ``  `,"^,,^.`"::^"^;,;.                      .  '. .  .           ..
                      "?~]_~-];_; l_]!+-->+~i-:~<~~>+l~;i_~~_]ii+<[_+_<<!-i!-+l]+l+-~-I{-]!<;<[<<+~"++--:'
                         . ..          .^^`'^,`^'.'`..'.'`.'`..'...'.... '. .'  '.  '.........''.''  .''
                                      .i_+-i~,~<-<<~<+I_?]_ii
                      `l",,:,:':` ;I,`:::^,:^^'"":"";::",":;","';":,"`^`::^.:"^^^^^.,;:;::'^"^"`^`'`:","`.
                      "+i~i+_<,i" :l<;Ii!I>!i-,!;lll_li;~i>_>~<,]I!~_!II<_<,_>+<<<-";<+><i`-l<]~~~~`>!++,'
                                       `:::",':":^,:,:"". .
                                      'l;!~il"i!~<ii<li>i"l"
                  ,i" ^i:;;,";:^ii>I!!^,^`               .
                  l+; ^Il<<!:!<"<i>lI>"<<<.          :I^"^^l"
                                                     ;'.^:'"I
                                                     I"-),I<,
                                                     ; `l,`,"
                                                     "?1l<~`,
                                                     :>i",I:,
                                                     '"`,,":.

                 >?<_++_<<<+<    l. .~<+:~+_l!->]<"!l"_i~;!i^i~!;_!:><<!IIi_!;><!<_;
                 ^",::^"`"^^,         '^ "^`.'"'"^ '  ;',    ^"'."`^^""^..."".""":,`
                                .<' '<`~i^'iII;il!":_; ! ;.l>I:!l;, !;, lII;;;;I "!:Il!;I,'l'!>Il>I!!:`I":>l`
                                .I' 'i;~~!!-++>ii~;I+_;<l_:!~>_~~+~"!ii:>+_<~~[<"l+>~<->-`.!'l!>l><ii,"l",!>`
                                    .l>:i>>;;!!<"!I>,<<;l~!:iI+<Ii!!'ii~;<<l:"<^_>l!I>+<<^
                                 "   ^.'.  .` . `..''      .   '` . "..  ....  . . ..     '. ..`'.. ..'..'..
                                .-` `~Ii+:+_?>>,>:i<i:+:i_;~~_<_]-_"]??I<-li?l+~<?~_[-li+:!_~_;+_?i;_!??+[~~^
                                    '<-<i~+~_Il+>i~>]?<>_~+,                  .        .           .
                                     `' '.... . ..  ....' `
                                .+' '<i<I<>~>+i<;l_?<iiIi~;>-l><<<~_<+.:~~+lI>!_l>~Iii>>>-><<>;iI<>><!i<<,:,
                                 `.  .^"'"`^^^`;,":"^`^'^,'`,^,;,,^^::..`,;:`":;^";,:,:::;:,"I":";:,:""::''.
                                    .<i ^<+>!<+i;?~:+>+_i-~>:
                                     ^` .,``'""`'.`^^`"^```'. ..'.    ''.  ' .  . .  .        ..  '
                                    .<! `[_+i~_<i"!_l;i;i;~-<<+l!_I:~>~<i~-~ii,-l<?~-]-~,-:!_~<-~:]+:<_]l<-,
                                        ^~<<->~_+l<~;__i<;]li~i-~>~<!,<+>i__<+". . .. .. . .'.  '  '  .`'.'
                                        `;^""",""'"^ ","^','^"`,:^",`.,,^^",",'
                                        `iI<>,~~^l>+:;~"!i!+>~>>;I,I-I,il~il~!;"i<+:>~"l+!l>_~<.>!--"^>;^_I
                                        `~<!_I+~l<?<!<>++>~~<:~:l<!<>~?>!I~~i>~++++!:+!<<~~<i"<!~<;i~;' ."`
                                        'l;;;":;,"I";;,lI;;I;`I';;;l;;l:"^ll,;lli;I,^i!l;iII,'l;I!' l^































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


                                                                                              ."""^`" :`^`"'
                                                               '`'.``''. . ..''...'' `....`'' l?-]_i?.+l+<];
                                                               <}<<i<+-_;<.++-_<![[+<~i+_<>_+<i^<-+_?]_~~~]I
          .````````^^^^^^`''````````^`````'''''```''''''`````''''''..'..'''`''.''.. '.''''...`..'. '.''.'''.
          .^"^^"::,""""""`"^``^^`^",",,,:,^^"^^":":"^`^^^",,,:^^^"`^^`^"",,,:;;;;:::,:::;IIII;;:,::,:,:;III^
          `>.Ii:  "-!l!l>~";l!;I<><I>l:l,>!:lIii:I`i!l":~i:lI^_;;:I:ll:,<;lI,
          .I'^I:  ^i_i>!>_",l?!i<l!<~+i<:;:<!>~~ii";;~",~>>i>:!l<-{i?<I:!l__>
          ...^... `"   .. .'  .
          ^I,+!I" ;il_]>_i;>~<~'
                ,I^`^`,`^^"^`;,"`^"^^^^^,:`^`:,`,;;`::,;",^^^^:^^""```.`"``^',^''^```''.^^`''^^^.``''`'..'.
                >?i>i~~i[~-_l+-_!~<i;<+~>>~~l<<<~__!<><_l~~>i+?+~i++_[~!~<!~i+++:~?<<~~l~-?!~++]i+]~__~]<-_I
                '>l !i~~<^+i~<I:>~_,_<~+;~-<!:'>'~i!+>;~_?+<i>_,_l+~!>[~<                              .
                ^,`.''```^`''''''^,'`'''.`'`'```'^'''`.''"....,'' ..' ''`.
                l__!l?~~+]<~I~<<+-__<+;~,i~_<-]_i!]->?:
                      '                '.   '. .        .. '
                 !~I ^->-_<l+<_+~+;i-+:[I+:]~-_>?]_?}_![]_<<<.
                 . .    ... ... .. .'`.. ..'  ..'...'. .. ' '
                        '"                                                                  ."
                        ^:   ,[{,'                                                          'l
                        `,   ;tf}?.                                                         '!
                        '^   ,-_'                                                           ^>
                        `"  `;".'`'^^``'..."^^^^^^^^^^""^```^^^'''''''''''`' ..  '''```'''  `l
                        ""  '_{?[]11_1][]?}i^`````"!`^^^^`:I^^^```I,``````!!|iI?[ll^^^`'..  'I
                        '!   .l{)?-!^>[_[]-;       ;      ^,      ,`      :`_-i-<'; ;;IIlI, "I
                         ^;,^'"i!l`"^;<;li",'......".  ...,, .....:^ .    I '+l: .l.<+<~[[~,l.
                           `^,l":,I^':::;;;'^I,;;I"',l;:;!"`;;IIiI`"i!I;l,';;^,,!:,!:;;l^^^^
                             ~^_<l`~;iI--:I:i"+<_`<">^--!"!lI;-]`>">"-[[^_,i;]>l:l;;+]1"+,
                             ~:~!l,~;<l<-Il;i:<!_"<,<,i~>:!!!l>?:<">:i>-^_:iI<!;;iI;!i]`_:
                             ."^!!,  `^'`"^  ,^^`". .^'``"  ^^^`"'  "''.^. `^`^"^  ^''.^'
                                 `:,_+-+<_l!__-~_??[+>}<<<:
                      `.          .``'``^^`^^.``^`^"^^^'`'
                     '~<_'i>><+!.~>+i~-~.!:,?+^i-<<~<>iI_+_<_>_l+---_!!{>^~+_>?~~i^_><__!"?~+:_+Ii~<>+<<+^<^
                     '~~+~-<~_l>l!<+;?<<~~i..'.'''''``^'`'`''''.'^^``. `` ^^^'^'`'.^``"^'."`^.'^'.^``^``;.^.
                     ';:l:lI::':"^":':""I;"
                      .-_i:+<+>:~<_+<_+_>+~_':___~~_--]?I??_<~:
                      ']+~["^^^'^^^^^"^`'"^`..''^^^"^","'""',`
                      .l;i+
                             .^^^.....`^....'.'^"""""".''.'`.....`^^"^^^^^^^^""""""""^'
                            ^I^:;-]]-[+>[][->?+::::;I!(+-}+!--_--::II:,"""",";;;I;;,l::;
                            I  ^;>--~]~I~<+<;~<^``'`':}!+]+i]]-__,""";<?>_<!~,l>!+i?<" ::
                            ;  ;:1<+}~l}[][-{],-)(|)(;<1+<""^^^``",,:l>~i>~1t(n\[f~->, ^;
                            ;  >;jr|f\:l!i>;ll":I!!li"!>lI,,,,,^^^````'`^^"!l!>;,I^.I: ";
                            I  I  `.'^                                              `, ^:
                            :  l                                                    `, ,I
                            "  l^'..'^'''''`'.'....`^^^^^^""""""^^`````^^^``````````:, ,l
                            ,   '>{[_:>i?>_:<[?}[](I.'''''''''''''''''.''''''''''''''  ,l
                            l    <)):,:)x_~;<:,,,",'                                   ,I
                            l    ~~?'>;>\<ii<^ ..`^'  ```` ^`"''`  '..                 ":
                            l    ~-_+-}}l>1+t-^1n){f~:(+{_-tj?~)x;I(]];'">:";^`l:      ^,
                            l    _|[-;>}+{{_![}x?i.<l`,;I`__<..i+i"<_~l ;[!;<:"_!'     ^,
                            l   .1)}1-;+1->[[x[~.`"":.                                 ^,
                            l    '''^'.. ^..:"  .  '.                                  ^,
                            l                                                          ^,
                            I                                                          ^,
                            l                                                          ^"
                            l   ,<>;                                                   ,:
                            l  '>;:,^^` .'```'..'`''.    .`..   '.   '''''``''''''```. ,:
                            l  `` .'^!i/+:''!i]_".'I<}f}[~<]-?|_l+_[-`.I"..'''l^`^"""' ^,
                            l`  "?-+ ;":?}-l;.;}?<""~+{[1<:"?{){>,+1+>i;">_~<':        ;"
                            .::^"Il!"I,`Iii;:^"l!I,":,":;,"';II;;`,;;:;,^I!!!,"`'''''";"
                              .;l!!Il^lii!!:`lllI;,^l!!ll,^!l!;I^"lll;I`"Il!l!^:I!!Il`
                              .~"]>.ili;}[^l!lI<?`~I:i]-`~i,~[~,i>:]1<,<>"}+;;i>"-),~;
                               ;;:::;';:,l::';::;;:';;;;;"`;,:;;^^I:I!I^,lI;:I`:;;lIl'



















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


                                                                                               ',,,^"" ;'"^,.
                                                                '`'.^''`... '.``...'' `.'..``..<?-?+_~'_l_i["
                                                                _{_i>~>-+!i^-__-<<?_>i~>~<>+_><l"+~+~<-+<>>-`
           '`''''````````^^`^^^``````'```````````````'''''````````''..'..''''..'''''.`.''''..''.'`''`'`'.`''
           ^,"""",^`^,"^""^,""""`^^^^^^",",:,"^,,"",",^^^^,"::,,,,:"""`^^^^^`""",,:,,::,,,",""^,",;:,::;I;;;.
                  ;_; '?I><">>l"<llIl^Ill!;.l!-:,!il!',!ll>+;^llI!"!l^<!,:l:i":I:I;ll^;!I;l`l"!^lI^;l,;.
                  :l, .;";l'"::^l;:::'"::;:'lIl^`;l,I^:I:,,!:`;I:l`:I.;I^"l:;^l,;~:l:`;;;;,^l,!`l!`:>;I'
                      '+! l-_;i<l~;;IIIiI">l;lI"i!;!"" "+~!`i!!>,iI;I<,Il<^`IlI>^':~i^li;i: l`i+",i!Il:'
                      .!<<??i~i>i+Ii+l<+!I+<><!:;<~-]>l><<>ii+<!l<>i>>:><>>l~<Il^^`;l`;!"I:'I':!,"ll;l:^
                       ^::i, II,:i^I!:I!,^ll:l^` ":;i^,l,,l~^l!';lIl!^.':!!Il,^
                      '~i_"l~I^l;:ll!:I'!I!l"Il>;lI:,^;Ill: :;II;!::'I";!;I!"I^I^lI;:!!<iI;l;;il;^.
                      .l;!^"II`!:;!lI:;';^;l,:lI:l:Ii,ll;;l`;iill!l;'l^;>II!;!^;^,;I`;II^"^i;IiiI"
                      . ^;^l:>l">;:lli;i>!,lI,,llI!^lIIlI!:.>!I'>:';I!!l^Ii>I,.;"l;;!;;lIlI;l;,`ll~l:<!!^"iI'
                      ..,+i+~+~^I,,I;;;;I;"I:,:;;;::I,ii;l"`;;I.:,.;;lll"lIl;;^I^l;,;l:ii~;IlI<:l:!l,;l!::iI`
                        ">!!iii.
                      ..`>:ll^ :~i!:"'!>!iI"'l;!"!!li:^IIl^;I^;!I;;:;!I:^I^!I:
                      .' ;,;!. .:,:". `"I!; .i;!.^,:i" I!<;Ii^;<l!+;iii:^~:i>i
                        l!,!'><;I!:"ii!l`I`>iIIlliIl"'~i!!"'l>I:!`;lI;l;l'
                        ^"`;';:",;"'I:,;.;';I;ii:lI;" ^";;. I;,"l`;IIilI;'
                        lili>^!<l!i;:>>l<`>~l!^<Ii"i<!ii"~l!!i`l~!I!";,;~><<l<~i>'ii"ii!I">>"IllIl
                        ^`":;`,:,^:^`;:',.:,":'^":.^,^,:`:^,:".::"":'^`^;::!^:;;, lI`l::,'l:`:;:I:
                      ..^?[_+I`.~}+i;^._!<`<}+il"`iI'"I!!_"!i~;;~:!+<i+!<_~i:_:<~>
                        .^^'`'. '``'. '"`^ '^`.`  "'.``^`"`^^,"`"'`^"^I`",,^`;^^",
                        !!i~^<~<~~;I-_i<,+:+++-<i?~~l'?{+i;`i?>I-!l-<i_-<i
                        ``'`..^''^'.'''`.''"``",'`'^` .'''' '`..^''^'^`^^'.   . .          '.
                        lI~~+,_+<<_!;-~i_"__+~,_~_:i<<_~;?+~_<,+]~>_I~I<[+-[~-[_-^?_,-i<<,?{l><<+i
                      ';'`^^""'                                          ..` .   ..       .  .  .
                      "~>+>~+~l
                                 ;"':;:`,;:^              ..'"  ^,:`;,"'",,"`,"" `""`'
                                ._<;][_;_]+<              `^"<. l_l,ii+;<?_l:?<~^!}_il
                                                                " i"^!l<i,:~i!>li
                                 ;"';;:`::I,                 '  ;;!;!i>!<!!i!<<+:.,,^`
                                ._<;??~;<__+'             ^",+' I-;,il<:l++::!i<;,{[i<'
                                                                " i,^l!><:;+ii<l!
                                 :"^:,,`'.^::"            ..'"  ;:!;l!>!i:;+~<i<i^`
                                .~~Ii~-l>I>}]_.           `^">. l_:,>!~;;I:-_~:+_<!`
                                                                ".>"^ll>>,;~ii~ll
                                 :^',:,'"";"^:,^'""" .^.  ...^  ;:i;!ii!>li<!<<~I^"^'`^^' ^^`'   .'
                                '-<I-]_;<_-~_}]>!]_-:^+^  `^"i. l_;:ii<;!__":!!i>?}?l-[?-^?}<i^^ ,<
                                                          '`"l  "'~^"ll<!,I_><~il
                                 ;"^;:"'^::"`:;,'         ''^I  ^';!l!!i!,,l;IIl:
                                .+il]+l,l?->:--+:         `^"!  `:`-ll!!`
                                '_>!!>I,+_+I>--iI<<>:     `^">. ^:^?!lli"
                                 ""``"`^,::"";:,"`,"`      ..`  `"'l,"::`
           ;,l+I~. <+>__<_!:>~->+
           ..'^'^. ..^;:^^'.^";"`
                .--<_:>l>_i+<,<~_;i_+;>_[i>!-<-;_->:+-<>><ll}_~I+,]!l1}!<_~]ii~>i-?_+I+__<+,<+-l
                 "''``"`^!"^`.'^^'^`^.'^,'^`'`,'`'^.`^^``""'``''"."'.^^''^''..^''```^'.^:",'^"^'      .
                '<"-~<ii'?l`+:--_~~+_^I<->i-+^;_^;-<>>~I+_I__,_??_-!_i?_i!-+}_~~~_,->~l+!~:_!]-;ii[-+i<++>
                 :"^.''`'`"'`.``'^`"'^'`'^`^^'``''``^''    .. .. .. .   . .'^  ..^.'.. ..... .'..'``'. ..'
                 >i<:i~+<_-<!I-!<_+?++li>,~-~~]++;~->~_.
                   .  .`    .   .       `.. .`'...` .. '..^`' `.
                 .i+, l+<_]i!+<<]--;_-i>-_]!-_[~_?[_[1l<+i_~>i<i
                                     ..   ..
                        `l    .'                                                            .:
                        ^i   :1);^                                                          'l
                        `I   ,tt?-.                                                         `i
                        `;   "~+.                                                           `i
                        `;  'I".''.'`''.'..^``^"""^^````^""""""^``^``^^^^^^' '`''``'`^^^^^. `l
                        ^;  .~}][[1\~{?[?[1i'''```^!''''`^;l^^```'I,`^^`^`<!/<<}{l>`.'''''  'I
                        .!.  .,{{+_!^!]-[]-;       "      `,      ,`      >`<_>+!'i l!l!i>; ,;
                         ^I,^'^<il,^',>;Il^"' ....'"..'...^" ....."`  .. .l.'~!" .;'>~ii_]<:I.
                           `^,l",:l"'""^^",'`;,::I^':I::;I``;:,";:`^I::,;"^Il"",;^^!,^`:^'^`
                             >"?<I^<:i![_;l:~,+~+^~"!:]_l:II;!?]^>^>,_[+^~"i;?<!;!;;i+["~"
                             ~,_ll"~I>l+_;l;+:<i-"-,>;~~!;ilIli-"<"<">+]^_:iI+l,;~l;i>1^~,
                             .:^",,. ^,Ii""  ^`^^"  '^`'``  ^'''^` .,"^^,' ^"^^",  "^^^:^
                                        ,"I+++!-+<l<<~~?_-[!>ii>l>i
                                         ^^^,,",":"^^"",:;;,;;,""""














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


                                                                                              `"^"`^^ "'^^".
                                                               '....... .  ..'' ..'. `.. .`'. i[][++i'<;]}-^
                                                              .?[_>i~<-+>!"?_--i<[]<>+>+~<-_><I"_+__+-_~~~?"
          .'''''''''''```'``````'''''''''''''''''''''''.''''''''`''''`''`''`'''`''..' ''''..'`''^.'`.''.`''.
          ";:;::;;;;;;::,;:,,,,:;""`^^^`",::",::,,,,,,,"""",,::;::::::;,:;::,::::::"^"^"","",;:::;:""^":",,.
                      !Il :;Ill, l;l;;l;.:":<l':iII!I;,,lIl:!;;^;:;;I,,i; :;I;lI:,.I:;I:".;:I^I;^:Il,;;,,.:`
                     .<>~;<<<_<!:~~_l?_~;i!:i!^;!l!iil!;~!>!>ii"li>>>:">i'i<<!<!!;`>!l<!:^<I!^l>;">!l>iI-^i,
                     `+i~!~<i!^>;Iil"!Il~>I
                       l!:'I,;;^;:;l:I:II;;!.^iiI;Ill;lI"I::!!";;
                      `}-~i~<>!;ii>~i~ii!ii<'"i<>i~<><-~:>>l>!!i;
                      '><i<;|"
                            .   ......        .....   .. .. .....
                             "::;II;;:",,,",:,;;IIII;:",""",,,,::;:,,,,""""":;;;;:,"":,'
                            :: I;{/t\t{~)|\]+/{::::,";/_?(]i(\)){;""^^",",,""",;"^",;:'I^
                            ;  ",lIIliIlii<!!>;;!Il;;,ii<<!:I;II;:::::>)+??+)<}{~1+1-: `I
                            "  !;x({j[!}1}1-})l>1(|)\!}}}[<"""",,;;::;;::,l1|\n(]|!:l; ^I
                            :. l'<i~]..       .            ................ .. .. ..^; `I
                            ;. I                                                    `: `:
                            ;. l..         .                .......                 ^; `:
                            I. "";!!!:I;iIl:l<!iii~:^^^^^^^^,,,,,,,"^^^^^^^^"",::,"",^ ':
                            >    ~|{i;<?\_[:~[___-{;                                   '"
                            l    +_? ,^_\+lll                                          `,
                            ;    ?~_~]_<]!-?[+'~{~?-".?<]_:]?+i>?..+i, .               `:
                            ;    >(][:[1,-[~[?l\x[l\-,-I[l1/rI;[(-:|)1~.!|+;-l"[~`     `,
                            ;   .))]}~;<)?+[itt(";'^". .  ...   .'  ''' .`. '' ^'.     `:
                            ;   ._~i+!^,li:!](I`' ^::.                                 ^I
                            ;                                                          ^;
                            ;                                                          `:
                            ;                                                          `:
                            ;    ^",'                                                  '"
                            ;   ;-?_'                                                  .'
                            ;  ^l^^^,lI!l:^";:;:"^^;:;;:;;;IIl!I;I:,:^^::""^^^:^^,,,,` `,
                            I   ."""';l|-!"'l;?[I`'>+)x1(_l-[{j{;i-)["`:"`^`^.~^..'''. `:
                            ";' ,[--^"^ i){i; .-[-;:>!>~-l" +[?+; I[>_+,"<[][^l'      'I`
                             `,,:`^,"^":"":"^,,"":^^,,":l:":"",:^^:""":,,:^",:"";"^,:,,'
                               l;_<,i:>l__;l:!i~+:l"I!~<:!Il<?<;I;l~?>;;lI-+!l:;I-?l!^
                               i:~i^>!~l+?"!l!i>-"i;Il>~"<>I<+~:!ll<-~:!i;+i;lll:~?:>:
                               ."'`"' '^`^"' '``'". ^^''"  ^''`"  ^`''"  "^^"" .^''^`
                 .'  .'....'. ..     .       .           '.          .                .
                 +]^ I_<]_:--il1~<~<;<]>-Il_?1,I?_~?'++iI_[!:_~~-;-i;-~:~+~_;+i+]~_~,~-~_!l_I+:_>,++]<+`
                     ':`"" '",:,',^^`^`'"^"^^ ''^^'''.^",""'"`^'"'^"..``^^`..'^;l`""^:'^`'`^`'`^``^'^^``..
                     ,<>~;'><+]l'+il<]:;?<!><`l_>~<;".i<+-;^_i<i[:i?!^>?<-<l',-?-!<+>?:!+i>_+`_+<<~I"+-<]!I.
                     'i]?~i_>_!>+><_<!-i^<_i<i,.I><-++!`
                     '"""'^`.''.''`"`''"`^^'"^`.'^^.```'.      .         . '
                     ;[_];-~il_~~_--<!,<!<+!<__~_<_<l<<>]>'<--__]+l_<+!+;i;?_!<[~<_:~_+~+?:
                         .  . ...'  .     .    .   '     .      ..             .     .. ..
                     '.:}?+-;^`?]_i;^,?>+^-1_>l,';<, +l-I>-:>_?l!-;>-+~]+_[?>!?;i~<
                       '^''.''.'''...'`'` ```''.''^.'"^"^'^'`":^'^'``^^;^^^^''"'.'`
                       <I<<,]+<+_:l-+<>:~,]__-i~?_+,`]-<i:'<-!l-l!-<~--~l
                       "```'."````.''`^'.^"``,:`^'"^.''.^'.``.'^''`'^."^`''''''' '. .'...'"......
                       ~;~i+"?+ii-:I_i<~"_~_i;]+-"><<?~I?!~-+:__~<-;~;+[?-]<---<^]!;_i+!;][:<<~+!
                       .`''.' '`' .. `''.      '..           .            '
                     `.:+~-~"'!~_>;"'<~_?;'_~_;l<~_i^^>~]I~_,-__?}<]]->i?I-+i
                       ^'''.^^.'`.''`..''."``''.'`` `:,,,^'`,^```"^``^'^'  ..
                       !;ii"?~i>+:l_i>i;<,?~+->~_+<"`i>+<^^_]I>~^~~+++_~.
                       ,^""`.;"^^"'`"""^.::^^,I^^.:"^^`.,^^^'.",^^^.".^^^^^^,:"" "`'^^^''":'```''
                       l"+!<"?<!i~:;+>>i,+~~i:+<<"~l<_>;+>>~!,__i>~,i:i~<~-!-?+<`?I:+i<:;_~">>i<l
                       `^.'.' "^ ... '. ` . ...'.. ` ...    ..   . .'. ''..    .. ''    .. .. ....'...'''.
                     '.!~__i>^-;"+<?l~_,_-_]_!-]?! ~I_?+-?~--_I,~+]I~?l,-;^+_~~~l_[>>?I_?]?-i?<>-~l_-]_<>~[^
                       >_>i>i+:>i<_~;<~?>~l}~~'                                                      .    '
                       ``''''`.'..'`.``"``.'``.





















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


                                                                                               .```'^^ ,.``'
                                                                .  .....    . ..   .. . .  ..  i]-]~+>.-I]_l.
                                                               .??+><<<?~l!^?~--i<]]~>~>+_<_]+<>:~__><-_>>+_`
           .''''''''''''```````'''......''''....................'``'.'''''''`.....'. `.''`'..'' .`.'`.``.'''.
           `::,,,"""",,^,,,,,":;;:,,,"",;;;;::::::,::::;III::,:II;IIIIIIIIII;,,,,:,,:;IIIIII;:,:::;;;I;;;;:,.
                      .~;lIll>:
                      'l;!IIii;
                                 li;<^i+~I:~~>'           .``!' :l!,><l,"i<i"li!;.i!!I.
                                 l!Il`!_<I:~<i'.          .'':' ;!l"~~l::>+<:i<i!^!i<i.
                                .>_l<"<[-l!?__<-          ^:"i' I~!,[_l,:_?>,<++!<<<_,
                                   .   . ... ..            . '  ^^;",I;lI:;!lll;!` '`'
                                 .. '. ..                       ,^il">i~>;;+<>i<>
                                .<~!<,-->!,!;]+?>>.       `,,<` ;~>;]<l:":;-+>Ii!+!,<.
                                 l!;!,<>l:^:,<ii;Ii"      .'`I. ;>I,<iI:":;<<i;!>i;"I.
                                 l>lI"~<l:"l:_<<Il<,      '``l. ;<;"+>;,^;;~<>;:>+l:i
                                                                ^ !;^ii<>,:~<i~i!
                                .Il"!`li!,:!ll`I!I^;Il;.  .'':. ;li;>i!lI!i>;>><I:;::`:I;^":;I.
                                .!>Il^<_<;l~><:<_<;i<<i`  '``!. I~l,-<l::<+i,<~>!i!<~;~]~I!~++"
                                .<_!<^+]-Ii]~~;+[_Il<?<l-.`",i' I~I;-~!";--i"~__i!~>>;<-~;<<+<^
                                 ``^..`"^`'"``^^,^`^^``"^  ..`  ":;^;;:I:;ll;ll;!^^",^":,^""""'
                                                                :.<:,!i-+;I--++~<
                                '~+i!I+<-i>[}iI[-]I       ^::~' ^I -<!l!"
                                 '.'  .^^^`""^',^"'          .  '^.;"",:^
           ,:^!!   l+i!-ili"<__>:<>l~<
           `"`:;.  "i>l!I;]lI>!l^iIIil
                 ;l:`:,,:I";'"`;;`l:'l<!;>lll^;:;:l;:"^:";l'
                 ^:I:I!;lll!^il!i,i>"i>!:!I!l"~i!l+i>I:i!<-"
                  '". .:``^."``'"^` ^' ';^" ""."".
                  l<, "l!<_l:>lii!>,i~<;~"i:~<!!I;
                      '^,l'""^l::I,,:"^;'l:"`",,::;:::;:"
                      .";i ,;,i<ii<li::l^li;,lIll!~Il:l!;
                      ^:,'i<;l;'!lI!lIllIl':Ii:Ii",II`::I!l!!;l^lI:;i^
                       "`'lI";l^ll>!>>ll,!",I!li>:,I!"III~Iil;_:!:!>!^
                         "                                                                   '.
                         l'                                                                  ;`
                         ;.                                                                  l`
                         I'   I+                                                             >^
                         I' .;+:`'`````^^```````'''''``'``'''.'''''''.......'''...........   l`
                         I. ,]^''^",l"^``^";i^''. 'lI``^``^i"`...":i`.'''',l,""^`^Il,"^^^^`  ,'
                         I" ;.;:I   " ^!!; .";i!!~;"";l`II^; '!il. l;l,::"", "^`" ,"         !'
                         .Il!`il!...;':+>;.`"!+__}i^"+-i>>;,.`i-_^.Ii-~<-l:" >+!I ,"      .`::
                           i,^":,;lI",I^^"I"`^"`^`,`^;",`,"`";^";!"`^^``,;^,;^""::":;,",l,,,'
                          ": :iI?~^!:!:+-+"i,~:_+i;II;~_?"i^+"_[~:!">;??;lII;_+-:~"i,+?~:>
                          l. ;!l<>"!l>,~+?^<;+:<~i;!!:<>-^i,-"<_~">:>;<?Il<!:_!>`_;~^i-_^+
                         ,;.^'::I;l:.^;""",' `:"",,  ,^``"^ ':""":. ``''^"  "^!}:` `,```,.
                         l;>-l~l_-_--?i                           <~+_!->ii?i+~;I.
                               .                                  ^^""""",,",""^"'



































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


                                                                                               ^^^^'" ^`'^^'
                                                               ......... . ' .'. ..' .... ''' "[]+]!]'i!<[]>
                                                               l[?~!i++?;_.~_--_l]{~i+<~_i+?_<-,i_<+~_+_~<?~
           ''```''`````````^`''''''''''''''..........''''......'''''''''''......''' `.'''`.. `..''.`''''.`''
           ^""^^",,",,",",,"",""^^```":;;;:,,,,,,"",,:;;;:::;IIIIIIIIIIII;:,,,,::;IIIIIIIII;:,::,:IIIIII::;"
           !.:l!  '>>l!;!Il>l`l!ll<!l
           ;`"ll. .lll~l<<!+<`IIi>~~~.
                 .`.  ..  .  .'" .   `^''..''.
                 "i<' !<-l<?-i;-]_!i;i><-<+<_;
                      "'";I";:,:`,"'.^``^'`'`"^'^.`^````^`.'``''`''.'`'.`.^'.`^.'^:'.'''.^ ^^^^ ```^
                      !;I_~l!i!+Ii~!:<+I~_-Il_~i!:><_>-<-+^~_>_~>__i;?_;>---<l]!:~-;+~+l!<^}]?+'+?+?:
                      :^,l:`I"""','^,:'^;^"!;^
                      I:"~l`iil!"!";;_I:i.!_!i
                      !iI'l<;`;:;,lll':l,I;,,'I!,;:^;;;I;!I;",Il;,:>;'
                      ^,l,"!,^I;,;!;!^;<Il~?!^iil;;:;iiii><!;;!~i;<+_^
                 'l;  ;:,';`",^;^"`^":`
                 ,<i  :;<^ili;;!!>l>i_I
                      :`I>!^Illl^;:`:,,:;,I;';;:>"I:,!::,,l::l;,:l,^:,,`;,"!I^"^,""""I;`"""""";""",,:^`"""^:
                      i!<?<i~il?~>+!>>_!~i~>`;!i+l<>l~_>!l+><_~<i<<l<i>Ii!!i-l<li>ll<--I__~<!>_<!+<l+<!>>ii!
                      !~>i^!~; :<>l<:ii!"~_~_!;;:_i~>"i>>"!!~l~>_:`>`!i,+-<<l!-~i
                      :",^^."^"^',,''"`^"^"''^"^`^`.""'`'^".`",` ^^^"`.^":`"^"'`^`.'``..'''''`
                      !Ii<i;<!+<~~?:I}+~+-~I>_?l>_?l!>l~~1iI>l_~'?i!++;_-[!i--i_~_[!!<!i{>~<__.
                 .^`  `'  ..  . ..'.. .''.'.''    ..   .     '..                  .
                 :?~  li+__<~<_:~I___!!-?>+l!_~-+__-+Ii?<'<_:?-I
                      :^^^' ``^^`'^`"'^`.``'.```'`.,,,"^'^'"^.''`^,''`^`^'..^.''..'''`^'',.'...''..'.  . ..
                      -_~<_l~~~~~I~-_!-+li~I!-?+l~I__~>!I~><-l+]?<_<-_>i]:;"i;_~Il~-+I~~I~>~~]_+_"~__?i][__^
                      I><;>_;:<~;i<Il+li?ll>l"!+?!<,ll+<<,_>,~ii<l l_l~<`!l+!;i^<<<l!<!:+>I+~l'+i!:!!II_]<~l
                      !i<+!;~i_li:il_~i~l!<<_i_~<!l>+-i_Ii<~>l;?-+;>_><l<<:I<i<i><Ii~!>l;>l+~;i+>!>~<>i<ii<:
                      >><~_i>l~!<i~!>-i:",::;;;:!l,;;;,;^;;;I:^l:l":;i;":l":!;,!>l^;lI;,"I;!!"!l;^!<li!i;:<:
                      IlIIlIl^"i<;!; ^
                     .I',II!l,, ",";::I:Ii,^;:;"I;;I:l;`:;I^,I:I;I`;,:!:^::,::::::I^,:,";:^:,::`:,",,::"'l,^
                     ._!+~~_+ii:~<~_<!~<l<<l<~i!>_~<_~~!>i-!>[+-~+,-~!<~;~<i>i>!__+!<;+~_~l++<+;<!_>_<_<,-+I
                      >_::<+il<:~++<i<><!!<<+<<>:!l;<>;~-Ii>>;<i<l->-~^i"<l~<i>ii!~_?`.~l>;->:<<>;~<~<~_?:il
                     .?~~~->i~,[<!!+_"                                            .                   .
                               ^  .
          '!'!!;  ,_-lI;li!I;lI,::^iI;,>;;;I.
          .l`Ii!  ^__~<><!->i_><~>"i<~>+>i!+'
                 .'   . '     .  ..  ''     ... . .  ..  .  ..'..  .   .   ..  ..     .   '
                 ;~i '>I__:<-_]<_[>>:~}!l?_+-:<^<:>~__i_Ii-->_]il`~i++<]"><>+_`l~i,_~_~i-l+]"i;I>ii>-]I
                     .l!<i<l_]>: ;+<<ii!i':;>i`<ii<;!<>_i!l_<I:!<<<!>;>~<!+~<i:>~i><;i~"ii!i<+_>~:!i>i<>!.
                      >i>!?>Iliil"Iii+i;~l!l>;<]l;~!!><i~l,iii+>_!i<]:<?~l<i<i,_<~l+l;>!><<>i+[<l!<~!!l<+l'
                     '_i~!!>!I>__l+Il!!;>+~>+;<iIi_>ii>;~iI!i>~_>";>~;!+l;i><!:!i+;!+Il<~_>i+;~i"~>><l`!i+"
                     '><>>+"!<iiil-_!;:i"_!i<~~ "li>~,<_+~~l<:`+<,>I;i^i>~~>~_i`!>_!-+i<;>i"!~I>+`i:!~<
                     .!>~<~<<l??i<lli:?>++?<~<'[><:>_+:~~~~~i-!!~_+~+]_"+,?+-?_+<~,<l;+-:><>~<[il>~+;
                      '^^,`":'^^:^''''```':"^^'`,'...' ..'''.,`.````^;`.`.`^"'""``.`'.'^'^^'^^^`.'^^`
                       ^;~?_+_~I+]I!++<-I'_-~_~-!
                     .;^"^ ^``^^.`'':`^. ^"``^`"``'''`^''^```'.^^"'.`^```''.`^^'.'''`'. "^..'''^'..'..'.. .'
                     `[~_-^l~<++i_l:_~_`^<-~+~>+>]!<!l>~:~<<>-:_!~+;<-~+i>lIiI<+;_<++l-~_[!ii<I-_l;><+_i<">I
                     '>>"'~>~ ;<+^'.<>~,I<<+~_-]^!]_'i~i!~_<<-i^_>.-_+~_~<+,!<>~:,-+~~`_<i^_+"i!^+!<<+~+~~-"
                     'ii_>+<-_<l`.  ..'..'''``,^.'`' '`'.``'``'.``.``"`^,`^.``^`..^'^` '^^.'^.`^."^^""""^",`
                      ^`:`,^^:^'
                 :+; '!>:;".:;:::;^:"<l"i;l";!;,~<I:!l<:;;:;;:,:^I;,il: l:l:`iI^"::::`;:,,i;,:,'::,^ll`;`
                 :>; '-<l~!;<-~+I?<<li-;!!>:I><l__i!>i>lI<i!_<;>:>_!~<!:>I><;~_;!-<i<:]~~<~~i!i,!+<"~i^~,
                     `~<:;+!l<^+lli+!;ilIil!_i>i^i<];~"l>Ii!!+:;+i~i>~I;i'i<->>~?~;:_+>>}<<I._!<;<~I
                     `<l~->_i:~+->~+<;;<_-><_;~_~I]'?::~:{;,];>-l~:!]~">il<:        .       .
                     ';`"I`"'.`^`^^`^'`"`''''.`^`'".^^." `'.^.`^.^.'^'``^"^.
                     '-~!+_>?,i<:_I!!I-_!__iI~<><l~<<_<i_~i->~!>~+_+~<~_!_<l~+~__-?_<_<?-_~ii>+~>+?_i:_~+-?,
                     ^+<~~-<li<I_+<~?<~" ... ....  .  . .. ^`'.........^. '.''.'''''`'."^''.'`''.'`''."'''`.
                      ```^`` .`',^^^`^^
                 l-; '~!l"<I!il^i!!`I!li:i<<:_i;+<~;<i>~:illl>,l<:i;I!!I:^l:;i:!;l~~:!>l<:l;IIIi!I:
                 ;l"  ^"I'::i!I';:;';l;:`;:"`;I^:,;^,,,;'::,:l`::`";:;:;^',:II"l:,!!,"I:l^:;;;!Iil,
                     '+:^i,l"">l^l;;l^!I;i:i!:`>>>,>!i;,,;lI+<;lil~:l;ll>+i!:l^IlI! ^-lI";!i"i;>.!I,ll!l!I;
                     `<+i~;>>!!!l>><>:!I~i+?~_><~ll!<~i~I>_~]<i!ii<!l;:;lIlI"I"lIIl'"lII";I!,;Ii";;^;I!!;I>.
                     'li;!""ll^iIl;i;,;`<iiII>il:'I!;l,<l"li!':II!>i"
                 ^:' .,.'."".`^.'' . ^` ' . '.',^^. '''  '^  .''. ..``' '''`.'."'.^`''.`.'..''. .'.''.'''.
                 i]; ^]__~+~!-~<<<:~i~!l?:"i<i-}+<":-<-<<i-+;+~_li?><i<,+?_ii?;-_i!<-!l<_~~++-::]_l<~--_-;
                     "<:+_:!?i>~"_+_,+!^!,_{__`
                      ...'.'`..'.''^.`' ...'..














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


                                                                                               '"^"'^^ :."^^
                                                                ''..`'.'.. ...'' ..'. '.' .`'..<]_?<+<`+I??-'
                                                               .?[<!<~<]~>l,+_+-i>]-<i~<+~i+_>~i:-_-___+~!_-'
           '````````'''''```````^`````````''''```'````````'''''''``'..'.'''.'''''''.'`.''^`..''.'`.'`'``'`''
           "::::::"^","^^^^`^^`",:,::",,,^^^"`",,::,,,::,,:^^`":::,:::","^""""^",::::::;;":,,",^^^::::::::,:.
                  l_" ^l:^IiI;!;l`;,,l;;l~ll"ll;;'^lII,:iI^l!<.,lIiI: ;^l<l"!I<:,;:"!;:'.>"I;,">::'"":lI::;'
                  ;l" ^Il~i~!+<~_>i!;-_~>~ii;->~>;<<+_+;<~Ii-<lI!i>;!I<Il>-i<l+i;+>><~>:;]Ii_~I__~:~>l<<l>>^
                      ^<I_>~:-~~<_+_:<_li_:<~<_~<;<:>~!;_!>I+i~:!~<!~-li^ !:ll<i<i!>l"i:?i<i~~+,!i^<~I
                      "_[<-+?-~.!'l<?!!i~ii^iii!+lI:i<::<_>~+__';]!~+~i>^:>i:+!^_>~~~~~i,_:!<i,i!!>l_;!><_^
                      `i!!!~~:i<_i<~><"<-!>>,_<<~~<i>+i>ii-i~~_,!~<I>>>_i>-;>l!~i++<~I~:i>>+i~;<<ii-~:+;>".
                      :-i<:";`;II:I;;"';;`:I`I;;,;;",l;II:!,"`;";:l,I:;Il:!^;^"!,!::;'I^i:IilI"I;l^ll^<^!
                      ^i:<,
                  ^:. '"` '``'.^^"^''^^^'``^``'`.''^'.`,"'`'```''`'''.
                  ~}: I[<>+i<[;+l~?l;~>>;_~<^"!'!~i?+'>+?<++>l+i<_<i<!
                      "lli         ilIl',,`,::;^,."^';::"l"'!,Il^";;,:;`:;;';,:^:l;"^:^:;I,,:",'",,",^
                      :<ii'''.  '. ~>~i.^;.>lil'l^l``~i>!ii"_:l<::<<I><">Il`<l!">~!ll!I<>_l!+!!"l~i!>!
                      :_?i_+>[" `  'I':_+<~?<l:+>">+!i<:<?[<i~!<~_<l<>i;!+!<~;i><I,;`!"><<>~_~!!<!,><!+~I+]+.
                          .        >_-_~_~~;!?-i-_;_~]l.''.'`''^'``'``'.'^.`^'^'^. `'` ^,"^`'^^.'^'^"`^^'^`'
                      `l!:,lI,:l'  ;,::,;:;I";;I::";:l:'`",`'`''``''''`.'.`''..''`'  .`..'.`"..`^....'.. .`^
                      ,i<~!i<ill`  ,<:>1?]+~_-!]+!<?<?_l+-_~~_i++-~<_<i;~_<~-!_<_,;I">^+-]-_?-~i]~!~-~?-l-[[`
                                   ~>_<;<!i":<i!~~^l;<^
                      :~>?<<`   '  ^;.:ill!+ilI+;"!l;!i;i+_!iiI!><Il<il,!i!!>,i!!;:"`I"l!ili+iI>~I:>iIl!,l~i.
                      '"",.^    .  i?~?}}]-i_}+]]~i-_}>";;::lI,I;l,:lI:^;!:;l"l:I`^,^:.Ii!I;IiI:l;">i:!!,!!I.
                                   ;;;;";:,'`I:,;;`:,!^


























































```

*Figure from page 20 (2346x3317 px)*
