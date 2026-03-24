class: middle, slide_title

# Programmes coopérents 🚀

## Introduction réseaux 🕸️

<p> <strong><i>Basile Marchand</i></strong><sup> 1</sup></p>

.footnote[1 - Plateforme SISDev, Centre des Matériaux, MINES Paris - CNRS - Université PSL]

---

# La coopération - mythe ou réalité

.center[
<img src="media/architecture.svg " style="width: 80%;">
]

La plupart des systèmes informatiques/services web que vous pouvez utiliser quotidiennement ne sont pas **une** application mais un **ensemble** d'application qui intéragissent entre elles.

---

# A l'issue de ce cours

Le modèle coopérant le plus courant dans le monde de l'informatique met en jeu le concept de **réseau**. En effet dans le monde actuel tout est interconnecté via des réseaux. Et grâce à ce réseau il est possible de connecter tout un tas d'applications entre elles.

Cela introduit alors tout un tas de questions :

- comment communiquer entre deux applications sur un réseau ?
- Comment envoyer un message d'une application vers une autre via le réseau ?
- Sous quel format envoyer ce message ?
- Comment fait-on une application Python capable d'écouter sur le réseau ?

---

# Quel modèle de coopération ?

---

## Client-serveur

.center[<img src="media/client-server.svg" style="width: 50%;">]

---

## Architecture trois-tiers

.center[<img src="media/architecture-three-tiers.svg" style="width: 50%;">]

---

## Architecture pair à pair

.center[<img src="media/peer-to-peer.svg" style="width: 50%;">]

---

# Le Web

.center[<img src="media/web.jpg" style="width: 40%;">]

---

# Le cloud

.center[
  <img src="media/nocloud.png" style="width: 40%">
]

<!--
<div style="position: absolute; top: 25%; left: 75%;">
<img src="media/logos/logo_cmat.png" width="200px">
</div>

<br>
Centre de recherche commun MINES Paris - ARMINES et Unité Mixte de Recherche CNRS (7633).
<br>
<br>
Thématiques :
.center[Matériaux, Énergie, Durabilité, Sûreté]
<br><br>
Quelques chiffres:
- Création du centre en 1967 (initiative MINES Paris / SNECMA)
- Effectifs : ~ 200 personnes
  - 45 EC ; 35 ITA ; 80 Doctorants
- ~50 partenaires industriels
- ~60% de l'activité sur contrats directs avec les industriels
- ~100 publications dans revues internationales par an
- 20~25 thèses soutenues par an
- ~ 4 brevets déposés par an
- 2 Chaires en cours

<div style="position: absolute; bottom: 20%; left: 50%;">
  <i class="fa-solid fa-location-dot"></i> Actuellement à Evry mais déménagement sur le campus<br>de Versaille Satory prévu pour été 2024.
</div>

-->

---

#

.center[
<img src="media/orga_cmat.png" width="70%">
]

---

# CMAT et enseignement

- Programme Gradué PSL : Ingénierie, Sciences appliquées, Innovation
  - Master PSL : 2 mentions
    - Science et Génie des Matériaux (porté par le CMAT)
    - Énergie
  - Cycle Ingénieur Civil MINES Paris
    - Mécanique des Milieux Continus
    - Mécanique des Matériaux solides
    - Matériaux pour l'ingénieur
    - Informatique
    - ~ 10 enseignements spécialisé
    - Métier de l'Ingénieur Généraliste
    - 2 Options (Matériaux ; Ingénierie Digitale des Systèmes complexes)
    - 3 trimestres recherches
- Mastère spécialisé : Design des Matériaux et des Structures
- Formations doctorales :
  - Microscopie / caractérisation
  - Informatique scientifique
  - Simulation numérique

<div style="position: absolute; top: 20%; right: 10%">
<img src="media/school.png" width="200px">
</div>

---

# CMAT et recherche

Assurer l'intégrité des matériaux et des structures par la prédiction et l'augmentation de la durée de vie
.center[<i>Vieillissement, Endommagement, Mécanique de la rupture</i>]

