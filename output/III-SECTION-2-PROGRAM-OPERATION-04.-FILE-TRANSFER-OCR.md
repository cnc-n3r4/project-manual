# III SECTION 2 PROGRAM OPERATION 04. FILE TRANSFER OCR

*Converted from PDF: III-SECTION-2-PROGRAM-OPERATION-04.-FILE-TRANSFER-OCR.PDF*

---


## 4. File Transfer

4203-E P-189



SECTION 2 PROGRAM OPERATION



This is the command to transfer a program, with the following sub commands:



Item Command Functions


#### Read READ

Registers a part program after reading it through the tape



reader.



Punch PUNCH Punches out the part program stored in the memory.


#### Verify VERIFY

Verifies the program in the memory with the program on



the paper tape.


#### Copy COPY Copies the program file on memory.

Forward FAST FORWARD Tape reader rapid forward feed motion


#### Rewind FAST REWIND Tape reader rewinding


#### PIP quit QUIT

Ends transfer mode and restores the program operation



mode.


#### Macro


#### MACRO LOADING

Copies files with extension .LIB from 3.5-inch floppy disk



program loading drive to MD1 :.


#### NOTICE


# I :

Never turn off power supply during the execution offiletransfer or file editing. If it is turned off,



the file contents will be unreliable.



4-1. Read



This is the operation to read a part program from program reading device such as tape reader and to store



it in the memory.



The following explanation is given assuming a taper reader.



(1) Set the program tape in the tape reader.



Set this portion rn the



tape reader.



oc><>Oooooooo ---------... --00 000000 -



Tape feed holes



~rogram



Tape feed



file name holes



