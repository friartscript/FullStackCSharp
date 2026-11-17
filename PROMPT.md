# Directives de Développement — FullStackCSharp (.NET C#)

Ce document définit les règles de développement impératives pour le projet **FullStackCSharp** (écosystème C# / .NET moderne Fullstack).

---

## 1. Séparation Stricte des Logiques

- **Découplage Front / Back / Métier** : Séparation stricte et étanche entre l'interface utilisateur (Frontend), l'API / exposition des points d'accès (Endpoints / Contrôleurs), la logique métier (Services de domaine, Interfaces) et la persistance des données (Infrastructure / Repositories).
- **Modèles & DTOs Dédiés** : Les modèles de données exposés (DTOs / ViewModels) sont strictement isolés des entités internes du domaine pour garantir la sécurité et la clarté des contrats d'échange.
- **Indépendance des Dépendances** : Utilisation systématique de l'injection de dépendances (IoC / DI) et de l'inversion de dépendance via des interfaces ciblées.

---

## 2. Règle d'Or de Modularité : Plafond Strict de 300 Lignes par Fichier

- **Plafond Absolu (< 300 lignes)** : Aucun fichier source (`.cs`, `.razor`, `.xaml`, etc.) ne doit excéder **300 lignes**. La zone cible recommandée est de **80 à 250 lignes**.
- **Interdiction Formelle des Fichiers Monolithiques** : Les classes géantes ("god classes") ou fichiers de milliers de lignes sont strictement proscrits et constituent une violation critique de l'architecture.
- **Découpage Systématique** : Dès qu'une classe métier, un service ou un composant atteint 200 à 250 lignes, il **doit être immédiatement scindé** en fichiers partiels (`partial class ClassName.SousDomaine.cs`), en sous-composants ou en sous-services spécialisés par responsabilité unique.
- **Règle d'Extension Future** : Lors de l'implémentation de nouveaux modules, endpoints ou fonctionnalités, il est formellement interdit d'ajouter du code dans un fichier approchant de la limite. Chaque nouvelle fonctionnalité doit faire l'objet d'un nouveau fichier modulaire dédié.

---

## 3. Syntaxe & Qualité de Code (Clean Code)

- **C# Moderne & Typage Fort** : Utiliser une version de .NET encore supportée et cohérente entre les projets, sauf exception de compatibilité explicitement expliquée. La version effective est celle déclarée par les fichiers projet ; nullabilité activée (`<Nullable>enable</Nullable>`) et zéro warning introduit par les changements.
- **Conventions Microsoft** :
  - `PascalCase` : Classes, Interfaces (`I...`), Méthodes, Propriétés, Enums, Composants.
  - `camelCase` : Paramètres et variables locales.
  - `_camelCase` : Champs privés.
- **Nommage Explicite** : Noms clairs et auto-porteurs, aucune abréviation cryptique.
- **Structure Limpide** : Retours anticipés (*early returns / guard clauses*) pour limiter l'imbrication à 2 niveaux maximum.
- **Sobriété des Ressources** : Aucun asset graphique lourd ou binaire propriétaire ; privilégier les SVG intégrés, polices d'icônes ou rendus vectoriels/CSS légers.

---

## 4. Commentaires & Auto-Documentation (Règle d'Or : Zéro Commentaire C#)

- **Zéro commentaire dans le code source C#** : Le code source C# (`.cs`) ne contient strictement aucun commentaire (`//`, `/*`, `///`).
- **Code 100% auto-documenté** : La lisibilité, la clarté et l'intention sont portées exclusivement par un nommage explicite, des identifiants parlants, des méthodes courtes, des abstractions étanches et le typage fort.
- **Déportation documentaire totale** : Toute l'explication conceptuelle, les schémas d'architecture, la justification des choix et la pédagogie didactique sont déportés dans les supports d'ingénierie dédiés (`ARCHITECTURE.md`, `ETAPES.md` et les micro-fiches du livret LaTeX `Livret/`).

---

## 5. Documentation & Supports Pédagogiques

- L'explication de l'architecture globale, des choix de conception et de la structure du projet réside dans `ARCHITECTURE.md`.
- **Méthodologie Pédagogique Ultra-Granulaire (Une Micro-Fiche LaTeX par Action)** :
  - Le livret n'est pas rédigé d'un seul bloc, mais construit **au fur et à mesure, micro-action par micro-action**, sous la forme de **micro-fiches modulaires ciblées** (`Livret/etapes/XX_YY_nom_action.tex`, par ex. `01_01_creation_solution.tex`).
  - **Règle 1 — Public Visé & Objectifs d'Apprentissage Vérifiables** :
    - Définir explicitement le profil de l'apprenant cible (ex: développeur junior débutant en C# moderne et Fullstack .NET).
    - Formuler pour chaque fiche au moins un **objectif d'apprentissage observable et mesurable** (ex: *« À l'issue de cette fiche, l'apprenant sera capable de... »*).
  - **Règle 2 — Manipulations Reproductibles, Résultats Attendus & Exercices** :
    - Chaque fiche d'action technique détaille des étapes pas-à-pas strictement reproductibles : répertoire de travail (`cd`), commande CLI exacte (ex: `dotnet new ...`), prérequis nécessaires.
    - Présenter systématiquement le **résultat attendu** (extrait de sortie console, structure de fichier générée ou code effectif).
    - Fournir une **méthode de vérification concrète** (compilation `dotnet build`, appel HTTP ou test).
    - Signaler les **erreurs fréquentes du débutant** (ex: mauvaise arborescence, confusion d'outils) et proposer un **exercice de réinvestissement** avec critères d'auto-évaluation.
  - **Règle 3 — Distinction Formelle entre État Réalisé et Cible Prévue** :
    - Distinguer sans ambiguïté les fonctionnalités réellement écrites et opérationnelles dans le dépôt de celles qui sont planifiées pour les jalons ultérieurs.
    - Si un composant utilise temporairement une approche basique (ex: code-behind dans `MainPage.xaml.cs` au Jalon 1), indiquer explicitement qu'il s'agit de l'état du template initial et que l'architecture cible (ex: MVVM complet via `CommunityToolkit.Mvvm` au Jalon 8) viendra remplacer cette amorce.
    - Ne jamais décrire comme présent un élément qui n'a pas encore été implémenté (EF Core, JWT, MVVM, SQLite).
  - **Règle 4 — Nuance Technique & Exactitude des Versions** :
    - Bannir toute affirmation absolue ou simplificatrice :
      - *Immutabilité des records* : préciser qu'elle est superficielle (*shallow*) et que des collections internes (comme `List<T>`) restent mutables sauf usage de types immuables dédiés.
      - *Partage de bibliothèques* : préciser que le partage binaire de DTOs en monorepo assure la compatibilité à la compilation, mais ne dispense pas d'une gestion de version d'API HTTP dans un environnement distribué.
      - *Minimal APIs vs Contrôleurs* : expliciter les gains (suppression du pipeline de réflection/filtres des contrôleurs) tout en rappelant que la performance globale dépend des I/O et de la logique métier.
    - S'appuyer sur des versions de .NET actives et officiellement supportées (**actuellement .NET 10 LTS**, .NET 8 ayant atteint sa fin de support en novembre 2026). Dater et citer les versions des packages.
  - **Règle 5 — Contrôle Visuel du PDF Compilé & Rendu Typographique** :
    - Après chaque compilation via `Livret/compiler_livret.py`, inspecter systématiquement le document généré `LIVRET.pdf`.
    - Vérifier l'absence d'erreurs LaTeX, d'alertes *overfull hbox*, de textes tronqués, et traquer tout chevauchement ou collision dans les diagrammes TikZ (notamment les étiquettes de flèches qui ne doivent jamais couper les titres ou bordures de boîtes).
    - Proscrire les blocs monolithiques rigides (`tabularx` ou boîtes fermées non justifiées) générant de grands espaces blancs vides en bas de page.
    - Privilégier une mise en page aérée, fluide et continue, avec des sections sécables (`breakable`).
  - **Cycle de validation itératif et immédiat** : Après la réalisation de chaque micro-action technique, sa micro-fiche `.tex` correspondante est rédigée. L'utilisateur la lit (lecture courte de 2 minutes), valide la compréhension ou demande des éclaircissements, avant de donner le feu vert pour passer à la micro-action suivante.
  - **Compilation automatisée** : Un script Python dédié (`Livret/compiler_livret.py`) assemble dynamiquement toutes les micro-fiches validées dans l'ordre chronologique vers le document maître `Livret/LIVRET.tex` et son PDF associé.
- **Relecture avant assemblage** : Vérifier que la fiche correspond au code réellement livré, que ses étapes sont reproductibles et que ses exercices ont une réponse vérifiable. Après compilation, contrôler les erreurs LaTeX, les références et la mise en page du PDF ; corriger les débordements, schémas illisibles et pages inutilement vides.
- Le suivi d'avancement opérationnel et les instructions d'exécution sont maintenus dans `README.md`.
