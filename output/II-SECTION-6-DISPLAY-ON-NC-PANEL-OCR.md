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


                                                                                               .^^^^'" "`.''.
                                                              '''.`'..    ...'. .. ..   .  .. ."][_-!?'~II!~;
                                                              ~1~<>~~?+i>'-_??<l]i:-{i<{~:_--?__+<<~-I+__?]~.
           '"^^````^^^"^^^```^^````'````^``^^^```''````'''''''''''.'`'```'`''..^'''^'`.`''`.'^'``'''''.'```^.
           .^^'`'^^^""^:^`'^"'"::::,:``'^`^^^^,;^'``::"^^'^;^"",,,"","""":"":`"`^::,:"^""`^,::,:,,",;:I;;;;;`
           ;t-([_}~}([[_-1[!`)l      --_?1-]1?l ~]<-;"_<__< [>~~< l~i-]~?;_?'_;+~l!>l<!""?!!;Iil<il`
           ln\n/)(~_{{j[\\u-;Y[ .    \(fjxxv[}r+nn{u'-t|nuu Xvvt('t|fX)fU}cx/ctt]\n1nvCi?c)XnxXuUxf(,
                       '              .       '^      '.       '`  ^    '`  ^ ..  .,  . .  ..` '`"',^

                 >_<!^~ii~!I'+>i!!~ii^<i:"!I>>l~l'>:>+;"_~<<ll_"i!IIl';;`il^!<l'I;!Ili::':l;ll :::l;:!""l,>;^
                 ;~+iI>++ii;i<<<il~<llI+!;!i><i-~;i;i<>I!ii!Ii!^~<i_~:!il!<I!-i:>-->++i!I~+!++^l>l<<>~lI>:<~;
                 liiiI!+~~!;__?<-_+<!-!<_i;+<I!_!!:!!!_~;<!i>i,,_!>!i>;<~iI!+-i>"~~_i>+<+;iI;>-:+~_i_>;+i+~>^
                 ii><"~>,]~,I><<<il??I~_+;<<>-_i.
                                             .. .
           .'      '"'  .   ..  '.   ..
           I1^     -vftjt{t/;r(|ut)1xr\(/f;|>j|(|/)(
            ''      '.^^'""^ ''^^'"",^^'i_ ,";,^li,;
                 ;l^II"";:'",,",:^`.^"", ^,'"^"``^`.',"^;:`"",^^'^":`",`'`^^``''``.`''`.''` ''`^^'.' ...'``^.
                .liI<_~I<!;__+>_~>ll_<>_;<<<I><~_+i_!+>I+>:~~+~~;!~_<??<-i?<_?>i+~;_l_~_]~<"+i<>~+I~<i+<+>-+"
                 i+_i<-i_I<+]><"i?i:-l,<~~_<~_~l<i_Ii~<I?+_i,-+<+:!I+i
                        '.                   .        . '... . .. .. .
                             ````''. ..'``'.''. .'`'''..  .'''...'.... .  ....'      '....
                            ;_`^^;]]+_[I^^:1i_i)i"^:I_(1]:^^;?)(|}<^^,+!]{!_:`"_-_[{],^^^<;
                            :+^^^<]--_--"^>]__-[],`i?_]]??:`;_[][--I':{_]]+[!'"[]}}}{>'`'_<
                             '^`^'''''''^^`''``''^"^````'`^"^````"^^"^'```^"","^^^^^":,,,;.

                'l;;;;;:^"",:;,,,,"""",:;::::,"",,:::::,"""::::::,""",""^^^^''"""""""^^^^"""""""```^^^^^^^^`.
                !-^"^^"~-[-?i}{}[["^^^",i'``^`''`^^^^`^^```""^^""^^^^"-+~-[]+<"""""""^^`^",,,,,,^^^",:::::::-
                I<````^:I;~}l_<,":"^""""i>!;:l!l!;I;I!;;!!lI,lI,:;:IIIl;>iii_>::,,"^:;I!;;"````^"""""^''''',[
                Ii```^^^``I~~-i'^^""^`'"<~~+~<[<?<<}?}_i]~_il?-i~+i?_+?<-_]<__<i]?+~[?[}+_I''.`'''`.```'```"~
                i>.''''''`[Ii>{"`````''^l!~+i>_>~Ii_~-<;-+]<;<~l-?i;>:>~<i_]<<>+>:<~<~<<<i>l<<l~<>!~..'``^";-
                ii        `' '^        .:!_~ii{>i~>}?_-+;><~++?i+_i-]~]l<?+[-{i)>+[~--[{[~[]!?;_~+~]:I"    '-
                i!                      ;<]-~+-+!-^^^"";.  ^:""',"":,,;.^I";:,'l.;,:I;I;I,I;:l^;I:!lIl,    '-
                !~:::^,l"li!;llI:l:":::I_?_i<<~+_~I,:"^`",,,":"^^^`",:"::^`^''"^""^..'.'``''^''... '''`^```:?
                l;    ,[!+_[:~__~-,    ^>Il<I!_!?l~{][~l]~-~l]?!+}>-1_l[?[<_l]?[__;->!??I~_]_?__l+[]??}~+"."_
                i!`^''.       ..... .''^+-?_[<!~>_+]_-]+    . ..  '. .   .`...    .'  .' ........'^.'...'. "+
                <i^^+[[?-]]?])~_]?_[i``,<_?-<~]+_l>-[}+i->>!;~<l+]>I!:i;+~Ii>!ii>~l<+<!:l:<!Ili+>il>:il!:,,!_
                >;  ''^"^,^^":.`^'"^   .;!>]iii"?l_}[-+!>+}_I<{<l?~![!<l~?>_~_1~+<!---!i<;+_>>]ill!<^il_`  `+
                i~,"^^^^",:II:;^``^",,:I+]--<+l:~i]~__<~![_?-<--;<__?<>+<><~~~+<~!__!]i?-?~+-_~^'...```'`^`;_
                !:       ^>-{_i.       "ili+il}>-I<{+-!!<__lI-_!~]-+~I-_?;<~-]-_i<~:-;i>I??_<~-!--l__1+[?[!"_
                !I''''...       ......',?_<_]<<!'. ^        ...'  ... ....`'..''''`'`.''.^^"``^..`.``'.''`."+
                ~i""""^^^-_>}]1-^^^^^^"l+?[]i~_<>l~<_-!I~>>i;<il+>!i;l!<<<i:i;^^",,,^^^^^`^",,,,"^"^^""^,::>_
                +:       ;l:I:!;       ':;!i,I>;i":_!>;:iI~:^i,,+il!^I!l!<l^i,                             ,+
                ~:                     ';><~II+i~,!~>+:I!i!--!,-~<~">:+>li>~ll~+++_??:>i>~_!!>><:+<,~~+><' :+
                _!'`''```^^^'''''''''`',_]~~;?}[{)]<^^``^``:^`'`'^``^`^^```",'`^^^^;"'^^`^"`''^`',^',,"^". :_
                ^;,,,,:;;;;;,,,,:;;;;;;;;;;:;l!!!ilI,,;IIII;II:,:,:;;;;;:,,";;;;;;,",;IIIIII;:::;;II;;;:",,l;




































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


                                                                                               """:`;'`;."""
                                                             '^^`^^'``.' ''``^ ''.'`'.''..'^```_]+->?:l<:><i
                                                             :[-<ii~+]I-.>--[_i+?,>?];]_:i___~?+i><[iI~?-?_^
           ^^^^^^^^^^^^^^^``^^``^^^^^^^`^^`````^^^```'''`````'''''.'..'''`'''.^'''''''''.'. ...'..''''.''``'
           ^"::::::^^^^^"^'^^```'^^^^"^,"^`'``^^^":::,",;;;;;;:;::;:,:,,;;;;;I;;;;;;;;;:,:,::,,,,,:;;;;;;;;,
           }>      ?]>_-l~]l<|<>_+}-<i<^>[-_i>-_>l'
           [<`    .-]}-[]{(;<<_[)[[][]_;>[_1|/[)[/^
                .''                                ...
                "?-~_:;_i>~~>"l_-"~_]~:]?<~~_}!"_<~]~i:!_;-<_+_->,>"}-i:?_~<]_+I:~i+?l'[-I!-~!?>;_~_~<+'<-~<
                ^~i<+~,>!i]~~~><->' ''.... ...'  .....'.'`^'````'.'.'`'."^`'^``..'``^`.`^'`"`^"'`"^^'^`.`"^^
                `I"":,'^^^:;::l::"
                'i!!:!>l>>lI!!ll;:~+<I<,_>i+>>>i!;>>l>>~!>!l!i<!<l;~!>~!~il!><<ll:-~~:~>i<>lI!;i<!:<IiI>!;!I
                "~~li_<_<~i<<<_<!ll+_<I>+~+~<i>!i<;^~_>li-i<]!;!<>i~><l<~!<<!!<<il+_+i<!<<+~Ii<<!>!~i!<~>i:"
                "!>";!!i:i,i!iiIl:"ii>"ii~l<i^II!<; "I!:I><<i+^l!!>iIl"i>":>,:l>!i_>I:+::>ii_:l<:>i__"i<<<.
           ' .             .
          .[;i:   '[?[}_1i+[-]]{_?~;]?}?][[;                                                             .
           .  .  .  '..'`'  '^..'. ...^".`;'
                :i>:i~~?I:~,+l~~_i-:<!>+>i`i+-i:~~~+_:I_>"i_~><<^ii!+~;I<i;~!!i~+>:`]l<_~,i<-<!<!<`l!l~!,~I<
                :>ll!~+-,>~~!l<l>:iii_~'^+-+>+!,_!-<il~<<><I!~i-_:!->i!<l~<;li~~!!<!l>~;i!~;<~i~;~~i,<~-!~>+
                "<<>;>i<I><-<!~>I'i;>-<: :l;:I^^l':l"^!!il<,`I;l~`:iIIIl`l!';!!!^:<!';i`;i;`!i;+,:<;.i~<i;!!
                :~+i-!>i-^l_~:l<;.>'><,_.
                  ..  `'    .. '.  '  ` .......
                 "><' ~~[)+>+l>]<+<--!?<-->_+<~^
                         '                              .,^^.^```^''^^^''```^.'^^``^'
                                                        i{-_>}-{-]><+>~I>><+~>>]]_-[:
                                                        `",`.  "i_+!_+~->~I>~!!;<<ii<i;li+]lii~<<i.
                              ,<>,i>>;:llii>,!<!>>l       .":,':<<l:;l!!Il,:;-__->-_-]~II!iIll!II:.
                              ,l>Ii>>!Il;!I!:l!l!i!,`        ',"'.`^`       "]~>!:!!l>l
                            '`'           .''......"Il"`.'..``',liI;;II,"'.'`"lI"' .
                          .;,;l~__l>---+<_!::::,,;I::l]{-i_~!::::;!~~i<+~]~i;,,:!<_;:;.
                          ;^ ":_??!+[[[~i[i""""""",,,,<+~<[]>;:::,""?({(]]|_i<!~I-|l ^;
                          l'                                        :!:!<I>Ii~!~!~l" 'l
                          l'      "[.       `?[!']~]<.   ><      .<+~!~l             `i
                          l'      `l        .lI:';;l:    ::       ";;^I,             .;
                          l'                                                         .;
                          l'     .`:       ",l!.'II;:    ;,             .,"^ ",:     .;
                          l'     ,!i       l<[?;,}-]+.   [_             ^--< <_-.    .:
                          I'     :"                                                  .,
                          I'    'l                                                   .;
                          I'    l.,[.   ^,!!<[[I"]-[?'   -:        +<'?;'],    .-I   .;
                          !'   ": '^    ....'^^`.^^^`    `         `^."' ".     "'   .;
                          !'  .!                                                     .:
                          l'  I`                         >;          .i^.i`    .!"   ."
                          l' ":            `^:^.         <l          .~"'_^    .~:   .^
                          l' !'I;          li[i^                                     .,
                          l ;`:{]            ',                                      `i
                          ;,; :}?             ';`                                    `>
                          l<..;,`  .'.''.'`.  .`lI`.'..''''''''''''''''. ..''''''``' `i
                          +: ,_-]-}~I~+~]iI~_?!  !~[>??"i'...'"!^^^^^I;l+-]II,'.'``. .;
                         ._" ^}_[+i":_-<_,^+[}?+_"'\[?; ;;+>_!^^     ,^i}]< ,'!>!!_<.^;
                         l',:,!;;,'^;;lI,":II!i><;^l<~^.,:!;I;^^'^``^,,;i;,'"^I!l!~i;:
                        ,:   ^;l!l!:,!i>ii,:liill";li<_>'I;iiII`!i~>!I"l!i!l;^IIi!I".
                       .!    i;]~:^~i,~]!"><^?-lI!;,??"]_<,?1'~;i;[{'>!;<_>'+!;<??^]
                       l^`.  ^!;::I"^lIlI;^,l:::I`,lI:;;:_;^:,,.::"::,.;I;;;"'I;;;;,
                      ",`_+l?-~_<^:;}-~?_l<-+~!_?>!--+_< .;^ '        .              .
                      i^l_i--]<+?i>_<<I+-[+i_<-+_!<>-_-i   ;;--+-+]i_[[-_i-~_+]<-[]??]"
                      ... ........    .               ..    . ... ....  .. ...'`'.....
                                   ,`. ".' ^'^.'."`.``.''"''''.  `^. ..`' ^' .'. `.'.....'.
                                  '>>]^]:;.+~?+-;!<+-_~~l_~???]""!~[{_!_<![~~-?[l-~]]>-+--;

                      lII"IIi:lI:^,i;Il;`;li:,;:::^I:^:^":;:::,^:^:l,,;:^":;^,:^,,;I""';;l`:I,::"'"",,::"^;,
                      ;!~;<~~>+<~~!_+~<?;i]-<I_ii~;-~IiI!<<!i>>;i!I>~;~<!!_<i+i~+~+<<l,___Ii~~>~-I_ii~<<i:il
                      i<li+-Il<><l+i!^:i<Il!iI;i<l>>--i+>i>^+!>,~~~">:l<~i+l!<~_~iI"-~_+_l;~!~__:-]"
                       ,^      .:.^^^.^^"`^'^`^:^^''`.``:``^,``,.           .         . ..       ...
                       i;   .' ^<,~>>:<i~<<;<i<~>l:Ii"~>~ii;<ii_^
                       ;^    . `I,!;;^ll;;!,I:li:;`:,^;;!;::l,;l
                       "`   .. .,"!;;^!IIll;l;ll::^;,^I;lI;,l:;l.
                       >,   .. ^>;<><"<><!+;>!<~i>:Ii"<<~lll~i!~'
                       :^`   . `,"::"`:,:;;":","",`""';",,"^,"",.
                      .i~~' .' "?+<~"i!i!+ii~<^~~~_<l,>ii_+-'
                       ,"    . ':^"^",;``,:""^^""^"""'^,"",.
                       !I   .' "><i><!]!l-~i~l<ii]~_i:I+~<+.










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


                                                                                               ^,,,^;^.;.^":
                                                             .^`'^^'`^.' '```" .`.'`'.''..'```'>[_+<-l:+,i<+
                                                             "}]<<<~~}i_^!__]~i<?:!?[!?-I!-~_+?+~i>+<l-~_[~:
           '```^^^^^^^^^^^^`'''''``````^`^^^^^```````````````''``...'.''''..' `'.''''''''.. ...''.`'''.''''^
           ^"",:::::::::"::,,"""^^`^^^^",""""""^^^^`^``^^````,;;;::,",::,"",",",:;;;;;;;:,,,:,,,::;;;;;;;;;:
                       ^-'   .  !i!I!Ii>^!!~I!">!i;i!l!,;i!!l
                       'l.   .  ":;^:,:l'I;;:;^l;!Il:;;^"l;:,        .
                       I!    '  >~i!+!l~_<><-:l>!~!i<~_l"il!+<-<~>~~i<"~?>+<
                       ',    .  ",,^,"`",":;"^^,","^"",^";":I`"^^`"^^.`",";^.'...
                       "~    '  i~>!_l!]li__,!-++<lI!!-<~_??i,+<<[~+<~~-~:_,~]_+_.
                       ^l.   .  II:;::,;!,`!i;!^:,:I;;`          .
                       ^l.   .  ,!!:,i;~>:">ii>";!ll!i'
                       :<.   .  !l>]~^:><i<,"Ill!!Il!<!i:Ii>>~~I
                       .^    .  ^^,,: `:,":``:"^:,^";:"^.',"`,,`
                '-<i>>_>!>!_l   '+l~I+:lI!~>i";+!i~>^I!;<<~ill>!;i!>,
                .:,II:;:";":"   .",;,;`:",,,:.^::::l',`":,,":"I"^;;l"
                                ^>"~<;l~!<+<"<<+i!>l~"~_><~i"i!i+!
                                .`'^^`'"`"^"'^^^^`^^"'^":",;'`^""^
                                    .i_;~_?-_>i]:_~-;>-_>:>"?+~>~<_>i-_<_i"[;+~~l'
                                    .^^'^^^^"``^."""'`^^^.^.`",`""^'`"^^`' ^'""" .
                                    :_!>l~~!<>i!_+~<>l~~l~+!l?_~l><;_~<_-<+<>!;>_,i~~i<__-^;+<<_I+l?~~__---+
                                    :_lI~<>>>>i>_<i-~+I~~<l]_[:{_+~?+]-<;-i>;?--,<+_~~i_-_---]]:.'.'''''''''
                                     :,^"","`"I."^^"""'",,`"';':^`.,",,,`;",^,,l`;:,",`,^,;;;l;^
                                "_;~-l<<i;i+_l!~-<!<i>:!?+___^!i>~~.
                                 '..^^'"^'`^^'`^""'^^`.`^:,^:''`^"^
                                    .i+I~"+>iI~<~->!^~<~,++-l>>i"]~<__<+~I;l__,>+~!i___^,-+<+l+I~_<-++[--l-~
                                    "<~~++>+!~i><><I!+~:?+{I_]+_]--[_I+<+l-<[li____!_?_-__-}!''.'`'````'`.`"
                                    .^`"""'l'^``^",`^:I^:`l"::"^"",:,`;,;"I^!"::,,:',^":::;I,.
                 '<+. !>!!l">;;_III:i!l;lI>;;I;l;
                 '!!. ":i~l^I:::,;;^;lI":IiI:I;II
                               .''.. . .. .. ''''`^"^"^"^''`'..``````^"'..''.''```^^`'`.
                             ";"lI~_+l]_+_>~-:::::::::::i]-<~_~:,;IIIll<~+<l~!l""",;<~":,
                            .l  ::?_+I[_-]i~]""""::"""""I-~>_?_;::;;;;<//)\?|{!~i~<>f)' i"
                            .:                                        "i!l!I,!">!>>!_;. l:
                            .^         .<il                 ^-+>+<  .}>'><I<~`          I"
                            ."         .(mi               . ,[z)|X""'f1x|<0]{[ .        I"
                            .^         .;'I                 ^l;'<,l! ,i,;<^!i'          ;"
                            .^         ^!,;              `[.;+,<l   '<i:_:`<l           :^
                            .^         .|Y"              .L"frf|\[,'!cx/t|v~rl          ;^
                            'I          'I                l.I!I,i:+,'ii;l>l<>.          :^
                            'l          :<!            +`.~.^<^,>`   li'll.!;           ^`
                            .;          ?nI        ^Il`x+.Qltlcj!j'.>/<U??Lit!          ,`
                            .:         .1!^         `^ >; -'l-<<?l~;'_-i~_<_-`          :^
                            ."     ,~_".i>I   "_.;_+><+    ~'       `~.^>               :^
                            .^     ;_?,.__!   ;].^!-ii-.  '~`       ^]:I].              :^
                            .:                :f"          ?_          :}`              :^
                            .:   `l^          .,.          ^^          .,               :^
                            .,   <|!                                                    :^
                            .I   ~1l                                                    :^
                            .I  'l^'  `'.'. ''. .'``'... .'''```'''''''``'. . ''''``^^. ;"
                            .I  >]-][[;I_<][,~_]+^.^l!_<[<^,'..''!,```^^i,_[++^i`''```. !;
                             l' i]<]+,^:[_i~.!-{?+-_";[__.'`<+?_!:.     :.-[-, ;`_<<_-l !`
                             .:,;I::".:^:;^"`:,;;I!l""I,,'"";lI!;:"^''`',^I:;^^:"I;,!i!:`
                               .";Il;I`:;IlII';;II:,`I;l;l:`I;!Il""!l!I!""IIl!!",;ll;;'
                                ~,]<^l!~,[?,ll>I_?">!l!-['+ill]_`l!:~[_^i~:-<I,i!:?{l!>
                                ,I;,;I':;;l:;';;:;;;';;I;;,`I;:I;``l;;II^^lllII`";,;:I`
                                  .'            ..      .        .                .
                                  i~}^_i_'>-?+_~>~+?]~>I-~__?];^;_-]-li<:]<_+;+_-!_~__~+_~-I
                                    ^.  .  .....  '...    ''.^.   '"`..... '' .''..'.'.'''''























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


                                                                                              ':,,"^" ;```"'
                                                             ^^``"^`^''..^``"` ^'.`^.'''.`````I}]__><"_;l!l.
                                                             ]1+>i~<[<i!^?+]_<!]!,_};<]!;_~__-+~>~~-:__?-+!
          .''``^``^```^^^^^^^^^^`'''```````````````````'''```'''`''`'''``''` .'..''.'''`''.''.'..''.'.''''`
          `"""","^`^"""""","":::,,"",,,::::::::::::::::,,,:;;;;;;;;;;;;;;;;;:,,,,:,,";;;;;;;:,,,,,",,;;;;;;'
                 l]: "_!i>"<_'
                 :I" '^:il^II`
                               .'''... ..'''''''''''''''..  ....'''```''........''.....
                             "::;l!ilIi!ii!i!:::::::::::ll<>lII;;;;;;;Il,,,::::,::,",I:;.
                            `I ^l~}-~<|]{[~]_",",;;;,,,"_+{+l",:,,":;;+|!l!Iil;!::;i+_ 'l
                            ,,  .,i!!i l<l::+I.......... .;il:;ii;>^..;<~~_i-<:~<1}-],  ;.
                            ^"   "l";l'"!;^"i"          `^li;",+_;!   ;>;    :_!^<;  ~~ ;.
                            ^"     l;          ^~ I<>_: ;`     Il"^!^^l?;^ll^;~i"^>::<?`;.
                            ""     --          :};>]])I :"'..'.I.  '   .  ''      ^     ;.
                            ,"     <i          "?`l]_]I ,!?:>+~+.::                     ;.
                            ^^     ll          ,]I!?-]I :`     <'+-                     ,.
                            ''     >>          ,{^i[?{; :^ `I  ;.                       I.
                            ^^     ~I          ^-,l_+-: :` ',  ^ +_                     !.
                            :,     xf          ;1">)1/! ,' ';  ;.::                     ;.
                            ,"     !;'.   ..`^.'l,,I;l^ ,' .^  i.+_                     ;.
                            ""    .?:;^'"'[,>>"         :` ';  l.;I                     !.
                            ,"    '+   'l~]             "' `I  I.i~                     <.
                            :,    .]^ .I ,!<>i`~~<~<    ,' ^!  ;.>i                     >.
                            :,    .}l ._. i|(}:(/f(;    l^     I.;I                     l.
                            :,     '.  .   ''.  '^'     .      '                        >.
                            ""                                                          >.
                            ``   .                                                      >.
                            `` '~?<<<>ll!li!;>i<i^`:;i!>>I;"'`''^l^^"^":;;l!lI,;^``"""  l.
                            ^, .?}[}{>;>[~[~`+{)_;;l'-[}-`,^;,I:`!     ':,[(]I`:`:,";:' !
                             ;:^+i!!^ ;">>,^^i>+~?[<'!+i: ;:-~_+:;     ':,_!> `";]>>[[I:,
                              `^:",,;"`;"",;^',""^".":"^::`::,":"`:I::!l,lIIIl,^;;;;I^^'
                               ;I<+I^iiI_?>:l+:]-!;I>"~[:!I>;[}">"!;?}^!;iI~~^+lI<?]"_
                               ,!ilI:I;!!>!;:!I!i!I,!;l<Ii:i;!~;>^!li_Ii:i!ii:>:!!>+:<
                                ....'  .....  .'  .  ..     ..             ..'  ... '
                                              `-+;:-!!.?>_<-;~>~+~+>;_+_-_>;?~
                                                "^.'.. '``^`. '`''^'.'^,`",'""
                     ',"^^,,`^::",,^:^      `"..' .''.'. '.'.' ^^.  ..  '  .  .'^... .' ......'^`
                     `!>i>><;l]_~++i-!   '. "><~<:!-~<~~^_+-i-,I_~!<l-i;?__i[Il<}I!~!><^+~!~~I,-}:
                     `lll;l;";l>l!<i     .  :!,:;^"::l:`;;!::`;!:"::;,^l:;;;",I>^,:^:;':,;:,";!^
                     .:lI;lI",:!ll>i'    '  `lIiI^liIi!^!>~i!",iiIl;<l,><~l-;,<<,l>i>!I~l<~i,i~;
                     ,I>>+l,+~_~lI+;     '  ;"!!ill`;I:~<:l^:i!!I^i!::<:`>:;"iIiI
                     '"^^"^'"^"`^"^'     .  l+<[~~+i+<~!i<~!+;<<+I-_i<~_!<~_!_+<,
                                            ,l,l;Ill;"i"i!lil`!II"Il"I!l:^ii!I!'
               .<>;lIll;!I!,   '!;,;!;`III,!"."^::"":^""",:"."",^;I`;I`` :"^."":I:;`^I``::,:.":":^";":;';,;`
               'iii~i!!;<l!:   `>>Il~~;-+ii<<I~+-~+]+>+-->[+"<+~i~-i?_>!"<<<I-~i+<>`">'`~i~+,;i_-:!_i++:-i~`
                               `_?iI+_<~_-_'Ii>++I>-!~~!I>_!ll:III<i l<<;_~+<+~~iI<;~><I~l><<, ;l+;:<<>+~+~.
                               .,>>+<+i_~"}_~?<!!~?`l:,,;iI;.i^i_><+~<<,l!<~>~i"+'II>+-i!}~---<i]?,i;!I!~_!.
                               .<i~~<!~><i<Il<<!~>il+I~<:!~iI_>i<_<~_<+!<~<!I+><>>>>l`^'.^````.`^''"````'".
                               .Il:;<,::;iI^";;:;;:"<:,I'li:;;;::;;l":i!i;I!^>!l;il;,

































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


                                                                                               ^,,,^,`.;."":
                                                             .^^```''`.. ''``^ .`.'`'.''..'^'``<[-?<_l;~:><_
                                                             "}[~<<+~]I+`i--]<!~?,!-[l-_:!-~-~]~><i_~l___]>:
           '``````^^``^^^^^`^^`````````````'''```````'''`````...'''''''''''''.`'''''''''''' ......'.'..'''`^
           "::::::""::,"""^:"":::::::::::::,,":;;;;;;,::;;;;;,,,":;;;;;;;;;;;;:;;;;;;;;;;;;;,,,,,,",,,:;;;;:
                  i<. l>!!i^~i
                 ';I' ""l<I^II
                               ``^'..`''```' `^^^^""^^^``'' . .'^^^^```'...''''`^`^^^'`'
                             ';"l;<-[>_}]?_~[~IIIIII;:::;???i?~illllllI~]??i~~i,",",I_;,I.
                             I^ ::~-_l<-_-<>[i,::,"":::::+-_<?<!""""":;]j)/[?|~Iil~![/i ^I
                             i'   i<!];.++;I:-`                        ,l:Il"II{tiiI>l, .;
                             l'   ^^',".'"'.'^        .                        ^,       ';
                             l'    ... ''''``.`'     l>`^'    .l;.^'     .'!>.`.        'I
                             l'   -)(-;}\f)~())+    ^|!]1<    "|[!(['   .,<(?l)1^       `!
                             l'   /|t"+)ff} ,>!^    ^)l?)<    "1[!|}.   .;>}-!1[^       `i
                             l'   |()>}[~|1-<.      `\l])i    ^{[!|]    .;!}-I1{^       `>
                             l'  .{\||\{I~)tf{`    +_)![)i   ,[)-!\]     ^~(?l){`       `i
                             l'   >1ff-l{_|)":``.  ^,)!](>   ';{}!\{.    ,<][I1)^       .;
                             l'   !l<>??Ii]{>!I?l    Il>]l     .<;__.      .>;--`       .;
                             l'   :::"'.;^"`':,,.    `'":`      ^',"        ^.,,.       .:
                             l'   tf/(+`|+-i;)-f:    >i?\i     .-!(1'      ._:))"       .;
                             l'   ]_{)i-t)];>|[I^    >>_(i     .-!1{'      ._;)1"       .:
                             l'     `^ ,^"^.^:^      ''`"'      ^'^^        ^'"".       `I
                             l'   `'          l<[+"                                     `l
                             l'  :1?                                                    ':
                             l'  :{]                                                    .^
                             l'  ::`   .     .    .'..    . .''''.......       ...'..'. ',
                             l. I-+-_[>:<<>-l;!+_;'.:,+!_+"i`'''^:i,,,""I;l_~~;!I^^^^^' 'I
                             ;" :{]1[_,,[?<?,^<{{_i+^.}-]l ::+i~l":     :^i1-~.;'l!l!<; ";
                             .;,,<liI.^,:!I"'";I!>~-,'iII`',;~i<i:;''.'."^;i;:.:^i>li+>;;.
                               .,;IlI!":IIlll^:;I;;,`ll!l!I^I:I;l;"i!!!!,"lI!i>,"I;lII^'
                                ~,?<^;!_,}?:l>>l-?^+i!I]}'~>!i[}'i;I![['>i:~~i^>I,-{>l~
                                :lI;Il^;I;l;I^;I;l;I`I;I!I;^llliI:`l;I!;,"l;;:I"^I;l!l"

                                               !<-,<i~^I?+<+_i+>_[~>;>-++--l>[l
                                               ..:'.'' .`^^^`..`^^``.'`^,^:^^,^
                      '`"^^" '""^"""""^"","^      ^.'...   .'...   .' ..   . . .```...... ....'..' .  '...
                      I!>>!_:;<><>i?<<?+!~<~  .. ,<>+_>!+:!++i~!i~~l~ll<~,<<]<:>>!~<:<>_iI~i<<?i-}!!?~-+>:
                      ;>Il>!,:IIIi<!!I'Il!l'   . ^l:;;,,:`";I,:,":;":^:::`::I:`";;;:`;,:"`,,,,I,:l"^;,;;,"
                      :iIlli";lll!ii!l:>il~:  .. "!l!iII!":!!Il;Iii,l:;l!"!!_l"IlI!i">lI:,l!!li;>~I:~!>>l;
                      l~i<-+,l!>><~<>i        .. "~>>il;i"Ii>I!llilIi:ii!^li>!"IiiiI"!Il;^IIlI>Il<I^!Ii!!:
                      ";,::;",;,:;:;;I``'      . `;;;I",;`"::,:",::":":::'::i:^:"",;'I:,"`:::,;";l:`!;;I:"
                      <?~>>>~~?^!>>i~?<~<     .. :~~~~!l~"l_+!<ili~l~;i~!,i>>>~i+"ii+i,
                      :l;l:;II:;;^:;;,lI:I'    . `I,:,""",^,,,,":,^""",`;^,,,:"'"^";!"^'"```""'
                      ;!>ii>_~<!l^!I!i~~!_"   .. "i!_>iI;l!l>+!>?lI_i<_:i>~lI><;<><__<I!_i<<+?;
                      ;<<~i<!;`l>l,><         .. ^<i;!!^Ii!l`
                      ^;l;Il:"'II!;lI         .. .I!l>;':!ll^
                      !<~ii++<_?^??~?______?' '' I~><~ii<"!ii+~i>+i>l>_~;-><-<l~~_i;~<<><<+!+~>;>>i<!
                      ",:::":,';,,;;:^;,l,,"     `:",,"",^^,"";,;,;""^^:`,,;;^,:""^^,,"^^,,"","^,^^,^.   '
                      ~?~_]<~_'<-<~l:;]<ii_i  '' ,+<+^Ii-<!-!"+i_'~i!<IiI:>!i_~_"i-->+~><i^~^!~?>i->"_"+~_-~
                                                 :i<I_-;!<]>!+~+i>,!~~>~-><`                           .
                      ^^^^^'"` ""`",^`,`"^`      ':""^""^",`""^,:;'";,^"",`.'.... .  .    .       .   .  .'
                      ~]+-_>_-`~]~_!l"<>i+]"  '' ,_><`.i_+;~- ^<!?.,?i<>>~.l]~-_:'-^^__-i_]',-`"_<--I.>_<<]>
                                                 Ii~+!<<~~~l:__~i]~<l                           .
                      "^"^^`'""""^""'^`^^,'      `;,,^",^,,^^::,";""^.  .. '..  ..  ..
                      <i>>+~I-~--+?~l+~?[?,   .. `<i>?+>l-~+:!<l~,!><__+<+??+];++~~~~>
                                                        .             .

























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


                                                                                              .,,:"`: :^'^:'
                                                             `^''^^``'.' ^'`^' `'.'`.'''.'`^``,[--_>+'~I;<?:
                                                             +[+il<~++i_._-[?ii]<,_?<<[>:_]_+-_~!i~[:<~_]]l
          .`^^^^^^^^^^^^^^^```'`````^^^^^```````^``'''```````''``''`''''''.'.'^'''`'''''.'  ..''.''''.''''`.
          .`,":::::"^,,"",,^`^"`^"":,"""""":^^""^^^",":;;;;;;;;;;;;;;;:,,:,:;;;;;;;;;;;;:,,:,,,:;;;;;;;;;;;`
          "~^+    ,?[+:I-_~i?-.+>!-:!-<>-<?`~<Ili!!,
          "l"!'   .:!":l;,":Il.;!:: "";;iI, l!IIiiI^
                ;>l";_<^;>l;>:,i:l^<I;>I,`;:,:;`:"ll,!iI^l:Il!;;l"
                `:!;">illI,I!;"!;,`::;>;^">;!>i"ll<i:I>>"<l:iil!>;
                             '```````. .`` ''''`''''`'  '..' '^^`",,^`"^^^",^,:"^^``^^
                           'I^I;<-]i_{?[?<{~:::,,,::;l}[+?}_1[~I;:::l<^"",;;?;,,""Ii!"I`
                           :^ ^"!>!;i<i~i!-!^^^^^^"^^^>il!ii+iI,,,,,l_-++-i-[i+!_~\{> 'I
                           :'   >-I+;~;^+"^+_l,                      ,!ll!I>;[tlIIii^ .!
                           :`   `"`''^''^..`^..                              `"       .>
                           l`     ->     !?-1_>`>({(~     _~     ;{?]?'?)1(I          .>
                           l'     ^`     `^^^^.''"^"'     ^`     '"`^".^"",.          .>
                           !`                                                         .l
                           ;`    'l^     "lll!; :I>i"                                 .;
                           "'   ."i^     "i<~+>^:i_?;                                 .I
                           ,'   ;.                                                    .!
                           "'  ^I ..      ..'.. ....      ..                          .;
                           ".  !. _!     >]](_>^~|{{~     ];     >]^-< }l     -<      .;
                           I` :" ^:.     ''''' ..^:'.     .      .`.'. `'     `'      .;
                           l'.l .!                I.                                  .;
                           l.I' :`          ''"`. 'l                                  .;
                           ;;: `_"          !!]~:  :"                                 .;
                           !>  <\{                  !                                 .;
                           +, "!]-                  ^:                                .;
                          '?. !!!"'''. ...'`` .. ..'.!^''.......''''''..''''''''''''. .l
                          I! I:""^^`:l-1>?i!l)]i_;l"`"<`^i`````"i""""":I^^^^^l;''''   '>
                         :"^l:      `:<)1]_-`;)1?_-   ,^ !     'I     `"     "'!>!>?<.^I
                        '!  +:"`''`'^":IlllI"`Iii!l^^`^<`:''.''`:'''``",''.''""!<Il_~I;.
                        l' ;^ ,!!il!":llllI`Iii!lI^li>i~~`!l>i!;`!i<iiI"!!i>!,"!!ilI".
                       "; 'l  >,~>":<i"+-I,l_"_?:!l!:+].]<ll?]'i:;>}{'<!Ii~<`<l"?1_,_
                       !  l'  ^l:,:;`"I:I;;',::;::';;;;:I!;;,;:".;:,lI,`lII;;"`I:;;;"
                      ;^ ":                              :"
                     ^I  l'<-l--<>]~-"                    l>-i]-][_>~]~]~+-?-?i_[[^
                     l'"'::""`"",,"l;,^`.                 .^^`'``'`````````^^"^""^.
                    "II]i][_~i_-}~![---_l
                             .
                                               !>l.>;i +<!!iIl^ilI!iIil;>;;ll,
                                               ^;~'l:!.I!!il;!"l!;::li;,i;Iii:

                   ;<I ~!<;,iil!'
                   :!: ::;".;;";
                      `>i-!<<>I:!>~_>:l~~i:~>i+:i_'i,;i"?"iI:~,!~<-<!i~i;~i!,i+i<,!_.?I:<'!~;;'
                       "^,^"",^`^'::^'^:^^.",':'"^ ..'^."'"`': ";",,"";"`:""'";^;`"".:`.".":^^
                      .-_"~++?~!!?:i~_:I~<~>,>"?<<-_~~<;i<_"~~+>^i~'i~_-<!l+:!i<;I<+:i+~i^><<>>~~I
                        . '''..  ' .'.  '.`^.^'^^"^",^`'^':.^`"^'^"."""^^^`,'""^^'":'^,,^.,:","""`
                   i-;'[?!!!,<i~~>,+_~>_!>
                   ":^ ,,``^.^^:l,',`"`"""
                      '_?~_l:~ili;I<~-_Il!I][<~-<<'~;+ii~il-->",,,~;~+<<_!><<>~~]<~i+_:~<+:l_~i<.
                       ^^`^'.`''`''``":'``''`^`"``'`.'''"`'^I`    ^`"^"^"`:^"^""""l``,`,""'`:"`".
                      '?]~+!l_~i+ll~+[[>i>"><;_}-<]i_`!<:+~?:<ii-_><+^
                                     '`         ...... ...`^ ..`'''''.
                   l_I.]-_]]<<;-<>++l~<_+>+,~?]i
                   '^' ^^^""``'"^`^^^^^^^`^.^""`
                      `~_+--ii"_<<+_i_>_-<<"+]_<;-[<>-]--;!-?-_<-_l]]_~?<_!+-~~[~~;<!l{-+~__-<>I!-_;__?~___"
                      .!><l~>_+_~`'.''.'... .'''.''.'''''.'''^".'' '''''."`'^^''''.''''^^'^``.....'.`''''``
                       "''.:"",^^
                      `_<<+<II"!>i!<I><<+!!,>+~l `" I+!I!l+;i~;">!;!'!l<;lI>II:;>!^!I;l<<:"l,
                      .";:I:,,^;:::,:;;;::"^:lI: '^ :l>_i<<l<+l;i>!<l><<--";l_!I>i;>l+ii]<`;;'"^`^
                                                    '.i<+>~!>l<<I~>~~li'^i^'">>~l;_l]}:;+~_-,i?___`
                                                    '`+]_~i_<~^>_>;;<->]`
                                                   "^ '.''..';;:^:^"^^`^`^`^'.`'''.`.``"'.''..'''..'`'.'...
                                                   ;i.......'_+~+~>+">II<<i~~:!++li-;+>-,_>><+<I+I>++-_l>-~^
                                                            ^+>:++:_!+?i,i<_>>+il+<~+<~+~^~<+;?_";>`_i:l
                                                   `^       .l;^""`I^^""`,"""^:,,:":"^;:".,",`^,^`,`""`'''
                                                   I?..''''  !i_^.+-+!~i<~ !ii_-l! ^> >~> !_ii !~!!I _> !-<'
                                                            'l!>!ii~,:!!i>+!>_;`~l<<ii"l~;^?<:^<>_>l!.>i<I~`
                                                            '!i~+>i<``<~>:i+~II;+<i+>!i^il.!<l^_<>:i_I~~<>~'
                                                            `<!<_<!;  Ili`:i_`!+~>~<>!~^"~^l~i^><l.~--I_l!<'
                                                            `~>+?~>!"+_];I+^l~`l__?+~~i_i!~<__+~"_--]!-;
                                                             .              .              .          `








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


                                                                                               `,,,^:^ ;'`,,.
                                                              ^`'`^``^.'..^'`^. `'.``.'''.'````i[--~-!^~,!-~`
                                                             .-]+>i~<->+l"-+}+i>]II-?I+]l:__+~]_~i<<_;<~_[-;
           .``````^^^^^^^^^^^^```'`````^`````''''''''''''`````''``''`''''...' '`.'''.'''''`  ..'..''''.'''``
           `"""""",:,",:"""""^^^`^`^^`^",::::,,,,,,:,,,"":;;;;;;;;;;;;;;,,:,",,:;;;;;;;;;;;:,,:,,,,:;;;;;;;;.
                    ,~I +<~+!i!!i,il!~il^
                    ";, ,;";":",:"I";::"'
                        l!<^l<~!ll:i^IIi<!i,ll><I:<>l^Ii<>,i:~>:I!<!<<<I:!!I!i:>+:Ii>~ii,l!!;!":>>i;!"!~<!<!'
                       '~iiI>~->~l><>>+i<i<<>>;:<,~!~>+>l>li>!;_!I~>!i!!l<<!!<i>!!i?~<>Ilii>>i!<><>l<l<li-_?^
                       '~_iI<<~!i;<i~<~!<>i>><I"<:!;i<+!:i+i>!,<!I<~!Iiii!ll;i<i`~>~ii!;~i!!~;~<l!~><<l, ;i~`
                       .I~+l>;I~.I>i~ill <""+-i>~?~+^!>i<'!<i`?_i-?i+`i_->-,:~>!`-_-+?_+-"<+'l~~?I"_<_'~;I--^
                       '~+_~_]~:~<_I+<[_~>'                    ..                  ' .' .  . ...   ...     .
                        :^"^`^`.^''.","^``.                             `.                      `
                       '----<_<<~;+<<?+>, `I ;+i[->i>~<!l_<+-+>;i~<><]?";i"`;_<+>_!+~_]-~!:~]<-"<+.
                         . ..'.'.'`''.'.   . .'^"^^`.`''^^^:'``.`''```^. ..'`"`'``'"`^^^^..^^^^. '
                                             .'>+~>I+~[-I"~?+-:i?><-"`"-~-+_~~<;-~>:~~>~<
                                            ^^        ""''^''''^'`"'''^"'`'``'^'.'^'`'''`''..'...'... '..`..
                                            ,i'......'l?-I!_<;_+i_<<~~-+~i:?--~]+^>;>>~<+-<~i>i!_+~~l>->_-i>'
                                                      i,;i>><!:>~il>~l<<-l~;!il!I!Il><i_<<!I_>ll;~<liillll<<'
                                                     .!!i+i>llii~>]_l+i;>+?><l><~il<i]-l<<~!><!I<__<ii_>:+<-'
                                                     '-<!iiliiiiIli!^!i^il!l~;Ii<II!"il^!illl>;I>i!l;i<i^~!i'
                                                     .>!'^! ~I`,
                                            :!.      .:l;,,"`l,.",;";^^",;I":':'^:,`,'l,^'""^":",:^'"^:,"^'"
                                            ^~`''.'..'~+i_<!:~<"><<>-,<><~~i<^+,!_i,<"_~l"<<!!~!?-i,?+--<I"_`
                                                     .<+i>^
                                                     '[-]-;i<,i!"-?+]~_+<_!_>>+-i>,]~]->~:.
                                                      '"^"''"'`` .^"""""",^'`,,,"^.",:,,!.























































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


                                                                                              ":,,`,`.:.^"^
                                                            .^^``^``^.'.'^`^"'.^''`'.``'.`^```~}?-<+;:<,i_I
                                                            `]_~>>~~?!+"l]?[->i?;!__;-[Il?__~_~~!>_~I<_---I
          '''````^^^^^^^^^^^^^^^```````^^^^^^````''''``````''''''''`'''``''. ''..''.'.''''.''.'..'''..'''``
          ^"""""""":::""""""""""^^``^^,""^^""::::,"":;;;;;:,,,,,,::;;;;;;;:,,,::,"""":;;;;I;;;,,:::,,,;;;;;.
                 Il` ^+<+<>>lil!<!i_!!^<<~_li'
                 ,"` ',:";,:^:"'`,;;,,.";I;,>.
                     `<><"i~il!!iI"ll<+I;`l:!<,<>!:Iii>:+;><>:l!i><!<:lI!!~li_;:il<<i!,>ii<Il;">!iIi,!~<ii!.
                     :+ill+~-i~;<>>>~i<i><>i,l!:>;!]~<Il~li-Il~<li<!!Ii<<l>l]~!I-<_>!!I<!>~>i+<i<>i+!>Ii-_-'
                     :~+;!<~<!i;<!<>>!<i><>>";<"!:!-<+"!>>~]:I-<:<<!l~<<>ll:~<l;<~-!>;!>>!>+!-_;~<~~>l` :i<'
                     .>~~!i!>i,<ii<!>^:+i^~<"+<__i<<;~i:_+_l?;_<!;<<>~~!-?:I~_!!^<:~+;>~-i[;>>+~<>l
                     ^l^`'^,^^"^^^'^`,,`^'^"`"^'``^^`,"`',;""^`^'^```'``.`^.``,"^.`^`.`^'`^'^`^"'`'^`^"'''^.
                     ^><~:~+~!~~~~i~+_~<i;~]!>-;~~!<;<_i;]~_i~<>l>-><+~~^l]!>?-?+?i_-;?~>+~l++~-<<I[ll+"?~-`
                     I+:!?]->?!?~,<~>!-;<<+_>+:!-I!!?<+>-!!<>~_li'
                     ':`'^`^^:''"``^`^^'^`^"`^.'```'^"``"^"^^``'`"'..`'```''`.  ..    . . .  ..''
                     `-:!?!!_+:<-_><~<~,>><~><I"~>+?;i~!i+i!;-]!<+]<i[i<>-~[+i:i!<~"_<+<~+]-:l1-_`I>^<-?!!?`
                     ^!><!_>;; ii!+i >~~~+?i?< !~_i`<ll<+l<! i]}!:_-:.-[~?~+}[<l.i<<l"?[-!~?<.I-+]<]_l<`>+<'
                     ,_~~>~<>i!li!>!!!~i_<<i!}l~l~!;>-<~,i>>:l!+l><:' ::^^"^:,`  :,,` ^,,,""`.'`^;"::'. :;,.
                     ">l!+li>I!;"I;;>I;,!!i;:;l>,ill!;I<.I!i~ilili~I
                       ^                                                                   `'
                       ;"   ;-<                                                            :"
                       :`   i1[                                                            :"
                       :`   ;}?                                                            ,^
                       :`  .<:"'''..     ..      ......''..'''... ..............  ......   ;"
                       :' .^:"",,"!:-_l<l,Il?l!<;:I^^^^,:<I:::"^^i^^^^^^,!,,,,,^;i^^^^^'.  l,
                       ;,         ;']}?-i>l^--]~i<^      !'      ~       ;      "!.:,:":"` l"
                       .l"'       :`~~_+_~l "+]++<`      l`      l      .:      ":"-?_?|]l"l
                         ^,":l:",:```^'^::'";"^'^'`,;::::^^,,"":,",I;:;l,"^,^"",^,;"^^:'^,^
                            !:~>I:i`il_+l!,lI~<<,<^i:_<lI;:l;~~,>'!l_-+;>^<;_~>ll^li~_;<^
                            +`?!!'?;>:-];;!+"?>]']I>"__!"<<;;~}`<,+`-_].]l_^-i;"_:"<_1.-;
                            `:`^,:' ,,"",,  :""":' ,,`^,;..;:",;, `;,^":" ,,^,:;..;:,:;,
                   :;'^i:!:,'":".,,:^:`"^"I""',"^I^
                   <-^`~><li<:l!"~!i><:<l<~!l"~I^>
                      "I,l";.:l,.:"",,l,;^'IlI:"';;II'";ii:;`!;:'III:!';,;!;;^'!`,!`",^i;``;:l;:,.,",:I,:;,
                      ,!>-~_::!i^>;!!!!i!;"~<!il`<;i!`;>>i;?,!!!^<i>i<^<lii!i,"-^^>.;;"><:"<i_!>!`>i>!<l++>
                      ,_i~_!!
                   '' .^.   ....'..... '"''.^^` '^' '`'`''```` . '         .  .''.
                   !> ;i<-_!i~_<?~+:_]>>-<?I?]-!_~i'~}<_+_}{>~;+:]-li~~+<<?]<`]1->'+;l+->i-i;--<~-<+l
                      "i!<[l              ..   .                  .... .  . .     ..  .' .'..'......
                      `,^^,`     .  ......
                      "+i<I~>~~~>^l;--~[]"!?_I?i![_~_-_?>I_:<~<I~><++];?_~:-i]+l>?+_?-:_<>+_i.
                        .'''...'. .    .. .'. ''.'``'"``..' .''.`..`'`.''`.' ''''`^^^,'^`'^`'.
                       ,'    '                                                             ^`
                       ;`   l)?                                                            :"
                       :`   !{-                                                            :"
                       :`   l1?'.                                                          l,
                       :`  ^i|}[-^"`...'''^`'`''`^^^^^^^^"`^`````^`^^^^^^^''''''````^^^`'  l,
                       ;' .`~+'``^;"]~!+l,I!1~<+!,,^^^^^`<,``'''`>``^^^^"!``````:!'..''    I,
                       :;   I     ".?][__+!.+}[_+~'      l'      ;       I      `"^<!li~>, l`
                        ;;^!"...'.:">i>>~ll.,l>>>!^''''. :`     .:. ... `I  . .."",~<l!-_l;:
                         .l!:il!!!"";;::::'"l;::l""l!IIII'`lII;l,'"I:;:l"';;:;l!,,i;;:;^'`.
                         .l <"[~l^>:l!]-,!:+"?_-"_"!I?-;Il<:<{}^~`~"_?+^_,!I]~;Il>:-]}^~'
                         l  >,~ll">,ll>_l!:<"!l~^<,!;>~;;I!,;l+`<'~,>~-,+,il~i:!!>I<i?^~`
                        ,:,;;>I;;l,`l;;;[> :i!l;<;`!+!:>l I<i!l<;"'"`^^"  `"^""^  "`'."'
                        i"~-<_i!<~]]?-_+.":!<-_<++>~_<i>l:-_~~<_i>"
                         .              .


























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


                                                                                               ",::`;`';'",:
                                                             .^`'`"``^''.'^`^"..^''``'``''^^^^^<[-_i?II<:~]<
                                                             ^[?<><~<?i_,I?-[~i<];l_-!--ll]___+_<!><<!+__[+;
           `^^^^^^^^^^^^^^^^^^^``````````^^^`^^`^^^^^`^^``'``''```'``'`````'`.^`''''.'.''''.'..''``'``'````^
           "::::::::,"::""":":^^`"````^^^""":,":""""":,,:""^^^",,,,"::,,:,,,",",,:"^^^^""^"^^`"^",,,,,;:,,;:
                    I> '<il`l.!l>^li_i;lIl!!^II'Iiill !l^!^l!,!l;:;>,;ll^!lii;lI! "~>li,"l^;l!,,l!!IIl^;ll.
                    "; "~~-lll+<+i~+!i_<<<>_i!_,!_<>>,>,'I^ll^;;:;ii",:l^I!il;!;I.`l:li""I"I!l,:!lII!!^,i!'
                       `!l!I'i!>ii,I' l :::il,!:^<`!><i.
                       ^i,::I,I"  ;:^Il":l`I,'l';";^:`:;I^
                       ^il<!><>I  "l`li'^I ll`i"<!i:II~><:
                                  ..II"l:.,,
                                  ;:_+i_~;}]^
                                          ]
                                  '   .   :   .
                                 :]__:_,-+~;+_[_--?-?'
                                   .'   . . .........
                         `                                                                   ^
                        '>                  l,]il.                                           !
                        .<   'l<,           :"i;;                                            l
                        .i   "[(l                                                            !
                        .i   `~{;                                                            l
                        .I   ^-t-]"<+                                                        !
                        .;  ^;i>!<;>~!-l!>:::<>,!i,"^^^^^^,l^^^^,,:;"^^^^^;,^^^^^"l"""""""' .<
                        .!         '^i{~-~I<"~1~-<!I      'l      ^:      :`      I.^`'^^``  <
                         ::.       ^,I---?_?` <]_?+<      'l      :;      ,`      ; -[~+[1+`;,
                          `::","":,,:,"``^`^^^`'^^`^^^^^^^^"^"",:",""^^^^`"^^^`^^^"^""""^,::`
                             :lllII;'i!iil!`"ll!l;I'Il>l;!^^!I>!;!.:!l!i!I'l!><i!"^lI!!l!'
                             _.]il ]!+"?}:,!-^~>] -I<^}?!^i<,!]1.<:_'_?1 ?Ii^->:,+i,i_\._I
                             ;!I;!!l`i!I>ll`,lllilI'II,:;I^^!l;ill.:lll>Il'!I;;:!"^lll>l!'

                    i! ^>;!l:l!l"<i<l!i"lI"                                            `````
                    l! `:;i!;;l!^!;I::l^i>l                                          '>"^"^"!
                                                                                     '! ,,^ l.
                                                                                     .:I\+"il
                                                                                     .: :I".;
                                                                                      i|+l-,:
                                                                                     .il:^;"l
                                                                                      ^^^^^"`

                               '''...'. .... ''''''''''' ..... .'''''`'``''''..'''`''`'.
                             ':"l;><<I<+~~<<-l::::;II::I+ii<<<+~;::::I~!;;:;;!<;:"""ll,:,
                             I' :"~~~;??-_!<[:`^^"""""":-><<<_?_,,::;,__~i+>l]+!ll<!)+, I,
                             !    ~lIi:+`l>`^<>I^                     '<~!~iIi;)1l<!~!` ;l
                             ~    ,""`','"".'""'                               ^"       ;I
                             i      }^         <_'+1?]"   l}     `[[[}^<1}{+            ;I
                             i      ^.         `^.`^^^.   '^      ```^''^^^'            :I
                             i                                                          ,:
                             :     .i'     ;i!<<; li~~'                                 '^
                             l      !.     ,!>~~!':>~~`                                 `^
                             i                                                          ^,
                             i      .          '. ''''                                  ^,
                             >     .["         +-`-)[}:                                 ^,
                             <      `           . ....                                  ^"
                             i                                                          `"
                             ;                .'`.                                      ^"
                             ;   ."`          i_-<'                                     ^,
                             ;   l/_                                                    ^,
                             ;   :|?>`!;                                                ":
                             ;  .ll:l^;,    ...   ..............'''''.............''''. :I
                             ;  ^:^`^"I;?_!<I!I[<i>:l^^^^^:!^^^^"l!,,^^^I,^^^^^i^.''.'  ";
                             ;`       :"}\}?_].~|1--<     `;     ""     :'     ;.>i>+_! :"
                             .;,`''''',^!il!l!'^liilI'''''`,.'.''":`^`''"^'''''^`!!l++i;,
                               ."ll!Il^,;;II;';II;::'ll!ll;`!l!l!:"iii!!:"!l!!l"";Il;I`.
                                ~"_~,,i~"--::!_:??"iill-?.<!Ii]-'<lli[['_i:<>!^<;"+[<:>
                                ,lI;;I^:I;l;I`;;;l;I`Ill!!:`l!li;,`l;;!I:^l;;;l"^ll!!l"

                       ^~i!,<-~i~>>i!>>>+<i"~-~"+>!<;i~i:~<!i>:i!<<!l^ii_<ll_<~~!><~~;_<i:>"+lIi,<+~>i<>l~!<
                       "i~+i>il~+i<~i>><_<i"+~~;!~i_!:_~i~<>-~~!>><lI>_"+<i!~>i?:~_I"`:"^'" ^.'"'"","^"^^,^"
                       "!!iII;">ll!IIIlIllI^li>:,l,l!">i!<>I<i>"!i!,;<l"i!!l+I^!.";













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


                                                                                              ",::`;`';.^,,
                                                            .^^``````.'.'`'^" .`''`'.''.'`````~?-->+:I<"<?~.
                                                            ^]?~>!~<-!_"!-+}+i~-:!~+I-];I-<--_+i!i_>;+~~]~:
          '`````````^``^^^^^^^^^`````````````'``'''``````````````''`'`'''... `'..'''''''''.'''''.'.'. .'''`
          ",,,,,,::"^,,^^^""","",^^^^`"`^```^"^^^^``",,":,,,,,,,;;;;;;;:,,,","",":;:;;;;;;I;;;;:,,,,,,,,,:"
                   !>^'?>_>I!l<l^ill!~,il!~il`i!;,i<li!!;Il!i>lI
                   ;I^.lI;:">",:`;::II"l,;;:,.;:"":;;:,;^I:I:::,
                      "!:!;i^ii:,l;lll~:i"l>~l>^>il<";<+_!!,~i"I<~l+l!i<<<!l,_,i,-><<<>l<i<_i<:l;l<!^<~>_l<'
                      `I!ii_!i_>I~i__<<,,^":,":':^":`";::,!^,:^":,,;^;,:,,,^`;':`;,:,:,:I:;:::`"^^,:';;;;,I.
                      ';;;,l;l!!`<!!i;:
                   ^^ ';``^.^''.,'` ''.'l:;'III'";:.;lII:I::^`^^:^'^'"^^^"".';:,.'`'^`^`'^'```'^^``.`''^'
                   ,i ^!i+_iI~!i++<:>i>:<!]:~~~I>>l`ii_?i]<I!:!l~~:<<<>i~-_l^[+~:;>,<<_<<_"~-->[?+<:~<~]>.
                      .:`' ''''''`' "::;"" `^`.` '^`'' .' .'.,'  .'..`..`. .^.'. `'..'  ....'
                      'i<+I->~>-<`I"i-<<<~'+]<l-;~-[][?+-I<<,]~ll+<<_?~l+~il~I~?:_?]~?_:?<~_~i.

                        !                  `',^`                                            ;
                        !    '"'           !l]<~.                                           ;
                        l   '+)i                                                            ;
                        !   '<[;                                                            ;
                        !   .<\_!'                                                          ;
                        l  `;)]~]i:;::"":",,",^":^:"^^""",I,,,^^^^,^^^^^"::""""^^:^^^":::`  ;
                        !   ,<    ^"i\-+_:!"_)!+<;i`.....'<......^l......;;......~"   .     I
                        I"  ;     .':?-]?~-^ _[~?__       >      ';      ""      <'>-_+][i ^l
                         ::;>'`^`'^"^:":;,,^'",,;",''''''`:'``^"^,:^`''''"^''```^I^,::,l!l;;.
                           l!!I!!i:'lllIIl`"!;I;I;'l!i!!i"'!I!!li^,illIlI'l!!<<i,^i!lIl!''.
                          .!~']<!.~l~"-[::!_^_i- ?;<^}]i`<!:l_1'i:<`<]} -I<^?<l^+!">_('i:
                          :^,;I,l;I.!:;<:l"Il!i};!.l,,:::"'I;;i;!.,;;;>:i^iIlI:l;"lII~;i`
                         .il~<<~:!,<!>il<"  ..`~:^<l+!!>_;+_ii+I^<+++->!   ....    .. .
                         'l!<l!i:il~~i<><:      ^:;Ii!il<><>!ii::I!!!i;l'

                   lI ^!;,^;'I;l`;l!l;;;;;I`;::,":;,:;:I""I:,,:I^^;;;l^l;"^:I"::^:,II,,^:':I`:""';::,":^
                   !! ^~~+i>;+_+I~<_<_-<<++:_i<!ii>+_><+:l<i<<:>:!_>~~:~~!l_~>_>>+>~~<i"+;++,+lil<++>~+I
                      :i!<->i^i!l!>?"i<i">~_ii?i~ `+l!<^:<"i~+ll-_~~~+;!~~:<~+!;_~~<~;i`!+>^~i>i-l<>_~<~,
                      ,~:__;+I>"-__+-~:~i_]_~;>~"<_<<"~_+l                                       .
                      ',.^^.^'```^,`^``,"^```'.^.`"^`'^^`^..    .'        ...      .
                      !?<?>~--^!` ii:_+;?_li_?~?i~<+]?~I,_I_;?i+l<i?+?I+_!?]>>_~i<]?I"_-__++_<]]`
                         . ..      ..''. .  . .. . . ..      . .  .......... ...  ... .''......`
                                  I:}]-_-;]?]--?[-~
                                  '.'.  `"I)ill;;;;`
                                           ;
                                 :-~!:<"~i<,<<~<i<><i,>!>:l!!iiil<,!~>!<:
                                 '";;."';,:':::":::;,`:,:.",^:,"";',I:,;"
                      "l",,":;`I. ;^.,,^"^.^^^."`'``,"`'.,',".^^^ ^^ ^,`
                      ;~!+!i<_:~` l!"~<"l<:!~<!_l<>~+i<;:<:]!l_~+;~<^i+l
                                   .:"^"^ '..
                                  ::?~i>_,_{].
                                          .}^
                                  .        "
                                 ;]_~;<;<l<i<_<<~-:_[~-:+]]<<_I_+_~_?_~~i?~>l??-<++_+<
                                   '` ..' .'.'..'' '''' '...'' ``''.^'`"'`''.`'''''`''
                        "                                                                   "
                       '~                  i;]i!                                            ~
                       .<   '>_"           ,"l::                                            <
                       .!   ^])I                                                            <
                       .!   ^]);                                                            <
                       .<  .,{f1};-[--_-[I..     ..................'''`'........'..'.....   !
                       '<  '^"",::i!~}i~+;>;-_;<!"i^^^^^^"l^^^^^^,;,,,:,^I:^^^^",<:`'''.'   I
                        i         `^i1]?~i]^i1]]>!<      .;      .'      :`      <';;:;II, .l
                        ^;^'.     ^";>~~_<~` !~~~i!      ':     .'`      ,'     .!'~+>>]}~"l^
                         .",";",:;``""`^"^'^;^"^"'',:""::``:::;l;,,l;,";^`,:":Il,,I"^^,''"".
                            i;]_!;l:ii__I!">:~<~:i^!;+~;l:I;!__"<'i:~-_,<"il_+l!l;I~-[;+`
                           '~^]!;`+!!I<-^!;-^~!_'~:i,<-I;!<:!<[`~"+^+_]'?;i;~!^l+i,i>{'-"
                            ^;",::. :,,,:: ':",,:` ,:""::  :,",:^ ':"^^:` ,"`^", .:",";^
                       .
                   -~ !~i+_l<_>I]__i_!l+_l                                           ,""^",`
                   '` . '``'.'' '.. ...`"^                                          ^>..^'.>
                                                                                    `I`<l:"~
                                                                                    `;,1>^l~
                                                                                    'l^";: <
                                                                                    .<f-:],i
                                                                                    '!`^^",i
                                                                                     .```^`










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


                                                                                               ,,,:^; `,'"",
                                                             .^^'`"'``.' ```^".'`.'`'.'`.''^''^?[-?<_"i!;+->
                                                             ,}[<i~<~?l-`i__?~i<-,!??l-_:i_~-<__~>>_!l+-?_~"
           '`````````````````````````````````'''`````````'''`'''`. ''.''''... '...'..'.''''.'''''''.'....'''
           ",,,,,,,,,",,,,,,,,,,:::::::::::::,,":;;;;;;;;,,:;;;;;,,,,""""","",,",",,"";::;;I;;;;;;,,,,:,,,,,


                              .^^,^^^"^^^^`'.`^^^^^^^^^`.''''''''`''''.^^""^"^`"""^^'``'
                             ^;^!;_?-!-?--<~?;:I;;;;;;;!]~+_-+?+::IIII~!:;:,,l~,,,""!i:::
                             i  ;"<<i:<i~~l>+^'^^^""^^^:~i>~+-?+:""","-?]~]+>1-!i!~i)-, ;"
                             l   '-iii;_`l~"!]<l^                     '!>Iil;!I|{;!l~l` ,:
                             !    ,,^'`,'"^.'"^'                              .:"       ,:
                             l     .{'      !]+]!^]-]]^   ![     ^][[]'_1}{!            ::
                             l     .,.      ^"""^'""^"    `"     .,",:'^:,:`            II
                             l                                                          ::
                             l     ';.     ,l:lI^ :;l!.                                 ""
                             l     .>      !++-_i'l+?['                                 ",
                            .<                                                          ,,
                            .~                                                          ""
                            .i     `['      l{]{i^[[[]^                                 ``
                            .;     ."       '^^"^.^^"^                                  ^`
                            .I                                                          ,"
                            .i                ...                                       :"
                            .l   .`.         '>+_i                                      :"
                            .;   i(!                                                    :"
                            .I   <f?i`><<i~>`                                           :"
                            .I  'il,;^ll;;;:`.     .....''....... ...... ...... ....... :"
                            .; .^"'``^!;~!Il,>!]l>!,l^^",,:;^^^"^iI^^^^"!"^^^^^<^'^^''  :,
                             l.       !:{11?+?'_1{?-!     '"     !:     l.     <'iI!!<l I^
                             `;,`''''':"!i><!!'"i><i;.'.''`"''''',".....:`....'l^i!li+>;,
                               ',!iil!^;ll!!I^li!ll:^l!i!!;^!!<>i:^!ii!!,"!!ii!,,IIl;I^.
                                l^]~`Il<"-]:li~;[?^<l!:-['~lI!}?'~lI<{['<i:~+i^>;,_{_,>
                                ,llIll^:lli;;`I:;!I;`I:,;:;`l::I;:`IIliI:^llI;l"^IIIlI"
                       ..
                       :<<i:~~>i<>>!ii>?+>!;++ll+!i>;-<li<+!-li>~_<<;Iii~!:+i!<~!~+<;<><;>;i!-<<><l!!><i!I:i
                       "~__<><<!+>>l-~_><!!i_i<!>!<_<>i!-_+l_>?<l~_<ii!>+>ii<~_i~+l<!+<+>!>lii->+~>_i~i~-ii:
                       'l;l:"l:,;""';:I":^";::;^;:;;;;^^lll`:`:;`:!;li"ll;:"lI"^I"'::!;+l`I`I^l;l,I::I:llI:.
                `<I;:ll:","I'   ";,;,"^^`I,^I;lll;^:"'^;:^^"","^,^'^'^::"^""^^"`^",^`'"^^,^,``"^^""``:^"'`^:
                "~<+~~~!l~l~:   Il~+_<!}<~~;iii!l!;~_!l~>!><Ii<_!~~l:<++><<<~<<I<<>Il<i<<i<_l!+<+~+iI~<+!!>>
                                :_+,>!_<>i-"
                    .. ''..   ..          ''  .. .. .
                   .<~'!_?-li-[?<-:__+1!i-~!l-_~i??~<<
                    .            '   ''
                    iI l>~-;iI;<>!;>;+<!,!>!!<<+ii;li<->!^i"!!+<,>><_~><~lI~,:i~i>i>l,<i~i_ii:!_>;<<>
                    .' :->!i!+:><<i:ll><><,!I_<<~,.-liI>ii>>>~"!~><i;!!l<<:l!!ii;ii!i:]+-!i<>;>>_i,l~l"":l^
                       ;_><>><l<i<+!~+~<l~;i;l>>>;"lii:~i<I-<+^,~>~I';":i<!!>i<l:!~i!i<i~i:><:!l+!";>+!>!;^
                       :<i<~!^;I"<<<!~>!.;;i^<il_~i>>i,<;'^:i!, ";<;i~~><'i-l:~<<"+~_+<>:<:!<;:>~II->++>!
                    "' ``''  ''.`   .  '"'. ` .''. ..   .'
                   '?l I<-]ll-~,_~,_-;+]-<l:>~,>i~~-<->!]~-+"
                       ,,`.,^^"`'^`^'  ';;;;;^;;;'^^`^,.',l:;;",I;"^"".
                       l!<"<!+?;!-<+i ."____?l+--"lil,<',~--+?!>?-I;i>'
                                      .lI,^".:"'."":.,^:;,`'" """^:,: II,'::;:,:^^,:,^"^^,:,,,I:;,,I^^^
                                      "_~>+~;i<i;!<>I-+__~iI_;_~_~~+-I~~>l~i_<><:!~<+;l!I>i!>i>~>I!~IIl
                                      ^i>~>I`i+i~"<!+:!><i~<<,:IIi,l~_!!^<<"l<>l+;:+!--:^
                       ,,^'^""^''^^^^  'I:;;;`:;;"'^..:::::"";:,.`:`',^'"',,"^''^,'^`:^"^'
                       I!+"!>_<<;-<+~..:-~++-;<++"`<",++__?i!?_!.I~>"~+;il<iI'`<>+:-~>~>>:
                                       'llIl`lIIl"',.`;lIl^:l;I;.";"`:"^,^:;;"^.`^:'"`""",^
                                      .,__+_I+++-"'<";~_++l>~+_i.l<~,i<l!l<~~I^'<ii,+<~+<iI
























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


                                                                                              `:,,"": ;'^":'
                                                             ^^``^```'.'.^'`^` ^'.`^''``.`^`'`![?_+>!^~:i--^
                                                             _}~>!>+_+!<'_>[-<!->,+}>>{>:__<~~_<>>>_I~~+?+i.
          .```````^^`^^^^^^^^^^^^^^^`'```````````````''''````''''..`'''``..' .`...'....'''..`''''``''.....`.
          '""""",^`^,,,,"""""""",:::,",,,,,,,,,,,,:::,,",;;;;;:::,,;;;;;;,,,,::,:,,,","",,,:;;;;;;;;;:,,,,,'
                 ;-I '<I>Iil~!!<"
                 ,;^  ^',`":",^:`
                   "!; ;;!I':^I:,I,I"i;^^;!";:l!;;^;:Il:"^:`;:!;^I:I;:,:;;!;^;:;;;:;`":;::!,,`:,:,l:^
                   :<l li<~:!;!<>i:I"!>I;i>,i+i>il:~i>>I;,l^lii!,~;_i>_~<;!>"!!~!i!>"l>~ii~iI^~li;>>;
                       i+!>l~i"iI!l;>i<~il ~"~i><. -;!'ii~i!+-, _ii>"^!.!~<:~++>">~!>"~+++,[~I>l~+I`<<~'
                    . .i>+;<<~_+i,>;~__>_~_,i;<;><!i+ii~<!i<:;:><lI`.   .''..''...^`' '.''..'.''''.....
                       "`^.:;","`.".:,"",:,.`."'^:":>`,::'"; ..""^"
                   :>:.!l:;,.,:;,;;I^,l,.:ll,;:,:':,:!;:',I'>^,,:,';:l"l!;,";I;,';::;.;I:`;;l::;:^;:""",
                   ;>I ~<i~!;~<_i?+~?!i+!!+~<<<><!_><>>i"!l;_"ii<i"!!>l>><<;i<<>,<<>>";>>,<l+!i~I;~i>l;i
                      .;!_<+i__<Ii-,_><?<^+li"<~?i<!
                    .. `.             ..        '   .  ..   . ..   ..       . ..       .
                   I-> i<_:i~-i<>!<;+<<+->,:++>>+l~+,+-I><^+i;>>]+<-+~"-~+: <:<+-;i-_?^!+~:-~>__i+~--<<"
                    .. <_]i!i:_~+__~~>li,~+i!1[!i?<<-~:-i~:__<-_<,+><~~i''. .  .'..'''...'.`'''.'`''''..
                       ,:,^'^'":;,;:,^'^.^," ^"^^^.`"` ^". ``^^^ ."^":,'
                      '!Ilii;i: iiii":~il.~i~<>l~!l:;+_>"i<,!i<~+"<~_^!__>+<<+:>i<~+il"+_->+l.<~`~,i+ll_I_<,
                      '>!_<<~+_:><_!^>_!~><!!-l<<!>^`",".`^'`^,""."^^'^,"","":`:"""""`':,"^I; ^^ :',;`":`",`
                      ."^I::l:I^;II".II:l;I:`;`;",;
                   "l: Il""^';"'`^^":."'^`^",^.l, "I:,:"""',",l",',::"":"",,",^^I^^:""`"""'^",""^:"""'^`^^.
                   I~!.~<i_!;i-><_+_~"<I<<i<<ii-l"_<~~~i~iI+<~~>~,<_~>l+<<<!>-I`~^i~<~>II<;!~i!++_~+il?l!]^
                      'i!l;i_'~>,<I~~,!!~+~. ili<:>~+!i!!"+<!"li_~;<,~<~_i<~~ll-"_~l:--~<<I~l;>i+~ii;"
                       ,^``^""' ^"`^'`"^'"'`^^"`^.^",'``:^````:'''``""`""'"`"^^^'''`'`'^`^'^`^```^^`^"^`^`.
                      '><~++>+i:->~<;-+~<-!<<__~i:+[[<Il-<>l~i~;!~+i_<~-_I++_->!;<,>~<<?+>~+->_>~~_!I?+<i-l
                      '<:-;`^<,~~~"~_+`-~::ii}:<ii^:>-<l:~+~!I<i>l_!<_I!^`<+>l+Ii<,i>+<l+'<]~i;l,<~i><+<<;l"
                      '<>i!l>!Ii<+:.><>><?i>i:~<+<I~~i++i~!_~l>~~~i><l]<<I<~~i!~i,<!~+i<l+_+i+<>>!-iii>+_l<"
                      '<_~<i~liI>~l:I!i!~+~;:`l";:",;"I;;,"l;":l;;,:;^l:l"";l:.;''l"IIlI"i;l",;ll.:'";:!;:i`
                      'li>lilli,>lii!>,,~~~`
                   '^' "`.`  ..'``.'' .'. ..'^.'`^.^`''''.`^''.^'..`^'''''..'.'`..''..''... '... .'.
                   i?I.-+++;!<+~-+~]?;!__<-lI_:l<>I~~?i]<:?++<I~_!l--_+->-!<<~-_i!;~->l-+-!I+~?<{_-:
                    '. .'. . .     .       .    .                  .    ...'.  ..               '
                   .]!.?-~_!:_+:!-~->+:~+~<[!-<_+__:l-<>>:>;-!<]?!;++~""-]]?[>>]?iI><^;,[[}]![}}[!i>_;<_"
                      '~<I!!<lI+i?_<<:^,^+__]-[-l~-]!:-_l<~:_<~_+<<>;>li-<,_~<+~!:<i~+-;......... ...  '
                      .":^.^"``;"""^"`   ^'`^.`."^`" .,`.,"'"",^:I,^."``",.",:":;',^":,'
                      '-+~_l"?~";><[i~,i>~l~:iii~>!,"<i!+'i^<i>~I"~><`'+?_]_>I]?!^!i,:I~][{>+{[[<I<_iI-II~~^
                      '<i-;!>~?<>~"llI+~]_??>i_-?I!<<!-i!~+>+~-+>:<l<<!;?++~_;i~!i<<:^^^^""`^"""`'^^'."''`".
                      .""".^I,:,`:  '.:","`^`"^"" ^;^'I`';!l,!::"`,'^::'Il!,i,"I^;I,^
                   ,l" !I;'lI::I:.l:l:'`:;l;:^":I,I`::,!l,^'I`"':l::.",;'`"::"^`;:,:`^;::;^:I:;;,I:;^,:^!;^
                   I_,.!~_;<<_<-~;~I>-!I-_?i!:li>l<:>!i>>!I;!,i"i~~<,i<i:;!i~!i;~>!<:;<ll<:!~~~>Ii!-I!i"i<:
                      'l>~<!"~!!^-+_!_>+_>i,
                   ''  ^ . .   .'          .'. ...   ..'' .'..
                   ;~ `->~]~l!?~]l>+~!<<_+<]+_I<_~!l??+<_i-_ii'
                       ,"`.`"^"``'.`^''^.^``"`^.''.,"`"'.`^.``^`' ^` ''`.`"^`.  "`. .'^.''... ..'`.' .. ''.
                       i>_`!~+_<~;;-+~?<^_<_?~+^;>`?_?-?-_<'++<+>'+: _~_,i[-l'. ~i_^l+-<~+<_l:_~-?++`ii"[_~`
                      `]_+-?~<~;~?[~Il>'+<~I>]-l'
                       '.' .`.  .  .    ...  .'
                   <_ `]<-_i;l+~l;?}!i_i_i:_><I<!-i!ii,;<_+>:<-<_"
                   `" .""",^^^:^`'""''"'^^':^^'`"^'`"`'.^,",`^,^,
                      .<!>^>__+!<:~~<>ili!~<l!"!>~_i>~!I<i!I_<l;>il-?>l^!;l+>_I!-l>,<_<i<><~,<i;l!; _+_;!_+`
                      '!;~>I!<l;!i+>l<_~+:l_<<_<~;>:l>ll~~_+iI!!+i+l!!><>!;i]]iIi:>!i<_<+_>>>_>ll<,I!il~+~i.
                      `><>>:+<Il+~i+;i_i+;l~!><i>I~,i><<<><<<l>~ii~I>>~~~i:<+l+;l<<~lIllll:;I;;::: !;I,!ll'
                      'i;ll,!ll">I.!`li!>`l<:`i;^~i"+^i!`">iliI~,!>lili<>:"~I l"`+^`'
                      'li,:^";"^,:ll""",^;,^""'::^^"":^:i,I:,`:,,"^:I:^`":^`":":l`:I,,'"':l;!lii:,lll":lI:,.
                      `_~>?!I~+l-<<_<<~<i_<<!>I~ii<++i!__i>i<:<iI!!~~>!!+>ll~<<!<i~+!!,`^li!i!<!I!i~!'~_i>~'
                      `~i~<++~~:+!^~>_i<!;+<!->!<>-_!l"i<_!
                                               .























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


                                                                                               ";:;^;".!'",I.
                                                             .""^`"^^"'`'.^^^"'."''^^'^^''`"""^>[--~-l;~:<??'
                                                             '_-~ll<>?i~;"_~]<!>-;;~?;_-::~<___~i!><<:<~+[+:
           '^`^^^^^^^^""""""""""""""^^^"""^^^^^^^^^^```^^^`'`''''`''`...'''''.``''''''''`''....''.`''`'''..'
           '.^^^^^"'''`````'''`"^``'''.'`"::::::::::"""::::":,::::::::,,,,:;:;::;:::;:;:::::,,,,,,:;;;;;:,,"
           >)      ?\_++_-~?-]~^({--<]{-~I
           I_^     !Ii~-/\i[-+<^_~~])?]]|i
                 '..                      '   .   .  .^'. `..'`.''''.......     .           .
                .<,+_i;__<>->_!l<i_]`><_-~!~i!_<~:~_!<-<~I__]~~:<<+>~-~~?}!!?i>^<+;i>>?>_<I>~<!>+-i>:!<l~+!~"
                 !!;:<!<<i><<.!>ii!"<i:!li>;i<><l"~!~l!>><;^i<Ill<+!i,!<ii>i,l!!i<!II!~<:ii"i>i!~i>l;>>~>~<!.
                .<i~il<>i<<<<^ll<!-~_;!!I!<!<i:]~!:~_i]_!I!;i<>Il++!>ll<_><~l>i<>l!!!>>i;i_li>__~->!ii;<;l;,.
                .;;<I,>,l+;l:^i:;"!!;">li~l>l^ :!<^!>_><<^>!!>l":i!"I<"lI~l+?i;!~">i>>>;_:l~I:!<!_;;<+,
                  .'   :`^'`'^'','..'^'
                 .li, "-<<_+<_+;il_]<->`
                                 ...    .....'''.............................. .....
                              ::;;l!iIl!IIII!I;;;;,,,,,:,,,,::::::;;;;::"""";;;,:;::;l;:"
                             ,: ;:+-?l_[}1-~)+,,::,"""":::,,""`^,,:::;;;I:I;+{_"::l;<f< ::
                             I'  .!<!ill   . ...  ....,i!l>il;lI......`>]_}]i]i-)i[<}_I .I
                             ;'   :!>i<>              :>!!<i>!ii              '<+       ';
                             I` ':i<!' I-<'<>::                        ,!l".I   .;:<I   .;
                             I' .`1/};.{/_-[l+}]I_><l>+!Iiii          ';""''~   :_>(-   .;
                             ,.   ?1[l [j[(["_/|_l){-'`..`''          `:   'i   ">!}<   ':
                             ^.   [\]" <[<~>`+[~<^?+!                 `:            .   ."
                             ;'   !-:                                 `;;"  I"          .^
                             !'                                       'i?"  i: l.  .;,, ';
                             l'                                       '>_      -'   "!i ^i
                             I'                                       'i[, `~  '  i;_(l ^>
                             l'                                       `l~, `!     l;_{: `!
                             I'                     :         .^      '^  ,             `I
                             I'   i+,I-<l';}??:    '(I>-I    "]_,_>.    ^:]<^<~'        `I
                             l'   ^".'""' ':",'     ^`^,`    ."^`,"     ''^,',:.        `I
                             l'  "-~                                                    `;
                             ;.  :({                                                    `I
                             ;.  ,l:                                                    `I
                             :. "_>>>~!:l!li::i>~l^^::!;i!"I^``^,;I,"""";;I!><:;,^``^"' `I
                             ;` "}]1[]:^[-<)I`+{[i,:^`[+{i.;";,;,":     ,^i[]-';^",,";" `l
                             'I",~l>l '";+l:.^l>~_-]".<!i ."l_+_<,"     ^`;<l: I^>-i_{_";'
                               ^";,,:I^^;":II^^:,","`;I;,l:`""^^:""llI:I,^:,:;i;:l:"":^^.
                                l;~-l:>!:--i:;~,--;!;!;-["iI>l{[^>"l;-?^iIli+i^il:<]-:<
                                ;I!lI;lII>~l;,i;l<I!:l;l<,i:i;i+;!^!Ii+:i:!lll:!;I>+_Ii
                                 ....'  '....  .  .   .         .      .      .  '''''
                                               ;>l.l;i.;>l!lili,l!I;:Il,,<;III"
                                               ^,~^;:l'"!;I!!!!;":I>!!!:"!Il!!:
                      ..
                      ">>!I~?i<~<~,_+~<_;l_+<I?<>+,<~l!:;!iii<!li!l]<l~+>_~}?__:-[_++i_?+<+]-_[?^~[~+~!_-+]-.
                      i_]_i_-__]<;<i<<[}_I-?-<_-_--}l_~ii~!:<<<ii<!^^''``''^^`` ^"```'.'``^^`^""''^^`^'^"`^^
                      "^,:"::,;l, :"^.;:"'`^"^";"":I.::;"II.:,,;,;:
                       "><>,i.  <_ii~<Il>I>;!><;:i!I~iiii:I<i>lIi:!Ii-<,~<!<i:i!>-!!'
                       `;::^,.  ,:,";:"";:,",::"^,,":,,;,^,:;::";",",::`;;Il,":,;I,,.
                       ,<~>";'  i-~i++i>+I;I<<<:!<>i+i~<i:<+++i!>,<:<<i:+i++Iiii~_!l.
                       ^;;:`:.  II,",:",:";",::`^""^,",""^"::,"^"`,`,:"`:":,^""",:"^.
                       ,>ii;!.  !<iI~<li~!i,i>~;I!!Ii!i>!;li~_<i~l~I<_<;?<_-l<~>~->>`
                       "!;   '  !>;i:^lll!i;!i^II;!ll`:,IlII"
                       ^;;.  '  ;I:I""III,I;!!":>:II:^:;;:ll"
                       ">    ' .!i<I<!]>^~!>il;<I<>i~l"i!i><!'
                       ^:    .  :::^,"l;`;::,"":";:,:^^",^,;"..
                       I_    ` .!i~i~!-<^~><!i;+<+l<li~^i~><++'
                       ",    .  ;:I^;^II;l:;;`::"I:,;!:,`:"",,,,":,:::'"I":"
                       ^`    '  IllI>"li<<I<<^ilIil;i<>I;!;<~!iI;!>i:^`i-i<!
                       :>    '  l!i:>:Il:;<i`i!i!!:lI;l;I>!l:"l,;l;!;:l;;:!^l~!!l
                       ^:    .  :;,;l^:I,,;l^;llI;^I::I^"I;;::I"li:l",:lI";"!!ll;
                       l>    '  !~<!!~>~]:;}]_~^!ii~~~`_!~:i?<<I;+~+'
                       ^,    . .,"::"^"I:`"`^,"`^,^",;`:`"',":,`^:,;'.'`.''''^`'..''.
                       l!    .  il~~~^I<~!_"i<i__~!>+~>!"l!l~<_,Iii>;><<+_><_]~<"!?~+'
                       ^iIi:i!l<I,'i!l!>!;`!     l,I";"I^,::^",:I;"^^"";;`"^,,";:',,;",,I"";',:"I"^"""::":;'
                       ,>I:^;;Iil^"<il!ii!"i  ' .<<+~-!>:>iilii<><!;:l;!<;i!l>ii-:~>>!il+ii<,<~i+Il>>i>>!++:
                                                 i~<~!!i
                       "i;>"llIil;`i!;!<!:^;  .  l;:^;^:":,;^"",;:"^,";:"`^^",";,',",""^;"^:'""";``^^^,:^,:'
                       :~ll^Il!>!:"~>l><<!^;  `  <<ii?I;;_i+l<i>>i>:!;i><;>iI~i~-:_><<<I_<i+,+~<-;l><!<+i__,
                                                .i><_!>i
                       "l:I"lI;lIl`!!Il!I"^l  .  I::`,`I^,""`^"";:^^`^""^'```^^:^.^^"^^^"``^'"^`,''`'`""`^^.
                       ;+!;"!!i~iI:_+><<~i:>  ` .>><i~;!:_<~l~<~++>l;Ii<+:>>I<>--:_<><~i<><i;_+i_li<ii~~>--:
                                                .>~~_~<>
                                                 '`... '








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


                                                                                               ^^""': ,^'`^`
                                                             .'''``''' . ..''' ....'.... ..'.'"-]-?!?`~;;-~,
                                                             i]~<i~~+-l-._+-]~;_~,<]~I]_:>__]??_<~~]I~~+][<`
           ``^^^^^^^^^^^^````````^^^````'^^^```````'''````''.''''..'.''''`'''.^''.'''''`'''.'.''''`'`''''``'
          .",,:::""""""""^^`",,::,"":"^^"",,::,,::""^",:,,"""^^^^``^""""::":,,""^""^,"::,;,,",^",:::::;""^"'
                "_i>><<!l>I~'   `<!I'!>>'>!!'";I,:<!>^<!i<!l'<<!!++l.!!>,`>^I!i>!:;i":I;l':I:'!;;l::I;`:`!;,
                ^;:!!II,"l"I'   :>-~;<<<,_++l!<!,"l:"':,I!;^^i!;Ili!`!>>I"i^iiii>ll+"!<i<"ii!^<i<<~~~i^I"i>l
                                ,iiliil+::i>:;i'
                                ::"^l:^l,;^,II;,,::"::,.I:^"::""""I:,:,,:,:":",";,^":`,""^"":^':::;:`"^"^^,^
                                ll~!<+~~i_!--_+~i~+I]+?I+]<~?]_I>i??+<-++!<+~>-li~lI>l?<~^i]-~l~!<~>i+~>i]~>
                                I>:i<.!ll~<! >++lIi,+<l;;!i~~ll,i;<i!li!<+>,I!i!~<<ll_ll>l iII!>>,~<i!ii!_!i
                                ;~>>!>~__<il~;~i>i'_<Il~~!I!:_>~+<i>i:<,_<li~~+!!+><+<_-_l<!;<i<~~<<i_>i_~>;
                                l++I+-}<<-~+?+?__l!i~l_-[l!_~_-i_]--+~+>i,";;l!"";":;:;:;^,l,I,;;I"i";:,;::'
                                ^li"l^>;:I;::lIll"iIl:!,~"l!!I!^ll!ii!lil
                 '!:  ;::,,"";l,,.:;^^`"^`
                 :~! .li+l>l;!<>>:lli-~<~I
                                 .  ..    .....''''''`''.  .......'......''.......''..
                             ::;I!<~i!+~>il>>II;II:;:;i!>il;:;:,,,,,",:"",;I",:;l!;:;I::.
                            "; ":i]~i![{{-i1?,;;;""^^.!i[~~,:""^^^^`"";l!I<-I:"I:1>l<_ ^I
                            :^  .,><>>>.      ...>l>~+<I`>:!"~<~>><I.'l?++_<?+-|i]])[!  "
                            :"   'l>l!~'         !;>!<<:"-;l^!<~i~~;         .i+.       "
                            :^ .:!l!~:                                ,i!: l    :"<!.   l
                            :`  '_())]?-~+-!                         'l""` ~   '~!)['   !
                            :`   >][}/)::"..                         ';   .-.  .+!)}'   l
                            :`   >1-l--[[,                           'I   .-.  .>:]?'   !
                            ;`   <({++-_?^                           'I;;  ,            ;
                            :`   <)]l~_]?^                           'i?I  l  ;.   I,I  ;
                            :`   ?|-  .^.                            'i+      +"   ^;?  >
                            :`   .`" .^'                '^^.""'^^''''"!]; .~  '. l>~)+ .i
                            "'   ~)|][t~"ll            '!--"[[ii]i,!\\!<" .>     :i<}i  l
                            `.   :;^<I:.l~i      ':         `       <>^'"       ";      l
                            ,'   l~:"~<;''[_-l   .+,__'     ili-;      :~:+i    l]:+i   l
                            ,'   ^".'^"' ':^"` :i]->""      .`^,`       ``:,    .`^;:   l
                            `.                  .'.                                     l
                            ,'  .!!`,                                                  .i
                            l'  "i;`"            ..                                    .!
                            ;' "__~<-_ii>i<!;ii<I`'!;~!<<,i`'''^;!:,""";ll!!!:;:^^""'. .;
                            ;^ ^{]}[[il_}~[i^-){<;;i.[-[<.!^!Il:"l     :,i}]?","",,:;; .l
                            .I,,_!il'.lI~l,`^i><++]!`ii!` :I]__<::.  . ""I~!I ,^i_i+[[;;^
                              '^";::I:',",:I"':",:;",l::;l^":,,;;^:l;l!I^:;;;l;"::,";"^.
                               ^<I}~'>Il!]-`l!;+++">!,_}!:!>,-1;!;<:[1:!I>:_<^<l!l?{"_'
                               '!Ill:l"l!><;:,lii<l;:lI!ll,IIliIl^lI!<Il"!;lI,i,lIl~;>'
                                                            .  .   .  .   ....   .  '
                       :;.  '. l{>!-:!<~,<<<l;>i"<<Ii!_]<'
                       "^   .. "!,,;^;::'"::``":`^;"";;;;.
                      .l    '. I[~i_:>+-~iI~<>!~-<;
                                 ... ...'^.'.I:^';^".,^`^`^^",^^.,"''`'`'`^''''.
                                             !!?`_I;.><~i-<l<?-_;>>i??~+il?+~-+l

                ;l""":,""",:    l,^`,^'`^,^:"'^`^^^^"`^^`^,^'``^`";'`"`^ ^^`'`'`^''''"`''`''..'.''.'`.'.'''.
                ~+~_-~+i<>i-   .<i>,><:>+<>_-:~<_><-]!>++~?_,>--~~]>?+><`i~~;-ii_~!`'<`'~~+-;`~_?:!__~_,<!~,
                               ._<!:~<<~<_-';l><_I!)<<_>!i_>:!:;:`:l.l<!,_<~<<<<i:~">>i:+:l<~I ;><I;<<<~_~_`
                                ;~i~-+~i-:[-i-->~<]:II;:I^l;"i:l_>~+!~~!;i~_<++:+"iI<~->!{?_-+<>_]:!l!l!l-<`
                                Ili>ii~<<:i!I<i;<iiliIi!I:!!"~ll~+_<-~~Il!<!!<l;>:l!!:I,`>I:::":I;`I","".:^
                                >ii!_iI>!+i:,!l;>!ll~I;>`>~!<>l!l!><!l_++!i_"i<~!-ill



























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


                                                                                               '^""'^` ,.'^".
                                                              ''.'`'''... '..'. ..... ... .....![[]~~i`~"l?}^
                                                              -{~>i+<?~+!"-+?+<i[i;_]l<}>;-_---_+>+--;+_-]-l
           .'`````^^^^^^^````^^^`^``````'''````'''''''''''''''''''..'.'''''.' .`.'''''.''.'..`.`..''''.'```^.
           '""""",,",::"^``^^""",,"^^^``^",;;;;:,,""""""",;;;;:,,;;;;;;;;;;::::,;II;I;:,,,:IIIII:,,::,;III;I'
                  :_; '_>>>;++ii^iII!li!,
                  ,l: .,;Il";;l:'``:>;l;^
                               '^"^`'`' '^"`''^^,,,,"","^.''^^"""^`````""""^`^``^^.'`'`'
                             .l,:!+-?~<[_]_!_<,,:::;;II+>-~~:;llI:,,:::;;;,;!^",",i:^:l,I'
                             ," ^"!<!;;<~->I_~::"^'`''^ll_~~"''.''",,""I+<<?]+!!~;{<_-< '>
                             :'   l-_]-_         ._+]-,~+::;?--]_-`    I_~~<l<ll_i1\{~:  ~
                             !^   `,:;::          "^::',:^^`:;:;;:.               ^l.    !
                             i" 'I~_][l """^'                         .Ii<; ~   `i;]+    !
                             i^   -1111[~~__:                         `I .  i   `-i\[    i
                             l`   _?]}j[^!`                           `I   .[   ^]<t}.  .~
                             ;'   ~1_:+~?-`                           `;    !   .;,i!   .~
                             ;'   -1[-{--[^                           .:~l .;           .<
                             l`   -|}:>~?i                            .I]'  '  ~'   iI! .I
                             >`   ~+:                                  !-   '  ~` ''^l> .;
                             <`   ^I<`!+;               .:>!^+~:;~;::>!>1: ^?     ~>]t! .;
                             >`   }{[)11l!->            .:il^<>,"i:,:t(;I` .:     ^";>^ '!
                             l'   ``.:,'.,::''.   ^i ..      ,       ^,.^:       li     'i
                             l'   <_,:-<;'^{]-I '':-;-+.     !l+[I      ;~I]~    ;>l[<  .;
                             l'                 ;i?>;                      ..      .'.  'I
                             l'                                                         .;
                             I'  `<i";                                                  'l
                             ,.  ;;^`` .     .   .'''.    ..'''.........         ...... `>
                             ,  ;]]]?[<:<>>_I;~<_l'':,-!+<"!^``'',I^^",^I;;+~-;I:`'`""' `>
                             ;" ,1-]]~::]?<]:'_{[~!>" [-?I ::+!il""     :^!{?_';`;IIl!;.^l
                             .;::<;I;.`:;iI:^,IIii<~;`il!^`:;->>!,:''..."";i;" ,^l<li+_;:.
                               .^;;I;l"^!l!!i""II;,:`I!!li!^;:;:;;"i!!ll:"I;Il!,^IlI;I^'
                                i;~+!'<i,~-i,>+,-_lIlI"+}"i!<;]}'l:!I_['<!l<<<`_!;<{]"?
                                ^lI;lI"^I;llI^:I;llI`:I;l;l^l!!i;;`lI;i;;^ll;;;I"I;IiII

                                              `~~i"-i<`[_+-!][_>:~>i+<~<;<-!<~~;
                                               .":.^`` '"",'^",`''`^l,:"'`:^":,`
                           .
                 .+]^ <(}>!-<+?+?i`
                  `'. .`'.  '",'`..
                              '"""^^^"""^`"^^:;:"""""""^^^^,,:,""""""";,""^``",,:,"""^"^
                             ,;'I,?-]!]}[1+_|<II;,,",:~}{~{]]:;::::::;lI;:<{[[~_!;:,"~:^I'
                             I  '`!!l;ll:;":l"^^`"::,^;!II!ll```````^"l]1_1}])>[-~]~{-, ^"
                             ;    <-__]~         ^+{! i?+_]?~          "^'`'.^;1]^"`"^. '^
                             :                ;l:i!lI;,               .`", .^   ''','   ^,
                             I    >~>>~<<<l   ;lI><il;I               ,!l!':i . !i+/+   ^,
                             !   '{/r~;:,:"                           ,^   "!   l!~\_   ^,
                             !      `                                 ,"   .'   .``,^   ^,
                             !   '^`'^^^^^^^^^'.''````"^^^^^^^"""""^``;""               ^,
                             !   .''''''''''''i<<~++~<'''''''''````'''`![l!<l '^   ':^. ^,
                             !                ;l!;;!;;                '+l`!I^ ^_   ';>; ,;
                             >                                        "~-. ^; .,  i,<}: ;l
                             <                                        ">-` ;!     +!))^ ;I
                             i                    ^.         `        ".'               ;l
                             l    ll`l!;I.;~<l^   I!"!:     .~^!!'    "I<;l:            :;
                             l   .!;':lI, ;~>l^ II_+l!;      ::i>'    !-,:<I            ",
                             !                  ",I".                 '.                ,:
                             <                                                          ,:
                             !    ``                                                    ,:
                             l  ">_?:;;:,::"^,"","^,:,:,:,^"`^```,,""```^```^""^`````^. ,:
                             !  !??[})!;[~_{^l-{]".^I;{+}!"I'''`'!:''.'.!^~[-]^l''.'.'. ,:
                             ;,.!?>-i.^;+-Il ;~_]?]}"^?>< `"+_?]<,'     ;'++~" l^_++?[<'l`
                              ^,,:"","^^""^,",,:,":,^",^":,:;;,",^^"^`^"^^:"""",":"^:;::'
                                ;;~i:!,!;+~lI"!I~<;!,l!+>:l,li_i;;"l~->I;;l~~>l:Il~_!!"
                                !:-!"!!_:?-:!l<l_-"<!!l_]"+!Ii_~"iI;~]_"<>:~i;:!>,~}!!>
                                ':^^," ':",,^ ^:""^' ^^`":  "`'^"  ,``^, .,`^^, ',`":,
                                                 '^  ''' '""''". .. . ` .. .
                                                 I!-:i>_"<{_+!~>_?~+<:?+>++_^
                                                                 .














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


                                                                                               ^^^^'^ '".`^^
                                                             .``''`..' . ....'  ...........'..'-[_?!_"li,<?+
                                                             ,1?>i~~~[i-^!+--~>~-:!?]I[];!-+?~-++<<?~!+-??_:
           ^^^^`'''`^`^^^^^`^^``````^```````````'''''''..'....''''.''..'.'''' `''.'''..'.'' ''''''`''..''```
           `"::,"",'''^^"^",^^``^'`^":;;;;;;;;;:,"":;;;,,:,,,,;;;;;;;:::::::,;;IIIII;:::,,:;IIIII;,,,::,;II:
           _>      {\[<>!];"}]~<!__~l"
           ~_^     ]1[[}]{~:}?[)\}{)f!
                                             ..
                ^-:~]-+?{+<,<<+[_^-++__+l!+_;+i_!l{+i?<?l>_-<-!!-!<~<~_l~]+l_<~?"<?->I_<+_<+I
                .`'^,`."^'''.'`^^ .^^^,``^":`^.^""'`^'''.'`'.'`'^^^^``^''`^.``"` `^^^."^^^'^`
                "<i>_< ~~<'+--?-l-'~:;1!i~>? !~_++^._<i !<i_-i<';~'++i?,"_-[::-+~~]:"-~"I_<+<[-?,^_~~}[[--?l
                :{!?+___+`-]~~~+[{;?+~+~+-_'<i<;~>_-_>i}>-~_-_i... ...'..'''..'``'"'.`'.'^``'^'`. ''...'.'..
                ':`'..^'` ^^.`''^` `"`. ``` "^^..`^'^'',^'.."^'
                '_+-+_,-__~+<:-i<~~~Il<<:_+->~++?;i~:~<>i~~<I_>!i___{!i++"
                   ''^ ..` .` ''''.'.... ^''.'^''..".```'`',`.'`.'^^"'`,;`
                 `i>' >~i>~~l,_I<i>,?+!>lI<i_IIil!>l~>,_!i!;ii>`
                 '"". ^",;:I;`:."^:`:,,:"^,;I"`,;^:",l`;:;;;;;;.
                               `''.` .   ..  `''''''''' ..    .'''`^`'````.`'.'..''''.`
                             ":^II_-+l-?-+i__::::::;l!-}}<]-i:::;;:;::,"""i+~<;i!""";<":^
                            .l  :;-+>;+<+<I++"""""""^^!<~i-~l^""",::::I~+>({(\i|?li~}|. !.
                            'I   "~!-I^~lI          i+?~~;            ^!!!l::I"!~|(~_l. I'
                            ':   ';:"''^'`  ''.     '^""^''.' .'        `.       "^     I'
                            ',   :{]'       1_<'      ;l '{[};]1" ;~   I_' ]l       "+  I'
                            `;   ;{+'       \+_,      II ,[[{!()" ^?,  l~. >;       `!  I'
                            `;   :(}^       /_["      ^^ ^^,I"!l' ,]`  ;>  l,    "":!^  i'
                            `;   :/{'      .\~[,                  I}   :< .]i    >+-t<  I'
                            `;   ,)['      .t+{;            . ''  :+   :<. `     '''"`  ;.
                            `;              ]>_:      `"    <l[):       ,' _:       "<  ;.
                            `;                        :>    <l])l `!'  ^!. ]i       I_  ;.
                            ',                        !;    <I[)l '+"  "<. 1l       `:  ;.
                            `,                        ;~"   +l{|I `>`   "' ]l       `:  ;.
                            ^I                        I["   ''^~! .;'   :' ]!       ;_  ;.
                            ^l                  '^^'  ;<'       .       :' \_^^^.   ">  !.
                            `:   ^:            'i_->                    ,'  I|?<:       i.
                            ',  .~\,                                                    ;.
                            `;  .+(^                                                    ;.
                            ^I  `i,   '. .  '.  '``'.    ...'''`'.........    ...'..'.  ^
                            ^, ._-_-[]!l_i+<"~+?_^';;<<+-:l"..'``!^^^^^^I:+?+i,l``''..  "
                            'l. -}?[-,;![~<!.<}1-<+<'~[?~ ;,_<~i,:      :"][-^'"">ll_>^.!
                             `:,l!;;".:";I""^:;l!i+!,li;,`""!lll:"`''''^;,i;:.^^,<lI~<l;`
                               .,;!!;!^IIiill^Ilii;;:!!i!!:,I!<ll,,!i<i!:Iliii!";l<>II'
                                !"+i'i!i;-[^i!l<+]`<l:i+-`i<:<]<,i!:>}_,<>,-<:!><,_1:i,
                                ^;,:;: ":",:" ,""::^.:,"":'';""I;'.;,,::'^;,,;I.";,:::.
                                      `   .  . '       ..    .    .
                                     "~-l;]"+!"?__+-],_>>~_<>{~+?;+-[]I~>!~_+]><?+]<<-_<
                                        .           .                         '   .
                      I;,',,I^::"^`I,,;".,:,""I,,"'""`^^'^"""^^^^"'I"'::";,::; ^;:^"",,"^;`,",,;`.^``^:^"""'
                      i!_!>-?-~-~_l_++_]I>-+>l?<i~:<>l;;;<>>ii<!;~:-_li+~iI<_<,I]~><<~_!i[><!<++l;?<>,~~+~?:
                      -<>>l~~~"-~~>_l:<I~+!<"
                       "^      .:``"".^`^^^^^``'``''
                       !;   .' `~,+~<,!>ii!_~iII_<<~
                       :"    . .I,lI:`;:;;:I;:"";:;"
                       ^`    .  ,"ilI^lIII:>l;":!l!:
                       <;   .' `+:>ii"lI!!!ili;;<i!I
                       :'    . '"^:::^""",":,"`^:":"
                      .,    .' ":>i!li~!<:;++<i
                       ^'    .  "",:,,::,:`,;":.
                       ;'   .' ';;!>lI>~!>">~!<'
                       >"   .. ,>^lIllI!II":i!l,
                       :^    . ^;`:::,"!::':!;I^
                       i.   .. ,i>><>+_,:l>ili_!~;~~l_'
                       ,`'   . '"",,,::^^"""",:^"'",^,.'.'`' ....' . .
                      .liI  .' "l<_+<~-:I>>ii<_ii:>_!>^?!<-<"<<~_?IiI_];
                       II    . ^:`""::,::,'";,:^I:`;:,l"              .
                       ;l   .. ""^lIIIl<l!^!~li"!i`>>!<^
                      .<I^  .. ,!i!iii<^!!:`~i>:;l!;;lI!+"
                       "`'  .. `^:;:;;I`,''`li!^:I^""l;:l.
                       ~"   .. "]~<i-_"~<_~_;!i><!+~+:I-+<<
                       ;"      ';:"","^::,;"`""^^"^``.'^^^`
                       <<   .. "+>>~+,]>l>-!:-~<~~
                       l;`   . `I::":^I;:"I"`:,::;":":::;;l,`""^,""",,""`;^^::^,'
                       i>"  .. ^>ii>>,-~!!<l:_<~+<I>!~>l~<->:~l!]i<ii!~<:>;l__>_,










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


                                                                                               .,,""^: ;``",'
                                                              '`'''''`'.. '.''' '..''.... .'`'':]?--<~`-;!?[:
                                                              ~1<<l>~_-!~.+~?+~l_<"<_<<]<:+_??_-+I!~]:<~?-[<.
           .`^^^^^^^`''''````````^^^^`'`````````````````''''''''''''`''''...'..`.'.'.'..'.'..'.''''`''.'''''.
           ',:::::::,"""^`",:::::""""""^`^,,,,,",;;;;;;;,"":;;;;;;;;;;;;;,,",,:;;;;;;;;:::::::I;IIIIIII;;;,:`
                        !<.     .~l>I!"ili,lI!!!l
                        "I.  .. ';:::I`;I;`;;::lI.
                        l!:  .' ^-+<>I~i;Ilii~~l
                        ,:.   . ';,"^",,^^":^":`.
                        _+   .' "}:!<!><~<+i,<_i~
                        ,,    . 'l::";:"I!."i;:;^:;;l::.
                        :;   .. .l!l^<i!_! :i!iI`lil>iI
                        <:   .. "i:~<I'!i_i!'Ill!l!;;i<lI"!;!<i>^
                        I"    . ';,I;,`;III;`,;,I;;,;lI:"`,,";II.
                       .<I<  .' ^+>i!?;~><+i_<^<!!!!<<!
                        ;^.   . ':,:",^;,":":"',"^"""""
                        >,   .' `<>>i~"?~i<!->^<!li>><;
                        i;.  .. ,>Il,^I":;,;"`I:::l^,,,I::;`:;I;l;I,^:;::I::"
                        I"   .. ">!i";i;~>I!,"!iii>"lliI,:<^llli>ii;">>iIiI!"
                        <<:  .. ;]>~l;<l!>!i;:!i!;i<ll`l!Iilil^!Illil~:"iliI~i>;
                        ,"`   . ^I:I^:;"!l,;^":::";::^`::,,",l`l",;:;l,"!I;:I:;"
                       .+-I  .. :+i+l,l!!<<l^l^>>i!_i<[<"<-~i>]_>!
                        II'   . ^I,;^^"",::^",^":,:::`''.''''''''.
                        >l   .. ">i<;:!!li~;,<;`>>~+~
                       .ii,  .. ,<Il;;I;l":llII>!I;l^ii;"!lI,!I;I^!l!^
                        ;l^  .. ^!l!ll;:l";ilI,I!:"!,:l;`!Il,i;li"il+,
                       .<<"  .. :?i!~^!!ii+i>-i"<i~~<I^ii!<<+
                        ":'     ^;`,,^,",:"^::"^;:,:,^`,:"":,.....'
                       .i!   .. I+l!>~_";!I<<~>i+_<>l;~,<~`<?~+_++;
                       .;;"  .. ,!",;:;^";",,:,^,;:,"',,""l;^,:",::":
                       .;i:  .. ,il;!>~^;!,ll~<l>_<<I:+ii<?-,!?<~__<<
                       ._<;  .. I_Ili`:!:;i!^
                        ;;,``^' ^;,;;`,::":;`  .
                       '?+[_!il .  l]l"___,i:-<]-<
                        ;I:,:;' .. ":,,^",",,^^`^"'`;`^.
                        -+><~<' '  l>~-I><<~+>+,;;>i]+>`
                 :I`^^,^`''`"    :^''^'.'`^^''`^.''' .'``,^'"``..^`.``^'.^`^'.'``"`'''.'.'.."''.........^'.`
                 ~_~_++~i<<<]   .ii>l~+;++_-~i!_:_~<I[?->_<_[~>:"~_l~-?<I<!~_;-__]-~+_;]_-~l[~];l-<>~<~:]+~]^
                                 <;i-_<?+<~l<+_i+:+~I:?;_~-::[_?:
                                 .  .`..`.'  ....  '  ' ''. .'..
                  ![I "____?_,~>i_+>i}><_"<+_~:iI}i[]<,]lI_!~<~<!>++l~]<+<
                  `^'  '`"^^,.' .'``'^`^^.'^"".''^^`^`.,''"`'`""^^^"''""^^
                              '"""^^^^^```^^`^"""^^"^",",,"","""^^^^^"^^^^"^^^^^^,"""^"^.
                             ";'!l]1)i_1{)[?\~,:,,,,:,>{{-]]-,;l;::::::,,:<{}}<<}:"""-!`I`
                             I  '`l;l"";l!:,;"`````````,",IIl,,^^`````,~}~{}]|<-(<[~1}! ^!
                             ;.   ~i+~'~>>.               <]>+[.       ^`"^`.^:]}""^,"' `I
                             :.   ";^       ^::        ,. ^:,'`;^  "    ": '`        .. `I
                             ^   .[}>       ~]>!       +. +)1<~|~  ]"  ']; i1`       -: `I
                             ^   .]]l       <]i~       <.'>+)<~|_  ~~  `-; `I.       "' `I
                             I.   ]{i       <)-_       ` ...^'`,`  [;  .-I :~`   .i:-~. `;
                             I.  .[|i       <|_~                   ?^  .-, l<'   .+l}[' ^l
                             I.   ~];       ~|?]       .    .^^:^  i`   >" `'        ^. ^!
                             ;.             ;i;l       :'   "_~|-        l >-'       _, `;
                             ^                         _'   ,_>1-  ~>   <i !?'       _" ^l
                             "                         ~    ,_<1+  ;I   Il >{.       `. ^i
                             ,                         <>   ^<~1+  >l   .l !~.       l' "i
                             ^                         +<    . '>  .'   '! !)'       _, ^l
                             :                  ,,>;^  ;,               `i l]i<l:    l^ ';
                             ;   `+"            ;;<l"                   .,   >?;:       ^!
                             ;   It]                                                    ^i
                             ;   ,};                                                    ^I
                             ;  ^i;,"^""`^^`^,^`^^^^"^````":,,^``^^`````^^^''.'``'``^^' `:
                             I  l[][]|<I?++[;!_[?;..i"?~}+"<``''';;'''''I">[?]";^'.'''. ';
                             ,:.I[<?<^";<-!!.;<[]_]]I.--_'.:i-+-l;"     ,'_-+l ".<~<-[!.;^
                              ^:,I::""",;;:;;,^,,,::"^:",,,,:I:,,^"^^``"^^::""^^^,,":l;:^
                                "l!>l;;:li>>l"II>iII"II+<l!"lI+<:l`!l~<;l"ll<iIl"l!<iII
                                !I<>l^+<;~-<"l_:++iIl>,-],i!>;-[^<;>l]{`-!li~!'-iI<-[^]
                                .,""",. ::,::.':^"," `:^`," ""^:;^ ":,",^ ,"^":' :::;;`
                                 ''  ' '  '.  .   ..'  .^  . ..   . ' .'        '       ..  .
                                 ><[`];il.?_?-_{l!<;+~_I{?~]!>-]-:!;[]-}_`]+I-~!-~?~~]]~i]+<]:
                                   '         . .                          .       . ....  . .











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


                                                                                              ',"""^" :'`^^
                                                             '`''`''`... '''`' '..''.... .'```l[?-+~<`<:l-i.
                                                             _}~ii><]~<i`-+]+~!?i:_]i+]l;~?-_?_~i~<-l__-?-!.
          .''''''```''`````^`^^`^^^````````^`````````'''````''''''''.''..'.'..`...'.'.''''. ..''.`'''.''''`.
          `,"""""^`^""^^```^,"",""""`^^`"","":,:,",,"^^`",",;;;;;;;;;:,,,,,",,",:;;;;;;;;::::::::;IIIII;,::.
                 l?I ^+i>><i`li;>!ll]I!>"<l>!^;^<!IIll;~!>_!'
                 :!, ';:ilIi`:"^::;^I:II`:;!l`,':l;;:;,Illl!'
                              '``. ```.'```..^^"''^`'.   .  `^^^^^^^^^^^""``'.'.'``"``'
                            'l"!!?[1+]|({[-1<;;;::;;:i]]+?]-:::::::,;;:,:!]]_>!-;,;;_l,I.
                            I' ""i>!:i<~<!l_!:::::,,`,il!<<<"^,,,,,"^,!?<?({\_<(i_>?|< ^;
                            l.   ~I~<^~><.         "?<<{:i-~-?'      .;i;l;"!!{|;i!+i" 'I
                            !.   ","^'"^^. .'.     ."^,:'";"",.         :     ,:       ':
                            I.   +]l       i}<"       ~  !-[i![~  -`  .~l ;]'       >, `;
                            I.   ?_;       ~[>_       ~. ~{(~_|_  ~<  .-I "_`       l" `I
                            I.   ?{i       >]+_       l ':;<;I~I  _!  ._l ^;.    "';;. ^!
                            ;   .?)!       >]+_                   {,   _i i)"   .]i\f" ^<
                            ;   .?(!       _|_-                   ],   ?! `^     ,^;;. ^!
                            ;.   ''.       i[~-       ,    "i!1~  .    `I :>.       !" `l
                            ;                         i`   "+i\[  "^   ^I I{^       -: `I
                            ;.                        -    "~l1}  <+   i! l{.       l^ `I
                            !                         +I   ,?i\]  ::    : l]`       ,. `I
                            !                         <~   ."^I]  ;;    ^ I-`       ?, ^I
                            ;                  ..`..  >l       '       .l !|,''.    <, ^l
                            ;   .,.            l!}~;                   .:  ._|>i.      `I
                            :   l\~                                                    `I
                            `   I)!                                                    `;
                            :   I;'  ..    .'.  .''..    ..'''...........      ..'.... `,
                            I  l]___]i;~i>_Ii_-_:.'l:_!-<,!'``'':I^""",!;l~>+,>:^^"'.. ':
                            I^ I1-]]i::?]<-`:-1[+><,'}+],.;l~!>I,"     ,'<{-~.>^I!;!<; ,,
                            .;,;i;l; ^,:>;"^:l!ii><,`!;I'`,I<!il""'''``,^;!;".,^!<I!_i:;.
                              .`;;lll"^ll!!i""l;;::`:;I;ll`:IllI;`I!!!!I^;;Il!:^;;I;I,.
                               lli~l'<<;_]<"i-,?_!;!!"_[:l!>,-{^~;>:]{`iliI+<'<I;!?[`]
                               `lI;lI,^l;llI^,;;III`:lI!lI`;;;l;l'Il!<lI`l!l;;;`I;I!Il

                                      !<],>>:-"I-_?~-~"-l~~+l-}<+_"+__i!>;]~iii~I]<<_~'
                                      ..;`'`.^..`^;^",.^.^`^``^^"^.`,,^`^.""""`"'",`""

                .>?" ;-+-~_~,_I+~_!-}<~-:__?<!<,?+<~!{>[[<
                 ''. .''"``".' ..`''````.'`^`''  '''.^^'"`
                             ',""``^""^^^^''":"",::,"```'`"""::,,"",",^",:;;,:"""",::""
                            ";'i:]}{!])1{-?1!::;;:,::]_)]~,,,,::;;III;-!:,":]:",,^"^::"l.
                            I  ^^il!:I!i!:;l:"""^'^"";ll;:,,,^^^^^^``:-[~]?<\l~+i?~1_: ,I
                            :    +!_~`+<<          ,]l?:!_~_['       .^",::"I]);";;l:. ,l
                            "    ,;'       ";,        "    ''^;^  "    "; ..        .. ,l
                            :   '[];       ](<:      '~    l>+t+ .}^  .?l <}.       ?, ,;
                            ,   '?-:       ]}~<      '!    l>_(<  ?<  ._I ^I        ". ^,
                            "   .}{I       -]]~      ^)    l~_)~ '{^  ._I I_.   .!;]<  ^,
                            l   .}\I       ~[-i       .     .    .].  .]l !~!-[{?i\~^  ^"
                            <   .+?,       ~[]_       '    ''^:` .<.   ~l ^`....    '  ^"
                            !              +)}-       I.   ;<+\+        l ~?.       _` ^,
                            l              ";;"      '-    I<~(_  ~l   <! >[.       -` ^,
                            l                        '+.   '^^,`  :,   !> <1.       ". ^,
                            l                        .-i   "ll]~ .<;  ._> i~.       +` ^,
                            I                        '{i      'l       'l <|        -` ^,
                            I                  ;I_!^  :^               `l :~~?>l    ^  ^,
                            l                  ,,!;'                   .^   i~::       ^,
                            l                                                          ^,
                            l                                                          ^,
                            l  ,<;,"",",::,,:::;"^^"^^^^^^,""""",^`````^^`^""""^```^,' ,:
                            l  <}}{{)i;]_-1;,+11:.';:{~[>^l'''`',".'.'.I^+1[}"I`'.'''. ^:
                            :" l[>-_',;+_i!.^>]]_?]^']+~ ',~?]]!^'     ,'+-_; :'~+~]{_'I`
                             ^,,lI;::"",:;;:"^,,"::^";",,^^,l;;;"^""`^"^^;;:","^;:"I!;:`
                               ;;<<;l:lI__i!:iI<~;!,ll-+;i,ll-~:l^!!_~;!,li~~Il,I~-<I;
                               >:<i::!~;_?Il!~;~_;!I!;+[^~!!I+?^>:l!_]`~ll!i!`<I:~]+"<
                               .,^^", ."`",^ .^^`^` `"``"' ^^``"' ",^^"' "`'`". "`.`".
                                       ^". ^`'^ `^..'.  ''".. ^^.'..^.. ' '"...'` "'
                                       >>[^_!l?^i~~+~?~:~;<i-I+]__<I_+-<!i,<<+<i[~--i















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


                                                                                               `^^"`,^.;.`^"
                                                              ''..''.' .  '.''. ..... ... .''..<}-->-l,+">?-'
                                                             .]]~><+>[i_l,-<{?i>]II_]!_]l:---?-+_~<~_l++_}-l
           '`''''''``````'`^^^^``^``''''`````````````'''''''''''''..'.''.''.' '`..''''.'''`..'.'..`'`'.'``'^
           '`,,,"",^'```^"`"""":""^^''`^"::""""":,""""^`"",:;;;;;;;;;;;;::::,::,;II;IIIIII;;:,:,,;IIIIIII;;:.
           i?      :{-][>`{~ii-:~[>+]_>ii:l}i>_>"!-~>!!+>i;^
           >{"     i?<l_! <-?][,<{{]]]__j?;1-1}|i>[-}|\}1{t^
                   !\f\--{~_+<>:/)__~<1+-]- ?]]-1"~|<+]~>?\?~+{{]__-+
                   i]?--<~~_++{,><]-<_-~_~~"~~iI_^l]\]}]-__?_]{-?[-??
                  .`           .       .   '  '' .                            .       '           ..   .  .
                  ,_<_-+i-I<~i<-<>`~_+,}+{']_+!~_-~_`i<~<~[?:I~+^~_<`?>+]_<_+"]-_-?~ :~<<<?<~,~+_^?>1I!+>-++'
                  "_+[?_![-;i}<<-l!<<;]_<I~>+;>~[i+!i_+?I_<i_Ii+!<_?~?~... .. .'`.``   . ..'. .'`.. `'. ...'.
                  .^`"'^"```^,^""`'`^.`'`.^^^'"""^;:::!l'^``;^,:",:::,"
                                 .   .       .....      '.'.       .. ..'''''''````''...
                             .:":;l!iI!<<>il>;:::;;;:;IllI;:::::;III::,"^^^^"llI;;,,,:;,;'
                             ;` ",_--!+[[{~>{!"^^"`^"^`^:^,;,``^^`^",^";ill!;1~:!Iil>+l .I
                             ;                 lI`~!`>~l.~~^:~~"i-!`.>;I?++_i~i;+i-__~;  ;.
                             ^                 "`.:" "I:.I, `;;.,l,. :^                  I.
                             "    <?""_]^  ;-i.i]I   l+"`>]i   `_~.i?<                   I.
                             :    -]''{['  ,{! l(l   i}^ '-1^   ]_ .]]' .``' `'.    ..   I.
                             ^     ^:<};    ,~^_i^                      :]->;]-`   '-}   I.
                             ^     :!<)<    ,-,~_:                      I(-`~1)'   i)?   I.
                             "     :!<1<    ^+"~<,                      ';" ^;;.   ^l`   I.
                             ,     ;l>)<    "_"i~"                      "[~?<l}"    "i   I.
                             ,     ;!>)<    ^-,<-:                      ."`^`'".    .'   I.
                             ;.    ,;<{l    "<"~>,                                       I.
                             "     ;i!1_    `_:<~:                                       I.
                             `     <i>?~    :['l1:                                       I.
                             ,     ^'`'`    '"  :.                                       I.
                             "                                                           I.
                             `                                                           I.
                             `                                                           l.
                             "     .                                                     i.
                             ;  ^"`'^":;""""";,"""":lI~<:,:i;!i:^"I^^^^^:l,^"""::^^^^:"  i'
                             ;.   I!" ^,     ".     :;{_;"^I"[[_:^;     ^I ;":.,:        !.
                             ';^'.i<".^" ... `'  .. ,"_>_~I::?>~+I;     ':.~l:.^"     .`;,
                               `^lllli;`!!!!!,^lI!!i"";;:;I";!!I;;`:!I;!I^:::;l;^III;l;"'
                                `II-i'~ll<}+^!~;?_<,ii,-?!Ii!"?{;!;<:}1:ii>:__"~I;!]{`?.
                                'llIl;!"lIIl;::IIIl;,:Il!ll,;;I!:l^;;liI!,ll!!,i"ll!<:>.
                                     .    ^'  .... ''''''.  ... ^. .`       ..`      .
                                         .+_-^?:i< <_+!:-~<:]]!>->+>[-]+_+<+?:__<--<`
                                            `                . .     .     .'  . ..





















                         .
                         .

















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


                                                                                               ",",`; "".^"^
                                                             .`'''''''.' ''''' .'..'......'`''^??-]<]^<!,~]<
                                                             l)+~!i~+]!_.>_-?<!+_">[+I[+;i-_?~-_!><-l>_-+-_"
           "`''^```^^^^^^^^^^^`'``````^^^^`^`````````````'''''''`'''''''...''.`''.'.''''.'. '.''''`'`..'''`'
           '^"",""".'^^^^^^^^``"`'''``^^",,^"```````'";;;:,,;;;;;;;;;;;;:,,,:;;;;;;;;;;:::::::;III;II::,,:;,
          '\l     ./\?~~<~+<>_!,1]_~i+?~!,,?-~>-?i!>+`
          '[>'    .1{{}{[11(x\+,[-[)\]1{tli1-)([{[]-|:
                 .
                ,~'?_i'-++>[_>! i~i[_.l_+__?,i-+`~<>~__>^]~~1l,?>~"_<~+II+<++>+"l_+:I]>-`-[{~?-_-_?i'+<+"_~i
                ^>~<<~<_-!l!!!><!~>_~;l~>I~~:+<~><<>+^`..:^'^'.^'''^'^^'.^`^``^..^,`''.^'^^`'^^^^^^^.,^".^""
                .^:,,:lI:"''^":",i";^'";^':,',;;:I;,"
                ,__><`l>;.~>i<+;^!li<>^,::""~!.;!l!l!<!'~<i<<I^ill_: -<i!~l^!>i>`l!>";>^:i!>!iil,i'i!I^l!;li
                ,>!<?l!I~!~_-!!~!<i>+>:-ili!;l<ii+l_+?~IlI_>+>lii~i<l+~-!i~!~~_<:ii_il_;!<~ii!~i,Ii<>i>---?+
                l<i~+>i;<+]>+>,+i<?>+;;++_~_<I+_+i;~<<~_!I_ll!!i><:>+~i~<I~<!_<!>i<+<lI<>i+ii:><< ll~;~~++<!
                "!~lll_><:!'i,<!i-l~>^<<_il!_~!+]::<iil~,<~l^-><+~;"!l>?^~Il!"~~;"~~>><~-'I++~_+^i!!->^<'+~!
                :<I-<~_;?~+?-I!~<-?`'-+~"<~~<<_]!!-++]+<<>l~;__!!?--_+;<<>__ll<l_~:><~:[_+~]_+i~I-+i!_i+>>~l
                ;++?`^^'`^"`,`.```". .'^.'^^^":I`'^,"";""^`^'^"``"::";`""^::``:`",'"^:'l:;,",,^^`,:,:;,i;::`
                'II^
                lil>ii<~"
                ^::;"::;'
                            l<!<+'     '
                            :iI!i.     '
                            ;<!!"
                            Ii!>>I?+~;~_~~I;>i~+!<!">ii!:l.     .>Il",:::;;l!"I!".I,II:;;'l:`'I,:I:'":":;.:^
                            ^:";;^l;I^;lII,:;:I!;I:',;;;:;....''^-<+"!?__~_[]ii~?:--+I[[-l;~_<[){{|;:-][1!+>
                                                                "-_i^!~_>_~{)i ~++_[:.~_~<^`I!I!;li. :l!li,.
                                                                '_~<<<l:'i^Il!,<<_l~i"i;<<<,
                            <_i_[l][][]> ........................+!i`'>+-!>~!']<,`+i~++l !!!-i"-^i-~'I>~_>_!
                                  .'.''.             .        .."_~+]>"""^^,".^"`'"":";,.`"",".:.'^:.^^II^;^
                            ,:",:.                              '^^^:,
                            l>li~.     '
                            ii:!lI_I_-,i!+-:<]_~?[!>+_--??: ...."-i~<il;i,+!":<ii><";!I~!"!>,l>l`I!!!!!i;,l"
                            '`.'`'`.^"...^"'^^`^`"`''^""""` ....^++-_-<~?<~~_~-+_-?l+-_?~I[_l<?]>+++]]}|-!1!
                                                                ,[-?[[>}--l~___<+_]l}}[[}}i]_[-\?[>^I::;;^I^
                                                                'II!IiI`;l^;:::I!;;."l:;;i^":l,l;"


                             .,:,"^"""""^^"^,;:::;:,,"^^^":II;;;;:""","",;:``^"""::,"""`
                            'I':l~11__t{)]<)],,,,,,,,,[[|)];;:,,,,,,:I,>["!\{[l;:,,,+?'::
                            :, .`":,^^"","";"''.`''''`::;,^'''''''''^"i}??[]([<]<}-})_  I
                            "^     --)[_(`.]])\,;                     '''`''```^^,,,"'  ,
                            ^`     ^`"""". '"";".                                       ,
                            :^                                                          "
                            :^                                                          ;
                            ;,                                                          !
                            I:                                                          !
                            :"                                                          !
                            :^                                                          !
                            :^                                                          l
                            :^                                                          ;
                            l"                                                          :
                            ;"                                                          i
                            :^                                                          ~
                            :^                                                          i
                            ,^   ",'^                                                   <
                            I"  `~<"!                                                   !
                            ;^ `iI","::",:,",;,::^^::I:;:";^^^^^":""^^^":":::,,,^^,,,"  l
                            ;^ ^[]1{(-:_-<)>"_}[>'.;']_}['i'^'`''l.....;il11[l:;''``''  !
                            'I``[i<<^ ;>?<l"`<]?--}! ~_~" ;;{-[-""     ^:!]<i ,^<?~_{]I";
                             ."",:,,;:,:::;;"^,,,,:^";,,;:"";"^:,"";;:;:^,;,;I:",:""l::^
                               ^!!_>">:l<-+;;!I<~i;I;;--l!:!:_];!">;_];!:!I<~;i,!l__:~
                               "i!>i"<l!>+<"I<;>ii;!;:>~llli:>_:i:<I_[:!I>Iii^<I!l~]^?.
                                `^`^"  ^`'`^  `.''^  `.'.'  `..`'  ^`.`' .`''^' `"^'".
                                               ;"'.:',^ ;,"^`````;^'`^''I````'
                                              '!+<^~"<i'?_++_-}~;~~]<--,]<>__i.

















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


                                                                                               '"""^`^ :`'^"'
                                                              ''''``''... '.''' '...' ... '''..I[?-_<~'+;l+?,
                                                              ~1<<>~~?~i~'-+]-~>-!,~[i~}i:_+]-~-~><+];<+?]?<.
           .^^^^^^^^^^````````^^^^^^^^`''''````'``````''''''.....'  ...'..'''.'^.'.'...''.'..`'''.''.'.'``^^.
           '"::::::""^'''`'`"```^"^^^"^,,",;;;;,:;;;;;:,,;;;,,,,,,,,,,,,,,,;;;;;;;;::::::::;I;IIII:,,:::;I;I`
           ,[.     ;[_-~+>?<'}]-~i~_<!;
           ^i,     ;?<-1}?[]`}?[)t}]1\] .
                 '.                           ..
                 ~<><i_^+__<-_il^~`<~_i!+_-:`}[<I ~`I><<i_l^<!<[""l;!I<><><?!l~"~+_+-,-~;~]<"+~_,i_]<^-i+I<<:
                 I><~~_+il<l~<:ii~++~;i+~~_+<li<;i_><_~~<><+~>i;~;<~il~!><il`.^.`'^^`.'^''^'."^"'`""^.,`"'`"`
                 ";^":`,^.`.`:':;,::^."I,:::;`^l'^,;,;l:I!:I!:"^l";II^!:;l;"
                 i<<;<+>i+<>>"~!!+lI_<!l"i>::+;I_<><i!iI
                 '."'`"``""^;'`^^^^`,``^.,"''"'^":",I,,`
                 __i?;?<?;_<;!~_>+:i++_-+"~><~+>I;~il:+><-;~->~!;_?:i_~,i~i>><_~!<-~:~++i_<<;~<~i_<<?~><!
                 .''`.'^`.."^"^'``.^^"^",.^`'^`'``^^```^^^'`"`^`'"^.^,:`""^"^^",;`^"',""",,"`;::""":;,,::
                       I   !?<"_+-~-+<[-~lI+<+_!
                       ^   `^".^^^.'`^'.. ......
                      ^_.  !-i"+<_;<]-_
                      .,   ^::'^`^.`^^.'`"^`''.,``^`.
                      '~.  l-i"+~+"!__ll<~-~?~:----]>
                      .:   ^::,"^^;;^'
                      .!.  :l~_<!i+>i;
                      `l   ;i,!l;,.:l:l!il"'`!;l^l!!:
                      ';.  "!lll;"^li:lllI"''!;l^l!!;
                      ^~   !<lii!I^l!I!lii"`^iiI,:~iI>.
                      ':.  ^I;:;"^`:;^;,::`'`;;,"";,:;.
                      .l   i~i~~>!"!>!~<<<,`:>i!,__i~^
                       '   `,"""^`.^"`"^""'.."^`'"^""
                      ,].  i?<-?<!,<~>-__+:`:+~-->>l~?<_<_]]I
                      .^   ^,^^^`'.```^^^^' '""^^''"""^^'^^".
                      ,-   i]~+-<l:<_i-_--;^;<ii+!><<-?<i
                       "^  ",^^^^`.`^`^^^^' ',,'``"`^`'^''`''.
                      .l>' !_~~~>!:>+!<<++:`:?~,l<ilii<><_-~~;
                      .:`  :;":,^^'^"","""'..^:"".,",`
                       I,  I~i+<iI^><!~!>~"."><<!^~~-i
                .>!>ll,!l:,;ll':^;I.;;"II,;l::`';`:!,.;I;::l:^;:,,:;;;';:I^!;'":';:",,",:`:.
                 ;IIII`;l;"iii^I^I!'Il!!<>!!"!l"+"I~I"~~!!l_l!~>i!!~>+^<i<:<~,:i"~i;I!!l<:>^
                .<i!I;>!il:`l^!!i;!~l;`l,;Ili:l;
                 ,;I;:lI;;^^:^l!I:llI>"I,;;llI;;                            ll'!i<l;~ii,!>;~><i!+'!~<"
                                                                            ""`~i[_??~}-::^,"",":^"::`
                                                                           I```^'^"^"",;^`^`````'^"^^^.
                     `:"^^^^^^^^^^,,,"^^^^^^^^^^^^^^^^^^^^^^^^^'^^^^^^^^^""~``^^^``^``''`^`^```^"'
                     "` `^`^^^^^^^`'`'^^''`^`^`^^^^^,""^^"^^^^^^^^^^^^`''.'i..' .'  ```''.'``^` ":
                     ^' !':I::;::;I;Il..   . ................... ..'''":l_i-<~I?-;][;<+li+>:^'! ^"
                     ^' ! ^l;::;::;;;;"""""""""""""""""""""""^^",,'   ^Il~<]~~l-_I--l<_!i-<l` l `^
                     "` ! l"^"!""""""""""^^^""","""",""""""","!,"";   `i`.:l'`^`'^''^^`"^'^i" l ^^
                     :` ! l'  ;                               I  .;   `<]]?|]]_-?_[+}~1+?_i-" ! ,,
                     ,` ! l' .;                               l. ';   ,<~_i_~_~~_-}]]]}+]>i_, ! ,,
                     ,` l I' .;                               ;. ';   ,~!<<~-i_i<i+-I!-i~[]-, ! ,,
                     ,` " ". .;                               :  'l   ,-+|?~)~-]__>~[)1{1{{-" ! ,,
                     :` : ;. .;                               I. `!   "-~~_![>~_<-~?-?}~[~<-' l "^
                     ,` I i' .;                               I  ':   "-_]]-}+}-??_{__}_1+_-. ! ^`
                     :` < !' .:                               !  ':   :-!>~-<!<!I!!+lI~"~~>_^ I ^`
                     ,` < >' .:                               >  ':   ,_,,<':'!ll>l!ill:'+<-" : ,^
                     ^. ! !' .:                               <  ';   ^-{?-]<'+~~?<++~-:,}][^ " ,"
                     :' l l. .;                               +  'I   "[j\}v~'~<>_<+~~1,:+?]^ : ,"
                     :' l I''^I```'''```````````````````'``^^^>`'^I   "?11>)i'<>>+>~~~_""+<+^ , ,"
                     :' l ;>i!!l!!!!!!i!!!!>>i!!!!!!I;I!!!!!iiI!i>"   "]\[+)i.~<<;~<~i!":]~_^ ^ ,"
                     :' l ".'_?!<_i!~}><+~:>[!,>]!:?~;!?ll-]l~<i.^:   :-_:;l"`""^""""",`^,:>" ^ ,^
                     :' !.,,,!iIll;:l!lll;:I!I:I!II!!;i+I;!!I!!l,:"..."+I":,::::::::,,,::,,i^ ^ ;"
                     :' ^^`^^''``'``''''''^^''..'`"^`'i"`'''`''`^````^^i`^^^^^^^^^"^^^^^^^^``'' l,
                     ,,^^^^^^^^^^^^^^^^^^^^^^^^^^"^^^,>^^^^^^^^^^^^^^'lI`^```^^^"^`````^`^"^^`""I'
                                     .             ..I"..............'!'".^`'''^'''.'''''''`''.'`
                      "'^^`'''''`'.'..^^.'```'^.``^' l               :';]`>~-_l+_I_?+I-<liI~?<}I_];.
                     "]><_]_!_+___>?]~[~>++_?+?i--_-<^               i"^`^>~_-<!}]_[><-><~~-<i]i><++`.
                                  . ..  ..     .   .'                '`'''.....' .''`'........ ... .'.

                                       ^~!:"i^<l'>!lIl;l;:,!l"ll<<lil;ii<<,I>!!ll,>;:l`
                                       ':>i^!`!;'ll~!!<!!~"I>";;iiI!I:i!!!:I<!!ll,;>??"













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


                                                                                               ^^^^'" '".`^'
                                                             .''''`.'' . '...' ....'   . ..' .`?[?]!-^l!,>[i
                                                             ;{[~!<++]l].~-?]~l__,>?_;]-;>__[_-_~~<-ii_-?-+"
           ^`'''``````^^^^^^^``'`'``^^``'`''```'`'`````'''''''''''.''.''.'.''.^''.'''.''.''.`'''..'.'..```^`
           :,""","^^,:",""","^^`^^`""","^:"`",:;,:,,::::^^^:;;;;;;;;;;;;:::::;;IIII;:::,::II;II;::,:::;II;I:
                 'II  ii!ii"!<li;:-<<~l!~`.++<; l^li;!!;lII'
                 '^^. ^',:;^,:^;^'l::;;":".II,^.;."I"^"`:l<"
                 .!l  ;l;::"l,::I,`^;:'!!I"^Il!l,!;`;l;l:
                 `<>. ,"l!i"!!;l!:""i<,<;:":!!!i;l;"ii;l<.
                      ;>!",l:ll;`!l!!!;:^,"!;;I`:!lI^:I!,!i;l;"ll;I.
                      .^I",I";I,^;:i!i<I"I^II!l";>!!^;llli!I;I;i><!
                 '!l  l;,::.,I,,^";^.l!!: : :_-, `^`"'"^''^ "^^"'.':"'","":.:",'^:^^^^"
                 ^<<  :,!ii"iil~lI<>'<]-;.i.l<>;'<<?~"i~>I~,~+-__<I++:>>+<<,_--ll]_>>+<
                      l!I;Il:,`<><^`!;<l"!I;I;;l:^^";I;`
                      ""IIl:;>^+(_"^l:I,:!II!:Ii:,:;i__I
                      >>!i!ill`_|[`"il!;,i!:;l^:,ll!!
                      ^^:;;::! I,I .::;"`;:"`:^",I;>!.
                '~~!I]i!<->~l;ii~i>+ii;~ii<<>;~~l:>!l<:<+~!><,>ii:>i!~I;<<i>~!>^:~+!!l!Ii!ii~l<~:l!i!!lll~>I
                "><<I><<I^"^`^"^"^";,"^,:;:I;"":,""::,^:;:,,!^:,:`:;::^,!;:;I::`"l;,;;:,lllllIl!;l;lll:!iI!;
                ;!!<:`li"
                ,<l:"!IIi!!_>i";!:i!il<ll!I,!::il!;+:;!;!;"~lIIl.l",lI>iIl;III^l::l;:"l;l":l:l:^;^l;:^::;"
                '"","lI:I,:l,:."^`!I:,l,,":^"^,I,:"!"!!Ii:"+!ll! !::l;i>!I:il!"<l:l!~,<il,!-><<"i,!>!,><~!
                 'l;  l;::,^l,:II:`":,.!Ii^:!l;l!;;:"
                 "<! .;:iii^iI;!!l",>~"i:+;lil;>l!l!l
                      "`;l.>`l!i;!Il!^;:"!l^:lI:I:';;ll!:"IlII!!^ll;
                       ``. I':l>:l!;l`;"`:!^;;iIl>'llIll,"IlIll!`lll
                 `<I  i:;I,:I,.I;,:::"",":."^"",".;"``."^^,^'"``:'`^:'
                 "~i  i;!<::!!^~iii>>I!i-~`:ll!>i`l;;!i_;,i<:<~+~>_~~"
                      i<I`:l:I";!l,":"i;I;;;;,;Ii;:I,,'"'l.  '
                      ":I`"I:l"liII:I,!!il>i!::iil!i;~',":^,`'.
                     .-!><l<~;  `^i`' ,<'
                      `^:,^l""  ... '.':.
                 'I"  ;,^^^':^'::;;:;`^'`.
                 ;?i .ll<~<:>~^!<!<;~"i~~.
                      :I,"^;I'!:";,`,I,.!I;I;:",;:,;`;II^
                      ":I;:iI^<><i~l;ii`~<>i!l^II>I!`i~+;
                      !>;l,`lI`!!<Il>';;`""":II;;;,:i;",l;;;:i<;;"ll!,!l!;II;""^:;..^';I;^;::"':l;:;,`;;,::'
                     .~>>+!:>?l<<!<!<l+<<i!!;!!!ii:!iIli>:Iiliil~;!i>;I!!!i!>>'::""".`I!<,!<!l:l<-><_,<>><!^
                     '<>i!<"<_;!<^<~-+~~<>`
                                            .......... .............. ............ .
                             "::II!iI;lllI;I;,,,,:::,,"",,:,,,,,,,,,,":,,,",:,,:::"""::,
                            ^I "I~({_<)1(?>(],,,"^^""^^",^^^",,,,,,,::::,:I:1>;il!;I>< "l
                            ;,  .         .  .."iii;">I;'i<>:......'.'!\1\)i~~i}<-~]?!  l
                            I:                 'Ill:^i:: lll"          ;i~:             ,
                            l:  .i[`   `>[_               <_     ;+1;          .        ;
                            ;"  ^;i:):<}1ii1)+'           i-;]-`"{\!:[]]{_>[[)\i?!      !
                            :^    <It,-{+l+)[l:l" :"I"    :_;}["^{)`,(|[i)1_>?f;;"      !
                            :^    >I}li[~><}?<++; !:<^    ![I11,^((^:\!-\r]{-1~I_!      !
                            :^    ~;<_'[?_,[[}:~~; !:~`   ^;`;;'.!!'.!iIll'I!I^         !
                            :^    _l\t)\ii[[<^`I;^ ,":                                  !
                            :^    !lf{!<>|(}+~:  .'                                     !
                            ;"    -;]{:'{/;`1-];|]?;`                                   l
                            ;`   `-;][:'});`)1}:1-});;~I                                !
                            :`   :>,}[:'}(,`1(~"[[{1;;<;                                i
                            I^   "~:}[:`{\I.]|>^)]{1,i]>                                ,
                            ;`   '` ... .'. .'. ' .' ^,^                                ;
                            :`  ^~"'...`^^`' ^ `''`'   .                                !
                            ;`  `~_!^;^;~+>"`l.!;I~I  ^:                                l
                            :`  '<;".^'^;;:`'; "^:l"  '                                 l
                            I` "+~{}+_>?{]};l-<1-i~i,!l!i"I^'``^,l^`^^`,I:l!!;:;````"^  l
                            I" '~1--1>;++~?I.!{{~,", -_[~.;"<IiI,I":'":::I[}?:,::l;;lI' l
                            .;"'`?l!I,,'><;;,i>~+_?>'!>!^ ,:_<<i:;<<l<~l^:~il ""l<l>~+;;^
                              '^;,;;l,^l,;I!:"I:,",'"I::Il^":::::^";:,:;,;;,;l:^;;:";"^.
                               "l!]!`+lI<?+^!i:_+~,<!"?[lIl!"]{,i:~;]{:!;il_<^<;l!-[^-
                               ^!!l!;!,!lii:I;I!!ilI;l!il!:lli<li"i!<+;!,!IlI,i"l!>~,~
                                 ...'   .  .  .         .                    '  .'. '
                                                <l;.>"II.!<II!,l>l!!l,:<I;ll"
                                               .,;<'l":^.;I;ll::l!~!>l"iII>!,

                l<~iI++l!~<~_->>-l!+_>+i+<<_<i!~<i<~<+i<-~;?-?<++I++!>i:_~_>_li+<l_~~l+~+I;>!<>"><i!i>i!_>>`
                i><~i!^'.^'''^'.^..^""`'^''^`'`^``"`^^^``".^`'''^'^,"`^'",;^:"'",'","";l!^^^`":',;;,":,^;:".
                ;::lI,.










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


                                                                                               .,,""`; "^'^,`
                                                              '`''``'''.' `'''` ''..'.... .'```"?]_->?`<II+[!
                                                              i}_<i<~+?!?._~?_~!_+,<_~i}>:>?_-?-+><>-!~__]{i'
           .^``^^^^^^^^^^^^```````^^````````'''''''''`````''''''`''.''......'. `.'.'.'.''''. ..''''''`.''''''
           .^^^,::::,"""""^"^`^^^^""::::::::,,,""""""::;;;:,,,;;;;;;;;:,,,,,,,,",;;;;;;;;;;;::::::;IIIII:,::^
           .<'l    ^+>!!>>i"i-IIi!!I
           .^.".   `;;i~li-:">l;ii!:
           .^'.`'  ."".^^..`: .^.. `^`^`'
           `l,:;:  '-_^i}+<i_i+]i>^i!<~_l
                 "I"'^I:.;;;,,',;;:`:.^`"""^,,,`I^""'`"`^"'^""^`^`^'`",^""^'``'`'`^""'.`^`.',`.''.'.^'.'
                 ";!i:+i"~>!i!^l<_<l!:~!<+i:l+-:~I<_:i___~,<<<!+-]?:>--~~_~:!<>~>~<~]!;_->-!]_;<-?-l__++"
                                               .       .      .. . .          .
                              "::;;liI;i>i!l!l::::::,,,,:::;;II;:,::::,,"",,:lI,":""";l::.
                             `l `:i[->>)[}-~{-""^'"`''^^''`",:::,""""""":::!l|_:!";Il-< `l
                             :,   "i!l^,l!^   ..^~^I~i`;<>!^...........?/\)[<__!){\+]{I  ;
                             ::   ^!>i";lI"     .<';ii'^<<<'           ,!~!     .~_   .  ;
                             :,   l_   ;il"    !""^;'II;^:"::l;l:I;I:;;:,"^;;;;          ;
                             :,   `>"li-_[~!-_ _{|I~/\~~{1:>[?`<[)+i}r>~\{i"1n!          ;
                             ::    i,_|[_-?_{[ i?)!!)|<I)|!i1|<!{(~l\|<~/1:"?)+          !
                             ""    iI?+!_]?<]_ _1|~<{(<;(1>i1|~!|{_</(~l|)<!(-i          :
                             ,,    >,~__~_+>-> _1)<<))_l|{>i-)_!1)<:!;;>1|_!t}I          "
                             ::    ~I]?))?)<]_ [))<<{t-',I`<+{{i?>i"i"^i_-_l((-          ^
                             :,    !"<[{[]}+}- ?)[>>[1!!+!'+(1_!)-I>|{l>1-Ii(_>          "
                             ::    ~,<?{1}+>}- ~)[!~)1ii/]'<1_'"[['>(}"i()i!){+          !
                             ,"   '-;[1[]]]~[_ _))!+|f<+/}:-?|+_))>][[>_\]!~t{>          !
                             "^   :_'_-<?--<[< +]|l+(}^_/1^?f(~~1}>+t{:!f/l_/?~          l
                             ::   ,-^[1)]{t+}? _[t"~/_;i/|i~u(i~/[I<t|<!t/l+\}>          i
                             ""    `.````''''. ''"..`^'.^`..^`.'"^ '^^`'^^'`"`.          i
                             ""                                                          ;
                             ""                                                          I
                             ^`  .'                            .                         !
                             :" ^]-__~>!<>>+;"!i>!`^::<lii,l"'^^""i,""^`"l,li!;,;``''^^  !
                             :; .>{[}1_:+--[I^][1~::, ]]]_.I"iI>l,l^"'^:,;,-{[:`",;;I!I' >
                              ;,''?>i!,"'~~,;"ii~++]i'l~!" ,"<>~i;;<<i~_l:"~i! `^;ill_~:;"
                               `"I;Il!;"l;I!i:`:,:,;":!;;Il^":"":l,:lI;;;`,:,:!I";:"":"^'
                                'Il?i'<!i>-_"I>I_+~"!!:_?i:i!:?{ll:>:]{llI>;?+,i;!!]}"_'
                                'l!ii;l;ii<~;;I!<>~l;;liii!IIli<!l,lli~l!:!l<l,i,!li+:~'
                                  ...'   ....   .                          .      .. '
                                             >i;.~`!>.<+;:+!!I>iI<il,,i;i>l^<;:II:
                                            .^li.l':I ;!"^<i!I;l!<!!,"lI!i!^il;i!:.










































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


                                                                                               ^"^^`: ,`'`"`
                                                             ''.'''''' . ..''' ..... ... .''.'"---?>]'+;;__"
                                                             i{?~!>~~?!~._+_]+I-<,<-<i{~,~[-???+i~<?I<~_--<'
          .^^^^^^```````^^`^^^^`'''''''```'''''''''''''''''...''''.'''''''''. '...''''''''. `.''''`'`..'''`'
          .,,,",::"`^"^`"","""":,,,,"",;;;:,,,,"""",",";;;;,:,,;;;;;;;;;;;;;::::::;IIIIII:::,:;IIIIII:,,:,:^
          'i""!:  `-+,l>!l:<><l
          .^'`,^   ,;'^;,"',;::
                "_<lI[~`<i>,i++ili:?~~~~<+i:l:?>><!_l!l<<~~<l:i"+<!;_<i>~"l>!i<i';+"i~I!>;;i<li;
                 '^"'""',""`":,"`"'::;,;;:^'^':,""^;``,""::,"^,',::`:I;:!",;,;;:'"!`;:,;I,"ll;l:
                              .`"^`''`''. '..`'````'````^"^```'`'''^``''.''''''`^'.''.'
                             ;"^:i]{]~1][?>-?::::::::::Illl;;::::;;;::,"""""ilI:,"""l<^;"
                            `:  ^:<i!;<i~i;<~:,"^",,,:,^^^^^,"^^^^^^^^l~~+->{-;~I+~+[+  i.
                            `,   ,<]_:;+>;     .["!_>Ii?<;           :{\1i?;;I!|1!;!<:. l'
                            ";   .'''  . .      '.`^.  '..    '      ..'. .    '^       ;.
                            ,;       :l"^         ^_.:^       <^"".      !i`:`          ;.
                            ",       -|+l          +!(?       ~l{[^      !<?(l          ;.
                            ^"       _[}>      .~~]]l({.   i<~[I)(^   ;<l[l-|!          i.
                            ^"       +){~      '{1\[I(1'   }(((l)/,   _|-/l_/>          >.
                            ^"       _([}I`     ..,<!)]    .'`+!11^   '`.+!?)l          >.
                            ^"       ~|{-(\!      `~l)-       <;}{`      !I?(I          i.
                            ::       -[{[}1l    ^Ii--1?    .II?<{}^    ;:~<[);          I
                            ::       ?11[-_     i\(|1{].   ^f\111)"    1|(1(1l          ;
                            :,       +~){_[~'   ',,<({-    .;:!))}'    ,:;](\!          ;
                            :,       ..`''^^        ^``        ^^`        `^"'          I
                            :,                                                          ;
                            :,                                                          ;
                            :,                                                          ;
                            :,                                                          "
                            :, .^"    '... .''  .'''.  ..''''''''.'`'''...   ......''.  ;
                            I: `]]]?]-i?~i]I:-~]>. ;:]<__:!"''''^i`^`'."lI-__i:I^``^``  i
                            ^I  "1-1[i:;?]+l`+?{?_-! ,}??`::?-]+:I!<:l<l:.+}[!'^:~><->^.!
                             ^:"^l;!:^,':;^""::l!!<I^`l:;^"^:;;I,I!l;l!;:',I:,`"^:,,II;;'
                               'I;!I;I^lI!lI:^ll!II,,!llIl^:I!<l!^:I!!;I^ll!ill^IIi!II.
                               `!l-~._ll!]_'!i:~_+"-i,+->:~_"?{;I;>"]);!!>,?+^+i!l?)'?`
                                :l:Il:.;::;;"';:::I^`I:,:;'^I,:lI."I:;:I':;,;;;';I,;:;
                                                 .
                                                ;<]Ii~:]I,[-:~_->i??]l_?><~_,
                                                  ^'          ... .''  '.'''
                ll;l:      . :;l:"""^"'",:""""''^"''^,^"'`^'`.`'^'''',`'..''.'^'..'`.''
                l>>>"      ' l>><!>il~:>++<~<i^!>!i!<~<>,<<l<"_>>l~<+-il,i!<ii-~`I!-~!;
                l<i+I      . lIi!:;::; :l!l;I;, "ll:;I!I; "l;:: lI!`^;;li:: "I,::ll`.;:i,I'"l!: ;;,Il::l;;:'
                ,;:I`      . !~>~<~>+?;!<___<_!"iiIIl!!!; ;!Ill >I!`;ili!lI.;!Illii^'i!+l>':>l: <i!<>i!<!>l'
                             :<ll!l;i!>:.i;!l~~~;
                <_i>+~     . II>!,i>>lI"iiII
                ,::;;:     . :;l;;Il!I""Il;;
                ~<+<+'    .' <li<>!!^>iili?!,<~_i-`
                ,;:,:;`    . :""::""`:"",,;"'",;":..`.'....'....'`.`. ..  '   '. .  .   .
                !<~<<<I    ' >l>~~i!"<i<<><l^l<~l<"~~+>"lil~-~;>_+:_~!l<!>_"~_?-!;+:?-?>++~`
                !!iI<;l>il^. ;I;":`:lI,"!II;;;;l:";:'"";I:I",;"I,";,':;i^l!:`,,;"";,^:,:::::,'"""^:`;:' ,,^.
                ;l!lI,lll:^. ;!;:l^;iiI:ilii~liil,;!"Il!!ii:l;;i>!i+"!!i,!<;"iii!:<Il<l>ii>><`i>il<:i~;.liI'
                i++!~li~_+I. >~i;!"!><l;~<i!>li+I;>!"I;Iil!";I;<ill!^l>_^!+l^!!!;I!;;l;l!;!il^lI;;i,!i".II:.
                :::I,^II:,`  ";,^:`,:;,^::::>:;l:^,:^:,,;;:^:^,I!I;i^;Il`,l,`il;;:!:I!;ll;l!!`lll;i";i:.:I;'
                ~~!+>__<~ .' <+~<>>]i:+<?<^~_?:
                Illll;;;, .. I:,:;",`",""::"^;,"'
                !>I<<!>i: .' lIi<<!I^<l!i<+""++-,
                iii>i~;!>;.. Il<I:ilI^!I^:I>:I;;II,l<>i!<~,:!!!"
                ";!:"llll:.. ;I!;li!l";l^:Ii;I;l>;",Il;;;l`I!>i,
                            .~+_-,    '!iiIlilil'l-+l>I!" IIl l<<"->+,~>`~<<~<">><>+><<>";i>>[:~,i>~_<>~!i.
                             `^^^' ...^~---_l~i>i<<<<I_~>!il<i:""';":'^" ,^":^'"",:,::l,'"",,,.:`"::";::,:.
                                       "II;: ;';I;!!;'lIil><!>^
                             ]-}}; ...,<!~i>>!<!"iI~]><~ll
                             ;;;;` .  ',":,,,":"'"I,,;,,::.''  .           .       .      .         .
                             -_~+: ..."+<i!+~<+i,>]->~i>><<_?<><+iI]?<~ili;-~_~]>-I+<+!I><]?!-~+l+I<]-~~i+l
                             ;:I;`    `,::^:"":"'"I,";"",,";l"",^^`::,"^`^`,"",I":^"^^`':l`",^^,^`""::",""`
                            .~~-_, ...,>++!+<<_<;~_+<-<~~+++]~<~<il-?_~!l!I~~<+]i?i<>~!l-?~~_<>!~;~+_->+<<I

















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


                                                                                               ^"""'".':.`""
                                                             .`''``''`.. ''''^ .'..'......'`'''<[??i-:;<:i]_
                                                             "{-~<i~~]i~`!_-]_>~-:!+_I--I![-]+-_~i>_+l~_-{_:
           ^^^^^^"""```'`^`^^^^^^````^^^`^^`'```````'````^`''''```''`'````'.' `''.''''.''''.'''`'.'''..`'^^`
           ":::::,"""``^"```,"""""`^^""":,"^""`^"^^"""":,,^^^^,::,,,,;,,,,^"^^^":;,,,"^:""",;:::,","^"",;::"
                 !li'<~:`~li.!ii,"!;!l;I',!l,^iI!:>;^!I'!!<;llI"';lI;.l!I;;'lil<: ili!i `l,;^:II>I.,I,:;',:;
                .~><Iii!!><l:<_+i!_<l+><I>~_!llI~?+<"i~;>i~!>_~_>~+]~,_li><:!~<>:!>iil>,I~>>:><i-l,__!<~:<<~
                `_~_i~~~~`>`!>!~>[<!`!!<!~!<!>` ^!;>"~+?_`!:,~~~__<<l:-;">i~>~<?:?<I"<+]>`~_>"~i<:;<+'<>>~<I.
                `i>]i-?~!>?>>+i
                                  .   .....
                             .,,::":,,,:;::"^^""""""",,,",,"""""":::,"",,,",,,,"",,:,""^
                             l``ii1}[,~|))1_1}^""""",::;:",""":I:,,,,:,,:::::-i^",,:,<,^I
                            ^; .`^;;;,;l!I:":",`'''`'`^'`"`'^``^""""""l]]+}~+1<1_-?_{~` I`
                            ^;   ,i[_;:_>! "rj+..\{1i_|',)1)_+t       ':"^^^``.:]{:",'  ;`
                            ^,             .+[-":]+:""l.'lI;":!:I""I"^      . "''"^   l';`
                            ^,             .]\)~~{^            >//j{{|      _>1|ff)` .r):`
                            `,     ./l      .i(,"[}[{<    ,()]()(\~.[\)|]   `,`-[;`   ':;`
                            `"     '<:       ^<,`<ii<;    ^~<i~><<l^i<~+i      I~       ;`
                            ":     .}:       ;]:"[1[}!    "{[-1{{)i.-1[(-      >-'      "'
                            :l      >^       :];"--_-l    ,[-_]?-[>`-?]{_      i_.      l'
                            ,;     `1:       l}!,]|[{>    l{)]i-\|+`{\)j[      _}.      l'
                            ",      '         '`.'.''.    ''.' .''`.''``'      '^       I'
                            ^"                                                          I'
                            ^"                                                          ;'
                            ^"                                                          I'
                            ^"                                                          I'
                            ^"                                                          ^.
                            ^"                                                          :.
                            ""                                                          ;.
                            ,, 'Il",^";::",",:"^"^^"""^^""^^````^^``````^""^^``^`^^^`'  ;.
                            "^ ^]{}?)]![+~1!^+-{~' ;:+~?[,"^^`^^`;...  '^;-{[i^;`"^"`'. :.
                            'l` `}+-+;^^?]ii`i?[]?{-` ++~^^"]-[_;^><I<?l. ;?]>.^:-+<[[;`I
                             '::,lIll,^^,"",,"":,:l;^^:^":^`""":,""::,:;"^:;:;::,;^^,:::.
                                l;-<,!,!I-+;l,!!_<:!:!i-<;i:l~[~l;:l<->IIll~~>l;ll__!i"
                                i:+i"ili:+-"lIil~_^>l!l~+^+!;>_~,ilI~-+,>i:<i;;i>,-[l>l
                                 "'`"' .^..^` ``'.^. ``.'^  ^`'",  "``^" .,`^,, ',^^""
                ^":;;:     . `;"".`^`"^"'"^^''''','`"''``''``
                ;ii<+!     ' :_~~:!_+_+<!---<!l!I?_++?+_i>>,+`












































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


                                                                                               ",""`; "^'^,^
                                                             '`''``.'' ' ''''' .'.''...' .'`''"?]-]<?`iI;+}>
                                                             !1?~i<~_]l-'_+]?il-~,<?~I[~,<_+[--_!<<]I>+_-{<`
           ````````^^^^^^^^^^^^^`''``````````'''''````````'''''``'.''.''......`...'.''''.'. '.''''`''..'''``
          .^^"^^""""""""""""":::,"",,,,,,::::,,,",:;;;;;;;:,";;;;;:,:;;;:,,,,:;;;;;;;;;;::::::IIIIIII::,,::"
          .!",!l  '~i>~i!><!>
           `'`""   ",Ii",:",;
                ;_<i:!<<>i>::~!__ii!!l~+:>~<>>ii,<_;l_Il_+>><<~I!Ii;<~<<>l<<>l<>!i~~,i;i>l,!l>>i:
                '"^".`"'`^^^`^'""''''.`".'"^`"`,'":..:''";:"I:,.^`"`,::;!^:,:''"^^:,','`,:^;:;l;^
                ^~~<;?_?_<~?<+I<<>~?<iI~:_i!<_~~!<,__,i~<>:<;>->,i<~<!!i,<!i,<<<;~_!<Ii<`
                  .'.'`,'''`'`..`'''`''`'^'```^`'^'`^'^^^^'""'`"'`^"`^`"'^"^'^,"^":,""",'
                                                             .!--+_-l+__?<
                                  .    .     . ...........  ,I"^^^""^^""^"...... .. ....
                               .::I;IlI:III;;:;,,,,,:::;l;;~i"^"",::;;:,"^"""""":;;:"",;::`
                               !` il{][!)1))]}/i,"`'''`"`;>l::::,"",,,"",;I::,<[,lIll;![:.!^
                              .;   'l>i!^>il ..'..i~~<!`-_l.''''........`<(1t[>|i?__){f]: ";
                              .;   .!>>l'>l<i     <--i>l_l!.              ">+I !^.. ,_!.  ":
                              .;         `".l.       '"l"         .I          l           ":
                              .;   "(_-_|!l_~]-.   .;:`_!-i       '<,?i.     .~!>?:       ",
                              .:   ';>}l" ","""^^.'I^  . ..        ..'.        '''.       ",
                              'i   ,-}+_?^)t|/ftf_^                                       ":
                              .l   `>+,.i^|)}{11)il;"`.l'                                 ``
                              .:   `!~:,[`)t]1)11!,"'  :                                  ^^
                              .;   "]]",]"|f({_[);  "[][?[-`    `?[[-?]`   .~-_-??;       ,"
                              .;   ^!!",{l1/)t({|!  "]-[+_-'    ^[[{]}{^    ?}]}}1l       ,"
                              .;   "~[;I['|tt\t1{l                                        ,"
                              .;   `l"."<")f\/|\1I                                        ,"
                              .;   ,<I^l(`|j/tf|ti                                        ,"
                              .;        ^"i!i!>>l!`                                       ,"
                              .;          ^,^,^,"";^                                      ,"
                              .;           ^;":,::";"                                     ,"
                              .:   '        .;":^,",;"                                    ,"
                              '; .>_lii>iii!!!<~+>_!I!>:l;!lIl^```^:"`^"""!:;;::^;^"`'''  ,"
                              'I  i1}[(1l~]~{_.]{(}+!<<<[]{l`:I;lI";""`'^^<`+)[].!.::II;" :"
                               ,,` ++>~:;.l~ll^;_}-1)(i^-~l;'"<<+~I;~_>i_>l '~~+.I`<<>--i^I.
                                '^::",::";I,,::`"!i!ill<ii":,":"^":"`::::;^"I,,:;^";^`^,^^
                                  !:-~^!;l:]?:l;i;[{l-i~~[{"iIl>[+,;;;<?<,!!;_~!Ill:-{il;
                                  lI>i;!:ll~~;l,!Il_>+i+~-[~i;lli>::,Ii++;ll;il:II!;<-il:
                                   '.'`.  '..'. .''."I";;I;I;.^"^^"'.^^^`".."^^^^ .^^`^'
                                                     .I",,:,,:l+_~~_>~+-!<~~_++!>!~__?:
                                                       ;,:,::"l<><i~l>~_li>i<<i;ll>~+iI;ll!!il
                                                        :::,;"I>!i!>Ii<+I!ili!i;!I!i~>!i!!>iii'
                                                         ,:::,I+<<_~~>+i;i+!l<<~?+!;<l~~+i
                                                          ";,"I<i~>>;_iiii;ii>;!>>~~!:<!!>i!`
                                                           ^I":>i<>~I>iil>li!i;!<><il:ili>i>"
                                                            `;![l-++_i-]_}-<II>__+
                                                              . .  .'   .''''''`'`.
                                                 :;".:^,I.";"^`^`""^',,^^``.
                                                 !l["~!<_^l++[_<<-++i!-~~++,

                ii  I" ' ,+i!i<!li;;!'+il'i><;^+"<iI.~>i>l!>>`i+~i':li!l>!!`iiI.;:III^:!l"'I;lIil;:'I;lli;I^
                ;:  "' . ^<<__+?i;""I.;::.I~;"`l':;;.ll>i:Ill'I>ii'";lIli!!`;!l';lI!l`,i<;`i!il<ll;`iI<iiI_:
                         ^iI!!I!"
                         .II;,; ;`lil;l'Ili!;I;';`,l;^I'II,`;:::;:l::;:';;:,:;'';:;:;.;Il:,:,`:."^",,",,"',.
                         'I;;Il l'Il!II l!>ll!!.;.,<;'I :I:`!l;ll;!I;>;.l>!:li^'iI<i!._<<ii>>'+^l>i<+++_!^~'
                         '~!;!i<iil"l^;i~;^<;li:!~i:;i!!:iiI!^!illiIll!;^!lllIl!"l;^";,I;^:I:l..i<>.  :i>;
                         'I><l;;I!>l;^:,I:":^,l^;lI;"il:"lI"<:;;IIIII:II:!l!!l;~::l,:l;!!":!>i^.i~i`` ;>>:..
                          ^~?+   >+_; l
                '.  ^`   .^;;"'''"l:'``. '`'```'.''
               .->  -~.' ,~!--_:~~<>-?i>"_!i~<}i>??+.
                   ..    .^^^^^.``"'^"``.^`""^"''^^`
                   '!..' "<>_?_:~~_i-?<<"~Ii+<?li??_.




















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


                                                                                               ',","^: :`'^,'
                                                              `^''``'''.. '''`' ''.''..'' ''`''I[--_<_'+;I+]:
                                                              +1<<!<~--i~.__?-+!]i:_[i>}i,~---__>!<<?;++]?[<.
           .^^^^^`'```````````^^^^^`````````'''``````'''''''''..'`''`....''.'..`...'.'.''''..'.''.''''.'''`^.
           ',,,",,""```'`^"^`^""""":::::::::,,":;;;;;,,::::::,"":;;;;,,",:,,,,,",,:;;;;;;;;;;;::::::;IIIII;I^
           ^!"^i^  :-!~<ii"><!ii!il
           '```:`  .;;:;,"."I,:;"::
                 I-+::i!~<!_I,<!+>,<<+->i"!_>~-_+!l+<,--~<+i<<;i!I?>:><!<>!'
                 .'^^'"^,"'"^'^'^"`":""^`.^;^,;"""^,"`,,:^:;,"."^'^,.",^;,^
                 i~!!+"li!>>?<!"I~l<~<>;l<!I^>_>-";_I""l>Ill!!_:++_+_<>>;i:><~l+_+~ !<>:<i+<:>+~___+Il-<I!><;
                 !+~+!I+<I~~;_<!+_i+~i_ll~<~<~!ii<il><>~!<>i``"`^";",;""`^`"^"",;l,..'"',,,^`":";,::"^",^^,"`
                 I;i~`';: ";.;:I;;l:,'I;"::Il;:!',:';!>;.IlI
                 iII.~~>~-:;iIi!"i!i>i:^!il<<<";>>!>i ,>_l`!";-!i+<>,!+<i~<<i::I;>i,<i!i!>!!lil!i?<i:Ii'
                 .'^ """:,'`.^,;^;:,:"''",^;,;'^:,"::''::" :. ,l,;:".^I;,l:II '^'";`^":+II:,,;:>,!II,Il
                 >~:illl;;ll!    ,I^II:"l;;;:';,,;:,,"l:",,":I^`;:;:;"^^:""^.:,";;:,'"".^I",:^"^^.l`""';""I,`
                 !ll~<li;l!Ii    <<!i<~i--_+?l<<~~~i<l->~<ii_~>l+?-~+!--<_+<l~_+_+++i~+!>+~}+__-i;_>+-i><;<~I
                                 >!+:~<<_ii>_:~>>"i<!^~<ii_~~i,i^<!,,-?!">:~<:.i,_l~"'~+_" I:i^+>:;+!!!i;iil;
                                 -iIi;+~+_>ii~;<<_l^-+,<?_i!;I->~~~i!!;!,<>;!-~+I~<>~~~-~_I~i;<~~<__+<~~i-<<"
                                 <>i:[-[:_++~?_]_~;>i~l__[;~~~--!__-?_--_I^`"";:`""^""""^"',,`^"""""l',"^""".
                                 ;I!^I">^l::^::;;;`l;:,;,<"I;l;;^;,ll!l!i:
                  ";" .i:I^IIll`
                  ;;: '>i>:;!<~"
                                ''......  .. .''''''''''`^^^``'''''''''''``''.''''''`''.
                              :::,li>I!<<>!I>I""",,,:::;;;;;::,,,,,,,:;;,::,";:"":;I:;;:;.
                             :; ^,<-~!>?_]+~1+",^`^^`",^^'.'`^^^^^^^,::I<lI!!(i!~i<li-! ^l
                             :`   :<~<`Iil`     ,~>>?!;_i!_iI        ..I})|(<(_!-i?1f+,  !
                             :`   ^;I;.":"`     `""^I"`I,,l;^            ":, "`    lI    ;
                             :`       .' .       . I: '      .'l '.     . l`.            ^
                             ;`       ?([['     :t(t?<\]   ')||}!\1'   ]}[t;}|;         .l
                             :`       -)[-.     ^~<]~>(-   .~~_[>|1'   >~i1I{\;         .i
                             ;^       []}].        ll~\~      '<i|?.      +!]),         .I
                             !^       ][?{.        i!_\>      "_!([       _![1,         .I
                             i^       ?)t}.        "+-)+      .+<11`      >i])I         .I
                             i^       [f\+.         :{1+       ._{]`       <[}l         .;
                             I`       ])[_.         `1t>        -t1        I|\:         .;
                             ;'       [1\{.         `l!-       .!l["       :i~>         .;
                             I'       ^,:`             `          '.          ^         .;
                             ;'                                                         .;
                             ;'                                                         .;
                             ;'                                                         .I
                             ;'                                                         .:
                             ;' .^^    .    ..    ''..    '.''........''..       ..'.'. .I
                             l' :{??-[>l_><_^:><-!..,,?i+~:<"`'''"l''``^;II++<;!I`^"^^` '<
                             :,  l1_[[iI>]?+:^>[{->~! i[?_ ;:+~_!"IIl"l!;"'?{];^`lili>!'`!
                              ,:^"<I!,",'!l":,;I!ii~l'.!;I`,"lIlI";l!;ii;".!l;:'`:I:I!!;;.
                               .^l:I;I"^ll!ii",;II:;`:!lIIl`;;!!ll`:IlI;;^llIII;^I;l;I,'
                                I;<?<'+!:~]<"i_"]?>;!i"][;!i-^]{^i:<,[(^+i!l?~'_iI>]]`~
                                'Il;lI,`ll!lI^,ll!!I`,I:;:I`;lliII';;;l;l^l;I!l;^III!;:

                                          ~~]^]l<>.<]~-?+l:--<??__ii->~~<;^`-<+!>++-:
                                           'I.`'`. ',"^"`'.`^`"^^"^'"^^"^'..^""^'^,:`































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


                                                                                               ^^"^'" `^'``.
                                                             .`..''''' . ..''' ....'.. . .....`][]]!?^!!:<~"
                                                             ;{-<ii~+];+.i_?[_i--,>]~l[_"<-~}_?_~<~[i>+?-[]"
           '````^^^^^^^``````^^^``''''''```````''''''''''''''.''''.''.''''..' `''.`''..'.''.`'''..'''..``^^`
           """""::""::,^`^^^`""^::,,,""":;;;;;::,,"","",:;;;:,,;;;;;;;;;;;;:::,:II;II;,,::II;II:,,::,;III;I:
                 '~>  ;+!l"!-_i~^
                 'I:. ";::^,;;II'
                               '`^'''`.'''``'""^^^^^^^^^^^",^^^^^^^^^^^"^```''``^`^`"^`.
                             ,:"i;-?-!}[]?_[]IIII;:II:::,:;l;;::::::::;;:;""!l,";:"",i^;,
                            'l .I,~!i;+i~+>__""""^""`^''`''',:,"""""""l<_i+i?{;_<<>i--. l`
                            'I   ^>?+I,_>l      <~~~-^_-l?-<'         "[ff{i+l,>i[f]~;. "`
                            `l   .^""'.^''      ``^"" ^"`,,"            `:' .    ':'    :'
                            ^l       '^^"^ ''      < `.       l"''.      `! ..          ;`
                            `;       ;+_i>`~i      ~I11^      i>[);      "~>1~          ;`
                            `;           ^^_l    ">[;?]"    .,]!-(;    .,+<<|~          ;`
                            `;           ,^_l   '<t+:_]"    :_(l!{:    ,{t+~(+          ;`
                            `;           ;"]!    '-?l)("    .:[;+]`    .I}_~\_          ;`
                            `;           l,}i    .-1:))"    "<)!_t!    ^<{++|_          ;`
                            ^;           I"~l    :[[;[}"    "{\>-|l    "[|>+(~          I'
                            ^,           ;"{!   '>1_^?(^    :])l])l    "]}i<)+          I'
                            `,           ;!{l     ;I;(1`    ;?\!{\I    "{]!+)_          I'
                            ^,           '^"'      .',,     ';I^:;'    'I!^"l"          I'
                            ^,                                                          I'
                            `,                                                          I'
                            ":                                                          ".
                            :l                                                          :.
                            ":  '"    '     .    ``''    ...''''' ....'.      . ......  ;.
                            ^" '?--?}-<_<>-I,-<<>^`::_<~_;:,'`^^^l`'`'`"<:<~~!,i,`''..  ;.
                            `I  "[?]1+i!]]-i`-}{-><!.:-]]:.`-~_+IlIl":!:l.<}]~.;"~>i__, l
                             ":"`!;l;^;'I!:,"l!ii<_>^ ;l;,`"!lll,;i!li>I,."iI!^:"i;;~~I;^
                               'I;l;;;'l;lll:`lII;:^^!lI;l""I;I:l^^Ill:I^:lI!!i":;II;:`.
                               .>:->._!iI]?`i!;>_?`<!:<??^>>,<]>:!i:?{i:i>"_~,!!i;[("<`
                                ;l;IIl`l;l!;:^l;;il:^lI;lI,"!!llI^"lI!!l";I;;:l^III<I!'

                                        `~_!,?l}i.]++]_~I!]~i?-__:-~i~+<^^;?~>I!?}<+:
                                        ..,,.`'"' `:^""`'',"^:",,'^"^,,"..^:,"`^",::'

                 !{i ._->il_[-_+I-~,~_+-~<<
                 '`'  ``''.'.'`'''` `"`^`'^
                             ."";"","^^^`^^^"""""",,::,:,,"""""",,""""""",:;,,""""""""".
                            ";'lI?}}>[\1{+_(>","""""",,:;:,,::::::::::,"""":[I,",","~I`I^
                            !' '`;lI;:Il!"":^``",,,:^";:",""`````^^``">{-{}</<>]>[<{[; 'I
                            l'   !~++^<~~'     ;<>l[;l]>>]<;          ^l]1]"+!^,^i)?^' 'l
                            l'                    ^.         .^          `             `i
                            l.      .>~+<^`l      i!;~:      '<^<!       ~"ll'         ^>
                            l'       :II,:;[.     !i_\<      `+i\}       ~l))"         ';
                            l.           ;:}.     !!~1i      "~i1-       _!))"         ."
                            l'          'I;}.     ;<~)<      .~>1[.      ~l]|;         `;
                            I.          .:l].     ;>+)~      .+>)}.      ~l]\;         `I
                            ;.          .;;?.     Ii~|+      .+i1{.      ~l1|;         `I
                            ;.          .;I?.     Ii<|-      .~!)[.      +l[):         `I
                            ;.          'l!1      l<<|+      .+!([.      +l]),         `;
                            ;.          .!~_      I>>{i      '<!1?       >![}"         `;
                            ;                                                          `I
                            ;.                                                         `;
                            ;                                                          `;
                            ;.                                                         ^l
                            ;.                                                         "!
                            ,  ">;:,",,,;::^,,","^^,^""""^"```'`^"^""^`^^``^``"^''''`' ^I
                            :  I{}}}\><}-[{^l_}?:''l^}+[~'l^"",^,;'`'''I:i][]"i"^"",`. `:
                            ,:' l_!+l;^!_~I^:~?_-?{; ^?<<.;l?_]~^!~iI]_I' ?__^l`~1])" .;^
                             `,";;::,^^"^^^"^`"^^,:"^""^,""`^'':""":"","""I,","^^^"":":'
                               "l>~I:;:I>~!I:!I~~!l:;;><;!,!;~-Il`lI__;l,!!_+;l,l>_~Il
                               ll~<;^>!;<-~:i+:-+!I>>,~-l!i+"<},l,!:-1^~i>l~>`_il<-]`]
                                ""^^". ""^",  ,"^^" .,"^," '^`'"^ ^:^^,^ ^`'`"` ",,,:'
                                   ,`..^.^` ,'.'.' `` .'' ' ^... '   `   .`^ ..'.     ....
                                  '>_+"?l-+.??~-~~;l]+>[_+_;_+>_->"^;]~ill+?_}><?~:?_-?~~>
                                                                                   ..














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


                                                                                               '"^"^^, :'``"'
                                                              '`'.``''..' ...'' '........ ..''';}]?-~+'-;l_],
                                                              ~1~<i~~-?l+.~+_-+I_~"+-~![<:+~-]_-~><+[I<~?-[~.
           .^^^^^`'``'```^^`^^^`'''''''````''''''''''''''''''..'.'..'...'''''..'...'.'''`''. . ''.''''.'``^^.
           ':::::,^`^","^",,"""^",,,"",;;;;:,,::",,,,,,",;;;:,,:,",,,,,,,;;;;;:::::::;II;II;:::::::;IIIIII;I`
                  ,~l  ii!;;<]ii;
                  "I:  ^;I"^:I!I^
                               .`^`''``.'.'`''^^^^^^^^^^,"^^^^^^^^^",,,,^^^^^'^^"````^^`
                             .I,:li]?<>{]}?~}];;;;;;II:,::::;;;;;,,::::,",,:;~i:""^",;I"I^
                             ,: ^I!-<i!_>_<l_+^^^``^'`^^""^"""""""":::;>_+>+i1-:+i+>~[i  !
                             ;,   ,~-+^l_>,     ^+~>]i;]<!{~!          :>(|/!?[">!~1r~"  ,
                             ;"   '`^^.^"`` .   .'.'"'."'^,;:            .^^ .`    `;    ^
                             ;"    `` >~[+~+"    '^        ^"'" ;~[->+>     `.           ^
                             ;"    ~].   '`!:    <(`   ^'::,^I1,.'`,"!I.   ')~    '`,`   :
                             ;"     l  '!!!(]    ">. .l?l(};" ;^  `}:]):    ~l  ._>-\+   !
                             ;"    .?. :\+i?_    ,]` ^{[:\]," <:  "}:-1,    ~>  ._i>(~   l
                             ;"    .-  .;+!t}    "?` `{[;(1I" <"   il|1^    <i   "<~f+   l
                             ;"    `?   ^_!|-    "-' ^{?l1~," +^   +l1["    ~>   I<l|~   !
                             :"    `+   ^~<)+    :]' `~}l{};" -^   ?I}{^    ~i   i<<(<   !
                             ;^    ^i  '~>I}+    :+' ^<?i|]I" <`   <;]{^    i!   !+~f~   !
                             :`    "?  ;{;i[~    ,}` `-]!|[;" ]^   ,I{}^    -~  ^-l+/+   i
                             :`    l+  :[<!(~    :{` `][!1{!^^]`   >l1{^    [+  'i!<(-   ,
                             "'    ..   `' ..     .   ''''''. '    `'`^     ``    ^'"`   :
                             "'                                                          >
                             :`                                                          ~
                             ;^                                                          i
                             !^ .^^    . .. ...   ''.' .  '..'''''.''''...     . ....'.  !
                             l` ,[???[<!?<>-:,i<+!..;;]<__,i^''.'"i"""`'":I+++l":`'''^`  !
                             ::  l)-[{>,<]--;'i]{?>~l l[?-.::+~-~";;I^;!;l'_{[!^":>!i~<,.!
                              ,:^^>I!:^"`!i:"";;!i>_I'.iIl`,"IIlI^;!lIiiII':iI;^,;!:;i>l;'
                                `I:I;I,`I;I!!"^l:;::`,l;;;l`,Ill;I',I;::;`II;lI;^lll;I,.
                                ^;l~i.<>i>?-`i+;__+">I"~]lli<"?{,i;i,]{;!i>"++^iIII]1`]'
                                .I;;;;;^ll!iI,"lII!l",l;I;I^;!!i!l';II!Il^I;;lII`I;;!:!

                                         `_+<"?l]~.]++[+<Ii]<>[+<+:?~i_-<"^:?>~I~]]~?`
                                         ..^:.^'^` ^:^"^`'',^^:^",'^,`,,^'. ^",'"^,::.

                  ~{; '->~!<}{+-:__;l_~-_~~"
                  ``'  .``.''``'.'`.',^`^'`.
                              ."""````''''^^`^""""""",:::::,""""""""",:;;;:""`"""""","^".
                             ^;'!l]})<]|1(-]\<::,,:;I;:::::::,,:IIIIll;:","":[:",,""^<I^l`
                             ;. `^l!i:I!!i,:l,``",,::,::,":""^^``^`""",>1-??>/!<?<]~1[i ^I
                             ;.   l_-<.~ii.     I_~<{,i[l+[?,          ^>})[;[I^";1|;^' `I
                             ;.      .:"::::               l'   ":,:::'                 `I
                             ;.   .<:^~l<>i!     !l        l.!l i~>_<~`    ^~`          `I
                             I.   .<!   ^^I<,    ]<.  ";:~lI.l-.  .;^>l    :):   ;^!>`  `I
                             ;.    "I . i<]\!    !i   ,<~|_l. i   ,-<\[    '<`   _I}|:  `I
                             ,     :>   !<_(!    !_   "<<|+l'.+   ^~<)]    '?:   ~l[),  ';
                             "     :<   !i+\>    i_   ,<>|~l' -   ^<<|]    `],   +I[(,  ';
                             :.    l>   ><_(!    <-   "><|~l.'-   "+i)?    ^{,   +l[),  `l
                             ;     :l   ><?1l    <<   :~<|+I.'~   :_!)]    "[^   ~l}1"  ^i
                             l     !l   <!-(I    !~   ,~i(~I.`~   :<<|+    `-,   ~I]1,  ^i
                             !.    <>   <<])I    ~?   :_<(_l.^?   :-i|[    `1;   +l{\:  ^i
                             :     i,   I:<+"    ii   `l;->;."!   "~I?<    `?,   !I<}:  ^!
                             ^                                                          ^l
                             ^                                                          ^i
                             ,                                                          ^!
                             ;                                                          `;
                             ;  ^i:,,",,",""^:,",""";::,::::^^^`^""",,"","^^^^^"^`"`'`. `:
                             I  I??[[(i<[~?}`l~][; .i:{~{~^i`^^"`:;.'..'I:i[[],I"^^```' ':
                             ,:. ![i+>,'I?+l:^<-_?-]! :]!!.:<[][+:~>>;]-l` >-_"`'i+>-}-`:"
                              ^,":;::,`^"""",^^,",::^^,"^:,"^"``"^,":",:""":,,:^^"^`^,":`
                                :Ii~l;l:I>~!I:l;<>Il,lI~~:i">l_+;!^iI~+;!,!!++;!"!>_~ll
                                !;~<i"+!;<?>;><;-_l!!i:~[">l~I?]`<:>:~}^~l!l+i`-I;i_-^?
                                 ,"""" ."""", .:"""^ '"`'"^ ^,^^"` ^"`'"` "^^",' "^`^".
                                    "'. ^.^^ "' '.. ''.'''.' ^'...'   ^ .'.^` . `.    '..'
                                   .<i?'?l-_.~?~??~;I]-~}_~-;+_++_+:^`++-li--__;-+Il-_}]>?;
                                                                                    .














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


                                                                                               ^^""'" '^.'"^
                                                             .''.''.'' . '.''' .....  .. ..'..`?]?]!-^!!:i]<
                                                             ;1?<ii~~]l?'~_?]+i_-,<-+;]-;>?+?~--i<~-ii_-?-_"
           ^^^^^^^^`''```^^^^^^^``````````'''''''''''''''.....''''.''.''''..' `''.''''''.'' ''''''`.'..''`^'
           :::::::^`""^``^"",,""^`^``^:;;;:,,,,,,,","";;;,,,,:;;;;;;;;;;;:::::,:;I;III;,:,,::IIII;:,,:::;;I,
                  _+  !+l><l:;<ilil!>>,
                 .!l. "llIl:"^^I:!,IIl"
                               .'. ..'.  ...'""^```'''`"""^````^"^``'''`````'`^^`'''`''
                             ,:"ll--_!]}]_>~-:::IIIlI::;;;;lI;,,:::::::,""""ll:,;::":!":"
                            .; .;;_<>l-+-~l+-"""^^^``^^``''`"::::,"""";<<l<l?],~!>>i]~  l'
                            `:   ^<?~;"~!I     .+++]-"-_l]+>'         "~(/j~[):~l<|\]:. ;`
                            `;   .^"^''^'`      ^``,, ""`:,"            .": `^    ^;    ;`
                            ^l       .^'..       .^~ '.     .'!^''.    ' ,;             !`
                            ^I       i){+;      :))-;11"   .}]{I[|!    _1)<>|+          i`
                            `:       i){+:      I){];){`   ^{1)l?\;   `-1)>~|<          !`
                            '^       >1(_;      ;)1[:{{`   `{11l]|I   .[|(i~(<          I'
                            '^       i-({:      ',I?,[}.   ':,-;+(:   ':I_>>|>          I'
                            ^,       >\?]:      '.'-;){'   .. <!_):      I<<1~          l'
                            `,       <v|_,     .?]]-l|('   <[_1l}\;   l}[{~-|~          i'
                            ";       ;_I,'        .I:+>       !;~_'      II!?l          i'
                            :l                                                          I.
                            ^:                                                          ;.
                            .'                                                          ;.
                            ''                                                          ;.
                            ^"                                                          !.
                            ""                                                          >.
                            ""  .^    .     .    ....      ...... ......         ....   <.
                            "" `]__?-_i+<~-I"i<_<'.:;_~++:;,.'.'`!^'`''"il__>l,;``^'..  !.
                            `I  :)-])_:i[]-l'>?{?><<`;}]]"^"_i~<,;;!";i,,._1}<.,"<i>+>" l
                             ":^'<ll;^:'l!,,,lli<~_>^ lIl,",i!!l",i>l>~;" ,i!I`""!;;~>I;^
                               'I;ll;;`IIIiiI^ll!I:"^!II;i;,!l!;l^`llI:l^:lIll!^:II;l;`.
                               .<"+~'+i<:-]`!il<~]`<;,<--`~~:+[<"Il,<1<;~>,?~:Il!;[),>"
                                ;l;;;l`ll!i;;^l;l>l:^lIIlI,"!!i!I^"l;!ll,;l!I,l^II;!;!`

                                     ;~?;!+!1I"[<~-_~,<?~_[++<;[<<-_!``~-<-~<i!++<<!<~~I
                                     . ;^'`'"..^:^""`.'"^",^""'""^,,`..`:::,"^`':,,`,,:`
                            .
                 ,+i .+-~<_I+>+--~>
                 ...  .''.`. .'```'
                             .^""",:"^^^^^"^^""::;:;:::,"""""":;:,""""":;;;;,,"""":"^""'
                            'I`:;~[?<<1{1?~1-",,""",,,,,,,,,::;;::::::,"":,,]I,,;:;"!i`;"
                            :" .`:!;;,Ill,^:,``^,"","",,^,""``^``````^i{?-]i)+!?!?-{]!  !
                            :^   :+-~"~<>"     ,~<i->;?>l[<;          `l}}}I]l`"`I[{"'  l
                            :^                    .^          "          '              i
                            ;^       i?<<;.l'    !]<I~!     "~+"<i.    `~?:!<^          !
                            :`       "I^`l"{"    ?)i_|-     i/?i)1'    ,\}I1\;          l
                            ^'           I"{"    ~)><(-     I{-l{{'    ^}[I]);          l
                            :`           !,[^     _+!)?       <I1)^      <![)l          l
                            ;`           !:{'     ^~i{]       _![[`      >I}tI          I
                            :`           i"]`     ,<i|[       ~l[}`      i;?|I         .I
                            :`           l,]`     "<i)?       _l{(`      iI?\l         .I
                            ;`           . '       ..'.       '.'`       '''^.         .I
                            !`                                                         .I
                            "'                                                         .I
                            ;'                                                         .I
                            I'                                                         .I
                            I'                                                         .I
                            I'                                                         .;
                            I' `!I:,",:::",^","",^^"^"^""^,`'`'`^"^^```^^`^"^`"^```^"` ';
                            I' ^_}{}(~!}~+}":~[[>'';`[~[]'!^:""""!.'..'""!}[];!I^^^",^ .l
                            ^;' :[i<>:^;-+;""i--]]1< ']<~';;{_?~;l~<;--I` <-~:"^i-!<{?^::
                             ',",,":I,,"^^^"^`"^"",^^,"^""^`^''^";::"","^^;;;:"^^^^`"":"
                               ^lI~!:l:li~i;:II<>iI::;<~ll:l;+-I!`lI~_;l"!!+_l!"li__I!
                               ;!l<!^~il>-~"!+I_~<:>l,~?il>~,~]:l:<:_}:i!>;~i'~I;!_}`-.
                                ""^::. "",,"  ,"^`" .,^^"" ."'`"^ '"``,^ ^"``"^ "^'":`
                                       "^  ^.^' ^'.^'...'.''''. ``....  .'... ."  '
                                      .<+?`-l+l.~]+]_~!;]]~?---l>?i+?+,^,-__<+l+<?-__i















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


                                                                                               ."^"^^, :'''^.
                                                              ''''`''''.. ''''' '.... ... ..'..;[?]_<~'_,;_?,
                                                              ~}<<i~~?_i~.-_--_!->,+?~i]<:+?___-<i<~[;~~??-<.
           .`````^^^^^^^^^`'``^^^^^^^^``'``^^`''''''''''''''''..''..'...'.'''.'^...'.'.''''. '.`'''`''..'''`.
           '""""":,""::"","^^^"""""""^"^"`^""",,:,,,,,,,,":;;;:,:,,,",,,,,:;;;;:::::;IIII;,::,:;IIIIIII:,::,'
                  "]!  ~_;:<l!l!lIll>_Il,-;__l.
                  "!:  ,;"`:::::;:":l!;:^l;llI
                               .''.   . . ..  ``^^""""^```'`^^""^````````^"""^'``'`^^^`'
                              ;:,I>_-~<]--+<-~::::::;:::::::II:::,,:;;::":;::i:"";",";;,I'
                             ,; ',l~ill_~-+>_~;:,",,",:"^`''^:::::::"""l_!!il(>;~I<i<[i '!
                             "^   "~-~";+<,     "+~+{i:?~i_>;          ;-)|t>1+!-i-(t+;  :
                             ^`   ',,".`"^`      ^^`:^':^"::^            ^,: ^     :I    ,
                             ,^       `"'"''.   `'....                                   !
                             ;"       >[~1_-I  "{{}{){^                                  !
                             ;,           ![l  `[[}{{{^                                  !
                             ;"           i(i  `(}{))1`                                  !
                             ;"           '^'   ^^^^^"                                   !
                             :"                                                          !
                             ,^                                                         .~
                             ;"                                                          !
                             l,                                                         .:
                             "`                                                         .l
                             :`                                                         .~
                             ;^                                                          i
                             :`                                                          ;
                             :`                                                         .;
                             :` .^^         ..   .''.'    . ...... .......       ...... .;
                             I` :}][[[<!_l!-:;~~+I''iI-<_<"i`'''',l''`''Ii!_?~;I;`'^^^` .i
                             ::  l)?}1<!>-??:"]{}~!ii ![--.;:+>+i,;l!^;I:"`?1}:,"I<!~_i.'!
                              ,:^^>I!:",.!>,,:!!!>>+l''i;l`::ill;";>>l~<I:.Iil:^";!:!~i:;'
                               .`I:l;;,`l;l!!,^lII;:`:!;;;l^Ilil;I`:;lIl!"!IIll;^l;I;I,'
                                ^:i+i.>!I>?_`i~:+_>,ii"-[I!!>,}{^>:<,])"!l>l]+`>ll>}{`]
                                .;l;ll:^l;Il;""I;II;^:IIlI!^;l!>!l'I;;!;I^llllII^lI;!:I
                                   .
                                  .+~_'-I??._?~-~<;l?~<----:-~>~<<,^I[+;<><<<>i>>>_+>lI-i]~:
                                    '; `'^` ',^^"`.."^`"^",'^"^""^'.."^'^^"^^^:^",:""``,,":'

                  ~1: "_]~?;>__]l
                  '`.  ''.^ .'``'
                               ^""^^`^^``'`^'`"""""""",:,"""""""""",;;:""""""^",:,"^"^"".
                             'l`:;<[{<~)11[~{?,:,,,,,,:;;;::,,,,,,,,:;;;"^^^"~,"^"^"^ll`I^
                             ;" '";i!I;l!iI,l;^^^""""^"::,:""```````^",>{-??<(i!_l-<[[! .!
                             l,   ;~]_"<_<,     ,+<i[lI}~<[<l          "i1/(I{i":"!{(I` .l
                             I"                            .                            .:
                             :`       ;I!>.      "              !I,       ^I;;:;;`;'    .;
                             :`       ])}i      ,}~i>i!;<`     "]11I      ~{)){{1_1^    .I
                             :`       -(-`      !)11)){-):     "-|)-      I+{--+~-('    .;
                             :`       ?1(_       ... ..:~      '1{}{      l)[+1{{+1,    .;
                             :`       --[+`     '""^""^:_.     "f){?      <}}-_+~<_`    .I
                             :`       }\?;      l(111){_)"     ;1{/_       `I':;::       ,
                             !^       }u1]'     !|1{[1{~\"     ;[}ti         `i~}\:      `
                             l`       [x~;      l1}[]1{+{"     ;1-|?            '>,      ^
                             I`      ._?~?`     '``^^``"i.     :][(`      ~+--?]+<_.    .;
                             !^      .++j:      ![)({-}_1,                ....'.''.      ^
                             I`       ;I>.      "<<ii<il>`                              .:
                             ;'                                                         '<
                             ;'                                                         '>
                             ;'                                                         '!
                             l` `iI,,^",^""^^",",,^^"",^^^^"``````^^````^^^"""""^````"` ';
                             l' "]}}](<l]~?{:`+[1i. I"}<}+'l`^^^`^I.....::![[];;,``^^^^ .I
                             ^;' "}>-<I,:--<I^>-]?_}i `[<>."I[?]~,!~i;??l^ <--:^^<+>_}~^,,
                              ',";;,:,^"::;,"^^,",::"",,":"^^"``"^":I:;l"^^,,,:"","`^,":"
                                ;I~~II;lI++iI"!I+<;l"lI~<,i:il_+;l"i!_~;I:!<~<II:l<+<lI
                                <;+>;:<~;--l:I+;_-;!!i;~?^~iil_]`>IiI_[`<iI~<!^<!:i--"_
                                 :^^", .:^^"" ."`,,' `"``,' ^,^""' ^^'`,' ,^"",. "`'`,.
                                         ^". ^''" '^.''''.`'..''  ``...    ''. .''..
                                         !~1:~i<[^l[+-[+<:-?>-?-~il[<~-~I`"<+~+iI--]+















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


                                                                                              '",,"^^ ;'`^:.
                                                             ``''`''`'.. '''`' '..''.'.' '''''![?-+<>`~:i_]^
                                                             -}+~!i~_+><'__[_<i]i:+]!~]!;+?-~-+<!~>_;~_-[]>.
          '^^^^^^^^^`````````^^``````''''``````````````'''''''''`'''''''...' .`...'.'.''''....'''''''.'`'`^.
          `,,,":::""""^``^"^`^"::::::,"",;;;;;;::;;;;;;:,,",;;;;;;;;;;;:,,,",,::;;;;;;;;;;;::::::::I;IIII;I`
          ,;,"~' '-;lI;<i!,~i+l
          '```;`  ``^'':;"'";;:
                ;l;^i!,;`I;:'l;l":";>IIl:;I,:",l:;;;l^:,:I;::`",`I:^,l,::,'"",:," ':`^;"",^^,;,,"
                ^:>;;ll;:_ii"~>i;;;l~~<>~>>:I,;<!il>~"lili>>i,II"li:l~~<<-"!i!<<l^"-;l<i>~;:+_i~>
                                             ..      .          .....
                             ::;:I!iIli>>i!>!;;;;;;IIIllII::,,::;IIIIl;;,"",::;:;:::I;:,
                            :: ,,+-_!_}[[+>1~""^`^^'``"^,,:::,""^^^^",II:I!;)I:l,;I!_l :;
                            I'  .;>i!^Ill'   ..;!:^<ll"<i!'..........`~\(/??-i<[[/-{-: '<
                            I'   ;iil`lll^     ^I" i:;^>;I             :>>';    i<`    'l
                            ;'                   "1`         i>                        'I
                            ;'      .1_~^        .>+!]>      .?;]?`                    'I
                            ;'      .)?-^         "+<)-     '"_!))^                    'I
                            ;'      '1}},         ;~~|~     i\]i|}'                    '!
                            ".      .{1|,         I<~\~     i(]!|1'                    ^>
                            :.      '([\}.        ;i+(+     i\]!|{'                    ^<
                            l'      ^|1{}'        ;i~|<     it?i|{.                    ^<
                            l.      ^|)[{{:       !>~|<     .,_i({.                    `!
                            l.      `]+~_?I       ;ll-l      'il?-.                    ';
                            l'                                                         `;
                            l.                                                         `l
                            l.                                                         `l
                            l'                                                         `I
                            I.                                                         `I
                            "   '                                                      `I
                            ;. :]_<<_lIi!!i^I!!>;``I:>I>!,I`'''',I^^^^^;;Il!l,,"``""`. `I
                            I` "}-[]{:,?-][,,~1{<;;:'?][+.I:!lil,l",',:I,;[{[:`':I:I!; `;
                            'l":_l<I `^"+>,:"l<+_-[: '+l!';;<><i,i~<l_~l" ><>""`l<li_>,;'
                              `^,:,:l^^l:;Il,"I:,,:":l:,;;`,:;;ll":I:":,^;;:;I,^:",";"^.
                               ;li+l^~l:_->,l~:]-!;I>"~];!Ii;[}">,>I[{"<lil_~"+ll<_-"_
                               ,!!ll;!:l!>!;;!Iii!l,l;l>;!,!I!~;i"i!~-l>:il!l,i:ll!~:<
                                .....  .....  .         .             .      '  ... '
                                               '<!;"<;+:'+ll:I>ll:~lil,~IIll"
                                               ',i!^l:i"',Il":i!l,!!>!"illii,
                .....        . .
               .+]~?:     '..+<[-~<i~~l_-_~+_!:<]+i___+l;_]>_;-i_!+<_->~:<~<<~[~^~>[<_,
               .,::;^     .  I,I:""^""':":",,^`^,,,^:,:^^^":"^^^,,:`,"":`,^^"","`,":,,^... .^. .  ....'....
               .>~<_,     '..+i_+>~li<'<~~++~~:`<+>i+-_+I^<]i_`!?<!,_~_+<+,:+i<<~_:.~>{__,!-}!']<>+_+~-_+>`
                             ~-l~-~i_<~;;_<>!+++;
               .I;,,:"       ;::,"::,,"`";"^''``.
               .<<ii<~    '..!l<!i+__>:I_~<!
               .l!>>!     . .<;:!!,:^l;;:Il^^;II:I
               .Il!:I.    . .;:l!lI:"illll!",i><!!
               ._+!i+-    ...i!<i!l<!i";>;>"
               .;;:::;`   .  I;:","l:,^ll;!,'.'`.'.     .        .   '
               '-+~~<_]^  '. !>+Il!>~>,_><i_;!?[:~<<;<~?_~~:~~<<~}?,i[-]~l<~~_-<<]-_ii]-+_-~I?:-__-_i+,<+-;
                            .<<_Ii+_+>~!~:~>~i-~i-<<<_;  .  . .. ..    .   ..''..... .``' '. '.'^''' '.....
                ^`''^`.      l;:`,:;;^:I>:!I:,:;,I,,^;^ .            '
               '??~?_]!   '. ;i+;:!l>>^_<_i<'<--'!~:l>~?-+>,-><~~?i^+1+?!;+~_?_~<]~+;<]?+_?<!-,-_-_+i_:~-{:
                            .~>_Ii+-+~>!<"<>+>]><-<~~-: ..  . ..... . ..  ...`'..''' '^^'.''.'.`^'''.`.''.
                ^''''`''.    l,:^",::"^,>^;;,,,":I,,";`                  .
               '_+_>~__>I '..~+>!i^-?_;>~>>~->~-l!~>,<<!->>,~I<-]~_?,+-[;__l;-++>~_I~_>-<~__i"_~<i];__,`+>I.
               .l;I::;II, . .l:,""`;;:^:I,,:I",;^:;,`,"";",',`"::::;'":;`;:"`:,:"";^""",^",:^':""^I`:,'.""^
               'i!<!<+<~i . .<+!lI^i<_I>+~+_?i+-li_~:<><?>>:<,>~]___"~+];-+I:_~+>i]I<_<_i<~-i"__<i-;~+:'i!I.
               '~>!       . .!I:Ill!;
               .I;:.      . .::,;;:!"
               ^]+i       ' .]+~~<>!~:
               .;;^       . .::;l:",,`...`.  ...'  .  ...  . .      . .` .    .. .'  .       .'     .   .
               .l_:       '..<-l>~"~?<?<i-i]:>l!_+:~_?<<<?!_?-~]:~]_-.l[+--,_;~_<;}?_~[><]<+<!1[+>~]I-!;?+;
                            .!++<+>~:<,i>ii}<>;                ` .      . .     .  .. . .' ..  ...'. ..  .
               .,.          .":;""^:`^'::;,"""^..     ..   .          .' .    .   .
               .-:        '..<_!<~^<]++>l+I+"~ll>~;~~?<+~~I_-~~-I_-_+.l]++-:_li_<!]_+<{_<]+~~i{?]>+]l-<I-+;
                            .i~~>+++;<:><~~[~~:      .   .  . .^.....   . . ..  .  .. '..'.'' .''.'' .. .'.
                             `,:^^":'`':;::,,,`














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


                                                                                                ^^"^': ,^''"`
                                                              '`''``'''.. ..''' ......... ..'.'"][--i]'~l;~}!
                                                              !{-<i<+>_!-'+~][<i_~,~_+i{~:<?+?__++~~]l<~+?1<`
            `''```^^^^^^^^^^``````^^^^``'```````^`````''''````'```''``..''`'''.^''.'''.'`'`'.'.''.'`''.'``'`'
           .,"""""""""","^",,`^^""""""^^,`""::""":,,,^^`^;",,,,:;,:,,,""`^^,,,:,:,"^"^::,:,,::^"""",:;;::"""'
                 ^~!i~!;I+~" ~l".;I!!!;l lIl'^>>i.;IiiI!;.<!Il!:.l;llI,.>ll!I;;I^">>i>.,>!ii:'l:I^;;I^`IIl':,
                 :~~~<>i><_+:<~i!!<>>li<:~_-!l!!!`;;Iil+;'il>l>!'iIl!l,`i!~!i>:>I"!i!I`"!!ll;"<li^i><,"><~"II
                 :<I~!_~i"!!+!~i+ll">"<liI>_~;
                                     .        ''''''.''''.''''`'.....'..'''''..........
                              ";::;!>ll<iill><IIII;I;,,,,,,;;lllII;;::,""",:Il;:":,,:;;::.
                             ^I `Ii]?~+\[{?~{]:I,I;""^""^,:":,::",:,,""Illi<!(<:l,Il!~~ ^l
                             :,  .,i>i,:!l" ^+>'i,.II!::>,.i;l;lI^....'~?~_?>~>I{{|~-?l. "
                             "^   "!i!";!;, i[[i}" )(|<<)< (1/_~)<               !l      ^
                             "^             `_\[>?}'        .   _1[[_]>      i^_++<i  "|l"
                             ::     ....    '~[~>~I^'`'`        i?]1!~~'..`  <!+?[1>  '1_I
                             :,     >Jt}       .[<'_\})['          >[':){{{;     .}!     !
                             :,     "{-~.      ._i`>--_+.       ,>l~-";]-_?^     ^]:     !
                             ;"      ~_1.      '[<^~1]1]'       >\{}(,I/{//,     :1I     !
                             ;"                 ...             .    '    .       `      !
                             ;"                                                          !
                             ;"                                                          !
                             ;"                                                          I
                             ;"                                                          i
                             ;"                                                          ~
                             l,                                                          >
                             :^                                                          !
                             ,`                                                          !
                             :`  .'                                                      !
                             :` ,]_<<~!:i!l!",ll!;`';,iliI"I^''''^l"""``,;,;I;;;:```^"`  i
                             ," '~))((_l-_](;'-{)+::!'-]}]'i^!I!l"I^"'^":;,]1}I,,:;::lI. <
                             .;"'`?i+I,;'><;:^ii~_-]<. ~!i`::~>~<,;<>l++l: !+~;^"l>!!-_:;"
                               '^;:;:l:^;:",;,.,""^,'^I"",I"^,"^":``:::;;`";""::`,,^`,^^'
                                .ll]~`>;li]_"ii!+-+,i;:~->:!>:-}!;,i:-}ll;i;[_,iI!;_}"+'
                                '!!i>:>,!li>,lI!l!>:l:II!!;IiI!~il,!;i+ll:i;>i:<;iIi-,+'
                                  ..'`  ....'  ....'  '...'  '..''  '. ..  '.'`. .`'.`
           `:``;'  "!I:;^;,^"^^,:^`
           ^;,,_:  ;]~i~I<+]]><-+<i
                                   . ..    ..''''.............'.............. ..... .
                              ":;;;I!;;ii!i!i!;;::::::::::::;I;,,,,,,,:;:,,",:;lIl:"":;:,
                             "; :;<?_>+1{{-<)-,,^`^"^^^``^":::,,,,,,:,:;I::I;{IIl;l,;+! ,;
                             ;^   :<~>";!!`   ..;_l,l;><<;l^..........'it|/]>}_!-![}\_:  !
                             I,   "!il`IlI^     ,~;";:!i!:I.           .l><' ^:   .<<   .>
                             !:       .   .''.        l          I^ .       ^:          .~
                             :^   ~{~>__^]}[?l       !Il~'       !l!-^    . :_l]I       .~
                             ^'               .:^"  :l,`:l^.I:" ,`  .,",                 i
                             `.        ^";I'' ^(][. l~>--+;'~_}!?"   -[}i;;;;;I;II'      I
                             "'        .'--:; '~_+.    +:    I-]l    :~~_-_++____?^      :
                             :`          -_;! `__+.   '_;    !?_!    I-+_+++++++~_`     .;
                             !^          ~i;l '!i!    .>,    :<>:    :>!><>i!>>i>~'     .;
                             !^                                                         .;
                             !^                                                         .I
                             l`                                                         .;
                             ;'                                                         .;
                             ;'                                                         .;
                             ;'                                                         .;
                             ;'                                                         .,
                             I'  `.         .     ..         ...                        .;
                             >` :]_~>_>i~ii~";ii<I''::+!~i"!^'''`;<,"^`'::;!i!,,"''''`. ';
                             l" `<)-?|<:_???,^<{{<;I,.~-]-.I"<>>l,l",`:;:",]}};"^:I;l>; 'l
                             .;,'^~l!:,^`>!^:";l><~];..<l!':,><>l":>il~~I^ ;i!"^^;iIi->,;'
                               '^l;lII"^l::ll^^;:;II`,l::;I`,;:;ll^,;:,::^;;:;l,`;::":^^
                                ;;<-l`<l:-]<,!+:}-iI>i,[];!li:{{"!,i:-["iI!>]_^>ll<-[^_
                                "!l;;:;"Ili!;:IIl!!l;lIll;!,!li<ll`l;l>:!,!l>!;l,ll!<:i
                                     .                                            .. .
                                               :+<,;<I~^^?_!~:~!!!lIi+ll,~IIIlI
                                               `"i;"I,;''iI,I"I;i<:I!iIl^!IIl!I
















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


                                                                                               ^^^"', ^^.'^^
                                                             .'''.'.'. . ...'' .....   . ..'..^][-]i[`<l:~_;
                                                             I}_<!<~<]!].~??}~l-_,<?_;]-:>?_}_-_>~~?!!+__]+`
           ^^^^^'''````^`^^^^````'`^^^`''''''''''''''''.'''...'.''.''.''.''''.^''.'...'`''' `..'.'`''.'````'
           `":::,""''``^,""^"^`''""""""^``^`",,"":;;;;:,:::,,,,,:;;;;::;:::;;I;III::::,:IIII;;,,,::IIIIII:,^
          .(i      }{ii~`~}>I_+[~.-?~>;i+<l;
          .{+'    .+?}]_:<}}[]{))`][?(/)]||)
                 ..                                              .
                "-??I!__~>]+-+-_i?+_>;[<-<>~<-]"~~__><-<<[>i!_-!++~<>}_-+!]<+~[?,:_>~<~<![<-<<]i-_}I<>!<>l!i
                "+>~<<<~~".',..'....  .`...'`'`'^'^^`.^'``'''`"^^ .^^.`'''^^``^"`'"^^`^".^"^^`"^^^"',,^,,^^"
                '::I:l:,,
                 .:,  li,<<l<<>:I!:i^
                 ^Il. ;l;!!:l!l"":Il.
                      :!!"^Il;;+lI^:!iII"I!IiI:_l^Il;ll>!^l!!;lII:l^!iI!!:II"I:Il::;!";I!^::;^":^!:^",,:::.
                      ^,!:,i!;;iIl^;ll;l";,"lI`iI^l!:lIl<^i!!l!lI,!"i<<i<<ii"<IIi!:i!,i+!;>i_:!!,<>;i<!~+i`
                             ..     .''    .  '..'.            ''' .     ....    .'
                           ";"I;-?-_]<~]-_<<?!::::;!_+!~>>+;:ll!;;:::,",":,",^",:;,I:;,
                          .I  ;;_??_]!i_~_ii]>;;;;;![?!-_~[;,"^^^^^':i~!~!!>,>!i<i_>^ I^
                          ';       ,+_<I-`I;i               I-!+i"<](t][]1!>:~!l>i_I. ,,
                '.        .:    ''.`^::^:`.,I^       :      '"^"' ^,,^ .'^            ;:
               `+I'^^^^^^^;<::^;/}1["l1~{[l1[}'      l.^ . ^.'.'^"                    "^
               'I`.'````''"!''.,)-}l+~l'<[+    IIl,!,:'/([+;,>`>]}.                   "`
               '>".`^^^^``,i'`'^[_-!)1_<~"I~-^ ><~i_l:.|(_<i>!>!;`!~I                 ,^
               ';`'^^^^^^`,i'`':)??<,I!!+:I>~`   .:  ;.)(_+Ili!iI,<-I                 ,^
               'l^.``````'"i'''  '.'             ^;  I.?/i>;I`;+["                    ,^
                          'I   .`.'.".","""      `,  I.{f~_""":I;".^^'''              :^
               .:`..'''''.^l.'.:}(1~]"}+~[+      ^,  l ?~i_",]]?!}"1-i-~              ,`
               ^_:'",,,,:";!^"`^Ii!;             ^,  !                                ,`
                          `;                     ^,  l                                :`
                          ^;                     ^,  `                                :`
               .^. ......."l.'..............   . ":                                   :`
               ^-:'^````^`I<,,"''`^^^^^":::,^^^^^"'                                   :`
                          `:   ,I.                                                    ,'
                          "l  .-\,                                                    ;'
                          ";  ^l;`.....'....'''''.....'........ ......     .  ......  I`
                          ^, ."^ .`^!^`'`^"!^^`^',;'...'I:""^^^!,",,""l,ii,`:i"`''''  I`
                          ';   :i?' l ^~I`.;l_i<<``~_+]<,`     I      i`]]!,'I"<i>+i^ l'
                           ^,"`":I^':.^:^'`,,lI::",;IIi;"^'`'..,'...'`l^+I<_':,!;I>!::"
                             ':l!lIl`:IllIl`;IllII"lII;l:"ii<!!""!!i!i",l!!l!":lll;I^.
                              !"[<^I!<"]]"ii<;_?`-iIi_-'~>:>{+"i!:~}_"<>"_+l:ii,_)li!
                              ";:::;':lIi;;';ll!;:`I;I!l,`I;;II^^l;liI^"I:::I`,;:!ll`

                                                '_+~"?;]<._~ii<>~!~-~l?_-~__`
                                                  `,.'.`' .`'''',^.'^'^`:^^;.
                       '.
                   ;[+.~i+,~__~?_<:!~-{+>-.
                   .'' ^^^'"^`^```''`^`'^'  '. '` ..  .      .    .
                       <~>i!__+:<~_i?__:i<_l_]>!?~:~[<i-_+l;-__<]+>i_~>!!!~_<_:_-?>-?_<
                       ..'`'```````'.    .``'``''`''``'`````^`^```'```````^`'".''...'^`'''.................
                      ,-""",,,,:,::+]__~->,:::::::,,":!":;;;;;;:,,,",::::;::!-~>~<i~<:;;;;;;;,,,,,:;;IIIIIl_
                      :]:;;;:::^,^'>__[_}?:"^^"""```":>;,"`'``''^'^^^^^^'''.">ii+-i_~`''..'...`^^`^^^`''''`}
                      "?+?--]-)}}-^?]i~[<_i[(-[[{"```">_??]_[~_i+]l--[]<_[!?<~_<_<l-]}[{}?i>--?]-[_],`````^[
                      ,_?_~_[+_<!~l>?~++[:"""^```````">___~~~i<il<i>~~+<l>><i~]<~;;lIII;;,^":,":;I;I,^``''^]
                      "+<<i<>!<>~->~]~~<~"^^^""^^^^`'"><<!<_-__-!<ii]>_i">]-<~_~~^.    . '^^``'''.'.'`^^^^"_
                      "{)}{}__{<l1)-?[__l(){11[^^^^`^:?_}?-~}]_!>?I~_?ii[i-~+[_-~!+[}}?]__"^^^```````^^^^^"-
                      .:,:,:;;:;:,^,"";;;IIIII;"""",:;lI!!llI;;::!!l!il!iliII<l!!liii>i!il:,,,:;;;;;;;;:,",;
                   l_l.]_<-~l+i<!!~+]]~
                   ^:" :,^^"..""''"^,,"
                       <<_!!]_il~_+>+~~;-]il~?+:_]ll+<<+:>>i~>--,><_~+_~I
                         .. `'. ''.''.`  `. ',^.`"`'"^^"'""`"^";'""",",,`
                   ;<l.-_~+~l~-~>~+_+]>!+~-?+
                   ^:" :,^^"''^"`"^"":``:^:,^
                       <><l!<<>;>~+i+<~;?<;;>__,-_;i>i~i~<:l<i>+,!!i>>~>,i~_i<~<;
                       .'"^.^^^'^^^""""'^"^`":"'`,`:^"l":^'`,"^:`,,^,"";`,;:,,;:^


















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


                                                                                               ."^^^^, :''`".
                                                              '`''`'''... '..'' '.... ... ..'.';}]-+<~'+:l_}"
                                                              +1_>l<~-~i<'?_-]<;-i,~}i>1i:+-?---+><~[;<+?}]<.
           .``^^^^^^^^^```````^^^^^^`'``'`````''''''''''''.....''''....'''`''..'...'.''''''..'.''.''''.'``'`.
           '"":::::::"",^`^^^^""","^""^^"`";;;:,",;;;;;;;:,,,,,:;:;:,,,,:;;;::::::::::IIIIII;:,:,::;IIIIII:,'
                    `<> ~+i+~_+<+;~_<<<ii+;
                    ^II ":""::",:`,:^'^^";`
                        >>~ll_~>l><<!+<>:>>i;_<<>+>>l:~_?i><:_l+~:i!i~i~>"lli!>i-:;<ii!~>l
                         `,"'"^^'^"",:,:`^""`l:,,:",^',;,":"','":`;^;<,I"',:,";,!,"l,;,Il:
                       `<:",:<>i!>!I::,^:I,::,,::""^":;:;;;;>l!!Ill;^^"":;:::::"^""^,,I
                       :-'^. +-[}})_^^^^l<....''`''''..'.``,??]]1[{]"^````^^^^^^^^^`^^<:
                       ^+-i}{<`.'.`^^^^^;~?~<<~?l+?+~__>>^''.''`^^^""^`````^^^^^^^^'`'~:
                       "?+i][-;,"^````^^I<<+~!l>:<+~>_~>i:",,^^`'`'`""""""^`````^,",,,]:
                       ;[-i]-+:^`''''''`:>i-~{~"~<i<<<;?_[+{?<>.  .'.'''''. .   .'``^`-:
                       ;[-<[?];"^``````^;<-+++<_~>l!+[~<~<~<<i><<i!l_<<i><>!l!i!!!^^^^?:
                       ^<>i___I:::::,""";<+-?+-[-_l<-+~+-<_+]_?---]<[-__]?{]-1{__<,,::+^
                    `,^ :,""^,,,^^:::"^..                                         .'''.
                    I_l.!~~<l+i<,;~~~~;
                        ;I,^::,,^"::";:;^!;^^"",:;,",:,:l",',::^"',,,,^`"^^"",^`,,"":":
                        ";lI:!!!"Iii>~><"!<::iIl<i;l+~i~-li^>~+!<"<;Iill>I->><,:_>~>~~+'
                       ':""","^'``'^"""":,""^^^^^^"""^^^^^'`'..'.`''^^^"^```''^"^^^^^^`
                       !+'``^]][[?1~",""!!`^````^"^^^^^^^^`;-~+[}-)_^"^^^`````^"",,,:,]"
                       l_<~l>-~-[_-;'''':i<lll!!I^:;;,:III;!<~i~~>ll:,,::l;l!I,,,'''`"-^
                       l[}}??-il~~<"`^"^I~+~_[<-<;-[?_+-_<l~+>-_+?!l[]<+~]!_-i~_<"^^"^_`
                       I[]<+][]]]-''''^`!_~><?>-<;_l<-~<<!++<i_+~i`^'''''..  .  .^``^^_`
                       ;-+~__lll!l,,^^^`i_+>~]~-~;>li<!~-><__+~+>i:^,,:,;IlIl:l;:"::,,[`
                       :__i-!           ;<<i<]~_>I<_-i~]++Il-?;___~;+_~]??-_-;++-;--!.?^
                       i;               "i>~]">:]<i~:l<-<!_+,!_+I<><]>~+"iIl_~~<_~l:i -^
                       i~""""^^``````^^^I_[}<-??]![?-]<[i}}}{?~``"`^,^^``^^'`'```````'[^
                       .:,,,:::^"^^^",,::,,;:,,"^:l;;;;;;;I::::,,;;;;;;;;;;,,,,:;;;;;;l
                  >[: "[]l>_i<"-_-_+<<l~!i<
                  ^"' .,`'^`'' ^'''`'''.`^'
                      ,i"[^:-i+;,~i!<!~_"+<_~-I<<-_+~]+Il+i__+_i"-?-~_~i!'}-,<l;-__--~+<:[:[<!^~~<:l~[:i<l~~`
                      "<>+~~l.' .'.'' '' ''.."`'`'`.'^''``'""``..^`^^`^'`.'^.`''`",^:"^''".^`^ ,;'.',".^''^,.
                      ';,,;,`
                             ^^^'..'.'`.'.'`'`"""^^^'.'`'`'^"^```^`^^"""^^^^^^"^``````
                           `I^,^<?---~I]+?~l+~^:,""^~-i!_!?!:""^"^:;;::::"^^^",,,,,:I,I'
                           l' !]/f[/)f\{(]{[1|+iii~+|t/+})|+I!>+!_::i<;`,<_-_+_;:::;: ';
                           l. ">!I^!{{/_1:i~~<:""""::':. ;'`:}+{-~l_[1I::><I;;I.       ;
                           !.     .'lIl;l,'':'       ^`      !II: :>li",,;`           .;
                           :.   ]{|1][;[/)~,"'"'"    ,,'"''.` ..^:'                    ;
                           ^    _[([)}i"ii+<>`;;i!>, ,^>t]-i_}:,?|>  ....'......'''...'I.... ;'
                           ^    }-~i){}<~l^<-I   l>, ,^</]_-\{+~-,_}{"``````''``"""^``"!`^``.>`
                           ^    {[??",;;l;^li"       ,^i{~<"!<~>+:i+_"``````"^`'''''''^l'```.:,
                           :       .                 ,^l)1l>>>;]{-   ...''''``''''''''^!''''.<;
                           ;    ,^^';^^I,:,.         ,^ix]<l"<>>l!:;!I:I"`^,,"^^^^^^^^,<^^"".i;
                           I   .{1\+};!?!~~`         :^!1}{_`_]{i[<~(>+};'`'''''''''''^i'`''.i^
                           ;    ":I:                 ;,":>I^ '..'.''.''.`"""``````````"i""^`.!'
                           ;                         :,                               .:
                           ^                         ..                               'l
                           "                                                          'l
                           ^                                                          'l
                           "   "<;                                                    'l
                           I   ;1>                                                    `!
                           :  `i:^```````'```````'````````^^^`'``''``'''.  ```'''''`' ^I
                           "  '"`'`'I:'''^'!^'''''i`''.'"!^"^^`;I``^^`;">_< `<"`'''`' `l
                           :^  :l1" :` ~~; ;;[<i~""l]_})^:     ^"     :.i?~<'".i<~?-l ":
                            ",^^^""^^^^"^^^"^,,^"""^,"::^"`^`'^",'`'`^"^I>I_:^^,;:Il::,
                              ^!!>lI::!i>i!":li>lI,;l>iI!"lI<+l!^!!~<l!"!l<>!I"!i~<!I
                              ;l<~I`~~I~?<^I<,-_i;~i"_]I!ii"~{">:<;]{^+i>l+~'<l;l_}'_
                              .;;:II`.I;;;;.`I;;,:.^:::I: ":"":, ,:";;,.:,"":,.;,":;^
                                                '        '          .
                                               ^~-<"]l}<'[]-__i-><-;<+?,+-[?--"
                                                 .`   .   .... .  .   . ..^`.^
                     ^ .''''.'' '.'.''`.
                    ;}`;{-_-li<>+"?_][(;
                       .,`'.^.``''`'.`'.``..'....^. ....  .' .. .''        .  .  .       ..
                       `<<_;+~_!i<?<_?_>i_+,i_]!;]?:>-~_l![?-+__>!!<>_<-__?!;?-_<]~~;~+>-I~-_:~<<>!~-!
                       .   . ...                                    .  '.            .  .  .. ....  .
                   .-1`!{]-]i<-]~--+-?[l??[}1I
                    `^ ','.'^..''.`.'''.^'.''.. `.       .              .
                       ,+_-i?--><~_~[-~!]+i>~-<I_?!_~_[~?~;~[~+!i___<]_i_><~>~[<-_l_-]~?-?!><>~;_+_;<<i~+_-:
                                                   . .`     .   .. . ..  .'' '".'..'..'..' .... .''.''''.''.









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


                                                                                               ````.^ ^'..'.
                                                             ....''...   . ...                ^---?!?.+;;<}<
                                                             >{-~i<__?l-._-]{+l?_:+?i<}~:<]-]+-?i>~}><_?-}~'
           ^^^`'````^^`^^^`'`````^``'''''''''..''.'.'''......'`''..''''`.''`' ^''.''''''.''.^.``.'```.`^^^^.
          .::::",,,:"":,",^^"^,,:","`^";;;;;;,:;:,:,;;;:::;III;IIIII:::IIII;,:;::IIIII;:;;:I;I;;;::;IlIII;;^
                   '>! I-;-I~~I+^~i~_?,
                   `;;."I":"`",l.;:;II.
                       ;_<i:?~+:>!_!<+<l>~<:><il]!:><i<:i><><<<;~llI!Iii!i:;i!ll~I;"iIl;:!l,,l;;IIIl'
                         ^" ^"".`^,^,,^'.`"',^`.,^.":"I^Il;I;ll",,;I;:+!ll^:!II;!;:"i:!;"i>::!l!il>i`
                    l< !-!:~iI!~<I:-Ii~>><<;l~<>!iiiI
                    ;! :l",;"^`;;"'I:,ll;;!::il""I;!;
                       ;i;!,<li,II~;i>!^il"^lI;;>ll`:i<<!!l:iilI<!l:<llI`,"I:I;;I"^;!I;il;^I:;":;l,";:,,::I'
                       I~>!:~~<!_>~!~~+_i>il+<<i+<+li<+ii-<i-<_!?~il<<~;!?<-~1-__!i[~+_<il">:!:,!+l;>!i!I>>^
                       "l<,:<<ii+l!":l>+l>lllI<~i~!~_l;I:_~~~,<^_l;l,l! ;+><+~+~+<!i!~>.




































































```

*Figure from page 36 (2346x3317 px)*
