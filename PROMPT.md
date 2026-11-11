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

- **C# Moderne & Typage Fort** : .NET 8+, nullabilité activée (`<Nullable>enable</Nullable>`), zéro warning toléré.
- **Conventions Microsoft** :
  - `PascalCase` : Classes, Interfaces (`I...`), Méthodes, Propriétés, Enums, Composants.
  - `camelCase` : Paramètres et variables locales.
  - `_camelCase` : Champs privés.
- **Nommage Explicite** : Noms clairs et auto-porteurs, aucune abréviation cryptique.
- **Structure Limpide** : Retours anticipés (*early returns / guard clauses*) pour limiter l'imbrication à 2 niveaux maximum.
- **Sobriété des Ressources** : Aucun asset graphique lourd ou binaire propriétaire ; privilégier les SVG intégrés, polices d'icônes ou rendus vectoriels/CSS légers.

---

## 4. Zéro Commentaire (Règle Absolue)

- **Aucun commentaire** : Ne jamais insérer de commentaires dans le code source (`//` ou `/* ... */`).
- **Aucune documentation XML** : Ne pas utiliser de balises `///`.
- **Code auto-explicatif** : Le code doit être limpide par lui-même grâce au découpage modulaire, à la rigueur de l'architecture et à la précision du nommage.

---

## 5. Documentation & Supports Pédagogiques

- Le code source demeure rigoureusement vierge de tout commentaire explicatif.
- L'explication de l'architecture globale, des choix de conception et de la structure du projet réside dans `ARCHITECTURE.md`.
- **Méthodologie Pédagogique Ultra-Granulaire (Une Micro-Fiche LaTeX par Action)** :
  - Le livret n'est pas rédigé d'un seul bloc, mais construit **au fur et à mesure, micro-action par micro-action**, sous la forme de **micro-fiches modulaires ciblées** (`Livret/etapes/XX_YY_nom_action.tex`, par ex. `01_01_creation_solution.tex`).
  - **Mise en Page Fluide & Typographie Moderne (Interdiction du « Tout-en-Bloc » et du « Tout-en-Tableau »)** :
    - **Fluidité de lecture** : Le contenu principal est rédigé sous forme de texte continu, élégamment aéré, avec des paragraphes naturels, des listes à puces percutantes (`itemize` / `description`) et des sous-titres clairs.
    - **Fin des blocs rigides et des tableaux systématiques** : Il est formellement interdit d'enfermer systématiquement chaque texte dans des boîtes ou des tableaux rigides (`tabularx`) non justifiés, car ces blocs monolithiques créent de grands espaces vides inesthétiques en bas de page.
    - **Schémas TikZ ciblés et calibrés** : Maintenir les diagrammes vectoriels d'architecture et de flux dès qu'ils apportent une valeur visuelle concrète. Veiller à ce que les flèches, étiquettes et bordures soient parfaitement espacées, sans aucune collision de texte.
    - **Tableaux réservés aux stricts besoins comparatifs** : Un tableau n'est employé que lorsqu'une comparaison multi-critères synthétique est réellement pertinente. Ne jamais forcer un tableau là où 3 puces explicatives suffisent.
    - **FAQ Pédagogique Fluide** : La section systématique **« Questions Fréquentes du Débutant »** est mise en page de manière typographique fluide (Q\&A aéré et sécable), permettant à LaTeX de paginer sans interruption brutale ni vide artificiel.
  - **Cycle de validation itératif et immédiat** : Après la réalisation de chaque micro-action technique, sa micro-fiche `.tex` correspondante est rédigée. L'utilisateur la lit (lecture courte de 2 minutes), valide la compréhension ou demande des éclaircissements, avant de donner le feu vert pour passer à la micro-action suivante.
  - **Compilation automatisée** : Un script Python dédié (`Livret/compiler_livret.py`) assemble dynamiquement toutes les micro-fiches validées dans l'ordre chronologique vers le document maître `Livret/LIVRET.tex` et son PDF associé.
- Le suivi d'avancement opérationnel et les instructions d'exécution sont maintenus dans `README.md`.