Améliorer les propriétés matériaux pour élargir leurs champs d'application
.center[<i>Allègement des structures, optimisation de microstructure, contrôle des procédés, <br>évolutions microstructurales au cours du viellissement en service</i>]

Développement de nouveaux matériaux
.center[<i>Matériaux biocompatibles, nouveaux alliages</i>]

Développement de nouveaux procédés
.center[<i>Selective Laser Melting, Cold Spray, Metal Binder Jeting</i>]

Développement de nouvelles approches de modélisation
.center[<i>Formulations EF, Réduction de modèle, Science des données, outils numériques</i>]

Quelques distinctions : <br>
2021 médaille d'argent CNRS S. Forest ; 2017 Prix Jean-Mandel T. Morgeneyer ; 2018 médaille de bronze CNRS V. Yastrebov ; 2018 Médaille Bastien et Guillet A.F Gourgues ; 2020 Médaille de l'académie de l'air et de l'espace G. Cailletaud.

---

# Moyens de calcul

.columns[
.fifty[
Un cluster de calcul auto-hébergé

- 43 noeuds de calcul Intel
  - (2x) Processeur Intel Xeon (12 coeurs)
  - 256 Go de RAM
- 4 noeuds de calcul AMD
  - (1x) Processeur AMD Epyc (48 coeurs)
  - 256 Go de RAM
- Réseau mellanox 25 Gb ethernet
- Stockage distribué Panasas 160 To utiles

<br><br>

~30 utilisateurs
<br>
<br>
Taux d'occupation moyen sur 2021 ~75%
]
.fifty[
Types de calculs :

- Simulations éléments finis :
  - Z-set
  - Abaqus explicit
  - Castem
- Analyse d'image
  - Matlab (génération de maillage)
  - Python
- Autres :
  - Optimisation : identification de paramètres
  - Analyse de sensibilité
  - Contruction de méta-modèles (krigeage, TT, ... )
    ]
    ]

---

# Outils de calculs

Le principal outil la suite logicielle Z-set, co-développement Centre des Matériaux et ONERA.
<br>
<br>
.center[Code de calcul éléments finis, dévéloppé depuis début 90 en C++ et constitué de plusieurs modules]
<br>
<br>

.center[
<img src="media/zset_apiculteur.png" width="55%">
]

