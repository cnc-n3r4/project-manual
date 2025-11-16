# III SECTION 3 DATA INPUT OUTPUT OPERATION 3. TAPE PUNCH INTERFACE OCR

*Converted from PDF: III-SECTION-3-DATA-INPUT-OUTPUT-OPERATION-3.-TAPE-PUNCH-INTERFACE-OCR.PDF*

---



4203-E P-327



SECTION 3 DATA INPUT/OUTPUT OPERATION


## 3. Tape Punch Interface

(1) An RS232C serial interface is provided to allow connection of a tape punch.



Connecting a peripheral device such as a tape reader or tape punch that also has an RS232C serial



interface to this RS232C interface enables bulk transfer of NC part program data.



When the RS232C interface is used for connecting a tape punch, it is necessary to set the



parameters so that communication is possible between the NC and the external device (tape



punch}.



(2) There are two methods for data transfer using RS232C - the normal BTR (behind tape reader)



method and a method using DC code control - and the method for connection to the peripheral



device differs according to which of these is used.



3-1 . Operation Commands



{1) The table given below indicates which command can be used with which input/output devices.



~ Tape Reading Tape Punching Printing De-



Sector Device



Device Device vice



F2 DIR Input Output



F1 READ Output Input



F2 PUNCH Input Output



F3 PIP



Output



F3 VERIFY Input



Input



F5 FREE Input Output



F6 LIST Input Output



[Supplement] For the operation of the commands, refer to Section 5 "PROGRAM OPERATION".



(2) Peripheral Device Classification and Abbreviations



Sector devices



MD1: _,. User memory



FOO: _,. 3.5-inch floppy disk



FD1: _.., 3.5-inch floppy disk



Tape reading devices



TR:



_,.



Tape reader



CN0:



_,.



Tape reader connected at RS232C channel 0



CN1:



Tape reader connected at RS232C channel 1



CN2: -+ Tape reader connected at RS232C channel 2



CN3:



_,.



Tape reader connected at RS232C channel 3



Tape punching devices



CN0: _,. Tape punch connected at RS232C channel



CN1: ..... Tape punch connected at RS232C channel 1



CN2: - Tape punch connected at RS232C channel 2



CN3: - Tape punch connected at RS232C channel 3


```text


                                                                                               .,""``^ ,`^""'
                                                                '`''``''... '.'...''' '.'. .'' !]-]-<-.<I-}<^
                                                                ~}~~i++__I~'-_+<<>]-~<<i+~i!+<<!^>__---~l<<?I
           '^'''````^^^^^^^^^`````^`^^^^`````````''``````''''''''''`'.'..'..'''''''..'.''''...`.'`..'.''''''.
           '`^""""""^^^^^^,^^`'''`',"^^^``'''`^";,,;;;;;;,",;;;;;;;;;;,,,",::;;;;;;;;::::::;II;II;::,:,,,:;I`
           ,)'     ")-~<_i"t~!~<<~-'_<?~~i]_<!>l
           ,[;     '~[|)1-:-!{??{~?:_-}{)_~(|?{-

                  :>l ._<;]-]_--+,<<>~!!~_>-~>i:i;>lli<<<l>^i_li;;llli!!!i;,<;I!<ll"lII!i.
                  ^^^  ,,'^^,":"^.::^;`^";",I,,',:;^"::;:`;.,:";`^:"";:,";`",^::<!;^;I"::.
                      'iIll!>iii<II!<!!<i:!lI>;!I:,;l!^iI:;>~l;"iii<I";"<l!^lI,;::>!l"<!::ii,l>:-__<~~i:i!l<;
                      '>~>>+<~I~++_+i-[--_-+l<~~~->~i!>~_<<<++i+!~++i<~I>]~_]>!<<l!<<!~+~:<->+l^:;I;I;:^I;"!"
                      ',:;"II;':^,";`,;!llI:',I!;>ii,:!;<!li"ll>`"!l:!>,^I.il^iii`:;l~!!!:;<<<
                      '><l!: ll"^+i!<!i; ;!!;lI:^ : ^::I.:I'.,:";;"l,, ,',l,:."`,:l' I :.^,^",::;:'"; :;:`!:'
                      '<<<+i:><!:l~<i-~~`i~-i<~~>,+li~i~::~;:~_>i<<_<?I>;I[?<"?+~>~l^>,~,I~+~_~~~<!;+'>~>,~~"
                      ^<~iii~<>l!.<;'!>_`!>!!!I!i>~-ii'l!;~i+++<i'+_~~++>.I<i`__":~i!^~>"l<~_i!?"I[<>~~ <?~-:
                      ^_<<<~i                                                                           . .
                      .`.   .
                  i}! .>i<!i,_<;>+>"!>_i!i~,~!`+~~lIi~i~?!`l<i~!__+~++~,.^>!";ilIi<:_>+!,>i>i!!;>!>";ii!i!"
                  `"' 'l!-+!iliIi!!"i~-i!>II>>;l<_i,ii~!l!I<<i<;"><~i_>";I<-lli<lI>l<l!l><~l>iii<i~li~_<<>!
                      `<>~>!!;]_ill,>~<i><,i+!+i>i!:i>_<:iil!!^',<ll"Ii"li<!!!,;i'l>ili>il!"Il,i!,>>!+Ii!i>
                      `+>l!<:<-_<~:~<!ii<<-~i!:+~>_:l<!_+~_:~:i--~"
                                           .
           !-"!.   !_]+-<??~+!I-~+_<_<-~~?~
           ^,.`.   ',>;:^;,",'.,":"","I"::;
                  ",'  ;""`,":" "`"^',""`^.:,:^::"'^:,",.^^""^^"^"'^"'"".'^^"'^:".^,^^`'^''^^'^^.`."```'`
                  ;l: .!l+;+<+~l[<_>I+~i<<:<><>-__;<+>~i:<<<~!-<<>l__:_-:~__+;+?<,-+++Il_-<_<>__<<:}~<<~?,
                      ;<!i>lI;:;,,"","~_~<<~<i<l!""^^^^":::::::!"''''""":,",,I!^^"^:,:::,::,:i""^^:",,:,";;:l
                      <" ''^",,"^^'.  :I!][_]~-,:.'     .      ;^+>l;:<III>II.;;!ll'i:;:l!I;"< I!l;!;:^il^ .-
                      _:        .^"",,^`'i+<!!i:II{_+?<:~]~~+_`i.;~_{~_]-_ll_';^!>~++<??_!l~;> ::ll?-1iI>, ']
                      ~~<>~>i++<>     '`"^^","^,< ..      . ..'<   'l!;;I;   'i   .!iI;!;   .i     IIi:    .?
                      +?_+l__[>l:^^^^^^",,,::II!~^^^"l;IlI,""":<^^^`''""""::,:_^^^`^^^"^",^^">`^`"!,,",I"^^,[
                      ~-~~"___,'''''..`'``^^^'.^i'`'^_--_!'^^`^!'`'``'.''^`''">'''`^^^^^^'''^i'``I[[}{?_'''^~
                      <:''^''.^~-<""[)_][l'^^``"!'`'^+~+]~?,^`^!````i][<+"^``"i'``^`^^^^^```"i``^^^^"""````"<
                      ~'      '_+<;:?+++<!I^``^;<,,,:~<i+>l^`^:>"""";i<I;```^:<""",;^"^^"^,"I_",""``'''`^"":~
                      +~>II>~^`?_];:+<??~+_^'``,i^^^"<_<<; ''`"i^^^^`. ..''`^:>^^^I]-]]]+^^^;_^^^`''''''`^`"<
                      _!;l^;l.`!^^^"`""'`^'```^:<^"^,~<<-i_"`^;+^"^^^''''``^";<"""^```^^""""I-",""^^^^^^""":+
                      _'      '!<+` <---?!i    'i    ;:;i;,   '!    ;__i<    .;             'i             '_
                      -;``'''."I.^``^^^^^'`'''',~'^^"+~<_!.''',~''``^,;:"''''">''''''''''''',<'`''..    '''"-
                      _]]_`<-[[{i'`^^^^^^``'''':~`"":->__i^```,<``^"^^`^`'''':+'^"""""^`````,i^,,l-~-~ii```:_
                      _+~~"!!_-~:``''````"""""":i``'^<li<l^""":i'`''''''^"""";~```````^""""";!''',>i~~<>""^:<
                      _-]]"+-{-I",,,,""^"""",,,I<",":-[?-l"""";<"""^^^^^^""""I<""^^^^^^""""";<"""l]_?__-^"^:~
                      .'''^"""",::",,"`^```^"""":",,^`^^``""""",,""^^"`^^`""",;,:""^^^^^:,,,;;::::,::::",::;"
                '-?>~~~+>_>+!   .>i;l~~"+~~i_-<!^~;i<IIi<i>!<i<<.!_-!"<"~~!~<i^<"l_-<<++<~-_:<~_~~<<ii<_:
                 `.'^^'` '...     '  .`.^`'.`''. .  '.''...'`''^ '`^^.,'^,"",,'"'.`^"",,",;,`,^",","`"":'.
                  >?^ ;<>!i>>i+;!~i>>i">><i>-ii<!>,lii;!_~i!lI>i!!i.
                  ,:' ''^`,`:^,''^^",:`",I::::;:,;^:;:"";;::;,I:;:l'
                      ;}<i>!.~~i~<+I
                      .```:l:::``^,` .'`''.'.''''.
                          l[_I:  `;. 'i+_>`i+<>~<i
                          Ii>~"  .". '!I!;!!;I>l!i::<<i
                          :l!i"  '". '!;I:l!:;ilii;,!il
                          ;i!:.  .,  .>lI;!<lI~~++!:~__
                      "ilI"`;;li:,^!:;:;I'     ....
                      '!_<l"!<<<l_">!i!li'
                          "<~.    ,   <>!i,ii<>i`
                          "liI`  '". .i~>!"ll!!l'''```'^``.^'^""""""'.^.'''`'`
                          ;><~I  ',. .<+<i"iii<>^liii><<+>,_;I~__+_~;!+>+i~_I~.
                          ;i<I^  ',. .>i>>"i!i<>^;lllil<ii:>,><>>~<>::illlli",
                          :!il"  '". .!i!!^lllii^;lIl!Ii!!,i,li>i><i,:!llIIi^;
                          :i>~;  ':. .+_~i^!i<<<"I!li<!<<i;+:><+<><>:I!<i!l!:i
                          ;<<~;  ',. '~~il"!i!<i";ll;il>ii:<I><<~<<>::!ll;!!,i
                      ^"'.";;!,''`".'':~il^;lIll`;I::l;IlI"i::Illl!I":;ll:ll"l
                      :-[-;!!lI~<i-l--!!i<I
                          I~~<:  .:' '~i!I,!;!ll"ll;;!l>!l,i;+~>i><!^lliI:!I;,
                          :iii"  .^  'ii!I:!;ll;"lI::iIi!;:i,>>>><il^lI<I:iII,
                          ;<<l`  ";  '<+>>"<;lil,!!>!<ii<I:>:_<~>~_>^il<!I>l^`
                          :i><,  '"  '<>iI:!l;lI"I;;IiIiil:i;~>ii<<!^IIlIIl;;"
                          :!!<"  '"  `>i>;:!l;lI"l;;Ii;iil:i,ii<><<l^Il!ll!;l,
                          l<_?;  `;. ^+?+>!>i~<!,>>>>_!<<<!+;___~-~i"<i<<!~liI
                             .         ^`.``'.' .'...`'''..' ..`''...'.`'.`.'.











```

*Figure from page 1 (2346x3317 px)*


---



4203-E P-328



SECTION 3 DATA INPUT/OUTPUT OPERATION



Printing devices



CN: -+ Console



PN: -,. NC operation panel



CNO: -+ Printer connected at RS232C channel 0


#### CN1: -+ Printer connected at RS232C channel 1

CN2: -+ Printer connected at RS232C channel 2



CN3: -+ Printer connected at RS232C channel 3



(3) If no device name is specified, the following selections are made automatically.


#### For sector devices MD1:

For tape reading devices TR: (This selection can be changed by setting NC



optional parameter {word) No. 57.)



For tape punching devices CNO: (This selection can be changed by setting NC



optional parameter (word) No. 45.}


#### For printing devices PN:

The default device for a tape reading device or tape punching device can be changed by changing



the parameter settings.



(4) If no output NC program name is specified, the same name as the input NC program name is



automatically assigned.



(5) If no input NC program name is specified, the name "A.MIN" wm be automatically assigned



unless a program name is designated on the tape, in which case that name will be used.


```text


                                                                                              .,,,"": ;`",:`
                                                               `^^'^^'^`.' `'``..''`.`'''.^``.l----<-'_I_-}I
                                                               <[_i!<~-?I+.___~~!_-<iii<+i>~+<i'i+<~+_<i>>?:
          .^^^^`'''`'```^^^^^^^^^^^^`'''``````````````''''`````''.'.....''''..'''''.`.'.... .'.'''.`'''.''..
          ':::,"""""^"^^""""",^"""^^,,,",,::::::::::::,,,":;;;;;:,,,,","""""":;;;;;;;;;:,,:,,,:;;;;;;;;;;::`
                      <ii><lI:_!!!i<.
                     .^^::II!"l::;;l...
                          !~<.   `"  I><<~>+!
                         .i<l.   ^"  Ii!"l;I:;l,,':,";^
                         .Ii!.   ""  !~l^><>:~<>;,~!I+"
                         .!>+~^  ^"  Il>~?>^!iiIi>~>!"+;___+__<"i<+i!>>!!
                         .l>!I'  ^^  ;Ill>I^Ill:lIi!l,i"i>iiii!^;;iI:lI,"
                         .!<i;.  ""  !l!i~l^!iiI>!><>:+,<~~>~~i"Il~!;<i^"
                         '!><~'  ^"  Iillil^l!i!>!~>!:~;~~~<<<!^l!<!Ii;;I
                         .l>ii'  ^^  ;lIIi;`Illl!I!!I,>,<>>i>>l^lI!I;l:;;
                         .l>i>'  ""  I!!l~!`!l!i+!i>!;~"<~~<+~l`>!~il<lIl
                 ^i, .l^:^`:^^",'"",:'`''`^^^I^" ,"'`":"``'' '^,`""'`..``.^^^"'''^^^^^"`^:'
                 I?! .!`!I,~>I!<'l<;<;l!l-~<!_+~"i~<:>+!<i:?l~~+~_+iii!~~:i+-_!l+><>>-+<]]_'
                     'i:"^i;;l:`~l;IIl                 >>;I.
                     '!;::>lll;">illli^....           '~+l:'  .^'.    . ..       .                        .
                     `~!l;-++"i_<+l_i>[+<+-~           l_>    I~<-< <?]~~?+! !-]^"]< i<_+~}->.+-.;-_{<?::1-:
                                                              !_+~~+-;<_i-~<?]>:?<>>};?_^!{l;. '      ^'
                     `>:;,!II";,;;iI;:^i;;;;l'        'l!!!.  "<l;;.IIiI;!::':::"^l:`":;:",,: ,^ `,;;,^ ^l;`
                     ':lI"~+i;>lll!!i_:<!!i><^        'l!>>'  !i+-~^----+-_<"~_<;:-+,<_?<+(]i.i_.:+~~<]""-~"
                                                              ;++~I>~"i~i+l~+_I`_>ll-"~>`"-l;.
                     ^~!!;+i<+i<;?~>>~~`              `--<
                     .I;;,!I!;:~,i;;;;I:'`^"^"^`"",:"`^I:I^"'^^,""^^^^^"""`',"`^^''^^`"^."^^`'`^^^.'"'`''`'.
                     '?i-l-[?[++_}>+?]>-l<l~__i:__~<~_!]>i>~:<:+?_i~~>i><>-i+_><+!!?+I_+;<+->]-~i-<l~<+~]<?l
                     ^>i:!<iiiI>~!.++_~>]!
                 ^I^ .:'^..`"^`^^;:.`'`"^^"'""""`^``^^^,;^,.":^'^^^^'`^^^^.^`",`'^`'``,,''^'''`^.'''`'''
                 !-I `~;~;l<_?~>l?iI+!+[<-!">_i_II!I-~~~-+_,i_~;-?i_ll-~>_:?i<?+;~-~<;]+:-+>]<?_:i__~_;_'
                     '+>_<>~?i~~+">-~+]<_~.
                      '.      ..''. ..'  .
                 i1! `<:~:l+>~Ii?I,<!+~><l"~_i>:i:>~~i~+<<.>~!"!~!~";<;-~_:,<>;~l,>i>i!<]i<-i^~<<<>><>
                 '`' .l>_><lilil><<_>!++<<Ii>;-><>>_]_>;~!i-<I<~+I;>^<~<<i^!~>I~+i~l<>i+I<+!+i!>~__l,^
                     .;:I;l^:,l,l<;!:.,!,l:","!II<:I!!;^I^:ll`i<!;'l'!lIl,^!!i;:I!;^!l;!'!;`;>^I!!!"














































```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-329



SECTION 3 DATA INPUT/OUTPUT OPERATION



3-2. Parameter Settings



Set the following parameters before connecting a peripheral device.



After setting the parameters, press function key (F7J (BACKUP) and on completion of the backup



operation switch the power off and then back on again.



The old parameter settings will remain valid if the power is not switched off and back on.



(1} NC optional parameter (bit) No.1



I\ Bit No.



Paramete \



r No,



bit 7 bit 6 bit 5 bit 4 bit3 bit 2 bit 1 bttO



Special Special Tape Tape Tape Tape TV Automatic Tape



tape tape rewind read delimiter check tape code coding



codes code verify code: recognition system



ignored alarm % (ER)



(a) bit 0 Tape coding system



= 1 Tape code set to ISO code (lnitla! value;;;:: 1)



= 0 Tape code set to EIA code



(b) bit 1 Automatic tape code recognition



= 1 Tape code automatically recognized (Initial value= 1)



;;;:: O Tape code not automatically recognized



The codes used for tape punching and tape verification depend on the combination of the settings



made for bit O and bit 1.



bit 1 bit 0 Contents



1 1 In "READ" and "VERIFY" operations, EIA and ISO tape codes are auto-



matically recognized.



In "PUNCH" operations, program data is punched in the ISO code.



1 0 In "VERIFY" operations, EIA and ISO codes are automatically recog-



nized.



In "PUNCH" operations, program data is punched in the EIA code.



1 In "VERIFY" operations, the control assumes that the coding system is



ISO.



(If the tape code is not ISO, an error occurs.)



In "PUNCH" operations, program data is punched in the ISO code.



0 0 In "VERIFY" operations, the control assumes that the coding system is



EIA.



(If the tape code is not EIA, an error occurs.)



In "PUNCH" operations, program data is punched in the EIA code.


```text


                                                                                               ':,,^^" :'",:.
                                                                `^`'^`'`'.. '.``..'``.^.'..`''.i[?]___'~I?]}"
                                                                ~[+i><>_+!>^-__~<![?<~~>~~ii+<i>^~_<~_?~><>+,
           .^^^^^^^""""^^``^^^^^^^^^^````````````````''''`````'''''`..'..''''''''''. '.''''...'..'..'.''.'''.
           .'^`"::,""^"^^`'''`,"""^""``^,::::::::::::,"",;;;;;::::;;;:,,,",;;;;;;;;,,,,:;;;;;;;:::::::;;IIII'
           :_"_   .]>+!<!!>_<l'_>>->ll>,
           ^l"l'   ""!,i:,ll!: I!!!I,-~"
                 i<!I>l"!!I:;;!"^I::l:Il!l,Il>Il,":;;lIIl;:,,,II;!l;;!^!I:;I`
                 "l;^!l^:;;:!,liIi;Il:!ll;"IiI;I"";:,!l;;!<::l>;lliI;!`il;I>"
                 l~>i ^>>~:! >l: :l;IIl!!!l `;:;I';lI:l,:.^lI.'!;i i<!!li,!!'^>I!';I.:IIIIlilI"'!^i!;'II;I"l`
                 !~~~;~+~i!}i~_il?~!_>+_<!-!l~>>+Il<i<>>i"!>_;l>I!'!!IIIII;:^"<;l'lI';lI!!!i!!"`!.l!!'l>!lI-^
                 I<lli!:;.;!i!!^;>;,>li>,`i:l!!^;I<:"><>::<'i-_!;
                 III`^;;"I;:::;I:.,;ll":,`:!^,,:,;`'";:^:":,',^",:':^::,":,;:;,:^:!`,^,,"":^`,'
                 ,:i:;!:liii!;i!!`!>iil?!"><^!>li+,,i+<;l:i>:<!<~<`>:!<ll<i<<<<<:~<I+l>!+~~II~:
                  '^'  ;:'.`"^`'```````'^^. "^.`" .'
                  ;l: '+<,I?~<<i<l~_<+!<~_;:~+I;_I^"
           ",","""^`^"^.'`^^```^^^^`^`''''^"^`"^`^"^^^^^^""""""""""^`````^^^^^^^^^`'``^^^^^^^^``'''``^^`^```.
           1>,^?|~[}!l>^^''"^,,,~:,"^^``"";<,:"^"",:">I"""",":::-::"````",Ii,:"^""""">l:::,,:::,,+l;;::::;;I_
           _I!Ii~i>+I!;  ,;`,   >.  I:,,  .:  ';",   l^  ",'"   >  .,^"`  ^;  ':`^   ".   ^`..   >`  ^^'`   ]
           ~i_]+!l<_,_I  ;i",   <. .<iII  'l  ,~I!'  !"  !>,l   <  ^~ll:  ,l  :-;i'  l^  '~i""   >^ .+~;i  '?
           +;!_i''..'++.'    '''>^'.    ''"~''    '``i,.'    ..'+'.     ..;! .     '.>^        ..<"        .]
           +`'''"""""i_<lll!i^^`-_[??__?!I+~^:>l!l",,~<;;~<i>!l<_,>lIl^```l~!;II;>l:^++>!><__?+<i[~l<i!!IIl~}
           <         ^![[-ii~   ~:-]?+l+` i! ^?[]+`. !I  >}[?' :i +{[]"^` ^;_)]_:I!  i-+-?+<_?_:'}: <??_'  l?
           -    l.   "l+]-;.    ~:+_]i    ii "<i<i<^ iI .<-]-. :> ~?-+~~+.`I<~_<>    !~-}-ll~_{;^{,'<~]_[> I+
           ?         "!>+-]_".  <">~--'   i!         ;"  I~l_I ,i +i~{:.  ^"         !><?<~->]>i>{,.-~-]-< :~
           [......'''i~[-~<-],'.-i{{}+>^"^_<.''.''''.+!`^''''``l~.+;~{+]`.": ....  . >~.'''^'.'.;)I.''.....i_
           ;,,,,,::;;!I""::^",",!<<>>lIl!iil"""":::::i<>>>!!!!i<>I;II;:;I;;I::;IIIIII>~>iii<~__~<_+<<<<<>i!<l
                      .>> `<Il:      iil;',:iil,:IliII^
                      '!! 'l,:^      ^>iI^:;l:lI,i;l;:^
                                     ^  "   '!,"^'"^;^^;:,:'!!I`"":; ";,;,"^,:^".'`:
                                     ;. " '..!~il:!l>lI+l:>^!>l"ll!~.lil<_;I+~<>":^<.
                                     ' '"   `;'''.`'"..'''.',`^ '.^.
                                    .l ^< ' .+_<>:~<]!l-iI~;~<<,~<-~
                      ."` '^''.      ^.` ''`` .      .        ..
                      "]~ ;?!,`     '?+?~~<[?Ii[-+:~~-~;-~<?[+]~<"
                                            .'             .
                                    .i '! `."]}]~l+~1>>-~_<<]-<_?~;?+~-_<-__; _<~+]ll??-!,^!!
                                                         .  .    .   .'. .      ..' .`'`'. .'
                                    .: ,< ` ,[-_i;<<-!I<~;-~+<<_-<+}_">~><+i<<~!
                       ."'....'..  ..`'.`..  '"^``^^`'.^``^`^`'"","^:.^"^";'^^"'
                       `<i_,<<+_~I_~-ii<,+-_ii>><<><]l->+>_<-I~->-i_?~~:]]~?>_l>>!~+I<i~[+i_}+-;>i_+<i-?[~?_.
                       'i<~+li~:i<l>;><!i-;l.       '.     .       .    ..'. . .   . .. .. '... . ..'.'''.,`
                      .^:;::,,I":;,"`:,":I^"^`````''...'''''''''''.....        .'..................
                      -;"<]~il,:>:,>_i~l"">:::,::,"^"""",:::::::,,,,,,,~++?]+_-l;:,,,,:;;I;;;;;;;:,,,,,,,:;ii
                      [:`;~iI:""<"`I<l!:``!^`,;::,:,^```""^,:::,:,^''``iii<-_~?;^`'`````'..'````''...'....'l_
                      ]^.  l....l..  l  ..i_>"]{_+]~`?~+"!-[-}?><,+_?<?-~<+"<_]>_?-i_{]!+}??I-_1]~!?_I_~?<^;<
                      ?`        ;         ><<_+!_]i"<<i_~>+~<I    .''.'.'.'. .. '''..'' .^``.'''`''`'.`^`' "!
                      +.        ;         i"^;l,;;;^::^;:^,,:`                                             "!
                      ~^'.. ....>.... ''''i~>^_!>_~>~,;__~>-~~~i"_i<]+]~,_[]ii<!<~+~+_~;<!_~;i?+li<+{;  .. I<
                      ?:"^"i^^^^-^^^:_:,,:+~l;i<_--<+>!--+<_~<<>;]<->+~~i]-~I!i~<>;+~i~<+<>><<!<<li~~<>l::">~
                      ]    ^    i   'I    I>i">~ll!`:.^>i!l~i!!i'!l!^<;i"iiI^l!>>i"+>,i<i!ii_>!~<!;>!!_:   I~
                      ]'        !         l:<~ii                                                           l~
                      ].        I         Il^`i:!<!;!,^!IlI<l;;,.;:,;Il;`!ll:,,^:,,II:I::^i:^iI!`""II.     I~
                      [,^^",",::+::::;"^^"~<!I<<--__+Il?~~<?~>>~!]<_{~-i;_-_~i~~-~<-~~~i>:_~l<<_l<<-[:^`''`i~
                      ?'..,?'..'i...^<...'+~l,<?+-_<<;:-_+<-_<-~"]]!!+>-_<;~<+~-+?~i_++!-_"<~+~+i<_+___l~!'!~
                      <         l         !>~i;        ' . .   .   .  .    '  .  '..'^`.'`.```'""'"^^`..'' ;i
                      <         l        .I+]_-I,<i!::II>"I,;lI:~il.!I`l;;;^I;;:l""                        ;l
                      <         <         I;":II^!<l,;;;l^,",I:^l;:.l;.l:;"'llI;;:,                        Ii
                      ~.       .< .      .!>;"+:~_li<^,!l>i-iliI'iI<<!~I^!~~;II:IIl>i>i:l:+~:>_~;Ii!<"     !>
                      ]^^^:i,,:;+:;:l<"^^"<ilI>?-]]]~ll~<>>+<i<<i[<+-<+<!><~<>>-_+~-+~<i<l!<l>~~!<++?>I:;,"~>
                      ]   `>    ;   ^i    l<l,i-ii_Il^;+_>i+>><!^+<;:<!~ii,+<~ii>_!!~_ii~~"!!+<_<!_~-_+;_l !>
                      -        .I        .!-i-"                                                            !>
                      ~        .I        '<_+i__I]?_l!<<]:>I>+<!~-!^]lI-i>I;~~><~I:                        !i
                      <         ;         <".`:"`:;,^^''^.'```'..'`.^''".".'^^^^``'          '             ;I
                      _"""""""^"i^^^^^^"",~-~!{~?]-+]I~{]]]}_-]<:]+[[-{_l[{{~+~_~_~__[-<?!][>}]{!_-?{"'''``il
                      ^,,,,,,,"""^^^^",:,::,,,^"^^"""::;:::::::,:,":;,::::;;;:;;,,""";;:;;:;;:;;:::,:,"::;;l'
















