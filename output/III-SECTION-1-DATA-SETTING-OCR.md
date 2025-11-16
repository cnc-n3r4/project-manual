# III SECTION 1 DATA SETTING OCR

*Converted from PDF: III-SECTION-1-DATA-SETTING-OCR.PDF*

---


# SECTION 1 DATA SETTING

4203-E P-157



SECTION 1 DATA SETTING



This section describes the commands used in the parameter set, zero set, and tool data set mode



operation. The procedure for setting the zero point data and tool data is also explained. For the procedure



used for setting the parameter data and the contents of the parameters, refer to III "PARAMETER" in this



manual.


## 1. Mode Selection Keys

MODE selection keys



---~---------------,



--'------------------



I \



Fig. 1-1 Mode Selection Keys



The mode selection keys are classified into the three groups, operation mode, data setting mode, and



machining management (MacMan) mode.



(1) Operation Mode



(a) AUTO



ln the automatic mode, the part program stored in the memory area is read into the operation buffer



and then executed.



(b) MDI



In the MDI mode, the program is input from the keyboard and executed.



(c) MANUAL



In the manual mode, machine operation is controlled using the switches on the machine operation



panel.


```text


                                                                                                ^"^"':.'".^^^
                                                                                   .'..`...    '+]?->],l<,<-!
                                                                                  .]1+>+_~[~,^;?~+-!!{+i>__-~
            ^^^^^`````````^^`^^`````''`````^`^^`^`'`'```''''''''...'''''..........'''''..'.'..'`''''``...''``
            ^^"^,`^^'^'^^''^:"^:::::,"``^."^:^";"^^'^,",`^'```^^,,,;;;;;::::::;IIIII;III:;:::::;IIII;;,;::;I:
            }1+)i[_<|_[--]{? !+      :}_:(l)l}> +}i)<~]<}<?_>~_I
           .\n|j]f1l1!n))tfv <| .    >r|/x1\]xx'1z/U}_),f-vnvrf\
                  .     .                   .  . .  .         `

                 `_<~`,>i<<i'^~<>!i>>!'+>"^!;l!!<l!~`"!>>;;;'+!^^iilili~>`,ii ^>lI';ii :!;;`l:I.!!!"^lI':;;lI
                 '!!~Ii~i!"><!i!>!!<+<:i<!:i!~+i<>++"l+~ill!I!~!<>~><>~~_"i_<:I~~>,l+~,!_i!;!~<,<?_I;_<"!<i~~
                 `~~~>?il;.:<+I!ili<><!>:~;l<~+l~!>>l~>l;<<ii;~_?!_!lI!il!~~<!il<<i;<+>_<i__ II<,<<i~<~++~>!i
                 '>~<ll~;!?[~!+!~_I+?<?>_--lI?-_l?i<>_~I+i<?<~~">!_~l>-<-~~?-<~^;~]+;?;]]">+?__][)i>?__"<:++~
                 ^><_li-^     '   ..         .   . .  . .  .. ...  ..''.'..''.'..'.' '..'   ..''''. '.  '.''`
                 .`",^,:'

            [:     'xr}?[/{`\(}1{[-{1-_[,?|_[<_]
            ;:.     -_+_+-]'~-]~?]-~_--+:!~??)+}.                 .
                                                                ^1]??{l[?-_[_<!?_-`
               ",^^^^^^^^^^",""^""^^^^^^^^^^^^^"""^^^^^^^^",",""";;Illl!I!ii!;;l!!<"^^^^"","^^^^^^""",""^
               l'  '`'''.'''''.....'`''''''''''''````'`''`'''''''........    .    "l.''...'''.....'''  ';
               ,' ,:"lII;;;;;I:::;,^"^`````^`^^`^""""^"^^"^^^^^^^^^^^"",","",",,,:"<~,;I,",:::,,""",;; ."
               :. ". ;:,",,,,,,,,;"                                      ;"-1+;[[_l\ni>v/I+}_l{1-:I .l ',
               i' "' I!lI;II;;;;I;::::;I:;;;IIII;:::;IIII;;:::;;;!i>^    !;;;;::,,;;,+I,;;;II,:;:ll `l `;
               !' l' i .'l^'''''''''''''''''''''''''''''^'''''`i^. ;;    ~;''`''^^^^'`>"^`^`^"^,"i~ ^> ^I
               l' l' !   l.                                    I.  :,    i?[}](}?[<??]([~1i[?_[~![< ^i ,!
               l' l' !   l.                                    l'  ,^    !+_?>[-_{<??}}1?1]}-?[<~-~ `l ,i
               l' l' l   I.                                    l'  "`    !l:;lIlI:+;l+;?<,;i;l!-~-~ `I "l
               l' l' ;   I.                                    !.  :^    !+[\?}{-----}_-]-[{-{+)([> "i ^:
               ,. l' ;   I.                                    I.  ,^    l+~{_:?~>+~>?+I[?{}<{_}_-l ^l ";
               l. i' i   I.                                    ;   ;^    i_~~_<~+_+_+?__1<<]<<}!>]l `, :l
               <' <' i   I.                                    ;   :^    <-_]]~~<+{+_{-?{>~}+](<~{< ^: ,I
               >' <' i   ;.                                    l   :^    >>i>i?~>~~!Ii!i~::-":}~~}< ^: :I
               >' <' ;   I.                                    >   ,'    i~";+,I'"I;;l;;l;;;I',il~! `: ,:
               l. !. :   !.                                    i   "'   .>->+[l+':~>~-+>?<~>i.i(][l ^: ;;
               ;. l..;   ;                                     <.  :`   '~)f1?x(.:_<i_<>->i1< ~<~]; ^: II
               ;. !..;   ;                                     i   :'   .+)({?t(.;<ii+<i_<i?i.><+-; ", II
               ;. l..!^""I:;::",,::,""""""""""""""""""",;;:::::I^,`i^   ._[]il]]':<i>+<i_><_!.I_i+: ", II
               >. !. i<<>!>i>i<!>!i!!l!>!!l>ii!!!lI;Il!!il!l!l!l!>~<.   .+)}-_{}.;+i>:!~~>i!i ~~<?: ", II
               !. >..; `_]!i<{l!>}+I!_-::<]Il!{!:l]_;l<_l<~(<:<-<" l`   .+lI,:l:'`"^`,"^,^^"^'"",<l ", ::
               l. i. ;":>iI;Il:;IlI:Iil;:l>l;liI:li>IIllll!il:Il!"`I.    ~"^^""","""""""""""":"",i; ^, :,
               I  ;"^^""^^^^^^^^^^^^^^^^^^`^^^^^^^^`^^^^"^""""``^"""^^^^^^`^^"""""""",""""""""""":"^,` ,,
               l'. ......'''''''....'.'...''......'''''.'..''''.''''''''''.......................'''.  I:
               ^"^"^^^^^"",,,,,^^^^^"^"^^^,,"^^^^^```""``^'.''.`'...'``^`''''^^^""",^^^^^^^^^,,"^^^":::I'
                                                  !i~`""; ~?l<_"_<<>i~l;;+i!i
                                                  ``i^.'` ,:":I`,;;I;;:"^;l!;.
                 `^'  . ..  .. ''....       ..  .'
                 ,>+l:~><+"<~_<~_+;,_~+:l~i^~_~<__~+;>?>;_?;-++?l>?<<~-;^+_?~]->I,~<<->'-?]iI+_]i?:i+>_?'!~~i
                 l>_<i><~_;i-~i_+_<+-+l~{-<+[+~>"i<<?!..  .  ..'.^`.'`'' `''.'''...'''`.````.^'`':`'``'^.'``'
                 `'"^``'',' ``.:I``^^`'""","":"".^"":"
                  ,l: .><!i!_!!`!_;li.
                  ","  :;;:,!:;`:l;;!'
                    '!l I:,I;,
                    "~> Il"^;"
                        :^il,:Iil;I<>";l;><'<!I;!!llIIiIll,!!Il!I;;~!,:ll;;:,:I;I,;,II;I;I::!:"::I:I!;:;:,>;`
                        i!<>+<+>>i<-~i<+>!>"II;lil:>;I_I!;,!lI!i;;:ii::ii;l;!lil<I!;><ilI!!I!!;i>~!~~>llil>~^
                        >!!"iii,l~>ii>~<:
                    '^' ^"^'
                    l]i.?[<I
                        ^.:,^"l;;`"^^;'.;^''^``^^^'`'^^''^,`^`'"`'^`'^'''`'''^''''..`.`
                       .!:<_<I-<<I>>~[i"]~l~<<{+_<:!!i_~>!><~i;~_I~_-+>-~>I?>~l+~-<~?~-'
                    .'. `'''. .
                    ;-i.]_-]+i_<.
                        ^.^`'`'`^'^^`^'^^ ```^"'`.'''''"''''..''`'^''..''. `....''''.. ..'. .. .'..     .'
                       .<;><ii>+>>->;+<~?^i+]+_i_l!~?~+[+~;_l<_~_>--+l~?~]>~_!i?-_~~+<l~I~_!i~-+]~~<!-?>?[<~,
                       .~->_~                                            ..                          .
                        `'.'.















```

*Figure from page 1 (2346x3317 px)*


---



(2) Data Setting Mode



(a) EDIT/AUX



4203-E P-158


#### SECTION 1 DATA SETTING

This is the mode for reading, editing, punching-out, and printing out the program, operating the



tape reader, and managing files.



(b) PARAMETER



Parameters and variables, including system parameters, user parameters, common variables



and NC optional parameters are set.



For details of the parameters, refer to IV "PARAMETER" in this manual.



(c) TOOL DATA



Used to set the tool data such as tool length offset values and cutter radius compensation values.



(d) ZERO SET



In this mode, the work zero offset value is set.



(3) MacMan Mode



The actual status of the production field is collected in this mode, and the result of data processing is



output to the NC screen, printer, or 3.5-inch floppy disk.



For details of the MacMan mode, refer to the separately prepared manual, "MacMan


#### INSTRUCTION MANUAL".

(4) Pressing any of the mode operation selection keys will light the lamp in the key.



(5) If the mode is switched from any of the operation modes to the data setting mode, the lamp in



the selected operation mode key starts flashing. This allows the operator to recognize the



selected operation mode at a glance.



(6) Once program execution is started in the AUTO mode or MDI mode, switching the mode to



Data Setting Mode, such as EDIT/AUX, PARAMETER, TOOL DATA, and ZERO SET, will not



interrupt the program execution. Therefore, program editing, tape punching-out, tape



reading-in, parameter setting, zero setting, tool data setting and other data setting operations



are possible during stored program execution.



When program execution halts in the AUTO mode operation, while data setting operation is being



carried out, due to Single Block ON or Program Stop command, it is necessary to press the CYCLE



START switch after switching the mode to AUTO to continue the AUTO mode operation.



(7) Switching the operation modes in the following sequence will reset the control:



(a) From manual to auto or MDI



(b) From auto or MDI to manual



(c) When the mode is switched from manual to the data setting mode, although the control is not



reset, it is reset when any operation is selected after that.



IACAUT~NI : When the data has been set, the new data is stored in memory after two to three minutes



have passed. Therefore, if the power is turned off immediately after the data has been



set, the data may not be updated as desired.



Before turning off the power supply and after setting the data, backup the data following the



procedure explained in 3-4-1. "Back Up Command".


```text


                                                                                               ^"^"'".'".``^
                                                                                  .'..'...    '-[-?!-"l~,<?-
                                                                                 .]{-><+~?+,^"-<__!<1~!!-?_+
           `^^`''`````^^^^^^^````'`````````````''''''''...'''''''''''.............''.'..'''..'`''.''^'..'''`
           ::::"""^^,:,"""",^^`^`^``^^^;:;;;;;;,,"":;;;,,,::::;;;;;;;:::;IIIII;::::,:,:,:IIIII;:,,,:;IIII::"
                  <~' I<i<;l~>+li"_~I<l
                 .lI  "::;,`l:;^i:IlI!I
                    ;!.^!;:!,i:l;
                   .i~`"!;"::iII;
                       `!II`I.>;,"!;l>^il';lli!I: l!<ll,'I";;!;::";;"'!;I^;;Ii;:`,::Il:^;,,:,:, `:,",l;,`::,
                       "!i~:<l<<<:I>>_;><:i~~+i<[:+iil>>^iII!l;I+:li;^<!!:>l!~!?:!i;l~i!<l__i>l`:_>!i-i+i;><
                       ,+~>,l<<>~;.~!<:i<~i?_!_;<-<:
                    `' .```'''^``^^'
                   ._?`;~_?~_[]<i]~+
                       ^,`''`'^`'. '`^.`^^^"^`' ``^'`"'..'.``'' ..''''''..  ...  .. ......    ... .   . ..
                       Ii-~->+?~ii"_i>^>_i]?++!.!i~_~_~_:[++-+!"__<-i_--<+`;_]-^~?~+>+_-~-^;+~++><<">-~]]--~
                       ,_i!l-i^<__<i+>!~>>+!~]++:_~!;~-^                                             . .
                       ^"''.``."^'^`^'``'``'`^`''^`'`^^. '..'' .   ..'....
                       !i_,>?-?+i;+i__:>-<_i_+_<~'l_]~"-;?+`~_]]-[}{><-__^+:-~_;<_?!>[;
                              . .     ... . ... .. ... .      . ....  .   . ..'..``'`^.
                   .+~',+~_+:l__~-I
                    ^^ ..'.`^.'..'`                            .
                       !<+_~i+:_->-+i~~~;?]-i<+-_:]>i+_>-+<[+:_1_-il+<+-il+><l<-?~:~+?<~;<~<++<<~_+<i:<->~~"
                        '.'. ...'  .  .  .....'. .'..'' ''^"..'.'`..`'^`''`'''``^'.`^`^^'``'"^``^^`^''"""""'
                   '+]'I)-_]i;[_i^
                    `` `````..`'.  ..            .
                       ii;]-!l~~+],~?~;-<+i;?+>,i[[_~;_]~~I_;--;
                                     . ... .... . ''..''''.'.''.
                 "]-. ?[+<[-~;i1<<]:
                 .^^  ","^'`^.'^^`".   ..           .
                      ;>~;<<~>_I<~~i+;~<~>;~!>->><~I+->>>ll<]~>+~<il<<~l~<~[<"]i<+?_I~+~?!<i~]?>!i><++_~i<<!
                      I!_~i>iii+<;-]l!<i~~~"l<>_->^il<>_!<><I]<~~<,~++l'``^^^'"'`'^"'^^^^'^'^,"""`^"""""^I"^
                      ,::;,`'`'^,'^:'^,^::".,,`^;, "'``,"""^.,:I;!',:l^
                      iIl .~~<~~` !" _i; <+<i?_+I :<i<?" :<<~` >, +<! ,~<i~i~+_l !><~<ii~^`>!<lI+^ :[_><[+<:
                      ~_?i<[<_~<~!-<![--~!_-!:^,^ '""":^ ',^,. ,^ ",: `:;:;"::;: ;,:l;:,;..,::":I^ .IIl;IIl^
                      ",:"`"",^'":::"l:II::;`
                 `l;  l:",,,"`',"`':;;^.""^;^`::,"l:,^":;",;""^,"^^`,;""",";"`""""'"':"`^^`.
                 ^ll  ;;!i<ii+,iil;llii"!>!~I:_<i!_i!"!~~<i<il,<~~!;+<;_?>l<~!!-!-;i,<~>;+_i
                 ."`  ,`^' .''^' `.''"'`'''`''. '.  '^`.  ....`   .. .. ' ..  . .   '.     .'. `..'.'. .
                 ,-<  ?!<+!i_~_~I_;+_]+>-_I~~~!!?<!l<i~-;__?>-_~>:+~<_+!<<;~-"~-]iI__+>[;<~i]>._+I>]l-I<I
                      +<!"_++i<<l^_><I-ii,:!l>_^i<!,_~~-:?_-_l<+ ^>>_,+[<+_;<_!;_+<<-~;~<^<~i~?>~_I]+!
                      >~?_~-+!i_~i-]>>;><>]>I?lil]_><+^'..``..`,  .'`'`''``'.`''"^'`^^.'^.^^^,;`^^'`"'
                      ^^^"`,^.`:"'",^` ``^,^','^,I,^,,.
                 "+! .Il;::`I:::;l^^;:I:Il:",:^!:";;,"^;l:`i:lII`I:,!"""^>!l^::"I".::l;l:,"`!:`"""I"";.
                 ^!; .<i~~l-~~]+i<~i~_i!+>~!I<;--<?+><I~!~i_+><<>+-+[>:<I]_>"++_?~`<+~~-+<1!~_<<~i+~I~^'
                     .i>_+"<~+>i~:?>>_:^+l~;;+;ii~!;<~i+"I<<><+-];!>!i I!il!^ii>i<.<>~;>->+~"i[>:.~_II~-.
                      i<<ili~:~<!Il!_i<<,!i>i!-~i, ^+i<!_>!> !I!>!i<::~+~l_`i-<i^!i<!i>!!,Ii`I+i<'
                      l>~>i<lIl.!+i<+<_~;,+~?<>I^~iI"i~__><^~><:[-?!l+__<>>~i_i~+~~,~<+!~~]?iil+<!;ii;;;
                      >~>li>+!<iii<>>i>i~I~<+l-~;~~>li~~+!]!>>;';ll:,l;I;<^I:;^I:;;'Il!:,i!l;<^l!!I<!lIl.
                      !I:,l;l!l>:^l;I;i"~l,!I;!:~>!!""!!!;IiI;
                     .!>I;,';"";:l:`,::,^l:,':;i,",^i;'I":l:`,;"l;`::;:I:," ;l:;^:II,^;I!:"`:::,:;""`"",,,"'
                      i<!~i!~l-]i_il~>-~<<+ii<_-il_><<I-<II>;<i~-<:<~~<_>>i"~~!+Ii__>I_+-i]I~]_i+_~l:_i_?>?i
                     .i_<!_+;l<";~<l~">_i_+:?<!>!:>~^!,ili]i~i;~~><"ili!!~i~,;:<:i<i~<<~i;i!l>iii;_~!i!<<l_:
                     .]<+]_<"~_]~+,+[?i,_?-~il<>>+~"_+<]I~il]l<<i!_,<~>?<i_I]+l>-<-_iI_<-}:<_~>_-i<"     .
                              .      .  . ..  '` ..  ..'    ..    . .'.''.`.... `' .. '''^.":"^,"^"'
                 ;~i '-+_-><i~I_~i;~+<<]<~;l~><+~"i:+<;ii<!<i!i:<iiIi!!!^><;l<!<:l>l"l!<ilI
                 ``'  ````''',`.'..,"^'"'".'^'`",'^'",^^,",:":!^;:l,:,::';:^"I:;^"::^::;::"
                   ^~i <!!i:,liIIi!:I^ili`l:l-<!
                   ';, '`,"''";^:;,'"'l:I`,`^l,"
                   "!:.i:,:""::;',.i<!^:^^:::^:I.
                   ,i;.,";;,;!ll^I'liI^l;";iIl>>
                   .^^ :;,^`."` '``^`.^ ^`,^^''.:`"`'"^^'^"^^',^'`^"^.`^:`'.'`'`` '"^''.''`^'...'`'`'...'
                   ,+> ~~<_!:~<I;>>~_:~;_~__><+;>i~!:<_>l_+I~;~~!I_-~I-~?i-<!><+-`<-~<~+[I<?-;~~~_<<i<;<+`
                       l<>+I;!IlI+<_Ii<<~::+>;;?<<<?>>"~;i+~~<~<;<]_!;+>+.
          ^^^``'.'...'. ^"^''''`.''`.. '`'`"^^'"^.'^`'.^'`^^^`'`'``''.`^"'        .   .   . .    .  ..  .'.
          <I\~!]?-(11-l'<"i}-~~I+~!:+~+Ii_~l~~<l:<~,l~i;~<~l<+~i;!;<!ii<li;i!!!l!II--<I>i!Ii;~ii>;!~<i~~<:Il
          <J0w))r)|r\|i`i :>I!l"l!!:<>iIi~i,~<i;^+~I:l!"!ii"!i>!:!:<!>>!,I:l<>liil,-~<^><l,>,iii<";i;li>i `i
          ,l;II,":^:"I^"! I!<<ll<+>~il ^!i<i~iI<.l:+<">ii<+'>^i!;>_!;]lI~<++_+]~-I!_~<,~~;!--~;<+!;_+~l   ^!
                       "l :~+.>_!,-_~;<><:;<!i~I:<i+~~<Ii<"<>i!i<;         .   ....  .  ...... .'. ''..   `;
                       ^: :I:"^,:^;I;"":>I,;"^;"^l:;:::":;`;;:,;:^  ..   .                                ':
                       ^, >?~~!>,<l!!i!"~l_>!!<<~<":>~>~>^-l!:?~~^!<?-l~!_+;~][+"+__->?:__ll-__I_-~+_i]!]+~"
                       ^: ;>i!<~~i<:><-+~l>~!-:~l~,l'-[~~i;<iI<i~li<<!~l  . ..'' .''.'^  '..''' ....' "`.',;
                       ';,i!!!!!!ll;!!><+i~~!i;!I!:I";i<<il~<l!i!lIi>><::,^^^^^^,::,:,^^^^^^^^,::,:,,:""^`::
                                                                                 .....        ............








```

*Figure from page 2 (2346x3317 px)*


---


## 2. Data Setting

4203-E P-159



SECTION 1 DATA SETTING



Here is a list of parameters for data setting, together with their contents.



Internal



Sub Entry Axis



Category Subcategory Data Elements Unit Data



subcategory Type Type



Type



Work Microns; Linear 4to Max. 100 Inch system 4-byte



coordinate integer axis Metric system integer



origin

- -



Rotary 4 to Max. 100 Degrees 4-byte



axis integer



Tool data Tool data Tool length Microns; Linear 50 to Max. 300 Inch system 4-byte



offset integer axis Metric system integer



Cutter radius Microns; Linear 50 to Max. 300 Inch system 4-byte



compensation integer axis Metric system integer


#### Parameter Common Microns; 200 8-byte

variable integer floating-

- -



point



data



System Travel end limit Microns; Liner 2/1 axis Inch system 4-byte



parameter integer axis Metric system integer



Rotary 2/1 axis Degrees 4-byte



axis integer



Pitch error Microns; Liner 2/1 axis Inch system 4-byte



compensation integer axis Metric system integer



range



Rotary 2/1 axis Degrees 4-byte



axis integer



Pitch error 2-byte; Liner 1/1 axis Inch system 4-byte



compensation integer axis Metric system integer



interval



Rotary 1/1 axis Degrees 4-byte



axis integer



Number of pitch 2-byte; Liner 1/1 axis Inch system 4-byte



error integer axis Metric system integer



compensation



Rotary 1/1 axis Degrees 4-byte



points



axis integer



Zero return 2-byte; Liner 1/1 axis Inch system 4-byte



operation integer axis Metric system integer



execution



Rotary 1/1 axis Degrees 4-byte



sequence



axis integer



In-position 2-byte; Liner 1/1 axis Inch system 4-byte



width integer axis Metric system integer



Rotary 1/1 axis Degrees 4-byte



axis integer


```text


                                                                                                "^^"', "^.^^`
                                                                                   '.......   .^]-__i?'<i;~[>
                                                                                  `}[<ii_+[iI`i++i+l+]iIi+-?!
           .^'''````^^^^^^`^^^```^``''```````````''''''''''''''....'''''...........''''.''''...''''''`'..''''
           .`^",,,,"^^^^^^:^^^`'`^``",;;;;;;;;;;;:,",;;;;;;;;;:,,,,;;;;;::::::::::::;IIII;I;;:,::,::I;III;:,^
           '1:     '{-+]+>`|<+][_<!>.
           ^)!.    `{?){1{^1[)[{[]1v"

                       >]_~;+I<!-?;->+]>?+--?~<l_l:[][;<_]~<<'~<-_-<>^+]]:++_!:+<~_<~+'
            .''''''''...```'``^`^^'`'""`"``^^'`.`''^""'^^^`^:.`";^`^^ ^^`'`^^''"^`"``^.
           Ii::,,,:::;~l""^""",:::;l<IIIII!II:::;Il~;;I,"^":!;;:,::;;<:^^^^"^::::::;I<I:::;;;;lllll>i~i!ll<li`
           i",IIlI::, l.i:l::l;::,`.;     ~<-"    .~ :->+>. I  <~i!  I.::::^!;:,:,;" ~^   ',,:.   .;`<}]-_['~:
           i""I!i+>I> I.!!i!!ii~!l; : ;<_~~[_?~!<  > '+_-+  ;  ~_-?. ; I>~~:<<+!+i+! l.   '<i~.    ;  [_{]  ~:
           _<"^````''^<"....'`^^^^";<,:::,::,l;,l,:+,"";:"'`<"^";;;^`!^.   '.. ''. .`i^''`^...````^!.'I~~+,^-:
           ~?}_-_'.  .+`..'.''`````,<''...... ..'`^i}[<i<+-^+i~+_]I''l':<+<~([],>]{I'!>~_>l?_?__I ^i<!~<?:^^-:
           ~<<>++-<][,>.           `i              l<_?-[<` !>_+!`   :   .' .'`  .'  :_{?+<i+_?[~>^ii~]]]>  i"
           ~__-{?"'^^.~'    ^:.    ^>     ."`     .I'`^:,`  >~>i!:,",+;;!l:;l:,^:liI:+_-<iiIi>li<<l-><+-_l"^~^
           +I'^:'     <.           'l             .;        I<+-?~i  i "i!!!]_~':_-, ii<_[<++;    .!<!_~?:  !^
           _l.  ''''^^~"'...   '```,i``'^'''..''''^! ''''..`!>_~I .''!`         .  .`+`  .     .'`^!+]]]-<'.>^
           >?]+~i[-];^!<]_>>]]_^```,<]~_i-]?[-"```"_?-<<<++,<lIi<-;^">"--i_l[?_Il}[_,~<>>!I~>_<il^;>~!>_-,^^-"
           i"^"`'"",. ;.^"``:,,    'Ii{-+>^:I`    .i>+++]>, i<++<;.  : ""':':;I`.::" :<[-~<~+--~i: :_+?]}l  ~"
           i^         l            ^-_~-?l^^^,",",l_<__[?!^"?i~>!^,,,~"^^^'^^`^":,,,"ii+~<>:i_~__~l<~+~-_!^^]"
           i^         ;            ^~!!-]<I??]_~. `i?-<i<__'~!i+-]:..I.-?!-l{?[l;[?+.Ii<+iI-<_+_: ^><l+~?".._"
           _,        .i.       '''':_~+<?]~~-]?_i.^i<__}[I '~-]-!....i. . .    ..... ;_{[+~i_-[]?_,<i-][[!  <^
           _]--+-~_--;+iiii>ii<,,,,l+,:,:"^^"^^^",I_?]<+i!!"~""":,,,,?^^^^^,+__:,,,,"i"""""",I;;I;l+<>>~~,^^_`
           +;"I:I,I;I l!_?-]]-:    `;             .!-}->+<I.I        <     .iii      <            .!?i?--I' >^
           _^         I"!Il!lI     ^I     ':'     ^<;l!+>, .l  ."^   >               ~.    `".    '!~<-?I]; -^
           _"         l            `;             ^i        l        I               !            .!]-+~'   -^
           ~^         !^`'`^^"""""";>^''''`''`^^^^I+""``''."_^^``^"^^>````''^''''^`''>'. .'.''.'`^,>+?-i `^^]^
           >`         I~-+_]?l.'```;<~_-+-l-~_+[]_"<[]>><++^_i~_?:^^`>''`^-_l~]-<^`''ii>_il_~_-_;';+il<<_,""[^
           >`         I<[--__-+l   ,! '`''.`''.''''!+}-][!^.><+_l    I    '. '^`'    I+{[~>i+_][+l`>>_{-[;  +^
           >`         l"^``'`^^'   ,i             ^l`"^l:. .++<>l;I::+:::";;:"":;::::++-~ii;>>li>>!?i~+?+;"^_'
           +`         !            ,!             `;        !~~]?<!  !    -i"i_-i    <>+-?<++^    `><>-<-^  <'
           _`         <            "l'...'.''`^^`',! ......^!+_-, ..'+.'''  .    ...'_   .      ..^i>-_??i''+'
           _`         !            `i~-~~I-~~I`''`;_]-l!l~<,<;!<+,``^<`^":]-i~--i^^^^->~_>i_~?~>,':i>!~?-,,,}'
           _^         l            `I!~_<~?_]+li: ^<~]-_?>".;<~-i    ;    "` ";:^    i+]]<~~__??l,'l__]?[,  ?'
           ~`         l            `l?]_[_,,;;,I" "i`:I!l` '~_~>:""^"~,,,,::"``^^""":_~__<<:>>>~>!;~~-_]-i^^}'
           <'         l            ^::;Il^        ^I       `~>__??! .l...'?>"~--i . .i!__-~--,    ^i<<-+_`..]'
           <'         l            :l        .```',;..   ..^~++-;'`''!....       ....!  .'      ..,<i--__l  +.
           <'         l            :?_~>i;~ii;^"",I<<ii~<:^:_!<~+;:::~^"^"i>I>~-i,,,"~Ilil;!!<>~;"i-i>>~<"^^-.
           <'         l            ,i><~+>__-+l:^ .l_]][{; 'l~_-!    ;    "".:Il"    >+[]~~_-_??l"`><_]_},  <.
           >'        .>            "!_?-[--II!!;^ `;;il<i^ '>+~+;",,,>^^^^`^^'`^^:,""-~_<!<,><+~+~!+~-+]+!``_.
           _'        .>            ";"l!";l       ,;       'i+~-?-!'`!....i~I+?[>''''_++??~--,  ..,i~i~__'''[.
           ?'        .>            ,:             ;l       `!+_?:'' .I       .  .   .~..`^.''     '!~-]][I  ].
           -'        .>            ">+i!i<<;<~>_++i~!Ili!"^:_i><<:"^,>^"^"l!li>>l""^"~IIl:;Iliii;,!~>i>_<,""}.
           -'        .I            "l--~il!';^I!ll,<_~]][: `<i<-i    :    :,'!>!,    ;_[[<~__?]-;''I<~-_-'  ].
           -'        .;            "i+!+;``"^;"^. "!;><_<" ^-_<<"'^",>"""`..'   .^^^"i-__><,<_~+_i;<_]-}[l``[.
           ~.        .;            ;>___?-ii~-<<: ",       ^+~~+?-!`"i`^``><;_-]i^^^^i++++~_-:...'!+ii+_~^``-
           >.        .;            I<l!!<I        ",       `!+_]I^'  :       ```.    :'^,,`^^     ,<!+]__:  ~
           <.        .l            I<<ll:I<!l!,"""IiII;ii;:l_>>>l"^":<:;;;!!I;:;,""":~;;I::,:;,:"^!<li<]+l::-
           >.        '>            :!-_+i<[_~i.   ^!~_]-}: `!!__<.  '<    !l^~__;   .<+?{>~--[+<,."li>-+]'  _
           ~.        '>            ,l_+_~?<_;     :i<_+_+: `i~~_".`^:+''''  .   .```^~__-<<,<+---~:i~?]]]I.']
           ]         '>            ,i_+~>+_+<     I;       `>-<_-_i";~`^`^<+I~-]i",",+<_~~~++:`^^^l<>!<->`^^]
           ]         '>            ,l~+-i<I><     ;;       `!~_-I,` .l    `' ,:,'    l^:II:::     `l<+?]["  ?
           ]         '!            :>I,,",;,,"^"",><I;:I,"^I_>ii:^":I+,:,""""``^:;;;I+,`^``'`"""""!~<_+[-l^^[
           ]         .;            :!+!?__[_~,    ,>+<?--, "~!~]+'. `l   .!i"---l...'!+_]!~]?]-+".:i>i_-~. .]
           -         .;            Ii~i_~.        "l<__?]; "<-+-^  .^!....       ...'l?{-+<I__]?_!I~~?]}?; .?
           ~         ';            l:             ,"   '   `i->~>>I,I+,,,:>>Ii<~l:::;+__<><<~;,,,"<-<~~]_:,,-
           ~         .:            I"             ,"       ';+_[!I^ `>    "".;I!`    ;;li!Ill     :>!<?+-.  <
           >;:::;;lll!>,,,,,,,,,,,,!I;;;;:,,"""","ll",":;;;I>-+-;",:l_::;I::,"^^",,,;>,,","^`""","i<!+-[?i:;~
            ....................... ...................'''''.   .'''..'''```''''''''''``````'''''''.. ...'``.





















```

