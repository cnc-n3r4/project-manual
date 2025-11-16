# III SECTION 2 PROGRAM OPERATION 15. DIRECTORY SELECTION BASED FILE OPERATION FUNCTION OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-15.-DIRECTORY-SELECTION-BASED-FILE-OPERATION-FUNCTION-OCR.PDF*

---



4203-E P-277



SECTION 2 PROGRAM OPERATION


## 15. Directory-selection-based File Operation Function

Operations such as writing files (part programs, etc.) to the NC and outputting files from the NC to floppy



disks are collectively called "file processing". In order to execute a file processing operation, a command



that describes the details of the intended processing must be created and the created command must be



given to the NC.



15-1. File Processing



15-1-1. Procedure for Executing File Processing



(1) Calling Up the Command Creation Screen



Press one of the file processing function keys - for example COPY or READ - to display the



command creation screen.



(2) Creating the Command



Create and editthe command on the command creation screen. Since the first part of the command



(which specifies the command function) is entered automatically, the user has only to input the file



name(s) and option codes.


```text


                                                                                               .^^^^`" ,'`""'
                                                                          ..'.''..    ''.   .  I[_]-~_ ~;?<i^
                                                                          _}?<~+++_l<'-_}+_??-?[:<~?---~++<?,
           .^^^````^^````````^^``^`^`''''````'`'''''''''''''''''''''''''''''''..`''`''..'`''.''`.`..`'`''``'.
           .^^"::::,^````^'`"""":"""^``^'",,":""^`^^^":","",:,",,""",,:::::'^"""^^^,::;IIII:,,,::,:IIIIIIII;`
           '_-+    ;{?_><i~+!i!I^i!<_~!!-~lli^-li!!!l+^]~->:`_<lI!Il!<l;;;.}!";;:!i;,;"
           .~-[^   I1?{_)[]{{][\l)1|[\{[{{1[[i(1\\||1/:}i|\]:11f)f[1f(1()[;1<({{|()((1-
                 ..
                 l_~_>]-~><I_>_ll?,~+-<~!~]~!!-__l~>i]<_<+":?i"I+:_<!!]>^_l<:!<-I<]!<I?~>:+l>;i_i!]~,<;~<>i>,
                 l_~~ll<!:!!-~>_l+>,l<><+,_]!!<<>i+>~-<;'-:;>>_;il:>ili!<l!i_>I_i!>i-~<>!l!iii>i<^il;iii<_<_l
                 ~~~<i<~!I+><i<~!!?Ii+>l>,i+!<i>>~++~i?"^>:!ii~;!!!<<~!>_;<!~>l<li~~i<i~!~_<l~ii>"!I>>!i!~ii;
                 i><I!_<<i<<~;i>i"-<~>i,>;liI!<<l>~<i_i><>~~<~>;<i-Ii~;<>~_-~;+<~i~~;;!~-_+lli>>i~?~+;<!~!!-;
                 <_i_;;<,>_l~[>.                              .
                 ^'.'
           ^~[:>"  ![~};}?~~~+++_+__.
            ."...  '.':.. ^,","::^,i
           '<!,"l" ;+!li>~;!:i>">iiIl><ii!~-;i<!!<<<il>'
            ""''^'  ',:"""^^``,.^^:,^,^"!'':`'`""::;,"!.
                  :I" .!;!!I;:I;:>:^l:,,,:;:;"l::;!,:`!:;II:.
                  ;;, .;II;l~^ll:l!":;l,:;!;l`::l>>ll'!l;!l;
                      `>:lI; ;:; I,IiI +i'";,;lII;,;^i;;!l;`:!lI:..ii^"!I!Il!I'!!><!,^l'~~li>"'.I,'!l;!I"^iI`
                      `!!_~~;<<~"~!>_<;!_I~<>>ll!I;~`llIl!l^"l!!:..:!`"il>;<!!'I;!;:^,i'l>lii^''l;`<>+>+l"i<"
                      'l!II:i!!:;l!<ili`i!!<>;
                  `:' .^...^.  "' ''.. '  ..
                  i?l `>!~_?<-!-+!li~i>i_>~I
                      .:^^^"`^"`^`,:",^'^^^^"^""^^`,,`'`^^^^^`^`^^`"^^'``^^`` ^,''''"''"`^'''`.`^^'.'''''.''.
                      ^<i__]>>i~i+-~<-_I<~><i_i~!>;>~>l><ii>?i~!+i-->~l<>i_~i'I?<~>!~<!+<_i-+iI>i_+;<>>+>?_<:
                      '~<!i<:<]<>!_~l:<~"i>i>i_!~l~~<__i>:<;>i-+i~<!_~~<<--!~?+^~<>:>_~I~_>;<<<;<:<~<>!_<;?-^
                      `<~>~<+_I+!<;~++>!:<<~<<`.. .'......'.'.''.`''^''''^`'`'"..'''^^`.'"`'`',.^'`"^`'`^.`".
                      .^:^":::';`,`:::,^^::::;




















