```

*Figure from page 3 (2346x3317 px)*


---



4203-E P-330



SECTION 3 DATA INPUT/OUTPUT OPERATION



(c) bit 2 Tape TV check



The tape TV check is a check on the number of characters of tape data in each block of the



program.



It is checked that the number of codes from the code following one LF (EOB) to the next LF (EOB)



is an even number.



bit2 Contents



0 In "READ" operations, no TV check is performed.



In "PUNCH" operations, the number of characters per block is not adjusted.



1 In "READ" operations, it is checked if the number of characters in each



block is an even number; if it is an odd number, an alarm occurs.



In "PUNCH" operations, a space is added if necessary to make the number



of characters in one block an even number.



(Initial value = 0)



(d) bit 3 Tape delimiter code %/ER



Sets whether or not the %/ER code is used instead of tape feed to mark the end of program



information on the tape.



bit3



[Supplement}



(e) bit 4



Contents



Tape feed is taken to indicate the end of program data.



The % (ER) code is taken to indicate the end of program data.



(Initial value "' 0)



The data up until the second appearance of an CR, and LF or EOB on the tape is



ignored.



Tape reading verification



Sets whether or not the program information is automatically verified when a tape is read.



bit4



[Supplement]



(f) bit 5



Contents



Verification is not performed on completion of a "READ" operation.



Verification is performed on completion of a "READ" operation.



(Initial value = O)



File names are not verified.



Tape rewind



Sets whether or not the tape is rewound after reading (if verification is not performed).



bit5 Contents



0 Operation stops after the tape has been read.



1 The tape is rewound after it has been read.



(Initial value= O}



(g) bit 6 Special code alarm



Sets whether or not special codes ($20 to $5F, HT) trigger an alarm.


```text


                                                                                              ."^"^`, "'`^^'
                                                               .''.''.'. . '.''  ..' '..  ''. ;?-?]>_.>;+??:
                                                               >)->i~~-]l~'+_-~+l_?+<<i-_><~+>l`~+~}?-_>++[;
          .````''''''''`'````````''''''''````````''........''''''.'..'..''.....''''.`.''''...`..`'.^'''.'`'.
          `::::,,,,,,"^`",,,:,;;;:,,"```":,::,,,,:;,,,,,"",:;;;;::::::::,::,,::;IIII;I;,,,::;;IIIII;I;:,,,:'
                      !l. ll:l      l<ll^li,,ilI!^
                     .lI. ;"^,      'Il;^',`":;::'
                       I><`;<I>`i<,:<ll<`;,:,,>!!_,:~^><i`!i><>>^:>^>><!ii<l!'!!I<i>'i~<I"l'!!!>`iiIi,">,>!,
                       I!<!i_~i.'^'^"::;'""^"",:;I`^;'":;.:I::;I'",';:!:I;I::':^,i!l';ilI^;'lll;'IIIl""I`;l,
                       !I;-;I:"
                       l,:.!;;llllIllI>>:";:llll^iI:;i!;;I;;"il,,;I!,!lI;II:,":;,;!`i!I<i":^I:""::I^;";i:li`
                       <l<l>~<~<<>I>->~<I"!lIi>l"!:ll>>l:l!I:!<IIii~;iili<i<+I!>Iil`~!l_+;>;!ilI~<il!^~~l<_:
                       <;>i'!I>I'i<!i<~.
                         ';:::::;:,^^,^,:;I;;;;;;;;;,::;;;;;;;I;;;;;;;"""",,:::::::::,""""::::::::::::,,""""
                         >+`^;[+++^^`+`'`'.''''`'''''.'``^^`^''``'``>]--{-_{l`````^^^^```^^"^^^^^^^^^^^^`^^?`
                         !>^^^,>;::::-~il+_i><i:;;!ii~!!i",I,i>I:iIIii~ii~<_lIIIl:^,:::::::,"^^^^^^^^",,,,,_'
                         l;    i'    iI:.;~il<; li<li~!I>"`<^"l;"i!i!^i;I<>l!I!>i,                         <'
                         l;          iI:`iI;<i;>,'II;:!l,I: ~l"`;:;lII.l,,:I;;:l:I"Il"I>Ill^l':l,:!!,llI:  ?'
                         l<,,"":"""""i~~l--??]-_lI]-++-_++]!?-+<--~+_~l_i<<]+?--__!--li_~~_!-l+?>_?]~+__i^`}.
                         lI    i'    ;!l^~}>~_!.>_<!+~!>_^!!_:~+<>+~<l<I_+,l!!><~^I~^~<~><<?i!:!;__~>    ..].
                         l;          ;+?!>i;!:?,i_~-Il>~~?+!"~i!<!i?;>?-I~i>_+-I,-il[_i_;><>!~i..'''       ]'
                         >l          ;"""I,`;,;^,^^"``,"`"^'''''^`^"'^,,^`,",""`.,``,"`^'^"^"^"'           ]'
                         >I          :!!`<ll?_i~,"_~_>_>i>i.~,+>_<>"~;?<?~<:!I_><+_+_~;-I!~-_+I--I!_~+_?!  ?.
                         <>''''''''''~~[!]_}~?}]~<>~;-_<i[-??I}i~-+-il+-+]--`''''''''`'''.'`'.     .   .   _.
                         ^!;:::::::;Ii!ll!!i!i!!;;:;;l!!l!!!!liIllII;:Ii!i>ilIIII;:,,,:;IIII!-+]__i>~i<lli->
                                                                                            `<l~<<^i<!~":"~^
                     `~-."_iii      _->~:~-~i>?+"li<_,~l[~-.
                     .,:  "`'^      ';:"',;^`",:.",": ',"``
                       ~~-!._><_<_;^< l>I,!~">!_??^!!~-`<:,<~~!l<~-~+~"_:~_~i:-<+!ii"~~<_^~>;;<>!^+;<ii+<<<"
                      'i-~<i~_~iIli"<!!!~i<;..```..^^^".^'`^^^''`^^",^'" ":,^ ^""'`^.^:"^.`"^`""^'"';",!,:"'
                      .::;IIl>;;^"l^,II^><!^
                         I!,,;>lil",:i:;:::;IIIII:::::;II;IIIIII;I;:i>!i<>~~lIIII;;II;:::,;IIIIIIIIII;:::::!
                       . _>""I?l<l```~`'''^`''``'.    '..'''''..''''l~_<[+<[;''''``'..'`'````^^^^^^^^`'''''-
                         +i^^''_`.`'^+<}[[!][-_i_i[[+-I_li+]_+}->[_l~>~lii<+~]___!<?[_^'`''''^^^^^^^^^```'`+
                         +!'``^>^```^->-?<<ii-~<l;<i<lI!<<<~>~+<ii<Iiiii<;~~<}i+il!!ii:"`,,:""""""^^`'`'`'`-
                         >!,,,,+:,,,:+>~[i+-!)]1<-[]1>]~[)]?<>]i[[}]1(~}{]i-_-!-~1_[{-)_i(|)?''..'^```'^^^^}
                         ."""""`"""""^``'`'^,"^^,"""^"""^```^^","""""",""""^^^"^,,"::,"","""![_{]?i]]_[i<~)I
                                                                                             "^",, ^"^" .'"
                 ,}+i_+?~<+i-;   `+i>'~~+;:-,;>+>I<i,~<ii>~;<~>~<i<<i~I;+,~:;~?:^+!<;>~`<"+<<?";I^~l,I<!i`!^
                 `:^,;","^,^"`   ^>i~l~_l^^l'^""^'^,'::,,",':l:::":,";^^,'I``"""'l,:`;''I'"",I`::`::""!!I'l`
                                 ^-!::;;'
                     ';:.^l::"      I,^^',,,I:"'^:,I,,;""`
                     ^~i '~;,,      I-_>^l>~~!+:;~l>i!~!!,
                       ili^^i;l!:l^:^':;:!:',,,;:,;`,!:,:,!I:,":^;II:;I!::l:':;;!,;";l,:^""I,;","^;:;'
                      'i!!I:<;!;:i^I:^ii;ii:<l!-!<i:I<!l!!<!l::!,<>>Il~<l!!<^!>li!i"<iii,!:+<<Ill:<~<^
                         ;:^`;!;!;;,;<,::,,:"""^^^";;::;::::;;,",^""lll!il!iI:::""""^^""::;,:,::::,,,;;;:,:l
                       . -I``![!<I`^,+``'``'...''.'..`''````...'.''.i~+-[?_},'`.'. ...''...'''''^^^^^`''''"}
                         +;``'^+''`^,i_]-[-~]+<!!<I~-l-?__~<_~~l~I!<><~<+<<il-!>:]{~?]i,>i~<_?~~:^^^^`''''"]
                         <:```"i"""",>>~><i!~>!;Il;><<~~!i!;!>lIi;l>i_-~~>_iI<>-:i_>!<:"~__>~<>!"`''``````"[
                         >;"""">"""":<_1-]]?1?]>___}][]?]{[i+-!---[[}{--!-_-ii11_[-Il{}]-1+-<''.''`''''```^}
                         ',,,,,",,,,,,"""`^^^^^",,:,,",,,,"""""""";:::::::::,^^""""":;;:::::l~>+i!;l>Il:;l~;
                                                                                            ,~!+<!"<-!<^::-'
                 ^<I,;::::;:i"   ,!l"":::::`::"`,;^"::l::'
                 ,+<~+lii!~l_:   ,I<;"ii!>>"<<I^!<,i_!~~~^
                      :   `.`'      :`.. '.'..'
                     "-" "+;i"      >-_~"<~~l~!
                      .l;l'`:::!::',''"^";"':"""^"^,,,^",:`:l"`^,"::"^`I`^,,I`,:^"'"'^"^`^":^^""^"
                      `~~~II~li<!>`i;"il:i<:~?<l:!:<<>l<!>;<<<^:<<~>i_;<^i<l~!_~ii^<"!<;l~<>ili_i>
                         :;,";l;I""^";^",::;::::;:;,"",""",",:;;::::ll;::,:,",",:,:,:,,::,"^^^^^^^",,::;;;I:
                         -;^^~1![;``,i'...'.''``'''''...'...'.''`''`--~][-?]^.^^^^^^^^^^^^`````````````^^^;]
                         ~:""^;+''``"><<<<>->+!i-~~>;+-<;~+il~>~!+~+l+>ii"!<>i`''`^^^^^^^^''''''''''''''`"I?
                         <"'''">^^"":~~-+~>~!>;I<<<il++-l<?~!-_~:!++:><~~:~??+"```''''''''`^^"^""^^^`''''',-
                         +:^^^">^^^^:<~-[l-{]+<_l]]]?+]]>{[[!~!-{+l-[]<I-{[<.'````^^^^^^^`^^`'``````'`'``':]
                         ,;:;::;:,,,:;,:;:Ii!llll!!!llll;;:;:;Il!ll!l!lIIII:,,",;;;;;;;;;;;;;I;;::::I;lII!>I
                                                                                            I+>~+l;+?>_";l?.
                     :-< I-l+"     "?<_<<-;>>_~,]-+<l
                     'l: .".`       ^,""^^.^^^".:,"''
                      `?_-;!+<?]+~^~,I<i:_~<i_i:!!_-;>1?]l_:]-[:i+-I<-+_?!:]I!~~i<"
                      .'`'''''^'`` ^.'`'',^^`"`'``^"`^,^^.^'^^'.''''`";I:'':'^",`^'













```

*Figure from page 4 (2346x3317 px)*


---



4203-E P-331



SECTION 3 DATA INPUT/OUTPUT OPERATION



{h) bit 7 Special code store



Sets whether or not special codes are .stored.



bit? bit6 Contents



1 An alarm occurs when a special code is read.



1 0 Special codes are read but not stored.



0 0 Special codes are read normally.



(Initial values: bit 6 = 1, bit 7 = 0)



(2) NC optional parameters (bit) No. 8, 13, 14, 21, 22



NC optional



parameter



(bit) No.



No. 8



No. 13



No. 14



No. 21



Used to set the RS232C data handled by the channels used.



Channel bit 7 bit 6 bit 5 bit4 bit 3 bit2 bit 1 bit 0



CNO: File



DC Standard 8-bit Even/ Parity Ready 1-bit/



CN1:



name code DC code JIS/ odd check signal 2-bit



read/no control control 7-bit parity performed/ setting stop bit



CN2: tread TYPE2 JIS not



CN3:



performed



0 0 0 0 0 0 1 0



Initial



value



Explanation of settings for parameter (bit) Nos. 8, 13, 14, 21, 22



(a) bit O RS232C stop bit check



(b) bit 1



(c) bit 2



(d) bit 3



{e) bit 4



= 0 2 stop bits



= 1 stop bit



Determines whether or not the RS232C interface uses the "EXT-INT' signal as



the ready signal.



The "EXT-INT' signal is used as the ready signal.



= 1 The "EXT-INT' signal is not used as the ready signal.



RS232C parity check (determines whether or not a parity bit is appended to



8-bit data)



= 0 Parity check not performed



= 1 Parity check performed



RS232C even/odd parity



= 0 Odd parity



1 Even parity



RS232C 8-bit/7-bit JIS



= 0 7-bit JIS



= 8-bit JIS


```text


                                                                                               '^``'"'.".`''
                                                                ..... .       .    '    .  ..  +?_-i?I"+I[+!
                                                               `[}~>i>+}!<:I?-~-l_]-<~~~+~i~-<<II+<]~--<~+~_.
           `````'''''''''''''`''''''.'''''''''''.'.''...........'`''.''''`''`''...' ''.''`'. '' '`.``'`'.`'`
           :;;;;::,,,,"`^"^`,:;;;;::"`^`",,:,,,,,^"^":IIII:::::II;IIIIIII;II;I;,,,,:,;IIIIIII:,:::I;;;;;::,,
                      "<; :~:;'     `~l!;ll^II>l^iIlI.
                      ,I, `!^'       !!l:I;';;ll^!IIl.
                       ^_<~^I->_[><^i`,lI"ii!Ii,,I;!!,;!i"~i!l>:
                       ':::,:l:I;:;`l^,l;,iIl:i:,I;!!:;ll"!l;I!".......
                          i,,"<~!i,"^l!::I~~<+^""!;::;;::;""",,:;;;;;;;;;;I<ii>>>~<I;;;II;:,:;I;;IIIII;::::l;
                          -"^`>_Il^``;!"":?~i~``'>:```''..''.''''`'`''`.' '<~~+[~??^`'`   .''^^^^^^`'''''''l_
                          +^``.,<.''':l^^^.;" ''';!]>l?--_l!~+_-_l]?+_I~l++~i~~,<<]~i+!-+-i'`^^^^^^`'''''''l_
                          +""""I>"^^`:I'`^,<l:,,,!i~l!<+_>i>+>il!I!l>i!~i+~~<+>!ii>i:!I><<l"^```^"",,,,,,,`I+
                          ?''''"l^^^^li^`''<;''``Ii?~->_?;~~??~l-_i>?__i~<;l+<!1+_[_`.'...'`````''``````^^`l+
                          {''`'l_^^^^!<^`''~;''^^l<]~<i>+l+~??~l-_!i_+<l>><<+?-:^^^'`````^^^""^^`'`'```""""i_
                          <;;I;!<;,,"I!;;;;~i;I;:l!+_-__?<___+<!_~!i-?+>+_+~-__,^`",:,",,,,"``",:;:;:,::""^;i
                                                                              '>!~>>,!~iii,'<il<"^l`I<:!",!>
                                                                              ^l:!il^li!!!" !l:I`',`:i^^^,Ii
                 '~+' <~>,!i_i!iI;>ii>!i<!!^<<<,<>",<.l+`"i;^>:.><`
                 ';;. ^,^.;I:;":^:;;I;,;;:,^;;:.:I''I `;' :"',^ :;
                      ;>~~l:i^<+li!:!__~<~+l:<~~"I<i!?>!!<,i>!"~lil!!<::i<>I
                      '^""`.^.""''^`.^"""""'',::'`:"",:"`;"^":',";"",,^^:;;^
          .:",,^````'`^`^"",","""""^^```^^"""^^^^`'`````^`^^^^^''.'''```'''`^^"^^^`^^^^""""^^```^^^^^'
          ;]]_!~-[~<_~i"```^^`"+""``^"^+;,^^"",ll^"'`^^,,<l,^^"`^;i^^^"",:?:,,^^^^":!i:,":,::<""^"",:]"
          il<+>_-~__-`;l_~~>>~"I ,_!;" l..~iIi `" .~!;i  l^ !<"! ', l+,!. >  '>l:;  ": ;i^:  l "i;I, _:
          il"][]!_}i^ <^^^,^^,'l ."^.  I. "^`^ ^"  ,"`"  l` ,,'^ ', "I`"  !  .;""^  ;l ";'`  l `;",^ _:
          i+">-_!l_;`^-^":::,",+ll:,,,^>l;:""",<~I:`^"^,,>i;,::,,Ii:^'^^,:_l::,^^`^^i<:"^""",+"`.''`^],
          ii`.!?<"-'``_^!_??I^`il_[,.. ;+-~"...;<[[?>[[-~,++-[:..`!?<--<'.<+-_]['.'.;_???]{I'_;!??I..~^
          !!`:+_;;~<"^<"l~~!^``>!_>__  I!<>?l  "i<<:i<+{""l~]i   'I<i-`   !i+~i}.   "!<-__?  >ii+~   ~^
          !i";~>""iI''!'l_-<I::~!]~~<~l!<~+]__"^i<<+_~>. ;il~],  "<+??]l  ~~_??+<~+~ll?{{_-l l_-_i!?,+"
          l!`;-~::~>^^>^l__[l^^+li]?-".ii<+-)i+l:''....  il+[:.  ,i``'^`  _>+i . .''::^``'",.I^^"^'"._"
          <i':?_;i_I""<"!++-;`^I  '''  !.   . .,"        !"'.    ";       +<]_<!!!i!,"       ;       _`
          i<;l_-li~l:,i"l<+?iII_,,"^":,<,^^'`^^ii:::^`^"^+:`^^",,!i,,`'^^^?!!l!II!>IIl^^`'^",<","`^^^]l::,,;.
           .'.  .. .''.'.   ''^-..'i'..l'..l"..II.''!".'.>"..l:'',;'',!..'>  ..l^.. ll.'",.'^i```l`''l<_{}[~I
                               ~..'!.. l'..l"..!l   l" . i^  I,  ^,  "l   !    i'   ll  ^,  '<   i.  :I~]++i!
                               lII;,:;;llll;Ill>!;;;,;lll>lll;I;:;I::;:III>IIII",::l>>llI;ll!<:::":Il>i~~<<~"

                      +i<<<l>~!<,I>I<<_l!>:<!,!<!>l!>>;:><Il~l!.~"^<l.;!.!!.:~;
                      ,"l;;^:;:I^:",l:;">I';,`;;:I`;:;``Il:,lIl'!,'l;.,l'l:`:>:
                      l_, i~;>      !-_+>~+:,?i<"~~"<i>>l
                      ":` ^^'^      '`",""^'`,"; ,"`"",,^
                                    :" <^ ' _"_>];>+-.
                                       .    .  .` . '
                                    ,^ I' ` l,+i<:>_^
                                    `' .  . .."^:'`"
                      +]I +?:;      i<+_~lil<~"!<!_[+<^_;I~>i-~I__-]][_;~<_~-++iI-__I_+!"[~+il[~i`<~+>_:-<
                      .'. ..        <+iI<>~~;!+>i_!'`' `..`'''`..'`^^^`.``^''"^``"""``^^ ^`'.'^`  ^:;^,.:"
                                    ",;':IIl"";l,l`
                                    "' <'   ~<<^I<<+I~_-I,<<~+>l>,<~~!l-;~<!:<i>_,<<~i-"
                                    .. `. . .'^. `'. ''' .`:""`'`'"""'',.``^.^^,:.":;^:
                                    ^` ;. ' il>^!<i~I><i;^ilIl;:l"I!";lI!"!:l>l^;lI!^,lII!;
                                    `. '    '';..:"^ ",^ .;i:;"^;.;:`:;I:`!",I;`;ll!:">~"!,
                      ><" ~+l~      I-+<~~~;;<>-+^<~+i!`<~>>l!i!!~^i<i<>>l'i`;!l;,;il~,"<"l:i+<i>!+>>l>'
                      ^". ^^'^      ii~+I+~i+;,";',":,"`,:::"",":;`:":;,;"`:'";":,;I,I;^;^:^:i!;;,II:"I.
                                    I,!;`!i!!
                                    `. !.  .>ii~l^<>iil"!i;!!!>l!ll>.
                                    `. :. ..^,::l`::I:"`::"lI^;:,;!l
                                    `' , ..'i:"l"'::,;:`:,;"","""
                                    ^  ^   .:;;l<`I;i>;,i!I!!l<>l
                      l_" !!:i      >_<i><>:";Il:lIi,"I!!:
                      ;l` ;:^:      ^;I;;l:^"::I"";;^l!!l<
                                    "  i   .<i+!I<!i>
                                    '. ^. . `^"`::^`;
                                    ^. : ..`>,lI`,ll!;
                                    `  ^   ';,l:`!!:!!
                     .<~^.~<:!      <__~~+<:i!>i!;;~;^+_.
                      ;;' ,"`^      `,:,:;"':",:".^I""::.
                                    :. <   .!:+!,??.
                                    .  '     .^.'''.
                                    ". ; ..^+;!I^~<'
                                    ". " ..'l"l,,II.











```

*Figure from page 5 (2346x3317 px)*


---



4203-E P-332



SECTION 3 DATA INPUT/OUTPUT OPERATION



(f) bits 5, 6 Specify the DC code control conditions.



bit6 bit 5 Contents



0 0 No DC code control



1 0 No DC code control



0 1 Standard DC code control



1 1 DC code control TYPE 2



(g) bit 7 Required file name output in DNC-A mode (special specification)



= 0 : Required file name not output



= 1 : Required file name output



(3) NC optional parameter (bit) No. 12



(a) bit 2



bit 2



(b) bit 3



bit3



(c) bit 4



bit4



(d) bit 5



bit5



Specifies whether or not the file name is punched out.



Contents



The file name is punched out.



The file name is not punched out.



(Initial value= O)



Specifies the end of record code when punching in the ISO coding system.



Contents



CR, LF is output.



Only LF is output.



(Initial value = 0)



Specifies the code used for tape feed during punching.



Contents



The NULL code is output.



The SPACE code is output.



(Initial value= 0)



Specifies whether or not feed holes are punched during tape punching.



Contents



Feed holes are punched.



Feed holes are not punched.



(Initial value = 0)


```text


                                                                                               `^^^'" `^'^``
                                                                ........ . . ... . `  ..  ..' ^]]-]i}'!!i]]>
                                                               ;}_~i>~+[l-`~_-<_!?__~i<+<<>++>_,i?~_~+_><<_<
           `````'''''''`''````````'''''''```'..''...'''''''.''''```''''''`.''...'.' `'.''`.. `..'`.`''''.`''
           ::::::,:,,,^`""^^":,:,:::,^^`",,:^^"^^"^`^`":,:""""":::,::::I;;;:;:,:::,;IIIII:,,:,:IIIIIII;;:,:"
                      ;_. I<!^> i"  ^~;!;<!"<I"!i;"I;i,^;I!;I"::II>;,;;
                      ,l' ,i!,;'I`..^i!il!i^II,;l",ll>;,!l!l!,l!!i>ll!i.
                          ~,,;>_i_I;,,:",;><ii:"^l"^^^::::::"""::::;;::Ill!+iii!lil;;;;;;;,"""":;;;;;;;:,,"l"
                         .[^^`~-l-`'^Il^^,-<><'``<"``^`''....''''''''''''';_+_-}~]+^`'''''``^^^^^^`'''```^^~<
                         .~^^`.l> ''`;I^^' <:.'''!+?<i]_:><+?l~++_+_`'''''... .'''`^`'''''`^^"""""^``````""~>
                         ']``^^l>:::,!!```^>;,"""<~+!l~<;<~+_l<>i>i>^^^^^",,,:,,,,`'```^"""""^`''''''`^"^"^<i
                         '[^^^`,;''''!i^^^^_:''''~~?!![+,><_-I~_++~_.. . .`'```````````'''''```````''''''`'il
                         '[^^^^!!''''!>^""^l^''`'<>?-+~-+>!__>!<<-!l<<-<>I``````^"""""^`````^""""""^`````^`iI
                         ']``^^!i"""^lI''`^!:"""^!!+-i>~+<i~>I;i>->I__+<<I^^^^^'''''^^^^^^`'''''`^^""""""^`il
                         '[^^^^;I`^^^ll^"^">,^^"^>~[_l__-]!?_--_>l+--|!?"'^`^^^`^`^^^^^^^^^^^^`^^^^^^^^^^^`_i
                          ;;:I,"^^":I!;::;:,:;::;I;;;I;I;,,lIIll;I:;:;;;"""^^^,::;::,",,",;;;;IIII;,,,,:;;;i^
                      <{i <+,l      l__~>!+_:~[;I+->~"<<]l<;>`>+~>,_:i<>+>:+>+<!-;~~+<_~>?<i~;
                      .^.            .."^..'"^`''"^`^"^`"^^''.``''.'.'``'''````'^.^^^^''^"``^`
                                    ,, <: ' +-~~ii<~I?<:!~i<i;i~"<i->~"
                                    ,: ;^ `.+]_+~>~+l]_:i~i+i;>_-!<'.
                                             '"^^`"`.",'^,^,"`,:I,"
                 "_>  ~-i,<+_!!+lI~i<ii>~<^~>i"~!`'i;
                 `;:  ^"^`;;:""l";l:I:",:; ;;:.,:' :^
                      !]; <>:<      I-i>l<+i^l+!~iil`<"i~<i<<l-i"!~i!Ill:>!iii+>;l>I
                      ^:` ,,", .'.^`,III;,;I";;;l,I;"I^:;:,:I";I":l:,"^"^;:"::!;,Il:.......................
                         ^~`^"_-<]:;:<l^^"^^,:::,:,,:""^^"::,:,,:,"^;~ii~<<_!:",:,^",,:III;;;;;,,,:,:;;;;;;<`
                         ,]`^^<il>^""<iI,`^"'`''^^^^^^`'''..'```^^"";<~>_+i-!`"""""`''''''`^^^^^^''''''''^^-,
                         "_'``.~i.^^^ll_-+<{-!_[+}>+<+_<+-?-+i_};''''.    . .`^^^^`''''```^^^````'''''''`^^-,
                         "~''^"!;"""^!!~ii!+<I<+>~l!I!iiI>>~<<~~;;I:`^`^"""""^^^''''''^""""""````^`^",,,","],
                         ^>,;::il::::ii+_-~[]>]}_[~_<i_++[----[?>_?>"",:,,,,,,::,""",:::::::,^''''^^^"^"",^-,
                          .''`''''''``'. .'..`'.'.''''..`''''''''...``^^^^^^^^^^^`^`^""""""""_<+__!<->~ilI-!
                                                                                             :::;!.,!,!,"`!,
                      <+" >~:>      l~iil+i>,<>;Ii!!;i,il;l!,ll~l"!I!l^II!lilII:;">l"l<i":Ili:"`:"I;""
                      :;` ii;!'`"^""!+~~<ii>;li!ii>!i!I<il!lI>>+>I<!<l:!!l!I!>]!!;<<;l<i;i<<~~-!-~~~il^'```.
                         :_`^"]?~[,:"i,``^`.'''^^``^`^^`''''"""^",""i_~>_+<]>"""","`^`'`,"""""""^"`'``^",;:-`
                         :]"",!>;;'`'!;;!,,Il:,"",,^,^",,,,,^``````^l><i<~l>I`````""""""`'````'`^^""""^^^`'-"
                         :~^^^'<I.``'l>+?ll]!~~l--?i+'`^^^^`'''''''``''''....`'''`^^^^^`'''''''`^^^^^^^^``'-"
                         :<^^^^I"`'`'!>_>-!I_I<Ill_ii>^^^^^^'''''''^"""""````````^"""""^`````'`^""""""""^`'-^
                         ^<III;il;:::!>+~[~<~l?~++?_+>:;;;;;;;;:,,,,:;;;;;;;;;::::;;;;;;;;;;:;:::,;;;;:;:;l+'
                              .  ..                                  .              ''''''''^]~?}[!-{_]>!;}!
                     .>~`.<i,>      i+<>!+i>">i:;l!~:,>i!Iil"<ii;!<li"iI!l!"l:ll~l;l
                      ":..>!I!"^^`^^;<<>i!><I!i;I!liI!<<>lii:>~<ll<>>;iill~Ii!!i>ii]:""""`````````^^^^^^^^^'
                         l_^";}?i-^"`i^'``''^`'`''''^```^^^^^`''`^`^<[_~}-+[I```^^"^,::::"^^^^^""",::::::;,?'
                         !_``^;~I;""">l!:";l::"";;II":^"^:",;,,,,,^',;I:!l;>I""""`''''''''^"""""""`````````]`
                         l+``^`_I`^^`!!+<<<]~<~;+?_],-I><-_+i'^^^`'''.....''`^^^`'''''''``^^^^^```'''''''`'?`
                         I>``^^!,"^"`i<_~i![_?_[-l_+]!iiI<~_i+"^^`'''``''`^"^^^^`````````^^"^^^`''''''''''.?`
                         "iIlIIilIIIl>l!<<!+>_++~>--]~!>!_-[+_l;;I;,::::;II;III;I:,,,,:;IIIII!li!!::;::::;!~.
                                                                                            ^->-]?:+}<-l!l};
                     .>?^'~<l>      ~+><i-<<"<<i_<<:,i^;il<>i>,!!>i^i<I;!!l!i!>,>lil!:<i!,:I;I!!;l`
                      ",.'i!ll^",",,!<!!ll!>I<!i>!<Ili,I!I!<>i;ii>>;i!;l!!ll!<>l<>!l_l<_<!i<ii>>!-l^^``^^^^'
                         i~^^;1---""^i'..'..^`^`^^`^^``''`^`^^"^^^^^i_~<?+-]I^^"^''''`'^^""^^^^^^`^"""""",:[.
                         i~``^;!:;"""><il;I;:;;:":I;;;IIl:,;^``^^^"";I;,lI;l"'^""","^````''''`""",,""^`''''[.
                         !i'```<:`^^^!><-_<!<_-_l-_<__~~~<+~`.'`^^^''..'..''`^^^^`''''''''````^^^^````'''``[.
                         !!'`^^<"^^^^!+<<><li++~l_~!<+i!<!i~_-?I""^```````^^^^^^^`''''''''^^^`^`^^``'`````'}'
                         ,i;;;;iI;;;;!ll<<>l~+_+i_~><_>~_++_~--!II:::::;II;;;;;;:,,,,,,;;;::;!IlIl:,:,,,,;l-.
                                                                        .......... .. ......"?<-}[;_[>?;Il},


























```

*Figure from page 6 (2346x3317 px)*


---



4203-E P-333



SECTION 3 DATA INPUT/OUTPUT OPERATION



(4) NC optional parameters (bit) No. 27 to 31, 49 to 51



(a) These parameters are used to set special EIA codes.



Parameter No. blt7 j blt6



blt5



blt4



blt3



blt2



blt1 j bit 0



No. 27 Sets the punch holes for the EIA code that represents"=".



No.28 Sets the punch holes for the EIA code that represents"*"·



No.29 Sets the punch holes for the EIA code that represents"[".



No.30 Sets the punch holes for the EIA code that represents"]".



No. 31 Sets the punch holes for the EIA code that represents"$".



No.49 Sets the punch holes for the EIA code that represents"#".



No.50 Specifies an irregular code.



No. 51 Specifies the regular code (ISO) corresponding to the irregular code.



I 0


# I Initial

value



(b) In both the EIA and ISO coding systems, it is possible to have one code treated as another in



program reading and program punching.



(c) Set a code which is to be treated as another code (Le. an irregular code) for optional



parameter (bit) No. 50 and the regular code that corresponds to this irregular code for optional



parameter (bit) No. 51.



The regular code must be set in the ISO coding system.



1) If an irregular code is encountered during reading it is read as the corresponding regular code.



2) If the regular code corresponding to an irregular code occurs during punching, the irregular



code is punched.



(5) NC optional parameters (word) No. 1, No. 2



Parameter Factory Set Setting



Item Contents



No. Initial Value Range



1 Tape feed For punchout in the PIP holes in 600 1 to 10000



holes in (transfer) mode, tape feed hole areas



punching are punched out before and after



program punch out.



The number of feed holes is set by



this parameter.



2 Defaults of A file of machining programs which is 180m 1 to300 m



tape too long to be stored in a roll of paper (590 ft) (3.3 to 984 ft)



lengths in tape is divided into smaller files to be



divided punched out. The lengths of the divi-



punching sions are set by this parameter. The



divisions are closed at the breaks of



each block, so that the actual tape



length is slightly different from the



setting. A divided punchout gives the



beginning of each tape part a file



name. Note that the setting does not



include the lengths corresponding to



the fife name and feed hole.


```text


                                                                                                ^"^^', ,``^^'
                                                                .`''''.'' . ..'`..'.' '... ''' ;?-_]!].<;~]?;
                                                                i{~~l~~+]I+.<+_+~i}[><>>++<~~_><^i~+_+-+<+~?;
           .^^^^`''``'``````^^^^^^`^`````^````^````''''```'.''''''''..''.''.'......' `.'''`...' .''.`'''..''.
           '::::,"^`^",^`""^^^",^,"^^`^`"",,:,",,""""^""::"",`^",:,:;;;;;::::::::::::::III;II;,::,:;;III:,,,'
                  "+!  ~~l"!i<l;<;:<!il!i>ll`>>i,~l.,>"l,:i".~!II"<"
                  "I,  :,`.:::,`I`,l,I":I;,,`I;;';:'^:.:"";^.!:"I"l`
                    '!l ;lI:;"^;:::":;:,.,;,.":,:""'::^",:^:,`I;"'^"I:^
                    "<> ,:>i<l><<!il><<i,><i"<+<lI>,~~:~~~i_>I+~!;<i_+i

                          `~~>>><i>iI!<!Iil>>!<IlI;!l>>l~l><ii;IiIii!iI!lli!il,l,;II!;Il;ll;:":,;lIlI;l
                          ,]i]-?~<?[>+(+:~.__;!.I:"]>+>'+.<[l?`;<']_l+'i^,[<>l'?._}i-'";']-I!`i"i1+-i^{
                          :> ..<<I"_<`'`:_+~+>l?-!~<<~+I+~+~;~<!]~I-<~;<>_i!+~+i~<><<<i_l:lI"":,""`''^[
                          ,+","~_l">l`^";-+__<!<>;>i>~~!~+__;>!,><l_~~Ii<_il<<i,i>i<+_i_i:l,^''`""""",[
                          I+'``~}!,[]`'',~_-?<>]+l~i<++!<__~l_iI~+l+~-I+~]<!__>l_<<-++>-i:i!,''``````^[
                          l_`^`~-i;?_^''">~_-<>-<!<!!>iI<~-_i_>!~iI~!<I~~-~i++~l>>l>><i_il+,"^`'''''^,?
                          l_`^`i+l,~_,,,;~~~~i!+~!+<>+>;>i+<;+iI+~!_><:ii~>Ii~<l_->_~~!-!I+"^^^"""^`'^+
                          l_'`'<?!"]_^^`,>-+?>>-+!_~~+~I_><_l-il--l+<+;>>+ii~+~!--+_~<~?iIi^^^^^^^^``"]
                          ;>``^~+!;-i"`',~~<+>i+~!~>i>i;><_+i_i!+>;<i>:ii_>>~~<l<>!>iii_!!_I""^'''''':[
                          ;<""`<<I,+;'^^I-_?+i!><l+~+++I~+_<I+!I--l-~~l~<_ii<~>!_-~-_?~-!:[:`````````"]
                          ;>^^`-_;^+_`^^;___-il~+;+<~+<!+_~~l~<;__!?+-l+<]ii_+>I]_~+__+_l;]:`'`^^^^^^,]
                          I>'`"+_!I_+,^`:><<~~<-+>~~l!lI!l<~I>>!>!:;;;,I;!!Ii<!I>iI!!!l>!;<::,,"`^`^`,[
                          i~^^^~-I:?<`'':>-}_~_-+>;?:i~-}>_-:<<+-^  ...                 ..   . .. . ."]
                          i+^^^?_;:~;''':<]--_-?~i<_~l_-+_?!i<+?;<__+>>++_-~~>i_+<!+>i__!~~~>!~!:ii?i:+
                          :>,::<_i!~!IIIi_i>llll~i!<!I>?-l<":!i->>>!!ll<!!ii<ii-<-~i<I>+;!l+?i]~!~>?<,-:;I;;;
                            . .      ...,<  I"  ,'  !.  >  :I  :;  I^  ;. 'l  'I  :;  ,"  l`  i'.'!  "+~_[}~].
                                        :-'`l:'.l^.'l`'^+'':;..!!.'l"..~^.^!..`!..;;..lI..!". ~` ^i. ^+i]--l].
                                        .!;;,:;,:,:;:;;I!;;:",:I!II;;II>lI:"::;ill;;lIiiIl,,::ilI;:IIl>!lII;l
                    .'  ' . ''.'  '.'     . .
                    l[!.-:!i_>:-<:__+"?!<:?+>,>i-~?l>~~__i~:!><l<<_?-??l_Ii+~_I!~_li~+]I<<_]-_;-~l]!+-~+"<^
                     ...~ii_><>,<~_~~~!i_<>>i>_<~~>+i+~~~i~,..'.`''''''.'' '''.'''.'`'`.''^`^`.^`'^'`'`` '.
                       .".^l^,'.',"^`:,"""`:`^!^"^.:"^"^^`!
                    :i; <iI^,^;;~^:!IIl`l`;'II`I;I>I;"l`,I,i>l;`I;>;"::."!`;:I:,!I'::;!:,!,`;Il:;l,
                    ^I,.>+ii>i~+-:+~<>~;!I-:i~l!_+<<>l_!<i>~~_li~~+ili<,i_:ii~]<+]:!><+i:_!,~~<_i?l...`'..'
                       '<>!~i<~_l"_<~"+i.i_,i!>,!>I^<?~i+`!>>~,_>?,i<!i+_><l_!,i:<<!:!>-_>_;:<>[;I_,!??+~~?'
                       '<~i+<<_-l"-+<;-<'i!`
                       .I,````'^^'```^`'`''`''..'`'''`..^^^...''. . .'...
                        !!~"!~?>+i'~i-~`>!_>;+;I?<;>,i+:<-<,>>~~i<l-~-+<;
                    "!..>">;:!>i!!>":Il<"!,;ll;I;!iIll:!I;Il"lll!iI:;:!^lIl;:l^il,";;;lI;;Il!:,^;:::I"^::!"
                    ., .,^l^^":ii:l`";,l",^;,:"I::l:;l`II,:<^:IlI,i:^^I"I!i":>`;!:^l;:i>iII!lI~^!<<Ii"^l!_l
                    l+..>I<i";ii:!I.l:~!"!!lii~l!l+!i:>`l!^Iiiil!!`!l<!"l::;!^!i:ll::I;I!!ll`,il`:;;l;!l
                    ^,.'!l__:<i?i~<i<~>:`:"^:;!,,,I,i,:`::`":l>;;:`I:;I^:::::":l,,!!;I;:;;;>I^;l^,:l~II!.
                        :Il!'l"I;IIl!l^
                  :l' ^l;''`:^^`".`^`^^,;,,^`,"",:^;" ^.";^ ,'
                  i-: ^~<"I_~<!i+;<~!_!+_+<I:~>ii<,_>.:^:-> >'
                      '``'```'`'`,"^^^'...'`^`^^^^"`^"`^`.`^'^"^""^""^^^^^^"""""""^`.''''`''`^^^^^`'..'.'```.
                      +[-[?]+]{}~~i"""!II;^^^,~","""""^^^"^,!IIllI!;"^^^^^":::::;__-_~~+~;}[+li::;[?[{>_l"":<
                      ~, ^l1<,`^.!"   >+>!    i            'ilI~+l+l             !:>{--l?~~-!."   -]__<{'   >
                      >;""I~-I:::<ii;;"::,I;:I]il;":,::;,,I;:;I:,I;l,:,,,;l;:;:",-;i>>-l+-<+il!^,,!i<>}~;;,;+
                      ~^   ';    ,I-1?~i]++" '~~~<l--<_+~~+<li?_I~[+"+?--I<:..  .~   .]]-^   ": :;+I,_]_]~."-
                      -^         ,ii+_~:~`   .><>_<~?_i,i<>-!"?-?lI_+~;>~[,<~___'>           ":            `-
                      _^         ,>_>i+~<-!  .I~_iI_!>+~_+;~_!~]?~~ii]<i<{--'....!           ;l            `-
                      _^         :"'. .  '`  .l]>>]<-~I~<+~_I!<<.    .    ..     I           ;l            `+
                      _^         !^          .;_--~><<+]_;I-i}]?!<><<lll:<!I<;   ;           ;l            `>
                      _^         i^          .l<__"~-+_<+i<i."""'^,":"^"`;^`;"   ;           :l            '>
                      _!::::;""""~!;:;::l::l:I?<<~l><~~i~~->;"``^^```":,,":"^^"^,+^^";;;,,,"^!i^""^^"",,,",I<
                      ~^ . l<    ;<-?[]~}~l?'^~<:+[:iIl~_<!<-+?!-~~1~?_]I?_~?~I?`<..'+1?!]:..:; ;;-I~[-!<i.">
                      ~`         :>]_~^      '++~;I+<~!~;_~;?<--+l~I<I<],+li-?~<'>  I[[[I?!  ,:<~!>~l<1?l-+`~
                      ?`         :<[_?{<!i<  'i+_~<I<<[<>?-<<+~;~~>+}~:-__;->_?!.>  '```..'  ,:``'.'''``.'^"_
                      ]`         ;I_l?]~_ .  '!<+_<+~<>l<+^"?~+:]<<}-~^~>-+il~<;.I           ,:            ^+
                      ]`         :>+<<]-i>:  'i+~>_li-i;?-:l!l_~<!?]~_<_>~;`_<~".;           ::            "+
                      ]`         lI:"",^`!;  'l-_i_>i-!l]~,[+!<]l+++-<>++_l,;l]'.;           lI            "+
                      ]`         ~'          '!~~>?l<~!?!I!i_--~<->;~~!<<~-_il; .;           lI            ^~
                      -`         !'          'i+_iili<i_!:]i!!]~_+~;-~-_>;[--'  .;           lI            ^>
                      ~'         l.          `i~+?)_,~;-]1i{_:]<->~~!!<<>li~l``.'I           ;:            "<
                      ~'         l.          `i+_??<] IiI[>~]-!>ii<~<i_!__~-!~__^i           :,            :+
                      +.         l.          `!~]_+>~+]l<!i-~_li[]~!-->;~i]<    'l           :,            ,+
                      ].         l.          `!>]_+< I1_[l>_-i<+_I??]i_I~~>~"l<i.l           :,            ,+
                      ].         l.          `i<<>i+<I-<l~+l-+~:!>+><~-_~[]+<<_`'l           ;,            :+
                      }.         <'          `i-]>_]<l_?i_!_-_~?+]~<_}+^'^`^:`^ 'l           l:            ,_
                      >l;IIIIIIII<;::::::;llli~<_<i+<l<<!~i_<->-__<!<<>:;;;;:;;I!<::,,::;IIII~<IIII;:::::::!i
                                                                        .......        ......  ............










```

*Figure from page 7 (2346x3317 px)*


---



4203-E P-334



SECTION 3 DATA INPUT/OUTPUT OPERATION



(6) NC optional parameters (word) No. 6, 39, 40, 41, 42



Set the baud rates for channels CN0: to CN3:.



NC Optional



Parameter Channel Contents



(word) No.



No.6 CN0: Any of the following baud rates can be set: 110, 150,



200,300,600, 1200,2400,4800,9600, 19200,



No.39 CN1:



No.40 CN2:


#### No. 41

Initial Value



600 baud



CN3:



(7) NC optional parameters (word) No. 34, 35, 36, 37, 38



Set the ready completion waiting times for channels CN0: to CN3:.



NC Optional



Setting Range



Parameter Channel Contents Initial Value



(Unit: Seconds)



(word) No.



This is the waiting time between


#### No.34 CNO:

output of DC1 (tape reader start) or


#### No.35 CN1:

the cessation of data reception and



reception of data; or the waiting



1 to 9999 time (when CTS and DSR are ON) 10 seconds


#### No.36 CN2: until the RS232C ready completed

status comes into effect. If there is


#### No.37 CN3:

no response within this time an



alarm occurs.



(8) NC optional parameter (word) No. 45



Used to select the punch channel for data transfer.



Setting for No. 45 Peripheral Device Initial Value



0 CN0: (TT:) [RS232C]



1 CN1: [RS232C]



2 CN2: [RS232C] (This selects CN0:)



3 CN3: [RS232CJ



(9) NC optional parameter (word) No. 57



Used to select the read channel for data transfer.



Setting for No. 57 Peripheral Device lnitial Value



0 TR: [Standard tape reader]



1 CN0: [RS232C]



2 CN1: [RS232C]



3 CN2: [RS232C] (This selects TR:)



4 CN3: [RS232C]



5 CN4: [RS232C]


```text


                                                                                               ",""`: ^^`"^'
                                                               ''''``''' ' ..... '.' '... ''' ,?--]<]'il<]?l
                                                               ![-<>~~_[;-.>+_>+l]?<><!~+<i+~><`i-<-~-+i<~]l
           ^^``'''````````^^^^^^^^^^^```````````^```''''``'```'''''. '..'''''''''.'.'.''.'.. `.'`'.''.'..''.
          .:::,""^`^",^`"""""""",,"""^^``^":,,,"":,"""`",";:,::^^,``",,,:;;;;;;;;;;;;;;;::,:::II;III;::::,:^
                 `_>  >+!^i>~l;>I:i!iliiill^lll!~"i>"^~.>_.,~,'i: i>.
                 `l;  ":^`I:;,`I^;I,;^;I;::`::;:l^:I^.!':i``I"`I,'li.
                      ~_<I_~:i~l<,I_<>:!l^!<<i;i<i,>+-";>`i~~~'
                      `"`.^"'`,,,.^:,,``"."";"`,:,'"":`':'^^:,.
                     .!i~<!<>>i!!!:;:":::;:::!;::",""";I;II;;;:::;;IIIIIIIIIIIIII;;::::::;IIII!I;;;:,,,,,;;l.
                     ^iI)-;+[[-+~["l:^^'''''.!        .........  .^'.'..'.....................!`'.'..'.. .'_,
                     ^i <>-~+~-_+^ l;<~~~~~?^;                   .~~_?]<?~                    ;'>~][<l?]<- ~:
                     "_'<]_<]_:{+`.i,.     ..!                      .    .                    I'...'. '''` +,
                     "]";,>]>,+:"^`i:,~_-_;"^>iiI;I!<~>l><i!!Il:iil!!!~>iIIiI"II:l!:"li!:<~~;">,^^^^^,,,,::[,
                     "?"""!-<"-:`^`!,"__]-;"^<~}[>l~+]ii??~<?~1_i{-]+>?}}~++?i]{l~}i;~-~.!_~" ;.           ~:
                     ,-^^:]_:I[?'`'l""+_-l"^`~!<~;`~~<.~~~: !<+_.i<+]I'_-+_'i[++< i--~_l      ;. ...     . ~,
                     "-"":_~::-i```l""~+-+:"^+                                                i.`{-[!-]<-, >"
                     "~^^,_-II]<^^^l"^>>_~,""<                                                <' ... .''.  i^
                     "_^^;{?ll-l^"^>:"+?}?:"">..........     .                                !.           _"
                     .:`^";l;;l:::,!;:ll!I","!;;;I:;II:;;"";;,;;:;I::III::::::IIIIIIIIIIII::::>lllllllllllI~'
                 ^>l  i<I";;l::!;;I:IIIIl;I^l;::i"iI`^i; !i.;~"`i:.!i.
                 ";:  ;l"^!I!;,i"!i:!;lll;l^il:,i^ll''!I'l!`,~"`!^ i~
                     .~<!l<l^I!!<;^llI!>>~;I`!l>!I:,illI:!;^l;>l:!~",<~<^ll,i<~!.
                      ";"`,:`":lI;^;:"i;II:^`;II;;!";,I;`;:',:!::ll"":II.,;`::!:.
                     `i!iili!!I,,:,:,,,::,::;!,`'''`^"^^,"":I;,""^^",:::;::;::::,::::::;;;;;;;I;;;:,"",,:;;;
                     I_i(_I?-?-+~}^l"^^'''''`<^~l<<l:I_!IIi'!"''.''..''''`^'''''..''''''''''''~^''' ''...'`+`
                     :i ~><~+i?_+` I:+<+?+>-",l?--~_(>_]~1):;'           I~~>_+i]I            >'+_?-!!-]>_ +`
                     :i.+]?-]<~}~'.~`. ......Ii!ll^"~<l!Ii<ll`             . .. '.            !.'''^..'``` -`
                     ,_:lll;II:;I:,-;^""^",:;~","""^''````^"<>~i!I!;<l,:Il<!!Iii!I!I!lIII:""::_;:::,:"^^^^^]`
                     :l  '_>',-;   ! .<_[~'  :              ;;!+?;-l[]~_]+?-[!~<-ii]-_?]?+... l            _`
                     ,<^^^`",,",,,"<:""`^"^^^l              ;<-~]~>;~;-~!"I[]-<:~__-~^___-l<< !            -`
                     ;<''^i;^:>;`^`i^"l!l,`'^>              !~~~,~-_+[_<>"-I<]]_;+~~[_+~:!]>i !            _`
                     l<  '~~^,_;   I 'i<~,. .>       ....   <!?++]-_+:!~I[}];,~,__l~]]]+]l    !            ~'
                     l]:,^ .`` '"""<;,^`'^,,;<  'li_I{{[[`  !>?~?I_]-?<;<i_+<?<><+}]I~_+!+~_` I!?;<-<><+?: >'
                     l<  ,]<^I[l   ; '~_+<. .!     . ....   ll><>I}-:_--_--+;>~-+~,<!+_]_--?. !.'.'`'`'`^' +'
                     l~'``":"^;,^^^<"^:,;,`'^I              Ii]?-iil><<++l_~I:[1-]I'_!]<??i-, ~            ]'
                     ;i'`";"'"::^^^_,"II:,``"I              I!<l>-+<~>~_l>_?_<i-]<+i++I]_:',^ >            ?'
                     Il  ^-+'l~"   ~ .<+_>.  ;              I!_>l-i-~i~-l:,",,.,:,"I,l'!"     l            ]'
                     "!:;;",::,,;;;<;"^``";;Ii;;;:;II:,::::;<_[[__i_?-+<_:""::;::::::,;^":,::;~IIIIIIIIII;:-.
                 ">,  l!,":I;,;I",:,:::;;"^::",I,!:'`!:... .             ..................................
                 I?l .i>,,>i>ll~:><>il>i<;"<i!l>,<i^^~I
                     '!<<<I>,;<i<>:<i;:l;l+l^i!~>l<I!l'~__l<~><_->.
                      ::,"`"^^;,:;^,;:,;;:I,,::I::I,:I";I:"":,":,".  .. .'''''''''''''''''''.    .     ....
                     !<^]--]+~!?~>{_;i{>,<l"^^^^^^^,,,:,l?_~+_>!>>>-+++-i:::,"""""",;;;<I;;;<+?+_>-_><!,,,,<
                     >~^i<>~i_I+i:>i:I_l">I",,""``^,,^``;!~i-<~+_~i+~<<-!""""^`````````>^"""!~-_-;+?~_l````_.
                     i>.       <:   .  ..;^`>_]_"'i<<;l'.     l?+_+<-<?".'''''........'~''''..   .     ''''?
                     !l        :'        :' !i!:. .           :~>>iii!<^               <         '         ?
                     l;        :`        :`.!>!;'             ;~><i>il<"               < '`     `-'  ...   ?
                     l;        ~"        :`'i><<'             ;_~+~++>~^               i`__<];_--_-];_-[~i.?
                     !;        !`        :' l!i!.             ,<ii!iili.               l                   ?
                     :i:;;,",,"~!""":::::~!;_-]-;^^"^^",::::;:_[]}]?[__;:;;;;;;;:,,,,,,<,:;::::::::::::::",?
                 :+: `~<I;!<illi:l!l!!i<>;:il;li:~l^li;'``````'..     .'```````````````'`^^^^^^^^^^^^^^^^``.
                 I_; 'lI'"<ll;:>^li;l;i!i'^il;l!.!! ,l.
                     `;I!i:l^:!!ll"iI"^I;!":lI:;!;;i""ii!:!!II<i"
                     .;I;l^;":!Ill"Il:^!!!"IliIli!:i::ii!";l:;l!^
                     ;l^~!~~>i!<!i_!:<_I"l:""^",::;:;;::!_illiIli<++~<<<!I,,,,,,,,:;;;;<;;;;Ili!!!!illI;III>
                     <>^][}[-)<]+>[_,<+:`>,```'^^^^^^^`'I<]~-~__-~>_-~+]: ...   .'`^^^^-`'''l~?][l?1-]l``^"{
                     >!'....''`~:'..'. ''i"`~[i^^^^^^`''.   . I?+-~+-~<l-?-li_-]]]+""""_````''...'..'''`^""[
                     i;        ;.        I. ;I;,              :<i>!>>!I`:I,'',:::"^    i                   ]
                     !:        :.        l''ii~>'             i<<++~~>i.               l                  .]
                     l,        >`        l'.!~!:.             >~><<~~ii.               I        .:         ]
                     l,        !'        <'.li!:.             i~ii!>i!i.               I .,"^'.`:-`^'`,"'  ]
                     l,        >^        <''i<+i'             <-<~~~_>~.               l ;i>_~I]<<~?>"<~!' ]
                     >:        i`        !'.i<i!'             i~<<i>>i<.               I                  ._
                     ~:        I.        I .l!!;.             !>!il!ll>                ;                   ~
                     ~!`^^^^^^"[;^"^^^^^`>^:-?[+,^^^^^^^^^^``'+{][]{}+]"````'''''''```^~```````'''''''''''`_
                     ',"",:::::::::::::,":"""^",::::::::::::,":^",,;;;l;::::,,,,,,,;;;I!;;;;;;;;:::,,,,,,,:,















```