(2) Press function key (F3J (PIP).



Program name (number) and



machining program



Tape feed holes



The functfon names on the screen wfll change to those given in item (3) below.



::PIP



DATE DIR



"PIP>" is displayed.



MULTI


#### PIP EDIT PIP LIST CONDENS [EXTEt,0]

Press [F3] (PIP).


```text


                                                                                               ."^"^`, "''^"'
                                                                          ....''..  . ''.....  :]]?-~_ i:l-{I
                                                                          +}-<>~+__I<.?_[~+--_][:<-~--?+!+~];
           ."^^^^`'```^```^^^^^``````````''''''''''''''...'..........''''.''''..''''''...'''.''`'`'.'.''''''.
           .^,::::,^'^''":^"^^^^``'^:;;;;,,,,,,,""";;;;:,::,,,,,,,,,,;;;;::,:::;;IIIIII;:,:,;IIIIIII:,,::,;I^
           '{`     ,|+[-,I1>~~>><}~~`
           ^]l     :~i[|l`?~1(_{}[({`
                 ..
                 :i~_;_!]+Ii~~+~_-_+<>i+_<-]_,<!~<__+]i'~??,-_<I+~<++~_;><_,<~~!>_<>]l
                   .^'`''' .''''^^^'`^'^`.'.' '`'':,""'.`^`.``^.^`^^^`;`^^^'^'''."'`^`
                  "_;;:;;~-<i:":;;;-III;!<!ii<<~<+::;"l;^""::;:;:;:::,"""":I;_<i>><lllIllllllll;::::;IIIIII;<.
                  :- '.'.i[_+,^^^^'_. ..l~~~_~??~_```^<!^`'''  ......`''''''.>i~<+]<>~`..      ...''''.   ''}^
                  ,]>I::;  ..`````'il>lIl:''... . ''``!_[---+?-~!~i?-~+?~?_-+ll]]+,>+-?-~<~<]i<<<[!++<!_+~:`]`
                  ,-i+~+;          Il_<i_;            "I>_]]_l^^'^""^.,^`l,"^`^,:: `:;,^;l^`"`^"I;.`^"'Il:. i'
                  "_l"::l:,,,,,"^``>;:;lIl!;"^^^^^^:;:i+]_+<_:^^",:;;:",,^``````"",,"``^^``:",,,",,^`'`''',:]'
                  "?~~_+-:''''````^>+<~-?_?I````'''''':<<i>~~_[Ii_~+-?l]{_>}+-}_]!;}[+_-i~l[+<!?]_---!'. '`'['
                  I-^"^,'````^"""",?":::,I,,"""""^^`^`I!<+~[~~l+>;ll!~<--!->-]+I<>><<~!i+]!i+i:i<>~<+~I!!^``}'
                  I_>-i_!          >l]~+_li`          ^!??l~?+!<~<_~>_:l;`:^,;:`;!I;Il:"!!^:ll:>;i_Ii,^l;   ?'
                  I];:"`^^^^^^^""",-::"",```^,,,,,,^^`i~~~;~--]~l]-+; . .`^^^'`^.  . .'^``^^'''.''.'`^^^^"^^-.
                  ;}~_}]:..'```'''`>~_-[~<..   . .. ''i~i>__-i<?+:?i_[-[<!{?I?_l_-_+-__`'`````'`````^^^^^^`'+.
                  :->>+_+~<:,,,^``^>i<-_il+~__~><i~~,"i<?+~!Ii!i<>i<-?++~ii!Iil<<++i+i_;:^'''^""""""`'''''^"?.
                  ,-><i+_>>`'''``^"<><_+I:!i<~]_-_-+"`II_[~>;+__-+;~]<<I~<<_-~>?]]_!++-__!^""^^`'````^^^^^^^[.
                  "]}?--<?;'`'''```<~-]?!;{{+]-?[~..`'II~_+>;_-?]+:+<+~!-><,...         ''````'''''''``^^^^^[.
                  l~";;:^:",::::::"_"",:,:I!llII;,^^^^l<___<!_+~~+l!<~~__>[~!:;;I::I;!!I:I;"",,,,:::;;I,,```}.
                  l-~_!:~>!        <i+>+!             ^<-!__I~<>~<+"l!i_i,<i>:__-<>_i>+~l_i-[_?i:]-_<?-~>.  -
                  !+^,`,;:"'```^^^"~";:^'..''.'```'`''li_+~]!..   .            .           .             .''_
                  I{[?_<i' .   ..."!;I;:;I:,^,;IlIlIl^~~>!<+_>?]_>i?}<!____-]_-;~-1!_<+i~~?<-~?I-<~~<I__[!,:?
                  l?__--_iI:!i!<;l.:_-+~>++I!!~_<>++_.l>-~-<+>!{}~iI:`^;,:,,;," ",;'",:^"":":::.,I!!i':;!'  ]
                  ^_~>--~<il<-?-_{!>::::"",,;;;;;;:;::!<+>~<<_>?-~<I"""^"::::,:;:,""",:;;::::::,^^^",:::":;;_
           illI!!>IIIl;: ;";:^^""";IIl>II;:,,,"":I;;I;;^'^^^^`^^"",,::,::","";;I;I;;;,,",::;:;II;:,,",",:;;I^
          .+"u|}??t[({"?.!.i-~>_;ii>;i+;>~~-II!--~>;-ii~_~-_!-+-+_[+~;]~[?!<]~--_:->]}i_?1<+]'<~<+>+~>--~>1~l
           i:l!!;l<~<>>!'; >+i;?>,i!<_i~~">_li<:l>i~i+<~i        . .     .  .   . .  . ... ."    . .' ''...:!
                         ;,!!!:!i;i><+~<~l<>I!>:i<<+<-++!""^"^^^",,,,,,"^^^^^^":,:,::^^^^^^^^:,:,,,"``````^I;
           "I`l    I_!;li`                                                     .. ..        ........... ....
           :i^!.   :<-~_+`
                 ;I"'''""^^,,,,l,,^,`",,,"^^",`^^^^^""":^"`'^`^^^^``^^^"'.^"`^''''`"'````'`.'''^^.'`'`'.''''
                 li+>+ii_<!]_~>?><;>Ii~_<i><_<;<!~]<_>l><<I>ii[~_~!!++<+<~~_<<>>!+++I+_!?[_I>_--];+_+i+;_-<+^
                 ;,i;-<,l<~>ii<.
                 ::^'^",`^^'.'"`^^``"``'`..`'''.''..``'...''''..'''''
                 l!_I<++<+<~+i~-+_<_->i,+I?+<+ll-__>+-<-l!>{_]I;-?_?~.
                   .   '  .'.             ' .          '
                  !<I "[]>~]+!-<--~-il[-?;<:__>!]+_;<?_--;
                                ..     .        ..
                      ''.''   ..
                      <]i<?i<_~->:Ii?;
                      >{?I+?]?".....^.
                      ^,""^"",^^^^""_'
                      `,'^^"^'`^"```+,^""""""^,"^^^^"^^^^"^",^^^^""^""^,^.,^^"^^^"^^^^":"^^^^^^^^`^`^"
                      !``'`'```''````..... .... '''''''''  ............I^;^...........''''''.'''''''^l
                      I,"","",,"":,,^`'`''''''':I,",","""^^''''''..''''l^I^.`... '.'.''",",,""":"^":';
                      ,,"^`^^^^^^`^^~,"^^"^^^"^i:^`````^`<!^^^```^,,,^": ;""^^"^"",,^^,~"^^^^^^^^^^"l:
                                    l  .       ,'''...'..I"   '`. .. .                'i .
                    '>~+;<~<;><<, ^l];l]~}?]<.^_;;_{-;__~~l^`'!<~]_+I!?+~l~ii~~!l~<"..">' """`"""^^""`
                     '::'^:"'",:` '"I"!}l<-<+'`!"I>+<`  .I,`'':i<+<+-i+>-~~i    ...'`^;i,.:<_Il<<;;<<l
                                                                     .  .
                  ";' ^l^""`,^"^;^^`""'"I:"'I:;"
                  <-" ,lI><;;i!l+i!,i+l!<ii:<i>!.
                      `!,"^:"",""'^,,,:, "^::` "":::^^::`:,""",^:';"""^',^^^'"';""'`I`^""`^'
                      'lli,<i<!ii:I~>i~>,<Il>i,<i>_~:l~!:<i~i[~:~,!i>~ii]i>l:>"~<i:l?Il-<i+I
                         ^                                                                   ,
                        'l                                                                   !
                        'I    ```.                                                           l
                        ';   ,+li.                                                           !
                        `l  I!;^^^""^^"^^^^,""^```^"^""""^^"^''`'`""^``````^^^"""^````````.  !
                        ^i .?' ..'`l;`'. '`i"`   '`i`'..'`:!I(+li^I!`'. .`i"..''''l^....     !
                        .! "'^<l!. :" :;i' I. !I!  l :>;; `i.+_~I ," ^,>: il!i!liI; ll;l!>; 'l
                         ^;~^;>;l' ""';Il' :`';II'.;':>I,.^l.";!^ ""'I;<:.l!<_++-<:'>~!i~}~:I'
                          "I^^:,:;l"`:I,";l^^l:,:lI`,I"^"I"^ll::;I^`I:"^;I^^:`^^,`^II""":'^`
                          l  >:-]>`<"+`]->"ilI>_~"!:i,]_-^~:<"?];;;;I<}[`<:<"+>~"~"!l?[i;!
                         ":  >;~!!"~,-,<_i,illi<-:>,i"ii<'>,<^!_!;I;I>~}"~;<"i!!^-,il<?!:i
                         l    ^'.'`   `.^^"  ^"I[;`,;!l:Ii:^iiI^"^  ""^`"` .,^",,. ^,"^^"
                        ,;;<>,,,!!_<~ii>.        :^ii<+i>i<>>>i^
                        ^::::,:,II!!l!ll`









```

*Figure from page 1 (2346x3317 px)*


---



(3) Press function key [F1] (READ).



=PIP



4203-E P-190



SECTION 2 PROGRAM OPERATION



[EXTOO]



®@@J@@J@@J@J



\ Press [F1] (READ)



The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.



PIP:READ R


#### PROGRAM OPERATION

PIP :READ



RII]



INDEX DISPLAY PR:lCEDURE



[F2] - Wl:*.MIN



[F3] - FDO:*.MIN



I 97/07/15 14:10:00



OVERWRITE



TO DISPLAY OTHER ltf)EXES, AFTER PRESSING [Fl] ,



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS [WRITE] KEY.


#### DEFAULT DEVICE NAME= Wl:


#### DEFAULT FILE NAME= *.MIN

>XR



l.01: FDO: COMMAND 01/ERWR/ CHAR.



INDEX INDEX INDEX HI STCflY INSERT DELETE CANCEL


```text


                                                                                              ^,",`"'':.^,"
                                                                         '`.'`... . .`'.......<?-}~_I,~,>{_.
                                                                        "}}~>+~~[l_^i_?__---?}<;+~]<-_~+~<+
          '``````^^``^^^^^``````````````````^````''''''''........'.....''''''.''''`'...'''''''''`.'''''''''
          ,::::::""::,"""","^^^^^^^``":,:,:,",","",,;;;;:,,,,,,,,:,,,,,:;;;;;;;;;;;;;;:::::::;;I;IIII;;;::,
                 !+. ;<lii:l;Il<!l:ii:Ii:l"~~!i~>^
                .Il' ^^;;!,,;,IlI;^l!I:,^;,IlI;lI"
                        ,                                                                   "`
                        <.                                                                  !:
                        l                                                                   ;"
                        ;    ~<~l                                                           :^
                        ;   "<`^'....'''''''''''''...''''''''    ....    ..''   ..........  ;^
                        ;  '"``'^^"l^`^`^^;l^`'`'`I;^'''",~,`i<+!`i`'>_~~;>,,+>>^;I^^^^``'  :^
                        l.   ;",`  ; :,:"'',^::`:^," ,;I` ;,:+[]<^l`;_[]<^I ">l> ;;',":,:"' I`
                        `l^.`}?{i .,^~?1_I'"!]?!iI:"'<?~: ;<?]1][<,!({l?]^; -_;I ;,,__~-1];,l
                         .",,^,^,;;,""^`"::,'`.`'^`^",^^::,`^'.'^'^'^^"",",,^^`^",,;""",^":"
                            '!I~<:!",!<+<;i`iI<>iIl`!l<<I!^;!<?~li.!;<<lI;^il><li^;!~++li.
                            ,i:?!":>~:+_].<l?'?>-.?Il;+[,Ii-`!-[ ?"+`-{+'-ll:><'>i>`-+( [`
                             Ili[;I'.;::I;: ";,:;l".I;:::I'^l;:II: :I:;II".l:",:l."l;;II:
                               .I:.__++l[<<i]?+_i
                                 '```""^^'"",:,,`
                     '^.  ... .. .                          .         .
                     ,i<!^?i<__^,-~+~-+i^_^<-+^?+-_-~_li]??~_>!!--___,_];;?_~<{__;;-<__~:!_~!I_-,?-?~__~~;-.
                     ;?~~_+>~<;_;_~il->_+~:  .   ....'. .... .  .....  . .`'..... .'..'' .''. .' .'''''`,.`
                     ^:::,I:,^`:`^^"`"^,:"`
                     <<_I~]<~]l<>?]
                     . . .''.'''.^^   .     ...''....'...........'''''.........''''..
                            ",:Il>!ill;!ii!ii>lI;,,,:;:::;;;;;IIII;;;:"",,,"",,;;;:,;::.
                           "I ':>)(){)l1{1{_]1;"^""""",:,"""""""""^^,I!!i>;;:"::I;!!+.`l
                           l, `":;;`!<~l'``^^"":;:::;;;:"""""","^^^^,i_++-~11?t]1}]}+. ;.
                           l; II_t1;?{}+","",,,:;;;;:,,""""""",,:::,"^`^^`!?](\]_-^^<. ;.
                           I: ;"^~l                                               . l. ;.
                           :" :"                                                    !. ;.
                           :^ ;:.   .      .  ... .````'''''''''''''''.........'''''>. ;.
                           :^ .^^>~~:lI>llI,~<~_<-~,,""^^^^^^^^"""""""^^^^^^^^^""""""  ;.
                           :^   ;((+,>>n_~<i{1illiI                                    "
                           :^   i?]:'l^|[l!-]_        ...                              l
                           :^   ;}<-<]_-I-_}|,I/\[]-._][}l?|}-_(>.[?>"' ^^'`` '`.      <.
                           :^   ,\1[;;{]_[-!_!f/(,)/;;I+;>])>.<_?,~[?-`.-}Ii<`+_;      >.
                           :^   ~t[[_<:1-<>+1x}I'^|]?l'                                >.
                           :^   "I";,`''^, l>I `  ."lI'                                >.
                           :^                                                          >.
                           ;^    .                                                     !
                           :^                                                          l
                           "`  .l+                                                     i.
                           ^'  :<!'..    ...    ..                   .  ....           l
                           :' `;^'^"Ii_]l"";l><;`';!>-_<+<~__?_;!ii>"'">"""^`:;"""""^  ;
                           :,   lil^.I!]+>;"::[-I,"~-|){}+l_1\\~l>)}>I;!^III"`"        l
                            ;:^`<_~I^l :-?~:" l~~i"I:;:>Il.^<+~!:`+><<l";~+<!`^.... '^;^
                             '`;,:;l:"!I::I"^l,,";^^;:,,:'"I",;:`,:""""`",,:;:`;;::l,^.
                              ,ll+>'~II~-~^i>:_++,!!,~?iIl>"_};I"i:]}"!Iil-+"<IIi}{^-
                              "!lll:!:!i<>:lIl!!>;;IIlill:!;l<lI^!I>_l!,!;lI"i,!li~,<.
                                ...'  .....  ... .  .. ..  .. ..  '. '   ...'  ..  '





























```

*Figure from page 2 (2346x3317 px)*


---



4203-E P-191



SECTION 2 PROGRAM OPERATION



(4) Enter the file name of the file to be punch and press the WRITE key.



Example: TESTS.MIN


#### PROGRAM OPERATION

197/07/15 14:10:00



PIP :READ



R TEST9. Ml NII]



INDEX DISPLAY ~IJlE



[F2] - MD1:*.MIN



[F3] .... FOO:*.MIN



TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl) .



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS



DEFAULT DEVICE NAME = MD1:



DEFAULT FILE NAME= *.MIN



>XR



OVERWRITE



[WRITE]



KEY.



INDEX



tl>l:



INDEX



FOO: COMMAND OVERWR/ CHAR.



INDEX



HI STORY



INSERT DELETE CANCEL



@J @J @J @ @J @ @J @



.._WR_I_TE_,



Pressing this key starts the tape reader. The commands on the tape are read and stored in memory.



While the tape is being read, the screen displays "READ" along with the "file name" on the first line.



When the first EOB code appears after the start of the tape reading-in, the message "VALID



INFORMATION READING" is displayed.



At the completion of the tape reading-in, the tape is then rewound and read in the reverse order to



verify the read and stored program against the program on the tape.



When the tape reading-in and verification is completed, ">" appears on the console line.


```text


                                                                                               .,,""^, :'`"^
                                                                          ''''`'''... `'....'..:?-_-<_.~:i]<'
                                                                          -[+<<>~-_!>`_-?<_--?[],<-+_+_~~~<?:
           .```^^^^^^^^^^^^^^``````^^^^^^^^^`''``````'''`'''''''````'.''.'''''..''''''..''''.''''`'.`'`'.'''.
           ',,,:::,",::","^,"^`"`^,""""",","^"`":":,^"^^"^^"^^^":,,,,^^^"^^`^^""^^^;;;;;;;;::::,::;I;I;::,::'
                  ,+; .-l<+,li!:-l^!!I>;,!Ii!,>!"i^l!"lIlIi`iIl:;Ill"ll;,<><l<!"!I,
                  "I, .:^^;''^:`I;':I";"^^^"I^:l^l";!:!l;I;^i;IIlI!i,:;I^!;I:;;"i!l
                      `?!+><~~l  l-~~l<l-]_i
                       ^^:"^:"^  .^"^'"^""^^
                               ...           .. ..........       ..
                       .::;IilllI;;;;;!IlI;;::::,,,,,,:;;;,:::::,:;;::::,,,,,,,;:,.
                      .I'.;;{)11|<_1))~<(<::,",,,""""""""""":,"",:;IlIlI:;;;:,:!`'l.
                      `l  ,:;l^,!l;^`^^""""",,,:::,"""""""^^",,^l_]~]~-}i(?]1])<^ l,
                      `l 'Ii]1~]j)/!ii:::::::,",""""""""":::",,""""""l11(n1~{I,>^ I"
                      `l ':";"?~>;->]-`........         .............'... .  ..l^ I,
                      ^l ':                                                    :^ ;^
                      ^I 'I..   . . . .       ....      ....                   "' :`
                      ^I  ::;ll;:;I!ll,iiI!l!>,,,^^^^^^^",,,"^^^^^^"","^^^^^^^^"  :`
                      ^I   .?t)l>!|}>-"]1-~~?_.                                   ,`
                      ^I   ^?[~ I'1|!!!|]!                                        :`
                      ^I   `]i+I}i~<i?-\<I~_++< ;_<-:l{++l-i :iI'                 ,`
                      ^I   .-{]!l{};1]~]I~txi-jiI<~~!)j?,!1(I~1}], -(~~-,i-l.     :`
                      ^I   :({[}<^]{-_[<f|1""}|<:..  '.    .. ..'  ''..'..'.      :`
                      ^I   `~>>~I';,i^<}1',  ,,+i:                                ,`
                      ^l                                                          :`        .::,,::.
                      ^;                                                          :`        ;,.`".,I
                      '^                                                          ,'        I";<;:;I
                      '^   ':'                                                    l^        I^i{,;>"
                      `:  .i-"                                                    >"        ,:,"l"':
                      '^ ."; '^^::l:,",;;I:"`"::;:,,",:::;";;::"^^:^^"",:;,,^^^^. !^     ~?[:])i!?^:
                      `:   .""^ ,i\i;``Ii[_,`'l]tt{1I!}}1t<~+{)i^^i'`^^`^<......  l`   '>!<?:;`^^^I,
                       I"' l}[< : .-[+;, ,]]-`,>i~_~;.`-]]ii'?_~<<:;-}-<`!      .^I    ^^ ,  '`'''.
                        ^^;:`^"^^:"`^"``,^`^"`^"^`"^^":`^"``^^^`""""^`^"^^:;::;",^
                         "l!+I:I;l_-iI:lI~~lI:;;_+;!:!;?-;!^il+_:I"!!~<;l"I!<~:l
                         !!>>;"<~l~->,i~;<~iI!l:~-:>i<:_["<;<l-}^>!il>i^<II>+]"_
                          '..'^  ^`''^  `..''  `. `.  ' `,' .`..`  ''.'^  `^^'`
                      :_i~<~li!-<l!~<,<~i_l_<!>>!i:<<>_<.:>>l:ll!l!iI+!:>;~iIi>!ll<>:ii<;!!!:<>!i!I;:!i!!ll;
                      ''^,,,^;,^^``:;^^,"^^""^^I:"',,,:" .'^^^"^":,;,::,;'",^,l;",;:`I;I^:,,`Il,;:^^^,;,:::;
                      "]+!~I_~ii?~<:<!<~><Ii~<i'<>Ii<!<~l;-~__~<l"_}>~~I^+ii<I!~?:+>l"?<:I<>!>'llI+>;<!>!>i:
                      .""'```,``:,^`,",:^:"`"^`''``^"`","'^,I^::^ `"`",..,"`:"""^.^"^ ",`^:^^" ^^'^^'":,"":,
                      "?~i+l"-~^;i-;l<i};^<i->^-<~~+<l._~_:;__^l-?>'>Il_~`>?~+.i_--+>>i! <~+.l<+<<~?- l~]I<~'
                      "_]+<__?_+~+_[I+{<_+-[-?;i~I]_~-+~>i. .....'. ' ..'..^`' .'`''^".'..'`..'`'`^:^  '''''
                      .""'```"^`'`^^'',"",`"^^ '"'"::";:,"
                      "_,+il"!>i<~-+!;^~l+i,<~<;:<><<ii;; <~i,_~<,~:~<~,;><i!I!l:!l~!+~+IiI~+II~i<i+!;>~]!l<.
                      ">>~-;?~!l-~+l+>~l+<<>~>~ii_~-~l]<+<i~i~_<>ii>>~~:I<I+<!l~i~"^`"""'`'`,^`,^"^:^`"":^'"
                      '::"l'::`^:::'I",'I:";:',";<"I:';i!;,;';:^:,">:;"^,:`,,^`!ll'
                      :-+i>I;ii"<i>;;<!<>!l:;,+!!"!l+<I~<l::!^lll>!i>!i.,"`i!!ll!;^!;I<>"I!iili;:li,
                      ."^":``":':;:^^:::,:l`^^I,"^:,,":;:,^":^::,i:;;;;.`^ l!i;ll:^;"":I^:;;I;;:^:I"


































```

*Figure from page 3 (2346x3317 px)*


---



4203-E P-192



SECTION 2 PROGRAM OPERATION



[Supplement} Tape rewinding with or withouttape verification is selectable by setting bits 4 and 5 of NC



optional parameter (bit) No. 1.


#### PROGRAM OPERATION TRANSFER READ

TEST9.MIN



file exist overwrite? (Y/N) !Y



varid information reading



TEST9.MINI



97/07/15 14:10:00



PIP



QUIT [EXTEND]



(5) Press function key [F7] {PIP QUIT).



TEST9.MIN



file exist overwrite? (Y/N) !Y



varid information reading



FAST FAST PIP



READ PUNCH VER IF Y COPY FORWARD REW IN D OU tT [EXTEND]



The screen returns to the one displayed in item (1). Details and precautions on this operation are



given in 4-3-1. "Precautions for Tape Reading-in, Punching-out, and Verifying Operations". Be sure



to read this item.



[Supplement] If an error occurs during tape reading, 31 characters preceding the error character are



displayed on the console line of display screen.


```text


                                                                                               ^""^`: :^.^"'
                                                                         ....''... . ''.....  "---?>}.~!I_{!
                                                                         >{-<>~~-];+.-_[~+[?-?};!?+-<?~~+<]!
           ``````^^^^^^`````'''```^````'''''''''''````''''''''''''''''.'''```'.`''``'..'`'`'''^'`'.`'``''`''
          .,,:::,"""""^^^^^`","::,",,,"^^^^^^"^^`^,::"^"^^"""^",",",,"""":::,,:,,:,::,:^^^^"":,:::::::::^^^`
                :_li!i>!l!l+'   ^>ll;:lI!:il;";li":":i<;;;;lII,,!I~Ili;I";";l!:llI!,;:^I!i:;,Ii,,";::I,:Ill,
                ,I;i!Il;:l:i'   "~?_<i_<>i+>++<~<;_i~~?>!<Ii<!:;iI!!>il!:!:>><li<!<lI~;~<<;_!i~!;;<lllIi;!i:
                                :_>!i!_,!+!>Ii~+!`_+>^+<.^^
                              '`' ..   '       ..'..''  '  .'...''`^^`'''''```''.....''
                             :,:;>-+___I++-_<~-lI;;;:I<~_~++!+~>:,,;:::::,^"^:<i>!l!ll,;'
                            :, ^:>][{1)l]-{[i_{:""":;!])(?]]i{)?""""""I<i<~lii{\{))//~ 'l
                            ;'                                       .I+>~+>_>;+:<+_?l  ;
                            :`                                                          ;
                            :`                                                          ;
                            ;`                                                          ;
                            :'                                                          !
                            ^.                                                          i
                            ^.                                                          l
                            ,'                                                          "
                            ".                                                          :
                            ^.                                                          !
                            ;'                                                          l
                            I'                                                          !
                            I'                                                          !
                            I'  .^'`..'.                                                l
                            I'  :]-~!-<+  '``'.`   ``:^ ^'                              !
                            :.  ^iii!~>]I+}-??^_+>;~><; :`                              l
                            ,.  ;>,"".;;;!i",I':><:!;  .       .                        ;
                            I' `"..'^:l`. '^;;"```^!,^''^"l!<>,^";I!>:':l;ll:^;;``^^''  ,
                            ;^  ,<l: `;^!<!^,,Ii:l,, ^!>" !~[{!;"^>1{l!,:.<>; :,:;;;l;` ;
                            .;,`;+<l.^,"<_<,",!>ll;,'I_~;'II!--+i"l<>![,".~!I'""i<i<]-l:^
                              '^:^^";``:^`":`^,^,;;";;,"I:'",``:^`""^^"^`;",:;^'"^``"'`.
                               :,+-l:!l:-[!;I<;-_;l:I;??"i;iI{]"i"!>{-">;I>_~"!II+[+,>
                               :Ii!lIllI!~ll;>;i>Il:l;i+:i:i;i~,i"!i+-:i;l!!l,!;li_-:<
                                .....  .  ..  .  .   ''.'. .'. '  .'''`  ''''`  ```'`
                 `:`  ;"^^^^"^`:^`.```.:",.";;^'"`^:'
                 l?l '!i++<:+>i-<>:i+-,_;~;+<];l-~i!!


                            '`     .                                                    ".
                            ",  '-+<!~_!'           .`' .'                              ;.
                            ,,  'il~l+i-lI?_i-,i~;I;><> ,:                              ".
                            :,  `>;,I.;l;l~,,!^,<>IIi                                   ;.
                            :, ',^'``";`'..`",`'..'"""``^"Il!i:``,:II;`";"lI:^",^`^``'  ,.
                            ",  .I,"  !.;;;`.""I,:,"`.:I" !~[1!,,";}}l:^; +~l'':',",:,' ;.
                             :"`"-+>.';`<-~;`"!+i!I,^^~+I.;!i_?-+:;?_I};,.iiI^'":+>>?-l,,
                              '^^'.'"`'^`'."`'`'''^'^,''^"`'^'.````^'`^^`^^``"^`^`''^'^'
                               .Il~l"!"l!+~;I;li<>;;,;~_l;,l;~]l!^lI__Il"l;i<:!^II++:i
                               ^!!~i^_l!!__"<<!>>~,>l:~?>I!<;<]I!;<:~}Ii!<;~>^<lil_{"?^
                      .         ``'^"  `^^`^  ^`'.`  `''^^  `..`` ."' '' ."'`^' '^''".
                     .<!<">l>~<;"+_;;<;!";!l^ilI,_!>~iIll:I:~ll":!. !i>i_l">Il:ll;!Ilil!:^!,i!l`llil>!;::>l`
                     .!!<!!>;<!>:l;->~i<i><i!!~<:~__~_{~<i+l<!<"~>I;>_~<ii!_:i<~~~_+-~~>!<>l>>_l~++;<]iI!~~"
                     "[IiiIi;il!;:'l:l!>>!!;!;;l'"~<i^i><i>;+:i^;;>!liIil;!!`il>:l<!i<I<lli>>i<>I!I "_!l>!>^
                     ^+"l~+!!~+;!->!
                ''     .   .    '    .. .    .    .  .       ..  ... .
                +]-[[-+>?<_]   .+I_;i<;>,!<>i~>;+ll>>I]~~:!<~+i+l^_";>~>~__+>li~_~-+?~+i]_;_><>:]+?~+~?!!-~"
                . ...      .   .<+~~_>>~;i~;++;l<<~i]i>]>I!_I]<_]+;l<><~<^.'..'.''`'''".'`.`.'..''^'`'^.'^`.
                                ""::;;,:`",'^;^^,,:,,,`,"^""`;;;:!"";,::".
























```

*Figure from page 4 (2346x3317 px)*


---


### 4-2. Punching Out Stored Program Data

4203-E P-193



SECTION 2 PROGRAM OPERATION



This is the function to punch out the program data stored in the memory.



The procedure is as follows:



(1) Press function key [F3] (PIP).



The function names on the screen will change to those given in item (2) below.



=PIP



DATE DIR



"PIP>" is displayed.



WLTI



PIP EDIT PIP LIST



COtl>ENS [EXTEND]



Press [F3] (PIP).



(2) Press function key [F2] (PUNCH).



=XP



FAST RAST PIP



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEtl>]



Press [F2] UNCH).


```text


                                                                                               ^^^"'".':.^"^
                                                                          .'.''..'   .''...... <?-]!-I"~,<[-.
                                                                         ^][+ii+~[i<"!_-++_?__]i;-+_~-->~++_.
           '``````^^^^^^^^```````^`^^^^^^^^^```````''''`''''''''''...'''''''''.''.'''...''`''''''`.'`''''`''
           '`^^"",:","""""^^`"^^^^,"""""",""^^`^,"""^^`^^"",,",;;;,,,;;;;;;;;;;;::::::;III;I;;:::::,,;IIII;:
           >Il!    ~>:l!>i!li"i<!>"?ill!>;~-I!lll!!"i>i<i^
           ;:;:    "`I:lI:I;]^:Iil'<llIli::";i_ii>l^I!<<~"
                .>il":"Il:,I";l;:^l'":",,^`:,,!,'",,::"".;ll:^l;:::":"!:`,:::""".
                 ^"I,:",;;`I,IIII`l,;l::;^:il;>>;<!i-i>l,i~>!;<ili!:!;~<:I<~ii!~"
                .>!!^!lll!>li:;l"+";>>Ii!^
                 ^^;"l",::";,^^:`!^`:::;:.
                  ::. Ii:;;^:;::!^,^:;`"i!!^<i<;.
                 'll^ ;:;!>,"i:!!I:`l>;:ll<"I;l:
                      "!l;:ll;<;;':!;:I;';`!!;`l;llI,:ii^!ll;ll"I^i;:l;"!:I:^I^l;;^"i^:;l:;`
                      '"II"llI!Il^:il;!l^l^;Il"i;l!I";iI"ll!I?i^!"lll<l!+l<l"!"i<l,I~,I<>i~,

                        "I                                                                  .l
                        "!                                                                  '>
                        ^I   'i:I'                                                          .l
                        `;   :>":.                                                          .I
                        `,  ?!:,"",ll::::::l,"^^^""I:,,""",:";,:l:ll,""^"";:::::"^I,,"^^^^. .;
                        `; ^<..''  ;, '.'  l' '.' .! .... ";;f-ii.!l.  .. l^..... ~'.       .!
                         l^l I[i~' :^ ~>_. I .<<!  : <[;; ^;Ii!;  :^.;I[! ;>_1)]}+; --~_][i.;:
                          I~,,"^```^"^"""""::^'''`'^`":""","'``'`^""`^`^`'",,"""",:";;:":II;"
                          ;'.^!!iil;.,ll!i!:'l;ll;l'"!Il;lI.IIlil!^'!;;;;l'^!l!lIl`llIll!^.
                         `l  >,<?> >I_.}-+ ~I!:_~:I<>`]-[ ~;?'[{>`<;lI-),I<>^->_ -I<`_{_^?
                         l'  ,!!Il;!`lll!iI;`ili[I!^";;;!:I.l:;;l;:`!ll<l!":lII!;>^!li<!I!
                        'I'``  ...'   ..  .   .`~:.;i><l<~i;<_i'     .. .   . ..'   .....
                        I,i_-l!i~<]?-]--`        "":l><!lIilIlI,
                        .'.  '''''.''''..

                 ^]-. ~<__-l-<~_~~!l__I-_?I>]>?[-~-i
                 .`'  . '``.'`'`'`..`"`` ^'^.'''`'`^
                        `                                                                   ``
                        :'                                                                  I;
                        I'    ``                                                            I;
                        ;'   l[<                                                            I;
                        l` .^!`'```^`^""""""``````^""""""^```'..`^`''' .'''''...`^``''''``  I;
                        l'  '    ''~'.. .',i.  ...;l^`''`^I^.>+-i'!` l{?_:;`'i<_:;>^....''  ::
                        :;   <>~!  > !!~!: :^<>:!:`^ l~<: ;!i])[-I:`>-?_-'` ,<i< ';.!lll<l: I^
                         :;"^l!il..,`;!~i;^,:>!;;,'`^li;"."l>>+>~!,"<~I!<`^'l~I;'`:"<>l<-_i::
                           `^.',^,::`.,,,:l;`':^"";^^:,^^::'':,:","'',,,^;^`",":;:'`,""'"^'.
                             .>:[~:,!I!l++"i,~,-<~"i,i;??Il;l:<?]^<'~,_]+"~,>l_i;ll;;~~],<.
                             '<:~;:,>lil<]">:<"~!<`i,!,l+:Ili:>>]"<^~"<_]^_;<I<!^l>!:~>}`+`
                              '"'^^"  ""![:`^:!l;i>"^lIl:;;  ,""^,` ',``":. ^,"^",  ,""^:'
                                         .;,<~~-i~+~+><?-++'
                                           .



































```

*Figure from page 5 (2346x3317 px)*


---



4203-E P-194


#### SECTION 2 PROGRAM OPERATION

The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.


#### PIP:PUNCH P


#### PROGRAM OPERATION

197/07/15 14:10:00



PIP :PUNCH



Pll]



IN:lEX DISPLAY PROCEDlRE



[F2] - MDl:*.MIN



[F3] - FD0:*.MIN



TO DISPLAY OTliER INDEXES, AFTER PRESSING [Fl) ,



OVERWRITE



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS [WRITE) KEY.



DEFAULT DEVICE NAME = MD1:



DEFAULT FILE NAME = *.MIN


#### K>l : FOO:

COMMAND OVERWR/ CHAR.



J tflEX INDEX INDEX



HI STORY INSERT DELETE CANCEL



@ @J @J


# CED

@J @J@@



(3) Enter the file name of the file to be punch and press the WRITE key.


#### Example: BOX-1350.MIN

This step is unnecessary for a program without a file name, i.e., A.MIN.


#### PROGRAM <PERATION

I 97/07/15 14:10:00



PIP :PUNCH


#### P BOX-1350.MIN[I]

INDEX DISPLAY PROCEDURE



[F2] _,. MD1:*.MIN



[F3] _,. FDO:*.MIN



TO DISPLAY OTHER l~ES. AFTER PRESSING [Fl] ,


#### INPUT THE DEVICE NME AND FILE NAME. THEN PRESS

DEFAULT DEVICE



NAME= Jl.l1:


#### DEFAULT FILE NAY:= *.MIN

>XP



wn:



FOO: COMMAND OVERWR/ CHAR.



OVERWRITE



[WRITE] KEY.



ltllEX INDEX INDEX HISTORY INSERT DELETE CANCEL



.,_WR_I_TE...,


```text


                                                                                               ^"""'"'':.^^^
                                                                          ''..'..' . .'....... ~?_[i-I,~,~]_.
                                                                         "][<i>+~]i~^l~?____-+}>;_~_+_-<<~-+.
           ``'''```````^^^^^^^^^`'```^^^^`^````'``````'''````````````'.''''`''''`''''..'''`'''`'``.``'``'`'`
           """""",""""","":"""""""^^^"""":"""^^"^`^,,,^^^^,,,,:,:,,,,^"^`":,,,,"",::""""^,::::::::"^^",:::;"
                      `>ll !;Ii!"'il!Ilil.i`I+!'!>!I!II,:!!!;>:;"llll!"l<"'l;lI>i;:`l:III``;::"!;`I;I,II;,.I.
                      ^<<~l+i>->l:_+_!]~~I~;"ll';;IIIIl;:il!I!;:"lii!l^:i,^<!il<il:"<Il>!^:ilI"!i";i!l<!i+`<'
                      ^>>~i<>lI^I`;!I^<I!+l;
                      :ll;;l:>ill^!"<"
                      ,:I";:li<Il";"]:
                                 . .    .    . .''''''''''....'`''''''''''''````.......
                             ';,I;_?+__<i--_~<+>:;,;:::::::;;;:::,::::,:,"""::;;;I;;:l:;,
                             l. ;"-{[?{<l?}{+>}_,"^"",^^^^^"""^","^^^^:!>l>!I!";l;iI<>, ;,
                             !  :;ii:;<_?<^'`^^`""^"","",,,"""""""",;:i+_>_<>\[|x1)\1~: ^:
                             !  i;[f~l~]?~;;;;;;::"::"""""",::::""""""^^`^^":~--[~I-:l; '`
                             !  I ^i"                                                ": `^
                             !  :                                                    `, ^,
                             ,  ,'.  .'...''`'.... .''''''''````''''''''''''`'...'''':" ^,
                             ,  '`;_~>:i!>I~:<_~-+-[:```````^"""^`````````^""^```^""":' ^,
                             l    -)1I;l{|l_:]}[!!i>'                                   ^,
                             l    --_ ;^<\<l!1_<                                        ^,
                             l    ?+->?]_~![_)_^}([[]",{![<l[[?~]}.:?<<'..'..'. ..      ^,
                             l    >([+"_}I}{~-+<\\>>n_">!]:[{[^"_{>i}}}i !)~I_I;]>`     `"
                             l   ')([\_,~1-~{<r(].^_\+;^                                '`
                             !   .>!l<l^^^<,;-["'' '^>ll                                ",
                             ;                                                          ,:
                             ^    .                                                     :;
                             :                                                          :;
                            .>   'i"                                                    ,,
                             l  .!~"       .                                            ,:
                             ,  :; ''"!!]!;^`;I~l^'^;i+_<+ii~>i~I"!!>!""!:`'''^I":::""' ,:
                             I   'ii! :,]-~I^I^+[i;`!+{(1\<I<)(t[:l]1~::l":;;; I        ;,
                             ^;"':_-~^;' >-~;: '<+<,Ill;<<;^ >~>I;.>~ii<;">-~~":     .`,;
                               `Il;;I;"!l:,;"^!I:,;^"llIII`,l;::;`;l::;:`:;;IlI^;I;:!:"`
                               ^ll_<'~ll!?_^ii:++<,i!,~-lIli"[1:l,i;{{:!I>:-_"iIl!]{^?
                               `i!l>II,!I!iI::lll!l::ll!ll"II!<ll^lI!<;l"ll!!;!"l;l<:<.
                                                                                    .
                 'il  !;!i:,il"lI^,I;;;`l,!I^lI`:^,I^"^,"l`",:^":,:":l,^IIl:II',,`
                 ^i!  l:l>:`Ii"l!`,>l!!`l^li":~;!;l-Iiii!<^>!~I~><~!!_+,<><!l_^<__'
                      !llllliI. ;-!iI`l~<l!+>i
                      ""::,:::. "I":".";I":l,:
                      ;!I:`I;:`I`^,,:::::;"^^I,^:";,;;;I^"I!:,:,""!l^"::,,.^,' I^li!^
                      ";i!,>i~^!:lIlilii><li:>I"il!I-<<i"I<il!<;l;!~:;~>!<^:>,`<;++~;

                        ..'  . ...... ...'...'..'''........................... .
                      ':,lIi!!!!ll>><il!I::::::::;;:::::,:::::::"""";II;:,"":;l::`
                      I' l:}{)1(_~1])?~)~",""",;:""""""",,",""",;lI!I;I";,;I,Ii".l^
                     .:  ,,;l,,><>l^'''^""""""","""",:"""""""::l~]~[+~)<)(?}}{~, ":
                     .; .ii}]}][tr1i+<_i"""""""""""",,,""",:;:,"^^^^^;[){f[<}:>: ",
                     .; ."^""_i'"!;l~i?!                                     .;: ,:
                     .; .,                                                    ", II
                      , .l..   . . ..'.      ............................   .."^ ;;
                     ."  ^^;!il:l;!l>:!>i<ii<,^^^^^""""^^^^^^^^^^^^^^^"::"^^"":. :,
                     .;    -){lI>)1i-,]1-+<<+'                                   ,"
                     .;   .~-_ l']|<ll1[i                                        ,"
                     .;   .]>?~]~+_i][\~"?1-__`:]![ll]--!-+ :~!:.                ,"
                     .;    -)}-;?}I[{~]!~tu+>x-;i!-!}\["i[(ii{[]l _|i>?"l{>.     ,"
                     .;   ,t[}(?"-1?_)~x/}^^[\+I'                 ... . .'.      ,"
                     .:   ^+!!~l'",<,i?{'^. ^"+i;                                :"
                     ';                                                          ,^
                     `l    .                                                     ,^         ^,"","'
                     ."                                                          ,^        ^<'`"``i
                     ':   '!^                                                    ,^        ^!'!;,'~
                     `I  .!~^                                                    ,^        ^;;|<"i<
                     `I .": '`"II~;,^">>+!"^";li!Il;!il!!:IIII:^^;^^^^^:l:"""^,' ,^        'l.^:" !
                     'l   `I:, Il{~l"`il}]:"'I-(t1)!l?[|\~i>{{>,^I'^"^`.l .      ,`     "_-l~\+;-,l
                      ::`.!}?~.;  -?~;; ^?_~";!!>+>, `+_~!I.~<~_+":~[_~':      ."I     ;<>1>i"^^""i
                       '^:;^,::`:I,";"`;:"":^^;I;,:^";"":,^":""""^",^"::^,l;";:,"     .l "^ `^`^^`.
                        .!l]<^>;i!]-:;;l<_+,>l;<->;!l:+]l!:!;-]ll:i:_+;!:!;~]:<'
                        'il<I"<I<!__,;;l!!+:>II!>iI!lI<_il:i;<_ll;>;~i^i;i:!?"_^
                         .`''^. .`''^. '''`^  `'''`  ^``^`  ^'.`` .^```' '`'.^.











```

*Figure from page 6 (2346x3317 px)*


---



4203-E P-195



SECTION 2 PROGRAM OPERATION



This starts the tape punching out operation, during which the screen displays "PUNCH" along with



the "filename".



When tape punching-out is completed, the message "file-end" is given on the console line and ">"



appears in the following line.



>P BOX-1350.MIN



file end



FAST RAST PIP



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



(4) Press function key [F7] (PIP QUJTI,



>P BOX-1350.MIN



file end



[EXTEM>)



@J@J@)@@®~@



Press {F7] (PIP QUIT)



This completes the tape punching out operation and the display returns to the mode as in step (1 ).



[Supplement] 1. That tape punching speed will be slowed down while machine operation is carried



out simultaneously.


## 2. Tape Punching Out Format

Feed holes File name Feed holes



(1) (2) (3) (4)



1-----..::.--1 Program name



Machining program



(5)



(1) 600 tape feed holes are punched in the tape leader section.



Feed holes



{6}



The number of feed holes to be punched out can range, as needed, from 1 to 10000 with a



parameter.



For details, refer to IV "PARAMETER", Section 4, 5. "NC Optional Parameter (Word)".



(2) The file name is punched out following the "$" code. (Program data is punched out in the ISO



coding system.)



(3) 50 tape feed holes are punched out.



The number of the tape feed holes cannot be changed.


```text


                                                                                               .,,""^: ,``":'
                                                                          .''.''.'. . ''.......;]-??~-.~I!?1:
                                                                          ~[_>>>~_+!>`_-]~___-]],>-~-_-+>_~?!
           .^^^^^`''''````^^^^^^^^^```````````````````'''```'`````''`'.''''''`''`''``'..'''`'''`'`'.`.''''``'
           ':::::,"",","^^,,"""","",^``^^^",,,,,:,",:^``^",,::,:,,,,,"^^^^,,:,:,",:,,,"^"^,^",,,:::;,"^""^",`
                       I!l:^!l!l,iI,>>i:I!;;lill";!l,!!I!+Il'^!,;;;^!>;i";l;"l:llI^l!I!!;l`iiI!!lI;'l;;:":li^
                      .>>>!__+i+!>~;l>!:l!;;;II>;;i;:>!I!<lI",!I:I<"iIl!":ll:i:!>I"!i<i<<>^:;il!lI"^+!l~<!>>,
                      .!iI ><I;<;!,
                       ll:;^';:"`"":,I;::^:,,;^":;:;II:I^I:,^::,,,";^;i:`,";:"^^;":^',^,:"'""""""^;^"`"",^'``
                       <<!~!;__+l?~i<~+i]l<iI+!li!<<~<<~:i>>;<+>><?[:,+~;~l~,Il<?i+;"<:l<<:<>>~>~I+i~I+><`:,'
                       ~]_~~+i,<,<+Il+_!++>+;l_l
                        ..                 '
                         !                                                                   I'
                         !   '!^',".'^:^'"^`                                                 >`
                         !   '?l>1{~<_]>!]<i                                                 >`
                         !   .I^>,;~<'                                                       >`
                         !  .,l`^`^^"","^^^^^`^``^`^^^""""""^^`''`^^",^```^^`^`^^"""""`^^"`  i'
                         !  ..    '^!'     ;;      l"'.  ''i .<+-!.l. +{?>,;'`++<^!:`. .     ;.
                         l^  .-~-: ."`+-?<"""!-<>+:,.'<?-" ;i+{\[?l"l[{_[<`" <~i! ,.:~>!+->` !
                         .;:^^i><:.`,^I~<!"^^;iII;""''I!;^';:!>~i!I^;_+I>l^^ >>"".,':>l:>-~I;^
                           '^^I:,;!I^,!::;!,'::::;I^"l,:;iI^:;^`":``;,":I:`^l^"";,`;I,^:l```
                             !;i~~.>:~^-_+`<l>I--Il!:"_<?'~,<^?[l"!:!I-}:l;i"_<_`_:i"_[<,<
                             l!!I>">:<:><<:i;<Ii<I!l;;<i+^~,<:i~i:!,ili+,!:!:<l!"_:>;<?i:<
                              `'.'^.  ^'.''  .'''''  ^'`.^. .^`'`^  ``'.``  "^^^". '"^``"
                  '"' .:^^^'^^''^'..^'..,`" :,^`'^.":.
                  I_l ^><-]+!-><-<<;~++!?;<,]>~;!?>>~!.

                         l                                                                   l.
                         >   `!`',"..":^'"^'                                                 <'
                         ~   `]I~{}<i--i!?<l                                                 i.
                         i   ';'!^I~~                                                        I.
                        .l  `;!,","":""^^"^,"^^^^^^,,,,,"^^:^""^":::::"`^^"""""`^`"^^"""^"`  !.
                         i  ..   .',>.     I:    . i^.....'< '+--I'I. _{]!;I'"~~<'i". ..     >.
                         l"  ^{_]: ':"-[}_""^<}_i+:I ^~?_^ !<?)\-[!"i[)~{>", -<!l I.~?~<-{~`'i
                          :;,";;:^'^,^:llI",,;I,"^`"'',:"^^;:lll:I:""!l,l;""'i!:"`;`:II;l>i;I'
                            '^I;;Il;';!;Il!"`!;I;II."lIIIi;'llI;II'`l::::;',!;Ili;`ll;:I!`'.
                             <^+_> i,<'[->'<>I!~]^>l<'-?[.<;~'_};,l!;i]1`>l~']!i.?:II-{;;~
                             l!il!;!`!Ii<>II,i!l~Ii^l;IIi:!^iIl<!l:,!!I<:>"!I>~!;>"ili<;!l
                              ..'''   '....  .''.'   ... .   ''...  ... '   . i>'    .
                                                                          ;""^'!I^::"^,`,^
                                                                         .iIii!!;I!!;:>Il;
                       .
                      '+~_;!~+_-+__~i_~!]?_!i~>i_>>+;<_>i-_<~-~<:~~_i?_;+__~+<I+_<~i!>>i]~;i<i_!I_;~;~]-!;>;
                            .'`^'.'`.'' '". '`... ."..` .^'.'.`' `''  ' ''"'`, ''''.. '.''.'''`' ".`.^",`..'
                .]-<-<+~<~<<~    i.  !l~i:~>i"!IIli!!l;>>iii;~l:~;I+!>>iI>ii!"Ii!+::iilii!;"!!!l_ll";:,illi!"
                 ,^,;,""^,"^:    `. .ll<i<_~__~<><!~+>"I:::,^:^`;"";,:;:^:;;,`,:"I"^:I:::;,^!I;;!::^",,!;,I;'
                                    .Il^,i^:l>lI!l!li"
                                 :   ,^`` :''.^`'. "'`::^^^^"
                         ...'...'~^.'>?-_Ii<<>+<<?;~_>>>+>i-~..    .   . . ..  .
                       ^:"^^,"""^`"""'``'^``'`''^,"^^"'```^'',"^^"^:i'!::::;I:,^""",,,,,,",:ll
                       :"     .. .  ^^'"".         .  i;,I..        I:;'       I`^,         ;:
                        ! ``''`^ ^`.+_i?-; '`.^`.'`l>'f1[1Iil'I`:,,''i^!'.''`';x?[1^ "^''^'" :"
                       "!';''''''';^.    ;`'..''''^:.';"":...      . !';      'i:"I'....... . >'
                       `^,i:::::::~I::",,_;,:,;I:;i_;;","!:,,",i<!+i?<!?+I~~~:,^""~"",,,,,"^il,.
                          _l`````;]~^^""!}<``''''^-;     i_;;;l<_[-i>+]~~l++<"```;_,;;,",:,^<`
                         .',>>!i<^'iii<i"`.:i<>!<,.'  '  ..     ;___i<~i>_<<: ...''`~?]<+_+``
                             `I.     !,      `i'     .i.          >_                  >?.
                  ^". ^l;,^,^^.:^^^"`^^^.""'`''`"^^"^`^"``"``'^``"`.'^`"^`'
                 .!i" :_~!I--~">~~!;i<~i"+<I<>>!>>~i!li~<:-?+l!<+~+^!-<+~il
                      ':^" ^^^;,,..:'I,",'"";:.`^.," ^`^`:^,^.`^.'"" ."`'"  ,^.""",,"^.:^"^.^':.^:,::".",: ^.
                      `!!~^>~>++~"">`~_~i"ii+_:;>^~~^<<i!i<_I,><^l_~^:+i-_,'_i`~~~<++!.<i~!`;^-^,~~++l^_+<'_^
                      I~+!_l<+i,
                      ^;`'^"^`^` ^",``^.:,':::;",":":"": ^"``^''.` " ^"^'``'^'.''"^''''.`'.'^`..``
                      ,l~:!]++><`<+_>,+"<i'i>?_+?-?!<_i>`l-_~~+i:_^?':-+:!_-]+i-l><-~-i_]-,>-+~>-;.
                  .'  .`  ..    .                        .   ..   .   .                                 .
                  _[^ `><<l-+:<-i<I>!~_~<~~_<I<+i-?_~-_]I+_>"1::~~[< l{<<??__;l?-_;_;+<+_+__ii+>I!l+_:_-~^
                      ,<i_>~!i<~-+<;;'.    .  ..     . `.       .... .  .^'..  ... ..''.' ''..`. . .' ...
                      .^`^.;^^,'^"''.
                  i+` :~;;iIl"i!l:il<iI:>l"lIIl!li;;!l.
                  ;l` "!^"i!I.;II",II;,";:^l:":";l^"I;
                      "~il`;;!<!l'l:>i;I<i!,~!il:;<iI`!<>lili>"i~>>!>ii
                      .^",',:":;:.:`,:"^!!:`;;I,^:;;;^;;:,;^:I^;;lIiiI;










```

*Figure from page 7 (2346x3317 px)*


---



4203-E P-196



SECTION 2 PROGRAM OPERATION



(4) "%", and "CR", "LF" codes are punched out.



(5) The part program data is punched out following the program name (number).



(6) The same number of tape feed holes as in (1) are punched out in the tape trailing section.



[Supplement] 1. When the program data is punched out ln the EIA coding system, the "CR" code is



punched instead of the "CR" and "LF" codes.



When the program data is punched out in the EIA code, the presence of a code not



available in the EIA coding system causes an error. Tape punching-out halts and



an error message is given on the display screen.



When the tape delimiting code is the "%" (ER) code, i.e., when bit 3 of parameter



No. 1 of NC optional parameter (bit) is 1, the "%" code is punched out before feed



holes.


## 2. The part program is split and punched out, if it is too long to be contained in one

paper tape roll. Paper tape length may be changed from 1 to 300 meters (3 to 984



feed) using the NC optional parameter (word) No. 2.



As the format, the file name is also punched out, for the second tape and so on.



Since the tape ends with "CR" or "LF", actual tape length is somewhat differentfrom



the tape length set using the parameter.



When designating paper tape punch out operation on more than one paper taper



roll, specify option Din the following format:



P <file-name>, <device-name>:;D

• • • • , , $A.MIN • • • • • • %



~**** \, \. ... __



®_®_•



•..,..•-••.,..•_.I



1st tape


#### Food holes


# f.=


#### Tape length foe parameter seW~

.. {; "·®@n,,,



12nd'1ape



~-----------~\ '1_ ______ ,_


#### Machining program

Refer to 4-3-1, "Precautions for Tape Reading-in, Punching-out, and Verifying Operations" for



details and cautions on this operation.


```text


                                                                                               """"': ^".^,^
                                                                         .''.''... . '''...'..^---[i?`li:+{~
                                                                         l[-<~~~+[l+.~_[~+-]?-{l!+~?~-_><>_>
           `'````^^^^^^^^^^^``'`````````^^```'`````````^`''`'''''.........''''.'''''....''`.''`'`'.`'''''`''
          ."""""":"":::",:,"^^"^^^","",:""^^^^`^"^""",,"""^,:;;;:,,,,,,,,,:;;;;;;;::::::,;;III;I;;;,::,:;II,
                 '>>  "<l',<l!"i_?".!!i`ll<<!"!!:;lIl!!!l"Il"
                 '""   ^' ^:^" ^"^. ^:. ,,I;I`;,^:;,:::I,`:I`
                 '>l  ;!l,";l::I,:III^"l!:':':",:;,:^""^;:;^:I:":l,`"",,,;:`",,:"`;^",:,:^
                 `!l. '"i:Iii,!i;_il!";i<i"i:!lIlli!"l>;lii!<i>+I>i:>I<]i+l"!<!<i,<!l!<+<I
                 .;"  ";^''`'^^ `.^"^" '`'"'``"'`'''"'  ' '  ' .'. ' '.'.... .. '^ .'   ..`^. ...'`.'
                 `-<  ,!~Il~!>_"!<>+++`<li[+<I-+_II<-_!I]I>;l>;>_~;~<>~i_+l>~!il>_+l]--!~+[?i]I_<~-~~.
                ',  '`'   .`        .`^   '.     .    .'      .   .      .  ' .              '.  . ..
                !]_]]-_<>_<[" . ,I  l-<<+,+~ii<i[<-?li--~!_!-<!~~--l~_!i:~_i[_]l<<?-_+<-+[]-Il--;i~_!:+~[>i<
                                    ;<>>~~<~li<?+_<:_!-~I:~?-^~<<:i>+"!i~]_I .  ... '`.`...... .  .  .'.'..'
                                    ,:,`^`,^.'^"`"`'"'`"' `'. "^" '"  "",:"^
                                    l?<>>;_i!i>!~!+~,>_+i!!l>!i>>~>I>~::!+<:-i>:i<};^-iI!i<<<!l<,+!!;i!+l;ii
                                    ;>!+>+~_;<:~-I_!_:i!_+!>li><<<;:~!li<;i>:i!!<":_i>>l<!<<~!<iIi>>i<_>;i><
                                    l~l<>~<>IiI!>l>i!ll><<~~l-<-+ll<<~+<iIi+;~i:I. ;>illilII;;>i:!i";i!I:<!l
                                    :!.;I:i'I>ili<-!.i:+;!i'I:"><,l_<i+_`>l!+~:
                                    ,!l;,':;^";,:.I;l";!,"."^,:."'I"'":"';;l^.^";" `" ':;,:`":^:':^"^^,"":,`
                                    >-!~~">+<>?-~I__~>i_<}lii~_:_l__I^+:"]<~+I+<_<";<^^+>~~:i~;>;~!+~!+>-+-;
                                    i~l :"~;+~"!_-<Ii_l~<>_i+<+;l__;il^'i>~.!+';>>{li>!<ii<~~~I<~I_~+i<;?<<<
                                    l~-_<`      .     ..        .  .   .  .    ...  ...'.......'..'...'..''.
                                    .'.''
                                >l  ,<i;">>l;il>!>i,:;"ii>^>lI,!Illii!,IlI.i;:!"!I::lII"!^;l`":;llllI:;"^:I,
                                "^  "l<>>>+i~i!?_;+iii!~+>l+i<!<_i!>~i:<<ll!l;>!i+>;~l-!~;+-ll>!~+<<+i>;!_-!
                                    +~+~~`<?~;:<! li[>~,<__iI+I-~;I><<:+l;<<<+-+!!ili""l>;_<i:!<<<!:>ii!i]+I
                                    >~_<l;~~l_:<~;~_;"~-~<>]!!_>~+~--~^++~i?:~_:^~
                                    `"',"`""`:^^.`^'`;".```^'`^'^``.`'`^"``^'.`."`'^`.....'''''.....''.. ..
                                    i]Ii<+!+ii+[,;+<:]-:!?_<~l~:?<_l_>><<>_I:i~.>~^_+i:_~>!>~I?]+:<<<!i>"ii'
                                    i+!iii~<;>~<;>li+:i_<`!i_:;l^i<:.<i-i_<_-_!><<-_;~!<>~+~-~_+>-]<i><~i><;
                                    +_>l_>+I<--?[;i-<I+~<l!->,i~!~ii<-~"""'":"`^^";``"^"^^,""`,^"^^"^"^^`"^'
                                    "", :;; ",:i;.:;^^:,"!^":`II:,^I;;"
                                    !+~+!'l~iii;>+;!,!il>";>l!'lI!!!':!l;>>>i?ii;I>,!ii~;_i+I,!!lIii!i,i<!<^
                                    !<~;~!~~?-i<_]<?!->_i>><?-_~+_<il~~ii[i,:I,,^":`"::;^:,!"^:::;IlII';iIl'
                                    ";; lil::l.l!!l^." ,':I`,l!I!lI_,!IIi~^
                                    >"^_i:"l!;l:. :!i;!!;"Ii;I,`;!
                                    ^.^:;:^;I,I:^':;;::l:^;!:I;^;;
                                    ^l"^":,^"`'``^"""",:",:"^^`"'.^", ":,,,^"":,"":",;^
                                    !" ^``''.!+l_~''"""^>i|{{1>:::  :.'    _\+)l"""".;~;;Il;
                                    l;`"""^^"i+i>i,:I"":l!1]]]i;;;^'; "````_1<[;,"`"^l!;l!+i
                                    IlilIl!!,,"t\;^i(t/;",::":,;:::";`";I::::,"Il1({";,
                                    i~-{+_}}~>:[}[><]{1<i!]}<[[1<+~~1[]-[+>{]{}<i)f(^l;
                                            '`'   '`   '^.                    '"' .''^.
                                    I;:::,":^^"":;,",::"^^,,,,,,,::;^ ;:":,,,""^""""":.
                                    ~.``'''`?l<_, ```    ..  .. ..."^``  ''<|_1;`'.'.I~~i!+i'
                                    i^",",,"!Il!:""^^``^^^^^`'''`'`^I.:``^^>)~{:```^'lI,,"!I.
                                    .''`'``'.``'^^`'``:;^^^^`",",""^^ ^""^^`''':"^"",:
                                                      "i`''^`_([}]-?~]}??!`^'':~
                      ".'.... . ... '^.    . .  '  ''  ^`^.'''. ...^".'.''`'''^^
                     `-_<+,"_.>I~"l ,+>+<~<_ii_`>+"._?~!"[_~+-~-!+"^_<~>~?<_I>~> +<~:!]~-?!<<^+?_~~]~_<!'~_"
                     '<++_-:i++!!_<?>l>:!>;_<!;~<<i-<+l.  .''.."...  '''.''"''`' `'' .`'.^.`, '"^'`^``'. '^
                     .,",:,`",:^";:::",`""',""`l;,,l:,^





























```

*Figure from page 8 (2346x3317 px)*


---



4-3. Verifying Punched Out Programs



4203-E P-197



SECTION 2 PROGRAM OPERATION



This is the function for verifying the program transmitted to a target device or medium against the program



stored in the source device between the paper tape and the floppy, the paper tape and the memory, the



floppy and the memory, the floppy and the floppy, the memory and the memory.



The following explanation is given for the verify operation made between the program punched on tape



and the program stored in memory.



The procedure is as follows:



(1) Set the tape to be verified in the tape reader in the same manner as for storing a program from



a tape to memory.



(2) Press function key [F3] (PIP).



The function names on the screen will change to those given in item (3) below.



=PIP



DATE DIR



"PIP >" is dis layed.



MULTI



PIP EDIT PIP . LIST CONDENS [EXTEND]



Press [F3) (PIP).



(3) Press function key [F3) (VERIFY).



=PIP



READ [EXTEND]



@@J@@J@



Press [F3) (VERIFY).



The screen changes to the directory-selection-based file operation screen and the following ls



displayed on the screen.



PIP:VER!FY V


```text


                                                                                               ."^^^`" "''^"'
                                                                          .'..''..    ''..  .  ;[-]?i+ >;!-_^
                                                                          +)_i<~~-~!>'-?]~_?]_]{:<_~_--_>+~[!
           .^^^'``````^^^^^^^````````````'''''''''''```'.'..'''''''''.....''''..`''''. .'''`''``'`'.'.''.'`''
           '",^",,,"``^"""""",^^^^^""",:,^^^^^^^^^^^",::,:,,:;;;;;;;;::::::,:;;I;II;;::::,;;IIIII;;:,,,:::;I^
           `~`_.   "<~!<~l!i;;];!lli!!i^>lI:!+Il!lIllI:
           `i^i`    l>l;<i;+~^";i;l;<>!';li,,,;>[~!<;!!
                 :l;"^",;"",,,l:,^;^.""Il^"^";,',"^",:^,::,:::i;::,`",;,,;":;","^`^`,",;`:`""""^"^;"``"^^^^"`
                 ,!i<!+!>~i~i<+~~IilI~<i]!i-i>~i_i]]<-l!<_!_ii-+~l<!~i]_]-l>-~><!Il:<_~<ii:~[-+><I~<i<<>-<?>;
                 i-llii"":~~^~i>l<I;-i>i<"<<<>~_I">~;l<<<i'<+_::<!;i~>,+<><i'<~;l~+<i'+?_Il-~!<-<,~~<i!i>^_<;
                 __-~+:>~~I_+l;++<~++:l_<I[<_~<,-<<!]?I]i~~~:<-~:~~><~~l!_~+~+<:___<>><^'..... .. .'. '.`..'.
                 ":,":^"``'''`.'^'`^"^.'^.'":",`,'^''"..^:":..`^.`"^^"^"'"^'``^ ^,"`"":
                 l~-;i+-i~+<+:~_<_>>+!~:ll;<l<l:_i;-~,!-+}!,-~~>[+<;,<~--:+<~+>+<"_~il<i_<+-!I<i<~~_~:~i;?<+;
                 l<<<i~iI~i~-++il-<<+~!!:<_~><<l'. .'.'`'`^."``'^``..'^^^.``'^`^`.```"^`;,""'^"^^^`"^."`',,,'
                 :;^^'""",^!:::.`""","''.^:,,;;I
                 !<_Iiii><~i!>,~"+l>+-i<+I
                 . `',`''```'` ' "'.^'`^^'
                  ;>: .~i::i!,~!!"l::i^,Il_>!:i,!iI;~!i"I!!>>,;:l+l^I!I!::!!;;l:`l,II^:i;;:I^:"I::;II,:I:;`
                  ,:" '<<>l<>!<_~l>il~",;;;II^I",I;"<>!^:!!!i^,,:i!^!i;!;,l>;:!;^<;,!^I<!;I-Ii!<l_~<>::ll!"
                      '!,_+<"!^"!>;iI>"
                  ','  "' . '.'.' . '...,^^.,","
                  l]! ^i>+?~l+i~-~<,-+~;?![:-!_>"
                       :"^`,`^,,^''"^^^^ '``,` '^^^^`.^;'^"`^'`'^'"^'``.`'``.`.^`''."'''`''.
                       li+:<<i~_~I;-_!++,<l,+-;~<i~_l:--;<<~<-]I+Ii+>+-:]<-+,~:<]+iI[>!-]<_<

                        .i                                                                   l.
                         !                                                                   <.
                         !   .;;I^                                                           l.
                        .!   `~:l`                                                           ;
                        .!  i~l`'^,::^""^"^;;,,,,,,:""^^^^^,^^^":",,^^^^",;;::,"^^,"":,,^^'  l
                         i  ~^ .'..:!..  ..l,.'....:'.  ..'l^|-i<"^!... ''il..    !"...      I
                         l^""`}~_" ^, !!+^ ,' i;>  ^ :}!l' :`_~<  .; :"_~ ;_~]}][?I'<~++_[>'`!
                          :_,":^^^^^,^::,"^"^'^`^'','^,:"^^"'^^`'.^:`:,;".":::II;;,';lIIl<iI;.
                          ^;.,lIll!I`l!!i!i"^!l!!!!';!l!!iI'l!iiI!^">l!Ill':!;lll,'lI!ii!`'.
                          l. i'{+i _I-.]]!`i<,<~?'~I~'?-? _;!:[{:,l!,>[1.~l~`[~<'];l;+(:l<
                         ^:  ;!iI!;!`il!>!l,,!!+?;i';:II!:;'l;;iIl""!!l~I>^!II:::!^!!!+li;
                         l'`' ....'   .' .    .:<" l>~<I+~!Ii<!..    .. .   . ...   .'.'
                        ^l;__l!;+<][?]-]l        "";!>iIlIiI;;I^
                        .''..''''`'```'''

                  >_, :_!<~l!iii->>:<~II_<<">~<>->l>'
                  ,:` .'^,;"`:",::,',I:""";`,,,^;``:'
                        .`                                                                   `
                        "!                                                                  .l
                        `;                                                                  .I
                        ^l   ^+l<'                                                          .I
                        "!  '!I^^``'```````'''''''...''''''...   ...''   ....   .'......''  .I
                        "I  ""`^^",!I^^``^"i^..''.`I^`''`";i':<>~";l',?_+!;,^:i<!:>"``^""". .I
                        'l   ^!::  ,'":I;" I';l,,;'I ^II; '!:i[[?IlI;!{-[::..!l~" I ,"",::" 'I
                         :;^';?--` ,`l<]-i'I"+_~i!^:.;+>l.'!<-]?_-!,_[-l{;;.^[!:` I._-<+}1<"l`
                          '""`^'`":`^`"^",,``^^"""^^,,'`^:^`^,^",```^`^",""",'^^:,""`''^''"".
                             !;<~l:i^>:_+ll"lI<~~;>`!;_<i;l^!!?[Ii^Il<_~:>^!I->!II^!l>+;>"
                             _`_!I'-l~,_?::l_"+>?'-;<^__<'+II:~]`i;~"~_1.?l<^_!:"_I;!<|`~!
                             `I,:;;` :;,,,;..I:_[;"`;l;:ii^'!I,:;I ';:,:;" ::^"";'.II;;I;.
                                                ,,`<_??>[+?i-??_i~`

                      ^<<l'i!>><""~!<l<>l'i^i+~`+<>><i<:l~~<!_!!:<><>i:>+:"<><!+!<:^ili<>^,~!l:ii^l!iIi<!I^i.
                      "~<>l<i<+l!:_>il]<<I>,`":.,",,,,:"";::"::"`:;;::`^;^'lI;,I,I^`l::l;'"l:,`,I'";::IlI<'l.
                      "!l!;lll;^I^;l"`!ll>I"
                      li>;:~<<>>l"l l+
                      "";`,I;:I^"';.;>





















```

*Figure from page 9 (2346x3317 px)*


---



4203-E P-198



SECTION 2 PROGRAM OPERATION



PROGRAM OPERATION



197/07/15 14:10:00



PIP :VERIFY



v[l]



INDEX DI SPLAY PROCEDlflE



[F2] - MD1 :*.MIN



[F3] - FOO:*.MIN



TO OIS?LAY OTHER INDEXES. AFTER PRESSING



OVERNRITE



[Fl] ,



ltf)IJT THE DEVICE NAME AND FILE NAME. THEN PRESS [WRITE] KEY.


#### DEFAULT DEVICE NAt.£ = fill:


#### DEFAULT FILE NAME= *.MIN

>XV



MDT: FOO: COWAND OVERNR/ CHAR.



INDEX INDEX I NDEX HI STORY INSERT DELETE CANCEL



(4) Enter the file name of the file to be verify and press the WRITE key.


#### Example: BOX-1350.MIN.

This step ls unnecessary for a program without a file name, Le., A.MIN.



PROGRAM OPERATION



PIP :VERIFY



V BOX-1350.MINII]



INDEX DISPLAY PROCEDURE



[F2] - MOl:*.MIN



[F3J ..... FDO:*.MIN



I 97/07/15 14:10:00



OVERWRITE



TO DISPLAY OTHER INDEXES, AFTER PRESSING [FlJ,



INPUT THE DEVICE NAME ANO FILE NAt.£, THEN PRESS [WRITE] KEY.



DEFAULT DEV I CE NAME = l.t)l :



DEFAULT FILE NAME= *.MIN



11'0EX



f,1)1: FOO:



CCfJMAND OVERWR/ CHAR.



I N[E( I NDEX HI STORY INSERT DELETE CANCEL



'-WR_1_TE_,


```text


                                                                                               """^`" :^'^,'
                                                                         .''.''.'. . '''...'.."??-?i?.+!;_}!
                                                                         !}_<!+__-;~._~]~_][+]{;i+><<-_+~~-I
           '````^^^^^^^```''````````````'''````````````'''''''...........''.'..'''''....`'`.''''''.`'''''`''
          .","",::::::::,,"",,""",::::::,,",;;;;:::::;:,":;;;:,,,,,,""",":;;;;:::::,:;IIII;I;;:::::,,,;II;I"
                                .                          .
                             ,;,;l>iiiil!ii!i!>;;II;;;:::;II:::::;;;::,,:"",,:;::,::;I::.
                            ^I `:![{{1\![}|(]}/!;::"""""",:"""^^^",,::;I;Il:l:,;;I:ll> ^I
                            "` ',;;I^I~~!<;,""^""""""""""","""::::;::;<-~_?~|{]j-)??]>  I
                            ^` :;~{{;_)?>~:""""^^^^^^^":,","",;;:,,,,""^^^^>}[)\_-}:;~  ;
                            :^ :^^!!                                      .        ..i  "
                            :" :"                                                    >  "
                            :" :,. . ..     .       .........................   ....._  l
                            :^ '^^l>iIl;I;;:"!l!!liI^^^^^^^^^^,,"^^^^^^^^^^""^^^::::,;  !
                            ^'   ,)(?,></~_<l1)+++-!                                    !
                            `.   i]]:.;"|]I!_]-                                         !
                            "'   i]i_<}>]!+_1|I;[++_I ~i~?^~_~+i]" i!l..                ;
                            ;`   ")1[;]t+i\-+|"1jt;(t:<i[>~)r<:?t1:])}?'`}{!?+'-+,      ,
                            :`   ~|}1-lI)]_[<[\r>:^r{i`.. .''   .'. ''`  ^`.'^ ^`.      l
                            :`   l_i_~"";!<"?1-." .:!<!.                                l
                            ;`                                                          l
                            :`                                                          l
                            :'                                                          l
                            ;`   ",                                                     l
                            i^  ,~<                                                    .>
                            >^ `;^.`^:lii;,":Iil:^^;Il!lIllIll!I,l!l!"^,:^","^,,^^^""` .~
                            I`   ",^'^;-[i;^^:~?~"';_}r\/[!<}}/1l>_}[:`,;'^^^.;, . ..   <
                            ';^.`_-~;'; I}[<:` !{]!^~!i>[il I]-~l,"+i~<l,i]-_;"^      ';"
                              ^";,,;I,:!:"",^";"^,"^:;:^,^^::";l:,;,"":",I""":^^;,"";",`
                               ,:<+I:ll:-_!;,i:+_;i;!I+-,i:ll]~,l,!![-,i,I~_+:l;I~]~;I
                               :;>i!IiiI~+!I;i:i~;>liI>-,>I!I~-,!:!I~?"~II!!!,!l;i_~:!
                                ^``^^  ^''``  ^''`' '`'.^. '`'`"  ``..^  ^'`^"  ^'''^



                 `;^ 'l","':,^^I"'^""^'`,,"^^I^'^'"^.``",.``^`'`'`'`"`',",",,'''.
                 I-! '~I!~^lli:-i^!~i~:;Ii!>^+~:_;~+:<+<]:~<>i+i+_>!__:]~~<i-"+_~.
                     'i":::,I"  li:I`^;!I^li!^
                     `!I<i!<<l  >>;!""!~~;>+il
                      :^^.`"''^" ''`^`'''^` `^`^'`^`^"^"'^,;`'^``^;^'^^^^'.'' '^`,,"
                     .lI~;!~->:>;>I~~><~+_+!l_:!l>ii[<<!,>__ii<;>I?<"~_>+!`!>'I<i[__`
                        '``.  . ..   ..  ''`''````'``'''`'..'''^^`.'`''''^^`'^`'.
                      ^I^::-[]][-i[]]_>-_:;;;I;;:::::::::;lI;::::","":;I:,:,,^;:,I.
                      l. ^"!~_+_<I~<_<l+<""""""",,::""""""""""":<]i_<l<,I!!<!?<, ,:
                      I  ;;+~l"-}__~````^,,::,,:;;;;;,,,,,,,"::;l>li!}t(r/_|+~>: ^l
                      ;  !:-<)}>_()+{+|?^`^""`````````""""""^```''''`l!!il,;"`I: ^;
                      I  ;   `'  ...'.,^                                      `: '^
                      l  I                                                    "I '^
                      l  :"^^"""^^^``^^"","^^^^^^^^^^^^^,""^^^^^^^^^",^^^^^^^^I, ^:
                      l    ![1-;<<[i-,>{-_][{I.................................  ^,
                      l    ?}[`",-j_i;[{[                                        `,
                      l    -<~"<!l1>><|[>:::I,  :;l:.I;I,", .,`                  ^:
                      l    +[-~>[{;+1<1_`(u)_t_,)<)~?xf~<)t!l|[_l.,-!;~"`iI.     ^:
                      ,   .{f]]ll_}}-?;{)j<I!n_,'`^ I!;  ,I;`:II, ^i:"i"'i:'     ^:
                      "   '1{_1-:l+~;_1r-l'.I~]?i                                ^:
                      "       .    .  '.      '..                                ^:
                      l                                                          ^:
                      i                                                          ^:        ,;::::;.
                      ,                                                          ^:        i. '" !"
                      "   "_l                                                    `"        !`_-::~"
                      "  '!:"```` '````'.'````'. ''`^''. .'.. .'`''''''''''`'''. `^        < >+^^<^
                      ,  '' .'';l|_:.';!}+".'>~1f11+!}--|+!+<?_`'l". ..'!`^"^``. ,I      ^ <!;"!":`
                      ;^  ^]]~''',-[-I,."]?<"l++][1i,^_}[]i,~1~<~I,>_~~.:        I,    "[[}!}+"Il;^
                      .:,^";;;^^'.:ll:"'':lI":;;",:""',;:,:`;l:;;,"I!l!,,'''''`":"    ;i"+;:^'^^`l.
                        .;l!l;;`ll!l;:`ll!II,^!iill""!!iIl',l!!;I`:I!!l!^Il!!ll'      ^  '  .....
                        .!,-i.il<I]?`<<!!--`<!:l?-^~>"+}l,:!"-)l:!+,]<^!!i,~)^~`
                         :I;II;';I;!;:';I;I;"'I:;ll^"I:;;:'"I:;II':I:::I';;:l;;.















```