*Figure from page 3 (2346x3317 px)*


---



Sub Entry



Category Subcategory



subcategory Type



Parameter System Home position 2-byte;



parameter integer



Machine Microns;



coordinate integer



system origin



User Programmable Microns;



parameter travel limit integer



G60 Microns;



over-passing integer



amount



Backlash Microns;



integer



G/M code Simple call Charact



macro er



Axis move call Charact



Program Charact



name er



Pitch error Integer



compensation



NC optional Integer



parameter



(long word}



NC optional Integer



parameter -



(word)



NC optional Bit string



parameter -



Axis



Type



Liner



axis



Rotary



axis



Liner



axis



Rotary



axis



Liner



axis



Rotary



axis



Liner



axis



Rotary



axis



Liner



axis



Rotary



axis



(bit)



Liner



axis



Rotary



axis



4203-E P-160



SECTION 1 DATA SETTING



Internal



Data Elements Unit Data



Type



32 axis Inch system 4-byte



Metric system integer



32 axis Degrees 4-byte



integer



1/1 axis Inch system 4-byte



Metric system integer



1/1 axis Degrees 4-byte



integer



2/1 axis Inch system 4-byte



Metric system integer



2/1 axis Degrees 4-byte



integer



1/1 axis Inch system 4-byte



Metric system integer



1/1 axis Degrees 4-byte



integer



1/1 axis Inch system 4-byte



Metric system integer



1/1 axis Degrees 4-byte



integer



10 4-byte



character



4-byte



character



4-byte



character



384 2-byte



integer



384



2-byte



integer



64 4-byte

- integer



120 2-byte



integer



512 bits 1-byte



[Supplement] The unit system for data setting can be set at NC optional parameter (bit) No. 9.


```text


                                                                                              .^^"^': "'.^"'
                                                                                  .'.'`...   .,]]?_>-'_I;_[I
                                                                                 "[]~<+_+[;l.i-+__;+[<!~-_-l
          .``````````^```''''''``````''''''''''''''''''.''''''''''''''...''''''''''.''.'''''.'`'''```. .'`^'
           ",,,,:::::,:;::,,,",:;;::;:,",,""""""""";;;:,,;;:;;;;;;;;::,,,:;;;;;;;;:"",,"",;;;;;;;;::""","":`
          ll"""":::;;~;:::;:",,:;;liIIlI:,"",:::,:i;:,,"^,;!;;,,,:;;!;::"",:;;;;;;;;!:::::;;;;I;;I!l!I::,::l.
          -;^^"^`^^' _.:`"``"`'^`.^l     +I>`    '~ ;+>>l..i..>i!;..i'^`''',`'`''`'.~`...''``''''^l,?}-_]-'-:
          _,I<--]_~< i'_<?<+-~?<_;.I ;iii-}]~i!l .I "]-]-  I .?-?-  < >+-_i?--~_~?! >.   :<<+    .; `-~]_  ~,
          _;        '>.      .'..':> ,I::::,!;:;.`l ."!:,.'i. ^!!l..<.            ..i.          .^i '-__-'._:
          >_-?-]-?]?;<++>~<~;'`","I~_~!!!;ii>+i>"">~<>!!,^"]!<<~:^""<^^^^!-l<<~l""^^i!!>i!<>~<>;"I-l;!<~l;:?"
          i:^l:I:I;; I>[-]]-+l:   ':";,:;:llllII. l--[]}i  i<-?_.   ;    "i'lll"    ,_1]<>-_?]-!^'ii~]_}:  i^
          >^         ~Il;l;;!!;   ^:             `<;!i<<: .i?_+l^^^^>^^^^''^'.'`````~~?~i<:>__--+;il_+?+>""]^
          _"         ~            ^:             `>        l>~_?-~''!''''<1i-][l''''++_]?-??l..  "!<l>+-,^^?"
          -"         >            ^:             `!       .;~_-!'`  >     ' ''.     >''^,``^.    .l<???}l  ~"
          -"         !            "~<>i~>>i"":,"":~<>lii>!:~i<>!;:;;[;;;;l;::;II::::_;,:"",,;Il:,l+<~<?+;""]^
          -"         !            "<_?-_]-?:'    'i]}-<_+i'>i~_+.   i    ;I`!_<!    I+_?i>]-?]~;'^i><__]^  ~^
          -"         !            ^!>>~>?<~{~`^  '!I>>_~, .~?-_;.'''i''''  .    ...'i_{_><:<__-_<:~>[?[]>`'~`
          _^         !            ^I+<__~I,>+]<' `I       .~_+_??i``>```^~~!~-?i````<~_]-__-l^``':<!l~_+:,,]`
          ~`        .i            ^"             `l        ;~_]i,^  I    '' ^,,^    i^,!i::;.    .;i+-_?:  _`
          <`        .-::::^^",::::!<!:,",,,,:;I;:l+I:",",";+-++i,"""+""",;::,"^`^^^"[,"^^^`^,^""^;i!~~[-i:,]`
          ~`        .~>+]+`.`'.   `<-~_[_?<+_?~_,'i]-<~~+>'!ii<_^  .<   '->:<?]i . .~~]_i>?-]_~: ^l<i__-^'.-`
          -`        .l<_>_++]-I   ^>~_>-I<l+I    `ll+-__; '>_+-,  ..<....        ...i+--~~I++?]_<^i+--[}l  _`
          -`        .;            Il             ^I   '   `?[_~+<I^"_^,:;-~l><<l"",:+~-_+_<~l",,"l_~~~-_:""~'
          -`        .;            ;;             `;       '>~_-~l,  ;    l^ I!l:    I,!<<l!i`    ^>~_[+]^  ~'
          -`        .;            :!,,,^^^",,,,,";i^"`^`^"I_+_+,.'^^i^^""`^"'  .``^"~`'''' ..''`^;~>_-?+i"^[.
          ~'        .;            "i-[[,   ..  '',~]-<<<-~^<!i--^..'l.''`<+I_??i.''^<<-?><-_?+_" ,!><+~-^`'[.
          >.        .;            "li<-:<++++-<  "~i-[][l.'l_+-:   .i       ''..    ~?]-<<l_+[[_<`;>_]?];  ?'
          <'        '!            "i[__~+-"''^"  "I.'`,^  '<-i<>!l,;-"^^";ll!!>l;:",-+~<>~>_<!ii!Iiiii-<;::{.
          ?.        'I            ;;'..'.        `"       `~+_-+>:  i    :I`i>~;    i>~-]>+~'    "i_~--]'  -.
          ?.        ';            li`'`'''```````;l`^`^`'.:_+<~".`^"~^^^'. '   '^^^"!       .''^^!_~-_]_I''_.
          ?.        ';            :_)[_][]1I''''',<{]<<+-i,_;i~_"^^"i^^^^>~;_][>"""">i>_!i+<-__:`i+>>~~+``^-
          ?'        ';            :,`^`'^^`      'l-{?]]!``!++];    :    .. ""^'    ;-]]~<i-_[?<;">>-[-],  -
          _.        ';            :"             ,l^,,l,. `~]++I;:":>,:::Il;"",""^"I--_~<<I<i!i>ll+>~~]+!,"[
          <         ':            :"             :I       '!~_--+I '!    !!"+__;   '~>_?-+-_'    "!<~-+?'  ?
          >         '!``'``.  ''''l:.....''  ''''I!''....',>_+_,.'`,+```'     .''''"~.''' ....''':!~?][]I..]
          _         `_?-}~i_?],`^`i_}?-_[!<]]^`^`I<+_--_?i;<`^`^^^"I-,,,"^^!-;",,,,;?,,^^^^^^^","!~<!>-<'.`]
          ?         ^!>-?<<;,:    l;"^^",'^:"    `l-,:,,:'^!   ^.  .l      .,       I     `^     ,!+<]-?Il^<
          ?         `I`,;",       !i"""^""^^":;l,!<_;`^`^^l~,:,","^:>^^^":::,:,^^^^,>^",,,,,,,^^^>~>i~~++[i_
          ?         `;            ;i_+_;~<>_li]? "!>-]_?-:`: ..^'  `l .  ..!_".....`l.....^^'....l<ii++_   _
          ?         `l .     .....;^ ... ...'.. ."i-'     ";..'^'  `l . ...  .     'l ....^^   . I<~?]+]]]!?
          ?         '>_ii_+_<"^^^^l:^^^^^^^":,^"^i~~+~<<<I;i,,"^^^^:<^^^,,,!<,""""";+",:::,,"""""!<i<~_+;I;}
          ?         '!i~?1>;"     "'     .`      :i~lI:I;.."   `.  `!      `,      'i     `'     "I>+?-+,"'?
          ~         '~+-<+I'`^^^^^!:^^,,,,,"^^^"^i~<:``^""I!^^^^^^^I-,:,"^^`'^^^^^"I-""^^``^```^^l<<~+<_-]l]
          <         'i>+_~;]>~l...:^...''........;><}]1}l':<i~~~'..,~'`'''I1{!.'.'',~'`'''``''''';<<i+-+. ']
          <         ^>i<>~-~i_[<<!;^             ," ..^.  ,>+~_`   ^!              `i     ^`     "i_][][" .+
          _         "i.. '.. .... i"     `".     :"       :_-i>iiI:!~:;"""I<>I,;:::!~""""^``",:::<+<~<->"^,+
         .-         "!            ;'             ,"       ^!+_-~>^ ':     ,_<:     .:     ``     ;~<<-?_   +
         .-         ^<,::"^"^`'`^^!,^^^^"""""^`^`l;''''`^"l<?++^.'`,!`^^^^`  .`````:>^"^^^^^'''`'!<+]-[-:'"[
         .-         `i??!<[?~+]~''l"''''``'``''''l>_{?}[l`II'. .''':i'^^^`"}-"''''':>^"^^`.''''`';!i><-~``"[
         .-         '!+->~_+_~:.  :'     '`      I:'^^:^  ""  .^.  "!      ^`      `l     ``     "!+?}?{` .]
         .-         `i]+?+;?~~]^  ;'      .      I"       ",   .   ,i              ^i     ..     ,"^,;I:. .]
         .+         `<+<!+<-<<_<;:<;"""""^^"::::,!!;I::;,^li:::,""^l<^"^^"I!il:"^^^;>^""",,,,,^^^!;"^`^`^,I}
         .~         `i?-:<}-_++<  i`      .      "li-_}?" I;   .   "I     "+]l     ^;    ....  . "i~+-]?..`-
         .~         ">+?<]~i~>`   !'     '^      ,'       I;  .^.  ^,              ',     ^`     ;!+??[?^ .<
         ._         "<_-~<?' . .'.!^''''''''''''.;^ .     !!'`'....";...        ...^;............>,   ' ..`<
         '?         ^>__Ii+-~!_<^`i"````^^"""""^^l+]ii-~__<i::,^`^^;l^^^!_~~>++:^^^:l",,,,""^^^^^<ilii_<::I+
         '?         `l_-i_}_?~>,  I.     .'      llI":!;li:^   '   `,   ^;:::li`   ^:     ..     I:"l><l  `-
         ']         'i[[?:^,";    I.     ..      !^       ,"   '   ":              "I     '.     ;'       '-
         ._:::::",:;l>+++:,,:",,^"i:"::;;::::;:,,<l,:I;;;;>>;;,"",,i<:;::;;;;,"""",i~:::::,""""""!;:::;;::l-
           ....'I:`^""```":"''.'I"^'^",^^^,""^"^`'^""^"":"^`^^^`"^``^"^",,,^^`^```"`^^^^"^"^`^^^`"``^,^^^^^.
               '?+i++-+i_>+!   .<i_:+>>I-<__~!l+I;_]];-?]<~~;+_:~-:~-l+<l->,_++<<-~:_+~~<-+-"++]l_-;^]
                                                           .                       .         .




















```

*Figure from page 4 (2346x3317 px)*


---


## 3. Data Set Commands

4203-E P-161



SECTION 1 DATA SETTING



The data set commands are detailed in the following pages, and may be classified into three groups:



commands for data setting, commands for parameter selection, and input/output commands for



peripherals.



3-1. Commands for Data Setting



This group consists of three commands:



SET, ADD, and CAL



3-1-1. SET Command


#### ADD CAL SEARCH ITEM t ITEM! [EXTEND)

Press [F1] (SET)



The data entered itself is a command serving as new data. The SET command is effective when function



key [F1] is pressed, and displays "S" on the 21st line on the display screen.



Enter the data from the keyboard and press the WRITE key, then the keyed in data is input.



3-1-2. ADD Command



=AD



ADD CAL SEARCH ITEM



ITEM ,I. [EXTEND]



@@] @J@@@ @J @J



\ Press [F2] (ADD)



"AD" is displayed.



The data entered is added to the current data to form a command serving as new data.



The ADD command is effective when function key [F2] is pressed, providing a display of "AD" on the 21st



line on the display screen.



Enter the data from the keyboard and press the WRITE key, and the entered data is added to the current



data. The result of addition is input as the new data.


```text


                                                                                               '"",^^` :'`"`
                                                                                  .''.''...   .!]?]~+~^_:i-i.
                                                                                  ![+<>~~+]"; ~~~!<I]->l<-]-`
           .^^^^^^^^^^```````^^^^^^^^^^`````^^```````'''''''''''''''''..'.''''''''''.'..'''''''''..'''..''`^
           .`,:::::"^`'''^^'``",""^^^^^``'``""";;;;;;:,,";;;;;;;;;;;;:,,,,:;;;;;;;;:::::::IIII;;:::::,;IIIII'
           :).     >)+_??:>|<-i,}i><<i<<><ii+_l
           :{;     >}?1]|il1}{<;]~}}_[}[))+}}{[
                 `'
                 l+?;;-]]^~];;~_>i~?~~+`-~l;_~?_<+;l,i_+"_<i>+<+;I<+_~l <i>:;>_;:~!^++~~-_<i^!~"l<l~>^~!l>ii.
                 ;li!!i>!<i'<<,^~+-l`<~-+~l.l~~<~<<>>~`~>;^<~<~-+_-_:>~><i_li^,+!_,;~>i+i!<>li^liii~i!-~i;?<`
                 i<>>><~i~< ,;..III".I;I:!l "I:,::!;;l "l`'!l:!,Ili, ;!llI!;l' iIl."!i;l;Ilii; l!;I;I!;!I !!'
                .><i<>i>i>>`

           l["<.   >-_-+_~_?~-[i~]~:]+[[_:{_]1-<-"
           '".'.    `^'.`.""'"^` ^^ ,`:," """""^i.
                 >_+!:-!!!,;ii<~++">l_>i<I:!!lii<>_~`
                 '`:,"l^",``^^,:,:',`,",;^":,"",I,;;.
                 ~{<>.-~_~'<+<!i<-l
                 .`.  ''.. '..   '^
           l!I,!.  l{_i"<i~i>!~>~.
           ^^''`.  `;^'.",:,,,;,:

                         "'                                                                  ",
                         "'                                                                  ::
                         ;'   ';                                                             ::
                         ;' .i[?,^^^"^`^^^`^"^^","",,^^^^^^,^^,,,,^,^^^^^^",,,"^^"""^`^``^"  ::
                         I'  <" ....l'.   .`I..  .',;      !"''''''i'..  .^>''  .':l'     .  ;I
                         "I .;~-I   :  +-i .: '<-' ``i-_}+!;'      l ;<[i: ;'!_};`."`-~>+]_I !^
                          ":iI;;^'''^`';:"'',^";l,^"",::::",^'''`..,`":i;^'"'";i:"",^l;,I><l;"
                            !`IlllI!"^!lll!l`Iili!>;^lI;:I!`"ii<!l;'l!l;;i,`!lll!i":i;;;l:''
                           ", <`]i,'>>lI-]`iI_']~-.<;l;]}"ll>'+}].+^+']1<'-Ill--"i!<`]-1.?'
                           l..il>-II,^l:l<:!'I:ll>II^i!!>li"Il!li:i'iI!<<Ii">llI,>,!l>!_;<.
                          ';   .'+;';i<<I~i;;__<; '   .. .   ... .   '....   ...'   '.'.'
                          ;"'     ,,I!!!I!:Il>l;I
                         .l<+l~<[[-?__'
                               .......
                 l;,`,,:^^,;,",^^:":,"'^'^^""^"^"^^"`"^''"'`^^``""" ':"`^;,;````^^````''':"'^`'.'^'''`.''`.'
                .l!~I?]?i<~__<_i;?~+l+l~l<<>i>]++!__!+>-i]l!++!!-_-".l~<:->l,<<i<>~<+!ii<_?>-<-l++~-I!<<~+ii.
                `+<i:_"<I<:ii>i+_l ~i+:+<~>_~>'+l.~I;~<:<I~;~i~^iII-_"~+_~-i"<!i~~;
                 :^,^'^,`':""`,``^`"`'`'`,`^"^.''``''``."``^",,":``'`.^""^^;'^"````'....... ..  .
                '+l~+,i+<,__?I<!!iI~_,<__+~_~<I]><<~<__;<+l!?+_i-;<+?:<_<!:+<l~___-l<I!]]-;+l++~-`
           '.'.`    '`' '                                                       .             .
           <!;I+.  >]_];<>++_~]>-^

                         :                                                                   ^
                         i                                                                   l.
                         !                                                                   i.
                         i   `<)!..  ......  ...... ....... ......  .....    .....           l.
                         i  'l],"^^"l^`''^^II,"^`^^l:^"^``^!^^^^^^,l""^"^^II"",,::I;"^^^^,^  l.
                         !   II"'  'I .""' :: '"`  !`:,,:"'l      'I ^,^`.,: ^^`. !^`^`^`^`. !.
                         "I`.>?<^  '; :]]: ,, ;-_. l^[?--+,"      ':'!]1l`^"^>]}!'I'i[_<}(?,:;
                          ',>l'"^",:",,"^,:""^"'`^:"^'^''^^^`,,^^,^^`"`^"::""^''^"^^:"^`^`:;"
                            l.iI-+iIl^i!_~li"ll_<<;i^il-_i!:;l>_~;i'il+-~!i`>!~~!i::!>~_l>'
                           ^: _'?!l'_Il;~-"!l-`]i[.?Ii^_]I:<+"++[.~"+`[]-.?l<:_>";+i^~+).~"
                           l' ,I,:Il^.I;<1;;.^I::;I^ :;"":;.'I;:II: "I;;:;" I::;;I''l;;II:
                          'I             ;,.>>+?i+_<i]_]l
                          ;IlI^:^I;lI:I^  '`'`^^",""^^^^`
                          I!-<:<!~___++I

                .-<<:<-?li~+_<~>!i;~<_~i!<:<<I;li<i<:>_-l!Il~!i,!:!!i>!>!!;I!ll>!;;>,li<:!>ii.
                 ^`"':;;"""^:",^'"^:",:^',.`,``^","^'";;,^`.;,"':`,,""^:,:`^;^",;;"l^";;`^;;I'
                '~~l,+>~;:i!!l!+>>;!,<~<>~>iI+!<lI>!!_!<;<<!:~<_:!;>>!><i;,i;!!<<!II,<>>!<I"!">-<:I>:~~Iii!>
                ">i>:>I_<!I?>>+_I!><>~<:^^^^`^`,`',^",",^"::^^^:^":,",::,^,:^"":,;I,^::l,;;^, ^:, ",`";""^,:
                ',,"`;',;: IIlI!^,I,Il:
                ,+,!!^~I";~!IIl:l"il,:II<l!iI,ll!llI!>;l>;l~<~>_!;i!^:ill>i;,l!i!!l,!i<;l,;!iill;:;lI";:IIlI
                ^+>-i'~->l<~~!+l<i>~~~_~ii><i;ii!<i<~~l!<!;+i<,::"li::l;:;I;,l;!ll!"I>>II:Iilii;:;,Ii"l!:!l;
                '~+_; "li;^<>i~"<:i<<<>l,I!,<~!;l_,liI:~<l:~__,