*Figure from page 8 (2346x3317 px)*


---



4203-E P-335



SECTION 3 DATA INPUT/OUTPUT OPERATION



(10) NC optional parameter RS232C {CN0:)



This screen displays the parameters to be used for the tape punch interface function, which are allocated



to NC optional parameter {bit) and NC optional parameter (word). Note that they are only for CN0: device



and it is necessary to set the parameters for the individual NC optional parameter (bit) and NC optional



parameter (word) screens for other devices.



When the following parameters are set, the corresponding NC optional parameters are set accordingly.



Conversely, if NC optional parameters are set, the corresponding parameters shown below are set



accordingly.



PARAMETER SET



*NC OPTIONAL PARAMETER"



197/07/1~ 14:10:00



Aszn: <CNo:)



NO.



l STOP B IT(l '. lbi t/0:2.bi t) 1



2 PARITY CflECK(l :Yes/0:No) l



3 PARITY(l: Even/0:0dd) 1



4 8 BIT JIS(l:Yes/0:No) 1



5 DC CODE(l :Yes/0:No) l



6 DC CODE TYPE2(1:Yes/O:No) 1



7 FILE NAME REQUEST at DNC--A(l :Yas/0:No) 1



8 MASTER/SLAVE or RS CONT. (I :SLY, Yes/0:MAS, No) 1



9 BAUD RA.TE(bps) 99999



10 BUSY TIME(sec) 99999



ACT POSIT (WORK) 300. 000



SET



100.010



100.000



ITEM t ITEM l [EXTEND]



(a) 1 STOP BIT (1 :1 bit/0:2bit) {NC optional parameter {bit) No. 8, bit O)



RS232C stop bit check



= 0 : Stop bit 2



=1: Stopbit1



(b) 2 PARITY CHECK {1:Yes/0:No) (NC optional parameter (bit) No. 8, bit 2)



RS232C parity check (sets whether or not a parity bit is added to 8-bit data)



= 0 No parity



= 1 Parity check



(c) 3 PARITY (1 :Even/0:Odd) (NC optional parameter (bit) No. 8, bit 3)



RS232C odd parity scheme



"" 0 Odd parity



= 1 Even parity


```text


                                                                                               .^^^'`" ".``^
                                                                ....'. .    . ..    . .    '.  l}-?_<- +;-[{,
                                                                _}_<i++-+l<'?_-_~i}]~>><_~<~-~<<"++~-+-+<~<?,
           .''''''''`''``````'''''''''''''''''''''...'''''......'`''..`'''' ''..''''.^.''''  .'..`'.^'``'''`.
           ',,,"""^^";;,,::,,^^^^"^^,,,,,,::^"^^^"",^^^::;;::::;I;IIIIIII;,,,:,::;:;I;IIIII;::,:::;I;I;;I;::'
                 'lI<..~<;,li!ll!^;lIl;I!!:^<>><iiI`li>!:^
                 `:^!. ;;`^!l;::l`I!;I:;I!".:IlllI,`;;ll:^
                 ,>i,,~;lil`l>!lllI,il":l:!lI!!;:";;!"`IIllll"<i:!iil;I,IiI:!il>!IIIIlIi;I^`!!;l":I:^>i:;!II,
                 II~_<ii~-iI<>~<<_<!~_!l?~_I<<~~+il!_~!~~il!<;>~><-~<<<l<lI~i_><-<<i<>i><<::+>i_I>_+i-i~~+~~;
                 ii;_>,~~<i!+;!~l<ii~+i,?~!,!IIl<I,+~+~l_;!+>~li~~l`~<i>< `_l<i!!<Il>~!I~<:!!_:~i,i<-l'<<!!>,
                 l>i:l,<^!~i<+~~>I:!'<~"_<ll++>>i<~~i^!>"?_ll~+~>_!?ll-i"?_~<i+li_+<>>_-+`<~-:~>~;_?!,~~+ii]I
                 <+<~~<_?~,++<i?I~~~~~~il_l:+++~"[-i<<+l ....''.''''. '. ^`'`'`.^^``''``^.```'```.'`'.^```'".
                 ::""""""".""^',.`,`""`".^'."`"".,,^,::^
                 i->>>`-~I;+_i~Ii>">iI<l~_<!;;<!^i~^^<l^!!!i~~>>i<i>Il-i`i><i>i;;>>!!!><>!,!!l^>i"!!lil<<i~l
                 iii<i>i~+i,i!>]_!!+_>~<+,<<><~~<-~>^i~i:~~!;1+l:<>__!~iI~?><,>i~~~<~~+~Ii~<<<Il_l+<~;>~ii]?"
                 liii>_>>~_'"`^!; :iI;;ll.li;!:I!iIl'IIl.i>:.l!"`liIliil;l!;-^li!!ll<<!l';!l!i;.ii!li <!l'><"
                 ><!>!><!?_"
                                ..'.......'. ...''.''''''............''.............''..
                              ':,;l!ll!!l!I!I:,,,:::;;;:;:::::;I::::,:;,"""",":,"""":,:::'
                             'l.'l!}11/?}]!)_:,,,"`^"`^^``""^",`^^`^,"":ll;;:;;";":;I!>'.l.
                             ^l  .           ....:~;"+l:<~:`i><-!!~l...;_-}r1)\>)|[?+[i' :`
                             ',   "?:            .I"'l`"!>;';!i_;;i^      "ill!:;<;'     :`
                             `,   .:"!~-,~!l!,!i:II"~"I`                           ,     :`
                             ^I    :l+(1i?I<}--!l~}+-!}<'                         .!     :`
                             ^;    ;!!-{!;;!~~-~~l?{_^ .                          .!     :`
                             ^:    ;;<i+-i-~l!!+[~]i~,                            .;     ,'
                             ^:    ll]?`|r]:__)+iI}-"I:>;                         .!     ,'
                             ^:    :I+i-<-(|;_)?-->!]:{j><iIl_<il_>`               ;     l'
                             ^:    l!]{}-{?}~[~l<"}ll-)!`<!]<I+?<__)-:-i.       ..'I     I'
                             ^:   .~l{(};[[|_][~'              .   .. ..       ')1|1.    ".
                             ^;   .l^i<>`"l};>+;                               .+<_<     ^.
                             ^:                     ,          ^          .^             ^.
                             ^:   ^!:^><I: >_+l. .i<>l~"     "!i;l:     ^l>i!!           :'
                             ^:   `I^':l:` Ii!:   I;':l`     ^I"":,     ';:^lI           ^.
                             ^:                                                          ".
                             ^:                                                          I'
                             ^:  .^                                                      l'
                             ^: ';,',,"l,""^^"l"^^^^",''''';:^^^"^I"^``^"l^`''^:!,^`^'`  I'
                             `;   !i.  I     .I     .'!<!i;:^     I."!i,.I "i!^';`!I!il" l'
                              ,:^'>l'.':... .',... .`'!<i!;"'  . .:'"i~:'^ "!>:^"">!!<~!:,
                               ."I",I:`";::I:`:;::I"`;,"^"..,,,:;^`;,^^:'.,`'^:`";^^,".`'
                                >,[<`il+:{],!I!!]?^ilI!?-"<>I~{<,!I:>[~:i>;]_lIIi:-[li;
                                !IiI,!:>;><;l:lI!<:l:!;l>:!I!liiI;:li~<Il!Iil:l:!l~+li:
                                    .             .                ..     .. ..  ...'.
                    ":`.",lI:l;:!I^^^`,:,:^;":^`;:^'^,"`^"`^^^^^`""`.""^^:' ".`"```
                    !_: ""i;Ii"l~;'l,^!<i>;<>+lI+~I;~_~ii_I~_>-<<--i,__~:_<`+Il?I>~
                       ^<>!IIlI`::;^;I`,:,::
                       'l!>ii>;'!;>,;!^i!iii.
                       '^::   "?!!"Ii^!
                       .^"".. `I:l"":`:
                       ',,".' :]>>;!+";
                        .     ."^:''^ .
                    ~+^^i;~<~<lI"I!~_!~<^l"i>!<!>~!,!+~I:!<!l!i"!!I!!l>>:,~<II~;.<^;>,!I
                    Il``:.^,""`` ^^,;":"'^.^::,,^;:',:;^^iI:;:l`;I,l::l!"^ll,`!: l`,!";,
                       "]-_<-+>:~<>_"I_<i+"ii<~^!>i-_>;`>^;l:::!il+,;<,l"!ii<!;i;I!;i"!>~<^
                       .`",","^^:"`:"`":,:'::::`,,:;,;"':`":^,:II,I;^;^:^;;;I;":",:,;^;ll!`
                       ^;!I   I]!:+<i?"
                        .''   '"'^"`.,' .
                       ^;:".. I<_>]I>-_~?"
                              . . ..
                    <_""ii?-]?>~,i;_<<+!-i<~~],+[_;l-]+i>-!+_<+i<__;l]_l!-!']^i~:+l
                    `^.'"''^'`'. ^.'''^'`''`'^.```.`;^^`^"^""^"'""".^,^^'""."'^"'^^
                       ;]??+]?<^<?_;+_~]:<<!+~++
                         `'...`^`^''`^``..' '..'
                       ^:>;.. I~_+I+_i-I
                       ..'.   ""'`'.`'""
                       ":"`'. <<<_I:__<["















```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-336



SECTION 3 DATA INPUT/OUTPUT OPERATION



(d) 4 8 BIT JIS (1 :Yes/0:No) (NC optional parameter (bit) No. 8, bit 4)



RS232C 8-bit JIS



= 0 7-bit JIS



= 1 8-bitJIS



(e) 5 DC CODE (1 :Yes/0:No) (NC optional parameter (bit) No. 8, bit 5)



DC code control



= 0 Controlled by DC code



= 1 Not controlled by DC code



(f) 6 DC CODE TYPE2 (1 :Yes/0:No) (NC optional parameter (bit) No. 8, bit 6)



DC code control type 2



= 0 DC code control type 2 is not executed.



= 1 DC code control type 2 is executed.



6 DC CODE TYPE2 SDCCODE Description



0 0 Controlled by DC code



1 0 Not controlled by DC code



0 1 Standard DC code control



1 1 DC code control type 2



(g) 7 FILE NAME REQUEST at DNC-A (1 :Yes/0:No) (NC optional parameter (bit) No. 8, blt 6)



Request file name output at DNC-A (option)



:a:



0 Request file name is not output



= 1 Request file name is output



(h) 8 MASTER/SLAVE or RS CONT. (1 :SLV, Yes/0:MAS, No)



(NC optional parameter (bit) No. 40, bit 0)



Master/slave station designation or RS control designation



= O : Master station or without RS control



= 1 : Slave station or with RS control



(i) 9 BAUD RATE (bps) (NC optional parameter (word) No. 6)



Selection of baud rate from 110,150,200, 300, 600, 1200, 2400, 4800, 9600, and 19200.



Initial value: 600



u) 1 O BUSY TIME (sec) (NC optional parameter (word) No. 34)



Sets the delay time until data receiving or RS232C getting ready (CTS and DSR ON} after sending



DC1 (tape reader start) or interruption of data receive. If there is no response within the set length



of time, an alarm occurs.



Setting range: 1 to 9999 sec.



Initial value: O


