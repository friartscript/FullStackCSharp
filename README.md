# FullStackCSharp — Écosystème C# .NET 10 LTS Fullstack

> **Auteur & Concepteur** : Kevin Friart  
> **Plateforme** : .NET 10 LTS (C# moderne)  
> **Cas d'usage** : Boutique artisanale de glaces (*Gelato Artisan*)

Ce dépôt contient le code source et les supports d'ingénierie d'une application Fullstack moderne, modulaire et hautement didactique en C# unifié.

---

## 1. Architecture du Système

Le système est découpé en trois projets étanches coordonnés par une solution maître et documentés par un livret d'apprentissage modulaire :

- **`FullStackCSharp.Shared`** : Bibliothèque neutre (`classlib`) hébergeant l'autorité centrale des contrats d'échange, DTOs (`record`), requêtes, réponses et énumérations communes.
- **`FullStackCSharp.Back`** : Serveur web autonome ASP.NET Core Minimal API auto-hébergé sur Kestrel avec console d'observabilité en temps réel, persistance relationnelle SQLite via EF Core et sécurité JWT.
- **`FullStackCSharp.Front`** : Client riche multiplateforme .NET MAUI (Single Project) pour Windows, Android, iOS et macOS avec architecture MVVM cible et panier d'achat local.
- **`Livret/`** : Ouvrage didactique ultra-granulaire composé de micro-fiches LaTeX d'ingénierie assemblées dynamiquement par un script Python vers `Livret/LIVRET.pdf`.

---

## 2. Prérequis d'Environnement

Pour compiler et exécuter l'ensemble de la solution et générer la documentation :

1. **SDK .NET 10** (`10.0.403` ou supérieur) : `dotnet --version`
2. **Workload .NET MAUI** : `dotnet workload install maui`
3. **Python 3** (pour le compilateur du livret) : `python --version`
4. **Distribution LaTeX** (MiKTeX ou TeX Live) avec `pdflatex` accessible dans le `PATH`.

---

## 3. Guide de Démarrage Rapide

### Compilation de la Solution

Pour compiler l'intégralité des projets membres de la solution :

```powershell
dotnet build FullStackCSharp.sln
```

### Astuce : Compilation Accélérée du Frontend (.NET MAUI)

Par défaut, compiler le projet Front sans paramètre déclenche la compilation simultanée pour les quatre cibles (Windows, Android, iOS, Mac Catalyst).  
Pour une itération rapide sous Windows (quelques secondes) :

```powershell
dotnet build FullStackCSharp.Front -f net10.0-windows10.0.19041.0
```

### Lancement de l'API Backend

```powershell
dotnet run --project FullStackCSharp.Back
```

L'API démarre sur le port Kestrel local (`http://localhost:5227`) et affiche sa console d'observabilité.  
Test de validation de la sonde de santé :

```powershell
curl http://localhost:5227/health
# Réponse attendue : {"status":"Healthy","service":"FullStackCSharp.Back"}
```

### Génération du Livret Pédagogique (PDF)

Le script assemble automatiquement toutes les micro-fiches de `Livret/etapes/` et produit le document maître consolidé :

```powershell
python Livret/compiler_livret.py
```

Le fichier compilé est généré à l'emplacement : `Livret/LIVRET.pdf`.

---

## 4. Parcours d'Apprentissage & Lecture Conseillé

Pour appréhender le système avec un maximum de clarté, nous recommandons le parcours suivant au débutant :

1. **[`README.md`](file:///E:/Documents%20perso/0000Site%20internet/DEV/FullStackCSharp/README.md)** : Vue d'ensemble, prérequis et prise en main de l'environnement.
2. **[`ARCHITECTURE.md`](file:///E:/Documents%20perso/0000Site%20internet/DEV/FullStackCSharp/ARCHITECTURE.md)** : Comprendre la topologie 3 tiers et les flux d'échange.
3. **[`GLOSSAIRE.md`](file:///E:/Documents%20perso/0000Site%20internet/DEV/FullStackCSharp/GLOSSAIRE.md)** : Dictionnaire de tous les termes techniques (DTO, JWT, MVVM, Kestrel...).
4. **`Livret/LIVRET.pdf`** : Le manuel pas-à-pas complet (assemblé via `python Livret/compiler_livret.py`).
5. **[`ETAPES.md`](file:///E:/Documents%20perso/0000Site%20internet/DEV/FullStackCSharp/ETAPES.md)** : Feuille de route d'ingénierie détaillée des 15 jalons.

---

## 5. Règles d'Or d'Ingénierie & Conventions

- **Plafond strict $< 300$ lignes** : Aucun fichier source ne dépasse 300 lignes (zone cible : 80 à 250 lignes).
- **Zéro commentaire dans le code C#** : Le code est propre, auto-porteur et documenté par ses abstractions. Toute la pédagogie est déportée dans le livret LaTeX.
- **100% Vectoriel** : Aucun asset matriciel lourd (PNG, JPG) ; utilisation exclusive de SVG et formes XAML natives.
- **Zéro simulation** : Tout le code compile et s'exécute réellement sous .NET 10 LTS.

---

## 6. Suivi d'Avancement du Projet

- **Phase 1 : Socle Technique**
  - [x] Action 1.1 : Création de la solution `FullStackCSharp.sln`
  - [x] Action 1.2 : Création de la bibliothèque `FullStackCSharp.Shared`
  - [x] Action 1.3 : Création de l'API `FullStackCSharp.Back`
  - [x] Action 1.4 : Création du client .NET MAUI `FullStackCSharp.Front`
  - [x] Action 1.5 : Rattachement des 3 projets à la solution
  - [x] Action 1.6 : Configuration globale Roslyn (`Directory.Build.props`)
  - [x] Action 1.7 : Câblage des références inter-projets (`<ProjectReference>`)
  - [x] Action 1.8 : Test de compilation et validation globale
- **Phase 2 : API Backend Complète (Jalons 4 à 7)**
- **Phase 3 : Client Mobile .NET MAUI (Jalons 8 à 11)**
- **Phase 4 : Fonctionnalités Transversales (Jalons 12 à 15)**
