# III SECTION 2 PROGRAM OPERATION 06. MULTI FILE TRANSFER (MPIP) OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-06.-MULTI-FILE-TRANSFER-(MPIP)-OCR.PDF*

---


## 6. Multi-file Transfer (MPIP)

4203-E P-248



SECTION 2 PROGRAM OPERATION



The MPIP command is used to transfer multiple part program files at a time using the RS232C interface.



The following sub commands are provided.



Item Command Function



Multi-file read MR Reads multiple part program files from an external device



and stores them to the memory.



Multi-file punch MP Outputs multiple part program files, stored in the memory, to



a tape punch.



Multi-file verify MV Verifies multiple part program files, in an external device,



against those in the memory.



Multi-file transfer end Q Quits the multi-file transfer mode.


## NOTICE

: During file transfer processing, do not turn off the power supply. If the power supply is turned



off during file transfer, the contents of file might be destroyed.



6-1. Multi-file Read



The multi-file read function reads multiple part programs from the external device and store them ln the NC



memory.



The operation procedure is indicated below:



(1) Press function key [F5] (MULTI PIP).



MULTI



DATE DIR



PIP EDIT PIP LIST CONDENS [EXTEND]



"=MPIP



>" is displayed.



Press [F5] (MULTI PIP).



The function key names change as indicated in item (2).



(2) Press function key [F1] (MULTI READ).


#### MULTI MULTI LULTI

READ PUNCH VER I FY



Press [F1) (MULTI READ).



"MR" is displayed on the console line.



M-PIP



QUIT


```text


                                                                                              .^^^^'" "'``^'
                                                                         ....''...   .'.   .  ,]?_-i? ~I+-[;
                                                                         ~1-<<_+_?l+.+_]~-]---[;<-_-_-_~<~[;
          .^```````^^```````````^`^`'''''`'``''''''''''.'''''''..........'`''..`'''`...'`'`.`'`.`'.^'''.'``.
          .`,:::::,``^^``^''`^:,"""^`^`''";,^`'^^'`";;;,:::;;;;::::IIIIIII;IIII;;:,:::;III;I;,,:,:;IIIII;::'
          :)`     ,|)l<[?,?{-~.~]!<ii!~]>i.![[{[+{[;
          :|l     ,\1[[]}i-}{|^l_+|1]))1\?'{|/|+[(-[ .
                .'
                I~~i~)-_-:+-~<~?~+l~l>-?->_;i__~]]I;_>][-~;~-~i>i_++_!i[_<:]I<!><_"i-~+I_+Ii[-_~--!l+_<-+i<.
                '^`'``'. .`'..'"''.`'^`^^'`.'`'``^'.`"':^``""'"^`::^^''^"^`,'"'`^"'",^I,^,^'^":":,``":,";,,.
                ;+~i<_]~+-<-;+-<,<~i>>_<_-"?~I<ii>~+~>
                 .!I;I;IIII<!II:,:;;;;lI!II;;lilIll!ilII;:::;;I;;IIII;;;,,,,;:::::::;:""":;;;;;;;;:,,,::;:;;
                 ;~ '..' ..l{__;'''````';l?_-_+~{_[!!.... '''`.'''''..'....^?<-<[]_!''.'.'``'``''`''''``^^^[`
                 I{]<~-!_i:!!>i^^",,,,,^!;""I?--I::l+~ill>:liI~ii!,II!,II;;IIii+><!i;I::l;l!ilI;I:I;:IlI:::[`
                 I_>l!i^>>^!i~l         ;^  .+>l   `i~[[-}>!~>_|__!_}<i]<-1+-<I~~~:ii<ll+:i~~~l>?;__<~~i   <'
                 l_ .. '       .''`^^^^^<:``'  .^^^;_?<+:++<-+l-_~~!?:<_!l<<>~_->                       ..'-.
                 ;{|[}{+|-!_i+++^'`^^^^^l"'',11-"^^:<+~~_l_!I<i-+-]l~?_l~<<_~-~!{[]i;]~<+_<+!?_>!~+~>>~l>+,}.
                 l~^"^^.^"^:^`^`        ,.   ,"    .;<<}]_>~l~<]!:;`:;"`;";<:l"',II"'l:,I;^:',I,',l:,:!,`; -'
                 ;_:"",,:,:,:;;,::""""""il::;:;:"^^:<~l-?~l_~<i<,'.'..``^^`'``'`'  `"``````''. .'.'``''"`'^[.
                 ,+1~[-i?-:_]<}I..      :^..^)[<.. ^I<->-~?;i!<~~}i>-?i!_<]?__ii1--"-!+}I?-{-<_-;-]_-]>`''.].
                 ;I                   ..!^..       `l-]?<_-I-~~?!!l_[_:??--_~~'  '`...'` ''``.``.``''``    ]'
                 ;__!!<!-!l>!i!il,II!I"^_;^"^,i"`^^l+?[__i~!lI>i<l<_><><~~ii;~I;i;"""""^`''```^""""""``^^^^}.
                 :_]_~?~{?>]}]{}]l-~?!,,+I,,,![:^^^l~_]_1<??_!+~]i~}+>[{-][[l_]-[],""""""""^```^^"^^"""^^``_.
          ",`"::;,I,;l"`,,,"^^^^,:",":;:,,:,,,"",,:::,^"^"^"",",^""^,;"""",":,",";;::::::::,:::::,:::::::,,"
          ~,/1{[{)[({"i.i'!->_++i?_i_~<~-_:<>~<_~~<+!^-l!>i!i<il[_<~>!>i<~I!~+~~~^>__<l!i<~+l>>~<~I!i!l>~<-;
          <,]-_ll_+-~;i`! "<>ll~!I;;<Il!ll;+;"~>l;I>~:il;:!;+!^;i;ll!!I!<iII!><il ^",:";:::;',;!ll:,;";";IlI
          '`  ''`.. .".^i^!_!>__-?]l]>i<_<][+,]-+l_<~]+_+l-!?]l<+1_l>?;~]-{+_]--`'....'.'...'.     ......."i
          .' '    '`. `.":`':,'''"`. ....''''^'''`......'`'`''`'.'.'..''``'`^^''`````^"""""""^`````""""""",'
          <],+'   +(-?1!~-];-[[[}]
                `'  .. ' '.   .'`   .
                li~l!>!->[]I~-]>><i_}+>l_-+]!<~_1__<~__~-<~->->~i+<+!_-<>+__i~-l+-<i_!<<+<--+~i-+_>!!i_<~?_"
                l<_~i++,  .  .'  ' ......''...'''`''`'.'^.`".' '..''..'''`'`.'^.``''`'^'`'^^``'`^^''''`^'``.
                ^""^^^,'
                !~~:!_~<-}~<;++~+_-<<<I~I~-?>__+!~_~~_:
                  '.`"`..'.. `..''`'...'..^''`'` '`'`^'
                 ;i: "_!><ll<!!<!i"><!;]<?"--!<l~:i+~:
                 ^^` '`^::,':",,,,',;;":^!"I:,;"^^^:""
                        ^                                                                   `'
                        I`                                                                  :"
                        ;'    ^^'`                                                          ,"
                        ;'   It~Il                                                          :"
                        ;' '!i`'`'`^``^^^`^^^"""^"^^`^````^^.'^^^"^````^````````^^^^^```^^  :"
                        l' "-  . ''!'.   '^!''..'`:;'  .''i`[\l_i^i`'.. '^l      ,i`... .'  ,"
                        :: `^<<>i  ; `>ll .; :ii" ^^ ~iI" l ~+<`. ! `"Ii. l!i_<++I:'ill><l^ l^
                         ::i;I;,;..:'`;:,.`:`,::`'"^.lI,`.:^"":. .;.":II.';I!<><~l"^~iIi_+!:,
                           >^:;;;!l`^I,:;!:'Ii;:;i^`l;;;I;':l;:;l"'I!I;;l^`;"",I:^,l,,,:''`.
                          .:"!l]_";I>"_+?`<:<^-~i"!l:i_{`<:+`-]<`~^i;[}!,!l;<-_^_;i"-??^-
                          ",`l;ll;l;!l>>-,<,~:i<>IlIl!i_"<,<:<_+,!'!;i~I;l:;!l!^<,i:i>~"-
                          :""-?<+^.  ''`'^. .^```^  ```.`.  ^'~+:l,Il;l!:IIIlI;>!`."`''^
                          l^l~_>]><~<>.                        `;>~_<ii+l-_i<i!~<i.
                          :;:":,;lI!II^
                     .`
                     ^~_-l+~~-+_li_-:>->~]>;?~?~}~l{ll+[+~}__i_;-_~;i}!
                           .      .'  '....  ..'". '  ..''``'.'.'`..`^'
                 ~[" I+<~-liii<<i>;-+i,?;~;}{~<!i:_[<-~!
                 ^^. ..'^"`.^`^`^`'^""'' "`""^^''.`"`^^"
                       .'                                                                   `
                       ^I                                                                  .<
                       ^;                                                                  .i
                       ^I   `?\;~'                                                         .I
                       ^I  '"1n:....     ...    .''''''..........  ...... .          ..    .;
                       ^:  ]?{i>l^I;!_;l!^!;]<Ii^,l,,,,"^:l^^^^^^l;^^^^^"i:~ii;i^l^^^,"^^. .;
                       '; `,I1->> ,`~)+<! I,\[ii;.^      `;      ;,      l.]_>il l         .l
                        ;:!` ;]+_."";i?]i':`<<iii"`      `:      ,^      l'l_!l  :        `l^
                         ,<"""'``,""^"'`^"^^"^^^:,"^:""",^^","","^^,,"";"^^,"^^,"::"^^,",::'
                         I. lI>>l:I`<!+<!!";li<+Ii`i;>ilI;"!i-_;i'Il>~~;i^i!__<lI"!!<~Ii^
                        `l  +`~!i._l+"<?;:!~^<![.-l~`~-<^~!:I+{'>,~`~_) -l<^-!;^]l:i+)'~l
                        l'  'I::::+;iiIlI; `I::;;" ,:`";;' :;,;I; ^I,":;: ;I:;;l`.l,",:I.
                       `l',ll'"`:"";:ll""`' ':""`;,`^l"^"`;;":^
                       "::<__;<>+--?--~.'^,,l>~_>-li~}+_~l~?~_~^
                     .   .
                     ^[--Il_:]?-+_~-_;~;+_>:<_+~>-;<<_'
                      ... .`.`^"'"^^`'`.''`.^^`^`^.'`".