.footnote[Projet en cours : depuis un an développement d'un nouveau code de calcul pour remplacer Z-set.]

---

# Calcul parallèle distribué

<div style="position: absolute; left: 5%; top: 15%;">
  <img width="100px" src="media/aube_dd.png">
</div>

<div style="position: absolute; left: 20%; top: 15%;">
<p>
  Comportement type AM1 <br>
  Discrétisation spatiale : 7 Mdofs <br>
  Discrétisation temporelle : 28 incréments
</p>
</div>

<div style="position: absolute; left: 20%; top: 30%; text-align: right;">
  <p>
    Résolution solveur MUMPS distribué <br>
    32 sous-domaines <br>
    4 coeurs/sous-domaine
  </p>
</div>

<div style="position: absolute; left: 5%; top: 45%; z-index: 3;">
  <img width="300px" src="media/aube_dd_2.png">
</div>

<div style="position: absolute; left: 25%; top: 65%; z-index: 1;">
  <img width="300px" src="media/aube_dd_1.png">
</div>

--

<div style="transform: rotate(-40deg); opacity: 0.9;position: absolute; left: 15%; top: 25%; border: 1px solid darkblue; border-radius: 10px; padding: 2pt 10pt; background-color: aliceblue;">
  <p style="opacity: 1; color: crimson; font-weight: bold; background-color: aliceblue">
    5 heures de calcul
  </p>
</div>

--

<div style="position: absolute; left: 65%; top: 15%;">
<iframe width="420px" height="315" src="https://www.youtube.com/embed/90-kA3wYuoM?autoplay=1&mute=1&loop=1&controls=0&playlist=90-kA3wYuoM">
</iframe>
</div>

<div style="position: absolute; left: 55%; top: 63%; text-align: right;">
Comportement élasto-plastique <br>
Grandes déformations<br>
Discrétisation spatiale : 10 Mdofs<br>
Discrétisation temporelle : 222 incréments<br>
</div>

<div style="position: absolute; left: 55%; top: 80%;">
  <p>
    Résolution solveur MUMPS distribué <br>
    48 sous-domaines <br>
    4 coeurs/sous-domaine
  </p>
</div>

--

<div style="transform: rotate(-40deg); opacity: 0.9;position: absolute; left: 55%; top: 55%; border: 1px solid darkblue; border-radius: 10px; padding: 2pt 10pt; background-color: aliceblue;">
  <p style="opacity: 1; color: crimson; font-weight: bold; background-color: aliceblue">
    90 heures de calcul
  </p>
</div>

---

# Mécanique du contact

Prise en compte à différentes échelles des phénomènes de contact

.columns[
.fifty[

.center[<img src="media/contact/basava.png" width="80%">]

Thèse B. Akula 2019
]
.fifty[
.center[<img src="media/contact/andrei1.png" width="40%">]
.center[<img src="media/contact/andrei2.png" width="100%">]

Thèse A. Shvarts 2019
]
]

.footnote[Thématique portée par Vladislav Yastrebov.]

# Mécanique de la rupture

Z-cracks: propagation de fissures de fatigues

<div style="position: absolute; left: 10%; top: 25%;">
  <iframe width="420px" height="315" src="https://www.youtube.com/embed/jFLLajbg38E?autoplay=0&mute=1&loop=1&controls=0&playlist=jFLLajbg38E">
  </iframe>
</div>

<div style="position: absolute; right: 10%; top: 25%;">
  <iframe width="420px" height="315" src="https://www.youtube.com/embed/vy2VRuaQL7A?autoplay=0&mute=1&loop=1&controls=0&playlist=vy2VRuaQL7A">
  </iframe>
</div>

.footnote[Développement V. Chiarrutini (ONERA)]

---

# Rupture ductile

Modèles d'endommagement, milieux poreux (modèles Gurson)

<div style="position: absolute; left: 6.5%; top: 20%;">
<p>
Par exemple calcul plastique poreux (Gurson) <br>
Éléments finis mixtes U-p <br>
3 Millions de dofs
</p>
</div>

<!-- <div style="position: absolute; left: 50%; top: 35%;">
<video controls autoplay loop src="media/output.ogg" width="500px">
</div> -->

<div style="position: absolute; left: 50%; top: 20%;">
<iframe width="500px" height="380" src="https://www.youtube.com/embed/4r6frld1UNE?autoplay=1&mute=1&loop=1&controls=0&playlist=4r6frld1UNE">
</iframe>
</div>

<div id="plot_eu" style="position: absolute; left: 10%; top: 40%;"> <!-- plotly -->
</div>

<div style="position: absolute; left: 5%; bottom: 15%">
Des travaux récents (Thèse A. El Ouazani) sur la transition endommagement rupture et l'insertion/propagation de fissure
</div>

---

# Homogénéisation Asymptotique

Homonégénisation et relocalisation des champs jusq'au 3ème ordre

<div style="position: absolute; top: 25%; left:5%">
<img src="media/mouad1.png" width="500px">
</div>

<div style="position: absolute; top: 10%; left:60%">
  <img src="media/mouad2.png" width="400px">
  <p  class="legend">Champs relocalisés vs solution exacte</p>
</div>

<div style="position: absolute; top: 58%; left:55%">
  <img src="media/mouad3.png" width="300px">
  <p class="legend">Champs relocalisés et corrigés aux bords et carte d'erreur</p>
</div>

.footnote[Thèse de Mouad Fergoug, thèse CIFRE Safran Tech, encadrement S. Forest, B. Marchand]

---

# Méthodes de réduction de modèle

.center[
<img src="media/model_reduction.png" width="65%">
]

.footnote[Thématique portée par D. Ryckelynck, P. Kerfriden, L. Lacourt]

---

class: middle, center

## Merci pour votre attention 

