# Cadrage du Projet — FullStackCSharp

Ce document définit la vision, les objectifs pédagogiques, l'organisation technique et la feuille de route pour la création d'une application C# Fullstack modèle, didactique et explicative en français.

---

## 1. Vision & Objectifs Pédagogiques

- **Nom du Projet** : `FullStackCSharp`
- **Auteur \& Concepteur** : **Kevin Friart**
- **Finalité** : Concevoir une application d'apprentissage complète, modulaire et hautement pédagogique en C# .NET moderne.
- **Domaine Fonctionnel** : Boutique interactive de commande et dégustation de glaces artisanales :
  - Catalogue des parfums et coupes de glaces,
  - Personnalisation (options, arômes, garnitures, portions),
  - Panier d'achat réactif et calcul dynamique,
  - Validation de commande, authentification et profil utilisateur.
- **Principe Fondateur d'Indépendance Code / Didactique** :
  - **Zéro commentaire dans le code source C#** (conformément à `PROMPT.md`) : le code est rigoureux, propre et auto-documenté par son nommage et ses abstractions.
  - Toute l'explication conceptuelle, les schémas d'architecture et la transmission didactique sont déportés dans les supports d'ingénierie dédiés (`ARCHITECTURE.md` et le livret LaTeX `Livret/LIVRET.tex`).

---

## 2. Choix Technologiques & Décisions d'Ingénierie

| Composant | Choix Technologique | Justification Pédagogique |
| :--- | :--- | :--- |
| **Frontend** | **.NET MAUI (.NET 10 LTS)** | Client riche multiplateforme (mobile et desktop) articulé autour du patron MVVM moderne (`CommunityToolkit.Mvvm`). |
| **Backend** | **ASP.NET Core Minimal API (.NET 10 LTS)** | API serveur haute performance, épurée, découpée en modules d'endpoints typés avec injection de dépendances. |
| **Console Pédagogique** | **Console d'Observabilité Kestrel (Approche 1)** | Tour de contrôle en arrière-plan avec journalisation ANSI colorée en temps réel (requêtes HTTP, SQL EF Core, tokens JWT, validation de commande). |
| **Persistance** | **EF Core + SQLite** (avec Seed initial) | Base relationnelle légère, autonome, sans dépendance d'infrastructure externe. |
| **Gestion des Assets** | **100% Vectoriel / SVG & Dessin XAML** | **Aucun asset binaire lourd (.png, .jpg)**. Utilisation exclusive de graphismes vectoriels SVG et de formes XAML natives. |
| **Qualité de Code** | **Clean Architecture & Limite 300 lignes** | Respect absolu de `PROMPT.md` : fichiers < 300 lignes, typage fort, nullabilité active, zéro warning, guard clauses. |
| **Support Didactique** | **Livret Unique A4 (LaTeX)** | Format A4 avec mise en page optimisée : schémas de flux, diagrammes conceptuels et tableaux de synthèse. |

---

## 3. Dispositif Documentaire & Pédagogique

### A. Vue d'Ensemble Technique (`ARCHITECTURE.md`)
Fichier Markdown à la racine qui décrit :
- Les flux d'échange entre l'application cliente .NET MAUI et l'API ASP.NET Core.
- L'arborescence des solutions et projets (`FullStackCSharp.Front`, `FullStackCSharp.Back`, `FullStackCSharp.Shared`).
- La mise en œuvre du patron MVVM côté client et du découpage Endpoint/Service/Repository côté serveur.
- La stratégie d'évitement des assets lourds via le vectoriel.

### B. Architecture Didactique Ultra-Granulaire du Livret (`Livret/`)

Le livret n'est pas rédigé d'un seul bloc figé. Il est conçu pour être développé **au fur et à mesure, micro-action par micro-action**, en synchronisation étroite avec la réflexion et la validation humaine :

1. **Une micro-fiche `.tex` par micro-action (Approche Ultra-Granulaire)** :
   - Chaque micro-action d'ingénierie fait l'objet d'un fichier LaTeX dédié et autonome situé dans `Livret/etapes/` (ex: `01_01_creation_solution.tex`, `01_02_directory_build_props.tex`, etc.).
   - Ce format ultra-court (1 à 2 pages A4) permet à l'utilisateur de lire en 2 minutes le concept abordé, d'analyser le schéma TikZ associé et de valider immédiatement chaque petit pas.