```

*Figure from page 1 (2346x3317 px)*


---



4203-E P-249



SECTION 2 PROGRAM OPERATION



{3) Following ">MR", enter the file name of the file to be read using the keyboard and press the



WRITE key.



The machining programs are read and stored in the NC memory.



While the program ls being read, "M-READ" and the file name are displayed at the upper right area



of the screen.



After the start of program reading, "Valid information reading" is displayed on the console line.



At the completion of reading, ">" appears on the console line.


#### POOGRAN OPERATION M-PIP


#### BOX-1350.MIN

tile exist overwrite? (Y/N) !Y



varid information reading



MULTI



MULTI



MULTI



READ PUNCH VEfl I FY



{4) Press function key [F7] {M-PIP QUIT).



MULTI MULTI MULTI



READ PU/\tH VERIFY



">Q" is displayed.


#### M--READ


#### M-PIP

QUIT


#### M--PIP

QUIT



Press [F7]



(M-PIP QUIT),



The function key names return to those as displayed in item (1).



[Supplement]



Command format



>MP <input-device:><input-file-name><,<output-device:>><;option>WRITE


```text


                                                                                               '"^^`^` ,.^'".
                                                                          '...'...    .'.  ..  i}-]+_~.~;]+{"
                                                                         .]}+<><~[~ii^-]-~-??-}?:+-_?--~><_]`
           .^^^^^^```'`````^^^^``````````^``^`'`''``'''''''''''''''''.''''``'`.'`''``'..''``'```'`''^'`'.```.
           `::::::"`^,,""`^"""":,^^^"::",",:""""`^:,""^:,:",:,"::::,:,"":;:,::::,:"^,""::::::,^"""::;:::;:;;'
                  ;?l .<:~IIill`^!-]+`"!!<l,>!">i":lllI`!;<l,i<,;,"!""IIl^"II;"!i::l;II,I:;";::,:::,^l;'
                  ,!: `~_[__]!]!:;!l:`,l;iI^I!";!,:i!ll"!:i>;I<;;I:<;,i<i"l>!<>!>i;<~<i!<!ll>!l<!><i:i~"
                       i!ll"I'l><
                      .I;:'::I;;:lI:"I::;;::,"I;^:::;";,:"l::,:,,,l:^ll,",,,"""`
                       ":!`;!>l!I!l~;!I_<!Ill:~!^;<~I:~;;I~!i>lII,>>"i+::l~l>ii!
                      '>>l<:l;;^;,;;lI"":,I;::^:Il".<l"<>;ll^^;::!;"Il^^;;":',:":i;;l:";,::l;,'",":^:,I,^:",'
                      .~+_-i!><++<_iii,:l;i!;+I!>~I.>i:i~l>!`!>!l><iI~!;~+l~;<>!!_-~_-i~;<!<ii:--<<:i]-!i_>_,
                      .!,!>I"i;!>!'
                       I!:""l,',::,^l",""",:"^,,,I"".":::""";"""":""'`""":^^^^'`,^^^`'`^.`',^'.''`'`''^''
                      'i<<;,<<">~_:;>!<;_<!~:"<~+~!}".i_<i;i+iIl<_>i,,~_+~i?`~li?]__]+->!+:-]il+>+___;?++
                      .i,l!;.":;:;Il::.I":;,II"`.^^`l:,",,"."`;;"."",,":':":.
                      'iIl>i"!lI~!iiil^>"l~<<!<< :^`__+<+i!,>:!<i:>i!~>~:>i~^
                               ..'.   .'`.    .'"^``..    .`'`.     .   ''`'..''. '.```'
                             ^l"II-[}{}-<[}]_~?~:;::::_+__l;;:I?<-+<:I;;",":+~lI<-!><>::;
                             I' ",>-]][+<-][+>?_::::""]+>~,",:l)~[[~"":i->_+tn_-\/1tu|; :;
                             !                                        '!<!~i:i;ii,>;_<" `;
                             l                                                          `:
                             "                                                          `:
                             ;                                                          `:
                             ;                                                          `:
                             ;                                                          `:
                             ;                                                          `:
                             ;                                                          `,
                             l                                                          ',
                             i                                                          ^;
                             ,                                                          ,l
                             l                                                          ^;
                             <                                                          ^:
                             <   :l^."l^":"                                             ^,
                             i   ?[]:-)>?>_;:;^"; ` ,:<''I.                             ^,
                             !   I>i+!!~_I[}<[>:{~+l[I!'.,                              ^,
                             !  .;:','^:^":"'"` ^;:,l` .'...........''....    ..''....  ^,
                             !  '{+ll`!;_+I!^;l{ii"."`^`"":i^^^^^;:^","^I:_>>+I;,,"^^^' `,
                             I`  :1?-',^_({?`,I|[><":     ."     `'     :.[->! :        ;"
                             .:,^.Iii^"^"lil^"^I;:,""`^^``",`..''""``'`',`I!,`':'..'.'":,
                               .;llI:;';II;;,`I;I;I"^!i!li",!i!Il`:!!ll!`,;:Il!':II;l;`.
                               '<;}>'<l!;{[`li;~__^-i,+?<">_"-1!::l^-1lIi>"]_:!!i:](^_^
                                ;lIlII`Illi;:^lI:I;,"lI;;I":I:;!I'";;lIl^;IIlIl^;;;i;!.

                 .i~' !~l!>:iIll<!l,ii:l<!;:-li<+,!~;!i"
                 .;l' ^^:Il,:;:;II:^li;:"",:i:,:I'Ii;:;:
                         .                                                                   `
                         I.                                                                  <`
                         ;                                                                   i'
                         ;                                                                   I.
                         ;   .li                                                             ;.
                         ;. <_[?ll",!;~ili:I;!l:!:,;""""",:i::"""",I",,""":;:;;l!:::^^^",:^  I.
                         I  !")}i!`.:^f?><',,[{<>l.;'      <      'I      ^"I{i~?^:"         >'
                         ";;, '[_[;.,`~-1-""">[+!~;:'      I      .:      `^^}<!` ,^        "l
                          `_,,,""",`^`^"",,,,,^`^^":""`^",",","""^^^^,,,"`^^^,,",",^`''`'^:;,
                          ,, ;!i>!I!'!!~<ii""i<~<l!'!!+<>iI`iI>!;i',i<<ili'll!<~iI`iliiIi^.
                          !. _`]>i -l_^}]!^>i^_~].-l].[?-.-!!;[[`l;~^-]) -I+'?!>.]ll;+\"i>
                         ,,  ^l;"II: ;;:lIl`^!I;lIl.II,,:I:'!I:lIl'"l::!Il'II~[,:".ll;>l!^
                         l'`,'`':^^```'                                    .:;<lll^I;I
                        `I,i_I+i]?-?_?<.                                 ';;` >}_1]i?]l!'
                                                                         Il^^^;I,,:"llIl;.
                      ";^'"``',``'^`.'`'`''.'`'''.`.^'... ..'`..' ..'..''   '.
                      ^<_l!<<<?~i:-]<:_-i<_:i_<~!;-;+~~?>l[l>]{__?~_ill~[<~;i<`
                ,]<<>+!;ll;_^                                    .
                ^lIli!!I;l:<"...' .. .
                   <!"l<!>!l-~_l_~<>]! :ilIII!!!!!ii!lllll!!!!!!!!!II;I!!!!!!!l;I;Illllll!!!!!!IIIl!!!!il
                   {.  ."":`'``..`.^`'.'..''.''`"'.'.'''....'.`''''`.'''''''''.'.'.^^"^""^'''''''''````,)
                   ]   "_}-,:>-?+>!{~~~+:I>~-<+!?-I>-><+;I,l<_]+_><}<<<i,;;;l_-_iiI>?__l]!             .1
                   ~i!lI;;:li!iii!!!!!i!llIl>ii!!ii!!ll!ii>iii>>>lIIIIiiiiiiii!IlI!!!l!!!i!!!!lIIl!!!!!>[
                                                .       .. .... ...  ..............'''''''''''''''''''''












```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-250



SECTION 2 PROGRAM OPERATION



(a) input-device:



TT:, CN0:, CN1:, CN2:, CN3:, CN4:



If no input-device name is specified, the default device set for optional parameter (word) No. 57 is



selected. (If "0" is set for this parameter, CN0: is selected.) ,



(b) input-file-name



Main file name: Alphanumerics (max. 16 characters), beginning with an alphabetical letter.



Wild card<"*"·"?") can be used.



Extension Alphanumerics (max. 3 characters}, beginning wrth an alphabetical letter. Wild



card("*"·''?") can be used.



(c) output-device:



MD0:, MD1 :, FD0:, FD1 :, FD2:, FD3:



Default device is MD1 :.



(d) option



Y: Unconditional overwrite; if the file of the same file name to be output already exists in the



specified output device, the file is unconditionally overwritten in this operation.



[SupplementJ 1. If the text (tape data} read from the input device does not agree with the specified



input file name, it is skipped and not stored to the output device.


## 2. If input file name is omitted, input file name of"*·*" is assumed and all read texts

are stored to the specified output device.


## 3. If available space in the output device becomes full during reading, an error occurs

and communication is shut off. In this case, the file being read is not stored.


## 4. If the file of the same file name already exists in the output device while no option Y

is specified, the following messages are displayed on the console line.


#### A.MIN

file exist overwrite ? (Y /N) !



If "Y'' is input, the existing file is overwritten, and if "N" is input, the text to be read is



skipped and the next file is read.


## 5. If an output file name is specified, an error occurs.

5213 File name, error 11


## 6. If the read file agrees with the file selected for DNC-B mode operation, the text to be

read is skipped and the next file is read.



5226 Main program file selecting 'A.MIN


## 7. If the read text already exists in the output device and if it is protected, the text to be

read is skipped and the next file is read.



'A.MIN File write protect


```text


                                                                                               '```.^'.^.`''
                                                                                               <]-->[!"+;]_<.
                                                                         ^}[~i~+<?i~^i_?-+_?-?{<I-_[??_<++__.
           .''''''''`'..'''''''''''........................... ...........``''.'`''`...'^`^```"''^.`^`^`'^`^
           ^",;;;;;;,^""^^^":,,:,,:::::::;IIIIIII;II;I;:,;III;,;;:::::;III;::::::;;;III;;;,:::::IIlIIIII:::,
                    I>``!;;!"il:Il"
                    !<^^li!l"!!;;l"
                           I!: !~+>`,+->I'l+++:'i~_~`,~+~!.
                           `'`.^,:".'",^'.`":;^ "^:;.'::;"
                       "i:>,!i!>,l<Il>;I!i!l^l"<!i;<ii",i!,>i<l>>;~lli!:<i!<::i<il!<:i<!ii>~+;:<!l!il<I.li;!.
                       ">>+!<+~:l-!_>i<;~<!_Ii<-ii>><<il__:i+_->I>!<i~><+~ll`"l:;::l"l!:I:!l!",l;::I^I;':,`l.
                       ^il!IIlI :; l^^i">l"iI"!I;!<ii>!>~~,"l!>:^>^~>i!>i!l'
                    ;:''^''`^,'`^^"`'
                    +-,"iii>l>i;l_l<!
                       ,_i!"Ii:^llI;"  ^i:;Il,,;II;I,.I:lI  lI ;;;,:;!;;; ";;I;:I::.:l>'^I^'l;::!,II"l`:;l:^
                       ^!!!""I;`l>Il:  l1)_~?_?+__~_Il[_-?l,_];<_}_}!~!ii.:>~-!!i!_'i~~^;_""_-l<-i~<i-^i+~+;
                       .               "<!>";<ll,`I'.`,:^;~!,_!,>i>l
                       !?_]~+]__"   '. :-_>>-!><++~+il>-};^~;>>+><~->],i--[?+-~_!-_~l]I<1_~-[-[+-<>?[-i.+[~-`
                                       ;_]<!!l>"`>!l!]?l_]l<[-]l.'.' '. '`^....".'  .' '^'.'''''`'.`'`' .'.`
                    ",.'"",^,`,"^""^   .''......   ..''..`.'`''.
                    <~^,<<-!i,<~!l>l
                          .i>II.'>l:I."<l!, ll;:."lIl".illI.
                           i<I!``<i:;'";Ii;';!l;^:li+I^!!<~'
                       l><+;Il"~I;:;`;,+i,:.
                       ":;;lI;:iIIll^I"il,"'
                   .;>'':::"^
                   .i+`"~>>!:
                       ,I  "I;:;;;<!:;!,,;l;Il!!';;i;^i>,"lIiI`:;;;";>:^;;:;^;^,;`,"l,:,,I:,,l`"::;I`:`I,"
                       ':. I<i<i+<+>i!?Ii>+<<~><"~!i_il_l;>!<_I_]<~!!]i:~_i_I-!!_;<<}_+l~~>+_]!!<i<_:i,iii
                           :<~~l>~i:ii_>~:i_!i~l`~~:i-:III!>!<<_+!!i-?;li<i><<_~IliI+_I;_+i<?i~,
                .,'.'''''.'`        .``. .   .. .  .      ..'   ..       .                    .. .      ..
                ;}_-[__~~->],   "I. li<_i!_~Ii__~l<[_]I:~+_l~>>!>_<:<-ii;?~i>-"~<+~:i+;<?+<i:?]_:?_I~_~~-]_<
                                    :~-<<l]i;<+~?:l>il+]_~~<<I-i~;<+;-_>>~l+;<+>;><_i~:?[>>+:'.. .'.'`''..'.
                                     `,`' `` `^ ^..''''^,^`^^.,'`.`^.^^``^.^'."".,^;^` ,"``,'
                                Ii  l!:!I!:li^;iIlI":`l;!>ll.l::I">!^:lIIl"!^:^';'l^;!!::IlI"!I!,<l:!!!ll;!;
                                ^"  ;!ii+_li+l<<_~>:<!~i?++>;i_~~Ii-li+>;l"I.",":.l,li!!;lil">;l,~::><!;ilil
                                    "!!^!!l>i,i^!!l"~<!I>ii,l>__>I;>!l!<
                                `^  ``.''^'''..'..'.. ^'   '.  .`.'. .. ''''''`'''.''..'''`'.  '..'...... ..
                                ;i  ll+<----+!>-___ii;__i!<_-~>>{<+-+l-~!!!__;<_:~+!i]!!_~-+_i:-;ii!<,i<~~<>
                                    l+>>;<>iii<>!~]~+l!!!_i~:~].:+:-_<:~_?!^]_;+]l>?i<_:~~~!<>;~~I?>i<-: .
                                    .'.  `   .' .'. ' .. ... .   .  .. '''' '`  `  '. , .`` .. '..`'''`
                                Il  !<~>I<+;IIi~l;~<lil]i,!<li:!~l!!~,!!>>!:;:~!"!!_!!:~iIl!"l~i<"I!"li~>!:!
                                .'  l!I~>i~->>"~_!i~<~i~~!I~i<i><><<!<<ii_+i<i>~il<<]~li~i><!~!<~!":`:;:;"'`
                                    ,;">II;:;I':II';lIl!;~I;l!i!>_!!^il;:i~>i~!!I"I^!iI"!:l!li^IIi
                                         !^~<i"
                                        ^]<i<<i;`,":,::I","";:!"^.
                                        .i>^lli<`Il>I<;>l'`:Il~l`
                                    Il"!^:'::": I;"`:";;^;"!:`,',;l;IliI;'^;::l,lI^;";I:;'!:";;::I^::`"::,""
                                    ll"I^+iI?~_l_<!!+<_+<]l><I~l>!<l>!><l^;illl`Il.<;!-<>">!!l+<I<Il~:l~~!li
                                    ;i~_~<>,+i>l+<,I~~I:?!;<^<<_l
                                '.  '.     .   '              '  .  .  .
                                >l  <l+<^>i}<~l_?;<_~++;~;]+_~[-_l"}!>]!-I!_~~i<`
                                        .:"",'     ;"`.''`"` ''``.^`    .  ... .
                                        `?~;+^    '>>_:>_i_+'+<i+`!;
                                `.  '``.     `' .       .  .  .      .  .  .... .
                                _!  ii>~l>++i>+!<}-~+~;+-+I+~![-l+++<<<<~->~_[?;[~i~<}_l++-+]~_II[_i]-_~<<-i
                                    I<~_l+:~__>~+>i_~i~_>:~>+;-?;+;!++~` ..   . .. .....`'..''....'.`'..'.''
                                    '"""'"'"";"""'^"^''^^.^^" `:`^''^,^
                                        ^?--]'     -]_>"<<<_i_<"_-;>+_~++<+^-!}[?l
                                         .  .        .  ' '".`.  '..''`.'." . '..
                                l:  iI><:;<i!><~l>_!>>i,lilii:I;>i:lI>;i:>!i!>;i!ii>!l!;!!~i!>!,:<!;>il!I;<I
                                ..  Iii~I>!?~>~<!ii<~~-<il<<~l-i;<;<>~~;^;:,,;"I::"""":;::II:I;"^:I"ll,::"!:
                                    :ii!"l`i;!i!i,Il:";;; !ll"I!`;:l!!i
                                         !:!><:    >l!'I;i:`;,l;::
                                         ;;lll;   .:;i^i;!!;i:iiI:

















```

*Figure from page 3 (2346x3317 px)*


---


#### Example 1: >MP *.MIN

4203-E P-251



SECTION 2 PROGRAM OPERATION



[WRITE]



All files with extension ".MIN" are read and stored to MD1 :.



Example 2: >MP BOX1???.MIN [WRITE]



All files beginning wi1h "BOX1" and with extension ".MIN" are read and stored to



MD1 :. Files such as BOX1001.MIN and BOX1002.MIN are read.


#### Example 3: >MP [WRITE]

All input files are read and stored to MD1 :.



6-2. Multi-file Punch



The multi-file punch function outputs multiple part programs, stored in the NC memory, to the punch



device.



The operatlon procedure is indicated below:



(1) Press function key [F5] (MULTI PIP).



=t.FIP


#### WLTI

DATE DIR PIP EDIT PIP LIST CONDENS (EXTEND]



"=MPIP



>" is displayed. Press [F5] (MULTI PIP).



The function key names change as indicated in item {2).



(2) Press function key [F2] (MULTI PUNCH).



MULTI MULTI MULTI



READ PUNCH VER I FY



Press [F2J (MULTI PUNCH).



"MP" is displayed on the console line.



M-PIP



QUIT


```text


                                                                                               .'``'`^ ^.'`'
                                                                              .                l]_[++- +;}}!.
                                                                         .?[+<i+<[+i!^---+_[]?}[;_-]]--?+~+[,
           .'''''''''''`''''''''''''''''.''''''''''''.....................`^''.'`'`''...```^`^^^.^''"'^^'``^.
           '::",;;;;;;;,"`"^^^:::;:,"":,:^",::,,:::,:I:;:;IIIIIIIII:;:IIII;::,:;;::;;III;;;::;::lIlIIl;;::;,'
                      .<;!lll!,,^ ^!++^,`><~:;<<>l<<I
                      'l;>ll<i:^" ^:>: :^!lI::!l;,,!l
                                  :l`il;^"l!`::;;:I;:,^I~>i,^lI^:III";:;"!,:::,,"i>;:.
                                  ,l^!ii,l<!"i<i>;>il, I<!i',<>:l~+i;~>iI_>i~!;>:--!l`
                      ^]>-_~?]l~I ,_[+^?+<+Il>i:~[_!>[+~<!_~
                       ``^``,^'`' '`^. '`'.     `^''^^^'^.^,.
                                  i?l~-_:>~~+li>i!;<]:^?>>~l""+;i;~?>"><<I>!li'^_~+i.<>:"!!>:<i~:~<i!>Ii"
                                  ](-~i"l-[(_i_~{~<[i1_?]+_[<l{}{~~]-<[1][-_{}ii|}]l~[~>~]}i`I:;`I;;:;^:^
                      .` ....' '  "lI;^`^";l;:;,".,;';,^,^":,`";,"";;,":":^"I;;,l:,^>:""lll.
                      ,]<?_+[{l+I ,[{?:{?+_l~?:
                            .     .'.     .   .      .         .   .'
                                 .<}!~~~~l[?+:__<:[-?!?_]l?_~+->?I-)-i:.
                                      ...  .. ... ... '.. ....' ...'. .
           <?l].   ~(]<1l-[?:-~+~<_~
           ^,^,.   .:,"".`",''.;`"^"
                 >><`^!;];i+:"!II>l"~i!<!i:,!<~l~!`iI>+i<,,i!I"!Ilii>!!."<ll!i^l'il:,<>":!III;I^'l'!lI`l:I;l'
                 !>~i!<:l""l""I;:I,`I;;I;;^"ll>Il;':;Iiil":!l":l:>~!i;!`,ilIil`I'IlI^i!^,!iIl!il'i'l!i"+!!i!`
                 l!:!il
                 IlI`":il!>Il"!IIIlill::;"I!ll<!l;;I!;l`
                 ",I";ilIllII">:Ill!!I::I.:!Il<i!"lllI>`
                  `,' 'l"^^'^"^^,^^.^^'';;:.;;``";`;:;
                  Ii: ,>i~~!;~i>~~>:<+<;<<]I-?<i!>l>+>I

                         I.    .                                                             i.
                         ;                                                                   >.
                         i    ,?Il^                                                          I
                         >    <}:l'                                                          I
                         ;. l_l'^`^,I::,^^^::^^^^^^;::::,::I^,"^,":l,,"^^^,:^"::,^:,,:::::^  ;
                         ;  !, ''..^<..... ;; .... l^...'..!.t1i>"`<.. ...;I   .  :^....     I
                         ;:':.{~-, 'l !>~; ,, ii_' , "{!!^ l.~i~   : I,_> ^<-}{{1-: >++_[}<'^!
                          ^+l":""""":^""^^^,"'`''''^'`"^`^^:`^^```":^:,,^'"":;I;:,:`;I;;li!I;
                           l."i>~<il'I!ii>>,`!l!!I!':iill!I'!l!iii"^>!ilI!`;ii>>!,'!IlIIl`.
                          :: <^_~< <:<']_<'<<;i~]^il~'?_} -l~^-[l"!I">]('~!~'[!>.[III-);;>
                          l  ^ll;ll!'llIi!l:^!il>l!`;lll!;l`il?~!!"^!iIi;i^!l!llI!`!;;<l!:
                         "l'"^`'                             .?.                .    . .
                         l,i}-_~"^^""                        :`^,""',:^^:^`^'""^
                         ;:":Il<~~-++.                       I,i-++l~~<<]__~i+~~^
                      "+iil>I!_!>"<<!"Ii!ii;:i!ili;:>";l<l!~iiIl^<!i^;<^
                      .^:;^I";lII`;li`:!:I!:,:ll!+:,i",IiI!iil";^!il^li"

                 ._?^ !_~-?l>_~_}+<I__!+[-il1?~_i!>-<]?___^
                  ``.   .'`'.^'```'.`^``.'`'`'`^'...`'^`'^'
                         ;                                                                   "
                         !.                                                                  I.
                         I.   .^'`'                                                          ;.
                         :    +X<>,                                                          I.
                         ;  ^>~xi`^""^''^``^^'.``'`^`````^^"""^```````^^^^``..'..``'''''`^'  I.
                         ;  l-t+I~"^l:/]l>^:;[[>>;.;"'''```+"^````^!``^^^^;:>_!<-;iI````""`  :.
                         ;^ l !(_-, :'[1[~:'^+1?!~:`.      l      .i      ^`;{ll: ;^        .l
                         .:~I`'!ii,`;^:iil,^",!I;:""`...'..:. ... '; ..'. ^^`+I,.."' .   '`,l^
                          .i`^I:":l!^:!"::l;`;:,:;!`^!;;;lI',!IIIl"'IIIIIl`"!;!liI`:l:;Ii,"^
                          I^ ;!;[~.l:+^[-+'>I~:]_!;il"+-]'<,~^](+^<"i;]{;li!,?~_'_:<"]}_^<
                         'l  ^l;ll^l^!:><],i">:iilI;,;!l~"i'>"l><:i"i!<]!ill;>;!,+,<;<+<:>
                         l,,!~lll!_l;;i!^-i:;l>;><i">!I!;>;Ilil^'^  '^`'^`  ^'`^". .^```^
                         ;"l~~:Ii<-_+_<<^ ^!i<~!<~_<->i!l!i<~i<;
                      .   .
                      "}1<^<i![[]]-+?>i_;+_!l~_~~__;~+<.
                       ..  ...'^^'"``.''..`''`''```.'``



















```

*Figure from page 4 (2346x3317 px)*


---



4203-E P-252



SECTION 2 PROGRAM OPERATION



(3) Following ">MP", enter the file name of the file to be output to the punch device using the



keyboard and press the WRITE key.



The part programs are output to the punch device.



While the program is being output to the punch device, "M-PUNCH" and the file name are displayed



at the upper right area of the screen.



At the completion of output, ''file end" appears on the console fine, then ">" appears.


#### PROGRAM OPERATION M--PIP M-PUNCH BOX-1350.MIN

97/07/15 14:10:00



=!,f>l p



>II" BOX-1350.MJN



BOX-1350.MIN file end



YJLTI



MULTI



MULTI



READ PUNCH VERIFY



(EJ @J@J @J @J @J @J @J



(4) Press function key [F7] (M-Pf P QUIT).



MULTI MULTI MULTI



READ PUNCH VER I FY



">0" is displayed.


#### M--PIP

QUIT



Press [F7]



(M-PIP QUIT).



The function key names return to those as displayed in item (1 ).


```text


                                                                                              .^^^^'" "`'"^'
                                                                         ....''..    .'.   .  ^]]+?i? _!~]]I
                                                                         <1-~<+~-]l+._-]~-]]_]}I<-_-_?+~~~}I
           ''''`````````^`''''''````''````'```''.'''''''''''''''''''''..''``'..'''``'..'```.''^'`''^'''.'``'
          .,"",:;:",;;,,""^^^^^,:,":;:,:",:,,:"^""^,:,:":"",,::::;::;:"":"^^"^,""",::;:,::"^""""",,:;IIII;I"
                 ^<l  >;>I;!;l"^,>+!''l:!;"i;`!>`^;I:l`I,!I"li::;^l;^:l!:;:;"<:^,:;,l`:!,;::':;",^l;"
                 "!I .>i~_<~i?>:i_~I:l+I]_;<-+_[+!~+i~^l"li;;i!;i:<i,i<_i!;i,i!;ii!li"!+!!ii,<>;_;i<l
                      i>>~l!>l:~ii,<i>~;!>!^<>>;ii">~l
                      l;:`^,;"^"^":,",'""^',":',^:';,^^""";^";"",".   .
                      ",i;i<>:>!!]i<l<:iil^>>]!>,<^!>;Iill<"l~il><
                      !>;;";!;^,",;,;"",,II""."";"::""l;",`;,,'I,,;;^"<l;!,>lllI`;,:II:;i:^::,:^""^"I,":,":,
                      <+<~>l<~<+l_]~-l!<i+~~[>>i_~~<<l!<i~iiil:~>>i<I'~>IIl><!i:^_l!i>~!+~:<~l~;<iI!+~~<-<_l
                      ilIi<`>+<~,^_+i,~!+;:>I_>`<!i~<I
                      :,":^'^^"^",;""'^"'^"`'` ;:^.^^"^^^^^^^"'`^':^''^^^`"^^"^'.:`^'`'`'`'''``.
                      <<!~~:i<i~++~~<">ll~+_<<.!+<:+~~'i_+<++~:!!,+~II~!<<++I__i"?_+:^!^>}?_~?~i
                               .                  .     .'... ..    ..  ...    .. ....
                             ::;;!~>~iiI<>>i!!i:::::l!i><llll<iiii!:,,,::",;I;:Iill!l;:;.
                            :; ":~)1|11i1}{[<]{,""""+1___;;I;]]-1|{I"";i!i>1r}<(j(\f|< ^!
                            I^                           ....        .l__][~-~i-l_+]?l  !
                            "'                                                          l
                            ;`                                                          >
                            :`                                                          <
                            :`                                                          >
                            :`                                                          !
                            ;`                                                          l
                            :`                                                          l
                            ,'                                                          !
                            ;`                                                          l
                            ;`                                                          !
                            :`                                                          ~
                            :`                                                          ~
                            :`   `^'.                                                   ~
                            ,'  ^j)l_".`:,';,`                                          <
                            ;'  !n},)t_~|1Iil, ';^,`;I`                                 !
                            >^  I!:`^I;"",.     "^;^ll^... ..      ....                 l
                            :' '>_:I"^:;<"I";I_l;;.!,^",,,!""""""!",:::l<i~<i!;I":,"^`  !
                            ""  :(?~;':>(_~"'"){i~,I'     I      I     ^!!}i>^",       .i
                            .;,^ ;><:`,"l~<;,,;iII::`.....;'''..', ... ^;"<:, ,,  ...'";`
                              '"!;:,;`"I::;l";;,,::`;I;:l:^llII!,';;;:l^`!;lli""lI:I!^^
                               <"~+,;l>,-?;ll<;]_,!l!I_?^<!!![-^>;!i{}^+l;<+>,~l:_}>:>
                               Ili!ll:Ili_l!:!!>~Il,!Il<I!:!!!<:l"!l!~;!,lii!Il;Il<!ll
                                                        .   .  .   .  .  .....  ..  .
                 ,i" `i:;;,:::,l,:^:,""<;l';l,ll;`l,;!:
                 !_I `lI~<!;~ii+i<,i<>l_,<:<<Il<:"+iil!'
                                                                                             .
                        ::                                                                  `:
                        ;:                                                                  `:
                        ;:                                                                  `,
                        :,   `>'                                                            ^I
                        :,  ]?{l!l:>;i>l!I;il<ll!:;l""""::!!:;::::!I:,""""I:l;lI;";^":::::. "i
                        :, '!}/<ll i.[\~i; !;t-l!''l      lI      I`      I.)>>->.l         `;
                        '!`:^ -{[+ l'<])]< l^}[+>~^;      ,"      :'      : __lI  :        .l^
                         .:+:^",""`^^'^^^^^,`"^^`^";",",,,:,",```'"""^````"`,,"""":^^`^^"":;`
                          '; ;!i<ll,'!lii!!':l!i!lI'!i~>!i""i!>!ll.;ii<ii;'!I!!!i""i!>ii!'.
                          ;` -'[~I._lIl]?^ll]'->[ _;i`-[!^i_"!-{ ~"_._}[ ]l<:->,,~>"~?\.<"
                         .l  l!!l!l;`i!!<l!`;l!l>lI'!I;;;l""!lI>l!.;!l;!;!`!I?!:l""l;;i;!'
                         ,"                                                ';~I:,`^I;.
                         !:;l^:"!;;I;l`                                  `;, .[-}{+<?i<,
                         ;l<~;>!~+<+<~:                                 `!,^^:<lIi;I!!i!^
                      ^.                            .
                     '~__l?+<-_+:<_?;~-<~_>l-+~_;+i!?<++;-<;?_-]?+_<;+:?~<Il+I
                                  .'  . ... . .  ..  ... '...'`.``'. . .'....'




















```

*Figure from page 5 (2346x3317 px)*


---



[Supplement] 1.



4203-E P-253



SECTION 2 PROGRAM OPERATION



Command format



>MV <input-device:><input-file-name><,<Output-device:>><;option>WRITE



(a) input-device:



MD0:, MD1:, FD0:, FD1:, FD2:, FD3:



Default device is MD1 :.



(b} input-file-name



Main file name Alphanumerics (max. 16 characters), beginning with an



alphabetical letter. Wild card ("*", "?") can be used.



Extension Alphanumerics (max. 3 characters), beginning with an



alphabetical letter. Wild card<"*"·"?") can be used.



(c) output-device:



TT:, CN0:, CN1:, CN2:, CN3:, CN4:



If no output-device name is specified, the default device set for optional



parameter (word) No. 45 is selected. (Jf "5" is set for this parameter, CN0: is



selected.)



(d) option



P: Only protected files are output.



C: Only files which are not protected are output


## 2. If input file name is omitted, input file name of"*·*" is assumed and all files are

output to the punch device.


## 3. If none of the specified files exists in the input device, file is not output.

File not found


## 4. If an output file name is specified, an error occurs.

5213 File name, error 11


## 5. If only one file is output, it does not cause an error.

Example 1: >MP *.MIN [WRITE]


#### All files with extension .MIN in MD1: are output.


#### Example 2: >MP BOX1???.MIN [WRITE]

All files beginning with "BOX1" and with extension ".MIN" in MD1:



are output. Files such as BOX1001.MIN and BOX1002.MIN are



output.



Example 3: >MP [WRITE]



All files in MD1: are output.


```text


                                                                                               .'``''^ ".'''
                                                                                               I[?]__+.-:]]?"
                                                                         .]}~>!+~[<il"-]?~-??][?;_--+-?-~~+["
           .''''''```````'''''...'''''''..................................`^''.'`''''..'``^``^^^'^.'`'^`'``^.
           `:,::"^,,,,,,,"^^":,,,,;;;;;;;::IIIIIIIIIII:::III:;;:;IIIIIIIIII;:,I;:;;;IIII;;::;::IlIllII,::,I;'
                 >+;!!llIll!<    ;'
                 !!li>Il,;;;i    ^.
                    :,`!!!lll+i<i~i!<_^ ;III:,,,,:;;;;;;;:,:;;;;;:,,::::::::::::::"",,,,,,,,,,"^^"""""""".
                   l{,^,,,"":I",`:,`,I  ^"""`'``^`^""^"^""":,""",""^^,,",:,,,,""""""",,,:,;;;;:::;IIIIII_~
                   l_   ,+-!.;iiI>:<<lii;^"lii;l;_l"Ii!!l"^.;I!<:!,!i:ll:`^^^,lll;,"<<~ii~              ;<
                   :[;;Ii<>il<<_~~>~<i>~<ii<+-~<!<ili~<~<iiii~_-~+>+_~<~>!>ii<?~+~>><>i>!~;::,,,,,""",,,-~
                    `^^^^^^^^^^`^`^`''''^^```'`'^'''`^"^""""^""""",""""^^,,,,,",,,,,^^^":,:;;;;;;;:,;;;;I'
                                      ^" .^`'^.,^`^`.
                                     ._[",i~i>l]<ii~I
                                         "iil; ^!l,` lllI'^il;^ Il;;.^l;;^
                                         ,+i!!.:_!:"':I!>'`l>l:^li<+^:ii_!
                                         ;ii~il!"<ll!i"!,??l:.
                                         `"",;"``;"^":'l"!!,"`
                                     .~+`">iIl!-!^!!Ii;
                                     .Il'':l:,";:`:I"::
                                         i}<<:!?l:i<!<`..  `_~!!>l;li<>!l;>>+; i~,~ii!i>>I<^:<!ill!ll,i<i"<;
                                         `:::``:"^,;^;' .  ^-[_<[~_~<_!___~l>?!<~I~+_>_<+;~~>~~[>!+<+!_~>:>:
                                                           ^~<!I<iiiI!`ii<!  >>l;"!II"^,^  :^'"i!'!!.li!!
                                         >-+?<i_><'    '.  `<!l!l,,;lI;I,^!i~, !`l;lI!liIi,.>i!l,!;;":l>';>^
                                         `,,;"":"".    .   "_+_~?i_<>_!+-_+I>?!_!!>~~~<+i!ii?>]_i<~-li~~lli`
                                                           "~><i<ii!l<:i~_i. <<<!:<I>:,l"'.;"^;~>,<>^i<<~'
                                     .;;.^:I;,l"lI:;;,
                                     .>i'"!i<!i^!>!li:
                                         ,lI :!<i` l!>I'"><~l.li~~"'!<i!'
                                         '""'";Il".:II^``:Ii".,"!i"':III.
                                         !,^>^'l<_<~^~~!i<''~>I_ I:`<lll-+~;.-+l'->~ilI^]i!!i.;<I'il'I<~!>><.
                                         ;ii<il~-_;<~+~?i_+;:-~i!;+>]++~+;>_"-~Il!~+~+!:]+!i+li_>I~<`![-]>!_.
                                         !+~><<~<>';!;:!:"!; Il`!^>!!!l!i':l.l^'i^ii"!I^li;li>!>I>>i"^;i+,^<
                                         I~l>i+~i;
                                     .,, ''^^`.
                                     ^_+.:~+~<;
                                         I:   ^I:;`",:I,::,:!::'","`",:^:.
                                         >l.  l_<?l]<~_~_-+><~_:<~~:~~}>~^ .
                                         ll   ;<>-;+++;l+<><^-<l:>>l-!~_>--<I?-I><?_~i
                                .^  ."'''.'`"..'.`` '..''``.'.'..'','...'.. '`'. .^'.     .  .   .   .
                                "-. ,>;<+>!I}<,~-i-,<l;>i+_~~'<?+?I[];>]~<~,?;,>^<":~;]--_~-?<!-_~i-,]?-:__~
                                    ^<>+<~!_,+_il+><+!l{<<~+`  .                    ...... .. ... ..  .. ...
                                     `''.. '  ...'..'  `''.'
                                "_  :i:ii~l;<i+>,~><!<~>l>?>Il<><_:!:~<!;i>!i;_!!!i'!+lIl,li,;I>l!"
                                ."  '"'^^"^^^'",'lI;:":;"^I;",;:;I^"`:::^:l;:"l;:;l^"l;,;^;I^;;iIl^
                                    l<+>:+~:+>l<<
                                      .. '. .'.'
                                "<  :>l+,!>~>iI+?I;>~i<:<"<<~!-+~l`_l:<!i::!l!Ii"
                                ."  ''":.";:",'',`.,,`,.:';;;,,:;"'l"^I":^";:;:;"
                                    ;]~!_.~<_:i_<<~.<>i+'!;
                                     '.     . .'..' ' .' .
                                ;~  l<I<~i:>>ll?!Ii:i>>I>'i;+i+i:!+;!~l><,_I:>I!:
                                '"  ````",.^""':"`,^:":",.^`,:;:`,:^:l:;;^!"^;^;^
                                    l_>_<~--^I. l][~`!I1?]!?-_?!~?:
                                    .'`^'^^^..   .'  .....''. .  '.
                                               .-_I]~>,<+<,!>+>i<!>'i[]+,!:?_>l.!il"!i~I<^
                                               ."^ ":^.,"^',":^^",, `;,^ ^`I;"^.Il;^IIiI!`
                                    !+!il!!>"<' ,<_i,-!>!:lll,~<<"!<<>I>~"
                                    ";I!:lll^I. ^;I.`!::,`'``^!II^;!;;,;!:
                                                I"^i,^^,"","""` ^:; "!,""^^^"""":;'`,:""""^`'^I;;"`^`I;,^
                                               '~>l-~~l+-]_+!![I~~?^;]>~~l^~~+!<-+Ii+<+i__+l`l]+-:I+I?+iI'
                                               '~<l"><-<i I!~-;i<!<,++I1<<_!~+<,?-?i!_<l-_>-i~+_!~{-?,+~,
                                               '+<]>-l..        ..  ..       .      ... ...   ...... .'..
                                                ^'^^"
                                    <~!<!i~~,~'.;_]>;_+]~~_>'
                                    ":;I,III`;. ':I ^;:"".^:
                                               .i",<;,^,^<>::.:I:^::I,;.
                                               '>I;~<i;l,++l:'><i:<i_>>'














