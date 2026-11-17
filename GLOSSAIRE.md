# Glossaire Didactique de l'Ingénierie Fullstack C# — FullStackCSharp

> Ce glossaire est conçu comme un compagnon de route pour les débutants. Chaque terme y est défini de manière claire, concise et illustrée par une analogie concrète.

---

### A

- **API REST (*Representational State Transfer*)** : Interface standardisée permettant à deux applications (par exemple un client mobile et un serveur) d'échanger des données sur le réseau via le protocole HTTP. Au lieu d'appeler des fonctions arbitraires, on manipule des *ressources* identifiées par des URLs stables (ex : `/api/icecreams`) à l'aide de verbes HTTP universels (`GET`, `POST`, `PUT`, `DELETE`).
- **Assembly (.dll / .exe)** : Fichier binaire produit par la compilation d'un projet .NET. Une bibliothèque de classes produit une `.dll` (*Dynamic Link Library*, réutilisable mais non exécutable directement), tandis qu'une application exécutable produit un `.exe` (disposant d'un point d'entrée d'exécution).

---

### C

- **Claims (dans un JWT)** : Paires clé-valeur d'informations textuelles embarquées dans le corps d'un jeton JWT (ex : identifiant utilisateur `sub`, adresse email, nom, date d'expiration). Le serveur extrait ces informations pour authentifier et autoriser les requêtes sans devoir réinterroger la base de données.
- **Client-Serveur** : Architecture fondamentale de séparation des rôles. Le **Client** (ici l'application mobile .NET MAUI) est le demandeur qui présente l'interface à l'utilisateur. Le **Serveur** (ici Kestrel et ASP.NET Core) est le fournisseur qui détient la logique métier, contrôle la sécurité et manipule la base de données centrale.
- **CORS (*Cross-Origin Resource Sharing*)** : Mécanisme de sécurité des navigateurs et clients web autorisant ou bloquant les requêtes provenant d'un domaine ou port différent de celui du serveur d'API.

---

### D

- **DataBinding (Liaison de Données)** : Mécanisme réactif reliant automatiquement une propriété visuelle XAML (ex: le texte d'un libellé) à une propriété logique C# du ViewModel. Lorsque la donnée C# change, l'écran se rafraîchit sans qu'il soit nécessaire d'écrire du code impératif de manipulation graphique.
- **DelegatingHandler** : Maillon intermédiaire inséré dans le pipeline de requêtes HTTP sortantes du client .NET. C'est l'équivalent côté client d'un middleware serveur : il peut intercepter, modifier (ex : injecter automatiquement l'en-tête `Authorization: Bearer <token>`) ou journaliser chaque requête HTTP sortante.
- **Dependency Injection (DI / Injection de Dépendances)** : Patron de conception où les objets reçoivent leurs dépendances (services, connexions) depuis l'extérieur (le conteneur IoC) via leur constructeur, au lieu de les instancier eux-mêmes avec `new`. Cela garantit le découplage et simplifie considérablement les tests unitaires.
- **Directory.Build.props** : Fichier XML standard de MSBuild placé à la racine d'un dépôt pour propager automatiquement des propriétés de compilation communes (version du langage, activation de la nullabilité, usings implicites) à l'ensemble des sous-projets sans duplication.
- **DTO (*Data Transfer Object*)** : Objet passif dont le rôle unique est de transporter des données sur le réseau entre le client et le serveur. Comparable à un colis postal scellé, il est modélisé par un `record` en C# moderne et ne contient aucune logique de calcul ni interaction avec la base de données.

---

### E

- **Entity Framework Core (EF Core)** : ORM (*Object-Relational Mapper*) officiel de Microsoft pour .NET. Il traduit automatiquement les requêtes C# écrites en LINQ en requêtes SQL relationnelles natives exécutées sur le moteur de base de données.
- **Entité (*Entity*)** : Classe C# représentant directement une table de la base de données relationnelle (ex: `User`, `Icecream`, `Order`). Contrairement aux DTOs, les entités contiennent des clés étrangères, des propriétés de navigation et des champs internes que le client distant n'a pas à voir.

---

### F

- **Fluent API** : Approche de configuration d'Entity Framework Core utilisant le chaînage de méthodes C# dans la méthode `OnModelCreating` du `DbContext` pour définir les relations, contraintes et index SQL sans polluer les classes d'entités avec des attributs.

---

### G

- **Guard Clause (Retour Anticipé)** : Pratique de Clean Code consistant à vérifier immédiatement les cas d'erreur ou conditions d'arrêt en début de méthode et à retourner immédiatement (`return;` ou `throw`), évitant ainsi d'imbriquer de multiples blocs `if / else`.

---

### H

- **Hachage Salé (*Salted Hash*)** : Méthode cryptographique irréversible pour sécuriser les mots de passe. Un sel aléatoire unique (128 octets) est concaténé au mot de passe avant d'appliquer une fonction de hachage à sens unique (HMAC-SHA512). Le serveur ne stocke jamais le mot de passe en clair.

---

### I

- **Immutabilité Superficielle (*Shallow Immutability*)** : Propriété des types `record` en C# dont les accesseurs `init` interdisent toute modification des propriétés après l'instanciation. *Attention* : si le `record` contient une liste mutable (`List<T>`), le contenu interne de la liste peut toujours être altéré ; une immutabilité profonde requiert l'usage de collections en lecture seule (`IReadOnlyList<T>`).
- **Implicit Usings (Directives d'Imports Implicites)** : Fonctionnalité du compilateur C# important automatiquement en arrière-plan les espaces de noms les plus fréquents (`System`, `System.Threading.Tasks`, `System.Net.Http`), évitant d'écrire des dizaines de lignes `using` en tête de chaque fichier.

---

### J

- **JWT (*JSON Web Token*)** : Jeton de sécurité compact et autonome structuré en 3 parties (`En-tête.Payload.Signature`) encodées en Base64. Le Payload transporte les informations d'identité (Claims) et la Signature cryptographique permet au serveur de vérifier que le jeton n'a pas été altéré.

---

### K

- **Kestrel** : Serveur web HTTP asynchrone haute performance intégré nativement au cœur d'ASP.NET Core. Il permet à l'application web de s'auto-héberger (*self-hosted*) sans nécessiter l'installation d'un serveur web externe tiers comme Apache ou IIS.

---

### M

- **Micro-Fiche Pédagogique** : Fiche documentaire ciblée (1 à 2 pages A4) rédigée en LaTeX, dédiée à une seule micro-action d'ingénierie et articulée autour d'un objectif mesurable, d'un schéma de flux TikZ, d'une manipulation pas-à-pas et d'un exercice pratique.
- **Middleware** : Composant logiciel inséré dans la chaîne de traitement séquentielle (*pipeline*) d'une requête HTTP sur le serveur. Chaque middleware peut inspecter la requête, exécuter une logique (sécurité, journalisation, capture d'erreur) et décider de passer la main au middleware suivant.
- **Minimal APIs** : Modèle d'architecture moderne d'ASP.NET Core permettant d'exposer des routes HTTP ultra-rapides et modulaires via des lambdas légères (`app.MapGet`, `app.MapPost`), sans l'encombrement et la surcharge mémoire des contrôleurs MVC traditionnels.
- **MSBuild** : Moteur de compilation sous-jacent de .NET qui résout le graphe de dépendances, interprète les fichiers `.csproj` et orchestre le compilateur Roslyn pour produire les assemblages binaires.
- **MVVM (*Model-View-ViewModel*)** : Patron d'architecture fondamental des interfaces riches découpant l'application en 3 rôles étanches : la **Vue** (l'écran déclaratif XAML), le **ViewModel** (la logique de présentation en C# pur) et le **Modèle** (les données et contrats d'échange).

---

### N

- **Nullable Reference Types (Nullabilité)** : Système d'analyse statique du compilateur C# distinguant explicitement les types pouvant contenir la valeur nulle (`string?`) de ceux garantis non nuls (`string`). Les violations sont détectées dès la compilation.

---

### O

- **ORM (*Object-Relational Mapping*)** : Couche d'abstraction logicielle faisant le pont entre le monde orienté objet (les classes C#) et le monde relationnel (les tables, lignes et colonnes SQL).

---

### P

- **POCO (*Plain Old CLR Object*)** : Classe C# pure et simple ne dépendant d'aucun framework lourd, ne contenant que des propriétés et aucune logique d'infrastructure.
- **ProjectReference** : Balise XML dans un fichier `.csproj` déclarant une dépendance formelle de compilation vers un autre projet de la solution, garantissant que la dépendance est compilée en amont.

---

### R

- **Record (C#)** : Mot-clé de C# moderne définissant un type référence immuable doté par défaut de l'égalité par valeur, d'une syntaxe concise de constructeur primaire et d'un affichage texte automatique. Idéal pour les DTOs.
- **Refit** : Bibliothèque réseau transformant une simple interface C# décorée d'attributs HTTP (`[Get("/api/icecreams")]`) en un client REST fortement typé généré automatiquement à la compilation.

---

### S

- **SecureStorage** : Service d'abstraction de .NET MAUI permettant de stocker des données sensibles (comme les jetons JWT) dans le coffre-fort chiffré natif du système d'exploitation (Keychain sous iOS/macOS, KeyStore sous Android, DPAPI sous Windows).
- **Seed Data** : Jeu de données réaliste initialement inséré dans la base de données au premier démarrage de l'application (catalogue de glaces, tarifs, options) pour permettre de tester immédiatement les fonctionnalités.
- **Single Project (.NET MAUI)** : Modèle de projet unifié où une unique arborescence de code C# et de vues XAML compile simultanément pour Android, iOS, Windows et macOS sans dupliquer les projets de plateforme.
- **SQLite** : Moteur de base de données relationnelle léger et autonome stockant l'intégralité des données dans un simple fichier local sur le disque, sans serveur ni processus d'arrière-plan.