```text


                                                                                               `''`.^ `^.``'
                                                                ..... .       .    .          `}]+[!}'ii>]]_
                                                               ;)}+>~~_[l_`>__++l?[-i~<~+<+-+!-:i?+-_--+~~-<
           '''``````'''''''```'``......''''''''''..'''''.......'^``'.''''`.``''''.' `'''``.'.`' '`.^'`^`'`'`
           "",:;;;;:"^"`^`^",:;,""^"^`'^^^",::",,,""",::,""^",::,,;:::,^^,;:;:::":,:::;;;;I;;:::::::;IIIlI;"
                    l>."I!;+il.i<";";il;i;i;:^<i;`;ll::l":I;;::I!I'I;l^i;.,:.l:"l
                   .l!'^":^l"'`;;^"``;III:llI,i!;"iilll~;><iil!<<<^>!<">>^Ii`~l:~.
                       !-~<>_~I;>l<:l+i
                       '^,,,;:^^"":`,::
                       ""<^.  ;I<i`<?;
                       ..^.   ..^`'^"'
                       ,,;.'. -~_]"~]l
                              . .....
                   '~~.il<_!;<~<+-^iIi_>>+i?<l:-_!,<~_i!_ll~i!!i><>`~_<:_i'!l^~!i<
                   .," ^`^^'.^`^``.^.',,,,`,:"^,:^`I;::"I";I::,,;;;'llI`;;'::`l::l
                       !_i"~>~+^<<<~<i
                       ..`.`'`"'`^''^. .  ...
                       :"+`'  i<!~<!_?_l->I-+"ii_]^
                       . `    "^`''''^`^^^``..^^``...
                       :^;.'  ~-<I<~<-!]-~!~_:__:i~~]:
                     .   ... .   . ' ..     '
                    >[ ~i~-!l++?--`ii+?_~,<,~--~__-<;>]_ll]-+>~[l<~!->~__l:_-<l?~'-;l_i_i
                    .. ^"^...`'.'''.....'.''.'`''.'`''.'.',``'`^'^`'^'`^^''^^^.^^.^``"'""
                       >-i"ii_~">><<<;~_-!ll
                       . "    ",".''"''"`^^```'^'^``.'''.'''.'''.
                       ,">''  i<I:<~_!;<i<i<;~~-!!;+I!<I!++~<_-~l
                       '." .  I;,`"":``^^"^^",""'^`^'^^^^':^".
                       "`, .  !>;"ii~l,>li!i;++-l!,>:>>~!l_~<'
                      .l,:!!>i;ll!!!,II;!lI;:;I,,",";Ill;lIIl!I::;;;lI;I:,,,:;;;:;;I,"":;:;::;;;:,"",::::::;
                      ^}'!?+{-i??[-)!i<-?){>^il^```:?<{{!_-][{+'`^^^!:^'.. .'.''`'^?--]+[}{-]:^^`````^""""^]"
                      ^]''.`'````^~`''...^"""!l````''`^^^i>^''''''^^l:"<l!<!!-<~i<li_<Ii<-_;:,"^``````^^^"^?^
                      ^[`,,","","^~"`^^^"^^"^l;````^""""">i`^```""""<;^<i<~<~?-+i_!i~!I+~--^'.'''''``"""""^-"
                      ^]`^^^^^^``'!''''``^^^`I;''''```^^^ii'''''`^^^~:`--_:<>_~<--_l_>i]+:i~][,'''''`^^^^^`-"
                      `-""^^^^^''^<^''`"""""`!l````"""""";;````""""^>"^+~<<__~~<~+!l<-_i<>~_<<"`^^","""""^'_^
                      `~```"""""":~^`````^^^^>!``''''`^^^;I"`''''`^^>:"-~?i>-><l~~;i~+-:i~~_+~"`''''```^^"^?`
                      ^+``^""""""">^`````^^^^!;^`````^^^^!!^^`````^^<:;]-!l+<{<<->[_~i_+-!-;``^^^`````^"^"^}`
                      .l:;;;II;III!I;::,":;;;l::;,""":;;;lI:::,,"":;!II!!;:lI!!lil!ii:ii!;il:::;,;"""",:III~.
                   :[~ l:<<>~:+<~]_,]?<_i_+__^+>>-__lil;!,+~<+!_+>,_?~,>~-<i><:>~>+i<_>"l<_:<_;`?'~~l?,
                   ."` "`..''.^"^''.'`'`'`^''.^`^^`"'`'`..`^"`''^^'^`^'":""^""^,,":^,,:',,:^`,^.:'""`:`
                      ._?+-+_?l<}ll?<<~"<<-~+;-l<?-~,_:<+-?i~!
                        .,'. .;^``'""`;"'^^^^'`'''^'''^^"` ...
                       ;,i ' .<+>+~_~,~_,i+!ii:>:>>"><?~+,
                       '." . .l:"""""^I"'^"""^^"'^^:`"
                       ^., .  !<i~i~>"i~,l_!!i;>"><->i.
                   `:` "^::,::"`"`, ^^"'.' "".`'^^"' '."``''"'.^`""^" '`..
                   l_!.-![-_+i_>~<?!<~+l;~,+?li><-+;^>:_>>I`-__+>]]_];l?_I
                       <_~";~_>i>_:_+i<i++-"l_-l!?l.--`I_:_!
                       ,^``^"`^````"^^^'``^'`'``'^^.'^^"".`` .   .
                       ?[~-]<i<_<~"~_-i~;I]--[<+}~<,i;!?_,><_->ll{_?[~_[+~:
                        '"   .;,^"^''^^"'`.`',^"````":^.''^^''.  ...^.....
                       ;:i ' ^-++_-;:+<?i!^>^l<<><_il_>:<<~<~:
                       ''" . .;""^'`:":`^."'^,;':I,.``""^`
                       "', ' .~!>i;;~<~!l"i`!<+:!~>,><>i>;
                    "^ "^:,`":."^^"' '....^"'  ''  '.    .''`'.'.''`'`'..^.
                    +i._;-<>i>;_~<~!I__+!,?]i"---~>?><__~<<_?<`~_~i-l~?;`};
                       ;,"^,;^" ,^`"^,'^;"'"`"`'":` :;, ,,:' ::, ,,:' ^:," """,'.,""^ ^,""' '''.^^^^^
                      .i<l><~lI`i:i_ii`l]~:i!>;"i~!'>_+^<+?l,?_~^__-I'>_+~`___-;,]-_+`+}-]!"->>`<]?_?"
                      .,:iI^^l!::   ,!!:
                      .,:!!",iilI   :i!;
                    :^ ,,`!"::^';ll!.```"';;;^^":""""'^^^"^^"^'`"``^^^,` ^""
                   ._l Il:-l!>:.I>~<'><>i^!<i^I_~i!<i;+<>_!<>+,;+ii>i;+i'l+~
                      .I:l`I:^`l;:^^I:,.":l':;:'`,""^:`^''^l;:;;:,'^::`^`"^^:`^:;I:`"",:;;I^":,'^;"``^^^,^`.
                      '__-<<+>l~~_-!~>+i~<-;~-+!!_><<<>]li;+~+~+~!i-~~~}~i-__iI>I!>l~<i!>+>I>~~;+_-:l?>~_!]:
                      ^<i;:I___l,<i<~;,_+~l:!;i<~l!>?<>;~>>?_iI>i_+>i >!~~>>,iI~I;~++>>>_:>_~~!>_<,+_!+<<-_`
                      '<!<i~i`_>:?-~~;!<~i><'      .         .   .  .    ...   .. ..'...' .. .  .'.''.'.`^.
                      ." ^''`.^'.`^^`'`^^"`^.
                      `]+-]<_:~i~]i ":~;<}]{<!_~,
                      .`^`'`".`."". ..''.'''..`'.
                      ^+~+];l-_~>   !l













```

*Figure from page 10 (2346x3317 px)*


---



4203-E P-337



SECTION 3 DATA INPUT/OUTPUT OPERATION



3-3. Tape Format



3-3-1. Input Format



(1) ISO Coding System



rape file name-i (d) Program s;;ction



(,__--_---...__I



$-Filen _ame



_....__l---__._-l~...._l ~,.. .......



~ I



_o Pro_gram_name.........._l



..,..~..... .


# I..____,\

\~-'~Pro_g,am_end .........



~,-~I. _. ,--_--_---_-~



"'1- Program Start block--/ /-Program end block +-tJ- Feed holes -



(e) \



(b) Feed ho/ ""



(c) Tape start Program start



Tape end



Fig. 3-3 Input Format {ISO Coding System)



(2) EIA Coding System



(d) Program s;;ction

- Feed holes_j



(a) -,



Program start block-,



(b) Fe;d holes'/ • '



Program end block..k+- Feed holes - r-



(e) '\;



(c) Tape start



Tape end



Fig. 3-4 Input Format (EIA Coding System)



(a) Feed holes (in ISO coding: NUL or SPACE, in EIA coding: BLANK or SPACE)



(b) Input the file name after the "$" symbol.



If no file name is specified, the same file name as that specified for the output NC program name



will be automatically selected. If no output NC program name is specified, the name set will be



"A.MIN".



(c) Feed holes



(d) Start and end the program section with the% (ER} code.



(e) Always include M02 or M30, or END, or RTS in the program end block.



[Supplement] Codes that cannot be set in the EIA coding system can be replaced by codes that can be



set so that they can be read. For details, see Section 6, 3-3-3, "EIA Special Codes".


```text


                                                                                                ^```'" "''``'
                                                                .'..''...   . ..   .' '..  ... :[_+_i- ~l_]~^
                                                                i)?<>++_?;_.~_-_+i[{_><>__i>_+l>">~+_~-_~~+];
           .```````^^^``'```````'''''''''''''''.......''''......''''..'''.'.'''''''' `..''`...`..''.^'``.'`''
           .`"^,:::,"^^`"`^",,,"^,,,"""":;;;;;:,,",,,,:;;;::::III;IIIII;;,,,:IIIII;,::::;IIIII:::::;;I;;I;::'
           ^-^_`   <_il>^+!l;I;i!
           '!`!^   :i+i<^,,!::I_!
           ^;:""^  `;:,,;l,,,:;
           ^l;;""  `l_>l",!I;i!
                  '".  ,:".^^',^`';^^"^^'
                  ;!l .+_<:!<+]i?l~_~__>:

                         '          ..   .                                                   .
                         [;i~:<;l!l:~"   -;^"^"'``""""""^`' .i,;!ll:!l!`  ^",^^^^^^:,","`"";?^
                  .l,::,,+,,;::,":;:<l,:I<"!:l"I:""""",",:I,II,l;;,::;,I;:::l:"",,,,:l;II:!,~:^",,,"^",`
                  !!^^^^,?.>!;Ill. ._I""I1-{?(?+::I;ll":lI?_-{l+...'`++,'''.-"l;I;";:<?-(!}<-;^",,""""iI
                  >:"^"";["I;:;;;^"^-;""l]-{){[_,;;lil,;l:_{-{>~`'''^>~"''''_`I!iI:!;+([|+_{}:",""^",">:
                ^`':,,:I>~""^^^^``""~l,:><;~^-:+I"::,::,:";;;:i>^"^^^'',"^^"_,^^^""",l;;:l+`_::;::::,::^
                ";]i;:lIlI       '.'<!,:!i-l +>?, ^IiiI:>;;!;^!:            ~">+>!,;!:Il^>-_-,"!!:!>^:^
                  :             .i;liIIl<;.    ^:"                            "^           "l
                                       ;"       .,",^""`""'                                 ;:`''`.
                               "!;<lI<I.           :IiI,l!^                                  ;<Il!'
                                . .  .
                                            ^^. ^.` `'..'"'.'.'.'^``.^..`. .` .. ..
                                            !<}`~l_.>_~_!<>+~<}!>-->;~<_]~[l]_--+<<
                   .   '.. .     ..           .                           '  .    .
                  ![! ^}~~I+~+_<?!}_--~<'
                  ...       ...." '`.'.
                                        "                                                   .
                                        -l""",,,,^^^,:,,," `i:IiII:>l>'    ,,,,:,,,,"`^,"";],
                   ,:"::l:^",,,^":::,"::I`,^,^^^^""""^^^^"'^,^^""^^^^'^"^`^"""^^^^^^^""`^^`i,``''''`''
                   _:^",]`!iI;lI`^^~l",:1_])]"^",,,,""""^_)+<^"^^^"";+<,,""!-":,,,,"::i|?{~?!,,,,,:::ll
                  '?""":] ;:,,;:.  ~;`^:n}]j1 ^I;!li,l!I _r];       l[,    ;< ";iiI:i'"x\|t-;'.``''`'~:
                   ^,^^">,"":,,,I;;<;;;;~;<~>:,"^^,:":",,~-+!::::III!i>:::;<~I;::"",,:<}[?+-l;;,,:,:;i:
              ";"ll,:!,!-          !l^^!<;-"~,",::"";":,"`^i"              ;>'""","",,,^">.~:'^^^^^^'`.
              .',-,^^:^,<       '''<I""l[_+"-^^,lI",l":;,^,<"              l+'->l;,;;;Ill)+[I.:!l:!i',,
                                i:l!,;li!                                     `           ;:
                                ^I"~!I<I                                                 :~!I>,
                                 . '...
                                            '.  .        '       .   .
                                           .~~['+I_.>_+~!~~-<<[;--+~l~>-~+>i[~_]~_l
                                              '       .    .  . .        .` '' .  .
                    !-I`_~+_><i>+!l~:+]~I><+-<~^-<<;"<"?_-_i]:">"+<~,>!_<<;I},<+?+^<"+_+~!?<'
                    ''.  .'' ...`.''  '..'.'``: `.`' ` '.."^"^'^'`^^`,":,!:':""":"`:.:,^,,::.
                    l<:'~iI!l<>;>~;;<<ii^~}>"<!i^-l^>l!>li
                    ^:^ ,;""^^,^`,^'::",.:::.",: :`.I:^;:,
                       `>`i,i+::<>!i^l"<i>I~<>,:~!:i<l!:l<I:i<l>"~II<<i;~>il~i>I!:l~i"II+i>;<+::lI>iil;:!II!.
                       '!+i!l:>l_<i<_+>-~l>>~<i>i<'~+!i:!i-l<<~-!i~li~<<+l<>>+!l!;!<<!-~]l~<i!l<>i_>+~Ii]>>~'
                       `_~!~]l<II;:IiI!Il"I!;l;ll: ,^,;`l;~!l";!,:i;>>!!,^Ii;i,ll:~i!!i<i`,>i^><ll::<i"<<:>i.
                        ;!<~~~'
                    .' .`     .'..
                    l~;^<~__!<+--!

                    >};'1]-_![~+i+_~<?~I-<___-iI-~~++>l-[>!-+:_:![~?:~~?[,
                                     . ...``.   '. ..  ..  .'  ..'   '.'.
                    <-:']_~_~~;>>~<]ii1_-,i"+]]_'l!i?_-l`<,<-<-"i,_<lI>l<i<>Il!>!l+!~>
                    '^  '''`"^'`^`^`' ^'' ^ .``` '.'''"' ^ .' ^.`.^"`"^^l",^`^`"'`,^,"
                ^]+!>!+>!>l<l   .l;!>i:il>"ll;;;I!!"!i,;li!;i!l":;l,;,I:I;:^^:;,l:,;:;I:!::;":;!!I;l;l";l,I;
                'I::I:;:";"::   'i~i<>!+<_!_~iIii>>!~i!!i!l<<iI><~<<~;-~>~_l!+<I~~:_~<+>>_>?!+~~+~ii+_!?_l<!
                                '<<"iI:<<>lii+^!~;^<I^<>>, IlI'+<_~+:^+~l:_+<~iI;<'>;i;! <i<:i]><I~;;!<-~+`






















```

*Figure from page 11 (2346x3317 px)*


---



4203-E P-338



SECTION 3 DATA INPUT/OUTPUT OPERATION



3-3-2. Output Format



(1) ISO Code



Feed hofes File name Feed holes Part program Feed holes



(a) (b) (c) (d) (e) (t)



Fig. 3-5 Output Format (ISO Code)



(2) EIA Code



..__?---___._--,_ $fllenam_e


#### L--...Jl----1--L...L~,~,

_OProgra-mname .J.::..1-IRI _---J?....__{ ---1...IR...L...------_---- .



Feed holes File name Feed holes Part program Feed holes



(a) (b) {c) (d) (e) (t)



Fig. 3-6 Output Format (EIA Code) (1)



(a) 600 tape feed holes are punched in the tape leader section.



The number of feed holes to be punched out can range, as needed, from 1 to 10000 with a



parameter.



For details, consult III, "PARAMETERS".



(b) The file name is punched out following the"$" code. (Program data is punched out in the ISO



coding system.)



(c) 50 tape feed holes are punched out.



The number of the tape feed holes cannot be changed.



(d) Either of the following is punched out.



%, CR, and LF



ER and EOB



{e) The part program data is punched out following the program name (number).



(f) The same number of tape feed holes as in a} are punched out in the tape trailing sectlon.


```text


                                                                                              ."^^``" ,'^^".
                                                               '''.`'.'. . ..'' ...' '..  ''' ;?-?-<+ ~;_-[;
                                                               <1~><~~-+I>'__-_<i]?+<>>_+i+~_<!`<++]--+<+>?;
          '^^^^`'''````^^^^^^^`''''``````''''''''''''''''''....''''..'.'''.''..''''.`.'''' ..`..`'.`.''.'''.
          '"",",""^^^`^",,""""^"""":;;;;;,,:,""""""""";;;;:,,,,;;;;;;;;;:::::::;IIII;I;,:,:::;IIIII;;:,,:,,'
          :illi^  ,~l+i!I!l!ll~:
          ^:,",`  .,;!;,^`":^"!"
                 ,I^  !!I^I::i`
                 :I: .i>l"lli_I

                 ,,""""",,"^^",","^^""""""^`'``'^```^^`^^``'`'^``^^^^^^^^````^'.````````'''''``````````'
                ._,^^^^^~_^::":::,""+~,:,]I>_!];[","",^""i-!?l_:",::::;::,,,,:l_!",,,,"<+I[I-I"""""""""`
                ;l`'.'.'lI lI,,lI   !!'^'-|]1~-??::IlI::I<(_<[_               ~>       ,[_~]+".`'''.''''
                "<",:"",~<:,^^^^":::?>,,^]:<?-+~],,:;:::,<]~]<[,^^^"","^^^""",~_"^^^",">-+-<+:"^^^^^^""'
                .:,,,:,'::'"I"",,``',;:,"I^'.'`^l`^^^^^```.'"`"^`^;:":,""`^"^^ '````^^^^'.^.I`,:,"""^''.
                .l}~i~<:?-"I->>~>,":_[~i-)+""^"i?,^'`^^^^^^^``'''`><i+__~"`'''^^^^`'''''`"^:_,;++!~-i^:.
                  ..:>.'<l'' ."<''`^]",<`-^`"_"I~^'''''`````'''''' .'`>"'``''``````'''''`^^"-"...ll'``".
                    .'  '      '    ^  ' ^   ' .`                     ^                     "    ''

                                              ^>i:`il;'<I>iIIIl;;I>::><i,!;I>l'
                                              '"il';:,.;I>>I:^:;,;<:;l!I"I;l<>'
                 ,i^ ^i;;^I,II.
                 !~: ^>ll,ii~+^

                 ^+::;II,l<I;,:;;;;:I<!:,,i;i!iI"""",:,"":!;;I:;:,"",;;::,,,:::^:::"""""::I,:,",,,"^^^,"
                 !I''''`'>!'!;,I;: .._l`^`]1_()I,;:,:,":;`?\]>'`'''''````''`^`I~>`^`````^^})~!^""""^^^""
                 _"^```^`_!':,"::"   ~:'``[)[/t^,,,I;"";;.-f1;                I_"         ]f];``'`'''...
                 I;:,^,;:<!":""",:;:,~;,"^~I?+]!,,,"",;:::-+_>;:,,"":,""",^",:I>>:;;;;::::]?]>"^^","",;:
                ">~i;>i..!l.l<IliI..'i~l;~~'  i"..........       .ll;li!l.  ..   .........  l"`!!I!il.'.
                lI;I~I;,:[_::;I~>I::!{+i>~1l<i{<:::::::,::;;::,,,,;IIi~I;::::::,,,,,^^"""",I]>:l~I;!l,;I
                    ;    ,'    ,^    l `; l l'I.                     ,;                   ..>". !^   .''


                                             >!<'>l+'i>!~II;il!!><^_>~:l!!i>":i^
                                             '`> "^: ^:,l:"'':,"II'l::^^:;Ii",;"
                   ,!^'~i!,!II"I;;;;;;ll`;I"::,"::,","';,',;,`^,"":`',",,^'
                   I~,'<lI"i<!^,l!l^l;!i`<!:lii!l!il;;^!~"l-~l:>~i<;,+i!i!l
                      .iIl `":I!!"'>^i;;!'Ilil',,'l:';,l:l;;`^::.,;,.,I,;I ,!`"I;;l;l l;;l.:'l^`!!!!l';!l':'
                      'i>~;!<_<~!"^l'lllI`Ilii^:I^il:ili!I!i":!l`li;'l>l]<';~"^iii!ii'Ili!.,'<:'i>><!'>>i`>"
                      ^<i;+;i<~;
                      ^l,^`ll;lI.:IIl;!:l<``i!i>li<+!<i>ii`
                      `"I""ii>i!':!Iii!"I>^ ;I!lli<>,I!lil.
                   :;' l""'I^ `^"^.`..'^`^""`..`'^^`'^^' ","'I,'^`,^ .;,^``^^`',^^'^.''`'"''`''`'''"'.","'
                   i~, >i_;_+:i-~<i!>i><i~>_!;i~;<_<>-<+_~_+'-I"~i+<.,-!i[+~+i;}?-l~;><~i+~~!!<+I!;_~;<?<:
                      ^>i<>_Ii_<_+>l:
                           .. '
                   !_,^]>l]~_l-?_<i>--~,+<;<>i<+~_>I+-"
                   '`.."`.^"''^^`'.^^^`'^''",'``""`'^^.         .
                      '!<_,+i>-+-"<i<~~l-~-:_-_>l___<:~]<>_<>]I!<+~_[-<
                                                       .  .  . . ..`^..
                   <},:]?<_l,?i]_;__+~-!+!il!<ii~~++I<~"
                   ''. '..'..^''^^"`'`^`";^'``''''^'.``.
                             "-.I+-^!~<l:<,
                             ";!`,^,:l:ll
                             l<i,+i!;<l<>
                   ,:'.;""'",^.`^'`^^`."^:`"'```^:"^"'^"",:"^""`',^''``'`^^''^^``.^''`^```
                   ><^.:I>:<~II~l--<~l:-__;>:<>l!<~~!;<<I_+><~<]!<+l!ii]<_+II?-i~,+!<<+_~i`
                    " .".  . .' . .. .  '.. . '   . ..          .      .        .         ..     .
                   :}"'><_;-]>-l!<+<~];l_i[??;-_-_!--]_:?<i<;},_~>l?~>_~]+;_+liI~~il{-?l?-]~++l?~_~~!
                                                                                    ..      .` .






















```

*Figure from page 12 (2346x3317 px)*


---



4203-E P-339



SECTION 3 DATA INPUT/OUTPUT OPERATION



[Supplement] 1. When the program data is punched out in the EIA code, the presence of a code not



available in the EIA coding system causes an error. Tape punching-out halts and



an error message is given on the display screen.



When the tape delimiting code is the "%" (ER) code, i.e., when bit 3 of parameter



No. 1 of NC optional parameter (bit) is 1, the"%" code or "ER" is punched out before



feed holes.


## 2. The part program is split and punched out, if it si

too



long to be contained in one



paper tape roll. Paper tape length may be changed from 1 to 300 meters (3 to 984



feed) using the NC optional parameter (word) No. 2.



As the format, the file name is also punched out, for the second tape and so on.



Since the tape ends with "CR" or "LF'', actual tape length is somewhat difference



from the tape length set using the parameter.



When designating paper tape punch out operation on more than one paper taper



roll, specify option D in the following format:



<file-name>, <device-name>:;D



0 0 0


# $A.MIN

0000 00



o/o~Hf)o*"'** . \ \ ..



000000 1st tape



File I Feed



Feed I



.Feed holes ~-name,



?Oles



Tape length for parameter setting. holes .



. { ·.___-_®_~_-_···._ ,,_·__.I 2nd tape



\ \ \f.)



'------------------



~ ~



0 C



$A.MIN



Machining program



Fig. 3-7 Output Format (EIA Code) (2)



3-3-3. EIA Special Codes



(1) There are some characters, such as"=" and"*"· that are not represented by codes in the EIA



coding system. To make it possible to use these characters when creating an EIA program



tape, other characters are sometfmes temporarily substituted for them.



(2) When a program tape created in this way is read into the NC, the substituted characters must



be converted back to "=" and "*" by using editing functions.



(3) This troublesome procedure is made easier by setting EIA special codes for the characters for



which substitution is necessary in advance; the control then automatically substitutes the



appropriate characters when a program is input from or output to tape.



{a) Setting the EIA special codes



1) Special codes can be set for the following 6 characters:



=, *· [, ), $, #


```text


                                                                                                ^"^^': ,``^"'
                                                                .'.'''.'. . . ... ..' '... .'' ,_]-]>-.<;~?[l
                                                                >{~<i>_-];+.~+-<_!]-~~~<~-<i++<<">__?_-_<+~?I
           .``````^`````````^````''''''''````````````'''''''''''''''''''.'''``'''`''.`..''`...`''''.`'`''''''
           ':::::,"^^^^^^``"";;;:"",,^``^,:,,::,:,:,,:"``,::::::,,,,::,"""^,,::::::,::""""^""::::;:;:;:"^"^"'
                 "_!lil!ll!!~.   ^,  ;+>I;`!I,:I,;;;;^:li,:,,,::II;l,:::::!:,iII^;:!^'l:^:;:,:,:;`I:"^,,l^"::
                 ,!lli;I:;!I!'   '"  I~i_<!<<!_i_]!-~>l~_+<>>>i><~+il~i!ii<>!<<>!~!+?:><l~<<~+i>>Ii!<!<++I!<!
                                     ;<i<i]i>,!^~i:!!<,lI+><>;_>~i!":i>l>~"l>^ilii  +-+>IiI<>i><<lii;>-?ll~>l
                                     !-^i~>>`>++<++-+,_;]i~<,<i:_+:i-__-+"~ii~~!                .
                                     ^,^``'"''^```^;^^^";``'.`'.`^'^`":";',":^`'..       .        .
                                     i-<-_;+~i!}+<"~_+i>-!+,>>>_:~,~_,"_:.]+-<,i<]i':+.^-<~!"~<;i;+l++~+!~+<:
                                     l~l ;;!>+iI_+~>!+>>_<]~~~+!!]_l>Il`?<>I~l:>i?+:<:->?:~!!l>!!<>!><<><]<~I
                                     !_<!I<!i~;'::""^:,:;,:":,:^";:""^``,," ,`.:,I;^: ,"^.:;;:::";;^:;,,I:;:,
                                     "!Ii"I:!i,
                                 "^  ":` .`^^.^^^^""^^^'^,:'"^^'^`^^"^"```` :^'``^`''``''`.``.'``^^^````'.`'.
                                 il  "<<;I--!<~>]-+_iI>:]_~,_~iI+~i<i+~;>_i"~l;<:<_!,~>[;~:>-:!ii+->__l!;;<<I
                                     !i<~<"__<,;<+ l!-~_^<_<ll+!~[;"i<<,<I:<i>!~<>!<<+:I!<l[]~;<~~<>:~><l~}_l
                                     ~-+_>"~-<<!_~I+_<l~+-+<_I<<+~<<___,_~>!]l?]::<'``. '^'^^''`"^^`'"'^``^^'
                                     `:":^.:^^l``;`",`';;:^^;';:^,",;:^.;:,^l`^:`.:
                                     !~"!>i:<!l!_ Iil"-i.:!!!!"!^+>l'Ili;!li,:II i!^<>l,iill>!;~i>^ll!"II`I;
                                     i-!l>;><I>><!,<i!!l!_+:~<_>,~I<l-l;~>~><l_>l;+Il<-:~lii>i!_]~i!<[>i<l!!"
                                     i<!<>l>iIi+><I<;_!,<~I.I!i';i'"!:'"+><i~"~<<,!>l]>"i:liIl<i!i_"<<<!>>;<;
                                     lIlI"+>:!-<i:+;+_;;~i^>>l~l!<>l~_~+I~<~:
                                     "l:^, "^`"^^",^^.^^^^`^"`,```^^,.`^^`^^^^:^^'`^.^^^^'"^^''^`''```^'^''`.
                                     !->~~"<~_?]>-+>?l_?__!I[[+l~~<ii:>_>l-~<<]<~:l<:>>~_I>~-;l~+!>+[__,+?_]"
                                     ;!i <-_<!<"++_<i:<,i"-~;<_+!~<<~!+!i~[:
                                      ..!"`'`;l"":","^'.`:,",^"^",,:I'^:''`.
                                        !^"'"~+>,>~l<i".l~~!>>!I~<i-!,i-`
                                     .'' ''''  .''.'''`^'''''''`'....'"^^`````' .``````'.``''``'```'`
                                     +""^^""""""^``^`'":"",,,,:^,>i:l"`````^",; ""^^""":<:Ii,^^`^^^^i<
                                    .~  ''..' . l?l>]-; '^```'"-,\}_}_<;::;.  ^ `      -|>-[;"^^^^' :<l-l<?+I
                                    '+''^^`^^``':>,:I!:'`''''^^l;{[<}<l:,,:^'';.^,`'`''<1!>_,^'...''l>';`"l;^
                                    .l"^`^"^^`^,I^_-~^`;l--_?ll""`.`"''````'"``  ^`''^`..''`l"-[]]<:I:
                                    ',!+~~li>_i'l ~1\+l ;{)/|",.i++<;?<+-;i_^i-<_i~_+"!+?++II -1/(! 'I
                                    '_>i+<!<<<<i-ll<i<~!<~ii<i~I:~_iI<i_i;l>:i~i>li><:i><i~?<l>~<~l:>:
                                                .
                                     ^^""^^""",^^""^",""^"""""^^^"""^",^^"^^^"` ',,,",,"^""^"",,,:,";^
                                    ^-`^`'````"^^^^"`^``````````````'``''``''," ^``````,_ll~,`^```^`!~:,^'^'`
                                    "~ ``.'.` :{>~[[I .'.'.                  .^ ^      ;/?-1l.      ^>+__;]]-`
                                    "-`^^`^^^``^^^``^`^^^^^```^^^^^``^^`^^^^^^I.^;""^^^,+i;+:^^^^^^"l+
                                     ,"`^^^""^^`^^`^"^"""""^";""""^^`^'.'`'''''  .'''^^`''``l"^^"^^^"'
                                                            'l       i]-+_~<_<I_<_>_~^      i.
                                                            .!;^^^^^`,;lI:;:li;;:<;l;,^^^^`;>.
                                              ^"' `'`.^^'`.''^.'`'`.^`'..' '   '
                                              I>[`<!l.i~<[<<I>i>i<[:]><!l>~?_ll]!
           ... '   '`. '.     .. .
           l<<i?"  >-?!>)?_<]+i~<-]-'
                       .'                              .
                  l<I .!!+il:_>,>~><>:<<+>>>+ii ~iil`+i`;^,~iI`l;'<<+!l~!^!>::_>i~>>!~ii!~^I!>+~"!"<iI!_-l
                  '.' .Il~<<Il>!~><I'l~,<<]>!llli>i+!<Il":>i;~:i!,I>~iii~!il;i~+!;>~i_~il<>I-<?!!!li>~i:"`
                      ^+>>!i+~->l><!^;il!~<~l;I~i<<_<>;<:~_>:i><-!;ii~i~~<<I!_!<!:!>>il<<:i^l;l:<;>+!<l.
                      `~_<I.>~ii'!l+>+!_>!^~i;I<li<!,>~ll+!<~!!~i_">>~<~<!_~;!>^<i<!;
                  '".  '^..'    .   . .      .'     '.           .... '  '.'  .      '. . . .    .   .
                  i[I ^-_+-:I<><>[~~~:~[_+;~+_]+-!>:~<+;_+_^~"~~_i!<_:~_il-+:>]_;-++-[+~?_l>__<__[++;~<>[:
                      "+i:~~><_~<-li_~~l_^;I"-<+::!">_,!+<-l>+?->~l+>>+~!>! .    .... .... . . .... . ...
                      .^' `'.''.'' .`'' `    ^'^  ` .: `'.^^'"'`': ``'^`''^
                  !]; .>i<">l;iiil!ll!"!I!ll<;l^l""!!i>^i!!il"!,"I!+;;^<li'<li;!i^;I<l:l!^ii;`!l!IlllI;:<I
                  ";^ .!>~iili~~+_i<i<I<;!~<<<>liI">!+~I_+>+II?<,<i~~_!~+il<~>><~I_<~_i:<:~<~!i~+l-~~;:"l:
                      '~l!i:I<>~~<>iii"i;:~i~<>~i>^l"~>!+il<;;i>,!!l+!!l>i>'iI>l!i~!i<>;l<~<<~i<>:i<<
                      `?__i>_>-]I:i>+<-~-<;I_~~::!ii<-<_<;>!!~~~l~~i!^<,l>[?>!iil]i+,
                       .'  .      . .             '  ^..   . .'.  ..  . ..''. ...''..
                    i]l.--]_i+!?+:?~_:-__i<<:<~]<!
                    '`' ,^.:,;^^"^`^^,,"^^,^",^","`'."'.^`^.''. ''.`....`...
                       .<: i]<-i-~;~~-~;:+~'~~,_-:<~:[_l<?]>?~~_>~!~+_+_?_<~
                                  ., ;':,;`] ~'                '
                                  ."',`"":`!':.
















```

*Figure from page 13 (2346x3317 px)*


---



4203-E P-340



SECTION 3 DATA INPUT/OUTPUT OPERATION



2) Special codes are set as bit patterns in NC optional parameters (bit) No. 27 through 31



and No. 49.



Example: Suppose the puncher key



[Supplement]



"[ ]" is determined for punching the "=" code, and



that the arrangement of punched holes by this key operation is as below.



8 7 6 5 4 3 2 1 Channel



0 00



Feed holes



Set this arrangement of punched holes by a "1" and a "O", where "1" indicating a



punched hole and "O" a position not punched. Setting will be as below:



01011011



Set this at the No. 27 of NC optional parameter (bit). Repeating the same



operations, set all the codes used on the NC.


## 1. When inputtlng a program in the EIA coding system, if the special code"$" is input

at the head of the program, the character string immediately following the "$" is



read as the file name {in EIA codes) for the program.


## 2. When outputting a program using the EIA coding system, if the "$" special code is

set the file name will be punched out in EIA codes. If the"$" special code is not set,



the file name will be punched out in ISO codes.


## 3. There is no check to determine whether or not the bit patterns assigned to special

codes already represent characters in the EIA coding system.



Example: If the special code for the character "=" is set as 01100001 (the EIA



code for "A") and "A=B" is output for punching, what will actually be



punched is "AAB". When the tape is read, the data will be



interpreted as "==B".


## 4. Special codes are only converted when commands are executed ln the PIP mode.

They are not converted in the ONG mode.



3-4. Specifications



3-4-1. RS232C Interface



(1) Communication Method



Start-stop synchronization



This is a method in which a pre-determined signal is sent at the beginning and end of a character.



The data for each character comprises the following bits (see Fig. 6-8): (A) start bit (1 bit), (B)



information bits (8 bits), (C} parity bit (1 bit), (D) stop bit (2 bits).


#### LSB MSB

7 1-


# I ·---1

1----



------1



1s -1I ,_.___:


#### L-..J ______________ __.1...-,1.___ _. .,

(A) (8) (C) (D)



Fig. 3-8 Bit Configuration


```text


                                                                                               ^```', ^'''`'
                                                               .. ... .    . ..    ' . .  ... ;[--?i} ~I~?_!
                                                               i1?>><_-];_._+-<~!?1~<~i__i>_+<<"<-_-+-_>++[l
           ''''''''''''``''``''..''''''''''''.'''''''''''''''..'```'.`'`'`.`'..'''' ^.''`` ..`..`'.^'``.'``'
          ':,,,,,,""":;,:;;,,"^^`"^^^",:,,:,"""";:,;:,,::::::"^^,:::::::;::"^"^^""""":;:,:;"""",,:;,;:,::::^
                       lI 'i;I::;^,"l!;`ll";l;"l^I!^;liI:I,,;:>!^,;l::;:`;;:;:;I::^";l^;l^ l;"!"""^l`:I.
                       II ,[]?_{-"_(_il"ii:!<;I~,!>;<<<<Iil;!:>!"l<i!!>!I~~!<l<>i!II><;I_!'<;,+l!<-],!>`
                          ^!:;,i; :<"
                              ?i+_<<_~. <-~_~<+~;[<:<>!i<~<^<~i`l!^i;i?~+>>~!~<l~I"<i!i<><:>>>^;:`il>> ;+<l
                               '`''^''  ?_}_-?~i_i]~?[__-?+:?<]<__<_+<_<]-l~-i]~_>-[i!??+?)++>i!!+>+-}<]I"`
                                        `'^''^`'"."`;:^^"^`'``,:`^"""'``",``I'^""`:;^^I;"":,"',",l',:,:;
                                                            .
                                                       . ~;'> _.l< -   _^^~ <`  !><<l_"
                                                       <"                     i^''``'^.
                                                       ~^  ^I   ;``; ,.  `` :.<`
                                                       +^  "<   <,"<.i::,~<'~.i.
                                                       +.               '^,I,,-^.
                                                       ]::::"":;;"^^`^,:,"^":I-",:,',,""^^""
                                                       l"'     .'^^^^^`.          '.I>~iIi<<.

                                        !ilII;"ll;lIil;lll:!lI,;I!lII;I!;;I",^"",l";:"!! :I;,;"^:`,;l"Il,::"
                                        _?+~+-+]_-{}][~]~[~>~___[[?-l_?--<?_?<i!,[--}>~!I{]-]+l!I!_[?-+iI-i;
                                        il:lI!!;"!li`>Il ;^`;Il!l!;:`l!,!IlI;><! ">!ii~I!<!,~:I_,i>!l>`
                                            i^:;:, ";:^.l
                                        !!;"<::'!^i;":i: "!"^;^i!"^,I;:"I'":,:::I;,'I;I. ll::::l:,`;:"',,":`
                                        ~[?!]]-l);~[];{]I_-,>~i[];<[[]~_]i]?+)}_~~!`~><" !<_~~~_i-l!<!^++l-;
                                        :ii;;iI;!:'~>^<:Ill^!I>il^i>>I^>'Iil`>i`
                ;<;I;illl;I>    :'  Ii;:,`""":;"^`"'""^",:`^`:,^"I,"'^,:"^.^^"",".I:;"^,","",`"^;^^l""^^^`^`
                ;ii~i>>l>iI+.   :`  i+<_il<+~_~i}>~<<!]<~_Ii;>~<l<~il~+_i]l--~~<>"<l<+I]_+>_~;<!-i'}"!i!_<>:
                                    <;:~i'i~>i"il!<>,<l~_i_i',i~^l!+>~>~i ~~l!>^>>l<~~-++_^+<~<_i<<i?_.>_.+:
                                    i-_~l?l_-~I{+:<-~-!!];?<?;><?]_ii?I--<;+<~]~~<`.. ...'  . ...'^. '  . ..
                                    .'`. "...' .' .^'''.. ... '''^`' ^ .``'^'":``.
                                +"  ~+!>l'lI~ll~!i:I"l:!>l!l"!!;!"<l:!l>`;;!!;:I;l<!i^"i>i!`-;,!!l;!:,l;>"l"
                                ,'  !<i~<l__+i<+>~!<_~i+~i!!!~<i_!i<l>-<ili<<~~:]+-+!<>I<<+,-;I-+_l<;l<<~!~^
                                    >+li_iI~i;~<l<;~+I>il<!!>iii;i>I!i+!i;i!<>I !;!+`li`_><><<;>!+IIlIiiI_>.
                                    >>!i[>"+-i~"<-ll_;<>i<_~_iI+_,!:+]>">~~--'
                                .   ''         .    . .          .          ..
                                _"  i<+>>:<:il;!<~<;+;I?~_>>~!>:~>~[<?I:>:i!l?<l!~:>~__>!!!]+~-<~+l+l<-+<~]:
                                    !i+_+:_<<~~+:i_i<~<<~!l~<i+i-<~;>Ii_<i__!Ii>+i>I+<-+>>^"^`;'`^.`'`,```".
                                    ;:,;;^I":;:!""l;";::"^,":::;I;:^"'";:"":^";;;;i`Illl:,.
                                   .-<++i+~<  .>!+<"_<-<+_"ii+iI+;l?+"+>~i+<->'"^`<"<-:i>"<i>_+_->^<~~:]~_^
                                     ... '..  ^>>--;?~"-+iI?<~;]!~{^~!ii?_+><?,><<<<]+~:!-<-ii]]I-~]-[_!?-'
                                              ^_!>~>~>;<::-]1-. ??~~~l--<-]_~i_!?]]+I}}l<[[?l?[i~]"^"`,'^"
                                              "?}?_<_[--li_;<i<];^',`'`^``:,,',.^,:^'""`^,:"`:^',,
                                               .^^^^'""^."^  '^^
                                ~` .-~_<~?!!>~?~:>>;li>;I!i!<>~~il~~+i,!i<>i+<i_:<~lI<<>!_<>li;~>l~_?:>>i_!
                                '.  ;l,^^,^^^":,^""^"":"":"":""I:":^;^`,"^"^:"",`,,^^,,,,;::`^`":"`^"."::;,
                                    i~--:+_!;+~I+<><+>-+IiI>_~;~?-I;++-[,
                                       .                             ...
          <-l].  ^){?]+])+-{?_~-i
          '' `    ^I^^^'`^""'`'`'
          !li:!.  i?_~+__l;i~~++i+`
          `''''.   '"^``'. '``.^'^
                 Ii^ ^il!!!lI!ll~l!"~+<+lii
                 ",^ `;;,:":;":;I;,':II:,;,
                     "_~~l:+!+^!il!ill!~~-<i:
                     `~i>^l:II;!<!llll"i!l!I"^":"';,:",::","^,,":""'"","^,,:"`,"^"^""^'^^"`,^,'"^`.,^^^`^"`
                     '>l<"i"!"!ii!!iI!^<;Ii:lIi~!^~i<iIii><;!+?!_:<,i~iIi>Ii>"~+-~l>!_i>!>:~l<;<:~:_i+<+~_!
                     '~i!'_+_;"<^^><>;^ilii~>~: !lIi!ii>:,!i^!<~I>:!l,++,"<!>"<>< +:?!.i-";+i>:i~^l^;_~''--'
                     :+]->-{[+_l__[l1>_?]+"]?>>_??_>[+>~i_[!:]]l-{_<+[<-+~1}]"'"I."`," ,"^`::"'",'".^;:`';;.
                     '^`^'`,^^".^^,.,'^^`` .`',:"^;.,^^`',:^`:"',:I^';':^^,,^
                                        lI?-.                               ~<~-^
                            .,,,,,"    ^?}1(l,::,:,,:,:,:,,,""^^^""^""""""":1][{;``^^^^^^^^^^^`^^`:
                             ""","-`   }^''"{,^^I[,"^i[,^"~~"`^+!"'"?;"^:[,^ ,<.^^><,::]!:,,]:",,"+
                                  ~'   ] >^ ? <> _ l~^+ +^:I -^i``] + '< + <!`<   I:   ^    i
                                  ?'   } :`'] ;:^- ,;"~ !`ll !'i`'i +  ,.- l:^i   I;        <
                                  >I;;I]:^^;-:""!+::,>~:""<>:^"_!:";_llIi};,,!~:;;>'        !    :]
                                  "<;;l>!;II:;;I;:;::,,,:;:":;;:;III;l;II;Ill><I:;il:,"^^,";"    ',
                                  .`![I'^`^^^````^`'''`'`^,{-^^^^^^^^"`^^^^^^^^"~]I",",-];""'
                                    '`.                    ^`                   ^^.    ""
                                                   `   . . .  '  .
                                                  `+-_^_>~`{-;~~~_?-<+{__:
                                                    '`         .  '`.....