```

*Figure from page 6 (2346x3317 px)*


---



6-3. Multi-file Verify



4203-E P-254



SECTION 2 PROGRAM OPERATION



The multi-file verify function verifies multiple machining programs, stored in an external device, against



those in the NC memory.



The operation procedure is indicated below:



(1} Press function key [F5] (MULTI PIP).



=f.PIP



MULTI



DATE DIR PJP EDIT PIP LI ST CONDENS [EXTOO]



"=MPIP



>" is displayed. Press [F5} (MULTI PIP).



The function key names change as indicated in item (2).



(2) Press function key [F3] (MULTI VERIFY).



=f.PlP


#### MULTI MULTI llJLTI

READ PUNCH VERIFY



">MV" is displayed.



Press [F3] (MULTI VERIFY).



"MV" is displayed on the console line.



M-PIP



QUIT


```text


                                                                                               ^^""'" `^."`'
                                                                          .......    .'..  .  '?[][i[`!ii[?~
                                                                         ;}]+i<~+[l-'~_[_+?[_?{ll__?--+<_<-+
           ^^`''`''```^``````````'''''''''.''......'..'''''..............'``'..''''`...''.`.''`''`.`'''''`''
           ^,"^,:,"^^,"":",,:"^""'";;;;;;:,::,,,,",,,,:;;;;::::;IIIIIIIIII;,:::,,,;;IIII;,,::::IIIIIIIIII:;,
          .?"i;    ~~:<>"~iI"><l>+"
          .~,!I    !ili!^Il!'i>i;-;
                'il,.:`:;`!".^,:!.;":;I,,':;:i;:';":l:l^,,:,I::,"`,""",:":'.;,",:`"'""'"","^""';^^"" '^^""^,
                ^<<+;ii<+l~~;+~<]l>ii<!!I^><;<+i"!!!_~~:Ii+i<<il+l+l<[<_!+;"-<i~~,!"~i"~<+<!+<:[<i~_,I][?~+_.
                :~li_"I"~<i"->`Ii~i!>~'
                ':"^.^^^`""^'.^``^`^'"'^'^^,^`"^^^^^^^`
                '!i~"++~>]<+!I+i<_++i<;iIi~-<~_~>l++>_~.
                  .   ''    .   .      .^.  '.  ' .''.
                 "<<' ~<_?]l-~+_?_il]?!]_[!<)-_+>l<_-+"
                                     ...
                        `:                                                                  .:
                        ";                                                                  '!
                        ,I   .;!";.                                                         'l
                        ^:   ,1[;>                                                          'l
                        ^:  ~+:`"^,:,^^^^^,,^^^^^^":"",""",:"''^^",^^^`^``",",,,^`^``^"""^. `>
                        ":  ~` '.`'iI... ''!`.. .'^!'...'';l!t<i+^l;'.. ''~"....  +'  ..    `<
                        '!'.,;[<?. l, <l<  ! .>!! .; +?;! ^";??;  :^.;,_; !><]?-[>l <~>~--! :I
                         ';!!,I,:`.^^."^^'':''^^`.'"';I""',"'^,''',^':^;^`;;;ll;l;:'!iIl>+>I;
                           l":!!!!i,'lIIl!i'^!ll;l:'li!!!>"'l;;;l!`,il!Iil^I;:::I^^>llIl:.'.
                           l _'-<I.~I~"[?:,I+^?<] +;i^[]i`><;!]{'i:~^?]{.-;<`?<l"+l,~]('<:
                          `; !;!;lI!^>li~l!"Ili!~;>^iIl!lI;:ii++I>^IllI<:<^>I!l;ll:lI;~:>"
                          :,.':",'.   .....  ....'   .....  .,[ '   . . .   '..''  ... '
                          ;'I+]>_""^^,.                      ; '    '.  .    ..
                         .i;il~!___?_?:                     '<,_~]]~[]<-}++<>_-<'
                                                             .'        .'`^``'.'.
                      !+~I!i!!+!l;<>;:!i!i>^!<>!!~"!i:i!+I<~!l;;:!Il`ii.
                      .^,'';^,:,`':;,'::^,;'^,I:i<';;'":l:!il;,:,!I;^!l`
                 ^<I  !IIl!"l,:ll:^:;;'ll!"I<l:"l`:i!i!:::
                 ^iI  ::ii>,iIIi!l:;><,l:~l!<!!::":ii!>,:l'

                        I`    .                                                             ;"
                        ;'                                                                  !:
                        ;'   ,]>!l                                                          !:
                        I'   >z]"^                                                          !:
                        I' "]-{>l::i;<>liI;!!<:I:^;:""",,:!;:::"^"l::,"""";"II!!l;I""",,:,  !:
                        l^ I"}[i>" !.({+<:':+t~>!':,      !`      l.     'I`1<~_;"! .  ...  l:
                        `l"l  ??+l l'<~}_l.::{+iiI^^      ;'      :      .: ]_I, ^:        ^l.
                         .il"::"^"^"^^^`^"^^^"":,,::;::",^"^"^",,`^`"`^^"^"^""`,,:::^`^"^:::.
                          I `!i+~I!^;!><<ll'!I<>l!,,!<+~Ii`ll<+!lI'i!__!!,"!!<<l>^li~~<!l.
                         ,: ::l+<'Il?^i+] ~;>,_>!"+>"<~} ~;-']?_._,~"?)!"_!,!i~ _l<'_]-.{
                         !  'l;":;;.`l;Il;, ;;>{Il``!I:;II.:I:;!l,.Il;III^'l:,;II.:lII;I:
                        ^il?]li_~}__-+-^       !.
                        .'``''^"^^"`"^^'       'l><__!~~>>?~i!,<_-~!>^
                                                ',;lI:,:;:;;:,":lll:I^
                      ":,"'^.""`^^'`^'''',`.''`'.` ...
                      I]~I'_:+-[+-?~~;<!;~_;>+<_+]>!~-I