2. **Cycle de validation itératif et continu** :
   - **Micro-Action $X.Y$** : Réalisation technique (commande ou 1 fichier de code) $\longrightarrow$ Test/Compilation de contrôle $\longrightarrow$ Rédaction de la micro-fiche `.tex`.
   - **Relecture & Feedback** : L'utilisateur analyse la micro-fiche. Dès validation explicite, passage à l'action suivante $X.(Y+1)$.
3. **Compilation automatisée via script Python (`Livret/compiler_livret.py`)** :
   - Un script Python assemble dynamiquement l'ensemble des micro-fiches d'actions validées (triées par ordre chronologique `XX_YY_*.tex`) dans le gabarit maître `Livret/LIVRET.tex`.
   - Il déclenche la compilation `pdflatex` pour générer le document de référence final consolidé `LIVRET.pdf`.

> **Orientation du Contenu** : Les micro-fiches s'interdisent toute récitation linéaire de code ou de syntaxe. Elles se concentrent sur **l'explication d'un concept fondamental unique**, rédigé sous forme de texte continu clair et fluide (avec listes structurées), illustré par un **schéma de flux TikZ** percutant et d'une rubrique systématique **« Questions Fréquentes du Débutant »** (anticipation maïeutique de tous les doutes et interrogations d'un débutant en C\# Fullstack). Les tableaux et encadrés ne sont employés que lorsqu'ils apportent une réelle valeur comparative, évitant tout effet de bloc rigide ou de grand espace vide.

---

## 4. Spécifications du Format A4 pour les Livrets LaTeX

Pour garantir un confort de lecture optimal et une mise en page digne d'un manuel d'informatique :
- **Classe** : `scrreprt` (KOMA-Script) ou `report` avec option `a4paper`.
- **Organisation** : Livrets modulaires par étape assemblés par script Python.
- **Mise en Page & Continuité de Lecture** : 
  - Marges équilibrées de 2 cm (`geometry`, marges blanches de sécurité sans bas de page répétitif).
  - Texte fluide et aéré : priorité aux paragraphes rédigés et listes descriptives.
  - Bannissement de la mise en boîte systématique et des tableaux superflus pour préserver un flux de lecture naturel et éviter les ruptures de page artificielles.
- **Éléments Visuels Ciblés** : Schémas vectoriels TikZ clairs (sans collision de flèches), tableaux de comparaison strictement réservés aux synthèses complexes, et encadrés légers sécables (`breakable`).
- **Typographie** : Polices modernes avec rendu net des extraits ciblés (`Fira Code`, `Inconsolata` ou `Source Code Pro`).

---

## 5. Feuille de Route d'Exécution & Méthodologie

> **État Actuel** : **Jalon 1 Validé (Actions 1.1 à 1.8 Réalisées)** — Solution .NET 10 LTS, 3 projets, `Directory.Build.props`, `<ProjectReference>` câblées et micro-fiches rédigées. Prêt pour le Jalon 2 (Contrats Partagés dans `Shared`).

1. [x] Cadrage initial et configuration de `PROMPT.md` (FullStackCSharp, règles strictes et pédagogiques).
2. [x] Gestion des supports pédagogiques dans Git (fichiers `PROJET.md`, `ETAPES.md` et `Livret/` versionnés pour garantir la reproductibilité aux apprenants).
3. [x] Définition des spécifications fonctionnelles et techniques de l'application (.NET 10 LTS).
4. [x] Définition de l'architecture documentaire modulaire (micro-fiches `.tex` par action + compilateur Python).
5. [x] Rédaction du document d'architecture globale `ARCHITECTURE.md`.
6. [ ] **Développement Itératif Jalon par Jalon (Jalons 1 à 15)** :
   - *Phase 1 (Jalons 1 à 3)* : Socle technique, solution, Shared, observabilité.
   - *Phase 2 (Jalons 4 à 7)* : API backend, SQLite, EF Core, JWT.
   - *Phase 3 (Jalons 8 à 11)* : Client .NET MAUI, MVVM, Refit, catalogue.
   - *Phase 4 (Jalons 12 à 15)* : Panier local SQLite, commande, profil, finitions.
7. [ ] Assemblage final et compilation continue via `compiler_livret.py` vers `LIVRET.pdf`.