*Figure from page 10 (2346x3317 px)*


---



4203-E P-199



SECTION 2 PROGRAM OPERATION



This starts the tape reader, and program data on the tape is read and compared with the stored



program data.



While verifying operation, the screen displayed "VERIFY" along with the "file name".



PROGRAM OPERATION TRANSFER VERIFY BOX-1350.MIN



tape file name =BOX-1350.MlN



file end



data match



(5) Press function key [F7) (PIP QUIT).



tape file name =B0X-1350.MIN



f lie end



data match



97/07/15 14:10:00



FAST FAST PIP



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



@@J@J@@J@~@



Press [F?J (PIP QUIT).



This completes verification of the punched out program data and the display mode return to the one



in step (1).


```text


                                                                                               .,,,"^, :''":'
                                                                          ''.'`'.'. . ''.......;]-]-<-.~II?1;
                                                                          -{~><~<__li`_-?~_-?-[],>~+_+-~__>?;
           .'''```^^^^^^^^^^``````^`^^^^``````''```'``````'''`''``'```````''''.'`''`''..'''`'''''^''`''''''`.
           '""",,"::::::,","^`^^"^^""""":"^^^`""`^^^`^"",^^"`^^,:,:,,,:,,,:^"^^^,:,,,::,,""",^,:,,:;,:;""^"".
                       :I<,:<iii'i!";ili'li!<>^`<Ii,!;l!liI'>ii""l`li;"il!^l""I;I`I;!":;;III:I:"l<;,iI`;l;;I"
                      .Il~!i~_l+!+<",ill`;!ll!"^i:I;!:<<l!:^!ii:,l^;!I">>i^l,"!!l"iIi"liI>iili;;iiI,!<"!>!!>,
                      '>;I~I!:`,<<I
                      .iiI!"';;!;":,"lII:>l:"`i;",;:;I;`lI:I;,:;";li!ii;l`:;,,^^:!,,I,'!l"`,,,,,'
                       iil<l,>!!~I>~:+>il+iI;"ii;!>!<~l"<<+<+~<~^,<~!~>:;.~+>>+;+-ll+~`!->,>+i+!'

                                .              ..............       ..... ..    ..
                              "::;IlIlI;IllI;II;,:,,,,,,;;;ll;:,,,,:;;;;;I;I;:,,;I,",:::"
                             :; Il[t\|\(</|/)_)(:,:::::;[(\){\<[\[]]I;;;!llI\t[<1\+1}1l.::
                             i'  '.........''.'''.''''''''''...````'``^>}+_-<]>i}~[_|);  I
                             l'                                            ..    ....'.  i
                             l'                                                         .<
                             l'                                                          I
                             l'                                                         .;
                             l'                                                         .;
                             l'                                                         .;
                             :.                                                         .!
                             "                                                          .l
                             "                                                          .;
                             ".                                                         .;
                             ,.                                                         .;
                             I.                                                         .i
                             :.                                                         '<
                             ^   "<_;,,!;,~-:,[-i,~[l+~<                                .I
                             "   ;+]>i]]"'^"'.^`'.'^'`''                                 ,
                             "   !-i;I+!<^                                               ^
                             :. `:`'``""'``^:I,""^`","^^`^"::::"^"::;:,^,,";;:,;,````"^ ."
                             I.  ^,"` :;",""';^",^^',.`""'.i+}["^,l>}}l^:,"~~:.I"`^^^^` .l
                             ^;`.i[-; "^i-]+^^"__<!:: I-<" I!_{]]~"i[_>[,^.?i! "'!-~][_";"
                              ."";,"::`^,^^:;,::"":^^:,^^;"^:,^,;^^,"^",^^:::,:^"::,;:",'
                                !:?~"!:<;]_:;:i!+_:!;l>-_,>;I>1_:l;!_}~:IlI~+iI;l;_]il;
                                <;~!,i;~;+_:II>ii<"illi~_,<IIl~<,!;l>-_:l!;<!;;Ii;<?ii!
                                 ^'`^.  `..^   `..`  '`''^  `'.'^  `''`^  ^'``^  ^''^`
                  `^. ','''.`''.`.. ...'^`` "^,.''.""
                  <]: ,<>+->l_<<?_~:+-<i_I~l-~[,+_~+~;

                        ^i    ... '....''' .""`.`"".^`^                                     .:
                        ^i   ;[{?`il+l^_-[`!}-+,i-?;}__^                                    .!
                        ^i   ;<!?"??_"'                                                     .!
                        ^!   ,-!i`<<;~,                                                     .I
                        `;  `I,``^'^^'`",,,:"""""",:,"""^^":^`^"^,;;,^`^^^"^^"^""":^`^`^""' .I
                        `I  .    ..I:.    .!'    ..:.   .."->]_"  Ii<??!  l`,~-i''<'         l
                         !'  I{__' :`l_[_~ :'-+<I>^` ;__i `+>{|[-?!^<{1l?;:.`-il" I >~+<-[l ";
                         .;:"":::`',,",::,',`:;:,,",'^:"^.^;"Ili!!I,,II"l,,'`i;,'',';;;,l<!:;
                           .`,ll!i>;^!l;l!!`^!!!l!l^Ii!!!!"'l;IIl!^:!IIIl:';l:Il!"`!Ill!l''.
                             ~`[~>.-I<,]-;:l+^_i? _;<'[?<'_II;]}`l:>^_}{'_:>^{il`_I:i])^il
                             il!;!;i">li~I!,ll!l~;>^i;lllI!"!ll~Ii";li!~,<^i;!~lIi,!i!+;>,
                              '.'.'   '..'.  ..'.'   '....  .''.'.  ... '     !>'   .. .
                                                                         ':""^"ll";:"""^,'
                                                                         `;l<l<;lll!,!i;I"
                       .
                      "<><:l>i>--?+il<i?~~}+i;!~<+>ii!><+~+!<>!>!~~<<l;-__l<<<<+~;+-<+~i:>i>+:!-il!li!->;l!>.
                      ,!:-+~Il+;^^^`'^`'`^"^`.`''^^,"^^^^,^`"^""`;I",'`:::^:,"^^:`,:;,:;`",,:`":,"^^"^:;""":
                      ^:^l!>^,,^