```

*Figure from page 14 (2346x3317 px)*


---



4203-E P-341



SECTION 3 DATA INPUT/OUTPUT OPERATION



(2) Baud Rate (BPS - baud)



110,150,200,300,600, 1200,2400,4800,9600, 19200



(3) Data Configuration



Start bit 1 bit



Data bits 8 bits



Parity bit 1 bit or absent (selected by parameter setting)



Stop bits 1 bit or 2 bits (selected by parameter setting)



(4) Parity Check {character parity)



Odd/even parity or no parity check (selected by parameter setting)



(5) Signal Descriptions



Signal



Direction Details



Name



Protective grounding



TXD Output Send data



Data line from the NC to peripheral devices.


#### RXD Input Send data

Data line from peripheral device to the NC.



RTS Output Request to send



Comes ON when data transmission or reception starts.



Thereafter, it is normally ON.



CTS Input Clear to send



When this signal is OFF, data is not output from the NC.



Used for BUSY/READY control.



If this signal is not used, connect the RTS signal at the NC.



DSR Input Data set ready



Indicates that the peripheral device is in the communication en-



abled status.



If this signal goes OFF during data communication, an error will



occur at the NC.



This signal cannot be used to execute BUSY/READY control.



If this signal is not used, connect it to DTR at the NC side.



SG Connection for signals



RG1 Output Data request (register 1)



This signal is used to execute receive BUSY control at the NC side.



It comes ON when the NC is in the reception enabled status and data



transfer from a peripheral device is requested.



It goes OFF on reception of a start bit from the peripheral device (it



goes OFF once per character).


#### RG1__j\J

High



Low



(output) I


# RXD Fl R High

(input)



Low


# I I

Start bit Stop bit



RG2 Output Register 2



Presently not used.


```text


                                                                                               ."^^`'` "''``
                                                                ....''...   . ..   .. ' .  '.. l}-??>~ +;~_<'
                                                                +}-<>_+__;<`__-_<<}?<<~<_~i><~~~^<~___-+i~~[I
           .````'''`'''``````^`'''''''''````'......'''''........'`''..'''''.'..'''''.`...'` ..`..`'.'.''.'``.
           `::::,,"^^,"`^"":,""^"^`^`^,:,,:,",",,,,;;;;;::::IIIII;;IIIIII;;:,,,:,:IIII;,,,,::IIIII;;,:::::;;`
                  "+I  -<I!:!~i>^<-!~l.`l!:!!
                  ,!:  Illl"^I!!^l!^:,.'I!Ill
                       ;!+`"+-l'?++'>_]::]_> !_-]:;_+]-'<[-]l:{??-':_]--<
                       '.'. ^`'''.` '``''"^^..^`^''``"".`,""^':"",'.",""^
                  l}< `-~_+;>i<]-+l~]><:
                  .'' .I:,:^",'.",'`^'`. .'.`'
                      .~<~!I<l        '  '::+,
                      '<l>!,i<I       '  ">;i~"
                      .~!!>"lil       .  ^!;i>"..'...... .. . ..         .    ..
                      '>ll><^>l       '  ',;+^!:!]~_+-:<-~_>~_!;-;>+<>+i~--^~_-+~{l
                      .~+ilI<<:       '  `;;<"l:Il!>i^ii>lI>!lIl,l>l!!l!>I^;i~I;l:
                       ;III`lI"           '"l.,`""Ili">i!!lii;;<,!<l>!!><l^i>>Ii+.
                  :-l '>ll<l"il<i>^!+ii!!><:"!!!i:
                  "I, .":;;l',"l:,'I;;I;I;!`,lI,>:
                      '<~-~~><<">-~~i"_">l:+<i-,l><<]"+-?_~-_>I+;!~<<~<_?_"++-+~_:
                   .   `'.''`"'.^^''".` ``^"^','`'^`^.""^^^^"`',^"""^^^""".,,"",!'
                  !{! '-~]i?l<_~<!i_+>>~
                  ''. .":l",^^,:;:,,"^^"`^^^^^"^^^^^^^^"^^^^^^^^```````^`'````''''''````````''''''````````''
                      li^]{]]?-"I!!!;;;IIlI_:::::,"""":;;;;;;;:,,,,,,,,:lillI!:"""",:::::::::",":;;;;;;;;;;:_
                      iI _]{<[i `^><i~>+>l'!                            ,~~_-?i                             ~
                      i>,l_[_+!:Il```^^`,"I?<!I;::;::,;;:;;l;"^^^^^^^",,""""^`^^^^,,,:::::^^^^^^"""",,,"^``^~
                      i>^^!i-,.':l``':;^'^,~~i~?_--+++(_?~?[+1!`^````^^^````'``^`^^^^`````''````^^^`````'''^-
                      i<^,~_[+^`li^?-_]<]:,i__>>!i?-~"^''..'.``'`^^^^^``''''''"^""""^^^^^^^^",,,,,,"^^^^^^";[
                      i;   `"`  ^, ``";^,  ;^;;_!<<i+:`:"""':^'::"`^ `"^^"^`^'."'^'`^                       ?
                      !>^",^^"^^l!,""^`^'`,i^."~?}_!+]>>~_<l+]<-}+~[<][~}+-_[_<1-]-][:````^""""""````````^^,[
                      lI.,[]{-`.:;',]{?[l.^i]}+~I!]?_               .        .       '''''`^^^^^^`''''''`^^,?
                      i:        ^^   .    `i  ^_~~<I~i,ill!^i<!i>iI>I:<I!ll;i"il"i<i.                       >
                      ~~,,<ii!""!i;<il!l!"I->lI<_??<+~i!<~<I<<>-<_<-<>+ii>>l~i<+i>_~l^^^^^^,:,:,,,"^^^^^^^,;~
                      <; '+!!~  "".>~~?~+.`<~]~]~+-l<:<-~~;                                    ............`<
                      <;        ",        `;  `+i<i<>,>-iI_>-I^___;>+~!<>___~>"<:l_<~~[+~"<]_-+.           '+
                      <;        ;;        `;  .<~ii~~-_!^<l<;i!>>~-i;+]>.''''' ' .```^``' '``'^            '-
                      >!";<~_~;:~~::lI;I,^;~ii!<~?>~_~__;ii~l<~i!<><:!i!"::::::^"^^^^^^,,,,,",^^^^^^^^^,,,,I?
                      !" ^<l><  ;; `~]~~^ `!i<_[;<l:_<!<                                 .  .          ....^-
                      !"        :"        `;  `]>i+II>_;i~-i?;>:i_<>'+][l!i;++;~~{!+i_>_I>]~;]_;           `_
                      i"        :,        "!  ^<><~;>i,[~-?><-1<_<i;;>>+ii, .  '.`.'  .. ..' ..            `>
                      _,        "^        ^;  "++?~,!<;>~I>:l!~;<>i,,~iii<l":,^^l";^^,^^:.,'""`"l;.        '>
                      _l^",,,,^"i!,::,^^^^:l"^;>~_-<+-->+;_Ii+!i--->;~<i<__>~_-!_i+i~]]~]I]>~?-<{?!^^``````:<
                      _;.I?-}_'.il':_?__".^!_]]+;-?:i~_?>                                         .. .''''':~
                      _,        l:   ...  `, .,<i~!~~~I!>~li>!"<<l~>>l<:>+ii>;lll:!~!"!l!lll!!li<II"lI'    ^+
                      _,        l:        `:  "-__-+_[-><~^`""`:,`;":^:':;"":"",^`":;'::":^I;:;lI:"^;".    "+
                      <"        l;        `,  ,+l<<"!><i+:''^^'":;^'^``^..""^.`'^^^..^''"'`  `  '''..^,    "+
                      >^        I,        ^:  ,ii<_I+[[??i\]]<:ii!,l~iI<+l_+_:>>iii<ii~_->~,;_,i~i+"<-~    "_
                      _^        :^        ,l  :-<i<,><i+>:~<:                              .               ^+
                      -^        ,^        ,l  'll+"~+<!_"<+!!+i;-;l--~;~;I+++>+?I{i+_!>?[>?+<;:>!_<-;      ^>
                      _"      . I"        ,;  :<<-_,~?~i_I~"l>I;+~_l:+><~~~i<!~I_~-]:-i+<l<}i,~+-".'       ^>
                      -;^^i~~:,"+!""^,"^^`:ii!~~+-?><_?~<I+i~_~<ii!:,ll;IlI;lI>ll:;I;<;l!Il~!l<><:^^^^^^^",i+
                      -;""+?-:"^<;'`'"".'^:<-~+>_+<~~;l]Ii?1~-_i..''`''````^^`'''''''.``'``'`'.'.'`````^^"^!+
                      _:`l{?_i``>:^?+]}<_`,+]-]<"++<>++,~_?-__i^~;......`^'`''..' '..'`'`''``....'' .''''^"!+
                      ~'   '.   l" ''^"'' `,'^:~i_l+<<<i;<i><~i:i^;:;:"!,`I,;;,,,~"!i,`:";;,^::;;""il`,:l^ "+
                      -`        ;^        ^"  ^lI~;!_~l_!<^<~<!;~:>~?<i+!;~~<!>iI_i~>;,~i<+~I~i>><:~>:<~-<`I+
                      ]`        :`        :;  !_i~+?]+!>->i->_il]-I_[;>~l~!++,+_<-]_+>I+!+<~+lI_->+Il+>II__1_
                      ]`        :`        ;I  ;<+!+_<"_<~l;!<_>+<i+><^]<><+">I!~_>~~]_+.                   ,+
                      ]`        ;`        ;;  Ii!+~?li__!'<!"<i+-_ii:;~;l!]-<I_~~~<<,+-li-<~-_~>-:__<>+;<~ :+
                      ]`        >^        :,  l][}~i?__"i+_?;_[>l_~-_]-]-l^^  '..'`'.'^'``'^^`^`^.^^``^'^` "i
                      ]`        <^        ,,  `,''' '   ```^'^^.^!,:,^`"`'  ":'`.       ^"^.               ,!
                      ]`        >^        ,,                    _{""l       []:;-       I~~"               I~
                      _'        l'        ,,            .,^' .`^<!  I:^"^^^:>l  _"^^^^^.''`                I~
                      ~.        I'        ,,            `]]?:<!,^!^^:,::;::;^!^'<;;;::;'lii.               I~
                      ~.        l'        l;             ::!l!"  ^l>.        ,!l^                          I~
                      ?.        I'        !;            '<i!.`,::;<"l:::I`l::;l;:,I",II`i>~"               I~
                      ].        !'        ;"            .+-__I....<Ili+i>l>..`l>~>}~:'. .`^.               I~
                      ].        <`        :"             ....     i~iIil><:  .I<!I>>I  .Il>                I~
                      [.        <`        ;"                       ;     >              ...                I<
                      _         !'        :^                    ,lIl"I  ;l,^;"                             :!
                      _:,IilI;""<,"I,,,:I:<<!;,",""":",,,,,,,"^^!++ii~,,_+->-i^^^^^^^",,,,,,"^^^^^^^^^",,,,<!
                      <. l?-?!  !."?+-]+~.l~?[]]_-!:>                 ..      ........'''''''.........'''`'>>
                      _..     ..!'   .... >: .~_~__<~]II>+:>~<~'                                           !<
                      !IIIIIIII;l;::;IIlll>ill!!i><i!~>!~~i++~<;::::::IIIIIIII:,,,,:IlllllllllI;;;;;Illllll~;









```

*Figure from page 15 (2346x3317 px)*


---



4203-E P-342



SECTION 3 DATA INPUT/OUTPUT OPERATION



Signal



Direction Details



Name



SG Grounding for signal



SG Grounding for signal



SG Grounding for signal



DTR Output Data terminal ready



This signal comes ON when the NC is ready for operation.



If data is transferred to the NC while this signal is OFF,



EX-INT



it will not be



read by the NC.



Input External interrupt



This signal is used for BUSY/READY control at the peripheral de



vice side.



When this signal is used, the following applies for transfer of each



character:



{1) When the signal is OFF, the NC cannot start data transfer.



(2) When data transfer starts, this signal temporarily goes OFF; when



it comes ON again the next data is transferred. (It goes through



the sequence ON, OFF, and ON for each character).



High



EX-INT Low



(output)



TXD



~nput)



High



Low



Start bit Stop bit



The EXT-INT signal cannot be used for a peripheral device which has



a buffer, meaning that the ready signal does not switch ON/OFF for



every character. For this type of device, use the CTS signal.


```text


                                                                                               ^^^`'" "````'
                                                               ....''.'. . . .'  ..' '... .'. :[]--i] _l~_-l
                                                               >1_<>>~-[I_.++_~+l?]~<<i+-<>_~>~^>_<-~_~<~>-i
           '''''''''''`````````'''''''''''`''''....''''''....'''`'`'.''''`'''...'.' `.'''`...` .''.^''''``''
          .,,,:,,""""""::,:::,::",,":;;;;;:;;;:""""",;;;:,,,:;;;;;;;;;;;;;;:::,,",,,":;;;;;;,"",",,:;;;;;,:'
                      i;>->>><lI>:""^"",,:!I;;;;;,,,;;;;;;,"",::;;;;;;;;,,,,,,;;;:::::IIIIIIII;,"""::::::;:I'
                     "_ !)1[--  ;;_!>i-><^l^        ... ...............`-~~<>>`..........................'.>,
                     ,-'!]?i<+^`!";,;:;II^+"....       .      .........'l!!il!`...............       ......~,
                     ,-^":]-<^",<`''^:^`""<_]<+>>~~<!+-l<+<i~:``````^^^"^```^^""^^^^^^^::::::"^^^^^^^,::::,?,
                     ,~  `-~!   I   ."'   :!_l<>i_<_<<_,>--!_`                                             ~:
                     ">  `-_i   l   .`.   ;!_!><i+>+<~_"i-_!+'                                             ~"
                     "~``"]-i.''i'..`"` '`i!-ii>>~<__~+:~-?i?".'''''''''''''......'''''''.................._"
                     "+",]_+];`^>`!]+]_-<"_~~--l>~<-]~-l_-_-l'`''`"""""""""`'```^`""","",^`^^``^^,,,,,,,^^^?"
                     :<  ,^`".  ! '":I;:` !,,l_>i<I~!i+;!~~+i^',;^'"^`'."`.,:"'`.^``" ^' '''''"''          +"
                     ;+        .~         I   :l>i;+_l_iIi>i_+,>_!!]i+<;+_;~?ll~,__+];>~">]_+?]~<^         +"
                     ;~         i         ;.  ~;~-[liiI>->-->!_<!<:~_;~_I:-i>~:]_!:__i_l<ll-~<'+:-~;<+i<]; _"
                     ;_.       'l..     ..l   !_?+l?i!+-!{-!.....'..'.....'..'..'''`,.`''...  ...'...'..`. ~^
                     :-I[_i~__;">":+_~<<::i_<<<><_>+]++_i<!"^^``^^^"""""^^^^```^^,::,:::"^^^"^^^",,:,,,,^^^-`
                     :l.iI:;l;. ;  ;ii!:  ,i!!-<!_I!>+>i<<"...''. "`.^`'^"`'^`'   ..   ..'    . .    ..    -`
                     :!        .I         l   l>_iI?}~_:<!;?--l~-,[]<-<>-1~_-<!:~>~+<I+~>_+I?_--~[<-l~{;   _`
                     ,!        .I         <.  l<~l!+-<                                                     _`
                     I>        .i         i>-!>>,_l<;-_>+~I>;<+-i^_<l>~~<++>>:]<~_~iI~;l<+!~?>^~!i~!i`     _`
                     !<        '>         !!?<-~>_+>'`;^^' '.^^"' .`` `````^I.;,"^"^ ^'.^,`""^ " ";:^'     _`
                     l<        'i         ;Iil^<?~<l`l,'^::";^"`:!!l i:'"l;.":^"^,':,,`:,:^""""":^         -`
                     l<        .I         :l~; i_<>>,~_!l-]!_l<II~ii:~<<!_!;<_<<+<l++>;~]_!!~~i+]-,` .' .  ~'
                     l<        .;         :!+l <_!_~:+?]+~+~l_-<,-++?!"?-il-]>+!i?i+~~~~<-:[<~~,<~<l^_-?_; ?'
                     ;l        .;         ;    +!>~i+-II?-:]{}-;~-+I~-]I+}{~+<<_-<??~~+?^'[>_+_?l~>><_}>   ]'
                     ;I        .;         l    ?-<I-~_+_>~-:-?l'<~<!`?<~I~+><]:i[-?I>-_~~~-??,..    .'`    ]'
                     ;l        'I         <          ..  ..   +>:,"":;".  >+^;::;;; . '+--"'.              ]'
                     ;l        ^>         <                  ")l.'''."+  '|!.''.. _    ',".                ]'
                     ;l        ^>         >        :[<>[i.,::!~:     <~::l?,     i+::;,!>i                 ]'
                     ii        ^>         l        '~>]>+"    "i    ,i    ;i    '+                         -.
                     ii        ^>         l        ^<~i.  ",,,!_,^`^<l,,"^i+:"""i<::,:^li~'                ~.
                     ii        `l         l        '?-+_^ ....>]^><<1<....l?!i>!-[.... .^^                 ?
                     ii        `l         l                   I_;i><?I    :-i>+~-~    .:!l                 ?
                     !I        `l         l                   ';    ;.                 `"^                 ?
                     l;        `l         >                 ,l!i,I  <!:^;"                                 ?
                     l;        `l         ~",'.^^""'""^.'.'.:i<;l>`'l!>;>;''.    ...'...... .    ' ....    ?
                     l;        `l        .i!_?!}-_!>[+:>]}+[I!_~>!~l+i,~+~<l_;>l~?<??-+~_I[~___;[?_[i;<[!  -
                     l;        ^i         I<l+<?_!'!~~~i~[i_~}!]+!I+__-;+_+>?,+<_<,+~:~[-_-;i_-~+<~:!-"    ~
                     li^"""""""l-","^^^^^^>]?[?+i}]{[1-]~"?-[!}-[i{}}i-_<)]-?[;~[1i{{_<_+}i-{]-)I``'`^``'''_
                     ."":::::::::::,"""""",,:::;::::::""""^":,,:;:I;:,"^"""":;;;;;;:;;,,",::!!Il;;;;;;;;,,,,








































```

*Figure from page 16 (2346x3317 px)*


---



3-5. Connection to Peripheral Devices



4203-E P-343



SECTION 3 DATA INPUT/OUTPUT OPERATION



If an RS232C interface is used, a special-purpose cable must be used to connect the signals that are



required by an external device since the signals used for the connection vary according to the external



device.



A typical example is shown below.



3-5-1. BTR System (No DC Codes)



Example 1:



FG FG



Peripheral device



[Supplement]



TXD



RXD



RTS



CT$



DSR



RG1



DTR



1/0 BUSY/



1/0ALARM/



READER START



Fig. 3-9 Connection for BTR System (No DC Codes) (1)



Since no EXT-INT signal is used in this example, bit 1 of NC optional parameter (bit) No.



8 (No. 13, 14, 21, 22) (Ready signals of CN0: to CN4:) should be set to "1" in advance.



(1) Timing Chart for READ



r;;::-,C .._ ~P=e=rip=he_ra_l _,



~ _ device



Ready



DSR



Data request



RG1



Receive data



RXO



n n



\/ \I



11 11



8 bits



Start bit Stnpblt



Fig. 3-10 Timing Chart for READ [BTR System (No DC Codes)]



High



low



High



Low


```text


                                                                                               .""^`^" :'^^^.
                                                                .''.''.'... . '' ...' '..  ''. i[][__+.~I--?"
                                                                ~{-ii<<__!<'-_-_~i[?~>>>_~i<+<~!^_~~__-+_+i_:
           .^`^````^````````````^```'''''''````````````''...''''''''..'.''''''.'''''.'..'''. ''.'`..`.''.'''.
           '^,"::::""^^^^`^`^",:",:"^^^^``^:"::,,,,,,,:;;,,,;;;;;;;;;;;;;:::,:;IIIIII:;:::,:;IIIIIIIII;:,,,,'
           :~,+   .<ll;I!>I~!I;^<:;-ilIli!!;i"!i!:lII!:
           "i,<`  'I;i;Ii<l!ii;`<;",i!l~!><:_,;i<lli><!
                 +;!l'+<<><~i':!!!~ll:^;.;l!! l'IlI;Ii"l:!!!<l`li!~",iI~:Ii^"il!:l:^llI!!i:!l;^il!;i;;~!!^>!^
                 ll~!l!<<+<I~l:<+<<<~i:+!~<~ll~I_>]~!><<!~_!i>I<><_:i<>iI!~;i<-<l;lI>l;<>>li~>:>?!+~l;~+>I+<:
                 l~~~i!!:l<'<l">l>iI>;,>ill>^~!l<">!I:~_I><::<~>"Ii"ill"iiIl>I<i>`!~i;I+l!i>~<_"<^ii;I<i<!!~"
                 i_i><<
                 "`^`"^""`^`^^^,```'"^`^`'^^```
                 >l+_<i-!!+~+i_]!l>l_>~+!,+_<+~
           ''`.'   '^'^ '  .    '  '.. .
           !<_ll'  i[l_;__+]-_l<[?;+]!!_~??_<
                  `i^"^""l`^'               .
                  ^_>~!<+_;"^
                             . .....   ..  .. ... .                             ..        ....   ..
                         +I;;;::III;I::::::II;::,;I<                        "+:;::;lI::IlI;;;;,,;;I;:"~'
                        .? .~~`               ;!" i-!::,:,^",",:,,,,"""",,,;~+'^i;       !>i<i>>:i<l>;+"
                        .]  .'                ";" i?l::::,^",",'",,,,,,,,,:;__``Il       .^^"^""`^"^"`+^
                        '[                        "[           ~^           >~                        -`
                        '-                    I~-:___;;!i!IllI>$h[lllI;Ilii+-_"^?i.                   +`
                        '?                        ^]          .~            ><  ..                    ?`
                        `]                    ll!:~-<;:,;::::,">Uhi::,,,",:!__^'l:                    -'
                        `]                    :l!"l],^`'``````',/Q:^^`^``^^,~<'`<l                    _.
                        `?                       .l]^.........,/!'......  .'~<.                       ?.
                        `?                    l<>>~_<;;;;;;;I;+B0~;I;;;;,,;<__`'<_'                   ?.
                        ^]                        "-           ' ,          <i                        _.
                        ^<                    li<<--+lllil;::;;[aB!IIIIIIII+_?^.!ll~i<!^              ~
                        "-                    .   I]            ;1.         _! .`''^^`.               [.
                        "~                    ^;II~-l,,,::,"^""<xY:""""""",l_+' ""^^`:::'             -
                        "<                    :ii!<_l",:::"""""+Cp:,,,,,,,,!_~''!II!l>>~^             -
                        ,_                        I-                        _l                        -
                        ,~                    i?!"]_+!i!iil;;IIl<!Illlllli!__-'`?+`                   -
                        "<                        ;~                        ~,                        ]
                        ,~                    !~!!+_>;;::;;;;;]WYi:;::::",,>_~.'~il!<>;!l!!I         .?
                        :+                    '"^'>_^'''.'''''iv_^''''''..'^-! .:;:;I:^:":;"         .]
                        ">                    ^,"">-^^''''''`'!t>^''.''''''"_l .`^                   .~
                        :<                    lili_]!I;;;;,,;;{8zi;:,;I;;I;<?+ `_~                   .?
                        "<;IIIIII::II:,::::;;;:,:,<;                        <;,:",:;;;:";;l;;,"::;;;;l~
                          ............,,'."^"'""^^'.'^.'.`.."""'``.'... `' '`"`"``^``'``''```''''`````
                                      <!]^<!-'!<<i<?~?~+;?>;[i_>i{_??+<;][!l?~:~<<__-:>>^
                 '.              .      '.                                         .
                '}]+]_-+>-+?~   .__ii!!~l+<<;<?+,~++<+:!:i+><i;?i<l<>_!<-i`~~""i~!]I;<~>Ii_;><i+l>+_:li~l+~:
                 '.`^'...'..'   ^?I]_I`<~^li'i>`I]];_]i~~~;+<>>-il+i+?_<I~:<+>il;~>!!?>+>;+~!<;!!;>I!<>~<li;
                                 :'",` ', .,':"'"I:`::IlI!`l<II!;^;^::l"';^":I;""!,IIl,ll^!!^I` ^ ;'!l;i!;I:
                  ;i` "<I!II"!iII:;l"I_iIiI
                 .:l^ ':;l;~I;;l!,"i""!l;!:
                                 I"`^,.   ":::;II;"^
                                I+"]<I+!""??()|_+I,?
                                ',`"":"  .;l!l!"^`",
                                      ^'          .!:::;llllI;;;;;;;:"""::,""^""^^^"":::::,:,,:;:;::'l~_"
                                  ,]_?_'          ^<                                                 .^^
                                  :[}};'''''''''`';<
                                  .""^^^^^^^^,:::,:^                                                 li~`
                                                                                                     '^^

                                  .. .;^  ..           I!;;;;l                   ";^^^";             !-_^
                                  I]}+;+<><!           <`   .<                   ~"   .<
                                  :?_i''`''.'''''....''+     ~.'..........    ...~`    ~.......      ..'
                                  ^``",,"""""""""^"^^,,!`   >l::,:,::,,,,,^^^^",,i'   li;;;;;lI::::^ :!+`
                                                       ^< .<;                    ,!  !l
                                                        -">"                     ._.l,
                                     ""                 !]_:;::,"""",,::,:        !<~:;:::::::::l^
                                 ^-~~+>I>_+`            !:>.            'i        :;!`    ......!I
                                 ^][}"`'`^`'............~:+             `<  "     l:i.          <:
                                 .","^,,,"^,:::,:::::;;I>:~>!!!llllllIlli~ll<;;IIl<`I::::,::::::+l,'
                                                         ~`'``^:;!i"''```.l;
                                                         l     ,Il+,      ;`
                                                         l: i++Ii!        :: `_>i;~^
                                   '        .             . .'`''`..          ^^,`".
                                  ^]-!"]:?> ~_>++<i~<->l?i:?]>]~;{_<[;?_~-+~:<]<"<-ll~~?_<]!
                                    ^^ ' ..  '.'^"...^. '' .`''''^. ..`,^`^`.``^.'`'.`^^^^:`








```