```

*Figure from page 7 (2346x3317 px)*


---



4203-E P-255



SECTION 2 PROGRAM OPERATION



(3) Following ">MV'', enter the file name of the file to be verified using the keyboard and press the



WRITE key.



The specified part programs are read and compared to those stored in the NC memory.



While the program is being verified, "M-VERIFY" and the file name are displayed at the upper right



area of the screen.



PROGRAM OPERATION



tape end



file end



data match



MULTI



MULTI



MULTI



READ PUNCH VERIFY


#### M--P IP M-VERIFY BOX-1350. IN

97/07/15 14:10:00



M-PIP



QUIT



@J @)@J @J @J @J @J @J



(4) Press function key [F7] (M-PIP QUIT).



LIJLTJ MULTI MULTI



READ PUNCH VER I FY



M-PIP



QUIT



Press fF?]



(M-PIP QUIT).



The function key names return to those as displayed in item (1).


```text


                                                                                               ```^., ^^.^^'
                                                                              .       .        +]?[>]'i!>}}<
                                                                         l}[~i<+~[;_'<_[___-]-[l!-_-<--_+~->
           ''....'''..''''''''''''''..''''''''''''''.....................'^``''``''^...'`'`'``^'`^.`'`^``^``
          .::,,,,,^`",^"^^,,:,:;:"",,:"",:;::::,:;::"^,",:::;"^,:;,::"""^"":::::;:::;:;:""":,,,:::::::"",,:"
                 .><  ;:ll:;:;,`,<<l: ;;ll^ll,;<:^;;;l`::;I::>:";`;:'::I!:I",;:,^l;,";,I:,;,:"::,":::""I,.
                 `i>' !<]?~[<+-"IiiI``iIi<^Iil:~!:i>l+,l:;>>:~i:i"<>">i!><i:i~l_ii<>;~++<<_!li~<l+i__<I<~`
                      I~I~I<:;i+:
                      ":"'`""^,l,:"",:^"""",,""'""^^,",^"""`^^"^^"""",`""^^^'""^^""^':"`^::'^^^^'`'.
                      ,;<I;_!!i~<il<~i:>l<-i+l~"<!;,+-<"-li,!ii~+_<~l>;lii~+"+<><+l!:<i>:_>"i+~!ii_'
                      ;!;;I^l,`^"",":"`:";,,^'';:!I," !!`;iIlI,;'"""^;:`,:`'""^".^"`":",:`^"^`^:"`.^"^"'^","
                      l+i>~l~_i~!~?>->:>l<<!<i:~<<+<i'i_,><i<i,l.+><;<~l;~!;~~!~;<<!i_?_-?<~l~i<~<:_-~~,![~i
                      i+i_,<I~~!;~I~~<"
                               ...     .   ....''''''..............  . ....... .  ....
                             ^:,;;lIIIl:!ii!!!>l!lIII:::;I!i!lI;:::;;:;:;:::,":,,:lI;:::.
                            'l `;i{|\\x+{\\|+]/!::""",,:/}?[I,,"I|_\)[{<I:;:;i||--(|+)?-:.
                            ^"  .. ....'.      ...........  .....'...'I[]-}+_]I1_?]])<` "'
                            ^"                                         ...... ........  ,'
                            ^"                                                          !`
                            ^"                                                          I'
                            ^"                                                          I'
                            ^"                                                          I'
                            ^^                                                          I'
                            ^^                                                          I'
                            ``                                                          ".
                            ,"                                                          ,.
                            :,                                                          ;.
                            :,                                                          ;.
                            :,                                                          ;.
                            :,                                                          ;.
                            :,  '<-<^__^                                                ;.
                            ,"  `~+?;1{I^                                               ;.
                            "^  `<lI"~IiI                                               ;.
                            `' '!~:;"^;:l,:"":I:::`",",,,,;,"""""I"":""":,::Il;I"^^^^"  ;.
                            ^"  :\[~I.lIt?~:^;{{~+^:"     !`     <     ':!}i-!^!......  I.
                            .I"' ,[->.;">+_I'^I_<!!:^     I'     l     .,^-I! ':      '::
                              ^";;":;,";,^^:``,^^",'^I;;ll",;,";,^:l::;,^",",I,^::""I",^
                               "I!-!">;l~]+:!!;?+>;l!,__;!I!;[}:>"i:?],!:i;~+,i:!!?],~
                               :i!il,<I!i~~:i!;<ii;!!;<~;ili;<_:>,>:~[;!;>;ii">;!l~],-
                                ...'`  .. .'  '  .'  '.''' .`..`' .^''^' '`''^. '`''"
                 ."`  ,"`'''^''^''...'."^^.`,'^^".^``^`
                 ,-i .i~+++;+>++~+ll+-I?;<;+}i>~+"_~+i~^

                        >'                                                                  :^
                        !.                                                                  I^
                        ;.                                                                  i"
                        "    ^;                                                             i"
                        :. "~~-,;""I":,,:",;;I;;,":,""":::;"^^^^^^;",,,""";^"":::,"^^^^^^`  ;^
                        l  Ii|]i>`.i`|[!i,^;[\_l! I, . ...i'......i......"!:)I<_I^:.......  :^
                        :I.I  )}-l I.-?)~l',I1[i<!,^      I.      l      `i'{>;, ",        '!.
                         ^>i"^;I;,^:^^:::"":";::"`^^''''``:^`^```^,'''^^`":'I:^`'"^'`'..`":I'
                          l'`!IlIl!`"!lIl!;'llllIl`^!II;!l`;!l!!i"'l;;;l!^^!,;IlI':iiI;!,`'
                         ^; III-> !I-^]-?.<I~"?+l"i>"_-} ~;_'?}>'>;i:{1:;<l^+>-'+I>^][_'+
                         l. ^!;:;"!'I;ii<:!^>Ili!!:;l!l<;i^>I!iiII^i;I~!!;:Ii~l,>"l:;ii;i
                        ^i">:ll<~<<l!<'..'   '....  ....'   '....   .. '.  "!],"' ^,^  '
                        ^,:!:Ili><><i!.                                  ':" ;-+?-+~_^"
                                                                        :>:",i?ll+;<_i>I'
                      .                                                    ..          ..
                      _!_I_l>~~<!i_-I!_+<_<,<+!>lI<l]<~-;>?,?_~>+~<_l>,__>I:<l
                      ..".``````''^,`'"^`"^.`^^`''^'^^",`":'"";^,;",'^'":^`^^"






