```

*Figure from page 11 (2346x3317 px)*


---



4203-E P-200



SECTION 2 PROGRAM OPERATION



[Supplement] When a data mismatch is found during tape verification, the block (line) which contains



inconsistent data is displayed on the screen and the inconsistent character flickers.



PROG (J'ERATION



Blinks



>V 8.MIN



tape fi I e=BOX-1350.MIN



N005 GO



verify continuing? (Y/N) !



TRANSFER VERIFY BOX-1350.MIN



97/07/15 14:10:00



FAST FAST PIP



READ PUNCH VERIFY COPY FORWARD REWIID QUIT [EXTEND]



The following message is displayed, asking the operator if he wants to continue



verification.



To continue verification, type "Y'' and press the WRITE key.



To abort verification, type "N" and press the WRITE key.



When no data mismatch is found in verification operation, the following message will be



displayed on the screen.



tape end



file end



data match



If data is left in the file after data on a tape has been read, the following messages will be



displayed on the screen.



tape end



data match



If data is left in the tape after data on the file has been read, the foHowing messages will



be displayed on the screen.



file end



data match


```text


                                                                                              `^^"'"'.".^^^
                                                                         '...'...   .'... ..  <?-[>-;,<l]-_.
                                                                        ^[[~i>__}l~"i-]~_??-_}~l_>]_--><~?_.
          `^^^^```````^^^^^```''`````````^''''''''''''```'''''''''''''''''`''.'`'``'...`'`'''````.`''`''```
          ,:::::^^^^^`^"""",::,,^^^`^",:,"^"^^`^``^^^^,,:"^"^,::,:,,,::,,^""^,::;:,:"""^"":::;:,:"^"^"""::,
                ~<l!!<!;!!<;   .<>I!;",,l>I,;IlII!;:,,lI,:l^l:,,;"IlI"^I:i:,lI:^.l;^Il,l,:;,;^,!,::',,:I;::.
               'IIll;I;"I;I:   '>i!+ii<~~_>i>~<i~<+l!~!<<>>li_il+i~[+>;+>i<__<>!:i+l<_<_ii+>-l>_l<<!i>!_+!>'
                               'I!iI!<~-iI"!~<!,l,~+<~_>>l,<`<i!,+l!<+"i>!l>i!^!i>!<~+_!>,~i_~<>-:;_!>+>l
                                           .......    . .``'`'... .          ..'..... .  '... .  .
                                         :::;>~>ll~>ii!>>I;;;;:::;;<~<<~~!Ii!i>;:,"",,,l!I;liIllll:;.
                                        ,: ";_1)<_()1_<{_::,^"::::"+1))[(<i(?__,,,I~>!>)r{i1\{|ff~ `;
                                        :`                                       .l?~<_l<iI?i-~??;  !
                                        :'                                                          !
                                        :'                                                          l
                                        :'                                                          l
                                        :'                                                          l
                                        :'                                                          l
                                        :'                                                          l
                                        :'                                                          l
                                        :'                                                          l
                                        :'                                                          l
                                        :'                                                          l
                                        ,'                .                                         l
                                        ^.              ^:?-_+`                                     l
                                        ,'   . '.`.   ',^                                           I
                                        "'  ^+l~<]~`^il^"l,.";"`::'                                 :
                                        ,'  ;)\+:]!(?-!;!~i`;<l"+>`                                 !
                                        I`  l(_!_+i1?lI;"l'"'ll~ ...                                >
                                        ;' `"I""l:~I:;i!>],^^;I~:,`'^"l!i<:'`l:I>I',I,!!l"l!^```'`  !
                                        :^  ^I:" ^:`ll:'"`:!;:^' 'Il" l<{)i;:II{1l;^; +~l.II^;::I:. i
                                        .;"':_+!.^,:_-<:,,i+<i;:',-<:'l!~--_~";]+I}::._>l'""l-<~[-:;^
                                          '^;`",;`^:^^,,`":^^,"`,:^^;:`""`'"''"`'^,"^;^^":``,^,^"`^.
                                           !:?+,;;>,_-ll:!;]-:!:!I[?"i:l;-]">"!>]],!;l<~<:lII+?>;I
                                           !;>l,lIiI<_l!;il<_l!:i;>_;~;!Ii_,i,ii~];iI!i!l:l!l<_~;!
                                            '      ... .  .  .   '  '   '  .      '  ....`  '..''
                               'i;I !!i;l!l,.IlIIllI,.l.;>;;l;IlI ,I;;:: !;:.;:;:I;:.;^,:.^:,,;'';.^,,;:"",
                               `ii_;>+~>+l<i'li!ii+_;'<'I<<>>~>>i.l~i!I_'!ii'<<<i+~>.l^;~":~<!+;"+`;>!<!i>i
                               ^i<;+!>llI
                               ^l'`^"::^""^;:!;,;:,^';,:^"I:^:":^""::^;,^:ll;;I"""^.
                               'l::l;!lI>:"<!!l!<>I,.+_~I.I.,+!lIi><<,><I;+>>I~Ii_-:
                               ,+^:!;I:^Il>l:ilI" !ll^^!,^I;l^,,;;`l;:,ii!;i,:,:'
                               .;^,lII""I;,IIiII:.i>!, I.'i;lI;:li";I;^i;;^I:,!i:
                               ;~<l;^";'<ii""I!II>l;"!Iil!;l::"!Il!I>!I,"!!II<Il`;<!I<!llil!;Ill!l!il,!lI!:
                               ,-i<~!!>!>_i_<>i<i+~>;:"::;,:"""I;":I!I;,,>l;;!;I^";l"l;;Il:<l:I!!!i-l,!::!;
                               ,>i<i~il;`l'Ii!"~I!<i:
                                     :I;;'I:;
                                     i_<!;>il.
                                     <+:I+!;
                                     i?_>^<~?<<
                               :;";;";Ilil;:>I:l:^"i;"^;,"`"^`",,"^^""""^^^`^^^'^;`",,^^^^`'^^^```'^''^,^^'
                               l<>__iii~<ii!<<li~!i?_!;-~~I>;!!~[_!:++!~+<>I<++II_>!+_<~_i]~I-_~_-]->!]_>-!
                               :?+-_?>~>,<"++i;~!<+l"
                                  . ';:,"^,":. .  . .
                                     i-+!;<!i
                                     !+-!^!~_<!
                               ;I,;I"I;;>l;;!l:";,,^;l,`:;;"`"^,,";I^"""^,"""`^""".:^^,",^^"^'`^^```'`^'`,"
                               iii_?iiiI~i!;l<~l?+~!-__,>--<I>Il>>i-!;<_!~~+>;i~+<"><!>><<+<~-l<++~_-?_I<-i
                               !-;l_~!<~i<:l<"++:!>i>~>'
                                    .il",,:^
                                     ~+,!l<^
                                     i+[<,i?_+!
                                     '```.'^''.




















```

*Figure from page 12 (2346x3317 px)*


---



4203-E P-201



SECTION 2 PROGRAM OPERATION



Example 1: Verifying A.MIN in TR: (paper tape} against A.MIN in FD0: (floppy disk)



I...J



TR:A.MIN,FD0:A.MIN



Example 2: Verifying A.MIN in TR: (paper tape) against A.MIN in MD1: (memory)



VLJ TR:A.MIN,MD1:A.MIN



Example 3: Verifying A.MIN in FD0: {floppy disk} against A.MIN in MD1: (memory}



1....1


#### FD0:A.MIN,MD1 :A.MIN

Example 4: Verifying A.MIN in FOO: (floppy disk) against B.MIN in FOO: (floppy disk)



Vu FD0:A.MIN,FD0:B.MIN



Example 5: Verifying A.MIN in MD1: (memory) against B.MIN in MD1: (memory)



Vu MD1 :A.MIN,MD 1: B.MIN



Note that the underlined device name MD1:, which is the default device name, can be omitted.



4-3-1. Precautions for Tape Reading-in, Punching-out, and Verifying Operations



(1) There are two tape coding systems, EIA and ISO. The selection of a coding system can be



conducted by:



(a) Parameter setting



Bit 1 and bit 0 of NC optional parameter (bit) No. 1 are used to determine the tape coding system:



bit 1 for tape code parity discrimination and bit O for tape code. The tape coding system is



determined by the combination of these bits.



Refer to IV "PARAMETER", Section 4, "DESCRIPTION OF PARAMETER AND SETTING



PROCEDURE" for the procedure to set parameters.



(b) ISO or EIA designation for READ, VERIFY, and PUNCH operations



Follow the steps below when conducting READ, VERIFY, and PUNCH operations. This will allow



the operator to directly select the coding system regardless of the coding system set by the



parameter.



Example: To punch out stored program data in the EIA code



Key in the following command in step (3) of the punch-out procedure of a stored



program.



Indicates EIA.



BOX-1350.MIN;E



Key in ";E" following the file to be punched out.



Designation of EIA ISO, and Verifying



;E ..... EIAcode



;I ...... ISO code



;V . . . . . Verifying


```text


                                                                                               .,"",'" ,^","'
                                                                          ''''``.'. . '`'...'..:-__]!-'~!_-~"
                                                                          <}~<i~<~?li.+_]<_-]~]["!_~__?+>~~];
           .^^^^^^^^^^`````'```^^^^^^^``'`````````'````^`''`''''''''''''``````'''..'''...''`'''''''.`.''.'`'.
           .,::::::,""`^^``^^""^"""""",""`^`"^:"^^"`^",":^^"`^^^``^`^^^`^,:,::,"^""^^^",:,,",;;;;:::,::III;I^
                   "_I>i!i~^:.^<!!+l!i"i:-<_:l`!+!.>lil!^iil!":l!!:i:l;<<~;;,;<i>^:~;III`IliI
                   `:,l:;II^`'.:;"!I,>^,^;";",.'"".i;!ll`l<!!,;~>l,i:,:llI:;,":Il^:!I>i<"I!i!'
                              :!'''~-;<;]??;<++ii!~?~~
                    .         .''^ .`'``,"""'`"""^""`^
                   I[>-___]:_",-<!_~>+;+i}+-I~'l+i'_>-~_:<]~-I>--]i-!>!-?-<!!~1?>I`~>_i>><~"
                   .`'`'`^`.`..^' ":,;^`""^''^'..`.;";^^ `:""`^I:"'"`''``''''`"^''."`,`^"";.
                              ;i`^'<?I+![_]l[{->I<I]_?^
                   '".''''` ^ .``"`.'..^'"^";I;!I``.^`.   .'.'    .. ...'``.. .'`.  ..
                   ;->-~???:?^"__~]++-:<i[~_;!:ii+i'_~~??il[??;<[??<-i><]]]<!!i{-<l`_~-+<+<-^
                              `^  `;,I'"`,,:`";^^."^::;`..      `'                  . .  ..`
                              ,l,:"i>+Ii!_~_!?{~iI~!]+_"
                   "i,:::;I';.`;:;:`^^':^II:`,`ill" ;,`^"`^I":'^^""^,^I,I;I^"`":,,.^l^`^`."",^
                   :~i~i<_+,>'^<>l<ll_,iI<ii,l^:;!l'>i<+-!l-<_:>]_<!_l<i_+_li;Il>+^l-~-__,~~]~.
                              ,:  :~l!,I"ii!,l!!;!IIi!!
                              ^,''^:lI:;,!!II,;l;!llil!
                   I-l<>i<~,~'">!<<il;"!l+~i"I"<~l; :;;!lIIl,;iliI!;i!<_~I:I;~>l:.lIIII;Il"
                   ^;;!;lll^I.';;,!I:i^:,l::`,.II:^ ;^;I:I:!,;~<!;!,;Ilil:,;,!;:"'lIilI!l<"
                              Il.';?_!;!li__>>[~I,+i<-+!
                              .`'''""`'`^^^`^;i!I::'",^"
                   :}_[i<+?<>~>^~>_~<<<~~I[<i<<,<_<+l~1-<I'>_<~~;+I__li??->+:?-ii_lI+_<+`;~-;<~,i<~?+~l
                    ...   '   ' ''..  '.  '...' '^... '.   ...'  `  '..`.`^. '`..`. ,"^,'`,,'^,'^^"":"^
           "<iil^  :+!>>+i<i<<:<;"-<<iI-<<~+!>li.><i!i<>!II!i'!i<,!>l_<!iIl+>il~>!!!
           .^^^'.   .^,^,^'^^^ ^' `;"` ^,""^^I^' .'"^^,^;,^,^ :^,.^:^^I";;';;:";,:",
                  :!:  !Il;:'II^Ii:^!l!:";;i;:^l;!lI:I lI!^::I`!i!' Il:`:;I::::"`:^"^I:<;I^I:Il;;`:l::l"
                  ,:,  I!+~<I-<ii_i,i<!;:ll!I<"i!!!!:!`:;l,lIl^I!;^ ,;!,i>!!ll!;:I,!:il~I_:><>>iI"!~l:<I
                       ii;i>!l>i"<i
                    .`' ^'  ..... .'"^'.
                    ;]_.ii~~+>~_+^+_]+~+
                        ;;`''^^``,^".",I:'^^"`^^^'^^^^^^"^.,^"`:^ ''^^'.``^^^.`^"`'``''^"`'^''..''^'..''`'''
                       .?]l,i-<i!~!>l~l?<,+_~<!?ii-~_~>-__,?~_;-_`,:?+!;_~<!<I!--~i>_<<!_~I_[+I;<~~>-;_~~_>i'
                        !~ ; ~! ~-<l.il<+^<i>_;.?~!l;i!>+l<I._i<"_~,>"->'_-_;"~>-+  !>-:!-~~"!>~_i<`?<-]~i'~;
                        _]_~<<+<~_<+;<~<;>~<__~+-i<:>i-~~~iI~_l'.'. ' '' `"^..`'``.  .^''^"^.'`^`';.^"^^^'.^'
                        ::,,"""":,^I,^",',"^::"I:""`"."^"::':;:
                        <>i~; ~^.+; I+~+~<+}>!-><` i_>i~!: ~  >~~<+i-++i<+_-.!?< _--++-[[!~~_",[+-l']{i>i~+_:
                       .+-]++<?_+>?+i,+i;?~iliiii>ii~!+I<~!!>li<<~+>il'.`^^^ `^. '^^`^",,'`"^.'"^,' ,,'.'^",'
                        ^',"":,",:,:^ ,,.;:^::,:::I:,`I.,l,"Il;:;I;:;`
                    "l: l!l^,",:I`";:I"";:":`:"'i!,;;''!I:Il:`.:^`,I^!lIl""::,:!,,;`
                    :>l I!I`l::Il":>!i+:ilIl^II.!<;!i``>!;iI"""<;I::I!il!,l~<li~!;~^
                        !,<!;"i!:^!I,:,l:,;""i;l"':^"!::!,,^><,lI ^i>!ll:`",""I;:i;ll,:I;,!i;:; ^~l;^;l^;!,;`
                       .<><!<!><~!~i_!l-~i_+:<>-il>l<~!i~i{il>!<~;I~li<Il;+~>i;l~>_>!;~__!+<<l+"^>i<I+iI<~<~"
                       .><;.~<<l+<l <`;~!i>]:,_~+<;:><`I!i+l_'+<<~<l'l~]?>_+>+":l'<~";i>_!-`i~<_~i';_<^_!^>~,
                       .>+~_<~_-i                                                         .
                       .I^`^`'"`. ^`.'.''`...'.`.'.'.'. ..'. ''..'.^..^``....'
                       '?<_+~??>  ;~l->>~~:<-li[<<_><+i?++?!l][]:!l?~!++?;i<+]"
                                  .         .          .
                                  ++-";l^--;i?}~+_<-"<+~+<_++<:~`]-[;;{~^-:>-~^_<<<_:i<!I-i~>+?++l"-"~^?->+-:
                                  i<<_<<i;.. . ...." .... '... . '.^..`' ' .''.`'.'..'`.``.''`'`'..' `.``''`.
                                  I:"i;:"^
                                                                        ..
                                                              '+<]__}-<!__<.
                                                            .,;`....... .
                                          '`'`..'''.```... ,_^
                                          <[>-i,~-]>-{[_]+
                                                        <]
                                                       ,`
                                                 Ii;,,;,:~^;li,;l::,i;"!!^;^;I^,,::;;;;"";`
                                                 :i>!,l :i.:i>Ii>I_;ii:l<,!:l~:<i!il><l:!<^
                                  .
                                  +_+~-<<]<<;!~>--!i[+l`?~+:-->?-+-,
                                  ..'',"`'''.'.',^`.`'`.^'` '`.^"':'
                                      '?" . .. ^?>~:>i_~
                                      ^I ..... `<<i"!i<<.
                                      `i^..... `<<ii><>!.
                                      '!` .... .ii!<~l+;













```

*Figure from page 13 (2346x3317 px)*


---



4203-E P-202



SECTION 2 PROGRAM OPERATION



(2) There are two different methods to operate the machine with stored programs.



(a) When one main program is stored in the memory



In this case, it is necessary to assign a file name to the program. In the memory, however, the



program is assigned the file name "A.MIN".



(b} When more than one program is stored in the memory



In this case, a program can be executed in two different ways.



1) One file for one program



Only one program is registered in one file.



2) One file for several programs



More than one program is registered in one file.



In both cases, it is advisable to create the program by assigning a file name on the tape. If the file



name is not assigned on the tape, follow the steps below and assign a file name when storing a



program in the memory.



Press function key [F1J (READ).



Key in the file name following a comma.



",file-name"



@ Press the WRITE key.



With the steps above, the file name is specified and the program on the tape is stored in the



memory.



To simplify program tape management, it is recommended to register one program in one file.



(3) To store program data following the program data already stored in the memory, follow the



steps below.



Press function key [F1J (READ)



Key in the file name and ";A".



",flle-name;A"



@ Press the WRITE key.



When the program is long and cannot be punched on one tape, the second and subsequent tapes



should be read following the above steps.


```text


                                                                                               ",""`, ,``""`
                                                                         .''.``.'. . ''....'.."--?]i_'~I_?[i
                                                                         i1?<i-_+-:>'__?<+?}_]{;i_+?~?+i>~]i
           ^^^^^^```'''```^`^^^^^```````````''''''''''''`````''.''''''''''''''.`'''''..'''`.''`'`' `.''''`''
          .::::::"^^"""^`^",""""^^"^^``^,,:"^^^^^`"^^^``",",:^^"""^"^^^"^``^^,:,,::,"""""",III;I;::,::,,,,:"
                 ^+i  ;>i!i"!iIl>!"!_+!!l!"!li>Il<"!:"!!II<I;~l^;l!l!Il^;!<":l:;l;,I;I;I;I:
                 ^I:  '^,":';:"^l:`,:;;;:,`,;;,;:l`:""!l,;!;^II`,IiIII!"l!!";l;Ii;lll_i>l!!.
                    ll ;>!;I`";I.,;;"',"",::,':':,,":""'l"`':^""^".
                   `>i.,ill;^IIi`:i>,:>:!~li;^i"i!!li,I,ill^!<I;!iI
                       :^,<I"`lI!` ;:"'l:;;;;;,`;"'I,I:: "^!"':;:I,:;:>l"II;l;lI^ ;:"!I^:lI;;;;':::;;:I,.l;"
                       I!l<<!i<~<l;ii!;~~>?_<]-Ii>!-~>[<I->_<"liI>I:l:!i;<ll_I>I" :;"!>";>>Ii!<":l!><!~l'!>!
                       !iI-<<~":;l+>~]i>i"~~:!_I;+~!~.;!<_>~`
                    ^' ``'..  . . .  .               .       `  .. .
                   "]<.i]~_+;i_<~l<+]l:-~<l_>]---i!~I]~~+~I<!]_;i_+~>~_'
                       ^''"^''^`` .''``'``".."^'^'.``'''"'^'''`'.':,``^`'''.'.
                       ill><!i]__:l<~~i]~_<:!_~:+_:~+_<<?_~;!l__Ii[[-+<+I_~--I
                           '   '  '
                       l< :_i+:[[;+~^i<-I+>_}+-~^
                              "'^' `''.``''^,`''.'.'''.''''..'.."`
                             .<>~_"+_~!_<?-+-iI_^~[]??~~-!+;i~];?{i
                       .. .'   .  .               .
                       _i :_~?;~-:~_,_+>+i?l-~~]~_>_,
                             .,^``.,```.``'."'`,`^'''.' '''..''' ....^.
                             .[_>+I~<-;:!>ii+i-<++l:<,+?__?~~_i~:!~-:--:
                       ,^,^":.'``^^ "`'`""^^^",`^''^^`"^:"'.`''``^'^` `^`'`^`'.'^:`.''``.'''^''`''. ^^^'."^.
                       >l~<<~:~-+_~,~!!<--i~?-~l<!l<~_]!~<ii~!--<>Ii?;+-~~]<!?ii!-+,>_<-I>!,~_l+]+< i!i_I~]I
                       I>iIi^<"i<,l~~_<i<>^i;!-~:-__l`~_<<l>+>:++_~;<_-!_,->~I_+~~-,>I_?;l~<l<:?~~~,<-i<~iI!
                       >>!~~~~;!l~-<l_-~<><i...' '^'' '..'. .'.''^'.'''''.`''.```,".`..^..^''`.^.^`.`^`'^;``
                       l,"i",` ''`^".`,"`^":
                      .li. <li>!:i:Ii!l,ii!^-li"l?[i-+!
                       ,;  ,";;I^I:,II:^:I!^I`,,,,I";::.
                       <_. <<~">:i<ll?<:<<i_;i~?<+~><lli<<~<?<
                          .`!>;";::;:'. .' .. . ...'".... ..''
                            !i!,><;~,
                      .i~. <;I;;`II`!<+i<~"III.
                       ;l. ;;i!l^:!"II;;"!^l!>'
                       <<_!.>>";+~<<`+~i!<';?<"_-;;+_i+^<;l_+~~]~_:~>_l+<!:~l~_<~>"<l"<_;!_<<^~"!+i><!,l:+i,
                       i~~>!>+,`^",^'"^^^"''^"''"`'",`".^`^;""^^,"',""'^""^,`Il","',`'^:`^I::':'",,,;^'^`",`
                       ,:l"::;.
                       <~"~i!>--:<!>~i<>I_+~l:>+<i<<>i<i<`i:>">i!liii>!<+ii>;I>ii<<I"!!l,i!i!i>;;l"il;I~l.
                       ."."`^;`,','"I^"'.:;,`.`;",I;"^:^" `.,'""""^"",^,;:`"`';i:::^',""":"il:;``^':",^Il.
                 I-I .i:`<lI:`!;lIlI,"!i>"!!!;l:I":;:^:::l;I:`!l!^:::I:!'"i,;l^,":iI`::;:":" ;":::"l:`
                 :!,  i<l+<<<<~<~ilI:"lii,;!I;!:ii:II;l;>>ll:"i!>:l:l<!<:;>Ili,I;;>>"I!iIl!~^IlI!i,ii:
                     .i<_>";<!;>`
                     .I,  I^`^``""^:"^`,"^'I:"';l;,;:'
                     .:: 'l!!~!:>ll~!l"!><"~"!"<+>!]+l
                     '_! "~Il"!"~I:l>,,!ilI'!Ii"'i;
                      I, `l!i^I^;I:^!;^!!:;^!;I'^l^.
                         .`>_!I+~i~!-^
                     .;" .:'``.""'^!I^`"`.'.
                     .+i `~!<+il_<"+><i!~^+_~
                     '!I:;`;!,^:"::,:,^:^:,:"::;^":":::::`:":,I,:,":'",,":":',l"'",""",",",^"":,"^^"""^"^^".
                     '_>l~ii+>l_i_?~~<l+I~!?<+i<li+l!~i>~l+i>ii>>I!i,i!>;+~~:l~>,<+i>!iI_!<I+i~_~~~+iil-+<+,
                     `_~i!_;;+,I+~>l<<~~-i_l_~;!}~i<;i__~<
                                          '            ..



























```

*Figure from page 14 (2346x3317 px)*


---



4203-E P-203



SECTION 2 PROGRAM OPERATION



(4) When the file name is already registered in the memory and when it is necessary to store a



program with the same file name, follow the steps indicated below to erase the previous



program and to store a new program.



Press function key [F1] (READ), key in the file name and press the WRITE key.



The following message will be displayed on the display screen.



file exist overwrite? (Y/N)



PROO OPERATION



tape file name= TEST9.MIN



TESTS.MIN



file exist overwrite? (Y/N)



TRANSFER VERIFY TEST9.MIN



97/07/15 14:10:00



FAST FAST PIP



READ PUNCH VERIFY CIYY FORW.ARO REWIND QUIT [EXTEND}



@ Type



uy»



and press the WRITE key.



Data in the specified file is erased and new data is read from the tape reader and stored in the



memory.



{Supplement] If data does not need to be stored, type "N" and press the WRITE key.



When a file name is not given on the tape while the name of the file stored in the memory



is "AMIN" (that is, the file is not assigned a file name), it is not necessary to specify the



file name after pressing function key [F1J (READ).



(5) File names can be specified and changed as required by inputting the following.



[F1] {READ) "input file name", "output file name"



When an input file name has not been specified, the file name given on the tape is taken as the input



file name. If no file name is given on the tape, the program is assigned the file name "A.MIN."



When an inputfile name is specified, it is necessary to check that the specified flie name agrees with



the file name on the tape. If the specified file name agrees with the file name on the tape, an error is



generated. (An error message is displayed on the display screen.)



When an output file name has been specified, the specified file name is created in the memory.



When an outputfile name has not been specified, the inputfile name is used as the output file name.



In this case, the delimiter"," can be omitted.



To specify an output file name without entering an input file name, be sure to enter the delimiter",".


```text


                                                                                               `,,,^^` :',,,.
                                                                          '`''`'''... ''...''..i?-]<<!`~I]--`
                                                                         .]]><i+~[i>;:+_+<-]--{~:_~+>_-~li+-'
           '`^^`^^^^^^^^^```````^^^^^^^^^`'``````'`````````'''''''''''''````''..'.''''..''`''''''`.'`'''.'''
           `",:,::,",::""^`""^^""",,"""",""^^``^^"^`^^^,,,:^""^^"^^^"^^^:,,:"`^^""^^^",:,,,,,::","""^,",::::.
                  ;+, '~<!!,;~l">l",l!II,;"~:I!i;';llliIIl^I^l!"^Il:I;;""l;:,i;I,,:I^"I,;;;Il,^!';l,I`;.
                  ,I" `<!i~li<!!~_:~+!i<!~!__~<~+;~-~-?+~<l+II+<I<<ii+<i<~~!<~!~l!!!!l_><+_+<~I+I~<ii,i^
                      "~l<-i<!^~~>">i:!~!i>^_i^l>!~;`+<><ll~~"~+_+;Il<>~?~<;+<i<iI>^~i__;I>il+<i<il<
                      "~i~?>_>;[>~!>"_<i<,<:<~_;~!<?<~i'
                      'I^.`^.  .`. .'.... ..^`..^'"^'` .         .                      . ..
                      `i; "<!_-il>><_<~,-_<:_:~;-?+<?_;;?_I!ll-_;[-:l_~~iI]<<i~+~~;-_;~[}_~{l<+_"
                      '>" '!::,;;;,;:,`"::;,,`;^::,,:`l,,;:"",""^"I"'I:",:,^,:,,:".'`..' . '.'`,.
                      `+: .lI~^!~i>~!+::iii_-?~`~<;<+"-+_>--<+;i!I<~,~+_<?_:_i<+~I
                          ,-!^iI!i^;!!!i!>!":il_I
                          'II^I;;;^:I;,I:l:':,,I;
                                                 ........      .    .......'.       ...
                              `::I;i!l:!!lll!!,:,,,,,,,,Il;!i!I;ll;l:,,""",:;;I!;II;:,;,:'
                             'I 'l~)|[>|}1{<}{"""""""","<)1(1)]>|{_]!,;IIIIl<(){[1{)l!~.'l.
                             ^:  ..           ..........             .'!+~~]<?-l[i>~_[i. I'
                             ^:                                                .         I'
                             ^:                                                          ;'
                             ^:                                                          ;'
                             ^:                                                          I'
                             ^:                                                          ;'
                             ^:                                                          :'
                             ^:                                                          I'
                             ^:                                                          l'
                             ^:                                                          l'
                             `"                                                          I'
                             ^:                                                          I'
                             ";                                                          I'
                             `"                                                          I'
                             '^  .>I  .   '`' .'"^"'^^`                                  I'
                             ^,  .]))li!+`!~<.`^_><I~iI                                  ;'
                             ^"  '-__i?<~;'::,:'", '',I! ^                               ,.
                             ^" .","I,>il:,ii<?"Ii"";iii',^:;;I,^^;;llI`^I^I;;^,;^^^`'`  ^.
                             ^;   :"^  l ,:^'.;`,^^^"` ";" :<?{>:,;:]{<,'! >~i'`I`:",:,. ;.
                              :,'`+~<'."`>-<!`,I_i;;:^'++;."Ii????;,?-l_I: !<I^',,-<<[?:,:
                               ',;^","`,:^^,^`:"^^:``;:^^:^`:"^";^,l:":,`";",::^";:,I,`"'
                                I:_<`>;!I__"!;Ii~+"iI;i_+,!i;~]i;;l:~[>;l!:-+I!I!:?};~^
                                ll>>:>;!!~_:!:!i>+;!;Ili>;l!l<+<I;lI!~i;Il;il,iI!;<-:<"
                      .^. ''   .',''^. .''.`. .^^^^. `'  '  `''''  `'.''  `''`.  `' `.
                      :[: ,-__>^<""_i<l~<~_,+~I!-_~i_;I+_"
                          ^IlI"^`:;:^,:,:!:,,!,`,'"^"",:;:^^^""`^,"^'^'^^^^,`^`^"`'^``''``^^''```'"'```''^^'
                          ;>~-!!I<<i;++<i+<~l+<;<;<i~~~l!~il!++l!]__:<;~_-!>i~!!<~;_-+!l~__-ll-<ii-~~_ili!<+.
                          :>i<i>+l
                            .. ..'
                `[+--+]_>_+[<   ^+;_--:-<+~:~_!i-__i~!>_:<~<<~!"-<-:;};;~<<l~<~~I~+I<?+-_[I>~~"
                .''^^`''.`'``   .^^^^"'^:^^'`^''"^^'^'`^'^^^^,`.:"^' ^.`^^`^^^^".'"^`^'".`.`":'
                                ^]+!_;i!?_:i_i_I~:;~i++>-:Iil_<!<_+!i++-I>~i:><>+,ii~i!?~:_>l>i!Il+<;!i>>!ii
                                ^>.>l~-+<^i>~~Il'+>I~{;~I;il!~<i~~>iI!<?!"><i~~`<l>:>~;i~!<<<+<;>l;+i><[l+~<
                                ,}l:i~iiI"?~~ll>l><l!!>i!i~li~+~_<_<I!~}<i-+:;I'"":^;:':I,;;Il;:,,"!;I:l:"::
                                'i>`l<:l";i!I`iIi!l;~,!;Iill,"i>,l:,:,l~;!il.
                  ;;. ;l;`^""^""''``'`..``'^:`^'''^.`^''.'`.`' ``''`'``  '..':^'."^'^^`'`^`'.
                 '__` !i-l^<>l<l"i~;;_;l_><i<<~:<>>;>>~!_+~"~<,+++!i_<>?l<+<~]<_~<~<;+i>_-i]!
                         ._:;'l~>;l;^`,"""^l:'":,,,'.,^:;^,;;"'",,,,.                      .
                         '_^!"i!iI>!,':lll^i<^I~l!l. :i<<il:!i'>~I>;
                      ;~il:`II^;;:;li^"I;:;":;"",l;Il;`",:,Ii:l.:;"l!:"II;;^I:;:`;:I;:,l:;,I:l!::^,,:I,";;";
                      !_!i<;+>:;]<<l_+!><>~l!~!I<<<<i~;~-<<~~~iI~~i!<!;+><><_!+i;<!ii~i_~?i<!__<i:->i+_li~l!
                      ;!l'l<,i: I^;:,-< I~Ii"!;>~li"`>^Ii!^~~<":~>,ili]l!l"!`!>i~-l<!"ii^i+"I~>l<.>;>_>>.
                      "l;""',"^,""";I'`,""^^"`^,",I":.,^``"`"^"""`^,'":"^",,"^,"`"^^^":^"^:^'^^^^''``'``'":"
                      i?i+-;_<l>_>i!?~l_<>~!<~?+~i~~<;+ii!]><~~__<!~Iii+<<<~+~i<<>]~<<~<~l~+:>?!~I~?<~+>!__!
                      ii!,+<"><i~"lll>i:+<<: <lii,~i<i+<<,i~::<ii!l_<!<>"i<>:>!:+?l;+~i>;~,__i!_~+`><"+lil;~
                      I-+<~i]_+,.<_l:~<>!;<~<i>~];>l<-_~+<<_il~;-~l<[~<~_;>ii~~!l:..'..'.'...'.``''''.'....'
                      :l,^"^,^". "`'',`^' `"^,";I''.`,I"^:",'`^'^"^'^,""I',,`::'^.
                      !]<<+"i_,<~+<il_+:!_>>>:>~I>_-~:l+>><]~~,!_i"~i~!]-<l~_;:~>!+;~:><~-?<Ii;>~i:~<<i><!.
                      '^```.``.'`^``'``''^`'^.'^''^"` ',```'^,'.`".""^`'",''^'."^'^.^.`^^""".'.''`.^"```^"
                      !]_<i;~lI<~->i<+i;+<<+l~?~l~+<__~,!]_~_}++,--<I<<>>~_l!~i<~!il~_+i~!<-<;i<+>><->;>+i-;
                      '''"'.'''`.^"'.````^'''`^'.''``'''`:``'.''..''.'``..'..'.''.''```'`'.'`.``^`'.'`.``'^'
                      !i!+<lI-?]:I-+:-_->+]+^"':++,<?:i~<-++l
                      ^,.''`',^.^' '`'''^"'''''`'`^"''`.``^`^'..`.''.'`,`.''''. '....'.'...'..`'..'''.'...'.
                      ,_I--+i--;]l;i_-~>!]>:++<_:~+_>>>I->-~<+_i-:i_~~!]-;i-~~+`~+I?~_l_l<<_-;~-+I[++i_-i`:^
                                                              .