*Figure from page 17 (2346x3317 px)*


---



4203-E P-344



SECTION 3 DATA INPUT/OUTPUT OPERATION



(a) Data request signal RG1 is output from the NC.



(b) On receiving this signal, the peripheral device transfers serial data.



(c) The data request signal is forcibly set to the "Low" status in the interface circuit by the start bit



in the received data.



(2) Timing Chart for PUNCH and LIST



Ready



DSR



Clear to send



CTS



-~;~d



d_ata



____.I I.___I.__.__._I


# I __._I

_.___I



Character



Since CTS has



gone OFF,



data transfer is



suspended here.



111



Since CTS has



come ON again,



data transfer is



recommenced here.



Fig. 3-11 Timing Chart for PUNCH and LIST [BTR System (No DC Codes)]



{a) While CTS is OFF, no data is sent from the NC.



High



Low



High



Low



{b) If CTS goes OFF during data transfer, data transfer is suspended within two characters from



that point.


```text


                                                                                              '"""`^` ,'^^^
                                                               '`''`'''... '.'' ..'' `.'..`'. !??[__<'<I--_`
                                                               -[~>i~~-+l!,-+~_><]-+>><__i<+<<!^~-_+__~i<<-^
          .`''``````^^`^^^^`^^^```'``````````````''''```''''''''... .'.''''''..'''. '..'''..''.'`..'.''.`''.
          ^,"",,,,,"",:"""","""^^`"^`^",:,,,::,:"^`^":,,""^^,,`^,,"""",:;;;;;;;;;;;:::::::III;II;::,:,,:;;I'
                   :<;.~!>i`!!!I!<:l!i!!"~<i:,I`;liI;IlI!^>l,;~!'
                   ";".,";;.::l::I^,!i;;.",:^`:`;;l;,^";:^::,^l;.
                   "l^.lI'"l,;,;:""!,^`;;,;,'l:^^"""::"",`I"""^',::,!::^^:,::`I:;`
                   ;>:.;l^I>l!lil_;iI;:<_I~l`i<;>>I>i<!!i,_!ii>,l~ii>i!;I~!<i"_~+;
                   '`' :"^ ^^^..`''.'^.'.'.'`.'`.'^'  ''.' ^. ' ... ''' . . `.  ..`"''..`'.''`..^. .'.''`'
                   l+l i<-:_??il-__-_~I+-<_<i>l~!<+_!!]~!<I_-::!<]:,]?_~+l<:__;>+?>-++>l+<~_!+_:+_I<]_!!]i
                      `+">+!,+>-~<-<I???;
                             .   .  .'..
                 <]; ^+<<i~ii_<-~l~!;-~]]~_li<<>;<?~'
                 ^^'  .``',,'^'"^ ^`. ^''.. '`^'`^^'
                            lIlI"l.  ^l<><~~>I""
                            -"_~^_^Ilii]1))>i:l<
                            `^''^^.  '","":^^"I".......
                              .` '!'         ,i,:::,,,;:::;;::::::",,,,:::",::"^,:,:II::::":::^"';__l
                              l1}}<.         I:                                     ...... ..... .`:'
                              l+-_"^``^^`````>:
                              `''^"^^^""""^"",.                                                  `:i"
                                                                                                 '"I^
                              '''........ ..
                             .""^;:^^^`","::,::,"::,",:;,!,                .;,,,"^":"^^^,,^^""", l~~;
                             .;;;:i";;l:                 !l                ,l...............'''' `,l`
                             `--),,";;I"                 I:                ;l
                              ` `                        ^<;^`^^,,,^::"":::!;                    `^:'
                                                          .,;^              <                    ^;i"
                                              ....'''     ..':I:"           ;i
                             .:``;I::.       ^!l;",,,! "liI::,^_;           lil^"::l, !Ii:::;i"
                             '[}]!:++`       :ll^    i ""i'    l            !^i    ;I <"!    !I
                             ^l<i"`.'""^""^^^i;!:`^^'~`!I<"````_`;:''`''..''!"~.'''!I.!"i....i;
                             ..  '''`^`'^^``^^^:;,::I;:l!!,"""",">l"",,,^`",:::^^,,,""^.:^,:,I:'
                                                :<!!iii'         `           ,
                                                `",,,,:.    ,i:I,;;i;li`  ;i;I:;Ii";!.
                                                            !]~?!_+~`:l'  ;_~?!~+i+])i
                                                            >{_>l+~<<`I'  I?->i_~_}>_:
                                                            l_--_~__~_-i  :-<~++?~~->I_<,
                             "'  ` '. "'.'. '`. .''.',.^'''. .'^''^".^^"^.'  .  . '' '`'..
                            '~_+`-,!, <+i_-_!___il-<!-~?-<_!>~<>l>_<^{?i-l~]+?__ll]];<-!;~~~-+-!
                        .     .'     .     .                         .     .. .  .        ....''
                   <[,"}--[!i<<_I_;+-_i^-!;_?-;+:__+<~<_>l}-;~[>'
                   .'  . ''      .          .    .     '.  .  .
                   ~+^`i;!!_,<!<<:~?-II+i~<>;-~+I<ii<_+,`-+_I<<>>-_;l!:i>~<<l++<l>+?i:;~>;I~>l>i~~>:ii!l.
                   ""';~!i,>!?~""'^`' `,"^"I`:::^^"",":`'::;""::,:;`^"`::l;:";;:^,::,``;:^"::,I;;I:"^::".
                      ,l!l;lI;!



































```

*Figure from page 18 (2346x3317 px)*


---



4203-E P-345



SECTION 3 DATA INPUT/OUTPUT OPERATION



(c) When CTS comes ON again, data transfer is recommenced.



Example 2:



NC Peripheral device



FG FG



READER START



DATA BUSY/



Fig. 3-12 Connection for BTR System (No DC Codes) (2)



[Supplement] Since an EXT-INT signal is used in this example, bit 1 of NC optional parameter (bit) No.



8 (No. 13, 14, 21, 22) (Ready signals of CN0: to CN4:) should be set to "0" in advance.



(3) The timing chart for READ is the same as that shown in Example 1.



(4) Timing Chart for PUNCH



Ready



DSR



Peripheral



device



----



External interrupt



EX-INT



Send data



TXD



Fig. 3-13 Timing Chart for PUNCH [BTR System (No DC Codes)]



High



Low



High



Low


```text


                                                                                               .````'" ".''^.
                                                                 .. '. .    . ..    . .    ..  I[--?<_ +:+-{,
                                                                +1?~i++-~l~'?__~<<[?+<~<~~i+_~<~^<_+-__+~+~]I
           .'''''''''``'''''''''''''''''.'''''''...'............'`.'..'..''.`'..''''.`.''''...`..`'.^'''''``'
           ^;;;;;;;;:,:;^`^`^"^,,,:,,,,","^,;:::",,""^,""""^:;;:"^"","^^^^^"^,:;IIIIIIII:,::::;II;II;;::::::'
                    `!; ><ll;^l!>l"Illll^l~;^;;II.^ill^;I;:!I`,""I,":::::,::I
                    "i; ::"I,.,^:I,!ili>"Ii;:__>!,,~><:;<!!i<";;:<l!l!liilii>'
                      '?I>lli~:i,
                      .;:l::l;":^
                                 ....................                           ........................
                           ;>lIIlI!!IIIIIIllIIIII::l;+;                        <I;;:IIIIIIII;:::IllI:;:,Ii
                           !: I_;               `lI "--l::,,,,,,,,::,,,:"",,::i?!.;;       `!!l>!ll:<I!!:-
                           l: .'.               ',I "_+;""""""""""``""""^^""""l]I':l.      .`"",,""^:"","+
                           i;                   .''^.~<           ;;          '[' '                     ,_
                           i,                   `i~!l]]i;l!iii!;;:cQillll!!!lI-_<`-<.                   ,~
                           !"                        ?l                        ]                        ,!
                           ~"                   "-~<>-]>!!!llI:::;lJ\;IIIIIIII_+!`_i.                   :l
                           -^                    .''._:..     ....'<!''.      "]..^'                    l!
                           -`                   ':,,;+>,,,,""^         `""""""i]" :,.                   lI
                           ?`                   'l:lI_<:::,,,_"       `-:",::;~-: <~'                   l;
                           ]'                     . .]"   `^ _,       ^+ :'   "]                        !:
                           ].                   `<i+__[lli0u:>'    .  .<lOJl;l?_l.+-'                   l,
                           ?.                        [.    '             `    ,-                        <:
                           ?.                   'li!~-_;;:,"::::::>X+::::"""";+-:.ll.                   ~:
                           ?                    .:I:;[;^```````^^^;ti^^^^^```^i~^.II.                   ~:
                           ?                     .  `},........            ...I~.                       +,
                           ?                    ^-_'<--IIIIIII;:,,:llIlIIIIlli-_:']-`                   <"
                           _                         |                        :i                        >"
                          ._                    ^_+l+-?IIIIIIIII:;p|:;;;;;;;;i_-:.~<ii<<I!i<<i.         i^
                          .-                     .' '{`......... .~" ........'!<. ''^^^^'^`""`          >^
                          .<                    '::Il[I^^^```'```"{l`^`````''^!<'.":                    _"
                          '_                    `I;!+-+III:;:,::;!Z1;lIIlII;;i??,.i>'                   <^
                          '_                         {                        !<                        _^
                          '>                  .?<,<>]_]l!lIIIIII:;{p!;lIIIIIl~-_" ~<<i!~>+l'            -^
                          '+^"^^""^^^^^^^^^^^^",,,,";]..          '!'.........~_`^""^^^"""^'''''''''''''_'
                           ,,,:::;:,,:I,":::::;l;;;:,^         .              ';;:,::::::;;:::::;;;;;;;;l
                                     ^~~l^_"_!.~ii<<~+_<!l_I<[~[!--_[_+!i[~:~-!:<i+_~i"[>
                                       '` . .  .'   . .           ^.'.. ..'  '. .''``'."'
                .?]<+~<~i~>+>   .~~l!l!i,_i!;!~<:!<i!<:l"li!:I,iIl"!Ii;!<l.!i^^I>!<;"l!;I;>IIlI!;!<<;:i>:i>,
                .:,;;:":^,^",   `-!--l;~<;>~^i~,:]{i_}i~<_i_i>l_>!<+_}--<_;~_ilil<~!l?<~~l-~<_!~~>+<l>-<>i+!
                                'l^ll" ,l ^I`::."!l`I;i!i>`!<>;>!^I^;!>:.!,;;!;""!;!ii:i<">i,i:`<.!"!>!!~!>l
                  :!' ^!:"";":"^'""`^":."i;":^'^^^'.````.." ,'^ `^.`` ..,^'``.^` .
                  >~" 'I!!:<l>i_:<<<!I>,;+>i>I;i!><:~?><l!?;_>?I+i>++IlI~~+?<?-_^I.
                  '^  .^.'`  '^''.'' `^'^'''
                  >?, ^<l~_]<>~_-!l-Il<~_-<_;

                             ;<l>!i;.``!~-~--->"I:
                             <<"_lli,>;~>{[{_l;`l<
                             ':"^"".   :,,",,",:;'
                                  '.   ^!;;;:,""",,::::::::::::::::::;::::::::::::::;;:;:::::::::``~->
                              ^:",!'   !l                                           .. .           .^'
                              i}1]l    lI
                             .!i<i"::::_;                                                         ^iii
                             .'''^""""""                                                           `''

                                   '       .l;;:::::;;;;;;;;;;;,        "::::::,",,,"""::,,:.     :<+_.
                              "^,^^>:;:"": :?``'''''`````````^`~`       -``````````````^^^`_"       `.
                             .-?_?[!,ii;i> :i                  >.       ~                  ~^
                             ^iiIil^^``^``^<I                 ._"^`````"<                 .],```' .^:,
                             '''^''^",,"""^"l                 _I^""^^^""!^                ~i,,,," .:l;
                                            +`               .~         ^+               ._
                                   ..       I~               ;I          ~I              :>
                                   ".        _!_:::;;I;IIII;:>'          I-~lIllI;::::::;<'
                             ^-i!;!<>'       +^]             >.          i"_'            <'
                             `?-<``^^        ~"?             i '         <,i             _.
                             "":;::"^,;;;;;;l-^[;;;;;;:""""""]I]""",::,:,+^~:,::::,""""""};]",""`
                             ...''...'.`''`''. '``''```.''.'.'''''.```^'^` '^"^^""^`^``^`^^"""""`
                                  ;^' ,.^" ,"`^'.."^'`'^'.:`^"^^^',"""." '^.' `^. `^.''.'. .
                                 .ii]`_"!+ l+>~>-;~~?+I~-,ii_?~<<!1~>+;]-_]~~,+]~;+_I!>>]-~]:













```

*Figure from page 19 (2346x3317 px)*


---



4203-E P-346



SECTION 3 DATA INPUT/OUTPUT OPERATION



(a) When the external interrupt signal EXT-INT comes ON, data is sent from the NC.



(b) On reading the stop bit, the peripheral device forcibly sets the external interrupt signal to



"Low". It is essential that the external interrupt signal be set to "Low" temporarily.



(c) On completion of processing, the peripheral device switches the EXT-INT signal ON again.



3-5-2. DC Code Control



When DC code control is effective, the NC outputs DC control codes to control data transfer.



The user can select whether or not DC code control is performed by parameter setting.



The available DC control codes are DC1 through DC4, as shown below.



"DC" is the abbreviation for "device control", and these device control characters serve to start peripheral



devices.



DC1



DC2



DC3



DC4



