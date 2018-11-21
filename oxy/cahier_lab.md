## Oxymetre

Dates : 20 et 27 octobre 2018

But principal : 

### Preparation



### In lab

Générateur de fonction : broche 4 et 2 branché a l'oscillo, 2.5V, 
​     temps UP = 11ms, temps DOWN = 19ms -> duty cycle = 11/30 = 36.7% _l¨l__l¨l
​     phase entre les 2 en degré = 168, devrait etre 120 pour cycle 33%

Broche 4 de la carte a broche 2 oxymètre, broche 2 carte a 3 oxymètre
​     On voit la DEL rouge qui clignote, mais on a pas assez de noirceur pour vérifier 
​     Ou est le ground?? : pas besoins, circuit flip et un devient ground de l'autre (insane)

**Discussion dan :** 
transimpedance passe de source de courant (photodiode) à voltage
"facteur de gain" du transimpédance = resistance en haut = 1Mohm

haute fréquences (AC) ignore condensateur, le voit comme un fil
basse fréquences (DC) voit un circuit ouvert.
  -> filtre rc avec condensateur vers ground : passe bas, rc avec résistance vers ground = basse haut

condensateur vers ground = short le bruit haut fréquence : bypass condensator
Si fréquence plus petit que fréquence de coupure, on estime en DC

**Détection**
Fabrique le circuit de détection sans le filtre RC passe bas. On affiche le signal qu'on envoie a la DEL et le signal recu par la photodiode. 

    - Signal DEL : carré expliqué dans générateur de fonction
    - Signal recu : au départ, ligne horizontale et non ondes carré déphasé du signal DEL. On essaye de remplacer les                     pieces, mais en changenat le step vertical on voit des step mais qui ne sont pas tout à fait carré. 
    - En ajoutant le cap-ranger, le signal est encore plus bruité initialement, et augmenter la capacitance transforme le signal carré l¨l_l¨l en vague /\/\/\. Ceci est lorsque l'op-amp est **fermé**.
    - Lorsqu'on ouvre lalimentation du op-amp, le signal sature a environ 9V.

On remarque que pour que le courant DC continue, il faut un load au bout du courant avant l'oscilloscope, sinon le courant DC a nulpart ou aller. on ajoute 1kohm

De plus, On soupconne que le signal sature a cause que la résistance est trop grande. On la descend a 1Kohm
si on estime une puissance de 1mW de la Del, et photodiode génère environ 0.5A/W. on a donc 0.5mA ce qui devrait donner un voltage de V=RI = 0.5mA*1kOhm = 0.5V. On detecte toutefois 8.5V constant en dc, alors ou la DEL emet beaucoup plus ou il y a un probleme avec le circuit/l'ampliop. On descend la résistance a 100 Ohm, mais maintenant on a un courant DC qui est a 4.3V. Il semble donc que ce n'est pas un problème de saturation, surtout que l'expérience demande l'utilisation de 1MOhm au départ. On essaye a plusieurs reprises de changer des pièces, changer les ground, changer les résistances mais le signal a la sortie lorsque l'ampli-op est ouvert un toujours un signal DC. 
Le signal sans ampli-op semble suffisant? 

Si on met nottre doigt entre le load de 1kohm ajouté avant l'oscillscope et le résistance du trans impédance avec une certaine force, le signal devient carré et très stable. Si on pese plus fort le signal sature, si on pese moins fort le signal devient nul. Il faudrait donc augmenter la résistance?