```

*Figure from page 15 (2346x3317 px)*


---



4203-E P-204



SECTION 2 PROGRAM OPERATION



Example 1: [F1] {READ) BOX-1.MIN, BOX-2.MIN [WRITE]



A program assigned the file name "BOX-1.MIN" is stored in the memory with its file



name changed to "BOX-2.MIN".


#### Example 2: [F1] (READ), BOX-2.MIN [WRITE]

The program is stored in the memory assigned the file name "BOX-2.MIN" regardless



of the current file name.


#### Example 3: [F1] (READ) BOX-2.MIN [WRITE]

The control first checks whether or notthe file name given on the tape is "BOX-2.MIN".



Then, the program is stored in the memory assigned with the file name "BOX-2.MIN".


#### Example 4: [F1J (READ) [WRITE]

The program is stored in the memory with a file name assigned on the tape. If not file



name is given on the tape, the program is assigned the file name "A.MIN".



Example 5: [F1] (READ) BOX-1.MIN, BOX-2.MIN;AI [WRITE]



/ I



Stored in succession with a file name Designates the ISO code.



which is already stored in the memory.



The ISO-coded program data which has the file name "BOX-1.MIN" is stored following



the file which is already stored in the memory with the file name "BOX-2.MIN"



{6) The following command reads a tape which contains wrong codes up to the end while replacing



them with"!".



[F1] (READ) file-name;C [WRITE]



The number of read wrong codes is counted and displayed after the completion of tape read



operation. Correct them in the program edit mode.



(7) Reading of a Tape which has a File Name Punched in the EIA Code



The file name punched in the EIA code can be read if an EIA-coded character which corresponds to



$ has been set at NC optional parameter (bit) No. 31.



File name in



Feed holes $ Feed holes 0 Significant information



EIAcode



EIA corresponding code



The control recognizes the coding system of the file by the first "$" code.



The coding system employed for NC data within the significant information area is recognized by the



first end-of-program code (EOB).



During tape punch operation, the file name is always punched in the ISO code irrespective of the



coding system which is employed to punch NC data.


```text


                                                                                              .:,,"^; ;`","`
                                                                         '`''``'`' . ^`'''''..,?-??>?'~I+_-I
                                                                         <}~~i<~--I<.+~-<_-_+?["!++-+->i<>];
          .^`'''`````^^^^^^^^^^^```````^`````^^^^``^^^^````````^^^```````''''..'''``'...'.'...''''.`'''''`'.
          .,""""""""","""""""":,,^^"^"^^^^^",^",",,,""",^^"":,:""",,","""^"""",:;;;;;;;:,,,,,,,:;;;;;;;;;;;^
                      ~!ii!ii!^: l{;<,-?~<_<,-~!<",l-+<.~_l+:!:+_~,l~<~i++I
                      ::;;,l::'^ ::.:^,,"";:';"^"..^:",',;,:^;`II,`,:,:"^,,
                                 ^;`:":,":^'I"::,::`;;",!^ ",,;^`<l:I'`"ill:`:'I;,;;`:`l:^^:,,,,:``;l"`I`lI`
                                 ;>i_!?_+<!;+<+[~~[i~->l_-l_?!<l'+i!>,,;+i<"'i"~<!~~^i,i>!;i<l!>~I:+<l,_;>+I
                                 "!_l~"I!<i<~>;!l -_I<,<;?++;
                      l""""^:^", '!""'lI"::I'^;":"`^::I"::,;:ll^
                     ._i~~i<_>li ;<:<I+_~<~~:l-i<!il+__i_?~+<>?>
                                 '^.       .'   . .    '        .  . . . .'. .`    .  '`''' ..''.'     ..
                                 ^i~>!~i?_~~!<ii[ii-i!l-~<l_]<_~-l+]?][_-_>i_!--l~-+-i,)+~-I~>{_];l_][~_}+-l
                                 ,~!__;l<~~>i;?~:!_<~>               .'           .                 ^'   ..
                      .          '"'`^^^"^""``^,`':^^,    . ..
                     .]<__<-]i!< +];_l[[--?_;}+~-l<>}-_i1]]-<-?^
                      ..''.`.... `. '.  .  .           ..     '
                                 "<i;:<i<Ii!~i<;_>!<>,><I~!!I^I"lii_>:~i;l>>!l:<l~;"!:<>l!+i!,!"~~l~;!I__~I.
                                 :~<~!;<<i!ii>><<!~i<~i><>!!~>i;~~>~<!;ii!~>i<+~>_i;]!l+~I+_~l<^__i_I<!]?_l.
                                 .,I!;.":;;I:!:l,`:"I>;li";"l!l;!i!!li;I<i!+;i!"il;:ii:l<::<iI!.i>Ii:i;~<i:.
                     '?l>i!!<:ll !+:;"~~liii"~><<i+<'
                     .I,l;,lI"", :^'"",;,,::"l:,,^:;`
                                 ^l;^^"^",,:^^^"l""::,^!!"^::,:":^"I!^""l:^",,:^`:,,,:::","^;"^:""^ ;,","l;'
                                 "l~><i>-+_~l!!>_~>+il;><~!i<i<i<!i_~;i!i~;l_>~<l+~-[<~<l>Il+~!?}?> i;i<I~-:
                                 :<il_`!"+i!~^:!'<>;:_~_.i_i;~!~~>_I^~^_i<~>!_I<~>"?_"!~i~!`+;?__!.
                     .!^"""":'"^ ,l""';;"I:,'I,,:''";;; I,":^"`Il, ^'^;:I,lI"          .
                     '+!+~<_-lil <i;_I<_<~+~:-<>~,:!]~-"-_i_l<;___[][+]_-<i?+.
                                                              .`^^:;<
                                                            ^,,^.  :
                                   i?><>!l!!i<<<i!"~?,!<_;i~+i  '~+i~<~~il~Il-i:>~<.
                                   <}<+i<!-_?}<~?~_~~>-<!+_+__^  ```,^^^`'^''^''^^^
                                             ..   .    .     ..

                                 "!:":il"^,,:,:,"^,,::`:::"^::,,^,,":;",l,`,"",`:l,::'`:II:`"',"^^":^^^^"^`.
                                 :>><>+>li<~+<>+<i{>-i;~+_>><<~~;i->i~<I_~;+?!?:;[~<i":~_++,-!?+i+-~+~>~+i?l
                                 >~>;<<"+l><;;iI?<~<?!;_ii+~ll,__:l~+>><>^+<+:--iI[!"~-!<`!)<~il<_[?+'
                  .   `. ....                                           .             .        .
                 >1!  il~;+>~<___<i~_<<~_><:_-_}I~I]]_I>]~~i:~<<-]<+,_+>i_l><_-~"~_;_I_-l<>~l<_>-I!-_?+<<-^
                 ... ^-i+>"+__,li^... ..'.. .''..' '^'....'..''.'`.' '''."''''''.^".`.'`'`''.`''`..^^`^`';.
                     .,,:"':"^'.
                         -<l;;-{~??<:]-:l_~~~>i![-]_+[]'
                      ^' "..`^''`'^"''^'`"^`^''`^'''.`,.      .
                      ii+':i!<-_l <,:__-`!>l!_;">!<<""l.<il>+><`_l+^_-+_--+-;!?-_'~_>`~<~~-_[~<`!+"?~];:__]:
                     'i<~i_[<<`^_i~i~~!-<~<:!l?~>!~i+i~+l!~}i!<i-<^ ''^''"'' '.'' .'' ''.^`'''. '. `^^..`^^.
                      ",^'""^"  `^^."^''^"`.' ',`""`!"^".`,:'.""""
                 ;<: '!!!l<;I^!lI^~>lI^>>;i:l!!^;,iI,I>lIl,;l;:;II!:I:<l:<i>,lI;<;
                 ::" .:IIlI">":`:'">!;`l:Il""Ii^;`";;^l>,;:`"l:;:!l^,";l";:;^",;>I
                     .>!i"~!^;!i!,I:;I!IiI,">l,~l~":;il'lI^ll";I!ll:i"<l~":;l<il"l~ii!<!"<<l!;;!!!i>i!!i~:!'
                     ^~I+il<ii_li~_!+i_->li~>i>>l<!>~~+i_il+-l+_>:<>!`;:;":;:Il:,:!;I;l;`l:::^,;;:l!!;;;!";.
                     '<`l<",ill`,<;">`i!':~<!:l!:!iI<:>!~"l>iI;!: l;
                  '^^^'^^`^^`^^"^.'`.`.'`'. .'''`'''.'.'.`''''''`^'`""""^`^^`^'`^`^^^^^"""""^^`````````````
                  '^^^^^^^^"^^^`""i>^'l~^";!I:;IIII;l,","<!"""^^``^""""^"","_;{iii""^`^""""^^^^`````'```"""
                      l~>>il!li<, ;;`+^!  !_]!:_-<~:~'   l,   !>!il;!lii^   i`ilI:  I<!li<Iii;;>i;!l<>lI
                      .',""'^^":` I;^-`i  I~<Il~~?:      l:   '`::"',,:;'   i'_>;;  ^:!:"::I:^^::",:I::,
                  ^:::::,,::;;;:;I<il+I<::,,,,:::IlIIII;;<!:::,,"",,"",:IIl;+I_>ii::,""""":::;:""""^^^^",,,
                         .. ......  .,                     ............''... .  ..........''''''''''''''...
                                   ^+i<,!!!!iilll+ll"ll~>
                                    ,^"',:",;i:""I^!^,:II
                     '_i>,i!i~li">!l!!liil;>l`IIi!l,:ll!Il::i!>!:~i"!I;>!,>;<^>i`ll>>'
                     ."^,',"",^" ,"^!:":;,^,,'::;:lI:!::,"'^^^:;.";':;`,:'^"l "^ ,:;I.
                     '~!!:l;<Il:!l<_i;:ili>Iii;lI"!+!:_~>:<?_<,>iI;i!I+i!i>I!<I!!i<l!,~!>!>;!<l!ii!<>><!<_>`
                     ^~><;~i>I]<<~>+~i>l!++_i-_i[+,,^^;;:^::,,`",:";l",:;:,",",""I;;:`I,;::",I,;i::II,:!::;'
                     'lI:^;,"`;:i";~;l;',,l! l;Il!'
                     `I,::I"I!::`;,::I.;II,!!,, !:"I~:"!!;l"I`I>Il;l"l,IIiIl;I^>lI:<iI,I;i;^;I;II;l!I,"!l>I'
                     ^i>>!_ii_~~i+i!+<;_<~I-<><:>>!I_I;<+!_;_l+>+_?i:i;;lI!!,;^ll!"!l::!l<!^;!!<i!!!i;:l;ii'
                     `>i<!<!l<i<<!,!+<<!"i,<l+<<+<~;>:<lIi>:>~;^-+-;















```

*Figure from page 16 (2346x3317 px)*


---



4-4. Duplication of Stored Program



4203-E P-205


#### SECTION 2 PROGRAM OPERATION

To duplicate a file in the memory (MD1 :) or a floppy disk (FOO:), follow the steps below.



(1) Press function key [F3] (PIP).



The function names on the screen will change to those given in item (2) below.



=PIP



MULTI



DATE DIR PIP EDIT PIP LI ST CONDENS [EXTEND]



"PIP>" is displayed.



(2) Press function key [F4] (COPY).



=PIP



Press [F3] (PIP).



FAST RAST PIP



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



Press [F4] (COPY}.



"PIP >" is displayed.



The screen changes to the directory-selection-based file operation screen and the following is



displayed on the screen.



PIP:COPYCO



Enter the device name, MD1: or FOO:. (The default is MD1 :.)



PROGRAM OPERATION



197/07/15 14:10:00



PIP :COPY



CO[I]



INDEX DISPLAY PROCEDURE



[F2] - MD1:*.MIN



[F3] - FDO:*.MIN



TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl] .



