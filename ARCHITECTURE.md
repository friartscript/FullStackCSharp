# Architecture Logicielle — FullStackCSharp

Ce document détaille l'architecture logicielle globale, les patrons de conception et les flux d'échange du projet **FullStackCSharp**.

---

## 1. Vue d'Ensemble du Système

Le projet est conçu selon une architecture découplée Fullstack 100% C# .NET 8 :

```
┌────────────────────────────────────────────────────────┐
│             Client : .NET MAUI (.NET 8)               │
│                                                        │
│  [ Vues XAML (100% SVG) ] ── (Binding) ── [ ViewModels ]│
│                                                │       │
│                                           (Appels HTTP)│
└────────────────────────────────────────────────┬───────┘
                                                 │ JSON / REST
                                                 ▼
┌────────────────────────────────────────────────────────┐
│       Serveur : ASP.NET Core Minimal API (.NET 8)       │
│                                                        │
│   [ Modules d'Endpoints ] ──► [ Services Métier ]      │
│            │                         │                 │
│            │                         ▼                 │
│            │             [ EF Core / DbContext ]       │
│            │                         │                 │
│            │                         ▼                 │
│            │              [ Base SQLite locale ]       │
│            │                                           │
│            ▼ (Télémétrie en temps réel)                │
│   ┌──────────────────────────────────────────────┐     │
│   │   CONSOLE D'OBSERVABILITÉ PÉDAGOGIQUE        │     │
│   │   - Traces HTTP & Requêtes REST              │     │
│   │   - Décodage Claims JWT en direct            │     │
│   │   - Requêtes SQL brutes EF Core              │     │
│   │   - Transactions & Vérification anti-fraude  │     │
│   └──────────────────────────────────────────────┘     │
└────────────────────────────────────────────────────────┘
                         ▲
                         │ Modèles partagés (DTOs)
┌────────────────────────┴───────────────────────────────┐
│              Contrats : FullStackCSharp.Shared         │
│          (DTOs, Requêtes, Réponses, Enums)             │
└────────────────────────────────────────────────────────┘
```

---

## 2. Découpage des Projets de la Solution

| Projet / Dossier | Rôle & Responsabilité |
| :--- | :--- |
| **`FullStackCSharp.Front`** | Application cliente multiplateforme développée avec **.NET MAUI** (.NET 8). Présentation visuelle, composants XAML, gestion d'état MVVM avec `CommunityToolkit.Mvvm`. |
| **`FullStackCSharp.Back`** | API Web légère et performante développée avec **ASP.NET Core Minimal APIs** (.NET 8). Validation, logique d'affaires, persistance SQLite via EF Core. |
| **`FullStackCSharp.Shared`** | Bibliothèque de classes contenant les DTOs (*Data Transfer Objects*), interfaces de contrats et énumérations communes au Front et au Back. |
| **`Livret/`** | Supports d'apprentissage modulaires rédigés par étape (`Livret/etapes/`) et assemblés via un script Python vers l'ouvrage de référence consolidé (`LIVRET.tex`). |

---

## 3. Stratégie Graphique : 100% Vectoriel (Zéro Asset Lourd)

Contrairement aux architectures traditionnelles qui intègrent des dizaines d'images matricielles PNG/JPG :
- **Ressources Vectorielles (SVG)** : Les illustrations de glaces, garnitures, boutons et icônes sont intégrées sous forme de fichiers vectoriels SVG ou de géométries XAML natives.
- **Avantages** :
  1. Zéro dégradation graphique quelle que soit la résolution de l'écran.
  2. Poids du dépôt et des binaires considérablement réduit.
  3. Indépendance totale vis-à-vis d'assets graphiques propriétaires.

---

## 4. Règles d'Ingénierie & Clean Code (Rappel `PROMPT.md`)

- **Plafond strict de 300 lignes par fichier** : Aucun fichier source ne dépasse 300 lignes (zone cible : 80 à 250 lignes).
- **Zéro commentaire dans le code source** : Aucun commentaire `//` ou `/* ... */` ni documentation XML `///`.
- **Nommage explicite et auto-documenté** : Conventions Microsoft strictes (`PascalCase`, `camelCase`, `_camelCase`).
- **Retours anticipés (*Guard Clauses*)** : Limitation de l'imbrication conditionnelle à 2 niveaux maximum.

---

## 5. Console d'Observabilité Pédagogique Backend (Approche 1)

Dans une application Fullstack, le client mobile et le serveur web tournent dans des processus isolés. Sans observabilité, le serveur agit comme une "boîte noire", ce qui nuit à l'assimilation pédagogique des flux sous-jacents.

Le projet configure la console native du serveur Kestrel (`FullStackCSharp.Back`) comme un **tableau de bord pédagogique interactif à code couleur ANSI** :

1. **Cycle de Vie HTTP / REST** :
   - Méthode, route invoquée, paramètres d'en-tête et temps de traitement en millisecondes.
   - Codes de statut HTTP contextualisés (`200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`).
2. **Observabilité SQL & EF Core** :
   - Impression en clair des requêtes SQL générées par Entity Framework Core (`SELECT`, `INSERT`, `UPDATE`).
   - Visualisation des jointures, des filtres et des transactions relationnelles SQLite.
3. **Sécurité Cryptographique & JWT** :
   - Visualisation du hachage sécurisé (sel cryptographique et hash).
   - Décodage pédagogique en direct des jetons JWT et de leurs *Claims* (`UserId`, `Email`, `Name`, rôle, expiration).
4. **Vérification d'Intégrité Métier (Anti-Fraude)** :
   - Comparaison explicite entre le montant calculé côté client et le recalcul strict côté serveur à partir des tarifs de la base de données lors de la validation d'une commande.