[SupplementJ



Example 1:



8 7 6 5 4 3 2 I



Tape reader start



Tape punch start



0 oQ



Tape reader stop -+ 0 0



Tape punch stop -+ 0


## 1. Since DC control codes are automatically generated from the NC, the user does

not have to write them into programs.


## 2. The control codes used are the ones shown above, regardless of whether the ISO

or EIA coding system is used.


## 3. The NC unit cannot be controlled by control codes sent from the peripheral device.

Peripheral device



FG FG



TXD RD



RXD SD



ATS



CTS



1/0 BUSY/



DSR 1/0ALARM/



SG SG



DTR DR



Fig. 3-14 Connection for DC Code Control


```text


                                                                                               '`''.^ `^.`''
                                                                .'.''...   .  .    .  .   ... `?]_?i}^li>][_
                                                               ,{]_<-__];+^>+-+-!-?_~<~~+><+_i+:l---_]_~_<_~
           '````````^`''```^````'''''````''''''''''''''''''''..'`'''.'`''`'`'..'''`.`'.''`...`. '`.`'`^`'^``
           ",,,:::::"^""`^^":,,""^``^,,,:"^^^,,::,,:,:,""":,::""""^";,,:;,:,,"""^":;::,"""::::;;::,::IIIII;"
                    l~."_>!>"lil"l!iI;!I:!!I;;!:;!l;!">l>;;~i"":;,;;`!<,.lIl","^I;;:l,;^I;":I;'
                   .;l'';"II'^,:^I:l:"l:";I;;li";><:i^;:;",iI':!;:il^l>;'i<>;II:~ll:!!i"li!;>!"
                   .::.`;,.";:;,"':"``:^^`:^ :^''^^^""^^"'"`'"^."`'""' ^"^ "^..'''''''.^'...'.'`''`'^.
                   .i<`:<l:<-~?<?!i~il--+I]<,>-l<_<_~<~>_;-+><~:+<>_~_;-~]l__il?~-~~}l!~-il~?I>?_<-:-;
                       '!!_<' <;+:~<+_l+_ll<[;++i;+-?<![!i~_<l>?!<__>]I<>"_-I~:I!i_;,[~<+<>?+?I
                        .                                     '.  ..         .  ...  ' '^. ' ''
                   .~_^;->:<~~-~]_~<;_>~<~~?_-?~_`+-!!-+~-<~<-:?_i>_;<_~~~<_l!_~l?~-!~_~"~~>>~;<-ll_+~!'
                    .'     .. .   ...'.^.''`'`'`:.'`'`^'^`'`'^.^^``"'^"`^`^"`'^"'"^'.`^'.,I,":'^^`"i!:^.
          `_!~ii  '++ll+i~<:+ii+i_`
           `'``' .''''`""^^.```^`"
                ;]]~_l!-<"><?_:>><~i!!l>]-~?+_!:[_I~_!:<+]><~;~_I!<i<><:<i-~il~"><<?<>I-_+I<~>>_+:
                ',.''.'''.````'`'`''`.``.'`````'^"`.'.'^^,^`^.``.'`^^'^.`^,^^.` `^'"^'`,",``",::;^
                ^<~>,<--^i_>"_-]~~;]?-}+-,l!"~~;+-ll~<?Ili>?<<I<I~++-~>~+~!_;!_++~~+-+">~?+~>
                `"``'`'^^^"^'""^'''^'`..``^'.''."^```"`'''`'^^`^'``.'^.'`''"^`^`^^`^^^.^^^`";
                ^!>>;-i__-+-;i<I;<>~~!"!<-]_:_>l<_!l:~~i<+}:i+!_"l[;+~<++li~?>+l
                ',,"^^`:"'.""^^`^""''^"`'"^'^`'.`'^`'^ ``"""''`.'"``'''''`'`''^'...'.. .....'  . ..  . .   .
                '>>i`<!~~il?<~_>>]-ii;+i`+_i<<iI+~<><l'_>>i+<-?~l]~~~~I<>~>~!i~-___--<I+_i+<<il[]?i++<?-?~_+
                ;?<i~+_^                                                                           .  .
                 ......                                     l'<^I'<.i !`>^!',`;
                      ;_>i".. ,?+<i:~<<~i"~+~I         ^,   <".   'l<^",'.^!ill
                      '^`'     ^;,".,::," ":,^         .`   <`     :;`.^   IIl:
                      :+!<; . ;?>i;I!;Ii;:~!i`         ""   >'     :l''`'il  l:
                      '^`,'   .,l:"::"^"`";;,.         `^   >      :;''^.I,  >"
                      :<ii; . ,~>l:,!ll<I^>;l`         ^^   <;!"  .l!.^``!>>l~^
                      '"^"`   .,>;"^I;;l:'l;i`         `^   <;i"  .;I.`.'Ii!;+^
                      l~!i,.. :<;l,,::;l^,!:,          '`   ~     .Il."!l^   +`
                      "I;I".. 'I>!:Illl!^:il!          ^"   ~     .lI ^ll"   +'
                                                           .?,::",:"""`.  '^"+.
                .'         .    .   ..    ...               '.      .'`"'```'
                l}~-+-]<<]<]'   I:  <_li<^i+::<l~><"!>>~<^><;:<i>li_~i+<>"+~>_i_-+>i<<<:_+;i?<`i_<"!~~,l~<~:
                . .`'.. .. '     .  !<>!_>>il>;+<+il-~~l!<_Iii<<<>!~!^"^"`;^`"`"^"`.`"`'^"`'"^'`",',,:'^,,:`
                                    ^"^'::,"',.;^,"`::".`,,';^,>:;",:
                                !,  Il;`^,"I:,^,:;:".":;:",:";,',",,'l;:;,`;;,";'^:":";l::^"I^I:,I",^I"^:;;`
                                l,  ;!-<<~l<>~l<>~~>l~~~ii><!~<:<!<>;<ii<l"~>!l~;:~?_!>_<~Ilil_>~<<~:~<!!~>,
                                    iI;<<I;><_i-:<i<_>;,~^<<~<
                                `.  `^. '''    ....        .  . ..    .. .   .      .    .
                                ~I  !-?i+]ll<-<![~<+<!?>i~<+><_->~-;>~~_<~i~~[-l<?~<-<~!>-~l~+~-__<_i<[~<++.
                 '~;II;:l^^^                                      '       ........   ..   '.''.`.'.'..''.''
                 '>l<>l~+l,:'''....'...............                             .               .
                      ~I;l!!!!!lIIl!IIIIIIllII:;l;Ii                           -;I;IlIIll!l!!l;l!l;;I;I;;!l_"
                      } .+>'                  :: .<]l^^""^^^^^^^^^^^^^^^^``^^^l[: "`        "<!l!!!i;+l!>` +l
                      {   .                  .;i'^-+-IIll;;;;;;I:;I;;;;;;:;;;I_+~.i~`       .`^"^^^^`,^^"' ~l
                      {                           `[            ^              1                           ~I
                     .[                      .I!::]-_;l;;;IIII;;a*rl;:;;;;;;lI-++.><'                      ~I
                     .-                       ":"`>[:^^````^^^``Cni.``^^^^^^^^I]: ":                       ~I
                     .-                           I{              >i          '{                           ~I
                     .-                      ^]__!?+[>>iiiii!iii?q$J!>!lI!lll![~_.-+'                      ~I
                     .?                        .. ;[              ]_          .1                           ~l
                     .-                       ^^`^<?;^^^^^^^^```cfI.`````````^l]: ^,.                      _I
                     '?                       <i<l_-_!llllll!I;IMa\IIIIIIIIIIl-+~ !~^                      +:
                     ^?                           l_            "  .          .1                           _,
                     ^?                      .Il!!--_l;ll;:;IIIl+0$fIlIlIIlll>-_> ll;il>l^                 -"
                     ,[                       ,^;`+_"`''''.''''`,_v_'`'`''```^!-^ ^^`","^.                 ?`
                     ,_                       ^`""++'...........`!|l..       .I-. ^^'`.^,"'                ]'
                     ;_                      '+++?_]<IIIIIIIIIII{b${IIIIIIIII<-_! i!;>!i<~,                ].
                     l~                           ?;              l.          l~                           ]
                     !~                      .><'i+?!I;I;IIIII;;:,`",,,,,,,,,!+_: ~~`                      [
                     >>                       :;.:]~,,""""","""""^""^^"""""""I+-" "".                      [
                     ii                           ?"                          li                          .[
                     <!                           -,            .             i!                          '[
                     >l                           [^                          iI                          ']
                     il                       ^^^;[!`''''''''''+x+^'''''...''^_<..^".                     `[
                     +;                       iI>_~]lll;!!lIIlIr$Z_IIII;;lIIl_+-^.i<'                     '-
                     ~+I;;IIII;:;;;::::::::",;"^^^)'           :I             ?~""`'^"^""""""^^""^^^^"^^^^I?
                     .,,"",,,,,",","""""""":;"",","                           .,"::::::;;;;;;::;;:::;IIllll"
                                           !<-`>I:~^!+_>i-<+<i;-~,>_lI~>_-:<>>+!+^
                                             ,... .  ''..`'''...' '...'``^.'`'`'^.










```

*Figure from page 20 (2346x3317 px)*


---



4203-E P-347



SECTION 3 DATA INPUT/OUTPUT OPERATION



[Supplement] 4. Since no EXT-I NT signal is used in this example, bit 1 of NC optional parameter (bit)



No. 8 (No. 13, 14, 21, 22) (Ready signals of CN0: to CN4:) should be set to "1" in



advance.



(1) Timing Chart for READ



r;;7 --



"-""Pe;.;.;rip=he_ra_l-'



~ _device



Ready



DSR



Send data



TXD



Receive data



RXD



Data

- -



D D



C C



1 3



\ \ \



\ \ \



. \ \



Data



Within 100 characters Within 100 characters



Fig. 3-15 Timing chart for READ (DC Code Control)



(a) The NC sends the DC1 code.



(b} On receiving the DC1 code, the peripheral device starts transferring data to the NC.



(c) After reading the program name, the NC sends the DC3 code.



(d) On receiving the DC3 code, the peripheral device suspends transfer of data to the NC. Data



transfer stops within 100 characters after transmission of the DC3 code.



(e) When processing at the NC is completed, the NC sends the DC1 code again.



(f) On receiving the DC1 code, the peripheral device starts transferring the data immediately



following the data sent in the last transfer operation.



(g) The NC sends a DC3 code and a DC1 code during reading of each 256-character section of



the NC program (equivalent to a tape length of 0.65 m).



(h) The peripheral device sends the end of record code and data transfer is terminated.



(i) On completion of data reading, the NC sends the DC3 code.


```text


                                                                                                `^^^'".'^'```
                                                                 ...''... . ...'. . ' .. . .'' '_[-]>?^Iii]<I
                                                                :}-<ii~+[l_`!__~+I-[+<>i+_<i~~>~,!-_?~-_><<+<
            '''````^^^^^^^```''''``````'''''`````'''..'''''''.'''```'.''''`''`...'.'.`'.''`.. `'.'`.'''`''`'`
            """,,"^^"^""""^^^^"",:";;:"^^^^"::,,:,^^"^^^",,,,,"""::::::::::::,""^"",::::;"^^,,:;;:::""",",,:"
                 ^->l>!>illI<I   'i  `<l;;",,;i!l,i>;";I;II::^;::,,;l:":,:;::I^`I"^^I;l;^:;I",,"^::,::::,^I;:
                 `lI!>III,I,l;   'I. :]<;_l!+il!>:l~;"_[l__~!_?<<i!!<ii<~~i+_-+i+;II+>_>I<-~ii_i<_>~><~~~!-~<
                                     "+i !:i<i.^~I l>`<I.>+i,+<<~~+:<?~~-l,>,!~?I"_,l++<l^_!!i_Il_"i_;>i.i';i
                                     "-_<->>~^                       .
                                      ' .. .'.
                  ^<<' :<<~>_l<+>-!++,~[+~-!
                  .``   ..'';`''`^``^'``''"..
                                 ~"I!;l;`` li__~+~~!">
                                 ],<?IiiiI._;-1{(~i;:~
                                 .^..'`    .````^```^
                               ^       ,i;Il:,,,,::,",:::::,:;;IIIIII:::::,",,,,,:;;;:"""""",;;;;:,"
                              >~i<!    i;        ...    .........................'''''......''''''''
                              <[)?:    +;
                             '!!;:"::II<`

                               ^         :;;^          ';,,            .:,"             '^^`
                              l!;;:l!`   +-->          !~+}`           ;<+1.            <!++
                              -{}l,ll`   +l>!          ll!~            I;!{             !:~<
                             ';l>,"""",,;-i~_","""`^,,,>~_1;:,,,,,,,,,"<>i1"^`^^^^^^^^"^~I+]^"^"^^^'
                                 ..'''.....'!,''''..''''`']<`````````````'I!'''``````````'`}l`^^^^^.
                                             l            ,^;              l`             ';""
                                             '~`....'.....!.,~.            .<^...         ^! I!
                              "^              ~<,,,,""",::-:,[!             I-,:,^^""""^,,l~,:}'
                              <?~+<>!--:      >;    "",'  ;  l!             "!      '^^'  '"  !`
                             .~[]~^^`^^'....'.~l....l<+I.'I..!l....       . l+..    :>+i  :l  >`
                             `:""""^^""^^^":::l;,"""""^,:;_,,ii,:,,,^^^^^,::l!:,"^^"^^",::>+:,<;:;:.
                                                          <..l,                           l>.'>.
                                                    ^^``.`i:"!"''''.                      ^l^,l
                                                    <<>~:;<;I>+<<~~;                 '-+~~";+:!~~~~+~:
                                                                                      ...' .'.'''''''.
                                         .
                                        ,??i"-"~<.~+<~_il<<?!>~:~}++-;i?_l!~i_?:<><<i~~
                                          `^ .    .'''""''^^..^..`''`.^^`''^^",.`"^^^""
                    "-~ l~~Ii->"~<!~>!_i;~<l:,>!<!
                    ',"  ."` ^. ,"'""'",."^^ ',^;"
                    ^+l.!<,,iIi>:I!"!!"I~I;`IIli Iil,!ll!!!;i:I!;II:"il!i";lIl!;:;;:`l;I"l":I:"il^
                    `l: ^,''I;I:",i:";"":,"';;Ii',;;:iI:!:l:!^:!:II:"i!I!^;!I!!iII!_,>>>I>;;li">i,
                    ':: ;ii;.":;l:"^;;"`:"",,,^.::",'':,';;^`,"^,'",^.:","'`^:
                    ^iI ;!>>'I>iiIi!:!l;!;<>ii:^i<:>;"!<"i>"I+i!~II>>:>!>II<<-;
                    .", ""' ^''`'`'.:`.`,^"...^" ^"' `''``.'' .` ''  . ....'. '''`"`.'^'`^'.'."'.^^^ ."'`.
                    ,_+.><!:+<<<<!-!+<!i~i+l<<+}"<_+;_++?~+!-;i?i<_il<<_~~<->I+_i~_+^>Il]]+;_I?+l<]>'^-_]+
                        <<~>+_!"[~-_"<-[>l^<-~,~+<<~+-~Il?-<,<~!<ii~+<>!,_!-~l!~>_:!i_]`
                        ...       .          .  . .. .        . .  '.    .  .. ..' ...`
                    ;]~ -[_-<;_<<<~__>+l~~~~+;]_;<l!~<+_??__,I+~;]];!+>i+;<~>!-~!,!>i-,i_+~!.
                    .'.    '  ' ...'' ^^''.''  .....` '^'''' ..' .' '`.''..'` ''. '``".^I"`'
                     ~~ !>,"i!i>!!!">i,!<!;`!l<>.<<I"<l!il!l>"li;lI,"iil!,i!!!<!Iil;I!!^l!<::iIl!!iiiil
                     ,".~~~l+~<i<<-;~~<;!>!I>ii-lI+~>~~~+>->!I><i<-!!ll,I^:IIIII,;I>,:l"I!!;":::lII!!l!
                        ;l!Il;;<:Il'ii<,:>;:,:^!>^i>I"ll:!i!.!<!;><ll.
                    '"" ""` ""^.^`','  ^"`".''^' `.'..`"`' .'^. ` '' .```"`'.`^'`'^.^^"''`''''`'.'''^'' '`
                    ;]> li+l~-l:-+!-i!!l<!+;>~_~;_ii!!!~!l"<!]<,-><+]:~+__i[l~!>-~~;~_[l>~_<_~--"~_~?_<"+i
                       .-~!i?>,~i>_>->^_++><<[++<<l!!~]~!!]i-[iI+!>~1II-,  .
                        .        .'     .'    .  .. . ''. ' ^.  .      .
                    I+i l<-l<-~<-><<<;?~ii~:+_>-_:++;~<<,~ll<i>><I<<]Ii_>>l_-iI~>>+]~,>;~i!<<i_+<I
                    '..   '.''.'. ..'.'' .' ^'.'' .^ ''' ^  ```''.`^"'`"^''^,,`",":::',^:,^,,,;::^
                     >!.~~;;i!l<i~~i;:~:+<>::<<<i!;'_i:>_I">!;i;:>l"!ii!"Il~,
                     :, ",^^:"^l,:;:^^:`;;;"^Il;:I!':I",;"^!I,;;";I^;:;;"Ili;.





















```

*Figure from page 21 (2346x3317 px)*


---



(2) Timing Chart for PUNCH



r.:::-7 __



Pe~pheral



L..::'.:::.J



device



Ready



DSR



Send data



TXD



O2'



Data



4203-E P-348



SECTION 3 DATA INPUT/OUTPUT OPERATION


# I I

Data


# I I

-_ ------;L_:-t- -



Clear to send



CTS



Fig. 3-16 Timing Chart for PUNCH (DC Code Control)



(a) The NC sends the DC2 code.



(b) If the CTS signal is ON, the data to be transferred is sent immediately following the DC2 code.



(c) When the CTS signal goes OFF, data transfer is suspended.



When the CTS signal comes ON again, the NC starts transferring the data following the previous



transfer data.



(d) When data transfer is completed, the NC sends the DC4 code.


```text


                                                                                               ^^^"'".'".^`^
                                                                ''.''... . ..... . ' .. . .'' .-[-[>],I<!]-_
                                                               ,{?~>i_<-l+^i_-<_!]?+<<~~_~+_+<~,I-~}-?++_<+>
           '``````^^`''```````````````'''''`'''''''''...'''.....'.''..'''`'.'...''' `'.''`.. `'.'`.``''..`''
           ",,,:::""::"^^^``":,,":,":"^^``:,:;;;;;;;:,,,;;;;:::::::::::II;;:,,,,,:;IIII;,,:;:,;IIIIIII;::::,
                  <~. ;+i!!l"!il!:!i"!<l~ili`
                 .ll' ':;I;~::;ll":!^^:I;l:;^

                              ,;"",;^   ^IlI!!ll,":
                              +,~];<i"+:~_|{|}~+^^}
                              ,;::,;` . ,Iil!I^";;l
                                        '`'``^```''`^`^^"^`^^^^``````'''''''``'''''''..'''''''''''...
                               ^l;''    _""",,^^^^^^^^",:,",,,,"""""""^"""",:::,,,,,""^":::::;;;;:,,"
                               ~}}]l    _
                               l+-l'^^^^_
                               ''''`^^^^`

                                '.      '"^"^^^^^^^^^^^^^`^^^.           '''''..''''''.....
                              .":"`^^^. <<-?""""^"^``,:,,"::;~          ~,"":,,,"^`^",:::<<?+
                              "1?]li<>. <:~~      Ii!.       <          ~       .l!l     !:_]
                              `>->^^`'^^-!]-`^^^^";II"```^^^:_`^^`````'^~''..'''`;ll^''''_;-?.......
                              .`''^""^^^,^""^"""",^``^"""::,i?":;:,,,;,i],,^^",,"",,:;::;illl,,,:;;;.
                                                            i:         !;
                              `,,,,^",,"^^^""`""""``^"""",,"+          <"^^`````^`''''''''''`````'''
                              .;:'''''''''```'^^^^`'^^^^",,l>         ._",:,"""::,"""""",,,,:;:;,:::.
                              :~~_Ii;~<~.                  ^!         ._
                              ;i<~ ..'..                   ;_^"^^`````:_
                                                           ."":",^^^",:^
                                      ."' .`.^` "'''  '^. '..  ^ '''.  .'..' .  '  .  .
                                      "i_!"-,?~ ++<--~i__-<;_>:+~_[__!!_-!l~~__;+~<~i_+
                       ''  . .          ..           '                .              ..
                   ^?- ;<+li?<:-__-_i}_;+-+_;~~?~.
                    ..       . ..     .      . ..
                   ^]< _>_+!!<<-:~__~~;~;+?i:-~:>-_il>l+!!<<i~?>!<<;~:~i<!>>i<<+<~<+;>~+l<<!i:>>:<<><"!!<l
                   .`' . .. .  ..`:^`' ' .'. .`.'^^".' ^`.'^'`^"'"^ ^ "`^'`'^,:::;:I,^;:,;:,i^,I^:::;^;;;;
                   `il i-><<:~~lIii~:i>>i!,<!il:~<i",~>i;!lll~i^;,:lliIl;iI!'
                   ':: ^,^:,`"""^"^,`"II,,"i,;:.:"`'`;:;":;,:I;`,^^:;>;:"I:;.
                       i->>I">>;ll!+;>~!<<:!>!i<:<+!l+<_l.>>!l->"<~<~:!!iI~<!i>>l~<Ii__>Ii_!i<iiI~>;li!!!;l;
                       i<~<~~iI_><:^`,l","`""^,,`"^`"iI:^'^",',"`:;::""::";:,",i:";",III^::::;,<::I,;:;:::;,
                       ^,;^;l, I;l^
                   `lI ;!:," ,I,`^,;:;l:`;`,,::;;l::.;:":l;',,,:,`;,`;I,:'^^;"
                   "<> I>l<!^!~<!I!~i><!^<,!!!++~~~i`iiiI+i^~<i~<,i~;!<!<,>>-+.








































```

*Figure from page 22 (2346x3317 px)*


---



4203-E P-349



SECTION 3 DATA INPUT/OUTPUT OPERATION



3-5-3. DC Code Control TYPE2



In the standard DC code control described in 3-5-2, DC codes can only be output from the NC. In TYPE2



control however, DC codes can also be output from the peripheral device.



When this type of control is used, the NC uses the four control codes DC1, DC2, DC3 and DC4, and the



host computer side uses two: DC1 and DC3.


#### DC Code NC Host Computer

DC1 Enables data reading: Enables data reading:



(1) Starts data reading. (1) Responds to DC2.



(2) Cancels temporary stops. {2) Cancels temporary stops.



DC2 Sent to the peripheral device at the be-



ginning of a data transfer operation as a



data reading request.



DC3 Requests temporary stoppage of data Requests temporary stoppage of data



transfer from the peripheral device. transfer from the NC.


#### DC4 Terminates data transfer.

To make TYPE2 control effective, set "1" for both the standard DC code control bit and the DC code control



TYPE2 bit in the NC optional parameter {bit) for the relevant channel.



Example 1:



NC Peripheral device



FG FG



TXD



RXD



RTS



CTS



DSR DTR



DTR



Fig. 3-17 Connection for DC Code Control TYPE2


```text


                                                                                               .^^^^`^ ,'``^.
                                                                ....''...   . ''    ' '..  ''. l[-?]>> +I-?}:
                                                                ~1?<i++-_;~'?+?-~>[_+><<__>~+~>>^<__?_-<~+<-,
           .^^^``'''``````^```''''''`````'.....''''....''''.....'`''..'''''.'...''''.`..'''  .`..`'.^.''.'''.
           '""""",,"`^,,,,",:,^^`^^:::,,,",,,,,;;;:,,,,:;;;;::;II;I;IIIIII;:,:,,,:IIIII::,:::IIIIIII;;::::::'
           ,i!I!"  ,~>^ilI~;:i!li;,:>li_>I
           `;:,;^  `:"'",:l,':I:;;^.^^"I;"
                 iI;<!,<!I;iil:ii":!!+,"Il>;!:+!!l<ii!l!:!iIi^!>l"lI~il"!>":ll;;!,;;<!lliI!Il~l:<<: l:I!><~i:
                 li!+~!>+i>~~><:!<~!<+~<<Ii>!:-+<!~<ii!~Iiii>!l<i;l>~~~i~+lI<~<!+I:I!!!::;I::l!"ll, ;"`";,!i,
                 ,l:::l';:l!II<'`l;'II<>I^l<,^+!I^i;`il~lI^,li^:!i,>ll>l>:<.!+Il!!
                 I>!:;'l::^;";.::^::;,:^:.,:,I iI":!; ^,:,;!,`I"^.:",;,:'""l:`:I,,.,l;l^"l;I",,:,;l:: ,":":,'
                 i<<_>Ii><:-_~:<!>ii<i<l~:>_?_I~<>l_<l~-<!!>>:i>i"i!i>ii;ii+~ll<lI^;>l~;:<!<I<i<I<>li`+!~I!+:
                 !i><^>lI<ll_::+~+`i<~l"<>"`<ll^I<il;<l~
                  ':^:;;;;;,,,"^":;;::;;::;;:,"",",,;:;:;;;:,,,:::::::;;:::"""",:::,,"",,^^^^""":::::,""""""^
                  i+`I1[!>_][["^;~'`''''``'''`''''<}];^^^^^^^^^^^^^^^^<:'`'''''```;?-[[>_~_---1[;"""""^^^^^^[.
                  !_,:,,~>ii,;:,l+_i!>>!l,!!<Ilii><i!^````""""""""^^^`lii;i>i>lliIl;!>i<~<i!i!l;^````^""""""{.
                  !!   .!l;"    'liI<-~>!^i~~,:<<<!!_                 ,i>I_+i~;;_<~^l><_>_l                 ].
                  !i            `l;!. -~__<'+_~,:i>~i<>               ::lI :-i>il!l+:I:I_>_:                _
                  lI            'IIi`.!l!;I:I;!;:IlI:II`,```          ;:I; ^IIl!l!;!:;:,;:l" ''...          ~
                  I!```'.''.`^^^:>-?"^<~+<+?+;]~~-~<+_;i[--?^`'''' .`'<>[_`!~]_+-?i<]>_-++??!?-+]<'.'''''``^]
                  !i'''"?-_-`^^^;+?~~>l!;-_l<_>_+~!!<,]<><+:]i-+>>~!''+:'^^^^^``'.''..`````^^''^^",:I!!iii!!}
                  iI    "`^^    ^!~?<~<+:~<i!]<[!>~__?{~!??<??_-i!{!!.i`             ...'^^^"",""^^`'.      ?
                  iI            'I{]?~>1~_<_ii-+>i-[;l;^'!;;"!:;`"!`!'l'  ..''`^^""""""^`'..                ?
                  i~,:"":,,"^^^"l<_-->l><>>i-;<~-+~~:''.'   '.^^^^'^^^<>!lIIII;;;""'''..'^^^^`^'..`'`'..'^^"-
                  i!...^_-+-. ..^!__+~+~_?;_<<_>>~~l!1+__][[l!-!}{{;`'I~[~~>_+[<l]+_+<_-+!_{_[]]][l?~~{{-^`^~
                  il .      ....^!!+~_]]I_<_+;}-!~-_<~+]?+>(__+_:``.  ;>+]-[[+l?<?i_{_!{[>'`'^^`:".` '^^^   ~
                  >>`^`"i<><,,,,l~-~>i<>i~~!<+~+>~>!~~>I;;,Il;Il,``^^`~ll!Illl":I;::I>Iiii;:,",:,,::;IlII!I;[
                  :!^^"l]-+-",,,!<<?_~]~[1[<_)}[<_-+-[}I^^"^^^^'````^"_!IllIIl!II;IlIIllIIl;::::::::,,,,""",]
                 ;:";I!I"!Ii<i!;;;;;::">I";;;`";;":";,"I;>Ill;;!;;;I;l!iiIII!l:::;;;lII:;:I;:,I;;"::;:::;l;;^
                 >_i+]_~;lIi!_<I~<+~>i<~_><!+;l-~`I'<+;~<-l!+iI++><-+>!>i"!i~_;>><!i>~~!_i<i~~i<i:~i+i!~>?<>^
                 :;<!~<"><;>"+-I+_;,]_-i!?Ii_~->~-_~"[]_:+Ii-~:<-_i+~>;<>-!>[l
                 I,,",:;"^"   .     '......'. .......'.' .. .' .''.''....'..`.
                 <i~~i~>I^,
                      ``'.`""",""^"^",""^^^^^^^"""`                            ^^^^^^^^^^^^``^^^^^^`''`^`^`
                     ;{;l~~IIIII;:::;I;;::::,,,:I,],                          ~-:,":::::;;:I>!iii!!llIl!I;>~
                     !_ ^>;                  ;!l l+?i;IIIII;:;;IlI;;;;;;;;;;;~-_;I!        'i><i<i!:<!li` ,~
                     !+                      .'^ "+>"^^^"""^^^^"``^^^^"^^^^^"I_~"^;.                      :~
                     !~                           +I            "^            _i .                        :~
                     l~                      :~_;i_}<!!!lllllliiXa]!l!i!!Illl?--i-_'                      ;<
                     i~                           ?:            "'            -i                          :~
                     >+                      ^,"^:_<"^^^^^^^^^^^`+(^^``^`^"^"I+<"I:                       ,<
                     l<                      :<<;!--I;;:::::::::;rL;;:::,;I;l+??;il.                      ;<
                     i~                           -^                          ]!                          I<
                     >>                      ,!l;<+[iIIi^                IIII?_];+~'                      ;>
                     ii                      '"^"'?;'..>!                ]'.'^]!.^^.                      li
                     >i                          ^_I'''<!                -..'^]!                          ii
                     <I                      ;<~<~_?lII!`                !lll[_-">_`                      >l
                     <;                           1                           {`                          <I
                     <:                      ;<~i__?III!.                Ill;?__">I<^                     +:
                     >^                      ^""^:[:``'],               `]^^^;]I.' '.                     _,
                     _^                       .'.'['   ?"               ^?   .{' `"                       +,
                     +`                      I~i>?+[IlI>'               .~ii!}+?'~_'                      _^
                     ~`                          .{                           {                           +^
                     -`                      `,`.>-i""""""""""^^^^^^^^^^^^^""l?I.;:.                      <`
                     ?.                      :+I <]+:::;::::II::::;:::;::::Il-_i >i.                      +`
                     _!IlllI;llll;;;Il;;;;;II:,:Il]                           {":""::::;,,,,:,,,::,,,::","]'
                      ``^^^^`^^^^```^^`````^^^^^^^.                           '"""""""","""""""":,""":,"""^


                                        ^-+>^_">I'+>>><~+_<l!_;!_~,>ii-Il>!>>!i:i<~_<l
                                        .':;.".`. ^"^^":,,,`','^""'^"":^`"""""" '^'",^





















```

*Figure from page 23 (2346x3317 px)*


---



4203-E P-350



SECTION 3 DATA INPUT/OUTPUT OPERATION



(1) Timing Chart for READ



r;;l _



..__Pe_r_ip-he-r_al _, L.:::.J



device



Send data



TXD



Receive data



RXD



Data



' '



\ '



\ '\ '



\ \



\ \



Data



Within 100 characters Within 100 characters



Fig. 3-18 Timing Chart for READ (DC Code Control TYPE2)



(a) The NC sends the DC1 code.



(b) On receiving the DC1 code, the peripheral device starts transferring data to the NC.



(c} After reading the program name, the NC unit sends the DC3 code.



(d) On receiving the DC3 code, the peripheral device suspends transfer of data to the NC. Data



transfer stops within 100 characters after transmission of the DC3 code.



(e) When processing at the NC is completed, the NC sends the DC1 code again.



(f) On receiving the DC1 code, the peripheral device starts transferring the data immediately



following the data sent in the last transfer operation.



(g) The NC sends a DC3 code and a DC1 code during reading of each 256-character section of



the NC program (equivalent to a tape length of 0.65 m).



(h) The peripheral device sends the end of record code and data transfer is terminated.



(i) On completion of data reading, the NC sends the DC3 code.


```text


                                                                                               `^^`', ^`'``.
                                                                .. .. .    . ..    .      ... ^?]-?>[.~l~]-l
                                                               !1]~<+__]l-'~+-__l??~<>i~_<>+_>~^>-+]i__><~[<
           '''''''``''```'''''''''''''''''.....................'``'. ''..'..'..'''' `.'''`.. `..`'.^''`''`''
          ."",;;;:::;;:,,"^^"^^^^^^^:,":,",::::IIIIIIIIIII::,:II;;,,,,,,,,",,::,:;;IIIIII;::::::;;I;I;;;:::^
                 `I:  l!I!I;"ilIi:II`!+I!i"
                 ";I  ^;;ll<"I:!i,;!^;>ll!"

                        ,!:",l^   :;,I;IIl;::,;'
                        -"I+:>?~;'?'`--[}-~-;._l
                        ~Il>I+!"`.[,,??+-i^""^_;
                        .^`'`^    '^^'^``^",,""




                         ::      ^!!<                ll>'               lI!                     ::I.
                       .<!!II~<" >!~/               ']!f;              '-lf'                   ^-!rI
                        ]]],`;,. <:I{               '_:(^              `i^).                   "~:("
                      "",;;"^`^,"}<I/^"""^^^^^^`'''`,[;|:'```''''''.''',+^|'.''''''............;_:(^........
                      ^^"^^"""":,+i">~,,,",:::,"""",;-"!_:",,,""""""""",;,~~:,::;I;::::::::::,,>]"<-:;II;I;:"
                                 i^  ^!             `~  'l`                "l.                 :>  "l.
                               . i^   `!I           'l   .ll                `!;                ,I   'l"
                        '^       <^    .]+:;II;;;IlI>?I;::;)+                 --;:""""^",::;;;:~?;;;:I\>
                       .!l"""^";:~'     "< ..,:;,...:i.....^-                 '_'''''':,:^````'!>`^`^`:?
                       .]][<IIl<<+      l>   :!<!   "l     "~                 ^>     .i<~"     lI     ^~
                     .^^!ii"''...+"^",,^++`^`'. .``';i'''''I?'`'..''''........:_......    .  . iI . . :_ .
                     ."^```^,,"""-::,;;,<+;;;;::;;I:<+,:,::!?;;:,,;;;;;:III;;:!>I;;::;I:::,::,,_<;;;I;<];;::`
                                 +  ;;  ::          ;I     "i                                  l"     ^>
                                 <l^,;::+,          ^~;::::+I                                  l_"^"",<:
                                                 .+++>:l_;!<+<<~<:                         '+~<+;!_;i~+iiii,
                                                  ..... ' '''''''.                          ^`^^.'"'`^"^"^"'
                                    :`. ^.`^ ,`''' .^'.'.' ."^.'' '``.'. ' '' .'..'`'`^''
                                   `~-_^-"<_ >>+<__;_<_~l-~:[}<-_,<+_:<<>[i!~+_?~i,i>~]_["
                                                  .
                   '^` ""`'",^'`''^'^"''"^^'.''^.
                   I]< I!-I<]l;]~i]>i-~;_<!,l~~}>
                    .  ..          .  ...       ..      .
                   ![>.~_!!]+?_~+[l++l_+<!"++]-^-~~l?~+[~_i-"-]>+-!!----;<_~+-->_<_I??-!+I~_<l?_:
                     .           .                  .  . .    .      .    ' .    .".'''.'..'' ...
                   ;-i _?[+"+--}+_!+_i!_>?<_<il<-<-"l-+:}?;l+-!<-~+};__l<_<_:<<_-`
                    .. . ..   .. ''  .'.."''   '' ..  '     '. .`.'`  .  ..'.''.'
                   ;?< !<:;>l<iI!>;?~:i>i~"l!-> >iI,~il<>i!_^iiIl!":I!i!i;i::l!I!~!`!:i__!l>:?>,<~i :<<~!
                   `"^'+<>>?-i!_<]<l_+__II>-ii-!i>>++~l<]->>>~~<~~i<<<+l+>_<;<-<-l<;+I;I;,";`::`":, `:;;:
                      .::;;l!`"!l!I'lIIl` :l^^;!IIII;;":!!;'Il;lI,li;I"'I^;l",I;l`I;!>
                   ";" ;;""^ "^'`"",^^ "^;,`^I:.^.'`^^""^`^ ^^`';, '``^, :^.`"^` `'^^ ^'^^'
                   I<I iil+l:~l!i~~<l-;~;!~>,_>">:!~><<<<~<^i><:_<"<+i~-;__lI~i;^><_?:-]-<I
                    ^` ^`  ''''''  "' ^`^. .... ''.  ......' '.     . .     .. ..      ' . .....''...
                   '-i'<<I!_>~i~~[!]+;!~!;:+>-_'<>>l_+>_>-<_^?->~_Ii--+_;<->+-_>~+-!+_;???!!~<i++-?-+<
                      `--_<+~+<+~+:__-;>->i>l>?+:___!<~i~->^_~+i--<<'             '                  .
                       '. .. `^    ..'.''     .. .'  ''.''. '`' ''.
                   I-i !i+"~-;;~il+;;;<!i<"!l>l,>l;;;i>l:`ll~l,<;I!!,ii>_i<:<;><><"__]:><>i<i~i^i>i~ii"<l
                   `l^'+ii>+~:<+><~~i:+i>>!~-<~l~I!l>>>Ili>>-!;_<!+);>-l:,i":':;;"':;I^:,;:l;;;.;;:::,`;^
                      'I;":l""!:i<;i,'ili;IIil;"l^I,I>!::>;+!^,l:IIi";i'
                   "I" :"".',"`:^^"`':'```.```"^`:`.``^.^''`.`^'.''^'.'^^^,,`^"^^^:^.^'"^^^^`^`^`
                   l<l ;l<;<_!~><>+i;~>!><,~~!<>l~<,>><">:!<i<<!;><_;i<<I>-?i!+~>_-_`~;__><<+?++!
                    `. ^' .. ...''.  ` ''.    '.   ^  '^'    . .'  '''.   .
                   .-I'~<;!~<~-_]_-l!_;[-_;>__]~++"_-I~[!l]_i_><__l-~+<l++}!
                                                 .























```

*Figure from page 24 (2346x3317 px)*


---



4203-E P-351



SECTION 3 DATA INPUT/OUTPUT OPERATION



(2) Timing Chart for PUNCH



r;;l __



.__P_e_ri-ph_e_ra_i _. CJ



device



......



Send data



TXD



Receive data C



RXD 1



Data


# I I

Data


# I I


# J1J

Within 2 characters



Fig. 3-19 Timing Chart for PUNCH (DC Code Control TYPE2)



(a) The NC sends the DC2 code.



{b) On receiving the DC2 code, the peripheral device sends the DC1 code to the NC.



(c) On reading the DC1 code, the NC starts transferring data to the peripheral device.



(d) If reception processing for the data transfer cannot keep pace with data reception, the



peripheral device sends the DC3 code.



{e) The NC stops data transfer within 2 characters after receiving the DC3 code.



(f) After completing the processing backlog, the peripheral device sends the DC1 code again.



(g) On receiving the DC1 code, the NC starts transferring the data immediately following the data



sent in the last transfer operation.



(h) The NC sends the end of record code at the beginning of the transfer data and the DC4 code



when data transfer is completed.



[Supplement] If the times t1 , t2 and t3 overrun the set values for the ready completion waiting times for



the RS-232C channels set in the NC optional parameters (word), an RS232C device



reading error occurs.


```text


                                                                                                ^^^`'" "'`"`.
                                                                .'`.''..  . ' ..  ..' . .. ''. :-?-_i] ~l+[<^
                                                                !1]~!~+-];_.___~~l[[~<<>_->~~+<>"<?~]+_+~<+?;
           .^`''````^```^^^^`````````````'''''''''''''....''''''''.'..'''''.'....'.' `.'''`.  `..`'.^'''.'`'.
           ':,"",,"^"::,""""^"^^^`",,:,,,`^^^"""",;;;:,,,,;;;;;;;;:::;IIII::,,:::,::I;IIIII;:,,:;III;II;:,::^
                  ^~!  l<!!!!:>!!!,!I`~!!+<!l
                  ^l;  ^;::I~^::!;^:;`,;;!l:,.

                               :"^",.  ,""""^^```^^".
                              ,-i-I<!:l_^!??[]-_]^"l>
                              ;-I~:~!!~~`l?++?,``'';>
                               ,"^""   ::,""":""",,:`


                                   .`'.        `````'''```````''`          ''''...'''''''...   .
                          :,       ?!)l       I>"""""`'',::::;::i<        _;;;:,,,""",;;;:::+.;_}>
                       "[+-li_~'   +`);       ~;     :Il^       ,+       '-       ";;"      ~ <l}-
                      .^>]+'.'..  '-,\:       <,     ,li:       li       `~       ,!il      ? ~`]i
                     .;:,:,,:;::::I~I_l:;I;:::1I:::;:"^^:Illll;:~<;::::::<-III;,,,",,"::::::_;-l_<:::;;;;;I"
                                     i'      l+                "}       .['        ......... . .  ..........
                                     <'     `-                 -`       <,
                         `'          >.  ';"i^              ,"l;     `^:!
                         "`          >   !i?{              "?<|      +l/,
                       :?ii<i!__<    >   l,-[              ,<i)      +^|,
                     .'l{[-"^^""^...'<.'.<:>_..            I+<)     .-'[`
                     .:,:;:,;;:,":;;I?:ll?!IiI:,,,,;:::II;I>~l];!;:;I]:~l::::::::::::::::::;I;;I:::::III;I:'
                                    .>   i'                  .> i'  `<                               ......
                                    'i !'i'                   > i ^"'<
                                    '?l?!?.                 ,>-^-;>~i<
                                     .   '                  .`^!<iI"i:I;:;I:"
                                                               ;I:l,""!i!i>iI

                                    ;"' ".^" ""^`'.'"^'^`^'':`"""^`."^^'^''`.^'.''..^`^"^''
                                   .i<?'+"!_ l>+<<?l~<-+;+<:~<_?_<>I]~>;~<+};<~++~~lI!+++__.

                    ^,` ;:^'::^`^^`"`""``,,,^'`^".
                    !]l !>_:~-;l_>!+Ii~<,<i+ll<<[;
                    ..  `.    .     '  .'.'   .  '.   . .. .. .  .      . .  ....        .  ...
                    i_I'~<Ii_<_<<>]I_-I<_~_:~~?+`__>!]+<?+-+?:{?<~-I~]+~[I_~<i-~>:~<_]:?;~++!{-,
                        .         `   ..        .  .'.                               .
                    !_;'+~:>]--_?~!__!-~>;i+-1I;]_I]]ll]-_]I~-~+[_!><_;-__I+l>+<I__<-~->?!!?<<~+.
                        .        '          . .        .. .  ..  .  .^ . '    ...'''` '''  '..'`
                    !-I.~,<ii<~<i";<l><_<!!i:~,l_i`<~_;;i<i-]I,>_ii~I<~<~,!~<~,i+]"l~-!">i>i~iI,^_<;
                    ``'`>>~<__>~iI]<~<~I_<<]!<_iI-<~_!<i[i^""`'",^^,`",";^::,,',,:'";;:`:,:I:,"^',:"
                       `;;";^,,:`^I,:":.I:,::`:;`:",,^;;!"
                    :!" i;:^Il^^;,",.;:I':,""l;``,I""'".",:,:::,"`ll:`^:",,,"^^;"^";,;'^^,"
                    li, ::l"!!";ili!"><<:!>ll>+:,>il!"!"><~!<!~!!,-~~",~!~iil-;<~I!>!<"<>~~'
                     ;` :l"` '^`'^^"^. "^..'...'''. '`.^^.  '`  .` .''... . .'.  ... .`  `'`'.'.'.. .''
                    '-:.<--l"<>!>~++i?li~I~<>~~+_!~<!-~+-~[,i~<;_-i_>_<?l!?~>+~l?~!_><?-l-~!II_~-!i[[]<'
                    '   `. .. ...   `. ''`.   '  `..'..   .'   . .      '                  .       '.
                    <1;'<<:>+~?~i~+l-_,>~i";+>[>']~;>]i;[]+?l<--~[]<<-[i-_li[?_I><>~_--[_?;[__+-+_>i_~;]]?,
                     . `--_!<;i~<l]-i<~<>-]!,~<+~->>i                 `.    . .    .. ...'  . .. `` ...'''
                       .^' .  ... ''...''.'. `^''^''`
                    <~, i!i"-<"Ii!I~,<!;"iIl,>^iI;I!,ll+<"+I_i;i>i<!IiiI:<I>!,l!ll<<,:<<i^!lI;i!:!<li"I;il
                    ,"`'><~!li!_~><_!<->;~li!<!++_>~"::II^l^;;":I>i:,;l!";^;l^:l;;li",>>!"iII,I!:;l;l,lI!!
                       'i;!l^;>~!,Ii;!!I.l^IiI~<i<!!.
                 ;:^"","```"`    "``''`'`''' '` ..'^^``^`''',"''`^'`^'```^'^^''`''`..'`'''`''...'`' .''.'''.
                '+~+_<+_<+~-! . ^~!<-+-i?_i~^<~!+~>-iii+<ii;~_~!?+;<_<_<l+;l~<;~+~_li<><_-_><l~--]i->?i<_!<>.
                                ^>i"l_<:~~+>"!<<<!i+>"__:~,<<!;{+^i~~>>~<:~<i+i~+-<l:_>~i+.l_"<?-__{_;I[<>><.
                                `>~>+>>;><!i">li!!!''.`'.'..'` ''.`"'`'^``"^`"'^`"`''"^^`"'`"..`^^^"`'`,^^""
                                .:;;;,!:;,":';,::,:





















```

*Figure from page 25 (2346x3317 px)*


---



4203-E P-352



SECTION 3 DATA INPUT/OUTPUT OPERATION



3-5--4. Slave Station Function



If an attempt is made to transfer data between two OSPs, it is normally impossible because both of the



OSPs function as master stations. The slave station function allows communication between two OSPs



by making one of them a slave station.



In the slave station mode, an OSP operates in the same way as a tape reader/punch.



OSP master station l"•lf ,-------•.. ..



l_ _



o_s_P_s_la_v_e_s_ta_ti_o_n _ __,



Master station (not OSP) ------- OSP slave station



Example 1: Example connection to a peripheral device when using the slave station function



Slave station



Peripheral device



Master station



[Supplement}



EX-INT



DATA BUSY/



Fig. 3-20 Example Connection (1)



Since an EXT-INT signal is used in this example, bit 1 of NC optional parameter (bit) No.



8 (No. 13, 14, 21, 22) (Ready signals of CN0: to CN4:) should be set to "0" in advance.



(a) The timing chart for READ is the same as the one shown in 3-5-1 (Example 1).



(b) The timing chart for PUNCH is the same as the one shown in 3-5-1 (Example 2).



(c) When reading, the tape feed data following the program section is ignored.



(d) When punching, the tape feed data following the program section is not punched out.



(e) Notwithstanding c) above, if the end of record code is NULL, one character of NULL data is



punched out.


```text


                                                                                               ^""^': :``"^'
                                                               '''.''.'. . ..''. '.' '... ''' :?]??<].+I~[]l
                                                               >{->i>~?]:_.+~+~_l]}<>+i++i~?_>>"<~_-<-++~~?!
          .`````````^^^^^^^^^^``'``````````''''''''''''''''''..'''''.''..'.'...''.'.`.'''`.. '..`'.`'''..`'.
          .^^^^",,"`^""",""""",""^^``^:;;;;:,,,""":;;;;;;;;;:,,:;;;;;::::::::::::;II;IIII;:::,:;IIIIII;:,,,^
          "~!ll"  `?<li;l_i~lI^~;Il<>i,
          ';,,"^   ;I::^`::I:"`'^":I;I`
                l;ll.l_<!li";;:i<>!^!'>!ii~~;,_~i,>>~>ii!^i!l">~+>i l,>`!lIl>il`;lil!!i!!"i!;l:;<,iI>l`!,il:
                I!-?<!<~!>]I!;il!<<i+!I<<~+<lI:i_!i!_~i>;l<_>l!iil~!lIil~>i>>>~ll>~>~<<+<Ii~>~>i_l!<<I;_i--l
                I!ii!ll<IliiI"~!:!>_<<^~++~!!<.`;>!,~<l!"<>~i<,;!i!+lI"~i!<>"!!!!!!!!l+~!!,<<i><>i"<<I,!+~!l
                ;+,li-~!+lI!<"!;ii~i"i;~+>>">~]~<!
                ^^^:^.^"^"''"^^''.^`^". ^``,::`'``^`"^''`'"`.''`''.''..'...`.'..'.''.'. ..'
                l!I__;+?~~l!_-<<i,~~+]l,[Il~--"i]__~]-<li:+-;<-~<>l??~I[lil+}?<I_-+]~~-ii~_^

                           ^:":,,",:`'''''`'''`",::I'               .,^^^`"^",^''.''...'^,,,:"
                           :'  !<]-"><_+_!:--+!i"  ^_:^^^^^^""""^^`:_^  .!~_+,>~!>;!~~<!i.  'l
                           :^.."";"',:lIl:"II:::`.."l`'''''''''''''^i"...,:I,'IIIl:I!iI;;.  'l
                           ':"^``'^"``'"":,"^^``^^":                 llI;"^`^"^^^"::,"""",,,:^
                           :,!I:I;"^::I",";:;::Ili:";.........    ..;"^^";;;l,",""^"::;::`''^;
                           l^__--_l,~_?ii"<!~Il<-<l`-:^^^^,,,"^^^^^I?.   l<-~"<~~~;i+-_>l   .I
                           ,,''```^"",","^^^`^^```^;'               ^I"""^^``^^^,,:,^^`^^"^^""
                  '          '.             .
                 `]<--<_]<,; ~+~-<-?+:~<_+-+-~>I-;>!--~-__~_l>}><~<:?-->"!_i_!<+<:?-<~;_+-~<;i_~<]<<^
                   ..  .          .          .  . .``'.^.''`.'`''``.`'^'.`^."" .. '`'' ''`''. ^'```'
                     !I;;Il!llIIlIlllIII;;lll;Il;!.                          .!;;;;;;;llI;;I:I;;;:,;;;I;Il;
                    "]''<~:..  ...''''''''''",^`^[i                         .~-```'''''''''`!l!!!!!:l!l>l^{
                    ^-  ~[~!;~+i>"          l<I <~]~!!lllllllllllllllllll!lI-_-:"<>         -{]1-~]?]]ll,.?
                    "-  .'``'^^``.               ]I                          <>             ^,""^.":"^   `]
                    "-                      ,,".:?<,^```````^^^-|:`^^^^^```^:+~`':"                      '_
                    ^<                      I<<^!_-il;;;;;;;;lIrZ+;;;;III;II~_-,`iI                      ^?
                    "-                           [,                          <i                          ^-
                    :-                      i<i">_]illIIIIIIIIIIxCIII;:;IIIl-+-",?l                      ^?
                    ">                      ";:`"]>"^``````^^^`^_)``^^`````^:~~'',`                      ^-
                    "+                          .}I                          ~>                          "-
                    ,-                      !<~l~_[~iii!!l_.        `~liil!l?_]:`]~                      "?
                    ,~                           {:       }'        ,i       _i                          ^_
                    ,<                      ^^"'I?~,"">f!,1'        ,_^t\;,"l_+`'::                      "_
                    :~                      lI!;l-_I:;]O+;:         .;:vXi;:<__^`ii                      "?
                    ;~                           }^                          _l                          ^-
                    :>                      !_?!~_[!ll!lIIIIIIIlcLIIIIIIllI;?_?""_i                      "_
                    ;~                          ^[I''.'........'>?.'....''''^_> `;"                      ,-
                    ;~                      :!" ^[I'............  ....... ..`+i.                         ,_
                    ;~                      ;<; -~]>i!illllllll!!lllllllllll-_?^"_<.                     "_
                    :<                           )`                          ?;                          ,~
                    I+                      !<!^>--;;::::::::;:nX!::::,;:,,,<+_^'::                      :+
                    i_                      ^:,';?>,"""""""""""|t;""""",""""l-~'">i                      ,+
                    !<                        .  1^            '             ];     ..                   ;~
                    >i                      >>_l-_[!!i!IlllllilmZ<llIlllll!l[_]':~!l~I                   I+
                    ~!                           {             ,             {"                          li
                    -l                    .I,";;<->""^^",^^^^^^"(?^""^^^^"""!?> '"""^"^""`               !l
                    ~"                     >l:!;<]~::",::,,,,:,!U\,:;::::;;:~_i ^!!lI!!>l,               Il
                    ~~ll;IIIll;;l;I;;;;;;;l:::":l}                           [,"":""""""""::::::::::::::,<;
                     `````````````````````^^^^`^".              .            '^`^""^^^^^^^^^^^^^^^""^^^^^"

                                               l;" ;^I; I,"",^;"^,^"""^:"^'`"'
                                              .!>[`<l+<.~<~<i~?<;>><>~>_+>:!!;

                !!:::l::::l:   .!;":"","l;l":l!",,,",""'",",,^;:,^"^""",".,,^^^,,:"'`"^^^^``^^^^`"^'^""^:"'
               '~>~+<~ili!>!   ._><_!i+!>>>">_!:_]++?;>I>~~li;><<!-+-<]~~"--:;>!i+lI~~<>i+l+_>?~-__;!_~I<_l
                               `~;?-: i~ :~^ii';?_"_-?~+],-?~~]~:?l<-?i,-;>_?~I:~>i!~I__;+]l<:,+`~:>+i<_l~i
                       '                .  .            .  '.           .     . . .      .. .. . '.''.''.''
                   >[;.-__I?~<<+;~~?+i?Ii}}~[+;~!-~;~+<_!!];-_i;>+!!_<<_!,<;+i>I,+?i-~<+-,!i
                   ...         `      .   . .. ' .. .'  . `  '. .'  '.''  ' ...  ^^."'.^`  ^
                   ~_:'+><;<>~><;+<~<l+li-i]+<_l>;i<!:~+!+"<i:<>"li<,~ili~:i:ll<:,'-l!<l!il"_^
                   `^'   ^ '`'';.`',' `'  `^`''.^..'^'",'".,".`"'^^,.,`",,'"'^^,'' :^,;^l;:^l^
                   ;!"`_+!<I^!!l<;l.>i;:<!l"i!!I"!>i"li!;l!;"!!:"I;:lII:`;;;!:"":"l:,::I.
                   ":^ ,",;"':;;:^i'::,`ii;':lI"^l!l^:l;;l;>l:l:;!:iilI,^!IIl;",l"?;II!i`
                   ,l`'!!":"^"^,:;,;''I:.",:^::":',:;`^""`"^^^`,".^`^^`^" `^`"^^." '``..^",^^"`^^'
                   l>".i!I<;:illi!!_i"><"i_<!l~ii,~+~l;>l!<!!-;!<I<l~]i~i,>_>ii>,<,l~!>>><<!<i:><,
                   `` '".^'^,.^`'`^.... ^.  . `'^'  .'. ' .  .'  .`   .`..       ..   ..  ..'..   '.. .
                   ~-,^_i+__~>--<_+~_l<;{~i>+^~i-_I~<-l<!l->~<>l<~{>i~l[<!>::~<+;_+-~?+[!:+:[->i;I??-;-,
                      "~li>i~~;!+i
                      .`'.'.''.''.