OVERWRITE



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS [WRITE] KEY.



DEFAULT DEVICE NAME



1.01:



DEFAULT FILE NAME=



*.MIN



>XCO



f,01 : FOO: COIAIANO OVERWR/ CHAR.



INDEX INDEX INDEX HI STORY INSERT DELETE CANCEL


```text


     .                                                                                         ^,,,`,'':':,"
                                                                         .`'''`''' ' '``''''..'<?-]>-;:~!]-_
                                                                         :[]~ii~~-I+^!~]_~]-+-]i:___>?_><>__
           `^^^`''````````^^^^^`^^`^^`````'```````^``````````''''''''''''''`''.'`''`'. .'.'.'''''`.'''''.`''
           ^,,^,"","^^```^^"""","",^^"^^^^^^,,",""":;;;;;;;;;:,,,;;;;;;;;;;;;;;;;;;;:,,::,,,,;;;;;;;;;;;;;;:
           I;,i    ~+li>>l<~lll`!i:-<lli>l;~lI!l!l!"
           :;,l.   lI!+lll>iIl,`i"^i!!;i>:`";i]!!il"
                 <I`I,l;,!!',"<I';^I;`^::;:::.;>!:^"^I^;:<:;:,`!l!'~!!!:':l;;;^l;,`l;:;^;;I::.
                 ;;"i<<;l><"l,!i^l"li,,li;;!i^I>iI,I"i^!;>>~i>"><<"~:!>l,:<!i<:ii!,+~+<:>+>><`
                  ^,  `;^``'"```:`^.^"'`;:^ ;;I`
                 .!i" :;!<~;;!Ii>i!">+!!<<>"i!<l.
                      `!:"";",!:,.^;:,:,."`lI".,,:;:^";l^;:;:::^:`l,":,`I":"`:`I::`"l^,::":'
                      'l!!,il!+>i^;~<!<i,i:i~>,<!!~i,I>!:il+l]<:>"i!!~!<?!<!"i"<~i"l~;l+<i+:
                                                                                             `
                        ^:    .                                                             '!
                        ^:                                                                  'l
                        ^:   '>I>'                                                          'I
                        ^:   ;I",                                                           'l
                        ^:  ]i,"^,";:,"""::i,"```^^;^``^^^:;,l:;l,I:^^^`^^;^^^":::i:"""",:. 'I
                        ^; `i..``  !" '.'  <. `.'  I ''.' ,Ilf+li.:^   '. I'. ....i . ..  . .l
                        .!`I <}_-. !^ -_-  l .<>!  " ~{I! ^,;><"  ,'';I-" :<_}}})~l._[_]}1i.l,
                          ;~,^`''^`^^`^`'``:""^"^^`^'```^^,:","`^`""":,,"":",^^^^""^:;,:"III"
                          :`.;ll!Il,'!I!!!!`,!!illI'l!>ii!"^i!>!Il.;!l!l!I'!i<>i!^^!l!!ll'
                         'l .-']>;._!i:-]";l<']![ +;<^[-<`~~:!-).~,_.-?] ]I!;]~;,~>^>+| _;
                         I`  llI;lI:'!ll>l!`:l!}<Il.I::,:;"^!I;>l!'Il!!>Il'iI;;:!,"l!l<I!'
                        'I'^` ..''` . ''       ll`"+~]~__+I<_+,                        .
                        :;i?-!il<>??_]-_`       .`^,;lI;:;:,,,".
                  `^  '^'^^'"^^`^'''''.^,''.```"`'
                 '-?^ i>~+_I+++~-_>I_-!-<~ii_<--!+:

                        ;'                                                                  ::
                        :`                                                                  II
                        ^.   ."^"                                                           ;;
                        ^.   !i!I                                                           ,:
                        ^' .<>^^^"":""^"""":""""^"",",,,,":,,,"",,:","`^^^"^^"^^",:,,,,,""  ,,
                        ,' `_   .''!'     ^!.     ";'.  .':` +-]<.!' !}?+^l. >i_^,l'  .     ":
                        ,; ;.~~~!  ,.~i_~:.:"?~lll`" i+-l ^!~}(][>":[]_-?'; i+;l `^:?<>~-<" !^
                         ,l<`Il!;..``,I!l:'"^!I:""`^.:;"^.",;!il!l,,<<Ili^:.Ii"^.^^"i!;liiII,
                          I,`";":;l^`I;:;Il'";,;:I,'Il;:;!``I,,,;;^;l:;;l:`!lI!ll`"l:II!;''
                         'l .~`]<,^~I;i]]^!;-`[<].?:i:{_;:l+:>}}'+^+`[{_'_:!l-~:;!>"~_)._^
                         ;^ .>;!;;I!"!li~:i"i;>!~;>^il<-II":;II>,!.l,Ili:i"iI!!;!:llii-:>'
                        .l .  '..''   ...'.  '.'.'  .'^-;<Ilil~illl!<l:.'  .'''`.  '''.`
                        :,!__;I!><?_~++~.               "Il>il!ll!!!;;I
                      ^;,"^::;;;,";;;;:;^'"."^`."^``^'`.'.' .`...'...'.,`..''''"''..''''' .''''`..``^'''. ..
                      ,>>!"<i~_<::~<+i]+i^+">~<^?+~<+<+l~___~-~ii_??__;__,I-_><{<~,l_>~~~^>+~Il~~"<--~?~-+I<
                      ;_<<~+~+i:<:-_!I+i~+<,                                                             .
                      ",;,^;:,"^^^"'^"'.'''.
                      l>+:i~~<i:;~~.~{
                      ^^`^`'"' ^"'``''```` ^,"^' `.;,"" .""`.'`"`'"''',"^` '
                      <~<]~:>_:~]>~+!:_+>+">[+i:`<,~<+_`,i>-l!_+-+?;~;[?>l"l

                             .":;:,,""",,,,,:"",,,,,,,,,:::::,,,::;;::::,,",,,,,::;;,:,"
                            .I`^l<|)||\<1)))]])I",""""",:;;:;::,",,,"""::,:,""^^,,"::!'^I
                            ,I .,:!>li<i!:;I::;,",""",::,::,;;;:,,,,,";?]~]~][<|--]?{<' I`
                            :l "!<)1i<{{<,,,,,",,,,:,:::::::::::,,,,,:;;;:,!11)r{-};:~' ;`
                            :l ":,+[_    .............  ...............''...       ..!` ;`
                            :l ^,                                                    ;` ;`
                            ,; ":                              . .........         . l` ;`
                            ^" .,^;;I:,:::::"lI;l;ll^^^^^^^^^^^"",:::,"::,""""""""""":. ;`
                            .'   `}(]I>!|?~+;)1_-~_?.                                   ;`
                            .'   "]}:.i'\1il>)-,                                        ;`
                            ^,   :}i_!{!-~>+]\>,?-_+i I+~[Il?__l?l ;>l`.                ;`
                            ":   '}}}l!1];|[_1:_fxi]j!>_+~<|j}:_((;<\1?" [|!>_`i_I      ;`
                            ^"   lt1[_i,)]-[_<|t[,`)(>".'  ``'   '. '''  `^..`.''.      ;`
                            ^"   ;[>~+l`!l!"-1{`,  ,!?<:                                ;`
                            ^"                                                          ;`
                            ^"                                                          ;`
                            ":                                                          ;`
                            :I    ..                                                    ;`
                            ^,  .i_+.                                                   ;`
                            ^: ."I`^``"''````^````````''''^^`````^`'`^"""^""^^^^````^". ;`
                            ,;  .....'!<)i" `Ii[_`.`!-\/}{!~?_1\i;+]{<'`!''.'.^i''''``. ;`
                            'l'  i1-i l :]}_," i1_<^!!+-}];'"-{{-'^}?>>i";_]_~',       'l.
                             ':""",,:^"^^,;;",:":II:,,"":""^",::""^:::I:^":,";^^^""",^:,.
                               `Il>I;;,!!il;,;liilI::l~<;l";;i<:l^!;i<;l"!Iii;l^l!<<Il
                               ;I<+l`+<l>-~"i_:_<>:<>"--;!>!:_[,<;>;-1">!>l+<`<I;l~{'[
                               .::,,:'.:::::'.:"",, ':",:: ^:"":" ","":" ,;::;^ ,,",:^

  .



```

*Figure from page 17 (2346x3317 px)*


---



4203-E P-206



SECTION 2 PROGRAM OPERATION



(3) Enter the file name of the file to be copy and press the WRITE key.



Example: BOX-1350.MIN, BOX-2000.MIN



t t



Input file name Output file name



I PROGRAM OPERATION



I 97/07/15 14:10:00



PIP :COPY



CO BOX-1350.MIN,BOX-2000.MINII]



INDEX DISPLAY PROCEDURE



[F2] -+- MDl :*.MIN



[F3] - FDO:*.MIN



TO DISPLAY OTHER INDEXES, AFTER PRESSING [Fl] ,



INPUT THE DEVICE NAME AND FILE NAME, THEN PRESS



DEFAULT DEVICE NAME = !,01:



DEFAULT FILE NAME= *.MIN



>XCO



MD1: FOO: COMMAND OVERWR/ CHAR.



OVERWRITE



[WRITE] KEY.



INDEX INDEX INDEX HI STORY INSERT DELETE CANCa



@J @J @J (B@J @J @J@J


#### WRITE

I 7 ______,



The program which has the file name "BOX-1350.MIN" is duplicated and stored in the memory with



the file name "BOX-2000.MIN".



While the file is being copied, "COPY" and ''file name" are displayed at the upper area of the screen.



At the completion of copying, ">" appears on the console line.


#### PROGRAM OPERATION

>XCO



>CO BOX-1350.MIN,BOX-2000.MIN



TRANSFER COPY BOX-2000. IN



97/07/15 14:10:00



@J @J @J (B @J @J @J@J


```text


                                                                                              .,:,,^: :'",:'
                                                                         ''''`''''.. ^`'''''..:_-_?~-'+I__];
                                                                         ~[-<i<~+~Ii'+_-~-?-+]?"!_<__-~<~~-:
          .^'`````````^^^^^^^^^^^^````````^^`^^^^^````````````````''''```````''`''`''. ...'.''''`'.''''.'''.
          ',"""""^``"""""",,"","",^`^`^""""","",","^"^,",:",,,,,,""^^":",,:,::,,:;;;;;,,,,,,,:;;;;;;;;:::,:`
                 ^+i  _>~~:!+i:~!^l~!>;:i!<i,_<,i"li";I!;`!;!:lll!"!l,;~><!<l,il^
                 ^;:  ,",:'',,`::'"I";"`"^,;',l`:^"I':;ll.I^;;I;I!":;:"l:I,;:"i>:
                     .]!<<<~_>  _[>-I,~?~l_?[! }+i+,+<~<:[+-"
                      ^^""^:""  lill;,Il1!llII"ii!!ll}~l;!!!"
                                        >.           l`

                                 I~+>>>-!"+_i>"    "+!-~!i<-:;<!!~`
                                 '"I,^'"".::`,.    .",;;:^^:^`;,";.
                       `"""'''''^`. .'`.'^`^^^^""""^^``^"""^`^'``^,::,,""^^^^"""'
                      ::^!i1){{|_[|()-~)~;;;;;;:,,,,,,,::::;I;:,",,",,":,;;,"^I^:;
                     .I  :;>~~~-!><~~l!+l,,"""",,",,,,,,"",,,,,l_?~[<~-;?~_?+[+^ I`
                     'I .Il-_:>{1_"^`""^,:,,,,,:;:::::::,"""",:;!lIl!(||v)-\><_^ :`
                     .I 'l,{i?|_>?1>[_]_/[i[}-~)})<'''''''''''''''..'"",,"^,^`l^ :`
                     .; '; . ..     . . .  . ... `'                           "` :`
                     ., 'I                                                    ^' ,'
                     ': .I^^`^^",,^`^^^``^```^^^^^^^"",,,^^^^^^^^^^""""""^^^^^l' "'
                     `!   .-{[il<-+i_`-{---{}'............. ....  .............  ,'
                     .;   `{}_.;^t1l>I1[! ..                                     !^
                     .;   ^{>~^+,_}l<+|~,"^^:^ ',^,^';,;`"` '^'                  i^
                     .;   .[]->-1}"]}](I:|f?[|I>1<[~]x)_~\|^+(]~" l<,I!.:!:      ,'
                     .:   ^)|]<;i[-]]~>-\\_:]ji^^;"^>>; ';!,"iii^ !+:l<.I~;.     ^.
                     .,   lf[])+`??_>11n~i '_+-<:                                ^.
                     `I   .^''^'  .^ `,^      ^`'                                :'
                     `I                                                          l`       `;:,,";`
                     ':                                                          ,'       ;^ .^ `:
                     `l                                                          ;'       l"l]::I,
                     `!   I-~'                                                   l`       !`,-"^!I
                     `i  "i:,`'`. ''```..'^^^``..''`'... .`''.'^^^^`'''''''''''  l`     ".I<>:!l"l
                     `l .`.  .`I~(l".^l<]<,`:+?|\}1<<[-}|>>+_[>'`<^'...^l`^^^^^. l`   '?]\l-};:>,I
                     .l'  I[-< ;'l?]_,:.!{~i'!<?{{}l":?1)-i,[]<<>;"<_~<':       .!.  ^>^>i^,'^^`;^
                      .,,^,;;;`:``;II""`^;!l":I;,;,:^^:;;:;^llllI""II;I^"'^`'^^,:'   '  `   .  .
                        'll>;:;^ll!iI,"l><lI",l>>ll^;!ii;l'II!i;I^lIli;I^l!>ilI.
                        ,il-l'<!li--^<+:--+"il"~]i;!-^_{:i;<:_{"i!>I~~`~!!i_)']
                         ,:":;".;;;;;'.:",;;.`:"",;.^:,:;, ":",:,.,:,:;:.;I:;;"
                      "'           . .     .  '       ..  .  .      .
                      <>~;>!~+<_!!-~++:!__l+_;--!>-_-_"{+<-:!-?-![-]l;_!_--+_]__I-<>l-_>+_<<;__l!~+<><~I_-+`
                     "_~;_-;i_><_^_]>_!>]]?!_]--" .            .      ...`'.''''.'...''.''....'..''.''^'''.
                     .",`'^`.^"`, '"'`''^^^``^^".  . .
                     ^?+~[!~<>i[l>!i~_>+I><~~<",+<?->l:_i~;]_!!_<+_"++i!]+_~_<_ii_<~~:<-<_Ii<~>;<~_<I~i~~_l
                      ^'^^'.'`'`^`^'^`^;'`^'^`. ^'^   .^'` '^``^``^ ^`^`",,`:""'`^'`"',:""'^^"^'`'^^'"^^""`
                     `]!_+<;~<<?__-<<,~,<~++<~~.;;'??~+__+:~l!+~"i<<~>+I;!>"
                              '"`. ....'''`^'`"''''^"^`^"`.'...```'.`^^^^^^`''.'.  ''.
                            .;,I;<_~+__!_<<>!>i,,,:;,",,:!<i~<>!:!<<I,"":"","l!l:!!IIIl:
                            ;^ ;,~[[?{}!--[?<?-"""""::;;"i[11[}_"~1[!,I<!iil>_/(+t\\1}il:
                            l.                                       'i]<_+i-Ii~l+![+, .i
                            I.                                                         '!
                            "                                                          'I
                            :                                                          'l
                            ;.                                                         ^<
                            ;                                                          ^i
                            ;.                                                         `l
                            :                                                          `I
                            `                                                          `I
                            `                                                          `I
                            ;                                                          `I
                            ;                                                          `I
                            ;                                                          ^l
                            ;    ""'                                                   "i
                            l   ;<<"                                                   "i
                            l   :!,;<I^I<;;!!">i"l>i^ii:                               ^l
                            l  .l!:;i;^;iIlll:i!:!i!">i:      .                        `,
                            l  ^^  '`I:^''`',`  ..."`  .^"i!>i^':;li!^`I;l!!""I"^^```. `:
                            l.  I!!` :',l!I.,`i!:I^I ,ll.'_-)?;II;](_;,;.;~i, ;.,:,:;^ ^,
                            ';"`l<<".,^;>+>^:,~>!I":'!~!``l!~]__!"<]i~~"',+:; :'>_>_[~";.
                              ',,`^:,':;"";:^;^^^:^'I:"";`'::,,,'^:""",`";";;;`,::::"``
                               i,]i'~Ii;_-"lll>~-^iI;>_~"!i:~]l;Ii:_{i;Ii,]+;lI!:-[:>"
                               !lil;<:iIi~:l;!ll<:l:l!i~I;IIlilI:Il!+>l;!I>l,!:i;!~:>^
                                '.'`   '..'  ....'  ....'  '....  '..''  '..'.  '. '.









```

