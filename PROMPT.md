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
- **Méthodologie Pédagogique Modulaire (Livret LaTeX A4)** :
  - Le livret n'est pas rédigé d'un seul bloc, mais construit **au fur et à mesure, étape par étape**, sous la forme de **petits livrets modulaires** (`Livret/etapes/XX_nom_etape.tex`), à raison d'un fichier par étape de programmation.
  - **Cycle de validation itératif** : À chaque étape, le petit livret explicatif correspondant est rédigé. L'utilisateur le lit, analyse les choix, demande des approfondissements si nécessaire, puis valide le passage à l'étape suivante.
  - **Compilation automatisée** : Un script Python dédié (`Livret/compiler_livret.py`) assure l'assemblage et la compilation finale des étapes validées vers le document maître `Livret/LIVRET.tex` et son PDF associé.
  - **Directive sur le contenu** : Aucun catalogue de syntaxe ni code dump intégral ; focalisation sur les **concepts d'ingénierie fondamentaux**, les **schémas de flux** et les **tableaux comparatifs**.
- Le suivi d'avancement opérationnel et les instructions d'exécution sont maintenus dans `README.md`.
