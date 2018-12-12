## Optical tweezers

### Preparation

Lecture du protocol en profondeur.

### In Lab

#### Première séance

##### observation du montage

Le montage comporte 3 sous sytèmes; l'illumination, la détection de la position et la mesure de la force par rétroréflexion.

![](/home/sebastien/.cache/.fr-72oEET/TPOB-GPH-4102-master/Pince%20Optique/Montage.PNG)

Le laser 5W infra-rouge permet de piéger la particule grace à une grande force de gradient qui dépasse la force de diffusion. (Déviation des photons et conservation de la quantité de mouvement) L'illumination rouge 633 (He-Ne) permet de mesurer la grandeur de la force et la position puisque l'intensité de la lumière diffusée celle-ci est proportionelle à la force et qui est relié à la position. Un photodiode à quadrant permet de trouver une équation qui permet de trouver la position de la bille.

l'illumination sur le dessus blanche permet d'avoir une image du système au plan focal capté par CCD.



**Discussion avec guillaume sur les plans conjugués et matrices**: Guillaume nous a explicité les termes ABCD du formalisme matriciel pour la propagation gaussienne avec l'approximation paraxiale. Entre autre, la condition d'imagerie a été discutée. Le terme B agit en fait comme condition sur le fait que le plan sera conjugué, parce que ce terme fera que les distances  des rayons par rapport à l'axe optique sera complètement indépendant des angles du système à ce plan. 

ON parle également de la correction des objectifs qui sont habituellement corrigés à l'infini.



##### Mesure des pentes de déplacement [V/mm]

Billes utilisées: polybeads polystyrene 5.9um



| Fichier  | Sens | Pente mesuré excel [V/pts] | Pente [V/mm] |
| -------- | ---- | -------------------------- | ------------ |
| Bille003 | y    | -2.87*10**-6               |              |
| Bille009 | x    | -8.64*10**-6               |              |



La vitesse du moteur en y : 0.003mm/s

La vitesse du moteur en x: 0.006mm/s

Vitesse d'acquisition 10kHz

Nombre d'acquisition 65000

Temps d'acquisition: 6.5s

distance parcourue y: 0.003*6.5 = 0.195mm

distance parcourue x: 0.006*6.5 = 0.39mm

Résolution Y: 65000/0.195= 333 333.3 points/mm

Résolution X: 65000/0.39 = 166 666.6 points/mm

Volts/mm en Y: $2.87\times10^{-6} \cdot 333 333.3 = -960V/m$

Volts/mm en Y: $8.64\times10^{-6} \cdot 166666.6 = 1440V/m$

 

Une première mesure de la constante de rappel a été faite. Le fichier donné est *rappel1.txt*.

#### Deuxième scéance

##### Mesure Constante de rappel

Maintenant, afin de s'assurer que cette constante de rapelle est connue, nous pourrions observer sa variation selon la puissance du laser infrarouge. De cette manière, pour de futures expériences, si la trappe optique est trop forte et que les déplacements ne peuvent être mesurés, la puissance du laser pourra être ajusté.

| **Puissance laser** [W] | fichier données | déplacement [m] | Constante k |
| ----------------------- | --------------- | --------------- | ----------- |
| 2.0W $\pm$              |                 | $\pm$           | $\pm$       |
| 2.5W $\pm$              |                 | $\pm$           | $\pm$       |
| 3.0W $\pm$              |                 | $\pm$           | $\pm$       |
| 3.5W $\pm$              |                 | $\pm$           | $\pm$       |
| 4.0W$\pm$               |                 | $\pm$           | $\pm$       |

*S'assurer d'écrire les incertitudes sur la puissance du laser et sur les déplacements en X pour pouvoir mettre une incertitude sur la force du moteur bactériel à la fin! Les incertitudes des éléments mesureés pourront être calculés par la suite, mais les incertitudes qu'on ne peut pas mesurer en dehors du lab doivent être prises en compte*

##### Mesures Sur la bactéries E.coli:

afin de déterminer la force du moteur bactériel de Ecoli, la même technique sera utilisée, la bactérie sera trapped, puis ses déplacement seront analysés. selon l'étalon mesuré avec la bille, on pourra déterminer la force qu'exerce la bactérie qui essaie de bouger.



##### Mesure de la vitesse de rotation de E.coli

.La plupart des bactéries seront immobiles, mais certaines tourneront sur
elles-même étant accrochées à la lamelle par leur filament (elles sont dites tethered). c'est avec celles-ci qu'on mesurera la vitesse de rotation.



##### Mesure du Couple du moteur flagellaire