```

*Figure from page 5 (2346x3317 px)*


---



3-1-3. CAL Command



SEARCH



Press F3] (CAL)



4203-E P-162



SECTION 1 DATA SETTING



ITEM t



ITEM l [EXTEt-0)



An arithmetic operation is carried out between the data entered and the current value to form a command



serving as new data for setting.



The CAL command is effective by pressing function key [F3], providing a display of "C" on the 21st line on



the display screen.



Enter the data from the keyboard and press the WRITE key, and the math operation is executed between



the entered data and the current data. The result of math operation is input as the new data.



3-2. Commands for Parameter Selection



This group consists of six commands:



ITEM, SEARCH, AXIS CHANGE, CURSOR, PAGE and EXTEND



3-2-1. ITEM Command



=IF



=IB



SET ADD CAL SEARCH ITEM



ITEM



[EXTEND]



IF"~-~


# @J@@@~@

/ Each time [F7]



Each time [F6] (ITEMt) (ITEM!) is pressed,



is pressed, the screen the screen display



display switches to the switches to the next



preceding category. category.



This command is intended to select an appropriate parameter from those belonging to the subcategories



in the table given in Section 4, 2. "DATA SETTING".



The ITEM command is carried out when function key [F6] or [F7] is pressed. Each time one of these keys



is pressed, the display screen is switched over to the preceding or next subcategory items.



"IP' or "18" is displayed on the 21st line on the display screen and the screen display is switched over.


```text


                                                                                               "^^"': "".^"`
                                                                                  ....`...   .^]?-_i[`~i;_{>
                                                                                 ^[[+i~-~}lI^;~++_I+[il>+-?<
           ^^^^^`'``````^^^^^^```'''``````''''''''''''''''...........'''''........'`''.''''...'''.''`'..''`'
          .",,,":,"^^`"","""""^^""",:;;;;;:,,,,::::,,,;;;:,,",,,,,,",:;;;;::::::::;IIIIII;::::,,::IIIIIII::"
          .>";I!  .>i_'I!II!l!li:
           :`^":  .:,I^^::,;:l;I"

                        .I                                                                   ;
                        .;                                                                   !
                        .;    `'                                                             >
                        .I  '+[l```^^`^^^`^""^""^^^^^""^^^^^`^^^"^^"""^^^""""""""^^'`^^^``.  >
                        ';  '_  '''":'.  '`l"`. .''!'     ^i'```^`:l`'. '^l:`'.'`^!^....     !
                         l. `i_<'  ^^ :+~' ,. ;~:  ;`]<_~>";      `".;i>;.,'^l~i, i I>i<<+I '!
                         `;"i:>;'..^,.;~i` "` :il. "`<>>i!",      ^"^:i~".;^^;~>;.l.I<i>+[<:I'
                           ,>^I;IIlI`:l":;!"`l:,,Il`"!I;:!;`Iill!!""!l:^;I`"illli:^I;"::l'^^
                           ;.l;i_i.>:+`?-~'<lil_-:I;i^-+]'+;_^?1!"i:ll]1,il<"-<-`[:i:_{>:~
                           ! I!!I!:>,<:i~<,i:>l~_I!^I,ll>`<">"l~>;l"i!>_;>;i;>l!,]:i;!_i;<
                          ,,  `''`"'  ^``'`  '^>+"`iI~i;i~;:l~I^`^  '``.`'  ^`^^"  '^'.'^
                          l                     .,^i!<>i<~~>>>i^
                         ^>_i<<<_?-___'
                         .`,",:",:":"".
                '^'.'^^''''    ..'.   ....'.....'..'.. ..`  ...   .        ..       .
                ;_li<~~li__!;?_<i]+~;~!;-!i+~l<~<---?_-~I]+l>?-+i-+[>_-l_<_<-+I<~+~~+l+?i_!+I+iil>!><__~+_+<
                ;+<i>~iI-:I_+iI?]_l_!,_?[i~;                          . . .  . .. .   .... . .. ...''...'.'.
                ^;^'^,I`"''"^`."",'^``^^"':"                      .
                ^>i!I!_I'i<>ii+!>l+;~?<<]~>!-!+<+_-++~+~<-]>ii_-l[<}>,~>>+_+~>~l?+_+?il_,+i,~!!~~l+>_!+<<:~;
                !+<:?_~-+!I+i<+<;.''' ''''''^`^''``'"".''`''..`^`^ ^^'^````'","`^":^:,`^ ^.."'`^"`^`,`"""`"'
                ":,.;;l"I:.:^::^`
                iii-;"!i`!+>;l;>;I_i;><><!~<il+l!!~!>i:>>:++?<<_:i!i'<!ll>!,!!_<^i><I~!I;;l,!!!;Iii!i>~i>ii,
                !<<!<!_<>+>~+~>!>i!+<>I+<<~~>l-~~I,+++,!~l!>;<:>l-~il+~i<<<II>>il~_><i~<l;<i~l+<~i;,;lIIll;^
                ,;l`!;<;l!";>>!,il;:!!'l!;llI"><>^ ":>^;i!l:,!^I>~;'><<l~>!:,!^!+i;:_"l<!^><!`><~;
           ` '     '               .
          ,[I1^   ;-~]?+_-{--)+l}]:-~{_[-_?[[?"[{}[[_}+?+.
             .  '` .      ' ... .. . '.'  '.'. ..''`''''.
                :~~~:[<i-i;~~~_+_;!>!_II+><~<]i~+'
                '^,,,"^::"",^"`'"^"^'"`^"^^^"`',^"^`'`` `'.'`.   .`''``'..
                I>__['>}<+-_~_;"___-;~>~--~-]`l+<-?]~_?"<__?):+~_l_~~~?-_~'
           . .     ..`  .                                     .
          :+<il^  ,<++{!<<~<<~_<_'
                              . .
                        '                                                                   ^.
                        ^                                                                   l'
                        ,    ^<:                                                            l'
                        I  ^`i{+ .          ....                                            !'
                        ;  ],",:"",I"^``^"Il::,:,"l,``^``">:::,^^"I^^`^^";I"^`^::l;"^^`^"^  >'
                        l ': ,,'  .;  ^^' :, .^.  l`,,^"^'i      .I `^^''`: ^^`. :^.``````. i'
                        ^:l^'[-,  .: "]-; ,, :->. ;^]]_-_l;      .:'l?|i".^^l-);."':?__[{?:";
                         '+:",::;:,^^,^`^:"^",`":;,,,,^'"`^^,"":;,,^"``^"^"""::;^^^;,"^"^:;"
                         `: `il_<:l"Il<+~;i^>;+<!l::!i~+;<^!I_-<I!'>;~+ll;:!~_-I<"!I~_<li
                         ;^ ,iI-<^;!~"<_['~I+^~~>^ii:i<{'<;_`<~+.+"~'~[i"+!,~!!._l<'~]].-
                         l   ";^,;:  :"""," ,;:;;;..I;:,I: ^I:",;^ ,i{l;I'.I:>[:: "I;;II"
                        ^l~!:i`->,Ii+><>i~.                       ^:".        ,"
                        '^,^";^;,":;l!l!lI'        .'.'.'. ^`'.'`II^      .?__l>>~l+iI  .
                                                   !~]+<--!+}-!~+]-i`      +__?_i<<~~-++!
                                                   <___->_~!~~i~<-]"      .+~!++-_!]{-]},.
                                                   <{[-)~?_]?]-<~:l:      .+[[-_?;l:il"<<`
                                                   :;;:I;l::!I<;l.         ;!l<;l'
                .
                i~<!:<<!!l_!~li;i~>i+<<;>"<i~~!:+"l~!!liii_>;~+<_>i_+l><l<:<!!+i>_+>i<<iili!_>;!;<i<_>>i!!>^
                I,~~il+>+i!+>>i;>;?<>+>!I>:~Il_<]>_>[_!~<--_<;:,;^"::^`"""'^"";"";::"i;:i^:^:;^,,:;IIIi;,:I`
                :'^;I`l:l::>,l"'; lI:,:; :.;' :::,;.ll. `I;;`
                "ii^:>>~l:I;:;;i"l,:^Il,!I::;:;!;I^l,:li;,"l;"<<<l::;iIl:,:IIlIIi`^>;;I;i;!^;;;^ll>IlI::I:I`
                lI<iIl>~<I~~>I_-!<>il+~l<~:<!l<~~_li~l<<<!i<-<<;++i!i<;!Iiii<++><I:<_~ll~!~!>><:l:!!i>;:iii^
                !^l!liili^"l!'i!>l_:;>I!lI'l^!i!!li>;:li!`>`I<;>li!>i~I~^i'">>;:!~<>-<_~;>^~+Ii;
                ,~;.,.">l';':l,I;,:;^^""l:`;::,^""."^";".;::","'"""",'`:""::^'"^"^"'^:,:,"'".^^:::,",'^^".
                "i``!'^~l.i:!<+>~+>>:ll;><,>;<!;l<">;;><,><-<~_"~ii~~;l~i!l<<:+!>++,i___~-:~:i+__>~+i:<<>`















```

*Figure from page 6 (2346x3317 px)*


---



3-2-2. SEARCH Command



4203-E P-163



SECTION 1 DATA SETTING



ADD CAL JTEM t ITEM



! [EXTEND]



Press [F4 (SEARCH).



In the subcategory group, which involves several data elements, the screen display is, sometimes, greater



than one page. This SEARCH command, engaged by function key [F4], may be conveniently used to set



the cursor with ease, although it is possible to place the cursor at the desired data using the page key and



the cursor key.



Operating procedure is given below:



(1) Press function key [F4].



This produces display of "F" on the 21st line on the display screen.



(2) Key in a data number on the keyboard.



Display of "F" is followed by this particular data.



(3) Press the WRITE key.



This allows the cursor to be positioned at the data number specified. If the current screen does not



include the data number, then the screen is switched over until that data number appears and the



cursor is positioned there.



If there is nothing corresponding to the data number entered, the cursor is then positioned as follows:



(1) When smaller



The cursor is positioned at the first data.



(2) When greater



The cursor is positioned at the last data.



The screen for setting bit type data, NC optional parameter (bit)) allows the simultaneous setting of both



parameter number searching and parameter number setting.



(1) Press function key [F4).



(2) Key in the parameter number.



(3) Key in a comma (,).



(4) Key in a bit number.



(5) Press the WRITE key.


```text


                                                                                               '"^"^`^ :''"".
                                                                                  ..'.''...   .I]-?~>~`_:i]]"
                                                                                  ;]?<i~~~};l ~<~~<;][lI<+_-^
           '""""^''`^``^^^^^^^^````^^^````'''''''''''```''''''''''''''''...'''''''''.'..'''''''''''''`..''``.
           '"""""""^'^^^",,",,"^`^""""::::,,,,""""""":;;:,,:;;;;;;;;;;;;,,,:;;;;;;;;:::::;IIII;::;,,,:IIII;I'
           :i!l<"  "[>!++iii;i!!!lll!l
           `,"^:^  ';"":,,""^:;,:,;;;,

                         :"                                                                  `"
                         ;"                                                                  :I
                         ;"    ^                                                             ;l
                         ;" '_!-"`^^"^`^^^^^^^^""""""""""""^``^^^^^"^""""''`'`^^^^``''`^^^^. ";
                         I" ">  .'``>^'   `^i`'..`^,I'...''I:`^^^^`i"`'...`i''. '`,>'..'..'  '"
                         "I ; i+;   l. !~i  l .li. .'I_<-<l:`      I ^l_i: l ,i-;`.I'>!i<<!: ;"
                          ";<`Il".'':^'!<!'':``Ii"'`";>i!I:"^..'''.;^^:+!`.;`,!?l,':`!ii><+i;;
                           "!^`;;Ilil^;!;I!>:"!l;!i!^"!;,:l,'I!IIli^^l;,:ll";iI;I!:`;I::;l`^'
                           I` <:~-<.<:<`[?<'<ll;]-,l;<^--['-;~^}[;:!::<{)">Ii`~i_'-;>;-[!:~
                           l  l!!I!,<"i;i<>;!:il!~I!,i;!++">^i:!>;;:^;l!-,>;>;i;l"+,>li-iI>
                          ^I". `^`^".. `'''`  '`''`'  `.~!!i;!l~<i;>l>~<!>^  ^'`'^  '^^`^^
                          :!~:_!-]?]-]l                  `I!<<l<i~!-+>>>ii,
                           . . ..'.....

                 ^',^''.`''^`..'..''... '`''''..'.'......'..''...... .'  `    .   .'  .  .      .
                 ~l+_>><~i<?-]?+~!]<<[i,]><<I<i<>i~~l-<>~iiI_]-l-_<!+i?<,->l_~i__lI]___-l+,;~>!+_ii<<'-<~?~<'
                ._i~;"><li~~+! l~~!!]>+-+i~I;!!llli!i'+!~~<><>>i;<I!+~i;!iiI}l_`!><l;+:l>i!<<lil+<"i>i+!i;<~`
                .+i<I!l>>>!?[l;ii~I,_-i!l~<I><I!i<~-_>i>~+?_~l<-I!!>~~lI<~->l>_!!~_<l_<I!>><i~_l!_!<><>lI!<+"
                .+i!;<!<<;I<>;;ii!:"il:Il_l:;;:lllli!i"l:!l!I::!l:iI!i"l>;li,<>i;>!:i<~;;>!!~ii!I>+-!I>~:~I<^
                 il;^i!!l:">>;
                 ,:,:"I;,^^"",::;:;`;`,,,:^::;",`
                .l<ii!_!><!il!i>>i>"<,-i!<">_+>+:
                  .^   :'``.^''.^'.'^`..,'"
                  li; ,!!<~!I+!i~>l:+~<I<!}.
                      .l:,'""^:^^,,'::":,`';^!;'""^;:`:,,"":"'^^^I"'","""^'^^^""`
                      .l;il<ll>!!><,<>i!_<,>'I^.il"!+:>;>!l<<:!l;+~;!~?~~-,<i>-+I.
                  ^:' '"`. ' . "`' ` '`'. ..'"'....' '.'.
                  >-: "~~+^!,>,]__;l<!<~+^l<:_<Il+-+i~~<!
                      ';:,:,".:",l`"^;:;",,"^"'";"^'^",^'",',;;"
                      `I>~i<<`i^": i;!~<i~+<;<>I<>l<~~<<!>_^<--_.
                  ^:' `,'`' ^".',,,^:`.''
                  i_, :l!~~Il>>"+<>!i!;__!
                      'l""':l`,,^;^'^^,^"^I^:,`,",l:",:"":;;"`;::`^^""""'`^^^,I^,.`;,,`''`^^^"`^^^^`',`^''`^
                      ^>l~I-_<_+!_+!i+<~+I_li-!+i__<l>_!>+i+<;+-?i!<<!>+:!~~~+?++^;<<~>I!<>~<!!>!+<l;_<+>;<<.
                      :i!Il>l,ii`<_~I:>!i<~!.->~;~>i:+li+<"<I>~-_i><!:<i+^<i];_>_;>+?l:~>+_->^[_~~++i;-i>~<>.
                      "i<~~>:+:+~__<~<_><__>~                   .  .      .    .. .... ....'..``'''...'....'
                 '.'  .^^`^`'^`^`^`^``^''`"``
                '_!]__~:~"~+-_<-:><!<+-<<~?<-i+:~-~:???;ii<<~?;<<~-i~-^~_~;<<~_!:_:_+_:<<+-~<~~_;_!!_?>~_!
                      . .      `.   ..`....."'.. .' '''..'..'' '.'`.``.''`.``'^'.`.'^^."`^``^`^^."`.^^`^"`
                 .!<^ ;]+_-;!~i>~~I
                  ''. `:'`^.'`'^`^.   .       ..
                      ,-<<:<>+~>,~l_<?_~>~?i>?<]_I?~+;]--I
                           .      .'.. ...' ..  ' ..'.''''
                 .+?" I[->+:i~<___:
                  ^^. '"''^.,"`^^^    .
                      ,i+<,+i~+>,<l_~+__<+-><-l-+,_->l_]],
                 ,^'.'.'``'"^'`'^^^'`^`^.``'^`'."^,^''^^^''  .  ...  ...   .    .                      .
                 >i+,~i<_+lI+"i_?+i~;+i<_~>,?_?":[<^<-<<i+~!++>>>_+_^i_]+,?++-+I-_i>~<!-]++~>i<l??{<?l~<<~_>
                "<~<~<~-?l:i<+-~>"__->~-+-;~<<l<<!_>~]_!:~!<~<<"<~-<<>. .     .  . .. ..'....'..'..."'. .'.
                '"`'`'''`  '`.''. `''.''.,'^^^`,"^,`^""`'""`",^.,""^:I
                 .!!' !>i<~:!lI!+i!,>>:!~ii
                 .^`' '.^,:``^',"^".,;"^^",
                 .!<' lil^:,:!I`;l:!:;lI"^:;I!II'
                 .ll' ";!;,,";!"!!;>Ii!>:,!!lii!`
                  ,;. ,:^'^^'''^^`^`' .
                 '>+` l<_!Il;iI!i!!>!:!^
                  '`  `'  .   .'   .''.
                 `~]` i-->;il!i-;>>>~__"
                  .   ..    '   .''.'.
                 ']]` i+_+?l]?~i[-]i[>>__;
                                       .'.













```

*Figure from page 7 (2346x3317 px)*


---



3-2-3. AXIS CHANGE Command



=/J.X



SET ADD



AXIS



4203-E P-164



SECTION 1 DATA SETTING



CAL SEARCH CHANGE ITEM



ITEM l [EXTEND]



.}~,~F2



)@@~@@)@



Each time (F5] (AXIS CHANGE)



is pressed, the screen is switch



over to the next axis display.



In data setting, if there is a parameter of axis type, the 5th and 6th axes cannot be displayed on the same



screen. The AXIS CHANGE command is intended to switch the screen from one display to another.



Since the pitch error compensation data may be displayed on one axis per screen, the command is used



for axis selection.



When function key [F5] is pressed, "AX' appears on the 21st line on the display screen, resulting in a



screen switch.



3-2-4. Cursor Keys



Move the cursor in the arrow-pointed direction, where the cursor stays at only the points including data to



be set. When, for example, the cursor is at



rest at the extreme left, press the cursor key



@ ;



this brings the cursor to the data element located at the extreme right. When the cursor is at the



extreme right, press the cursor key



@ ;



this



brings the cursor to the data element located at the extreme left. A similar relationship exists between



the cursor keys



and



@ .



3-2-5. Page Keys



When the@ key is pressed, the screen advances one page in the same category only.



When the



key is pressed, the screen returns one page in the same category only.


```text


                                                                                               ""^"':.`".^^`
                                                                                  .'..'...    `?]--i{"!<:_]~
                                                                                 .??<>>~~_i,`,+<+_!<{_>>_+_<
           ````^```^^^^^^^^^^`````^^^^^^```'''''```'''''''''''''''''...'''''''''..'..'..'.'...''''''^'..''''
           `^`^^"",^""",,,"""`^`"""""""""^",,",:;;;:",;;;;;;;;;;;;;:,,,;;;;;;;;;::::::::;IIII:,,,,;I;III;:,^
          .<;il<   <~>~:l>>~<_+],li!!lliI!,
           ,^,^:   ,:,:^"",:::;l`":;:::l:;^

                               l.                                                                  "`
                               >.                                                                  ,^
                               ~'    `'                                                            :^
                               I. "-~(?"^`^``^^```^^"""^^`'``^^^^``.'''^'''`^`'''''''`````'''''``  ;^
                               ;  ;>  '^`^i''  .':<^^'.^^,^ ...''<:-~i>.'i'`' ..">'. .^";l`....''  :^
                               !^ ;.<<,   I .i>; ,! ^>i  `.><<+!:I`-_+_i^I ,!~::.!.Iii" `"`lIllil` l'
                               .;;>`~i^..':'`><; `"."<~`.`'i>><!,"^!<~+_,,`:<[l:'I`;<?!^'^^<~!>]-I::
                                 ;l^"ii<><l";;,;l!"^i;;i>l`^;"",l:^I!I::l^^!;:I>i":l:;l>:";;;;l;`"'
                                 l. ~"?->.<:_^{_i^!>;i+]^>;>^]_?'~;~"[{;;!lli])"<I>"]>~`_"iI?1!I~
                                .l  i;<I!,<"<;<~i;ll!i!_;<:i:!l<,<:~;<]!l;li!i[:~;i:<!!"_,>;!?lI<
                                ,;'`.^'"^,. .^''``  '``'^'  ^.''^  .^:?,'  '''.^.  ^'```  `^^'^^
                                Il??;+!-?]??}>                    ^'..';.."`..''''`.''.''
                                ..  .......''`                    <~_~_+->+]~~_-]!>>+][(].
                                                                  >>_<_~]>I?_<__?<<~~]>>;
                '`.^``.''^^'. ^``''.......''''''..`'.'.'. . .'..^`:I!^l:!;"ll:!!::i>!~'  .      .   .
                ;i,+_-l~]]_i-"~<~-_i;i!i~]<+>_~-l,_!_+~I?+_,;~~;[?^>!<!?]^<~ii^!+!li<i_:~~->_++-!<l:<<:~-+_i
                :<<+~~: !~~I<-_-il~+----1!;<!i>i+!<;+;<_->+_~!~:>~_+~;-+i:+>+-_l_>i~:i<~:??~_]lii,~>>}~+:.'.
                `,``^`^ .."```'`''''''''`..^`'``"'^."..""."""'^.`^^"^.^^^."'^"".'"^^.``:':,;,;"'" :,,:,:
                ;[il<:-?Ii+>i,i!il,<>i<-~<_]?<!:-_-I!_-;>_"_+<__~+~:~<:<i!l_~i!_<"~!>~~;^-~lI!i<i<>i>Ii">~~<
                l~:!+~iI+-+>?i~^.. ...'''.``''..''`..`"''^.`'^`^"^`.`''````^^^""^."^`""`'^"^^"^^^",""`,^,,,^
                ','^::,`:":",,"
                ;-iii`!>;l~ll`<~>,?>[,_:<<+~+~+""+-~'_+i<<<>"!i,-~;!>!~,~>i^~:!]>^~_><~>`>>>><l.I>il?!i:I:,l
                ;~!~~<:<<++-l.^",'^.:'"`,^,,,""' ^"' ;I:,,,"'"^'":^^^":',,,';`^:;':;l;Ii'I;:;I,',I;;I,lI,"";
                ,l::;I':l:;I^
          `I:::^  .;^^:"';:^""
          ^ilII,  ^><!<~:!<<~I

                                                      ":;,^^:I,'
                                                     `-~~_l!__~+
                                                     `>I<!^"!il>                        .
                                                     `iliI'"!>li
                                                     `]>~~l!<<~_
                                                     .,;I;",Il;^

                <]<!i;?<,I!ii<,!;_<:liIi<:!l!<<<;<iii<!!^I-<<i!<+>,ilii!,_<i<:~Il!i;>+lliil+I,l>l!+!!:<~<:!"
                i_!>+<`~-?~~l!+!;><~<<>+:>_>Ii>~i<;~l_l"``:":""",:`:,,:"`I:l;^I^,";,";,I;:"l:':I:;I;>,lll";^
                "l';I: `II;;^.!^'l:!;!;l ^;:';;:I:.l`i
                ,!~Il!>~I`l><l;!l,>~.:llil,+!^:IlI!^;ll`l+~;''
                `::^:,^""`;::,^,"'I:'I::;:';;`"I;;:`,ll "ll^
                __<I<!ii~;~<;I!l~~;!>:<<"<_~lI_il!l>;;!i<+<;~i<<i,<<><>>!:>_<" _+i~i,-<:;!!!i:!:I>lii'
                ``"'^`'::.`^`'^'^"`^^'^"'",:^'":,!I"`^,^"::`:"",,`::":,:,`l!,^ :,,l:`;I"";:;;`:,:I":I.
                <+<~+><,i]_~'<>_->;~_,!!<i>,_~>'++<".!_~;
                ^``''."`':''`^'^^``'`'^^'`^.`^".,;,..''^' ..           .  .
                i<+~}l~_<,<<~~i"<,~-I!]?_;?[_~_+<l~~-__li~~]+;_+__-<~!_]: -;-+~-?:l__?<<>-_[;<~<]_:++___+<'
                ,"'`^'`'`'^'''';!: '````!!,   .   ..... ..  . ....... .    .'...` .'''.'.''".'''``.`''```'
                _-<:<<~~l:+~-i"__+.~_~!:-+i..
          '.'.`   '`    .      .`.      '`
          l<~!_"  >~-]-;??-+.
                     `    ''^^'''^^'
                          "_-1~:<<i-l
                          :[+~-;~1[]i
                           "",`'`:,^
                ;l:^^'l"`"lII ^^'.` `^^^^^^.:^''`````.`"````'`.'''..'.'.`."'...'''...'.... ..'
                !<!>!"~>l;?{~`>~~,<I<i~><<i^~~Il~i>~!"__>~i>~~:ii~:>_?]:l;-+i;++<-"i___->~;l>]<
                ;l;:"'I,'"](!'"^^`"'"^"^""^ :"'`^^"^^'^,`^^`.`^^.^^^`^^'"^ '``^` `,"''^^.`"^  .
                i<>_!^~~;;+<<^><<:<;~i~~~~!`<~ll<l~~i:i-~<i<:i~~!_+}<:i:<_;<_!+<:+]-?-~+:<~[;
                          ..

















```

*Figure from page 8 (2346x3317 px)*


---



3-2-6. EXTEND Command



SET ADD CAL SEARCH



4203-E P-165



SECTION 1 DATA SETTING


#### ITEM t ITEM! [EXTEND]


## "=~"~F2)


# @J@@:) @:_)@)

Press (F8) (EXTEND)



Data setting involves many commands, which cannot be displayed at the same time (there are eight



function keys available). The EXTEND command is intended to switch command displays.



Function key [F8] provides a display of "EX" on the 21st line on the screen, resulting in a switched



command only.


```text


                                                                                                ^^""': "".^"'
                                                                                   '''.'..'   .`~[--i}^+i;_{i
                                                                                  `]]+>i+_[!l":?+<~I+[<!i-]-i
            ^^^^^`''```'```````^^^^^^`''''''`````'''''''''''''''.'.'''''''.''..'...'..'.''.''..''.'''`'..'``'
            ",""":""^^"^^^^^^^^""""""",,,""":;;;:,,:;;;;;;;;;;;:,:,;;;;;;;:;;:;;:::::::;I;III;:,,:,;IIIIII;:^
           .<;i!i  `-<i<_~_!:<llIl!!Il
           .:":,:  ':,^^;:;,^:::,:II::
                          '                                                                   '
                         .I                                                                   I.
                         .;                                                                   l.
                         .;  ':~]:                                                            >.
                         .;  <_ll,"":;""^^",l;,,,,,"I"^"^"":<:::::":l":,:::!l:::::";,","^^^'  l.
                         .I  I ''   ^,  ''  :^ ..   I.`''`''i      ,! `'.' I: '.   l`..... .  I
                          ;"`;"|+`  `, I{]^ "` l[_. :^{?][]I:      ";">{{>^;,:>{[l.:'_?-_{1_^"I
                           ^>!^`^"":,"":,::;::,:^""""":,",:,;^"^^,,,:","""^"""^",;":^,"^^,:I;,
                            I."!!~i;i^I!+~<li^>l_~!!::i~_+l<^>l>~i!I^<>-+!i,:><<~!<^!i__~il.
                           '! iIi_> il_'-~_ ~I+^__i^>!^<~{ +l?._[~.~:!;?);;~>^-i~ -l_'~]? ?
                           :" .I::,:: `;:IlI,.;l;lII'`!I;IlI.:l::Il,.llIlll'^!I::;l.;I?_ll:
                           l!<!^l:il!!Ii^                                            ^l'
                           ,l<il<i><>~><:                                    .<<~~!]_i~~><<~~I
                                                                                ' ... '.    ..
                 :!i>",i>!;l^;;:lIlI';ll;,'::I:;;::l`.ll;I"':I;:;",l`"l::l:::"'l'!:`':"",'::"".iI,:".::'^:";,
                 l<_-<l-<<!]l;<i~+_-I>!>-~:>_+_-]++_I"_>~~;;~+~i~!!-;l+++~_~+lI]"~<i;?~!-,<_>+"?~>ii`_<:l+->!
                 :<>l>l;'!ii!:<l<<+<_<  ;I~,!l!i>i_;^<!Il!~!>">"!~~l><<:>:;~~<<::!l!<!-<<:<~+~-~<.
                 ,,`"":"".:"^ !;l.^^^"::"''`';"^"^..I',;:" ^`.:"'',^"."^`.^^ :^`.^`^`^` ```';"`^`^.` ``"^^``^
                 I!>><>>!:~~+^<I-,>!!>!>_;;l:-_+<-;,?';<<,`~!"<~I;<i+^ii<'><^~~<^-i<-~l'i__~?_~-:>'_^_+_-<_-i
                 I~<>~!+i+"<!-"
                             .






















































```

*Figure from page 9 (2346x3317 px)*


---



3-3. Input/Output Commands for Peripherals



4203-E P-166



SECTION 1 DATA SETTING



This group consists of two commands: READ and PUNCH.



3-3-1. READ Command



This is a command to read a variety of data required for data setting from paper tape and set it in place.



The format is shown below:


# I I% I


# I~ Ip-

- ~- y - •• , )~-\~



-----1



····-·-····I



I• ►1



)lol• ►11• )ool


#### Feed holes p No. Q No. Data


# I• ,. I


#### Feed holes

The P and Q numbers must be specified, and are related to data setting as follows: P and Q specify the



category and subcategory. Axis data is specified by X, Y, and Z, and the data not related to an axis is



specified by R.



P and Q numbers are modal. It is not necessary to reprogram ff the number is the same as the one



programmed previously.



Both ISO and EIA codes may be used as conventional programs as the coding system.



The relationship of data setting, P numbers and Q numbers, is as indicated below.



Category Subcategory PNo. QNo. Remark



Work coordinate



100



1 to No. of work coordi-



system origin nate systems



Tool data Tool length offset 200 1 to No. of offsets



Cutter radius compensa-



210 1 to No. of offsets



tion



Parameter Common variable 300 1 to 200



1 to 40 real



System parameter 400 1 to 56 41 to56: integer



{Supplement)



User parameter 410 1 to32



Pitch error compensation 600



1 to No. of compensation



{Supplement)



points.



NC optional parameter



700 1 to 64



1 to32 user



(long word) 33to64: system



NC optional parameter



710 1 to 120



1 to 32 user



(word) 33 to 120: system



NC optional parameter 1 to 16 user



720 1 to64



(bit) 17 to 64: system


```text


                                                                                               """,`: `^.^,^
                                                                                  ''..`'.' . .`_]-->-^ii;+}<
                                                                                 '][<i~~<]l:`;_+~-I~}<li~?-!
           ^^^^^^^^^^^^``````````^^^^`````````````````'''`````'''''''.....'''''''''''' .'.'..'`''''''...''`'
           ",",::::"""^^^^```^^`,,,"""^"``^^""`":,,",,^^`",,,:;;;;;;;,,,,,;;;;;;;;;;;;::,::;II;IIII:,:::,;;,
           +"<:   .>!>;<>><I~iIi"i!ll!!lilIii^_l"!~!;l!il!I!i,
           i"!;    :!~IiI:l!<~ll';Il;Il;~l;!i`l!`":i:>+I<<l~<;
                ^iI;'":,,:'::,;;l,':,I:``::,":;"lI ;>,I;^^:"^lII!I!;'
                .:;I^>:;i!^lI:!l!;"l,<i:I>!Ill~I><^;>I!i,!~iII;>!!!l^
          .;^:`^   ;I"::'""^^"`^`"'
          '>:i":   l~l>i"l!!l!l+l<'
                ^~I;.:',`,"::,:":^;^:II;""`:;;l;'I:;lI,^;;:::::I:`,I:,`,:l,"`;"""'",""`",^"'"^,`""^"^^.,"^"
                .;:!^I"l^II;l:i:l^!",i<I,!,<<>~+"<,i-+i:<+_>i~!!~"!_~~:~>+i+!!!i!l~?++,l]_+:~!~;+~IillI+_~-"
                ^il::l;;!>"l'>l;Il^;ll:!^
                .^;;`;":l!^l^l:;I;^,lI;l^
                'I^",:;:,^,";,^:"^":"`^:";l,,::;:,,,,,:::,",::,""","::^^:"^"^^^^`^^^^""^``"^^^^^`^^^`^^^`'
                :<..........''.<l'.l~+!<~"?``''``''''''``''``^```'<1^~<<+>;l>``_}^^`^"<~+>?l;[^^<~,,",::,+^
                ,l ''''''''..`.!:_!">1!l[l~-l. ']l. ^[i. i: . ' ,";1'l_-I!+:I .!{...'.Ii}!i~,-,^l!...    _,
                ,! '....''''.' i;'`>~;i_:`? ',' `",'.^";^'.,I'. '` --!l!_l:I! ' [-.''.<><!il^_!~lI'''...'~^
                ^_-ilIIIi>ii!i]?!;:lI,ll^,-+<l<<i>!i<i!iii!I;l!i!::!~i,"~!:ii::;>~::::+>^I<:l_",<<I:::;;,<'
                ">!^III;;I!I",<<`         _-i;~-__;!+--+l::,""I_[^                   .  .  .. '.I]}:,ll!?-`
                    ,i+!"<+-^             :;l_'  >;~>.   :<-<                                   ."~~_;l~+<
                ">iI::"i!:;::I!l>lII^!;!<:!":>!Il_!i^:!!I:lI"liillI;:">!l^I;>l::^l^Ili;;I'!,,I:,I,l~~!i~l>:^
                ^!_~I:>>li!>:><i>~~i;i>iI!_!!<+~<i~>:i~>i_<>;~<~_i<l!l-~_!i<+~<[l~;i~~i<~:l:~~>lili+<>l~;!~l
                :~+~-?ii,_l~:<i<!~_+-i>I l~>>'_+~:!;!-<>i<<i:~!"< l`l->;ll`~I<:i+:!_+~`!>;;-~~~<:~,i~`<__,Il
                ,+~>i+~iI_>,~
                ":'^``^".^^'^^'`..`'.'..''. `.....'......... .. .       . '.'     ..     .           .
                !:;_ii:~"<!>+_<<;I_<"<><-]; ~:>!l+~"~-~-++-_>I+"i]-><[~?>"+;_-;I>~~--<"-,+?ll[-<_,~+:]_!I<-i
                :ii_~+>>>++!li~i<>>_+^                      .    .. '` .        .. ... .  ...'. . ..  ....'.
                ""'I","^'`^',""^'`^^".
                i?~_">?~:_i~I-_<:~>-_iI<-~;-<"+__<![;i~>>~!-_><-;_>~_~_<-:_il-_:ii__~<!-~?~~l
                `,^..`^^^^`^^`''"`^^`'.`,".'`:^^'`^^'`''`^`"``'^^"'",'^.^'^^'^^'`'"^^:',^^^`'
                "i~!,?_-+i<->+;!>;]?_:--?!_~,<,i+~++~~:_<~I+Ili><+~<i'-:_<;~~~<?_~!<_+<_"
          .^^^^`. ..   ''''''^^`''...'.   .'..``^''```'..  '`'`''```^``'... '`^^^^``^`'''''''.       ......
          ~i,,I]?1?-_+~"""I>:::::>1_}+]}-_++>:::::;<::~+<?>"::<I::::::",~<+[~I;;;;;;:";l",;;;![-_++_<""""",_'
          <l:",ii_+[-__:;:l>`````,>i<>+__[+~<^````^~`^I;;>>,`'i,^``^",,,+~l~>^''''^^^";!""'''^i~>!+~>""^^"^[`
          !<[_-_"<>~<_i][~^I... .     .'     .    '~ . "!i:...;l:~i~]>`+l!+!-!i_+<]-^';!''....      .''''''+'
          !<+~]_~lI_?[_`.."I          ''   .......`~.. ';!: ..ii~[],+_--+<+,   ''.'.  :l                   i'
          ~?{_->--_!:;"^^^I<<>>i<~i~-II+~ii^``^"",:~""^!>iI`",-<~]~_]~;<~l-~><>:,,"^^^l>^^^""",,,,,^^^^^`^`_.
          _:;I;^ii>:      ,+<+_!<+<[_Ii~_?_""""^^'"i`^`i+->","_!:<ll~!^<!>~~?_-"'''```li^"^^^^`''''''''`^^^}.
          -^              "_<!-}+"+_-~+:i>+]?[+][:'!.'.::;:'`'+I";"II"':I"!l,;:''''''';I`^````''''''''''^^^[.
          -^         .....:~<~~'.  '...  . '`'.`' .I   I;I;   !,^i;l<I.<ll+<+<~'      ^,                   ?'
          _-~<!<i!<>I,::::i--+>i!!lI,l>!><~I""""``"i^^^IiiI",">;,I,:l!;'^"^^^`'^^^^^^^Ii,::,:,^^^^^^^^^^^^"{.
          _i;~l~Ii<~"     ^<~~<~<~+!I_[+{?}>"""^``"i`^`<]}<"""ilI]i+}[>^"""""^````````;l``'^'`^'''. .'````'[.
          -^              ";                ```'''"~'''   .`^`i'.     .`^^^^^`''''''``;il~~:[~'^^`~_-:  '`'?.
          +^              ^I?~~_><;I~>_<>_-<.     `<   l_-l   l;,<;i];                ,i~iii!{i   :_[!l!'  <.
          <`              ^:`,^^^`'^"^"``","      `<   '""'   <'."``:'                ;l"'':.l]<,I!+-?1]>; +
          ~`              :<,,,:,:::::,:"^''^^^^^"I_:::;,,"^^^_;;;:;;;^^^^^^^^^",,,,,^!l'``'``i-+-]+~i~><i^[
          -`              :_+[}<l][_}~?{1>^^```'''"i'`'++?>`^`~!I?i~{I'.......  .   ..II``````  .. ..... .']
          -`              ;~l:^"^^^^^`^":,:;::;:"",>^^^"":,","_I:~;i+!"++i~+~<~>><?~il!i,:,,,","`^^^^"^^","}
          -`              :<i_~<"~l>!"~ii+~~i~->~i';   +??:   :ll-<_~, ;^,;;:I!::lil:^"^     .~-<+~-~!_><! ?
          -`              :<":;,:;:::;:"^,""",""""I+:::"`'`""">__<+-!^^'``'''''`^``^^^ll^^`^^","::"",,;::;,}
          -`              ">[]ll?--~_}!?[~[+-_]< .^!...l<>:...I,^I^Ii,..........'''''.:!!>~:1+ `''i~_i  ..']
          -`              "l_~>?l_~~?>..        ..">...:i~: . l,"<:i~"..              :i[+i~!{~'..___-<<`  -
          ~'              "~-_!<>-_++_!<+<~>>~<l"^I_,::,"^""""-^^.`"^,::,"^^^^^^^^",::<_>>li~+:^""i~<>Il;::-
          >.              "I__l!1<;;;l,iiIi;!<>"  'l   ;l_;   >l:+;,~-,               :!l~+;_~^;..~<-l..   ~
          +'              ,<+__>_:.`''^..'.'   .^`:i^""^^""^``-^`""':;:",^````````^^"^i+{<i+'![],^_~<??_:^^-
          ?.              ;+__:!]]-+-}i]?~{_?1}i.."l.'';!!,'''<,":^II"`^^`''''''''``^`I!:~i^?< ''`!+~;  `^"[
          ]`..............!<_??^,``'`^`"^`"'^^^.  ^l   :~_:   !:,<;<~"                ":!>+!>}i' .-_[-il.  [
          ;,,,,;;;;;;;;;;;l!i!i:",:IIIIIIIIII;::::IlIllI;;Ill;i,,",":;IIIIII;:::::;IIIii>l<+i_<;;;~+~_+>lIl~






