*Figure from page 18 (2346x3317 px)*


---



4203-E P-207



SECTION 2 PROGRAM OPERATION



(4) Press function key [F7] (PIP QUIT).



>XCO



>CO BOX-1350.MIN,BOX-2000.MIN



FAST FAST PIP



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



Press [F7] (PIP QUIT).



The screen returns to the one displayed in item (1).



[Supplement] 1. When the specified file name "BOX-1350.MIN" is not found in the memory, the



message "no file" will be displayed on the command line.


## 2. When the file name "BOX-2000.MIN" which has been specified as the output file

name already exists in the memory, the following message will appear.


#### BOX-2000.MIN

file exist overwrite? (Y/N)



To erase the currently stored program and store the duplicated one, type "Y" and



press the WRITE key.


## 3. The output file name can be omitted when the output file name is the same as the

input file name.


## 4. When the output file name is omitted, symbols "*" and "?" can be used in an input

file name. In this case, all the corresponding files are duplicated. (Refer to Section



5, 3. "DIRECTORY".)


## 5. In addition to the above duplicating functions, the following functions are optionally

available.



(a) [COPY] input file name, output file name ;A



Duplication is executed following the file which is specified as the output file



name.



{b) [COPY] input file name, output file name ;V



The message "copy OK? (Y/N)" is displayed before starting program



duplication.



To start duplication, type «y" and press the WRITE key.



To abort the operation, type "N" and press the WRITE key.



Example 1: Copying A.MIN in MD1: (memory) to MD1: (memory) under the file name of B.MIN



MD1 :A.MIN,MD1 :B.MIN



Example 2: Copying A.MIN in MD1: (memory) to FOO: (floppy disk) under the file name of B.MIN



CO LJ MD1 :A.MIN,FD0:B.MIN



Example 3: Copying A.MIN in FOO: {floppy disk) to MD1: (memory} under the file name of B.MIN



COLJ FD0:A.MIN,MD1:B.MIN


