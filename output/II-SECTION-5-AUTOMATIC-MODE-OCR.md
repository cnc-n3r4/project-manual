# II SECTION 5 AUTOMATIC MODE OCR

*Converted from PDF: II-SECTION-5-AUTOMATIC-MODE-OCR.PDF*

---



4203-E P-76



SECTION 5 AUTOMATIC MODE OPERATION


# SECTION 5 AUTOMATIC MODE OPERATION


## 1. Main Program Selection and Operation

In order to execute a part program in the automatic mode, first selectthe part program. Programs stored in



the memory have their own file names since programs are managed as files. The specified main program



is read from the part programs stored in the file and the subprogram, called in the main program, is



searched out in the specified sub file to be loaded to the NC.



For the selection of file, the directory-selection-based file operation screen is used.



The following explanation gives basic information on program selection operation. In addition to the basic



information given below, there are various functions including the function to display the registered part



program files in batch. For details of the functions, refer to III. DATA OPERATION, Section 2, 15.



"Directory-Selection-Based File Operation Function".



The operating procedure is described below:



{1) Press the AUTO key.



(2) The lamp at the upper left corner in the key lights and the screen changes to the automatic



operation screen.



Press function key [F1] (PROGRAM SELECT).



PROGRAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PFlOGW.I DATA SEARCH DATA [EXTEND]



Press [F1J (PROGRAM SELECT).


```text


                                                                                                .^`^'`" "''^.
                                                                  ....''...     .'.   ..    .   I}?-++_._:!}"
                                                                  <1[+<_+_]i<']_<_<[}___-:-]~??+"+__<~_-><~]"
           '^`````````^`^^^`'''''''''``''''''''''''''''''''''''''''`'`..`''``''^'.```'''`'``'`''.`.'`'`''`'`.
           '^"`^`^^`^"":"^^,,'":":;;;:^^^^```^^'^":^,^^^":;:",,::,:,^":"^""""":"";,:^`""^:,:;;;:;:::;I;;I;::.
           I)>{-<]>[[~_~~}_I'[,      ^[;!;+[~+>]+]"]:]~><~.I++>>ii>l~< :<!<-i-!<-^!!>_!Ii;>l:
           ictv||\_-?1j{trX?;X?     .|ufff<|[\|z0Y/c)|_xr\:-OJx\tv\tXj`1\tXt}0|nntnu(1|c1jxY| .
                 '     '                ..   '    . .   .^     ^' ^ .'. ".   `^  ^  .   ". .'
                    .

           ,<      <)[><>;"1<llIlll!ii'?<l~>I;<<l:l`"lI:<^i~I:;;:;!!:,I`
           "+"     ~x\t{[<I]~]1tX}1\1("))\)/|11||11l?r[|j;})v|/|[t\)()(> .

                 !,l>i_:ili~~>l<~;il+~!<i!_~+lI>I+<;i>+>>>->^!i!_!"_!<I~<<!l>il:i>!i:l>!i>`'<;liI>l!,!!l!!;l`
                 +i!l>~!iiil~~>~>_~_!!~_l]{i><i>i!!!i<<li><<!i>ii<Il><<~<<<i!~!-+~II>~[!+>l;+>~?i_><Ii>i<~i<^
                 <!!li+!<i>lI?>i:><+^!~l;i<!I~>>~!l!Ii<iil{_~il!!><I;i~i+_>!l<;ll<;.;;>:+__>~<~;Il+l;!l>]i_i^
                 i,"~+~`i>il^+i;:<+I:~l_-!!!> _+l<~"i`I<~._-^l~<l:~~'<>+<<i]<+_l !_}+_"<"!_~'i><!^>!~]~_<I _^
                 i++<i_-~;><l<I_[>"~__>{__:<>_;__;~:>_,i~+<~!i!!-+;+?>' .  ' . ..          .   .  ' .^.. . .
                 ,``^^'`''^`'^'''^`:``^'`^'^^^.'^.`'`^.`^"^^..`'^"''`'
                'ii<l_~:__-<_]>;I+I?-`-]>,]i+<+<~;~++<+_~l!~__-!>}<:++~i]-~lI?>~_~:<Il+++l
                 ""`'`^^`^`'.''.`'.'"`'.`'''`^``"'^"`^`'^`'``^`'.'''""`'^``''^'``'.'``^^^`   ..     .
                 ii_;~_+~-~+<<+_~-!?_<>I{><+!_-_>;~~<>i~-+<:!+l-i<]~~l,_+_~_><;i-<~<}>i^.>"_?-?>i:<!i~~I~+<>'
                .l>~ll>_~<:;?i~<"<>ii+'~~<~,li!'!+l>!!:<;!>ii>II<ii!~!il-i:><!l~i!"<"!~>i~i,~<l:<<<~<!>il>i>"
                .!l<>i<~"+-+>:~^i~_ii".<!<"i_~~<i;~l~_;;~>i+<>>l,!>-<,[!I]_^<~___l;-<__{_-[i+-"l?]+-~i;+,l_i'
                '-<~?i+!:I--i;i;<~<+>^^l!<,<~<-~!^~,l>~;>i!~ii<! :!!l l:`>> ^l!I!":i;il!l;;i!i',>!!<!I i'.!l
                 ">lll>Ii;,~~_l~il"i+~+~i::i:,>~i!~i>:;il!<<><^
                 I:,'^":":l"^'"^""":^"^`^`:""^::^"^^"^^^
                 :;<"!<<!>+!_!>Iii!<i!iIi;++~!i_<<l~+i~<.
                  .'  '"'.. `^. "."^^...
                 .!>" I<<-_i<__:-+>i>;_-~.                                                 ;;i,'^.:`
                                                                                          .-,<-)+1":
                                                                                          `< _tJ{C",
                                                                                          '_>,I,I;<;
                                                                                           ;~i~lI>>'
                  ^,. `;^``^``'.^`"`..''''''"'..'''.'."'.`.. '.'`. ...''. .....  ' .    . ..         .
                 .<-^ ^>i<;-><iI_l~~;>[+-<;__I>><~]:~l?~i>_-l![_]<l-<i<+<;]+_-_l!~+-~}-><<!?-;-<_+~+[?I
                      ,~~_<]~<Il<><~<:                        .                     .'         .   ..
                      `;^``^"`'`,`^^`' '^'. `^`.''`....'.. '...
                      I>i~_I<~~~?+<I_->i~i>I-_]~+?[_[1l-}-<-~i+;
                                     ..   ..             .. .  .
                         !'                                                                  :'
                         <'                                                                  l'
                         >'                                                                  I'
                         >'   .                                                              !'
                         l' .:i"""^";,,,"^^,;:,,""","^^^"^^:,:,"^^^,^^^^^",:,^```",,""""""`  i'
                         l. ._[[{]\?l![>~)>^~-{},  ;^~_~}-.!'     .l.'...':I:?{_1"I;'  .     !'
                         ;:  +}+]<I.il]?i<^.i?1][?{i i[_-' :^[~]-<:,      ";:}-?; ,`,_<~?]>^.i.
                          ,;,!lI;,`':",I"^`":";IlI!;`,I,;``;"lI;:,"".'```'""^!,:^."`"i;,l>!I;'
                            '':;;I!;.";":;!,';,":,:.^;","l:';I:,;I`';:;;lI'^I"::l,':;"^":.''
                             lIl]+'>;>^]~_`<;!I--llii"_-?'_:<`]1i"i:l![{"lIi"?<_`-,<^_}<"+
                             ;ill_,i`I,ii>"!`l;l>;I,;,Il>"i^<;>~>:!"iIi-I>;l;~ll"_"<:i_<;<
                              ''`?l^iI<l><>"!i~><~<i:>~I<>I".^'''`  ''''^'  ^'``^  .^`'`^
                                  "l<><i>l!!<!ii~>>~li<!<!l!.





























```

*Figure from page 1 (2346x3317 px)*


---



4203-E P-77



SECTION 5 AUTOMATIC MODE OPERATION



The screen changes to the auto operation screen and the following is drsplayed on the screen.



PROGRAM SELECT



AUTO OPERATION


#### PRJGRAM SELECT

PS!I]



I NOEX DISPLAY PAOCEDLRE



[F2] ...... MD1:*.UIN



[F3] - FDO:*.MIN


#### I 97/07/15 14: 10:00

OVERWRITE



TO DI SPLAY OTHER Il -llEXES, AFTER PRESS IN G [Fl] .



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS [WRITE] KEY.



DEFAULT DEVICE NAME = llll:



DEFAULT FILE~= *.MIN



I f,[)1'



FOO' ICOIIMANDIOVERl'IR/ICHAA



1N DEX , N;EX I



HI STORY , NSERT oaETE



CANCEL



(3} Enter the designation mode from the table below.



The input format is as indicated below and entry of an asterisk(*} instead of a file name, will display



a file name directory.



=PS w main-file-name, main-program-name, sub-file-name; option



Main-file-name . . . . . . . File name of main programs



Sub-file-name . . . . . . . File name of sub programs which are called from a main program



Optron . . . . . . . . . . . . . . Designation of A, B and S option



Procedure



Designation



Contents Remarks



Mode



(a} PSw* Designates main file name. Designation of device name



for calling out main file is also



possible.



PSw*; Designates main file name and Same as above.



option.



(b) PSw*,* Designates main file name and main Same as above.



program name.



PSw*,*; Designates main file name, main Same as above.



program name and option.



(c)



PSw,*,*•*



Designates main fHe name, main Designation of device name



program name and sub file name. for calling out main and sub



file is also possible.


#### P8i.J*•*•*;

Designates main tile name, main Same as above.



program name, sub file name and



option.


```text


                                                                                                '`^^."'.^.^`
                                                                  .'......      '.    .        .+]]?i?"l<,<I
                                                                 ^{{+<~-_}>_"l{~~~-}_-~-i!1++~}:!_<?~+-~~~_+
           `````````''''''''`````'''''''''''''''''.'''''.......'..''''.'`''`'''` .`'`'''`'`'''`.'`.^'``.'`'`
           :;;;;;;;;,,"^^^^`,,,,:,^^^^^^:,:,,,:,:",":::,^"",^"","""^"",::;::::""","",::::::"",",,:;::::,",;"
                      :>l:,!!lll^I!llIll^I^!iI^l:!`,:I;I>:;`;::;I"^l:";l:"l;::;::`:^:l:;I,,;"":^I:^",",,,.
                      `,;:^!;;I;'::I:>iI^;,;!!"<!i"I<<!<~!!">!I><,:<l;I!i"i!!i>l_l!;!<~~++i~;li:i~I!~!<~>"
                       ;i<>I><>i->:--I>!!!
                       i~<![l"",;,^l;;:,,`
                       :;i:1^
                               '''...`'''''' ....''''`''.......'``````...''.......'....
                             ';,I:i>~l><<>i!>;:;;;:,,:::;IIII;IIIIIIIl;:,",,,,;:,,::,;:;^
                             !' ;:?_?;_][?!<1l""":::"^""",,,:;;,"""""";i>liI:I"I;:;;i>" !^
                             !  "I+-+_-il+l~i,"":;;,,,":::::::,"""""::l_?<-~}/_f{+|_)+" ",
                             ,  l!jrn{)+i]~_i,""::::,^^^":::::::,"""",::,:`"-]{|-!?:^>, "^
                             l  , ,:l                                                :, :,
                             !  :                                                    ,, ;,
                             l  !'..''`'''`.'.      '^^`'''''''''`''''''''``'..'''''.:^ :"
                             !  '`l__<;<>~i<"i~<+~~?,"""````````^"^^`````^""^``^""""`^. :"
                             l    ]|1:;l(\i-:[\?llli.                                   :,
                             "   .?+- i^+\!li|}i        ..  . .                         "^
                             ^   .]+?_[{]!>?-f~`{j1][,;{>{<</)]~1{'I[+i` '"''^..`'      "'
                            .,   .]\]+:-)~}}+?_]j|><x~"Ii>,[1]'"~[il}?]I i(>;],l[!.     :^
                            .I   ^/|[|]"-(->{-u1-.`?1+!,                                :^
                            .;   .ll:l,'^`l`:<_.'. .'!;;                                :^
                            .I                                                          :^
                            .I                                                          :^
                            .;                                                          ;^
                            ."   `ll'                                                   :`
                            ."  .ii!^                                                   ;`
                            ';  ",  '^II_i:'^!!>I^'"lI<_>>Il!ll<;Ii!l;^^;"^```";","""". ;`
                            .!   ^lI; ;:{-l:`I;?}l,^<_\j))i!+{}\-!>{1~"^;'":,".l        l`
                             ":^';_~>':. <_-I; "-_~,lll:<<l`.~_>!!'><Ii>:;+[+~':      ',;
                              .`:;^",:':;"";;^lI"":"'::,";"^I"",l,:!:,,;`"l:::I^;iI;I;"`
                                l"]~`il<;[?"l;Ii-?^~lI!--"<l;_[<:!l;_}~:li,_+I!!i;[{;<,
                                ll>iIi:i!~~;l,!i!<;!:!!><;l;l!i>I;;l>~<l;l;ll,!;!I>-l>"
                                    .   .  .      .   .            .....  '..'.  '..'
                 `!:  l,;;^;I"';,"""^;;"^`"^,I':^"^":^'",:"`"""^^
                 :_i .<;i~";ii^<>>+il_<!I,l!<-"ll>l;i<"i~<~,><~<<
                      ;l:`;;",;:",:;^"'I^::i":l,:;:;":^:,,^:,I^'::;"";I;;;;^""^,,l::;,,:";l^^,:",.^:l^:"":"'
                      li?ii?~<!>l~~_l~!_Il!<!>>i!!<>!~:<i>I>l<>:i;~:!~<<!>>:!l;li+<<<I!;!l~!;<~l~,l+<;<++~-;
                      >^Ii"I+l>l"i;i!>!!
                      'll;.. ^^,;';l^`",,:'`,","`"""",,"^,^",`."^""I,`^"^^^.^^:^^'
                      ;I;!^: :I~i"l_!:~<!_,:i!l;i!I_<<>I;>>I~l'<!!;+<,i_!>~^>+_<~"
                       !<;I">i,";l::.       .il:',;,;`^I",:;`";^,:,",^
                       ;ll:^:l;"l!:i^.'.....',I!`Ii"!:;;,Ii!"!l;_!ll!:
                       >ll;>-!^li;i^ .      `~!:"Illl":I:;l^:I,I;I:l^;>!!>^il:"!~!l:iI;;";,ll!",I;IIIl"
                       ","^^;;`,l,l^ ...... .",,'"l";`""^I;^I:,>:I,I"";,;:^il;"i>!i,;l;:,l"l<!"!!l-ii!"
                       i~+<il       .    .. ^_ii>+!~_!!^>;>::+:!l:!!;>i!i"
                      .^,:^"^ .           . .^",,!":,""','^"`,^:"^`"^l,,,'
                 ^i:,""",::,;~l+_<>i!!>!i>l<lIIII;;,",,:,::,:,,,",,,,",:;Illllii;::::;lll;::;;;;,:::::;IIIIi
                 :<_i!>~<>I<^l i_+]}~-?i>, ;             !!!i~i!~`            ::        .+~>li><i`     .   ['
                 :~":;I;;I;l,i.  ']]_-+''``i`         ''.":;";;";'  '`````'.'.;:     .  .:lI";I:l' .  . .''].
                 l_'``!]~'`'^--[];l!'``^^"^+~-____<]?_!+-?~I]~:<~~+~^""""""`^`!+~<~<~<++<!^illiIii!I~+>~I""}.
                 l<   ^;,   .~`^:^"^       i",;;il,lI;`^:I"':I`:l:;I          ;+_+i_{_-_i<l+!_]_<{[;_+!}!^ ?'
                 l~         'i             !                                  ;>~i;+?-~~^l!^,li;`I<,:,;i!; ?'
                 l~         .i::"`^^^^^",,,<;;"^^^^^^`^,"",,:^``'```''`""""""^!-<i-~<--"'..'  ..'..''^^``^"].
                 l<         .!-?-l:>I....''I~_--]?_{?-;~][<i{?l~[_+<i]_-''''`'l~]-<+<:?!-)__-i'''''''^^^^^^_.
                 l~ ..   ...'I   '  .      ;!-?__>....  ..   .  '....'..      :,.^'`'.^.''''''             ~.
                 ;<^""!~!,,",>~+i";;,I"::::<_[+~i!I!l;:i!>i!~l:IIII;:l!l!ii!:^l!!;;::;l;I!l;:,"""""",;;;;;;[
                 ;I   I~I   .;;!i^:;,l     l!<+-[~+?__I>~~;^<~,>-i<!I+i;Ii+<, "I+-~i!;?;<_<i<I             ?
                 ;I         '>   .. . '^^^^--_<[_~<:I~-+?,'`  .     .   .'''''l,     . .      ''''''''`````[
                 l!         '--]-,">:<l````~-_<~+<>]-~,i+[>I{-:<<~-~"_?[-:""^`I~[+++~i[!_]_~~l^^`````^"""""[
                 ii         '> .`'.'.^'    li<<-]-_><-+<_!+!_i>_[<~:.`":^     I:":",,`l',;,",^             -
                 i_""":;:""";~!>I",::",":""~?<>}+-+<!~+~~I_~-l?]-_<I:,^^""""",~i;,,^'^'"```^^^:::::::,,^^^^[
                 ii   !_!   '!i++,^;!:i,i. !<_+i?-+{-~"<<?iI--^>]~-~^>_-<'    ,i--?-{_{[<>,]!~[~~_il?-~?:..]
                 ii         ';             l+~>[_-~l!+_<?"?~~l_+>I[~:~-~-!    "l~;:~{?<+;><lI+~>"_~~!~~-.  ?
                 !!         `!        . ...i'  `      . . ..  '.   .... .'    ,>}<;-;[-[;~~~_-]],`''.'``   ?
                 l;         ^_>_i"III!I>;::-!illll!+>i;!!<ll~l";IIl::!!i!"""""!<_<i+i+-><-<><!Il:^",::::::;?
                 !I         ^~;!~,l;,;"l`  +>__-{_-}_?l>__!l{+i?_<-<:>~[<^    l!~_><!;?,<~ii<;             ~
                 >;         ^i             <~i>}<~<";~+!<.l<>,~-,;<~>~"~!~.   i^                           -
                 i<,,,,,,,,^;<^""^"",,","",+_}]-]i`^^^```"^^^^..`'````^```^^^`~;^^^^^^^^^^^^^```'`````````^}
                 .,,,,,,,,""""^^^"",,,,,,,::,,"^^""":::::,,,:,"""",:::::::::,":,":;;;;;;;;;;:,,,,,:;;;;;;;;:









```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-78



SECTION 5 AUTOMATIC MODE OPERATION



Designation



Procedure Contents Remarks



Mode



(d) P&._i*,,* Designates main file name and sub



file name.



PSu,*•* A.MIN is automatically selected as



main file name. Designates main



program name and sub tile name.



(a) Designation mode PS u * (or PS w *;}



1) KeyinasPSw*orPSw*;.



2) Press the WRITE key.



The display is changed to the PROGRAM SELECT INDEX screen and main file names registered



are displayed. (This searches files having extension "MIN" from MD1 :.)


#### AUTO OPERATION A.MIN

PROGRAM SELECT lNOB(


#### MAIN PROGRAM FILE

JW.MIN



B.MIN



D.MIN



KS.MIN



K5UIIN



ABCD.MIN



K52.MiN



K53.MIN



P03.MIN



POD.MIN



=PS B



=What is the f i le name for program select ,



PROGRAM ACTUAL PART BLOCK



SELECT POSIT. PAOGW.I DATA SEARCH



3) Position the cursor at the desired file name.



4) Press the WRITE key.



01 NGTR 11



97/07/15 14:10:00



1nm



PAGE 1



CHECK



DATA [EXTEND]


```text


                                                                                                 '```." ^''`.
                                                                  ..  '. .      ..    ..        ,]---i_ ?:I[;
                                                                  i}_<>~+_?l+.?_<+<][-__-;_]<~?-"~-~__--<+~?I
           .''````````''''''''`'`'..'''''''.'......''''...........'```..'''''''^'.''`'..`'`````'.^''"'^`'``^'
           ',,;;;;::;;:,,,"":;:;::"""""::::,",,,,,,:;;;,,,;;;;;;;;;::;;:",";;;;::;:"":,,,::::,,,,,;;:;:,,"""
                  .i;:::,^^"":i;ii!l;;I!!lI;>I;;,"":;;;;;:""::,::,;IIIIII,"::::lI:;;,"",;;,,,:,^^":;;;;;;:,,;
                  I~i<ll>~<;>^! >-[}{+}[_-l +'............!i!!i!li^........'.'.i!.'.....''><llll!l^````'''`']^
                  I-:l!llliIi:i.  ^}]+[<...'~'         .  ,I!:!i;i`          ..lI..       l~<!<~!~`         -^
                  ;+^"^I_<.'',]?}],l!,>I"""">~><~iii_++l<<<!:_i,i<~_<i_<il!~l,:<i:,""""",,^^^^''''^"::::,"""_'
                  :I   "l;    i`^I^,,`:.    I~?~<[}~]<l`:!>;^!i',>;l;,iI::!i`  ;"                           _'
                  ;l         .>;I"`''^'^,,,,?~-i:+?i-l'^'...`.'"`````^' '' .",,+>"^````^^^^^^`````^"""""^```}'
                  !i         .l_]]:,I<;<''''i~!-)]!<!<--++~]?<-[<!?--<[?~I]>`^`>l`''''''````'''''''``````'''['
                  !!         .:  .......    I!><>;~[!!_>~_^'+__+-i_?_<;~+~>'   :^                           -'
                  i> .. .....'!..           !<_+-<+[iI[-~]:i<->_{+>)_I<_-]!    :^                           ~.
                  "i;:;I::::::l"":I;;;;;:"":>+<<]<+i;;~~<~i_<~i<<il_+i-?~_+l;;;i!llllllI;,:;;;;;;;:,,:IIIIII~
                    ^!, il;I;;:iI;`:::!::ii`  `.^,':!;   ``.                               ......... .......
                    ,<l Il!i_!!<!l`:li<i,:!",'I"!<,;!i::`lI,
                    .^  ;^' ` ''.,;.    .''::.  .
                    `>'.~~_:>:~-;I~I:`:"!>I!_I;'l!`
                    .'  `. . .'  ''^^"".
                    l]'.<l+-<l-+:+?++<-"_+-.
                        ::^."^'"^.'..^.''`^^^'""'^:,"""""",^`,:'"^^"'"^^,^`..'... ..'.... `. . ..
                        l~_I+~-_-~I~l~]_<[~l>l~-<li_~>~-~~]<I[-i_~!l;_-__<!+~<~_il~<~i~?+I_[!i]+~?_l_?+-}+??,
                       .-<ll]~~+++_+ :<~<i;-~+!~i_;i-~Il~<i>+,<~~><<>~'>?+?:i<!<,-}~!`l'             `. .  .
                        '....''.``'' '..''.``''''`'.``'.^^`':'^'`'```` .^'` .``'.`^'..`
                              ',":,,:""^"^""`^"",,::,^"^```^"::,"^^^^^"^^:""`'",;::,"""".
                             ^l'iI-}{<]|1)-?\_;;I,,:,,,__)]+I;,,,,,:;II~},""[)([:,,,"il^l^
                             ,' '`","^",,,^^,"`'.   . .``,,^'.'`'``''^,_(_[][f?[[<[~)]I 'l
                             ;'               `,:;:;':`,,' ",,.        ^"^^^ .'`"^,+|>' 'i
                             ;'   !;I":<iii!",~{+-_]"-!+~,'~?-"             :;;..       '!
                             ;'   [t][]<<i<>",;:                            l<~^^.      ';
                             ;'  !)1tf?"^^^^"",,;::!I                                   .;
                             ;'  '?-\|>'`''''''''''''                                   `!
                             ;'   ?_>[-,                                                ^>
                             ,.   ])+~]]I                                               `>
                             I'   ](-+}_:                                               `l
                             l'   ]1i[{+                                                `I
                             l'   _1~[(]                                                `I
                             l'   !_l_-<                                                `I
                             l'                                                         ^!
                             l'                                                         ^i
                             I.                                                         ^!
                             "    ^'''                                                  `;
                             ^   ,}~~l.' ^' ''' '`'.`. ..'.'..'''. .                    `:
                             :. ^<}[]!~~;}];l<-I[[_,?<!?~1+{i>?+]~:l^^^^,^^^"^^,"^```"' `:
                             l. ;}][{|<:]+>{;I-1[;.':"|_}+.;'`'`'`, ..'.l:>}]_";^`'``^' `;
                             ^I`;]i~>.^;!?iI';>__]]},`[~~..;!][?<".     ^'~_<; ".<-<-1>`l^
                              '"";:,:;^^:",;;"^;:,:,`,;"";,^,:"":"^,I;,;"^;:;Il:";:";I,:`
                                l;_+;;Il:+-!l;<;_-Ii;!l]+">:!l[],!,ii]_,i;l~_<;!;I<]~;!
                                iI<l:;l!;<_Ill<;<+;i;iI~+,<;i;<+"i:ii-?">Il~>l"!lIi_~:~
                                 `.'''  ^''''  ``'`' .`''^. '`''^. '^``^. ^'``"  ^^''^
                    ^' '"..`'..''     .    '        .'.    .
                    ++ ;~~_?~~I~_~:<i~_l;}l~+l<[~-+-<+{>I+_<-;
                                  ....                    . .
                    _~ ;_~--l~?~l[]]~-<l?-!
                    .'   .''. .' .   .' `^`


























```

*Figure from page 3 (2346x3317 px)*


---



4203-E P-79



SECTION 5 AUTOMATIC MODE OPERATION



5) If there is an option designation";", the screen automatically goes to the option designation



mode and the messages below are displayed at the lower block on the display screen.



A:method A B:method B $:without branch, subprogram function



What is the option for program select?!



Key in "A", "B", or "S" as desired. (Option Band option Scan be specified simultaneously.)


#### AUTO OPERATION A.MIN

01 N 31



97/07/15 14:10:00



1rrm



PROGRAM SELECT INDEX



MAIN PROGRAM FILE



JW.MIN



B.MIN



D.MIN


#### KS.MIN

K51.MIN



ABCD.MIN



K52.MIN



K53.MIN



P03.MIN



POO.MIN



=PS*:



=What is the f i le name tor program select ?



PAGE 1



A:method A e:method B s:without branch.subprogram function



what is the opt ion for r ram select ? !B


#### PAOGlAM ACTIJAL PART BLOCK CHECK


#### SELECT POSIT. PROGRAM: DATA SEARCH DATA [EXTEN:l]

6) Press the WRITE key.



Entry of "B" in response to the prompt "What is the option for program select? !" selects the



operation method B (large capacity operation method). If the control is not supported by this



operation method, the entry is ignored.



When the WRITE key is pressed without entering any character in response to the prompt "What is



the option for program select? !", the control operates in accordance with the setting of the NC



optional parameter (word) No. 11.


```text


                                                                                                '``^'^`.,.^`
                                                                  .'..'...      '..   '.        ~[_-<_;,+,~-
                                                                 ']{_<~_+[i~I:]i_+~}[--_~I1?__{!:?-__+-+i+-_
           '''''''''``````````''''''````'''''''''''''..'''''''''..''''.'`'''''``.'''`'.'`.````^''`.'```''^''
           ",,,,,,""^,;:,,,,,,,^"`",",:,:"^^^`^^`^,;:,,^,;;::::::""""^":::::;;:::;::^^""^::::;,:"",,,:::;::,
                    i! ^ll!II:^;^!'"!!;;`:!Ill:I!;;'^`.!;^^::;::';^;:::l;";:'",:;`;^;I,'::I,,'!::""";:,"
                    ;l "ii>-!!l<l]l!_~>>I!~<+]<__><",;,>-ii_i~+~:_<_<i~_~<<_i_~~~I<ii<>l-~+>l:-++?~>+i<l
                       ^i<!+:l!l:lil`!>ii~<>>,;<>!<`+<;,<_+~_<ili>Ii~,li<+^i_><l'<"I<i`-++~?!I~!<-<"
                              ^;"",!,^,^: <",,;I^"^l'`;^^I:`""^^^^`: '^^^`^`'`^^`"^'^"^' . ..
                              ,l:Ii~;il,i ~:l!_i!~,<^^iI<+>i<lIi~<<_:;+++~i_]>-<:++i+_>i
                              :<!:l`;^!;'::!,:'I,.:,:;";,.,;I,:;`.
                              ^!;!!"!^;i^:>lIl'I;`!;>+I~I`>i<!!,'.
                       ;+!I:<`i!.'-! ;;.<i'i;`+!ll!l  >ll>::`+`l;!,l!>l::>^I!"I!^;I;;!il;"lI:Iil;I;,;!""
                       `:;I^;."". ;^.:, ,".!;^!lI,lI.'!I!lI;^l"i;l^i!!I:";^Ii^;>^l<llll>l,>Ili>~!<ii<~i;
                               '`"'..'.`''^. ^``^^`'``'...'`"`' ...   . .'^' '. '. .'..
                             ^;^l;---l-]?-~~]l;;;;l;;I;<~]-l;;:;;:,,,,"!l"^,~",:""^,,~::;
                             l  ,"_+~;~--_li-;":"^^^^^"i>_<:`^"^^^^^^^I{1i~>}~:<<!+l~): ;,
                             !                                        ^!i!il"!"!ii-)ri' ";
                             !    ' . `^`^`'''[)[{)[:)>-~`!{]-'             .      `,   ^,
                             !   '/-_!]{]_1+:I<!.... ...   ''.             `_][^:       `^
                             !   '}][[l                                                 ":
                             ;   ^~_}_                                                  ,:
                             ,   '[~[]>                                                 ""
                             I   `)[![[+.                                               ,:
                             !   '))?~1];                                               ,:
                             i   ^}[i|]~                                                ,:
                             !   `}}>1]~                                                ,:
                             l   `?)i1-<                                                ,:
                             l    '^'^`'                                                ,:
                             l                                                          ,:
                             l   `:'^"                                                  ,:
                             l   <)>!,''`l"'^'^.:l^^:` ,",`l.":,"^ '                    ,,
                            .i   ~?{_!_iili+>__~1_] ->i<?(<+!<[]1;I~!,lIll'IlI,,l       ^"
                            .i  .?-[,!-I-i^[__?<<_>l+-[i]l[!]-<ii~|!>,!lIl.";:":l`''''. ,,
                             l  ![][-)~;-~?}:!+-_l':>~1-{iIi^"''`il^``''I^i_<<^>'''```. :,
                             l' i[_[?!:;[_<_';_{?~<<`,1??`'"!<~_!:.     ;`_}[l <'i!;>~; l^
                             .;,;!!iI."":!""`,:ll!>i^^!Il`",!>iiI"^'''''"^lIl^`I,i!;<+i;"
                               .:Ii!ll`;;li!I`;;l;:"^ll!I!:"lIl:I^^!!!ll^,IIIli";III:;'.
                                ~,[>'ii+:]["!i~l]?^_>I<[-'+~;~{+^!l:_{+^i<:]>:;l<:[{l>!
                                ,I:::;':ll!;;';;I!I,';:,II,`I;:I;^`I;Iil^"I;;:I`:I;!ll`

                   ^[, <~<ii:-~I!_-~i?l><<,
                   .;` ^^"""`^;,`;"^'^.^,l`
                       ~i<<;.<"^[^'l.!<~iii<<'<:;+>`<i!<i~`:-+!~,!;;>!'I>~l!'!<",iIili<;`>i<!!l';.i!i!i!`>!:
                       I>>!<i>l`lli_li><[,+~iI!"l<<!~+!,<~l;~<i<^>i<_<l+l"_i!>>^>ii-~>>l"~~i<!I::,_<+i~i:~+l
                       !_<i<-i>";<_->>i"-">~i}i^~+<+i~<"<!il>!l;';!<!lii. l^l>;^i;l;!",l`li^!<~~!!iil"+l"i<;
                       :!iii_Il^Il<<l!l`>+;Il<i:l;l->!!~l
                       ;!:,,';""II!:Il,;"'"^^",,"^:""I:^`,""::,"^`""``:^^^","`"`^^^^^^^`^^`,^````^`"`::"`^`'
                       <?i~<l~~i~_~i!~l+-<ii~+_+_-~<+?<ii!>i+->I_i_<~I<><<<<_:i!!~+~~i~+l+I<<!<l<>~+^~?!?<ii
                       li>'~<><;`>^'>I<<i~;`+>>><;`, <~i">><<~;I]?<<[+i:<^+ii<i_->>_`~__"_+l,+?->_I!!i<<,[]:
                       I+_+~<-;<~i-~__]il_<+~_;[<.,>^ .. .. .. .'...... . '.....'..' '.. .''.''.."`'...` ''.
                       `:^^^^,`,"^,^"",'^,""^,.""..`.






























```

*Figure from page 4 (2346x3317 px)*


---



4203-E P-80



SECTION 5 AUTOMATIC MODE OPERATION



(b} Designation mode PS



I.....J



*·*



(or PS



I.....J



*·*;}



1) Key in as PSLJ



*•*



or PSL..J



*,*;·



2) Select main file names in the same procedures as 2), 3} and 4) rn (a).



3) Enter the main program name when the prompt 'What is the program name for program



select? !" is displayed at the lower section of the screen.


#### AUTO OPERATION A.MIN 01


#### N 9\

97/07/15 14:10:00



1nm



PROGRAM SELECT IMJEX



MAIN



PfOOW,I



FILE



WHER100.MIN



SHIL2.MIN



OEAR-1.MIN



BOX-1.MIN



Ol{)LE.MIN



BOX. M!N



OSHT2.UIN



OEAR.MIN



SHAFT.MIN



,.pg*,*



what is the file name for program select ?



what is the rogram name for program select ? !



PAGE 1



PROGIAM ACTUAL PART BLOCK CHECK



SELECT POSIT. PROGRAM DATA SEAOCH DATA [EXTEND]



(EJ @J @J @J @J @) @J@)



For example, selecting main program name 0100 is as follows:



What is the program name for program select? !0100



4) Press the WRITE key.



If the WRITE key is pressed without entering the program name, the first program in the main file



is selected.



5) When there is an option designation";", the display screen allows the entry of option



designation code. Follow the steps 5) and 6) in (a).


```text


                                                                                                ."^^^'^ ,'^^.
                                                                  .'..''..  . . ''....''.   ....;[[?_~~.-:[]"
                                                                  ~}~>!<<-_!~.?<<_<?]_-~-:?]~-]?"~_____-~<~?`
           .'''``````^``````````''''''`````''......'.'''''''.''...''''..'''''''`. '''...'.''''''.'..`.`''`''
           `,,:::;;;:":;,,","",^^^"^^^",:,,::,"""""^^^^";;;,,",,:::::::;;III;;;,:::;::,:;IIIIII;:",:,:IIIII;'
                    :<: >!!!!!l+lI";;;il:i<^. ,^"^"!,l<i.. :.,^"
                    ,l: ":;I<I;l;,'";IlI"";^" ^^:""!"^:l";'I"I::
                    '; .!:,',.,,`l!^  '.''.,`!l^  '..`
                    'l..!i~"!`<~":i:^',:,,,i"Ii;^`:;,I^
                    `"  ,'^`''..`' :".''`''... "`..'`''.''''`^.`'.''." ." ..'.`.'..'.
                    I-'.+--+~;!~->"-];l]+i_<l<:_?;<?~+<!<><~__i+]:~_:-::]"_i~"_li!l?<
                    ..  '    ..  .                     ..         ..'  .                   .
                    ![.'_i<_:>__;<--l!+!]+__;;~?<?,><~_">+<:~!~<~!"+-i-iIi>~+I-<-?~-+;>]~->~-:i~<}_-_;
                       .~<<<<>,I;<,-~_-~_+<I?l]+I><+~I;-~+++lI+!+>"ili_+i'  ..' `^..   ' .. ' '..,'''
                        ,"^"^.. ."'"":"::"^`:'^"``",,'';,,,,'^^`^,',"";:"
                               ^""^`^^^''''^.`^^^^"",::''..'^^^^"^^'`'''`^""``^^"^,,"^`"'
                             .I^^l>)(]<([1[<}{;;::;;;;I~+{{?::,,:;;;:::l?;,;_+,:",,;;!_`:,
                             ^,  `,l;:,I;I;,II`^``^^"^`",;l;`'```````",<(?_]-{_i1~?+-}-  l.
                             ^,                ``^`` '' '. .`'.        ^:,",``^';::i|}`  :.
                             ::   ^:`"^I;;:;^,l1]-_1;~-<_! ~{_!             '^"`    ..   :.
                             :,   ?x]]!11[/jI:I!                            :+[i``       !.
                             :,   i|__![+~I;'                                            i.
                             :,   l|[-ii]_I                                              >.
                             :,   >t{l"[}-`                                              l.
                             :,   i({__{_i                                               ;
                             :,   >\]][]I:                                               ;
                             ;:   !|)?+1[!                                               ,
                             ::   <\(}+[-l                                               ;
                             ;,   '"^' ^`^                                               ~
                             :"                                                          ~
                             ;"                                                          i
                             ;"                                                          !
                             :"  '!<`;:"                                                 i
                             ^'  :)_I`~^i?:":i::_],:>';!<<li`~I>>^^`                     <
                             `. .!{?i'+I>)>><}[[[![1];]!![_)~/>-{+]i,!:,``'...`^`'```^`  i
                             :^ `-][[1_:<_<{+"_[[i'.;^]_-["i"`'''^i``^"^I>I]}[>::'''``'  !
                             `I''?~-~I.,i[<i:.<-?]-[i.-?~; ,;]_]~:,     "ll[_~ `'l+<~-_:^l
                              ',,;:::,,;;;;,,^",,::;"^;",;,:,;,,;""":"^"^",l,,""^;l;lilI,
                                "Ii+!;;:l~_>I:lI~<ll"lI+_I!,iI-_;l^>!-_;I"li~<ll"l<-+II
                                ll<~i"<!;~?<,l~;_+!ll>,~]:il>;-}^i:<;-[`~lli<i`~;:i-[^~
                                 """,,  ,"",, .,",," '"^^,^ ^,^^"` ^"`^,' "^^^,' ,^`^,'
                       '".....''..    '...   ..            .   ...'      '
                       ,<>,i_++l~_<'_-_+~<-~I<-+;<<>]+?_I!-]i_,<>>?!<!>-:<<<<+_^
                              `;I`,`^`:`.'^"''^^.^`^,`^^'.`''```..`^``,"`"^^"^
                              :-~i-,~;+<I+i>}i-<"l-~><;-Il~i]--_lI-_-~~:I_!<?i
                    `` ','.'.`'  `'^'`. .
                    ~_ :>>~_!i<~,-<_><<l_<>
                       `":,'";I;,;"``'.^.^"`^^^"'^:"``^'^"^^^'':`''`''`'`.'''`' "`'^``'.'..'.'.'."'..'.'."`
                       :i~+<I_+~!+!!_-;~!~<~~+_<l__~~~!<~+?<!]>-~>~i<}~_<;i->~-`<+<>i?>~~<]<+<I~l?_~l~-~;-];
                       ^~,__-<-+-`                                                        .
                        ..  ...
                    _~ :-~i<:>+<i>;>:_:l?+<i";-i~<ii?ii^^:.?~;:_>!>~"><!<+!,?-!~<;]+I!<<<;;<:++~!;
                    `^ ^->~<!i-+i!:<i[l`!?>?i>i+-+I?_<<,>,I~~i+<li;?>",^,,`':"^,"'",^""":"^"'l::,^
                       '!!l<lI>l;,"IIi;  ,:iI!":!;">i>!"i,l!I:il':^>i




























```

*Figure from page 5 (2346x3317 px)*


---



4203-E P-81



SECTION 5 AUTOMATIC MODE OPERATION



(c) Designation mode PSLJ



*,*,*



(or PSLJ *'*'*;)



1) Key in as PS LJ



*·*'*



or PS u *•*•*;·



2) Select the main file name in the same procedures as 2), 3) and 4) in (a).



3) Select the program name in the same procedures as 3) and 4) in (b).



4) The screen will then display the subprogram file names.



Files having extension "SUB" in MD1 :.


#### AUTO OPERATION A.MIN 0100 N 91

197/07/15 14:10:00



PROGRAM SELECT INDEX


#### SUB PRJGRAM FILE

JW.SUB



JWl.SllB



A.SUB



OSHT2.SUB



SHTHa..E. SUB



BOX1.SUB



-PS**"'



~t ls'the fire name for program select?



PAGE 1



what is the program name for program select ? !0100



what is the file name for program select?



5) Position the cursor at the desired file name.



6) Press the WRITE key.



CHECK



DATA [EXTEND]



7) If there is an option designation ";", the display screen allows the entry of option designation



code. Follow the steps 5) and 6} in (a).



(4) By pressing the WRITE key, the main program can be read from the specified main file, while



the subprogram called up in the main program is loaded to the NC, and the main program is



displayed on the display screen.



If the subprogram called up in the main program cannot be found in the specffied sub file, it should be



searched for in the sub file of the extension SSB so that loading can start. If it still cannot be found,



an error occurs.


```text


                                                                                                '"^^'`^ ,.^'
                                                                  .''.''... . . .'....'..  .....l[?]~~>'_;[l
                                                                  _{~>>++-+l<'}~<~>[]?-<~;}?~?[-:++_+--_<i+_.
           '^'''````````^^^^^^^```'```^```'''''''''````''''''''..'''.'..'''''''`'.'''.'.'.'''``'.'..'''''`''
           ^:""",,,,"^":,""""""`^^"^",",:,^",:^,:,:::,:"^^,;;::",,,":;II;IIIIII;III;,::::;IIIII:,,::,;IIII;,.
                    ,!, ~>i>>li_!l^Il;>I:<~^. :^,^^^"l,l<>.. ,.:.,""
                    ^:" ",:I>,;l:".";;I;^^;^^ ,^"",""l"^:;^"';"I";;I
                    ^; .iI:."',,^!>^  `''`.`':`ll^  ''.` `
                    'I..li<^;^li",!:^':::;,:"!";i,,^,I,:,!^
                    "" .:`^^`'"`'''`"'""..```'.' ,`..'''' ``````.'`..'."' "..'''`'.'.''
                    !< '~+<~>;<~!;i--;i_i:__i-:>:-+!!-~~+l_<+__+i<]li];-!`];<~<l~~l~:-_'
                    .'  ` . ...
                    i].'?_-~+l<~>i~<?~?_I;_-+?;_;~?!>]_~-l_<+_+-~<?!i[;?li]<i~~I_:-_^
                        .           `                          ..         .   .  ...
                    >-  _>_;+i<]?II-?l]<-I<]_+_-,-?l!<~_~>--__li-<:~_~+?l
                     . .^``.``.`` .'.'.``''',:`:"'`'`,",`.,"``..'`.`^'`^`
                       ,<-]~;--+>?l~_]~i-+_;,}~_[`l:+1+i;.
                                 `'.  . ..    .         ..
                              ^,::",;:;:;;IlI;,,,,,:;I;;:,"",:;:,,,,,,,,:,""^":,""""""",'
                             ,; I;?{1>-))|--|~::,,:;:;:??(}+:I:,:::;:![]1;::[!:""",",}!'I"
                             ,. .'`^''``^^''^^'     .  .'^^'  .'''^^``:_1_[[?)!~{<}_}]l .I
                             ^.               `lIIll.l,::' ;!I'        ..'''>_``^^```'. ';
                             ,.   I>I"+<+~~"I,-<~<~+`~i>!^'~?_"            :l!,'.       ';
                             l'   ~r>_|ill!'^",                            ,i~;^'       .;
                             l'  '+jl]j_   ....`'`^^^.                                  'l
                             I'  i1]/r+i>;"::::;::;;<"                                  `l
                             ".  .]|))>[(?!'.........                                   `;
                             ,    }1?~[{>~~                                             `I
                             :.   ;!: ;>:                                               `I
                             :.                                                         `I
                             I.                                                         `I
                             ;.                                                         ':
                             I.                                                         `:
                             I.                                                         `:
                             "   ^~i";;,;                                               `:
                             :   +{[;:<^?_^l,<,<-_^~i^<i_i-!:-!_i`;.....''              '"
                             ;   +}]:,+.-],+i{l]~<-|!:?;<~[?>{I}-+_^^':~!_              ^"
                             ;  "-]]ii_;+]l<l[>+{?"<-"-~}_[+;-i_i:>^^`^`,,:"^"^"^"^``^. "I
                             l  l[-{}}l;?_+{:;]{]:^`l^{-}>.I```^';:.....l,~{}[`I`"^^^^' "l
                             ^;`;-!+! ";i_l;'">--_?[:`_++ ':>]]]~;"     "'<_~, ,^]_<?{-^I`
                              .^^:,",;^"I",:;^^,^^,^`,:":;"`""`^,^^:,"";^^:"",:^":"^":",.
                                !;~~I;lI;-_ll;<;~-:<;ll-_">Ii!]_,i:!i]+"l;l~+<;iII_]<I!
                                i;>!;I!!I~_ll;<;>+;<IiIi~"<li!~_,i;!!+-,iIl~!I,>l;>-~;<
                                 '..''  `.'''  '..`. .'..`  '^`'^  `'.'^  ^^``^  ^'''^
                    "` ^,'`"`'.^`. ..''' '.`..'..'..'^` . .'
                   ._> !>>~?~i:<~i">><+i:?;~-Ii-+-~-l~[il?+~-:
                    .   .    .   .''''.
                   .[> i<<_?l-?~l[_?+-~!]]!
                    .                   ...
                    +! iii<<+l!;I~^i<+>!^<+<+<i_+i!.:`"~<:~-~_-+"+><++!I1+i_>!-_:<<-<,>iI~-~>,i-<~+i<?i>^
                     ' ;ii->'!<~?i<i?<l>_~~><[:+>>!~"l:i_;^^,"":."^`""'^:^","`",'"^,:`"`^;,,"'":::i":;,".
                       ':,;" .':;";'""'"II;,`;'I",^l'"';!^
                 '!!  l!'",:I;:"'"""^!ll:I:',"' I"'^:,, `",:,:,`":"";"`,,:,:""^^I,'"""^;;^,`"":`:;^ "",:'
                 `ii  +[!><+_+i<~I>~:_><i<<,<_<;_+;>~-i,<i>]>+i;i_i;+<;___!ii~i!_+:~-_~~_+i:~+_li~<'_i<?:
                      >!!,<!~>I<~i+l"!~!<i"_;";l>>,i>-!;+>~_~<lI~,<_<+~IiII~~,__;']<<I_~,!<~<:<><?~]!"~`
                      !+~~?_+->l_,~~!l-<~+?I<<i_~i'    .  ''       .. .  .  .   .....  .......'.'".'..'.
                      ",:^^:""''` '`^``":^;`'^`,,'.
                      >>~+I~l<_!!]>+i,i-?<!:_;I:<<l!>_l!+i~_<<l;+<Ii<i-i>i!!>i!l>~;_<_i<<>ll<+;-<^ii+Iii>i<l
                      l><>!~!~i<ii>l_~l>!~!?_;<>-+l<~_<+_<+l--?_!<;]>~i<>~?i>:i>I!_-+;:+i!<-<!i<~!~i~!+~ii+;
                      !~lii!>llii,>I";^,,,`",`,^:;";::;,;:,'::I:^;";:l`;lII:>";l^,!I:'.:^"ll""lI:;l"!;:ll;l"
                      !!`!I;!'i!lii!





















```

*Figure from page 6 (2346x3317 px)*


---



4203-E P-82



SECTION 5 AUTOMATIC MODE OPERATION



(5) Press the CYCLE START switch.



By pressing the CYCLE START switch, the main program can be started.



[Supplement} 1. If a main file name is omitted, A.MIN is used. If the main program is omitted, the



first program in the main file name is used.


## 2. Search of the subprogram which has been stored as a part of the main file is made

first.


## 3. When the sub file name is omitted, the search of a subprogram called in the main

program is made only for the sub file of the extension SSB or MSB. Therefore, the



sub file with extension .SUB should be input without fail. Only one kind of sub file



can be input.



(If the subprogram in the main file calls the other subprogram, the subprogram to



becalled must be stored after the one from which it is called.)


## 4. If there is no specified file name or program name, an error occurs. Then, the

program selected previously becomes invalid. Always confirm that the valid file



name or program name is displayed on the first line of the display screen.


## 5. A program once selected is valid until the next program is selected. Selecting the

schedule program is invalid.


## 6. Direct specification of the file name without using symbol "*"is also allowed.


## 7. Main and sub file name directory can be searched for using alphabetic character,


## 8. An asterisk (*) is displayed at the beginning of the file name of the file which is

selected currently.



When the PROGRAM SELECT INDEX screen is displayed, the cursor is



positioned on the file name prefixed by an asterisk.


## 9. When there is no file where asterisk should be set, the first page of the PROGRAM

SELECT INDEX screen is displayed with the cursor at the top of the file names.


## 10. An asterisk (*) is not displayed in program selection such as external program

selection, DNC-C program selection, and PPC program selection, other than the



selection made by an operator.


```text


                                                                                                 ``'''^ ^'''
                                                                      ..         .              :[?__<~ +:-[^
                                                                  +1-+>+<-?!~.?~>+>][_~~-,-]~_]_"--+-__]~<_[,
           .''''''```''`'''.''''''''''''''''''''''''........ .....'```..'''''.'`..''`''.`.`'''`^.^''^'^`'```.
           ',",:;;:,:;;,,"^^^^^"^^,::,:"""^,:;::::::;:::III;,:::;II;IIIII;:::::::::;;;;I;I;:::::IIIlIlI:;:,:'
                  ,~" .<:ll;I>I"!l!!;>"!l!><i^;I!ll"
                  ;>: ."`lI;":;`,"",;l^;::lI;.l!lll,
                      ^-!^il!!l;l:<!:;ii<l>l:~Iii<::>>>iI'_l:;!!i:Iili!!!,,i!"l!^!!!<ll.
                       ":`:",I;^!^,:"`^^,";^^"',,^ ":;::".;""^;l;^:::+l!:`,!!":l'l!!l!I.
                 i+;Ili;:;;;;    ,   !^``:";^:!^`,:",',.^:";",'.,"l!,.^ ^"^"  :"I^.``^^'""^"",,`,`^"^:,"^':^.
                 !i!>iii;!iI!    ,` .+Ii;>~i;l_>;+<~_:~;iii?_<l;>i__>:<:__<<' >l~<lli-i;_ii}i+i:+Ii>!~-~!:<~"
                                     ~>_:~!<[i_i,>:~>!;<__"~-l;?+<+,+:i-~_^
                                 '   .      '..
                                 -" ._++-<_;~>?-!~~+]~i->-_l<?-~_i_?<i_-_!!]<>+~i]I<i+_<!+<_~;>~-l!-<l<l>+_-^
                                 .  '-i_:....  ...'.^..,''..'''`..'`''```.'``'`''^'`"^^.`'.`^''^"'.`^'^'`,"".
                                     ^'"
                                 <` .!!:l;,~I^;:I">l^:I;:"""^I;!l;:'i:^":::,l';:,^"":"""",:"'^;!":,"`I,`""",.
                                 l` .>>!+!l~<l>~<I~~:i]i+iI~!~i<-++;<<>>_~>i~:~I<l<~[-~~?>]~l-]?]-!i;_~lI~-<^
                                    `<;<]~_l"<;!i<+;;>>l!~:<~iIi+"l+,!i!ilI~~_I<i>;;++[Ii`<+_[^ !i+>~+l>;:-~`
                                    .<!<;~<"<~~^~_]~i_<~'![l}l>-!i_<>-I!+>iIi++~><!-?! <->~"<i<!<l+I>l>!+I?-^
                                    '>+<;<iI<i>i^^^^'^^`.'^^^'^``^"^`,^`,,^'^^^"",`":` ^"^;',^,`,^:^"'",,`";.
                                    .,I"';:`";;,
                                     iI>~;`ll>I;l!I<<"!"i!::li<^<~;,><i:<!,;<!i^I;>il;Iil>I'_>;:;!ill!!l>l;i'
                                    ^-!>~?!+>+~!+~<<l<ili<;>-~li>~;!+<<!i~:!_~+;l<>+!i{]<~I`II:,IIil;><Ii:,!'
                                    'li;!>!!";lli^>I"<llil^<<i.!ll^!ll^l!l^!>i!I^;I;:<_<>;,
                                 :   ,':''' ^ '. ''''^"''':. .'.'. . .'  .'.  ..'.  '  . ...'''.'. ':`'' '`.
                                .<' '>;?~~<"~:!<"+]___-+~:?+^!_>+~"+`+<>[+~~;;?+<-:^[l,-l<;"+~>>~i `_<_<'>?~'
                                    `~l!-i~i'>__<i_<"I>>l>I<+!`~>!ll<_I:~I~i<` >+>~~<,:>l><i,;_~ll~>.l+>+:?~'
                                    '~_~-i;>:~><_<-<;~-++l<ii]+--+<~>!_:~~>~~iI><+;_~i>>;+<>~<I>>l~_!,,^^.^"
                                     'I^^^."':^;l";^'^;^,'^^^:!I:l;;``,.";"^";"^"I."'"::';l!I<""l^Il:
                                'i. .!';,:;:l,',":"`II;:I:;"^',lI"^,l:!I^';:;^"""":::^"':,,",^:  !^,^,;,^;;:.
                                .l. '>i+i??++II>i~<l+<~<_~~!<:>~>;!!>I>>l^~>>iil<+i<l;>;~<~>><<^`-<~<iii_ii~'
                                    '>!!<<<_ll>I?~>>;;I;l!_!<'
                                .^  .^.  .   . `. .    ...  '  . .    `.  .        .   . ..
                                ^?' "_+~+<I{--~]<+-~<;<<+?_!{-,~]>]!!-}_>+<l-~<_I-<~[+_"iI>>l[_i;}-~__?i
                                     .     .     .                             ' `                  .
                                'i. ,{-+iI_i>!<+!_[ll+?~-:]~_++>+;!_<l?<;-_-!+~+i>_I;+-i~I_<~>]++~Il~><~<~-I
                                    `;:^l<";~"li:....'`.'.'.''''"''`'.``'^^^''`^'.^'`"^`;'^^'^""^^```""""^,`
                                           '" ."
                                ^<  '<:.!II,:i,'::';^Ii!llIll"II;>I^ll;l:::I^,l:l:^>l^":;;;';,ll,"!:':l,;:`:
                                'l. ^~>;__~~i+lliiI~,Ii~l!<ii^!I:ii^i>_iI;;_III,!i"><:;<i!~^i"!<i,><`<>l~l"<.
                                    `!i<I!~i"I!;!li_^
                                    `!;",` :," :ll:;I>l!i".i!:"l,l" !lll:; ^"^^",.." `;"",^^", `,^'.``^^^.'"
                                    `_!>_l'>>+.!!_<>-?<~-:`-_ii+~!^'_-<_i<.i+!~_+'`~.l_-_++_~~.,~_,'<>>~<.:-
                                    ,<i~~ii~<!I>"~<!!{i,~+i_;><~-~-+,+!I-^<-_?l~~'
                                 .  .''             .   .            ..   .                       .
                                :[  "?+<+;~__i!i!Ii;-_:+~_~i;_~+i<_:<>!i_l;+;i~l:<~I_>+I~~-i,~l<<!<-_i~__+]-
                                 .  ,}]>++>~:?]_]<+:~<<+<:~!i?+__<~~>l+};<<>:ii<i!:~!+~i<__:<>~<ii_lIi~>i>I`
                                    .,:"```. `,","^.;",:: "^^,I::l:l`^:;."",'""",^ l"","`I:'I':;"^l:^;!,I;'
                                .i! `i,.ll!;I>^.""'I'",:.i;:l:",:': ,:^,::, ^::,,I:^ "^,: :" :","^^,.^`^"^""
                                 ;I."~<;-_+<l+>>~<:_;!>!;~++<-?_<l<:<!<[<_-l~-i+<~<!"~<<<:-~:_>~~<_~l-i??_+l
                                    ,~<<!il!"`i+<;I;l~l_+ii;`~__<_~<I`-i>:<<<:l>I-_~+;,_~_i+<~`^--~!:_>_:+><
                                    ,_~+i_><:>~<__;_l!_,<__>_-<^                 .
                                     ''''.'. .'`''.^''` `^`'``'.




























```

*Figure from page 7 (2346x3317 px)*


---



Table 5-1 Operation Comparison between Normal Storage Capacity Memory and Large Storage Capacity Memory



Selection and Operation of



Item



Normal Storage Capacity



Selection and Operation of Large Storage Capacity Remarks



Parameter setting Method A



Method B Method S



Specification of S option in Valid --



Invalid



PROGRAM SELECT command mode



S option not specified S option specified --


#### Program size

Main program



Up to total length of the stored main program Same as Method B



limitation



Subprogram



-- --



Up to the operation buffer



Total tape length varies



} Library program area size.* depending on the Total tape length varies



Same as Method B



selected operation depending on the



Schedule program "



buffer area capacity.* selected operation



Same as Method B



buffer area capacity.*



Subprogram function Available Available



Unavailable (alarm) Same as Method B



Branch function Available



Available Unavailable (alarm) Same as Method B



Instruction for Main program



Sequence label only -- --



jump destination


# Subprogram }

-- -- of branch Sequence label, sequence



instruction



Library program number



Sequence label or



-- --



sequence number



Schedule program



-- --



Main program sequence label limit No limit Fewer than 30 pcs.



No limit Same as Method B



Execution time for PSELECT Several tens seconds to Several tens seconds to



command several minutes



Ends at once Same as Method B



several minutes



*' This capacity can be extended by selecting the operation buffer expansion specification.



0 -I>



I\)



m "'



JJ r'n



0 '



0, z


```text




                                                                                                               !.
                                                                                                               <.
                                                                                                               >.
                                                                                                               I
                                                                                                               i
                          ':,"^^.^,"",^'"^"^""^`^"""^^,^^^^"^^^`"^^^`',^``'```'``'"`'`''``'^.^^'''             >
                      ....`llI::`:ill!I";;Il;;:^II;l:"l::l,!I!>,;!lll,il;I,II:;l<:llI<l,!ili;l>lll'            <
                   lll;"""^'^^^^"^`^^^^"^^II~~><!!>Ii<i<!:I,,^;I,:"":;:;:,:":;:::,""::::,",^"I""^:;;;;:""l'    l
                   ~i!".`'.''...''......''!"_-+-+?_-_<-?-?:,^.li>i!:ilI~>>i:;;l~<l>!+iI~>i<^.i`..!!l!i`..i"    l
                   +l><<_>l_++;`^^`^""",""!^`^"">?~<i!""""^i:^``^''^``^"^"_~ii+l^^````^^```^^i,^,_~>><I^`i`    <
                   >><><i<!;l!l~i;;^.'''..:..'''.""::''....;,^`'.''`^^`'..^<]_,^'''`^'....^^^I```,;I;"^^`<^    l
                   i~~>~<-<<~<<il>ii!I:!<;I.    .;Ii!.  ...:"^!l<>IIi!<!<<;^I;''lI<>ll>!><I^`i'''`""^.'^`~^   .i
                   _~i+<!l~l'';i>l;!i!i"``~,```````'.```^"^!^'^:~<i!~>~<_>!ll;ll<i~<li~~+l^''i!!l:IIi!l;;i'   .<
                   ~!!~>l'..  "i>!li~<;`'';,               l:'..:,,;I,,;I^:l>III;:!l;Illl"^''II!!liI>!!!l>'   .<
                   >          ,!l!Ii!!"```;,`l:,l;:lIl;":!I:I.;I":I^,:l`,;I ^;'' . .""' .'``^!   .`"'  ..~`   .i
                   l          Il!lI,;iii^.l:"_<!+~I,""^'^"^"I`_]_?[++~]<"^,.^>`~_><-!>~?I!<<^ii!!;!l~>!lI<'   .i
                  .i          ;!;:;;:II:,"i,               :;`~}-~~__+-_!`  ,!.-]-?_+~i-<'   ;:::,;;I;:::<'   .i
                  .~'''''`'''':!!!ilIl!<iI!".''''......'''.!;',::`,,`:::l"..;i^+?+>~~>--+~"..l!!l:l;<iIl!~'   '!
                   +~+-_?+>i~~_>^`''''`^^`l``^""i<~+-!"""^`l^`^"^;ii~~>^^`^`I;"l<<i+-_>-~~!^,~<>!l!i_<il!<.   '>
                  .+_<~<>i<+i`^^^^^^^``^""<^"^"">+_-]!""""^l^`^``;<+__<``'``!;^I++~_-?i__~>^^!+_+i+<[?_++~.   '!.?`
                  ._<+i~+>_<"';+_ii>+<<"^"<;'  ..'''.. ..'.i^`!+~~<~<__!~<^`!:`^,,",;;,":,"`^I":,";:;:::,~.   ';.[^
                  ._+_+_?!l!I',~<<i~~<:`^";:`;,",,^:;^"::,,il^^^^````""^""'';:"^'''^::^'''^^"i'''',:"'''`~.   `i }^
                  .><~<~+;    Ii+~!i<~ii"`!":__?+,^::^"::",I;`~<>>il><!!'   ",^^""^^,:,""```^<"^``"::""``!.   `i.-'
                  '!          l<>>~>i~<~>l>, . .           ;I'iiill,l!!!    I:''''`^,"`'`^^"^I.'`^,:^..'`<.   `i.+'
                  '?~>I!i<>;li<~~<~-<~_<ll>"'''`,~Il!`'^","<,'^lll;!:,I;!"^`l,^""`^!l!!,````^i!l;:lli!III+.   `!.]^
                  .-~+i~<+-~<~<_?+_+I":"'^!il;Ili~>+<l!;:^'II;l~+_~~<>+_~!^`;^'`^,,i;ll,"^`'^<i>>l!l<ii>i~    ':'('
                  .>__+--l",^:^,:",^''.'`^<--??+]<-_:;I:,'.;]??]<?_-?;:;,,''!"'''li>lll>!'''`ii!lI!!~ill!i    ^!.[`
                   ,^Il;:;::I";:,:":I;II;::IIII;;I:;::::,::l;;II;;;;I::;,:;:,"""^`^""""^^"""""^^^""""^^^""    ^!']'
                   . ^;:"!l;l^;:"I,Il:;I,;"ll;:l,;";lI!I";;i":!l;;;^lll!lil,                                  ^l`('
                                                                                                              ^;'?.'
                                                                                                              "!.[,{.
                                                                                                              "I`1,?.
                                                                                                              ^:`['>.
                                                                                                              ";`["[.
                                                                                                                 ' '



```

*Figure from page 8 (2339x1651 px)*


---



4203-E P-84


#### SECTION 5 AUTOMATIC MODE OPERATION


## 2. Schedule Program Selection and Operation

(1) The schedule program function is provided to continuously machine different types of



workpieces automatically uslng the pallet changer, etc. without operator's intervention.



In this item, selection and operation of the schedule program are explained.



For the programming of the schedule program, refer to Section 12, 3. "Schedule Programs" in



Programming Manual.



(2) For the selection of a schedule program, the directory-selection-based file operation screen is



used.



The following explanation gives basic information on selection and registration of the schedule



program. In addition to the basic information given below, there are various functions including the



function to display the registered part program files in batch. For details of the functions, refer to III.



DATA OPERATION, Section 2, 15. "Directory-Selection-Based File Operation Function".



2-1. Selection and Operation of Schedule Program



(1) Press the AUTO key.



(2) The lamp at the upper left corner in the key lights and the screen changes to the automatic



operation screen.



(3) Press function key [F8] (EXTEND) two times.



(4) Press function key [F4] (SP SELECT).



=EX



=EX



RESTART


#### Nl.M3ER SP SP-NO.

STOP SELECT SEARCH



NEW SP



ENTRY



Press [F4] (SP SELECT).



[EXTOO]


```text


                                                                                                .```''^ ^.''
                                                                  ... '. .      ..    .         ;???~__._:-_'
                                                                  ~)]<~-_-+li']~><<]]-+~_:?[+?]+:-_?~+-_i~_-`
           '^````'`````^^^`^`''''``````''''''''''''''''''.....'..''`''..`'''`.'^..`'`'..`.`''``'.^.`^'^'.``^.
           '^::::,:^'`^^"""^,^`^^'",,,,^^^``:""""",,"`":,:,^"::;:::,^""^^^^"^:I;IIII;::::I;;;;::::;IIlI:::,;.
           l[      i)!<->>!];<_!^1~!!IIl!!!>.__!<<l;>+I;l`^I;:!^l<:,:::;ii:";'
           >{"     i|[[]))[|1]|{:]+?)/z[1/[(:}|\1\(11\)1{!+r[)fI?)f\t/[f/|\11> .

                  ;>: `_>i"!i!ii;<::!Il;li:lIlIiIl^l"lI;;lil:!"":,Il::I;l;^;;;:I;;^,<~:;:;":::;^`I
                  "," 'i>+!~+i~<!>!~~>]<+>Iiili<>!,_l>!>~~->!~!Ii!!!<<i<+?;l!_li>~l>__+>~~I+_+-iI~
                      `>ili><!l>;:>!!!:<<I<i!"i>;<Iii,I<__i:<i~!--"^-<':~iI!>I,_~>>+!,I:l<-!i~!~><"
                      ^:'I:"^l,,.`:;:,l,"."":^""""::^"`"^:^'`^"",^^,.^^``^^^.^^`'^`^"^^^^
                      `l`!ll"+!l""<i>!>!!`<I>"><<;<>lI:!:i>,li!<<+i>:~i<~>~;^~>;!<_<~i__>
                      "l:'"!; "",I,:":,:"".l'II".:,:;I";'^"",",,' ":!,.;',;":;^^ "; "` ::::":",`^I"^^""""^'"
                      :<<:I~~I_i~[!]+><!<-"i`l>I">li~<!<">!!-i~iI'!~_>`<"I_>>~!l.!>'!!.l_<>+++~l"ii~?<_i_",<.
                      ,!l~[<+~<!<~!i?+>l~<
                  '`  .'  '       `    .   .. .            .   .
                  ~], ;i<"!-<I]--~[__:_i~I+<~-]-_>l+<[<_?l"[_l>]~_--+<I-~_~]+_l+--+-~+[~;_+<~[<<;!+>~_<,+^
                      ^!++<.            . .  ........^'.... '.'..'.''`.`''''''.'^^`^'.``'"^``"`^.^"`^"`."'
                      ':"""
                      `i!>^+<<~_i+;!~<~~!<-<>'l~!_!:~~>!`!++i>>_<!I'!:^<>i!>i<^:iiI^<>>~<!+!l'Ii:_>`l!i!>>ii.
                      "ilili!i'l!!_~_-!i:<l+~l<~<~!:~+<>l>+i!:><>>;l>iI+:_<i>!;>i;ll<_<<>>>>>:>!:+~I!~<<<~~~.
                      !<!+_>i!""<i~~+i>+;lli~+i~_<iI>>i!>~~i!!]>>>I<~~<~:!>-!I<+<,+_I<<<l<!>i+<<lll>><<<~!<_.
                      :<i~<!<l_I+-+~-_!~<:!~_>_~>~>+~~l~!<_>+l:><i;II>_><'`l!:!-__~l,!!<<;<li_<l>I'+[?:<!i[l
                      ;~+~+ll?~?>~-~<<?~']?~_<~:-"^-l'_~>+__!<;-?_+<-~!l{+++_!><_:~_+~i]~!;~i!>~~<i:       .
                                             .  '         '. ` .'.'.`^''^^^"^'.'"'`"""^:"^'''^^"^"`
           i;::    ~~!i!I<lIl`!;lI,>!;l;l!;::';l,<:l:;I:;l'ii,,,",":.
           i;":    !+~i>i<ii!"_I>l^!-<+!_~>il"+!:?<>__+~-?:i!>~1~_+>"
                  `.  .`    ..  ' `'
                 `>>" i~>_?I>-<;]>><>!-->.                                                 ,;l,""`:.
                                                                                          "};<+-_<;:
                                                                                          ,< )zLnC^:
                                                                                          "_;,lI!I<:
                                                                                           ~_~+!I_~'
                  ^^  `"'..''. .''`.  . ....`   .   . '. .   . .      .
                 `-]` ,i>>:?>]!i+!_~"<-_]il]-;~+i+-^+I?_i+_?;_}_?l>-+~~-<!->+_~:i~_~---!ii![_:_~]~+-[_"
                      ;<_+<[<<;i~>~_+^..                  .'..^ . ...  .. ..... ..'.^^'..' ''.``''.^``.
                      .^'..`.  .'.'^.
                 '__' !<<>~:~>!<+!I:<<;>_]il?>i>_<+~Ii<l:~!!<;
                 ."^  .'"",`^,`,""`',;^^':,""`^'"^:"^";,^I:;l:
                 '!i. l!IIl"i;lIiI:,!I^i>!;"<~"!<!"!lIl'
                 'Il. "";l!"IlII!l:"i>;!,ll:>l'l<lI!l;;,

                        ^I                                                                  ':
                        ^l   .;l.                                                           `I
                        ^I   ,)\"                                                           `;
                        `,   ,il                                                            `;
                        ^:  ,iI:lI;:,""^""";:lIlII::,l;:;:;:;:";;:;",;;:;",^^","^^,^":,""". ^l
                        ^:   !{/\}_;" .. .',^})x[1i`!)^  .">1I_1; I,||-"):I......'l.        'I
                        .!`   >}-{~]+(?~])i; '-~{: 'l1i-_l:""[_1]__.^[]-[`>       I.+-+_}[~ ;,
                         .::,`",,"":",:"::^,``"^:`^""l::,',^^!II::I`^ll::^;'.....^;';;:;i>i;,
                            'I;;;;I''lI!lll':lIlI!"'lIl;lI."l;;,I".;!;:;I``il!ll;`,!,:;i,.'.
                            "i;1<^:i<"~][.~I-']~+'<III-}^iI~'[}+'+"~"[)!,-l:<__`<I!^]-}'+.
                            `il!lI!:;!!i~:<^>;!!>I!"iIi],i`l:l!>,! !:;<i;l,l!;l"<,!;~>_:<.
                              ...'.  ... '   '...'  .'^-:^!I<!l!>"i>:<iIi:l;'''`.  `''.`
                                                        ":!<+>l;il<!,<<ii!ll


























```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-85



SECTION 5 AUTOMATIC MODE OPERATION



The screen changes to the auto operation screen and the following is displayed on the screen.



SCHEDULE PROGRAM SELECT



AUTO OPERATlON


#### SCHEDULE PROORAM SELECT

SSW



I tax DI SPLAY PROCEDURE



[F2] - l.01 :*. SDF



[F3} - FDO:*.SDF



I 97/07/15 14: 10:00



OVERWRITE



TO DISPLAY OTHER INDEXES. AFTER PRESSING [Fl} .



INPUT THE DEVICE NAAE ANO FILE NAME, THEN PRESS [WRITE] KEY.



DEFAULT DEVICE NAME = MDl:



DEFAULT FllE NAME= *.SDF



::,XSS



MOT: FOO: COf.llANO OVERWR/ CHAR.



l'OEX INDEX I M:lEX HI STORY INSERT DELETE CANCEL



(5) Enter"*" following "SS".



(6) Press the WRITE key.



The display will be switched to the PROGRAM SELECT INDEX page and the schedule program file



names registered are shown. (Files having an extension of "SDF'' are searched from the MD1 :.)



AUTO OPERATION



PROGRAM SELECT INDEX



SCHEDULE PROGRAM FILE



POO.SDF



AH.SOF



OPTD I SPLAY. SDF



=EX



,,,El(



,,,ss *



what is the file name for program select ?



NlMBER



SEARCH RESTART STOP SELECT SEARC~


# I I

NU'-1:lER



SP-NO.



(7) Position the cursor at the desired file name.



0 N 91



197/07/15 14:10:00



PAGE 1



[EXTEI()]


```text


                                                                                                `^^"'^.'"'^'
                                                                  ....'... .  . '..  ..    .    -??}>?"l<>)<
                                                                 ^}[+><~~]>-,l]~~++{]-+-ii1+--{;!_~-_-?+<<]~
           '''`'```````^^^^`````'`````'''''```````'''''''''.'''''''`''''`'``'.'`.''``''''.''``^'``.`''`''`''
           """,",,,::::""",^^^^`"""",,^^^":,,,:,,,:^^^,,",",""",::;,:::::;:,"^^^""";:,::^"^^,::;:::"""",:;I,
                      "+>I:iI!!!^Ii!lI!!"l"i>I^!Ii^;!;;l>;l^;::;I"`l::ll;"l;;;l;:^;`:!;Il,;;:";`l;^":",,,.
                      '";:"l,;;:',;l;!iI`:^,;I^lIl^;>lIii!l"i!Ii>;:<!ll!i"!I!i>l~!l:l<+~~+~<;l>,i<Il~!><!^
                       "~lii_~><i+"<++i<~_<-_^__!!?!!"
                       ;]_l?I"",":``^"",,",:;':;,:,,"'
                       "i!:?^
                               ```'''`'...'..'``^`^^'''''''''^^'''''''''`''''````''''''
                             ";"II+__i-~~<!>~::::;llI;;I;:::;ll:,,,,,,,:;,^"",;;;;""^;,:^
                            .l  :l[-_l]-}?!<?``^'``^;;;"^^^^^^^^,"^^^"I>~i~!Il^!l!!i<!` !^
                            .; .:;_+-[+~;_[-+{~i]<-_I:::,""""","""""""!__<-_1f1x1)|+[<^ l:
                            .; 'lIf/t___I<--+[>I_<~!,::::::""""","""""^^"""l__[[>i-"`!^ :"
                            '; ': ,;I                                                "` "^
                            'l ':                                                    '. ,`
                            'I .l^. ..'.. ..'....   ''''''''```'''''''''....''''....',' :^
                            'I  ^^!-~!;!i<li"~_+-~~+^``````^""^```````^^````",""^```",  ;^
                            '"   .-({:!It1>_,[)>!!!i                                    !^
                            '"   "]_< l'})!!l{{'                                        l^
                            ^I   `[>->}--l~-[fi"{/[}]`l[<}i<)]-<)_.l_<"' '`... .'.      l^
                            ^!   `}([>:?[i{]~-!}tt;?xi,i~!I{|-`;}1ll[1?: _{l~-`i?l.     ;`
                            ^I   ;f11(_`})_+]?v{~ '}[~~.                                ;`
                            `;   `l;:I"'^^I.;<<.'  .'l>'                                ;`
                            `;                                                          ;`
                            `;    .                                                     l`
                            "l                                                          l'
                            ^l   :<<.                                                   :.
                            "l  ^>ii`..    ..    ...                  .   .             ;'
                            "! ."^  '^l~}!"'"li_!^'"l+[[++li~<+-!!ii<;'`>``''`,!"^^^^^. I'
                            `!   ,~!; :,_<~!^:^_{<l.I_)/({!:<1||~;!1{>;;!^;II,`>        !.
                             ";"';~il';.'>~~,, "+-~`:;;;!;:'`>+>lI'iili>"I~+~>^;.    .^:,
                              .`:;";lI`Il::;,';;,":"';l;,;^^l:;Il"";,,";"";"":;`:;:,;;^'
                                i:]<'~I!:-}">i!>+]"il;_[+"~<;+{i:Ii:_}!:li,-_;il;:+{:i^
                               .!IlI:i"!li+;l:!i!i:I,l!i>ll;lI!lI,;li~>l,!I!l:i:;l!~:i^
                                           .   .. .      .  .   .  .....  ...'   '. .
                 ^>: .i:;I,^,""ll;:;::^:!!:
                 "<; .!;!<;.I`^>>!>>;_l`<~:.
                 ':^  :"^'``,^'"":",:.^^.
                 :]> .!l~~i,><,>~i!l~"i~+.
                      ;:"';;"::`':;^,^^,;;;;:;:";I",li;;IIIIl::!I`;I:;";;;I;^^"`"'"",":^`^^"^"^"`'^^``^^':^.
                      l!+l~~-_++i-<l_i>+~<_~~<il!?-!l<~><<<<_!!-ii+~!II+><+~>_]1?;_<<i<<l_i>++<_i<<i[~]_!+_;
                     .!+!>+!"<--~-><+:_>I;+l>~i' +!__l;<<l!+"_l:~~+<~+>;^~^;}+~:'-~lI_~~i_<+!~><<!]+I-]>i`I
                              ..           ... ..   .. ..  `.. .. ........  ..   '...'. ...'. ... .' ... .'
                             `,,:,:;:,;;;;l!!ll,,,,,,,,::;;::,,,,,:;II;::,,,,:Ill:""",:"
                            `l."l+1}_<||/}_\1::,;:,"""",;:;;;;::,,,:;;+_:;:__;IlII;;_].,;
                            :,  ''`''''''''''.   . .     .   .`''''''`_)-][~?_~1+(?[{<  I
                            ,,               .iI!I<^!I:!, ;il"        .'...   ..''l)<.  ;
                            :,   ;<>+iil:_---(?{{|1,>i!>" l~<;             :i<,'.  '.   ;
                            :,   ~|[~/|:',l;;i..',                         "!~:'.       ;
                            :,  '+/_)t!'^``"^.`'..'''                                   ;
                            ;:  ;]/}{[)-1<{f_I;:::;!I                                   :
                            ;:   .     .     ......'                                    l
                            I:                                                          !
                            ,"                                                          l
                            "`                                                          !
                            :^                                                          !
                            :^                                                          !
                            :^                                                          !
                            :^                                                          ;
                            :^  ^_].                                                    "
                            :^  "[1`"                                                   l
                            :^  ,[-"",.,I'^^`'',:.`"..^""^, "^^".'.                     i
                            ,` '<[]+l-l!?i!l~<+{|+_?I_+--~[i{_}-;i;,::::,^^^^",,^^^`^^  I
                            ;^  ;]){1il"'`^":,+[/)~`"{" . ,+<~1".I ....": . ..;;`'``''  l
                            'I^. l_~-++1-i]-l^ ~i_ ",?><~::.-][-<:     `,     :"i_+])},,:
                             ."":"^""`'^^``^`^,^,":"^,^^""^^:,,;"^^,^^,",""^",::;:^^;,:^
                               ^I!~!,ll!i~i;;lI<<!I:l;+~;!,!;+-:i^!I+_;!,!!_~;!"li__;>
                               ;li>>"<<!i+<,i+;~>i;!>,>_;!l>,<[:<:!:~}">lil+>^<I;l_}`]
                                ""^":  "^`^,  "`^^" .,``"" ',"^,^ `"``"^ ^,"":` ""^^,'
                 .`. ."..'.  ''          .   .     ..
                 !~; :~<--<<I+_~:~>__i,[I?]!l{?-~-~i{~I?]<_I
                                              .      . .. ..








```

*Figure from page 10 (2346x3317 px)*


---



4203-E P-86



SECTION 5 AUTOMATIC MODE OPERATION



(8) Press the WRITE key.



The schedule program is selected and the NC enters the schedule operation mode.



{9) Press the CYCLE START switch.



This starts the continuous operation in accordance with the programmed schedule.



When the schedule operation cycle stop key on the machine operation panel is



pressed, the NC enters the cycle stop mode. In this mode, operation cycle



stops after the execution of a main program. To resume the operation, press the



CYCLE START switch.



[Supplement] 1. Selection of a schedule program file by directly keying in the file name is also



possible.



SS w schedule-program-file-name [WRITEJ


## 2. Main and sub file name directory can be searched for using alphabetic character,


## 3. Schedule program selection should be done only after resetting the NC. If the

schedule program is selected during operation, an error will occur.


## 4. When the normal automatic operation {AUTO mode operation by main program

selection) is done after selecting the schedule program, the program should be



selected again.


## 5. When the CYCLE START switch is pressed with the SINGLE BLOCK switch set

ON in schedule program operation mode, the main program will be selected by the



schedule program and the machine will wait in the start state. Then, if the CYCLE



START switch is pressed, the machine returns to the normal single block mode



state.



But the machine will not stop in the blocks containing VSET, IF and GOTO



instructions.


## 6. When the RESET switch is pressed during the operation in accordance with a

schedule program, the part program selected when the NC has been reset will be



executed again from the start if the CYCLE START switch is pressed.



If the repetition number of the part program is specified in the program block



selection block in the schedule program, the program execution stopped during



machining will not be counted.


## 7. When the CYCLE START switch is pressed after; selecting the schedule program,

the main program is first selected and machine operation using the selected main



program begins after the completion of main program selection. If the control is



reset while a main program is being selected, the main program is not selected.


## 8. The main program executed in the schedule program operation mode is cleared

from the operation buffer after the completion of the program execution.


## 9. An asterisk (*) is displayed at the beginning of the file name of the file which is

selected currently.



When the PROGRAM SELECT INDEX screen is displayed, the cursor is



positioned on the file name prefixed by an asterisk.


```text


                                                                                                 ^^^^', ^^'"'
                                                                  ....''... . . .'..  .. .  ....`--_]i-.il<}!
                                                                  ;{?~i<~_[;-'~-<~<[}-?<_l<)+_-]"~_<-~+-<~<[>
            ```````^^``^^^``'````^```^`'''''''''....''''''''''''...''''.'''''''`' '''''.'''`''''.`'.`'`''''''
           .:::::::""::,,"^^"^`^"",,:,,^``",;;;;,,,,;;;;;;;;;;;;::::;IIIIIIIIII;;::,,,;IIIII;::;:,:IIIII;:,:^
                  '_i  >!!!i"~i:!~~<l_:Ill'
                  `!;  ^^:;;`::``:^:':.":l'
                       !<>:I!~><~>~,<li<!<!,<,~++>~<<:i!!!~>:~_;I!><!II~!,ii<!<iil,iiil~l!::!;li^
                        .^.`"`^",,"`,':l^:' "':,,""::^;,,^,;`,;`,::l:,":;^I;:;III;">!I:!;l,";;Il^
                  "-i  <!!!!"<!,;ll!;i::ili~<""Ill;:
                  "i;  ^";;I'"I^""^,;l"^:"I;,.:llI;"
                       !llI:-~>~"~i;,Il<<l;;!l"!llI<!i::;:>l!l!~>!>;:i+Il+i:!IIilillIl!:lllli!<;
                       '.^,^;;":'^,^`""":,:,;"`lI:";,,.`^^I,,""I;,I,`:I`^II"l"I<,l",:Il"!l;iil:,
                 l?~~~^!<!,!!!!<<<^i>i!>!I;"l!i!"<li,!>:^i,>i;;Ii!!:!:"<llI>:l^:iIIl::       ;c(,`^':'
                 :i!~>!iI:_<;>]~;~!++<:~>i,!<<<:i+~<,<<<<l`l~;i<+I>!>+i!>>~<>?l~!!>i~i     . [c~;:"!:"
                 i<i<><_>,>_I:<!"<l~<i,l<i"~<i>`<>+I"<!![: :l`!>i">!!<> l~<Ii+!i';~<_!       ,,????;""
                 I_~?i;--?I~>i><<!!<><;!I<!i+_"~>i-<?<: <il_+~<><<~+I__->-~i!"+<-+i-<i       lI;,:" I^
                 !><<+~~,?<-]-l:_~_<+'            .                  '.     .'.  .. ..       .`''''``
                             . '^''`'
                 <}><>++<>~>-.   :^  i_!i!~!i^I<"!^<i~<~I<,,>Iiii>;,-<^>!'<>l!i!^!ililI`l^<!:;_!`l!ll;`l'l!I^
                 ",:II::",:"I.   ''  l<i~~_~l',"`:'I:;l;:l",l:<llI"`I!`Ii.l;;l;!`;!!Il<':`II:^i!`I>;II'!`i!!,
                                     l;I<<i!"
                                     l>I  ';;IIiIi:,l;IIl!,l+;":I;l,;>><l!>I.
                                     ,I:",^!;;llIi::!;+i!i":<l^:>;>;Ii!II:i!
                                 ;^  :I"".^^"'``^';^ ^^^^.`,''"`'. `" ^` ''`^",^^",^'`^^`.`"^^^"`"^.^^``'``'
                                 i:  ~?~<I+<<;_<+;~>:>_<+I!_<~~<<<:+?:>?;<+->>~~~!<i,+_!?><[+i?-~_+:<~]~-~+<`
                                     '`.'i^.~:`i"'
                                     . .
                                 _;  ~~i<~_!-,li!+i~+,;?+~>_>>.++i!+<;+!`-ll>'>i+^I]~>'!>i<]<<l>+<^_]! '?;_+:
                                 '.  i<>+~>++:~i<]<_>:~l~_+i?~il+i<<<:~~i<+_<l"l+:<~<~^<?+!<i<~"^,.^"^  ^'^:`
                                     ""`:,,,,^;`II,;"':.;::":I;.::"`>";i;"I;,,.":.;;";.Il"^;;::
                                 l^  IiI,".;:^.:,:,:^"":""":I'.,",^;,"` ::^::"`,^,:.'^"`';""."^'",:,'",^^"",'
                                 I"  i~~~>Ii+!;~>+i_Il?-<ii_-l;]_~![+iI;-~iii!"<<<_;l[~i+-~~;i-,l<?<;-<>[>_i"
                                     i<~>>~!i":I`+!ii"-++":+i_~-i-"<+I:_>+~+>?:i<!-<_>:._>ll-i?_~<;^?>i>]:i-:
                                     ~-?+~__;+__->.              '             .  ^   ..   '..`'.. .  ... .'
                                     .'...'' ':^''
                                 _"  ~+!~i"~>::Ii!!i!,_i<-~;"<i<!!^<^ii>>il!">->:+!"i<<~~I~"~<:>!<l^!!>ll^li"
                                 ^' .<~<ii;i<>!~;>I>!;>!<i,;l~i+~!;!!<i_l<->,~<<;!<I!ii<>I~!<~l!><!I+<~<;;_~"
                                    .!!<:!l<li<+l<l<i<[>+!;+~<l_+<i:li>_:I+~;I<<:i>I]<><lI<+>_!l~~_<>~>>-!!+,
                                     ~~<+_++iI<I_+~i:I<;l<>i:><>><l~,+i^++~,<"~<:!+_>;<~_< ^!l+i !!+>,!liiI+^
                                    ._>>+~+`<_-+_;i!:~~++_+i^?+Il<~<_+<i:++>!~!I~;]-Il><~~];!~>_],~>~_l,><_]"
                                     <~_-,. '```'.'`'````^^`.`^''`^^`^^^'^^"'^^'^'^"``^^`^:'"^"l,'"^""`'^"",.
                                     ,:;l'
                                    .-lI _<:'!i<<ii~'I_<.iii'_<<",>.+>l'~+i~<;`>i!~>i~!l`<~->i ~+.ii>:,_>iii^
                                    .<~~;i++;i<;"^^:.^:".":^.;,l`',.,,, :;::;"';:";;:;I! :,I"^.:" lII^`l;"^:'
                                     ";l,;l!;:l
                                 I. .::^`' ,^.'I;:!;:'"",":'^`'^^^^^^^'^'"`'',`''````^``.'`.`''''^`''' `^".'
                                ._^ .+_<+i,+~I;_~>[>I`?+_+_,>!!<>_++_l:+!<<_;_+I;?_+<]-_;!i`?<><>--!<~`~??'>:
                                    .i!<~><i!l>;+~><l`-<;I~+:!~!->><"!-+~!<+ll<i_li_~"+~;I_+:><<l`i+++:<~;_+^
                                    .+<~>!]_>l+_[-;->+ii]_I~+-><-_+ii~_~_+-l?>_-?i:_++~+;iI+~<~_<i``^`.``.`^.
                                     :,:^":"`';!:^.^`"`'^,^,;;`''""`^^'^^"" "`",^ ';:::^^:^I:,;I:,
                                    .~'!~;'<+<<~il:'<li_<i ">^?i^"!>!`<Ii>I<l.!^`+iil+li`;"`+i':!;<>>i;"+!!_'
                                    'i!<i>l>ii->i~"!,+>!I>!i!ii-:l~<i<-<>l~+l,<!i-+_i;<<l!l~<~"++>-~<~;i><<<^
                                    '~~<<<i>I;i>_>:>:i>I:<!i~<<i"II;_i!l, ;!;Il;_ii!:^!!ili<lI`!i<ii!l"<!Il-"
                                    .l!<!lI!<_"<~"l>!l~^!!!!<+<
                                 ^   `^'..'' '`''^.` `'''^`   .''.. ......'.`.......... .'   .. ...       .
                                .!' ']-_-i<+~;>!i~i-:-i~-<>,__+~<l~I~<+<~+ii[?<`!+~~><<-<+~:+~~+++-!!>!?_~~l
                                    `>i;li>!:>;l>i~i"i"+!>,+~<l+<i:<i+;>+>i~ii,~i>;?_!I;i<ii!]<,i~+>__>ii>~i`
                                    'i>!!i_i:~>~?i!:~-!,<>Ili>>>~>i>i:lI<<!>;il~>>i+l!i><<__!:;<i_<l!~iil>ii'
                                    ^+i<[!_<:><-iill+<<"l>!;i!!_i<>il^>:li>l">~!_i~!:I~+>l+l!' i"!<"I<l_ii">'
                                     l<><"~<I+"!"!<>;i<i?-<~;:>I_+>_l~_?<<-_I:+~:<>->;_>~]i_i;-"!+!i__~<-~~
                                 '   ^.  .              .        . .. .                 .'
                                `['  >~-,><]i"~!++<?~:<<<il~~<"<:_+;I>~+~i<-,~l<_>->"i+_!+-<>`!<i_i"~:++?++-"
                                    "_!~I>+<,<~~>->~iI><[+;![_i;->Il><>++-~>Il_~[>;i!>-~<<;~>>i!-~<,'.'`^`'`
                                    .''^ .'` `",`"^^^.^^`" ^^,^ ^^'^"`",,:^"'`"`",':^:i":^.:":,";:".
                                `_. .>;.l!iIl!"':".I'lil!lIII^;l;i;^lI;l:";:"^!,l;`ll`':;,;.::,;"`l;';l,I;`I.
                                .!. `<<;~-_+i~Il>!I+,I!<i!>!!^!l:i!"!>-~l;l<!:!,!>"li;"><;<^i;;!>"!<^>i;<!^~'
                                    '>i<!!~!"I!Ii;><"
                                    'I!"^^ I;" ,;I:;;lll!: !!:"l:I" IlllI;.^"""^^'." ';"^,^`", ':^'.`'^`^..^
                                    '~+~~!.~+~ ll~<i++~~?l.+_ii+<l^ +-<~>~ I+i+~>^`-.:]___?~_+'^~-:.<<<~~'"-'
                                    "<!<?~<i~>l~:!+>;]>"+_+_;<>~~<_+:<!:?^i-~_<+]`
                                     .                . .. ..' . ... '`.' .'.'.''.










```

*Figure from page 11 (2346x3317 px)*


---



4203-E P-87



SECTION 5 AUTOMATIC MODE OPERATION



[Supplement] 1O . When there is no file where asterisk should be set, the first page of the PROGRAM



SELECT INDEX screen is displayed with the cursor at the top of the file names.


## 11. An asterisk (*) ls not displayed in program selection such as external program

selection, other than the schedule program selection made by an operator.


## 3. Cycle Start and Slide Hold

(1) Cycle Start



Press the CYCLE START switch on the machine operation panel to start the NC operation with



either the selected part program or the one-block program entered in the MDI mode.



(a) Cycle start after NC reset:



This is effective during automatic operation or MDI operation. The program is read and executed



for each separate mode, cycle start requires the following conditions.



[In automatic operation]



The schedule program or the main program has been selected correctly.



[In MDI operation]



The one-block instruction has been entered in the MDI buffer.



(b) Cycle start after shutdown by single block or program stop:



The next block can be executed by pressing the CYCLE START switch in automatic mode.



(c) Cycle start in slide hold mode:



When the CYCLE START switch is pressed, function generation which was interrupted, begins



again.



[Supplement] 1. Press and release the CYCLE START switch to begin the operation, but when the



machine is stopped temporarily due to the activation of the SLIDE HOLD switch,



cycle start is made when the CYCLE START switch is only pressed.


## 2. Pressing the CYCLE START switch during the program selection, sequence

number searching and return search is ineffective.


## 3. While the SLIDE HOLD switch is being pressed, the CYCLE START swltch is

lnoperatlve.


## 4. During the operation, the RUN lamp on the NC operation panel comes on,

excluding the slide hold mode.


## 5. Even in the data setting mode, cycle start is possible provided that the mode

previously selected is auto or MDI and the setting of bit 5 of NC optional parameter



{bit) No. 2 ls 'T'.


## 6. When alarms (P, A, B, and C) are on, cycle start by pressing the CYCLE START

switch is impossible.


## 7. An error occurs when the CYCLE START switch is pressed after return search has

been executed. In this case, cycle start is possible by pressing the SEQUENCE



RESTART switch.


```text


                                                                                                ''``.`..".``
                                                                   .  .         .     .         +]-]i-,;<i]I
                                                                 `}}+>i_+}i~;:?i><_{]-<_!i}~__1I;?+--+-~<~-<
           ''''''```````````'....''''''''''''''''''''.............``''.'`''`'.'` '```'.'''^````''^.^^`^'`^`^
           """",:,,,,,,,,","",,,"",;;,,,","",::;;;:;,""^,:::,""^,;::::;;::::;:"",",,^":::::::,",,":::;::"""`
                `_!I!!>lliI<:    Il 'i!:I^II:,""^""">;`;l;;:^;;I,,I^,;"^I:,:^,;,`I,^l,;^,,,"`:,:""llI:;Il;ll
                "il><i!lI>I>;    ;l.^]_>_<~+<_~>+i~;~+I+~++<l?~-<i+I<><+~<>~l~_>:><I_~+i_-[>!~!<~i>i~i>~<<+~
                                    ^_-li<l;.++!+i>,<!<+>^iIl-_+_+<+!I+};<~>:!>>~!'?Ii~i!<<^+!+~i!_i:+]i+~,
                                 '.  .      .            .       .            .                    .
                                '<l "]l'??-<~[;:i!^<"I>l^[+~_<<_~"_`>>i_!<i,l_>+<+~~`~<>>'+>'~_+i!_<,<i++<~i
                                    "_--~+>i,,+-_~;+~_,+~!I+<___<_;!<i+_<~,!~_<~_<i;i~+];i~:~>;~<i<~<>^,"``'
                                    ';::,,,"^`:";,'";I'":,`;"::::I^;,:<";,':I;;:;;"`,;;l^:i`!"`llI:l;,

           1~     `|-__+[):-f1[][_:{-_1i_/}}[}~:1[_?][.
           ~i.    ._l1++<1:l[_[[>!;)__};![+]][_"__[-[[

                 ^i>' i<+~-:]]__^                   ..
                 .`^. ^,:^".^"""' .     .   .
                      <!!<_:~il^i!i>I+`-<<?_+'><+<<^I<'~_l"i+i+Ii>'>>>l+_il"><i~;Il`><_:I>!^?+""<<<>-i<:I<]!
                      I<]~~:~~!I+<<>_<Il>~i!il<<~+Il!i><Ii!~i_<l~l;~<~i+~I!>-_>+i!iI-+<+~+i:>>!il;::;,:`":;^
                      :;,,^ ,:^^lI;,II`"ll`I,;<;i;^I,"!i^II>^llll"!;;-I!I^lIl!;!l;;:!>"<il^;Il><.
                   .Il ^;",!',;:"'l;"'ll^',"":
                   '<~',l>I~^!!l,;~ii`!>:"i>>i
                       ^I;I';'I~;:I::^I";;"`:II;;!i,^I;;:il:,";:<il^,:;,II,: '!,,^:,:::;,":^;:;,:,;,,,:""I,:
                       ;ii~!<i>>+><<<!~i><]<<<<!<_<il-+>>_>>l!i!_><;_<~i~i!i^`!<~i~!_~!<I;>:~~~;+!<l>i~i>_~i
                       ;>^;+>i^:><il!~I^!ll_:^+<>>"_-~,;+><<>_;+iI;<?i~~>-:>~>_-<li!
                       ,;'"",":,;:`',","I,"".                            '
                       i~"i~i>!I~i:"+>!l_!><.
                              "!I^:l;;::";'::;III;`I^l;"";;;"";,;:;:^,I;^:::;'":;,;I,"^:,,":l`
                              `"l":I,IIl!!;i;<~!i;"i^li;,lil,!!l-><l,:~~,l<<>^i~>>>_i:l~!!<~-i
                       i~:+-~>,>iil+i!i.
                       ;:`,::""!:,,I,:;.
                              l>+;;l~:>~i+!!_-<i~+iiI<~~I+<~>,~i_>><;lI_+iI}?<lil}-!
                                ^...`'''''..'^'^^^'' ."" ^^^^ ,'"^`" ''^^^ ::"^,::;"
                   ^+i.li>~+,>><l;_~!^i!!><!il"lI"<!!_,,~l!i`!`I;I!Iil^I!Il
                   ':,.^::":.",:'^:,, "^;,:":".,;.;:!l"`;,:,.:`l^:<:l:';I!I
                       Ii<!:_~>l?<!-">~I:~!I<i~li+>!il:!!~>~>>;i>:l!lilii,<i+_->:~<~<!;>,<!i!i>-i"!!!<l
                         .. `'. ``'` '`..^''^`^''",`":",":::"l"^,^^``^",^`"`"""'`;:::^^:^l;:::Il:`";;;;.
                   `>!.lii!>">~~I;I:_>~,!l<!;iI>_"
                   .:: ^,I":`:::^""";,I^";:"";:,I`
                       l-<!!"~<!;>i>ii-"-!<_-<^<>_~~:_:>i~~+<+`<<i>~>i^><>~i<_i<"!_~>>^>>+"I~+>Ii~<>!`>>><<;
                       !<>-<''^`.'.'^"^.^.'`''.,"^^`'"`,`",,""'`,^"""^'!,":",:",'",":"'::I`^:I,^l;;;,':;i;;"
                       :ilI".
                :<::;l;,^,,l.   ^`  ll;:;`:,;"::::;,"!"^::I;^l,:l;I!!"""::,`"^""^^^^:"'^^"^":^^ ^'^'^"^^`:`'
                l<!<<>>!l<i+`   ""  !!~~-l_i<;<~~+_+l++;il!ii_!i>i~~>">-~+i:<!i+-_iI~-!<-?>][__"i_<I?i-i;~~I
                                    ;i+>l~<;,i"->~i<<">>l~ii><I>^-!I">,~~:l_>!i?i>",!:+>`+ili?,I~_ii!:~+?>i'
                                    l~~_il?_+I-:<__[l!-<_>!-+l>+++~-!i+<_--ll~_?~!l>;<+<:~<~<<><...'..''''..
                                    '"''..``` `.'^^^''^^,...^.`'..'"''`.``' ^"^^".'`.^^,":'"""""
                                i;  >Ii!i!lI <I,.lI!!:~.,~!><<; lliI>'`;"l,I ;I:.l;;l;II."!lI;I:I'.lIl;l!;l"
                                ,^  lI<+_~i~;><!I<!ll<~;;<>>>l,;<+>_iI:>i<-?,<<<^>;!+I!I':>!ilIll^.i!<i>!Ii,
                                    :l;;l<"`~>!;!!I_,lI>^l+i!":_<>I!^<;;>i<!!>l>'
                                ,`  ^"^^' "^  ".`^^ ``^."' ..'.. . ....        . `^..`^^^.^`'^`^`^` ..'.. .
                                <I  <-~_+^~-l"[i~+]^i+~+-ll-+_++^-,>?_<];?<_+_-]`<]-"<i<~>];;_!-_+;"?~-<i^_;
                                    li~~<<-<<~                         .
                                    ..'`. `....
                                <:  i<;!!i -<I iii;<_!! "~~:"]i]~'~>i<`;<,:?<^I-<^:<<<i+>>I'i>li;'i!ii<;'!I.
                                `'  !<>i![l>!_!>>?<+!~i!!l+!l_l," ::"I.^:'`:;`':,.^ll::I:;"`II,;^.;;:;l,';,'
                                    :II;;I:>;;!:"iIl^:;Il`ll!<^
                                ;'  I^`^ .^ I^. "`^ '`,^'` `'."` '^`,^ ""^"'^.````""".'``'^^`^`,'^.,`'.`'`^.
                                <: .+i~>,;<"_+l:-+_"i__i!]"i<~?_^I_>_+^+_+!,+"<i+~+_]`+~<~+_~i;_>+`+~I`<>~-,
                                    l>>!>li+l:--~i__~>!!+++,~:[_?l_<~i-<;i+--<+!<>_I~l_i]~,!+~ii~_!~++_i~++^
                                    ++?;+-I"+I<"iI'...'.'.'.' ... '.'..''''''',''.'.''' ''.`"'`'^``^^^^'^`^
                                    ``".',' ..` .
                                ~"  !<;I:';l;:;:"_';"`_.:IlI;!^lI,^l^.;:l!`;II;:I`":;;;I;":;:^I;lI:!^IIl!il'
                                !^  >~~_>:<>~i>il<I>i">`Ili;:!"il;,>,`><!<"i>~;:+;!li><i~+:ii"l;lll_"!l!~!l.
                                    i<<>+^iIl><i><?~+l
                                `.  .              .  .`..'`'`.'''`^''`'  ....          ..              .
                                !^  ~~:+<<!"<i>!<I-~++I_+llli~!>!l_<_+<:l___~I<ii<<~~<<I?[-,l->ii,_<+!~l,<_"
                                   '>i<i`!!>!I<i<'.<:~>~:<+<i'l<!~I:+<<;<:>>>>_~-I+!I<<~<~>i;~~I>[__++-<_+{"
                                   .?[?-i_--~;~<_;;:'^^:`:;;;'"l,:"^;;,^;^;::;:,;^;;,;,I;;"i"";^"l,;;;;,I:I'
                                    ;<l!;l>;"'>ii!l`











```

*Figure from page 12 (2346x3317 px)*


---



4203-E P-88



SECTION 5 AUTOMATIC MODE OPERATION



(2) Slide Hold



By pressing the SLIDE HOLD switch on the machine operation panel while the machine is operating



as initiated by pressing the CYCLE START switch, explained in item (1) above, axis feed is



suspended or program execution is stopped.



(a) Slide hold means the NC halt is made during axis movement. Start-up hold means the NC



halt made before or after the completion of an axis movement.



(b) Slide hold during function generation:

- During axis movement by rapid feed or cutting feed



Axis movement stops after deceleration. When the axis stops halfway in a commanded axis



travel, it is in a slide hold state. If the axis reaches the target point before it is stopped, or the



operation mode stops after the execution of the other commands in that block are completed,



then this is the start-up hold state, and is the same as a stop in the single block or program stop.

- During dwell



Dwell immediately stops and the machine is brought to the slide hold state.



(c) During operation, excluding function generation



(durrng the execution of miscellaneous commands):



The slide hold is not effective for miscellaneous functions but the SLIDE HOLD lamp stays on. The



machine is brought to a start-up hold state, since the operation halts after the execution of



miscellaneous functions.



[Supplement] 1. When axis movement and miscellaneous functions are in the same block, there are



two cases for the execution order of the commands.



a) With . . . . . . The execution of axis movement commands and auxiliary



functions start simultaneously.



b) After ...... The axis movement is completed the execution of miscellaneous



function starts.



Depending on the above conditions,



if machine hold occurs during axis movement



(including dwell) ............................ Slide hold



if the machine halts at a time other than



axis movement ............................ Start-up hold


## 2. During the slide hold {excluding start-up hold), the SLIDE HOLD lamp on the NC

operation panel comes on (although the slide hold state is a part of the machine



operating state, the RUN lamp will go off).


```text


                                                                                                 ```^." `'.^.
                                                                   .. .' .      .'.             ^]-?}i-.<I~{l
                                                                  !{]~<-++]l?._+~-~]}?_<-I_{~+_]"<~__<+->~+];
           .`''''''``'``^`^``````''''''''.......'''''.............'`'`'.'''''..`' ''`''.'''''''`.`'.`.''.```'
           ':,,,,,^`^":,",":,",":,,"":;;:,,,,,,,;;;;;:::;II:::::III;IIII;:;:,,,,::,:IIIIII;,::::I;;I;:::::;I"
                  "+;  <~i~"!i!i.
                  ,i:  :;;I'^;;;
                      '-!,!!!l!:!li>;-li>_:i+<I<;i!!!>^l:i>l,li!!lI!"!!ll<I!::l;lI:il!l!i;":IIiIII:;^:;;:!;:,
                      .~+:+~-+_!_l<i">ii!~!!I<+<,+~~+i>i:++_<__!ii<~i<!>>~i~i<+!i>:-!<>I~<"i_~>>!!l<!i-~i-l~<
                      .+i'!~~~+<l"~l^+l>i<>_:l>>.l:ll!+:">;i~>" ~<<>>: >~~!+><<,"i.~<l,`iI.+_i!~: +>-^l_~<`!I
                      .~>?+<!!+~ll!:-i+_+_I:-~+i~?+>"_,?_--~~>
                        '..  .        ...  ....   .      '' .
                    ;?~.~-<],ii<<:i~<>~:~+;l_!"<~+:>"!<i_"iiIi<;!<<;I<!!<l>>il >{++<;+;<i+>I<<~i<;?~Ii-<'
                    .`'.~~]!ii~-!l~-+<<:i:<+~ll~+:l<l>+~+!>l!<<_;~<<:!>i>>~+<>,'"""`^I'`""^'^,:^,^":^`:"
                        ^::.^:;;"^;:,,:': I,l^^,;',:"I;;;I;^I::l^!!!,,III>l!iI;
                    ,>, !I;i^:";:":^,"^:::"l""'":,,",;"".
                    :~I !!l~":li:,!I;l<"iII>l;"--;ili~!I^
                         `~,;;l":I!""l;:;:;;I;;I.:l;l"I;II,;^;li::^iIlI.
                        .'::",<I:II"^:;;I":lI:">'I+l!^Ii!",;`><!,i:!>il
                         '<l>'"i;;!llll`:>Il:^>ii'^I:lII,>l;;  i!Il`'!:';Il""iI!l"l!<ll!^;"^"^;;;::I:l!I^I,;`
                         ,<~>!;I>!iliilI+__<~!_<~!i_!I_~+-!i>;^iii~i;<ii~><!I<~_<;i]~<+[!iIl!li<~!>_!++>;++>:
                         "i~i~l,Ill;Ill!~+<^!i~!l_-+: !,<i:!++!:+_><~+:<~!:_!-+:!~i>I!+<!ilI:!"i<i_~<~':>"_~:
                         `~>~i?+iI"il!-,l~<+l,_-+'_il:<~i;~<<l`<,~~,,?!>^:i!>>l+!>~^>"+i-:~>l~"!<>^iil~~~_><.
                         I]++:-~<li~-<;-_-~i~l>>_i<_-?:l+~i<>-<i!+~>>;_l!;-<~I<!-~!!<>++!<+>_I!li~!~<<~l<_<i.
                         '^^^.'`^'``""',,,`^;'^,"^":;;^^::^,"",",I,":^l":^;:l^,^:;",,;<I^;;:;^:`;;:<;l,^;I!l
                       .`,_><>_I<_~]!
                         '^`'`:"````'.. .  .       ..
                         :__+]I>~~<__?}][!i?--~I]<~<?_:i_-~++-;_I_>~i?]>>>!_~:--_<I~+-;-[?_^
                        .                    .  .    .       . . ..'`,...' .'.`''' ''`.`^``.
                    l~;`+i~<<>;~<<>_><;'~><>i-l+I~I><!i"l_i<>l+!>;
                    '`'.>_i<+_l?_I<~~ii_+~Ii-!<]i<+_><~!+_I~<<+~+i!>l'
                       .I;"^"l'";'::;::;:,',"`,,:::I,:;::,';",::l,Iil
                        !I!;>I<Il!>ll:;Il;_+!!!l:i;^IIlIll!:!;,l;!:,iil!;!I!<>l;_,<i_"><i,l;>Il::i!;;"I^ i!!'
                       '!!<<<l~:ll!~>!l_~I><;>:_~<<,il~~~~!i_~+i"~>i~i!_i;ii><<<+iii~!+i;<_!~!_<;<++<l<!^;l]:
                       `><<!!i>^l;"<!~~->:l!`i.<~iI:~:"Ii>'l>~~: iII>:"i>',><!!-!>""i-+l`?-+',>+'l><<i<~~,`~"
                       `>i~>+__>_~i<;<~>>-!i+.
                 ''        .         .'        .       .   .     .
                .?]+-?+?~-~_<    !. '_-~_l;_iili>>~><~iI<>>ll~<><__i+!!<!i!>><><!l_~I!>-+l_->+!_<>-:i_~<>!_~`
                 . .'.      .       `_~l:<_~+il<:+~>;_>><<]<i;+<?~:~<_->:ii~<~_<~?;`.'''^'""'"'^^^^`'`"^^^"".
                                     ":^',:,:"':."":^;",:,:"^',":;.,^,""':"",,;":;.
                                    '-; `_<[;       :<>: >li!;<li' <^ <!> ^!;:!<l>i~ li<i><+!~~ i>il.~!>++<i'
                                     "'  ''`'  . .. <i~<<<<~I++_<l!~;<[><ll!<+!,^:^" ^,"^",;",: ,,"^.;::,;:I.
                                                    :l,;;,,:';;l`,:";l!;,l::;i`
                                    "-: '_?_>...... I<!":l;,I;;:lli!!:;"Ill!!l<iI<>!;>!il!<Il,iI!!ll>iil!lI!.
                                    .;^ .",;,...... ii~i_~>I<~~+i,lI:";";;:i;llI,:;I:lIlIll;:";";Ill!I!;!Il!'
                                                    ll:llII^i>;I:
                                    ^<<il!l<!!:;!:~l^I>,,;`::;;>!;Il'
                                    ';I!::,I,>I,:`l;^l!:;l`,l;I!I:;!.
                                    ^I,lil!!II";!!'I!;:i,I<!Ii:,!i:">!lii!ill
                                    ^<i<~<->>l!~~-<:::;;",l;"!!:!I:"I;:I;:I,,   :I";`"^""
                                    'i:;:l!^<"!il<i                          .'.i_<]lI<><.
                                    `,;I;`:;:l,",':!+:">,;l!;I`!<lI">Il^
                                    ^li<il<~+<>i~l!>>;:>:II!Ii^i!i!"!i<"        ""'`'...'.''
                                    `~<>'!<l!~l>!>'           .    .    .'......~?--l!]:><<>
                                .`  '^  '  '.  ..  `.''....' ''. .' '.  .. .. '.  . .''  .. ..        .  . .
                                ,_  I-<>i?i++~;~>?l<<~~;-_~_+_>?!!]-_l>>;>>~+.<+<:[l><["i<+!>:i-i_^!i"_>;![i.
                                    ^<i<!_~!;^i<I~I:>ii~i`i;:___il!-:!_i`_~-i!><~,<<_+,~:!:<~>,~![+i:i<<~!i>
                                    "~~~i_+>l;_++>`?~l<]i_>!i~<Ii~<<!:l]<:":"',,,',,;;':^,";:"':^,;,'"I;""":
                                    `lll:i!I~,>i<l'iI:"l;!:l>:>"l!^l+^:>>























```

*Figure from page 13 (2346x3317 px)*


---



4203-E P-89



SECTION 5 AUTOMATIC MODE OPERATION



[Supplement] 3. If the machine is brought to the start-up hold state by the activation of the SLIDE



HOLD switch, both the SLIDE HOLD and the RUN lamp go off.


# ACAUTk)N


# I :

Cycle start in slide hold is activated once the CYCLE START switch is pressed. (In the



start-up hold state, cycle start is activated when the pressed CYCLE START switch is



released.)



Examples of slide hold:



[During axis movement]



Axis movement



----,.. Slow down Slow up


# TD"""'

slide (



SLIDE HOLD hold state



CYCLE START switch



switch



[During miscellaneous function execution]



During miscellaneous Miscellaneous function



function execution execution completed



Operation of next block



ll( ll(



During slide During start-up



hold state hold state



SLIDE HOLD switch CYCLE START switch



Fig. 5-2 Examples of Slide Hold


## 4. Even if the SLIDE HOLD switch is pressed

during the execution of a tapping cycle -



G84 {tapping cycle) and G74 (reverse



tapping cycle), the tapping cycle is not



•••••••• Rapid teed



interrupted. Slide hold is activated after the



completion of the tapping cycle. The



machine will not stop operation, but after



the operation is completed, it stops



operation temporarily. Note that the



synchronized tapping cycle (G284 and



G274) is different from above described



tapping cycle. For details, refer to



. --Cutting feed



SPECIAL FUNCTIONS MANUAL No. 1,



"SYNCHRONIZED TAPPING".



houring this period,



slide hold state is



not activated.


## 5. The slide hold function can be activated and deactivated by the programmed M

codes, M140 and M141.



M140: Slide hold ineffective



M 141 : Slide hold effective



The SLIDE HOLD switch is inoperative for the blocks containing M 140 and M 141,



and the slide hold function is not activated even when the SLIDE HOLD switch is



pressed during such period.



Note that the control is in the M141 mode after it is reset


```text


                                                                                                '^`^'"' ^.^'
                                                                  .  .'...      '..   .        ._?-]>],:il{_
                                                                 `}[_<<+~[i~;:]>~~-{]-~_i!1++~1;!-+?+~-+~~-<
           '''```````````''''''''`'''`'''.'''''''.'''''''''''''...`^`'.'`''`'''`..''`'.'`'`'`'`.'`.^'``''^``
           "",:;:,",,,,""^^`^,";;,;;:::^^"^^^^,,,,",,:::::;:;::","",:;:;:::::"^^":""^,;;:::,^",,,":,:::",""^
                .~>;ll!!!!l~I   'i  `l"I;';I;l!;l`;^;:",;I^;^,l;';;I:':^::;I^IIl"`:`lI,`;;;^I;,"';,;:^;l^I!!
                `ll!i!llI!;iI   `l. ,~i~<il+++++<I~!-i~_-+li~<+~!--_<;-l!<_<I}]?_;?!<~>;-<_~+<<I,~;!~l!~;>+~
                                    `<<>I>"<<>>>`li~+^i<,l<;~-l`+i>;i,+i>,i<:<~!+I++i~"[l^_<
          ':^,^;^":,:"l.^:,:^``'`'''` ''^'``...'^^``'' ...'...^^'`^"'''..`'``.'``'. .'`^^`''``'''`..'.'`^""^
          I!|n<+([)j)t}`!;^+~~-+I[-_!>I>~]]!++?;~l~+]<+?_~;_<<i~[+l+<++i-I--+?[-:<+-+_;>!><<~~++I.~~I~+i^"^!'
          "tm0U[1\-|11-.;' !~<<;lli!i!,i!<i'I!il;;<!iIi;>illiillI<;I,;>I;,I;;l;I^><<>liI>+<<+_l!;"i>"ll^   ;'
           ` .'` .. ' ' I. <~~l:~::!>!,>><i'l~!<:li<l:l"<i!l~><Il<i~;:<<:<l~<>>i;lIl!I<`~l<+ii`>~+<<"~"    I'
                        !'`<]--]__<!                                                                       !`
                        ^^"l:;;I;I;;:;","""",:;:,"""""""::::::""""""::;;:::""""""",::::::"""""^,::::::,^^^^I.
                          `-i-+<_~?Il<;]~?;!<+~.
                           :"'``^.```.``'``'`'`^
                          ^1~+il]l-~_:I<!<~i~+<?
                                     ^i!;,!;lIIl:
                                     .,,^`,":""il^`^^^`             ^..
                                      ^`````'^,<<i;!>~I            `->~;+; .`""^^^^^^^^""'
                                      .......^i'"^'                     '^,"^'...........
                                    `^^^^^^"":>`^liil,,;II;,,,,,,,:I,:!~>l;;III;::::::::;`
                                            '<l  ;;`^"^,,",""^^^^^,>'.i`   ..............
                                         .,:,;.     .~~~<~>+~:        "~`.
                                 -~>[<I_><<         .i__l]_>.        "Il>il:!li>,;;l!"
                                 i<~<^                               `:":,,"::I;'lll!"
                          ^[>!~i~;<<~i>~~!>i!>:>l!<<<!:<>>l><i<l
                          ':^"^^!^"":,l:!::;ll,!;;II!,^;::::,:;,``..''''.......'.
                                     '_~_]_l~_]?[--l!.          ?]?_]]+_<->+_-_>,
                                     `<ii><;i><!+i!'.''``'"I:;' l!!li!;;<>+~~<i
                                      `^`.'^^`<"`^^,,,,,,i_l`'       !"^`^^^'
                                              <          :;          > ^>i!i~<;!Ii~ii~i<'
                                     :;;::::::]:;lI;;ll;:~_:;I::::;,,-:;lllll`.'.'`''```
                                             .~ .+l,::+: !! I_;;;!+'.~  .....
                                       .'^,:l?~ "..' .'^.;:`..` .`'`'?~`
                                   .":::,^'..  ']??]}??<"  +-}_{[)~;!i;;;".
                             i:;!:;<iI:",:;^   .;;I,!i:    :!i"!i!'     "l<l"^"""":'`^^^
                             lI;l,:I;;";!!i"                            ;::l>I!lii!"<<~~'
                                                :l:',";.:;,::,::"':";;":'"^^^
                                                :l?;Il<'!~<_i_<~+,+;<_<-li<+~'

                                :,  ;;:;";;I;^!I,!i,:Il:::,::;:",^"::::::`
                                ;;  i<~_l!l+_;~<l<~!!<>i_li+<~<l>l<~+___~"
                                    l~!!>>;<~^ii~>!>i<'I<"i"]+<+i[^I~l~" .
                                    l__~ !-]><!~,'<ii_> li>l ]<<I.>_<~<><^
                                    i<i>!ii;~>i-> :?<;;!><i!I^:!lIi^i;:i+"   .
                                    !++~>!~"i+I__::i+:;_+~!i{^l?>+i,~:"<<^   :          .```':~!l!llili"
                                    Ii+ili~-~< <]+{;i<?;i:~i<<+<~!i[?~>~<`   ,               `l~>!;;<i<'
                                    ;ll<<__~<; i~ _~l l-~<i_! l><-I   i!+^   ^          '""^';l;<;I";l;i"
                                    I!i<+l<l"<_,!i!,-i<,>_<>++i+";>!:,-~<'  .~    `"`'' .`''.:!~~!+~I+++"
                                    ii~:,l>i;~<:!;,!!:~:>_+>~+<l`:>;:<<i>'  `f  {^^"ri;`  .
                                    !i< '_~<!>>il '~' i>!!<--><; ;i l_>~<^   >  +'  -,^:;l_+<_[i<~];~_+?+~
                                    I+>>+_!<` +<!-+!<~~~   ,?<?> I~_~ ;+<`  '(  >.  [.   "?][i_?~-;+][?l?;
                                    !~ii<iii<<>> ~_i+<<I`~!<+' !_<_?i >l~^  .[;:>.,:{;,. :[]<+<]_?~?]>I';'
                                    <-~~+l;~"<]]I~_-!<_>Il<~<::II+<>!;_i~^        ..  .  ^l!^!<iIi~<i`
                                    !<i:<I`>'i<-+!;I`<l>; ~<i>_,^<<~>ll<<`
                                    i]-~~-~ l_<<>   ^!il ,+~-~+I .<+~l ;<.
                                    ~-~_!i_- !~l+-!i+<+<_.++~__<-+.I?<'^;
                                    !-i__~<-?<>]~-]>!!_--~_]+~;^`^..^^. '
                                     :^";"^":,";;,;:` :;,""lI:
                                l'  ;":'^l,:.:^:^,^^^I^^ `"^ ,:',,I",;,:`,^,':""";^,:""^"',,^.^^`^^^^^^^^`;^
                                i"  I;-I>+<[l<++!!~>+?~<,!_<^<_"~>+!<++>:~!>,_~+>+i-?~!I]I>+>;_i~]<<>i>_~,?;
                                    !ii_<^,?!!-^ii>,_~l>l
                                        ::^^" .:^^``''^''`":'^^''
                                        _<l~+'^+i+<:>>+;I<-_~~~<+
                                        ;:""".`I:"^^^^,``l"',`^.
                                        <!;!:.^+<<>,ii>,!<+>>!+^
                                    ll;`l:"li",;I"",`,,::`^`^,^,;,:I",,;^:I"^;:","'^^";"","`"l"";^^^",I:^,^
                                    l!~;__i>?!!<~<<l<++~+l>!l>~~-i+-><!~Il<<:+<<<<;!<!~_<i_[>-I<-l_iiI->!iI.
                                    ~l>:ii:li>-"li-I!<Il~<I^~">+I~+_><?~<I+>]l"-<~~"+~ll[I~-~"+<-i~,+~_~+"+,
                                   .~>~<<__;-!>>_I<>+>;+_+i-^    .   . .   ..  . .   .. ..       .  ....  .
                                   .:'^`^,^."^.'I'^"^'^^"`^"
                                   '?~__I-<-:~-:!<>+~i;~I>;_-:[?>+lI_<_]:<]?i;~!!I_~~i
                                     .''..''..'.''..'..`.'..`.''.'..'``^'^'^'.''`.^^^`








```

*Figure from page 14 (2346x3317 px)*


---


## 4. Resetting NC

4203-E P-90



SECTION 5 AUTOMATIC MODE OPERATION



The NC reset means initializing the internal NC status.



The NC system is reset when:



(1) the RESET switch on the machine operation panel is pressed.



(2) the external reset signal is input.



(3) The MACHINE LOCK key on the machine operation panel is turned on or off.



(4) the operation mode is changed over from MANUAL mode to AUTO or MDI mode by pressing



the AUTO or MDI key on the NC operation panel.



(5) the operation mode is changed over from AUTO or MDI mode to MANUAL mode by pressing



the AUTO or MDI key on the NC operation panel.



(6) When the operation mode is changed from MANUAL mode to DATA SET mode by pressing the



DATA SET key on the NC operation panel, the system is not reset; however, when the mode is



changed to AUTO or MDI next, the system is reset.



The state that the NC is reset by the change of the operation mode is called mode reset.


#### NC resetting operation:

The NC resetting operation stops the machine operation immediately and the NC system is



initialized at the same time.



[Supplement] 1. When the RESET switch is pressed during axis movement, the machine slows



down and then stops axis movement. The actual reset is done after axis movement



has stopped.


## 2. Even if the RESET switch is continuously pressed, reset is done only one time.


```text


                                                                                                .^^^^.` "''".
                                                                  ....'....   . .'..  ..    ...."???-!i.-I?["
                                                                  <}-i><<+[!+.]-<<~]}?_~-;+[_+-]"+]_-_?->~+_,
           .^``````^^``````````^`^^^```''''''''''''....''''.......''''..'..''..`..''`''.`''.'''`.`'.`.`''``'.
           .`::::::,`^`````''`^":"^",:;,"",;;;;;;;;,,,",;;;:::;IIII;II;:,:::,::,,::IIIIIII:,::,:IIII:::::;;I`
           ^{      l\~<<>~?[_<l>'-]]_.
           ,}I     l[[{})|}}[?[c;+)}-'
                 ..
                 l__l>?i:-??]I_?-++!i+[_[~~~+~]~I+_-i<_I--Ii_+<<l
                 `^`.'^`.''^`.'```''.`'^"''^:.``.''^.'^ '`.'^^`^`
                 I+-!!]iI]+--+iI_:-_]+:]--~,
                          '    ..
                  !+l ,[_!<{--1~ll-___!"_;+__"<-_~<<_"<~+>?_<!;+~l-I<I<<~<~<<^
                  . .   ..    .  .....  .   ` .''..`"."""`,"^`^,,`:'"^:^,,,""'
                  ![; "_<I!<_~!i+,i>i>:><~l~"!:><Ii
                  ^,` .`^'^^^,``, `","."l;^, ,'"l""
                  ;<, .ii!"<>!lil>+l^:i!l;"lI`^;'!;;,IlI!l;,`;;;;!;I"";::I,;";":;;,,;',^^>:
                  :l"  `:l^lI;:,::i,^;::;:"l!:"l^;II";>!;ll;'>!ll<Ii"l<!I>"i,i::i>:!i'!^;<:
                  ^;` `I"'`^`'";^^ ^^`:`'^."^``'^^.''^ "`'`';"",``,  ^..^ ^ '"':^` . ,^"' ''"`'^..'`''`'.
                  I~; ,_~I>-+~-]>>;>_+?<I<:~~+i]_+!<i_:i>~!:?~<~>~_!"<~>]!>!I->i!>:_"?--l!+~-_I?<!~+_+~<].
                      ,_~;>~i>i,lll[_<:+_!:_,!~<;]_">+~i-+i!"<~!-<                                      .
                   .                    ..           .... . .'`.'.
                  <}l :_>:l~_<~?i~"l<i]!,i,<i<i_~i,!i+`>!ll`_!i!i^~:_[_~;<>+?:<;-]???!++'ii!+~:~ll<><<~!<.
                  ''' ,_~;+?<++l!!!]_~i~>!;~;_-?!]~:i+<!~?i!:~>i<l".`^^''`^^"'"`^"^^"^^"'`^"",'::,,,:::,i
                      .",'`:`'`'^`.:``.:I,': ";,.;: :l!,;l:,"Il:I"
                  l+^ ^!I,:^:;:',,I"lI,^.""`l`^`^,",^^"":"^"';,:;:"l, ,""I"""^;;;l""l:I',^^:`"".^,""",^':"`
                  l~" ,-~-]!>--!<~-!_+<~li~~{l!!!>~__]+ii<~i,?~<+<i<<^!><-il<I<<><!l?>;^>i>-il?;-+++->_<i>>
                      "<<i>;:_i;^~+!,>"i>!;?!`i+<i__!!^i~l<,^i>,I~i~~~^iII<i,+<~~'_<<~+>-:^-~+<,]_i:<<+-,+`
                      ^_>_i_[~l+;>+<+_Il!;1[~,<_+!"+-:<~~_~>:~:<~_?;      .   .... ....... . ..  .' .'...'
                      ':^^';"".^^.^`'''^^'^`' '^"^ `,'^,"^^. ^.^,"^'
                      ^>i~;_-[+!-_~i[+I[_;<!l-_?i>-:>+I;_+<~-ll<!_<,~_->]]<<,<<>[>li;__~+>!_>_~"<+~?"
                 ,"^.'''",`''``''^^'''  . .. ''' .`. ....''^"''. .'.`^`'^'''.'`'^`.''^``^''``^^.`^^^.
                .-]l;+~~]?<+"--_i_~!!'
                      .:`` ;I" ^^^";^^..^^"^,"^'."^`^.",^ ```^"^`..`'^'^^'' ''``'^'`'` .'.`.^'.'^^....'.'. .
                      ^ii~'>?I^~_-?]i-::_+?>-~<:^_<+_:i__`i>-+~~<l^?+->]+<!'i<>_--_?_];;}>+"-+!,}?"l[~_++I"]'
                      I>+_+i~+il-!_i"+?>_il>i+.
                            .. ..  ...'      ..     .
                ']?<?_~~<?<_~    !. `_->i!^<+,l[+~-iI'<>+i~.<^!ii>>i~,l!il<"I<ll'!ll!<l<l> I>!^!!i!iI>"I!lii.
                 ^`^,^``'^``^    .  '<li<:!i<!i><I~<lii<<~II<!~><_~_l"-~il-+l+<il<+<<!<+i>:_-~:><-l>i<Ii<~<+'
                                    ^+><!!_>ii<+I^l!ii:lll::lIIl,!ll^ :II;!II!I,ii~;l:!ll!;+>i">ii:;!l!l;~II'
                                    `l~i^~!-~~+l
                                 ^  .` .' ''`  ""^"`"'..`'`.. ...''.   ..  . .. . .   .. ...    .     .
                                ^_. :]>_~I<>-+;][>[-i"_---_"~l!~i__i~<<-_I~i_+-_-^<--?l<I~?<-!!~_i;>~!+-<_'
                                                                        . .         .       .   .'..     .






































```

*Figure from page 15 (2346x3317 px)*


---



4203-E P-91



SECTION 5 AUTOMATIC MODE OPERATION


## 5. Sequence number Search and Mid-Start

Sequence search is used to start the operation from a required sequence of a main program. The



specified sequence is searched by the sequence name or the cursor, and then the operation is started from



the searched sequence by pressing the CYCLE START switch.



The operating procedure for the sequence number search is described below.



Sequence Number Search by Sequence Name or No. of Blocks



When the main program is selected correctly in automatic mode, perform the following operation.



~-------------.-



~Fi][!]~~~~


# GJww

--------------~---



(2) Press function key [F8] (EXTEND) twice.



3) Press function key [F1) (NUMBER SEARCH).



Fig. 5-3 Sequence Search by Sequence Name or No. of Blocks



(1) Press the AUTO key.



(2) Press function key [FB] (EXTEND) twice.



Function names such as [F1] NUMBER SEARCH will be displayed.



(3) Press function key [F1] (NUMBER SEARCH). "NS" is displayed on the 21st line of the display



screen.



(4) Enter the specified sequence name or the required number of blocks.



(5) Press the WRITE key.



The sequence name is searched for from the main program head currently selected, and the



sequence pointer moves to the found sequence name position. When the number of blocks has



been keyed in, the search is made in the specified number (either positive or negative) of blocks



from the currently located pointer position.


```text


                                                                                                '```'`' ".`'
                                                                  ....'...      ...   '.        <]__~+l,_I]!
                                                                  -}_>i_+[+ii`]>><_1??-~<I{---]i:~+?_]?+>++_.
           `^`'''''``^`^``^``'''''`````'''''''''''''''''''''''''''````..`.'''.'`..``'...'.''```''`.'.'`.'`'`
           '":,,,,"`^"""",""^^^'^^":,""`^^`^^````````::"""^,:"":,;,",,"^",:IIII;IIII;:,::::IIIII:,:::::;I;;;
           +~      -{>!i!I>!i!l~":i:I>!-!i>"l[l!i!!l-:'iI;>;l[-I<^>+iI;iI
           _]^     _))[\|}){]1?ti<[}{{1\)\\:i/)(/|]1)+lr[]t<~u(1/>}\(t|1- .
                 .
                '-+++<+!<i'_~~i~;"_`<~<>^-,,?~~^~->'_~>>+<<i'+i>i^>.~~<<<<<"<i<>>!!<"^~^i.!i+!.llli!!l, .-li'
                .><~<-+<!!<~!>i!!I!:<~~ii<ii><;<>Ii!+>!i>i!lIl!!:l<i>!<li<>^<+~~-i<><l!,<l!<]iIi>!]~~>lI!ll<'
                ']_i!>>~l~+~<><!i!l!<<_i!!~<l_iiii><+-~~><<l]-<+~_;>>i!>;!l^l!I:Il!"!ll;<<I!<!i,iIi<ii!!i!l;'
                'ii,!~<!l!!i"!<iii!!>,I<,~I>><!_:li:,;lll!l"<!<<<:^<~~>!
                 l::'^":,:;,,',,,",;^:^;;`::"',:,^""^".^`":"^.`^`^"".^',""^",""^^^,^^.
                 ;,i^I><I>iI_;<l!iii!!;I~^I~!,~>~<>li<^I!l<<~^l<+>!!'<,+>~><+_~;i_~>_^
                '>l;:;I,;":i"II;I'!l;:,!'l"'l;,^,,":`:I,,;."`:!^ ^:"!",,"
                '~+~--+i+<l_~><<<"!+__~_!_-!-~_<<>>_!<?_>];<I;?<:<>!_+~>~^
                      ;-<l<"iil`l<<::!lii!lI"I^i>!I!il,llIil~;`l,!;i:Il<l^l!I>!.I!liIl;;>I"!i!;lI:"^I;;;i::^
                      `;":;^,:;`,ll"I;:<!I;"";"!ll;l!:,lI;!l!!^;^>lI;;!il^;l;ll'Il;;I;:"!>"!>i!<i<<:_>!i+!l,
                                                                            l;!i<<:!!<i:
                                                                          .l:;I;!i;;I;;:
                     `,"^^^^^^^^^^,"^^^^^^^^^^^^`"^^^"^^^^^^^^^^^^""^"^^^^l!````''``''''^^^^^^"",'
                     I' `^`^"``^`^`''`^^^^^^^^^^^^^^^^""""^""`````````'''.!^'''.'`..```'..''^"' ;"
                     l'.!'IlIIIlIII:I;................'''''''.....''''":I+_li<I->;?-l~<;i<l:""; "^
                     l'.; :l;:,:::::::^````````````````^^"^```'^"".   "li1_i+~l-~;[[i_-!_[+!` ; ^'
                     l'.: !^":I""""""",""","""""""""""",,,,,,,!,,,,   :>^i"```^'`^'`^^'"`^,~^ I :^
                     I.'I I  ';                               ,  ':   ,-_{?}<-<-_--~]i]>_<!~` ; :`
                     l.'I :  `;                               ;  `:   "~+-_[<[-?[[)]1[}-]<>-^ I :`
                     : 'I ^  `I                               !  ^;   ^>li<<i!_l+++-;!<!~]]?^ I :`
                     , 'I ,  `;                               !  ^:   :__)+]?<]]]{~?]1[{|()-` I l^
                     l.'; i  `,                               !  ^"   :?~_><?!-_>-~--)}~{++_..I l`
                     l.'; i  ^I                               l  ^"   :?_?_?]-)-?-?]i([+1<--..I I`
                     I 'I l  ^;                               !  ^,   ;_~+~?ii-!!>i<+_i:]++?'.; I`
                     l 'I l  ^:                              .;  ":   ;+,;!^"^IIl!I~_I!^"<!_'.; I`
                     l ^i l  ^:                              .:  ,;   ;?]_-+;^+<_-+)~++^;{-_''I l`
                     I ^! l  `:                               ;  ;I   ;{r1)cI^_<<_[->~{`!<++'.: !'
                     ; ^l I '"I^``^'''``''''`''''``````'''```^I'.;I   l{{_+1I^<i>(~+<~_^:+><'., l'
                     l `I !ii!!!!!il!l!!!ii>i>i!!!i!!l;l!!!!!!l!><^   l{1_-(l`+>]>>+~ii^I]_- `; l'
                     I `: l.,[+!>-!i+-lI]<"i?l:+?I;}<l<-l!?-!~+>.:,   !~!;I!"^:!>"","",`I>;_.'; l'
                     " `; ;":il;!_II!!;;!l:I!I;l!;;i!I!!;>_!I!i;`;^ . Il,,:,;;l<,:,,::,i<::i.`; l'
                     :  "``^`''`:l``''``''``'``'```''''';!`'``'`^`''`^``^^^^^"<"``^^^"il",",",^ l'
                     ;^^`^^`^^^^i:^^^^^^^^^^^^^^^^^^^^`I<",,"^"``^^^``^^`^^^`>:`````"i;`''.''..`I.
                      ..........!.................... :l..'.................l:.''.'"!<!li!iIi<><>.
                               `I                    ,:                    ^:      I^li:Ii<l!iil+:.
                               :^                   ::                    `!;_I++!ii-!I~~!>!>:l<i~.
                               !.                  :"                     .'^"^"::,;;::;II;:;,:Ill.
                              'l                  :Il^::::":";::^:,^ll^:;::;::^^^^^
                              :" ..'             "I;?l!++~i-+~<~l++i~+i~_~~_++i<_++`
                              l,_]>~_-><___?<<]<-i><?>-[}_>![_?-++<
                              .``''.'''''''''`^^`'````''``'``^"^``^

                                  "!,',:;^^l;:",,":`l:,,":^:^^I""^"^^"`::^^^'``";` `,,I^^:^.
                                  ,I-;;!!,,++_<~ii+:>+++i>:+<,_<~+_ii~l!-+!~Ill;?i'!>!-~<_~^

                 `I:  !I;;;^!;^;l,lI::::'
                 "II  ;:!i>,i>;;<;:l,l<~"
                 ."`  ,^''''` '``'.'`. ^:;'";"::;::"'^```.
                 :?> .!!~~_"<!i>~<l;_-:ii{I~+>li++?>"i+i~I
                      l`"",;"^'":^""'"^,".:`^;"^:;`I!l;;I^!l:l!;;,`";",^';"^:^`^".
                     .I;!!i<i;^>_l<<:iiil,-lll:!l+I<?-_<!,_i!_+>il,++I+i,_~+-?_<>`
                 ';"  ,^'...'.'''. .'. ^'' `,'^""`^^ ``.'"''`   ^'"    '. .   .   `...'''.'.  '''. .' ..
                 :?< .<!~<+;~~>__~Ii-?;?;!I~?~-]]]+_;-]~?_-~_~.`_?]">i!]+_?__?>I_:~~>!+~]l<~<;_l_+;+?+__-'
                      ><i~_>.                                              .                         .  .
                      ..  .
                 :-! .->+_;>?~:~<~i]_>>!~>!>~!>l;>ii<,i,+~i"<ii>i>>;lli>i>^iii!!<<I
                 '`'  `''^ '``."^^`^^^.'^,:,,^:"`::":`,',,:'::l;,;,^,:,:;;';^::;;I:.
                 ,+I .<!i!!:~i:!~~<<~:ilI
                 "l: ."^:I:':I`":^"";':;!'
                      lli':>lIl!,II Iill""i.>i<ii<<i"<i'~li!^<i,"ii>,`ililIi;`!lIi:^lI;!I~;.ll!ll!!^'!;l^il"
                      l!~Ii~<_i!!~<lili<!;+,<<>+!!_!:>>^ii<l;i<l,i~~lIii_-~~!^,+-+Il>~i<l~<:_~<!>_+l,+ii:>~I
                     .~~~_<i!<;!~~!+~'li!i+i;i"!<:l>+<!;_>_>~l!+:;+<<>^>I<<i!; l~:>>`iil^iil<~i'i,iiii>I:>_;
                     `~i~>`!<~~~;i,'<~"l<i!!!`~^>~>?:;;!<<"+~_<~?+>:i<++_>'_+-<_"<~<?_~!:~`i+~_->_>^~!~_>?+;
                     '-i~il++Ii<i<~+_:<~<-+~!i>>>->;~i<~i<;''.. ... .'.''. `. .'.`''.''..' '`"`''``.' ''''`'
                      `^^`'^"'",^""^;^^,,:,:^;""";^";","""`









```

*Figure from page 16 (2346x3317 px)*


---



4203-E P-92



SECTION 5 AUTOMATIC MODE OPERATION



The following cases result in errors:



(a) When the specified sequence name is not found in the program.



(b) While the schedule program is executed (from schedule program start-up to the end).



(c} Whether the search is made or not during the execution of a main program can be selected by



setting proper data at bit 3 of NC optional parameter (bit) No. 4.



(d) When the main program is not selected correctly.



[Supplement] In cases (b) and (c), the sequence number search can be executed after resetting the


#### NC.

Sequence Number Search by Cursor



In the automatic mode, the sequence number pointer may be moved as desired by the cursor keys



when the main program has been selected correctly and the screen displays the program.



@ . . . . . . .



one sequence advance



@ . . . . . . .



one sequence return



In the following cases, the cursor keys are inoperative:

- While the schedule program is being executed

- When the display screen is not the program display

- When the sequence pointer leaves the selected main program by the cursor key operation



Restart after Sequence Number Search



Program execution starts from the sequence identified by the sequence pointer when the CYCLE



START switch is pressed.



Since programmed commands which were not read during the sequence number search are not



valid, a model status must be set as needed by entering the necessary commands from the



keyboard so that the actual status and the programmed status match.



[Supplement] 1. During the sequence number search, the read pointer is moved, while the modal



instruction value and coordinate instruction value are disregarded. Subprogram



CALL and GOTO are not done.


## 2. The sequence number search is used for start-up after a pause during the

machining work, while the return search is used for the return to the block while the



machining is underway.


## 3. The number of the sequence repetition cannot be specified during sequence

number search.


## 4. Additionally, the optional block skip does not affect the sequence number search.


```text


                                                                                                '^`^'"'.".^'
                                                                  .  .....      '..   '       ..+?-?>?:;~!{~
                                                                 `{[~<<~~?i+:;?i~+-{]-+_>!1~+?{ll-~-_?-<<<-<
           '``'''''''''```````''''''''''''''''''..................'`''.'''''''`` .''''.''.`''''.'`.`'``''`''
           :;;,,,^^^^``",,,,::"^^^"^^^^^,::,:,"":;IIIIIIII;IIIII::,;IIIIIIIIIII;:,:,,IIIIIII;,:;::::;;;;I;;,
                .~il:i<!!i!I":!lIl^;IIl!,""l:II:
                 ,;l`:lI;l:!I,!l;I`,III:"^,I,lII
                    ,; 'l;""'::^."""`I,""^""^^"`""^,",:`"'",";,^":""'I"``""^^""`
                   .i+^^<l!>"Iii,?>>i<<>l!~__~~!>!:<il_"i:l<:i<i!~;>,~~l><>[~_i!
                    ^' '^^`` ^' ..'..' ' .     . .      ... ^     ..   .        . '.''  .. `.  ..'
                   .--^,?<_]:<_iI_>___>-I-~~[~_<:+l_+_+<___;[<+~;_+-_-_?<!?<]?_]!I[?+>i]I-:__<!]~?;
                       ..'  '   '       .   .                .              ..
                   ._-^,]~<+<->,~_,~?+i>i,+,<_+]:!I:<-:~!i>+!~~I!<~~!_~<:I<;!;i-+,+><]<-~:l-_:__:+-]~-_~l+>
                     . ,<~_!!,!l!>i:;+>i^~liiIil>i+<,l!+i;!+;!!li!>~>"i><:i<;'>`. ^.','`...`' '`.`''''`'.^"
                       `I;;">,I"l!;'^lI;`!^::^,::`l:.:ll;"l;,!I;l:!!i'i!i:;i:.!.
                   .:i'^l;":.::^'"",^."^^`""`^`.^".^:,`"^"''^`^`^`
                   .i+'"~l!<"!<i:!~>;><!-+<<;li">>:~_+<~~<;i<i~<>+:
                .;"'.'^'...`.   .'  .... '  '....  '      .       .`.......`. ..... .... '.' ''     .'.  '.
                "?+<]]?~<]~[I . :_;~?+?~I?>I?>~l_!"<_l<-++-~<-<I~+>?_!:?__!_ll--:>_;+_-<>[-~![?~^>__?]!_i~-~
                                ;]+:                                                                   .'
                 '        '.     '^.       ..
                :{[1[]++]>_[<+-?],?-]]_-l[~l-+~_-"
                .^"::,IIl!:":,;::,;::lI;lIl!:,,,:'.'.'.'.'`'.. .'''..'.  '. ...... . '... .'. '.    .  .
                      !!l~<;_<+~i~+>"i!i-I,-<,>_<i~<i+!li>~-_:<<i<-~:i~]l<~;><>>~ii-:+_+<<-i~<i<~"li>~~;_++<
                      I-><l!?~:!i-i:~>~-<?iI~->!_+_;:-_+~?~~I>~i<i]~"+i<i_~:<>>++I:?__<_~li_<l<!~+>~i^   .'
                      ^l:^...`..'^''`'^:'`.''^`."^`..^^^^""`'^^'^^",',`^'`"',"^,,''":I":;^`""^;^;l",^.
                      l-+"... .. `i<<;-~_<_>><,_+<~<<_^
                      ,>!`       .'''.^`^'`'``.`^'`'.'
                      l+~^ .   . `<~<:-~_i<i~+^<_><l
                      :;;;"^,,""""`''^^^:.^,^'`'^^`.^```.`^'^`````^^''
                      i;,>i">i!>+!+i;~+~_"I~>"<i<~!^<<~i;<~;i~~<~~?<<~.
                        il;I^:I,.:;I::^:`",^":,,^"^",:,"`"",^";",
                      '.lI;!;;ll^iII!ll>:llI+>iI:II:iil+:ii<li+i!
                      ..<+Il:,>l^l>Ill;'l;;Il^,,^;;:iI^;;:;:l;.!!l!!;'
                      . ;;";"^;;`;;l;;!`I::lI`":^I,^Il,i:I+:!,`l!i!li
                      ''_?i<II_i:l>!I!lIi::!!!<!"i<i:!"!iI`<i>l>!l^Il<,l!;!i>i:;i"<iI"!lllI,ii:,illl<l!"
                        ^"`:^'^".^:,,:"`:`^"""," ,;;,I^";,^!II:Il;^:ll`l;"ill;^"!,:;;^I;:;,^liI"<!IIi;l^
                !{-_[]~l}}-,-?+~>+i<<;]>!+__;>]<?i~,
                `,;:;I!!!l!;l!lill;Il,;ll!>>l!iiilI^
                      >!!_i~~,:<><i~<>;,_~<i,>i~:<-<I?+-~?<>?l~}_+{-_<>+I?-~I]_+>_>~_I+<!+-II?~_il]<;<>++i~!
                      <_~[[_:!+-_-l<!!<<~+~+l '. ....'.`''..'..''...''.^'.''.`'^``'```^'.'^.'`'^'''`'''.'``.
                      "^'``' ^"^"^.^^^"",,:,`
                      >-!l>"<!ii!<i>i>!"l!lll~i<_"<li~!"-~i!^i<:i<~i"_Iii<I]<,!_>i!<!!I"<;i+>i`~i<!~I:<l:l!!
                      ;<<~:,i^~~i-i^><+!<^l>!_,l+^I>~">l"!<<!~~;I~;;i~+i>-;!-i:i~<!<>>>l;li<<>l_>__;>!~!,_~l
                      >~<-;;>:l!!<+,<<?<!:!<>_"!_I;~!,<<"!<ii<>:;_;I<l_!>~+:i>,;+>>lllii`,lIII!<;!<.;;l"'li:
                      i!<~i><<:iI">+!:>>^->!<~,+_-<!,-l!!~<:>I<+>~>i!~!"~~_<i^ii_i>.
                `,..'`... .'    .   '' .'  `       ..     .'. ..   '  '.    ..   . .....    .  ....'  .. ...
                i[<+--_<<-i?'   ::  i<><>]l__I>+_+__!~!:~~><+i^~~-l_I^_>I:+-_;<><<_i"+"il!i~i'_~?_,_~!;i<<?l
                                    ,i_~I+~!i^;~<i!,~!i:<i>>?!>[iI>~?Il]~~:I~~<<"++;l?~>+-_i_~+ :[>_<ii+<~<;
                                    !<]<l,~<<:+_+-~;<<i:<~!+_!_!^'^,"^""""'`,","':"`^,:";!:^,," .:::;^"!,:^`
                                    "":I,.l:;';:"":';;:':l`II^!'
                                ;"  ^I,' :^^`,^'" '"^^",^ `^^"':."^ ^,",.:,'';,,^'"..:I"''^.^"`^^ ^"^"^'':"`
                                l:  ,>~!,__+~+>!_:,+_~~_+'!_++i~`li.<_+<'l~""[?~l>]^:-+_^;i:?_<~~.!+i!__^~+l
                                    ;l~><i!i~I<il>.>i>_"i-lI-_!iI+_?i_;!>l~_~>~!!]<I<~l<>!<>?<l+>>~:~<+?i>~l
                                    l<_~~~+~-l_,l<--i~~_; . ...  ..... . .... ..  . ..'. .'..'......'.....'.
                                    ''^^`''':.`'`'^`.^""'
                                i;  li!,.l;l!il ">'<i"'i!iI<!l>^"ii!><li`^il!Ii,">"^ilIl_ii:">;i;I'!!!Ill;l"
                                "^  :I<iI<>;<<<,i!.;;"'!Il;l:;l``l>II;;I'^lI;:l^^i"^<lIIl!!""!II;<'!!>i!!I!"
                                    "ll:i~I^>!<!I,
                                ^'  '''^` ..`' `'..'`^''````.`'.`'..`''..''.'"...''....  ...... .'........'
                                !;  i_]-_~i~[[:<+~:_??<>{i~-<?>!]_>;-_]>;+_l?}_+li_~![]]<_>~~:~>>?-?"~_+~~~'
                                                                                       .




















```

*Figure from page 17 (2346x3317 px)*


---



4203-E P-93



SECTION 5 AUTOMATIC MODE OPERATION


## 6. Return Search and Sequence Restart

When the machining cycle is interrupted during automatic operation because of tool breakage or other



troubles, this function ls used to restart the operation after necessary measures such as tool replacement



have been taken.



After locating the sequence pointer to the specified sequence by return-search-operation, in which the



commands are processed in the CPU, press the SEQ. RESTART switch. This positions the axes at the



point commanded lastatthe manual cuttingfeedrate. Press the CYCLE START switch, then the operation



will be resumed from the same sequence.



6-1 . Return Search



When the main program is selected correctly in the automatic mode, carry out the steps following:



(1 Press AUTO.



.---'------------~--



(2) Press function key [FB] (EXTEND) twice.



(3) Press function key [F2] (RESTART).



Fig. 5-4 Return Search and Sequence Restart



(1) Press the AUTO key.



(2) Press function key [F8] (EXTEND) twice.



Function name "RESTART" is displayed for function key [F2].



(3) Press function key [F2] (RESTART).



"RS" is displayed on the 21st line on the display screen.


```text


                                                                                                '`'`.`` ^.''
                                                                   ...'.        ..    .         <[-?>-I"<;{_
                                                                 .]}~~_-+[+>l"]<><~[[-~~<;{-~_}!I?~_?_-_<+?<
           ````````^^```'''''`````''''''''''.'''''''''''...''.....''''..`''''.'^..''`'.'`.``''`.'^.``'^''`'`
           .";;;;;;"^"^`^^`':""","^^^';,","^,^^^^""",::,"":,,:::,,^^,:::;;IIIII;II:,,:::;I;;;:::::lIII;;:,,,
           ]<      ]1>~+;l!i.[_il!I!i_.:!l;~`?>!II,:II;;;l ~_;::!;;l!
           {]`     ?}()}1[_]"{((1/?{}):}j[{\")(/(x))|1[(1f^[|f)t\tr{1 .
                  .
                `?_<_l:-?,I>+>>!<>_:<~>+"~,!~~lI~__~;i~!><;;+~~>!~~l'!>>!~>i!"i!IiIi~^iI!!i,<i>~~i><^;;^i!!l
                `ili_<i!"+<!<>!!+<_:~!i~><ii;<i~+~>->I><><++~~l+?-!l!<~<i~<>;l<<<<i<~:i;!_l!i>~~<<[?!<!l<!~<.
                ^<i<~>~<,i><I<>!Il:`I"l!iI;l^l!ilI"I>,l~i:l>Il^>i<""<!!!!i<i,l!>~>i!i;l!!i"_!I!!:;~~~~i>I>l!.
                '!ili^i>>:^~<!!,
                 ;!;^`"^";:^.;:"`;,"","",'"",::^^"'I"`^"^^,l^"'^""'`"`^'^`.^"^`"'^````^.````^"`' `''^^'^.^`'
                `~+-!:~<~]<->i~~:-~_~+!<_,+_<_[>l+"~+!l?_~<?_-I_?}__-+-li{;!_~<~;_][~i<:~_->?_~<`!;:-~<~,<_<
                `!!li!+~I-,!>i:<i>!<~~_ll!I<!"!<ii'~i<_lI+<.~]<< ~?~~<<++>`<>~<!, ;i<!I<i<+<li^>_;!+!<"<l!><
                "+i>>;><><i_l~_<>~+i>_~+>:!~~;>i:l+?l<~-+~_<?i._~i<<i~~li!>~i-i+<<~~?I_~-i<:<+~li+~l<~><_<>>
                ,__><i;>i!!~i<i_i<~I_<;>~!i<!<<>l<<>i>";I::;I: `^::;""I""^",:;`:",I:^'lI;;:^,Ii,^;l^!!I:>II:
                '!!"!i^I!l!;ii:;l!I"!i"l<ll;:<!<iili~
           . .     .
          .)ll:   `){{{+_+:{{]}-_[l .
           '. .      `'` .  ''`.'
                ,}?_-l>_+:>+?l:~i~_~]i:>:+__>?_+I<>l<>+>;~;?+;i>~><i-?;:<>~],"<_ll">>;+<;I_>i>;~~>i>!>;
                 ..``.''`.'^^.`^',,`^'.`'^^^`^"^'^^'^^^:'^'^"`":""^":,^'",,:^.:;',.::`",^";;;;`;::;:,>;
                                                                           `~!~+?_l>i~~"
                      ...................................................."l":",:,"^"^"^. ....
                     ,^^``````````````^`^^``````````````````^^'`^^^^^^^^^^i"```^``^^`^''^^^^^^^"I.
                     I  "^^":"",,"^^^^^^^^^^"^^"^,"""""^^^^^^^^^^^^^""`^'`>`'``.^".'`'^"`.''`^' !'
                     I ', lllllIIII;l:                             ...,:<{<<?<!|+l\?I_+l-]!,'^l l'
                     I '" Ill;;;;;;;;::,,,,,,,,,,,,,,;:,,::,,,,;;;'   ;l!}ll<>i~!I~>I<>;><ll '; I'
                     I ^: l.',;``''''````````````````````^"^^,l`':,   lI"i"^'`"`^^'^^^""'`^+.': ".
                     : ^, :  '`                              .;  :,   l})1{(}[+{][{])]|-{_<? `; ;.
                     " ^, I  '`                              ."  :"   :~i>>>>~<<+~[---_<_<>~.': ;.
                     l ^, ;  ,,                              ."  :"   "~>__?+>_<?<]-i+-<-|]i..` ;.
                     ! `" ;  :,                              ';  I,   l?_)<]]>+_-]>}{(?)[)-_.'^ ;.
                     ! `" ;  :,                              `I  I,   l-_]+~~__~__+[~)_+[>>_.`, :
                     ! ,; ;  :,                              `;  ^'   l+_[-?-][~[_?[]1~-1+[[ `, "
                     ! :I !  ,,                              `l  "'   !<!!~-!l!:l!l[!II,~i~] `, ;
                     i ,; l  ""                              `;  :`   l_`>I"""iii<~+i!!',-+_ `, I
                     i "".I  ,^                              `,  ;^   !1|?](:,->-{<-<_-'>?{+ ^: I
                     ! "^.l  ;"                              `:  i"   </f}\x,,~~{_>_i_?'!~[- ": I
                     ! ^^.l":lI,"",,"","",,"",,"","",","","",:l"^i^   <[{i_),,_?><>_<++`:+?_ ", >
                     ! ,, l!><<i>>!!ii!!!i!<>!!>!l><!l!i!!ii!!l!!i.   <[{~]1`![!;;i>>!>'>~_+ ^` !
                     ! :, , ;]~i~_Il]-l!?i;<_;:[~,i}ii<<;!{+;<<, I'   _I:^:,i!"^",^,^"`^>I:~ ^^ l
                     ! ":`;::;::;::"~;::,,,:::,:;:;;;;;;;+!;;II,",'.''I::::<!",:::::::l_!:;l.;" l
                     i .`^``..'`'`.l"'''''''`'. '^^^'''`i:''`''``'''``'''^i:...''''``I<:`^`'^". !
                     :^^^^^^^^^^^^Ii^^^^^^^^^^^"^``",,">;`^^^^^^^^^^^'``,i:`""",^^^`II``"^`''.'`,
                                 .!                  .l^               `l.         II+><>~<l__+~>.
                                 I^                 .l`               ^I.  .   ..  I^I;,:II:;;II!"
                                ";                 '!'               "i^_-i]?><-}<~__~~~-i?+~l~_i>]_]+?i+_--'
                               .!                 'I                        ...   .'``''^^^^``````^`'`"^"^^`.
                               I'                'II<:<i>I!!!>i!;>!l~~:<!i<<>>:l!l:
                              ";,"^"^^`"^""^`^^',l;!]i<__~>i;IlI:liii!l!lIl!!i!>i!I
                              I,_~!+?]i-~++_<_->?_<!_+<!<~>l
                                          '       `     .          .         '
                                         `___^_I<']-]>il!}_->-il?+i<[_-i-~~_;[-_++-;
                                           .^      ..'   ..'.. .'.. ''^''.''. '''`'
                 .'.  ". ...'  ' .^'..
                 l<! `+!+?-I++:_<!<<!-_-'
                                       '      .
                 ![! ^_<--~;->i?+~I>__;[-}"]++~-_?_~I-+>+"
                 ''. .^.``^.`'''``.':;"^^:`:"^.''`'`'`''"`              ..
                     ^+i+<+-~:i~~~[`~]++~<]?>":-:[___?_<<i?ll-<<+<<;<_-,[>[I
                                       .       .. .`.'^.. .. '..... .'^.' `'
                 i[i ^?i~~>i_~+_>_I~-~;{>]:+{]~++-[_~`
                 '`' .'.'^' '.. .. .`^.`.` '''...'....
                     .i_]l"_,--_<_<~~:~;!+<:+l~I>!<"~l>_<,-~~i+i:+!>+<;
                       .` .^'^":`""^^'^''`"'^'"'^^"'"``^"',";^,;':^":"^















```

*Figure from page 18 (2346x3317 px)*


---



4203-E P-94



SECTION 5 AUTOMATIC MODE OPERATION



(4) Enter the sequence name and repetition count, or the block count.



Input format is as follows:



L....J



sequence-name, repetition-count or block-count-value



When the sequence name is specified, the repetition count must be less than 9999. If entry of the



repetition counter is omitted, it is regarded as "1".



When the block count is specified, the count value must be less than 99999999.



For entering a block count, the relative number may be given as indicated below.



Example:



592 . . . . . . . . . . . . . . . . . 592nd block

* .................. Block count value which was counted at NC reset



*-2 ................ The block two blocks ahead of the block count value above



(5) Press the WRITE key.



The return operation is executed up to the specified sequence.



Restarting operation refers to the operation in which all the commands are processed within the control,



without giving output signals for axis motions, and S, T, M and B functions. CALL command, RTS



command and coordinate system shifting are also processed.



The block count is the count of the sequence executed from the program start after reset. Control



statements such as GOTO, CALL, etc. are not counted. The count value and sequence name are not



cleared by NC reset or by turning the power source on or off, and can therefore, be used for return after



reset. They are cleared when the operation begins.



[Supplement] 1. If return search operation is intended while a schedule or a main program is being



executed, an error occurs.


## 2. The return operation up to M02 of the program is possible by the [F2]

(RESTART)



L....J



E [WRITE] key operation. Reset by M02 (or M03} is not carried out.


```text


                                                                                                 ^^^^'" ^``^'
                                                                  .'..''... . . .`... .'.   ....^[[_-!_.+I+]l
                                                                  !1_~i+~+?I-.__<~<-{-_~-l~1_-]?"<_~___-~-<-;
           .'''''``````^^^^^```'```````^``^''''````''''''''''''''.''``'''''''''`'.'.''..''''''''.`'.`'`'''''.
           ',"",","`^,:"""^,,^^"^``^",,":,"^^^^",,:^^^`^"^"^^,,,;"""^,;::::;:::::I;:,:,:;IIII;,,:::IIIIII:,:`
                  "+!  -!i~,I~!^!!!l!IIi^;ii!;^!l!,!!l>>;l^,;;Il ;,:i:"l::l^,;:,I
                  "I;  ;"^I`^:;':;lI;^:l`"l;:;"iII"i~li!Il^;l!l!^!;:i!:!l!i,I!iI!'
                      .<i>!li>li+Il:;+,>!i!>!'
                       ^:;:^^:^^I^"^^;`^^`""".
                               ,^-]!^' ~<~i~<>-il--~-^l-~+--~i;l>!i<:~:~+i_iI<i<_ll<!<i
                       ''.  .' '..'.`' ^^,""^`"`.^^'"^',:,"^"`.'^"^`'" ^^^"^'^^:".^^`^"
                       _+i~i:-<;<~+<~>>~l:_<l>"+:_><![~~,,+i^!+<_~_>l,~>l>;li!~I<~:~~+;->+;-[[{i +l~~->,+i_<;
                      .i+~~__!i:<>>+-<:~;l+~?_~i:~<ii<~_>++_I_<I<I^`''^^`'''`^^'^^'"""'`^"'^"""` ''"^",'^'^"`
                       "l;"":,'',""`:, "'""";:,`.`^^`;>I,;I:`!, '
                      .-_i+!"<~;>~!~;:<!li;~"<<~>-~~l"~i";l:il^><!<,iii+I~i;<<>l?i~:~]]-?]?-_'
                       ,^`,'''^'```"`'^"^`.^.::,"`,"^.^"'^"^^^.",,: ^,":.,".::"`,":'"::;;;:::
                      `_!l:~<]~<<i!l~_i-Il~i<+'~~i"~-_<<<:!>~~+>^>i_,i~"+<!<:;~,l!!!<_<il<<li!
                       ''.'`.^'.`"''''''.'`^``''``.^^^`^^'^"`^"^.^^;``"'l"^^`^,'`^^"::,"`::","
                      '_i?~<?_>
                            . ."^".                 .```'..'..'
                              ']]]^......'........'.:-]_i>;-_<]`
                               `                    ^;`'"''`.^^.'^''.`"``'.'''.'..'''`.'`^^....'.
                               i'  .....''........' ;?ii-"!ii~i,~_i_^+_<~I:~_~:<i>i-+>i?l-~:>+~?;
                               "'::                 `I"^`,^^"',"'^:^":'."""^"'^":"''"'^^ '`'^''^^'''"```^
                               l`;:   .  .....'.....^i>iI<><>:_<ll~>~-<:_>_++:<l<<i;_<~<,<~>~Il-_<!l?<>~~
                  ^I` 'I"^"^^:^.,:;:;;'^`'
                  i]l ^!I>+i;~>"~~~i!+`<<+
                      .l,:',;"""."^"":;"^^,^:,,"";,,`,^,`l,^`""",l",`""^`^"^^`
                       ;;<"liiI,"<<>l>!i;,!,>i>!!<>;:~"i,~iI,+~<!+i<,<><!<i!~I
                 <iIiii!:,^:;I,l!^".;!I:""""::."",,;l""`, ;I,;'`l^I"^'",,,",`;:`;:`",,,,,,,:^,;l:^";"'^"":^^
                 l+?~_+<l]i-->!__>l;i++<i>iI++,~+?!__<>liI<!~~I!{;~?I<_i<>+~++_;-+i~!<>>+_]+;>~~<l!_~:<<+?~+'
                 i<+!><"i+il+,,i>_ii`<~<<~!^<I <<+,^I!>ii<'.<;i.~' I -i^_l!']`+_i~_i!<. l>_!< I>>~ii_i+ l+!_:
                 I!!!!~?<>;~~~l~><<?~-}Il~~]~~;<?_[<_l++!I?_!l<>><~>~<~.                     . .       .
                 ::`'`"^`^'^`.^"``',``'''"^`'^'"`''':^^``'`^`^^'^^`^",^. ..              .            .
                 !~+"I_i~~'<i!<>"~`__!"+<>~:;~"-+"I?>~i<i<>.+>_>>?_~"+l_;:?~">~!_~_~:^_~-,;{]+.;+<~I '>>>-<<,
                 i<<<>!+!~!"ii>,:_,>_i<>>'!i-!! l?i >+l,i<llii>~+~" li_";!li!,>_~<,!!!Ii~i<>ii!I,<~!i`!<!,!>^
                 !_~<>>ii>l_-!!>i_l;i;i:i;l>i>!>>!!:><i"l>;!i~;>>ll'I?lIi<>!>ll-i~I_<<l:_-><>><iIii<_:~!ii<<`
                 !~++i!i__;!i;l<++ll>I+!<~l!~+Il~I<><<~"ii!li~^!:"i^!<.ii!;;~>^ll!i!!l>.!~`i<>l,>"^~!i!,i+<<.
                 I<>_; ;>!-,I~i^>~+>+~^~<~<^<<i,++~i+i>,>~-]i>.
                 ''   '    ''    .   '.    .   ...      . '.  ..  . .. ..     .
                .??~]]~-~++~_    <` '+:++!<;!-~~>~^++-i?_<l;<!_[_>+-<I?<]_I<i~~?__i-:_;<l~__!l+>?]__Ii<!]_i?"
                                    .~<_<!~__^>+^+<><:~<ii<I.   ....  . ...... ..... '.'..''.''."^`'.''.``.:'
                                     ^^`^^``^ `" `''. "`^,`'
                                .+'  I;!. ;l:;, ;iIl!i,I' ;l :! I-i<^.i"`!l^ l;l!;;;.'! ^;:Il>i; lI "i;''~l<'
                                 :.  i_}>l~___<`,i?~-]--il--,l!`l+<~I:~,'~_l;-!_?~]<;"+^>?+-~~<i`<_";~~:;~l-`
                                    .>>iii:i!!l;^.l:<<>i;>!l<~>l->!l+>i;.l~+~~;<!i]<+;>!l-<~l;l,~!:+~I~_!l>l




































```

*Figure from page 19 (2346x3317 px)*


---



6-2. Sequence Restart



4203-E P-95


#### SECTION 5 AUTOMATIC MODE OPERATION

This function can be used only after the return search. (For the return search operation, refer to 6-1.



"Return Search'' in this section.}



When the SEQ. RESTART switch on the machine operation panel is pressed, the program status up to the



specified block is returned automatically.



(1) Automatic Restoration of Miscellaneous Functions



(a) Restoring the last S code



If there is an S command, the S code of that command is executed unconditionaHy.



(b) AT code is not restored automatically.



Since a T code (next tool command) is not restored automatically, it is necessary to set the correct



tool number if the next tool number presently active is incorrect. If the next tool number is "O", input



the tool number in the MDI operation before executing search.



(c) Only M codes related to spindle operation can be restored.



Since M codes are processed in groups, the last modal state of the individual M code groups is



restored.

- M03, M04, M05, and M 19 are regarded as M codes in the same group, and the last state of them



is restored.

- M codes related to ATC operation (M06, M63, M64, and M65) and APC operation (M60, etc.) are



not restored automatically. The operator must restore the correct status before restarting the



operation.



One-shot M codes (MOO, M01, etc.) are not restored.



(d) The axes return to the point programmed in the return sequence at a manual cutting feedrate.



(e) After axes have reached the return point in the sequence return operatfon, the operation stops



at that polnt independent of SINGLE BLOCK key setting. To resume the operation, the



CYCLE START switch must be pressed.


#### Search for

restart



---_,.,_1-N_____


#### N100

1) Key in N100 after pressfng function key [F2] (RESTART).



Then, press the WRITE key. This prepares for the return of



the latest state up to the N100.



2) Press the SEQ. RESTART switch.



The miscellaneous commands (S, T, M) are output to the



PLC, then after the confirmation of the respective answer



signals, the axes return to the point commanded last at the



cutting feedrate.



3) After axes have reached the return point in the sequence



return operation, the operation stops at that point



independent of SINGLE BLOCK key setting. To resume



the operation, the CYCLE START switch must be pressed.


```text


                                                                                                ^"""`^'.:',^
                                                                  '..'`''' .  . `'...'`.......'.<??{~_I:~!{~
                                                                 '[?<<>+~]!+:;-i>~~{-_<_i;}-~~{i:<~?-_-+<<+~
           ^^^^^^^^^^``````````^^^^^^^^``''````'''''''''''''''''..''''.''.'''''`..'''...'.'''''''' ..''.''''
           ^,",::::"^`````^``^,""""""",::,":;;:,,,"""""""",;;;;:,,:;;;;;;;;;;;;;;;;;:::::::II;II:::::,;IIII;
           _;ll    <+iiiI<l!!l,[>!>i!>:
           i:I;.   :iii+li:li!'l>!ii>I"
                .iI;.::",!," `;^ :" ",,I`:I!',>i:`>;,"ll,;'";::,I' ,<,,^!:'";;",'":::,;.,,,":;"" ',l;`^^^:``
                .i~_!l-l--<i,~_!:~-;~<<<I<>-:l>~l`>iI:<>il`I<>ili, !i!!^<~"I~~>!"i+~<i>^~-~i+<i!^"<+?,liI>,:
                 :<<_>l'i>!!!+'^i"<+I:~!-<>:;
                ';:"^'":`^l:,`'!I;:;;Il,'^",,^`^^;^'^^^^"^^'````^"'`'`^`^^`'````''^."'.''''''`.''`''...`.`'.
                '+~<~!<~+l?~>i"+_>~!~+>:l+~+<ll~l+~;l~_!><-!<-~i?+>!!+-~[!+>~<___<_:<+i~i~{<-+l-_[~+l-i<><++
                `_+_>+_+<~>i<ll>^--~<>_>!_<~><?]>__+.
                 ''..          ..        .. . .  ...
                 '>>^ l->+<<_[<;]-+-<i-<<i;]![]>!~__>+<i<I<lii+<i+i
                 .`'  .''.. ``'  '.`' `''' ' '^^^"^,^"^",`.`^^"^^,"
                    <_'"-i>+I!li;<<,i~!;~,i!~l
                    ;l'.":,,^^"!``;`:;"'"`,,::
                       l<+~>>IlII+`+;Ii>>i<<i!^+>:+ili<],!!~<+;I!>iii~<!;lI<i>li+>I:i!l>i_>l!!i>"
                       . `^^'. `.^ ..``.'.^^^^ .^.'.'^^"."`^";`",",":;:"^"":::,:;;^":,;;:;,::;;l"
                    <~`">:::li<"i:liI,i!ill!,:!!lllii;l>;
                    II'`". ^::l":^^;"`::::,;^,I:;,:I::lIl
                       :-!l!,;^:;!!i^il!!I!;l:I;llIi;i,;,;!l;>~>I!>;!i~!!l~>l+<,:;!:l!l!!!!i:lI^!!l<l^Il!i!!
                       ;<i>iIil!<!<?~<!~<><>!i!>!i>~>li>i!>i<i<<<i<l<<~>!i~<~!!_>><I<<~~<<_~i!<!~>l<>>!!<>>>
                       I+ill!!!<<;Ii>iIi_<I<-+;i>!i>+;<i<~~>+i!~!l>I>IlliIl<>^'li<i,ii!;i>l;!!!~<l,!`+`,>+i!
                       l~<:+ii"il<<~_`i,+_I![_i"~<<i-<<Ii<~<l<;+<-i<?~-;__~!<i
                        .   ..            .      .                    '
                   .+_`:+<?;[~:+<]?!l-_]-?I_;<]><]]:>-_<_-<>:<-iI_<:+~_~>~<
                    .. `"`^`."^'''^`.'``'`.'''"''^`'.^^.''''^```.^`.```^'^`.   '.       .   ..
                       I_<!~,-!l<~--I<_+I~>~~+__+<!<;]>><_i"__I>?_I<<~+[;~_[-,_i>-~I~++~]--_i[,>~+-;[>~_?il~
                       ;_~?~~~i                     .'  .                  ..     .  . .....   ....'^..`'..'
                       .^,:,"""'.. '..     ..
                       ` +[_+'?[>!:)]}>;]<~]]!?>]_l~_-]~]_<i-i1i<<_-~li!~_l+?<+i+~~<~`+++~++>~-_!-_}>I~_?~~l
                         <;I~+->~+l ....'..   ..'...`"''''..`.'.'''''....`'`^.`',``^^.^^`''^``"``^""```'`^`'
                         ,^'"",^",`
                       `._<;l!~!";l<_<i!!I~>i:>i<i+<i!;[?-~.?]_l:]?<:"~li+]-+;!ill<>>I,>!>!~!i:i?__I^<!,:>!I
                         !ii;<<_l>~il<>i<!<ili_<",-<~:><<i+iiI~>!+I<>~+<!!-<ll<<>i>:><<_<!<+_>!li~+<!_~!;]~!
                         !~i;<_+>!!,,!!l;I<!;iIi  :;i^!!i:ii;'Il!l`!i>i!;"!!^;l;!il"~<~i!^iiili":<i~<ii~liil
                         I<>i>>II`
                       ..;;,"`;":"i:,:;;;`li!i^"il;''I:``":"^,;"",::"";`
                         ;l!!:iIi^<:l!!<i"<+<~:^+<I^^<>:"i>l,>>:l<<ii>~"
                   .,: ,;^..^``..".'` ` "^. ..^^ ''`'..'`..'' '^. .` . .`''.``''.^''.`''..`'.."'. ^'.''''
                   `~~.";~!!-<_I!_>>!"~:~<il<ii!!~i-~_<!i<+!l;i++,+?<>ll-+-<_<~+;}I~;<+~i+?;><[>_<+]~~<[[I
                    .. .^'.    . .     . .....'               .               .          .       .
                   ^-+.l_]-,++~_;<_<+"~~_>>_>l__;~+<<!;_>>~li:__"<_~><>i_!!?_Ii">?~>++i<^:~+^<_~!--i~:_~+_;
                       li:<<ll>I>!I><+!~i!<>i^!,~_+<?I+"[!I+<+I!<<,~-[~<i :?;!<>i~~ii_~,<~<>_~~i'<<<. ..'.
                       >~<<~>_!-__??<!__-~i;~;<li~;l~<>i<<I^^`'`":'","^,;  ^``,,,^,"`",':;:";""^'^",
                       """,,,"`:^;I:^"ll!;^`;;l:,!":IllIll^
                                                  .:   I"^':^:;,lI`l!:^":",,,"^;",";^"^""^"i::';I;:;;:;I:
                                 ,"            ^^ '>^  ii~:l::!:<i"<<+`i!>i>!<~I<ii~!i"i<il_l+^>~>i!!iiii`
                                 iI            !I      :;:;' ,"::`I;"^ii!:!;`,:' ,I:"':,,,;":'I".I:^':,^:`,I
                                 !I            >I      il<~!I~<>_i<~>;~<<l~i;--<^lI>il>i+<~i~:li"i<!:~<i!:il
                                 >;            >I      +<!:-]~+">++<"-l:i;_~:<l<]~
                '?<>>l~,+<`      <~","::;::::::_: .'   '.    .  '''' .^..'..''.   ...
                `?]{[]+^l>'      l~][)I .  ....i: l[^ .~!++_;>~:~{~-,,[+~_<--]:>-+__i
                'l!i<~" .,;I;,"^`iiIlI^`^^^'`^^<:      ""`.'^```^"'^`. ' .'`.''^`^'','., ^"..'' ..'..'...`.
                           .'^"l?__->+[l^^`'`^`<:      <~_;:_+<<__+<+<<!^i<<<>+~i_::[l.<._1"l<+^i+-+-l:~^~<I
                                 !i>I<-"       >:     .<ll> i<<! >+_I'+<",il_i!!i_ii I!:+>`I<>>>!_><'l~l<>>"
                               . ~>,:,^,:::::::[;      iii!i>^i_l:><<l:~~l<lIi:_+!!!!~l;i~!!>_~~~<!+i~I+i++:
                                 i"            >:      ><[~~il!<<I~+<I^Il;;"^I^Il,;IlI::II;:Ii;!!l"!i;^>":!,
                                                       ;;+~!~l_<>>>_l
                                                  '^   `".  .   ..   ....`'.'``...'... .''...'`...
                                                  l[' .~-[+^-<+~;~_~>;~_<+<+!i+~:_?iiI!~<+!;ll+~,+__~++~_;
                                                      .!<I;!'!iil<-!i <<i^>>~l_+il"->i~"<;i!~:!il~,
                                                      .>i-<ii>~_>~I+l~?+~><]![<i_i+!<+i"<!_~<l,l<;;:,^:;"
                                                      .<i<~~~l!-il"!I>><i+iiI-!<+>_I>i<:+<_><+ "i:l<<>!~i..
                                                       i+l"-~i>_i>l"?i,ll!ii+:l_!+~<";+__<l:~!_~:-I!<+~<+-l
                                                                                                   .














```

*Figure from page 20 (2346x3317 px)*


---



4203-E P-96



SECTION 5 AUTOMATIC MODE OPERATION


## 7. Sequence Stop (Option)

This is the function to stop the program execution at a desired sequence while the automatic operation is



carried out. Note thatthe sequence to be set must be the one already executed. The operation stops in the



same manner as a single block stop. The operation can be resumed by simply pressing the CYCLE



START switch.



The operation procedure is described below:



(1) Press AUTO.



..__



__________



__,_



(2) Press function key [F8J (EXTEND) twice.



(3) Press function key [F3) (NUMBER STOP).



Fig. 5-5 Sequence Stop Operation



(1) Press the AUTO key.



(2) Press function key [F8] (EXTEND) twice.



Function name "NUMBER STOP" is displayed for function key [F3].



(3) Press function key [F3] (NUMBER STOP).



"NST" is displayed on the 21st line on the display screen.



(4) Key in the sequence name where the operation is to be halted on the keyboard.



{5) Press the WRITE key.



When the block of the specified sequence name is read during automatic operation, the blocks up to



the sequence before the specified sequence are executed and the machine stops.


```text


                                                                                                '^^^``^ ,'^".
                                                                  '''.''.'.   . ''....''....... I[?]_+~._;]{^
                                                                  +}_>>_~-?l<.[~>+<]]-_+_:[}+]?_"+_+___?<<~?"
           '^^^^^`'``^```^^^^^^^`````^^``^`^^^`''''''''.'.''.'.''.''''..'..'''.`..''''..'.'''''`'` .`.'''''`.
           `"::::,,^'`'``^^^^^"^""''^"",:",""^^`^``:;;:,:,::,,,::,::;;;;:::::::;II;III;:,::;IIII;:,:,:IIIIII'
           l?      >|+~<<l~>><!~:l)->!>:`?_~i__iii<^
           ;i^     !1{{)/[{[+}?)<I|}}{n<!(?|t111)])! .
                 `'
                 i<~>ii~+i!~i<+~>;-I<[~l>]il~i+-~?l;~i>!>+ii:-:!I]<+!<!;~i+>~!><,+i<>I~<,>l<i!!<~,I>~><?i>"i^
                 ;<>!i~Il~",-<_I<<+i~_!>>>i<<!_<>l>>I~_i<lii!<I_>!!><l~><<-<l!i<l>+>i'~+ili>~!~_>!I-<i<iii<<"
                 !+<!iIi>~I,<I<i:<iii<ii>_~<~I>i!I;l~_<;l>~i!_l<iI!i>!_l>_<<l<>~>>~ii`;!~,i<<i~<il!~!~~!>i<?"
                 >?<<~:iii!<~.!-^>^<l_?!^>l!+^!+<~  !:~^!-~!~-i<^;~_`!_^I~ii>i_i:-;"->+_+^~>~~+i?;i~>">!<<!+`
                .+>~_+~`<~+~~l                                                                  ..
                 :"'...'``^``.''.'.`.'....`...''..'..'.
                 ><-I>?-i-]<>:-<<+-_+-~!_I}-_~~_-<i-[_++'
                                                                            '''^'`.``^^'
                                                                           "i>>+-[><-<+<.
                      `'''''''`^``''``''''''''''`''''''''^''''''''''''''''`i.`^`''`''''''''''''''
                     ::''``'''`^``''`````````````````````^```^`^``````````I;'`^^``````````````'`:,
                     ;" "^":,:,,,,:,::^^^^^^^^^^^^^^^^^^,^"",,"""^^^^^^""^~:""","^^^^",,^`^"^": .^
                     ,^ , ^l;,:;;;;;;l.                               ^;i(1!-]!)1;{/!+{>+1-;, l .`
                     "` : "Il;II;;;;;:;;;;;;;;;;;I;;;;;;II;;;;;;I;,   'iI+i:;;:;::;lIIl;Il!<; I '^
                     ^' ! :. .l'...........'....''..........'.l' '!   '!:<;;:;::,:,^:"""":">! I ^,
                     "' ! ".  ^                               I. 'I   ^_{(?t-1[{))/]|[[[{?~-, i ^,
                     :` ! :' .,                               l. 'I   "<;Illll<ii<_]i>~!<<i_I ! ^"
                     ,` ! I' .;                               I. 'l   "_<?+[]~-]??-[>~[_{)|[I ! ^"
                     :` I l' .;                               :  'I   `?~[>~}i~?~[<<?1{-{[?]; ! ,,
                     :` ; l' .;                               I  ';   '~_+~~{~_]_+_]~-|~{+>]^ l ,,
                     ,` l l' .;                               I  `;   ^-~?]]{~[+_-+[_1]>)}_-" : ,,
                     :` ! l' .;                               >  `I   ,-I;!il:lI,l!i-;!^;>I~, ; ,,
                     ;` i I' .:                               >  `l   :?:I_`I'i>>_l[->i;'}?-, ! ,"
                     :' ! ;' .,                               ~. ^!   :|/([r~'__<_-1<<}:,?--" I ,"
                     :' l I  'I                               >  ^!   "|t)[r<'<>i[]<~<},"+<?" , ,"
                     :' l !;;;I,,,::,,;;;::":;:,,::",:,,::,,:,l::;;   "{1~!1>'+~<1<++~_:^-+[^ I ,"
                     :' l ;ll<<!i~il+->i~<l<+>>+~lI<iI!~i!<+i>iiIl^   ,[]__}l.>l-Ill!ll"'_i]^ ; :"
                     :' l I.'+_<<-l:+]i!]~;!_ii+?ll?_l_]l;[?l~~~.'^   :<"^""",^il,""`^"^i!"~" I ,^
                     :' l`"::,,,,"::,",<!,::,,,,":,",,;I;>>,:,::::`'''^:,:,,:,i~::;I;;;~i,:I^`I I,
                     ;`.'`''''''''''''l;''''''''''''''`'!I''''''''````''''''',>``'```:>,'``''`' !:
                     '"^^`^^^^^^^^^^`iI`^^^^^^^^^^^^^^`il`,,,,,^`^"^^^^^^^^",+,,"^^`;i:,:^``^^^:;.
                                    ;^                ;"                    l.     ,;i-i_-?<+-_i-"
                                   I"                I"                    ;:^'"^.`::;::::IlI:::;:.
                                  I^                I^                    `!l?i_[~~i<+!__+-~~>>}~_^
                                 l^                ;`                                        ..
                                I'                I;_i~i~~;~><+~l_+!--<~]<<++-i>?<+^
                              .I!i:lIl:;;:lI":I,I!+I_>>+_+~!~~~+l::,"",,,"^"",::I::^
                              ":I~ll><i>~i<<!!~<<i>l+~++<>>lili!;


                                               ;_-;!~-:;[~~<_i>_:~]><,~?><i-<<:
                                               ..;"'``.."^,,,^^,'`"":.^;,"^,""'
                                  .
                 ">>' +<___I[?i!?i++i>+_;
                        ...  ..  .    '^'
                 `_+. ~~!>~;~i!>~il;~~,>_]<>[<><_~__Ii~>il
                 ':,. ^'^",'^"^"^"'';;^"';,";"`^;":;^`;"""
                      ~~!>++>l:>+i_:;[++][[~-:-~i~?;:<"]<i_+<<ii~:l<<i+<+;+~>:}<}:
                       .. .'.  .` `. .'.'.``  '  .  .`.^^^`,,"^'^'.""^"",'",:`,'I^
                 ^_+. i<<<<:~~i><iIl_>,+i~I![>i-?--+:<<ii_!.
                 '::  `',:I^":^"^"'.,:":.:,^,,,,,::^."`^,^^.
                      ;]-~~^iI!-~_-_<<I!<^++;i!!<l+<II<">>II-<~_+:><<+~>`
                        ..  '. ``''"'` .'  ` '..' '`..'..'..`"^^:.^`^^"^
                 ^+<  <~<:lIi<i"i>i;<li>"l<Ii;:<li!:l<I"!!llill;"l"l"iI"l!>l!"l:I~l;>ll!;lll'
                 '^^  '":^'``^,.,,;,:",:."!,I:"l"l;,,;;^llI;!;I,"l^I^ll`;lll;"I,:!!"ilill!lI'
                 '<I  !l;Il"iI"l>ilIi"I;;.
                 ^>l  "^IIl^;I:"l::"I`;l>^
                      l~il::!I,!!:i":I!;":!!!i<!I;>II:!III:llI!:!"ll!,l;:l;,::l;I;!i^":lII>;l';l;ll:;!:^I,;"
                      <~iiil!>!>~><!>>i<l+_>>!<~>__~~<<ii<l<~;~!<;<~_I>~ii~<<~_~!!_+;i<~ii-i>;Illl!!!il,_Il;
                      >i!"+i<>il><:<>>li:<<;;~~>>_~>:<>+i<;l~"i<lI<>>!>+~:i<<l<~>;!+<>>i!:_i_-"














```

*Figure from page 21 (2346x3317 px)*


---



4203-E P-97



SECTION 5 AUTOMATIC MODE OPERATION



Example:



When N112 is entered following function key [F3] (NUMBER



N105



STOP) during the execution of N105 sequence, the machine



N106 stops after N112 execution and before N113 execution.



Sequence stop



N111



N112



N113



The sequence name, where the sequence stop is to be executed, can be changed by specifying another



required sequence name. It is also possible to cancel the sequence stop by pressing the WRITE key



directly following function key [F3] (NUMBER STOP) without keying in any sequence name data.



[Supplement] 1. The sequence stop setting is cleared by NC reset.


## 2. The sequence name entered for the step sequence name is handled as a character

string and therefore, comparison as a number is not made.


## 3. Setting during the scheduled operation causes errors.


## 4. If the main program is selected correctly, setting is possible either before or during

execution of the main program.


## 5. Even if the sequence name which has been already read is set, the program cannot

be stopped at that sequence.


```text


                                                                                                ^"^"',`.:'"^
                                                                  '''''.'' .  . ''....'.. ....'.~[]?i?I"<l]l
                                                                 '[?~<!~~?i<;:?>~<_}]?~~>;{-_-[l;_~-<+-~<+_?
           `^^^^^``````````````````''''````''''''''''''''....'''''''''.''.''''.'..'.''.'''''''..''.`''`'.'''
           ,::::,^^``^``^,,,:::::::,,",;;;;:,,,,,,,""":;;,,,,::;;;;;;;;;;;;;;:::::,::;IIII;I;:::,:IIIII;:,,"
                '-l<i!>~;
                .::!;:!I:
                                  ..              .    :+<!!"~ililIIll~>l>!Ii+lii;!Ii!I>!l:i!I:-!_,<<l___~>~
                                  ;l ^-<+]:    '' ,"   ;-~+_>l!I!ill~>i<i~>;~+i<!<{~<__!<i;!~+!~,]~>ii~~_<ii.
                                  :: '!:;i^    l` :"   :<;l>l;<>;i+<l~I;>>il~<!;I<l<Ii+,~>_>_<i<"I<!;l><ill>
                                  ,, ^_i>]:    l  :^   I?~~+,_?-;i_i><I-<+i>_ii,_i>:_?_~_:->:<!>+-+i]~~;
              :~I;:lI:l^l!l,      ,,    .      I' :^      ..   .     . ..... .  ... ......   ..'.''''.'.
              "<!>!ill<^i>+I      ,,  ..'      `! :^
                      ^"          ,,    '       ":"^
                       ^;:`       ,, ^>;;;       !:^
                         `,:,^'.. l; `>;::       l:^
                            .`""";}: ^-ll~"     ",:"
                                  :, `l,:!'    `? ;`
                                  "` ,_Il+"       "'




                `!ll"lI;,I;:;^:III,.I;;;;^lI^:;;,;;:;^"I,^:,:":;"^"::^;;:`',:`:,'::,:",,":"'",,^I^^^.^^`;;"^
                `i<~l_~]>~i>>Ii+>i>,+!<!i!i_:~+-~~i>_i<_~>l!ii!_>i__<i__~;;+~:>-I<i-<-?~l<-I+~]<~_i[_-?<?_-l
                `+<->l<<^+!~!_ll+`;-!!>  <,<"<<>^>!><-~~^~::~>l>~"+!";+i<~<;i>^_<~,!>`<!>>~<>I!>!"_>-i~_'~_!
                "]>_~[>!+>>_<i-!_~i__~;<]_:?~[!~[~?1)1_-I-++-]!;__<<>!>-_~>~l+,~><,+_<<~~>-;i?<<<"-__:   .''
                 .   .' .  .'':''''``'  `` . ''. '.''^'  .  ' . `..'`' ^"`';'' ``:',":",^^:`':"",':;;^
                :[~>+_~>!~i_`   `:  "_i!,~>ii~l!>"<i<"l<]_i!;i,>!<>!lI<,l+!^i>i<"
                ^:,;I:,"^:^:'    .   .`^',";::`^"',";."::",I'"'",:,,"'I,`:^':;I;^
                                ;!  ^il;:l:,";,::":;:!";:l,:;;!";!:^;l:^;,:,,"^"^,;I;::;II;;<::,l":,I;I;;l;"
                                ";  "<+<i~~_~~~~<!-~>+:~i-<<~>~!i>+l>+-l+_-~+>i<li_~<>~<I~!!~!lI_I!l!i~i~i<:
                                    ,+!:+,~!i:i>i><!i!.!>i+>~!~>!`+l:!,i><~~l:<^i~"Ii>+<
                                '`  '' `'.  . .  ..   '.   .     . ..
                                l<  l}+]--~i?~++_~_~:?~?-_+]-!!}--+{+~;!-_+_]l~~<~-l
                                     ..  .'     .              .
                                I~  !<l>!:i__:~<>-~<i"<l__~~<~+l<<i+~-?">]?->_!+I~>+-]]i>-?<_l_+?~~I<l!<!<_~
                                    l~<~ii_<l:-l_-I><+~:<i~+<_<:''.''.^''`'''"'`'``````'''''`.``'``'`.'``'":
                                    '"^^^^^^.'`.`^'`":"',`,!":`'
                                !!  !l:!";l!I^;::,;::;`,;,:`,;lIiIl!Illll,l!IlI!,;lll;::l;`i;::::;;;;":;;:I:
                                ,:  i~i<>l!>~><~~_~<i~l!<i<!<iIll:I<l;!!l"!Ilii>l;i>l:llil"!l!>;i-!>I;l>II>;
                                    ;_:;~>+><<,+:;l+,!~<!<!i<;








































```

*Figure from page 22 (2346x3317 px)*


---


## 8. Single Block

4203-E P-98



SECTION 5 AUTOMATIC MODE OPERATION



When the SINGLE BLOCK switch on the machine operation panel is switched ON, the single block



function is turned on and the program stops after executing the current program block.



There are two types of single blocks.



(1) Execute Single Block



This stops by the block accompanying axis movement execution, miscellaneous function operation



or coordinate system setting. This does not stop by control statements such as CALL, GOTO, etc.,



or a macro call command, return command, and NOEX statement.



(2) Read Single Block



This stops at all blocks including the control statement.



(a) Execute single block is generally used, but for checking programmed operation, read single



block is used.



(b) Read single block is switched on by setting 1 at bit O of NC optional parameter (bit) No. 2.



(c} Execute single block is determined by switch status after one-block execution.



The read single block is determined by switch status when one block is read.



(d) If the single block is switched on during automatic operation and single block OFF state, the



block under execution is completed and the machine stops operation. Jf there is any buffered



block at this stage, one block is executed every time the CYCLE START switch is pressed. If



the buffer empties, a new block is read and executed.



(e) Read single block is used to stop the execution of a program by each control statement, IF,



GOTO and VSET in the schedule program.



(f) During the program execution called in MDI mode, setting of the SINGLE BLOCK key is



effective.



(g) For the details of the stopping manner during fixed cycle operation, refer to "FIXED CYCLES"



in the Programming Manual.



(h) During the area machining mode, the axis stops at the completion of each motion when the



single block is on.


## 9. Optional Block Skip

When the BLOCK SKIP switch on the machine operation panel is switched ON, the block skip function is



turned on and the blocks preceded by the slash code ({) are skipped.



For details, consult "OPTIONAL BLOCK SKIP" in the Programming Manual.


```text


                                                                                                .`^``'" ^''^.
                                                                  .. .'...      ...   ..        :[-?_>+ ~:?1"
                                                                  <{_<<+~??!~'[<>_<-]--~-:-[~_?_"__+-~+-<>~[:
           .`''`````^`^^^^^`''`''```''''''...'''..................''`'..'''''''`..''`'..`.''''''.`''^'`'.```.
           .'"";;;;,^"""""^""'`'`""^;;;;;:"",;;;:::::II;::;IIII;::;IIIIIIIIIIII;:,,,,:IIIII;::::I;;I;I;;:::;'
           i1      l1>i!!<_!^|[~!!<-.
           <\:     !|?-]c)(["\1{{1{/"
                  .
                 <?-_i'i+i^]?]_~i_'1il<<[,:~~-i!.<!.<+;,>><<<l>.!<<!+?!!'!<><>^~.!<ii!i>i`<_! ?<i^+!i_i^->!<^
                 ~i><<ii;~:iii<~Ii!;+<il~i:~>i<i!>:i<>>:l?-!:><l><?i<l->:><i<>li;iii>><!<ii>i."",';^ll,';::;`
                 ,:^"";" :'""":,.""`I:"`";^I";i;;,^i!!!,;liI'iliIli;<"l!;:l:;!I,>:I-l>!"i<!iI.
                 ii<l!^i>;i~!"ii><l;i:>li+:!~Il!I
                 ''"^,'"^'',^.:;":^`^.,`lI":I:::;'
                  ,I^ ^<;!;,i;">::i;:_I;i'
                  :;, ^l;l;:l:'l:!<:"i;;i'
                      .<lI"!lIi,;l:<!"il;i"!lllii!!l!!!;:!i;;I;I!ll!!:IIlI;<ll^"llI;l!l;l;,I:I::!I;",;::;l:;'
                      .I:l;!!~<l!<:l!lii!l;<i!l;>]<l<!<~li!!;I!li!l!l:i!i!!<i!;:li<llli!>ll~;<l!i>>;<-~Ii>!!`
                      ^<^I>i;>>>-i:_<~<>;;++il?` !i+"i>~~"Ii;<!<I~<">!<+!;!>+<!i+i_!!~<+^<<l<~>i':_<ii<:,]~`
                      ^+,<:>~+!i:i?>I>!>i><i>'l-<ii"!ii<<<+i<'<>>:?+~_+Ii~]+<!<<+    ..  .. . ..' ..  ......
                       ' ' .``   `^ .`.``^"^^'."",^'^"`"^,:^".:^"'^"^""`":;:,^;,"
                  >-: "_~<~;~~>+_,_-l!!
                  :;^ ',::;'":,>;',,:,"
                      ^+!<,~+>~II+:-l<<i+_lIi>i~-<~l?+;!<i-<i,_<-~<>>>;
                       ..` ''`^`'`.^.^'''`' `.'^``;.^".'^`"^`."^:"^^^''
                    l+:^+Ii;I<I^i;!i:l~li!,!`>!Il;>~",!ll:"!;:!;';;I;ll;:;IIlI!llI;lI"!l!l!II,.IIl;,!:;!"
                    :l^^+<<_!_!;+i[<",I:;:";:~I:I:i!::!II:"lI";I`I:!IlIl>lII~!ill;li;,_>i!>l!;`!><I;<I_<;
                       'l!I>`!"I><i^
                    "".."...'.`... ^^'^.`.''^^^`'`.'.`..''^'. '..''`'`.'``^'..'....   . . .   ....'  .
                    <?;`~-_-l~+~[?;-_<+:_I<_-_~++iI+;~-,_-]-_+,"-i<?l<;_l]];i-_<<_+!_-~-<+-?II[?<;[~'+:
                       .'       .                     .     ..                               .. .
                    i+:,?<_<<?<:-i]?!<]~-iI<;]_?+~+>+-!-_:-_?<+:__?i~:?[?l;i_i>-><>,+~_><?<<^
                       .;^`.^`^^'^,`^'^`'^'`''`^`'`````^,.```"`^'^^^'''`".`.``'```'^`^'``'`'.
                       '>!<^<_->!?>[-;<>>-l<!I-__>>~>_+l_>I____~:?-?i<I?~_<"<<~I+~<],_;l_-+`
                    .'  ...     . .'        .                                               ..''
                    ~?,"<i~~:->+?>!~>_+,_,___~+__;!<"-_>>?;~<_~<>?_"l<<!<+i+"~!~"<<>}_,_>i~"~--i"?_-> -il
                       ,~!!!,ll~+;:<i!I>->l,<"!<!<_++>i;<~i~_i,i>+ii!~,+~i>:;><l<+l~; ii~ii!"!^Iiil<!]~><l'
                       :->><"<l~-i,+~>~i;<!l!!ii~!~!~>i!<~!il<I><ii>ii;+<<-!~?<?>-_+il+;i<_~!l!>!<Iii~+lI?`
                       :->!<,]!ii<:i~-?;'!l>:>!i+^<,<!~>>_<iI<i<<:!l<l;l!^l:IlI<'il!~<l'i<~i<^<Iil>~<<>" ~.
                       ">+,i~-_i"~i<+_~I,>,<_il~!<<^>,>~_>l+>!l<~+!<+_I
                    .. .^       .  .  . .     .      ..       .    .
                    -[,:}_-?;+!~{_;_<<?"~Ii~+~;<^<_+;i~+"~>~i<]<>:+!+;_<_?~+>;_!l-_+lI+<_~~l+--__~+i<'?l
                       "--i<~;~~+l>_1_<"!;?+I>~+<__~~:>i<_~+<".'. . .''.^^.'..``.``'..'''''.''``''`.`...
                        `'  . ^.' ..`.  . .` `^'`^"`''^',;^`'
                    ,[^"i,l;I,i!;;ll!l>!;:!Il;I!I;^l~>lI;"I_<l"lIl<,`!i_!l,:Ilil,~ii>i;>"_:I>l<,II;`I.
                    `l`"_]>i?>>;,;::>;I,":I;I;;;;,"I!l!,;":>l,^;;Ii:^!!>l<l;,:I!^i;l!!l!"<I;!I!"li<^i'
                       "<>ilI!>
                    `^.'`  ^'  ""^^^.^",^''^''``'..''''''.^'`' .^.''...''......`.. ..`... `^''`''.`''..`''
                   .+{^:i<:<<~I-~+<~"~l~~!l_~?-i++:>-~i_~^]-<!?l_+--I+++-:__+i?]ii";_--,-;;~<??-!li<<~~-]!
                       ,!;-_;<~<-__>+i_+~i1-~!+?..            '      ..    .      .                   .
                       ..  .    "'.  ..'^ ... .'
                   .+_^:_!i!>:~<,I>!~^!i>><<<!i">!i+";~i"><_:<~i~l;<l-<,l!>i<<>!i:;iI>!>;:i!+!l"i!!i,ii!.
                   .^".,+<<_~~+<i!!>!iI,:^""",l'^"":^'",`:::^::;I"";^:;^,:,;I;::;^,",I;;^^:;l;,^I,II^,;I
                       ,il_<,lili;"!^i;

          .]l     '++!l_>lllI+"_]~I;;~":?~l;;`
          .\?'    `1{x1|(({}tr,(f))){\-If\((ci

                ,]->~;~_>i}I>~>-:?-_-"~<+<i,!;I_i"!i><<!<">+<!!<i!I!>>>;i,li>~i<<il<_"l~<:~i!<,~~i;iIli>il:!
                :~><+<l<>;<>ii+i:<iiill<<<ii~>il>I!+~I>>~>!<>>?!ii!_~l~i<!<+~;"::"^",^^,;^:,::`;:I^":,;:;"^;
                `l::;:`:^^l,"^;;'I::;l^l:;;IlII^:I^:l';II!'^::i^::^!;'Il!>!!l
                :il^l<>i~I ;lll;~^Ii<li!<>>> i>,i!<i"+>!<`;:,!;,~;;;:l::;l;";_!l;Ii.
                `^;':I:lI;':I:;II'`;,'";;;Il^Il,;;I;^!I;:.:,";!"::!_Ii;Il!>>;<illi>.




















```

*Figure from page 23 (2346x3317 px)*


---


## Program Branch

4203-E P-99



SECTION 5 AUTOMATIC MODE OPERATION



When the PROGRAM BRANCH switch on the machine operation panel is switched ON, the program



branch function is turned on and the program branch commands in the program are executed.



AOGRA!I



BP.ANCH



Two PROGRAM BRANCH keys are provided and each of them turns on/off a program branch command



respectively.



For details, refer to "SUBPROGRAM FUNCTIONS" in the Programming Manual.


## 11. Optional Stop

When the OPTIONAL STOP switch on the machine operation panel is switched ON, the optional stop



function is turned on and program execution is suspended at the block in which M01 is specified. Pressing



the CYCLE START switch cancels the optional stop state and the program is restarted.



When the switch is off, M01 is neglected. In this case, the program is executed continuously without being



stopped.


## 12. Mirror Image

When the MIRROR IMAGE switch on the machine operation panel is switched ON, and the mirror image



function is turned on for the corresponding axis. For the axis for which the mirror image function is called,



the sign of the coordinate values is reversed.


#### Press a MIRROR IMAGE switch while

holding the INTERLOCK RELEASE key.



MIFmR MIRROR



'--+-"'-IMA_Y_GE_, _1MA_z_GE_ 4GE



INTER



LOCK



RELEASE



In addition, there is a programmable mirror image (G62) function, having the mutual relation described



below.



Mirror Image Mirror Image Switch of the Coordinate



by Switch byG Code Value Data Signs



OFF OFF Does not switch



OFF ON Switches



ON OFF Switches


#### ON ON Does not switch

The relation is established for each axis, independently.



For details of the programmable mirror image function, refer to "Programmable Mirror Image (G62)" in the



Programming Manual.


```text


                                                                                                ^^^^." ^`'"'
                                                                 .....'... . .  '..  ...   . . '---?!<.~;<)!
                                                                 ;{->i>_-[I]'<->+>[{++>-l?1_??["<+_?__-i+~?I
           `^^`````^^^^^^``````^^^^^`^`''''''''''...'''''''''''...''''.''..'..`'.''`''.'''''`'`'`'.`'''.''''
          .`^^:::::^^"^^^^`'`',"^""""""`^,"",;;;:,,,:;;;;;;;;;;:::;III;;:::,:;,,::;IIII;:,,:,:IIIIIII:::::;"
           <+?    `|_!>iii<~<~.?)ii>!!l-I
           i_}"   "->+[(v]](-]"](-[)+{]?_
                ..                         .
                l]<<_"i_~"+~_~+___[["[[+]?~>_"!~-~_"^~'>~i'i<>><!<`l~>l>_!>^;~>>>'~'!>+<li<l:<-:`+i:I>!<i~<I
                li><!<,~<l!~>!;>;~!>><:>l:<>i!_<I<>!<>i!I~!><~!;i<!~_<!<+;<"__!l<;<!~+i!>>l!l<ili<<^,""l,;,^
                ":I:":':;,:;;"`;^I,,l:`;"^l::,;I:!':+;!,";l;`;""!l;I:!:;i";`ll:IlI~>ii,;>l"!i>ll<<l.
                                                  ]t:^^`^: l|I``'`,'
                                                 'X(_i!<l"Ixf~!!<i`+
                                                 ^;!f|(\-'<:"/(/t[.>
                                                 "+``:l'."<>`^:<`..~
                                                 .l:,;l;;l";;:I<::l;
                '.  .''...'.   ..
                ;_~;l~_~<_]]?)_+1_--[~+<i~++;++ii~<~~?~ii_i<i__-;i<+_~<I+>i<lI<><_Iii~<_<+<;>><i!+,i>i>i+>ii
                :>~~i!>i>_!'.'..' ..''..'`"`'^`'^'```^^'`^```""`'^'`^"`'^"'^^`^^"``",""!,:"'"",^""'",""^;,"^
                ^::!:,"^,;l
                il!'<<+~-; <-_;ii`+_i]++[~<_-+~]ii>i-+!>~~_--"l;>>!;_ll<!<i!!i!;<-!ll!I
                ''"':::;::',,:`^:.^,","'""":"",;^`^,,:^`,::;: "^,:;`",I+;!:;:;l!:!!:ll:

          ^]]l    !1}]{)]_-_{1,f)[_-_.
          .III'   "~+{~+__i~[<'-_--)-
                '^'       .. .'      `^'^'   ...   .'  .   .                             .
                <?++<^<~i,+_l>~~__?^i->>?,;++-<<^~;l]_"i+_~>!<";~~~<]><^!+>>+^~^<~<~<i<!;-]`;?~,!<-<l<+^~>+"
                !Il<_lII<l!:!<l:i:l<illl>ii+!:>!>li<;!IiIil!i~I+~<i~i+!;_>i~Il,!+<>!>?+!:>;<i<>-~_I:_<<><!-,
                +->i_<~<i-!_~?_--:<<-~-;_]<<i~!-_>!>+>i<<i~-~il?-_l<>>i>~!l<liI<<iill+<>l+>]~l;;ll"'::Ill:<:
                II;`,^,:,; I^,l:^.I!;::`;!:,I!^;l;'i!lI"i^ll<":i>+"I!l,;I;:iI~<i>`^!`!i>>l~!"
                I>lI;"il:;!iii"I,!~'++!::,;!I!l;I;l ;"Il;":II:'!;^:::;;I:^;`:::"^l::,,:II"^,"I;^;!!,:;:;;::`
                !_!+>l<i:;lIl;"I,;I^i!:^:;:i~>lIll;.:,;Ii,!>>l^liIiI!-!<l,!;ii>!!>i!li!<<l!!!i~:><i!>!I<~I+I
                !<<_+<>"

          ^Il:    l~>:,"""`,:,`"''^'
          :{|[' . [Yt|{}(t:_f|(xrxx<
                                '"
                <_>i!:_!:~-<~_<>~,?++>+i">!>ii^!,!>I"llll>Il"l;II>!l:^l!;!,I"I;>I!Il;;<i ;II,ll,"ll:;";:;:l'
                <>i<~!iili!l!i<li;_+!+~!;~>>~iI<l>~<;!~~l;+~l~]~!+>~l+~>>-l+!+_<i<+~!l<+:<<>i!+ii>~!~,i<-]]^
                <~!!<>l;>l<I!>i;>I<<:i>!!<I!~+~>i>!>+i_>! l;i"~>:>>>l>!`<!i>!!~>:i<liI;i~+?lliI>?!I;>:~-+~!.
                >~l;<-i,<;-_;;>i!~->?-"l-_+-!li"~i<i<<~'
                     '                      .'^''.'`^"^^^`'"'`"' .''. '`.
                                             !+]]>i-[~]]}??[}[[>[]-[i[]]<'
                                           .,Iii<_~~~:~!ii~l<<><-!<<<?~I-+.
                                     ,>"'`~i~ ,i"^^``" "l^`^`^" "l^'''^^
                                     LcI:li~IiCzl:II:;iZnII;l:l>mn::;I:l:
                                    `Il?]}\+.-,i?]1)!.~I+]}[\l^?I_-[11I,l
                                    `l !{-1 `]I i{+> ,}" <1?< ,], +)?~ ,;
                                    'I'`I-I,I!i;,l!,;><l,^>i,;i<i:^ii,,!,
                                     +)Il[::;. ```'``. .'`'`^^' .``'`^^'
                                    .u->]]_"^>
                                    `" l]}~ '!
                                    ^>+[>]]_"!
                                    '><~i!<~i:
                '. ....   ..
               .~"!-~?-~_^~_-~>;_;<>_<_~+~~<>--?"~~~~<:~<-?-"_?{[i!-<~[~+;"~_<<+!_+~"+~+>]<:_-?+>I:]_~<[-_-,
               '~~+>~` . .    . . .'..^'.   ....  .... ..`"'.'.''' '''''''.'`'."".'`.'^`^"'.^^^``.'^^^^`^^^.
                ","",.
                         !!lli]_<<>ii!ll!;;IIiIIIi_<lIIIi>ii>llI;i::><i<i<l>!!l;!!l!!i!l!l:,;`
                         -^  `][><?l_-]}+.   !   ,1->_~l]_{1?'..._ .>]-?]?I]i{]><+]-~]~?[-'.!I
                         _,'.. >]"++~_+< '''.!... ,?!i_I>>-}' . .~..   :~-<<:><]_"-~_>>     l;
                         _;^``^'`l___:^",","^>```^^^">]]]I``````^~"",,^^~>i<ll<~!~<_<>,`^^^,-l
                         ~,""""""I<ii"``'''^"_"""```';<lI^^^^^^'`i''''^"<>+_l:>i;<+_+<,^`'`'+!
                         <"``````l+__,'''''``-```''''^~-_'````'''i''''``...+___+<<+^''^^`'`'~l
                         -,^^^^,,;~+~,,"^^^^^~``^""""l<<~,^^^",,:~,^^^^^^":_~<+>!ii"^^""",,"-l
                         ?"''''''`>~+`''``'''i''''''`i_>>^''''''^+```''.  .~_-_~~-~.  ''''''~I
                         ]"''''''"~?+""^^^^``>``````":_]_'``````:?""""`"-ii~Il~<;<i~i>`'''`^~:
                         <I,:,,,,:i!l````""""i,,""",`"!><,,"","",~"""::I-~-]>!_>!___+~:::,,^>,
               .<iI^Ill>::,!,lii>>>IIllli;;lll;:l!I^!;lI;!Ii>l>!"'```^^^'''.''.'`'''''^^^^^``
                :;i^Il!i;I`I`I!l>!il;!:"!^"l!;`,i!l.IIi~i!:!~l>~^
               ^l:`"lI;i;`I:i,`:,,:;l;l;Ill^,;;:"^;;;;::,:,I":.';>l,l":<;;;;;;;:Ii;,I>I":";::,:",l!!I",^::"
               "~>;l~<~+<i!;_-i+!_?l>Il;<!i:;!III"II+->:i!li!!:"!i<,!:^Ili-!<l!l~_ill+<;i,ll<--I!>_~<`!;l<>.
               ^il<]!~lii<><!__ii~!









```

*Figure from page 24 (2346x3317 px)*


---



4203-E P-100



SECTION 5 AUTOMATIC MODE OPERATION



Example:



a) In absolute dimensioning



N80 G90 X100 Y100



MIRROR IMAGE



Setting changed



here



b) In incremental dimensioning



N80 G90 X100 Y100



N81 X50Y80 ----- N81 G91 X-60 Y-20



(-50, 80) ~



.<It!;-··



(100, 100)



-;;. ~



.....,f //



(SO,



so~/ f



/ f



y (50, 120) (150, 120)



100



~ --?l_ .,, - - :;



1) _,...><-...._



..,..,.... (100,



100} '"' )



(50. 80) (150, 80)



/ I



--+---+----t-;--+-,-;---+-- X



50 I 100



-+--+---+----+--+----- X



50 100



/3)



(-50, -80)



(50, -80)



1) X,Y: Normal



2) X Mirror image ON



Y : Normal



3) X,Y: Mirror image ON



4) X Normal



Y : Mirror image ON



Fig. 5-6 Example of Mirror Image



When the mirror image is on, as shown in the example, the sign of the programmed command itself



is switched, disregarding whether the selected dimensioning system is absolute or incremental.



[Supplement] 1. When the MIRROR IMAGE key is changed during automatic operation, the state



will be changed over from the newly read block. The buffered commands are



executed in the previously selected mirror image/normal state.


## 2. During the single block mode operation switching, the MIRROR IMAGE key from

on to off or vice versa after the completion of a block of commands will change over



the state from the next block.



Example: N100



N101



rN102



Mirror image ON



When, after the execution block N101 in the



single block mode, start-up is done with



mirror image ON, the operation starts from



N 102 in the mirror image ON state.


## 3. Be aware of the following related capabllities:

The mirror image function is valid for the instruction G92 JP which establishes a



work coordinate system.


## 4. The mirror image function is valid for the instruction G51 JP which indicates the

coordinates of the center for scaling.


## 5. The mirror image function is invalid for the coordinate system shift G 11 JP


```text


                                                                                               '^^^`^^ ,''^".
                                                                  .''.`'... . . ''....'..  ....i]?]-+~._;l_?,
                                                                  ~1-<<+~~?!~.[+<_<?]-+<_:][+?]?"+-~___+>~~[,
           .`````````````''''`````````''''''''''''''''...''''.....''.'..'''''''`. '.''..'.'''''`'`. '.''.'``.
           ^:::::""^^^^^^""",:;;;;;;;:,,":;;;;;;;;;;;:,,,:;;;:::::::::::::;IIII;;:,:,,,:;;IIIII;I:,,,::;IIII`
                 _!i>l!<!.
                 ;:l;,il;
                   '>'  !;:?il!!>I"~lil;il!ili`      ""`'...'`''' ....'``    `!^  I,"l;:I;;I;!:^i;II;I:;I;;'
                   ^!'  i!i~i<ii!i:i!!iIiiI;:>'      i`',~>>~i>!:<!lii^'!'   'i^  !;:>ii~l!~l+i:~l>~i>llil_,
                        i_-l;~->">,>?"l!~_;  ;,"""""^!  ;{-]-_<_~[-?[]' l,`... ', !_?!:+-_"i!l+;,:I~l
                        >-<:;_~i,>_<         ,^'```''i  ;]-]I>:;;;I+l:  !I"``^^,! l~<I:+~l`<"!~:l,:+!
                        ,l:`^;I:.,l:                 ;^"!_+<,`^````'``,:!         ,!I,^!i:'!"li`^^,!:
                                         ..                  .   ....  .      ,.  ':` ,"^     .";..,;"
                                         :;                                   I   :-_'+?l     ;![?^>>;
                                       ..^"        :!_:"~-;                `,"i    '>`li.''^^,`^'-^
                            ."i_`~~^   i-~I.`'`^',"!l}'.'^'                ;~i>   `l .'',:!,"..  '''
                            .^":',:!~^,.^"I.`."->i":;:                        i    :_;^l!>.:<~;""!,-
                                     ,+. ^"i[,l[<,".:.                      `^~ ~[:i[I ::l'^II' :_[,l_;
                                       "-~I.'  ",. ^"                      .~<~ ....'.          ``:`":^
                                         ^:  '"`   ;                          I
                           .'.'..'''`'''',I';:^.'`;"'`'.'`''`   .`"^'`^`"``''^<'``^`^'''`""'^^'''^"':,
                           ^"^:^^^"":^^""!+:^^^~>;l`^!~!^^':;   '^;"`^^^,^^'`"~`^^^!?"''`!~>^`''''^.,"
                                        ';!    ;::   ^l;                      I    "!.   `::
                                      ':`,!     `^                           '<
                                    '",  "!    ^l";                          '~
                                   >l.-" ^l    +I~["^><"                      I
                               `:l'"!;'  ,<      ""'',,`                     .<
                              .:;!`'<i'  ">                                   i
                                         ^!                                   !
                                         .'                                   :

                                 '. '... '' .. .                      .  .  . ..
                                 !l i>lI l-<i!+_                     ._! !<ll !{+!>;I_--]i!?{:
                                ._I l! . I-!:I^:>ii~lI~+`             +l Il ..:<I:Ili .'`
                                .;" >! `.<1~<_>i:Ii<:":;'             I: >< `'!)?i<+_I:::""li'
                                    '' . ^I;:,i;                         `^ ..:>l,!^,i>-?l,!<^

                                                ,:^ ,^:.;,^^^`^^.",:,^^^'^``'`
                                                !i[">!+'<<__>~~_;-!]_!~<,><]?-'

                      :_<Ii,lil;ii;!,Illii,i,l:.iI:<;Ii;";;il,!I!!Ii>^:!I,llI"ll<;"::;I;lIl;ll,:;:;::::;lll!`
                      ;~I<<ii+>ill~~Il!~]]l>;<<;++i<l+~II><>~i+i-+<++!l>~i~-i;>><<l~l>{>_i<~~>li<l>!<i>i~_<l'
                      ,l">l!iIi<^^~i!i+<IiI+:iIl!I>I`I>^i~<>I+i,i>!<;ii!!>>>I+i+<!`!;!_>i!i-I,>`I!!~i!~!~<
                .;,'`^^'`..^'    '   ,".' .^' ^",,"`"`."''.^^ .. .  '     ... .     .   .    . .'   ..   .'.
                ^[_~+~?-<_i]<   .I. ^?<+-ll~-,]-~__~~iI{]_<[~;+-li!;+~_<]_>I-ii~-I-+<<>--~"___<__>i^;++"++_+.
                                    `<>^l_';<>>!+!!`i!_.;!!l.!<i`!><<;'~+_,I_!l>' I<<,iil?><-<"><<><~>>]"i<<'
                                    ^+>>i><<i>i<[~Ii<+<i!>?l;<_~l-++i_i>+!ii<<+<l;!>>+l~~~~,,^'""^^^,^^,'"""
                                    ':::"";:^^^'":^;";",;;l:^;;;:;;,'::";.,:;>>;;;:;:i`;lll
                                `!  ^l^::,.:;"^;""I`,:":`'"^,; ^""^,I^^."::"^,^^ ,,'^I;ll;,!::!;;:l,,,"`;"""
                                ^i  ^<>+i~_~>iI~!?+ii~<<<i<>+-:>__i~_+<,~+_<!_~[;!_<;_><~<><ll_~+<];!<+;!!!!.
                                    ^<:iI:+;i:I!<;:~>~>;]+<"<>l!<>~+i_>i;i>i!+~>?:~I>!>>!~+i-Ii~;l<__>[i;i<>
                                    ,<+:_]--;+<~l<?>:<_-i>->+>                       .   .       . ..'^.. ..
                                    '^`'``^^.'`'.'``'`^''''`^`        ..     .
                                    I_>_><~?I         ,?l<-,         "[+i~l^~-_ll~<;<i<~<_!i:+>~-;_!i<^l!li~
                                      .. ..           ':`":'         `<!>+!.<<i<:'>I!-i.l_<<:l<`;l'!!l!",<<i
                                                      :-!~>'         ^<<_~!`<>i>l^<+>!_,I<_iIi[,;!`+<>-"i+>l.
                                                ....".^,^,,'         "<~!<;,l>_-<,!<i.>-I">i<<?<i"I<<i<,>!>!
                                               I"^^^i^;_!+?,         ,-I<];<">~i"<~!<Ili_]]l;+-">+?~`
                                               `                               .    .   .``.    .....
                                              l[_l>Il<>_~!l~?:
                                              ';"',`'^:!i"`,,'
                                ^;  ,i,',,,:,';^;".",:'`^`''^,:,""`"""""I:^^.
                                ,<  ;_l"<><>!"~:>>:I>~l~>>~:~+-~~I;__~~i-_<>.
                                    .:^^.""``''^``"`"'^^^^``' `"^^"'':`.''^'`",^^`;,:':"  .^"^"`'^"^^"^"`^.'
                                    '!!<;><!<;Ii+[?!!><<<>Il<:+_~li<;_+I!~-!~<+<i:--]"~;'^,-<<~l!_+-~___~_I+
                                    :->_l:i>!i>>_]II_~-><;                              .'
                                     .              '
                                :<  ,>>i,i<Ii:I<i<i,!ll!+il:>"!+~!>i:<~!Ii<>li~!i,>_>^l_.  !~!i>^l!<I>><:<i!
                                '"  ^Iiil~ii~lII~_?l:ii>+<;!>"i<<<li^";:^:;,;;;;;`,I:.",'"^;I:I:`,;I:ll!,:Il
                                    ,ii!i>I+~<I,!^i<"l<i<>'!>^>!~_l?"
                                ''  '^              .               .  '       .            ... . . '.
                                !<  :]_>I~-i+l><<[}i~_~++~<:_l~>_}-i?_,__ll~+_~?<][l<__?_~,+-[]l]<I^{"'''
                                                 ''                     .  ...  .....`..'  ...  .   . ",'









```

*Figure from page 25 (2346x3317 px)*


---



4203-E P-101



SECTION 5 AUTOMATIC MODE OPERATION



[Supplement] 6. While the mirror image function is active, G codes which indicate the direction of



axis movement and I, J, and K commands are changed as needed.



Circular interpolation (G02,G03)



Cutter radius compensation (G41,G42), etc.


## 7. The positioning direction for 660 one-direction positioning is not changed even in a

mirror image ON state.



Example:



Mirror image ON Mirror image OFF


## -----------------------x


## 8. On the display screen, the mirror image ON axes are identified by the "-" sign

before the axis address of X, Y, Z, etc.



12-1. Mirror Image in the Work Coordinate System



Normally, when programming is executed in the local coordinate system, the mirror image function is



effective in the local coordinate system. However, it is also possible to activate the mirror image function in



the work coordinate system currently selected by changing parameter data.



(1) Parameter Setting



Whether the mirror image function is activated in the local coordinate system or in the work



coordinate system can be set at the following parameter:


# IACAUTIONI

NC Optional Parameter (bit) No. 34, bit 2



0 The mirror image function is activated in the local coordinate system.



1 The mirror image function is activated in the work coordinate system.



{1) The initial setting is "0".



{2) When the setting has been changed, press function key [F7] (BACKUP). After the



completion of backup operation, turn off the power to the NC and turn lt back on again.



The new setting does not become effective only by changing the setting.


```text


                                                                                               `"""'"'',.^^`
                                                                  ''''`'.'... . ''....''......'<--[<-l,+:<+!
                                                                  -]~>i+<?~>!^]>i<+[[-++>;{_+_1i:~~?_?_++~__.
           ''````^^^^^^^^^^`'''''`'''`^``````''''''''''````'''''''''''.''''''''`..''''.'`'`'``'`'` '''`''`'`
           ^,,,,,""""""""""^",,,"`"""^",,,:"""^^"^^"^`^,,:,"^^^^"^,,",,,:;,:""""":""^",:,:::,,;,",,^"^"^":;,
                 ~~Ii!i!l!l>l   ._  '<<l!,"!I'l!:::';Ill:,!:;lII`:^,Il;l^.>';:ll;';;I;,";;l:II`iI"^i:;:l;"'!^
                .lIIilIl,l;I;   .!' '~>>i>l<<;><!<l;i~_+i:~>>~-~:i!>_><+>,>;<i<_+I~i+<I!i>~<_?l+iI,>l>!>i:">'
                                    '~li"Il!l>:i>I"~;l^ :^:>!;!";><ii>_!+>,_>:ll~<<]+;!?^I~<>~~!
                                    ';;,",;`^:;,"",::",`ll;;`l:;;
                                    'l!Ill+""I~i<iI<l!I`ii!>:~<>~
                                    '!:>!I.;l!":`,;;;;;::;!:;.Il;;"!li>'"!;.
                                    ':I!il.;!lll"I!;iil:liiI;`lll:"ll!>^:il.
                                .;  .;"`.`^`,^^``' ,^``,``'"'";:`'``.'"^'^^^``^^::`^"^'^'`^^`,`^'`^"```^'^'`
                                .I. .!i+i~<~_<>!i[i->-~-<>I<!!]-!ii+l<-~~+_+I+~<--i><~~~!!~>i+__<[_<<~~_;<;_`
                                    '>+Iil:<>-?<;+?I<-_-:
                                    ':''`''^''^     .....
                                    ,-~-<<~]!
                                                              '
                                                             .;
                                      "I""'":""^,;`          ',         ^:^`'^^^^`,,"
                                      ;<;l"l<<+;I>,     .... `;         I+l!;Ii-_;!I,
                                      ''^^""^``^^'"I"^^"::::,,I""""""""""",""``,i
                                      .... .......^i.        '"
                                                             `:
                                      ..'''..................^;..............            ......  '.
                                      `,,,,"^^^^^^^^^^^",,,,";!^"^^^^^^"::::"^"^^^^^^^^"",:::::,.II
                                                             `:
                                                             `:
                                                             `:
                                                             `:
                                                             "I
                                                             '`

                                "!  ^!;.!I"'il;!I^^;":;;'.l;^`I;,,`":::I,^!i`";,;`^::':I,:!l::^:`^I,'^`^^,,"
                                "!  :<~;><!l+~+~?l:+i<_>:`i_i:>+;-^;<>+[l^!>"I~i~:l>>^i+ii~>~!"~i,><^'^.!+[l
                                    ;~+_!<:+>:><~li+~~<~_:iI>i.i`-`i-l

           !+<,<. .11_<~+^+_~-_]Il<,[~-,][+>],_<+<><]~i--~,[<<_?<<l
           ',".^   ,,^'", ^,,I+!''`."^; "",,,'^"::"":":ll; ;i;;l;,^
                ^+lI;l<~".ilI; ";;ilil;lIl;^l'l;l;l<I!.,.ll"'I:!^^IlI!~:i<^"!I>!l, ~l,`;!;;""l;lI;,!l:!lI^^I
                `>[<!-<~!:~~~l;<>!-<+i+<i_-:<;_++<I+]<;>;!~:l>i~iiiii<+>?-;!~><-i!l<<i;l~><I:>>__>:_<i~~>;;<
                "+>>i>!>,;;i~I>i+;:!ll<i!<>;<<~?!I :<!+<i>>'lIlI~<Ii!><~~~li;!i<i>-i;!<;>il!:Il>__I!!l!>!lll
                :-~,><i~"><<i?><_~;_~-+<!"~>l~>?-"_<<~~~<l_<"~<+!-<_>i_+~<i-]~^~__!
                   .  ..        .  .            .         ..   ..^ '`'...  ... ....
                 "~>' !<~<-i_??,>]--~-:
                      `^"`"^`'`^'''^^:`..'.. ..`..''.. .  .'..' '...'`  .         .                 .
                      i?>~_<?;'++"`~~;~,:+~_}~.~i!_~~l^_.<~_>i?<+^>,;?_'!-~},!~<~_?>?[;I?~--+i`?:;~^]_i^]~~<
                      ;>i<>+!+-:i~~->>;I+!:__:+_;-l-_!<_]>+<><;~~i_<~-_l'...  ..    ..  '...   .  .  .. ..
                      '^^^^^`""`^:"""`'^,^'`'."`."'`^`.`^^"^`I^,,`"`"""`
                      ,>,"""""""",;:;;;;:;;+_>I>!>!!i><_iii>>><l;i!llil;<~l!<i>!:,,,,,;IIIII;;;;;;;i`
                      i~`^''```^^^'`^``^`^`_]i;_[]_>_]i+]-[_---l:}]~!-_"~[Il}!~,...  '..''''`^^^^^`~I
                      !<``i+``^<++?>>]+>?!_i~__I-<!+_~il<!__+i_+_ilI+i!i~>]<l<i>+_~++;<_--++l^^^^^`+I
                      !>'`:I^^:?<~+ii~!Ii:!!<_<I~<i++<!liIii>!<>>!l;~<il~<_!Iii!><i~_!~_~_~i;`'''``+I
                      :<,"I!,",~>+[<~[?_?i?-}1{<]-]][?><+~[]}-{]]~?!?-+i]~?+<???]]_}{>~]-]?_>""""""_;
          ':",,:"^^^^',";lI;Ill;^'^^^``,"""",I::;:;:,,,:,:;::;:;;I;I;;;:,,,:;;;;IIII;;;;:::,;;IlIll!"``````'
          ~>(\!?1_}1{|{.I""<>,^]~_l<__-l~~]~+i<il]!`'''''.''''''````````''''''''^^^^^``''''''''.'''`"""""""l
          !rOQn]\|[\/x)';..,,. ,:I^,:II`;;I;l;": ".                                            .           :.
          .,``""'"",,^, ; '_-'`-_~<:'i<":~-]l~^i~_^I-_+",~~_>-++',~<<-">+!i]><`!~-`~i>;"{~_<_~>_<. l]-+^!-_i
                        ;  .. `!!i<<><>>^i>>~-<I<I;>>!!~i>^I>~l"<~<-iI>!<il;~"<~!~<<"!i<I!>I:iii><"Ii:+!<_;I.
                        ;     '+>!!<>>;iI+i!!!<i_:I~<!i~ii;li;<>>!!>!;+<!<i">!!~!l>I"-!l,>+i;l,lI;^",`l>ll';.
                        I"^"""">i+;~~+:<_+~++l_~->!~+>_+<<<~!i_-~~>+i!~~+!]i;~<i+{>]>~<l<_+?i-"   .. .   .'>
                        .^^^^^^''''...'.  ..''..'```'`'.......  ..''``'```.''.....'^^``^``'.'``^^`````^^^","




















```

*Figure from page 26 (2346x3317 px)*


---



4203-E P-102



SECTION 5 AUTOMATIC MODE OPERATION



(2} Comparison of Mirror Image Between in the Local Coordinate System and in the Work



Coordinate System



In the figure to the right, the local coordinate system X'-Y' is set on the X-Y plane of the work



coordinate system X-Y, and area A is machined. Under such conditions, the relation of mirror image



between in the local coordinate system and in the work coordinate system is as explained below.



0 X



(a) In the G90 (absolute command) mode



1) Mirror image in the local coordinate system



y;:



Fig. 5-7 Mirror Image in the Local Coordinate System (G90 Mode)



2) Mirror image in the work coordinate system



0 X



Fig. 5-8 Mirror Image in the Work Coordinate System (G90 Mode)


```text


                                                                                               ^^^"'^.',.```
                                                                  ''..'... .  . '... ....  ....-?-}i-:;<,>-_
                                                                 .]}+<>_+]<~l,[~<<_1}?~_<l}++~};I-~[_-_<~<_>
           '''''''````````````''''''`````'````'''''''''''''''..'''''''''`''`'.'`.'`'''''`'''''``'^.`''`''`.'
           ",,,,,"`^,:::,,,,,,^^""^",",:,:,,,,""`^^`^",:,:""","""","""::,:,"""^""^^^,::::;:^^,^^,,;IIIIII;:"
                  i~' "l;IllII!:;.;:!~I:;`IllIl^~!llllI^;"li;""I:l^I;;::i;Ii,:i;lI;;`I,I"""!:^!!:l^
                 .ll` I~<<+?-i_~li>l~_<II`;;i+i"!iIi!i!"I"li!,li!<";l!!l<!<+l:<<<<il:<li;;:!i,i>i<:
                      "!iiI<!!<~`<<<~il`
                      ^" I:'";^':.:``l,.",I: ;;:',"":'"^"";"";"',^::",.;^^;','^""'"`^;^.:^,`^:^^`."^^^`.^^^^
                      :i"~_<I]]!+;<>I--II1->^i~_">i-<"<i>i->~_~"-_+-~<^<";I'_:i]>,_:I-~"<;l^+-<i+^+;i~<^_>ii
                      :>~lI+l+_lI_i_~!"<"l'_<iI<i~;iI>:>_<i!!<~'^>;>-;!>l~;i!i!+~>i>'-~!l_-?>l"l!l<!I!:i!~>>.
                      !+_-~~+>;>:_>I<><+:i>>i->_]iI~<_~+il~<i<l<]~"~>~~:i!ii-><-i;<<~<>llil-;>>>~><><>>~_<]I
                      '"""",,^'^.'^`^"",'"""^"^:;"';:,:,^^:,^^`^::':,:,',,:":";I,`l;;;"^","!^;;l;I:;I",lI,I^
                                                 'i;
                                                 ."~~-           "!
                                                  .<l>;  .  .`^,;;l<
                                                  '>  i: [;;;:::   :!
                                                  .<   <`;~   ">`":"?l':;.
                                                  '<   .~.ll`,,"::;:!>::{:
                                                  `<    .> l?::;,"^'
                                                  `<  .^^~[":^'
                                                  `i .,"'ilI
                                               .`':~`^`'`''l^``````````.`
                                               .`;?>`"^^^"^`^^^^^^^^"""+?
                                                  :l                   ``

                   .ii'"!:~i:!<-!,><!l!I<,:l!!lllI>,:l;>!
                   .l!''"^;I"";!,^i!lI;;i",IIl;Il:!"^II!!
                    "^ :i,"^'","",`^`::^',^"".^^^::",:.'`,:,:'
                    ;l I+Il!,l!<_-!II!ii:<!~!;i>i><i+_;i_><~<:
                                                 l'
                                                .!! :-;       .'>^
                                                 ": " < !>":::,":<
                                            .'.'.;!:],,I,+ . l`  !!
                                            l~,,I+;  < < i,^";II;i[,:l].
                                            '< .<-;^"+"^i,]!l;;;:<1!..I
                                             ;-:^!i;:~_>1^;{;:"::' !`
                                   '::",Ill!!I)[~)_I:~[<,<^-^^:]+;I~]"l^
                                       `,"^'. l-"?+>i  >`i"I-<l;;;:<;'~;
                                               > l_il::[l < !,
                                               "-_;''. `  ;I
                                                .l"        <'
                                                 I^        "!
                                                 i^         <^
                                                 <`         ^<
                                                 i           .
                                 Iii"lII`!-i;l"!ii!<:;:I!I:,I:i;llI;I>:li:;>;l!;;^!<>!,~I;II'
                                 ""~:,:^ :il,!^;ll~-;:,:Il,Ill<:;IlI;i;i>;,<>i>!;,i><!,~!!i<`

                   `_: i-il!":lii<:I:!>l,>I>:,llll>l<~,lliill^
                   '!" ,l:,I'^:l<>""",;;"!;I""II;;;;><"l>!il;^
                                                  ^.           :~'            .
                                                 ;~;,^^^'"; ;: ._`'>I '' .''":<i
                                                '~  "-:^">_ ~'  <'."+.l_,,"l^' i"
                                              ^"i[::;>". i.;:   i'  `i ~   !"`^I_
                                              `:::,::,:l];.>    ;.   l`:_;I:;I;I>I1^
                                                    .'`^;"_l".  i. .^I?"i,"^`'.   "
                                                   .     `i.^.  <. .^>i:
                                                  .,,"::,:""`^"~}""^^``:"":;:"",:,"^;+
                                                         ^!.`. "~  .^'!,            `>
                                                  .'`^",i,~:^.  !  '":_"!!^^'.
                                              ,:!!,,,,,I_l.l    >    I':-i;,:II~I;"
                                              . <<^`;iI  !'I^   !   'l i  ^!,`,_l''
                                                'l .!<I""~i.!   ;   <'I?:":>,  I'
                                                 l~,`'''."' :. .I  .: '`..''^l_I
                                                  `            .<            .'
                                                                ;
                                 !i<`>l-'~]>!i,<>>>_;!,i<!;?>!i"il!i>_!<+:><!<ii:,<~?!!?!!<l.
                                 `'!`"^: ";,":',:;i>",`"::`I::,`,:;:;l;!!",!IllI"";li:,!IIil













```

*Figure from page 27 (2346x3317 px)*


---



(b) In the G91 (incremental command) mode



1) Mfrror image in the local coordinate system



4203-E P-103



SECTION 5 AUTOMATIC MODE OPERATION



Fig. 5-9 Mirror Image in the Local Coordinate System {G91 Mode)



2) Mirror image in the work coordinate system



Fig. 5-10 Mirror Image in the Work Coordinate System (G91 Mode)



In the G91 mode, if no rotational elements are included in the local coordinate system and the



coordinate system is shifted only parallel, the mirror image function has the same effect in the local



and work coordinate systems.



Explanation for the figures:



AX ....... X-axis mirror image is turned on for machining area A.



AY ....... Y-axis mirror image is turned on for machining area A.



AXY ...... X-axis mirror image and Y-axis mirror image are turned on for machining area A.



(Machining order : a - b- c- d)


```text


                                                                                               ^"""': `^.`"^
                                                                  '...'..' .  . '.....'.......`_]-[>]`!l:~]<
                                                                 ^[?~!<+~?>_"!}<i<+[-?~_!i1+__{,i-~?---<<<-<
           ^^^^^^^^^^`'````^^^^^^`````````````````'''`'`````'''...''''..'.'''''`.'''''.''.''''`''`.`'.'..'''
          .:::::::::"`""^^`^,,"",,^^^^^^```^:,,,,"^^^,:,,,,,;;:,,,;;;;::::::::;;IIIIII;:::::,:;IIII;;,:,:,;,
                    ~~.:!:~i:i_~::>Il!llil!>:IIllli!Ii`IlI>I
                   .:;''`',:^^;:.^;",,,"I,:I^::,:,ll:I`,;Il;
                    ;" I+I,,^"::;I^^^:;,`:",:`,"":;^,:^""":":`
                    II ;+l;!,;!i_?;,;I!!,il>l;<il>~i~_;!~<~!!:
                                                      :;,  "
                                                      ^!?'_-!             .
                                                       ^>   +'     .'",:;;>[`
                                                       ">   "_`Iii;:,"`.   "~
                                                       ;_",,,~~-)<    >. .';\;
                                                     +~!-`,;  ~ ^>".'^,,;::-}]::<i.
                                                     il.<._<'':-_|)]i:::":::^;?.`~.
                                                      +{-""^::"<]_?<^"^"-+'.:--"
                                                      ^x?:::,;l^_`i++!',i;;::^.
                                                 .`":;"]?`^:?-~^;{?~_;,^..      ...
                                     ;I;;:;;li<~!l>iII~i)+!>+ll>!_>"^""",,,^",:,,,,I?.
                                            ^`.       :;!^`.      ~'               '!
                                                       ;!         "<
                                                       l!          !;
                                                       lI           +'
                                                       iI           "i
                                                       <l            .
                                                       <I
                                                       i:
                                                       >:
                                                       I`
                                 i<+`iI_`>]<!>,ii~~~:i:i>i:Ii!+I>i!!>_l<+I!+!<<!I"~<~l;?i!>i'
                                 ''l'^^,.^:"^,'"";!!^,`",:`:::l`",:,:I,;I,^lIIl:"^;;;^^l;Ill'

                   "-" _[>!<"ii~~_:~:+~lI_i<:;i><<->_?:i<_+i<"
                   .^' `^``".``,I;'^'`"^`,"^'^,,"",":;';I":,^.
                                                       l<+  ,?!    ^;        .
                                                        "\-lli["'. '" '^,,:;!]I
                                                        "1:'.';],;--[~:,"'.  '~'
                                                        [1:  _??^ {-]+  ~`  ."1~
                                                        +|~;;::"?`!-[! '^,,::;;,'",!I!.
                                                       ^l+'`:,;!-/(xj|[~<ii!l:;l!;;,:?:
                                                       .:_^",::,"?{\\{]<!;ii!;:".
                                                        ));,^^;l:I(|[]  'i: .'??}.
                                                     '^"|-`:~){<. }\?|^ ^ll    ^>
                                      .'''.'...'''IlII;^I)+Il>lIlII)i:I;;:,;,_~[^''..'.
                                      ":::",,,,,,,:,"^"+-{];lII,"``<}^""^",:I!;I",,,"I1'
                                                       "iI         :[^                l
                                                        I!         .'~
                                                        lI           Il
                                                        >;            _.
                                                        ~,            :i
                                                        ~"             ~^
                                                        ~"             .'
                                                        <^
                                                        +`
                                ."  ...'..''.  ..      .!' '. . '.   .     .       .
                                :+?!l<;?;;1+i+iI~+]]<!>!_-;?_<?l>_~+~]>-}_I[+-?_~;-[[i,}-<]?:
                                                   '                        . ..  ...    ...
                     'I'l:^'II;'^:^:: ""^".`,::,"":.":""^^"".""``^``',^"'".,`''`'^'.''``"'`^.''`^``'.```'^`.
                     `~"~<~,~_<^;>~+_";;I~:!~?-<><-^<-~!~i>~^-+l;<>i<_~i:+'<<i"~>_:;~i<>_i-_l;]<+_<l:_i>,!+,
                     'li!!~l>->:+><<!;Ill<<_~i,ii~:~_<<+_`+~>,<>Ii"~><+]I~li<~!I!<-l>-il-<i~:+{_<ii;~<i!<i?:
                     ^->-l_i<i:<<<~-!_]!!~>__<<! '.''..... .. .. . ..'"^ ...'....'`..'''^''`.'.^`''..'`.``".
                     .;`^'"^`'.""^^"`":^';"""^""
                     :-<_-_i-]~!,_!I-<,__!i~>'
                      '`"`^'^``' `'..` ':`'``
                       ~_I      .^-:+><;i~><l;_>+?~;<;><<++;~lI_l,<~>~<ii~ii<i~,_'
                       '`.       .`.^`'''''''.`'^;^.`.^`'^^.^''`' `^^^^`',:^"`"'^'
                      .-+` ......`>I_>i:<+i<I:>+--!lil><>+<;+;i_;I<~<+><~~Iil<>:+.
                       ``''       `.^'`.'`'`..`^,:'.'."^^^'.^'."'.^"^'''`:^^`^"''
                      '__~l.'...."_;-~-:<_><<;~<__~:?>~:i<_-!;+>!>^>~__]Il~>;+i!++I>iI_i:<+~!~><_ii-~-:-"
                                  ^"`'^''`....``^^..'.'' ''''.'^.' ..'"".'''.`'.`'.`. ''.'`^.'''",`^^^'`'
                                 ^[]-__i~i?l><-?,.`+'I:_;;"l,:![
                                          ..









```

*Figure from page 28 (2346x3317 px)*


---



4203-E P-104



SECTION 5 AUTOMATIC MODE OPERATION


## 13. Override

The override function changes the feedrate or the spindle speed during machine operation within a certain



range. The function includes the following:

- Rapid feedrate override

- Cutting feedrate override

- Spindle speed override



13-1 . Feedrate Override



Programmed, manually input, or dial-set feedrates can be changed during operation.



13-1-1. Rapid Feedrate Override



This is effective during manual rapid feed operation and programmed rapid feed



mode (GOO, G60, etc.).



Actual rapid feedrate is "rapid feedrate" x "override value".



When 100% is selected, the axes move at the rapid feedrate determined by the



machine specification.



13-1-2. Cutting Feedrate Override



This is effective for the programmed cutting feedrates in G01, G02, G03 and



other modes.



Actual cutting feedrate is "F command value" x "override value".



RAPlO



'Vu % OVERR l DE



o 30 50



1 90



0 @



W./'v % FEEDRATE



80 90@105110



70 120



00 130



50 140



[Supplement] 1. Override rotary switch setting is ignored in tapping cycles called by G74 and G84,



or in synchronized tapping cycles called by G274 and G284.


## 2. After the M136 (cutting feedrate override ineffective command) execution, the

override rate is fixed at 100% irrespective of the rotary switch setting until M137



(M136 cancel command) is commanded and executed.


## 3. The axis does not move at a 0% override switch setting.

13-2. Spindle Speed Override



Spindle speed can be changed while the spindle is



rotating.


#### The NC operates according to the spindle speed

command given from the PLC. The actual spindle



speed is displayed on the screen.



TO% SPINa..E OVERRIDE



110



120



130



90 50



80 160



70 180



5 200


```text


                                                                                                ^^^^'" "`.``'
                                                                  .'..'`... . . .`... .' .  ...^??_]!?.~!I~_!
                                                                  :{->i~_+}I-'+-i~~[}?-<_!<1__-]^<+~-<-_<+<-;
            ^`^`^^^^^^^`````^^^````'''''``````````''''''..''...'''''''. '''''''`' ''''..'''`'''..''.`'''.''''
           .'`'":::,"^`''```^^^,:::,,,",:;;;;;;;;:,"":;;,:,,,,,::;;;;;::::IIIII;::,::,:;IIIII;,::,:IIIIII;,:^
            ?<}    `[]>>->>_<]_^
            >>[,   ^?_?-(-~-}[(:
                 '^
                 :~+i;<--<+[l~+i>~>l;>~+i_+i+_>!-~~>+[liI+]~l_~~_?!i~<~~i~~~i_l!<-+~i~I>-<>~_>>:~_]>l!li~+_<I
                 ,<<<+l.<<~l<>><-!i:<>~<-?>l-~l+__>~~>i`.'`^'"``^```"`^`'`"^';,'^,^``"`";,^,""^',""^^""":";"^
                 'I^;l` ..,'',`,;"^.^:^:;;:^;l^;I;:l:Ii
                   >i,;l">I;;:l:.,,;:,l;
                 . :!ill^iilI;>l'lli;;>>
                 . ,^^,`^.,^^,'"" '.``'^"
                 '.l>><l~I<_+_i-_:ii+ii__.
                   ^.. '^             .
                 '._[?>-1ii]-+-<I~++<+{;

           'i_;!,  l]~_~?__?_,~+i~il>__`
            ^I^^^  '';l;I:lI!`",:l:`:li
                 iiIl:;l;;IlI.;II:"l<"^ll:I.l,;i!;;iI!!;!l!iI""l;"l;`l;;::;I"I,,::^":;,:l,:'
                 ^^:!;;;,,;I;.";I::llI^;l:I'i,;i<:!<II<!>!<<i;;<!^i>"!I>I+~<:><l!?!l~+!<_>>:
           ';l"""' ^i;,:,;::"l,::':"^,",:'
           .;!"""` `!~>i:";>!!!><^;;!>;!<,
                 "il:";^>!"l;:^,::":^,;I""i;;lllIl;l;;Il:li;;";,;:;,;;;:::;:",;:::I,,"        ."`''
                 :i<-<i+??-i<?_+ii<-<;!>Il>;I~i!:i!i;><<I<<>!IiI!<il?><!!l<<:l-<i;>ii;   "II"l:|1(}l-.
                 :!l>i'iii>'^>>i ;+;:.                                                    l;!|:[-,i":.
                 ;Il:::^:,;,I;";;::^:"";;;I,l;;l:I;"."':,,:::l,`,;",".                  ^`+}>+!~i_[;I
                 ;!ili;"iii,;~i!Ii<,::.I<i!"ii>il>i' : "!!<lI_l^><!i`                  'I(i";":";,:(<;
                 I>l;;.:l!!"""^Il:"!l:"~I"II;;`;;,I,!:!I,^;;l:!l:;:lI"l!!I;;I;;II;,i;^ "\>:}>!lii1+~r~l;`
                 !~<+-!i><<>><_+_?<_i;^ll:!lll"Il;i:!;:ll,>>i;!>ill~>:i<i>;l!!>!l~;ii; ;!I<[IlIll))+>l__"
                 ;!<l!!!;I->>I!l><lI.                                                     .Ii!Ili;
           ':"`',. '"."`'.^^''^'`' "^^^^^"'                                                  ...
           ^+i:,<" :<<_~~~;i+~->?_">>_~!~[:
                 ;I,^'^ :i"^I^^`:^`:".^"^`"",""","^^;:"^^,^",^,^``^':,"..:,:'.,":`'``'  .''. ` .``''''
                 ;i~<:~:~~+<_i<,~i">~:+<>]><ii!<~I!i-~<]:_~~<+?+iIi^+_>,`_+?l`_+];><<;  :<i!.>^"?]+-<<
                 !~I_";<l<<<.                                                             ,^l-[\-ii'`
                 "^"'^^'`",``^"`^"`"`'`':'''```''''.'^.''...`'''''`...' .'              ,ii{{?{z]-|]i+:
                 >_~i-iI~_?<]l--+<~]~I_`>^<<~<<+~<!;--~_``l.!+~-i+}!;-]<-,             I~<|i"i1)1;"_/>_l
                                                                                      ._~r^':_+.)i; +\I+.
                                                                                      .>~r ;"I> ?,!`^r;_^
                                                                                       l_\}.`?]^{<^^/+<~
                                                                                       .l<|\_^<;< +|_-i'
                                                                                         '`;_     :<l^.
                 ..                  .
                 ~[_-_?+>_<~+    >. '>i>~li~;Ii~~!"<<~!!^~~]>~;!I!+i!i>!i;l+><!>!,<li~!^i__<!<~;_<~!!>>l<-+i
                 ..'`'.. '..`    .  .i;!!I~<i++i<-<_+i_+><><;+_><_ii++~>lil<][<->>_<l]+~?~,:^"I`"^`^,,,^":,,.
                                     ,.'`"I",,"^"";I;^;il""!`:I":I^:l:II'II'lI`,'!:;`llll:
                                .!.  li;" !;``i,:>^ ,^II"^ I:^;":" ``"^^:, ^^^i,"^'^ ''^'`""^;^'"^"^^:`^ ";".
                                .!' '<>~i"++I;-!!]l!+<-+~-"??--<-_^!>_<>~-^i+__-<>>_^!<<ii++l+;;+<~i~-i>^i-]^
                                    'il~I>><`>~~`i^~<_! ?'I>>iI'll+_<<i~!I^<,<<:^!<i<:l+~~<:I__-l_,i>~,+]I<<'
                                    .[[l>{ll+i<-i;><~>~?>?<;<:><<<i-~_-_i~~_I~~_>i-+-"..    .. . ^'. .    .
                                     `. ..  ` .' ......`.'' `.`'.`.`.`^` ^'` ``"'````
                                '-' .+><"~<~"~~<~"!il:ill!"_:l:~>`!Ii!l><^i!<!i^l!~!li
                                 ^   .'".,""',::;`":"`::,:^I`:^",`::;:"II^II;;;^Ill;l+.
           ":I'l.  ;I",",I"'l,^"^`,^I"'`^``^'
           ;<-;-^  i}-<~]?-^_1]]-]~;~~+?+<_[+
                 ;`'.^^ ...'''....'..`..  .. ```'``'..'.'^...                   .  .
                .--~<~-;-]_+_li]ii]<!~+~+?-ii?i+~>~+l[<~-[iii                   ])[:li:_I--!`>_-?>[^
                'l<__i_!                                                        ^,:il^:<;(<!<```.'^.
                 ,^^`"I:    ...       ..  .  .                                    ![[j1]i!i--?~;'
                 l!_^_?;"_<_<?-_"<<!i>--+il~I]~,!_i!<?,I<+<<i                    .i~}~f[?<^""<1l?,
                '!l!lI><>!!i!<I<!ii:_iI~+>i.^_~<;__><~I~~i<-I                    ,i|^.{-^!-:l !):<
                '~>>>><>I<?>+<l!>l!;i_!"!ii:Il,;^;;;;:"!:":I"                    ^!|""I;_:`+1.!|l<
                .<i>>i,l^i!<>>>i>"l::>!"ill~<I                                    l]i ":;]-!_^!>_;
                                                                                  '       `"^'
















```

*Figure from page 29 (2346x3317 px)*


---



4203-E P-105



SECTION 5 AUTOMATIC MODE OPERATION


## 14. Manual Intervention During Automatic Operation and Restart

Manual intervention refers to the function in which manual operation is performed during AUTO or MDI



mode operations.



(1) During the AUTO or MDI mode operation, press either the SLIDE HOLD switch or the SINGLE



BLOCK switch to stop the cycle.



(2) Press the MANUAL INT ON switch.



The control rs now placed in the manual intervention mode.



(3) Carry out necessary manual operations.

- Manual axis cutting feed

- Manual axis rapid feed

- Manual axis feed by pulse handle

- Spindle rotation

- Tool change, etc.



After manual axis feed, that distance is displayed on the display screen -2nd page of ACT POSIT



pages:



[Display screenJ



MANUAL SHIFT ACTUL ......... Manually shifted amount in the present manual intervention



operation



MANUAL SHIFT TOTAL .......... A total of manually shifted amounts until the present manual



intervention operation



(4) Before restarting the sequence operation, restore the miscellaneous functions to the previous



conditions, and locate the axes near the posltion where the intervention has been made using



manual cutting feed or pulse handle. Then, press the SEQ. RESTART switch. With this, the



axes return to the original position. The data displayed at MANUAL SHIFT ACTUL will become



zero at the same time.



IACAUTIONI : In this return operation, the axes are fed at a rapid feedrate. Therefore, it is necessary to



confirm that the return motion will not cause rnterference between the spindle or the



cutting tool with the workpiece or the fixture on the table.



If the SEQ. RESTART switch is not pressed, the manually fed amount ls not zeroed.


```text


                                                                                               .`^^'`' ,.'`^
                                                                  '''.'....   . .'.   ..       !--[~~!.-:!+?`
                                                                  _]~<<~~-+!<'}~>~~}]?_~_;}}+_-<,+-?~-?~<~-]`
           '^^^^^^^^"^`````^^`^``````^^^^`''''''''''``''.'''''''''''.`.'`''''''^'.'``'..`'``````'`.'`.`'.```
           '`'`,:::"`^''``^^^,^^'`'^"""""^`^`^,`````","^"^,,"""^^"^^^^;:,,:"^^"",:::;:^""^",":::,^""^:;;I;;;.
           :~?>    _/[_<<!!+-"_>-+<ili>!<-<!il'}_;l<>!l; [I:>l;l!;!<il.!~I:;;;I<>:,;'`;:,!^i-:,,I;::!
           ^>++'   <|?(]+}])]"]_})1<_])-]{{{}-"1}1}_[]vt:|11))){}(f){\,?{r/|\]ft|)()l-n1(jI{\t|t/tj{).
                 ..
                 _?_<!-,!_?~!~i?~<:>][_~;_;]_<>?+<-~~:~Ii]_~+;~>->i]li+_~~-<_:_I<~~_~<<__:~<~><;>_!~~II>I}++"
                 i><_>;<<<>+<~~<'...''''.`.''`.^'`'`'.''``'`'''`"`^"'^,"^""""'"^,,^^,^":,'":"^I,^,^`"`^,';"".
                 "^"::';;,`:,,,:
                  ,;' ';"";,.::^"i,!!;`;^><I^,:,I:`::::;;:: ",,:"`;I,:`::^"!`I:;`::;^;`^":",'``^,^'::,,"`,
                  Il" ,?~<+[~l<il+>l>l:+,_-+:l>!~+,~<<i~i<>^<i<~i;_>i_"i~i;]!+>>">>~i+:<__++;iIl__:__-+->~
                      "[i!>!+"<~<>~^<:l-_~:-_,!+i]!
                  .'  .'         ... .. .'.. ...
                  ~?, l+<--i!~+!{_[]~_[Il]+I!-?:+-?<_:
                  ..  ."''''.'`.''..'..''.. ''.."'.''..  . .     .
                      `+~+:~+_<~!>!l>_!i]]~_~l~:<~i;~?+<-+l<]+i-+-_+:>~~-[^
                   .                                        .  .  ..   ..'
                  ~[" ;+-~~;i~<I-++-__+<;!~-<>]>!-+~+]<~_I
                  ..   .""``'``.`^`''^^^'.^`'^`.'^`'``'`^'
                      ' >]->i_<l-~>:<-+!-;-_+<
                        ",^^'^^'^^`'^``^;"'^'
                      ' <++>!+!I_i!,~?><l?+~^
                        :I"^`"^`""`,:,"^".'^",^`""^";`
                      . !~>ll<;l~i;:_<~I_>!_<~~;i-i~-i
                      . II,,;i"^,;Il""
                      ..:i;,li:`l!iiI,
                      . !i!l">!i:l; !!:
                        `,I,^,:I,<; ;;"
                      :-~i':<<i:~ll~>:>_<+"++_l>~+~!!<:>:><i<~i><ll!:~i,i~<!>!"iI!!i,':>l!:llil"i,>li:lii>!l
                      ;~~+ii::",;",::^^;::`",I^,::;",;^:^::I;I!;;":,^:I";I<;l>^!;I!l^.,l;;:l>_l,l^I;:^,:Il;"
                      :l><l;
                      !~l!!><"ll!>i!;
                      ;:"l;Ii'::";;;,
                      i]+~-l!_.i+i-l;,-i<<>I ..       '-+!I;><,:+<-i>;ili!;!:i:<>l,!!!!li"ll!II<;Il!l;!liII.
                      `:^","^,'^,",.'',"`^," .........'~~~i_]~<,I;;II,l,;;;:";,;lI;!l!!Il";l!Ii<,;lilIi!!!l'
                                                      .liI;i<l;
                      <?+++l<~.i_>+il"~!><~`          .l^;;l^,:^II;,;l:`!;+!I:;I;:,Ii"^:lI;l:`:::::I^"::,"I^
                      :l:::::I',I,;^^.:;,:!^...'......^~i+~-i<<;<>!i~>_!+!<<i:<!I!!i~I;ii!li>;<!<~><:;~<!i-"
                                                      `I~~Il~l~>;'~<<>+-il
                  ""  ::""``'``^`^"`.`"'.'''.''''...''.'      .   ''      .'....  .'  .'.. .. '
                 ^__. _]_+~~:~~~-_~<-!+~:+++~_>i~Il-+>~}<~"^~_]<~!i]~:<__<+<-i_>!~I~!<~~i<i,~:+~;i~+>iiil
                      ;!I!-_>l>.;~l!Ii!-]"<>l,~><::~<<:><;!i~~+<!"~i!i!;_<,l~<!!<!>i>:i>!,<<~I"!><-::i>>~
                      I<>i!<i;>_+!~;~><il;:ii<_l<>!<?< :-i+>^i<>>ll<~;+?<+'i}-~~~~++I:!-_li,<~>+l-+l^-<ii
                      I><i!~il>~!i->~i!lll!~<i~;i_i>!lI:lI~>:ii+~>;i~:i_i~l!?+>i>ii>"<__<~l'!~<i"~<~^!>i
                      l<><,!<<II^i^~<;;<>_l_!i<<<<!!' ii_"i_[!I--<~_<+l!<I}+~->i-`;?>?I:'_~iii< +-<l?<!<~?"
                      l+il,?"~_Il_~ii:>l-,
          '"^"""'``''.".`"^^`.''''.'``^'`'  . .'..''   .  .'..' . .   .. .     ''        . ....          ..
          !l1(!]}~(\1{- >,I_;+<i;>~i~lI<~~>~><;,]<li<<<,>>l~++i_l!;>~i<<_<>>i~!^I->>i>~!i:I>>li<i!!!iill+I:i
          ;jZOx]f|{x/j_ ! 'l,!<i;l>!i,!<iiiili,:i>I!<i<l>il;>i,~:!:>?ii:<>i!!+!'.II>l~<!>,:Il;;>i<~i~<>:~` !
          ';,,::^:,:;,, < ^iil<l!";>_,_+";<>!l^il<>>`:~_`l~;;<li<^;i~>+~!i!>:<_]__-~"<_i:]+i<]i:~"_~:      <
                       .+ ^ii?i>;<i<:>~_^-_;;<i~~<~!_:i,_~i;_<!<i,+:~-i,+-<~.     .    . '. . ... ...      ~
                       .> `I:;";!;I:.ll;,;l:;l"";;:::^"`"""',,,,,`I^":;';I";' .                            ~
                       .!';~~_~,[[>_^-{~?<_]_!,-_]-_:-;>+i~<~--~+:<_+:>+<ii-1i~]+![<~<>+l~Ii+~l-~~-_!      <
                        ","^"^`^'``^"^^""^``'`^^:,:,,""^"":"::::""^^"",:::;,,,",;;I;;::"",,,I;Il:,:,"^^^"",:


























```

*Figure from page 30 (2346x3317 px)*


---



4203-E P-106



SECTION 5 AUTOMATIC MODE OPERATION



{5) Pressing the MANUAL INT OFF switch or SEQ. RESTART switch automatically cancels the



manual intervention mode.



Example of Manual Intervention: / ---



Manually _/



shifted a)



__J ,, ,.. --



amount --- ,'



~ b)_,'



~ - ~ - Manuar intervention



activated point



Programmed path



Cl ::---__


# M---~\

c--{,,r----/.



/ Total of manually



shifted amounts



programmed path



a) ---·-



SEQ.RESTART not pressed after manual



axis feed



b) - - • - - - - - - - -



SEQ.RESTART pressed after manual axis



feed



a) SEQ.RESTART not pressed after manual



axis feed



b) SEQ.RESTART pressed after manual axis



feed



c) SEQ.RESTART not pressed after manual



axis feed



[Supplement] During manual intervention mode, automatic return of miscellaneous functions is not



made. This permits the change of spindle speed or tools during this mode.



IACAUTIONI : Even when tool offset and/or cutter radius compensation data has been changed for a



newly set tool {manual change), this data does not become effective at the point when the



return to the originally located position is completed.


```text


                                                                                                ^``''" ^'.'`.
                                                                  .''.''...   .  '.   ..       :]_-_>- i;!~[;
                                                                  l}+<>_+~]I+.-_<_<?{?-~-l+{~+_?^~?+-<-+>~~-I
           .^^^^^``^^`^^^^^^```^^^```````^``^`''''''``''''''''''''''.'''`'''`''^'.''`''.`''`''``.`'.^'``.'``'
           ':::::,^^^":,,""^^^^""",`^^^,,"::"","^^^:,,^^^",::",,::^^"^,:,,,:^":::;,,"""",::::,"",:::::"":::I^
                  :?l  >l!i>i!Il>!,_>>~ll<^'<<I,<>>^IIi!i^,,:+>l"'~i!>ii>>;^I;l;;`;:;:,:!::I,'":,":I^::"
                  "I: .il_~<++-<++I+<_~+!+<;+<^"I,"'ll!!l";,"<!l;'lil!;i!l":<ii!;:~!!!l<+i~<<:i~>i~_l!i>.
                      .;l<::<"^i>;;!Ii!!^I!i<i
                      .<,;I;,I^'::!;,^";^,:"^,;;l::.        .",:,"
                      'il<i!1[>ii!}]>i<+,!>>l<<i~<!`    '^,'.'
                            <][~i-[[^                  ^:`    ',",          `_'  "``  .``` .'''
                           .+~-[-?'            ^>    ^,.  ',:;::^`           '  !-<li+i++<+;!<l!i>i>I<+l:i!Ii!
                           .]_+__+>           '`l,'^,:  `;;".                   _[-~]]~`^``.^"^"",,:^,:"`,:";,
                           .<i>~~><,"^":,"^'<l^. . l:  :l'                  ^i. ... .
                                         '^"><' .`:i>Il+I^^`'"'`^`'''`^''   .,  ;l::i<!!!!l";III;,,i:`::,,:^::'
                                          .'`i+<!::`.. ,}[]~]?:-~+!++_]-~.      [[]l;!I;;l:"!l!li:I>!^l>l!i:i!^
                                      ',:"I!^   ^`     :]++~-~[!~]_]I           "":
                                           ':` ~i!~+~_<~+_+l_?+:;;,"^^^^.
                                            .:,i!<]_+_<i>~ii_->,

                                           .I.   .,^``..
                                           '?`   ll.'^^"":
                                           `-;^^^>:`'    :^                 ,+  ~->!<~>><+<,i>Ii<><<:_~l,iili!
                                         ':",-`..:>``'`^^^!                  `  _?<>-_l.... ''.'`^`'.^`' ```"'
                                       .":. ^^`'`^^'''. ."i'                ;> .++<l-[~>><i"!>!l>:!+l,iilIl"ll'
                                  ':,,"i" ':"..''''``^:i+lI: ...     .      .^ .---".^`''`..^""^"'^"^.^:"""`,".
                                  ^+   :+!!,'.      ','`<~]-^?"<~~~!~-<     "l .<<i;<>!ii!l^lI"IllI;^<!,^:l";"
                               ."^,>,:i;:. .^"^^'.`:^' "?-]][I~-~~i~-!`     `: .]?~_[{i"::^';:,;I;I;^ll:^;l,l,
                                .. '?``;' ":",:I!i+<i>;i_~;l!,l!!!l;;I^.        ^`'.^^.
                                    .   :,_-+|[??_<+?i<[[-^

                 ><;I;I;;;;lI   .I,"::"`,,:",:'":,""::,""',"":' "`"`^","'^""'^.`"'^^''""^``'''`^`'^`'`.'..'`
                .><>+<!i;<iii   '<>><__:__<i+<,i__l_-<>~!:i><_!^+i~!>++~"!+_i>,il;>_<>+++<+><<,+~i++~_!!<"~_`
                                .!>__> ^+i+:<~>!<_,-<l;+>+<[i;~;?~i~]!:-<+<i;!,+>+~,_i><_;_~<,>!i[:
           :":":^^,^"`"..,"`'..'''`'``.  ..```^''.'.`^^'``^^.''':^`'.''^'```'` .'`^`^"'':'`^^'^^'``  '.'''..
          ,_-n_<{]~f1/{^;i^]i<+:i]~-iI~+<;][+-I+!~~<:!>[-<:<~<!~;<~<~<>i>+_>i,+~<;~<<!~>i>,~~~>i>ili!;i,"^^;`
          `1OUQ[(t-|/j|`l: Ili<;,i!il:i!lli!!i;l!i!i"!ll-!"!<i>I:!!l<i!!<>!lI:<><>!i~:ii~i:iI>!__<:li`!..  ,^
           ^'.'"''^'"`" !, :>>>_^<~:>ii^iI>li<i^il<!-~;'>!>"<_+,!i<~.:i:;_<!>i<"<?->+<<"-I-<<;~~!ll_i?!;?],;"
                        l" <_>>>:~:>+!"~i_l~[_">>~?~+l_~>-~>,>ll>>>~__+~;                                  !,
                        ^I:II;:,"::;llII;!:;;i;Ill;;:;lI!!!l;I;;l!i<>>!!;""::::"^"^^,,,,,"^^^^"::::::,^^^^"!`
                                                                                    ......    .............









































```

*Figure from page 31 (2346x3317 px)*


---



4203-E P-107



SECTION 5 AUTOMATIC MODE OPERATION


## 15. Inserting Pulse Handle Operations

On a machining center, it is sometimes required to feed the Z-axis manually while positioning of the X- and



Y-axis is made as programmed. Or when machining a cast workpiece on which stock removal amount



varies greatly, itis necessary to adjus1thedepth of cut manually. In such operations, axis motion controlled



by the pulse handle can be inserted to the programmed axis movements.



Operation to insert axis movement by the pulse handle is explained below:



{1) Press the PULSE HANDLE SHIFT key on the machine operation panel to turn it on.



(2) Set the AXIS SELECT selector on the pulse handle operation panel to the axis which is to be



moved. Also select the multiplication factor.



(3) Feed the axis by turning the pulse handle.



The amount fed by the pulse handle is shown in the MANUAL SHIFT TOTAL line. Automatic return



is not made for the amount fed by the pulse handle. If it is then necessary to return the axis by



turning the pulse handle while observing the MANUAL SHIFT TOTAL data on the display screen.



[Supplement] 1. The MANUAL SHIFT ACTUL data is cleared ("0") when the MANUAL INT. ON key



ts pressed.


## 2. The MANUAL SHIFT TOTAL data is cleared ("O") when the POWER ON switch is

pressed.



It is also cleared when the RESET switch is pressed when parametric data (bit 2 of



NC optional parameter (bit) No. 4) is so set.


## 3. Axis travel amount using the pulse handle is added to the axis position data which is

used for judging travel end.


## 4. While the PULSE HANDLE SHIFT key is off, the pulse handle is inoperative.


## 16. Lock Functions

16-1. Machine Lock



When the MACHINE LOCK switch on the machine operation is switched ON, the machine lock function is



turned on. In this state, actual position values on the screen are updated as the program is executed while



the machine is stopped.



[Supplement]



MACHINE



LOCK



Press the MACHINE LOCK switch while



holding the INTERLOCK RELEASE key.



When the machine lock function is turned on or off, the NC is reset.


```text


                                                                                               '^``'^'.".'`^
                                                                  ''..'... .  . '..  .'.       +?+-i-;"_">+!
                                                                  ?1<>~-~?><I,?>++~]]_~_~I{?+_{l:+<?~--_~<-~
           ^""^''``^^^^^^^````^`^^``````^^^^^``'`'`'''''''''''''''''''.''..'..'`.'''`. .'.`'''`''`.'`'``'`'`
           ^^^"""""'`^^^^^'''^^:^^"`'`':"^"""^``":,^`^``^`''`^","::::III;:::,::,;IIII;,:,;III;,::;I;;;;;:::,
           i-1,    ?->+~<>[-<i>'|?l__i~'_]<i!i--<`l?>l!!I!~+!IlIi
           ;>?i.   _?_1{}>][+|x"-i{[{{|:_]))-1({fI<}/\(|-||)11?{f"
                 '.
                `~-I~l~__<<<<_<!->?-"!l+I-<i-}_>_>:<<~<>~><!i-<+<~~;>;+i>:!i<;l_<Il_>>l!!i_+!ilil;!iilli'<I>`
                .<,><<"~,!!i_i;+II!i>l>ii<<~!'>+:i+~<!I><i<i!<iIl,!i>I<~!i!<<;<I>i:+<!<il+><+,!>+!Ii>l!!;i!<.
                .l!~><,~l!__!il~;<ii[>~!il<>l"i>:>~>ilI<?<!~il~i>Ii<~!l!!l~i<>i"!;,+>!>::>!>>^>!!i!<i;~l>>ii.
                `>+i~!i_i+~+Ili!l<<i<~~<il!"<?_<_;I<:<_~~"!!Ii!,>+!!~<~ llIiii,<<+!_-<i+">+<li++-<il>~>i<[_<.
                "+!l_<:+<~<;<+<<]<"<_;I_I!~-~+-<l_"?-!!_i_><~><>+!l?_iI+<i~_i~i?<
                .,"''`""^'"''^'`^`'`^.``''`^`'^^''`^''^``:^"'''^^''^`'.'^``^`^'^`
                ^+__<~-~>,_ll~_~<l_<~:<<~+->~~<l?>i-~;_i~?l<_~~-~I~;+-]]-<__I+?~~_`
                  .   .'       ..   .        .  .. ..
                 `i~^ ~~~_-l~-><_+-<|<:???]?+[l_-_[>li_-Il_;-_il~_~+i~i;+_~<-~~l!+~~_l~;~i~,~:<I.
                         ..   .  .. .   ... .          `. .  '. .'..... ^'''`'. ```'` '.`'' ' `.
                 `?[' !-~:>~I!~+-ll}_:?<lI^~~~!<>,"!"+>,:li>I:!~!>~;;>i!l+!l^!<i!lll,+i,l!l,;>lli^l,!";i^
                 ."". I+>l>+l'_~<l;~<>~ii!l!~i_+~!l~i>>l+<+<l'";":;"^I;,:I::^!!;I:,;";l"llI":l;l;`I"I",i^
                      ^;:;lI` IIl,,llll::Il`:;l<lIl>il"`il!!,
                 .Il  ;:""^":,.^^"^".'`^^^'',". ''^'.'``'".
                 `~<. ;;><!;i<^<i>:~>"<!!<<!><!l>i~+^!+>i-<
                      ^iI^";,",,":;";:`;,`",::"":,^II`"'I"",:^,^l:^IlII;^I,.l;;l;^,;:;I"':^^ ^"^"^^^,`'^,`^`
                      :!~i~<i<~+l>-i<?!l~>~<<?~!+->_+i+l_><_<;~;+_<~~<_+>+<"?<~i:":ii!~<"_>~'l_<~~<--i;~-+<;
                      >l"!~^l<<+I"~^I+<`~i>i>>;i~!:~"><>^~l>~:I~>!_~. <:l:!!<i!'l_i~>><<>'+"I~>lI`~>!^_ii^>i
                      iii-~-l>+Ii<<-~l+_i[[;<+_[I!_+->!__+>-~l[--?+i]l:{+?->"<+~~?>"-~-!!~I+~i;[~>++Il_<~<~,
                       .   ^'.`'^``^^ .'.'` ''.`''''``'``;.``.^'..`.`' ^.'    `` '` "^,`.^ `^^.:I;"I"^,^::^
                I}<_+~+>>~i_^   ,:  :+iI<-<~>I~~.~<>_iI;~I<!<""<<<,i^>i!l!i;!>l^!ili^i;:i<i>!:iI ;!I':!!,;;"
                `"^;:""^^:^:'   .`  :!l>>+<<<>,;`,,,:'`^;,^";^"ll!"l"ll!;ll:,l""!ll!"lIIIi;!llll^;!;';!!;i<l
                                    ,;,;Il!i!:
                                "^  `:^'",","',: ,:"::^`,":,, '"^`'`.^`'''`'`^^..^''.``.'"`^`^^^.``.  .....
                                ll  ^<~>>-___<~-^<-<+;;^>ii>?"!}]-I+:---~+-!l~!:~-+-l~__;~~+-?-_l+-!i_--~I<<
                                    !<>~~i>:
                                    "^`'""`'''...''.'...`..`^````^   '...          .
                                    !!_l-_~,~__<>-!+><~;-~<l]+~}<l;+_-~ili>+<++?-i--+_I~_+_~+-_+;_[-~i?<i>>>
                                    <?<,+][+i+~l_~><>_-~^_++:_+:^]:+;i>:+?I...'''.' ''.`''`.'`''.'^```^''''.
                                     .  ^"'' ^'`^``''^`^ "`^.'^. ".`.``."".
                                !I  liilIllli,!lI;;l,:!Il:ilII:>i;ii!I>I,::ii!!!l:!!I;!!I:II!i;:">ii,Ii;I:;"
                                ^^  ;<~<i~+l>!-~~<i<i~+><+i+;l;ll;:!I;lI,;;!Il!;I::llI>!li!!i!l:,<><;ill!:!;
                                    ,lIl:,l.lli_l+IIlll:^!lI
                                "`  ",^`^."^."^^'^;''^""""'"':,,:,`^`'.`.',.^`'.'.'''`'''^.'..'.....'..
                                !;  i_ii+;<+lli+!<];!~_+__>]"-+~~I"<-?,~;<?^>~<l-i~_;<?<~[>!~;~<+-<+]<_:

          .l!l    ""',^;; ~I'^"^:I,^"^^.
          .]|/^   l([/((f"/~|}{|)/|\11xI
              .    .                  .
          '<1li:  ?1[]~+~+-:i<+_<
           .'. .^",":,:^^:I";;:::^'.`^^`...'.. ..'.  .  '.        .            ...
                i?~-<:-+!~_-~<i<?+:!><~~:___<!;_!++>;i~<__<<,_~-!-<<;!l!~__><+iI~]"i~<;i<~~>><,i>_;>!;++<,>:
                ll:!~<:>, >:~~l;><+;^__<<+!i<_]>i:>-<~+I>!>-~l~i<++;>~iIii_+-~!<<<?>l<i<_+<>!>I<<~l~_>>>~i+:
                <-!I+<>>>li;>;+><+~~i:","^"^""""`'",,:,^,^^":`:",::';:"";:;II:"I;,;;:I:!i;;"":,;;I;IlI";;:l^
                :Il^;!!,IIl^l^!I><li;
                                                    ,,^"',^^;","^::.`",^'^"^''"`^
                                                    ~_{}~+1_?[][-}-<?--[<]{[[-]-_.
                                               .``:li><!~ii<:>i>>il>>!l+~+<>_i!_>.
                                          '` `,"`"l.
                                  ]\l;~<!+;:t]:,<+:"
                                 .j<>_[1:^I]X!``"^'~'
                                 '" l--> ';i!1-[>[ii'
                                 `>-}<]--,I+^.i-], <'
                                 .!!!I!~+i,;iI;;;:;!.

                <]i~+_<i~<<-   .--~+i:i<:l<+<~ii;l!<Ii>!!+!!"l:<Il!iI;i^!",-I"i!,<>:;I"!l!i
                ",,;;",`:"";    """;"'^:^^:I:,,:"";;""l:;;;,`:^I:"II"::`l^"l,^;!^Il^:I"!!i!.

















```

*Figure from page 32 (2346x3317 px)*


---



4203-E P-108



SECTION 5 AUTOMATIC MODE OPERATION



16-2. Cancellation of Axis Command



When the AXIS COM. CANCEL switch on the machine operation panel is switched ON, the axis command



cancel function is turned on and the commands of the axis set for the corresponding parameter are ignored



to disable movement of that axis. The axis for which the commands are ignored is set for NC optional



parameter (bit) No. 7.



[Supplement] With the home position return command given by an external signal, the axis set to be



ignored is also moved according to the command.



16-3. S, T, and M Function Lock



When the STM LOCK switch on the machine operation panel is switched ON, the STM lock function is



turned on. In this state, the miscellaneous function operation specified by the S, T, and M codes is not



executed, and only axis feed is executed.



[Supplement]


## 17. Dry Run


## 1. Override or dry function is also effective as in normal cutting operation.


## 2. The axis specified by the axis command cancel function may be moved by manual

or manual intervention operation.


## 3. Spindle operatron control is not executed.


## 4. With the home position return command given by an external signal, the axis setto

be ignored is also moved according to the command.


## 5. WhHe the STM lock function is active, manual operation of S, T and M functions is

possible by manual intervention operation.



Dry run is a function for running the machine at the feedrate set by the cutting feedrate rotary switch on the



machine operation panel, while disregarding the programmed feedrates in G01, G02, G03 and other



similar modes.



DRY



RUN



Press the DRY RUN switch while



holding the INTERLOCK RELEASE key.



1--J,Nv (Inch/min) JOO



(nm/min) SPEED



11 40



~ J00 2000 ao



8 200



4000 1so



4100 6000 240



250

0. 0'1 1 0000 400



In the rapid feed (GOO) mode, the data set at bit 2 of NC optional parameter (bit) No. 2 determines whether



the dry run is effective or not.



Switching the DRY RUN switch on/off is possible even while commands in a block are being executed.



When changed over, the machine is immediately set to the state selected.



S, T and M functions are executed as usual when the DRY RUN switch is on.



The dry run functfon is effective while the machine lock function is active.



[Supplement] Be careful when activating this dry run function since it is effective during a G74 and G84



tapping cycle, or during the G31 skip function.


```text


                                                                                                ^^^^'^ "''`^`
                                                                  .''.'`... .    `... ...   .  ^]]_]!+ +!!~}<
                                                                  :1]>>++_{;?`<_>_<]{?_<_!<1+--]">++-_--++<?!
            ^^`^^^^^^^^``````^^^^`^`````````'''''''``'''.'''''''''''''. .'''''.'' '''''.''.''''`'`'.`.`'.'`''
           .^'^^":::,"^``````^""","^"`^",:,,^^"```^",;;:,:;;;;;;;;;;;;::,:IIII:,,::,;IIII;,,::;IIII;,:::;;;I"
           .!_Il!  `~!>!l!<<>+!l!`i!"+IiI">;l!;lli;;!
            ,i:;;   ;;<:l!!I<ill;^!""!!!!`lIilI;!+;!i
                 :~i:;';,",;:;;,;l>I.::IlIII `::::^`,,!:^":,::":^^",":I""`,"":""`"";,,"":,I:';^``^"'``"^^^^^"
                 :~i~~l~<<!+>>i!>>_<,<>~_i<<l<_<<~l>+!~~!;~?_<!~I>+<!--<ii_~i_Iil<~++i_~i!~~:~~!~~_l!><>!_~>~
                 :>_<i>l~!!~<!">i>!l~~IiIl<!ll<iliiiI!~;_!;>i<>;+>!I-!;>^!i!:!Il>~>lIi~!<<><!>!~_~"+<li<!li<i
                 !>.-~>+>i,>ll>i;<<i"+l[~]:_~-: i-_;!__!!_:;+>~-:-_<,<i~~<_<<],i~~I?<><~]i+:<_li<,~[<:???~i+>
                 l~>+_~_-_,<~_I_+l:~'^.`^"'"^"`  '"`^,"^.,.`,^,"'"""',"^,";"";`,,,'<:,:::`:`;;^`:.";"`!lII,I:
                 ::::;^I;l.::I^:!` `
                 "!^^";""":"l    "!;:^l:^,,::"`"^:;""'","^^'^^""""""^^"`^`^`.^^'^^"^``^'`'``'."'.''`.'``''''.
                 !~i<++<!<~!?^   I~~i;>+ll~~<<>+>+~<<,i~_<l;>><<>-~~I-_<~;!_:+>:++[~l?~l?[<]!,++;__+;<]>>>;-!
                                 !?i><+iI>,-+i:>i>>_!!+l<>++<_I>:_~;!+~~~<->+
                                  .             .... ...... .".' .'......''.'
           `>?:<l  "[^^?.i>!_;--l-;i!!<!i:I:!I<,
           .,!"I:  .!^ : !!:i.!!^^I;Ill!l^,l!!i"
                 I<!,;'!!"^il<;',i;I"'::::^ ".";:`;::I;::'",;,:l""`,,",:^^`,,;,:""`,;; ;,'`;;;"^^"`^"^`:^^'^'
                 !>i~<;i+>"~!<~!ii<<i!<?~>;I~,!~<:i~+i><+,<_-i~_i!!_->+!;i;++?<>+<"i~+^-<>I~l_i!_~l,?>i->+:~!
                 !!:!<<`iI ">`>><^+>_> <!I:<~i<>><i>Ii>:~i<>!<";_~>i]>!`!-_>~-~>I-il~<,?`;;"+>!>["~~~+>`~`<~l
                 !~_+!~-+;;_l>;<<~:?<~!_~~><Ii<++i_~-;         ..       .' .  .. .'  . ..  ..'. ..'..'. ' .'.
                 ...    .  . ''`'^."`' ... ..''^''``'
                 >[<<+_+<~~>_    :^  i~>~!<_l:!^_i,!li<+il:>,_<!">]<l_i<,<i:i^Il!liI:;<~I!"llili>Il'
                 ^,,:;",^,:";     .  ``^,'^,^'` ,,''"",,"`',';;,.:":",,;`I,`" ","";^^;II"~^I!!:!l;:.
                                 i^  !!I`IIl^;;;,;iI;::^i:^";;`^::;;;;,:^,:,,;,":";:,'^,,',,'^^``,,;:`",,"^:^
                                 ;^  ;l<i+_>l_+~_>~~>i?l>il>+~ii~>l!i<!!:iiIi!"!>!>>i,l<+!l~;I!ii~ii_;;><li_:
                                     !;"i+iI~<:i+~;i!><i,,~+~!_i!;
                                 ^.  `..  '             . .           .
                                 _:  _-+<_[!!]_~_{~-;i+~?>~I_:+?I_+-_>[__"
                                     .'. .  ..        .                .
                                 +,  +_-I!+<:i<i~lli+->>l,<_ii;!<<>><+<<i~i_ll+:i<^<_-~>_~i_+!_"i?+I_<~;__>_"
                                    '_+;+~>~>+i<I~?_ll+>!<+I+ii><-~<!+l<]+;<!>+>+~<<`^`'"``,;'"''^"`,^"`,"`".
                                     "".I:"^^:.".^::'',"":"'::":^:"!,:`^,:',","^;,:"
                                 <`  i!Il,"I;`>i<!`,;::;,^!::','::l^: ^,,,",,`,,",I,,^"II:`l`:,,I;;:,"l,,,^,'
                                 I`  >>!<_i><l>I~~I<<>l_~i~<<l+l_i~i~:!~_<!>I;~<i>-il:llI!`::~lliiI~!!_>i~I<"
                                    '<!i!+__,<i"!<<li~"i_~:><<+~I"~<<~?<>!

           I[[>. . -j1?[^rt]]1,
           .""`.   "l:l+ :;!lI'
                 :,' .' ^ .^ .`^^^^"`''``^'.""''`''^`''.```''`''^'`...'`. `'...'`. ''..'.. ...   . ...   ..
                 ><~:~~:~l<><i<<<iI~l,><>i>-<-~I>~~i!<~I_li<;~_~~<_>l+~!+i>+i;i<?>]>?_~+~?i,i--_;<_-~i,<;l<<^
                 !!+!i<<"^~><>?><:I~+>?`"?~_~'__~+~+<<~<i,~<"i<!_~+i><~~!l_~+<_-~Il<`+-~:._-?<'_]-~"_><^<-!<'
                .><_?+;:>i-_~,'''.``'.'..`.'`.````,"```^:.'^."^`;^"'``^^'."""^"""`.^.^"`' ^""" ^,"^':^".:"",
                 :""::'.",,::'
                                        :l:;^"l^,l;^!:l"::;:`I;l         ..  '. ...   .
                                        ,]?)?+?]_~]+1{[_}[+]?-]{+~;!i,  '<~i'I-[+-+;'|)!'
                                  .'^^:i:!;lI!:lI,;Il;I;:;,;l:lliiI!<l        ^-[>l `iIi'
                             ''".^:,^"!'                                 ";!->i~)__-[;:"
                      <z+l<]!><`xv;";]:l"                              .^;"~\>~l,;Ii[i:<,;,
                      ?<:]-}> i,rl!^!"^,i                              ',I!u]t-i>i>_`j"^.'.
                      ; I_]-^.;::"+"Il"^!                               `;>t -<ii>+_lxI!"":
                      >_)~]]{!l:<:I:,!,:i                               '>_{)`^,:IlI\<:;"^"
                      ^;;;I;II, ,:,::"";.                                'l:I`     ^!i!`<.
                ."':^`'''^`^'`.`"^"^.`'.^..,'.```..'`.''`'`.`^^`...'...'      ... '   .  '..   .      .  .
                `_;~+<I-+_!~_-i!_+_+;<ii?!:[~l+?]>>-~i_!_><l~i[~;__++_-~<-_-_~_]~,][_l?_"~l]_?~>++_?!+->-?+<.
                `_~;l]i,!<"+:i-_i+i~:!,;~_'                             .         . .  .          .... .. ..
                .,`^^^"'''`^'"^,"^""`,..^^...    '.      .
                '-~--><>+;>~;l_~<^<~<]:>><~~^:_<>_,~"<>~~++_^<!-!,_i+-^!><<i<+l+;!!l!i~<~!I-~:~+<~<I_~~i+_~l
                `--><l"_+-!<+~;!!~::-<:i~<~_<+:ili><~-+_]_+;l~<ii;]>:<__-:><-+<+<!.''''``''^`.`^'^:'^^^^^^^'
                 ^'":..^^,"l,^'"^"'.`"''^"^^^".^'`"`^,"::;:'":^`:`::^:II;'::::";:^
                `?`!,~<<l]i!!i<~>!>:~<:>><>l~~~:+!^<i!_"<>><"+~l;<_~,>?;_;l<>>>,lI:<"
                 ,`  ^''.'.`^'`^`'`.^'`^`"^`^^^'"``"^", ^`"^ ^^`.^`' '^^^'^,^"".^"`,'
                .<~]:?~;I+il~~>+<+;>l<{?<~<_;<_<-;_<<I>_<<i~+I+~_;_<>-_<;i!;~~>+l
                             .. ..      .  .  . .   .  '.  .. '.. .. .'.  ..'..'.
                ^]->~<~<i+>]i   "[>:>!i+!l>~<<">l<l>_l!I~l;;>I,l;Illl!!I:i<liIi!ll__l!!i;il!!l;!liii:>lii~~i
                .^^""^^`'"`"^   ,_<!_<>I<l+~;I!I~!><~l]~Ii_~i!>+!;+ii+~>;;:";"",:,:;:,,;":::"llI";","l:;,ll:
                                ^><>iI~:ii!i`"!'i!;;_lli,;<!^"><~"<!!>ii:













```

*Figure from page 33 (2346x3317 px)*


---



4203-E P-109



SECTION 5 AUTOMATIC MODE OPERATION


## 18. Library Program Registration

This is the function necessary for executing such items as a subprogram and a G code macro through the



MDI operation or for operating the program which contains subprogram call commands in the large



capacity mode operation after specifying the S option. That is, the registration of subprograms is possible



with this library program registration function. Such a registration is usually made when the PROGRAM



SELECT function key is pressed.



The operating procedure is shown below:



(1) Press AUTO.



~------------.-



(2) Press function ke [F8 XTEND).



(3) Press function ke F1 (LIBRARY P.SET}.



Fig. 5-11 Registering Library Programs



(1) Press the AUTO key.



(2) Press function key [F8] (EXTEND).



The function messages will change as shown above. (The message "LIBRARY P.SET" appears



above F1 .)



(3) Press function key [F1] (LIBRARY P.SET).



"LP" is displayed on the 21st line on the display screen.


```text


                                                                                               '^^^'^' ".'^^
                                                                  '''.''.'  . . ''.. .'..  ... <]--<~I'_:<-['
                                                                  +{~<i<~]~ii`]i<++}}--++;[?__[<,__}_-?<<<_?'
           `^^^^^^^^^^^``^````^^^``````^^`^^^`'''```''''''''''''''''''..'''''''`. ''''..`''''''`'`.'`.''.```
           `^'"::::",^^`''``",^^^^^``'`"":"^""^``^",^`'",":;;;;;;;;;;:::,;IIIII;;:::,;II;I;:,;,:IIII;::::;;;.
           l+|I    _^[[<<_>i;:\~i>!>i>><>.}[>!!<<<<Ii__lI!`
           ,~1<.   -_[1]_|+1-:->-}|v-})[["-[|(z1)(1_/|()1}l .
                 `'
                 <>-!<l+_<>_<~-ii;~-_-__-i!<+I>~_<i>>_!><<<,_<>~:il;ll>]~ii_<<<:i>il!I_;i!-l;i<!i;>~lll_!I<>'
                `?~-;,+!>!~<!;"<'li":<<~i]~lI;_<"I>i<~-<;;~ii+:;l!<<<li,~><_ii>l<>::<>;l<>~il<<_>,<,><>~<ll+'
                '>ii;I[~!<~>+:,>,!<I;~!<++l>>;>~l!>![~~!!:~>~>;^_~>-~!;;<<><I>[><~,;i<"i>i!!<~l+<^>`Iii`_~?+'
                'l_?<~>+,<i>+II+_<<_!I^~~>:I+~>>]+l_I<<,<;~~<i! ;li<;+'~il:~-~<l~_ii"iI<!>~;l+i~I+:+I<>-~__>'
                .~~_^+!<l?!>i!:>l<+<<l"~+<+!~->>"~><__<> :{<<~,<;<_-_<~-<>,-;i+!~-<"~_-}Ii]<_>!_+I_--++?]+][`
                ']?<<[<<;~<_~]~<I?-!l>l~__+~~<''..'.''''  '`'..`.`:^`'```'.^.^^^^`".'"""'`^^"''`"'..``^"`^""
                .:"`^^'  '"^^"^`.",".^""",,,"^
                .<>_:<+-<?]i~I+iiii+>+;!II<!i~>:~-~<~'
                 ..^'^"^`^^`;""`^^^^""``^^^^""`'",^",
                                                                           '<i~~_?!~~~+l
                      ...............................        .            '!",^^:;:",^""
                     ":"```^``````^```^^`````````^```````````^`'`^^``^^^^^!;.^"^`'`^````^"^^^^^";^
                     ". ^```^^^^^^`'````````^^`^^"""^^^``````"^```^^^^``'.i^''`''`  '''^'.'`^"^ ::
                     ;..!.:;:::;;;::::                       .     ...":![-!++l{_;{[;<]!<-<:"`i ,,
                     l'.I ,lI;:;;;;;;,^^",,,,""::::;,",,""""""",::'   "l!}~>+<!_~I-_l<_!<_<i^ ! ,,
                     I..I I'',l``````````^^^^^^^^^^^^^^"^^^^^^i^`^;   :!`!^```^''`.'``'`''`<, ! ,"
                     I. , I  ';                               !  ."   ,_{1[(?[-}[{{-1+}~}_i-` i :"
                     : 'I :  `I                               !  `,   `><~i+i~~~--[]-?]~?<i_" l :"
                     ^ 'I ^  ':                               :  ^:   "<i+<+<l-i+___Ii~>_1{[^ ; ,^
                     ; 'I ,  '"                               l  ^;   :?_)<+_i[]+[~-[)?{{11]` I :^
                     l 'I i  ^:                               !  "I   :?~<<<_~]-<_<?_]-~[+~]' ; :^
                     I 'I l  ^:                               l  '^   :???-_]-(-??-{<-?+)_+{^ : :`
                     I 'I l  ^:                               i  `"   ;~!!<?<i~lIi!~;li,_~>?^ I :^
                     l 'I l  ^:                              .!  ",   "<^Ii`"`!liil<i!!^^+>-^ I ;`
                     ; ^i I  `:                              .;  :;   ;{1]]{!^-~~-~]++?",][-`.I I`
                     l ^l ;  '`                               ;  ;I   I\r{(v!^~<<+<-~+1",>--.'I l`
                     l `; !`^":"^^^^^^,"^^^^^^^^^^^^^^^^^^^",:I^'I;   I)[<<{;,+i>~<-~+?""++-.'l I`
                     ; `; !i>i!l!ii!iiii>i!!i>ii!!ll!!i<<iiiii!><+^   ;)}~-1:^+>lI>~<!i"l-+_ 'I l`
                     I `; l ;]<;<-!i_?I>?~:i[ll_?;;{>:<-;!]?I+~l :"   l>;,;I"^,,,:","":"",:> ., I`
                     I ^l.;:;!l;!_lIIlIIll;!!I;Il;l!il;;:>~I;;;:":`.. ;I,,,,;I,::::::::::::!'`: l'
                     I  ^`'`''''I;''.'''''''''''''''^"^';I''`'''````..''````````''`````","``^"' l'
                     :"^^^^^^^^^i,^""^^^^^^^^^^^^^^^^^`i<::",""^^^^^^^^"'^^^^^^^",^^^^^``","^^^^l.
                               .l                     :: .                      ................
                               ^:                    ::
                               I'                   I,
                               l                   ;`
                              ^;                  ;;>,!l!l:!IlI;,!I,!<;i!li>i<,
                              ;^`^'^''.`''`'..' ':l;+<++__!++_>i;i>l!>>~<i!>>~l
                              I"+-i~-]~-----><[<+<-+>+[?++lli-~i:
                               .      .      . . .''.   . ....''.

                                             li!'l,"I !>lll!lll;:,lIII,:>:,::;:I'
                                             ,:_^;:^: :!<_i>iil+!Iiii>i,II<-!<l~^

                 "!I  ~iii!,!i:i>!ii;>l!^      .
                 ^^"  ``:;;`^;^^;"`,`:I!'
                 `!,  i;,""^;^:;:"`":".Ili^;;IIi>!!I`
                 ,~l .;:li!`!;ll!!^:i<^i:_,i;;;l!i<l"
                      !l;':l,:i:" Ill;l;I;:'l>',:::;l":l`l!:Il,"i;,;: ;!II`::;;::::';,iilI!!,";;>;l"^;,,,,,`
                      !~<;!<~+ii;';!i!!>+iI^>i`I;i!++,I<^ilIi>,;~!l!!.lI!<^Il>>>~_>.l!~>iiii:";l?!;';]_~~+>l
                      ~_l!>";;.,.
                 .^'  ^ .  .  .''..'.. ^^'.'."^`'`^''^'^`^.
                 ;]< .<I+-+:<~>+_<I!+-,?;>;~i{[+~-_!;<>1~li
                      "';``'',``"''``'^.`^``,`''^'  . ^`. ,''`. ...'..
                      !<i`iiI?_+-]_-!I<:>~i!~<_I-<i;+:~?<;?][+[!i_<?_~:



















```

*Figure from page 34 (2346x3317 px)*


---



4203-E P-11O



SECTION 5 AUTOMATIC MODE OPERATION



Operating procedure for library program registration:



(1) Library Program Directory Display



Press function key [F1] (LIBRARY P.SET), key in "LP



L..J "



and then press the WRITE key.



The screen displays the library program directory and the remaining capacity in the number of



bytes.


#### AUTO OPERATION


#### LIBRARY PROORAM


#### NALE SIZE

0100 86



0100 10



=LP



=LP 0100,A.SUB



=LP


#### A.MIN 0100 3

97/07/15 14:10:00



lll1l



FREE



1904


#### MESSAGE

[EXTEND]



Fig. 5-12 Library Program Directory Display



When library program directory is displayed on two pages, use the BS or WRITE key to change the



display screen.



(2) Library Program Registration



Press function key [F1] (LIBRARY P.SET) and key in program name and file name as follows:



LP w program name, file name [WRITE]



The library program can now be registered.



When a file name is omitted, subprograms rn all the SSB files are registered when the entered



program name is "O****"·



When a program name is omitted, all the subprograms in the file specified following the comma (,)



are registered as library programs.



Up to 65 subprograms can be registered.



Note that a main program cannot be registered as a library program.



(3) Deleting Library Program



Press function key [F1] {LIBRARY P.SET) and key in the program name as follows:



LPL..J program name;C [WRITE]



With the operation above, the programs registered as library programs are deleted.


```text


                                                                                               '"^^``` ,.'`^
                                                                  ''.'`'.'... . ''....'.. .... !]-]~_<'?,li+'
                                                                  -[<<i~>]~!>`]i!><}]?_~~;{?_-[!:++-+??~<<-_.
           ^^^`'^``^^^^^^^^````^^^^^^``````````````'''`````''''.'.''''..'.''''.`..'''''.'.''''``'` .''''.`''
           ",,"",^``"""""""`^^^"""","^"`^^^,:","","^"^,,,,,^^^"::,;;;;;;;;;::::,:;II;II;:::,:;I;I;:,;::IIIII.
                .<<>>!+<!IIi!!!ilIi;~I,~!!iI,!;!!l!l"lIii!l<!l,
                .,;:::;":I,,:,::,":':,.;,;;;,l"l!:;"^I<~!lli!l,.
                  ,I. `:!,I;`!I,:::;,,l,:,;,:'l;::;:`
                 .Il^ ^;!:!i::,;>!!!:"I;!l!l>,:I~>i+;
                      ;<I!l,l,Ilill,il"Ii:;,;!_~!><!"iI>-i>':!!"l:,:i:''""!:I!>ll^;;;I,Il:">i<Iii,;:"
                      ^^,;I``^^:;I:';I,",^;"I:l;:II".^';l^,^`!>,," ;^.^^ `i;::!!l">I>>:;Il`!!!;;!^<>>
                      ^_II.~!i>i"^~>!i><:;~i'!lI>l'I!IiIli^"_I!iiIl.i!i"~!,.!I;!;I;;."l;;Iil.;`;!l ,"l!ll,^>`
                      ;!>~ll",:,`^:;I:ll"^:;',::lI^l::<;l;^^l;l;l;l'!Il^;I;'!;:>I;;+";>iiil~^I^;!>`Iill!>,^i'
                      I~>><^
                               '''...'...'''.'''''''''`''  .''''''``'...'``'...''''''..
                             .;,IIi>~!i<><ii+l:;II;;::;!!~<!II;:,:;;;;;:,::;!;;,,::;:;;:,
                             I^ ;:--_I_{{}>>1i::,,,,,,"_-)]>:::::::,",:!>!!-1\[l!:I;l[_ ::
                             ;   .':_+_,"+<<i+^                ...... `<?_]-l[><}<]_t(l .;
                             ;.   ^"i!!^`llIl<.                                    .i<  ';
                             l.       :?1+   <!?^                                       'l
                             !.       '"""   ';^                                        ^>
                             l.       !?[}   '\i                                        `>
                             I        ^:;;    ;^                                        `l
                             ;                                                          `I
                             ;                                                          ':
                             !                                                          '"
                             i                                                          `;
                             I                                                          `;
                             l                                                   "+-!   `;
                             !                                                   ':l,   `:
                             !   .``                                              ^_]l  '"
                             i   ;[i"I;""`;l^                                      ..   '^
                            .~   l)<:iiII,i_,                                           '^
                             <   il.              .                                     ^,
                             I  ^;;~~?_;::::"ll<i`^^lI+~,^:l;Ii<:II^"^",I"'``^"i:``^""' ^,
                             l.  i!){<>'     l<-(;",I^{)~'';![}],,;     ,!l:,;:>',:":;" ":
                             `;"`I,<l "^.....:l;i!<!;^<~_l`:I-i::^".... "?-~~?~;'<_!~]~"I.
                               ',llIll`,lII!;',;:;I:^I:,"l:^l;I;I"`!!!Il"'::I;;^";,::;^`
                                >"?_^ili,-[:!!~l-[^~!l>{]`~il>{-^i;;>}_`!i;++>:~l:~}ill
                                IllI:!"lI!~;l,il!~ll,!I!<Il:!Ili;;"!!>~I;:lll;lI;li<l!:
                                        .                                           .
                                           !i~`>:I<`;l<i<!:~i!<>i~;!<i!!<!i"><i!~i^
                                           '`!'"``:.^,::;;"'^:i;;I^"::;;I:l",;lIli^
                      '^'...`..           .                                              ..
                      <[<_>:[+i<iI-<-?~]iI[<_+~++l_;}??+]_-+!_;~-<l-]?-_"l~_l~~i-[<i!i[+->-<>-+l_;<~~<~]l__!
                      >__+_-:~<<_-i.'`.. .. ....' . .'`.''.... .'.'`'"''..''. ''.'.'. '.. ...^"'`'`'^`,:''^`
                      ``,^':.^`'`^.
                 "_! .;<!l>;:<lliI!i,_<!>>>!~ii:
                 `l:  ,;"";I'`^:~";,.^;l>I;:I:;^
                      <i<<>;~l>il>,l~<"_Il,!:_-__~+!I+!]~>!:~>iIii,!:I>!i!i<;,i>l!"ilil->"li!i::<,!!!l!!`
                      '',:"'^`"``^'`,;', ^",`,"`"`'`.'^:,'"^I:,^:l""^;;,<;II"`ll,;^l,I^Il^:!;l::<":;;Ill`
                       ;<l``;_i_-<<i,<_i_:,]<"!~l-l!?_-<+]>
                      ^"' "`^^`""``..`"'^'.`^.'^'^''''''.`^
                      !<+;_[~~<:<<i[<~~,!_<"i<_;<_"<??-_~~+~
                      ^"^``.'';"```:^`.`.```"``'.`'`^"''`'^' .  ..'. .`'`..'                      .
                      +_i_<`<"?-";_~<+^-^i<<]--i^-~--i~}~-<-:ill[,-_+,]-}il__<:-+lI+]_-_++-:-~+-,<?+"+~]~~_~
                     .ili->_<,;_~+>;~`+<!I;;:l,     .  '                       .    ^...... . .. . . '.''.'.
                     .:"":^^'.'"'``'" '`^''''' ..
                      ~-i~!^il<!+i_>;I<i!+,_,>i>~<<`!{!_-I<<~-ii-~~<_<I!~?<l[_:-_-<?++i~-]<_+<~~-~;<i<<<_:l:
                      <<!:<<~_+~-_!+>l{<~<l;<i><>>~<`'..'''`'^..,`''''..'.`.'`.""^`'`^''^^`^`^;'`^'^````"'"'
                      :"^ "I,"""^".:^',^:":',"l;:^^:
                     'l<;+:!],!!i<i!+<~i>I,<~"!>^!<>+_>>+<
                      ^"'`'``.``^,'`I^,```'"".`".^:l""^`"^
                     .?-]_I?-_I>;~]~;<!i_<_~;l-<<!>l+i:~~~--<~_!<<;>;_i-<lI<i~~<~i
                             . .  . .`  " ...'^`''''``.`:"^^``^'^^'`.^'"^^^^`;,""`
                 l}i ^->~~_>~II+<+il<~ii><<!.
                 ^"^ ."^`^^^;''^^"^"..`;l""`             .
                     `+i+~>I~~i-~<:>_~;};~,~!1[??-_!!~<1+~;!-<ii+_:~:_~Il<l<~<~I:<<!<,>>l_-<><i.
                       .,"' ``''`'.'`^'^ ^^^^^^^""`...'^'.'^"^``":'^.`^`"^`;:""''""`,'",'",,,,,
                       !+:"'>~>]~-+!;+_i+!<:?--]>_];
                     .^"^.^^`.."``'`'`'``'.''^'. .'.  ..     .    .   '
                     ']_{i>_~,__-<??_l;}~>~+']+<l_i-+--~~;-]]-?~~-!_-l{<~-~l-~+]~]<+:--ll]_?[__.
                                                .  '.      `. .  . ..  ...'.' '^.' ......'.'''.









```

*Figure from page 35 (2346x3317 px)*


---



4203-E P-111



SECTION 5 AUTOMATIC MODE OPERATION



(4) Initializing Library Program



Press function key [F1] (LIBRARY P.SET) and key in as follows:



;I [WRITE]



With the operation above, the programs registered as library programs are all deleted.



(5) Specifying Buffer Size of Library Program



Press function key [F1] (LIBRARY P.SET} and key in as follows:



n;I [WRITE]



With the operation above, the buffer size of "n" bytes for registering the library programs is ensured.



Note that when the buffer size specification is changed, the library program registration state and



the program selection state are all cleared.



To ensure the NC program registration area for operation without using library programs as much as



practicable, zero the library program registration by the operation below.



Press function key [F1J (LIBRARY P. SET) and key in as follows:



0;I [WRITE]



The library programs registered in the operations above, can be accessed by the required MDI



mode operation. They can also be referenced in the S option mode or the equivalent operation



mode {DNC, for instance).



(6) The subprograms in the file which have an extension LIB are automatically registered as library



programs when power supply to the control is turned on. Therefore, G code macro or other



subprograms which are frequently used are recommended to be stored in the LIB file. This



permits them to be called any time as conventional G codes.


# !·NOTICE

: (1) A library program is distinguished only by its program name. Therefore, it is impossible to



register more than one library program which have the same name.



If the subprogram in the user program has the same name as the library program, the



library program is given priority when such a subprogram is intended to be called.



(2) Turn off and on the power alter adding a new library program.


## 19. Operation End Light (Option)

The operation end light goes on when the following conditions have been satisfied. Note thatthe setting for



the related machine user parameter must be set "effective".



Mode Condition



Automatic operation When program is completed



Single block off (1) schedule program after executing END in a schedule program.



(2) main program after executing MOO, M01, M02 or M30 in a main program.



Restarting will extinguish the operation end light.



When the alarm occurs, resetting the CNC unit will extinguish the operation end light.


```text


                                                                                                '```.^ ``.''
                                                                  ..'.''...     .. .  ..       `__-]!] >!:ii`
                                                                  >1]<i<~_]l~.?_<+<}[--_-;]{<+--,+?+__?_~~~],
           '^^^''``^^^^^^``````^``````````^`'''''''..'''''''......'`''. '..''.'`'.'.'''.`'''''``.`'.`'^`'```.
           `::,"""^^,::""^`^^^^,,"^^^^",,,""^`^:;;:,,:;;;;;;:::::II;I;:::,,,,;I;II:,,:IIII:,::;;I;:;::;IlII;'
                  ;_I .il>>i!li:,!>lil">;;iI!!"
                  ,I, .,^":"I^I:`:::;;`^`:~;I;^
                      '~i<>i;ii!_>i,i<>^_:!"<:__<<_-ll>>]~~"l>!I>>i"i"ii;!~!!iI.
                      .'':,"."""":,^,:;^:.:^;",""","``^,;^^`;;;",li^:`ll^:l;Il;.
                       'i>:^`";}-~]~-+"
                       '"`.^'.'`..'.'^`       .
                      ^[?1l>-_:<+?<]]~!:]+<~_`[?ii_i_+-_~>:__?]-~~_l<<;-~~+iI_!<~<-<~,_~;i]:~_+_+~,
                                .  .        .    . .^'.    ',"`^'``.``.``^^^^"',:^,`"',"'""'",",,"'
                  >{I ^[-_<_-<<<![!]-ll[><"<iI_<i~!:~li<i<>^
                  `^' .:,``':`':'`^`". ",,'"'`,^",:`'^;l":"'
                      ,+i<+i!-+<_<>;~_~:}:<l_>{-~+-+;ii~}l!:<~~i+_+,<:_>!-<i++i
                        ',`. ```"""^",:`' `'`'`''''. . '^.''^^^'`^:.`'"^'"`^""^
                       'i>",^I!;??~_ii?I
                      '::^';^''``''`'''`^''' '^.'.',.......`'''. '. '.     . ..  .  .
                      ^+~>I<>>;]<><-><:~_>i+;!+~i~~}-,<~_li!:i"__-_><~:>+?+?+<>_<__l[_>]~>_<+?~?i_I~i_~_>~?_
                      ';`,`";""`:"^`':^'^.:,^.``^.`'`':^^"^'.'..:'`'.`` ::''^''"' `'.''^^`^.^,````'''`'^''`'.
                      "]<_ii_+iI-i~!I<+I>!<->,~>+,-+_>-i+_>~;i>l-~_<[-+`-_<:-<-_!i-<?-~_!:_]-_<<]~>,+_?]:_<-"
                      "i+"<!i_>~l"i+->~+>l:+<]ll+>"-i;__+>~<                        ..     '.            . .
                      ':``^``,`^"`",""'``.``^```^`^^```^^^^`'..   . ..   ..         .
                      '_lii~i><;~~l+<I<!>[i_i:<?-__<?~~:ii_<!~;I~_!<]~>;+_-il<l~-!~![>+_<i+>-_~++<i]!i>!-l~-`
                      ;i<+++>++?^:_!!;?~li->_<;<_!+<_<:!+++?>_~~>;_l~?<:~~~i--<i!~]+<>''`''."^'''''^'.'`'.^^
                      ":`^``^`'^^'^^`.'^^'"`,,",^^!,:,'^,!:,^^`"` ,"^"".;:,^:""^^;::::
                      l_<<_l!><>-<<;++i!+I>I~>(]_-]~"_:l)~lI;]<>l~+:!;!-,<>>!<<`
                       .`:'  "``",:^,::`. `.'.'....    .``.''^`''^,`''^"'`^`^"".
                       ^ii",`<iI-__<i+-"
                      ^I^''I"^^` ''''`^^^.```^"```^'`',`..''''^`''..^'... ....'. .......... .'.        ..''.
                      ^ii~"+<<<~"+<~[<]<+"!_[~]+>~>Ii,-~I:]+>i]~i+ll[~<<< i_<^~-`+>>~~_~~;I_^<~I:~<-+i_l!}~>.
                      :!!i?,:<~<+_l!; "<!~;`<_"l?+!:-i,_-~>+><<~:i"]~Ii<:--_+l,~>>[:i!![<"<_<<i_<<_;<>_i++!i.
                      ;+<~]:<]]+~^_~;l<<~+>>+".'`^'.^`.```'^`^^^.`.'^`'`':"^^''^"^,'^`'",',:;"":,""':::^;:"".
                      '^^^:.^^`^` `" '::;^^;:
                 .~~' ,!:,`l;;;::;::;,`,'i;'li",>I::"l;:;'I"^;;::,;,"^"<;^:,':^:^",:"";"'"^",:""""`"'",^^^'
                 .i!' "l>il+~+~!-[~+l>IiI+<l!-!>+<iiI<<><;?!l+<+!>+>!;i?l+]~:-++ii~_~~-+I>+]_-_i_>l]l!_>~+I
                      ii!-~>i;l"+i~I:~!<+i'~<__+"i;:!!^!!<i!:lI:i;i~i"<" "ii~!_~!< ll;!i?;:<+lI,"l"~~i<
                      ;>~<>l>-!~!~"<>i>;;~>^<<>>-i~?"I>~>:l>i^~i!!l!i+!><i^~:i~:_~+<+l~I?_!I~}l-_I l~~~
                      I-+<~_+~]+>il<;_>,<~~~!i_~l_~-!!?Iiii!<l_~<<~l_!i>+_i;'^,',""":`^'","`",`":^ .^,:
           .          ";:",,,`::"'`"';:`:::l",;I`:::,"!',I"";,:;;Il';^::II!`
          ,!<~~~_+_+]l! ""`;l:"l:!::;^:l;;,,;::;!!;:,,";;;II":,",^,l,:"^^^^,;I;;,"";;,;;l;:^^,"^,:,::","^"":.
          !:?r1[+[\-j:_^l^.!i` <l-i>~il~l-<<+I>>>+~~<[<~>~<i!i~!>+;?!+><?i-<;i-i<! :<+>i~!<<:+_!i+?~__}?[!_~'
          ^!::;;,:I!!l<.i'     !~>~-<,;<!+l>~_!'>>>;?<<ilIil<><~!:~i<~II-ii:i<i"<+!i,I<i!<        .  .    .!'
                        >'    .;;i:,:`:,:,^",I^^:;I^"":::,:";I,:"";",;"`:::,",:^II":^`l:,;`                !`
                        I.    '>;~>^!>_+!>_i_<"iIl+~^>+~`i>i_!i<;;!];>_i^<+l<":<i!>^_I;_~.-~>_<^<i~-i-<,l__>.
                        ;.    '?~>_~,~i<-~-<;~;_~<~;i<~<-_"_-~+,i>>+,>:<~++><_>-~:_:!_+!~-<i<Ii+Il+_>+:....I.
                        ;. ''  "``^^":'^;^^''"':'^^'^``"`:.^'"^ `^^`.^':",,`"I^:`."''";^,;:^"^^;`";"::`    ;.
                        < '??^ i>>l;-!><<;i<,-_Ii<~+-">[_l:_-?__Ii:i+_;<_<~<:i>l+i~<:                      !'
                        ;"""":::;"^""^""::;"^^"";;;;;":,:,,lII;;;:",II;;::;;:;;I>II:,^^^,:::,^^^^",:::,^^^^>.
           ``^     ^`      '.    ^`    .   .    `                                    ..............''''....
           ?{u,   :t\f|j)1rtt|1(,z|1|x;|>trr/("f|t\t/)()|+
            .`'    '';`^..^'`^'' ``."" ^^;?"^`.;",i,"":"I"
                "!;,`",",I,"'"",;::I^""^^'''^,"^':`',""'`^"'``^^:"^^^^"^`^^^^^''`"^,^``.,`^'``'`^'..'`^' `'.
                ,i<<l-++<-<i:~<_i?]~>[<<<!<I~<++l+<i<-~i_i+-l~~i_<>>+i+-<~i+_+!<-?_---i']~?<<~_~<~ii_-]<?~_l
                ;<>^ii<+~!,!+ii>>~'!~<`><i+<~++i^i!~<I_l;+~`>~_~>i<>'                                   .
                .``^``'' .'.'^`^^`````^"^^^''`````^^''`'`^`'`''^``^' ..     .'''''...................... ..
                ?:,,,"^:{[_}-::::""">:::;:,"":::::::""^":::;::""":;!]+_~-~<~I;;;;;,"",;;;;;;;,,,,;IIIII;:::i`
                _,""";;I?~i~i^^^",:,~","`^^""^'```^"""""'```'^,,"^'">><~?+--"''''`^^"^'''''''^"""`'''''`^"^~,
                <<~-+~i-_I^-_~i}+~>`!+]~_i:_>+-+~~:-I~_~?-__+-"..            . . ........ ...'''`'''''''`^^-,
                ~i+l!~,IiIii"~i    .<"!^.Il>li<!!";;;lIl!"i<I",:::,;I:^ll!i":`"`",:",""^'"""^""^           ~:
                -,l,<!"";:I:`l"     !:l" ll;ilIil,i:<~;<:">ll';!>iI<ii<!i<_,l,!:!il<<!!!l>!_<i>;.          <,
                ['''.''....'`'`^^``^!+}I^<_[_;?+~1~[~:?1[il--]~<->_!{?{l:}_<"l1-?!!I![_-:!,>;<<_!!_<+_~_i` <"
                ;!;II;I:,",Il;;II:",:;Il:;;:,,IIl>Il;:I:;ll!!!llII<l!!!!:II:Ili!>!l;;lli!i!>!i>il>~>-_<>!I:!.
                ;___-_<l_:i_,l++<<]<<<,<<I:_~~i_>~^><<l>+~I
                `,,`^'"`^`^`'`'''`"^' ''``""'.^^'`^,^^.`:`''`  ..   .. '
                i]<~-:~~!;?_+<,i<i<+<`<-_-?<_>>+~;+?]ll>>!i[+I_?-~}<~?I++>;-?+>[-<;!<~!!}?_.
                                            ..                   .^.     . ''. ... .... "..














```

*Figure from page 36 (2346x3317 px)*


---


## 20. Operation End Buzzer (Option)

4203-E P-112



SECTION 5 AUTOMATIC MODE OPERATION



Operates in the same conditions as the operation end light. The operation end buzzer sounds when these



conditions have been satisfied. Note that the setting for the related machine user parameter must be set



"effective".



The operation end buzzer sounds for the length of time set for machine user parameter, "Buzzer, 7.



Operation end buzzer timer".



Restarting will cut off the operation end buzzer.


## 21. Error Light (Option)

The ERROR lamp is turned on at the occurrence of an alarm. Note that the setting for the related machine



user parameter must be set "effective".



The lamp is turned off when the NC is reset.


## 22. Auto Power Off (Option)

The power is shut down when the following conditions are satisfied. Note that the setting for the related



machine user parameter must be set "effective".



Mode Condition



Automatic operation (1) Schedule program after executing END in a schedule program



Single block off (2) Main proQrarn after executing M02 or M30 in a main program



When this function is used and there are blocks changing/setting parameters on the program, it is



recommended to make the backup function effective with M02/M03 (Set "1" at NC optional parameter (bit)



No. 33, bit 1).


## 23. Work Counter (Option)

Count data is incremented when the machining completion signal (M02 or M30) is executed. The counter



has a six-digit capacity (0 to 999999). It is provided with the reset function.



000000



Reset button


```text


                                                                                                ^^`^'" ^^.'`'
                                                                  .''.''''' . . .`....''    ..."?]-?!?.>lIi~;
                                                                  l{+<l>~+];+.-+<_<}}?-~_I+1_--]^~_~?+-_++~[;
           ."""^^````^^^^^^^^^^`````^^^`^```^^^^``^`'''````''''''''''''.''.''..''.''`'..'''''''..`..^'''.'`'.
           .^`^::""^^''''^^^^^`'`^'^^^^"''^"""""";""^^``,,"^^:;;;;;;;;;;;;;:::::;I;II:::,;III;,,;,;I;II;:::;^
           ,)1-    :}]+~_>~_[~~+!^/<<i?^\?I!>i>il ~-_i<-illil
           ,]-_`   :-[\]1<[}??}[~")_-[}"\[[[{{1{_`\]]j11[(]{{ .
                 .'                                                  .
                 !___>-+_l>!-~!>-~+~Iil>-~>+-l?!<_>;<+~>[~<,>><<<]_; _i<"><<l->!Il!<>!i>i>!"ilii<~,+~ii:~<>>:
                 ;i!!~~!!>I~~ii!~>~!I+_~+++<'<_>+l-!?>?~!i~~+!i>_~~+l:>_<_~!l~<ii<<!;i~<I~>l<>~~~i;~!~il>!>~l
                 !~?+>_>i<":l,:^;;I^"ll;;;I: ";:l";,!"Il";!lI;<:!^;!!"!!>!l,";>l;l!::!!I"i>Ii;ii>,"l!>;l<"li:
                 .i!>li;!`
                 :l;`.,,,,!;I"';;;"I:;:;``;,":!:^!:'!;^,;",l,';^,,:"',I`:,'^""";,"^.^""''"^^^^^""'.;:'^`^'."
                 l<+!;]-<i~>~II<!i;+~+~_,l<i!!~i^~i'>~;;+l-_;^<"li~>^_-"l<`li_<~~ii^~_~"!_>~~i+_-;.~?<~<?!.!'
                 l~<>!_<!::ill!>i<<+`+!>+"
                 :;"""",^^'^"`'^^.,^,^'.``^^,^`''^``"''''`.
                 !++~-~>i[I_<:i+iI-I<_>;}-_~]+<;i_<i<~++~+`

           ^I:`    ,!^"^``., ".;"" "l,.^,`.'^'
           ~t_>' . [n{){tt^\_\cvtf"f//nff\/|\} .
                            . :    '  ^     .'
                 !<l:~!<<!i<;i;l;;;:IIIl;,;'I;ll:";;;IIl;:;"!;!,:i:;;.,!;l"I;I:I:,,;!;,"::^::"^:;I::"",":,,,'
                 :!~!!!>><>ii_i>~l<!~i>+>i>I{>i-ii~lliI>Il!,i;~,!<lII`^>!<Ili+;!ili<~ii-I>;li!:<~-~~II~+>!l+,
                 ;!iI,i!l<:i><',ll<",~`i<:'<i~i>l>^
                 lI;^::,,':`"^:",:'>:"l""';:^^l;','",,:"
                 :;~;!<!~,<;i>!i~lI_;<<<<"i~>:_>"+Il>~+l

           :~~:    "-":>I^;]I:;:;:,^<i+>'!<l"I!:",;^
           +||_.   +/1(\/~<1[||||/+:|)f]!r1fnt\\|}f- .

                 >><,i!i<+^~:~~ll;<l>I:~!!i:_i:!i<l>l!!"llI~-i!i,iiI:>~><+>< l~l<;i!ili<I"li+!!;>!"<l,"i!i!i"
                 !i+~?<~!i!~l!<~i~~<_<:>i>+l~+;i+!i_?~?~<<i;;::;"I;:"!!IIIll ^l;!:::!;:!;"!lil~ll!^ll:">i>>>^
                 ,I!I;,I`^!!""!l:i:!l!'^;;!,;i`!l`.!IiIi;!'
                `;^^^":,;;""::^`^`^",",,""^^^^:""::"^`^^"",;;;::""",,,"""""^^"",,,,,,,"""",,,,,,""^^",,,,,,"'
                !-.'.'``_(-}1;`'.''^i;``"^'''``^^^^^````^^"``^"``'`^~----)]_!'^^"^^^^^```^""""""^"^^",,,,,,;_
                l]~!~iii?_!<+<l!<l!"li>>"!+i>!>i>il<illIlII__i;III;;>><!-[-_Il,::ll!Il;;,":IIIll;^````"""""I?
                l_!!il:l<!';ii!><l!'^;Il ^<!!<>!II,>l_~li,,+<>.!i<!!+i~:!i>!^<">:<!!>><<I!!l~!~~!          `_
                I?[_+]_!-+_?;<1, ...I>]-`<)?+ll_~?-+-iI1{+:>~++!-<+l+[??,~,]{-<l!liI<+<:<ii+~<i, ......    ^?
                '!iII!;l!l!iI!II:::,I!iiI!iil;!>!~>>il;!l!I>i>i>!I>ll!i>l~l>iilI!><i>~>l~li]<~ii:;::"^":;;I;l
                .+_i<I.<i< <:!<~iI <':i<-",>!I^_>>> !>! i>!i<^'i!+l_i!~i<_~l< l~l<!!~<li :l l!l il!i!~!''i'~.
                .!ii>!>>>i<-~<+Il<__><]~i~~<~<i>_>>~<<l~}_<+<<I~-_l\-[}[]?_l)_]l<!!_<}_!!<~!i~_!~i_?<--~:~i?'
                `-+;I-<"<il+;^"`'":,,^,:^::",;;`:"":,"^I:;,,,;^;:"`:;I:;;;;";!l ^ :!^l;^ll;l:lliI;lII!!!"!!!.
                'l!^^>l'lI'I`

           i~+^    ~]~l;<!'-!;:";I>I;^`<<I:ii:,:;'
           }})<    ?f})){|^|-()111\t/;+r{/f/\\([t!

                `>!<i>;+++;i:>!>~!<~<+>il_i<:iil"i>!<<<i!!;l!!!i<!>;I<<l+:>_<~:l"~_~~:i;!!!!I>l!'"_il,lI;!iI
                ^><<lI!_!>_<~:<<i>i_!!?i~;-[+--?_,,_l>l>~~!_<<>>_~!<<<+>_i<_<<l-l<l;;";,;;lI;III'.:;;";I;:!;
                .:!;,:;!,:i+l^l>Ii;ll"i"!`li>>>>~".>;il~!!i~~<I><i,!<;`>i<;I>;l~<!'
                                                 l,^`''.'''.'`^'.'`'^:
                                                ':                  '!
                                                .:.                 'l
                                                ';!l;^;II:I;>!Il""` `I
                                                `!i!l^I!<iiIi!l>:;" ^I
                                                ^I~l .              ^I
                                                `; l                `I
                                                '!`;l.''''''```''''',l
                                                 ^"^i:'.....'''`^^^^^'
                                                    .::iIl;I;!I'
                                                      `I;;":;I;`





















```

*Figure from page 37 (2346x3317 px)*


---



4203-E P-113



SECTION 5 AUTOMATIC MODE OPERATION


## 24. Hour Meter (Option)

24-1. POWER ON TIME Hour Meter



The hour meter accumulates length of time in which operation power



has been turned on.



Hour meter range: 0 to 99999.9 hours



24-2. NC RUNNING TIME Hour Meter



The hour meter accumulates length of time in which the RUN lamp in



the NC operation panel status indicating lamps has been lit.



Hour meter range: 0 to 9999.9 hours



The hour meter is provided with the RESET button.



24-3. CUTTING TIME Hour Meter



The hour meter accumulates length of time in which cutting has been



conducted (G01, G02 or G03 mode) in the automatic or MDI



operations.



Hour meter range: O to 9999.9 hours



The hour meter is provided with the RESET button.



24-4. SPINDLE REVOLUTION TIME Hour Meter



The hour meter accumulates length of time in which the spindle has



been rotating (CW or CCW) disregarding the operation mode.



Hour meter range: 0 to 9999.9 hours



The hour meter is provided with the RESET button.



POWER ON TIME



4 .



eJ;



HOURMETER



NC RUNNING TIME



RESET



11012341-EYI



HOURMETER



CUTTING TIME



RESET



O 1 2 3 4



I - e}



HOURMETER



SPINDLE



REVOLUTION TIME



RESET



O 1 2 3 4



HOUR METER



[Supplement] When hour meters are selected, 24-1. "POWER ON TIME Hour Meter" and 24-2. "NC



RUNNING TIME Hour Meter" are usually equipped.


```text


                                                                                               ^",,`,`.:.^^"
                                                                  ^^`'`''`.'  ' `'''..`'..'..''~?-]<?!"+:i>+.
                                                                 ']?~>i~<]i+::?ii<_[-_~+!I}+++[I;_i-__->i<~<
           ^^"^^^^^""^``^^`^^^^^^^^^``^`````````````''`````'''''''..''.''......' .'''...'''.'.''''.'''''.'.'
           ''',::::^^`'''^`.'`^^^":``^`''````^::::::,,:;;;::::::::,,":I;;;,,,,,",,,;;;;;;;;:::::;;IIIIII;,:,
           -]}"    -[+~i~;if1+]-+! ?[-~-]<<<+l
           -++l.   <+]][};I|[{-{{<`)-?t[[]}?{_ .

           llI';   i>liii!l<^I!>,li>!~I`lI""":iI:;,^                                  '!;l!!;"l:^Il;
           <>>^!.  !l>>+~<!<^!<_I"i_-[i`<_>_ll[_]_],                                 .:>>~+_>i_~l_]~^.
                .I,`'^'' .`'"^ .'`.'..^^..'`'.^' ```^`'`.`"`^`.''''^''..''''.        l<",""",:::;::;+I
                'll+l<<-;l>~_+:-i<>i><--+<!-<-[il~i~<+:>,-+>-!l[_~~]<~!_~<-],        !~             >l
                ,~~iI___l:iii~-;i!                                                   !~ ...  . .   .>l
                .^^'''^``'^''`..'.`'. `````''..  .                                   I??~i~~>!>II+~i]l
                ,_<<i,<~-];I]<?]; +!-:]{1{1<+l+<i<i                                  I[?>i++>i>Il[~;];
                              '                                                      l!  .        ?+!:
                                                                                     !! !!il~_<li!>^<:
                                                                                     ;iI<<++-[]_-_<;>"

           !!I,i  .>i!`>~"i!>Iiili'Ili>_:"!;^"^:i;,::'                                '..'.'.....'.'
           ~<il~.  >_i^!~i><~<_~~_"";_]{l:~_>-,I[_~??"                               `_!;->__<]_,!+["
                .l;` ^`. ``^^' `'``^'`'`^''`'.:. "''''`^'",^"'"^'";`,^````.`.        ;i!;:;:l!!i!l!!~"
                '<>_l~~<:!~_-i:?<~_i<--?-ii?!}[:>_!i+<Ii;__<<Ii~!I->_i!?i?I<"        i~<>^^^'    ...~:
                :<+,~-I"-~<i-i+;!_i!+"+<?><^>><>_<!_,+i+_!l~?!>+~+,+!                iI;]>_>^       i"
                '"^'.'`'"`''``''`'^``.""""`^``''^'.".'.``'.'^'.`''..'                i_:",,,:Il::l;,+"
                "~<>I"<~+_";-i]?" <;<,----l~l>>><:                                   i)[~>~<+~_;+{_l]^
                ':"^^^'^.`^""^^".^```^``''",.""``I:":,"`^','`                        !i;:,""^,:`^;]i<"
                '!<~I<i_:l~__<^+;~!>i<_~;<_+:~_>:]?>}~;;-+]<<"                       !, '`'^,`^^`"_:i,
                                                                                     i<;-][[11{-[[i;+"
                                                                                     .`^''''.'```'`^'
           ..  .   '. '`'.. ' '`. ''
          .]?<i[. ^??_?-<-}}{!!-(1|_,--_-iI([[[?l                                     .`.''`'.'`'`
           ' ..'.' .''   . .'.  ...'  .'`  '..'^                                      ,<!Il__i,>?-.
                `<<iI<li^l+__!;_iiIi<>~~~;><!-_,!!<~~il!;_~><,ll]<i!i~<I<i>l'        !>~iI;:l!!l;;II>^
                ^I!><!i~!<`<]_i;`+]_-^><^<__-Iiii~_l^~;"_~;,<I~<~<_?";~"l[?+"        >l~i":,` .     ~"
                ,>i><~~<<i :;I"` ,ll; :; :lII ,;;!i: ;^.ll" !;ll:!ll'.I 'iII`        <^,<!<;'       <"
                ^iiil~iI:l                                                           <_i::;llIl";lI;_"
                "l,""`::I;^,l:,;''I;;^<iii,l,:::;`                                   >|]i!?-_<_;+]_!]^
                "I:l:^;!>>'">:+!' I:!^~<~>,l,!!ii'                                   ~!"^^"^``^'',[i<^
                "!!;:l;:'"li!I^I^!:;:iI;^;ii`!I,:_~i+>i;!I~I;.                       ~" ",^,:::;:;~^<^
                .^;;^:;;`";l!;`I"l:;:I!l"lIl^IlI^!I;!:^,il>l;'                       i>!]][]][]_?-l;_`
                                                                                     .'' .     .  '''


          '~~:li  `?-+-~-_><~^--+!~<~;!>-<i~_"<+-~?;:ilI;,I+!!l!"
          '>!,:I   il`ll<l!>l.;iI;I;!;l:,III>^`;<i~,^;ii~""+>>>~`                    `,",:^:'
                "il^`:^^ ^,:;: "^"`,^^,;,``,`"l^ ^.,,^ " ^;^^^.;"`""""lI^;,:.        !)~][<?>";;^III.
                ,!~~;i~_;<+~~_l[><<i_~]]+!i_i?+ll~;i!-;i,>~>>il_~;>+ii_+;!~+`        I+>i<<<~_--!_[[I
                :ii+l^l<~+<>"<l~:;I`il!<;^_<i<--i-i_I~~l;->~>?i!^Ii!~_'              ~i<:'.'``''^``,].
                ^;^^'^,,;"',:"^^.',,^`I;l;^:"""`^  ..    .                           <:-?~?l'      ._.
                "!li":><_<'l>i->'`ll!,-+-_liIii!!.                                   <;^::,"`````^'^~'
                "I;^,:^^."II;"`,^;"",l,:`"l!'l:`;>!!>;""";!",                        +{_!l~><<~:?[-i?.
                `,!I"!ll^;i><l"il<l!!<<<:>~<,i<II<>!+I`:i<~!l'                       ~+>!li!!!!,>~_>_.
                                                                                     ~`          "{I>.
                                                                                     _:;?-+}]}]_[]:^?.
                                                                                     :;;I!!lIII;lI;l!

                ,~::I;l;;lI!    :!l::^:,"^`:,;,,'^:"`,;:":,:.:;`" ,l:l;lli",;:^;;Il`,"``^I,,""^^^^`,"'" "",`
                :<!<_!~I!+>_.   i-<-_l~+_!l_-[_>!>+>l?_?>+++"i<,:.:>!<<~<~;!~~"l+?+,i>ii:[--?>'+><;<~:~',~_;
                                l~!~-+++_;l<-]<,_!!:i]~-_,'<~l:->~-_">~<-<+_~^
                                                  .        .  .... '..'''''...





















```

*Figure from page 38 (2346x3317 px)*