```

*Figure from page 10 (2346x3317 px)*


---



Operating procedure is given below:



G) Press PARAMETER, TOOL DATA or ZERO SET.



-----------------.--



----------------~--



@ Press [F1] (READ). @ Press [F8] (EXTEND).



Fig. 1-2 Reading the Data from Tape



G) Press the PARAMETER, TOOL DATA or ZERO SET key.



Press function key [F8] (EXTEND).



This displays the READ (F1) command.



4203-E P-167


#### SECTION 1 DATA SETTING

Set a paper tape for data setting on the tape reader so that the leading feed holes come to the



reader.



@ Press function key (F1] (READ).



This displays "R" on the 21st line on the display screen.



@ Press the WRITE key.



This allows the paper tape to advance, so that the data on the tape is sequentially read and set.



Note that the tape reader stops when an error occurs during the setting and the display screen shows the



message below:



read continuing? (Y/N)!



Press Y or N key. Keying in "Y" permits the tape reader to continue reading. The entry of "N" aborts the



read command.


```text


                                                                                               .""",`" "`'""`
                                                                                  .'`.'`..' . .,-??-i-`_!l-+"
                                                                                  :[{<i+<~[II.<~_~_;-]>!>]_-;
           .^^^^^````````````^^^^^^^^^```````^```````'''''''''..''.''.'...''''''''''.'. ''.'.''`''''''...''`'
           ':::::"^```'`^^^^"""""""""""^^^^""",,,;;;;:"":;;;;;:,::,::,:,,,;;;;;;;;;;:::::::::I;III;:,::::;II^
                 ;~>i!+<l!,l;l!i>I!;I;:>li:;iilll
                 ^IlI:!;:>:;"::l:,:,,:;l:;^^I;:::
                             `^ `,.'. ""^^^"^,^,"; ':""" '""""....:^""`."""`
                  ..........^~-"~--]{_?{[]]}1}>?[[<I][]]ii[[_]+_+>)--[_!1]~i^`
               I"",,,,"^",,,:,","^""",""^,"^^^"":`,:;:"",""^";I;I:,,"",,""",:!!^^^^^",,"^^^^^^^,,,"^^"";`
               i  .'...............'`'''''''`'''''''''`.'`'``.....''''..'.....:l'.' ... .'''....'''''  ""
               !  l`^;:::;::;;;;;;^`^`'''''`^^`''''```^`^^`^^``'`''``````:,;I,,l~l"!I,;>I,:;",,;II:^;" ^^
               !  I .I,"""^",:;::;'               ..                    .l:[(+!]][-t1I]x?;{(<![1~;, ^: :,
               >  I '!III;II;::::::I;::;:I!lII;;IIlllI::;;;;:Ill!i!i'    !:,,:,,""i>;,"^",;Ill;,,!: ,: :,
              .i  l ^;  .i``''''''''''.'.''''''......''''.'''.'!.  !^   .<:''^'`^''"!,^^^^^`^^""`<! ;I ;,
              .l  : `:   !                                     l   l`   .<_{{{\1]}_}{|)?[(<{+]1<<]I :; l:
              .l  : ^;   >                                     !   !`   '>i+_i?>+?<?]]}[-}]]-[_!i?l :: l:
              .l  l ^:   ~                                     !   l'   .<I;I!i<lI_;<_i};:Ii:;i?_]l ,, ;,
              .l  l ^:   >                                     l   ;.   .<~[{+[{-~?_-{+--[1[-)-|1[; ," ,^
              .l  l ^:  .l                                    .;   ;.   .~~_[<;-il-~<}il?[(?<{-}~], :" ;^
              .!  l ^:   i                                    .;   l.   '-~_<_++~~+~+[~--<+[<+]l<], :" I"
              .l  l ^:   i                                     ;   l.   '-??-__]~-[<+]<-?~?}<[}~?], :" :^
              .<  l ";  .!                                    .l   l.   '+!il!-+>>>llili>"l_^l_<<-, :" ;^
              '~  l "I  .!                                    .i   !'   '>i,l<^:.";;;lI;ll;;:.:ll-" ," ;^
              '<  l ^,   !                                    .!   i'   `--i__l~.l~i<?~<?~~il ~|][^ ;" l^
              .i .! ^,  .l                                    '>   !.   `-tj[}r] I_ii_>~?>>(; _i_-^ ;" i^
              .> .> ^,  .l                                    .i   ;    '+\(]}f- l<i!_<>->~]I ~<+_^ :^ i^
              .< .> ";^",l",",,,,"",,""""""""^^^"""""",,,,,,,,:I""`I.   '-}]l!]< I<!i_<i_><_I.l+~?^ :^ i^
              .< .> '!i!!llllllI!!iii!!ii>i>!ll!l!l!!i!!!l!l!l!Ii>il    '_1[+_{_ l~ii:i~_<!!l -~-?" ,^ i^
              '~ .l ", ,??i>~_:!l?>!!++lI<-;Ii}!!!}>!l_~!!_{i!<<<' I.   `>;;,:;"'^"^^,^^,^^"`'":>[" l^ !^
              '! .I ';";<>!I<-IIl!lIlll;;l!;;lilIlil;li!II>>!;-i!^`;    `<"""::,,""""""""""""""",]> !" l`
              .;  ;",:I:^^""<:"^^^^^^^":,^^""^^"^"^^^^^"""^^,i!``","^^^^^"",,""^"""""""""::;:,,""";!<' i`
              'l ..''......!"...''....''''''......''''....'.:!.......''''.............. .'.'''......:; <^
               ,^^^^^^^^^^i;`^^","^^^",",,,,^^"^^^,,,,^^^^`;>^^^^^^^^",""^^^^^^^^^^,,:,:"`,"^^^:;,:",li!
                         ,"                               'l                          "1i`?+-?-;][]-_(l;;
                        ,!  '.    ''  .'. ..             .!.  .     .      .          ';,,"^"""^^^^^`,:":
                       ">]~._~-[[I]i]l]{[_{]>'.         .i_[^!__??i<?1~<1--+[_[?i.
                       ^^""^^`"""""`,""";:::,"`          ,,I"```^"""'^,,;:"""^"":`
                                               >l: ;,l.<I::;:,^!I";lll^I"":`l:,"
                                               :l<.",; lii>!I~:!<I:i+_l!!!!`l+>!
                  .,` ."'''.'^.."^^^^^"^^^`^ ^`... '..^     . '   .
                  `i; "i!+~ii-+;>~++_]{+;~<~.;!<i+.>~--_:_,+}+--l>1~ll]_~.
                  '+l `l;lI,:,:,I::`l;""<l>'>;l;il>!;                  .'
                  .i: ^llii;"I;:lll^!ii:i;_,<!!,i;>il.
                      '!li,i-~+_>>;->:<[i~-;I~Il">li>i+i<:
                   ^'  ''"'`^,^^:"''`^'`^`,.^' ^`"``^`:^^'
                  ^]> ^-_llI<_-_i:[?-:~<^_-]!l?-?>_:>II~<:_]?!l__~]<"~I~++<>?<;_+_~><I_~~l>i+_!I<i<-:+;-<!
                      ^~-_[]l'^'  '^' .. .''. '...,'`..'`.`,^'.^^`^'.^'''^'.^^."""'`;.^^^''`^"``"``,'"`^^^
                  .;^ 'l::,,"'.'^'..`'.':`` ","`"^
                  ^_l "!li~l:iI><ii,~-<I-"!:___<?~;
                      `>!!"l>!!l:l`l~^:I^<l,:;:;,!I,,l^<l":il;!I`:::II:'
                       ":l^;!>!l!l.^; ::`li;l;Il:!!;;!">i;;>~>>+:liI<>I^
                  ^]I ,<;!i::iI^<<+l><"!l,
                  .;^ ^I:II,,;;`:;:^""';ll.                 .
                      .<I+,>_>++:_+!;?{<>^+]-~i~,-?<-~~-^l-:-<]l]]il]?_:+!!-~:_-~!!il?~~~_<]-[i;__-l<+>!<_>
                 "`^''".`^"`'^``''``"""^^.'"```'''''`'``''^'.'^.^`^''^^''.'^^.'"^'`^'^^,`^''^^".`^^."``.^"^
                ._~-~;+~<i~>;__+li--??"<-+-~I-+-<;]l!+i<:i<i~!<l]+><_!<?:~-]_-i>~_~_+!<?[~-_:?~~__l!_>~-<i]?^
                .li<~<~_~,<-<<+.                                    `        ''.        '..' .. .. . ....  .
                 '`^^",I^."^`^^     .  ..
                      'i~_;I<i_?~i>-~"<>-]~.
                 "`'..'"`^`"^`'..^`"'...''"`'   ... '. .       .                     '.        .. .
                '>!~+<^;:~:_:~-+ <?+?~_i~::<^<-<>~]i_->![_-;<-_]}I~~;~<<~~~<,___?>},.+_+;_<]~:_l!{"!1~~-~i??`
                'i<->;<ii<!>!<,.   .. '.     .          ..   ..    . ..  .'. .... ".   . . .`..  . .'...'..'
                 ^,:^`""^"^,^"'


















```

*Figure from page 11 (2346x3317 px)*


---



4203-E P-168



SECTION 1 DATA SETTING



3-3-2. PUNCH Command



This is a command to punch various data required for data setting on the paper tape. Paper tape format is



the same as with the READ operation. Thls command allows setting data to be stored on a paper tape.



Tape format is the same as indicated in Section 4, 3-3-1. "READ Command".



Punching out data under special conditions are shown below:



R Normal data



R/0 Empty



R/1 + overflow



R/2 -overflow



R/3 + underflow



R/4 -underflow



When the data of the type indicated above is entered, the same condition is set. Operating procedure is



shown as follows:



G) Press PARAMETER, TOOL DATA or ZERO SET.



---~-------------.,



'-----------------'--



@ Press [F2] (PUNCH).



Ke inaPNo.



Press [F8]



EXTEND.



@(J) Press WRITE.



Fig. 1-3 PUNCH Command



Enter the



device name.


```text


                                                                                              ',"""`, :'`",'
                                                                                 .'..''..' . 'I[-_~<+'_;i-}:
                                                                                 l}-~i~~<[;l.<<_i_:]]!Ii+_~,
          '^^^^`'''````````^^^^^^^^```'''''```````````''''''''''''''''....''''''''''''.''.'...''''''`'.'''`.
          '"""",,"^^^^^^^"""""""^"",::,,"":;;;;;;;;;;;,,:;;;;;;;;;;;;;,:,,:;;;;;;;;;;;;;;;:::;:;;III;IIII;;'
          ;>!li^  ;-!-~>i:!i!!ll<!!"
          ^:,,:`  '`,,,"^'^,:^""!::'
                :>i!";;:IlI!;>!!l>:!Il!~:l>i!l!,i~-lIi>i!!i>~l"~~<,i>_!!;:!,-i;I>>>!,<>>^.<!i!!:ii!:i!!Ii!l,
                i<<!i>><I~iI>[~l+~l?{~-_;!-<<+?!i!;+-~~ii>~!><l+<++<+_I+-+<lii<__~_!l_<_i,l<_><"<~<ll<I>_i>"
                ;;;`iI^l';l'll,'I;^^!I;l`"<lIl>;;^ ^:;:`ll;;I<ll"i<;li`I>>;ii^!ii"l"i<^i>l>~:l!"il<~ii`>_~<
                ;<ii"ll;I!;I,l!l`IiIl";!"lIi:I!l::;;<II!:"`; l"I^' !>lli:";:;:,:,:I'
                `l<I^";",!",:",;^Il,l"I!':II;!!l,^^^lIl;;,`I.I^I`' ,lIIi;:l!l!l<!ll'
                <;;l<<!i:;lI:~~<";li<;^iilI>l^l!I~>IIl'i!,;>lli;;iilII
                `^:,::,l;,;^`:;;':"";'^i;;:I:";;,;;::;^lI,,;:;l,"lI;I;.
                     .+.   +illl-:<_+<
                     `_i! '->>>+I.^"""
                     '+<i .i;i<+!^'.
                     '+!;  :^ii<~_<_'
                     '~<< .`"ii~<>i<
                     `+>~  ",!i<><_<!'
                     `->>  ",!!+~<_!~`
                     '>!I  '"!l~ii~l~'
                ^"^''... '''. '.'  . ....`'.'....'. ... ...  . .'    .      '.         '
                <]<~i:~~l<??<;_l+]l-[?il+?~_?-+;-_<<-l_I_i]<<?ll?-;_[~-i!_<i]+~<:_:+?I.~-_-~[-+-i-~~~-?>_I_:
                <_l<-I:?I<<>>++^    .                         .     .  . .         .    ... . .^.. ...... .
                ^``^"''"''``^`".
                           :<` ~~<<~;~____-{-i-<]^:+<<~^!~_+_"i:!{+-+Il]>i'
              .'''''''''''';!;,;I!i>II!><<~~!I!!lI:!ii>!i<>iiI>I!<i!ill~~>!l;.........................
             '!","""^''`^^"`.''''....''.```'``''..'````'.....'.'...''''.`^``:i"'````````^^^````''````^I.
             `I  `^^^"""^^^^^^`^'^^^^^^^``^`^""^^^"^"^`^^^^^""^^^^^``^"^''...^l".. .'  '''....'``'''  ,.
             `l 'I',l;;;;::;;;;Il'............................... ...''"::<>:I!]<l-!:+[!li!:Ii<;;^'l` ".
             `l ': ';:,"",,,:;::;`''''''''```''''''''```'''''..'``.    `;l]]l<?]~1|+;])>!]]!<}1!I` I` ".
             `! '; :l:;II:,,,:,,,:::::::::;;:::::,,:::;;:::;;;IlI:i    ,~^^^"^```^lI^``^,,^""^^,~^ !` ;.
             `I '; :^  ^l                                    `:   >    :i:::I::;,",i>:":"^:;:;""_, >^ ;.
             ^! '; :^  ^;                                    `:   i    ,<?j]|j{){](1\t}\\]|])|~}}" i` ;.
             "> '; ;"  ^;                                    `:   !    :i;ll;!li<>!<i~_><~il<!;l-^ l' i.
             "i `l ;^  ^;                                    `:   i    ,~l<>~--i~-i?--{<l>~<_[)}?` I' >.
             ^l ^l ;"  ^I                                    ^:   i    ^?<][i-{<+---[+~?-)-[/]|[?` I' l.
             ^l `I :^  ^;                                    ^;  .<    ^-~~_ii]lI_><]>~][{~~}?-+-' I' l
             "i ^l :^  "I                                    `:   i    ^-~++<~]-?++-}_--i??_[-I--. I' l
             "> ^! ;^  "l                                    ^:   l    ^?<~}-?]~[?<?{-[-l[-i}1-1}. !' ;
             "> ^I I"  "I                                    "I   I    ,<llI>i;,:l":l;<~":!":i;i-' >' I
             "> ^I ;"  ^;                                    "I   :    "<I.-;., llii>l!_]~I, <[~-' !. !
             "! `I :^  ^:                                    ":  .;    :~}{]_]!.i+i<_<+_<]}I --]-' l. <
             ^l `I :^  ^,                                    ^,  .I    :_t\-|u> !+i>+i<+>~(i:->{~. I. <
             ^l `I ;`  ^:         .      ..   ........   ....",   ;    ,[{{i?1i.!!!__ii_>_~",[~<~. I. <
             ,i `I ;!llII;;::;;;::;::;;:::;;::II;;III;:;;:;IlI;l!l;    "[]]I-[i.i~-]!~<+~<~:'-[1>  I. i
             ,! "! "l:li!lli!Iliilli~iIl>iIIi<l!i<lII<illiil!!ll:I"    ,--_i_-I ;_~,"lll!;I"._<+-, I. !
             "l "! :` i_>Il~iII>}!i!]>:l-~Il~[I~i1<<!?i,l_[!l>>l .:    ;>"^""^^"il`",^^^`^^^^>:">,:+  !
             ^l ^!.^:",::::,,;!iI;,::;,;;::;I;;,:;I:;::I~I;;:::,":"....";":::,,~l","",,,,,,"!>",!..};.l
             ^I  ^`''''''..^;;:'``^^`'`''''''''`'''``^l!"'.''.'''''````'''''.`l"'````^^^",^^~^^`'^^"';-
             ^!``'''''``^,!!:^'``````````````'''''`'`lI'..'`'`''.'`' ...''`'">"``^^``''''''l,'^'''..''?:'
              '''''''.`:I;'... .   .  .     .'''''."!".',~".!l:^:"::i,!:`'':!`'```^```````">ll^l;::,:I``:,
                    .",_i ll;Il^!!>,;~;i<!Il^     ,:    :{I^__?!~i~<+![]l`";              l'!! +~~[<;?+: ^;'
                   '!;"><"il<-]<-<]i<ii<+<i<i^  .;"                     ..               ,: ''`<{++_-:-1?{_l;
                                               ^I<_.;!iii,!l-"     ,_,!!  ~l!ll"<i<i><. .!  '''''''''''^`^`''
                                              :: ";.l[]}}]{-)~     l-lii",>!+~~;+~~<!<:^:`
                                             ^;`^'.';~!I;iIiIl^
                                                 `<l; ,:;'~;>>!>l:!lllllIll
                                                 '"l<.",:',;ll;I:"l!;lIillI






















```

*Figure from page 12 (2346x3317 px)*


---



G) Press the PARAMETER, TOOL DATA or ZERO SET key.



4203-E P-169



SECTION 1 DATA SETTING



Press function key [F8] (EXTEND}



This displays the PUNCH [F2] command.



@ Press function key [F2] (PUNCH).



This displays "PU" on the 21st Hne on the display screen.



Enter the device name following "PU",the following names are usable.



L..J



device name: File name



If a sector device is designated, a search will be conducted for the relevant sector device, and a



check will be conducted to determine if a file of the same name already exists. If a file of the same



name is found, a "File exists. over write? (Y/N)!" message will be displayed. Enter "Y" to execute



overwriting, or "N" to cancel the punch operation. A "Comment input" message will be displayed,



requesting any comments which may be required regarding the punch data. Enter a comment if



necessary. If no comment is required, nothing should be entered.



Parentheses marks"(" and")" cannot be used in the comment. If used, an error will occur.



"5320 Wring character"



@ Press the WRITE key.



The punch menu is displayed under the heading of *PARAMETER DATA TAPE PUNCH MENU*



and then the feed holes and the percent code{%) are punched on paper tape.



The prompt [parameter No.!] then appears.



PARAEER SET



197/07/15 14:10:00



"'PARAMETER DATA TAPE PUNCH MENU*



p NO. ITEM



100 ZERO OFFSET



200 TOOL LENGTH OFFSET



210 CUTTER RADIUS COW



230 TOOL MANAGE DATA



300 COIIION VARI ABLE



400 SYSTEM PARAMETER



410 USER PARAMETER



600 PITCH ERRJR C~P



=EX



=PU TT:



plese i~ut message I



parameter No. !



READ



PUNCH



VER I FY



P NO. ITEM



700 OPTIONAL PARAMETER (LONG WORD)



710 OPTIONAL PARAMETER (WORD)



720 OPTIONAL PARAMETER (BIT)



BACKUP



[EXTEND]


```text


                                                                                               `:",""" ;'`,:.
                                                                                  ''''`'.'. . .!}-?~_<^-;!]1"
                                                                                  i{+<>i~-]^I ~<+!~;]_il<+?+^
           '^^`'''`^```^^^^^^^^'`````^^^^```'```'`'''````''''''''''''''''''........'.'..''''..''''''``...'''.
           `::,"""""^""^,,",,""^`^^^^""""^^^,"^^^^"^^",,:":^`^`^^^`^^^^:;;;,,,,,,,,,,,;;;;;;::::::;;;IIIII::.
                   il .i,",^^;"^iI;;;llI;lIl ,;::: ",::: `.^l:;:`^l:"`"^.
                  .:, '!li>!;i>:!i!>>_<!:>i<'"li!>`Ii<i~:<"i[+<~;l{~:;--~.
                  '_i '!li<I;!lIilI`!i;,]>+']<ii<>_<!
                   :" 'I:lI;";:::;:":l>I!;>:!;I,I;;;;.
                       ii-:!]-+-_<:-_li>i-<~<:-i_,i>>-~_~+<
                   :, .,'``'^"^`:`'.^` .,'^.",`^"^^"...'''.
                  '_< "~l~_il+i<+>~,+~_;_!?;?<!_~ii_'
                      .lI;^;!;ll:;^IiII^;^;!:`I,I:;;;`;";I:`;;::;^`:",::`
                       ";l`Ii>>>>!``:i''i^:l!"l:<:I>!^i::l!^!i-l+>^~Il<!"
                  .~i ^~;>>^l!:^iIIII'I!:I"ll<;III;'>l;^iI,";!;::::'^;,:I:"I;^:IIIl:
                  .:, '>;!i`:l;"iI;;I^;!;l;:!!IllI-'I:l`>l!"i>i!>l_;:~!i~l;>!:i<~i>i.
                      ,_>,'`;~>!i<"<+i<l i~-:;~i<<
                      .`''`''^`'^".`"'^^ '."''"^^".           .            .   .
                      ^<lIi-~~>^I]>>>i^>"~<_-+<-<<;:iI+++i~^>]<l-:l>>>+!~-<I><`<~l,~_~!+<;i_!~~";?i>~~ l_>l!,
                      `>>~<<:~];>l:><i>i>_<i+ll-~~!!<!<!>!l_<,<!<i:li!>i;+~!>:!i>i>_:>><_~`:<!!_~;ii~+II_<!~^
                      ^ii>>Il!~Iii!Il;~_<il!!!<!;<lil!<i!+;<~!-!l!l!~!iiIi>>+I_l!?~~!iii+!;;l>l!-!!II!>I+<i+`
                      `!~I~li!!i!!~,<I;lil:~i<-I^!!~`ii<+;`;I!+<`^i~<+--]:l<ll_II__+~_><i !~!~<.,l.<;l<~ili+`
                      'il<l<l_l-;`<.>_.>;,<<i~>:~~:~~i!>'l_+i~<i<^ ~`:iiiil<<i:<i!>^`~~>i+-?"l~!:<;;-<~~>i+<
                      `<><i+~!l~l_lI^i!!!!<i-:I-~i<,li_:!-II~~!!<<l;>i+!~<iIi<!:~<>>>,~_-I"]~~?i,<:i++<~?+i>"
                      ^~~+_++~>_`I_!>!!><>~<_~!~!i>l!~-+I!!i_++ll]ii<}_>~I-~<>>>+:,;"`:;I" ",:!:`;^;;:":l,^^'
                      ';;"I;I!::  "'I'^I:;:llI^:,,!il:;!".;l:,:<^iIl;I,;!'l,!;:>;
                      ^:>i!iI!l!><!^Iiii!';`:!I;";.;ll::l;!"^llI,;`Il:^::;:I;:I :l,lll,^i,:!;l";iI^;;,;`
                       '^,::":^;:::'";;"; `';!;:'"'lil;I;:i::iil"I^;ll"!I;ll>;l.:,;!i!,">,I!:i^l<:,!!I>^
                       .<+~-iI]ii<:l~>!i!_<;
                   '.  .'^^"^'^^^l;"":""^^:.
                  "[l ,+i~_I!+!,]<_!<~^~<I
                   '. `l::,,^:;,""""^"""ll^^^'``''```'^"''`''`^'..^.':,",^^",",^"`^`""``"^"^."^``'``'`^^`'.
                      '>>~!+!i<+,>]i<,_:<-?<____I><+_li_<:<+~~_<_I_^!~+-_+-]]l_+~I!<~>~:<?~?l~~_?+~+l[[_-->!.
                      "+ii!~-<"~_l>-~~I<~_~"~<~l<_;i++i~<i:>i[!I?<"+<!:i>ii>_<"~;I~->+:<~<<.
                      ';`'.'^`''^^'^^`''^^``"'^``^'"^''^'.'`'^`'.^'^``^^^``'"^'^'"":""'`,,".
                      ^~i~:~i~~]!--+i_>++-!;->;!+~-<:]-_~->>.
                               `'^'... ..'. .''`''`''^^^`^`^^`''...''''''''```''..''''.
                             ^:,ll>!i<i!l;>i::::;;::::::::;;;IllI;;:::,"""":::;,:,""";::`
                            'l 'l!}})j-]-!1+^^`^'```"^^^"^^`"^",:,`",":i>!<li!;>!i><~~..l.
                            "!              Il!l<i!i^I;;':I!`;!!:^>!;:,?_~-i~~;-<_-?}i. I'
                            ^I              ;i~<[>i<^<ll':!i`l_+l^]~>,                  I'
                            `,   :"~-.  "~}:            l^],   ,--                      I'
                            ^,    '"' '""^",^"^.        `""' ^,^":` ^^`^``".. '` """'   I'
                            `,   ^]]  i||I:({)-.:l::^   ![l .1[![([`+11j1?|;l{/jl}]]l   I'
                            ^,   ;]_' I[{~?>({~_{<}v[   <}l `|_!(|[`_1{r|-\,>f?{:       I'
                            ^,   ;[}' l)}I[1{|)![~?_,   ^I` .:^`:;;.^::!;^:'^,.`        I'
                            `,   :)}' l1uf|<?)?+\|+                                     I'
                            ^,   ,[]' i{1_/~_)(r(?-^                                    I'
                            `,   I[?' ~{|-i(trxi1{~'                                    I'
                            `,   `!;  ^`^l`:!!!`;~+.                                    I'
                            ^,                                                          I'
                            `,                                                          I'
                            ^,   `,.                                                    I'
                            ^,  '-|^,I                                                  I'
                            `,  .!iii";i;'">lli!.^                                      I'
                            `,  :{_})>]{>1~<~l~>^^'..................... ...... .'....  I'
                            ^" .:I,"ll+,';,',l'.`^`:;^^^^^I,^^^"^l",""""i`'''':i,"""^'  ".
                            ';   l;l  l Il!: ^,iI:;^^     :'     ;      l:!I;i^"`i;;Il" ;
                             ":^`~~~^';"!_+l^";>!lI"^.....,`.....:`.....,!+ii~^`,_>i<+!:"
                              .`IIlIiI^!lIli;"l;I;l""!!ll!^,lllll^;i!lll`,;;;,;`;;lII,`.
                               'll]~.~lli]?`l!:___^>>"?[!,i<"+1lI;<"]{;ll>,-~^+i!;_{'-'
                               .IlIl;;^lIl!;:"II;l;,,IIl;I";;;lIl^;li<!l^I;I;:!"lII>;i.
                                                                             .      .



















```

*Figure from page 13 (2346x3317 px)*


---



4203-E P-170



SECTION 1 DATA SETTING



@ From the menu, select the item number of the parameter data to be punched. The data entry



format is as below:



P No. (A)


# I [ -I

P No. (B)



Entry of a P and Q number should be made without characters P and Q. Use a delimiter"," when a Q



number is entered following a P number.



When a range of P numbers or Q numbers is to be specified, the P number (B) or the Q number (B)



must be larger than the P number (A) or the Q number (A), respectively.



For the data entry, see examples below:



Example 1: Punching out all tool length offset data



parameter No. !200 [or 200-200]



Example 2: Punching out all the data from tool length offset to common variable



parameter No. !200-300



Example 3: Punching out No. 8 data of tool length offset data



parameter No. !200, 8 [or 200, 8-8]



Example 4: Punching out No. 8 data of parameter data from tool length offset data to common



variable data



parameter No. !200-300, 8



Example 5: Punching out tool length offset data within a required range, from No. 2 to No. 8,



for example



parameter No. !200, 2-8



Example 6: Punching out within a required range of parameter data from tool length offset data



to common variable data



parameter No. !200-300, 2-8



(j) Press the WRITE key.



The data within the selected range is punched out from the specified output device.



@ After the completion of punching out the desired data, the parameter No. ! is displayed again.



Repeat the steps f) and g) to punch out all the required data.



@ Finally, press only the WRITE key.



The percent(%} code and the trailing feed holes are punched out on the paper tape, thus ending the



data punch mode. The display mode is also restored from the punch menu to the originally selected



mode.


```text


                                                                                               ^^^"`: ,^.^"'
                                                                                  ''..'...   ."----<['_!l!+i
                                                                                 ^[[~ii+~[!;'l_+>+I_?il<_?]!
          .^^^^^^^^^^^```````^`^^^`''````````````''''''``''.''''''.'''''''''''''..''''.'`''...''''``^'.'.'''
          .:::::::,"::"^^^^^^":,"""",^^^,,:",:""",""^`^::;,^""""^"^^"^`^,:,,:::,",,,",::::;:^",,"::;::;;,,,^
                  l~  ;,":^:l:'":,". :;l,,"l:`I::'^"";I,".:,I,``,"",":;".::;^^^^:``^^^",^, .l"^.,",'`^^`.
                  ;i. ~<--~__];_-?-?l[+~>l;><,>~!";i!!~~l">;><I!~><>!~+>`~_-i!i:_l>>ii><~~''<i<,__-l>>><l
                      ;i;;~i^I,~,l<>!i`
                                   .  .'^^'`^.  `;' ''`^'.`. '^',^  'I`````'.'. '`  .,  '..  .' .`' "':`
                                  ,>~!]<"l]<,I  ", `:<+>[!`!}l:,':  ^l i~~~-l`!_;l` l^'`I>I<~:`--:! ^;^:
                                  "l,:>>,Ii!,;  ": ':!::i!^l~!I"':  ^I'il!;>!`!<!!` !'``;i;!_l,_~,! 'l";
                                   ..'..'. .'.  'I` .`'' .'..`"';^  'I'''.' .'..`^  ',  `.'''`^'.`` :^;"

                     ._>_~l;<!!iI_<!<!liii~~^<+i<+_i<;!>i->i+]~<<i>_++~>_<>i<l->+>i.i<+l>l--<i_~l"";+>~!;i<i
                      >!>~_<I!>:~__i<<i--<~-i~l><-l>~>___;^^""^",`^^:",","^^.^;",^".",;":";;,";;".'`;"I"";,,
                      ^:,^,I'^,":^!";;^:;:,I:i:,^`';;"I;I
                      <+!!l^I"!lIi`lI!^!;l<II;^;^I:,IIlill;I;!:I>:II>I+~Ii`~I:i,::li!!,l?I,l!<l:>,;;Ii!l`i_,
                      <>l+>><;?<-?I~>lIi->i?!>l<l<iI<-<>+l_i!<>l+I<_+>!_-l"~<!l,i~!~<i^l<;,I:l!"!,;i;!ii`i~;
                      :;Ii"li^iI~~":l~i`l!", ;iIli<"">l'I^+>l;!:>li<<l'>~,"~~<+~~<i~_.
                     .i::^!l'Ill,^;;;^.I;:^;;;:::;,"l;;;:
                     ."::'Ii^I>>l;I:ll'iil"!l>:>Iil,!>Ill.
                     .~IliIl!"`^ IiI;l!:l":;I^~;l:I:!l;>>`l~ilI:<i!`
                      ;:II,i;,'^ ^"l:;::i;^;,`!`,,I`lI!~;.I,Il"^!!l.
                                         l~!i>!+~>"-~".<<-;>!`>_~,>+-_
                                         ",^^"`:"^ ^^' ,^,';: ^,,',"^;
                     '~!>!!!+I!l !>;!ii!!,,;;">"i!;"ii!"i,l^";;,:I:;<',~<!l"!^:II:;;I""lIIi!l.
                     .::l;,Il,:, ^,;:I::iI^:"^l.,;:`l!l^:";^^;l,I!!->^;!i>l"i"l!I;l!!":>!i+i~.
                                         ;>ii>l+~<^_>`.++~:!~<"
                                         ","""`,:,.^,' :,:'^,,.
                     '_l>i!!<;!l i>!!i!Ii,,lII<; !"!ii,"I,lI::!Il~:,++!>"!!!,
                     .I;l;:lI,,, ^"l;I:,>I^l,`I: :^;I!:^,`lI":l;<l^,!l!l"!<>I
                                         I<li>l>+i"_<``+<+":>:!^l<_,^>l].
                                         ,;,::,;::',;^.;::"",,;',;;"^;,>'

                     '!",,"";`"^ ,:^"",^^'^^^::` :'"""'`:`^^`^^`"^'`^"``^'`'`'`''`''".',`'`.`''.` ..'''...
                     `+!+~i+_IlI Il><<<>-ii+i!+>'+;+-?ii~>__<_!+_?,l_]+;<<>;>~~;~++{_,<-_-<;]_-l-;i~<<<<~;
                                 :+_<~__"??_l
                                 ....... '^^`'''''.^' .^^`.``` .'
                                         <+~_<<___,-_,"?_]!_]];l+
                      ^  .  . '. ^' ..'.             .  .          .
                     ^?>-_+-[l~l +l<><+<_lI~~i+_I>]~}]:i[_--;[-[l<_+_<;~l_~<+_?~I?~+};l_i<I~[l"_!<;]~`~>
                           .     >~;i>~<<_-I  .. ...^  .  .  ...... .  ' .'`..'. `."^' .'.. '..'.' .'..'
                                 ^,'^":,":^'
                                         !-~-<i+__,]-":]-[;l<-I .
                                         '`.'. ''.  `  .''  ..
                     "-i+<>~_l-I >ill<!I>,;>!:<<l!"!`!l<;!<>;<<!-;I~;>~>~!<<<,I+~>I~li,!l!;!>l<-^;?>>!,i<<`
                     ."^,"":"`"` >Ili>>i+~i!>i~_~~;~<~~!"";:^;:;<""""II:;";:I`"!Il":::^,;;^;I;<I`:Il!:^I!!`
                                 !;"lIIl:l".;;"l;l:">ii
                                         :lI!ll!i;^~l.^+<~;><+^;li,
                                         ll;!;;!!I'l!^`ll!,Ili^:;l"
                 '<l ^>;Il:I>;">!<!!l:lI,
                 'I, ^l;li;,ll`lll;:l"iil
                     '+><`~++:!~+!<:<<,!<>~~-+Il+<~~;+:>i>>~~+Ill!!~!i,_>II~>><]~~;ll+li:~~i>il
                  ^'  '^"',:"^`"^`"'`"`"""^^""'',`l".,^"""^',,.^"`.^""'^"``l"""":,`"^;:,'::"",^
                 `{< ^-__l;~~"l!i<<>+ll`I;i!li~_l~"l!;>~!^-<!l<i"++_""]i^!>l>i!<<i:-<`";!^+><++~~+l_<_+"
                     :]<+~>-!~~I<[__!+I>_~>~l!<;<++++,><l<+<]<I<<~~__<l__]<^"``""^.^"'.'^'",:";:,"`;l:"'
                  ^. ';:;;;;'",`,;II"^";:I^>:,;";"":"';;`l,^;;`:Il;:lI`;!l;
                 ^}i ,i<i+~"I~>+_`;i-,_iII?i~l+I:<<,
                     ';::";;::::";:^,,,;"",":,,,,:!;^`:"^",`,^`'^`'`'^`"`^```^'``^`''`'`'``'' "'..'''"'.`^'
                     '<i+!~<l<+iI><Il>-?;~><!<~l<_+>-i--+>ii+~ii+ii_>>~<+~l>~i>>l<~i<??_!!]_~^+li!i~<?i+<_-`
                     ^+~~Iii!i~Ii<>-! <>_;~~-__~;>i>]l<I_~i:<~_<>-~><!i;_+l<!i>~ll~_<I~!<~~I<_++~-<;<<~_>~+"
                     "~<<-!'.. . ....   ....^.'^ .'.'.'''''.'''''''..'..'''^`'''''``'`'`''`'`^;`^^"`^^^^`"^.
                     .^,,:"



















```

*Figure from page 14 (2346x3317 px)*


---



4203-E P-17i



SECTION 1 DATA SETTING



3-3-3. Verify



The VERIFY operation occurs in the same manner as the READ operation. The data which is read is not



determined by the parameter settings. There may be cases when an error occurs even though the



numeral displayed at "Parameter Set" is the same as that at the verify data. However, this is due simply to



thefactthatthe number of digits following the displayed numeral are being held by the OSP, and there is no



actual error.



A "tolerance" designation can be made at the VERIFY operation as follows:



DV Device name; file name; numeric value



By entering the optional tolerance (numeric value) designation, an error will not occur even if a data



mismatch occurs, provided that part of the parameter data which is read is within the tolerance range. Only



positive integers can be designated as tolerance values. The tolerance system-of-units varies according



to the parameter types being compared. Regarding data items with decimal points (system parameters,



user parameters, zero offset, tool data, etc.), comparison will begin from the smallest displayed numeral



(following decimal point). Optional parameter words and long parameter words, etc., have no decimal



points, and are therefore compared as they are.



If the data error value exceeds the tolerance range, the following error message will be displayed:



5375 DATA VERIFY ERROR "MISMATCH LINES"



The following parameters (including the tolerance value) are compared during the VERIFY operation:



PNo.



100 Zero offset



200 Tool length offset



210 Cutter radius compensation



400 System parameter (excluding home position return order data)



410 User parameter



600 Thread pitch offset



700 NC optional parameter (long word)



710 NC optional parameter {word)



720 NC optional parameter (bit)



3-3-4. Omitting the File Name and Device Name



If the device name is not specified atthe READ and VERIFY operations, the setting will be determined by



optional parameter word No. 104 (initial value: 0, setting range: 0-11).



The devices which correspond to the setting values are shown below.



{This parameter setting becomes valid when power is switched ON.)



Setting Value 0 1 2 3 4 5 6 7 8 9 10 11



Device Name TR CN0 CN1 CN2 CN3 CN4 MDO MD1 FD0 FD1 FD2 FD3



The "CN0" device name shown above represents the same device as the 'TT' (teletyper) name.


```text


                                                                                               ',,,"`, :''^^
                                                                                  .'''''.'' . 'l[]-~<-'_Il!l'
                                                                                  ;}_~i<+~];l.><~i+:-_!l<___:
           .^``^^`''````^```^^^^^`''''``````'''''''''''``''''''''''''''''''''''..'''.''.''.'...''''''`''''''.
           .^^^^""""`'^`^"",:::::,"""",::::::,,,,,,""":;;:,:"""","""""",:;;;;;:,:;:",,:;;;;;;;::::::;;III;::'
           ,>lli,  ^~<l~,
           ',"",^   ,;^I, .
                 ;i~::+!~-~!">+<I+_I!"!i!Iil!;<iII>i><"!i<Iii`<!;<>;_~!+<"!iiI+<!! '>l>"_~~:!+l!I:l,i!i:!,;!:
                 :i+<l<<!>!,l<I+>i;>>l~><~>::i>?>!_;`i~i~<;I~I<:!>I;iii~;;+<<ll<>;;"I!lI~~<!il<i!lI<<~<!<:<~;
                 l~~+>><!~_:<_'l~I:~?+<l><<,;~+_>]-"`^ll<il,i_+,~+^!+-~+^!><~I^<l`+ili !!lli!"<!~i'<!>>}l">~;
                 ;<<i+!~;i<?~+_>!I_",!<i<li+_:I+~`lI~_l:+~l<,_;<<~I~I~~l:~l~<,]__: ii>++!~;"<<;l:><-,<>>__,i^
                 <<i!+ii+>+>_+li~<+~_;<i~-?-l+__<+>_>~_!>?___+<<l<!i~~i+!_<l+~~~~>~_<+~!_<i~_]_,_!<<~~<<<~l<"
                 i~-!-!!>>~,'"'`"`^""'^'^;l"^^"^""`:;`"^^";,,I,,`^,^",^,^:"^^,":!`::""I^^,"^":^`I^,^":::^,^:'
                 :lI:!'",":.
                 !:,i!>!!Il>"!?<>~><_i!,I~!;_>,i<<-"ii<>i:~-~--!I"liil>l!":<,!><l!!^
                 "^.:::,:";: ^;",i^::^"'^;^.;,.";,;.,"":: ,,"I;`^^!!l;l:I`:<^:llIll^
                      ._<;!<~ii>";>!i>'-_:;+!i+^;i<<<<!`l->!:
                 .    .^`'.`"^^,.',`^^.^"`',^^,'`,,^,^".":":'
                 +],l~i~i!+:;i<.~+->i+>'>>!l~;il"<IIl<li.:<I!+^;~>>~!<]ii, ~l.~!>l.i+i^i~";!!ll`<!<l'i^!`+~_,
                 l~>i!<_>I!>lli!,<!!i~-i>+i_<i+~;>_~i!i>l<<<_+:i~+i~><<_Ii"~i!>!I>!~<;l<iI>+i<i;~l>iIll,I_<~,
                 li<~>~<!!iii<i!;<!i~!~-!i!+~_~>l!I>~><>>~l>>~I!~~Ii_i!>l+;i++l!;<~!ilI>~I>+<!ii<II<~[~'I<!<^
                 ~<~_>!I;>~+]~i;!<l;~i:-+<]i<_i!l_";~_<ilIi;;~~i+! :l<lI+<i<<l~:<~~~>i,><li!~;;~!+~:+l!<!>l?:
                 <I:i<;~+!~i+>~"i+><il~iI~!ll!<i<!~~ l]+~<I_><,i_~i;~<ii^<+[^~~>~!>i;i<<+;I+i<+<l,><!_!<-~i<.
                 ;>>i:<+>~i<~~<I'_<iI;-]+-"!>>:>--i^i<:I;<i>i+~>+<>"~?i~><<I!~i<;+~!l_>>[<<~~?~+~><~ii!<~+!~,
                 <_+<l~~ilI-i~<i!;<!i<i,i+I~>>I<i+<:<<iiIl!i<<?Ii<lI>>li!_~;!ii>liIil~>_!<_l,<_+<+!>I,-<!+!_,
                 i<i<<<l?!l+ili+~:<~<<! `!?>ii~<I~i!+I<>_^:<!l-II<ii:il_:<~l_i>~-;`+>l>+.!?i'^i~i!'!;"]<!!<]"
                 !!<i-,^-<~;_>:_<+<-<>i:+<!_~<i~;<>l-<+^~~i
                 :^:^'^,,`'"^^`.^^'`'^``^^^,`,^``""``^"```^'''."'.^`^''''..''...'....  . '^.. .`...   .
                 <l--ll+-~,_;>I"++!>"~<i_~~~"<+:>~~l~<>+^i>l]<.+~li-?>_~~[l->+i,~-__-]]!>]_!]!![----_?~.
                      .I:;!^l,II"`ll!ll;^:;Il;:!`:I:I;::;,:,"`I::;"      '           ..         .. ..
                      .>>;i:>lllI^<<l<;:"iii<>!<^:_!<~<ill>I;l>~i<;
                 l<!,!!!:;;:`^:;:l:;I::^:;,:^l;"^!,"":;,,:^,``,;^:`,;:`;:::,;::,,;:;,^;I:^l>I!!;:`",,,;,"^
                 `,I^;!!!!l!iIi!l>l<ii!:Il!li<i~!>il;><ii>l<;:<~!~;!>!,>iI~>~i<;l~<i>~!~~^>+!~<,;,++><_>i;.
                 >~<I
                 ^^:,.
                 :>~"      .+_i!"i-<~;
                 i~_,      .~<>ll<!~?,"+!;l
                 ~<~,       i!_li>i]+"!<<+<`'''''"'`.
                 <:i:      '~l<_~.!+<i~^l!I~+_l+_?~~`
                 >--,      '-<>_ii:!<i<~i+-<"~~>~i++~_<<~>_:<<+_~~!;-+!<;!>-?l:-__+
                 >i<,      '!~_>;i<<<!<~<;'. ^``'``'`:.'`'`'^`^'``'.^`^'.`'^"'.""",
                 ~i<"      .~<+!!+>!_!+l+<^,'
                .~<~"      .!!>>_~l~_>!"!<_?,... .       .
                 I<+"      `_+::~+~il<,<<I<l>_-l:<<<<;_~~[:
                 l;>"      ^_~;;<+<ii_I><!~!><~I:<ii__.  .
                 !>_,      ^-_Il_+<ii-I<~i+>+++II-_<":
                 "!l.       Il^"iI;,:i"!!;!;!l!^"i!;
           ,":^:   ^;::l:"`:"`^::'^:^^".'''`"^'^^`.:"""^
           lIi;!'  ;<l>_>+>!<i:l_lI++<+Ii!!li<<<i+,+_>i~
                  '"^'  ' '.  '. .    ..  . ^' . .`  `".^^'.''``""""^`.....'... .'   .`.   .'.  ...   .  ..
                 .,i_+<l-<<>~I~~I+;_I>+l_++<[]~i-~<_!<{i__;+~<I<_<?_Il;<~<<_>~+!;_+l++{++_+-<__;---+i<~~+~~?.
                  '<~~ii-i!_<~~~++~^_<>~l-~^`<-!;<_~-;l->>!^_'<<_-!<,<<~-!^~,ii,        .'              .  '
                  ';"```"'^^`^`"^^".^^``.'^' `^'^^``^'""^^` ".^^`^^l'"^,;^.`.'`.
                  '~++^-<i<>+"<~i<i"<il+<~i!_Il!!~<^_+[<~l;_-!~i:<<^i~!>>">~+i~l
                  ^~_+~I~_~-~___;l+_]~_!-~<<<>+i;-]+!+]~?!>_~_-l><!_-+<_-_i_{~!`
                  .^''^`""^,'^^^'^,""'l^"""^^",^^"",'""^^',""^"`^^^,""^^:,.""^"
                  <;I[+[?++<[?~]i;<;;];"i:"i;:!I:-!:<!:+l";;"~<;l!;<+;:!"l_,;~;l?lI>ll[l:!;:_l;!lI__I!i;+~Iil
                  ?:"<>~<<-l+<>_;^~`^~"'>,`;^^~;^+;'!:'i:.II'il':l'l! ^i.:~'^_``i`'!`'_^.l"'~:'l:`~~`ll'il I_
                  _"!-]~_]i-{[--i^_^<-?`!i?]{<~~-[}!:!]?{-!<+-{[l<~_]}:!}1_}>i]([-l;![_[!l!_~_!i>]?]+Ii]___I_
                  lI;Iilll;I!l;l:^!"",;:iIlllI<Il;:,I:;;!ll!I;iI:l::;;:il!i!;i;Il:"I;:i<!ilIi!;i!lll;:II!>i!i
                  '+i>^i<__;"_!!ii^l<!<!;~li>l"~i!!i"<i!>i>i<>"~i"lil!l:~!IIi"iI;~!";!!":<>iilii!";!Ii!.   .
                  .^": ^",: `;,,,:`";":,":":;^^I;::;`;l;IIl;;I^:I^;l:;:"!I,:l^l;";I`.^^ "!ll!>!!I^,i;l!




















```

*Figure from page 15 (2346x3317 px)*


---



4203-E P-172


#### SECTION 1 DATA SETTING

- If the device name is not specified at the PUNCH operation, the setting will be determined by optional



parameter word No. 103 (initial value: 0, setting range: 0-11). The devices which correspond to the



setting values are shown below.



(This parameter settlng becomes valid when power is switched ON.)



Setting Value 0 1 2 3 4 5 6 7 8 9 10 11



Device Name CN0 CN1 CN2 CN3 CN4 pp MD0 MD1 FD0 FD1 FD2 FD3



The "CN0" device name shown above represents the same device as the "TT'' (teletyper) name.

- If the file name is not specified, a default file name will be designated according to operation function and



device in question.



The default file name is "A. TOP". This function features separate default values for the file and extend



names. If only the extension name is omitted, it will be designated as ".TOP".



3-4. Other Commands



The NC has other commands as explained below:



3-4-1. Back Up Command


# IACAUTION


# I :

Data such as tool length offset, cutter radius compensation, origin of work coordinate



systems and parameter except system parameter is backed up to the memory in a preset



interval. Therefore, turning off the power to the control right after renewing the data will



cause the data to stay as it was without being updated.



The execution of the back up command will update the data even when the power is turned off.



Operating procedure is shown below:



(1) Press the PARAMETER, ZERO SET or TOOL DATA key.



(2) Press function key [F8] {EXTEND).



The commands will be changed as indicated right



=BA



READ PUNCH VERYFY BACKUP [EXTEND]



"•M"l~d::,~@


# @) @ @ @J ___,.

After the completion of



backup,"=" is displayed.



(3) Press function key [F7] (BACKUP).



Press [F8]



([EXTEND]).



Press [F7) (BACKUP).



"= BA" appears on the console line and back up is continuously executed.



After back up completion, "=" will appear on the screen.



Now, all the data has been backed up and the power to the control may be turned off at any time.


```text


                                                                                               ^^^^', "`.^"`
                                                                                  ....'...    "??__i-`-!Il_>
                                                                                 ^}{+<>_~[!I'!_+>_;_]<l>+-?i
           ```````^`^`''```````^``````''''````````````'''''''..''.''....''''''''''''''.'''''.'`'`''''...''`'
          .,::::::,""^""^"^^^,,",,:,,,^""`",:,,,:,::,:"^,,,:","""""^"":,":;::,,:::^^"^""^^,:::::::"^""""",:^
                  !;!!",i:l!;'Il;;^I:,I:^l;;:ilI^!:;!,Ii:i!li^"I;;I<,:.`l;'";>!,^^II"l,'l;;::;,:;"::',,l,",;
                . ll!~i>_~<i<;<_!-!!;i_~:]+->~<>l~!;><"l>++>i,i-<<~+~illii;-_+~~~!+!I~>l-~-i!>i~+Ii_:~<~i>~<
                  >~i~~i~+>.><!!,>~; li+"i!<<~`>-!+:^>.>+_~~~"<<~]! i"!<; ^<~l^?><i~+`i_<<<`i<i>~~>!<i"~"_~l
                  i__<l+^!-<>i`i>l"<>i+i:~~>l>
                  !-__I<+>~+<__>,~<-<<!<<<<<<~<"I~~>:<><!^!l!ii^i"l!<i!i!!;~_:"
                  "",;^";";:^;;,`lIl:li:lI;:;ll":l!l"!;l;"!IlI!^l"lIl!;li,^ll,,
                 '<:-??]<<I>~>>_:;i,>~,;l^:i",>;!-::~:I_",<;:+;;!I"~:^;:^<>:li;<~;l>:i~,:>;i-II~I<-i:>:I+iI>`
                 ^~'l<<<i-i!<<+>':!';l'^i^:!^:-^:<.'<'"+^`_^`<'.<,`~;^!I'+!'!> ::.,>'!+',-`;~.`_.:~;`_^"<;'>"
                 "_'-+-<__!}_+~?^,!+?]]:!+1{_:+<[[{I!<}[1il<]-}i+,~]?^i-)[?]l_{{_>:i-?-]I++_~~"~>]-{l!<}_]l~:
                 '-!!!<i>iIllIl>;l!ll!!l!!I;::>l!iiI>l!!!:l!ii~l<lIll:>!IIllli!>!I;<Il!l"!Il!I:<li>>:;;li~!_^
                  l<+I;~+]_^+?<~~<;+-<]:~+<-_:i[~<+il?]<_?]~?i+]~;__>[l<[<!~>I?;-_~">>i^]?+-_+-_i;~+<-I...'.
                  ..'  ' .  ...... '. . .. .. ..... .``.'.' '. '' '' ' .`. '' ` ..'     ^'.'^^`'' '^ ^.
                ' i>?<!-~Ii_>~;i;l+i>+_<_]-~"_!-_]<-~->l>_>~;>-!>_:+-~_<!-_>i<i!i!+_><+lI+~>i_i<;<!l<~!Il<>!
                  i~i<i!!!,+l++_>>,'`"``''^`'^'^`^"^'`^'^,`^`^"'`,`","::`,""`""^"^"":I,^^l:",:,:`":",:,`,:,^
                  ;l"::"`^.I:;;I:"
                  ll!^I<_<IiI_I^I!l>,i^;>^ii_l  l<iiIiI;<!!^~i>I;!!`Il;!;i<"li!!;i^;l:ilI<lI_!;~!"lI!;!!i!ll
                  l<+<-?:!]i~-<I?]I_<-ii_!>I>ll;lI~ii-_[_-I!<-{_<-i>-?+->?]>~~~<>+<_[~!I"!;"ll,ll"!;I:!lill;
                  "I":!l. ,^l:l'I!^IIl!Iill`:>llI"I^l;l>l!'I"li";i`!>i>>;<!>;;~' ,;ll'
          ., "     ^^^  .'`. . '  . '
          ,}:[^   :-[-_{:l_?_+++-[~?(<
                `"  .'`..   .'     . .  ..            .
                ;~_ii1~:<-~:-?]~,<<~-<_~+];++I_?-_[~+~l-_<+_`
                   .       .          .    .. .'. . .. ..  .
          ;+ii;^  ;{?_~:-_:~><<<++<+
          '^'``'.''`^^` ":^`^`^^""^"..' ...'''.'`'.. .'.  .'''.''....   ......''    .. ... '...      .'''''
          +,{<;_->{1){~.+`l+<<llll+;!i;<!l!~ii?i;+-!~:,l><>;i<+i>;Ill!!i!i>~i>;:!!ll:;iIil<Il!lll!I!i,",,,;i
          >zmq|1n1{jxr_'~ "!><lliI!:i~,>iI;<;__;">ii~;"i>~<"l>>l~;l>!>~~I<<<<i,">i]i"il;<!>:lii!<i!__,    .i
          ">i<>l;!;l;,,'i :~>_~i!!:+!Il<!i<I<<!`<i!>~!;+>~<i^;~!i~!~-+.i:!->+i<l;_`i:_~l`iili!>:;,I:ii<-?l.I
                       `I :~~!Ii~ '>i>!+_i<'!<<li<:l]l_>:l!i>+">;!<>^!!>+lll<-+,~?~;Iii~i<<>;_>l;+~<I>+l' .I
                       'I ,i>ll!<I,">~>!<l!iliIi;_!!!IIii-!!i>:i!Il!:i+i>il^ii;^I:!^"l:lIl:~;;;,"!!l^!l^  'I
                       'I ,ii;>;,!>'>><,I,"~>I^_,,^i><`>!iIl;"><!<<^~i~<i<I                               .i
                       ^! ,~!I:!i!">!;:;>>!:li!I,;l":;l:I!;!I!<::IIi!:!!;,!>!:I;i;:>!!IiiI,;;I!,,;l;:ll!,~li
                       ^<^:Ii!i<~~>~<>i!!!!!!><>i<+><<>!!~!>l>>!+~>~+<i>il<<>li>+!i~!<!ii>li<+-!i<~+i~~i!<i>
                        ..                                  .  ........  .   ....''.. .   . '''``'''`. .. '.
                          ,>ilI!<Il,llIIli;I;:;,~:;l::lI;II.
                          ';!;;;l"i:l,:I;I:;;`,"l,;I""!I;I;
                 ,l, '>:;;,";,`!;!l;I>!:!;i ^>Il;"^l;:.^.,:;;;.,:;l;`,"^
                 :;: ',:!!l:!>,;liil<+i^!l>`;+iIi,:<l:^>^,!!!>^Iii>i,i~~.
                 ';` .:'``'`''`^'' `'  ;," ::^,:^""^
                 i[! ^+i++<I~>~><<I>~-l->],-<~l~>-~+^
                      !<+"i~~<>+~>?;l->:-I!+i<~[+>;-ll~_<~[_~:+]->
                        . ............  '.. ''`,'..'. ...'''. '"..
                        ^`                                                                  "`
                        ;"                                                                  ;,
                        ;"                                                                  ;"
                        I"                                                                  I,
                        ;"  ;i\[''''''''''''''''''..''''''..''.............''''''...'''.''  ^`
                        l" .?```.``!^.. .'^l'....':;````^`i:````^`l^`````,~'.''^':!`....'`  ,^
                        :: `,;!;:  I ;liI, ;.lI:I,""      !`      l      .!`;":":,;'!Illl:^ l`
                         ;,I,i_+<. :`l~?+l.,"]_>i;^^      ;^  ..  !.  .  ."I[_-_<""^_~i+]+I,;
                          '~:',`^:I""";"::I^`"""":,`"I,,:I^`:II;l;^,I:,,;,`^,",::^^:^``"^`"'
                           l i:-~>"~^>:]_i:IlI~_]:i"<,-~<">:!l[-"!"l;i-?^_:<;-~~:<^l!+]I!:
                          "I <,_I!`+:+"~_l:!i;i!-^<:<"+<+^~Ii;<]:!:>:>+}^-l~`+!l^_:I!~[:ll
                          :^. :^^^:' `,^^",  """":^ ':^"^,. "^`^,"  ,"^^,^ ';]l,:. ,"_+,,
                        ^<]+:<:~++~~];                                     'I.        "'
                        !]]<!?!~--_[}-><~'                                "l.       l__?i<][.
                        ,i>i<l :'l:i<~~<+I                               ",         "[-<~-+]-'
                                                                     ;liil!l:l+!l!IiI.
                                                                     `^::^,^",;,",,,".

                 I<^ ^>;;I";l;;i;;"!;,"~l>^<iili!I<l.
                 l>, ^;l!!;:iII!I;^ii!"!">,>!!Il!ilI`
                     .".~~i ><!ii!!.l:;!!'ll!!l>",Il^<l!;><>>`i;I!,i!~<il!i~_"i>>i;ii<,
                     '~~+!I!+]>l~I!!>>><_i>!;i!l<_i<i~i<il~<!<+;!i!~><,,:";;l^:;;:,:;;^
                     ';I!^"i!;``!'";,llI!I;^ ^' !!^I~iI!i.I:`ll';::ll:
                     "<;l:'i"!iI`>ii"IlI^IIl;,ll:III':,`I;;li:`;:;;,`;^!!:,l;!;l,;;I"ll":;:;;;"~,I,,;:`!II"
                     'IIl;^i^;lI"iii,;i!"!!l,"lll!!l"i!,i;;I!!;!Iiil^i^;i;:iI!Ii,li+Il<,li:iiI;<"~;l!~,<i<l










```

*Figure from page 16 (2346x3317 px)*


---


## 4. Zero Set Commands

4203-E P-173



SECTION 1 DATA SETTING



4-1. Work Coordinate System Origin



This is the origin of the work coordinate system referenced to the origin of the machine coordinate system.



As the standard feature, 20 sets of the work coordinate system origin can be set, and this can be expanded



to 50 or 100 sets.


#### Y~Ym

y~r_ __



____ •Y_:~00-1•_



Local coordinate



system zero y



(Set by user) 3



~1..~----------Xw1



Work coordinate system



/. zero (Set by user) y



Machine coordinate system zero



(Set by maker)



Position encoder zero point



Y,: Machine zero offset amount



Y 2: Work zero offset amount



Fig. 1-4 Work Coordinate System Origin



A function called the machine coordinate system origin has been implemented. After the position detector



is replaced, all that remains rs to set another machine coordinate system origin, without having to set all of



the work coordinate system origins (and others) at new values. This may be applied to soft-limits, thus



helping to reduce the jobs required after the position encoder is replaced.



How to set the work coordinate system origin as follows:



(1) Press the ZERO SET key.



This changes the display screen to Zero Set display.



(2) One page of the screen can display 1 O sets of data. To display the data for the 11th and later



sets,



press the page key



@ .



From the standpoint of axes, one page displays the data for four axes. Therefore, to display the data



for the fifth and later axes, press function key (F5J (AXIS CHANGE).



When the desired page is displayed, move the cursor to the data which should be set or changed.


```text


                                                                                                ""^"`, "`'^,'
                                                                                   .`'.'...   ."--+_i-^+!l!_!
                                                                                  ^?}~ii_~]II'i__+_I+]~i<?_+;
            ````^^^^^^^^^```````^^^^^^^^````^^^`````````''''''''''''''''.....''''''''.'..'.''''`''''''....'`'
            .`""::::"^^^^`"''''"^"^^^^^^^```"^":;;;;;;;;:,"";;;;;;;;;;;;,,",,;;;;;;;;::::::IIIIIII;:,:,::,,;"
           .{;      }]_i>i`/__]^[~<<+><~!~i>~-<
           .->'    `}-)__-^1})["]+}{]]{]]|-[){|^

           '<,l    `]_>_:>i<><_i_]li->__~i;<i<+I
            "'`     ^"",'`^",^,^;l"';::;:"'"`!I`
                 "~i>"!I+<:!l~>,li~i:;iI<"II!:!!!->:~!~_<I;<~il>l!<lll>+!:i!<!,ll><I:i<iill::lI;<<I<>,!l>ill.
                 "~l_>iI<<li<[<>+<+!<ll?<!<_>l-_~<ii__!>!l!+_>~<l<~~><!l<!~~_ii!ii>i!i>+i<_<i!>ii<i<<l<+<~+i;
                 :<!<~lli~>><i!!i>ill;^>;l>iI;!!ll:ili:;l!I!il~i;<><<!;:!!-!"l~:i<:!+:"_liii<I>_:l~;><><>!_<!
                 l>,?!,< !+~"_~_"


                                     <i^    >!"    >!,'   .~:;'
                                     !~,    ,_l    "++"    l[]"   .?!.          .
                                     >. .`  'l  '   ;`,,,`^:>.^,,::<_,^^^^^^^;l`<__^
                                     <,^i)>':<`^1{,`i^'l(+',l                 l  .
                                     ~""`'"^;<^"^:"^i^^`^:`,l                 !;`
                                     <.     "i      !      I!;I;;",":;::,^,,,^+~]:^^'-~i;
                                     i.     ,I      >    ^I,`-]{]<]]?[_[_;:  .~  ..'.^l<;
                                     i.     ;l      <  ':;. ^)]][>I[-!   :~_; <
                                     !      :;      > ,,.   ^><,!l:<<l.  l:"I <
                                     i      ::     ^->;''`'``'`^``''''^'':"..'l^````'+,^.
                                     <      I:    "I"^{]}~_}}[1[\__{{{];':` .''^`^``'>~~'
                                    .<      l:  ":"  ^__i<[-l[Ii]?i.     !i>^
                                    .>      l^';"                        ~:l!
                                    '>      <_I' .'.`'..'..'. . ... ..'''l^..'''''''.l^
                                    '!    ';l;{}][?]i?-?1])[i]]}{_<}-l`^"l"`"""""""^'_?l
                                    `i  .:l` ^1(+?~<]1[]:`"`',^""'`"`.   il:
                                    `l ,I^   .'' .' '...                 !Ii:
                                    '+l,        .       '''''''''...'''''i' .........,.
                                    ~1?]_i!+~~~~I~<l!<+<"""^""^""^^^",,,,"""""^^"",,`[[^
                                    ";l!l,:llll!`ll,;III                              .


                                   ><: ,11]-?~?:i_~!:?}<_;>~i>lii
                                   ^^' ';;;""^:'":,:':::;':,":;::
                                   >-! ")]+}"~]-i"-]-?I!++<i~<
                                    ''    . ...''.' ``.'`'^^^^
                                             .`    . .'    '   .. .  '  .   .'
                                             :<[;,I>,I}_~>I+<~<++~]]:_?_}-<!!-+]+;
                                                                               '
                 ;:I,::l,,^:!;,;!:"",,,;,,^^,"";:,;:`"":,,"'",,,^""^""""`^"",""^"":^" ,I,^^:^'`^^:"^'^"^`^"`.
                 i!~<>~~>!l<?_+>_<>l<-~~>~i!>>!-i<-_!_~~-<I!~~}>;i_<>+__I!i+++>~_<-~~.>--<;+?!><?_>+I>?~++_<^
                 >!;_i<<<~l._!<<~Ii~I<!Ii:!l;:-!I>l>+>>"!<<~l!~^ilil+!~-!l_i++>::>~+i`I<<ii!!!+l!!<>:I~<l?,~;
                 <+>"+i_l,<>i!+!+-;l~<_>i:I>~+i>"<<>!,~><!+^>i;>><^i>I<_, <~<i,>~~!]~,+~~?~_l<:<>1<<<+[,I?l<^
                 <++!i<l~li_<<><!?<l<_+>;>>i~-<>:]_<;_~l>!~>?ill_>I>~~iii^ll<<l<~<',,'II;,:,',',,:`"",I^`,,;'
                 ";;;"lI:^^l:;;;',;,^;;,.;:;":I`^I;I.:I"l;,!;:"'l"llii,^i,i<!<i>i`
                 ><li"i"li:!<l"il~;,!IIi~l>i";l!<!l^;ili"^!^i!<II!`
                 """,`:.,,.^:"';""^'":"",:I:':iIll:":I<!^,!";Il;ll^
                  ";^ .>:;l:"ll.l~;>!^l~l:":;'
                  ::: `,"Il;`:l`Il,;:'ll^`"I<:
                       ><i":>lllli:i<!"~ii!i",!li>!"!"i~!l,+<l:~iiii"
                       '":^^^,,;!;`^::`;;l,i:^:,:;".,`:;::';l:`Il!:>;
                  ;~, 'l,:^,;:l^";li:';,::;.`;;.:;;:;, ::':;:.I,";I" `i",l::::`!;,"lII^;,"!:`^:I^^:,"^:,"
                  I>: `<i+;!i+_:I;li!,<!!>i":><^!>_!>~'ll:>><">:!++>..i;;i<>!+;>>i:_++:!>:~+:^li:l~<l;_~>
                      '_<i;
                      .""",^;;"`,,""^:,`.!!i;
                      ^~i<<;I>!;i~?!"~_; <}-l
                      `;^^^^;"':I:";,":;"Ii!";^',::`:,:^:;:":",,;,^::;","";^^`,""^ ::"",;""``"';"^:"`,,^^:"".
                      "!!>>li]<~~+!?_~+~!il+><!:>><!_?]!<~->~_i<--!~][~<>l_<il?_-<.:I~<~~<>!;<I_~_+-<i~~i?-?"
                      `i!^++,i_>`~li;~_~`<+>~`li>i>:ii!_~!;:<~"+i-:i+~~_,>><~+__?i`
                      .::^``^"'."^^^^^'`^`^'^':`'"`'`".````'^:`'.'^`''`."`..^'`''"''`.^'.'`''...'....'.' ..'
                      ^_><~ll~~:_+~~++i-_}-,<;_~_--___"i~>+<!_~;i~~~~:_;_~i;[_-;__++iI-<<+?i~<l-+:~:>~-~+[-~
                                                                                                        ..














```

*Figure from page 17 (2346x3317 px)*


---



4203-E P-174



SECTION 1 DATA SETTING



ZERO SET



"PROGRAM ZER()'t



97/07/15 14:10:00



1nm



(3) Setting



NO.



ACT POSIT (WORK)



=S 45.



=S 32



=SB



X y



10.000 0.000



0.000 0.000



45.000 32.000



23.500 1230.000



32.580 -0.014



0.000 0.000



0.000 0.000



0.000 0.000



0.000 0.000



0.000 0.000



0.000



0.000



8.000



456.200



2.580



0.000



0.000



0.000



777.000



0.000



-260.000



A--Mtd



-100.000 300.000



SET



AOO



CAL



SEARCH



[EXTEND]



(a) When the offset of the work zero (origin of work coordinate system} is known, press function



key [F1] (SET) and enter that work zero offset. (The entry data is X



and Y



on the previous



drawing.)



(b) When the work zero has been set and it serves as the reference of further offset, press



function key [F2] (ADD) and enter the distance of the position to be set as viewed from the



preset position.



{c) When it is necessary to set the work zero offset which causes the present actual machine



position to be the new desired actual position, press function key [F3] (CAL) and enter the new



actual position data. {In the previous drawing, key in



and Y



to set X



and Y



The



entered data is displayed on the 21st line of the screen.



(4) Press the WRITE key.



This updates the data indicated by the cursor.



Note that a "*" appears before the number of the work coordinate system which is currently



selected.



[Supplement] Local coordinate systems are effective only in programming.


```text


                                                                                              '"^^^`, :''^^.
                                                                                 .'..''...   .;]]_+<-`?;!!_;
                                                                                 ;1?<>~_+]:l -+-~+;[}<!<-_-:
          .^^^`''''``````````''''''``````'''''''''''''''''.'...''''..'''''.......'''''.''....''''''``. ..'`.
          ':::,"""",,,::::::::,,"",;;;;;;,:,"""""""""";;;:,:,,,:;;;,,:;;;;::::::II;IIII;,:::,;IIIIIIII::,,:'


                              ^^^`..`^`",,,,,,,,,""^^""^^^^^^^^^",""^^^^^^^^^""""````^`
                            .I"":<[]i~[~;;;:;;;;;:::::IIII;::,,,:III;;:,:,,,",,":,"^";"I'
                            ,^ `"!_-i<?!:,:,::::::,:^```'^^``^,,^^^^^"!-~~_i_<i_!+>-~l '!
                            ^.                    .~-??_}"<--<.       :!Il!:llI<ll~/)"  l
                            ,'       ^!),       ^<.^^^``".`^^<'''        I^        ^`   !
                            I'       -";^       ;_l1?.       <l{{^       ~l?1;         .~
                            I'         <,  ","""i{~\(;^     ^-;1)"       ~l]\l         .!
                            I'         i,  ^,"""[1+|)I^   .!?[:)1`     `+{I[1;         .I
                            I'         +,       <_l)]      ,I+I--"     ';?l[(I         .I
                            ;'         -:       `_i|['       ~I[]^       <I-|l         .I
                            ".         i^       .+i1-'       +l1}`       <I-)I         .I
                            ^.         -:       '~i)?'       <l}}^     .:+;]);         .I
                            :.        ^["       '+>)['       -l11^     ':~l{|;         .I
                            !'        .^         ^`,"        "`::        "^,I'         .;
                            ;.   .'..`. . `''.        <` ..     'l ..     ,:           .I
                            ^.   >~`I_-I^")?_;      `_|_i{~   .:_-,~]:  ^__;-_"        .I
                            ".  .,.,`                :i->l                             .I
                            ;.  :{"{~                                                  .I
                            l'  ^];-'                                                  .I
                            l' .Il^"'''''''....''....'''''............'..........'.... '>
                            l. ^^..^";l"'.'^:,^'.`^l^..'`"i^^^^^,!^""",;I^^^^^I;`^'.'. '!
                            ;"  ,~I  `: l_; `  li  :^+>+i,l     .,     `,     "'Iii~>I ^I
                             ,,^:!"''^"'Ii:',^'Ii^'"^i!!l,:.'.'.`,.'''.^".'.'`:,!<l<+<;;.
                              .,I;lIl`,I;;II';lI;;:'IIl:;,`lIl;l,`ll!I!"^!l!ii",lI;::''
                               +"?<^Il~^+?,!i>:_?'_;:i_['+!;l?]`>I;>?-`<i:~<!"<!,-1iIl
                               :l;;;;`;ll>I;^I;liII`II;l;:^l!!i;,`l;I!I,"lllIl:,I;lIl^

                 I_: ^+>_<l!
                 :i^ .l;I;:<
                   "l^ Il::'"i:'^iI,:`;:l,`:,,:."""'"":,:'^:',^:^'^^",I",I`^^":"^"'"`"^`^"'.^^^^',`^^:`^
                   I+;'-~<-~l-<!~-[~ilil<+;~<~<:~ii;~>>[+,l<!~i~I!]<<>-~-?I<-_-_!+,<;~i>_<,I+<_~II~!<-i!'
                      "+<l;_"!"+]>!,i+<!l>~_"<i-I!+~-^<_>I:_-<], <i>~,_<_>"??]I!li-"+!_,il;-:l~<I_>>ii!_^
                    . '-+?-i><l.                     ...     . . .  ... .`....... `'..'  "'.. .''`.'..''
                       '.'..`"
                   >-,.~+l!:,>i^ii!<'iiI",><,!>>i^!<lli>II"ii;ii"l>">i":i~!llIi::!l;!~l;`l?l!,'I;li:
                   ":``<!!+ill<l>;+~+>i_<<?il<~i<l~+:?~>;~!_~!<<:_~>i!lI<~~>i!~Iil;<>!~l"+~~+i!-i<_!;^'
                      '>>>>~i;l<-;>;+I;!!i!^ii!"il!i`>iI:<>i<!ii">:>>:<!>i!i;:i"<!:~<"+l,<i><<Il!!l;+>;
                      "~l~~_;~>>~~>!
                      .''   ..           .    ..     .       '                .
                   i_;']+>-ll><ll~<~~~+>>,-"i_I<_i"_i~;l-!!^~?+-ll_<>+`l<l~~~,~~;l>>~+>lI_<!+!"<<>~>i>
                   .. ^il<_!~:!l,_I<<l;>+>"~+<li~;<iil<;ili>!!;"ili>;>l>i->ili>!l?<<;_i-l;l~<lli+~:++<`l!!`
                      "+<~!<!ll><+i:>~!i,Iii<_il<l+>>i<:+><i>iI^~>>!l:-Il~ii;~!l~;l~I>>li;i<<;!I_?:l;l'l!!'
                      `~><i~I<i~~>i,!]~<'`<;l><;~iii<!<,<!><<>[`l~<^l^>!,<li^ll'_,!+l:_,>><::<I^;l+,
                      ^_i-~i-li?~>:i:?<+?-+_<:~:!<>;~I_I++<"+I--Il><~+i`
                  .  .'    .   ..''''    ..                      .. ..
                .<-" I<<__l++~;]?-<_<i-<i
                 .   '"``'..'^''..`..`^"`..'. ..... ''    .
                     `~i~">_~-__<I?-:~]]il_-++]_+l?i!_+:>i>+~:
                     ^:`,'^;`" `'`'`.^``^``.`^^"``.:`..''"^`'..^'^'..''`' '..'^'.`. ..''.' .''.' '    ...'
                     ;-<?l;_<+^_.;i'I[-_+?~l;-_+i+`__i^i<+-~_^;~^<+l,?~_i^+~~<]~_[+`-_][++^+_>~~'-;:~>>-<__.
                     :++_<+~~.                                                                            .
                      .  . ''
               "[_>_~_<i+>-!   "lii-!!<>i-~<-_:>>~-+><,+<II]]><~il:<+i:i,<!!~i>>i<i>;
               '"^,:"^^'"`^^   .^^^"'^""^"^":,',:,:,^,`:"^^,,,",,"`,,;'"";";!,:,,:,l:





















```

*Figure from page 18 (2346x3317 px)*


---


## 5. Tool Data Set Commands

4203-E P-175



SECTION 1 DATA SETTING



5-1. Tool Length Offset and Cutter Radius Compensation



Tool offset or compensation has been incorporated since the tip position is dependent on tool type.



Tool data consists of length offset data and cutter radlus compensation data.



The system offers 50 sets of tool length offset and cutter radius compensation data as the standard



feature, and this can be expanded to 100, 200, or 300 sets of offset and compensation data.



For offset number 0, only "O" can be set.



Data is set as follows:



(1) Press the TOOL DATA key.



This displays the tool data.



(2) One page of display covers 20 sets of tool length offset values and as many sets of cutter



radius compensation values. If desired data is not seen on the page, operate the page keys or



the [F4] (SEARCH).



TOOL DATA SET



*TOOL LENGTH OFFSET*



(H--) ""CUTTER RC



97/07/15 14:10:00



1)...... l!J!I


#### NO. NO. NO NO.

1 1.000 11 0.000 1 10.000 11 0.000



2 2.000 12 0.000 2 5.000 12 0.000



3 1.000 13 0.000 3 2.320 13 0.000



4 14



0.000 4 0.000 14 0.000

* 5 15 0.000 5 0.000 15 0.000



6 16 0.000 6 0.000 16 0.000



7 0.000 17 0.000 7 5.000 17 0.000



8 122.432 18 0.000



0.000 18 0.000



9 0.000 19 0.000 9 0.000 19 0.000



10 889.499 20 0.000 10 0.000 20 0.000



y z



ACT POSIT (WORK) -260.000 -100.000 300.000



A-Mtd



=S 5.



=S 5.



=S 10



SET



ADD



CAL



SEARCH!



ITEM



t ITEM i [EXTEND]



@@J@@J@@@J@J



After obtaining the page displaying the desired tool data, position the cursor at the desired data



element.



(3) Setting



(a) When the tool data is known, press function key [F1] (SET) and enter tool data on the



keyboard.



(b) When the tool data has been set and the change amount from the set data is known, press



function key [F2] (ADD) and enter the change amount.


```text


                                                                                               ."^"^`, ,''^".
                                                                                   '...'...   .;[]-+>-'_Ii!?:
                                                                                  ;1?~i<<~[Il.>~_<~;]]>!>_+?;
           .^^^^^`''``````^^^^^`'````````^^`'''''''''''''''...'........'''''''.....''''.''''..''''''``...''`.
           .^,:::,""'```'""^^^^'"``'',","""^```````''^,;;;;,,:,,,,,,,,,:;;;;;;;:::::;;IIIII;:::,:;IIIIII;:,,`
           :{'     ^)_>>?:-[<+~_.[?<?"<_!i><!<!>i!!-<^
           :1I     ._?[]{;_?{1[|"]1)):_?]1{{{}[|)-}1|! .

           :i::    >~<!:!<!__,>-?~+:~!<l<I~+i,-~<~!!l>!i!iil!>ili'
           '"'`  . '::^^,,;i:.^^:;:'I":`":;I".,l::;,`,:";;;":l;:;
                 ;_+i"+?~-;!;I<~~<<<>~?<>:l>_I<<~~"><i!<!i<[+<I<I~_;+_!<+,><~]_~I;<;]~~_i~_<<,<:!ii;+~~i
                 `^``'`'^`.`.'^^`"^"`^`'"..,"'^^^`.'`^`,``"""^'"'^".'^`."'"`^"^"''^',:::^":""`"'^,"';l;,
                 ;<<i;}-~;>+~+_+~"<;~++{[:<{?-iI?__:~i_;i<{-:;+~<iI;<!<-+>><_~<,l[_-^
                 ^,^''``^`^`.^:``'```'^:'.^'^`'`^``.,''^:`^^.'^^'`^`^'`""'`^``^.'^^^'..   .      '
                 ;i+l"?+-_~I^_]_<:;]:;-~+'~:><~:l~i[]:,[[~?'~+~;l>-->.!__!+";<>!++i!<+i~:^_+_,I_'__~,[??>[_~l
                 >~?<><:"-!<<-ilI~~:-<:<~<~!~?~!<;I--;,-++'ill]-ii+_~,~;<}~_!!<><!i>~<~<i<]~~,!?~>`. '''.''.
                 ","^^"'.,`'.`^'`"^.^^.^::,`^""'`' '"`'"""."'`,,`^:,,`"."^,;`","^",,:l;::;I::',I;;'
                 ~>>^~1-]>I+~<~+l;<`<+["l~'i_i;_!:-+^
                 ''`.'''`''`''^^`.`'''". . '`'.`'.^'.
                 ~~-[I_;<?i!?;-?_+-+`
                       '        .. .
                  l~I ^_>--~l-+,<~_~<`~~-~<!__l
                  '..  ^`^```'^. ''^'.`.''''^"`
                       <<-li-?+-]-I__!!~~!+}?_.
                                ..
                  i[l '<!+lI+~_;I>:?<~~~:lil~i!:]iI<<i"<;>!<,+i>-i^_?i>:l<_i+l;<ii:~,li>I;"+<~"<;II~<l
                  '`. .i>_l<:<~l!!!l>+_<>"!_~i+;`~l__<!<i!>~~il~!!iIi<<l:~!>->I><i<I,i<~i_!i_~:!li<l~>,:`:^
                      '~_!~]!ii+?_-~__-i;';!lli: :^lil:Ii"Iii;,;`;l`lll;^!""l!:!i_~^^>i!lii^li:!i~~,l><>,>,
                      `i>;>l+!I~~!<i>I!<
                                           ........'''..  .........  .......     ....
                             .::;li>!I!!!;II:::;;I;;;;;::,,,,,:;;;I;;:,,",::;:;::,;;;I::^
                             ;" :l-)]:}}}I[}I`^``^:,":,,:,""""^^^",""""^,";I;!:II:;:l!:.I"
                             I  ..::ll.:iil:"iliI;';l^".......":;liI":l1j{{-?1>+-i]-|[!.^i
                             ;    l/?i'l>>;,^!;>]{':!`^       -1l;<!`,"<-l'_1,;.     i-^^i
                             :    .<:     ^'<i  ,?'  l,i+"    ;~    !,I<"  _<   `;;~!   ^l
                             !     :l    .<!([' "_.  _i?1,     <    !~_\~  li   :_>(]   `:
                             i     ll     Il1-. :-'  _![1^    '+    Ii~)!  i+   :~>(-   `:
                             ;   .:;l  ':l->/|::"_'  <I[1"    '<    I>+\~  l<   ,>i)?   `:
                             l    ^!!  ';i1~/\;,,]'  <I[{,    `-    I>-\+  >?   :_!)-   ^I
                             !     I;    ._I}]. "~.  +l[}^    '<    l<~|~  i<   :~!(+   ,l
                             !     ll   `<+;[[. :_.  ~!{{^    .<    !~<|~  <~   ,~<(<   "l
                             !     <!   ^!?l([. l{.  _!{)^    :-    l<~\+  ~?   :~<|+   ,!
                             !    .l"   !_!,_~  ;!   !:i+`    il    ;!I+; .<!   "l![!   ";
                             i                         ,         ''        `            ^"
                             I    +>^i_>>'i1-+,      `_),;+l   .,]_"-_'  I?-I_<         `"
                             ;    ,`.'"^' `:""'      .__{_!`    ',"`::   ^;^`;,         ^,
                             !   l~;!                  .''                              ^,
                             l   !_;-.                                                  ^,
                             l   !I.l'                                                  ":
                             l  ^,.^`^;,^`'^^:"^'^:;!,"^'`,;""""";:^``^^l:"``^";"""^''. ;l
                             i   :l`  ,' :l` I .;: .:"I;!;,,     :,`:;,'l`^;;` I.;:::;" :;
                             ^;"'ii`..:``>_,.;.`><''^;<>~i;"     "",!_l':^:<?I'"'<<i~[~";.
                               `:;:llI"IiII!I`II;:!,^I:::!,"illl!^^l;:;l^"l:;l!^,;,,;:``
                                <,]<'!Ii"[[^!i>i]]^iI:+?]^~i,+{>,i!:-1~:<>:}?l;l>:?{liI
                                lll;:l"I;l>;l"!IIi;;"llI!;I:lIiiI::lI!!l;;l!I:l"Il!<l!"

                      ^__<"`~<__!I<;!~i">~><^+~i~<<>i;><!`+><!i~Ii!<^~_<l.lIi~~!:;~l^;lll!";>;>!^l!!iliI;>>!.
                      ,~~_!i+<;:^`l;`,,`;I!:'::I:;l,l;":,'::;";;^:::'I!I;'I:;;I;^^:I^:l;II':I^;l^:Ill;!::!!!.
                      "l!II>;I
                  ";. ',`:^..
                 .>?" ,-+?+>+
                    .'  ''   '`..'.'.'.. . ... .       '   .       `.. ''''.
                    <};`?<i~:I+~;+~<;]_?I+I>>~--i^+_-]ii<~~_+_;__~I-;_l]{<>li-i<i__[l!__i>]}-;~l>--^
                       "~<_~>+i<.               ...  .. . . .  ..'.  '..   ........'. ''..'.'.....'
                       .'^".`^.'
                    ~+^`~>Ii^;>I"!!;"><i"lll,i!!;^!!^ll!;il":!li;i,:!lIII;l!;!"<!I"!!">!!";,ll:Il:.;I;I;
                    Il`"+!!-l!l~;>l<i-i~<<-_,<~~Il~+I>+~;l+I!!<<i[ii<>~!I:,Ill"lll,>!"ii!,;:ll:!i:`!l!i!
                       ^~!I<<>"!<~"~!_^!<>i<,<>!"_I<+`<<l;i~<i?l:~iiili.














```

*Figure from page 19 (2346x3317 px)*


---



4203-E P-176



SECTION 1 DATA SETTING



(c) Tool length offset



Before carrying out the above steps (1) and (2), set the zero offset of the tool axis. Mount the tool



for setting.



Manually align the tool tip with the reference surface.



Press function key [F3] (CAL) and key in the data, which consists of the axis name, the direction,



and the current position as viewed from the origin. Note, here, that the axis name represents the



axis parallel to the axis on which the tool rotates (X-, Y-and Z-axls).



Generally, the axis name is Z-axis.



Example: CAL



10.5



-20.5 CAL



(4) Press the WRITE key.



The data is set at the position indicated by the cursor.



The tool offset number presently selected is identified by an asterisk(*) appearing right before that



tool offset number.



5-2. ATC Pot No.rrool No. Table



For vertical machining centers and other machines which have a small number of tools, the



memory-random ATC specification is adopted and for machines with a large number of tools, the fixed



address ATC specification is adopted.



5-2-1. Memory-random ATC Specification


# IACAUTION


# I :

In the memory-random ATC system, the tool set in the spindle is returned to the magazine



toolpot of the tool to be set in the spindle next. Therefore, the correspondence between



the tool number and the pot number will change each time the tool change cycle is carried



out. This requires the initial correspondence between the tool number and the magazine



pot number ta be stored in the control memory after setting all the tools in the magazine.



In addition, since the use of a large-diameter tool will cause an interference with adjacent



tools, the control must be capable of recognizing a large-diameter tool so that the toolpot



which accommodates one is placed between the pots having dummy tools or no tool. That is,



the large-diameter tool must be returned to the toolpot originally stared.



A large-diameter tool is distinguished from other conventional tools based on the machine



specifications. Distinguishing of tools-large-diameter tools and conventional tools - is made



according to the tool diameter and the value used to classify tools into these two categories



depends on the machine specifications.



Setting of the correspondence between the tool number and toolpot number is made in the following two



ways:



(1) The table listing the original correspondence between the tool numbers and too!pot numbers



should be made beforehand on the display screen. After that, the tools are set in the toolpots in



accordance with the correspondence table data.



{2) Tools are set in the spindle and they are returned to the magazine in the manual tool change



operations. In this case, the toolpot where the tool in the spindle is to be returned may be



specified or the one automatically selected may be used, as required.



Explanations in this section cover the procedure indicated in (1}. For the procedure of (2), please



refer to II, OPERATION, Section3, 4-1 "ATC".


```text


                                                                                               """,': ,^'^,`
                                                                                  '''''''' . ."-]-->]`_!l!->
                                                                                 `[[~i!+~{I;'!~_<+I+[>;!+?_l
           ''````^^^^^^^^^^^``````^^^^``'''''''''''````'''''''''''''''''..........''''.''.'...''''''`'...'''
          ."""""":,:""::""",`^``^""""^,:,,,,,",,,",;;;;:,,,,,,,,",;;;;;:,,,,,,,,",",;;;;;;;::::;IIIIIII;:,:^
                   .!l ;+li;<Ii-i"<?!~,
                   ';:.',",`;^!l"',,:I'
                       <_~~I!^I>l>~!I:l!~_<;]+!i<;-+~<:li,_i~l+>'!+l<~i,~il,l-<~>;~!<>!<i!l<i! ~_llili>l;ill
                       ~_!i<_+>+,;,,;^,^"",`;,"",`::l:^""^I":"::',I^",:^;,"^,,;I,",^,;"I;";!;; :;,I;"::;^I;,
                       ,I."l;l^~.
                       i<il,Ii!`><!;;<i;>!I:<,;i~:l<l^l~<lilIl"l:>>Il^
                       ,;I,,l;l`II<"^";^Il"^!""lI""Il';Ii;!:;I^I;:ill`
                       !!l!!^I:;Il;,Ii!`<!_,ll<;^^l;:lII'I`<!,^!!i."llI<";llliii^!!i!:;li;"lI;i.Iil^il;li,I.
                       I!i<-!!lliii!!>_i_i~li~li<!<<<>_+i!>~>Il<>+:,]i<<^><i<I_+l<!>il<_<!l+<i<:l><I~i<~<~<:
                       !i!l!ii:~>Ii!l<!><<!:l]:I+<<<+i!!!;<ii:<i-l"'+><+"l<<<"ll_II>!I~>i"~~l<"l_<!~><i_:~+!
                       !~<!,+~<[-!iiI<+"+<+,!!^_<>~,;~<:~+<;>__-?ll], !^l?>i!><_<_;
                       ""`^^^^".."`'''^'`````''."'`'` . ..  . ..... ..  ..... .'.'.
                       l+_i+<~_~,~~:<--lI-+i~:+:~I?~]"
                       :^^^^^,^. '":"       "^         ^,^:
                       ~>+~l-_+` I~_+'      <;         ;~i+.
                                 ;<_-'      <;         `+-;_.
                                            .           ....
                 "<! .+!iii:<i:i+_<<~,>!!'
                 ^I; ."^:::'":^^:""",`;;i.
                      i>>"l~~l;i"<i,~,ii:;>>_~i!:><+!~~ilii:~>;;l!i!I
                      ^`"'^,:,`:':"':'`"`""""^^^'^,""::,`"l'",`^,"","
                      !i>l<li">-><Il!!++~,>~<~~>+i;~<<!<+il>I~<i__<>!~ll-,i~_+>+!;>l;_>><<>>>Il~+i<i~!il!i~l
                     '<!~;<)~~>l<><~~!^""',^"""``,`""""^"^`^`""^"^,"`,,^:.",",^,^^,"^l;,,:""l,`i,^,:",:,^,;^
                      I;:`:I;!,";";l;,
          .` ^     ^"^. ^'  .   .^    '   ^'.'.
          l[;}`   :}+~+:[<}i+}-l!}??-I{?<.i})}}-
                `'.   ''  '  .'.. ''   ... .'...    ..                                           .
                !I_.`+<-+~< Ii_~~+>>?^.<+i-<< ,?>_ l?~+I >i~i><i_I <-~<+ ;<<>~ ~'^~l+}'"<li-_+ '_`^+!+i '<<:
                ;!>!li>:l<!<!>!"-~<^<<~>+-!++>I,i,~~<~->i:<>>!+!;<><<~><i^~-~,!I+i~>;<li+~+:!<;ii<I"-~l<>>~;
                !<-+<~+;<-+<!~!Ii~!l-~<l<l>_<><l~"I::l::"`:",`;^',l;,:,I;';;,'I'!;<l':I:;;l'"^"I:l;.;I":lIl^
                Ii!;;!l`::;^,~I!;!Ii>;,`>^ilIlii!'
          ":,",.  `I"^'``..^`'^'` ::"',"'`':''^''.
          :i!;I'  :-_>I~<i,_>>~>i,~<>:>-+<<-i__<>"
          ,',`":";;,,:^ ,"^'''.'.' ..'.'`'`''..'`^^`'''`"","`'`''`'.``'^^^"^^`''.`'`''''''`"^^^''`'.......^'
          <?c/<1(~(\f|!'>'!>;]-I>~-~<<~:<]>]~~;>-+i:_~--+>`~~!l<>;!]ili;~<;___<??:<,<?~<>+_!~I-~i,>++~~+~_,l
          <XvJ({)[+)}}l'I ;lI~iiIl>>>!illllI:i:;il;;!~i;llll~!^!!ll"!<lI;~l<~^~>!"!Il>>!Iii!iI!II;<~_<<l",';
          .      ..  ..`I l~i_<iI!;li>;<!:ll:_;I~!II"I>:<<!i+<"><~I ,Ii>i><><'><l,iili~_iIl~>i>!,<~<>><;  `I
                       ^I !<>,<>>"lil<<!'~!i:i~,;ii"iI!<<i'<-"!<<!~-";>!!^+!>>I<i:<iI`>>_!]i">>>_`<'!_li+~`;
                       "! "li^ +!~::<!!!!~"~i:;!_<;"i<!i<>li!~iliI<_~><~<;;>i:!li,iIi!ii^i~<:+~:I!<i<~>!i `l
                       "! ;>i:,:l<lll~!!i!l>ill!i!il!I!i+~il!<!i>llli_<i!l!~>:Ii~:<!l!i>,l!l!!l;;!<-~~!l; "i
                       "! iil";!lI!<`!";i"!!;!i:;";i;^!!l;!":I!;!l>^l~<:'<++:_;>~"i>"!!ii^!`>>::!<_~i!i!  'i
                       "! :I.!!<<ll" !l:!"l!! :!;'>^;"!;Ii^!<!Illl^:I::"><.:!;l; l:'!>l!<llI:I':!>""l!;:l;>!
                       ^; I<I-!I?<lI;>~>+:!>>!!+<^>!<l-<-i>><_!<<+I!~<;Ii<l>-<+-I_<!~<~>+<><!+I<<~!!>_~~~!_l
                       ^, ;~~<>'<>::~!_i>;l!>+">~"l-?~~ii"+:I<!l?!<>I-Ii'i~<_;l+-l~++^;<iI,~"Ii_;:<>^<!~_!<:
                       ^, I<li<,i!!il!lil__~<,ii>;i:!>><>!>~~>~~i:_i;><+l;+<ii+:~Ill!>Iii?!<iI>I_>< ,+>]i<;,
                       ^: ~_~:_~-?;++~>_-~,~<~;>>>-i_~I+~iii<<i<;-~l~~<->>I>i+]>?-;>-~<~<...  . ...   .' .":
                       ':"IIl:!!+<!!iillI!"Ill,l!i!Ii!:lll:I!;:l;!>l!>i~l;,I;~II!ili<i<<i^'`^``^`'```^"""^:"
                          l!:-i-l,+~ii-_<`<ii^~'~~?<>i!<<>~;l!iI`<?!~';lil>!>>!i<,~!<~^>i<+<^!!"+<I;<_i~<<!
                          I<>~~}l<?>i~^"-l~+iii<~<iil-><l~>:<!!>"<<<i!<<:lii~;i>~:!i>i!>_>>ii!i;<!^^<l<ii_!
                          I-<<i!+<<iii>:!><~!{~+>i<?:i!<i_>;>i]~lI<+!+<+"i~i~l<l<I<<li+l~+!>~:~i>I^;<:l<~~l
                          I~!ii!+l<I>,~<:>i>:<~~I>~~"+~i;!>I"<+!<`><~!;i">~<<i~,ii<~"I>;i<>~+,<~l,~_<-~ii<l
                          ;-+~_>+>"~;li<,i<~><><,_~~~?<~-~i>i
                :^",`'.`^^`'`^``^`'```^^'``"'^``'"`"^.```^'.```''..'''..'.'.. .''... ...'....'..'.'...  '
                <_~]i]l~l>~!I~><_?_~i~]+<-!+---___;<_<!__!Ii<<??!l_~~<+<[+_I!+~_--:+!!+_?+l<l+-l+-?~?__~~-~^
                <~+<!.                                                                                ''
                ''^`'
                 li, `<l<,~-+!;~>!!I<+I^!l>l!<,i>!i>i!l!>l;!l,i>i!ii;:ii,!I!,;;!!!ll"l!l;I;lllI"!;l!l!l'
                 ^^` `<!>;_<><"><!_+l<+!!<]!<<Ii<;~+>i~><<!li;<<~<;l<<<<;+<<^~<l>>i~;><i;i~i+!>Ii>l!~<~I.^.
                     ^+i!<<l!~"Ii>_<:+~iI<!<>>;Ii,l<:I<<<~-^>ili<l .>>~I,i~<'~iIli!<:!>i:~~:i^l<:I>l<i<_,i^
                     ^+>>iI-?<<<,++<,>+:!>i<--~~i]_>~_:_->_:~+_>
                  .  .`                      .    .
                 ~]: ^-ii~"<<l,_<;>:+~;i-~i]~^_i<I+<+"<<!"~~i!><>!<:-<;Ii>~+>I<!:!I_i"i<~li-:i>!`<><!~?^
                 ''. `i>>i>+!!>'"i,_i>"~+>l^+il>il<i~:~+>lil+i;<i!Ii:-!;l~-~<~Ii;iI!+;I_+i<~!<i<!i;+<l:.
                     "~<>i?<!ii";+;!i<Ii~<>:i>ii>~+liI~i+>>:i<II>i"!;<iI;_ll>~:il!!"!:"!ll:l!;,l>i`!l
                     ^<i!;ii!;:;I<i^;!<^~l!i:<+ii<<`<<iii<i^Ii-,Ii^;<<~""~::>~+<i<I
                     "l",;"":,""^.^`I"'`"":,^''^`^^^;^'^```^:^""`^,:`:","^``"' :^^';,`^"^^","^"':^";.'"^^^^.
                     :~_-+~i_-i<+i<!--~i?_+<_:!~i~i;<+l->~-_-+<<;i~~>-_+I!Il!I !l>,++I<<>i<~~><:~,<_"><~_+_`
                     ,<_-;;i,+'l~<-~+~>~i_+.+?<<~<<<.~",`__il'
                              .            .








```

*Figure from page 20 (2346x3317 px)*


---



4203-E P-177



SECTION 1 DATA SETTING



Setting:



TOOL DATA SET



POT NO./ TOOL NO. TABLE



POT TOOL



NO. NO.



1 001



2 002



3 003



4 004



5 005



6 006



7 007



8 008



9 009



10[@]



POT TOOL



NO. NO.



SET



1l 011



12 012



13 013



14 014



15 Oi5



16 016



17 017



18 018



19 019



20 NA



POT TOOL



NO. NO.



21 NA



22 022



23 023



24 024



25 025



26 026



27 027



28 028



29 029



30 030



SEARCH



POT TOOL



NO. NO.



:SPCY POT



:ACT TOOL



:NXT TOOL



:MAGAZINE



020



007



ITEM f



ITEM i



[EXTEND]



Fig. 1-5 Tool Data Offset (ATC Pot No.(Tool No. Table)



(1) Press the TOOL DATA key.



(2) Press function key [F7J (ITEM ! ) .



The CRT will display the page of "*POT NO./TOOL NO. TABLE*"·



(3) Locate the cursor at TOOL NO. position of the POT NO. for which the tool number is to be set.



(4) Press function key [F1] (SET).



LJ "



will be displayed on the console line. (" u " indicates the space.)



(5) Key in the desired tool number through the keyboard.



(a) Conventional tool Su 1



(b) Large-diameter tool Su 7, L



(c) Dummy tool SuD



(d) For clearing tool number Su*



(e) Planer tool (optional) SLJ 6, P



(t) Heavy tool (depending on the machine type) SL..J5,M



(g) Press the WRITE key.



This sets the correspondence between the tool number and the toolpot number.


```text


                                                                                               .^"^^': "`'^"'
                                                                                   '..''...   ."-]__>-'+Il!>,
                                                                                  :{]~<_<~}lI.i+_i+;_{~!~---:
           .``````^^^^^^`````'''''''''```'''''''''''''''''......'''...............'''''.''....'''''''^' .''`.
           .:::::,""","":::::,,,,"",",;;;,,"",:;,,",;;;;;;,,,"",;;;;::;::::::;IIIIIIIIIII;::::::IIIII;;:,:,:^
                 I~>+I!I
                 ^III,!!
                               '`^'..`'.'^'.'```^^^`^^""^''''''`^'''''''``^`''.'''''`^`'.
                              :,";l++;l~~il_>,,,::::::;;I;;:,::,;lII;,:,"";::;I,^""""Il:::
                             ", ',l_-ll-~<i}>::"'^^^,"^,""`'^`',"`'`^^`;i_i~i+):>!l>i[~" ::
                             ;"                .-'<-:>-``:~_'I+'`<]>;^+^i~>_<>~:<il<i_>` ';
                             :"    .' .        ., `".^:`.',,.`:. "l;^ ,                  ^:
                             :"   i}l'+)!  ']?'I?}^  "?~'!-['   i];.+}:                  ^:
                             ;"   l?"'+{^   -].']]'  .1~ .!1!   I{: ;};  `"^.'"`     ^   "l
                             ;"     Il{i     i:i<I    <<'_(             '_{~:~)l    l|;  `;
                             :"    'iI{-'   .<ll<~    +_,1?^            '}1;,{(;   `{[;  `:
                             ;"    .>;1_.   .~Iii>    <_,}]`             ,:  :;`   .;"   ^;
                             "`    `<:{?.   .-I!!>    +?"[{'            .+_+_l]<     i^  ^;
                             ^'    `+;{?.   ._Ii_~    +?:]['             ^^^^'^^     '.  ^,
                             ^'    '!l)_.   .<:i~!    _<,}_'                             ^:
                             I"    '+l{[.   .+!>]_    _],}1`                             ^,
                             !:    I]]\};   ']i"}]    ?]:}1`                             "I
                             :^    `":I:^   .,` ,:    ",.:;                              "l
                             :"                                                          ^:
                             ;"                                                          `,
                             ,^                                                          ";
                             :`   ...                  ..                                ;!
                             :` `:"^","I^^^^^,I^^^^";l^^^`',,^^^::!;^`'`^l,^'``^,^'`^``. ;!
                             :,   ,i,  ;     `I     :,;lllI;^     ;'^ll:'I."l;^."';:;I;, ;I
                             .;,^.;i".':.... ^: ....""!><>i:` ....:^"!+;':',><;`,^<>i~+i,I.
                               '^;"^,;^';:::I``;:::;`,I:^:,'"I::l;^:;^`,"`;;^^:"`:",,;^`^
                                :;!+l^~I;<-<,;!:~_i:Il"<]I!I!;[],i"i:]],<Ill?_"!;l>??"+
                                ,!lll:i:li<i;;lIi<>;;lI!~l!;il<-l>"i:i+:<;il<i:i;!!<_,~
                                 ....'  ' ...  '   '     .   '  '   .     .. .'  .'  .
                                       ~<-`;,].!_~>l+??!l-}~_ll?~<;><~!-<:l~>II-<';_<~+l
                                         :   ' .`"^'`,:^'^^",'""``''`,`",^'",^',,'.,:,:"
                  ,I^ '>;;;":l:^>lll,`lI!I,":"`
                  ;:, ';Ii>l;i>`;l!!l">iIl:Ii<:
                  `:' ';``''^''`^`'.^^..;^, "::,:'^.
                  i?; ^i!~+l;>i>i>>">+<;_:<:~l<!_,~^
                      .l::`I!i,^:;'l;,II`"I:',:""':;",!!;l^!I;'I;IIl.;:;.;lli,l^"^
                       :;>^III':iI"i><><!"l!:<~+i`i,.!I;I;`!!;":;lI>'Ill."i<<!<;I'
                  "l` ''''",.",` '``'' ^'^^",^ :," .`'^^'' ``"`.""`"'^^' ^  .^.`'`,''`'`'`.`^'`.'.`.''..'`
                  l+; "l!i~-I!<<,<i><!"?^,l<i<'~_i`<<+-+<i:~l<+!!<ii^_+!`+<"__~_!i-~;+~~:+<<___^~;~l!-;i?+
                  .'  .,'.. '.. ^.. '.. "'' '^,`
                  !-I "<>_->l_ii+><,~_~i_,~;+[<!!.
                       :,  ''^;"^^.,"^:"'^"`^'':"'^^"^`"``"".."  .`^`,^`"^'^"`.`'''`'.
                       Ii^:.^<+Ii~,<~+<~_~~:>l;-~:i<i~>+!:!-:";`,''<>-~+?+il+~:]_+~_!,
                  ^,. '^...'.`  .... ....  .  .   '.    . '  '  '
                  <?: ,-+_,i;-+;<]++_?i>+_Ii_><+-;<?><~{<I]-l~+?~+_~<:
                        '                              .       .      .
                    i?l`-~<<___-~<?I~~_"                             !+""";
                                     .
                    >[I^i+>]<l}-+<-[~:_>_'                           i+"",l,I
                    ... '..^  .'  '`' ``'                            .'``  .`
                    I<:^-<<i<~;l>~:                                  li'.l<
                    `^' ^^^^`"'.^`                                   `^^`^"
                    :<,`~l:"!l!!l!;i!i:!;!>!i`                       ;I..'"
                    "I^.':^`,I;:,~::;:';:"Ill.                       ":::':
                    "I`'>:;::':"".,^:;:":;                           ,,  "^`!
                    l>"':;ili`llI"!I!i!;>!                           I!",I!"I
                     ,' "^''..`.`''^''''`^`''"',^''^^`"^`'````^      `'  '. ^'
                    `_:'i+_~_:i><,>~?~~>_+_+I_,~+>;~_<><>>;]-+~      !<,">>"},
                    .  .^    ..  ``'`^`
                    >{:^<>+->I<_,-+_<<+:++<
                     . .,^^.`^"'^^' '''`````'"``'''`^^'`'''^'.'.'.'.'^`'.''''^'.''.'.''' '''..
                       '!>_:>_?li+~:+~l~-?!ii]+<<~:+-_+__>;~_:ii>:~>l+-_"__~!__li_<[__!><~_-_l















```

*Figure from page 21 (2346x3317 px)*


---



4203-E P-178



SECTION 1 DATA SETTING



[Supplement} 1. The symbols"-" and">>" appearing in the POT NO. column indicate the position



of the corresponding toolpot.



-- Tool change position with A TC



» Manual tool change position


## 2. The range of tool pot numbers which can be set is from "1 "to the magazine capacity

(the number of tools accommodated in the magazine).



The usable number of tool numbers is identical to the programmable number of tool



offset numbers.


## 3. For a large-diameter, setting is allowed only when the two adjacent toolpots are

assigned with no tool number or dummy tool code, "D". An error occurs if either of



two adjacent toolpots is assigned with an actual tool number.



The setting of a large-diameter tool in a toolpot automatically sets dummy tool



code, "D", at two adjacent toolpots.


## 4. In case the tool number already used is again entered for a new toolpot, an alarm

occurs.


## 5. Any attempt to set a tool number for a toolpot which has a dummy tool in it causes

an error. In this case, cancel the dummy tool code by entering"*'' code. Note that



the dummy tools placed in the adjacent toolpots for the one accommodating a



large-diameter tool should not be cleared. A dummy tool may be placed between



two large-diameter tools as a common dummy tool.


```text


                                                                                               """,'" ^^'^,^
                                                                                  ''..''.' . .^????!?^<!ll_+
                                                                                 ^[{~>i+~[l;'I++>+l~}>Ii~?-!
           `^^^^^^^^`````````````^```^^`'```````````^`'''``'``'''''''..'''''''''''''''.''.''''```'`''...''`'
          .,::::,""^^```^^^^",,,",:::,"^"^^^",":;::;,"^",::;,,,"^""",^^^`":,::::",:,"","^",:,::,,:,"""""^","
                ;?!>i<~!Iil~'   ^:  `>!:"!Il!,!"^^"'llI"^""'I!IllIllI:,;i;:>ll,;<i'^;l:;I":;!;:lI"i;";::!l:"
                ,l;ilII:"I,l'   .^  ^>~_i+>><>+>,lI;-~iI:ii"--i!!l;i~:,:!l,:;:`,>l`:!!il!:;!il!>>:!iI<i!<i!:
                                    :!:<~"Iili>_>il~l<llii?<>.
                                     '        ,:""'^^:""^."""l,:`,;!';`;;"
                                    ';`   `   !++!Ii<-i[<l_<~_ii"~~-:>,:i:
                                    "I"   `   ?-->i]il~_;>+->_]I+~~_~<i
                                    .'         .             '. ' .                . .
                                !i  "~~>;_>?-,~-~>__<il><i~~<lI_ll>:i+Il_I>_l>;i><l^!"-l__<!~??__>i>I~_~-<-!
                                    I]<i;~i?-~>"~i+~~<,->><~i<><~-+<i<;<<!l~i><i~<<;. ^`'`^'`,l,:^`^`":",^""
                                    :l"^',^^:;,.,'"^";'I,,:,^,,,;lII`"'^,"`,Iii;":;,
                                    ^>i!:i>i<l";:!~<!"~!ii>l!li<>Ill!l_>!+;iI!:~!Ill!>i>i!!>~~iIlii<>i"ii!!!
                                    :_]><!~!<<!>>;,:"`"`::,":,":;",,:"II";,;";":;;l:;>:I:,,I;;;":I,;I;^:";;,
                                    ,!!!l`:::;il;:
                                ""  "^' ''"`'` ^``^^:"' ^":^`.`'.,"`^`"'`^".'"^`''"''^``.'^^''```^''''`'.''.
                                l!  l!<^~;?_[_;-+-l_-?I^-_[>_<ii;[<~_++I<<[:i_<_!!-_;+-<"-_?-<_<l<~~~~?+^-~>
                                    ;<>-_!i>:i+~`l:;i>lli!!~+l,i^_li!>i">iI;il+! >i. <>,>!!<,~<il<!<!_-<_:i_
                                    <_~:_+?+>_>l<<>~<->I+:+~+<><>~i+]I>+:<<+>_!+!>;!l>_<-I'`.^^^^``''^``"'``
                                    ,;"'""I:,,^`,:"l","':';::!:,I^^:I'"I.::::I.::,.";",:l.
                                    "!~:"~>-!i';>`;,~;<!^+ilIi<! l!<">:,;Iil!!~^!i~i!!<~I~~I"_++^i<li!>:I<>!
                                    ;!~_I;+_:>-l<ii;--}<i<_>~<-~I-i:'"`^^^:":::',;::",;::;::'I:;'";"""I:^II"
                                    "I;!: ," `i`;l,"ii!;!I,^l:ii!<:
                                ,"  ,`.^^,`;:``"````.^"^'.:"'^^' .^","^`"^,"'"":"""^,^'`'^^^`"^"^^" ^`."^`^'
                                I;  !l;+~+I>~lI>>II>li+_lI?><_<~:<__>!>![[->:+>-_~_Ii<"<;~+~I+<_]+_^?!:]-<>I
                                    l~><<>`
                                .   ..
                                ~I  >~<:i-~<>~!!lI-_lli<<I!i>_+_:i<,i!<i+<>li_~><;<~l;;<i!<>+Ii<>:i;!;><i>>:
                                ..  !>:_!i<.li!+<Il<><^;<i!i>>~<:>!l<i>l_<>;>i+!!!;_>~<ii!;!<:>>+<`;-!-><~+!
                                    ~~Ilil>,!!;~<!i!<_II_<I<I<>i:<~iii_!i~!i<!_!I?I><+>:>-';:^>!~-,,+~?>lI~!
                                    i<>'>!i>i+`<ii<"+<_>~!">'<~!^++_><i<"<_~_!~i^<i.>>,:>l!^-il!l!!<!~+i>!^l
                                    lii];!__i<<~I:>i!l<;l~~"i!:><^!~~<<~" ~^~<i>>~:_iil<_+;?<l_+<+_!~_-<-_~:
                                    ~_~;+i<~:__~<~_-;~~+];<<:<;i~>+~<i;?>>i>~l+!i".''...`^.''``'```.'`''``'.
                                    ^,^.,"l,'",,^:,:'^:,:`::`,^,,",,,^`;;,,"!';",













































```

*Figure from page 22 (2346x3317 px)*


---



4203-E P-179



5-2-2. Fixed Address ATC Specifications


#### SECTION 1 DATA SETTING

To select a tool from the tools in the magazine using a tool number command, it is necessary to set the



correspondence between the tool numbers and the toolpot numbers.



If an interierence occurs between the tools stored in the two adjacent toolpots due to their diameters, set



the safety adaptor in toolpots at both sides of the tool pot which holds a large-diameter tool. This prevents



an occurrence of interference between the tools during tool setting operations.



Setting:


#### TOOL DATA SET

POT NO./ TOOL NO. TABLE



1 s710711~



14:10:ob



POT TOOL



NO. NO.



1 001



2 002



3 003



4 004



5 005



6 006



7 007



8 008



9.QQ!



101.QW



POT TOOL



NO. NO.



11 011



12 012



13 013



14 014



15 015



16 016



17 017



18 018



19 019



20 NA



POT TOOL



NO. NO.



21 NA



22 022



23 023



24 024



25 025



26 026



27 027



28 028



29 029



30 030



POT TOOL



NO. NO.



:RET TOOL



:ACT TOOL



:NXT TOOL



:MAGAZINE



020



007



SET ] ,m1 i



ITEM t



[EXTEND]



@@J@J@ @J @J@J @J



(1) Press the TOOL DATA key.



(2) Press function key [F7] (ITEM t).



The CRT will display the page of "*POT NO./fOOL NO. TABLE*"·



(3) Locate the cursor at the TOOL NO. position of the POT NO. for which the tool number is to be



set.



(4) Press function key [F1] (SET).



The CRT will display "S" on its console line. ( l...J indicates the space.)



(5) Key in the desired tool number through the keyboard.



(a) Tool number



(b) Safety adaptor



(c) For clearing tool number



(d) Planer tool (optional)



(e) Heavy tool



Sl...J D



Su*



sl...J 6, P



Sl...J 1, M


```text


                                                                                               """:`; "^'^,^
                                                                                  ''..`..'    `-]-?<]`<!;!_<
                                                                                 `}[<i><+}!;^:++<_I~[<li~--l
           ````````^^^^^^^^^````^^^``^^```````````````````''''''''''''''''..'..'''''''..'.'..'`'''''`. ..'`'
           `^`^^""""""",,""^^``""",,,""^"^^^`^",,;;;;;;;;:,,":;;;;;;;;;;;;,,:,,;;;;;;;;::::::I;IIIII;:::::,^
          `~;>ll  '<!><!I~<~i><:l+il:_liI~~l<!llI
          .:^,"". .'`:,^^,;:";l^^,^"';I;,:I;l::";
                ^_";<!<>:!:>!l;ill"iiI:!;<";,I<!'i<>><<li^;i>!l:;!!>,!!i!i>`Ii!i>i<!>.>:i^i>l>iiii;;>^><I!iI
                ^i!!~<~>!<<~>>l!~~>><<l>++l~ii!~;<---+li~!<?~>-i>~i<:iii<~~Il;,:::I,;':^;`;l;l;I!II"l`!!",I;
                ^I;^;Il,,";:"I:"!lllII"':l^lII';l;I!I;^!!l,Il::l!~;I";:,I!!l,
                "I,!`;ll!>;;;:;^::,^:"I!l;;;;^;;,":"I""l",;:,",I"^l:^^Il;",,::;;i:;l^I;;^l"i;I^"l:;:;;:;.,;;
                ;iiiI<_-i><~><+Ii<><i<i+_>~-_!<<i!~<<!>?+i~<!i!<~;--l<_?_~-!!l~<-<!+l<++I_I+>~:;?->>~+><,<-i
                ;l>,<_++~,~!~>>i^l,<<_iI+,i>I>~l:+>~~:~:i>;li<-ii;+!i<,!!!<I;,<<~+^i__l<]+:!<<I !i~l<~~>-!+i
                ,-:;~>iii_<~+"~Ii_->?>_~i_I~-~_+~>:_+<I+>+lI?l~~ll~+li--+<_:++~!}->>~.              .
                `,'"^`'' '.''.' ..'..''.'`.'`'``''..''.``'''^''^".^^.`^`'`;'""^'^^``".
                ;[?{<+~
                      .
                              ^,"^`'`^''`^'^,,""^^"^^"""""":"""^^^^^""::"^^^^^,:::^^^""^
                            .I^^Il[1>i{}+i}_:,,,:,,,,,,,,::::,:::::,:;;,^"""l_:,,:^^;l:"I.
                            ^: .""l<l;<!;,!:^`^,,,,,,"^^"""`^"^",:^"^^:~?i_++(;+~i-<}-I ^:
                            ,;                 -.l~^l+`'`<_^:[` i?-I'-.::"",^:";;::,II' `:
                            `^   '",'",`   ",'",^   .^"'":"    `^"^,^.                  `:
                            ''   l(i.~/>   {{`"[1"  `[_',i|;   <|l`-ti                  `:
                            ":   ^l:`-[`   ;_"^~_.   -< '~<;   ^i' '>^ .l<"^i!^    .<`  `:
                            :I     <;1_'    !!l~>    <_^](`            '?(lI|\>   .~/l  `:
                            :l     ~:[}^    >>l~_    <]"[],            .~}:`-[l   '1-"  `:
                            ,;     ~,}['    ~!!~_    ~?"{{,             ::""^:,    '^.  `,
                            ""    .-,}1`    <il+_    +[^[{"            ._-~_I_>     l,  '^
                            ^"     i,{?'    >l>_~    ~_`]]^                             ^;
                            ",     >,]]'    >lI++    >-^[[^                             ^;
                            ^"    '_l|\:    _>:_]    ~},}|,                             ^;
                            ^"    :<_|}i    +! +-    i_`_]^                             ,l
                            ",      ...                                                 ,l
                            ^"                                                          "l
                            ^"                                                          "l
                            ^"                                                          ^:
                            ": .``^^^"^`^^^^`^`^^"^^"^^`````````'``''``'''''''''``''''. ^"
                            ,; .``^"^^>``^^^,<'^^^^,I^`'`',;``^^`l,``'^`i"''.'`>^^''.'. `,
                            'l.  ,[!  l     'I     '`!__?<:`     ,'"-]!';':~?I.I`~<>_-> ;"
                             ':,"::::";"^^^"^"""^^^^","",,^",^`"^,^",I;",^""::^::l;,;;l;"
                               `ii~iI!,!>+<l;;li<iI::l><l!,Il++l!^l!~~li"!!~~l!"!i++I!.
                               :ii~!'>!l<-~^>~:<<~">I"i-i;i>"+[II,i,_[,!!>:~<`~lll+{'[.
                                ^^`^,. """,,. ,^^":.':^^":.',,:;, ^,"",, ",",;" ,,^":^
                 '^' .;`''''"'."`^^' ^`^`' ..
                 IiI `~!++<l-_,!>+~_^~~~<>l_-i
                  .   '                ...  ``..
                 !}! ^+!_-~:+<<?__;<-_;}I+I~>__1:iI
                 .   ."^`',":"'`"'^^`,^.',`..'.'.^^'.^"^"`^^` ^```` ``` `^'`.'. '
                      !>+:>~<l,->:-_]+?<l?<;~??];!I`!+<<<,+]<;i>+~~'<-~^;-?[~~!i".
                  `.                   .   '`.`.                   '
                 !{i ^!i>+{i!_-:<<~_<"]!-~>;~~+_"!}_:I->_[+~;<>>++l+~+:~]_^i+:!?~>_;+_!i~~;!<+~_-!:<i+:-<
                 ... '+->...  . .. .. .  ..  .       '...... .  ..  .   ..  ' .'.'...''.`'..`'''`..'.`.``
                      ^^'
                 :+; ^>I!>!IiIl+!!"i>l;_;>"i-+i!.
                 ,l" '"";II`I;;;:;.,Il";'I^;I;`".
                     .~>i"!+_l^<+"+>>!>l`~<`i;:_:I>ii><>l~>I`I^'l!~>i-~!:~>,!i<!!;,
                       ."'``' .:`."";^:: ^' ,'.,``"^",""`""^ ^^ `^,":ll;`:l^I!!I;:^
                 !_: "~!I,!^>i;:<!III::;l,:l;!il,;>::";l^lI"Il;i;:;;^
                 ;l^ .I;l`;',;,"lII;!,:II,,!II!i,:!;l!+I^Ii:Ii>l!iiI,
                   ^l: !::"""^:;,"                             I   ^
                   :<! ;ll:"iIli<;                            '<:;':
                   '^' :`"^^ .'`.'^`                          .^   ^.
                   l-! ~_]-?I>__]<<l                          ^-:I^~"
                       '   ..       ... .'..                   .
                   I-!'~i>:[--<<?!~_<:<i~__],                 "[:;`>^
                                '                                .
                   ![+._?]<?I<_~;<~?]i>-?'                    "]"^"[`-,
                     .   .       '``'..``                      ..' '.
                   l+I'__<<>:~i<"                             "_`'.l -+
                   ^:^ `,"":^^"".                             .:`".".:,












```

*Figure from page 23 (2346x3317 px)*


---



4203-E P-180



SECTION 1 DATA SETTING



(6) Press the WRITE key.



This sets the correspondence between the tool number and the toolpot number.



[Supplement] 1. If the tool number already used is again entered for a new tool pot, an alarm occurs.


## 2. An attempt to set a tool number for a toolpot which has a dummy tool in it causes an

error. In this case, cancel the dummy too! code by entering "*" and set.



5-2-3. Clearing/Setting Tool Numbers



It is possible to clear tool numbers set on the "*POT NO./fOOL NO. TABLE*" screen at one time, orto set



tool numbers which correspond to toolpot numbers (having same numbers) on the "ATC POT NO./fOOL


#### NO. TABLE" at one time.

Note tool numbers can not ben set at one time unless the correspondence between toolpot numbers and



tool numbers are all cleared.



Operating Procedure



( 1) Clearing tool numbers



(a) Press the TOOL DATA key.



(b) Press functfon key [F7] (ITEM J).



The CRT will display the page of "*POT NO.{TOOL NO. TABLE*"·



(c) Key in "ATC" through the keyboard and press the WRITE key.



The following message will be displayed on the screen.



Tool table initialize OK? (Y/N)



(d) Key in "Y" and press the WRITE key to clear tool numbers.



Key in "N" and press the write key to cancel clearing tool numbers.



(2) Setting tool numbers



(a) Press the TOOL DATA key.



(b) Press function key [F7] (ITEM ! ) .



The CRT will display the page of "ATC POT NO.{TOOL NO. TABLE".



{c) Key in "TSET" and press the WRITE key.



[Supplement} When an attempt is made to set tool numbers without clearing the correspondence



between toolpot numbers and tool numbers, no data will be set.


```text


                                                                                              .""""', ,^.^"'
                                                                                  ''..'...   .,-]-_>]`_!;_}l
                                                                                 ^[[<<~+~[ll.>+~__;_-<!>--?l
           ``''''``````^^^^^^````````````'''''''''''''''''.......'......'''''.....''''.''''''''...''''..''`'
          .,,""","`^",",""","^"^^`^"":,""",::,,,"""",;;;;:,,,,,,,:,,,,",:;;;;;::::::::;IIIIII;::::,,,,;;III"
                 '-<  <li>i,<>:!_-i>-"ii!'
                 `ll  "`:;I'":^^::,';'";!'
                      ;~+!"~+>;-l"Ii!i<~!i>~~!i<;i<_~~~~"-<ll>>lI!!>~<!,<l!!_<:<l<>i!:!!<<<i.
                       .^`.^,:`""'",``";,^`^,`^".`^"",," ^""'""'',^^":^.:`"',:.,,;I,"',,":;,
                ;-!i><>!;ll<.   ^"  IllI,;;l,;:I!II`l;;IlI^";;;:;^;;l:^I:!,;:;l,^,^:;,;::l"I':l^Il:;"":::,;.
                :lIi>!!;:!:i'   .`  "^:I",;I^:I;IIl'i:Ii!i,:I!I,l:<~i;"i;>;I!:II"l,iiIli!_!>^l<">>l;,;ilili^
                                ""  ^;'`l:^",""`'"^``"`^'''^^^^^"''``'"'''',^'^`"``. ^.'''..^''`.'..' ... '.
                                ll  l_I<?~~~[~<!!-ili~><li!>__<l_l~~~>-_<!i-><>!>]~>i~~<<~+i~~~!ill<+!~~>l-I
                                    i<!~: <;l+_;!~<~`,++>~+;-+,<~<><~I<<~:>i~-:_>,+<]~l<<'i:^-l+;_-;
                   .       .     '.  .           .  . .  .   .  .   '. .. .... .`.. .. '^ .  '.'.''.
          :+i<<!  ^+]_-<~]+[-??+_;?~<I}~>__+<!
           .....'''.'``'^;'``'`^, ```.'`````'' .. ... . .^'``..' '''.. ..' `'.' '  .
                ;<+i~>~___i<<;~~~i<>>;!!<+~<>I_-li!i-_^:~>i<!i->"l><>_,>?~'I+-}>-ll'~>><_I!?I<~l-<~>`+:~;~_l
                lli!i!;<~<i!;~i><";!l!<-<<<<<!!~>?>ili!i~>~i;i~~><ii!<<!>:>l<_<<><:>l+~<,+-_li?>_I+]<;<<++_`
                !]-;,_~]<++;~<l~>;_<>i:l:,,,",^:,I;,^^;"";;,,:,I::I!,;:";`;:,;I::;^l"::; :,""`":".:I:^^";:;`
                ^l:' ";l;;^ i^,;l^I,!:
                :i;>,;:;`,:lll;;^"l,.;l,;!I"!i:!;;!!:lI!:";ill;l!l"I;Illl;I;!;:;;;I!!;ll::I;I;;,:,;II;;",;;:
                l_<+!i~+i!+>i-<!i>~<;><I<i;"i!,i:;l!,;:>;;:!i!I;!i,!lIi>~!lIi!;!l;i>>i><;;i!<<i:Iiii><ili>>I
                ;!!",!!I><ll:~l`>;'+~~i~>
                "l::,;l,""!""""I,:,
                :<+<!~<I_;II!i!i<>!
                  ^.  `"'`'`. '.' ''",^^^'
                 ;<! .i~++~<?l<<<,~>>?_~<;
                    '. '.    ^  '`.'. '.'^`..
                   :?_.>i---l]-I!<+~?"+_-~_l_-~
                    .  .                 ..  '`.
                   :[<.~<+-_;~i+~~_!l--:}i_l~<?-1II!
                    .. ^^`'""::''^```'"`' ^`' '.'.^"' '^'^'''` ^^''' ''` '`.'..' '
                       !>?l!-_i`_~:<?[]--;~-!<-?[I!~^!<~~+;>-~;<~~_+"i}_,"--{>_+<;'
                               ...      .    . .                    .  ..
                   "_< ~_?;l:"]_<i^?<>i~?I>_<I-_-+<]~ii?>>i-~+<I?-l~?]+~[;<+_^
                    '. """'```'.`' '`'`"^.''''^"^'^"''``''^```"''`.''.' '..`,.
                       il~l!-?<_~~-;~+_~+-[:i_:l+,i+?<+--_Ii~,?+Ii~<+?_^
                              ;^^^,""".^";"""`'",,``,,,"          .
                              >>+I!]+-,!_+~>_<,>+l^!ii-!
                   .^^ "`'.`.^`. ...  '.  `  `^^'`^..  .' ''...'.'.. .'...
                   I?~ <~_;>;`>`!_<i<<+_~;~<;~-_+>],<_+;~"<]__,+>~,i<<<+~+;
                       :""'"'";^'"^,`"^`^'"^''`"^.`^'`".'^^'"''"^`^^`'^``'`'^^```
                       <<-:>:^+^:_i<l+>>~:i~I!++-:>~~I~"i_>>-:l_+_i~?!_<>;~~~++_~:
                 ','  " ''. .' '.  .'
                 ![! ._+-+>?l~<<;~i<?->+'
                       '   . .  '...  . ''.
                   I}~._~-_~![_:I<___^_+?_+:+?>
                   ..                    .  .``
                   l]<.+!~~>;_~>-_~;>-~;)!_:<~]-{:lI
                   '`` ^`'`"^::`'"`'``,`` ^'` '.'.""..'' .'.'.... '...    . .. .  .
                       <-_;<--!,-~^?[__?+I_-I-_][:~~^]_<Ii_<+:-_<;_+_+_^+]_^I__1>-i`
                                  .. .  .    ' `' .  .     .     .  . .. ..   ..''
                   ;-i']_-;+;;~_[i<^_<~!<+?-i>?<;??[+_~;_-<
                    .   .` ..  ''   ''..^.''. .` ...  . `^"
                ~-i<~_~>><<<    <+>>I.il !~ill>,I;^l!>-^;:'i>"!l!`;;l><iI;^i<!lIl`!!>illI;<>`III!!iIlI><l;i^
                "",;I:,^",^,   .<<~+il+ll<<~i~<li<<<~~il!<I~<lli!I<~><l!iI:_~>I<_Ii~><<~!^;l';;";I!;;,I!::!`
                               .!>!ii<l"lII>ll`l>l<>!l"ili:l!!`IIl><ii:'>;:<<<">~;;~^>+;
























```

*Figure from page 24 (2346x3317 px)*


---


## 6. Parameter Setting

4203-E P-181



SECTION 1 DATA SETTING



To perform NC operations, for example positioning, program editing, and so forth, data such as axis travel



ranges, tape output code, and others, are predetermined for each individual function. However, there are



cases in which these data needs to be changed in accordance with the change in operation conditions.



The data elements used to control NC functions are called parameters.



The parameters can be classified into 18 types as indicated below.



(1) Display selection {selection for display/not-display of parameter setting screens)



(2) Common variable



(3) User parameter



(4) G/M code macro



(5) NC optional parameter (long word)



(6) NC optional parameter (word)



(7) NC opUonal parameter (bit)



(8) Input unit system



(9) NC optional parameter - RS232C (CN0:}



(10) NC optional parameter - Spindle (OKUMA VAC)



(11) Machine axis parameter



(12) System parameter



(13) Pitch error compensation data



(14) NC run timer



(15) Spindle load monitor



(16) Tapping torque monitor



{17) Machine user parameter



(18) Machine system parameter



Contents and setting procedures of parameters are detailed in IV "PARAMETER".


```text


                                                                                                `^`^', ^`.``.
                                                                                   .....       ^?[++![.+!;-?:
                                                                                  "{}-<+__[II.i-~+-I-?i!<-??l
            ^`'''````^^^^^^^```````^`^`'`'''''''''''..'''''.''.....................`''..''''..'^'.''`^'..'`^'
            `",",,,,'^^^^^^^`'^'`,,^""^`^```;;;;;;;;:,;;;;;:;;;::::;:;IIII;:;::IIII;I:,;;:IIIIII;::::;;II;;;^
           .(;      |?_>><<~>~+<+,I1i<?-<i!l
           .{>.    '?i|??)][11?)(:l|1111[?rr.
                 .'
                 ^-l+__-~>!>?>:___>}?<>~'_<:+i-<<+~;>><-<!>i_:!<!+<<i;i~?+i~.ii<l+;>>__.l-_~:i!~II~,~!!I><l<!
                 ^!i><>:;_<!:l!_>>l<<~~^!!>;!-~>+I:_<I>i>~~<?<~<i-<~>,>~>~I-!_!<>>i!<>i>!_I:~_>i!!+Il_ii>!<~l
                 "~<+?>l;~[_l~i+~<!!!--Ili>!i~l~lll<><~i<~~~<Il>><!!_:<+i!I<i<iii<>;<I!<>!".i>i+<ii!^>>~>;~i;
                 ^!iii:^""iIl!`,li~l^_<~^!><><^>^:<'!!<l_+!;l"!-!i!i?~I~,l++^:i<,+i->-_,~"?[+i-]<i^<~!<_<<>>
                 ^i:,'!II^;l::;::,.":,,,,',"::,";;,":^";:""`^,".^:;^,'^"^"^^,^^'     '                     .
                 ':Il"<!>">>lI>!!l^ii>llI"i!l!l;;iI">i!<!l>;!~i^i_~>il~<i~i+_~<l
                 "~!;";;Il:;lI;^,lI`II'lllIIl::"Il`"!:;::I^^I'":l,:;:;,:;,,^
                 ':;;;!;;I"l;lI",!;'ll"l!l!;II,";i"'i:>+i>;:_":li!<<i!:<<!i!
                  .""  I:""",'^:""";^^'"^,^^"`^^,'.:``"`.``^ "^'^`  ^'''.''.""`'^^:^'.''`````'
                  ^;;  !l<>i_I!_i~>~>!:--++i><>;_!"_+-_?_i>~I__?---:_;~]<?><-]!I-_]<?!<~>--~-l
                  .,^  ^`....'.  .'.''.
                  ,_< .<<+i><~i,<?>?_]!
                   ..
                  :[_  >_-~:-?~[~--[>
                         .
                  ,]_ ._-{-l_~{!l<_+_!
                    .   ..    .   .
                  ;{< '?-l:+_~><?Ii_>+<<__!,?><i:~i!~;
                  '''  .'..^''''^'"^'^''``''"`^; :"^,^
                  ;]! ._~I,>~~ll<:;il!l!>i:"ilI;~
                  ^;"  ""`'l;:""l";;";";;I^^I;:;i.
                  ^i: .i!:";l;:::`,;:;;,;;"^l,:
                  ,:, .;l""~ilIIi^!>l>li<~;,+li
                  `i" .:""".'^,.^^,^^'
                  ;?l .i_~<,iii,+~~+il
                  '"'  "^' '''.''  ...`'"''  ^,"^^^"''^"^`'
                  !}i '__l![--~<]l+_<_<+]_l'`i---_-_;i_-]+!'
                  . '  .'.  .                .       '.  ...  . .
                 `i<]`.][l![-+++?;?]_?>_][>^^_?__-[iI--?~[?-:~]-+;
                           .                  .    .    .      ...
                 `<!<.'1{[_-~_;_+_l>]~-~~_->.
                  . .  . .   . ..  .. ..'''.
                 ^>>?`'[~+_~<:~~>-<<--<
                 .. .  '`'''  `''`..''.
                 ^i<].`++><"~!!l,ii!!>ii<+>!I;-+~"
                 .`',   `"^.,```.":";;,,I;::^^lII`
                 'II< ^+<:"l:,<I!;
                 '"^I..:;'`;"^l,I:
                 ':;; 'i:I,lI`"":,";:;!;"
                 ^:;!..>+i;>~,li~;;!>l>i:
                 ."," .;`'``'.`''''. `.'"^`
                 "!<+. <-_-~?+i~>_<<:~+<_<!
                  '.` .^. '...             .
                 "i!~ "}]_~~~<;<--I~]___+??~'
                  .
                 ">-? ,1]+~-__:-+_?~i!__~?<][];
                 "^'"`'`'.''`'',:`'.'^`''^.```.`.  . . .       ... . .. '`.''.'...''`'.'.
                .~~-+?+_i;->~l??+>]>-i~~_-<<?!I-i_-<]>]?_~!>?~;[???]?<<!i],l__--?}{_<}+];.
                                  ..                              .                  ..

























```

*Figure from page 25 (2346x3317 px)*