```

*Figure from page 8 (2346x3317 px)*


---



[Supplement]



4203-E P-256


#### SECTION 2 PROGRAM OPERATION

Command format



>MV <input-device:><input-file-name><,<Output-device:>>WRITE



(a) input-device:


#### TT:, CN0:, CN1 :, CN2:, CN3:, CN4:

If no input-device name is specified, the default device set for optional



parameter (word) No. 57 is selected. (If "0" is set for this parameter, CN0: is



selected.)



(b) input-file-name



Main file name Alphanumerics (max. 16 characters), beginning with an



alphabetical letter. Wild card



Extension



{c) output-device:



("*", "?") can be used.



Alphanumerics (max. 3 characters), beginning with an



alphabetical letter. Wild card ("*", "?'') can be used.



MD0:, MD1:, FOO:, FD1:, FD2:, FD3:



Default device is MD1 :.


## 2. If the text (tape data) read from the input device does not agree with the specified

file name, it is skipped and not verified.



In this case, the following message is displayed.



5210 Input file name not same a '(tape) file name'



a.: Number of unmatched files



If no files match with the tape data, the following message is displayed at the end.



5210 Input file name not same error



Total number of unmatched files


## 3. If input file name is omitted, input file name of"*·*" is assumed and those which

match the read texts are verified.


## 4. If unmatch is found, the corresponding line is displayed on the console line with

unmatch character blinking on and off.



The message "verify continuing (Y/ N) !" is displayed. To continue verify, input "Y'',



then the program verify restarts from the next line. If "N" is input, the file containing



the unmatch is skipped and program verify is executed from the next file.



For each file, the result of verlfy is displayed:



(a) If all data matched, the following message is displayed and the next file is



continuously verified.



tape end . file end . data match .


```text


                                                                                               .'`'.'' ^..''
                                                                              .                l]?]~~< _:--["
                                                                         .-{~><~<]+il^-]_~-?--[?I_?_+_-+<+_]"
           .````'``````^``^`'''''`'''''''..'''.................. .........``''..'''`'..'``^^'^"^.^''^'^`'``^.
           ^::::,"^^`""",,""",,",,;;;;;;:,,;;;;:::::::;II;::III;:;;;;:::;IIIII;::::;IIII;:::;IIII;::",;II;;:.
                 i_lil>ill>!!    ;.
                 IIl!lIl":I,;    ^.
                    :"`i!ili!~i!!~!<<-^ ;;:;IIIIIIII;,,:;;;;:,:;;;:;;,,,,,::::::::""",,,,,,"^^"""""""^^^^
                   >[^`""""",:^^.,^^,;  ^^^^^^^""^^"^'``""",^^"""",""""^",,,",,:,,:,:;;;;;;:::;IIIIII;;;__
                   i~   :-_! l!>i>:~<I!~;`";I>!ll?l,!i!!I"^';Ii~Il^!i;Il:`^;<~<;!!                      ;~
                   I?lI;l!iil<i~~<i<>i>~>ii>>~<>i~<i<+iiiii!<~~-~~i+_<<_>lii~<~!i+::""",,,,,,"""",,,,,,,~>
                    `^``''`^^`^```^`'`''````'.'`^'```^^``""""^^`^","",,"""""^",:,,::,,,:;;;;;:,,;;;;;;;;;'
                                      ^" '^`'^'"`^'^.
                                     .~]^:<~<i;<!>i<"
                                         ^;I ^;Il^ :ll;.^l!l;.,IIl^ :l;;'
                                         ^;I`,!!<;.l!!I`^!<<I.:i>~l I><~'
                                         ll <" ;ll<">il!<^ !<li^'< i!lI!_i~ ;~i':-<~li,"~ll!i ;>!.<l.:!lIll>^
                                         ;!l>>l>-<I!+<i+<l>i;~_:!!;+]~_~+Il>:~+"!i<+i<I:-<!l<:i~i,~<`;[-_<I-`
                                         !~+>~<~~<`Ii!IiI">; !:'>`ii>!i<>'"<.l:'>^i<,l>"!>!:<~>i;+<~;`i<+l'<'
                                         :~<<i_<i;.
                                      "^ .`..'`"'.'```.
                                     `-+`^<_<i!]~"i_i_I
                                         "I,"',:''^"^^     ';^:^^^'^^^^^''^``. ""'"```'`''' .'..'''' .'^` .
                                         l-_<:i?l:+_>_`'.  :_+-<_>ii_+~<!!<<-!'~_l~<]_]+]<-ll-_}~><i]l+~i!+I
                                                           ;_+!<-<-+!_:~+~i ']?<l;~<>:III'`i!:!->:<<;>+>~`
                                         ;:,,"^,^"         ^!:,,,"^,,:^"^":`'`':`":,"^^,`^. `^`:,^:,.,;I,..
                                         i~~+><+>>.    '.  ,_-~i+!<i<_<~i;<~?i'~:il+i_<?<+>"-<?~><>?l!<~^<-'
                                                           ;]]~~-~+>>-l+[[< ^]--lI+<<;ll;^,<!;>-<:~~I>~~~^
                                                           .^`.```''`^.`'``  ''`''^``'.'..  .`',^.^^'"""".
                                     '+_.I<-]i>I]~<+_:
                                      .. ":::^.":,^`':"^' `"`'  "`'' '`''
                                         >-><! ~{>l".><-+.I~~!""____^>_+_:
                                         ;;I!:I,"I";;^^":<l,^ .     .
                                         I!iiil:I<llil,!:~!;^.
                                ^I  ^;ll,",""^;,"`';""^.,`"^:":^":,'""^,`;""""',"^^'^^`^``^`'^",',`''``'",``
                                "i  :<i><!-+>!?-_>i]+->;___I><~!I>_;!-~<;?<ii_:~<~+:><;~[<~<:+++;~~!<-++-?_<
                                    "-<`I-i<l.l:I;-!~<+<"+!<"l~:l_l-+_I
                                    '^':"^.^""`.I"',::^^"`'`^^^``''.^``"'``''''
                                    ,~,<>i"<-~!`-<I;<+i~<i?;~_-_-?_:!I!-~<-?~<i
                                        ;;,;.`:"^""I^.^^^"``^`'^^,,..'`:"^"^":^'""""^
                                       .~<I?:;+++<:-<:>_!+l!<!l?_!+";I"_-__i;+>,<+i_I
                                        !. +~;<~<I,>^i!l~]~!i<;i-_I
                                    ^;^"`I"^."^,":'^::':^`^`^`'"^".^,^^""^`^^'.```'''.'.'.`'.`...'.''`. ....
                                    ;iI<,!i<:l>_><^i~<"<i;i-~i:?_-,i_~;~<<<?~?>!~-+_-{]:+I_-]-]_+~!?l__!+>_;
                                        I;:;.^,""":;^."^^,.`"^'""",  ""`.".          .
                                       '+<!?,!~+~>l_>:i+i<;!<!l?_i-,!_>i:<^
                                       ^_  !~]>,<>~+><`~;i<i>-_~>+!i]_>
                                ..  .'..  ..     .       .       ..
                                I~  !i;>~~I~?l;<ii<:<"<!~-~>.I+~<i_1!I?-<~"_!">^i,;+:-~~!i~_i!?>i-_>+~,_~>~!
                                    ;i<]_i!++,i__i~~~_;>_!:<<~[_~^.`'.^`'`.`  `.` .`'"^^^'^^'`"`'`^^""."`^^'
                                    .`,"^..`^.",;``:^:`",".,,^,,^
                                :l  Il'::;iil"^:`I"^:`.!:'^"":;::;:ll,:";I";,^i;:;;,;I`;^:l:',,,,,l",;:`^:!^
                                ":  ;i><!~--!i!~:>~ii!;~+l!!I>~<+<i>~~~,;i;ll:<i<!+><i"~;;><"!ii<i_!;<~:l~+;
                                    ">>Ii~I:.>i<!>l<,,~!i<;~"i:^~;!.i!
                                    ^;"``",,,"`"'`^";; `^^;,`"^^`:"l^',^^^:"":^^^" ",'`^^:^''''^^:''^''^^":.
                                    :>~>;++~~+--:,++>];~>i_i>~_]!>!_<I^iil_?__-<+~';-;>~<-i!_ll-~->"~~i<`!;'
                                    l~<! !il!ii?<_<:;>!+!;<<-<<>l!!!l<<:Ii~il!~.^!^-"li"!>>;I_>;~~:l!~__>~~i
                                    !<<^~~~<]<-I+;+_~-~~>!_<><~i+~++;;->]+;<:~<~!!~~l<~<+l]_lI~>~i?+".``.'^^
                                    ^^`.^`'^""` "'^^",^"``"^',,`l",".',`^: ,`:,:,,;;"^,:,',;,^;;;`;I'
                                    <>~"<_~<;__,!?+,>+~-ii<:_>i~"+"--_~_~>+:
                                        ''.      ..  ''. '  .' ` . '."'`^..
                                     l-I.<,?:i~<i^!>+!>!i.ii!l<+iiiIi^l!iii>i!,i"~iii>i!>;>i!;!i^Ii!:!_:I;
                                     ^:`'!!+>><>i!~il<i--l>",`::,:,"i"":;;Ili;`;`;;!:!!;;"l;;":l`,lI""!,:;
                                        '!l:;"::"!!I.lIl!!I
                                           i!l;^!:; I~"^l,l "iii"IIil!^
                                          .l<iI,!;;.,i;:>;!."i>>:;l>ll^.
















```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-257


#### SECTION 2 PROGRAM OPERATION

(b} If file data remains although text (tape data) has been read to the end, the



following message is displayed on the console line and the next file is



continuously verified.



tape end



data match



(c) If tape data remains although file data has been read to the end, the



following message is displayed on the console line and the next file is



continuously verified.


## 5. If an output file is output, it does not cause an error.

5213 File name, error 11


#### Example 1: >MV *.MIN [WRITE]

Verify is made with the files which have the same file name as the input



files, having extension .MIN.



Example 2: >MV BOX1 ??? .MIN [WRITE]



Verify is made with the files which have the same file name as the input



files, having extension .MIN and beginning with BOX1. The files such



as BOX1001.MIN and BOX1002.MIN are examples of such files.



Example 3: >MV [WRITE]



Verify is made for all input files with the files having the same file name.


```text


                                                                                                '```.` ^'.`''
                                                                              ..      ..       `__-];- <l<[~,
                                                                          >1[~<+~_?l~.~?[+-??_]{li__?<-_~+~}>
            ```'''''`````````'''''''''``..''''''''''''''''................'^``'.`'''`...'``^'``^'``."'^^'`^^`
           .:::,,""":;;;;;;;;:,,,""":;:"",^^",:,,,::,"",:::,"":;::;::::"",",::::;;::;:,"":""::::;,,:""";;:;;,
                                      :>" i;i;'lli^"l;:;::`;>:"",;`;,I^;;",';I;;`"::^:::,'",,,""`l,'"",^^I".
                                      ;i,`+!+~l_~~l!_i<_i<;_<>~<[_,<~~;<_?~:<+~_;!+_I~~+>,>__>I>:__!<>~I;~~^
                                         '<<<i+!>l;>!ii~?_^i"<-_+-_~+,>!:+~;!>><~-i;i<:!~iIl<i,~++I?+"~,
                                         '<>i+<>~<<+<"~<+?+_^
                                          ''``'^``^^".``.'^`.
                                            <~~>;+ii
                                            ~[_~:<~_~~
                                            `"^,.'"""'
                                      ;i,'i:i;;.;!!"'I!;iII^;il;;,!";<,"!II,II:^;:;"';I;;;^,I;`;:;.;;,
                                      :!"`>!?-+Ii<+>;+<i~>>li+i>~_-ll_!l_-+;!_~;+_~!:~++i<!<~+:_>_:+<~'
                                         'i<!><I+I:i~<><-?^+"~~]i++~<"<i,><,Ill+>_il++,><<l-~i,~~~I?~"-^
                                       . `~>>?i>~<~?>"_-]]+-`     .
                                               '. '.' ..  ''
                                 ~:  +l+i,>i_ii;}+"~:!l_i~,I!<~<+:l>i:~>!~Il~,iill'
                                 `'  '',''"^:"^.",`"'^^,,"`''"",:'^,"^;::I^,:`:,",.
                                            +-!~":~~!,<~!<";_I<;^~.
                                 `.  . ' .. '^^^'  ^"^^,^""^,^"'.'
                                 _~_-<[[<"l ^>{-;::??[+<{-?~i-_.
                                      '                       '
                                            ,+<i],>,;<~-<^+_~,~~l<i~:!?~~-"!_i<I~<;i_~~~!]<,i<i<lI_;?+!l>i!!
                                            l]+i:~<ii><l<>-ii<i~^<?]_"^`"^.',^"``"`^:"",'""'^:^"^^;`":"^:;:^
                                            `:::.^:;,,<^;II":I;" ,;:;
                                 ~I;I:;i::; .,!I"l!:I:";:",i!:`Ill:,l!'
                                 >!>>I~~l;l `I>l^i<!iI,",,!_<>:~<ii:~_^
                                            `^'^^ ' .``"` '^' ". ^''  "^`^'^`'`'"`.''`'.^"'.'.......^'.'.. .
                                            I-~!_I+;!+_-_:-[~I~_l~_[l>+>+<;<_<_I++I!-_+~i[+;<]~+;!]:+-il~~<l
                                            I>_>.>+<<!<:~<~l>>i! <~~>,+!!I<i~!i~i<^>~>`[>i~;  ~i<:~<i"<i~~.
                                            I-I[?>?<<-[l<??_l_<i!]<_<>?-_>}{1I>~i~<<<><+~>,<;!;>~:-<~^^^^'
                                            `, `"''.'"' `:",^I,"";,:"":;;"I::^;:,"l;;,i;I;`;`l;I,`IIl`
                                .~!i>l!+Ill `l_i"><~<Ii~,
                                 :;ll:li:,: `:;:'!;;:"";,
                                            "I":: ".`"";":I"^!":,":"!::'":I';,":;"^^"^^"`';"`'"^^^`;"'`^^^`
                                            ,~<I~"i,;>~+i:~;I?:i~>~;~++,>>+"i<i!__<;~+!!-l<_il?~l+:_-:I-<<~.












































```

*Figure from page 10 (2346x3317 px)*


---



6-4. Quitting Multi-file Transfer



4203-E P-258



SECTION 2 PROGRAM OPERATION



This function is used to quit the multi-file transfer mode and to return to the program operation mode.



(1) Press function key [F7] (MULTI QUIT).



MULTI MULTI MULTI



READ PUNCH VER I FY



">Q" is displayed.


#### M-PIP

QUIT



Press fF7]



(M-PIP au1n.



">Q" is displayed on the console line and the system quits the multi-file transfer mode. The screen



returns to the program operation mode screen and the function key names as indicated below are



displayed.


#### DATE

DIR



PIP



EDIT



~~Tl



LIST



CONDENS



[EXTEND]


```text


                                                                                               ^^^^.,.`^.^``
                                                                          .. .' .     .       '?[?[i[`l>i?]?
                                                                         I{[~<~__]!-'<~-+~?]+-1i!-~?~-_<+<]<
           ``^`````^```````'```^`````'''``````'''.....''.................'`'''.''''`...'`'^'''`''`.`'``''^``
           '"",::::""^^`^"`"^^,",:""^"`^,,,"",:;:,,,,,;;:::IIIIIIIIII;::::;IIII;;:,,;:::;I;III;::;;;;;;;I::"
          .?"!,   .>>:<?>l!^~~:<i^~i!^_;!II><I'
          .<,l:    IiIl<!;["!!iiI`Ii>.;:_!!<+<'
                ^<I;'I,":l,,^, "::"""`:,""I"."^l;:i:";:,:l:',:"I,':"::,':;^"^^"':"``"^^"""'^^^^^,^^'^^`,^
                .::i,!!;!!!:"!^!i!;;l"-iI:>>^lIiI:i>:!>!<<~"!<i_<:-i<!<,~+>>;I~,i+I><i]~-<:>-+>~_>>:i<<?-`
                  ^'  ,:```.,.^``'''`` ^,"'';"`."'.``^".
                 "!!' i!~-_;_<>+<<lI-?!_l!!<{+<ii;l-~~!!.

                        !'                                                                  :`
                        ,.                                                                  I`
                        ,                                                                   ;`
                        ;.   "I                                                             I`
                        I. `-_?;I::l:I;:;:;I;,";,":,^":::^:"^^"",,;^^"""",;"",,^,:;:"^^`^`  I`
                        !. "+(?!<^.l'/]li',l[{l!; ;"......!`.....'i.....'"l;(>~-I,I''.....  ;`
                        :; I `}??I `'~]1_,',!}}i_l"`      :       l      ';`}<l, ",        .!.
                         "l<"`;ll:^^``::,`^"^;;:,",,``'''',^'```.':``'''.^:`!I,^',".''. '^,I`
                          I^`IlIIl!``!II;lI':!!il!"^i!!I!!^:iIII!:'l!;;;!^`!l!!!l'"!;I:l,^'
                         'l "i,[~':i+,~_['<;+`]<>'+I:!_{`!;_`_-_'<^<`{[i`+l;!~?^>!>^_-['?
                         ;` '!;l;:I":;l!~:>^>;!!i;l,!lI<;i"!Ii!>,i'>I>~<;i:!I<!,>:l:!<+,+.
                        .>:ll;ii_<<ll~^'.'   '''''  ....'.  '.' '   `'''`  "l[::^ ^;,. `
                        ',:l;;ii~i!>i!.                                  ':" :]_[_-+<",
                                                                        ,i:`"!?i!~;<<<~I'

                      ,;~l,>:?+<~~<~~,>,~<!;ilii<>:<~I;><!!<;I>!_ii,I!>~,<i:;l;<,~i:!i!I+<,:l;i>..<!!"!I!!l"
                      ;>ilI>;>l_~<><ii>!<lli~ii-<<,i<!<!liI>i>>>~<!<~>~+l>_!!!<<;l<ii~~l~~;l>~i+I,li~i<>!+>:
                      >+i<!il<:,l:!;;+!i!":>i!l>ll";I!i;">;IiI^iIl,!i:I>Ii!ll^>~i">_I<~:<!;i<<!<++;!~~;>^<>l
                      <>-~+__+;


                        ,                                                                   ^
                       .l                                                                   I
                       .l                                                                   ;
                       .l                                                                   ;
                       .l  ';l```""""""^``""^^^```^^^^^^^^^'  ''````^^`''`^^^^^``'''```''.  ;
                       .l  '`   '^,I^`'.'`!I^''.``~,`.''^"!,)~i+,:i^`^''`ll`''`'.>:'``'..   ;
                        i'  "+i+^ '" ,I<^ I" l;!  I ,+;I. :'{?<' ." ^'!; "!l>>l>ii':lI!!>;  !
                        'l:^:i:l^.^,.";!".:".:;;'.:':~;:'':`,;"  ^,.;,i: "li~+i~~;'l_<<+{~:I^
                          '^`,"",I:'^:",I!"';::,;I`^;^"^I:^;I",Il"^lI;,;;``I::::^`,:^":;.`^
                            ;I<-<'i:+^[_~^i:!:_+:lI!,_--`<">^_}i,i"i;-};lIl;_<_"+"i:-]<:>
                            ll>!>"<:~:<~+"i:!;l~Iil!:i!+^~,<:<+>:>,i:i[;!!!:<!i^_:>:+-~:_
                             ^^`^"'  "'``". `^`^"^  "`'.^' '"^^^"  `^''^"  """^"' `,""",





































```

*Figure from page 11 (2346x3317 px)*


---



4203-E P-259


#### SECTION 2 PROGRAM OPERATION

6-5. Notes on Using Multi-file Transfer Sub Commands



Send



(1) Communication Text Format



The text format used in multi-file transfer operation differs from the format used in a single file



transfer operation. The format used in multi-file transfer operation is indicated below.



(a) ISO code



File



% CR



File


#### LF NC program % $ %,CR LF NC program

......



% %



name name



------ First file ---------- Second file Last file



1} The file name is preceded by "$" symbol.



2) The data which follows "% CR LF" is regarded as the machining program.



3) The program end code is fixed to"%". (NULL code is not allowed.)



4) The end of communication code is fixed to"%%". (NULL code is not allowed.)