```

*Figure from page 26 (2346x3317 px)*


---



4203-E P-353



SECTION 3 DATA INPUT/OUTPUT OPERATION



Example 2: Example connection to a peripheral device when using the slave station function and



DC code control



NC Peripheral device



Slave station



FG FG



Master station



[Supplement]



TXD RD



RXD SD



RTS cs



CTS 1/0 BUSY/



DSR 1/0ALARM/



SG SG



DTR DR



Fig. 3-21 Example Connection (2)



Since no EXT-INT signal is used in this example, bit 1 of NC optional parameter (bit) No.



8 (No. 13, 14, 21, 22) {Ready signals of CN0: to CN4:) should be set to "1" in advance.



(1) Timing Chart for READ



Slave station Peripheral



NC +- device



RXD DC2 Data Data DC4



ATS



Fig. 3-22 liming Chart for READ (Slave Station Function)


```text


                                                                                               `,",`,^ :',^"
                                                                ```'`'''....'.``.''`' '.'..''..>?_?~?i`~I]??'
                                                               .?]~<i<<[~>l"+~~_i>]->i>>+<!~~i>l,_~-~~-~>>~-`
           '^^^^````````````````^^^^^^`^^```''``'`````''''```'``'''`''`..'''''..'....`'''`''.''.'`.'`'``''''
           ^:::::,,^^`````^^",^""",""":",,"^^```^^:,:^^^`^,,","","",:",^^""^^""^^^^`^,,:,"",,:"""""",;,::;II.
                  ^-I>!!i~,i, ~lI!;li;`;:,:I:>l!"i`;"!l!lllIi,Ii;ll:">ll:';!lI"<!:"il:I`!!iII^l:;;l:;`I;I
                  ',,l::lI":^ ?]]<~]1];_~~_]~III^I^;;!Il!:!;i,;i;Il;,!;!,^liI<!l!;,iiI!"i>i!!"I!;!!l!,<!!.
                              :;,'I:!l^;,;:I"

                        `<liiiiilliiii!!!iiiill;:;!il<                           ;ilIIl!llllllliiI;II!!IIlll!i;
                        I_.>{l....'............`;,.."}l'.......................'^{>',"........ "><<<+>>;+i<~'l_
                        ;< i_~<;<_->:          ">i. _~[>li!llll!!ll!illlll!ll!ii}+]"l<'        ,]-[]!~]?+~`` :<
                        ;<                           ['                          [:              . .  ..     ;+
                        !~                     .lil !-~,,,,,"""","\w\I"""",,"""">_~^!l.                      l<
                        !~                      ";: >-_;;;;;;:::;:n#nI::::;;::::~_+^lI.                      Ii
                        !<                           1.           '  :           }^                          I>
                        <~                     "_~<.++[ll;;IIIlllIIx&o!!;;;;;;I;]+?"~!.                      l<
                        ><                     .^^" ^1I```'''''``' ;fc``''''''''"]l.;"                       l>
                        i<                      ''' '1^           _-.           '{:  .                       l>
                        <~                     .<<+'?+}lll!i!!lI!l0$O~lll!liii!!}~]`!_^                      !i
                        i!                           {            <I             )`                          il
                        >!                     .Il!'i_<^""",""^"""^]LX""",,"""",i-<.,:^;"I,'                 <l
                        +i                     .::l.>?~,,,,::,,,::IfdU::,:::,::,~-<.;:"iI!;^                 +I
                        -l                           1              ^!           1                           -;
                        ?:                     `_?_:?+[lllll!lllll<L$LIl!lIIl!ll[+_.~>l+l++-"                +"
                        ?"                          "}.           .;\[ . .      ^{.    ..  .                 +^
                        -^                     .l;..!]:''''`'''''''   '''''''''';]" ;:.                      ?^
                        _^                     'i!.`?_-IIIIllI;IIl:Illl;;;I!I;ll]+~ <<^                      ]`
                        ?`                          ^[            '              1                           ?`
                        -'                     `!!>:-__III;;;;;::;ad(;::;::;;;:l__<.i!^                      ]'
                        ]'                     .^`"'>[:^^^^```^^^^Qu<^^^^^^^^"^">], ,".                      [.
                        <iIl!!l!lll!!llliii!lllllI;I!i                           -l!l:;!!lIli!lli!ll!!llllll!?
                                                                                  .........................''
                                                l;` ;^;" !,",,":^":"","";",'^I'
                                               .l~~'<l>:._>_+i-<!;>>i~+>_<<,!-:

                .>l",:l:,;:I"   .!I","",^!;!::Ii""",":",',,,:,"l""`,"",,;,':"^'^:;;"`^,,^^,^^"^^^^""`^":^:^.
                '~<><<~il~><;   '-__~il-!i<<,>_i:-]<+?!<l++~!iI_iii__-~[-+,?+::<I~_ll-++><?>--<+i-~-;>~+l<~:
                                ^_:?+: i+ :>`>i'!?+"~-_+__,<-~<?<:>:>+-;:<,<__<;;~!>!_!>+:++;<""l'~"++i_~l~;
                  ..  '` .   ..   '  '' .'               .  '.   .       .     .   ... .. .. .    . ...'..'.
                 '>~" "~>++-<<_<-ii-;<}-+[i
                           ''   .        .
                              .`'..''''''     '`'......'
                              >i)}[<~[}_{I"" ;!!}{[[]-?^<.
                              <![[-,,,:,>;:,.;Il)]-}!:,^+
                               '...''''''     '''..''''`.

                          .'
                          ^:            ;I;::I;<;I;,,:,"",:,::,:;:l'        ;;:::::::,"":::::::!<:,,:Ii
                          `_<~.       .+t ;<iI ].     I+->      . i(`      "}..     '~~-, .  . !> ><>`]!
                         .";I:,,",,""I]~),;I:;:?      .'`'        !{_;`^"^i1)        '`^.      !>^;II^?+-"^^.
                          ``^`^^^^^"^~<`^"""^",`                  .'^-"^^+<''                  .,"`^"",`i?^"'
                                     .~                              !, .~                               +
                          ^;          -_;:,,,,:,:"","""""""""","",:. ~` `_ """"""""""""",""^""""""","," `_
                          .`.        `?["'''''''``'`''''''''''````~:I;   i;~`````````^``^^``^^`^^^^^^^?`+"
                           _>~.      .}l                          i<`     !]                          \?'
                         `:;,l::,,,,:i+                           !l",::"^;_                          ?^,,"".
                          ..........''                             '''``''`                           .'````


                                     l~-"!<>[,"_i~><!<~~+!>-Il{?~]>I[-~>>,?+-+!I!>!ii~iil
                                     ..I`'``". '`^`;"``""'`,'.^"^,`^,",""'",:"^`'`,^"",""




















```

*Figure from page 27 (2346x3317 px)*


---



4203-E P-354



SECTION 3 DATA INPUT/OUTPUT OPERATION



(a) When reading operation is executed at the NC, the RTS signal is switched ON.



(b) The peripheral device outputs the DC2 code.



(c) On reading the DC2 code, the NC starts data input processing.



(d) When the NC needs to stop reading temporarily to execute processing, it switches the RTS



signal OFF. When this signal goes OFF, the peripheral device suspends data transfer to the


#### NC.

(e) On completing the backlog of processing, the NC unit switches the RTS signal back ON.



When the RTS signal comes ON, the peripheral device recommences data transfer to the NC.



(f) The peripheral device outputs the DC4 code to terminate data transfer.



{g) On reading the DC4 code, the NC switches the RTS signal OFF, terminating data reading.



(2) Timing Chart for PUNCH



Recerve data



RXD



Send data



TXD



Request ta send



ATS



DC1 DC3



Data



Clear to send



CTS



Peripheral



device



DC1



Fig. 3-23 Timing Chart for PUNCH (Slave Station Function)



DC3



Data



(a) On reading the DC1 code sent from the peripheral device, the NC executes punch processing



of the data.



(b) On reading the DC3 code sent from the peripheral device, the NC suspends punch



processing.



(c) On reading a DC1 code sent from the peripheral device again, the NC recommences punch



processing.



(d) When all the data has been punched, the NC terminates punch processing on reception of the



DC3 code from the peripheral device.


```text


                                                                                              ."^^``, "'`"`'
                                                               ..'.`'.'. . ..'.. ..` `... `'' :???-~- ~I+]-I
                                                               >}_<<<~-];+.++?+~!]}_~+!++>+_+>>"<<-?+-_<~+[I
          .^^`''````^^`^^^^^`````````````^`''''''''''''```'''''''''..`'''''''''''''.`..''`...`..`' '.''.'``'
          '::,"",,,""":""""","^`^^^^^`^,,",^"^^^^^`^``":,:"^":",,"",:^""""^""";:;:::""^^"""";;IIII:,:::IIII^
                   "<l i_!!!`Ii<~i!;:i!;l<ll^!"IllI:ill"i,>l,l<!.Il;^~i>;,l;;!":`:;l;lI;::i>'
                   `;: ^,`;,.^;l;,lI,l:";;;:';^;;l:,lI,^l^;I"^iI^;l!^l:I;;~~l+"l,!i!ili>;:i>"
                   ^!, ;lI^"I;:",:,,';:",:'"":"^:.;:^^;;;``^:;
                   :~I ":i;i>!>Ilil!^>iIl<,!!~il<,I!!:iI>"!i~~"
                   .`` ",..`'`"'.."`'^^"^ '.`  ^..^^`.'''^ .'.'.`'.`.''''''`'.
                   ,+i.!+I,~~++<-;<-;>>~~I~<_>^<~l!_!;-_+_li[?-:>-><!_i~_--?<[:
                    .' ``'.  .  `'. .  .  .  ..     '          .             '     .  .     .   ..  ..'.
                   I?_ ~?i~>,~-i>?>:<+<_+I+"+~?II-__~~-l]<-+<>?>_,~:i~_+>~-;~i<<~<~<_I:!<~_-_++!>+~:~!>!
                       i>~>?I>_+> i[+++,i<~,++~~~l+<_ii_~~:<_<:~+i_+<<-!I+>i~>I<><<+<_<"___li~+>~+lIi:?~"
                      .]1-",.`'.. '^`"^.'^"'"l""",I":^'"'''^":`;,"l":,;^^:,"::^;:;;I^:;`;;;"";;:;;^^;`;l^
                       ,I"
                   ^;" ::`^,",:;;I:",l,";,,:,"`^;^""^"""""^ :,^^I:`'^"`^^:^"`^',"`"l;;```````^``^'""`
                   I-!.I<,:!l!<<<i<~l>>:<~<il<i;iill><<~<l]`!i>:_+^;ii,>~+~ii_;i+iI~!<:i+?i+:-+<+"~<l
                       !!I;,';:';il!':::::'",;::';!: I,``,:;::"",',:^",`'"^^^^"^"^^^'':,"`"^^`:".^'^""^I:`
                       ll;>I`;!,:l,!"i?!i!,!!Iii"l!l`!iIl~i<~i<!_"i~!!~I;_ii!!i~~>>+l!?__I<+<>+_,ili<+;?+;
                    l; ^,^ '^^`"^`^'.^'`'`.'.^..^ ^''`^^^ ..`' . `..''.`' ''' ..  ...
                    _> ;i~;<+<?<<~<i:_<>>_,~~}+i+:>+Ii<!~:<<_+,~:+~<<~<}-,_--!i~_>_-~'
                   ' . `' ..  '   . .''.. . .  '  .''   ...   `  .``.       .``        .   .
                   !)~ ~~II??_+__l~_;++~>l~~-i,++l+[i;--?+~__l[+!+-+?;][+?-I-++:<?i<~<?]~-!][]>;_-]+~-.
                  ' . ^      '  '   .' . ..                            '         .    .  `. ... ... ."
                 <{l .<~_<_<!-~[_!-<I_>-]+_i
                 ..       .`   .      .


                                           "lI;:I!ii>!;I:           IlilI;l!!!lI
                                           ?:</1[>+?{_>^{+~;II;;;;?l}`-1{{{]_-`1.
                                           !Ii--+l::,::;~::`^^````I^<,>]_?}l;,"~.
                                                 ......                    ....

                    ',                .,^``^"^             '"^'`^"'        '"`'`^"`             ""'''^^
                   ","","^;;^         !!;-<I`-             +,l~<<:> .      ~:l_<;,<            "-^~<<,~
                   +1[_l!,>~;         !;."^. ],            +.',,"'?^       _'`:,..]            "< I:;.+!
                   ":,'      ':::,,:;:<"    .!?<;;;;;:,,,,,<.    `~__:,,,,:_'    .-];,,,,,,,,,,!l     !>];,,^
                              ........       ,>^...........         ~:.....        -,...........        :~...
                                           .i:                      ,l           `l:                     +
                     '                    ._.^,,,,,,,"^^^,"":::,,:. ~`          ,~I""^^"""^^^^^"""""""` ll
                   !>ill!i^               .i]_```````:lll`''`^```i]l;           "|>``''```";;:````````{il
                   ~}]!,;;`                 l~       ^!>>        l{'             I!       "!~<.       1;
                    '^       ^::,,::::::;;:;l;                   :iII;:::::::::::i,                  .i":;::^

                    ^,                      .,"""",""""""""",,:::::,,""",::,:,:::,""""""""""""""^",,,,,,,,,,`
                  .][_>_~I!I~ii             ;>'`''`'''''''''`^^^^^^^````^"^^"^""^^^^^^^^^^^^^^^``^""""^^""""'
                  .->?:.. ...^,"`^^^"""""`^`<l
                    ^        `""^"^",,,,,""^,:^""^^^^^^^^^^"""^^^````^^^^^"""^````^^^```````^^^^^^^^^`'``''`.
                  .l+ill:,ii;               ;>^,"^^^^^"","",,,,""^^^^,,,"::::,,,,,:,,,,,,,,,:;;;;;;;;,""""""'
                  .-?1!""^;;".'.'......''...>I
                   ' '       ";:;,,,I:Ill;;:l`


                                    ^   . '. `      '   .   ' . ..  .     .
                                   ,--<,_![<.~>++_<l_+]+!-~:_i-[~+>;]]?~<:}_]_<I!i!<<+<<!
                                     .'          ''   '  ..  . ..  ..'''' .'''.   ''''`''
                   ..  `. .. ..  '  ....               .
                  .+]"^++^>~~~~+<__ii-~i"i~]};_+~<<~~<I]+l>?_?~<+<+,[+<~-:i-<;?_Ii+_+i+?_l+<~~+:~i>~+~+~+>
                   .. `~;<+l>]~-"  .     .... .. . ..  ...''.^..'.' ''.'''..'..'..'`''```'^^'`''^.````^'",
                      .^ `^'',""
                   <<`^!;`;l;!;;"liI;>!<:II!i^I!l,i;ll"!l":I;lllIIi"lI;;l`"I;"ii,:,:I:l:l,^::,I:
                   ll`^>l:>~<~!-l,l;"I:l"Illi^!iI"::l;^Ii:!!;>lli!>"i!!l>,"Ii"!i"li!_i<I<ll<>l>l
                      :<l><<<iI?,
                   '' .'.    ... ..^`'. ...   ..'. . '.    ... .  .  .        .  ....
                   <_,^<>,<+___?i~!_+!,l~~?l<?<<!_<~:-_ii?_<_<_i?"--~~-!>[[_~^<-il[+:i_<<i~<-~>~-Ii~-~_;
                    . ;<!><~~_i?I            .    .     '. .. . . .......^^... .. .. .''. ..'.'''.``'''.
                      `'.''^```:'
                  .i-`^~i;l":!^<l:;>>I,li:I!ll,,:;:Illl.<!I;~!,il;I!I>!I"l;l;l`l;::I;Il;,,I^;I;II!;;'I;I;:
                   I!`:?>~~;>~I>-li+~?;l+ii~_<l<<i>!i~<`IIl^!;^il:;!l>i!;<illI"~Ill!!i!>>I!"l<!~~>i!`i:I!l
                      :<!ilI>>+"i!>;:+~,>+!<i~i~i;->ii<`











```

*Figure from page 28 (2346x3317 px)*


---



4203-E P-355



SECTION 3 DATA INPUT/OUTPUT OPERATION



Example 3: Example connection between OSPs using the slave station function



Communication between two OSPs is executed by making one the master station and



the other the slave station.



OSP



Signal Name



TXD



RXD



RTS



CTS



DSR



RG1



DTR



EX-INT



NC Parameters OSP



Bit 7



Data 0



Optional



parameter Condition File name



(bit) No. 8 Set read



NC optional Baud Rate



parameter



(word) No. 6



2400



DC code



control



TYPE2



OSP



Signal Name



RXD



TXD



CTS



ATS



DTR



DSR



5 4 3 2



1 * 0 0



Standard 8-bit JIS Even Parity



DC code parity check



control performe



indicates either "0" or "1" can be set.



(1) For the parameters indicated above, set the same values for the two OSPs.



1 0



1 0



No ready 1-blt stop



signal bit



setting



(2) Set the channel used for the peripheral device by setting NC optional parameter (word) No. 45



(designation of punch device) and NC optional parameter (word) No. 57 {designation of read



device) in advance.



(3) Bits O to 4 of NC optional parameter (bit) No. 40 are used to select master or slave status for



each channel: set one of the two OSPs as the master station (set "O") and the other as the



slave station (set "1"),



(4) On completion of the steps above, communication between the two OSPs will be possible.


```text


                                                                                               ."^^``` ,'^"".
                                                                ....''..    . ..   .. ' .  .'. !{]--+~._;_[["
                                                                _}_>>~~-_!<^]__+~i][_<<<_~<<-<<>:--__-?_~<~],
           .''''''''''```````'``''''''''''''''''''''''''''''''''``''.'`.''''`'''''''.^.'``'  .' .`..`.''.'`'.
           `,,,,,""`^^",,,:::;,,"`^^^^"",,:,:,:,:,,",""":::,::;:,::::::"^^^":,:,::;:;::,:,,,,,:::,::::;IIIII'
                  .~I!!ll>";, <iIiII!I^;;;;l;l;l^I!illII`I!<iI`:l;;^II,"!I::^lI!;;^!:;;!::.
                  .l;i!I>i,:,.l;li:l!I^II;;i;:;I`;iill!l^;l>:l"!i:>;:II:!ill^i!>;i^Illl!!I
                             il!II!l!!l~<!I`>~~!>>:^_+:;~--<;>Ili<>l_+>l~l,i~~!i>^>!lI+!^Ii+-?I;-+?<<"<>~"
                             ?+>:+~_>l_~;~+!<l>-_+!!"^'''^''`^`^^""^""^',:'`""^"l`"^"`""'`^:":``,:,"^.:^,.
                             II;^l;l:`:I^Ill;^;i!:;I.

                               i~]],                                 l++-,
                             '<i!>_i;IIl!!IlI;:;Ii                  ii><_!:;;;lll!!lllI<`
                             ^<'`'+]1-?-i]]~->'''_.                 }"..+11-]~l{}+-_'``?;
                             "+"""^^,^>-_"'..''''?"^^^",,,^````````'};","^;"l++:^``^`^"_"
                             ,-'`'``'^><?!,,,,,""}^^^`'''''''''````:[^'''^^^l!-!^"^'``'~"
                             ,_```''''!+}+^``````[^""^``''''```^^^^l]^'''``,]-??"``''`'~"
                             "+"""^^`"_<_<^""""""|!'''`^"""^```````._:"^^``^~>_>""""","_"
                             "<'`''''"<_]+,""""""{"'''''````''`````"_^``````i_}~,""""`'~"
                             "<'`''`'^+<<-^`````^]^^^^^^^^^^^",,,,">{`'''''"~i<-"^^^^`'~"
                             "~","",";~i<~``''''`+                  ],""""",?<<~`''`^""_"
                             "<'`''''"<l>_^^^^^^^-.................'[`'''`'^+~~?"^^^^^'_"
                             "<'`'''':_-]]"^^```^-'''""""^`````````>)`````'"<i_],^^^^^'?,
                             "<`^,,,,;+??!""`````]I^^''''''''''`^^^`]`''`^",<<<!^``''``?"
                             :_^^^^^^`l?_:'''''`^];^^````''''''`^^^"-^^^^^^`l}];'''``^`_^
                             :-^^^^^^`I<+,'`'''`"['^`",,,"^^^^^^```^-""""""^'.''`'`^^^^_^
                             :-","""":~<>:`````^"[                  _"^""""""^^^``^"","_^
                             :_``'''':?-<l``````^]                  +^`''''.   .'````^`+^
                             ,<^`''`':+>+_^"^^"^"?^"^":::::,"""""""<["^'''':+~+~"^^^^^^_^
                             ,i`````^;+l~<;""""^^<                 .-``````;++-<:""""^`~^
                             ,<^^^^^~[]<1]_"^^^^^~                  ]```````'''`^^^^^^`_^
                             .:,,,,,:;:;:;,,""""""                  :"""""":;;;;:,,,,,:;.

                  ^>>"i!;Il;;i;;`^!i<l
                  `>i,:l!i<;!<!l"'!!<"
           i:::;:::^",,;^^^>i"^^II^^`;;,,,!:,,:i:,,:l,,,!:"",!",,;I,,,l;,":l,,,;I,,:!:::Il:::I;,:,I:,,:l::,;:
          .+          '!``^--"``i>"""!:""^<,``"-^^`"i"""-!"",-""^l!`^`>:^";?""">>""^+"``I<^^^i;^"^>""":_^``:~
           ~":;,^""   .l''<~++''i!'``~:''`~"''"<'.'^!'``I"``^<``.ll.'`!".^:_""^<i`^'+"``I>.``l"``^_^``,~''',>
           +i}][~?[". .i>i>+?-i;l<i!:!>!>!-~~iI~i~:"ii!ll!III<<!<~!~<"!!l:Il`^`<_ili_;:,!~l;,lIll"_::i>~>!ll<
          .~-}__[?>)` .l-]+!!>!"^>_]_l<!<;l<+>i~-<" I][_>?[],I>I~l,<i ,>--{<   ;~~]+{"  ^i__!-?~_'>>__!I~+i'>
          .~I!!^lI.l. `>;i;     ,I!!i'    Ii--}-<^ '><-i_-~i.l        :!iil~   :>+?]?!:"`l+)[?!   <i~'     `>
          '-          ^<        :"        :``^":`: '<;!lll'  l        ;.       "<-lIl;i!';l>i:+^  <        '>
          .!,"^^,,,,,":>",""""""lI^"^"::::i:,,"",":;i^...`^""i^^^^"^""l:",""^"^l~i`"^^^^Il^^^"^"",+::,,,,,,Ii
           ::::,":,,":;I;;;:::;;""",,:.... ........':";;l:II:^Il;;^l"",";^,:,,I""::'''''..'''''..'.'''''''''
          .}<[li[-<~{>,_'"{[+]<?]{!'']             .!^!i<i><l;i!<i.!':l.;.l<l:~;l~l
          .]i+i_____" .+,,,,II:;;:"^^]
          .{_]_?]i1-`_,i''.'-__[I.'''[.
           >>>>>~liil<I;","",:::;;;::!
                  ,I' :>;^!!:"II;IIli;I,,I>ll>Il"ll;;I.,Il:l;^II;l,^II,;,:l::!;"I:,^l!<i,
                 .,:^ ^";';l;:!!;l;!i!:,^;!lii!!"i!Il!',!l^;!^i>;>;"ill!l^!;:!i"iil"li<;!
                  ";. `;"^^"`."`"``^'.^^"""'.:`.'```^'^`^.,`'^' ` .^`"`'.:"^ ''".'`..'.''^""^'"^^`:':"' :"
                  >+" ,--I!+<;~>-ii?I!_++!<<:-~!~+<++~~~_:]+><_I<<:-~_i]i~-I:-__~<-l_]<_<!_~<^-+<i-l~~:'-~
                      ^>~i<~i~-!l`!!!!Ii~,l]>>!~;!>~I~-!"_+<>i-li?_<li-->'~+<i-:<+:"];"+~<__!__i>^!~:_+-'
                      :]<~<-il<:~+i~+<_". ...........  ..'..' '.''.' .'...'.'.'' ''.' .`''`,'''''.'..'`'
                       `''```.'.^`'``^^
                  !_` ;_!:::;^:,:!l>;'li<Il!:"lll;Iiil'!!i"<l.^+,:l;':ll;"l'll!;l^;;ll!:^;`!l:I`Ili::"!l'
                  ;l' :~~+!;<!!li>liil<+~<l-!__>~<>>--!]<ili+l;<l>+~Ii<_>!>;>~~~!l~~~~+!l<:<+_~;>++<_Ili'
                      ,<~>l:i~+il+,^_<,i!>">;~<I;~i"l<_I!,-Il<~'i++~-:I_+_i>^>~<.ii::+Ii;!+'<~>>'_l;~+'
                      :++>+:_?-~_^!--l^;l"
                       .           .
                 .~[^ ;_<:i<>___]i>,>!+_>;]+<+,__>>+^;<<<~~><>~]+~l>+~+~i~!!-~I-~!;~_?+!I_<l_!l>><~_+i
                  ``. .''.``'"^^`''.`.'``'^^"^'^^``^''^````^^^""^^'`"^^"^"`'^"'""^'^^^.^`,^',^,,"","""




















```

*Figure from page 29 (2346x3317 px)*
