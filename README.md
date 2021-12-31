# Island of the Dead Kings (IDK)

## Présentation générale

Pour commencer merci à KikooDX qui m'a donné le titre. IDK est un jeu de rôle en Python pour Graph 90+E sur fond de mythologie nordique. Le but général est divisé en deux : s'amuser avec la mythologie nordique d'une part et réussir à finir la quête principale d'autre part.

Seule la version de démonstration est jouable à ce jour.

## Licence

La totalité du projet est sous licence GNU General Public Licence v3.0.


## Comment jouer ?

### Installation

Il faut placer le dossier `idk_demo` à la racine de la Graph 90+E. Ce dossier contient déjà tous les fichiers du jeu ainsi que le moteur. (le dossier de la version démo fait environ 170 kio tout compris)

### Lancement

Allez dans le menu Python, ouvrez le dossier `idk_demo` et lancez le script `idk.py` (via [F1]). Une fois le script importé (cela peut prendre quelques instants), exécutez la fonction `idk()` et suivez les instructions.

### Contrôles

Pour interagir, le joueur doit entrer le numéro ou la lettre correspondante puis appuyer sur [EXE] pour valider.
 - 1, 2, 3 5 : se déplacer
 - 4 : statistiques du joueur (nom, vitesse, agilité, attaque, défense, points de magie et de vie)
 - 7 : les sorts connus du joueur
 - 8 : informations générales (nom du monde actuelle, période de la journée et heure, classe du joueur et pièce d'or)
 - 6 : inventaire (arme et armure)
 - 9 : dormir (permet de passer le temps d'un certain nombre d'heure
 - q : quitter

Lors de certains dialogues vous pourrez être amené à choisir une réponse parmi une liste, entrez alors le numéro de la réponse que vous voulez et validez avec [EXE]. Entrer aucun numéro fait quitter le dialogue.

Les PnJ sont symbolisés par le caractère `*`, les `?` sont des points d'intêrets qui fournissent une description des lieux environnants. Les `^` sont les portes.

## Scénario et mécaniques

### Mécaniques

#### Auberges et tavernes

Il existe de nombreuses auberges dissiminées un peu partout dans les neufs mondes. Dans chaque auberge, vous pouvez acheter à manger (ou boire, voire les deux) et dormir. Les effets sont globalement similaires : vous gagnez en vie et perdez en argent.

#### Armureries et forges

Plus rares, les armureries et les forges sont des lieux où vous pouvez acheter des armures et des armes. Si vous possedez déjà une armure ou une arme, vous serez invité à la vendre. (Vous amusez pas trop non plus, vous revendez à 80% du prix d'achat)

Certaines armes vous seront données à l'issue de quêtes.

#### Librairie

Des lieux assez rares également où vous pouvez acheter des sorts. Vous ne pouvez pas connaître plus de trois sorts. Si vous connaissez déjà trois sorts, vous serez inviter à en oublier un grâce à un rite d'oubli qui n'est pas pratiqué partout.

Les sorts sont répartis en 5 niveaux. Plus le niveau est élevé, plus le coût en points de magie est élevé, plus le prix d'achat est élevé, mais le sort est plus puissant.

À l'instar des armes ou armures, les sorts peuvent aussi être gagnés à l'issue de certaines quêtes.

#### Les points de magie

Les points de magie sont sollicités lorsque vous lancez un sort. Ils sont régénérés avec le temps.

#### Le temps

IDK est muni d'un système d'heure in-game. Cela permet plusieurs chose, notamment de faire varier les dialogues de PnJ. En effet, les différents magasins ont des horaires et les PnJ refusent tout simplement de vous répondre s'ils ne sont pas ouverts.

De plus, ce même système est à la base de la régération naturelle du joueur (lorsqu'il dort, le joueur guérit et récupère un peu de magie). À noter que dormir dehors est moins efficace que de dormir chez soi ou dans une auberge.

#### Les cartes

C'est le gros point fort du jeu, les cartes sont assez grandes. Il y a une grande carte par monde (soif neufs cartes) et chaque monde est muni de maisons ce qui porte le nombre total de cartes explorables à 48.

Se repérer et se déplacer peut se révéler être long et c'est loin d'être évident de s'y retrouver au début. Comme souvent dans mes jeux, j'invite le joueur à jouer avec un crayon et un papier pour noter au fur et à mesure le monde dans lequel il est et où sont les points de passages vers quel autre monde. De même, tous les mondes ne communiquent pas entre eux, il est parfois nécessaire de passer par un autre monde pour aller là où on veut.

Les points de passages sont quasiment une mécanique à part entière. Dans la mythologie nordique, les mondes sont reliés par des sortes de portes cachées. N'ayant pas voulu rendre la tâche trop facile pour le joueur, ces "portes" sont cachées dans IDK aussi. Dans certains mondes, plusieurs indices permettent de deviner où sont les portes (dans les mondes que le joueur est sensé découvrir en premier). Dans d'autres mondes, trouver les points de passage peut s'avérer plus délicat. À noter que ces points de passages n'ont pas non plus fait l'objet d'une recherche très poussée pour les cacher au maximum.

#### Les combats

Rien de très original de ce côté, au vu des limitations du Python embarqué, il s'agit d'un système de combat au tour par tour. Vous pouvez choisir entre 4 actions :
 - attaquer
 - lancer un sort
 - fuir
 - voir les statistiques (met le combat en pause)

Le système de combat ainsi que les statistiques du joueur sont tirés des premiers Final Fantasy.

### Scénario

#### Mythologie nordique

Le jeu est évidemment en lien avec la mythologie nordique, cependant, plusieurs liberté ont été prise. Certains évènements mal documentés ou sur lesquels les sources divergent peuvent être mal rendu. Certains autres évènements ne sont pas représenté, le but n'était pas de refaire la mythologie, mais plutôt de rendre une ambiance.

#### Les quêtes

Le jeu est constitué d'une quête principale qui s'articule autour de la mythologie nordique. À plusieurs moment, la quête se suspend. Le joueur a alors la liberté de poursuivre la quête principale ou d'essayer de trouver une quête annexe. À chaque interruption de ce type, le joueur à le choix entre au moins deux quêtes annexes. 

Ces petites quêtes ne sont pas du tout en rapport avec la quête principale, elles permettent essentiellement de récupérer de l'argent ou des conseils. Et elles sont en général plutôt courtes. Néanmoins ces quêtes restent rares (ou dur à trouver comme vous voulez) en effet, lorsque le scénario se met en pause, les débuts des quêtes annexes ne sont pas forcément dans le monde dans lequel vous êtes (elles sont alors dans un monde adjacent).

Mais comme je le disais plus haut, ces quêtes sont purement facultatives et vous devriez pouvoir survire sans elles.