5) Leading and trailing feed holes (NULL or space) are not provided.



(b) EIA code



File File



$ ER EOB NC program ER $ ER EOB NC program



.....



name name



ERi



------ First file



------+1<1-----



Second file Last file



---.J



1) A fife name is preceded by "$" symbol (set for optional parameter (bit) No. 31).



2) The data which follows "ER EOB" is regarded as the part program.



3) The program end code is flxed to "ER". (NULL code is not allowed.)



4) The end of communication code is fixed to "ER ER". (NULL code is not allowed.)



5) Leading and trafling feed holes (NULL or space) are not provided.



(2) Timing Chart



(a) Multi-file read and multi-file verify (CNC: master)



DC1 DC3 DC1 DC3 DC1 DC3 DC1 DC3



(CNC-Hosn



\ t \ t t \ t



Receive Communica- Communica- % Communica-



(HOST -+CNC) tion text 1



tion text 2



) tion text n



%! %fl_



Infinite



1--1



1--1



[Supplement] 1 . The DC3 code ls output in the following cases.



(1) Just after receiving the text file name



1--1



(2) Just before writing text name to output device (every 252 characters)



(3) Just after receiving "%" code at the end of a part program



(4) Just after receiving"%%" code which indicates the end of communication.

2. t1



"t1" indicates the "RS232C ready wait time" set for parameter.