```

*Figure from page 1 (2346x3317 px)*


---



4203-E P-278



SECTION 2 PROGRAM OPERATION



(3) Executing the Command



With the command creation screen still displayed, press the WRITE key.



The created command is given to the NC and executed.



Any.screen



88[



lfm08BG



(1)



71/1,



Command creation screen



tlC0:019\.AY~



tF2l -> Ji01:•.1i1nt



!'3)



l'l:O:•,MIK



TO OISf"I.A'f '1ffER UUXE$.Wl'8l :P'FUS~ (Fl].



IIFVT TI-ii: IEVICE .11AE NI> Flt.£ M£, '71iEN Pre$ !WRITEl ID.



OS:Ml!,.'T QEVUl: -. a 11'1:



CE:FM.11..T F~U ME • •.lilN



IIOO(



O'§ffll{l



(2)



IPAO!JWI Of'ER,\Tltw.



_,,.



'/EAl;\'IO)PY



T!UIISFffl



ur:a: ot!PL.l'f



[F.e) 101:•~11•



(Fl] F00:•.111•



rt OISA.A'f 01lER IG.XES.AFTE'.A PAESSftG (Fl),



INPUT 1lE O£Vla: 1WiE" NO FILE IW£. nB !'fESS (lif'llf] m',



lEFAUlT 1):\/'tQ. 1WtE = lCIJ;



DE:F""1.T Fil..E IW£ • •.MIM



Fig. 2-2 Procedure for Executing File Processing


```text


                                                                                               `"^^'" `"'^"^
                                                                         .''.''...   .'..  .  '_]-]i[`lii++_
                                                                         ;}[~>~<+]l_'<~[_~???_}ll]+___-~+~-~
           ^^^^`'`````^^^^^^^````````^```'''''''''''''''...'''''''''''''..''''.''''`....''`'''`.'`.`'''''`''
           ::::,",^`":"""^""^^^"`^",,",,"`^^;;;;;;;;;;;;,,,;;;;;;;;;;;;;::::;III;II;::;,:I;II;;;,:;:IIIIIII:
                 .<_. <~!<ll_l!:~!,!ii!ll>I!^
                 .;l' ,::;;:;">^:;`":;::,!,;'
                      l-+-^-~;:>i!>i<!l,!!i~ii:!>!~~>,+_!I_~i>><~>^~ii~Il<!:_<~i+<;>iI
                      ^,^".""``"^^^^:^^'"":,"^.`"^::".,:`^;I,,l::"`l",;,";;`;",","^l!I
                      ;-<!I<<_]~i:<<!><_!<:<:_~<~,il!?i,]-,!>>!li<<;~~<,
                        .. .'^^^''^^'``"`^'^`I^^".^^`^"'^"'"""^",:,,,::`
                     .l,^,:;.
                     .!+___]<!!l;,,,,,:;II;::;::"""",,:::^  '::,:,:;;;:,,:;,""""",:::::"""","""^
                     ':i()[-{?[iIIIIlli11{>IIIIIII;Ill!l>!^.!!)11[1[}~I!!!!ll[1{_!!lll!>>>ii!!>!I
                     `I                                  :,.l                            ...   'i
                     `I                                  I,'>                                  'l
                     ^l                                  ;"`i                                  'l
                     ">                                  :^'l                                  ^>
                     ">                                  :"';                                  ^<
                     "i                                  :".;                                  ^<
                     ^;                                  :^'I                                  ^<
                     ^;                                  ;"'I                                  ^i
                     ^;                                  ;^'I                                  ^l
                     ,l..                                ,''".^`""`^`".                        ^l
                     ,l`,:^I,:":,:,I:I,,;``"I``^:i!"!^^^';`',`~~-}--~]!,":I,,"l""^l^^^;li";:"`'^!
                      ;:![!l~{+!~?~!l-l;I^,Ii:",:!?Il"^":;  I":-:`;?<^l]+>l_>^;`^`I^^^!;{i;,^^"I^
                       :>!:-i>!-i!l~i><:!><><<+!>l!;iI+>,    .. ...  ........+Z"l<:^``'. ...'''
                       ";:"!l;;!<!I<<_]~?:;;l,I:I::,I";;"                    ~k  `:!;I
                                ^`  .!.uu .                                  ~p 'I<j)l.
                     `::,,,"^;;:`^,;,  Jz                                    ~k ",-(+!
                     `>---?+>_-<!<~-i""}[,"``^"^",""^^^^,.  ',,,,"^^^^^^^`"::~c"`,!Ill^^,,,"^`^'
                     ^:_11{1)-]I!l!ll!~{}1illl!!iiii!!!i!!.`I_)|[[1[1iI!ll!!<1)(]i!!!lll!lli><>!"
                     :^[j~lI;IIlII;:::;llllIIlIIlli{)?+i!i`^^]/{[-_~__+lllIll!<!!!>illIIl[)1_!l:l
                     :IlI'                             .l!'^"i";ll;::I;                  .'.. ,I:
                     :;I":::,,:";,^"^^^^^^^":"^^^^^^^^^^;I.","^`'^''^``"``````````````````'```::,
                     :`,f~!_1~[)<:          ..  .      . l."^"t_l_{<](?i. ... ...'''''''''''''.":
                     :`,]i!I{]i1:``;^^",`^.              I.,^^]i;;_]i}I'.^'''`'.'              ",
                     ;'!}+]?]1>()(]?<{)_]~[;lil:l.       l.,^:}---+[<}1][__-\+{i}<;>l:!`       :;
                     :'l1{I--]\?,l[l      .......        >.,^:)}!-]_{)l"[~^ ' . .`''''`.       Il
                     :`.''. .'^   .^                     <.,".^"'.``:.. .,.                    ;I
                     :`                                  ! ,,                                  ;I
                     "''  ..   .                     ... ; ^`.                               . ,,
                     ,"^;!,l-+;!>];l}){l_1}l_]l::;;,l`^^.! ""`::`^i<::I_I,+}{>>-}l!-<:!":":^^^':,
                     .:^l~,"l-!,:]~:+---~{}li]~l;--I;"",;, .;,>]l,!}_lI{1I~]1~!?)+I]-<;<?>"^^",;.
                                       Zf                  .                 /m            ....
                                       iYt(|(|||(|||||(()(jnf(||(((||(()))))/C_ .
                                         ",:I;;;I:;::::::;I:;III;II;IIlIl!!l;
                                        `~l:.I,:.>::;;I:;""l":!:;,,l,:^Il,^l::Ill!I;^
                                        '"i>`::,':,;IlIll;"!:,!!!I!l:+;"!!";II!i!iI<I

































```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-279



SECTION 2 PROGRAM OPERATION



15-1-2. Method for Creating Commands



To delete the File "PROGRAM.MIN":



The procedure used for deleting the file by directly entering the file name



(a) Press function key [F3] (DELETE) in the PROG OPERATION mode.



The command creation screen will be displayed.



"DEL", which indicates the DELETE function, will automatically appear on the command line.



!DEL l!i1



{b) Key in the file name "PROGRAM.MIN".



DEL PROGRAM.MIN.



(c) The command is now completed; press the [WRITE] key.



The created command "DELPROGRAM.MJN" will be given to the NC and the file



"PROGRAM.MIN" will be deleted.



Copying the File "PROGRAM.MIN" from a Floppy Disk to the NC Memory under the File Name



"S01.MIN":



The procedure used for copying the file by selecting the file name from the directory



(a) Press function key [F4] {COPY) in the PROG OPERATION mode.



The command creation screen will be displayed.



"CO", which indicates the COPY function, will automatically appear on the command line.



co r,~



(b) Enter the device name "FOO:" and the file name "PROGRAM.MIN".



Do this either by keying in "FOO:" and "PROGRAM.MIN" or by displaying the directory for device



"FD0:" and selecting the file name "PROGRAM .Ml N" from it.



For details on selecting files from directories, see 15-4, "Selecting Files From Directories {OSP



Format)" or 15-5, "Selecting Files From Directories (MS-DOS Format)".



FDO:PROGRAM.MIN



(c) Key in the rest of the command", S01.MIN".


# I co

FD0:PROGRAM.MIN,S01.MIN1i!I



(d) The command is now completed; press the [WRITE] key to execute it.



The created command, "CO FD0:PROGRAM.MIN,S01 .MIN" will be given to the NC and file



"PROGRAM.MIN" in the floppy disk will be copied to the memory under the file name "S01.MIN".



Copying the File "S01.MIN" in the NC Memory to a Floppy Disk under the File Name



"PROGRAM.MIN":



The procedure used for copying the file by selecting the file name from the directory



(a) Press function key [F4] (COPY) in the PROG OPERATION mode.



The command creation screen will be displayed."CO", which indicates the COPY function, will



automatically appear on the command line.



IJj



(b) Key in the file name "S01.MIN" and a comma",".



CO S01.MIN,


```text


                                                                                               ."^"^`, :`^^"'
                                                                          .''.''.'. . ''....'..;[?-->-.~l-i]I
                                                                          ~{_<!~~__l>'__]+_]]-]{:<~~]--~>~~-;
           .^^^^^^^^^^```^``^`^^^^^^^`'```````'''''''''''''''..''.........''''..''.''...'''`.''''`'.^'''''`'.
           ',",,",:,"^^^^^^^":,"""",""""^^,,,,^^,,,,,,,:,;;;;:,::,,,,,,,,,:;;;;;;;:::::;IIIIII:,:,:;;IIIII;;`
           .i<""i, ,-<>>!>l<;">I!!~;I"ilIl!I!Ii!
            ":'`:i;!_<!lii;!!,!i__~i-!!i!!>>+>~~``'^^^^^^^,::,"^^^^^^^^^^^^^":::,^^^^^^^^"""""`^
                 :. l<,+~~+<;_<Ii~_"!_?_++?_~?~i[~_I... .....................''''........'''''.!
                ': .,,`"::,:`,"^.';''^,,",,"":"`;"^.`                                          l
                'l':-+-!?<+_]1~]<>+??!+-,-]-]++-i]?l]]i]~l1--_}<>-+[_+[<+-+>{?l_-+[<....''''...!
                 ^^`''`^"^`'`","""^'``'''":""":;`'^^`^``""^","""^^^"^^::`^",::,""`^^^^^,::::"^^"
                    :]~ <>_-_:~i<~_~;i+_:]<]l~-}<~~l-i:~;]~I>~]~_~,+-+~___>++-"!i>-<
                    .`' ^'```.```''`''`"`".^``'''`' '"``.'^' ..''^.`'.''`''^``''^^""
                        l!_:!_~~<+?~+Ii>_?<<:>~<~~i:_-I<_"_??-]__+"
                        ^":"'..^^`^.''"''^`''"`.":`.,""`^.``,'^`'`^   ... '. '.          ..          .
                        l-[-;`!]~<+!><-++{?<>]?l_1+>?!}!+~_+?_~^<_-l[_+_<-]~-{-:[]-_-<"-;~?_:<~<_<-__<!<?^
                             "l!ii,^`Ii''''``",,,""^```^`^^,",,:,,`^^^^^`^^^;". .'.        .      . .   .
                             ,l>__; .?|' .          ..    .........'''''....^,
                    ^;" I:"':^iI,:>;:I:ll,Ii!!!!ii!<>!<il;````````^"""""````^'
                    ;_! <~-;>,+~i;?~:><l~:"i>~<~~<~-~i[+_l^'''.....    ......
                             "l!+<`.,<<!l>~<i~>;<i!:+: ..^"""^``````````^""":"
                             ^l>_+l.^li>!i>>i+_!]<>!)I... . .'`.'. .  .   ''::
                    "l: i>i";l>il!!ii;I,IIl";ll!!!>il"!!i>l!~>l_+[~i_~li!l^^".
                    ,!; ^,!^:I:,";;;:^;`:;I`lI,l!!i!l^l:Il"";I^!!;;^I!;l!!
                        ilI`";;i<l,";l;;ll,;';<<^ii>Ii>~!>+I<i>l.Ii:;l`;I;!"l:;<!,<>;,lII>iI:~l.
                        :+?~<<_[--+i_?~+i~~<"i!<~>!~>il;;l!,l;:, ll^;i^~ll!^;:,li"Il":!I;ll!^ii.
                 ''.    .iI~!!+~<<]li<li i+;I_:!-<~<<!          .                                       ..
                `l`"~i>i!:I,~I:ii>,<~+>!~<><~~<?_~;I!li:!!+ii><l~+i!li;+iI<_>>?~!!l!I:l!!iI~>!i>!;iilIl;,:;
                ^: .II<<[](~+1?+<~`";!!l!!li<iI~>i`:!il^i:;i~i~:;ii!:i">>;!~;:+>!liii">i<+^>i!;I+l!_+!+;  I
                ^:     .,<l"^<>!,                                                                        .I
                ^I....`~+_l?><<_]~__;?]?<>?;i~?-__-<]?I][l--;]]]+]<?!~]<>]~:~->?!~~_<!-~:+~_~-++!        .I
                .:^^^```""^"`,,:,:,,""^`^^"`""Il;;l"^,^^"":;";;II;,I;"":",,^:I:;:":;:,:;,;:llll;I^^^^^^^"::
                    I]l.~i__<l~<i~<iI_<+,?!};+<>?~ilIli_~l++?<-l!-~~-?_~<~-<:<><+;
                    '^' ^^```.^`````''^,'` "``'`' '''^``^''.'``.'^.^^^^''^^^'^"""^
                        >++"><i>i~+>!;<<?_<>:~<<_+;;_-I_i:[++<-~+>.
                        ^"""''^^'"'''^'`^`''`''""""^``.```'`''",'''....'  '           ..          ..
                       .i~<i`!-~__;~<_+?}]~i_?;+~?~<:--<-]<>`~]~i?--~+}]~[[-;}?_+?!:_;>+~:+_~~i+<?i+<_'
                             ";ll;``!!``'`""""^^``'```^^"""""```^^^^``^`,:,;I"'. .      . .    . .   .
                             ^I<<l  -]''..       .. ...                     ,"
                    ,l^'>;lI^!!:">ll;I;!ii!I;+i>i;:lli>~l;<l,;llI;;<~~>>i>!i<::I;;`
                    I~;.>I>>`Il;`~Ill!^,iIII.;li!.`>Il;<i"!!':<I:I llllIi>i<_I<<i!.
                       .l;'!l:';I"I`::";:::,^,.^lll,.":"^"i;i;;;!I!I^l!l; ,."".I,"I;:;;"II""!,:;::",I"^l:,,:.
                       `_-i_<i!~>i_I<-!-+~<]<ii;I<<i"!~]<!~>_-+-+~]]i?~-I:~I~~,<>~i<~l_!I>l;<l~!ii>:>I:_<!i~'
                        :;>>' >l!:l>i!iiI>:i<'i<^i<!<;.!l<I!<<i~_"~<>;`>li"!:
                       `I"`.!;:;:."`.,::^;"^.I;,^`"^"'""`':`"^" ',".':'^ .I"",^:,^';:"^`;^^"',,""""`""'`:::;.
                       ,~>l;-+-_<,>i:-~+_+>_!>?+l!~<i;_<<<~+<+~,!_+;"_l_;`_?+-+->]Il<_<:l!<<:ii>+<+!>-!I~<?i.
                       "i!+<<_< <i^+li:.~_+_i>l+l<<~>;l;_~:_~~~-+l+?;<}[~~_~?!I>><i_];
                             ,i>>l^:<!i;liil!!><<l;!!l,iI^^^^^"::,""""^^^""";`  .  ''
                             lI<~l ,~+_i>~-<+-++_->[+?!(~.     .............;^
                    ^:`'I,"'",>:^";I,,;;lI,::;::,":,"^>lI:i>il"`^````^"""^^^^
                    l<:`<~+"l;?~lI__l!ll<~,<<<>>-!<:`"-<I,]_~l'  ...........
                             ;l>~!.;_<>;><~i>>~>~_l+~<:>>!^!i>i+?"^^^^^^^^^`I'
                             :;!!:.:li<Ill>i<~<><~;+<~ii<lI___><?        ..';.
                    ;~".i!l^Il!ll!!!!l,;I!,,!!!!!l!l;^lll!;ii;I~>?<<_!li!:>!;::;":l^I'
                    l>" ":I^;:,,"I:I,;"^;I,^!!;<l!!!,"ll!i^:l:"!lI:^lI,!>,I,^i>!;l~,l`
                       'l:; ,;;l!;: ;,:l;I;!" IIl^II!!IllIlIiii<:I~>l:<;,,><<: ;!,.l" !;II.:I.iI"^>l`^I:,^<;.
                       '<~]l+~]]-[<l]-~ii>~~!;>i<!:!__i;><!<ii<_><-<~l-<Il_<~I^~i;;+<;?~~i!i<"<<!"~_Ii<<<![~.
                 .'. ..'!li>!ii!!~>!~><'I"i~i!<<-_;I~_ll+l:~l,i<<>i;>:i<IIl>I>i!,ii!_i,<~:--:I+ii_'~]i"~_~~'
                 l^;+><>II::!I,>iI^!!l,!-__II;l<l;_<;><i>!lI:>:l;+!ll!:!+i>";IliI;iI,i!ll+!llI````^'^:
                 l 'IIl<?]|<-}-+](l_)]+>~Il.,,;ii^i!"!i>lII>"i,!;;l<<~!;>i~^!li+I:i>:I;<">+<!>.     'l
                 l.    .;:!!Il!l!>!i>l!'                                                            'I
                 !`.'',++~i~<<+_-~+II-??!?+:~+??~-+_?_<]-I]ii[-__[<?i]?!~1<l?}~_l]><<<}-:{-~+?~_:   `l
                 `^^''``"",,::""""^^"""^^^"`";I;";;^^"^`""::";:,,,"l,^,,^:"";I",`":::,;;,;:IIlliI,"","
                    <?":_<~~I><i>?>i;<_i![!-:+i<?I<:i,+-iI_-~>_:>---+_~><<]!:>l<_^
                    ^"''^^^^''"'^^^''^""`^."`^'^. ``''^"^.''``^.'`':^""``'^`'""",.
                       'ili`i!liI>>~::<>~-<<^>iI~+!'_>^!~"i~~~?_<+!:_~<^`_><+!^i_]>?]+;~_>:+<]_<"+~i<-!i'l-].
                       ">>~!><-<>?<"<<><~i,<;i~i:ill!li!>I!!+^'^''  ..   ' ''..'^``^^^''``.`'` . `^'^^`'.'"`
                       `I;:"^iil!i+I<<<i>l:i;;li:<>ill~!!Ill<"````","^^^^````
                             :I~~" '[i                       .'...'''.......!'
                             ,::;"`"<l"`'^`''``'''"^^^^```''`''`^^^"::,^^^^^I.
                   .--";-_il~I+<;-?;:<<>+`<[+:>}?-,!>~ii;i><<>+::,.
                    ""'.`",'^:;l::l:;il;I^,I:":I;;^l!ill:IlII;i:"""",,,,"^^^"
                             ll++, l}+Ii}?["+?                     .........!'
                             ;,,,",:I;:,:,::;;^^^^^^,::"""""""""""":::::"^^^;








```

*Figure from page 3 (2346x3317 px)*


---



4203-E P-280



SECTION 2 PROGRAM OPERATION



(c) Enter the device name "FOO:" and the file name "PROGRAM.MIN".



Do this either by keying in "FOO:" and "PROGRAM.MIN" or by displaying the directory for device



"FD0:" and selecting the file name "PROGRAM.MIN" from it.



For details on selecting files from directories, see 15-4, "Selecting Files From Directories (OSP



Format)" or 15-5, "Selecting Files From Directories (MS-DOS Format)".



j co



S01.MlN,FD0:PROGRAM.MINM



(d) The command is now completed: press the WRITE key to execute it.



The created command, "CO S01.MIN,FD0:PROGRAM.MIN" will be given to the NC and file



"S01.MIN" will be copied to the floppy disk under the file name "PROGRAM.MIN".



If Input Error is Found:



If an error is found in the created command, move the edit pointer to the location of the error and



correct the character.



(a) Assume that the following erroneous command has been keyed in instead of "CO


#### PROGRAM. MIN,S01.MIN" due to a typing error:

PROGTAM.MIN,S01.MIN if!i



{b) Using the cursor keys, move the edit pointer \\'M' to the character to be corrected, "T".



~,;p, I


#### PROG]f,AM.MIN,S01 .MIN

iii



(c) Key in "R".



For details on editing commands, see 15-2, "Creating and Editing Commands".


# I co

PROGRl!Vl.MIN,S01.MIN~I



{d) The command has now been corrected; press the WRITE key to execute it.



Executing a Command Similar to the Command Previously Executed:



When executing the command "CO PROGRAM.MIN,FD0:S02.MIN" after the execution of the similar



command "CO PROGRAM.MIN,FD0:S01.MIN", the new command can be created following the



procedure indicated below using the previously executed command.



Create the required command by editing the previous command.



(a) Press function key [F4] (COPY) in the PROG OPERATION mode.



The command creation screen will be displayed.



"CO", which indicates the COPY function, will automatically appear on the command line.



co El~



(b} Key in the file name "PROGRAM.MIN" and a comma",".



PROGRAM.MIN,



(c) Enter the device name "FOO:" and the file name "S01.MIN".



Do this either by keying in "FOO:" and "S01.MIN" or by displaying the directory for device "FD0:"



and selecting the file name "S01.MlN" from it.



For details on selecting files from directories, see15-4, "Selecting Files From Directories (OSP



Format)" or 15-5, "Selecting Files From Directories (MS-DOS Format)".



PROGRAM.MIN,FD0:S01


## .MIN iti


```text


                                                                                               '`^`.".'^.``'
                                                                           . ..       .        +]-]>[";>l[}~
                                                                         I}-+<<~+]!_`~_[_++?--1>;-___-?~+~-_
           '''''''''''''````'`''.''''''''''''''''.''''''.............'...'^``'.``''`.'.'`'`'''^''^.''`^''^``
           ,,,,:,"""^`:;,:,,:,"""^"^^":,,"",""""",,,:::,""":;::::;:"::::::,"`"^^^,;IIIIII;,;;:;II;I;;;:::;;"
                    ;!``~,i!^<l,,i;;ll^llI!";~iiI^"l:IIl;:>;`:;;l":<i>l!!il!>;iiiI'
                    I!^'I^lI.;I"^l:;;l^I!:i^`:ll; ,il;:l!"!!^;!;>,.;:I;;ill!i:>l!,
                       ,iI^<!;">+lI`!""lI;:!"I ;iii".ll:';<<!;l!I!>!,<<i^`:`l,^!;IlillI,<l,I>lIilI,;!,:<;lII
                       "-_~+i!>~<i<!_~!~_i~{!~i;;i~!,>+]~><~__+?+~?_<_~+,!ll<l:!iil<!;~Ill:Iilii!ll:<,;~!!i>
                        ",i!. <:I^i<>lI:<,ll!"<!^I~I>"'I><I!<ii+<I+<~',!>>'i.
                       ";:.^!l:I:':'':l:"i,,.l::`:^,".I,^^:^""^ `", `I', ^l"I,,;"""l,:,,I"",`I;,",,":,'";;lI
                       ;>i:!_+_i>:~il]<+-_>]l~_+I<~~>;]>~~++<_<,i_-";-l-":--[~_<!];;i->;lIii,<<<~<~i+-:!><-l
                       ;>!li+[!'<,:-I~``_~<~~+i-Ii~+!IIl>!,~i<~-~>_?:[}[i+~<_;!i>i~?+^
                             ;l>i;^;iII;!!!l>iii!!!lllll<<i>>i;!!^""""^^^^^,I.     ..
                             >l+~" l[~l!}+?~<_->i<_><?++]{>]]]!)]         '.l
                    ,l'`!;,`,lillllI::";";:;;I:;;::;,^::;;:!;"Ili!i<;I;::!;!I^`'^^'^
                   .<-^.li>:>!!Il~><:l"I!>,;<ii+>~~i:l<i><,<~:l<>>:~:i~+^<^!>+<!<~:<
                       ^I"" ^^"::,^.,"::",";  ;:; :I:`:Il"";:I":;;::II,ll"lII, ^:^'"` "^^".^`.:"'^;:'`"^`":^
                       ^i~_^~~-]+<!!~>><!_!~:`li~^!]i">+><!i<<ili~i_~>~]_i-<_:.-[i;?i;{>~~"i>"_<;:_>'i~>:I+<
                 .''..'^~?i:~]+_'i]_i[il~?--_i+:~?!<-_]];<][!I<~__:]+!<-l:_+<-,i~[-<_-??[?>{-[!.
                .l^l!!l;;;il:,":,i;:lli"^"^^^`^^"","""","^^^^"^^^"^",,"""^""^"^":::;,""""""""":;::"""""""""I"
                ': :!li~i!i!!i"!l!;>il~                                                                    ";
                ':   '<,+^Ii;!`<,llll>^l;~<;i<>+-<iI<i<>i<><`i>>!ll->,><+;>i<~<;!!I_i;>!!_<<;:>l<i"illl^<liI,
                ';   ^++_+-_+{_i__-_[-_~^^,'"""::,^^,"""",",'^,,,"`::'::,";,,,I`":^:;^::;I:I^":^:;`;"":'l,:::
                .;^^'`!l"Il;l!<;!Il;!;!;`..`^`` .......''.'`^^`'.'. .'  .``'``.'..'  .  .'.``' '''`.'''`'^^!,
                   '~-.^+ill!i:<!<:Iil;!~>~<!>:~!!ii<iil:ii<<!~i!I~~!!<<<l!~>>+i!il<<~i<i:+;>++:.'......''''
                    :;.!_?-_~-~~_+l-?~I]~>i?+[li<!!i>l>!!>>>Il~l!":I,^;;:`^:III"":":lII!:^I ^;;'
                       ::Il;i<<<_!i_i!l~i:,+<<""<>l:l:!;-<l_>++><:. ..   .'.
                             li<i^ i~+i!i<~~~l--~:<<!:<+~!>]^`'`.'````````^,i
                             :;l!^'l!~<i<I!~>;>iil>~i;>~>l~-  '.'..'''^'.   I
                   .<<.Ii>!i:<>;"!l!!;:i!!:'ilI!:iiI"!~l:lI;~>"!:l!;~<:!iilil!l^l^Il^:I;;;ll;^`!;.
                   .II.";I,i;!i!;<><~lI>>>l,!!liI!>>I<~l!i!I<~,-;I<I>+li!+i<i!i`l";>"I!Il!!>!:.:`.
                             ;l>~` ~-[__+))?-I?_?!_-~:_]-i_[       .  .     !
                             llll"^::IlI!<i!i!<illl!I:l!lli~,:::"^^^^^^^^^^,i
                   '<<.!-_!:l^?~'                           ................
                    ^^ `""^.. .'      .
                       !<~^_??+_ll<"~~[?~+;<i>~<_>+-^!?-::[l_^;_>__?<-l~<_l-~}<~_l+<<+<+_i-_"
                         . .'IIlI,"I!!;!i~!il;ll!:IlI:Iiil!i;,^:,:;::!;Ill;;;`'`;.'`'''^^'^`
                             I!_~`.<-[~~-<}r{i]}[<<{-l~{[_<|^               ;
                   .^, ^;"`'`;;::;lI;;I,,:::,:::"":;;I;;":"::::,:;,:!!!lIl::, ....... '.'.
                   .<_ ^<+>I~>iI>-!<"!-!,>>>,~-_i^><l~i<++`ii+<>;~~,~<<~l],_~<;~:+<_~<?>!!
                ';^~iI!I;i!!I!!ill!!ill;>>!i<iIl:~lIl!lllI!!ll_>l;l;:!;;>;lII<l!:^^^^"^"^""""":::,""""""""";.
                ^; >ii!!i>I+:l,llli!<!i,!<!!~>,~:+<iI!i>!!+i>;I!~i<ii~+:<i+i!_+~"                          :^
                ^; l-<<<"Ii<<!+><l+~l"i!!lIil>"I<<:>~_!>+~>__;?+>I>><l!_>!:_~~^^?+<^<>;;i!!li<;;^>!>!"I!>+i<'
                ^; ;~l~~i-~-"<_+<l_]]~?-]-}[>)~_~?-?!_]~l+[]},^]+<'~_?,l~>~~<?i?i>?<:_]il--]{?]l+-_+[_-_I)]]'
                ^; <+<<~_?<_"l+-!<-~~!-->-il___~+~~!~<_~><?-!;!~_>i?-+l>+~~<_--: `,, ^;`.,";;:;.^,,,:::! :,>'
                ^: :`"Il;II;"l;:;llI:"lI:I",!:Ii,;:`I:ll;:i!;"l;;;lII^:;;;,;l:I                            ,`
                ^;'  .<<~_?+!]-I<~-~>-~I<><~i_+~li?;<+[__>>+~:++~>ii<:>>~~<-+<>..'.........................I`
                 ^^"I;`ll;:;;!IlII;:;::"llI::lI!>ll";";,,illIlI:!>!l!;ll;II,:,;I;,^^^^^^^^^^^^^":,"^^^^^^^^,.
                   `_< I!~<<"i!!i>i;!<+:~I+li>l<!I!^<,i<I;l+iii">~<~+~+><<-:i>>_<
                       :I"^`"",,,"""',":I,"`^""""^'":"^"',"',"`^".
                       ,;!;;>lIliiil"!!~_ii^l>!<~l`<<:!~"<<+~~<<>"
                       ,!l!`.II:;`':!;";,,`I,`,;;II`"",";", .:!.,";,:,!::!;',::;:;':"^;;`"",::,:,,",:'
                       'lI;'"_iii;li>+_-_+li~!!<<>lI!_+_+~_Il--I-~~~>+{--]?I<~+~~~^iI,!~,!!!>!><>l;l~,
                            `I!<<' ;{`..  .       .......  ..  .     . .   ^:
                            .l;ll`';_`''`^``^"^`'''.'...``.'`^^'''''''```^^;I
                   "+i >__:!;><!I[<"l+><I;-__~_--__?i[]-l"_i<l!;>iii!l":` ..
                   ',, `,I"^"lIl:ll:liIiI,;:;;;l;lll;i!>I:<llIl;illll!^;:,^^'
                            `I>~~ .---<+]---[!?]-I:{"   ..            ..''.^l
                       .    ';,::^^"^::,;,:I>!!;;I,!"^^`^"^^,"``'^^``^````^:,
                   ^~<._<+[i!?_,?_<~_!l__<-`><__;`_>+>?_I_[l;~+i_^>[+li{+-l.
                   .'' ^`'"'''``"`'``''^``^ ..`,`'"^^.`^`^"^'^"`"..^`..`'.                            .
                       <+:i>~"i?__;,_,<><+i~:!'~>+<"._!<"!?!:![~-,;~:-!;?_--[-~-l]?!l[~-+_~>;_!:[<><-"<_+-l^
                       li+li_~+>+<>>?<;_-;i?>i!"_-+,_[_-"_i>I;! . .. '`.'`^'"^.,`.''.''`'`'^ `'.^`''^. .'`.
                       "^"`",^"^""l"^".`,'^,""" ,:^',,"^ "^,`.^
                      .<!!.<<~_<":l.l>~<l!ll`_i<'il!,'_i>!i;i<I i>il~"!"'~~<>!<i<:i!><;_ii>;:_~~<+ii~i^+~?-:
                      .<!>i<+_lIi"~ii>"+_<~+<<>i!~<>;>i!<;<~i~<l<<<;l__>^<+++i~!-<l>~l^``""`',"::,,";:':":"
                       ,,II;i~';i^iiIi^I~>il<>i<:!<<III>!,;ll>!!<i_!!?_+!~ii!":l;;>~;
                            ':~<!'.i~_+_~+~~+;+--I><~i>_<:!--~;-^      ..  `,
                            ^;l!l^";I!!>~>>i<;>>>i;!>!!_~li+<>l]:^^^^^^^",";;
                                 ..                      .      .......'''''











```

*Figure from page 4 (2346x3317 px)*


---



4203-E P-281



SECTION 2 PROGRAM OPERATION



(d) The command is now completed: press the WRITE key to execute it.



The created command, "CO PROGRAM.MIN,FD0:S01 .MIN" will be given to the NC and file



"PROGRAM.MIN" will be copied to the floppy disk under the file name "S01.MIN".



(e) Press function key (F4J (COPY) in the PROG OPERATION mode once more.

• I



(f) Read the previous command.



For details on how to do this, refer to 15-3, "Use of the Previous Command".



I co



PROGRAM.MIN,FD0:S01.MIN~I



(g) Using the cursor keys, move the edit pointer



"tf



to the character to be changed, "1".



PROGRAM.MIN,FD0:S0'IMIN



(h) Key in "2".



l~c__o _



P_R_o_G_RA_M_.M_I_N_,F_o_o-:s_o_2_iM_1_N_ll_'.!------.



(i) The command is now completed; press the WRITE key to execute it.



The created command, "CO PROGRAM.MIN,FD0:S02.MIN" will be given to the NC and file



"PROGRAM.MIN" will be copied to the floppy disk under the file name "S02.MIN".


```text


                                                                                                ````.^ ``.^`.
                                                                            . ..      .        '-_-[l].i!>[_;
                                                                          i1[~<~__];+._~[__?]_]}!>-_]~-_~_~[i
            `````````^^``'``'``````'''''```'''''''''''''''''''..'.........'^``'.''''`...'`'`'``^'``.^'`^''^^`
           .,,:::::::"":,^^^^",,,,"^^"^:,,,,"^",",",,::""":;,,,""^""^"^":;:;::,",^";:IIII;,:::;;I;;I::::;III,
                     !+ ,<!;^;!!!liI!"!^lI!^;IIl!i>!!`:III;"<I"i>>!!<,;;:^I`::;;,l:";
                    'l!.'":,^::,,:l;l';`::I`;!I!l!i!l'l;lll^l>`;l;l"l^ll>^!'lliiIii":
                        ;>I;.;I!>I!^';IlII!!! `!lI !<+!!!<!<<"+<<:Iii!:<!""+>i^ ll^:l"^i:lI.:``i!^!>i'I;l^!<:
                        :~_-!__[-?[I_?_~I~-i+I^iiil!i<i>->i-~I~>!+!<!i!_+;!]<i>:<<I!-ll{+-i:+<l~<":il'>l>^;~l
                        .:"lIl!I!>>,~>!:.>l^l<"l!i<<llI;<>"ii+i>^<<_`!!~_I;<<"~-,;_!!~.!-i^<]-+`
                    ."^ ,,''' `...'. ... '`'  ^'^"'' . '  ^^`''' .`'`^.''.'. .  .
                    ^-<.!i~+_;__i_]_>i-[<?<-l<_+]_<-i_;?]>~_[--]l--_+?]]~+~[i<_+{+;+~-~I+__+'
                             .Il!l`';+"`""^`^``'''^""'`'`````^'''`..'.''`""^":
                             .l!~>' I(,....      .`'''.''.''''...........''''l
                     ;i Ii;;I;~l^:llI;;!;l!llll!Ii,,"^^^^^"","^^^^^^^^^^^,"""`
                     !i ,i!<!,l!^!l!!!l!,;illli>Ii
                        !:;'l!l:I"",";";^:'^I'l:; ^Ii;^l^"!^!'":II^";Il:^l::",""^:::,,",,,;
                        ,:l^!i_~>!i>;!l~;>!i+:<!~":~_~,+:,~I>;^><-l<><~+Ii~?~<><;Ii~i<i_i~;.
                             '!!~>..<--i~-]+~]l-~+lii++I->;I-]+I[, .    .  .^:
                             .Ili!'`:;!lIil><<l>ll!;l<>I<!;;~!ii{!`.'...'...`,
                    "_<.l>~i<I+<;;ii>i:!<i<"^iI;>:<>lI>-;liili!",I:>,<~l:~>i<!>>"!;:i:"!;I;;l!'"l^
                    'iI ^,:"!:!!;;!li<I!i<>;"lll~!!il;i>;~<>i>l`!~"<;i~>!<~>><l>`;I">;:lli!+ii`.:'
                             `Ii+< '_-[~____}]I]?]>>+-i![<{)]-_!(,          ';
                     .  .    'iI;:^",,:;l!Illl:lI;lI!ilIil>>!i>!-:^"^""^^^",;;
                    I[>.--?I>l"?,
                    ..' .'^'.^:;::^"llI;:::,,,":II:::,"",:;I;:"""^^^^",:,,"^""
                             ^I<_+.^?_[__[}-][!)[]_--[_~{?(t}]]<f:    ......"i
                     '' "^...':;I;;;,""""""":;;:,":^,",:;;:;:",:!II!I;"^^"^^,^
                     ~~ l>-li~<~i>-+<!<:~~~:~<><-_]~-"~~<+l!-_:-_?i+?I?_i!~:+<-<i]!>I
                        ,^`..```^^".''^'^^```.^,,^`;,:,^::""""^"^."^"`",,'"",""``,``'  . .  . ..  ...     '
                        ><?I;~_?--_"<+~+<]++> :><;"><+<+-+_[+l-<_i!<?i>_-i_]<_'"_]`<-`_?>-i`_^l_?^_?i^}<+^][;
                        l~~_++-__--<}_];,-+l?+:<~+_<;+:~~>l?~_>l:[~<^<i_-;>+>;[+,i+!+!I}-]l-[?+".     . .  .
                            ..' .'..'.. .`'.`'.`^^`^.`''`^.`",,"'^"`'^`""''^".^"'`:`"^ ",,`""^^.

















































```

*Figure from page 5 (2346x3317 px)*


---



4203-E P-282



SECTION 2 PROGRAM OPERATION



15-1-3. Command Execution



(1) To Execute a Command



To execute the command that is currently displayed fn lines 4 to 7 of the command creation screen,



press the WRITE key. The screen will revert to its original condition and the command will be



executed.



The created command will be saved as the "command history".



(2) To Abort Execution of a Command



To abort execution of the command currently displayed in lines 4 to 7 of the command creation



screen, press function key [F7] (CANCEL). The screen will revert to its original condition and the



command will not be executed.



The created command wfll not be saved as the "command history".



Command creation screen



lfl9CUWf ~rn1t



I<»-••··~'I!



UU:X O!SPU.Y ~



ff2l -> 11»:•,11n1



CFJl->f't:0!•,1111t



11l O!Sl'\J.Y 01"8< INleliES.lfte> l'<ESSIIIG IF\),



IIFIJT H ce.rrce IIME NI) FltE JWE, UiEN PRESS (fRJ TEJ 1(£Y.



OEFMA.'f' DEVICE M.ti1: - 11)1:



OEfMA.T Fil.£ fWIE - "'.MIN



Original screen ,



11;:.:..



'fMiD


# I= l"1: Io:= I

t'MIC8.



l /!~



(!'BU.T~(t(



"""'



Command is executed



:!:!:.S!;~~Hl,R:C!



'- ,;;;;--_,. f '"""'


# I I I

I - •i;.,r



/i~~Ttl'.'1 """""'



Command is not executed



"- l'EAI)



I""°' lvei,FVI-


# I I

PIP



WIT



Fig. 2-3 Command Creation Screen


```text


                                                                                               `^`^., ^^.^^'
                                                                          ....' .     .       .---[i[`><>}{<
                                                                         ;}}~>~_+]!_'~+-__-]-?{ll?~[<__+~~-~
           `^`^`^''````````````''''```'''.'.''''''''''''..................'`''.''''`.'.'`'`'`'`.'`.^''`''^''
           "",,,",,""^^^,",,:,"^^^`",:;;;::,:;;;;;;;;;;;:::IIIIIIIIIII:::::,:IIIII;,:::;IIIII;,::::,;;;II;I:
           ,+,:">  i!!llI!l!;+l!I;i!!,
           `I^^^I  ":I,",;,;^;:;;;I;I^
                 .::  ">`l,:;^:;."^;^";;:;:;
                 'll` `l"I;i>l!<"!"l!;!l>>l!
                      "!^::;""!,:l;'"":,,;:::i;i::^,;;;:>:^!l;:;:I;",;I:I^:::^:";I;,^,,,,":":"":,;:,"^,""",.
                      ^~!<<>-_+>~?[i?+i~<_l>+~><Iil>~!>!?~;~_?<__~<lI!~<_l!i>::i~<~<:>>ii>-l>Ii~+_i~li~<+~<:
                      >~>>~`>~!`-<<i>i^--i  <<<'<i~~_I^+_^;~!<i^_::?,l~+?i_!:~<!?~i<`<<>:<~~`<><_!+!+,i-i,->
                      i+~_l<-~>                                        ..                    .. . ...     ..
                      ^:^```^`^ '.  ...   . .'.           .  .               .
                      :~~<I<_-}--l>~<++]~+!-}<i?I_?~_?l?<l+]"!+>>i<[<~!i_?~++^
                                                     . '.  .  '.  .`..  '..''
                 '?[' :-;+-<+><~+-++?<i:+l<l+<<><+__>
                  ``  `"''^``'.'`^`^^`''^'".`^''`""``                               .
                      :+`i]i~!:~~<!<-<I`_;<<::<<!!!+i>`ill+<_[^;-_<~+>_<"!,>i_;:lii^;:+;?+,;i>il><i>,i><-il;
                      ;<!i<i`,<<<<;~!!><i,:<<,?<<Ii_+]-+]~i;.+-~;<~>_~>,><;l~>>>l+;ii,i!<~!+l>!>+]<<,i<~>?~l
                      l<!><i!i~l<];!<>~~!!l~+I-l>;:::;I:III, `:!":I,;l,'l;^,!:lI"l`;!";;+;li^l;l!!l!^l!!,!iI
                      ,;";:;>:I'!<""l;;>^!i!;l>i!.
                      :il"^;;Iil;`;I:":,:;^:;`":::l",l;Il";I"!;":::;:;;;:;,II::,"
                      `;i;;li><il:i!I:liIi,il"I!l;<:;<!i<,><:i>,^>!i!!<>!I:<<>i~^.

                    '>+<>+<i_~~i>+_~^.   ..'''....'''.'.
                     "<}{1?}]?_!>>!ii!][}+>i!!llllII;;li!^
                     l:\(?~_+~~lIIIlll+__il!!l!!I:i_?<ll,I
                     i;[_--_~i~[;^^```''`^"^"^""^`;!iI"",:
                     l"                                .";
                     ;'_[!<_~_?__;""":,^"``'^""""^^^^^^"`;
                     l +|,l+|!(['                        ;
                     i'<_<]!{]!(-+<?<)-]~_!`:"^^^       .;
                     <.]t_?{}}()i)]l,~III;i"l::::       .;
                     !.!+~">l~_" ^~"                    .;
                     I.                                 .;
                     ;.                                 .;  ";,""^,:,
                     , ".^"::'`""''",:,,::^^^^'^`..`^``` I  "i[++>___l"",":;:::,,:;::",:,"^^^,::^
                     ;",-+:!{[!I[\i~\r):{v)l{/>!!-~;:^^^,:  .:i)1}[{?]!;Il!!I!}}[<i!!lllllIIIIIil:
                      ^,lI"`^;,`"!I^"":n;;I,:II,,lI,""^^^   ^l                                  'l
                                      '#,                   `l                                  `I
                                  ''.':a: .                 ^l                                  `l
                                  ,l_Iih.                   'I                                  "i
                                ."i[n~i#f~<[\)(/|1))(||t}<<-!,                                  ^I
                                '';}?>~b[11{}}}}}}}}[}}}{11f_,                                  `:
                                  `''`:b                    .:                                  `:
                                      Ia' .               ..^:                                  `:
                                      !o'                   ^;                                  `,
                                      lo'                   `,.,^;;""`:.        ... .         . `:
                                      !h                    ^;^<_+?~->+;:,,;I:"l^^^!``^;i_,!"^^`":
                                      !b                     :",+,^l-!':_>;:~!:!,,":`^`:,_II,""":.
                                      !b                      .  ..   '' ..' .   .''````' ..``^'
                                      !b                    'I~))[[1][!liiII!i[{}+!i!iii!!!ii!i<i`
                                      !b                    :l^II;:l:;''`^````;lI"`''``````````^":
                                      ik                    ^:                                  `,
                                      ~h                    ":                                  `:
                                      +b                    ,l                                  `,
                                  :II,<oI '~<!!i!ll<l>>!<~` ,l                                  `,
                                 '<+]l'_ufrnxjrxrrrxxnxrxxfz]"                                  `,
                                 ^^ll'   ..     .         .`^^                                  `:
                                   .                        ^;                                  ";
                                                            :l                                  ^,
                                                            ,l                                  ^"
                                                            ,:`` '^' .`'..`^..'`'``^`''`"`'^```'`,
                                                            `I^!?:I!]i;l~>i!_l^!'`^l`^^l>};l"`^^I"
                                                             `";!:":i;^";:"^l;^^```^`^""^:"^^`^"`

                                              i>_"iI~^i<<i>i+>~!i>><?<i:>-!>~>,
                                              '.!`^`^.`^"`"`;",^^^,;;,,'^;":;:`













```

*Figure from page 6 (2346x3317 px)*


---



4203-E P-283


#### SECTION 2 PROGRAM OPERATION

15-1-4. Operation Transition



Use the file processing function keys (copy, delete, etc.)



AUTO Operation



Program Operation



MacMan



Command Creation


#### Screen

INDEX. Displays "ISO" at the console line.



FolJow;ng the ISO character string. enter the



device name then press the WRITE key.



[II)



MD1: INDEX .......... Displays MD1: Directories.



[ill



FOO: INDEX .......... Displays FDO: Directories.



[EI)



COMMAND HISTORY , . Displays the command log.



[ill



OVERWR/INSERT , , , . Switches the command editing mode,



[ill



CHAR DELETE . , . Deletes the character indicated by the edit point8f.



[1IJ



CANCEL , , . , .. , Cancels the creatoo command.



WRITE •



I ...



Executes the created command.



When ttie device Is OSP formatted:



Directory Selection


#### Screen

I]]]



RETURN .. , ,



III]



CANCEL ... ,



WRITE



. Far device name selection only.



.. Cancels the selection.



. For selection of device name and file name indicated by cursor.



Command H lstory



Screen



CAN



... , . , ........ Same as (F7] (CANCEL).



When the device is MS-DOS formatted:



[II)



RETURN .. , • . . . For selection of device name and current directory only.



CT:IJ



CANCEL . , ... , , , , ..... Cancels the selection.



f WRITE



I .. ,. ..........



If cursor is at the directory name, a directory change occures.



lf cursor is at the file name, selection of the device name,



current directory name. or file name occurs.



CAN Same as [F7] (CANCEL).



III]



CANCEL ... ' ' ' .. ' . . . . . Cancels the selection.



WRITE'



I ....



Selects the command indicated by the cursor.



CAN



I ...



Same as [F7] (CANCEL).


```text


                                                                                               '"^^``^ ,'`"^.
                                                                          ....'...    '...  .  l}]?+_~ ~:-[]:
                                                                          ]{+<i<+-?>!^?]]~-]?-}-:~_+__?+>~<?,
           '^^^^`''```^^^^^^`^^^^^````'````'''''''''''''..''''..'........''`''..'''`'...''``.'``'`'.`'`''```.
           `"",,^",,^`^""""":,"^""^^^",;;;;,:",;;:;;;;;;,,:;;;::;:::;IIIII;:,:;::::,,:IIIII;,:::IIIIII;,:::;`
           ^~l""i^ :~iili>Il`>I>li~!i`
           .:,'`,` ^Ill:I;:,'":i;lIIl`

                              ^;!!>li!l!l^^,;. i>I!i~llii>i!!!i:;>Il>!,<i!:<:        .^^^^^^""".
                            `!<>-?_+]?--!"; :^            .      . ... ... ..                 ;^
                          ";~+?[+<!_<>~i: i""^                                                :^
                          i,i!>!`       l.:`"^                                                `'
                       '',>.            I',',^                                                `.
                      ";`I_'            <'l!,.                                                "'
                      ,^  !'            l;;'                                                  ,`
                      ^^  ":,::;;,""",,":.                                                    ,'
                      ,^                                                                      ,'
                      "^     `^^^^^^^^^^,"`^^^^^^^^`^^^^^^^^^^^^^^^^'^""^^^^^^"^^^^^^^,"^^^",,:.
                      ,^    ',''...... .............    ...........   ..  .  ..   . ..''.'.'''
                      :"    '`   .'`'''`'....'. ... ^;:,          .^'`' ^^..`. '.'..
                      :"    '^  ";^``'`^`''.'`I,><l:"!lI.. .......:[{{[>]-~[<-_][~~-_,lI,I;^
                      "^    ', .;` "^^''.'^^^.",^^^'              ^_~<l_~><_l<_>_!+-_~+-^"";^^^^^^"^
                      ,^     "^I_` lI;]]?_lll`:;<_+l>-;.~~<;..  ..,_<><l_!.l!>!ii         "l .  ...:'
                      :"        ;"      '.    ,:>??I;<l^~<>^.''`'."<<><;i!.Iliiii.        ^^       :`
                      :"        :;``''''''`'`'I,~-?!l+-_~_i>+<~<^.">~~>;!;>ll>l;~'`""""^^^^^^^^^", ,^
                      ,"         ^^`````^^````` >__!;i+<<><+~!' '.,+>i<Iill!i~l;<i>Ii~,          l "`
                      ^'                       '~_-:;li;I!l!;  ^~<<I:;;il!!"I!>iIII!;<;i!<:      ; ,^
                      ":''''''`^^`````````````I.<_<;l<+<!.. ......">!>ili;iiiI!l!>i^ . . .       l ,^
                       '''''''`^``''''''''''''I'l~)[]>:>' ......'.;+~<+!>!!~+>!~><+;             l ,^
                                               .''''''.'                                         : ,^
                                                                                                 I ,^
                                 ```'^`'''''''''.''..'```^```````````'`'``````'`````''```^^''''`^I "^
                                ,:'`^"^^^^^"^^^"^^^^^"^^","^^^^"^^^^"""""^^^^^""^^""""^^"""^^^^""'':`
                                "' ,```````^```^"`^"^^`````````^`````^^"^```''^`````^^````````^``^^`
                                "` I
                                :^ l  `l"^^^"^^^^"::;"^~il>il>l!;I~i;I!<i:
                                :^ ;  "l .          `I .<_-<'<_!<~"'''`^^' ,l,!ll:!l;!ii!:;>`
                                :^ ,,;-;.>ii->-+i>!.`l  !+<<';~>+!...    . :~i>!>ii+~+i`'..'.
                                "`   .":    ;:;,    `!  l;_1?}!I"........'.,!;i>ii;l>>i,Ii!;!li;il:l~i<i!;I!!'
                                ,^    ^I....    ....^l  >li][~;l^          "i;:I;lI;l!ii,
                                :^    .,"^^^""""^^^^"',!!:ll<!II";!I!lI;;!l,`'.''.''''''.
                                "^                    `"!i<!"i>;I>;","""";:;^.""^"'`^^^^","^:"^,,^,"""`",.
                                `'                      I-+< I~i+<.        ,iI<>>ili<~!",:"^;,,,:`:;::^:I
                                "`                      >i+1_?>>!"......''.Ii!ilIl!+i~i:".""..^:^,`',^,'^",;.
                                :^                      :`;llI^^.       .. i__]~+-+[~{-}[~?1[]???}+_??__]+:;.
                                "^                                         "III,;I!I^lI,,;I;ii;III,    .
                                ^`                      ::I-{>:l"  ....  ..:iI;II!:;!!!!^
                                ^'                      '``""^``.          .`''``''`'```'
                                ,^
                                :"     `""^^^^^^^^^^^.  '^`' `^^"'         '`'''`.'`''.
                                :^    `I`' ..... ..'"!  !+<+;<<>i:........ I<!<l>:l~>>I.'''...'....
                                ,^    ,: ^^^''``"^' `!  ;I-1][!;^  ........l>l!;ill><i!!i!ilIl!!;l!"
                                ."^^^,_; :;:-??_!I: 'I  :::~[];I^  ....... ;il";:;,;!iii^
                                      `:     ...    .I   ...  ..
                                      `l^^^^````^``^,:
                                       .'...''''.....


























```

*Figure from page 7 (2346x3317 px)*


---



4203-E P-284



SECTION 2 PROGRAM OPERATION



15-2. Creating and Editing Commands



15-2-1. Command Creation Screen



Lines 4 to 7 The command is created and edited here.



Characters keyed in are entered at the position of the edit pointer. When a character



is entered, the edit pointer moves to the next character space.



The downward-pointing arrow



Lines 9 to 15



'T' indicates the end of the command. Up to 255



characters can be entered.



The character string being entered to create a command can be modified by moving



the edit pointer with the cursor keys.



The procedure for displaying directories is shown below.To display a directory, press



one of the following function keys:



[F1} (INDEX), [F2J (MD1: INDEX), [F3] (FOO: INDEX)



[F2]



MD1: *.MIN



If the [F2J (MD1: INDEX) key is pressed, the directory of MD1 related



files (machining



programs) with an extend name of "MIN" will be displayed.



[F3] _.., FD0: *.MIN



If the [F3] (FD0: INDEX) key is pressed, the directory of the "FD0" floppy



disk



files (machining programs) with an extend name of "MIN" will be



displayed.



PROGRAM OPERATION TRANSFER



COPY OVERl'iRITE jcol



Command created {



and edited here



'EDIT POINTER



INDEX OI S PLAY PROCEDURE



[F2J


#### MOl :*.MIN

[F3]



FOO:*.MIN



TO DISPLAY OTHER INDEXES.AFTER PRESSING [Fl).



INPUT THE DEVICE I/Al£ ANO FILE NAME, THEN PRESS [WRITE) K::c!'.



DEFAULT DEV I CE NAME = Mill :



DEFAULT FILE NAlE



*.MIN



Fig. 2-4 Command Creation Screen



EDIT MODE


```text


                                                                                               `^"^'"`.,."^^
                                                                          .'..'...    '......  <]_]<-l"~I[]~.
                                                                         ^}]~<<_+}!+^<+?_--??-[_:_+?<--~+~-_.
           '```^```^`^``````'`````^`^`'''''```````````''..'''''...........''''.'`'''.'..''`'''`''`.''.''.`'`
           `^^"":::,,"^^`^"""",,,:",""^^""^,,,,,,,,,,,;;,,:;;;;:::::;::::::IIIII;;:::;::,;IIII;II;II:,:;::I;
           :>>^+.  !!lii<ill'!l;!"-l~<ll;^>l;lIlIl;;>!
           `;!">'  :;I<<<ll["<!li^+i~il>[^li<iiii-i>+_'
           '^ ` '  ``.... ..'... `   `. ...
           :-l~:I' !ii!~!_>_:>i+?]<<"++i_-<^
                  ^,;:;':,;'l     ^l:,`:,:::::;";`,::II:,:;;:,;!::";,,,.
                  "!li<,I;<^:  '. `lii"i!l!l<I>^>"!!<<~i;>>>I!~~<~,l~li.
                                  ;_><i<!-ii;<><i>:I^i!,i!~<l<Il~I~i^i!+~!~,>!_<I;<-:ii~<-~.l[+i<;ili>~>~<+~.
                                  ;<![?]--];>?-i[?_l_]_][:>-~-?-<-l]_<i?_+I~__+--}>i-??_~,^ .^'^"'"``^,^,^,"
                                  ,>;:^i:;;,,;;::::;!;,":^":;"l;^I";l",I;";;:;;IIl,,>!l:;..'' ...  ..    '.'
                                  ,-_+,[-?~+_?_~+-~_?+{>!}I>-"^!':<-~~[_~^_~i^_!~'_,!_~`>~~+~?-<~.'<[:i~"-]]'
                                  ,i<<<<<~!I"<~,!~"<i<+~_i
                                  "!l;`l:il!><`I<:Ii"I!lI"lIi!;l;lI"!ii+!:l:ll!l!iI>:l!,!!";lIi~ll;;;^ll;I;;.
                                  !+-i~?}+?[-{<i]?)[?{[>}??+--?[~_;"ll!il:l:l;I;l>;l,!i"l>,:!!ii!i:I<"!i!!l_.
                  . .   '.  ''    ;iI`II;,l;::!';l!`;ll^Il:I;^!!>l
                  ;~+-+I_i_^~_ '. "+>!!+i<_-~l<;<!^-++~+~>_!<_i!+~~-_!?l->~--;_?-<_;[l>[]]]-I~;[<+~_>~,<+~__.
                                  :~+i!<!+_;~+<>~+?l__+~?+~>[+__'.  .   .     .   .  ..'"^`"'`'''`'`'^`"``^^
                                  .''.l!,:,l!!<ii:,+!>"i<iI"^~<!!:I^ l,I';::;'^;:::,:
                                      <l,;:!ii~iil'~;+"+_il:.>~!+!~i,-;]I+Ii_:;_+~~>_'
                                      >>~~ ""^_<!;.,^>[>i
                                      ` '^ ..^>l!;`~!i"!~!:, ll;l;I,^:"'^^'""""""^.:"'`:^`"^`. ^`,;"".`^^"^^
                                  ,;"^       `;:i>"+;+^~-+l;.<_><i<i,+_lI!l~>+~+~i^~_Il-<]-+>-;-I?[>i`>++]-+.
                                  !{[+````'.'`^  .  ..'     '   ..'``'  . .             ^+!+<<+!i_I
                                  ;<!]~+<>-:<?]:~_,~+~<l<:__i]l><"[?]+`?_I~[I_[??[__]i           ..
                                     .>i<l "^`!!~:.:"_~~'                         .
                                      ;^:; '`^II!:">I>l<:^'.^^^^`^... .. ..     ..  '.  .    '.  '''.'..
                                  .'..       "<>~<<~+-i~~-<,-1-]+]l__+i+~++--__I<+-!{+-+-<_I_+~?!l+~]>l?+_-~
                                  !]]<                                                         .    .   ''..
                                             :?__'!++]__+><]`>~<-<-~~?",_]- >_':__]~_>'+?<~l.~!'_1[?,._[I"+i
                                  i--~_-+_>    .. '..'.....".`.."''..`..''. '' .`'^'`' `"'^' `. '^'`  ^^..^`
                                  ''^^'"^`'
                                                  .                        .                           .
                                                 :;[11{1|){1)(1\//////\|||({}[}[)\\\\(())111{1{}}}}}[[[+I`
                                                .> {ftttrjt/fj/czzzzzzccccv/\tffuXXXzccXXYYXXXYYJCJJYXY[.>
                                                'l /vcJLCLLLCCLLCLCJCCJJUJJCCCCCCJJCCUUUUYXXXYr/|\rjxzX[ i
                                 ^,::",",^":I;";': 1[n\!!l!!!ll!ii!!>>><<<<<<<<<~~<+++______+_<_{!<<<-]? I
                                 l-_~+[-~<-]<l;;.;.;  I'`^''.^""^^,.                         `'^;^.'^  ;.;
                                 ,l:"IIl:"l;.  :`!.!.  ^!!l:,li<ll>;'''''``'''''''''''''`'`'!_>i;-<_};'< ,
                                               '^i ^Iil",:;,",l:;I!,`````^^^^````^^^^^`^"^^^'.'''.''.`^".,
                                                `l  -{~"l>![:!-]?<>^                                    'l
                                                `I  >_l.^,"[>,l[~                                       'l
                                                `I ^!,!>Il^!<~;;~ii;^IIl^!ll:i':,"                      'l
                                                `l '_~i;[+;}i}l;{(l1~!+]I}|?l1+i[[+">-;>;">"            'l
                                                "i '-~>;"!+!<:i[_:"i]^''.`"' .^.`^".^,'"`'"'            '!
                                                ^l `[+?_"!<<i+)<i"':<_i'                                `l
                                                ^;  ....   ' '`      ''                                 `l
                                                ^;                                                      `I
                                                `;                                                      `l
                                                ^:                                                      `I
                                                ^, ,'......  ..... .'''.    .     ..   ... ............ `l
                                                ^; ^^````I:_l^'"l;_l^^;<][-]:+_~[?,i>~+,^,!`''`^i;"^^^^ ^i
                                                .I,''<[~';"i[{+:;^]|]l^_{|){"l!(f/IlI1}<<";;-~~`;`    .`!^
                                                  `^^^"""""`,::"""";I:","`^'^''""","",:,,^^";;;,^^"^^""".
                                              ."'  `.. `...'.. ..'.  .. .^ . ..
                                              "i]!:~!l^++<-+~-<~l<~-]~~i;[+<__!























```

*Figure from page 8 (2346x3317 px)*


---



15-2-2.



4203-E P-285



SECTION 2 PROGRAM OPERATION



Operation of the Edit Pointer



(1) Moving the Edit Pointer to the Right



The edit pointer will move one space to the right every time the right cursor key is pressed.



When the edit pointer is at the right end of a line, pressing the right cursor key will cause it to move to



the left end of the next line, unless it is on the final (7th} line, in which case it will not move.



(2) Moving the Edit Pointer to the Left



The edit pointer will move one space to the left every time the left cursor key is pressed.



When the edit pointer is at the left end of a line, pressing the left cursor key will cause it to move to the



right end of the next line, unless it is on the uppermost (4th) line, in which case it will not move.



(3) Moving the Edit Pointer Downward



The edit pointer will move one line downward every time the "down" cursor key is pressed, unless it



is on the final (7th) line, in which case it will not move.



(4) Moving the Edit Pointer Upward



The edit pointer will move one line upward every time the "up" cursor key is pressed, unless it is on



the uppermost (4th) line, in which case it will not move.



COPY OVERWRITE



~00


### ,oo,,..,,.,_ .,,_ ,,. ' •

'EDIT POINTER



COPY CVER!IRI TE



Fig. 2-5 Operation of Edit Pointer


```text


                                                                                               '^^^`^^ ".^^".
                                                                          ....'. .    ..       l]-]__i <;]}}^
                                                                         .])_<<~_]~<i"-_]~-]--1?;+-_+-?+<<<]"
           '^````''''`''''``'````'''''''''''''''''''''''..................'`'`.'`''`'...`'``''``'^..''`'.`'`.
           ^",,:"","^"^^`^:::,:,,,^^^"^^",,,:;;;;;;;;;;;:::IIII;;:::;::::;:,;III;II;,:I;:,:IIIIIIIIIII;;;;,;'
           ^~ll:!^ :<!lIi>;;`!;!l:ii>;!lIIi!`
           'l:;,l" 'Iil"lI:"';':I",:l""^;,l!.
                  ";' .>:",,,`l"'!:I`l,,":".;`;I,;<,:;'
                  ;l; ^+ll!;_:!l:>!~I;;<ii<^<,l<!;>+<i.
                       IlI^I!!^::;lI^,!l^;,::^,,:`;::";,I">l,"lll^;:I;"ll;;"I;^:;l:^",:,"";:`:"^:,::,:"
                       ^:!^!!::!;:!>`;i;^lIIl^;:!^>!!Il`l`ll;`~+I^l;i!:llIi^;!"I-i;"llI!;"i>;lII!i><ii,
                      `<<l!^,!l,I>:"l;I!l^;"lIil`II!,I;!"!;,I;; ^:;I::;"II",;ll'"",;,";:^,l!^:"":^:,"^;;;l;l'
                      ^_<!<<>i~i~><_-il~>!>><iI<I_->!<>~l>>!+><!<i_<?__+<~~,-[!!_><<!I~_i>~~i<<>~!i!i!!lli;>^
                      ^l>";_lI!iI:ll<!^>i<:;l~.;!>>>!,:i;I<"<>;i!<<"!~~,!>_^;l,+><+,I_~_:!:+<^!~:l<ii+.
                  `,. .,'..  .^. "'` "'.'.. ' ^'   '`
                  >]; "[<>>>?l__I_<]i~i~<?_,-:i+~I!?~
                      .,,^.^;,.`^^"^'',,'"``^'```.^'````^';^'`",.```'."^`'^"'``,''.`'''``..' ''''''`
                       ;!<"<<l;>i!<+^i_i,~<i~,>i<"_~+<<:~:_<ll]i;~~<~:_i_ll<~;__:i<~++:+__,_I-<~~~~~.
                      `ll""^",,`";"^,"::"'^^,:"^^;I`"""^:^^""' ^"^`^"`",``";'`'`^`^^^'`""`^'^^`"^'`^^`^^^^,^.
                      ^_<+<!!<~!+_<_<>~[<!<~<!>+!-><~<!>><+<~!I~<~~<!-<<+!_-l>ii~l;--i<-il_<<+i~<ii<><~!~l<-"
                      ^~-<:!<>:!lI<i,i~+l~~~ l>_+_!lI<:!>;?_:l[<_+i+>]lI-?~;?~~.>:>~<<>"i_+~I!!-_"~~:!<i~i
                   .   .'     .  .   '     .'              . .'...  .. .  '...'.. .... .'''' ..'. ''..'.''
                  ~{; :{_<>~-!--I?<}l_<~_[~,-<~+i++~_,
                  ''. ':^`'`;^.`'```' ^^`^' ''^`'"^```  .    .     ...  .  .    .
                      '>i~l_<>~~ll_>:_?iiii+lIl+!<i~:?>_i<~-~l<<-~i!<<-l++;l?~-_:I_>__<>_-!_!>~-+-?_"><--_!>,
                      ,<"+ii?+!}i?I!_?!!_>!"+"+-<-<:~~~!il~-il~+;~+i+I.  .  ...   '..'. '`'..'.'''''.'..''..
                       ' `..'^ ''" ..'` `.`.` ^''^.',:,^^`""``:,'^,":"
                  l-" :]>l>!iI_>,~i+:~lil>l"l!!!i!l
                  ,l` `l,":">",;`:,:^`,;";,.:;;:l;"
                      'il!,i>iI!I!>!`!l,Il;!;"!l"Il>^i!i<i!;!lil,~!>Ii<i"!+;,!l!i!;<<;llI!ii!i<,"i!<i!I;!;Ii'
                      ;~ill~~<~<i!-l![+l!_~!;<;+~i~+:_~~<<li_>i~<l<<!il; ,>'`;:,;,`;l;":;,;IIII^";,lI;"^:,:;.
                      ,!!^l<<>I,Il>^lil;,!!;'l'ill!;"!i>::"i!"^l!'!lI>,
                                                                       ''.....''''.....
                                  IZCObpdbdhdpbdpbpqqqqqwqqqwwwwwwwwwqppwmmww0YXuXLcmwU
                                  ^]<<1<-1{ur_[+>?I;:^^^^,,,,,,,,,,,,,,"""",,"""^""^,,;.
                                  ^         ;'":,"^I";,;;`                            '.
                                  ^:^^^``^^`'^li!I;!!iI!!;^^````^`'``''^`^^^`^^``^"""^,.
                                   ''''`"`^"`'   ...[    .'''''''..'.\_''''`"^`"`'''''.
                                       ;-xQ[,      .1                1!    l+Qv1,
                                     `!!?f|<^      .1                [; .,<!}t?<^
                                   ';^":!, .       .}              . }I^:^,I<`.
                                      ."            t                ?,   '^
                                  `iii~iiiiii<i>>i<+r~<<<<<<<<<<<<<~~|]<<~+>~<i!l!i!~~!
                                  >ZUObphhhhawkqpkmmQOOOOOOOOOOOOOOOOQ0OO0QQQUvufcXv00v
                                  :l`"I^:!!!<`I^"; .                                  ,.
                                  :.                                                  :.
                                  ":"""^,`^"^""^^^`^:`^^^"^```^^^^^^^:"^^^^^"^"^^^^^^^,
                                    .. ^"|-,^... . ^) .....   .......n>....,;]I,'.....
                                      '>l8U.I      ')                },   ll|$-`"
                                    `"<;>{I,'      ^(                -^.^;<:}\:"
                                   ','`I!.         ^{ .            . -^""."!: .
                                      .            "j                ~    .
                                  ,_~_-_____--_-__-}x????????????????t[][}]??_<>i++_[[l
                                  _0vOpOpppqQ0w0wdOOJLLCUUJLLLLLCJLLLCLQLJJUUvxrtxnxUU|
                                  ^,.^" ^:"_r.^.'^                                    ;
                                  "        'l                                        .!
                                  ","""^"""^'^"^^""^^^^^^^""^"^^^^```^"^^^^"""^^^^^^^^:
                                                .
                                                <<-'_!_.<_~~>[-i!:+i?_?l_<~~_~
                                                .':.`'` '^^^`"^`''`.^^`'.^``"^






















```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-286



SECTION 2 PROGRAM OPERATION



15-2-3. Editing Modes



Lines 4 to 7 of the command creation screen have two editing modes, function key [F5J



(OVERWR/INSERT).



Immediately after displaying the command creation screen, the overwrite mode will be effective.



(1) Overwrite Mode



The overwrite mode is used to fix the command displayed in lines 4 to 7 of the command creation



screen in order to overwrite a character or characters in the command.



In the example shown below, ''1" is entered at the position of the edit pointer and the edit pointer



moves to the posrtion of the next character":". Note that in this case none of the characters has



moved.



OVERWRITE MODE



COPY OVERWR 17:



r ""'""""·"" ~



EDIT POINTER



COPY OVERl\"R I TE



Fig. 2-6 Editing Modes (Overwrite Mode)



(2) Insert Mode



The insert mode is used to insert additional characters into the command displayed in lines 4 to 7 of



the command creation screen.



In the example shown below, the character string to the right of the edit pointer - "AM.MIN" moves



to the right to accommodate the character "R" as it is inserted at the left of the edit pointer.



INSERT MOOE



COPY INSERT



,OOC,tU,iM,M" I



"EDIT POINTER



COPY INSERT



Fig. 2-7 Editing Modes (Insert Mode)


```text


                                                                                               ^^^^'" ^`'^"'
                                                                         ..  .. .    ..       `]?_?i] ~!<[1!
                                                                         <1-~>~_?];-.__-~~?[_?{li-<?<?-<+>[l
           `^`^^^``^``````^``^^`'''''''''''''.''.'''...''''..............'``'..`'''`...'`'^''`^'`'.^'``.'``'
          ."""","::""^^^^"^,,""::,:",;;;;;;;:,::,,,:,,,;;;;:::IIIIII;;::::,,,;IIIII,,:I,:I;III;I;:::;::;;;;"
           l<:i;l `+!~ilIl?ll<i^
           ";":", .:,;;;!"i:;!I'
                ,I!!!'I:;.:^!^ii^I!iii>>~iI<>+~>>"i!i<+;I<>!I!<i,i>?ill:!l!>>^;>!l<>!"lil"+i+^
                `<~_]~-_-+><+~?]+_~:""::;",;;l;;:`;;,II^^Il;:"lI"II!;;<":;II!,^!I;!!l^;!>,>:<^
                 I::Il:lIlII;!!ll,;.
                :I;;I;>!lll'l<l"^!I!<l!I;,i!":I;IIIl;I";Il>;I^:::;;:.l!:`:,;:;;!"":,;;`:l:":`:i;"I",'
                ";::illi!li`!Ii^^!i>>~il~:l>:I!;Il!>;I:li<+!>"iiI<<!`!~>,i!~!<l_l:i!<+,<~;I~:~+_i+i~;
                 ."^  ,"^"^,";';!`^,
                 :ll .Il!<l>l+I!_l>+'
                      ;::`^^:":,::.,:;>","`;::II^ll^II"",;:;,;::^!,:I:,,:,"";":`"",.:':,:"``"""""^^,`^"":"^'
                      II+!i>~<><<-l<~>-l!il-++!<;>_;i+!!>><>~_>iI-+__?_<+!II<>-l!l~:;"+:<~Il~<<>>+i<I~~_]~~:
                      i>l>~;^!.ll~+^<::i<<>i!_"i">!~i_>+,"!'<i_i-!+>!^I:+~l;<<>>><!-.
                      "'",^."`,^^""."^`^".^^^^^.`"```'^^"^`^'``^"`.``^"`'.`"""`.^^".''`^'..''```..'^^.'''''.
                      <Ii>~:_<-<~+_,+ii+_,i?_~_I.I`;+;<i-~<_;]!!_~,+<-~i+"><l+~:__~!_+>+["!]~><+~"_?+;_+~<_,
                      I>!l<i:~"?+Ii~~__!l,<,~+I:-~-;_~?<-<]>`,` <-_?;+<]I<;i++">~<~:<>i~^~!><l:<<<~+-?<il_-:
                      !>><__"'. ..`.'...... .'' ''....^'^'`'    .'`^''`".'.'`^'^"^".`^`".^.'^`'`^"^,""`".,:`
                      ^",,::'
                                  ........................................ :<~~+_]~i>I?~~_,
                                                                           ":.     ...````.
                              iYnXLCCCCCCCCJCLLCLJJJJJJJJJJJJJJJJJJJJCJJJcxY/nuuUJ{
                              lj}\OXrvuuttf|[???]]]]]][[[[[[[[[[[[[[[}[[[-~<<-?_[[?
                              ,    !.'"`` `''``'                                  ;
                              :^''..">_>!;<<+~<<I.''''..'''.....'''''''''....''.''!
                              .^``^``^''''.'     '^^^`ii`^`:;;;,```````````````````
                                                      <<  :^.l.:"
                                                      <<  I'"]'";
                                                      >> ',<>:]:
                                                      ?- ^. "!"
                              ':"",^,""",,",:,""""""""{[""^;!^`^^^^^^^"^^``^^"^^^^.
                              ]qYwkMkkkhkbkbpwmmmmmwqqmmqqwZZwwwwwwwwwqwwJvnrCYLww[
                              l+:><f>___~i~!^.......''''''..''''''''''''''''..'''`:
                              I                                                   :
                              I;"^^^^^^'''^^^^^^^^^^^^`'```^^"^^""""^"""",""^""`^":
                               ''''''''...'''' ....'..    .  .. .''.  . . '.  .  '
                                            ><~'<l-.?~?-!~l[+>~~lI+>>+i~>?;~]i~_!
                                            .';.^'^ ^^""';`"^"",^^"^",^,^:^^:"":"

                 >{! "<>_?<<1~+?,
                 '`. ."^^^''`^^^' . .     .      .
                      >!~,i>~+Il><-<l!;<~~l>Iii_-~<[]?_~i-_!__+_~__+ii-~I?_I<+~<i~->+>+_+?_+~~>l~>~~;!~!!;~,
                     "?<Ili>!!<><<;~>+?~+:><><~>^ .'.....'...''''.'.'..'..'.'`''.``''''"^^,^^'''''^^..``..`
                     .^"^`"`''""^`'"","^"'",^",^.
                     ^>;_>;i><>~<~:!<li<:!>ll>^~ii;~iiiii~,i~lii!i!~>;i+>;I>ii!I<?ll!>!~I.`:_?!i++<'':>ii<~`
                     "~:?+il~-~>-;>>><~<>>~+--;-<!I+<~>~<_:l}i;]I>l<l!<?>>>>;~i-_i>--l+_~l"l<-:i>!i;:`,:,:;'
                     ';`;;:`!!:^;`I;II:::I;l!!"lI:"II!;lI!" ;`'i::,!":l!ll!I"l`;;`;!:"I"l<,>!!"il:I~;
                                                                             :l!ii;:iI;l
                                                                             :l:^'  ;::;'
                                i|{|/t\/\\/\/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|)t[}|||\;
                                ?JrC0CqwhbQw0UvvvvvzXXXXXXXXXXXXXXXXvczXzvvu\(/rcvuc+
                                ''    .'I-``                                        `
                                ^ .  .   `,!<+<>-+_i~+I. ...............''''....''.`;
                                `"^"^""""^^"",""","^""^^i^^^::::;:^^^^^^,:,"""^""^^"^
                                                        1  `:'"^`,.
                                                        ]  `` {< "'
                                                        -  "!+l_l:.
                                                       .}.,:`,!i^.
                                                        n    `.
                                1YuQZZmZZmOOOOO0QOOOO0OZw000O0QOOO000QOOOOOO0vxncO0O<
                                ~1+\([tttJ\\f1-<<<<<<<~+~_+++~<<~++++~<<<<<<<!l!i<<~I
                                I                                                   :
                                !^""^^^````````````````````````^````````'.'^^"^````,;
                                .'^``''''''''`"'.''`^``'''..`'''..'''.......'```'''`.
                                             "+_I,+;::-~[_~i~[i+-~,_<+_?i-?i--!
                                               ^^.'   ''''^".'''``.`'`^`.''`^^`













```

*Figure from page 10 (2346x3317 px)*


---



4203-E P-287


#### SECTION 2 PROGRAM OPERATION

(3) Switching between Editing Modes



To change the editing mode, press function key [F5} (OVERWR/INSERT). If the overwrite mode is



currently effective the insert mode will become effective, and if the insert mode is currently effective



the overwrite mode will become effective.



liiiii!fffilt:!!t



l....~---•---



INlEX l'.liSP!..AY ~



tF?i -;:,, 11cn;•.111N



:FJJ -;. FDCr.•.¥1!f



0'.S!f!IU



OVERWRITE MODE



11()£}:; OIP..A1" ~



(P:2! -> l()i:"'.t.llN



(Fl!



;::',.ti:'",lllllt



to or5?!.J.'I' O:H.€R I~. .. ~ F'RESS1HG [!='l,J,



USSEB!



INSERT MODE



i'O O,l~Y 0~ 1flU.X$.k"1c'R ~SStHO; [Fl],



Uf'VfirECEVIQ: ~ N(l ;:Jlf~.MN~ {11Jli7i,~ ~.



t;JEF'JULT O&lai ~ - El;



l!FU1' Tt!C :;E'nt::E fWIE UC Fi LE MME:.ike'H PRESS (J1Rr-:1'.J ,::g,



OEFAIA.T OC.IICE. !WE .,,, 101:



eEFJi!Jl.T FU.I MIIE - •.vnc CEFAI.\J" Fl~:1 ~ - •.itlN



Fig. 2-8 Switching between Editing Modes



15-2-4. Deleting Characters



(1) Function Key [F5] (CHAR DELETE)



Use of this key deletes a single character atthe position of the edit pointer, whereupon the character



string to the right of the deleted character shifts one place to the left to close the space. The edit



pointer remains at the same position.



In the example shown below, the character "A" located by the edit pointer is deleted and the



character string ":PROGRAM.MIN"tothe right of the edit pointer moves one place to the left to close



the space.



CO?Y OVERWRITE



r"·-""



'\_ EDIT POINTER



(CHAA DELm)



C0°Y OVERWR IT£



Fig. 2-9 Deleting Characters {Function Key [F5])


```text


                                                                                               '^^^`^` ".^^".
                                                                          .'..`...    '.       !]-]+-~ <I[[~'
                                                                         .]1+<+++]+iI"-]?+_]?-)?;~___--+>i+]"
           '``````^^^````````````^`^`'''''````'''''''....'''..............`''' .`''''...``''''``'`.'`'``.'``.
           ^,,::::,",::^^^`^",":,""""^^,^"",,,,`^^^"",,,,;;;;;:::;;::;IIII;;I;:::::IIIIIII::;,,;IIIIIII;;:::'
                  ;-: '_i>ii>l!:!ii!!!l^~l~>III-il>!:
                  :!" 'I:;;,,,>:;l:I;I"`::lI;i^i;IlI,
                      .~:"~I>l>I;i!^!<+:l:;;;<I l;ll;;!ll+!I;>i;I<>!:>><~~_<~~<->+~<i>" iI<I":Il;lI<!"IIli^l`
                      .lli<>-++<?~<><<<<-il><_<l_l++ll_!><>!l~~i?_<~<il;~!<~<~~>>~<iil!^!ii>;l!<!~<_<;-+~?;~,
                      ^~!I>!!~:>-+!<!<!ii:!>~<Ilil><I-i;<>!!!<iI_+<<<ii`-l>lI!<!Ii~<l:i<>~:>l!il>!i<:i+_<~i~"
                      ^+<:l><>_>>+,<<>[lI_+;__<~>~ll?-~-_~>
                                              .
                                               ">>><>!!!i!!iiillllllllllllIIIIII;::,
                                              fc11111{1)))))))11(((((((())))))(||((fz:
                                  ...  .     ,h;                                    Yv
                       ';~]?~-[+~lIlII;li-+~!Il;Il!ll;::II;;.."l>iii<!il:,:ll;:li<>;<+::;:::::::;;`
                       :"_\[_+]+-illiIIl<[[]i!lllli!!<+_<!!I, ;;){[_[-]_IIIllII+}[-I::l!!!l!+<!ll:I.
                       ,"_\l^"`^^,:,,",,"``^"""^""",i?__>:;:".,!/{::",,::;:::;l;,,,;;;;,::;_]-:,I;;'
                       ,:"                   l!ii>!l~;il>^ :" :l.'                    ">ii<l!l!, ;l.
                       :^,i;,!;^l:l;         ''^'``''`"^"' ;".I"::,;:";;Il"^^""""""""";ill;:i!i;:";.
                       ^.`|!:i}~~)i"                       :^.: ]{"i_+l[-I.                       ;
                       `."+i>l<];+>:,I:Iil;,,.             ,`.".<i;I;-!~<"`",`,",`^               ;
                       ".l1<~[]?<1[??!l+]!_!_l;l:"!'       :`':.?_i~>~~+(-[i<!(~]~++,i::;l        I
                       ;';?_;><>{>^^<!                     :'':.[[>l<!]{I'i<^        . ...        l
                       "'            .                     ,."l '''   ^.   `'                     !
                       ^.                                  ,.^:                                   ;
                       I'^...'   ..  .   ..  .         ... l.":..                                 I
                       I"^!i"l-+IIi];i[1{l~1};i-I::::,:``^.; ,;'":":l>:;:+l,<]]iI~-!:><,:,"^""'`^'!
                       .,l]]!!>{?i![]>-?}<i1}>>1-<l?}>l;:;;"  ::>{~!i[1<l{\~+{|?!]|?l[1_li1?I;::;;^
                         :l::_;i,<Il;;:i,+i>!lI!!l>ll:~i~!;    I>!"!;il<!<iIllll-!~Ii"<!<l>I~i<~!"
                         ^^`^^```"`^^^"^,!!_>[<",,:"^":",,^    ^,"^:",,;;;:,,,:!<>]l>:;":",";:,;:'
                                          ', Xc                                  ^ ~a`
                                             "xjttt\\////\|||\|||\/\///\|||\/\\\//|c]
                                               .''.^''`'``^`^^^^^^^^""^^^"":"","",,
                                            lll.;,! I!:l:;",^,;I:,,;^,:;l^,'II^:,"
                                            :;-`I:<.I<ii!lI>>I+<>>>~;Ii><;_i>~i<~<'

           :<,>,i .>>>>il!,iiIl!li!!:
           ^l"I^;  :IlI;,>,,,;l;I;l,"
                 .;,  :I`",I""`I:^'iIl`lI;I!I"li:;IIi:
                 'll` :;;I!il;"i<i:<;i^!;Ili:"!<li:;!l
                      ";;"`ll!:^:::"!llI:^"^;:,l,`I",;;!l`ll!l",;;II:;^ll!;":!;",:;l;'^l;:::",,^;!:^;,:::::"
                      ;+~<li<!~i>>~i?>~__>>!-<?}<>!~~<><+;~!~_+<>~<i!<!>i>_I+_!><_>_~:i+<~~+~~i;!~~:>+-i~<-<
                      :~!>_:+,!>!">-!^iIi<!^_~~~<i,~>~!+!_;,_<_~^i!>:~_<~;~;>!i;~_;>^!<>-ll<<"?++i<. <i+,~~i.
                      l<<I+_^i_i<]>~"]:~+;I?+i_:_>~+>+,
                      "^'"^'.``'^```."`'``'^``^^^'"`''^'...'...'''.. .. ... .'   .'.   .   .             .
                      !>'~_;:+~+i+~<^_<>~-"I+<i+! ~<>'+i_i~~_i I_.I~i_]~>,_I`+-^i_]"l~ii~+'l!.--+?+<`<~~"lii
                      :~i<!ii~,>_i!~"<_?_~+--_[_>{+?I<!~_i!_-+Ii>_<I~?+i<<<_+;>ii<+li<<l<~><i~!_<ii-+<ll~!<<
                      <?>l+<<<!"^'`; '.'`'^^``"^'"`^ ^^^""'II^^"`""`,,":,,^":'^"",:"^",,:,::^:""",^I,,"";,;;
                      ,lI^>l!;l.

                                 t0YZpqwqwwwmmmZZZZZOO0OOOOOOOOOQQQQQQQQQCCUxnrxvrJJu
                                 ](_)xJ}/\\\{t{_!!l!iii<<<<<<<<<~++++++++___<~<~_~]]{'
                                 ;    ;^ `.. ' ' ''                                 ^`
                                 !"^^^'^!?_~i-+]++}~^"^^^^^`'`^^`'`"""""^^^^^""^``^`i'
                                 .'...'.   .. .     '``'<+'^l::,:l`''''`'..'```^`````
                                                        __ ^:">_"^i<i>~Ii+l!l~:
                                                        -- ^!+~]+,,"`^`'^^^`'^^
                                  . ....................~<'I::;~!^
                                                        [+    `
                                 {t/rrrxxxxxxxrxxxxnnnnxJYjjrxffjttttttttt/(}{[}1}))-
                                 jzfJdkQmOmCLLzjfjxxxnxxrrxuvuvvvuuuuvvccccn/f\txrXYx
                                'I   `^ . .                                         ".
                                `! .   .       ............................. .    ..l.
                                 :"",,:::"^^^`^^^"""^^^^^^^"::,^^^^^^^^":"""^^"":"^";
                                         '`  . ' '.  .   ''         `.      ..   '..
                                         i>[^+i[`i---{~-~<+_?<_+-~<;?i_>~+_>>?-i!-_];
                                           '           ''   . . .  .  .   .   ''.  `.














```

*Figure from page 11 (2346x3317 px)*


---



4203-E P-288



SECTION 2 PROGRAM OPERATION



(2) BS Key (Backspace Key)



Use of this key deletes a srngle character to the left of the edit pointer and causes the character



string that starts at the position of the edit pointer to move one place to the left to close the space.



In the example shown below the character "N' to the left of the edit pointer ls deleted and the



character string ":PROGRAM.MIN" that starts at the position of the edit pointer shifts one place to



the left.



COPY OVERl'lfl I TE



f"-'""""'"''



"EDIT POINTER



COPY OVERWA ITE



[C O ""'8 """"· M< I



Fig. 2-10 Deleting Characters (BS Key)



15-2-5. Notes on Creating and Editing Commands



(1) Maximum Command Length



The downward-pointing arrow symbol



"f'



signifies the end of the command and the maximum



command length of 255 characters is reached when this symbol is at the right end of the seventh



line.



When the "insert" editing mode is effective, it is not possible to key in a character at any position



when this limit has been reached.


```text


                                                                                               `^""'^'."."""
                                                                          ...''...   .'......  <?_[i+;,<I]{?
                                                                         ^[}+><~_[!~,;_]?_][--}+;_+[+-->~+++.
           '^''````````^^^^````````````^``'''''''''''''''...'''''''''''''.''''.'`''`'...''`'''`''` '`'''.`'`
           ":,",,,^^::,"","^^,^``""""",":"^^^:;;;;;;;;;;:,,,;;;;;;;;;;;;;::::III;II;I;::;,,III;II::,;::::;I;
                  l+^ ,]+:<!!'~]>!i!!!li,~!lI
                  ;l^ `I:'::!';Ii;:li;;I`:;i;
                      ^lii.>"i!l'!l:'<<i>!l';,l;>_:;>ii>i<>"i:l~i"i-l;!l<!^li+^l!i<<:^iI!"l!;ii:;>l'l!l;!l!I.
                      "-_+!i+<_ii__]I>_<~+!l>i_i?il~i_~i~--,<ii~~,~>l>!l<!;<<!i+><i-:>-i>i-~<i+!l<ii<!<i~<+l
                      ^il;~;!I<^i>!!l,l^:l:iIiill':;"li`i>I;!i;li'l,,IIll`!I!:>>ii^I:!!!:<l,i"!lii^>i;:_<>i:
                      ^, !;".;"l^,l: I:,:I`^:;";`;l" ::;::,l; ^!'",.!;^^:! :"":" ,:I."",,:^.,.",::;"^`,"^^:"
                      ">;<<!!-><<-_<"~__]?ii]_+]l<--l><+~~~_+,"~"!_">~!I?>,~;i~+"~+_l_~<>[i^+:_?~+_+;l_ilI<<.
                      :<i_!~~_I,[i!]l'i!+><_<<+-l_-+~'<<_"_+<]l<+i~~"ii+_<<"i~i~<,<<>I<+>_-"+_<-l:l~!!-_~<I+.
                      !_~;_]i                                                        .               . ..  .
                      ..'.'''
                                   `^^^^`'```````''''''.......
                                   v0Udh*hkkkkbkbpwwwwwmwwwwwwqwwwwwwwwwwmZOZZXnxrCuQZml
                                   <~;+_xj_[_[<_>l''''`""""",::;;;;;;;;;;;;;II::::;:;I!,
                                  ."     :^'^``'^^,",,.                                ^
                                  .:^"^^`'^!~<ll><_!~~I```````^^^````'^^^^^^```'''````,,
                                   .'`'''''   ..   .  ''''`'}:^l;,:Il;^"^^^^^``````^^^^.
                                                            1^ `:]!_`I
                                                            )^ :l[<[,l
                                      ..............      . (^"l,:I+:'
                                                            x.   ''
                                   {))\||\|()(((|\\|||()))))c|))))}{{[[[[[[[[[_+~~?~?[].
                                   xznOakOwwqOOOCccczXXXXXXXvzXXYYYYUJJJJJJJJUrfttcjYJQ:
                                  .`   ," '.'..                                       ',
                                  '"             ...............                      :,
                                   ,":,""""""^`^^^'''``^^^^^^^^""^^^^""""^^^^``^`^^^"^:'
                                             ":' `''^.`"`^``'.`"''''``''.,,^'^..'
                                             !<[,il;_"l_--_>~~!<>-<_+]+_:}]_!-_-i
                                                             .
           ^;`:^" .;^""^.^`^,^^""^'.^`^":",``'"^``````^^.
           :_I~I< .~~~_>,+l;>i+?>>-,-<>!~+_!_!l<~>>>_<<-^
                  '   '`. ..    . '.         .'
                 `<~' +[--~>i<i;<~~<<~-<<l<-~]]^
                      ',^' ^^^`````^.^``^`` `"'``.`'^"``'``.'`.`,``.^`' ''`.'^``. ..'''''.' '''.^. ....'. ..
                      ,!_!,+>->_+_i~-<i<_i]"~<l~~^++!-~<',!.<?]i+-_"~-<^+l_"~l>-~`!<>i>_<i<,[i~"_-,,~_~<!>ii
                      ;ili><<li;?i+[~,_;-]]:+<-~++-+<,<:-__+<_<I-<~!,~<iI_<~?>!;il]I++,>??ii+~il<>?<,~+!~<{i
                      <<+: .... '.^` .'.'...'.`'`''''.'.'``'''.'`'`..''`',`.``''`'^.'^''I^'`^^'^`'^"'""^"^"`
                      ^^:'
                      !+!<<^+<!^i!<<<`I<_<!~:i>!+;:!I[[<~~<<'~;>,i~;i>~~-~~,~;><<"<,!,i<>!~>+i`_I!<<,>!>_iiI
                      l_<_l:~~!:!<<>>!I~~~<<i>~>~ii;'^^"^^^".^'".^"`:",,,",'"`^:;'"',`"^:^:,;,.I^::I^;,::,:^
                      :lI!"^;l,":I"^;!":l!I`:liI,lI^





































```

*Figure from page 12 (2346x3317 px)*


---



4203-E P-289



SECTION 2 PROGRAM OPERATION



(2) Automatic Space Insertion



When a character is keyed in while the edit pointer is located to the right of the downward-pointing



arrow«



f',



spaces are automatically inserted up to the position where that character is keyed in.



When the BS key is pressed while the edit pointer is located to the right of the downward-pointing



arrow"!", the edit pointer moves to the position of the downward-pointing arrow.



,00 ""'""'· ",. J



COPV OVEP.ffl' I TE



'EDIT POINTER



COPY OVERWRITE



COPY OVERIIRITE



L ""',,. .... _" ·-



COPY OIJERIIR I TE



[c o



,oo """''"·



",.1



Fig. 2-11 Automatic Space Insertion


```text


                                                                                               ^"""`, ^"',,^
                                                                         ..'.''... . '''...'..'-??[>]^li<{{_
                                                                         ;[_~><~~]l-'<~[++_]?-1Il-<_-?_~+<~<
           ^^^^^''``````^^^^^^^```````````````````'''''''''''.'''''.......''''.''''`....''`.''`'''.''''''`''
           :::::""`^,,^`""""""",^^^^""^^`",,,:;;;;:,,:,;;;;;:,:;:::,,,,,,,,:;;;;;;;;::;::I;III;;:;;,:;,:;;I:
                 .~+. I<l>!!!~!"+iii!"!!!l!ll"
                 'll. ^:;:,,:I:':!;I;`,:I:^,,`
                      l_lii"l"><>;i!>l,;;<!!>!,;:~<<:l>!,<~!;iii+i"!:il!+>ll>:<!!,i<i,!i<i:lili!!i!!;I;!ill!
                      l~!~_;i!l;-<-<->;~ii?~_i!!~_i-+:i<i+->+i>i~_,-i!i~+-_!<:<<~l-_+!_I~~ii~~+!<~><i~><<!I~
                      :l":!' , '>!iIil,il`iII;;!<ll>~,"l<!l~l`i>^i"l>:llliii;^i:i!I`!>i"ll~!<!<,"l"<~i>I:l
                      ;<iI;^>!I!<l"I:';`^I:;;I;":lI;`<:^^;i^,,::l,':';::I,,":^!,`^:;".:,I,'^,,,,::,"`""::;,,
                      l+i~~;i<i!->;+?~l!<<++~~~I~~<~!>-!!~_l_+i>~<;_;<>__~<l<I+<!I]_<I<:<+li>><!~~>!I~><>~i-
                      !~Ii+""l'l<<;~_-I++i~-,;i>i+<;_,-+l><~-~i<`<I!+!;+<+i-~]<l<>>i~i]I_!i+!
                                                                                      '
                           >)})\t\\\\//\\|\\\\|(((()11111111111111{}[[-_+~-~~--:
                           }CxCZJqdpp0OmJUXXXXXXYUUUUUUUUUYYCCLCCCCCCCvxxtXucLL[
                           :'  .  ^'`                     .1                   :;I;l:
                           ;..  .        ............ ... `>>i_>>;<i<i<<! .   'l`^`~}
                           ^""""",,:,^^^^^^^^""""""",<!"^:,^,!!I:,;Il;Il;^^","""   l-
                                                     _l I"':`';                    !-
                                                     _: l "|; !                    !?
                                                     +, ll<:?I:                    i-
                                                     )I`"."iI'                     >~
                           .'''...................   \!  .:'                       >+
                           tOYwpwdpddqpdwwwwqwwwwwmZZ0OZmwwOQOZmmmmmmmXunrUvCOO< . <+
                           <-I]-~][]1~?];""",,,,,,,::::::;;>]Il!l!!!!!lIlI!l!i~! . +~
                           `                               l{                  ; . ~>
                           :^^^^^^^^^^^"^``^^^^^^^^^^"^^^^^' `'``^^^^^^^"^````",   _<
                            .......................''}"':I:,::l'''''''''`''''''    ?<
                                                     }' ^'->?";.                   ?>  '^'^`^`
                                                     1` ":+>?l:.                   ?i  ,;-;>^I
                                                   ..)`^;""I>:'.......      ...    ?i  :;)~?^l
                                                     n'   ..                       ?i `l;::_:^
                           jzuC0Q0QQQQ0QQQCLQQQQQQQQCZCCCLCUCCCJYYUUUYj/\\xtcXX, . -i `  :l`
                           }{_\({rjff)f\_~~+-------?]?]]]]11]][][[}}}}__-_[_}{|; . ]!   '^
                          .,                              ~<                   "   [l
                          .I'''''''''''''''''''.''.....'''..'''...''''......'',"   ]:
                           ```````````^^``````''`^''''`^^^^^^:^^^^^^^^^^^^^^"":.   ],
                                                                                   {:
                                                                                   1"
                                                                                   }^
                                                                                   1`
                           +__]}[[??-???_?----_____+++++~~<<<<<<<<<<<!lI;IlI!il    1'
                          'YzumOZppwwOmm#CJJCLCCCCCQQQQQQQ0OOOOOOOOOOCrrfuUvOZU    1.
                          ',` `  ^,":```i                                     ^^iI^)
                          `^              .......                             l"+i,,
                          .:""""^""""""""""""""^,"^^^^""":"^^^^^^^^^`^^^^^^'^^;.
                                              .`  .'.'  ' . . '. `     .   ..
                                              :<[l;<,<.I]>+~~_{_,-----!i~____~i
                                                '.       .        . ..   ..  .
































```

*Figure from page 13 (2346x3317 px)*


---



15-3. Use of the Command History



4203-E P-290



SECTION 2 PROGRAM OPERATION



The last 5 commands which have been used are stored as the "command log". Previously created



commands can therefore by used again by selecting them from the command log. They can also be



revised before they are used.



{1) At the command creation screen, press function key [F4) (COMMAND HISTORY) to switch to



the command history screen.



(2) Use the cursor control keys to move the cursor to the desired command.



(3) Press the WRITE key.



The system will return to the Command Selection screen, and the selected command will be read



into lines 4 to 7. To execute the command as it is, press the WRITE key.



If reading to the command selection screen is not required, press the [F7] (CANCEL) key at the



command history screen. The system will return to the command selection screen without reading



the selected command.



lltj



~EDIT POINTER



IIUX OISP!.,ic't ~



{F:!l -> ici:•.•••



{Fl) -



FCQ::•, •tN



IBMSAFR



TO Ol::PJ.Y OnER INOt)tES,~ ~SSHC (Fl}.



I~ ll1:: 0£V!Ce«Ai11E Ail0 FH.E.wiE.Til£H PR£5S (MITEJ X.~.



CEFNJ:.r O£Ytt£ fWE : llll;



OEFMT Fll.1 ttM1E • ".IIIUt



l.eiiwi



(ff961'l g;



uax 01SPJ.Y



LF2i fiei1:"',IIUN



(Fll FtQ:f',IUN



TO OISP!..AY 0~ !ta'Xi:S,~ ~ING fFl].



IMPU'T T~E QE\/lce It'll€ All) .CH.i HAIE. 'l"HEN ~ f¥ftm:J x:~.



CEF4U..i ONICc HNI!: - El!



OEFMA.'r F!t.: "'6E - -.lt!l'I'



lf:1!0GW ft5!iljQk JBM!SrTI



CO RXr.f'!'IIIJWI.IIIH.Fol:



mae•~



ii ~)~~,\\'r,W,'~•~=lfJ~SSA/l£.



m 'CURSOR



pr:\0T JDl~TES'T.lfJH~C '


# '~ l._ ______ __,,,J

Fig. 2-12 Use of the Command History


```text


                                                                                               `^^^'".'".^^`
                                                                          ..... .     .        -[_]i[:l~l[{~
                                                                         :]}+<+~+[!_`~~?__-[?-{>I+<_+--<~~_-
           ````^````''''`''```'````'''''''''''''''........................``''.''''`...'`'`'`'^''`.``'`''^'`
           ",,:";;;,"^^",^"",,:::,,"^^^^^,:,,"",,:::::::IIII;:;I:::::::::,;IIIII;;:,;::IIIIII;;;::;:;;;II;;:
           ;i!"~   lIii^:<;+II^>I;lII;lIll"!il!:;,
           :!!:<'  I!<+^!l:<!<^!!ii!!i_i~i"!>+~>>_
                .!;: ",:.; ^^":^""`:..,,^:.`^`^''":," ,:,:',"`';,",:'"".;,``,^"""^"",`"^". ::^^"^`"^.'^^^"^^
                .li_,~_~:+^<<i>>-~>?ll_i_>";++_l:~_~I"~~~<,+<!,_<~~~"_+^<~l^i>>ii>+><^~}i  !<-<i>~~+;;>~_-+i.
                ^i>!il~<i-:">+.I!+!<<>!'<!^~__<"[??+:<-`i_]+~?~_"~~~~^-><II-~"!<~~<~-<<l<]; I~<_l,~_,:]+i^+_
                `+~~__+!__-~~;]+_I!+~"~-~-,.... .^.   '... .. .". .. . ...  '..'....'....^'   .^`.`'..'''.''
                 `''""` ^`.`` '`"'.``.^^`'
                 .ii. ,~">!^,l!lIIiIl"Il!~l!^;l!ii!';!!ii:>Ilil!,I!!^<i<;li!~+-<><<i^!<>!ii+ii"l":lli!::;
                 '::' i+lI>!!<<>><~><i><<<>>Ii~!ll;^lIl!!^lIIl;!":!>,l"i;II;liiili!l`;!!:;!!Il,!:l>!<>:Ii
                      !i>^!il!!~!i,;i+ill"<I>~i:
                  ""  .. .'`    . .   .'.'     ...'....`'.. ..... .`. .......  ...   .
                 `??' l~?<i?_;_<<_~,i+~]+~l-_-><>I_+<-l_-!l<~__Il<i[_;+[->+-!i__~~~+<_.
                      ..    .  ..'.''
                 `][' i<_-[l-+!i}-[>[ii--;
                  ..  `^`'`''^''. '`.'`'"''.'`..^...'....''...'. .  .. .    .'.      .
                      :!~!l-~_+<;i]-;-?<<"i!!-<:~i~ii<+>>;?++!-+<;i~>__>^i~<><~<:??->-?+l+<>i>+>+!+-I~-;<-_<
                      :i~:_++<:!i~"i ;_:><_~i+~l_+;!><>>~<<il_;~!~'<<~~!!-+;_-]_<];~<<`  .. . ... .. .'..'`.
                      `^^.`^"^.``"'.  ^'"""^^""'`"'""^^`""^'`:'^',':^"""'^,'^^``.".":l'
                      >:l~~_><<>l"-~"!>>i!<~<<"__~l_ii`iiI~~;`<^iil,~~<i!~:'ii>~:!~>^]!-"ii~~-<?+;">>i'_Iii!
                      ,I!ii!>>>!+~+i!,>!!i~i'I_~ii<<-<il<__!+~<iI~I_+<iii~<!_>~<<<<<~~lI!i><~lI~_~!!<<i+i+><
                      i~>;i<_i<i_>~>+l<>i~i" .":,"!;lI:^;l:^llI,^I,I;:"I;;;;i;;:ill;lll"IIIii""iI;!l:,ii!!l~
                      I!i"~<<i~~i,iiI!!~l>:

                          ^,:"","^^^^^^"^^"^^^`^`^"^^``^"^^`^'   ``'''''''``^^```'..'``````^^`'`'``'
                         ";[1)[}1-?Iliilll<){{<I:IllI;:Il;Ilil' ;![[]_]~_>Illllll_{[_lllllI!<>l;li<I:
                         ,^1/iIIl!!;;:;;IIIllIlIlIIIlIl?{[_ii:: 'l\[<~~>><>i!>iI!i!I;:;:;!lII~[[_<!"I
                         ";i~I"""`"^"""^            ...'`''.Il" "I!l:!ll;i>>l<+^"`````^^^'...'",^''"l
                         ,,"."<_iI<>~~_i^^^^^^`'````'''.'''`";^.;^  .....     ^l->li>~>~~`..''''.'`"l
                         :':|<l~+l_?~;  ........''.......'.'.,^.I.+?l~+i>-__^''......... ..'''``'''.l
                         ".^]l;;{_>}'  .                     ^'.: <+"I>]I]~                         l
                         ,.I_<_>+[![}?<_>?{_]>_;,:"^:.       ".';._!i<l-+l1_+!~l{_-><>`;"^^"        i
                         ;.!\]![?+))!<];^",':',"^^``".       :''I [1>i-_-|?I}<,^l^:;,l^;,"""        >
                         ,.^I;`"":i`. ,:                     :''I li;':"<!^ `l^                     I
                         ,.                                  ^.`l                                   I
                         l'                                  ` ^I                                   I
                         ;."``^:;"`"::^:;lI:III,:;^^"`'`"`^^.:.`,.` .^"^ ^""''","^"^^`^^^'"`.'^"^^` I
                         ":^_?:;_[~;i\->)t/>+|/i>|_!:>_l,^``^I .l^I-I;>[-!;]}l<|t["?|?I?1>!l+>l;^^^,:
                          ^!>ll~;!l>I><Il>l;;il;!li!!!i!>l!lI   .^":^''^:^'`:"`^"~x"l!,^,,`^;:^``^^^
                          .I;::>:l;;,l;I>?<:l!l;l;!;III:~,>l"                    ~a..:;^`^
                           .... ...',"^^:i`J?........'''.'.'                     <q  l>1[;
                                        .  h{                                    +k ":+(~!
                          '''.'`'''^^```'`'x_.````'''''````'.    ..      .''''''.>L  ^illI.......'.
                         :I]}}-{]__;llllll+??]i!!lIllll;;Il!!; ';>?]?-]_-iIIIl!l!_}?<lIIIIlllI;:;l!;^
                         i:|1i!ii!!IIlllll!<>!;:;;;;;;!?{-+!;I.^^+t?~<~><!IllIll!<_~illllll!l-}{]>l"!
                         <'ii ....''''''''...    .....`:;,"`'l.''I[:.'...'''`''''...'''``'`^`;ll;^``l
                         i   '  '                            !.'`                                  'l
                         ;~Q0Cnzzjtffrjttttt/\tt/\\\t|((|||\i, ,"?/r)(t\_~~l::;:,:;III;,;;;;Ill!lIl,I
                         ;i)|1fj|)tnc\t_1{]][?>!!!i!__-_[]?_:: ^^/ncczzczrzjtxvXcnnnx/////fxt//t//t:"
                         :i(](-}1)1_l~i!_<i~<>~i<:;. .,"::,^`l '^)[11})11{?~]!~]+_-<?_>>:I.^;i<+<<;:,
                        .l':^,^"^""'''.''.'''.'''```"^``''`^'; "^;;;!:lI!;'````''`^``,"""^"^":,,:,"^I
                         "                                   ; ,^                                  `I
                         ^                                   " "`                                  `I
                        .:                                   ^ '.                                  ^l
                        .;."''^^''`````^``'"''`^``'`. .``... , ,.``''^`''^^^'`'..''...`'''`. .`''''^I
                         I^^^^l;^`^"''^;.`^I^^`I"``,;~i^^''`^I ,:`^''i```i,^`;,''''.'`!```ii<;:"^^`,"
                          ^"""^`^^`"l;^;>,:Y,^''''''^:"````^^   ^`''''```^```````<]'```^``";l,''^`^^
                                    `^;}Z;'d{`'''''''...........               .'ZU
                                    `,i+l^ "\\\\\\\\\\|\\\\\\\\\\/\|||||||||||\\f(.
                                    . ".

                                             <++'<:!+`I<+!:_i?>;ii>ii><>>;~_+<i!.
                                             '`l'^''" `":^`"`""`^""^"":",'^:;:,I















```

*Figure from page 14 (2346x3317 px)*


---



4203-E P-291



SECTION 2 PROGRAM OPERATION



15-4. Selecting Files From Directories (OSP Format)



15-4-1. Procedure for Selecting Files from Directories



(1) At the Command Creation screen, press one of the following function keys:



[F1] (INDEX), [F2] {MD1: INDEX), [F3] (FD0:INDEX)



If function key [F1J (INDEX) is pressed, "ISO» will be displayed at the console line. Following the



"ISO'' character string, enter the desired device name and file name, then press the WRITE key.



(2) At the directory selection screen, use the cursor keys to locate the cursor at the file name of the



file to be selected.



(3) Press the WRITE key.



The display will return to the command creation screen and the device name and file name selected



with the cursor are entered at the position of the edit pointer.



Command crea~on screen



r,EDIT POINTER



l~OISP".,AY~



[~) -> lll1:•.lillk



{FJJ -► FtQ:"',l!IIN



ti) 01$1'1.AY OntEl'I !NJe:Xl$,~ PRESS,IHQ (F1j.



l!FVf 'J1,£ DEVICE 1WE M«'.l FILE K.4JI:. ilO fll!lle:SS [¥R11;J XE'(.



CE.F,u.:r ~ce MAJE - en:



CEFAUl.i ,:Cl!.E AA1i1E ,.. ... ii!N



Command creation screen



~eo w1:rcoui1-1NI



'EDIT POINTER



lffll;X 01$Pl..4Y ?!'«£!)!Jq('



['11 -> 11)1:•,"1•



[f'l] -



Foo:•,¥l'1\



10 C1$P'..AY On-ER IJaXES,k"'Te:t PR$€$J!tG [Ft'..



llf\IT iii£ :£,/la! MiE NfJ FI/.Z AA!E. 1'!-EN Pfl£SS ~f:'E} K..r:'f'.



IJEF.U..l' 0£¥1 CE: NA1E = i01:



OEFMLT FILI: l'IAIIE" • '".IIIN



Directory selection screen



I~ co



PX:2.IIIUI



~.il!H



P'X6.1t1N



:p;;xs,¥1,t



POlO,ti:IN



r'Ol2,llfl



P?'lUUft



POlS,¥1M



PJ19.imt



Fig. 2-13 Selecting a File from Directory



OYE:lf!H •



QVi::l!)fil"'=


```text


                                                                                               '^^^``' ,.^`'
                                                                          ....'..     ..       i]-?+>!'_I][i
                                                                         '])_<+__]+<I"_]-~-?]-{?:___+_-<><_[^
           .```^````````````''`''````````'''''''''''''''''''''.'..........'`''.'`''`'...`'`'''``.`.'`'`'.```
           '"":":;;:"""",,,^^,"^`^,:,:,,,:^"^",,,:,,,:,""",:;,,::"""^,::::;;IIIIIII;,:;;,;IIIIII:,:;:;;;I;;;.
           `l<'<'  ;+!i!;!!!l'<!i!I"+:I:;'>iI;;;I:I;;`"il><>'<:::;:!!
           .:i^i"  :<<i~i!i>[,;:<~<:l:<i!`iii<+>~il++;l~i+-I^!i<!~+[?`
           .^.. '  ``    .   `  '    '   ".       .
           "_>>ll^ !~<+__->_!<-,+]?-_[<-<~_-+!?>~;<-<-+?><[i .
                       .               `
                  !+l ^{l+?~l+<~<>--<>!~+_}]~!i?<~_~";~<_-;<+~"+i--i>_?>_-<+I~>i~_i;+-~_!
                  . .   "``.`""^"`,.`,^^',""^.^,^",^^'^:"^';""'^'`,"'^''``':.''''`'.'^""`
                       ']:~,+_]__<]"!~~?;[-<>^I?-?]~-'i~-_!_++<>]+]<<_
                      ':"``^,'`'^`'^I`^'::",,"".` ```^^.`'"","^'`^'`''"'''..'`.`'"'...'..'..'.. '^.`  .  ''
                      ;<!_<>__>,+++;-:>:_-?<]~+:_;_~-_~+i.;-+>`l-i,->"]+_~[~++,]l?_ll~<~<++,+-~ Ii~[>?<+<!+?^
                      '<[-<^i<_+_-[_`+?+<~.+>_-;]_i:[+-~?+;}~<~~"i+>~iI+<!~?lI_<i+,i-~~,~<<~il?_:-?]~~];-~>'
                        ..  ' . .'..    ., ....   ..'..'`. ^'''' '`.''.`'. .. ^' "..'`''^'`^`.'".'.'..^ ^",
                  >?, ^]Ii<l"_!illIl^>~~<<!>,li!i~!';><;+iI,ll!i;,i!i:<:I!li+I;!i`!:Il;`!;l!;l+;^l!l!^:!ll;
                  ":` :]il+l>+I~~+>_i-l,::",',:":;"`";;^":"^:",;^`;ll";"";:ll:^:I`l;:l:'l",I;"!;`li;!";:;I!
                      'Il"!^Il`!llI;!l.
                  "I' ^:`^`'""^.,:;,;:^"^'
                  i?, :li<+I!><"_<<l<<:<<>
                      ';"^'l,":,.":"':,^,^:^l:"^":,,,:,,^,":I^"`"",""`""":;"`":^"^^`^""^'^^^:,``^^^^'^""`"^^.
                      'l~+l[_++_i<_!I_~>il_l~+>!<~>!>+>><>~+-<<!_<>-~,+<~<<<!i-i<~i;--i~;+<<!~<I__!_I_??~-_+`
                      ,_?~;~~;iii~i`~+i,~<]<>_I->!<iI~>__ii^<i++i;+_;+~_<?-'
                                                    ..   .  .        .
                       :i!li!:;l!i:ll!:                      'I:;::,^,;;,"::;'
                       'l<-?-+_~+~>~>>!::llll:,,:::,:,,::,;:..:i~~~>>~+~i><>~l,::::,""""""::,"""",`
                       .;I{}[-{-?<ii!;Ill]{[~llll!illi<i!I!;; :,-{]+]]<<;!lII!l<11]iIIIlll!!!!!ii;;^
                       `;<t?":^^^^^,I::::,,,:::::;l;:<]]~;;"; ;"11i<ii-<,::::,,,"":ll;;IlIIl]}]<!;,"
                       ';:'I,::,,;:,:;                    `,: ;^"^`^^^:i^""`",""":.              ':^
                       ':":,l+iI>+-_ii,""""""``'^"^^^^""^`,"" I'''`"^'^";-<l!i!!i+;^^^^^^^``^''`^^,^
                       ^I {[,>?~![~;                       .; l !1;i~]!]?!`                     . "`
                       ^I.+<il>}i<<"^,;^;,,^".             'I ~ ;~;I:[~!_"''"``^^''               `.
                       ^I.]]-]+-_-\?{<<!)<-~++"i;,I:       'l ~ >_i-<--!)[[~~>]{+?i+I;!;,l.       ,'
                       ^;.{}<!]>[{;`~~`                    'I ~ ~1[I_++{_"!?I .  . ...'..'        "'
                       "l ''' '.`    '.                    ': > `^".''""   `"                     ^.
                       "l                                  '" !                                   ;'
                       ^,..  .       .                     ." l .                                 I'
                       "I',I",i_;::_l:>[}>l_[>:~~";",^:^^^`^; ;.,",":>l::!>";<-+;i+_ll<;,;","I^^^.;'
                        ,:>}<;!]}<l[)~~}1_I-1_:]1<I>]<I::,,:' ^,^~~"">}~:l{~;-{{ll11I!1_>:+]!;^^^,,
                         ,;;^-!<li!!l;iII;ill,i;i;i;I:~lii;.    .  ..   .       0?.l"",;:,  . ....
                         ^II:ii>+:,,:,;,:,,,:::^"^,,,"I:,,,                     d_ '`!<f~,
                         .""' .)<                            '^''`.'^`'`.''`'   k_ .^;[{>:
                               Qj .                          "l~<>!i+<!<!<>_i`^^u>'`'Ii!>:````````
                             . J\ .                           :I?]}_]-_~I::Illl_][?!!l;;;llllIII!I;
                             . J| .                          .:,)[i!!!!!lI;;Illl>i!ll!II;;;>[{-<l":.
                             . C| .                          .:'!i      ..   ...   ......  '`^`'..,
                             . O1                            .; '`""^"^'.'``... ..'''''''''..'`'' ;
                             . vY;"^^^^^^^^^^^^^^``````'''''`'">t-<+!>!"^"^,ii<_<~I,:,,,,,::;>[l!I;.
                                }tt/\\\\\ttttttjjffffff//ttrc!,;:`'`^^^^^^;lii!!I;.              ::.
                                                             '"?Jvunxrjrxxvnrr\   ~]++          .::.
                                                             '"~f+["              ]\?_           ^;.
                                                             .^~\<]: .            _}]_          .^l.
                                                             .`_1~}:              _][?          ';:.
                                                             ',i[<];^^^`````''``'`_--_`^``^^`'''`,"
                                                             `;.^`'"""",:"^^,^"";"^^:^^^"^..`"^^^ ;
                                                             .I"```;"``,;``^;`^^i```l<<_li_~",```^I
                                                               .'. .... .'.......````^",^"::^`^`^`
                                             <<~'~,i~.~_+~i->~;iI~_:iii!:<~ii>>il
                                             .^l.".`" ^:,,","!":'`;^`",^`":::,::;





















```

*Figure from page 15 (2346x3317 px)*


---



4203-E P-292



SECTION 2 PROGRAM OPERATION



15-4-2. Directory Selection Screen



If the selected device is OSP format, the directory selection screen will take the form shown below.



For its appearance when the selected device is MS-DOS format, refer to 15-5, "Selecting Files From



Directories (MS-DOS Format)".



Lines4 to 7 The command being created is displayed here.



The selected file name is entered at the position of the edit pointer. The edit pointer



cannot be moved by pressing the cursor keys.



Une9 The device name for the displayed directory is displayed here.



Lines 12 to 20 : The directory is displayed here.



Move the cursor to the file name to be selected by using the cursor keys.



If no file name is displayed, it means that the selected device does not contain files.



Up to 18 file names are displayed on each screen. If there are more than 18 registered



files in a directory, the page up/down keys can be used to display other pages.



The command being {



created is displayed



here.



The device name of -



directory is



displayed here.



The directory is



displayed here.



PRO\.."f!A~ OPERA TI ON TRANSFER



COPY OV'"t.RWR ITE



co D



'EDIT POINTER



P003.MIH



P005.MIN



P007.MIN



P009.MIN



POl l .Ml N



P013.MIII



P002. UI N



P015.MIN



P017.MIN


#### P004. MIN

P006.MlN



POOS.MIN



P010.MIN



P012.MIN



P014.MIN



P016.MIN



P018. MIN



Fig. 2-14 Directory Selection Screen


```text


                                                                                               ^^^"'"'':'"^^
                                                                          ''.''... . .''...'...~]+]>-;;<!]}_
                                                                         ,}]~>>~+-l+`i+[-+?][?{>;+~]+__><+_+.
           `^`^^^^^^^^^^^^````^^^^^^`^``````````''''''''''''''''''''''''''''''.''.'''...''`.''`''`.`''`'.`''
           `^^^,"::,""^"""^"^`^"""",,""^^^,;;;;;:,,,,:,,:;;;::::;;;;;;;;;;;;;;::;;;::;II;I;;::,:;;IIIII;,;;,
           :<,>;~  !~!<><ll"->+!!>!;I_Ilii,
           ':^,";  ^^":,:^;.:I;,",,^`I:,;l"
                ._<-~,~~+<~~i,<+ii~li;i+-_:_><>-l"-~,<~<><><:l~+~i+i!^<ii>i:;~_;+-i,~>I!!l>,<iIi>,!>ili,
                ."'^,',"^"^^"'^,^^:'^``",` "```:^ ":.^^""",,"^I:;,:,"':,":"`^:".!I:^":"`;""':"";:.:l:,I"
                `<!;'-";~!<<i!_l!;.?~<i'i>!^-+-!_~<'-+!<_:!ll]-!<<<];!>ii<~ ;~-+'i,'~!il <_><!<<iI!~~<:I<!!i.
                `~+>!+<i__;-[]+>_~->+~>!>+_I,^"^^"^.""^^,`^^'"^^"^^,``,^^::'`,,:."` "^^" `:,:,,,Il`^:;"'`"",.
                .;::,":":I'IlI:,::l,`";":!I.
                  "!><~"<;<^l  .  "<~!"i!!!i+~+l__-+iI>++?~<l<:]~~_+<+>>~>>:
                  .`'`^.''`..     ^::"^::""":,;",:"II^"::::"^:`;:I;!;:"^:;,^  ..     .        ..
                                  :~<l;-]-!-+II]!,+_>-^i"<!~~i<Ili;i<I+i~_<<;i<<[-:??-i-~~_?l !<-l>-[l_<_+]<
                                  "i+<>~l_~:+~!<_i>~,~>~~-~~I__>;>!<~ii+~<i. .  .'.'. `'...'.   '.''.'^''.`'
                  .....'          ^l:^^:`,,'",^,:^,I"l",:;"l:^",^::,:^';:I"
                  ll>_:?       '. :<+i:_<~>+"~?>~;i+^+_>"____-~_<;}i~+-i~,_:]]_-__-~I--_<
                  ^"",,.":^"';:.  ,;,^^;",::"^""`:"","^"",,:,,`'..'.''''^.'.''^'`"'' '`''
                  ;>!++^Ii:<:-i`. ":!I:<I<<~i!">"~+_>-+iiIi>iI
                                  l~;;!">I^",lI;,:";!I"~l`,lIlI;I:i:,!!l;iIl:I^"Il;,:II^:";;:^;:":.
                                  :i;;!";l"";;Il`::";l'l!^;>!!;"I^i;"!!!;>!;^>":!!!<";i^ll;il`l!>!'
                                  !;li,?<^I~i>;;!:+~<~~!<i.!,ii<<<"~i_;->,:~_i!~i!;_!i!!^>l<l^li"I!l~>!,_+~"
                                  `^^:`";"::","""^":;,II:,`^^";:;,^^,!^,:""I,;;I;"";,,::^::;I`,;^;;"::"'";;^
                                  ;_l>!,_>~~;!_!<+I<~iI+?_?->_>I<;-+>I!~l>~<."~!i<<Ii<I;il!I_>+;'~iI>~<?_>_~
                                  ~[-il!IIi-><+~<i:]~l>+--I!-<-~<~I<~<~;!_>l_>"i_+<i<:]+>-_!,__<!:~~+]~^'''.
                                  '^"^''``^``"^"^:'^"^:,l;`^I",,,,'^,;:`":^`:,`:;:"^,`;;I;l;^;";""Il>;;.
                                           `...      . .                                        .
                                         .I;rfjt\r\ttxntuvvnnnnnnnvu/|\||txxnnnuunxxxxxxxnnrfjjfI;.
                                         ^I (({11\1)1\/)ffjxxxxxxrrr/111)tnxxrrrjjrxxxxxnnnnunxx.;,
                                        '^,'YYQmZOmmmOOZ0QQQQQ000000OO0QQQQ0OOO0LQQQQQCrrjtXjJLJ`",
                        :iI:i!!!>;;i!>l':', ii|[`''`^^^^^^^^^,::::::::::::::;;;;;;IIIII:::;l;l!! :"
                        l<+_-!>i]+_-_],",':    :^^"`^.^`^`^"`                                    l:
                        i~+:. ...`'``' ',', """^">_<il>~~i>_>^```''''''''''.....          ..     l:
                        ""`'..'. ... ..'""`,dQY0QczzCzUqwwwwwpddqwmmwwwpppppddppqqqqwwqqqZYcCqOC';:
                        >+ii?i+>"~l<;i.^::`"-+l'''''`'`^^^^^^`,l+>[]_-<",,,,::::::::;;::::::;lI>':"
                        <<+_~<li'.       ^^,"                ^' ''`","`                        "`"^
                        !<~+><i;~>"    '^,^lZCQLUCwwmZZZZZZZqhwZ000|    `><;i!'                ,'"`
                                       ' ;:"|\)]([l!l!!!!!!!!!i>>>>;    ,{1i-?^                ^.:`
                        ""'`"`^^'.`    ^'::"-[~i-l                      "])<?_^                ^ ;`
                        >-~+-_+~_ll    ;`,^,}{~~->                      :[]!]?^                ".;`
                       .l!!i!!:"ll`    "`,^;[<;<~i                      :]il--^                ".;`
                                       ^.:""?<l~_!                      ;?>l-_^                :.i^
                                       "`:`,{_i_[>                      ;]_>[?`                :.>^
                                       ..:``l;"l!I^^^^^^^''.`^^^^^^^''`'^lll<i"^^'''`^^^^^^^^^^, !`
                                         :^ :'`'''````````````^^`^^`````'..'..'''``''''''''''''' l'
                                         :, ''.''.:'..'.::'''''>''''';;'''''I`^^^^,^'``'`:'''''. !'
                                         .I:^'''''"'````:"'''..;''''':,''''',;?<[~^`!-?+":...''`::
                                           '`'...'.'`'^`'. . ..''...'...`.'''''`^`^^^``^^`^^^""^'
                                              ;l;.;,^l."l,I;l::`lII:,I,;'l,,::,
                                              ,:_^l:^i`,l;<i<!>,!<<<!>!>^>il<+!.































```

*Figure from page 16 (2346x3317 px)*


---



4203-E P-293



SECTION 2 PROGRAM OPERATION



15-4-3. Cursor and Page Operations



(1) Moving the Cursor to the Right



Each time the "right" cursor key is pressed, the cursor moves to the file name which is adjacent and



to the right, or below and to the left, with respect to the current cursor position. If the cursor is located



at the final file name in the directory, it moves to the first file name in the directory.



(2) Moving the Cursor to the Left



Each time the "left' cursor key is pressed, the cursor moves to the file name which is adjacent and to



the left, or above and to the right, with respect to the current cursor position. If the cursor is located



at the first file name in the directory, it moves to the final file name in the directory.



(3) Moving the Cursor Downward



Each time the "down" cursor key is pressed, the cursor moves to the file name directly below the



current position. If the cursor is located at the final file name in the directory, it moves to the first file



name in the directory.



{4) Moving the Cursor Upward



Each time the "up" cursor key is pressed, the cursor moves to the file name directly above the



current position. If the cursor is located at the first file name in the directory, it moves to the final file



name in the directory.



{5) Changing Pages



Up to 18 file names cam be displayed on the directory selection screen. If there are more than 18



files registered in the drrectory, other pages can be displayed by pressing the page up/down keys.



l?SMM ifEiWfq.



lcrer



co Pf«P,1,11.VtN,I



jl(JEXCCICl"'TliJIII



,oo;



POJ2.:IIIN



POOl.lflN ?OOUIIM



FOl5.WlN ?O)E.Yll!I



PC01.IIUN PCCS.lllk



?X19.¥1N POlitMIN



ron.vm ~12.1111"



Ft]ll.iUH Ptn 1 umi1



POl5.tWt POli.V!ff



P0l7.fillN P018,lillM



co PACGWLli!ft,I



CURSOR



POZl.l,lfN



PC2J.lllltl P0:2"1, W!N



P025:.lllfl ?026, U!N



P027.Mll'I ?Q2fl.WIS.



PC29.MIN



Fig. 2-15 Cursor and Page Operations



OVFR!f!f!'1::


```text


                                                                                               .""^^': ,^`""`
                                                                          ....''... . ''.....  ^]???i?.~l~[?!
                                                                          <1_<<_~+?l<.__[_-??-]{li___~]_~~~};
           .```^^^``^^^^^`^^^`'````'````^``'''''''''''''''...''''..........'''..''''''..'`'`.''`'`'.''''.'``'
           .^^"","::,"""","""""^^`^^^^",",,^^,;;;;;;;;;;;;,,,;;;;::;;;:::::,;::;IIIIIIII;;::::I;IIIIII;,:;,;"
           .ii"!Il `>lli!^;iil><>>I;~!!I>i;I!.
            ,:^:,:  "I;:,.";:"'"i<"`;;;:I;,"l
                  `I,  l!::::^!;^^I"::,`;`;;^:<;Il'
                  "lI  liII;~lIlI^I!I!l'>,IiI"i_>i'
                      .!::l^I;;,I!;';;Il`,,,:;'"I""I,;;I;;l,">;^:,,;:^::::I,;,lI:;>;^:;,I":l;;:",^:lI",:;":,;
                      .~!+<:>i_~;><:i]>>"<<>_~l<__!]!>~]<~~iI~<!<i<~i:lii>_!!i>><I~<;__l+I-+~~lli!+]]<<<<>~>~
                       >;><!;]-!,>:i~!l~;_!i>l!~>l~+^!_]II<-_<!><l<ii!>l!_!Iil!<!I<i<_<>^ ~;l>:<>>~!,~l~<?~~>
                       ]i~?~l~>]l[]:<-<<iIlI~~"-_~<_<+,Il!>i<_iI~;-~I+i]I-_:!_<_~l<;_+:_?<>~>~l
                       .   .   .  .  . .     ' ..''`'^`...''``'.^.'^'''^.'^''^``^.'.'"'^^`^^^""
                  I]> .][>~>+l-~!!+i<~i:_:+_>Il]~
                  `"`  ,"^"`I"'^"'^:`,,.^.`^^`^^`
                      .+i<~:<~~li~!"+_i"l!><I;~<:>i+l<<+<<^+>ll!>>>I:>!l<iili_>l_>,!<i<l<~i>>:il~~<!~>l!~i<i:
                      .~~l!<+'i:!+iI>I!I>l>l+!I!<_+,i_?;>>!!~<>_I_~l:li!<>!lliil:iIi-~<l^i<<i;!i~+~!<!l><~<>i
                       <~~~<<l<I+-!!>!~i!I!>>i;!]<>"<il;l<<><>;+:<~il_ii<~!I<i>>:<i~+<ii^;li>!:il!!,;I:lIii!;
                       ~;i+i;i>i;~l^<<l_^;"~<l;+!<><!~'i,i>!i~:<:i<>:+<?:_+,l+i<>;l;<+,_-~~+~_!
                  ."'  ^`  .  `. .' .   ^ .     .                                             .
                  ![> ']?<<<]l--!I<<~_~:_<__<-___,
                      .:``^.,"`'",^'^"`^^^'''^``'^^.^`.^````^`.,`.'.`''.'''''''`."'.^^'.''''.'`'.`' '.'...`'.
                      '+<_>:<i~>!__`l_+]<`;><><i;+]ll!!~+~~__l,__:i~<_~`Iii<-~:~:+~!l?i"_]i+:<+<<_-,~_~i_;++l
                      .lili~il<><~i+^ i!><;ii~~>:+!+>~[~!I-i+_;+i]i++I!_~<<iI<_<I-i~>~i+"~l~~><_l<l-+<<+_>_-;
                      .<_<><l<!~~:-_<i+i<I.'''`' `.''`'`.'`..`.''^..`''^''`''''^'^'^`^`,`''`^^^"`^'`^"'^"``"`
                       `,^^"'^ ',.,""",::^
                  :~; '+!:I;I"~;"II,;I:^;;ll!ll
                  :i; .!I:;:<"l;:":II!;^lIIl!I;
                      `iI!I.;!l;"<!'^II`^;;;;"^><,"!`!Ill!;! <i;'III;I.:::I!:"!'>l,,<I'll:;,^i:II>^'i:,::^!I^
                      '<>~>Ii!<>l-~l`>-:>~i<<iI~~>I~l-_~~<~+l<<_;++-<i:!i>i_!i+,<_i;+<,i~>>!;<i~<-i!->+<<;_-;
                      '>i;><!i+<>~><"'!li>,!!i>l`>;!!<_>II~I<>,<ii:~i,_~l~:i,~>l!<<~i<<i^!;!!!<!liI_>;~l-!>_:
                      `>+i~!lll++"_+__-~~;
                   .   ..       `       ..
                  >}! ^~+__+]<-l+_]?-;
                  '..  `'`^^:^;:.';,^'..  .... .' ..   . . '  .'  .        .          ...
                      `>~,_""_l?+,I-<<-i;?-ll_!;?+~-+<+i;~"~~iI_<+<+i!,+>~i?<!"~>>~+l :>_~+>ll_~:><I<,~>_",]I
                      ']+~:<+-+_~>~>>I~+!:?!~~+<~"!-__Il+~++ll+~:~~;~+~-_~~<!+Ii~~~+~>i!+<!<<<+,i>~~><!l_i!i'
                       ^""'^;I"""^"`^'`^^'"^:",,I`",^;`:;!!;"^;:`:;`::!;ll;:^l::,:;;:;i^:;,IIiI`ll:;:I,`:Il:.

                                           +]]]]]]]]]?-??]]-_______+_~___++++++<.   ^<v~`
                                         "m/~~~~~~~+_+++_----------_-__-?????]])Q< ,i-+l'
                         .       ...''''.iL                                     nn `:;.      .
                       ';>?[_-[_]>!!ll!l!__?iIlll!ll!lI::I!l^ "l_-?~__++lllIIlI<]?_ll:IlIII::;;;Il"
                       :,~\}-+_~_!lII;II!+_~l:,:;;lll_]-<!!^" !^[1-i~+~+lll!lll>?__!l!lll!!i+_~>!;I'
                       ;,>-__+!+~`^''...''.'```````^`;i!;"^`, l`]-__~<?I"""""""^^^^,""""",";<+iI,^;'
                       ,"                                  `I i                                   I'
                       ;:-/~][_?lI;;:;lll!l;;:I;I:::;;!?<;>,; >^){<_+_+II;:;IlII;:::::;::;;I;i?;l,;'
                       lI,^      ...":l!><"          .  . ,;; <^;`         `:Il>>'    .......''..^I'
                       I;jvnvxnnnnnvXurj!  "?!~^          ":" i!jt|/rrjrrjnvrrf`  ;i;I           ^:'
                       :,}t1|'...... ..'.  ;j]|;          ""' I!r1\+,,",,""^",,   -t?[           ^:.
                       :^_}-]              ;)-):          ",` I;{~];              :i;I           ^!'
                       ""}-?-              l}<1,          '," ;,'.                               `l'
                       '"{]?-'''''```''''''l{_{l``'''''''':," ^I`.  .'.'''''''''. .''''''.''''..'^I.
                       ^."`^^,""""",,,,,":,",""``^^''`""""^^: ^':^^^^""""""""""""``""^^^""^^"""",';.
                       ,,''.'i``','``I^'`"^`'"li<l,!>":```';: l'^``",``^:```:``'^``';ll!;IlI":```'l.
                        ^"^"^"^^^"^^`:,:^1_`^^:!i;^!>;""^"""  `,"""",""",""""`^`+:^^"l>_l:<<:"^^^"^
                                    "?r{.XC.                                   ;Ml
                                  ',i+|! `/ft//ffffffffff/\\\\//\\\/t//tt//t/\\n[
                                    `^      ...''''''''''''''`^^^``^""^^""""""^
                                              '
                                             .++-'_,~_'~<~~+<,_>_i++?-:_?_~~1_><l
                                               ." .  . .''.'. '.'  ',` .^`'```'''



















```

*Figure from page 17 (2346x3317 px)*


---



4203-E P-294



SECTION 2 PROGRAM OPERATION



15-4-4. Function Key [F6] (RETURN), [F7] (CANCEL) and Cancel Key



When function key [F6] (RETURN} key is pressed, the command creation screen is displayed and the



device name only is entered at the position of the edit pointer. The file name that was at the cursor position



is not entered.



When function key [F7] (CANCEL) or the Cancel key is pressed, the command creation screen is



displayed and neither the device name nor the file name at the cursor position are entered on it.



Directory selection screen Command creation screen



ESiW1 esa'/'1~ 3iHSS



l~~SFl!lt ~~



Im ..Jlll!lll'l'!l:J



L··•-!



OVEf!Rli=



a,~.lllll.!



-- 'EDIT POINTER



',. ... 1:,..,..1(1,1



--- ....



FOO:



INCO OlsPU't ~



(1=2) - > II01 ;•.kl""



(Fl)



F!X):•.•i,



POOf.lllUI P'001:~lillll' to OISJ>IJY On,e! 1H:EXSS.AFT':R ~ING [Fil.



I P003.UfM P0)4.IU1' 1111"1,JT TI-'£ teVIC£ fWE A/"J Fl:.! ""11;. n-EH mss ~rrt] lit$.



j PCXIS,IUN PC()S.11:!ft /CURSOR



WMl'l.T !k'"VICE H:iA.WE-.. 11)1;



XXlJ,.fN POll.liUI



f'IC(5,Mlli POIO.Mll'J



Ol:FAULT i:'t:.£ iWIE '= •,IUN



?Qlt,Mlli



l"Otl.MIN: P014.¥1li



F(H5.111r. POUUII.N



?0!7.llt/C F"018,UIH



I I


# I I 1-1~.1

'""'


# I "11,.;,,.I ~~!:l~lo:rn!

CAIIC<l.



)BJ



CAN



/,~~l:12!



[':~·•"·FOO'\_ ED!T POINTER



~Ir-::



I folOEX OISP\J,'f ~



(F2l



u;n:•,111N



lFJ) - > P.:X):'+.lltH



TO OiSPu.'f ~ IQXES.AFTER PRESS1NC !}=1].



Ir.PU; "tHE OE\!lcE NMIE" N:o ;;ltE !WE. MK~ tifl:J1'l€ X!I'.



OEFM.U Dell CE MIE - CJl:


#### Of;FMJLTFl1• .EM1411e'-. •,f!N

\., ,,.,;;111;~1 ~EXl=lo::l"of=I ~LI



tm9W! Of"E6lt [Oft EW§ft.B



r~·.,._o:,iF1>t1.Nt•\_E:~~~!NTER_ _



_-I



-----··--·------~--



1ta'X DISPu.Y Pia:~



£F2) -;. 1iD1: 11 .1tlH



[f3] - > Fll);•.tl!N



TO OlsP!..AY On-ii;! 1u:<es, ...-. rm PRIS$!Mt f.C:11.



ltlvl lk!;-CEVIC:f HiolE U/0 File HME.lli£H ~SS )IR!~) K::Y.



DEFMIL.T DEVla ~ - il)1:



Df1='AILT FIU'. ~ • •.fttH



'""'



110,·



I roo·



f""""" I"""'"/ I,_ I I

• 1!0:x I il<e riiSTCRf. IHSefi •



oa.:.-re



CAN:el;L



Fig. 2-16 Function Key [F6] (RETURN) and Cancel Key


```text


                                                                                              .,,,^^, :'^,^.
                                                                         ''''''.'... '`.......;]-]-~_.~I_]?,
                                                                         -}_>i~>_-!!^-]]~?__-[]:>++_--~<_>]:
          .^^^^^^^^^``````^^^^^^^^```````^^^``^````'''''``''''```''''''''''.'..''''''. ''''''``'`'.`'''''''.
          ',","",:,"^^^^^",""",""^,"^^"^""""::":,:"^^^^^""""`",::","`^"^`^,::;;;;;;;::::;::;;;;I;IIIII;;:,;`
          .i>:lI, ;~lll<!l:+>!:_<-"<_-!l>-_~^"-;i^<l~~>!_l,">;l;!!II!:!>!"
           ":^""^ '`:,:::"',;l":">,,:l`^;;II"^I`:`;::::":""^!:;^:!:;l^"Ii,
                !-<il.i;;!_!;`<<,;+~<._]+I;!+__^!iI.l^!IlIl!l !i;.I;l!;!;I";i>><ll.il!l!;"!'+i!!>l!i^ill,i!"
                I_!<>Il<<<~lii_<<i<<?i~~>!i~i!<l<-?Iil?__<>~?ll>~l_~;!__i+<!!~+<>i!+~i~~!;~;-~<l~_<<,~i<>i<,
                !+i!>i;<_!<;!l~:!;>!~!i>;~IliI!i<<ii:;l!!iI>+iii>l~<.'!!lI_I,>iI>I<>iI<~>!<I!<,lli>Ili!<_>l^
                i;"<>:~!<ii+,
                ,;,^"."^^^:^^.,^`.,I;".:"::":l"`.``',^.^"```^`'``.'` '`''``` `"'..'`''`''`..'''`'' .....' '
                i?i?+'l+<~_>>'>~?`iii!^_!++i<?<!'iI`~_:;<->i?l"_-l`~^->+~+_+'l+~`I<>>!<_>_`!<~-]~<'<<<--~`-;
                >?_~--~_i>+~i>__+_<:-+;i_!i~<^~]~+I!~li?<I?~"i_~_!i?l]<;i<i<<">i~?_<I:_>,>!_+i~>I+;~^
                ''`''^'. .... '. '.  ..'`''^`.`^.`''^'.``.'`..^.'''^ '`.`^'^`."^"^^^'`"^'"`^"^"^`"'`.
                      ',"^^''"^``.`^"'                       `'`'''.''''  ..
                      ^l+++<~-+><l~<-<^^^`'`^^^""````^^^"``  :><i<>l>_+<!~<~I'`..''`''``````'''''.
                       ^l}[}-[][-i!l;ll!_){?llI;Il!il;;IIll, ':>]]+_-~?!I;;;lli[1]>llllIll!llIIll;^
                      .;:t(--_+_!llllll;li>!IIIl!!l:i]}_<i;, l;?t]+<++_II;;;;IIi>ii!I;;:;I;_]]~!;^:
                       ;'lIl!I:l.            .  .   .``.'..; ::!!>i!Il-^^'`'`'''...'.....'."::^'`":
                       ,.""^"",^`^^^^^^`'''``'''....''^,'`.; ,:^      .^~<i!~_~+_:...'......  ..^",
                       ^If1i+><!":,,:::::,,:""""^^^^",>_,;;: ,`"]>!~_l_--~'''''`^``````````````^^'`
                       ^,'                               .:" :`.?l,;]_i]"                        '`
                       '!|?|l              {{]<...  ..'..`:^ :',<>+i>[i~[+i<+~1_]i+;^:^`"'       '^
                       'if}\!              }1?l     ":!l;I": :';(]i_]_])<i}!,"I`;^:;^;"^,`       `"
                       'i|_\l             ,YYcnffrzr/t/t/f>` I`^l!"^:;~,' :!.                    ^,
                      .`!)-\I             `ftf|___+______?!` I`                                  `"
                      .,;->?;`^^``^^""^^^`^<~-!       '. .^, ;'                                  ^"
                      .".^`'""''^^'^,;"^":^``^'`^,"^^,,""" , I'^'.`""' '`' `""'`,^^^"``'^'.'^```.":
                       :^^^^I,''::``"l`'`:^`^:<~~"!-i:"''`"" ":^i+,;-|<lI|+l[ft!l1f<<(?!l>-lI"^``;^
                        ````^"",^'.`,^^"<c '`'^^^.'^^''..''   '`",`'`l;^':l"^""||:I"`:;:^;iI^,,""`
                            "lI;":i,li~,?W>^``````''''''''''''... ...   .     `dx
                           .l++;"`"`,;l^_a/tttttt\\\\tt\\\\\/ttttt/tfjttttftffj1
                           ^`lI.        _w                    '^'''''''^^^^^`"' '````````^^`^"^``.
                             .          _p                   ,l[1{-][[]Illl!!l~11{>llllli>>illllII^
                                        ?O                   ,^11?-_~~~~!IIIIIli!l;;;;iilI![{?>l:",
                                        ]0                   :"l:llll:I<<``''`'''`'    ....`^`'.^:"
                                        }O .                 :^.        'l<l;i<~<+~'.'''''''..''`:"
                                    ^''.{0                   ;.I[I!+~!?_~:    ..  .'.'```````''`':"
                                   ^l+<`}a<::,,"""""""""""","; ;];lI{>~]`                        :"
                                   :!~?^{w1\\\|())))(||||||jt" l<<_l--I{?-i<>]{__<-:"I;":'       :,
                                   .';` |J                   , ~{+!]-_1]:<?;'^"."`"^^"^`".       ;"
                                        \L .                 I "::'^':;'. ",                     :^
                                      . \Y .                 ,                                   :^
                                      . \Y .                 ^                                   :^
                                      . \Y .                 I ^^`'^;`'";;`;!i!;IlI";;"":``^:^^^'l"
                                      . /Y .                 ,,^--,;_}~:!)~>}|(i!()l<1~iI_?Il^`^"I.
                                      . rY .                  '`'... ''`'`"^`''...'`''^``,:"^^^^`
                                      . xY .                 ^;<_+i<<<<;I;;Il;!__+lIIII;;;I:;;;;:"
                                      . rY .                 ;"[[_~<~i!:::;::;I<<>lI;IlIIIi_-~!;";`
                                        xz .                 ,;~>~+iil!l!I~]'      ...''`^"l!;^`":'
                                   `^'`.vu .                 ":            ^:>iI!~>ii-"         ^".
                                   l!?<^cx .                .;'i+;!!:;ii<:`'^""``""^`"^''`^^``^^':'
                                 ."I+f-`xC                   ! <?^I>[l?_'                        l'
                                 .."<!!:`xx/\\\\/\//\|||\\\x); ii!>,+~:]>!l>I_<>lI:.'''.'        ;'
                                   .      .^^^^^"^"""""",,,;," -[>~_-~?{![<l;+i!i;>,II::l        :.
                                                             : <+<">l~_:.">,                     ;.
                                                            .:                                   :.
                                                             ^                                   ,
                                                            .^.' .``. '`' .'...'.  .  .''  ''''' ;
                                                            .;'"<l;!]+l:?[;!)/{!-|[;_{ilIii:;^^^`;
                                                              ``;"  ";^'^l^.",:^"!I^,I;",ii:^'^^^.
                                     ,I^."``;'",^^^,`^`:^''l::.::,:"`":" .'^'`.'. ''^.
                                     l>{,i;,-"Il~<<_>>;++~l_<{;+-+li<+-_,->_li++i_+I-?-.


















```

*Figure from page 18 (2346x3317 px)*


---



4203-E P-295



SECTION 2 PROGRAM OPERATION



15-4-5. Effects of the Editing Modes



(1) Overwrite Mode



In the overwrite mode, the positions of characters in the character string are fixed and the file name



selected from the directory is written over the part of the character string that starts at the position of



the edit pointer.



(2) Insert Mode



In the insert mode, the part of the character string that starts at the position of the edit cursor shifts to



the right as the file name selected from the directory is inserted to the left of the edit pointer.



If the command length is caused to exceed 255 characters by adding the file name, the 256th and



subsequent characters are deleted.



Directory selection screen



IA'f'<



CO~WHt:t



'\. EDIT l'OINTER



IICEX SEl.ECTIOk



"'°'



P001.IUH



f'OOJ.Ht



!'005.MIN:



PC07.Mltl



?:m . .lll:Oj



PO!t.lll



P01l.lfl:II



P01$,lllti1



POl'.l'.11111'1



Directory selection screen



[Pf01WI ?'§Y;Tl<Ji



o:)~illN;



'\.EDIT POINTER



11()(€ S l<tf



RX);



f'COl.VlN



f'COJ.jilll



POOS.¥111



1'iXl~.1m1



P009.IUII



P01LIIIN



?013.llltf



P015,IIIIN



A:,17,Vlli



/MIE:lIF



OVERWRITE MODE



P0:12.llt ..



?OOC . .lffH



"""1



=::::



/CURSOR



POll'J.IIUt



IWBI



INSERT MODE



POOZ.IIIN'



P(X)¢,IIH



~:::: /CURSOR



P()l(),lilllf



P0'14,li11N



P01G.ltllf



?018.IUH



Command creation screen



l!Gc): DI SlU.Y ~



{F2] -> ll)t:•.llinl



(FJ] -::> ,W:•.•11t



TO 01$1\.A'I' 0~ l,aJCES.AFTER flf£SSUC; [Fl).



!IPJT lHE OE\IICE it.VE Ne Fil.I NAME.MN Pf£SS DIJRltt] K'€!.



,OOFJUl...i CEVICE 1NE • IOI:



tEFillll.T FH..E ~ .., •.MIN



Command creation screen



H()EX D1$P<..,A,Y ~



l.e'2J -> IDJ:<".ltlll



(Fl)-> FO():"',ll!ll'J



1~ C>ISPU't G'l'HER ltcE'(ES.~ PFESSU<I (Fl],



lrf'U'f rt!E.



0£V!C'£



!WE .I.IC) Flt.£ K411e. n£H ~SS



(WR11tl U"'I'.



OCF.Q.T DEVICE IWIIE "" IQi:



OZFAIJI.> FILE fWE'. - ".lillf



Fig. 2-17 Effects of the Editing Modes



!l§ffiT


```text


                                                                                               '^`^'^'.,.`^`
                                                                           . ..       .        <?_?>?l^_;-{].
                                                                         ^1[+<<++[;+"i-]-_?}??}-:+~_~_?+<~-?'
           '`''.''''''''''''''''''''''''.'''..............................`'''.''''`...'````''``'`.'`'`''```
           ",,^^^:;^^`",,:,:,,,,,,,:,:"""",";IIIIIIIIIII;::;IIIIIIIIIIIII;:,,;::;IIIIIIIIII;::::I::;;;;;I;;;.
           ^>:I:>  i<+lI!`lIii;l!ii:l"<i:!l;
           `l,;:l' :;i!:l`;^;l:;Ill,~I!il>>!.
                  ,,  .I^:""":"`l,^:.
                  l>" ^l!~iii><"+<i~I
                      ^:^;,'"",:",l^^;,Ii',!;^;:Ii:::^::"I::;;;::",^!:"";,,:,I:`;I,:"^:":;,,,":,,;:"Il^^:,",.
                      ,ii~<i><?<+>+_l!<+-Il<~I+>+__<<!!;!>_+~+<~+!>l-~l!<<i~<_~,__l~_~~>!~<~<i~>~<~i!_i!+~i-^
                      "_+_l~_il!i!:+_;+~<~~><!<I~<_]_I!<+<I+~I<_+l+<<_I_<+~_~?i:-i>+>]<[l_-~?l_!-~!>~<~-i>:-"
                      l_~;+_[!_+~~_l                         .                     '.     .   .   .'..  . ..
                        . .'..`. '^'
                  <?" :>i_~I_?i+~.
                  :;' '^,;"'""^::
                      ,l;-i:Ii<l:!!!-<^[>Ii~+ll!<ilI~ii>>~~"~~ii!~>~l>+!>li<~<lli!<-lI"<><<;><+"!!i!I:<<[>i~'
                      ;_<l~~-<>_;+<!_-l!~~<_li~+<+~>i_i+i>-ll~>+_~<+;~ii>~~+><>+!-~>>~~l<<->!<<+i>>+>>>;:;,I.
                      ^;l'"_l",>^:I"";,';l:I^IlilI!I`::I^^:l`;:l;!ll^;"^:!l:!I^l';l:"il`!"l!";l~^lll:<,
                      :;!i:`;I:,:l,I"l;;~l^I`;l"lII,I`I;;!!l:>>!^!;!IIl!;,,l';ll!;,:i:^~I`";;;; !;",>!<>^!;!`
                      :I~+>!<i><><~<l+<][<;<!~>+--+i+;llI!il"llI,lI>I!IiII,<:!i!ll+;!i,!>";<l!<`l!l;>>~i,<l>'
                      ,><i>~il<!!:i>~<~i~<ll<>`~++~_~,

                       .^'''.'`''..'''                      '..     ..
                       'i~~_!<++~!<+~<^'...'`^``'`^^""^^`'  !>~+<lI~-~!<~_;'.  .`'''```````.''
                        ^l-?]-[+?lI;;;ll-}[+I!!;;;I;;::ll!; 'I-]-<[__>II;;Il~{[-!lIIIlllIlll!!:
                        :,t|]??+~;;;:I;;!+<i!:;::;;!]}->IIl.`")1+~++-ilI;;:;l<>iI;I;IIIl-{[-l,,'
                        ;'l]~<ii;`^^^`.. . .^l!!ill_i+i!;.! ,:<lll;!?!``'`^`''`......'''","^'^I'
                        ;`;;!}]+i+_~?>^^^`^^"l!!illI:>+il`I ;:'.'..''"i<Il+-~~+^''''''''...''":'
                        :lt]i<i<:"^^^:;::::,"^^"""",,;_I;<; I'<)!<]-_{->'.....''````````````'','
                        ;:,.'              ^^^`          l; I.l-:Ii1l1!. '.''' .              I'
                        ,>f](:             )|(]    ^",",`I; I'i_<-i?<_([_<~{}]_~-,!;"I"       I'
                        ,>t[{"             )|1+..:,!i>>>,I; ; <1_!?<{1l:[l... '.'.''.'.       I'
                        ,>1_|^            ^JXYcrrvjfttftr-l l''``...,.  .^                    I'
                        ,i{?/,.'..'''. ....)1)~''.''''''^Il l'                                ;'
                        ;`l:I:",",:::"^"",";ll"`^"^`"""""'l l'` ...  ..  .   .   .   .   .... ;.
                        l``'.;^^^:^^`;^``,^``:!>!;!<:!^``'l I^"i!,!]!;l]!!})1l_(]I??I!;!:;^^^`I.
                        ."^^^"""":::;l::!f^,"^IlI^li:"``^"   ^^il^^i<:,~+;><<[<_<,l<!"l~l"^^^"`
                                    :![!;k_``'...`..''```''``''  ..  ..  .  ;*>
                                  .,!{j~';\|\\\\\|\\\\\\\\\\\\||////////////f~
                                    ^<>i^
                       .`'.'.''''...'                      .'.'....... ...
                       ^>+~~i+~_+>~+->``''''``````````^`^' '!ii!<i!_<ii+++:'. ..''''''''''''''
                        :l]?--]~?l;;II!i][}+ll!!i!lIIl!!i!: "I-[[_[__!lIIIll_1}_I;IlllllI;ll!l:
                        Ilf(-_+<!II;IIlI!!!lll;;I;Il-]!l!:! ;"|}-_+~?~+~i!;l!<>il!!!!!!!?[~i!:;'
                        I';-iilI"^^^^'       '!!i!:-><,   ! :,l:;;;:-+~<>l^^^`` ........`^''.,;.
                       .l`!;>}?+~___-!,,""""^"lllI:lI>~""`! ;^''''...'~+ll+_+_+^^^^^^^^^````^";.
                       .;>\<!<!>,"""",:::,:""^```^""";+;IIl : ~{;~-<+[~;       ...''''......' i'
                       .l,^ ^              "^"'          "l , ~+:;>{!]:'.^'^^`.'              >.
                       .;!\]|'            .\1|l    `'"""":l ^ <?+->]i]}]-_>{]}<~~"il,l`       !.
                       .^!\]('            '|)\i'`:;!!<<~>Il ^ +1iI-~{[::?l    . '.'..'        ;.
                       .`>}_('            !Ycznrruxffffjn~; , ''' .." . '^                    ;.
                       ."<1])'......... ..`{-}I .  .....^l; I                                 ;
                       ';,I;I,,,,""""``^,:,;:;"^",^^","",`; ; '  ..  ..  .   .   .   .  ..... "
                       .I`^`'l^`^!^^`;'`':^`^;iil:i<;I^^^^; ;^">l:>[i;![!I{\}:]\?![]l!li:i^^^`:
                        '^"^^"^^^"^^;l;:_t.``^;I:"!>:^^```   ^^lI"^!l"^>i"lii1i~!"!<l,!<;"^^""'
                                    !>)l_k!^``'''`'.'````````'' .'' .''  .. ~*"
                                  ."!{t<.!\|\\\\\\\\\\\\\\||\\\\\\\\\\\\\\/\tI
                                    ,!;l`

                                             .I"' ,'"".;;:^,".^^,^':",:`'':"`,^`
                                             'i<_`+,!;'->+~+-,<:<_l<<-_i[l?+<]_~




















```

*Figure from page 19 (2346x3317 px)*


---



4203-E P-296



SECTION 2 PROGRAM OPERATION



15-4-6. Directory Display Method



(1) To Display NC Memory "MD1:" Directory



Press function key [F2] (MD1: INDEX).



The input examples given below show how to designate which file directory is to be displayed.



[F2]


#### MD1: *.MIN

When function key [F2] (MD1: INDEX) is pressed, the directory {in NC memory) for MD1: related



files with extend names of "MIN" {work programs) will be displayed.



[F2]



MD1: *.SDF



When function key [F2] (MD1: INDEX) is pressed, the directory (in NC memory) for MD1: related



files with extend names of "SDF" (schedule programs) will be displayed.



[F2]


#### MD1: *·*

When function key [F2] (MD1: INDEX) is pressed, the directory (in NC memory) for all MD1:



related files will be displayed.



{2) To Display Floppy Disk "FOO:" Directory



Press function key [F3] (FOO: INDEX).



The input examples given below show how to designate which file directory is to be displayed.



[F3]


#### FOO: *.MIN

When function key [F3] (FOO: INDEX) is pressed, the directory (in floppy disk) for FDO: related files



with extend names of "MIN" (work programs) will be displayed.



[F3] ---;,fOO: *.SDF



When function key [F3] (FOO: INDEX) is pressed, the directory (in floppy disk) for FOO: related files



with extend names of "SDF" (schedule programs) will be displayed.



[F3] _.. FDO:



*·*



When function key [F3] (FDO: INDEX) is pressed, the directory (in floppy disk) for all FOO: related



files will be displayed.



(3) To Display Other Directories



When function key [F1] (INDEX) is pressed, "ISO" will be displayed at the console line. Following



the "ISO" character string, enter the desired device name and file name, then press the {WRITE]



key. The following examples apply when an OSP formatted floppy disk is being used.



>ISO MD1: {WRITE]



The directory for the default file name at the MD1: device will be displayed.



The default file name is indicated at the directory display procedure.



>ISO FOO: [WRITE]



The directory corresponding to device "FOO:" is displayed.


```text


                                                                                               ^^"^'".`^'"^`
                                                                         ....''..    .'.   .  .?}-?!]^lii[[<
                                                                         I{]~<~<+]l_'<~[~+??--[ll-<-___<<<_<
           ^^^^``''``^^^^^^````'``'`^^```'''''''''''''''..'''''..'........''''.''.'`...'''`''''.'`.``'''.`''
           "","^`""^^"""""",^^^```^""",,"",,""""""":;;;:",:;;;;:;;:::::,::;I;II;:::,,,;III;II:,,,,:;IIII;,:"
           ;+:!I~ ._lI!!!l;:~>!iil,+>>!I!^
           ^;^,"I  :":;":,:'":I;;I';::":I.
                 ';:  "!`llI;l:';l:"iI:,":^"><!:^^Il::;:,"
                 `;I' 'l^:I<>!<",i,,>>!:lI; !>l,^ I!l!!!!<.
                      i!llI^lI:!>:;,I;`<i>;;~iII'li!i!lI
                      "^,;l`"I,;I,"^Il"!";,^i!"^ ^;I;;;I.
                      ,<<I"ii;l;Ii!!>i!,:<;>,^!ii!:"l;;l^ll!,i`!<!i!I>+;,>!I>"~~,l!II!lI":;l;:i:">lliI;II
                      ""I;^!>i;llillilI,!il>II<>l!I;!l!!,!!i:i,!>i>_l<i:"l;II`;>,;;Illll;:I;l,i;:iiii<>!l.
                     ':!_i~',,_-~i^.l,i_<>' .`... ..... `'..'.'. . ..:^
                     .:<!i+^l:~<!l^.!"l<!i'''....'.   ..'''' .  . .' I^
                      .I_>!~:<I!i>l!,ii"i<~l>[[<!`<-__+_i!i;i!iiiiI;_!^!ll;lII^;I,>i::ll;I;;;,l";+i;,`;lll;l
                       !-!i!l+>;<<<il~<>~l~!;_~>~l<<!<>i>:!iii<<~~!,<~I~ii~<<_l!<!>l":!i;!!i!"i::+!:,^i<~<>i
                       I<il:+~i,>i+><l"_>i~>,~":?<~^"+>i<:<!<]i+!+<"<<;i+^~~_+_+~_"
                     'I:l;:","";II,"'":^I:;:"^"`.''^^''`^,,^`^````^^`I'
                     ^;~+~~'l".>1]iI.;<:]~-;     .         ..        ;"
                      ^IiiII:lII;!:::;;";!I:I<~!I^l!l!!!;llI!I;;;I:;l;'^^`'^''.```""`''.''...''.'"^'. .'''.'
                       !-~~>:!>i>~>i;__;i!~i!?[<i`~[~+<~lli!>><>~<;:+>,_l++_>~;i>I_~:I_->+<_<;_:>1?i;^~][]_+
                       li~l;-?!:_~?~~;l_<><>"~^I?+_:'~<<+>+<-:<!i_<~!<~"_+!<~,-+>_~~+-:
                     .:"lI;,""",:,,,",:;;;:,",^^,,"^:ll;,::::,;,;>I!:;".^'.'`.``"`^,^^'
                     "i~--~`;:{]~>^'_:I~.          ..             .. :`
                     ';l;l;,Illl;:"";:,:",::::::,"^""""";::,^`^````^"l'
                       !?_<<`>!!<<ii"_>~`]!]^l]?i>'I[]??_?'_;_~_++--,;]_:!?~<_~+i^-l;?+:;+_<i>>~"~+"i[:}[~<^
                       I~<-><;]__;>?~i-!i_>__<><!.. .'.'.' '.^.'''`'. .`.'`'`'``^.^'.'`..`"'`^^,.`".^"."^`'.
                       .,""^".`::'^,``;.`^I",I":"
                 "+!  <i"!lIIil^>lIIl,"!;l I>l!"'!>Ill!;;.
                 "iI  ^;`,,!;I>`^"!>!;^:;l.`:;l" :lIll!l>.
                      ~!<<i:iIl><i,l>i"_!+;><i<:,+ii+i<'
                      "`"::'"^,"",'^:;`;.I^"^""`.",":";'
                      li~;l<><:ii~~>i~+"~!i~:!>>l>"l<IiIli<iI!^_~~~!i+~:!_~><:]+,++<i~i>:>:i;I~:!+<i<>>>;
                     .:";"";I;,;;llII;,^l;;I,:l!l!:;I;I;,II;;!:!!li!;!:'",,,^',;`::::::;",^,"^I^,;i;IiII"
                     ":~~_<`:,<~_i.I>;?--^     ....         ..'.     l.
                     `;l:!l"l;;ll;':I,lI!,`",,^`^``^```^""""`''''^`''l
                       >?!+>,>;ii!<li<!I->-I]<+_"-]-?~-I>!~><<~i~,-<!i~ii<!l;;!l?<~<i;~~~;<!;~<_!,<>~~>!+><:
                       !~-l!!~<i<Il>><-i:<l?__+;;>i>>:>li<~>><!l~i!~i;-~~~<><<"`,;l;;^:;:"^,'`":"`;:III"";I"
                      ^lil"lili:I:I>il<;^i'i<>i'i~>il:!l+_><I<I;>l:<i"i<<!~>i!
                     ,I<>>!`,<>>i^^>,<<i>'`....`'``'.'........''.....;
                     ":>I+!^Il!<>''<"<_+I. '....' .''. ...      .'...;
                      '>_li!;!l;>~i;iil;_>_I~>>>:+~>?<+Ill!ii!ii<;_iI!!::;,:^,;,i,::,^l;l";,,lI!:^;III,;iI;^
                       i~<>ll+~i+i>!><+l!>~~<<-i">>i<i~li!~i>>~~<;>!!~<~>i~<!i<I~<<>i:>i<;ll:;!<;,<<~~il<~~;
                       i<i"!~~>Ii"!+!i+l;+.<~>i.;+i!_+<~~,<!+-i<!-l;+I:_i"+<+<++>>
                     ^;;l;,"":l;;,`""`,^^`:"^``^^`^```^",:"`^^````^^`:
                     ;I[!]I`;;+~-! i<"_^        .                .   <
                     ':i!lII;;,:IlII!l;;+!i:>i!i:<~>>i!;;;:;;;;l!:!l;;"`'``''.`'^^.....`'`'^..''',^`....''..
                       <_i<!I~~!~~~,!+~!-!?I<l~+^>-+_>~l!>i<>~~+<^>~~;?>+~~<+;<li_]--i!-]-l_~:[!,~+-I,_+?-+l
                       +_+;i]iI_ll-?-___+>
                      .  .     ..  ...'.
                 ![! ._il+<-__+"~[<+Il+>~<_~+-i
                 '`'  .^^^',"^,.^^`"'''':""^":".'..          ... ..
                       ++>-!I~l~+ii:>~il{">:__+--~~l<l-><~~<l'~-~>`~_ll-,_~_+~<~+I_;~~;;l!~!i!!<<: +I+ii+i>:
                       _<l:+~<l"<i~i>>+i:+<<<,:i<~II~+:+<<~<<,i>ll!I:>>il"<<i<]>;!~li;:_iil!!<i!i~l,+_--+_{l
                      .+<> ;-<::~>~i+><;I~!i?<i>;<II<!"+~<il<;i+~_+iI+~I?i~!~!i>:I<>+!:ii>I<li<>I<>"!l;l";i"
                      `<i~` Ili"!l!>>!+li!~i<~_~:<___!I~!~I"~I:i~+^!~ll>--<l;~+>_;I__i!!I~>!],i~~~'
                     ",`li!;':!!::',II>i!!;'''''``'^","'''`^'`^`''^^^;
                     :"I<-~; !}_ii'!-_<<i__`.     .     ...          !
                     .^<il"!~l;!;;:!I"ll:,<<<liI<i:llllI;>!<l:iill,,!;^^`.^,"^^'",`^^''`'
                       ,l>"!!I!>Ii,;<`Ii;:+!>ii"i>^;+!!!"+:><,i<l;`^+!!!<">+Ii+,~~]_-?<~I
                       !l:`;l!:,l">,.:;";`"`""I,,;::';`I,.^"",,^^'`!^":"'^^``^^,`".
                      `Ili,>_<>ii:_i^l~I>,!l!>+<+?_~l-;~<I!i~~<~i<;-_+<_li!iii><><,
                     ::,l!!"."lll,'i!illl>,'''..'```'.'..'''...`^"`.':
                     :"I>~<: "ii+I`-~<~l>]! .  ....     .     '..   .I
                     .^<!!,!<iIiI!I:;;;l;Illi<!I<i;<l!!!:<+i>lIill>l!!"",,
                       ,;>"l!>!<l!::ill><<!Iii>>l!"<!!!<`,l!>; l;;<<~~_<<!















```

*Figure from page 20 (2346x3317 px)*


---



4203-E P-297



SECTION 2 PROGRAM OPERATION



The message "ERROR IN SPECIFIED DEVICE NAME." is displayed on the console line and the



directory selection screen ls displayed.



It is not allowed to use wild card "*" or"?" when specifying a device name.



>ISO FOO:*·* [WRITE]



The directory of all files in floppy "FDO:" is displayed.



The same happens if any of the following are specified as the file name:"*"·"*·","·*"•".".



>ISO FD0:*.MIN [WRITE]



The directory of all files in floppy "FDO:" with the extension name "MIN" is displayed.



>ISO FD0:???.MIN [WRITE]



The directory of all files in floppy "FOO:" whose main file name consists of three or fewer



alphanumeric characters and whose extension name is "MIN" is displayed.



>ISO FD0:ABC.* [WRITE]



The directory of all files in floppy "FD0:" whose main file name is "ABC" is displayed.



The same would happen if the specified file name were "ABC" or "ABC.".



>ISO FD0:ABC.?? [WRITE]



The directory of all files in floppy "FD0:" whose main file name is "ABC" and whose extension name



consists of no more than two alphanumeric characters is displayed.



>ISO FD0:MS*.TXT [WRITE]



The directory of all files in floppy "FD0:" whose main file name starts with "MS" and whose



extension name is "TXT" is displayed.



>ISO FD0:MS??.TXT [WRITE]



The directory of all files in floppy "FOO:" whose main file name starts with "MS" and comprises a



total of no more than 4 alphanumeric characters, and whose extension name is "TXT" is displayed.



>ISO FD0:ABC.MIN [WRITE]



The file "ABC.MIN" in floppy "FD0:" is displayed (assuming this file exists in the device).



>ISO FD0:123.* [WRITE]



>ISO FD0:ABCDEFG123456789.* [WRITE}



The message "ERROR IN SPECIFIED FILE NAME." is displayed.



In the OSP format, main file names must start with a letter of the alphabet and consist of a total of



no more than 16 alphanumeric characters.



>ISO FD0:*.123 [WRITE]



>ISO FD0:*.ABCD [WRITE]



The message "ERROR IN SPECIFIED FILE NAME.» is displayed.



In the OSP format, extension names must start with a letter of the alphabet and consist of a total of



no more than three alphanumeric characters.


```text


                                                                                               ."^```^ ,'`^^.
                                                                          '...'...    '..  ..  I}---i~ +I-[~`
                                                                         .-[_i<<~-_!>'__[~-??_]?:_]~++-+++_],
           .^^^^``'''`''''```''''''.'''''''''..........''. ...............''''..`''''...'''`.'''.`'.`.`'.``'.
           ':::::,""",:>!!IIl!l;;:;!il!!l!ll!llllIIl!>>iil;l!ii!!!!lllI::;;IIIII;;;:,::;IIIIII:,:,,::;IIIIII`
                      ,::<-~! :?_!l`;[--<i~~`......'''.. ..''''.......I
                      ":;!iil^,:I;I`I<i!il>+;`''.''''.``^'.......'`''.,
                       .li<;!+<~><<<`>~~__<?Il_l[_~<<+!_~>l?[>+~--i]_?[?""i,!<<<<!!i:;I;+i:Il!!l<:!!!"lIll~!"
                        i<<i<<~i>-{+I~>!:i!i!!l;>;+!i~Iiii^::^""::';";;l'.;^:I>l!iIl"::"Il";I;lI!:;;l"!;I,l!"
                        !!,lI;I,"iIl!lI;`!,;>!',;,<ii<<>!l
                        l^I';;";~;;::;:"`,I"`Ii:^l;:``"'^"`l,`l;II';;l;i;,;""";!::;:`:::;`
                       'I"l"!>;i<li!>!lI"lil;><il_<>";!`ll^;":~l~<,++_<i~;<~II!_il>!"<<l~:
                      ,,^!i!,.;~!!,"`"^!iii!~<;`' ..''.`''^`^`.'..`..`I
                      ,:I>~<I.;<<~I!:;;__~~!~->     .    .'..        'i
                       `><>,i_>iili:;<;>,>!>:I;+>ii!,>-+~iIiI;~i!i!li>^
                        ^"l"::,::II,";^i';l!^^^:l<!i^',;l, ::^!<<l>!l"
                        !>!"I!!>I,!!lll:;"I"lI';:;I::l>;IlI:'l:^^:;:I~l!"!::!;,~l":Ill;',:,',,````,,.^."
                      .'":l"l>l!!,>>ill:l:,;I<:!;!ii:i<i>>!-l~>lI+<ii+>!">I,ll"!i";i!ii'`l`'`I``.`l^''.'
                      :":<~<: ,!<~;:">~_;!<<>!+~!'..'......'`'...  ...;
                      :,Ii<>,.,;i~liI<+~ll<iiI!<<'' ...  .'...'. .'. .I
                       'i<>"~<i!>!<;;>,!;_li,i;+<~>i,i><~!,l<?!!>i:!><lIl;;`:lIl;^>>ii`I`:I;:I::;"
                       '"Ii,i!llI;!:,I:l^I!!":^;lii<,";i>I'l><;;!i;<<~l!>!l^I~!!i.iill.>,li~l~_>>;
                      i,:>~~;';i!>,l!!:<_~:li<<l<i" '''``''.  .'..^``'"
                      l:I!<<;.;!<~I:;::->_Ii~+_!~_l....' .''``.  .  .`;
                       `+<i':+ii>i!I'li.>",<!i'i",+!!!l`~~~_!:,<<li>":!I;`^<: ^:;:;.^:,;:;l''!`:,::^.;':I,,,.
                        l!_:lil<>~i>`+!,_;;<~<^>::<__~<`:l><;',+il<+,,!_iI!]-:;~<i-^!~I+~~+,"~`I;i~;'<`:~>>!'
                       `~<!><;!li<!I;<~<i-+<iI!_iIl_>>++:~~->+_>!"i_!_;il"[_+<'~^~~]__+>+:
                      :"`:::"`:I;I",::"`^'^:,IIll:`''`''`'",,,"^^^^^^^,               .
                      i,!_[?; !<<-!+]]>:< l1-<]>?+'..            .   .I
                      ^;<!l,ll;;I:;";lI<liI:":"!:;;I;<~>!;;:I;:;:;l;;:I"'.''`'.'.`^"^^'' '`.''  ..
                        :;i">l!i>li;lII-"<ii"i"~i+<+';!>~;.i<i<_>"i+-;i]>:~~i-:~;"-?+i`+l~}-_]?~_>
                       .i;,`",":^^:,,;,",^"":.:^I,'""^`:;"",;^'^^^^''""^'^:I:,'`^'";;"'`      .
                       .!l>:~_!<I;~i<~I!~-~<>^l;<~l<-~<~__<l+<:i_i_li]~<;"~-~!'!!'>?->,^
                      I"^lii,'l;;l^;I;,,i:l!l!;;I"'''.'^`^`'.'`''''^^""
                      l"l+?_:.ll<_l+__l:i,<]__i!]i .   .'.         ..'l
                      '"ill;<!lll:;^;:ll<<!;;:i;;lII<><>ll!iIIl:ll!li+:`^"""`^',Il:,'"^"`"^^^`'^"^`^^`''`^^^
                        I!+l~i~i_<~Iil~l>+_!i;+<-<+^!!<i':~>~>~ll<+ll_>;~_!-:<^!-?~,l-<><~i<_>i+-_!~~<I;-_<?'
                       `><i+~_<^~:!l"ii<i:~i~,<_>^-]i~-l~>i<i:;><~>+<>iIilI+_~?_<<~
                      ,^^,,,"^:l;;,,:"^^:,::,:;I;:,,^""""^:;;;:",,,,":".....''.`'..
                      l^l+]_, <<_?~{[~<"i+_;-}[}+_{<         .       ^l
                      ":>;;,;l:,!ll;"I::;"I:;":;;!;I,""lII::::;I"""^":". ''           .   .. '.''    .
                       .i!~.i+<<_iil'+'<_`-_-:;l^]i_+< l<_]>',[_<~],l<-+"i-<^<-_~<^__?]l,?[_ <1[+'~-_Il[-+_-'
                       ^<~?~l~!!^i_<<!I<^ii<!`>:<_-~-_><:                                         ...  . ...
                      `",,,,,;;;,":^",":`^^""^;,":I,;!;I,^,""^^^^^^^^^.
                      ,`l+?~" <?__>]]~il;<+>,[-]_~__^    .'''..'.....";
                      :;il!l"^,:;l;!ll";III,,!!II:;l;;:,^^"'``''```^","
                       '_il^-+<>~!i^!li?;]~i,i^+i~i>'~+--;'~~><~l;!~>:>~l^>>!!^!>><l,<+I'---,,iI!,l!!il!i<"l.
                       "><_l>i>lI<<i>~+~lI<<+<!<>~<<!!;I+ll>!~<<I^<<<;++i!<!>+><<_<<;<<iI!~!l<__l!ii+_i~~~!!.
                      ."!I!:;:,:^;l;;I;I:^:!<;:!:l;l<!l;li~!>ii!l:~IlI>II!I"!lillilI"IiI<:l`^;;:.IIIi~ii~!i"
                      l^:i>!^.ii>!;~~<:i~~I,i>~!i+~"'..'...'..'`^^.'."`
                      I"li<<"'ili>l++>;<?++!+<>>!+_' .'.'`        .  ^"
                       "il!l-+^!~-<,~_~>^>:_ll!l^i<~_!,!;i+>i<i!!lI>!!;I;;;"i:,">;^I:II:",^I:^;;:::;'
                      .`":l"l>'"I!!:i!!l`l^;li>>";Iii;'l:;<+>>_<<l!+>>!lII~I!:l,>>,>!<>!:I,l>:i<i!i~,
                      l`:i!i' >ill,!>l^";<ii!li!^``. .' ..  .  '''. ."^
                      !:>+-~:^!i~+;i+~l!i[_<~!+?"'''''`^"`''''''`^^^`;,
                      !,I<ii:,><!!I<~<>i<>>!I!i!i<~~+<;!l~<_~<<~lllI;i"
                      l^!_+>' i<<~I_?>i!<>!~!i_+~_~!_-,!"]_<~!>+"    ^"
                      `,>!i:!illlIi::<i<~i<+:~;l<<<l!>i~~!l<l>;ii<>~!l",':,":"^":`
                        ";!':iiii~-:.i:iiIll"i,;<;i;ll;~!,"!!>^!i!>+i..i`>>+i<~<<^
                       :I"!I^,liI^;;;,!.`;I;`II^`,:::,',";;^!:;`:l;',"l!;``;;;,.;I;:!:;^::;"":::::`;"",,;:`;.
                       :<;i~Iii_i:<l!+~!I+-~:i+!l+>i_<;i<-<i_<I,>>!:!;+~~,;ll!i,~_li-><:~!i:!ii><i:!l!!>->;>
                       ,i;:!>~l;++i'I~,-<!>>!!l~<>,li<i~~__<;
                      ;^^;:,^`;;",,:,",^,,":,;:"^","`^`^^```^"^":;:"";^
                     .;"<?-+`.~-_~I>^>]<~{-__+{+'                    ::
                      ilIlliii!!l!!lIl!l!ll!!lIiii!lllll!ii!lII!ii!I;i^
                     .;`>[-~'._++_;I;][_>>!}-_?~?+'                  ::
                      ,:!ll;,"",::,:Ill!ill!:;::li:,:I;;;,,:^"""""","I^
                       ^>~<,<~<~~+[I:?~?_~__:}l~-~-~_-~]-!i_+]:<[][(~"I+:]_+<-___^
                       '.`"''",:,:"'.'' .''.''''...'' .'`...^^.''.^'. .^''`"`,"'`..    .
                       lil__;>_[l;>ii~_`-<+~>_<~:l+><-i:i>-ii_?<!-[ii>_[[~,~i]+!<[?+]-?<_-_<>+>~_-l_><~_[_l~
                       :<:I<i<Il~+~;<!<~,_-<<~!l>><~I;-i><<++i<                  .  . . ... .. .........'...
                       .^''``^`'`"^'``^^'";`^"`"`^"^``^^"",",`,










```

*Figure from page 21 (2346x3317 px)*


---



4203-E P-298



SECTION 2 PROGRAM OPERATION



>ISO FD0:\ABC\*-* [WRITE]



If a path name is specified although the device to be selected is OSP format, the message "PATH



NAME CANNOT BE SPECIFIED IN THIS DEVICE." will be displayed on the console line.


```text


                                                                                               """"': ""'",^
                                                                         .''.''... . .'.......^---?![`>i<]{<
                                                                         l{+><~~+?I+ <-]~~_?--1!!-<-<__~<i_!
           ^^^^`'''`'`''''``''`'''''''''''''''.'''''......''.. .  ..  ...'''''.''.''...'''`.''`.''.^'''''`''
          .::::,""",",!!!!ll!!II;;;:;I!il!lil::;IllIlllli>ii!lllIIllII,,,:;;;;;:::,,:::;;I;III;:,::,,:;IIII,
                     `i"i?+i.'_<_>l_]-~!;^l ,?+]+<++,...''.........'.;^
                     ^!,I!il^,!Ill;i<!Ill;>"l->!<l!>,'`'.'``'........,'
                       il;,>?]"!<!<;I:!<~<~_<!,_~!!l_~,~>;~+iiil<I><I>i>!><>I!,!i+i;i!!!~`!<l,illli!!";+<<<l
                       >>_-[_I!~[+__++!1?l__-~i-~~_-_+il]i-?!__!~~~_:!<-~i+!!+!i>>;!ii>!?lI!>I>>~<<[]I',::,,
                       ;i!>i;`lI!!liI,^<i'>lI!ll,l>i`li'Il>!:iiIl!!!`.i+;;<^!>->>+<+,li^!<::il!><<,i>i








































































```

*Figure from page 22 (2346x3317 px)*


---



4203-E P-299



SECTION 2 PROGRAM OPERATION



15-5. Selecting Files From Directories (MS-DOS Format)



When working with the MS-DOS format-for example in the machining management mode and MS-DOS



file convert - it is possible to display the directories of MS-DOS format floppy disks.



15-5-1. Procedure for Selecting Files from Directories



(1) At the Command Creation screen, press one of the following function keys:



[F1] (INDEX), [F2] (MD1: INDEX), [F3] (FD0:INDEX)



If function key [F1] (lNDEX) is pressed, "ISO" will be displayed at the console line. Fallowing the



"ISO" character string, enter the desired device name, path name, and file name, then press the


#### WRITE key.

(2) At the directory selection screen, use the cursor keys to locate the cursor at the file name of the



file to be selected.



(3) Press the WRITE key.



The display will return to the command creation screen and the device name, current directory



name, and file name selected with the cursor, are entered on it at the position of the edit pointer.


#### Command creation screen

lf'PBYC OPfflATl!!t



ttr



COffilIB :qF(



co 'EDIT POINTER



llaX OlsPI.AY l'A0CEW'E



11'2) -> 11)1:•.•



[Fl)



-> Fm:•. •



¥Hr§ t;gWEffl'



TO DISPV.Y OllER INCaeS,Af!'!I! l'!e$1NG D'l].



llFIIT 1l£ OEV!CE NAIIE Mfl FILE !WE. 1liEII PRESS (Wl!TEJ ID.



Deill.l.Ttli.VICEIWIE •


#### DEFAllt.T FILE ME - •. •

omffllJF


#### Command creation screen

lfBIMI oew.rn•



llllEX Dl9V:f l'ROCBlURE



[F?J -> 11:11:•.•



[1'3) -> RlQ:•.•



lfS::QO§CtlfYffl[



TO DISPLAY OTIER llflEXES,AF!eR l'AES$1/lG !Fl).



llf'UT 11£ ll!:VICE !WE ND FlLE IWE.1181 PIESS (aim)



~LT De'IICE IWIE •



tEFAlll.T FJlE MME - •. •



(3)~



Directory selection screen /~



!l'ROGWI DPERAT lg<


#### OVEfffl IT E


#### PYfflffl)JE


# ':fr

8lftl'fBUiB :wer



'-eorr



DEVICE FORMAT



POINTER


#### I !!Et SELECTUIII

FIJO; DIR's


#### PNefl DIRECTIIIIY

A.001.DIR'



AOO:l.DIR'



Alltli,DIA'.



l'IXl!.llN


#### PIXM.IIM

l'tOl,IJN


#### POCll.llN

>'010.IIH



>'012.MIN



AOO!. DIA'\.



-.DIR'



!'001.IIM



f'OCll.1111,



POC:5.IIN /CURSOR



!'007.IIN



?OO!UIN



Fig. 2-18 Procedure for Selecting Files from Directories


```text


                                                                                               `"^"'"^ :.^^"
                                                                          ''..'..'.  .`'....   >]-]<_i`~;??}`
                                                                         .-}~>~_+]<>;:?]?_?]-?{-;__-<_-_<<+_'
           '^^^^^^`````^^^^^^`^^```'`````````''''''''''''``'''''''''''''''''''..'''`'...''''''``'`.'''''.'''
           `"",",:,^^``^""""",",^`^^`^^",:,,"^^``^^`'^^'^,:"^^^^::,:,,:,,,::::::;II;III;,::,,,;IIIIIII;::,,:.
           ^!+^_`  l-><<l!ili^-<<i!^-llIl`!<lll!i;l!!^:_>+:l~il~,;i:;;:;i:
           .:i"i,  "!i!ilI;I]::^i>i`:"I;I';!;ii!>l;+~";+!>;l<il~;,:>lIl+_!
                 !<;;,',":;,:`"I!',I";!l^;;:l^,""";. ::.^^,"^^;.``:"`'^`',:,:,`"":",,,""","""";"`""";II^,;,I'
                 _+l~>I<<<<l_~i+<I!+~>+<!!i~~;~i!~-:"i~:>~_<>+_ili-~<i<]+<<i~->i__!_]_i>+!lli>_>I~>!>_+;l<!+"
                 <_:;i>!~>;``i:>l_<+~~~!ii:]<~_-l><~"-!+i<!>-i">I]-i!+i+!l<i!-~l-i>+i:?_~<
           .`.'..  ''        .  `        '   .  . .                          .   ..''  ...
           "]>_ll^ ><<~_?]~-i++"_]_-_?<-!~-?<i_~<;~_~___~-[!
                                       ^                  .
                  !+: ^[!_+<;~>ii<<<<>!<~_]+~;I<i<>i";~><+:!!~,+i_+ii~_><+ii;<I!_<<;<<><:
                  ''' .'^"^`'^"^"^"`^"`^^,:,"'^"",,"`^",,,',",'"'","'""",,"l`,^":,:`";I;^
                       `[I~;_]__}~]`i_~+;[]>!`l]}+-__._~-ii_>+<>]~__~_
                      ."^ ''^.`'`''`:^^`^"^"^``.`.''`'^ `^"^^""''^`'.^.  .   .  ..              ..
                      :>!+i<~<~,~+<"-:<,<__-_<~"<I>>~~~+l ;_+<^:~~:~!^?+~+_++>;[;~_I;~i<><i;+>i I!i<>~+<<i_<'
                      .l-<!'!~>I~<]-^>?ii~'i>++"_?<^]+_><<"~<!!~l:<+i~"l+-]:><>~<.<><l_-I;<<>_^i<ii:~<>+~l++'
                      "_-]>i~;_<i,",.",`"!',^,:.^,,':::^,,',:"";"';:^;^,:I".";,,I.;,;^,I^`lI:!':;l:"i;Il,^;!.
                      `l:;":;'l>;
                  ,;' .:':"'.:`'^""`',::",`^'^^^""^ '^^':^''``^`'`^``'^'^`'`"'"^`.'.`''.``"`.^^..''''..^`'.
                  >~" :[!++il~<<<~!~;?__<<i>,<~<--<`l__;~+lI<i+<::~__l>ll<>+[!>~~;><~+<"]l~+il-i:<]!_;><<+~
                      ,~~;_:+<^~~+<+-+^
                       .       .  ..'.
                 .~], ;_>_+ll<<:[?_<->l-_!
                  ``. '^`^^`.'^.'''''..^""   ..
                      ^~><'_+~~_<'+-;I_<ll^+:!-+^!><ii_~<i,>i~?i+`l~!<+i'<>>:!<i`-~ii+",><<_.,i!!>i!:-i>>>>>.
                      ">_~~I"-ii<-~"i>>~l!~->>-+:>_]I>_<;i!>>>^>+>l_<?<<<i!>;i!~l+>I>i>-~i;ii!-~:<+~;~<~~_!,
                      .",`"^.,``.,:'":^:^";::,;:',::^^,:`:,":^ ,,,`;^;^,:`"^'^,;",;,l:!!;;^",";l^ll;:lI;I!,
              '~~~i__~I~+_+i!+<_>                           ii<ii<i:i>+<!,>i<>^
               '!~~+~<~++_~ii<i<!IIllil!lii!!llllll!!IIIlI. `l~__-~<++_~<i~<~>llI;I;III;;,,::IIIIllIIII^
               I:~1}(-1|](_llllll!>\{)+)){>I;;;;;;::!!ii>;! ,;>1)(]?{?_],,::",;I{1|}[/\[llII;;;::;l;;lIi`
               ;')ff]}t){[<([l!!!!!;;;::;:;::;:;:I{|f[?l<"> :^_/(t}jt|t+(\<i+!I!lIli!!!i>!llIl;+}(1{<!:l^
               :^<_("```'`''.... .     ..         .''''.;,! I:<~i_:+?i~l+>!<|_''..'.   '..'....`^"^^'^ll^
               l,:  "?_+I>~+-~-?^.'''''''''`''..........:^; !;I              ,l?_+;__]-?[_.....     .^!l^
               >^,-~I<_iI~-_?!^^^`^`^"^^^^""""`^``^^^^^^^'l l;^<~!!<!;!~~+<"^`^::"^";;;:;,"^",^^^^^":;"!^
               i`./1,<>f?_~^,'                           `> !; ]f:l>1}i]!I;                            l`
               I."+~ll:_}i,:""^::^;::,'".                `i !;.i+l;:>{i,^''."^'^^^^.^'                 I'
               !.:{]~{>[{?+v}|?_}>j/?t+}1:i+!;l!         `i l:.]]+]_+[1lf|[1_{~)x_\]?)<:-ll,>^         >`
               >.If\]l)]][f-:,,.. '' '..^.`^''''         `l I" |\[![}-_)1!:;'''^".'".""`:^^',.         >`
               I.^i!l`;";_:^ .,.                         `l !, <><,;I:+<`` ^^                          l'
               !'                                        "> !,                                         ;.
               >'                                        "> !:                                         I.
               >.^'..'.  ..   ..         .   ...... .....^> l"''  .    .                          .  . >'
               >'",;::i-~:I!<_";_}{}!+])]l_}~"l;,;^l"^^,`"i l"`,""^<<~;,<!~,^>_[]ii+-?;i~+,"l^^^,i"^^" <'
               ^I,>)?:l+t1<;<r)!?|(t>!{j1;~f{[li1{<l:'`^,l` `i";1{;!i)|>!;|(<>(|r-"_j/i:}t?>:~{-:I^^^^;I
                 i!!!i~li!<il!!iil!;>~Il;~>>~!_li!I<li>ll     '`'``'''`''`'^^'''.~Q;"lI";,;;I^```'^^^^'
                 Ill;;>:!!>-_}?li;!!!<l<!<!l>I~;>;^i:>~I,                        -%^',^^i!}il
                 .'.'`;::`l;!<l`'. .'``'``''.''^''`'^'.`'                        >o   ^l_[X]l.
                      ```   ,Y>                            'iIIII:"l!;lI,,;;I,   ~8  ."'I)]il
                             #1 .                          'I>_~~<!_++++>__-?<,,`ir"^`',>!!!i:,:"",,,^`
                             h}                             ";<}[}<_-~?~,"::,;!!{-]_[{{_l!i!iiI;:;!l!iil
                             o}                             ~`[1)1{/(1{_[[!l!I;I<>~i~~~!I;;;:II+-]~~I>"<.
                             M[                             <'[|vil~i>i,>!^`^^^^```^^^^^,><!i>>]{){]i<`>.
                             M{ .                           i'  .",,"'`l:I;I!^           I>>>il^I:!>>, >
                             &~          ";,."~-,";|>^      l'>}?<{)1{+~?[+?]<II;;:,,,,,l>[-^"^"^l~;':'>
                             LL<I;;;;;;;;I~!":Jm;~lk{!''''"'l^{j]]/]1{I"","""::,,,"""","l+><,,,,,i]!,>,l
                              {rnnnnnnnnnrJx""ii".;;;'_vvvOv~^~><:l<!>l                              '"I
                                            "_Yv-l?Xx!    ' i^1n{{1>":"             +|<?["        .  ^"I
                                          ^;++r+I^!-_,      <^1r}[[,                {j+\-`           ^"I
                                          `."!.             >^|r}|].                }r-t- .  .lIii!i;^,I
                                            '               >^{r})-                 -/+\!   '^,:;;:;^ "l
                                                            i`[f}t?                'CmLOJzzY0YzccvvvvYII
                                                            l'~]+1_^^^,^`^^``^^^^^^:(\)t)-?__??]-__-?]"I
                                                            ! "``'":"^"";:,::,""^",^''`` . `". .`^.... !
                                                            !:``''">''',~`^`,i'`'"i'^`:<~~?i~~_!:l''''^i
                                                             ^^..'^^``'`^''``^`'''""""";~<_lI+_~;;"",:;'
                                      !ii.<,I+'<>lli!ll>:il^~!>!l!;I:<>!:ll;l^l!IIIl:l!"
                                      ^,<';`"l.,";;ll;Il":I'l!l!I;;~""!!;:;;;":II!I!:!>;












```

*Figure from page 23 (2346x3317 px)*


---



4203-E P-300



SECTION 2 PROGRAM OPERATION



15-5-2. Directory Selection Screen (for MS-DOS Format Devices)



Lines 4to 7 The command being created is displayed here.



The selected file name is entered at the position of the edit pointer. The edit pointer



cannot be moved by pressing the cursor keys.



Line 8 If the device is MS-DOS format, "MS-DOS" [s displayed here.



Line 9 The device name for the displayed directory, and the current directory name, are



displayed here.



Line 11 Normally, "PARENT DIRECTORY" is displayed here.



To change the directory to the parent directory, locate the cursor at "PARENT



DIRECTORY'' and press the [WRITE] key.



Lines 12 to 20 : The directory is displayed here.



File names and directory names are displayed ("\'' is appended at the end of directory



names).



If no file name is displayed, it means that the selected device does not contain files.



When the cursor is located at a file name and the WRITE key pressed, the selected



file name is entered at the position of the edit pointer.



When the cursor is located at a directory name and the WRITE key pressed, the



directory changes to the selected directory.



The Command being {



created is displayed



here.



The device name of -+



the directory and



the current dlrectory



are displayed here.



The directory is



displayed here.



co!



"EDIT POINTER



/\001. 0 IR'-.



A003. 0 IR'-..



A005. 0 IR'-.



P002.IIIN



P004.IIIH



P006.IIIN



P008.IIIN



P010.IIIN



P012.IIIN



CURSOR



OVER/iRITE



DEVICE FORMAT



A002. 0 I A'-.



A004. DIR'-.


#### POOi.MiN

P003.IIIN



POOS.IIIN



P007.IIIN



P009.IIIN



P011.IIIN



P013.IIIN



Fig. 2-19 Directory Selection Screen (for MS-DOS Format Devices)


```text


                                                                                               ``^^.".'^.^`'
                                                                          .. .. .     .        _[-]i[";>!{-i
                                                                         I}-~i>~~?l_`<-[__+-?-{>;-_]_?+i_~_<
           '''''''''```````'``''''.''''''''''''''.''''................   .''''.''''`...'`'`'''^''`.`''`''^'`
           "^"^^`""^",,,,:,:,,,^^^`^,,,,,,::,,:^^",::,,"""^"^"^^"::::,::,,,,,::,,,:;IIIII;::,:,:::;;;;;;:,:"
           ,>,!"i  >iIlll;;"<lIIlll,:<;Il!":>;"~<l;iliII!;l;lIIl;:;;;;
           ^I"I,l. :;,I;I:l^!lIlIl!:^lI;l!^,I;'i;;:I:l;^,l;;<I;lIIIl!!
                  !!i+>"!!<^I     ^>~l"i!li!~>~I~<<iI:i<<~>l:l:+i!!>!>!l<i>:
                  '^`"^.''^..  .  ',,"`,,^^":,;"::";;^,:::;"^,^;;I:!;:^`,:,^   .              ..
                                  "i<lI+_~!]<I>]i^~~l~,i"+i-<>+:~ii~l;~i<~>~:<!?_>l_}~>~_~[_^ l_]l>_{I<<__-i
                                  ,<<>i+l~+,~<i<+li~:~<~~_i_l_~l;!!<>!!+<>i. ' ....'..`''.''    '..'''`'''`.
                  ...  '          ^I:^^,^":'^"":;,"l,I::;,"!:",;^;,;;^^Il;,
                  I>>~I-       '. !!;~!:]i>>~^<;]-i!_i+I><!i~< !]_>!+<+< >"_-?+-~++!<_<<.
                  "^^"`:       .  "I"^':""",'`,""^',^`I"`^:"":`.^"',"^^"'".`";,"l"^''"""^'.^'.'.'  ..'.. ...
                  l!i+;~       '. ,<<!"_<>>-^:+~>+^<>"?~l,?-_-]_+<"?~_~~+_,:]>+:_+,I<i>_+I!_>_~~_<^+->-~.?_<
                                  ;+~~-~<~>I~i<^
                  ^^"^."`         ,I,::;l,'"I;ll:,,^",:;:",:",""^'.'^''`'.''`'''.
                  I>>~`l,      `. I_>!i_?_`^><++->>^;<<_->I<i~<i'>!I?-~>-~+!:_~-:
                                  :! .;"",:" ;:` l:::I^: ": l:` ",,:,"'l;:::""..;,"l:.;;, "^",,''l'"iI:l;;I,
                                  I?li_~??]_;+_!^-<<~_i_:i~'-?_;?]-~<;^_!<iii<:.iii_~'i><.i>l~~""]`^><i~+i<,
                                  l><<<I;lI>i; l~!l;i<~!I+>,<_-_I>]l<~-
                  ::;II`l;::^>;.  ,l;""i:;I::^";`!;;;I,;:,;::'     .  ..           .
                  ;lI>i'lI;I">;'  ^;iI:iIiI!!l"!"i!il+!il"i!!,
                                  i!>":lIi>IIi!l!>!l<!i",<ilii;>i;<~>i<i<>!I!,!:<ii<l!<>li!li!;!lII<l>!!<!!:
                                  ;!_!>_>,;,,,,,":::;:;,^l;,I;";:":;!:l!I;,^^';"i!ll,;ll"l;";I:;:,;:;;IllllI
                                  "!!:i!I
                                  >;;I:~l"!+!<Ill;_<<_<<><^i:i<<ii:]>+!-i:l>~i!<i;I~l!i!,_l>I,l>:Ili<<lI_l!`
                                  ,","^,;'^l^:"^,^:lI;!l::',^,!l,:^;;I":;^:l;I;ll":!;:;:`l:I,':;";::!l,`I;I'
                                  >-l_<^<>l,<;i>:,I;>!~_~Il<:l>_;:~il<"<l>I~<"!<<?i-:!<>:~!i>+<<`_~!;_++>+~<
                                  >_ll~>>~;<;~~]<>+l~__-~;>>>?><;i_<<~;~?~;i+i~~:'.'.'^"`"'^^""^'`^^^,^""",^
                                  "I;';::;':`;,;::;^;:"::"I,;;:,`:"^::^;l":;:::l`
                                  >?i>!.>~!.!Ii!! i",<i<~<^:~.l`?!ii<I>.l~>><'-!_;[~!;}-_~[_;-_l;+~~<+_i`[_!
                                  i]i~~iii;<<-!__!iiI]+I<_+<~++l~~~<~i+I'`''^.^'`.'`` '.'..'.^"^`^^^^^^`.^^`
                                  ,;,:,:,;^,,I"iI;^:^:;^;l;;;!I";:II;I;I
                                                     "^""^'.''^^'^``````'`''^^`^"","``^`'''^^`''^'.'''`^`""
                                                   .i"rcnvxXvvvzYuCLLCCCCCJJJnXvnYunnnXCJUCCCJUJCJJCCCJUC\,!
                                                   '> }\((\t|\||\tjttjrrjrfjjtt\/fft\tfrfffjxxxrjtjtfftjr] _
                                 ^;,`,:,,,,",:,:. ^`> nCmCczruuurzzrxXUYUCUYJCJYUCCJYJCJYXcXXXXYvtj/rxuUJ| ~
                                 "~]~??_~)]??[][^.I'< ^"![                               ;~!li<"ii_-<i.    <
                                 l?]?>:;,!<ii!i^ ':.i     ':>iI"iI!;I!,                   `::.'    `'.     ~
                                 ^lI,             "'I ][]}{{f\(}|tf\tf\1111111{1111111{{?]f)}{}{{{[-_+][[i +
                                 ,iI"<l!!">!i;i"'^I";.L0YcJQzY0XxccccccYUUUUUJJJJJJJJJJJxnujcUJJJJJzxjYUY/ +
                                 l]~+[+-[ii_?,^..'^`:'i::.^l^,,^.                                        , ~
                                 I]i><--+<_+_il"  .'I.U0LJwOLYCUUwqqqqdbqppqp1.....`^''`'   .......   ...: ~
                                 !}<-}-[--?_?[~` .:';.{\1>[1<^'''''''':<:'..'     I)1i~]>'               , ~
                                 ^"'^,,":"`'""'  ."'l.}1{>+?!'         ^_>-+i];   !)[!?-,'               , >
                                 '`' `'''' `     'I`i.(1{<]?^.         '"",:",'   i(1<1?'                , <
                                 ;?]_]][[[~-`    `I.I.{1{>[].                     !|)~}]`                " ~
                                 :<<~~<i;<>I     .,'l.}(|<[?.                     i(1<{]'                ; >
                                                 .:`>.{}?<[-                      i{?i[?'                I ~
                                                 .:^i.[}--1["``````````'```````^""+)?-(1;^^^"^^``^^```^``l ~
                                                   ^> ^````''''''''''''''''''''``^^`^"^"^``````````'''`''' ~
                                                   `! ::^^^^;:^^^^,;^^^^`;^`^,,;:",,"^;``'.`;"'.'^:;```^`. +
                                                   .>^      ;"    ^;     l     ::    .;!+i];",>_~:'I      :i
                                                     ",^","":,""":",,,""",^"^""::^```^`I>!+l,l<~<!;I:;:::;;
                                ">i:"i"~l`+I!!!Il"!+l!l<lI^<!I!ll^<!,I~~;i>l~;iI;I;!;li;,::I;
                                `"iI^I'I,'I"Il;;I:,illI!l:`l!;l!;^!l",i!;;I;l:":l;I>:;iil!>>l

























```

*Figure from page 24 (2346x3317 px)*


---



4203-E P-301



SECTION 2 PROGRAM OPERATION



15-5-3. Changing the Dfrectory



The directory can be changed by locating the cursor at the required directory name and pressing the



WRITE key.



If the cursor is located at "PARENT DI RECTORY" and the WRITE key pressed, the directory changes to



the parent directory.



lffffflW l'.ffifilTltlf



1tfQ2NYERI83:aer



CURRENT DIRECTORY


# I . .

AX),, 11)11



1§-00Sm,yEF!r



l,00.0IA\.



Xll».Olll'-.



' XOOI.DIR'.



CURSOR



!fflitfflM CPffllTl(W 1§:00S g.;wEffi



lt'f9X6fflIFfl:ffl


#### MFIR!Js


#### Offlll!RIJE !trq>!l'y'f!![Bj:g)P\'

CURRENT DIRECTORY CURRENT DIRECTORY



1§:Mcy,Mffl


#### OYfflfUTF

I ~~~li!::======::iii!IS.oos~==~-q• I ~,~~=~~tllllC:======Al:&iC=::::eiai!L~•



/_ .t {_ •~:'Al:;018'



l«X)l.01"'-



CURSOR



"- .IOC!l.01A'-



' J\004.0IA''-


#### CURSQfi POOi.MiN

P(ll);.¥!N



1'(1)5.MIN



!'007.MIN


#### POJ9.MIN


#### POii.MiN


#### POI .MIN


# ~l...__ _ __ I

Flg. 2-20 Changing the Directory


```text


                                                                                                ``^`." ''.``.
                                                                            . .        .       '_---i] !Ii]~:
                                                                          <{-+>~_--;+.+-]+__?-[{Ii_-?~?+<~~}>
            ``'``````^```^``'''''`````'.'.'''''''''''.....................'`'''.`'''`...'`'`'``^.`'.`'``''`^`
           .^`^^"";:,"",,",""^^^^",,,,"^,,;;;;;;;;;;;:::III:::::::::::;IIII:,,::,,,;IIIII:,,:::;I;;I;;,,:::I"
            l!,!:l '><!lI>!I,>!:!iI!!!;I.
            ";";";  :;I:;<:!,:;^";,Il;,l
                 '>!I.~l!;!:i':ii`!i'!>i!!>>II<^ii!~~>!"->":l!!l:"~"~!;"!!Ill!I^~llI!;;';!II:`il!^lIII!;;"il:
                 ;~--!]<>~~lI`";,':I`::l,!l;""!`,;IlIIi`ll^"l;;I"^i`;l:^l!i;;!:^i;l;l:i':>II;^<ll:<lii>;_;Iil
                 ^!:;";:^!>:
                 ",lI,`,:,:"":"l:lilI:l"~i>~<ii;:i><>!I!li!l;^;:::l,"i!!IlI^::^^;,,,,:^";,`;,"",^"'";,,^^"^"`
                 l>>>>l<>~~i!<;_i~<iIIi'IIii>l!",i!iilI:!>l!`:~i!;<i,<i>!li"<+!i<i>><~;I><:+i<i>i~;>~-~+-_l<I
                 l~<I++i<>:><~~+i!I
                     .....'   .''````^'''`''`^^^^'''`^^^^^'
                    ^!-}]?_}?-~;l!!!!l]]{_{}]!lllIIl!!!!Ilil.
                    !"})|}\t|1_]~lll!l<~_~?-+I;;;;Il+-?~>l;!,
                    l^?)};>!!l:<;`^^^^'`^"""`^^^^^^^!<_iI"^l,
                  `<>++>i^:i~l!!<~^                        l"
                  ';!:?\??{-[+:;;;;;;;::,;;;;:__?;,,::_]!i;;"
                  ''i<]{<iiIl;,,,""::,^``^'``.::;^````:I^,iI`
                    i:YXXJnnnucccUUvun~   :"^:'           ;i:<!llllI;;I;;;;;;;;;^
                    i:()_]I      `;I":;:I^;;:;"          .l!>vt//tffttttttttttjjvc"
                    ll"            li!>><,               .Ii`                    mu .
                    i;,                                  .,!^                  . Xc .
                    lI^                                   :i`                  . Uv .
                    ::;"`''`''''```''``^^^````^"``^``'```^;!'                  . Uc .
                    I ;,,,:,,^^"^^^""^^":"^^"^'^":^`^,"""" I'                  . Qn .
                    ;,``^^i"^`:I``'>`'',l'''l!<_>!>~;;"''``i.                  . 0r .
                     ""^^",,,",:::"Ill,""^^^"li>l:i>;"^^^",'                   . 0j ..`''^
                                  `;Qr,                                          mj  ^:<<;.
                                ':>_f~^+{                                      . Z\ ^<~x/:.
                                ..^l   Uk                                        p/.":-1~I
                     ","",,,,,::"^,^""^?1^"",,:,,,"^""""",^   ."```^^^^'^^^^````'f?'.:!lii"""""""""^'
                    Il}1)][(-{i:Il;IIl{-[]\\[!!!llII:;Il!>!l 'l>11)-[[-[;:IIIlI<{-][\|_llllllI;lii>i!,
                    l`\||[/|(}-(<;I;;Il!!!i<>>iillI!{1[-i!"> "^>)([1|11__[lIIII!>>ii~+>llllll~{{[-i>">
                  ''!,?{<:!lI:;l;"''''.''..'```''.'`;;:,^`.i.^"i)|;Ii!!,ll"^```^`''''''``^^^^:!>iI^"">
                  ;~~++<~l~--<>i_i.            .           l~~_~<>I:>~>>i>~l                        `>
                  ",llrj-}?+[!II;;IIllIIllIll<)1[;;IIi1]I_;:;iI<t[]([[}::,",,,,,IlIllIl-{{?IIlI>1-!+,!
                  ..i!<!` `'`           .            ....";;.;!-1_{1[{_iiii!i>>i`''.    '`'....'^`.:;l
                   .!<mpLQmOZJvvvzuuuu,  '~;I!`          `:; ;"(0zJzffjrxnnJvrrt   `<;:l           ":;
                   .!;{-+-!;:;IlI+_<!i"``'^'`'.          ^;! ::-f+[-        `;,I<!i~n-{]`          ^:I
                   .i`             lli_+_:               `:< :"]j?|>..      .;;;I::if?/<           .,!
                   '<"'                                  `,l :,_f?)!               lf]t>           `,I
                   '>;'                                  ":I ;,-r}/>               !/?j<           ":I
                   'i",^^,:::,"",:"^:::^^"""^"""^^"""^""":^l ;:!?<?l^"^^^^^^^^,:,^^l_<[i^"`^^^^","^,";
                   .l I,"^:^^^"^`^"l^^^;:^",l^``,,```,`^^` i l:'^`':;:"^;^^^":^^^I"^`,;^^"I:"""""",`'l
                    I:^^^";``^;,"^,>"^";;^^^i_?[l!][ll"``^I; ^l^^^`Il```!``^:I^^`:''`"<~--!i[?;:`'`^I,
                     '```^'''`^^^;;::!^X{.`'.'''.'^"^`^`'`'    `^``''''`''`"^^""^t<```'^""'^,,,"^``^'
                                 ll}_l XO:`''''''''.'''''..'''...               ~B~
                               ',~+n}i' )xrrrrrrjjjrrrxrxxjjjjrjjjffjrjjjfffjrrxu~
                               .' ^,'`          .^' .`','."^'''``'':`'""`'^^`'
                                                ,!-!:ii?I^~<-~~[<]i?~!<+>++_i_'






























```

*Figure from page 25 (2346x3317 px)*


---



4203-E P-302



SECTION 2 PROGRAM OPERATION



15-5-4. Function Key [F6] (RETURN), [F7] (CANCEL} and Cancel Key



When function key [F6] (RETURN) is pressed, the command creation screen is displayed and the device



and current directory names are entered at the position of the edit pointer. The file name that was at the



cursor position is not entered.



When function key [F7] (CANCEL) or the Cancel key is pressed, the command creation screen is



displayed and the device name, current directory name and the file name at the cursor position are not



entered on it.



Directory selection screen Command creation screen



I' /"iPffflWI CfFMTfllf _, lf!J9WI rmu.r1m



¥5:-09$tffl¥f8I 1§::00S CQNfflT



\..



Ill• ii!li:J~CTj)llllN~======:::Jl~,,_- _ -.. ::.:::·~•"">GE~::.q,



FU):'-Jl!C.Dl"'-



~~:D!T POINTER



HtOEXt:>tSo1.J.Y~



[FZJ -> Kn:•.•



,,_., DI



J001.0Ul",



JOOl.l)IA'



~-0""


#### AIC2.ltll

Pl'01.llll



[F3J



POOG.lllfl



;:o(l;<a.•


#### TO DISPUY 01",el llo!IE:<e$.AFTER PA!:SSIM: [Fl!.

IIIPVT THI: OOVICE !WE MfJ Fil£ NAIIE, - PRES$ ['!RITE] K!'/,



~F".V.11.J OEVICE HMI£ -



~r FtLE 1WE - • •



\. Ital(


# §1 ....._ ____


# _,,,t

/ IP!3P!JUN OPflWUW l:"ir-0® gN';'ERT



llllE)(DIS'I.AY



{F.2) -> iDt:-•.•



(Fl) -:> FOQ:•.•



Til DISPLAY 0'!\£11 Uill)lcS.JF!Sl P!'£SSIHG [Fl].



IRT H DEVIC:S. MIE Nf) f:lt.e IW£. NEN PRESS (llllTE] KEV,



t:EFMJr..TtEVICEMM:-



CEFAUI.T F"lt.E ~ "'" • *



"YFIEIJE



:gpy "'llffl'ITf I



~N.R»:'veC.OIR\;>OOJ,MIN\EDIT POINTER



INCEC OISPUY ~



[f21 -> 1()1:•.•



[Fl] - > AJO;•,•



Am;



~--------~►,



TOOISPUY l>IIER l!Di>a.AF!DlPRESSIM: [Fl).



lriP\IT TIE a:Y'l<:E ~ ND FILE !WE.. nf9I PfE$S. ttrFtlTI(l KEY.



OOFAl>..TOEl'ICENIIE -



CEFJM.T FIU NME = •. •



, HID



1-:~ I '?'fu 1= lo: lc:m I



c,,o:a.



Fig. 2-21 Function Key [F6] (RETURN) and Cancel Key


```text


                                                                                               ^^""'".`^'^``
                                                                         ....''...   .'.   .  '?]?]i[`l!![?<
                                                                         ;)?<<>+~?!_'<?[~+??-?{I!-~?-?-~+>_<
           ^^^^^^''````^^^^^^`'``````^````''''''``````''''''''''''''''''.'''''.''.'`...'`'^.''`''`.`''`''`''
           "",","""^^`^""",""^"^^^,,,":,:"`^^"`",:::,,""^"::,,,,,""",,"^"",;IIII::,:::;I;I;;,,,:;IIII;::,,:"
           l<;~,i .+l!l~ii"!<i,+~_!;+-!i:<-~l _l<:llii<l>i,`IIl:Ill;;l;>;:
           ^;";^:  `"::;::'^;!"I`lI,,l^`:::I;.l`:,:,,,;,II;'l;I^,ll:lI^ll!
                ^-_!i"!!II~II`Il;I~+!,+-l!Ii--:^I;ll!!ll':>!`:;II;I;:;,;;l+ll^!;Iil^l:;>ii>lIl;IlI:il,Ii;:;;
                `~i>!l!<><<l<l<+~>;l~<i~!"ii>i<i<~>+<-~-!Ii<l+-iiI-~-<li~?>>iI~>!l><>!<?_>~-<<;->~I!<!l+<<~>
                "+li:<iI>i>Ii!~!>i<">?i~~;>i!;>>~l>>,~;iiI<!><~i!">;~~;!><,>iii+! '!!!l_;^i~l~:<<-:<<-"<!>i>
                "!>!<!"~!~~><:!;;~<;>l-<i~^
                `I:^"``"`^^^^''"^'.;,: ^"",:",,`''`.^`''"'`''`'^'..`..''''''' ^'. ..'''...'....'.... .. . .
                ,]i<?;`<i<><<;"~?!^-;<'<!~~-i_+i^I<.>~!`i~~i~~'_>~ _"l+<+_++l _+!'>><>i]<<;:<_--i<`:+>>+-`,~
                ^~<<i_+~!"-!<l?+,~-i<_iI+_>_^:i<>+~lI+~<+~ii"~~i_I!~~!-_il[i:i~<+;I<!+>;!!i<<"i><-+i!:-+:I<<
                :+~]<+_Iiil+'.'`.''''`'.`^'^''``.`'.'``^`^`".^"`^'^^^'`^^.^"'`:^"`^"'^"'""^,"':",,,"`^I:``:"
                `;";,::':"':

                    ^^^^^'`"```.```'                       .`'''''.'''....'.
                    I~___<+[--->_+?<^^`'....''''''`^^^^^`. ^i~<~~~l>-_~!~<-!'.  ...'^^````''''''.
                    .;_{{[-}-]<IIlI!!+}[_?{}illl!llI;l!i>l^ ,I--?~-_+?;;!!IIl??]~{{?iiiiiilI:Il!!I.
                    "^{|t1t/|)_1+!lii<+<><~<lIlll;l]1}-!!"; <"/t\{/|\[?]!!iii+_-~_+>ll!l!l~[{-~!I!^
                    "^!<-?{__)l:^''''..............,;,^'',l >"?~[[[-{}I;'''''......''``'^`:!!;"^!l`
                    ":       ."<+~I~~~<?<..  ... ..      ,! i^       ':iiI!~+<<~: .            .;>^
                    ;:[u[t|1(<;ll;;:;;;l;;;:;[-];;;;l]<:<:; !.!_!>~!l__[>"",,""""^^``^``^``^^^^"^i^
                    :l<~!!>~>:                          ::" ! >("l>1>~"`                         >^
                    ,:1|-[_::"           ![I<,          ^:, l i<i~l?[;<+~!~!>?++I<,'^''''        !`
                    ,:)t-|!              fX/r[_+~~~~~~~~_," ! -)+_[{-]t-_!l!i]l_!<~;~l;lI        l'
                    ::|n{/`             .nUvvffxcjttt/tt\;; ~ <]-,~<+{>^."                       !'
                    ;;><I!.                      ,;;ili.'!; i                                    !'
                    :l,   ......'............''..`"^^"^'lI" l                                    ;.
                    !:;;:,,:::,:;,:,":::,,""^^`""`'^"^":,,, l `  ..  ..  ..    .   .   ..  ..... i.
                    l;````!^``:"'`"!``';```;!l>:;!!"!'`^`;, !',!I">]+I><[l![|\<>1|~+}]Ii;lI:;^``.>.
                     ,"^:",^^",^^^^"``"),":I~_]!l??ll"""::..":;[?I;>[~:I[-I~-[-__[~;+-<;l?_;:,,,:^
                         '":,:.''.:;l;:W,                                     vd
                         "<+l;"~<'!-}i;MY()111)))((){{{{{{{{{{{11{{{{}}}{{}}{\Q+ .
                        `;>_!'    ``'`,a!i>>>>>>><<<<<<<><<<><>i>~<~<<~+++~++i.     .. .
                        . ,^          ,k.                   ':i>>;!i!!^^""","!>_<~~>llIlIII;;;;l!"
                                      ,b`                  'I!//|}/((?_+ii!!i}]]_){_iiiii>_-_~>i:I
                                      Ia'                  ',<|)\//\11[(_<<1i'`'"```""":::+][+!:;:
                                      !o'                  'l^          .. :II!!:;!!ii!.        ,;
                                      lo' .                ^>'i!I!i;!<+~:^^``,li:;I!l!I""""""^^"`;
                                 .,,""io                    < }|;~?)<]ll'                        I
                                 ^<[{I<&u{[[[[[[[[[[[[[[[]|_l.~_!iI{_";;;:I,I!l;:l.              ;
                                 "Ii-"!al~~++++++++++++++~[~> [1_}?]--f?[>~>]{<[![>;~l;i,        !
                                   "  lo                    i ])?l]+}|<^`^                       <
                                      ih.                  `l ...   '    .                       <
                                      <k                   'l                                    i
                                      >k                   'I.'                                  i
                                      ~h                   '!':;:,!_l:!i~,l-{}!<]{!!_~:l,;,,,^^^.>
                                      ~h                    :",?>"!])<li\-;[|\<i)t_l{[<:<{-;,^"":"
                                      ~k                     ^^`^^''`'^^'^^'. ''. .`'`^`^`^"":,,^
                                      +b                   .!i{}}+]--+:I!!!li1[}-)1~!!iii!l;:Il!!;
                                      ?k                   ^;>(|1)|))-[?llll!<~<Iiil;;lllI-{1-iI^l
                                      ?k                   ^:~~_?{]-+?i?>i!>+i-|^. .''..'.,;I:^"Il
                                 .^`'`]k                   `I;           ....' `:+__l+-__?i  .',lI
                                 :i+-:1p                   ^;'-?>__i<?_];^^^""^``""^^^""^"^^^"",'I
                                ^i~x|I[*`                  'I }]"!_)ii.'                         l
                                '^+[~<')vtttttttttttt//\/\c],'-~<+I[+;[_~i+l??_+!~"`"`'^.        l
                                 .'.''   ^"""""""""""""""";:;.\1<?{[])\<+;l:~~I~;~!:i;"l^       .>
                                                           ^l.]?i,~l]_"..^                      .>
                                                           "l                                   .I
                                                           "l                                   .;
                                                           ^,''  ..  .'  ...  ..  .'   '. .'''''.l
                                                           `l';<,:<}<lI_];>\t|!-(\!>|-I!Ii;!,^^`"l
                                                            ",l_l,;+?i:i}<!__?ll?-I:-_i,~[+,"",,:.

                                      '        .                  .
                                     l~]:!~~~.I<i>~?>i;--_;_+1;_{{i<+[_[I>~_!>~+~>_l-+_'
                                       ,`..'.   `.'''..'`"''."''.` .`.'"'^`^''^"^"".`":













```

*Figure from page 26 (2346x3317 px)*


---



4203-E . P-303



SECTION 2 PROGRAM OPERATION



15-5-5. Directory Display Method



{1) To Display Floppy Disk "FOO:" Directory



Press [F3] function key {FDO: INDEX).



The input examples given below show how to designate which file directory is to be displayed.



(2) When function key [F1] (INDEX) is pressed, "ISO" will be displayed at the console line.



Following the "ISO" character string, enter the desired device name, path name, and file name, then



press the [WRITE] key. The following examples apply when an MS-DOS formatted floppy disk is



being used.



>ISO FOO: [WRITE]



The directory for the default path name and file name at the FDO: device will be displayed.



The default file name is indicated at the directory display procedure.



The default path name used at the MS-DOS file convert function is route directory"\". The default



path name used at the MacMan mode can be designated as desired at the environment setting



operation.



(3) When a path name is entered before pressing the WRITE key:



>ISO FD0:\ABC\ [WRITE] (Absolute path designation)



The directory for the FOO: device, "\ABC\'' path name, and default file name will be displayed.



If the path "\ABC\" does not exist in the device, the message "SPECIFIED PATH DOESN'T



EXIST." is displayed on the console line.



>ISO FDO:ABC\ [WRITE] (Relative path designation)



A path name which doesn't begin with"\" is interpreted as a relative path from the default path



name.



>ISO FOO:\*-*\ [WRITE]



The message "ERROR IN SPECIFIED PATH NAME." is displayed on the console tine.



The wild cards"*" and"?" cannot be used in any of the directory names that make up a path name.



>ISO FD0:\ABC.1234\ [WRITE]



>ISO FD0:\123456789.ABC\ [WRITE]



The message "ERROR IN SPECIFIED PATH NAME." is displayed on the console line.



The following restrictions apply to the directory names that make up path names: the main



directory name must comprise no more than eight alphanumeric characters and the extension



must comprise no more than three alphanumeric characters.



>ISO FD0:\ABC\123456789.ABC



>ISO FDO:\ABC\ABC.1234



The message "ERROR IN SPECIFIED FILE NAME." is displayed on the console line.



If a path name is specified, the format is taken to be MS-DOS and therefore the main file name



must consist of no more than elght alphanumeric characters and the extension name must consist



of no more than three alphanumeric characters.


```text


                                                                                                ""^"', ^^`""`
                                                                          .'..''.'. . '''...'..^__-[!]'!l<??!
                                                                          l{_<!<~_]:+.__?~__?-][ll-~?<?_><<]i
            `````^^^^^^^^^^`````````^^^^^^`'''````''''''''''''''''''''''''.'''..''.'`'. .'''.''`'`' `.''''`''
            ^`^`^^::,""""""^"^``^`^,"""""",,",;;;;:,,","",;;;;;;;;;;;;;;;:,,,",;;;;;;;;:::::III;I;::,,,,,:;I"
            !<:>I! .<<i!<il;I<>!!<;;-<~!I>'
            ",^,^,  "::,,:",.^,;,;:':;:",:
                  `l:  ;l`!l;;l:`!:;;,^"!:l'Ii!i;^l!I;:;::.
                  ^Il. ';^;;ilii",,i~!I^lIl'`";!: ,Illll!<`
                       <!lll`+l~;il;lll;,Il"!>!i;^~~i~l>'
                       ^^,:I`:'i^,,":::^^;l`,"::".:!;l:I^
                       i_i:">i!;!!>>!>~>:I>!~II<i!i";il!lli!i:<"~<>>i!<-;I~iii,+<"i<>i<!!:lIlI,i::~!>>II!l
                        .^' ,,^'^^,"^,",';,":.':^^,^^",:^'"""';."::ll^;I`":^,^.,;.:,;;:;;"":",'l""li>!i!!I
                  ^<i  >~lll^;:;!i;,;lI`!I;::~>!>;i";"";;;::I`'!i;:.:l:,;',;:;;,,;":":;^."^",,I';"^
                  ^!I  :;"I,.,:,III,,li,I`"::;I;!:l^;,!;lIl!l^ ;I;`.!l,;i^I!~li<!>,>:IiI`l:!>!~,lI<.
                       >;~il>;Il!I"^<il:"ll!l;!!`;;l;;.l:I:^!I,lillI;"I!":,^":::: ,:!:`:I:I.`:";!;':lII:`i;!"
                       Ii<<<<_-~~?-i_[-:>i<II-~~l~_><}l<;<>l<>i+-ii>~!i>~<<>I+>>[<~_?i~~+>_!!+>i>?!l+i!<l<i_;
                       ~>i>l:~<:+>i<;>+I>~~. Il>:>~ii>I+Iii~i!<<>"i_+>!,+l~i^+I;__lI<i+I;>l!~_~~;>~_~~,!++"!i
                       <++<_:<~+<
                      .I::;;""""""^""^",:;:,^"""^""""":;;;""""""""""":I.
                      "::<[-> "+<]+.i[[]+_}<.         ....         ...<^
                      ':I!III;:":::^I;,::^;!::^",^^","^^",:::"^"^`^```:.     ..
                        l<-;l_<+<>i!;-;i_+,_--+]<i-[<:_<!~I!<~I+-ll?_~+"]l_+>i++-"![>~>>:-[i~_:-~_--<~_"
                        ^"^''`^^."^:''''`^.`''^"`^"``'`^^^''"`.'`'.`^'`'^..'` .'^.``'''`.`'.'`.``,`""``.
                        :!_II_i_><l<~">_>~;I<li_+>?__:-l<_i;]>~><<~^__-<?>I-i<_+-~+!
                        :,^'"",^`,''":.^^^"'.``^```^^`":,',,^,^:^.^``'"^""`^`^`'`''`'^.'"`'`''.`".."^'.^'`.``
                        ;!_!>-<_~~i~-<Ii?~_!!-++i-!!+<>_+;><i_l>+Ii<ii_+l~!~><<!ii,!~?l![><<<i<`l. i~~;-+-+-l
                        <i_l'!>;<;I~+-l+!>+<;}?~_[_~`!>i?>^+?^i-:!?~<?i+-++:?lI]~~>_<:-;>+:i~>_!<+<+i+;~+[<<l
                        i_+<>?~<;...'' '...' .''..''..''''.``..`''`'`:'```''^''``''`''^.'^'````'``'"``'"^"`:,
                        ':"^",^^.
                  :_l .<>II;':";>i^I!!!;;;"IliIll,l!i;l";;IIl;:^i;::>><I>l,l;"
                  ,i;  !!I!;,i>i<I";!llII!Iil>!!i,!i!i>l<i<~~i-<<ii;~!>,l:"!i;
                      ""^!>!I.:<>~l:><!!`..."~>_>>!I`. ...   ``^'..'..,   ,:^^,:,:'",l`^;""^^":""".
                      :!l<+>; ";i<I!~+<!"'`':+~~iI><^'`'....'.   .. ..;. 'i<><!>><:>~-^;-><]l<_!ii
                       `>i~li-i><ii;!>"~~<i-+~,"+!l!>,l+-]_>l;<~_:lii<i.;::^;;!:^;:i,.::,;^"II^:`^i;;I::I;
                        '^;^,I"::I;,^;':;I'^,;^`l;;:I' ;;i:" ,Il;'^!I:;.!,;"l!I!I!"!l`;i;i,:<!">,:~~>ii!>I
                        ~"!!:.!>_`.l<_il" >Iil :!l lI<l`! !lI.>l;ll" +i:.lIlII!!I i<><lI~l<!:.<i<i,.il><!>!i"
                        +!-__i!~>:!i~+>il:l<i_!Ii>I<>~>,_Ii,,.;;,,;,.;I,':;IIl<~I.,!";::I"l;:':;;:,`l;l!!!:"'
                       'il!!!I :l,+<+!_<~!:>`l<l"!!!<i~:i><.        .
                      ,:"I!l:';<l!:l>>!".'`,!l!Il!!"^^'''''^^^^^^,:,,,I  .:,`^"``'.`^^.^'`'''^`'`.
                      ::;~-~; :>i~!>--<l.. !-++<l+?` .'   .           ;  ^<+<~-!~II+]>^-~_-?>]>i+,
                      .^i":I<!,;lIl";>i!~:>!Il;l:;ll>lI<<!,i:;;:!!lIli>::','''."",,^'.";:.;^"``,^'",;"^:'^":.
                        iI~+_,^l<l>"I!;I!^!!><l:^l<~>,"<il :.;l`!<!ili~~i"_!I!,~~_i<l!~?<^>i<l;i~,>+~_~~i~_<^
                        !_<i~.
                      ^:^,,,"",;;;;:"""""::;:;;::;;:"""""""""""":;;,"";
                      ;"l_[_i ;++]!i>^<:`}]_?<?]"                     i
                      ',>il;;::,::,::ll!i!;>lIIIlll;;IIIlll>!I;:";:;;l;'.. '  .   .   .'       . .
                        l<+,l<<~<+]_.>~+++i?;I?:?<~<i+!]]<:<+i>i.+>_]}!'I~:]_-+-+~<:_li?+,<~>_>[I!<-^
                        ;:"`^::^^","^``''`^'"".^^'`^^^'.''`'`.'`'.`"^`'`^``^^".^^^````^'^'^^^`'''..``^...'..
                       .!>_I+?+l~+!_I"i`~<<;,;:<-!i~i~_!~++<<l<~~!~<>_!>+<~~~~<l+-<_+!~_+l<??_;~!<!+]~;!?~>+.
                      ,,`;ll;`";::"";l:,",:;l"l;:;::;"'```^^"^`'``'''':
                      ;,i-]_!.l<~?!~[}-I!-]]-'_[+_~>]~....    ..  ....i
                      ;+><llIII!lIII;IIl><~<!IlIII;II!!>~<llIIIIIIIIIl!
                      ;`I+]_; I~+?!!~_---?<])!<[[~:~[_-<>[>           !
                      `,!l;,;;I;ll;::!l!!lI!;I;;ii>iIlI;;lII;;;:lll;I;;'. '' .   ..   '       . ..
                        ;>_:!<+~<_?~'~>~~~<-,!+:-i+~<-i_~>:~+i>I>-_[[<``+:_--<?-~_!l<l~~l!<<_~->l-~i
                        ;,".^^,^"",'.^^^^',`^^ .^'`` ^..,^ ."`'^`'. '`^`'`."^^'"^^^`..'.'`"^.^'^''`.^^' '''`
                        i<?"l<~i-ii-^<+_<!_+<+;:}+>_`+!"<_"l]<~~~i<`>-+>_<'+~?`!<]_~.>_.~~_i.!+>>~< <<<'li-<`
                       .~>ii+l>:`~~li'I!l+`;!!>>i+i`!;'ill>`<l_`,~><;"-<li<Iii+><,;~<~~>_~<:l~!>l-~"~><i<<i<^
                        >!i_:!<>>~i~>:<;!>!i!~~<!l~l<+"<_ii>llili>i:<!_~><~<<'`'''''`````^`''^'`'^^.^`^``^`^.
                      '":;;I"II,!I:l;^I,:Il;:::l,^;,Il,>+!!>;l;liI::lli:l:l;;.
                      l":i~>: ;>!i:l~_!ll><>!i!!~i"><i: ..           .:
                      lli>~<l,l!<+i~++<i<__-__~i--i_?-!"",:,"""""""",:l
                      l;;><iI"!>i>!i><>!>~~!:!!i!^""^"",,:::,,,,,,:;;;I
                      l";i<>, ;!<~;>+_il>_+l,!<+<.  .                .;
                      .^>!!,!>!i>ii!"<~_<ii~I_i:+_?_>_~-_>l~!i!!++---;:;^:I;:;,,;,":`!:^^"",,:,^;:"
                        ^,l^,;l!l!<; I;I:;,;`!;"<"Il,I^il:',:I"^iliil. !"li~l!~i>,II`ii",l:>!li,!il
                       'i^^^Iil.,I"I:,,"I;I,i,I.;l;^l:;,!";^Il;:^^:.;I,>>,:l;!,':,";I:,!l":';:'`",;`l!"^;;::.
                       'iI!<<~>Ii_!<<!il?<~i>?~ll><;~>>>-I<I!_><i;>l<<;+_!ii!<!>-iI!>_>_~><;i~lI>+_"!_I,~~!+^
                       '>i>~;ii>i>!IlIi;IIiil>i~,ii]i;+-I><;I;>>i;l~<!<!~<i;<i<><i;!<<<i>>!;!+l~!;i>+lli;><_^
                       '~ll>,><>~:_+-;l<>-!;-+<+_I+~+~>:i_+i+~_~~;
                        .  '. '.'..''....''.``.`'''.`''.''`'`````'










```

*Figure from page 27 (2346x3317 px)*