```text


                                                                                               ",",`: ""`,"^
                                                                         .'''''.'' . '`'..''..'-?-]![^<><]+I
                                                                         I{[+!<<~]!_.<+]_~][??{lI-~?~-~+<<++
           '`````^^^^^^^^^^^^```````````^^^`^`^````''''```'''''''''''''''.''''.''.'''...'''.''''''.`'''''`''
           """""""^"::,,""","^^``^^^^`^^,,,,""",^^^^^",;;;:,:,,,"""";;;;;,,,::,,,::;;;;;;;;;:::::::,;IIII;I,
                 '<~  <>ii>:i!l>~l;,!!,<+ll,+><^~i!~>.
                 ';I. "^:;l":I,I;:"^;l,;"^:,","'lI:":`
                        '                                                                   ``
                        "'   :-_~                                                           ;I
                        :`   l"^^                                                           :;
                        :`   I+>")[!,~[-:1~-!1}I<[-<;}!i                                    ,:
                        l^  'i:"`,"`'^""^,^"","^","^^:^"'..    .....    .  .    .. .......  ,:
                        >^ .,:^^``^;^''.'`"l'..''`;l,^^^"^;ii>i"""!I<<~:'^!^!!<I,I~,""^^^"  ,:
                        l"   ",,^  ; ,";,`'i';,^,"": ^,:` ,>~}-^"`:"_}-:^.I !!>: ^< "^^^"`` :,
                        'l^. +-]<  :.i+[-l'l:[_ii!,: >[+; "!>}){{_:"][_~(,^ :?>l.`!'?]<])?>^!.
                          ",,.`.'""^`''.'^^^''.''^",,,^^"^^`^`'",":",^`^^`"^"^",,:,"``'"`":,
                            .!l+<Il""i!<~l!'ll~<ilI`!!<iIi^;!<-~!!.!l<<!lI`il<~ii^:l!!!I!.
                            "~"[i,`i<;<_]'<I~'[<-.-;I;+{:Ii?`~?{ _"_']{].?l!;_!`!<<`--) ~'
                             ;l:;Il`'!I;lII.:l;Ill".lI;;ll'"lI;ll; ;lIIll:'!;I{;l`,l;IlI;
                                                                              ::
                                                                         >!i>I+<ili<:<l>I.
                      l<>:;!liil^l~l;ll;!,il,,Ii"l>i!lIll,I^!!l:"I:      ^`:;,:',"^"':,^^.
                      '"I^":;l!;':i!"";"I^:;"::!^;l<llill^;`;il:^,:
                "<;:;l;,",,I.   ''  "l;^^'",^ ^`"'""^``;`.^"^`'.l;";^^:lI";IlI`^^'""`,^`"^'".,^`'"^"^`^' ;^`
                ;~i~+<<!l<l~^   ^:. I_>>>:!><:_+_~i_~!!-<"<]i~~'+-i<I;+?_!~+_+'!i"__:i~ii<"~`<<<:<_+<+~~'?~i
                                    "!>>i+~-"`l;,-+.;_+^~l"?~+~_>il^>:><l"!l>!<_<~;<i>
                                ,:  ,lI,:`!I""l:',,":^^>l:l^ll;l,lll;',;,,""""`:,""^`,"^";^"'^^^;^'`'^`'`,:'
                                Il  I~!~~:>+<;~+,~_i_!^[~i~I_~~+I++~!^_+~<I:<_II+~~:I_><~++_"~<I_<:i~_+~li}i
                                    ">?i-,><><<+"i>~_<^!,~+lI+~!~i+:!-~,~+<~+<_i;i~~~_--^~+;+__~<-^
                                          !l;l"!l;l,!>!". .  .. ..''  ' ......`` .'''',` '. '^^''`.
                                          ~il>"<>i<;<_~:
                                          ~~"I><<^l!>Iii~~l"~!_-'
                                    ^,.```:;,l;:;^;;lIl";!^",,"l` ..'..'.'.'.. ''. ' .'... . ..  .   '''   .
                                    ,~:+>+_!I+_I!+<<>i~;<-~<_>~<i]+_+!>-<i>-+_!<+~,?_-]~???<I>-i"]??l^~">-~~
                                    I!~+<:<<:i??_~-;<>+`                                          .
                                ,"  ;!I;,";l,,II"^:,:I;""^""`'^^,,^,`,""^`;^'''^''^:"''`^^''`'"'.''``''`."`.
                                ll  "l~!I_]?~!!-i;~>!_,i+il_iI<i~]_<!-i-i;-~Ii>_~~!>?!I__>~I~I~+;~_i+ii?l+-i
                                    :ll~l!-:,+~!<`
                                :,  :><l;">l:::II",li"";;::^;`,;;!:;`^:":;,;^^"^^;",^;"`,,^:,'^,":"^'"'^""^,
                                :,  i-i<<I~~lI<~]>ll+iI~+<_i~:i><_~~;l]<<+i->^i^;-!<'I"l+~:+~l-__~i!;}:l_-<i
                                    i~i"-+!-',i!-<lI+--,I]!+iIli!!>~<>!~<+~~-_l+_i;--__~-_~I ~_~?_;+;~->_<i:
                                    >:,i ii~[[i><>?->"l.                  .
                                :`  ::^;,I!,:";^:;^";^:"',^";"":"^`,'^""^^`.,^`^",'```'^``'^''^.'`'.'^`''``.
                                i;  I;l-~+?<i:~;i<I<+<i<;~<-_<_]>-i<li~+ii_^>_i!--<+<<?!~<>~>>-l++!l+~~<_+-!
                                    i~>_+-++
                                    ....``'^`'..   .'              '
                                    +}":?>+-I_l~]<~!?-:<]<<+'><?_<!+-!;?+!-"<~
                                    .. ':''`'`"'"'`..`''````'"^"^``..^^`'"^.'`'.' .   ..`' ' . ''    .  .`.
                                       "~>?<<__<<"<!!__+<~?+;++_<-l__i_~"?]:<_<~~^+;<__<?]_+:]l~]_"~+-~-;_-I
                                       ,i+>~l                       '                .                ..
                                        .' .'
                                    i<^^+><_!<"!<<i;?~"i<!<<.i!_>!I>-;:<~i>^!l
                                    ",'`:^^".^.',"^ ";'^,'^;.",l;:^`;^^I;^;.^'
                                       'iii :><>>+_]: !><~! i~+i.'~!~+I li i-<_-~~~! +~_>~! i_~+<<i >ii<!~<:
                                       ^_!_~!_-<>,;:' '^"," ```' '``'". ^" ",,:,;,,^ ,,^""^ ^""^^:; ;^"l":^'
                                       ^lll;,lI,^
                                       ^-^;~<<^~!+-!~~!i`l<i<"!i`~iiI>ii<I>~!:-++>-+;~!I.
                                       .,`^,;"`;:::^,""^.`l::  . ;,:`;"::^^":',^"`^"`III
                                       `+:l?l!i!<>`~<<!+_iI >~~>^->`-l~l>i><:<~i:__?i~~"~~l
                '.         .       .  ..`'`,""''`".,,^`^^^`'"I:" `' ,`^^"^""`'^".^'^''".":"
                ?~_?~]?~^l.<~--+>?;_l[?-I<;-1<!';+<<!<!<!:<;[-i>'>~_>i>i~l:!i+~^-<i!-!:~~i-:<i_i>}?~
                .... `..   ..'''.;,`. `^^^''`^^^^`^"``^""^"'''.. `.''.`'"''''`` ''`.``'^^'".`.`''`''
                                `>~!^'I[_>Il!~?+_-(_~l]>+}_i
                :^`^^`,``" ,^``'`' ^`:,"''.","^ .:,,:,`'''..:""` "`... '^'`. ..'..^..`'...... .'".```.
                ~i++!_?>;i.>i~_~i+;i!?~~:!I+-i!':i!~i<!~!;!,><_i^?<+__i!]]-:l~~]+:__li-il-_>_,_![!]+-l
                                .;;"  "lI,'"^:Il:,I;,,I,llI.
                                `!iI"';->;"lli_~il!i>i+l_~_`
                >IIlIlI::l.l:I::,,'l,<!l":^!iI: ;I","`'I,:'",:i!:, ::::,",,^`",:"^I"`II`^,:,,',"!"IIl"
                !l><l_!l:!.l;+<i;+,l;<i!,I,,lI;.!Il<<!">!>";!:~>;;'<l<>lii+,!!<~>,<>;i?I;_+i+:<:_l+~+l
                                `!i:. :<i!,!"<i>"ii:":i:<i~'
                                `II:""":ll:I:iIII]-~>>!;<!!`











```

*Figure from page 19 (2346x3317 px)*


---



4203-E P-208



SECTION 2 PROGRAM OPERATION



Example 4: Copying AMIN in FD0: (floppy disk} to FOO: (floppy disk) under the file name of B.MIN



FD0:A.MIN,FD0:8.MIN



Note that the underlined device name MD1:, which is the default device name, can be omitted.



4-5. Tape Reader Operation Fast Forward Feed



To feed the tape rapidly, follow the procedure below.



(1) Press function key [F3J (PIP).



The function names on the screen will change to those given in item (2) below.



=PIP



DATE DIR



"PIP >" is displa ed.



MULTI



PIP EDIT PIP LIST CONDENS [EXTEl\ll]



Press [F3] (PIP).



(2) Press function key [F5] (FAST FORWARD).



=PIP



READ PUNCH VERIFY COPY



FAST RAST



FORWARD REW l ND



Press [F5]



PIP



QUIT



(FAST FORWARD).



[EXTEND]



The prompt"> FF" will be displayed on the command line (21st line). The tape is fast forwarded to



the end of the tape.



By setting corresponding data at NC optional parameter (bit) No. 1, bit 3, it is possible to select



whether the control recognizes the end of a tape by feed holes or by a code. (% for ISO and ER for


#### EIA).


```text


                                                                                               ^,""': `"'""^
                                                                         .'..''... . '`'...'..`_??]<-`I!<]]_
                                                                         ;{?<!<~<_;_.<+[~~---?{ll_~-<?_<><_~
           `^^^^^^^^^^``'````^^^^^^``````````````^``''''''''''''``'`'''''''``'.'''``'..'`'`'`'`'``'`'''''`''
           "::::,""^"^^`^^""""""""",^^`^,,,:,,"::","^^"^``^^`^^^,,;,"^^^^"^^,::,,,":,"""^",:,:,;:::::^^^,,::
                :~l~>>>+"i'">llli!I;!i-+>,;;>i<"`_l!l!^li<!"i">>i! i<;lI:`>l!"`;:!!^!!:;i,^:I;l^:;>Il>!!
                `::l;Ill^,'`:;l!;;!^,:I::`"^^::``I;iI!^:;!:^!"";I;'!l!<i!"i!i:,l;i>^lil,il,!<I~:l;!I!>l!
                                 li~"''~~_ii!>?-<i<>~;+l?<-,
                                 `^`.`'.'^^`^^^^^^`^,^"^,^".
                ;[~]i<?_>~-+"~+?+<-~+i;_~<~~:i+>+li}+i;.!-<>~,~l-~!!]~-i-:__i+~Il_+i~`;~+:>_"i<>_<<I
                 .'    ..  . . .'...'  '..''.'^ '. '. . '`.'. '..''',^""^.""^""``:,^,'`,,'^:'"^^","`
           !^i"    il:,,'<l,;:l:^"!:",,,l,""  `i"";^I:",^^,"""I^^`".
          ._:_l    l_]~+`i?_?_?]::~?~-<?]<+i.`,i<??;iI->_~[~<;i_]--^
                ';`,^`"':` `''' ```,` ''`''.:^' '..`'`.' `'`''
                '>;l-~<:<+;>-~>:<]<+-:I>>i_;<+I+>><+_-i+I_-+~-'
                  ..  '^  . '  ..    . '`' .^.^.
                 "i<' i!~+_I_><_~<l!__l-<]!>_+_i
                      ',^'"```"``.'`^^"' ^'"'. `'```.'"^.^'`''''''"'''..'''..'.`.' '^.'.'..
                      ">-!i_~<-~<"<-~_?il-;!+<;_l<-~,~]>!<_-<1<!~I-<+?!_-<?lli;]~~;_?;?-~~?`
                         '                                             .                     '
                        'l                                                                  '!
                        .;                                                                  `>
                        .;   'iI<^                                                          `l
                        .;   ,l`,.                                                          `;
                        .;  +>^`^""ll,,,":,;"^`^^,:i"^^^`^:I:<;;!:ll,,^^^"!;,",,"^!"^":::,  `I
                        .l .l.'^". ,, ''^  ". "'^  I '^'` ^:;\~!I ;,  .`' !^``''`'! '.''..' 'l
                         ;";^,]<-^ ", i!_' l..~!>  ; !]i! `,,l<,  :" l;-l l+-{}-1~,.-_+~}{-'I`
                          "+,^"``,:^^`,^^,:"`^''',",",^``"`^`^''"":,::^`^`^`^'``^^:,;,`^",;:'
                          ," I!+->li`>;++>!:,!<~>;i`!l+~<!l^il~~;i^:i<_+li^!l~<<l!`ii++!i"
                          !  +`]>i.-l-'_-l^>~:!>+.>;~.__+._!!:-{";I>"<_1.~!+'?i!.?:,!_1"I!
                         :"  `I"^::" ,;";;I`'l;I1l; ,;,",I" l::;II.'l;:I;;.:;:I;I".II;I;l'
                        .l`ll`.`,`I";"^:'       ,;';+-[<-~+!--+"
                        ^I:<~Il;+>??][]]i        .^`",,,"`"^```^

                 :?>  ~>~~~I_>i_-+li++:[~-:++_?+:i~~_?--_-_+'
                 '"`  ..`^".^^`^^"''":`,.,`^'^"' .'^'^"^^^""'
                        `                                                                   `
                        I                                                                   ;.
                        ;                                                                   ;.
                        ;   .<>~;                                                           ;.
                        ;   ^>^,`''...................'......    . ..    . .    .  ......   ;.
                        ;  '"'^^",:l^''''`II`''`'`!:^'''^"I`^!i<;^l''~+<>II^^i!!^l:`^"^''.  :.
                        l.   l::'  ^.;,;:'""^I:^;'l'.:lI. l,![1]~";"I[][i^, ;<>i I^";,",:". l
                        `;"'^[-]I '^">+?+:^"!]_ii,:'`~-i^.li-]}>]i">{]:~<", _~;: I`!]+i_}-:;:
                          ^"^`^'";:``,^`^:"`^"",,;^^;^'^l;^`,^`""`^,:^,,;"";^",;;,:;``^,'""'
                            ,il?<^i:l;?-_,i">:-<!IlI;~-_^>^i:?1~:i^>I??lll;I~+-:<^i:-]+;~
                            l>l<>^il<,~~_`<:<,~+i;<i:<<]^<,<^>_<^~^i,<[!:~i:~!<`_:<^<?_^?
                             ",^":" .:^"^,' ^,^"",  ,"^^:^ ':"}:"^^:;";i!  "^^":^ `:^^":.
                                                               I`"[-]_<?[i;"::"
                                                                :I_+-~li<--_-?-I

                      i!l,I;:I;;`^^!<I`li;Il^>I;!l:Il";^!l:^::;::;:::I:,"!,:;;I:; `i;",;:,^:"I,::;,,::;;,,:'
                      <i<!->>!+~;,;!!,`>i:!i">ii>~<>!:i"!!!,!!lIl~li;ii!;~:i!!>><''l!!I-_>,<;<~>l<i>~<<_>I~,
                     .>iII>!;;;!~<:_-~;
                     .l".^^I:^'.`^"^"^`",I,".,:;^':^;;^`",,"^,`^^"""^""^.,",':"'.^ ""', "'^.'`^`"^^'^.''"'`'
                     '[],~-?+~?:~>i<_?<><-<?;<_]il?"~~:l--~<i+;+->_<>~_~^-~+"~_, !.+~,_`~I+I_<_-_+~"_:i--~<I
                      <~~~~+!I_~;i>~+>l:_ii-<~++i<~iI~<i!<li__-!!+I?~~i><-~iI>I?l<!>i__'^_li_:i]~;~+<>_]i!~"
                     `]<?l .     ..     ...^ .... ....... ...`...^..''. ..''.'.`''.'''' ..' ' .''.`''.....`
                      "^^"























```

*Figure from page 20 (2346x3317 px)*


---



(3) Press function key [F7} (PIP QUIT).



::?JP



4203-E P-209



SECTION 2 PROGRAM OPERATION



FAST RAST P1 P



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



@J @J@ @J @J



Press [F7] (PIP QUITI.



This completes verification of the punched out program data and the display mode return to the one



in step (1).



4-6. Tape Reader Operation - Rewind



To rewind the tape, follow the procedure below.



(1) Press function key [F3] (PIP).



=PIP



WLTI



DATE DIR PIP EDIT PIP



Press [F3] (PIP).



"PIP>" is displayed.


#### LI ST CONDENS [EXTEND]

The function names on the screen will change to those given in item (2) below.



(2) Press function key [F6] (FAST REWIND).



=PIP


#### FAST RAST PIP

READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



@@J@J@@J~@@J



Press [F6]



(FAST RESIND).



The prompt"> FR" will be displayed on the line (21st line). The tape is rewound up to the beginning



of the tape.



By setting correspondfng data at NC optional parameter (bit) No. 1, bit 3, ft is possible to select how



the control recognizes the beginning of a tape; feed holes on a code. {% for ISO and ER for EIA.)


```text


                                                                                                """^`" ,^`""`
                                                                          .''.''.'. . '''...'.."_-_]<_.~l+-]!
                                                                          >[_<!~+_-;~ +-[+_??-]{;l_+-_?+<-~-I
            '''```^^^^^^^^^`'````^^^^^^`^```````````'''''''''''''''.........''..''''''. .''`.''''`'.'.''''`''
           ."""""""^"::,"""`^^^^^"",,"",""",^^`^:,,""^"",",:;:;;;;;,,,,,:,,,"",,:;;;;;:::::::II;I;;;:,::,,:I"
                  '+i  <ii>i:ilI!!l,I>i`_!i"!+-i"~Ii>l
                  `I;  "^;;I`:;:::;^"li"l^,,;"I``I;;";'
                          `                                                                   "
                          ~                                                                   !
                          <                                                                   l
                          l   '~!i"                                                           l
                          !  .:!'^'''..''''..''''''...'''......   .'.'.    ....   . .......   !
                          !  '^''`""l>`'''``I;^`^^'`;^"`''^"i',>>>:;>^^~~<;I:^,!!I^~"'''`^^.  I
                          !   .;":. ^I':,:"."`","`,." .:;:. !"I?}-I^:^;?-]:"` ;li: <.,"":,,"  I
                          ^I^."]_}: ":,<?]<,^^~~<!!":."_-i^.!<_][+?!"<[],]!"''?>:" ;.~_>~]}+^I"
                           .""^'..^^``^'..`'^``''`'``^^'.``,","`^`.```..^''^,,"^^'^^^`'^^`^",'
                             `!l<i:!';!><<ll'!I>ii!""!!ii;!'I!~_>lI.!;><Il"^!i<<:!'l;l!!!;
                             ll;~> !l?`_+] ~l_^-+i"_>"<<[ <I]._]-.-"~`-)!"->^_>>.-!-'-]].{
                             'lI:Ill."lIllI:.Il;lll``l;,:;I.:lII!l, II,::l^^!Ii[;l'I;,;Il;
                                                                               !"
                                                                          !lll:l~;i<>;!IiI
                                                                          ^,;;,,`,:,,";:""
                       ,"`'.'''''''...'`".'`.. '`'. . ..'..'. ' .    . ...     .                      .
                       !i+!:<__+_--_l+-<-<[[+>I<!~+!+<<<<-~!i<_>~<1++_i>?]~>?~~[_<!]-_?]!<~~]~l+~<+;_![-~i~_I
                      .i:<[-!:>i                               .  `                 .' '.  ... . .  .. ......
                         '.^.  .
           `l^<.   `>;,;",>",:;;:`Il:::,I;",^..:i,,":",,
           ,+;]^   .<-+-i:~+~[+?~^!+]-+<}++~:``I_]__+>?l
                 I;.'`^^^^'^'.^'`.'""'`."`' ``''.` ' ''^``.
                 ;<"i_+~<>l<~;-]_;,~+>_l><<l~!><+_i~!!-_>-:
                   '   ". . ..  '..     ^'' '```
                  l>! ^+i++~l~<<]~~:+]_I}>1I_i-~:

                         ;;                                                                  :,
                         ;;                                                                  ;,
                         ,,   .:^,                                                           :,
                         ,,   Ii:l                                                           :,
                         ,, :l!"`'^^:^^^"""^:^,,,"^""^^^^^^""^"":"^,^^^^^^^,,,,,"^""^^^^^,,  :,
                         :: <:  . ..i`. ....i......";.   ..;`~t<il.!`.   .'!..    "I.        ;I
                         `I^: >_i<  l  iIi  l ^ll: `, -+I: :'ii+`  I ";!_` !<_}+]]l`"?~<~}-! !^
                          '~I",:,;"^;"^"^"`"I`^`^``""';:^`',^^^"`'`,'":,,'^,:;I:;l:`"!I,;<~!:^
                          ';.^I:IIlI';!;;;!,'l;lllI'"!:::l:.;ll;;l^'l:::;l'"l;;;I^.II::;I..
                          l` >^-_i i"<']_i'~!ll_?"!!~`-_-.~;_'-{I"i;;>-1`<i<^]>+'];!:-{i,+
                         'I  ;liI!;!`iIi>!Il,il>];i^;,;I!,l'!,:>lI;"!!i_I<:lIil;,<"!Ii+il!
                         ;^.. .'..'   ....'  .',_,.:l>>;~<I:ii!'..  ..'.'   '''''  .'''''
                        .I:~~;;:+!-_??+_l        "^:Iii;>I!lI;l,
                      .;,,,:""I;:::;;;;:^``'"^'``'`'' .` ''.....^."^''' ''''.'.^''' ^'''''..
                       I!~:>!l~~i:;>~>++">!,>+:>i!~_l:_>"<>~<?]I+;_-~-~I}>+~:>,+[<!;?<l?-+_>
                  .^. .^. . .   '.. .   `'' `'..^.^'''.''.
                  i]I "~~_-<!-<<?_~;]__;_~{I[<__<,]]+-?]-_i
                                      .                                                      .
                         :.                                                                  I.
                         !.                                                                  i.
                         I.   ;ii:                                                           >.
                         I.  '>:I`                                                           l.
                         I. '",''`^";^^^^^^;;^^^"^^;"^^^^^";^^;:I;";^^:;;:;:""I:;"l;,,^"^"'  ;
                         I.   .... '; '... ;l '. '.I` .'`. !.'~]?l.I..+[?l:I ^<~i >"...'...  I
                         ";' .-_1! .,`~}{+;'"i-~i>;".`<]+, I<-]|-[i^>)1I[+", ]<II I.!__>])?,^I
                          `:,","""^^"`^^^^^""^^`^``"^^^^```:":,"""""^""^,""^"::^^`"`^,",,:;;"
                             ,!i>lI;.lIl!!!^^lIlI;l';IlIIl:'!I!l;!`^!lll;I';!Ill!:'!!iil!`
                             i'[~> -;<`]-I`>~,<>].<I~.?-? _li"]1::l>"~]1.~!+'->i.?l;!?):l~
                             :ll:lIl'llIl;l""!lIi;!'Il;IlII'lI:l;l^"!!~}Ii`ll!I:II`!I!<!!,
                                                                      `>^     ...    . .
                                                                      ,"l"`:;,
                                                                      ~[}1<_){!!il.
                                                                      '`,"  "`^"::
                      `>ll"!;ll!l",:><l,i!i>I:<!!>l!!l;!,i!:iI;">I;!llII `i;:,I::`I"!ll;:;!;:,I,Il;;;;;;:I;;'
                      `ii+ii>><_"."^":'^l,:!;:l!i!>i!;;l"l!,l;l"i,;l;I!>'':I!:~>i"!,i>i!i;>I<!!II!iIi<-lli!-^
                      ^!"l!^l-<i
                      `!^`,lI^"',:,:;:,::l,,`lI;^,,:l:^,;I,,;"^,,""",:,^;,",l^.".,:",.:"`^^^^,,"`"'^"""^""^^
                      :]<l_+_i[i><l<<_><<~i}I_-+l<iI+l:-?~<<?l!_+~!~_+>:_>>I_>';^i<I+"!<!<~_-~~+I+I_-__i>~>~'
                      ;~+:!ii_i>:+>i-~i~_>!_+:<+-!!~<-!i>!l-__~^]~+<Ii<-!,_,ll><-?' ~+"+i"-_<,+!~>_+l~<I}><,'
                                    `.         .`    `'. . .'..  ... ...... ....... .. .. ....'....  .' ''.'









```

*Figure from page 21 (2346x3317 px)*


---



4203-E P-210



SECTION 2 PROGRAM OPERATION



(3) Press function key [F7] (PIP QUIT).



=PIP



FAST RAST Pl P



READ PUNCH VERIFY COPY FORWARD REWIND QUIT [EXTEND]



@J @J (ill@ @J @J @J @J



Press [F7] (PIP QUIT).



This completes verification of the punched out program data and the display mode return to the one



in step (1).



4~7. PIP Quit



This sub command quits the transfer mode, and provides a return to the previous program operation



mode.



The operating procedure is indicated below.



(1) Press function key [F7] (PIP QUIT).



;;;pjp



FAST RAST PIP



READ PUNCH VER I FY COPY FORWARD REW I ND OU IT [EXTEND]



"_@J@J@@@J@J ~@J



Q 1s displayed. Press [F7] (PIP QUIT)



The prompt"> Q" will be displayed on the command line. The transfer mode is quit and the previous



program operation mode is restored.



The display screen wHI change as shown to the right with assigned function names also changed.



=PIP



DATE DIR PIP



MULTI



EDIT PIP LIST CONDENS [EXTEND)


```text


                                                                                               ,,",`: ,``^^`
                                                                         .'''`'.'. . '''...'.."]-_]>}'<I+<<l
                                                                         >}+~i>+??:< ~<]<+]]_[1I!-<_<?_><<]i
           ````^^^^^^^^^^^^``````^^^^^``````````````'''''''''''''''''''...'''..'..'''..'''`.''''''.`'''..'''
          .""",:::""::,"""^"``^^^",,"",""""^^^""^,,,",,,:;:,""""",;;;;;,,,,,,,::,,,:;;;;;;;::::::;I;I;:::,,`
                 `~>  >i>i>:>!l!>!,lii^<i<I!<+>"~!l>!
                 `I;  ^^;;I^;;::;;",l!"I^,:;";^`lI:";'
                         '                                                                   ^
                         i                                                                   i
                         !                                                                   !
                         !   .>!>:                                                           <
                         !   "i`"'.................  ...... ..      .       .    .       .   +
                        .!  `,"^^",;l^`^^^^I:"^""'`;^`'`^,:<":<i<::l`^<i<l!;^I>>i:!"````^".  +
                         !    ,'^. ^!."^"` I,`"^'"., .^:,  i^;-[-;";^,[?[Il" ;l>; l.^^^"^^^  <
                         ";`."}_[I "l,+[}<","<[+!<;` "+_>` li]1}-[I"-1[;{i"''?iI" ;.+-<~}{+^;"
                          '"""'''^"""^'''^`^`^^^"''^^,^'`^^^^`'`^'^^`'`,^`^"^`^^`^^"```"`^,,'
                            '!l<i;!^:li<>I!'!I<i!!:^!liiIi'I!+-<!I.!I>>li,"!!<~!!'I;!!llI
                            ;!;+<.Ii?^__} ~l~`]<>`-l:!<1.<I~.-]_._"i,])!"_>^_>> _!<`[?[ }
                            .lI:Ill'"!II!I;.;lIlll^'l;::;I.:l;;ll, ;l;lIl^^!;i};l.:l;Ill;
                                                                              l,
                                                                         lI!!:i~l>>i:>I!;
                                                                         ^";;,:`:;,"^l:""
                      ^^`'''''''`''...`".'^.' '`^.   ..'.... ' ..   . ...     .                      .
                      l!~iI>i~_~--_l<+<?>-}~~;~i-+i~>~>>__li+_>~<{+_~l~[-+>+_>-_<>}___[!><<[_!-_>>l+!~~~!i?!
                     '<"<]?>:ii                               .  '                 .' '.  ..    .   .  .. .
                      . '`^'''`.
          'I'!.   ^<!<^:l`:,
          ^~"l'   "l<i`l-i+l
                ":^` `^" `'^"""^"^`^":.,"^`,^^^:^.`^'"" .```.``'`^^' '.`^'`'.`."^' '''''.' .'..'.'. ..''`''.
                :!>+,++~"~+~~>_<~I!_~-,i+>;-~!~--"l>>_[^:~>ii+><i_-<^~"~-<_!"_,>_~:?~~~~<_:->>]~-~,l[-~<]~+,
                ;>>_}`
                ^,^''`'''^`'..'.''''''...''^.'''`'.'...
                :<_!I_~<~{+_>>~>~-_~~+;~:>+]>]?-<!-_>-;
                      `    ..          .'.  '..    .
                 !+! `?i--+:>i<[++;<__"[i-;-_}l![+~<!.
                 . .    . . . ....  .`.. ...    ..  .
                         ,                                                                  .I
                        .I                                                                  '<
                        ';    ..`.                                                          '!
                        ';   ^~l<`                                                          'l
                        '; ^;:-!``^"^^"""^`^^"^`````'````'`^^^'..'`'`'  .'`'^`'.'''''`''`^. 'I
                        'I >!.  .'`II''...';".  . 'i'.  .',!.;~_~`;; `-+_;>,`!<<:`i`. .. '  .l
                         l'; ^+!>' `^`!i!l.,`!~l"!'^ ^<~l 'i!_{}[>;,i_}_1,l.`~i>` l i>!i<>; ^l
                         .~I`^<i<^'"^'l<iI`"`liI";""."!l".`;;><<i>;^i~i:~,"."<I"'':.>>I;~~i:I.
                         .l'"llll>l^:l;I;l"'Il;;Il":>I;;!:`:;,",;'^!;,";,'"l,",;,^Il,,:I''^`
                         ;^ !:>-<'>:+`]_+^>li;_?;l!!^~+]`~:+^-{I:i,;i?{,ili^?<+`_"i,?}>,_
                        .l  l!!li,<,~;>~~,!;ill~liI!I>!~:<,~:!~!Il,l><]I>;i:i!!"_,<I~->;~
                        :^   ''..'   ^```^  .^`'^'  ^``'^  .^'''`  ```'^'  `.i_^  .`'.'`
                       .!,-li!+-~_+_<                                    :^'' :l'"^^'`'^^
                       ."^,^",,:::;,,`                                  .i!+<li!i<!i:~<>!.

                     .<!>;iI!i>i`""<!,<_!i;l+!i>!l!I;l!<i;l!iil!!!!<!! !>>l!i!!<<,;!li<;i;ll!llli>l:ll!Il;l^
                     .l!<><<<I_>;l!_ll!<!++l~<i+-~~i<i":;"::::"I:;,;,I.`^I:,II;;l^";II!"l;iI:l;I;;II!;!;Il!^
                     '!:I~:i:'li~;iiI:`;Il<^:"^lllIi!,
                     .>lI`!II!I"`;:;II`,l:'l;I:;"`l`:I;;l,I:;i;^IIl;,!~,,l;;I;;;,;::ll:,";;;;:`:l:^";::",::
                      :;!"!i<!>!,iIl>!^l!::I!i!-I:~:il!!i:II:!i^l_!;;<~,l+>i]!>i"!iI<<l;:><!>>,i~i:I!<<<+<!

                        ,`                                                                  ;"
                        :`   ;<!!                                                           :^
                        ;`   i]^'                                                           ;`
                        :`  .l;       .       ...    .....            ..   ..               !^
                        ;^ .",`'`^^l^^`''^"l^`^""^:;"^^^^,!,i>:l,"<""",",I!,"`^^"!i,"^^`^"  !"
                        I"   ^^"`  I  ^^^ 'I '^`' "" ,^`` l.?[i:` > . `^ `!`""^"^I;.^'^^``. I^
                        .l^..-->>  ; '<>! '; ,I!" `` ]+I, ;'I,!   i II><.'i~]1-[[I`;-__]{?I"I
                          ":"``'`"^^^"`'`"^^^^'`^"^^^''`^^^^^^`",::"^^```"^^''`^":"^```'^::"
                            ,!>~>ll.ll<i!l"^!!<<ll';liii!;'!!>!;!`^lI!lI!'I!>i!l;'!;l!;!^
                            +`_~< ~;?']-!'<~;i+]`>!~.]-? ~i>,_}^;I>^~?{ ~l~'[ii._llI-(;;_
                            ,!;:II;.lI;!ll"`!I;!Il':l;;Il:'lI;lIl'^l:,lI!';llIII;'!I;l;!"














```

*Figure from page 22 (2346x3317 px)*