(b) Multi-file punch (CNC: master, DC2/DC4 code output)


```text


                                                                                               '^^^`^' ".^`^
                                                                          .  .'. .    ..       >]_?~-!'_I-][`
                                                                         '[1+<+__]+>l"_??+_}-_{+:+~-_+__+<-?'
           '^^^`'''`````^``````'''''`````''''''''''''''.'.....''''''''....```'.'`''`'...`''`''`'.`.'`'`'.```
           `""":,,,"`^^""::,,:,^^^`":",:",^^`",:,,,,"^",^""",""",:::::"^":,,;III;II;,:;::;IIII;::,:::;;;I;;;.
           >!;i    l<I<ii""l:"li!lI:;+!,+"l>!`Il:;:Iil:'~:;I'l:;I,;:;::iI
           !l;i.   ">i<<~:;i;"!><I~-:~>>+;Ii-,"I<_i-<-!`_~~<">i~<i<>?~~-?'
                  ``   ' ... ..  .   .   `'  .
                  i~: ,<~<<<<+<>+-<>:l_+~>>+~<]<
                      'I"`.^^"':^^`^` `^`..' ^'""`;`'"```,^..`'''^`'..,;``''^.'.'^..^'''.' ...'.' . .. . .^.
                      '><_^-_+,_+<i]II~-]I;I"i<+<I]<"~_>~_-`I]->i[<!::}?-><,+!~:;~~^+~>i-l"__~i,~"_"-~?{~:}[^
                      ;i_i+-+`<+~!+_<<" l~-:-<<!_>:_-~;~II>>[I?]I!<<<--!"_+~!_<i!:+,i-_>__-!+-~i+"    '.
                        . .    ...'....   '..'..`.'```.'..'`'..`'.``'`^`.""``^``''^.`"^^^""'^"^^"'
                    >?;`??+:ii+-.
                    `"' ^^'.`^""
                .l,,!:^"'`^":`',,""l;"^I^''^^^"""^'`",'`:"`"l,,^'^^,"'^:`^"I,"^,`'```"""^''`,^````^,:^`"^'^^
                `;";l"i!_I '!";"!I!<:,ll'll,`,""",:^"::^I`I`l`-~<. :";`l;;li^;l,";:`^"^^^^"'l^....."l"^:",'I.
                ^I;>:^I-)__lI"~,><<+li;l'+_;l<i?+~+;^"l!;'?"I'~[[+>:`<lI<~_il<l^;?+,+~<}<-~"!^ ''' ^I;~:^<l:.
                ."`^I:,;;";::`',".^I,^^;^..'`''^"^^`",'."^.`I"IiIIl:" ';'.';"^;I^'`^^`":,,"^!,^````;<""l:`^:
                .l^'... .'.''''. l"^,,:` '``'''..'''..'^;,'. .      ^l"`"",^I:'              `'^`",`  . ..`^
                '<,`````^""^"^`..i;i<I<> ^""^`''``''``^l-i'```''`'^':?+i<>~I_-,        '`'  '!<]il-~  `^"^>+
                           ^  ':^.`"'.''^` '..``''``'''  ^^ ..'^''
                          `>^ "<<<l_~,>->_;!l<<+!+<-_I<-'_>^]_>?~<'
                          ;_' "iii"<~+"!ii>!;<>!>>I`~^;<~:l~`!I,_<~i<~>I>i;+<,!<<>>!>i!"<!<~><i'
                          :+' ^i!!:<i>l!iII!I!Ii!+;"I>i!!I>""~!,"_]<~i;"i!>I!I;!<I!iii+!>;Il,:"'
                          ,_` ">l!I>!_<<>;;ii!:>!~Illl><>IiI`<l' !<i>~:;ii~!li;l!"i!i>>>I,
                          ,+' ^!!l,>il"<^><!i!<!<l_l<I^!l-l;>,+~-lil i!<l' >?ili:">>_::l;i+;-?~-_-+;
                          I-` Il<+_+~!<i~><>~!<!!-+<!i<_~;i?<iiI,<"~!<>i!,i~:!>>iiii>_~~'.. .....'..
                    .  .' ^,  '",:,";;:",^":,^:l`;;:`^:;;^":,,:,^;'lIlI;:^;:^"I,I::::llI.
                    -["l[>i:<~?!
                  ...'  ....''`......  ..  .....        .
                "I^^l^;:^^^I,^^i:""^^l^''^``^"""``I:''I,'"l:;:"^^I"'';``"""I^''``'``""",I:^^^``^^^,I,^'I`'`^
                :.>",.~_[^ "~><<I>l~i,'<i,:;;I:Il"^ii<~.>':'_<_. ;!l>!;!;ii:`!!,,:,::;:^;:   ..    ,!li~;Ii,
                :^i:l`>---?I<!l~l!l>iI`i>:<!i?i>>;:i<!+^~"I`+[?-~;i>i~I!!<~l^<>:~ii[~+>::,  .`^'...;~><~>>~;
                .' '"```'`",^''^..   ``..`^^^'...'"^..^"`,:`^"^"",`  ,`'' ."'''```^^^''`:,^^^'`"",^:^`':'''`
                ">^`'```````'^':>:!:~i^.`````^^"^`''`:<l`''^^^^''' >iI::I!!<;         .      :,lI:i:  ''''I^
                ^;''''''''. '' `^^l";i` ' .. ....  .."i,...''''.'. ;!II;;;,il         .'     ,l~!"ii. ^^`^>,
                          ^I  ,,:>"^::;I`;',;;,;;;;":`.i"`,,;;,,^;;^,".',;,`^;^"::",:::^`;;"";` ",'
                          :<. i~l+il~+l~I>I>~~~+>~<l-_"[:l[+>~<!;~+!i<:l-~_ii~;~-i>!><_l;+<i:_>'iii'
                          !~. ;><l:-~~">>!~::~-l<<,"__I>!~[,:<`+-]<!_i!!+"<i:I_+"!il+!i~;
                          I+. :>!Il!!>iii:;iil:ii-,!;i><>:+"I__<^'<_iil";!I-li;:i~:-]<<ii;"
                          ;~. ;~iIlii+l~;;i>illii>!>l:Iiii!;"!!;,,il!+_i!_-~":~l<!:lii~<l!,`^``,^^^^^`
                          ;~. ,lill!i:;l,i<!!!~;ii<ii;"ii+;!iI<i<l!,.+iI!!i^ "_>!lI.!li<"~"i~;>_i~+_i!'
                          i_. ,I~~->+;+><!+<i<~i~+<<I>___"i]+ii,:>^-~~i+;l<<:i>l<>><>-~i
                  ::  ":""^^',:","  `..    .  '` ...  ..... ..''.. `''.'.''...'.^.'''``'
                 `-~. ,!!>!?,i>_+!
                    '' .^ ''''    '...'.'.'`'^.  .'' '``'`  . .. .
                   '_]'i\+->>}<I-_]I_+_!<_[_l__,~+~};<_~]~^I+_-[_~.
                         '.                 . ....                ...
                        ;-<"               I?~l!~i^               !++;   `~>I               l_~!,+>,  ^~<<.
           ,!;I.        l`l'               ;,i.;"l'               I:;' ` ^;:"               `;,:'!,:   i:l
           !}])I,!!<>!`": ,:^":::,^^^^^^^^^: ":; ":^""""""::::""""I `:"]!l'.I^"""""""",,:,"^,^ ,," I`":: ;"'
           '''^''^^"^`     I"              +,     I^              <;   ''   :,                ,>   ,: ._
                            ]:`^`^^^''''``.I.     .]:`'''''.''``' l'         ~<''........'`.' .^    !~'i
           I]__~+".''.....'';;^---?_~-_<`;?>^......:;,_~+~<~-?>^l-l`...:.....`+^~<-~<~++<^;]>:     ;>i^l
           ;+<-_;;i~+>`^^^"",. i>,>_!l'.  ,","^^^^'^.'-~!+_!<`. .:^"^^,-i"""`^" <-i_-~l"`  :""^^^^^:>^ ",^"'
                          :<<^;i!>!              ">>,I^  ..                 llI^I. ..              !;l`:
                          .'^.",",:              '^".^                      ","`"                  ;;:`;
                "<;::II::;,l.   ''  ,l:":lII""":;'".^^,^,^"`I:^:,:"":"^'^"^^`
                I+>~+~~i!~l-"   ";  `;!iIil!:;l!+^i,I>>l<";^<il;>!l~+l-;>-_~+'
                                    ^I" '::I`!i;'"::;,;;"^!;';:;^l;'^:;:"
                                    ";; "Ill,i!!'^!:!;lI+,l!,!li^I>^;~!;i
                                    :+l ,<l>,l><!<^ii~!i:!li;;!lil:>`II>;i,<~!>>lI<li!Il+<l:iIiiii>!>`
                                    ^l, ^:,:':;"":`:,,"l,,l:"":",:^:`;:I::';;;":"^I,:::^::"",,IIl;l:!'
                                    I-i :<~i:+_~^:+!<>!i-'l+':<>};l-l_~"~<+,<l>;~_i,il>-><!.
                                    ^I" '"",'::,'`,",""";'"""""^"":^`::^,`"^:'"::",,^':;,^"'.''''.''.'`..
                                    ;~! :<+>;?++,l+>_i~>?^I><>'l>~];<?~<!"i~+i_-+l>~i:-!>:+;i<>+<>+i<?_<i'
                                "^  ^'
                                >!  l;
                                    ^,,^:"l":;,^,:"`l!l;;;I"^""":'^":"""""`^""""''^^^^^^,^.
                                    `I`'ll+!~~<I;>< ;<>>i<<;;<<<]"><_;l!~~'<-iI~,<+_~~<+]_"
                   'I, Ii"l^!l`^""";'^:;,: '`'`,^ `:^^","``.`'". ''` ^.
                   "~i >?>+;~-Ii<>!>,ii<~>"li<~-_";~i+~<<i>:<~]i;~+]<-!









```

*Figure from page 12 (2346x3317 px)*


---



Send



Communica- % j



(CNC-,.HOST) oc



tion text 1



Cornmunica- %



tion text 2



4203-E P-260



SECTION 2 PROGRAM OPERATION



Communication %% I ._I ___



text n DC4



(c) Multi-file punch (CNC: master, DC2/DC4 code not output)



Send



__J



Communica- %



(CNC-HOST) tion text 1



(d) Multi-file punch (CNC: slave)



Send



(CNC-+HOST)



Communica- %



tion text 1



Communica- %



tion text 2



Communica- %



tion text 2



Receive



(HOST-CNC)



1 DC3 DC1



Infinite



Hts



[Supplement] 1. t2



}J Communication



text n ,___ __



I Communica-



) tion text n



\ t \ t



DC3 DC1 DC3 DC1



t2 t2



Hts



"t2" indicates the "RS232C ready wait time" set for parameter.

2. t3



"t3" indicates the "RS232C ready wait time" set for parameter.



(e) Multi-file read and multi-file verify



Receive



_J I



Communica- %



(HOST -CNC) oc



Communica-



tion text 1



tion text 2



JJ Communication %% j



!~--



text n (DC4)


```text


                                                                                               '''`.`.'^.``'
                                                                             ..                +[_]!_"I~!][~
                                                                         :{]~>~~+]I~^!+]-+-??-}>I__?--_~_+?_
           '''''''''''''''''....'''''........................ ............```'.''''`...'``^'``"''^.`'`^''^``
           ,:,::",:;;;;;;;;;,,,,:;;;;;:::IIIIIIIIIII;:::;III;::;::::::::::;IIII:::;:::;I;;;;::,:I;lIIIIl;::,

                           .''''. ....   .''  '''..       .''  ....^:.            .    ..
             Il:l          l'i^^;><+~!<>~;^^<+i,"I<!!!I!l~!,,>>!^^^:-,!!!iii~>~>>;">lil;;^
             _}[},;!!<!;'^">:!  l]_~]?<!;'  ^!^  ,-+>?]_~I"  ,i"      -]_<lI;:ll!` iIii,;l""",:,
             ^'`^'`^",^^   :I;  '^`'"^           .^`.",``             ::"`            :>!`

                    ~_":1~?>i?>l<><_+:-<]+l"<+__-;"-~_?__~~:i<+_"!~Il>+i>_`
                    ^^. '``'.`'`^^'^''^'``'.`",""'.``""`^^`'^"",'`"'`",",,.
                                                                   ..
             "^``            I":l!!l;:lll,":i!>"":I;;;:;ll;"^;:I^^^I]";,;lI;;:;I;,,;IlI.
             ?{}}`^::II"`::"";  !_?_--_<<`  l_I  ;[-+]-__~:  i<;    `.____><<>_+>^'-i_!:^""""^`'
             ;:;I`:ll>l;.'...   "I;"il`.         ^!;^i!:,             li;".            .'''''''.

                   .!_`:]!+ll+I:lI!!!"><~i,^!!I!I
                   .li`^iIi:"!Il!Ill:,l;ll"^!!lil

                          `"":,,:":;I,^"^"       '"","""^""",::""           ,"^`^^``^^`^"^"        `^'
           ;]-_".'``^''```I';]-~]__+_:.>+l^"^^```I`;]]-?__?_I'<-l`'',>````':;,-+++---_i';[>:'''```"_{>.'....
           :<++;:>~~<l^'''^ ^i!"!>"'    .`"`^^```" ^>iI<iII    .`^.`^~,^^^`^.^<i;<<I:    `'"'^^"",,'^"`````'
                          _:             .l"     ~,             .I^        !>              ;:     ,+
                        `^;.             :.-"" `:l.             :.-"^      "!".           "'~!^. ^:I
           l[++_+"....''l."^`^^^`''''''''!', i`;'I^..'.''''''''.i.:',`'!`'.:":;.'..''''...;"'I':^;`I.......
           ,_~--II<_+>"`I<il`"^^^````````i`>><i!i!,`````""""^```i^li!>"_l"^;!ll^^^`^,,,^^^l;:iI~!iIi"^^^^^^'
                        ,,"'             ; ,:^^^:".             ; ^;""     .;:`           ". ;:;';;^
                      . I                i><.+                  <<<.<                     :~+.i^
                      _>~'l~<~I          . . <>~'~"             '.'.`                     .'`.I_>,;;
                      ^'`.^"",^              '`^ ,'                                           .::',:

                ;[++_~~>i<i-^   ";  !?'
                ^::;I:,"^,^;'   .`  ^:
                                    ^?~`><]i--~!i-_`>]?_-?-i,>~~-:i~-li<<<"l+<i+I!~+<~i~_~:
                                     .' '`^`""^`'^" .`""""^`.^,,;`",:`^^"" ^:"`,`;::,:^:::`
                                li  !-.
                                `^  ":
                                    ^+-"++[>---ii-+^<]]--?-l;<__-:i++i_+<_"i+li~,l+<~-<~_~,
                                     .  ..'.^`'' .`  `^"^"^'.^,,,'^""'^^"" ":`'".,:",:^::;'
                   `+< <[l-l+]l;~+_;~i<;i!~>l~i"ii!_^
                   .," `"^^''"`',::':",`^,,^`^,',,`;`
                           .. .                           ...   ...:^.
            .l;,::^       ^;:l"^iii!il>ii"^,+>I^"!!i!II!i<:",<!l^"^<+"iiil!!!!~!l";i>il^:
            '?}[1?!li>i"^:!l;,  ~?~~]_>I:   II'  <?~+_-_i;   !I`     ^]]+~ll;l<II ^>I<!^!,"""""'
            .^^^"..""::`  'l!,  `^'`"`           `"'^:^^.            .;:``           '>!i^



































```

*Figure from page 13 (2346x3317 px)*


---



4203-E P-261



SECTION 2 PROGRAM OPERATION



(3} Parameter Settings



Before connecting an external device, it is necessary to set the following parameters.



For details of parameters, refer to III "PARAMETERS".



(a) Optional parameter (bit} No. 1, 8, 12, 13, 14, 21, 22, 40



[Supplement] 1. In multi-file transfer operation, since the tape delimiter code is fixed to"%" or "ER",



the parameter (No. 1, bit 3) used for this setting is not used.


## 2. Verify in tape reading is effective only when the input device is TR: {tape reader).

Therefore, the parameter {No. 1, bit 4) used to set the device is not used in multi-file



transfer operation.


## 3. The multi-file transfer operation supports only standard DC code. Therefore, if the

parameter setting* is for "DC code control type 2" or "no DC code control", an error



occurs.



Bit 5 and 6 of No. 8, 13, 14, and 15:



Setting should be ON for bit 5 and OFF for bit 6.



5261 Device name error 1 'CN0'



Varies depending on the selected device name


## 4. In multi-file transfer operation, since file name punch is fixed to "yes", the

parameter (No. 12, bit 2) used for this setting is not used.


## 5. In multi-file transfer operation, since feed hole punch is fixed to "no", the parameter

(No. 12, bit 4 and bit 5) used for this setting is not used.



(b) Optional parameter (word) No. 6, 34 to 42, 45, and 57



[Supplement] 1. In multi-file transfer operation, if "5" is set in the punch device name designation



(No. 45), it selects "CN0:" instead of "PP:".


## 2. In multi-file transfer operation, if "0" is set in the tape read device name designation

(No. 57), it selects "CN0:" instead of 'TR:".


```text


                                                                                               .''''.^ `..''
                                                                                               ,]]?-i+ >;+[>'
                                                                          _]+><~<_~l<'_-]~----][;<_+---+<~~[I
            ......''''''''''.'''.'''''''................ ......           '``'.'`''''...```^'^^^.^'.^'^^'``^'
           ',",,,,:":;;,,,,""^^^,^""::::;:::IIIIIIIIIII:,::IIII::;;::::;::,::::;;;;;;I;:::::IIIIlII;:,:,::;;^
                  "~;  !!Ill;llI`<I>!:;I
                  :>I .^;I!I:iI!.ll!;:_>
                      .]><ll:`;;lIIl>II^~;;i<ilI>;l~!l!I.!I!"i!l!l!!I"I:"l!:!l,>!i;l;I:,I;;l;IllI"
                       I;,:"^',""";,:^i"l`^;,l,^;`:;:,:;.,^I'l;;lll!I":;,i!";i,li!l!;i<l<!!<I>i<!;
                      `+ll"-<~++^>l!<i>i!~~li.:~~i^<:!~"l++~~<+_il><~+I
                       '`' "`"`".`.""^"`^,"`"' ",".:'"" .`^""";;"':"`;'
                    "<!.!i>!I;>:IiIlIl!iI'l!!"+l ^`^i ;i."i^.I, !: ;i'^<;
                    'l: ^;I:,:>:l!;!I;l!;';Il'!!'.'`l :!'^!,.;I^l".I!^^i:
                 ;>::,;;:"^,l    `   ".`"^;';;.`""";:"'^"^`""^. ^^^`.,^.`""^':::":"`'``:`^`:"^^^"'",`'^':::"
                 i<>++<<!ii!+.   :^  ~l!<i_l<-li~~~]?!l?_<~?~<l,_<~-l<?!i]+~l[_+<+_l;!i-iiii+__!_;"+:"-^<_<;'
                                     -_i!-_<_!_-_`!_~"^,,-il?"~__>l_I!?+;!+_~i+:_,<_l!~<_l
                                        ' . .               .                 ^    .   .
                                 _:  <-<-~:<,]]>:;<++<iiIi;]_>~_il:<+<:_!>!"_i,;i>>l;_i!!i">^<?",_~<>"<~~_>l
                                 '.  !~!!>>li!l-l:!+<~~-~~I!]~;;ll~!+~:~><ii;i+!<+i!_<<!i!I!;!;!><_~l;~~[i?~"
                                     ll<>_~lii;<><~+i!;lIl^,!I".^,l"I::!!I:l,l<:,;;;<Ill;,l"ll,ii!I;":!Ii"l>"
                                     l><l+_,"~~<!+ii;
                                 ^.  ^'    .`.`  . . ^'......`.... ...''..'' .'..'..''``.  .. .^.  .. . ''.
                                 _:  !i_;<+!+I~<I<->~[~:l~-<_{~i:+>__>!_I><_I~[-i-1+>i-~:<>?_ '<i_!__i_^i!~_:
                                    .i~>~>>_-<:-_-i+<;>!_i"~_!l><}!l<!+<!!_<+I_,il,~iI~+Ii>~-I!i~_!<,:?li<>~^
                                    .<<>ii>""^'"^^';^."'"` ^^'^"^,`^"^""^'I,"`" "` ^"`^^'^",:^,,""^^.^;`,,":.
                                     ::;""I
                                       .-<:iI<<l~Il><+;`-.l~"^>l`>l>"<<.
                                       .;"`^",,^"'^`":`.l ';' ,"':", ,;
                                       '_~_-l!:~!!i+Ii~,![il_;i~l>"<i<;~+_:i<,>~I_
                                        ^"^"`;^"""^^'`".'`''".^"'"`:""'"`' ^,.,,`:
                                          :?--l <~+>~~^>-_~>;-l<:;^>+-]I
                                           '..  ..''''..^''''`.`.. :~!!^
                                                                    ,.
                                                          ^~<>i!">i!i!!<!!"!:!~!"i><!iii,iiII!;"!!;!'
                                                           :I,;,`lI;I",I:i^I`";:'!IlIIll^I!:,l,`!I,i
                                 +` .<".il+!;-~ li<l<_l ;>il!>:!" :!,;l <<^ ;!:!, I:;,l.^l !IIl^`l 'l!i; ;<!`
                                 "' .i!;<<~<>>l><i:>_lilI[<l~+<~~:l_<~!:~[i:l~!<i;>~~~+^`l ,;ll`^l'.!II^.";l`
                                    '!>l!;;i>,'>l; ,i';~`!"">!i;;!.Il!`><<!i!:I"!!`><<>.
                                 ;  .^ ''`,."```''^,`'..`'`".' .`''''``'`..'.. '.'...` '`^.``'` "`..'''''`^'
                                .+` '_l!<+]I<+!<_>i_?:<-_><?<<;!_~+<l-++~ii_l~<<<<,<l___>~<^i+;^]~i<-__<~--~'
                                    .-->.,_:"_;!;_~<l?<!_"~+_+i_!;+_Il+_[>_:+:!~I;-+_;
                        .                          . .  . ...       ..'.'.".'..'.'``'.
                    i]I`_--+~~+I++>-<--]!;-<~_?I[<^<!,]ii<,?<'?-`!>~i~_^
                     .   .  .'''`'.`..''  ''..`  .    `  . .' '^ `'``.'
                 +_>_>>>!<>_>    I  .>`:>!~"+~^l!il<+I.i!!I~!l: >'ll i'l<;ll!>>"iIli+^i>l!i;^!>!<,!>i>il<~!l'
                 ^^,:"^^'"^^"    '. ._<l"<_!"_I>__>_+;i?]?!!<<<!>IIl;>~]<;"""":^I:";:':;:,I,':I,l^:IIli:!I;:.
                                    .lll :ll :"!i!lII ;:Ii^ Iliii>^I;.;I'.
                                .;  .^ `"`"'l^`^''`"`'.'`'`,'' ``^"'....`'^,^`"`^'``^^'"^``''```^'^^'`''`"'`
                                '<' '+I!><_!+_l<_<++~;+[[++-<>,i,>;I~i]~i<i_+l][+I!_-<![~>~+I<-i_!~?~-]>--<>.
                                    '__i.<>> i:+-?>+>`<<-+;'l>_~~_Iii`i<!^
                                       .   ..  ......    .   ....' .































```

*Figure from page 14 (2346x3317 px)*
