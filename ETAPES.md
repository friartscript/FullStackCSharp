# Jalons d'Ingénierie & Étapes de Développement — FullStackCSharp

> **Projet** : `FullStackCSharp` (.NET 10 LTS Fullstack en C#)  
> **Orientation** : Application professionnelle, fonctionnelle et pédagogique en français  
> **Statut Git** : Fichier de référence pédagogique versionné

---

## 1. Principe Directeur : Construction Réelle d'un Projet Professionnel

Ce document décrit la feuille de route complète pour construire une application Fullstack C# **réellement fonctionnelle**, de la première commande `dotnet new` jusqu'à un système opérationnel complet. Chaque jalon produit du code qui **compile, s'exécute et se vérifie** — aucune simulation, aucun raccourci, aucun code mort.

### Philosophie d'Ingénierie

- **Le Backend est construit en premier** et testable de manière autonome (via `curl`, Postman ou la console d'observabilité) avant même que le client mobile n'existe.
- **Le Client est ensuite connecté** à une API qui fonctionne déjà réellement.
- **Les contrats partagés (DTOs) sont définis dès le départ** pour que le Frontend et le Backend parlent le même langage dès la première ligne de code.
- **Chaque jalon est une brique autonome** : à la fin de chaque étape, l'application est dans un état compilable, démarrable et vérifiable.

### Vue d'Ensemble des 4 Phases (15 Jalons)

```
PHASE 1 ── SOCLE TECHNIQUE (Jalons 1 à 3)
│  Jalon 1 : Solution .NET 10 LTS, Projets & Configuration
│  Jalon 2 : Contrats Partagés (FullStackCSharp.Shared)
│  Jalon 3 : Console d'Observabilité Pédagogique
│
▼
PHASE 2 ── API BACKEND COMPLÈTE (Jalons 4 à 7)
│  Jalon 4 : Modèle de Données, EF Core & Seed Data
│  Jalon 5 : Pipeline HTTP, Middleware & Endpoints Catalogue
│  Jalon 6 : Sécurité — Hachage, JWT & Authentification
│  Jalon 7 : Endpoints Protégés — Commandes & Profil
│
▼  → À ce stade, l'API entière fonctionne et se teste en console/curl
│
PHASE 3 ── CLIENT MOBILE .NET MAUI (Jalons 8 à 11)
│  Jalon 8  : Structure MAUI, AppShell & Navigation
│  Jalon 9  : Couche Réseau — HttpClient, Refit & Injection JWT
│  Jalon 10 : Flux d'Authentification — Onboarding, Connexion, Inscription
│  Jalon 11 : Catalogue, Détails & Personnalisation Produit
│
▼
PHASE 4 ── FONCTIONNALITÉS TRANSVERSALES (Jalons 12 à 15)
   Jalon 12 : Panier Local (SQLite Client) & Interface CRUD
   Jalon 13 : Passage de Commande — Flux Client → Serveur
   Jalon 14 : Profil Utilisateur, Historique & Détails Commandes
   Jalon 15 : Composants Avancés — Popup Modale & Badge Natif
```

---

## 2. Phase 1 : Socle Technique (Jalons 1 à 3)

Cette phase met en place les fondations indispensables avant toute logique métier. C'est l'équivalent de couler les fondations avant de monter les murs.

---

### Jalon 1 — Initialisation de la Solution & Configuration

**Périmètre** : Backend + Frontend + Shared  
**Concept clé** : *Pourquoi structurer une solution en plusieurs projets ?*

#### Éléments du Jalon 1 (État d'Avancement)

| Élément | Détail Technique | Statut Actuel |
| :--- | :--- | :--- |
| **Solution** | `FullStackCSharp.sln` regroupant les projets | **Réalisé** (Action 1.1) |
| **`FullStackCSharp.Shared`** | Bibliothèque de classes (`classlib` .NET 10 LTS) — autorité des contrats | **Réalisé** (Action 1.2) |
| **`FullStackCSharp.Back`** | Application web ASP.NET Core (`webapi` .NET 10 LTS) Minimal API | **Réalisé** (Action 1.3) |
| **`FullStackCSharp.Front`** | Application .NET MAUI (`maui` .NET 10 LTS multiplateforme) | **Réalisé** (Action 1.4) |
| **Rattachement Solution** | `dotnet sln add ...` pour coordonner le build global | **Réalisé** (Action 1.5) |
| **Configuration globale** | `Directory.Build.props` à la racine : `<Nullable>enable</Nullable>`, `<ImplicitUsings>enable</ImplicitUsings>` | **Réalisé** (Action 1.6) |
| **Références inter-projets** | `Back → Shared` et `Front → Shared` via `<ProjectReference>` | **Réalisé** (Action 1.7) |

#### Pourquoi c'est fondamental

Le découpage en 3 projets applique le **principe de séparation des responsabilités** au niveau de la solution :
- `Shared` contient **uniquement** les contrats d'échange (DTOs). Il ne connaît ni le serveur ni le client.
- `Back` et `Front` dépendent de `Shared` mais **ne se connaissent jamais directement entre eux**.
- La communication entre Front et Back passe **exclusivement** par des requêtes HTTP transportant des DTOs sérialisés en JSON.

#### Découpage en Micro-Étapes Réalisables

- **Action 1.1** : Création du fichier de solution `FullStackCSharp.sln` via `dotnet new sln`.
- **Action 1.2** : Création du projet de contrats `FullStackCSharp.Shared` (`dotnet new classlib -f net10.0`).
- **Action 1.3** : Création du projet API backend `FullStackCSharp.Back` (`dotnet new webapi -f net10.0`).
- **Action 1.4** : Création du projet client mobile `FullStackCSharp.Front` (`dotnet new maui -f net10.0`).
- **Action 1.5** : Rattachement des 3 projets à la solution (`dotnet sln add ...`).
- **Action 1.6** : Configuration globale du compilateur via `Directory.Build.props` (Nullable activé, Usings implicites centralisés sous .NET 10 LTS).
- **Action 1.7** : Câblage des références de dépendances inter-projets (`Back → Shared`, `Front → Shared`).
- **Action 1.8** : Test de compilation réelle de contrôle (`dotnet build FullStackCSharp.sln`).
- **Action 1.9** : Consolidation et revue du livret pédagogique du Jalon 1.
- **Action 1.10** : Validation utilisateur et transition vers le Jalon 2.

#### Vérification

```
dotnet build FullStackCSharp.sln   →  Build succeeded (3 projets, 0 warning, 0 error)
```

#### Console d'Observabilité

Rien de visible encore — le serveur ne démarre pas à cette étape.

---

### Jalon 2 — Contrats Partagés (FullStackCSharp.Shared)

**Périmètre** : Shared uniquement  
**Concept clé** : *Le contrat d'abord (Contract-First Design) — définir le langage commun avant de coder*

#### Ce qui est construit

| Fichier | Contenu | Rôle |
| :--- | :--- | :--- |
| `Dtos/IcecreamDto.cs` | `record IcecreamDto(int Id, string Name, string Description, string Image, decimal Price)` | Glace telle que vue par le client |
| `Dtos/IcecreamOptionDto.cs` | `record IcecreamOptionDto(int Id, string Name, decimal Price)` | Option de personnalisation (arôme, garniture) |
| `Dtos/IcecreamDetailDto.cs` | `record IcecreamDetailDto(...)` incluant `List<IcecreamOptionDto> Options` | Détail complet d'une glace avec ses options |
| `Dtos/AuthResponseDto.cs` | `record AuthResponseDto(string Token, string Name, string Email)` | Réponse renvoyée après connexion/inscription réussie |
| `Requests/SignupRequest.cs` | `record SignupRequest(string Name, string Email, string Address, string Password)` | Données d'inscription |
| `Requests/SigninRequest.cs` | `record SigninRequest(string Email, string Password)` | Données de connexion |
| `Requests/ChangePasswordRequest.cs` | `record ChangePasswordRequest(string OldPassword, string NewPassword)` | Demande de changement de mot de passe |
| `Requests/OrderPlaceRequest.cs` | `record OrderPlaceRequest(List<OrderItemRequest> Items, decimal TotalAmount)` | Commande envoyée par le client |
| `Requests/OrderItemRequest.cs` | `record OrderItemRequest(int IcecreamId, string Name, decimal UnitPrice, int Quantity, List<string> Options)` | Ligne d'article dans une commande |
| `Dtos/OrderDto.cs` | `record OrderDto(long Id, DateTime OrderedAt, decimal TotalAmount, int ItemCount)` | Résumé d'une commande pour l'historique |
| `Dtos/OrderDetailDto.cs` | `record OrderDetailDto(...)` incluant `List<OrderItemDto> Items` | Détail complet d'une commande passée |

#### Pourquoi c'est fondamental

- Les DTOs sont des **`record`** en C# moderne : égalité par valeur, immutabilité superficielle via accesseurs `init`, déconstructibles — exactement ce qu'on attend d'un objet de transport de données.
- **Les DTOs ne sont PAS les entités de la base de données.** C'est une erreur fréquente dans les tutoriels. Les entités `Icecream` (côté Back) contiennent des champs internes (date de création, clés de navigation EF Core) que le client n'a pas besoin de connaître.
- En définissant les contrats en premier, le Frontend et le Backend peuvent être développés en parallèle dans une équipe réelle.

#### Découpage en Micro-Étapes Réalisables

- **Action 2.1** : Création des DTOs Catalogue (`Dtos/IcecreamDto.cs`, `Dtos/IcecreamOptionDto.cs`, `Dtos/IcecreamDetailDto.cs`).
- **Action 2.2** : Création des requêtes & DTOs d'Authentification (`Requests/SignupRequest.cs`, `Requests/SigninRequest.cs`, `Requests/ChangePasswordRequest.cs`, `Dtos/AuthResponseDto.cs`).
- **Action 2.3** : Création des requêtes & DTOs de Commande (`Requests/OrderPlaceRequest.cs`, `Requests/OrderItemRequest.cs`, `Dtos/OrderDto.cs`, `Dtos/OrderDetailDto.cs`).
- **Action 2.4** : Test de compilation isolé (`dotnet build FullStackCSharp.Shared`).
- **Action 2.5** : Rédaction du livret pédagogique d'étape `Livret/etapes/02_contrats_shared.tex` (Contract-First, immuabilité `record`, DTO vs Entity).
- **Action 2.6** : Relecture, questions/réponses et validation utilisateur.

#### Vérification

```
dotnet build FullStackCSharp.Shared   →  Build succeeded (0 warning)
```

---

### Jalon 3 — Console d'Observabilité Pédagogique

**Périmètre** : Backend (`FullStackCSharp.Back`)  
**Concept clé** : *Rendre visible l'invisible — comprendre ce qui se passe côté serveur en temps réel*

#### Ce qui est construit

| Fichier | Rôle |
| :--- | :--- |
| `Middleware/RequestLoggingMiddleware.cs` | Intercepte chaque requête HTTP entrante et la réponse sortante : méthode, route, code de statut, durée en ms |
| `Middleware/JwtDecodingMiddleware.cs` | Décode et affiche les *Claims* d'un token JWT présent dans l'en-tête `Authorization` |
| `Logging/ConsoleTheme.cs` | Définition du thème ANSI coloré pour les différentes catégories de logs |
| `Extensions/ObservabilityExtensions.cs` | Méthodes d'extension pour enregistrer le pipeline d'observabilité dans `Program.cs` |

#### Charte Visuelle de la Console

| Préfixe | Couleur | Information Affichée |
| :--- | :--- | :--- |
| `[HTTP]` | Vert | Requête entrante — méthode, route, taille du payload |
| `[HTTP]` | Magenta | Réponse sortante — code de statut, durée d'exécution (ms) |
| `[SQL]` | Bleu | Requête SQL brute générée par EF Core, paramètres liés |
| `[AUTH]` | Jaune | Opérations de sécurité — hachage, émission JWT, décodage Claims |
| `[ORDER]` | Cyan | Vérification d'intégrité des commandes, transactions |
| `[ERROR]` | Rouge | Exceptions capturées, erreurs de validation |
| `[STARTUP]` | Cyan clair | Bannière d'accueil, ports Kestrel, version .NET, environnement |

#### Pourquoi c'est fondamental

Dans un projet Fullstack, le serveur est un processus séparé que le développeur ne voit pas directement. Sans observabilité :
- On ne sait pas quelle requête SQL est générée quand on appelle `GET /api/icecreams`.
- On ne voit pas les *Claims* du JWT qui arrivent sur le serveur.
- On ne peut pas vérifier que le prix recalculé côté serveur correspond au prix envoyé par le client.

La console transforme la « boîte noire » du serveur en un **tableau de bord pédagogique** qui révèle chaque rouage interne.

#### Découpage en Micro-Étapes Réalisables

- **Action 3.1** : Création du thème et des codes couleur ANSI (`Logging/ConsoleTheme.cs`).
- **Action 3.2** : Création du middleware d'interception HTTP (`Middleware/RequestLoggingMiddleware.cs`).
- **Action 3.3** : Création du middleware de décodage des Claims JWT (`Middleware/JwtDecodingMiddleware.cs`).
- **Action 3.4** : Création des méthodes d'extension d'observabilité (`Extensions/ObservabilityExtensions.cs`).
- **Action 3.5** : Enregistrement du pipeline dans `Program.cs` et test d'exécution (`dotnet run --project FullStackCSharp.Back`).
- **Action 3.6** : Rédaction du livret pédagogique d'étape `Livret/etapes/03_observabilite.tex` (Pipeline Kestrel, télémétrie, couleurs ANSI).
- **Action 3.7** : Relecture, questions/réponses et validation utilisateur.

#### Vérification

```
dotnet run --project FullStackCSharp.Back
→ Bannière ASCII, ports d'écoute, environnement Development affiché
```

---

## 3. Phase 2 : API Backend Complète (Jalons 4 à 7)

À l'issue de cette phase, l'API est **intégralement fonctionnelle** et testable de manière autonome via `curl`, Postman ou tout client HTTP. Le Frontend mobile n'existe pas encore — et c'est intentionnel.

---

### Jalon 4 — Modèle de Données, EF Core & Seed Data

**Périmètre** : Backend  
**Concept clé** : *Entité ≠ DTO — le modèle interne de la base de données est différent du modèle exposé au client*

#### Ce qui est construit

| Fichier | Rôle |
| :--- | :--- |
| `Data/Entities/User.cs` | Entité utilisateur : `Guid Id`, `Name`, `Email`, `Address`, `PasswordHash` (byte[]), `PasswordSalt` (byte[]) |
| `Data/Entities/Icecream.cs` | Entité glace avec propriétés de navigation EF Core vers `IcecreamOption` |
| `Data/Entities/IcecreamOption.cs` | Entité option de personnalisation liée à une glace (clé étrangère `IcecreamId`) |
| `Data/Entities/Order.cs` | Entité commande : `UserId` (FK), `OrderedAt`, `TotalAmount`, navigation vers `OrderItem` |
| `Data/Entities/OrderItem.cs` | Ligne d'article dans une commande |
| `Data/AppDbContext.cs` | `DbContext` avec `DbSet<T>` pour chaque entité, configuration Fluent API dans `OnModelCreating` |
| `Data/SeedData.cs` | Classe statique fournissant les 18 parfums de glaces et leurs options pour l'alimentation initiale |
| `appsettings.json` | Chaîne de connexion SQLite (`"ConnectionStrings:DefaultConnection": "Data Source=fullstack.db"`) |
| `appsettings.Development.json` | Surcharges spécifiques à l'environnement de développement (niveaux de log EF Core) |

#### Concepts Professionnels Enseignés

1. **Séparation Entité / DTO** :
   - L'entité `Icecream` contient des propriétés de navigation EF Core (`ICollection<IcecreamOption> Options`), des clés de suivi interne et potentiellement des champs d'audit (`CreatedAt`).
   - Le DTO `IcecreamDto` (dans Shared) ne contient que ce que le client a besoin de voir : `Id`, `Name`, `Description`, `Image`, `Price`.
   - La transformation Entité → DTO se fait via des **méthodes de mapping explicites** dans un fichier dédié (`Mapping/IcecreamMapping.cs`).

2. **Configuration EF Core avec Fluent API** :
   - Pas de Data Annotations dans les entités (les entités restent des POCO purs).
   - Toute la configuration relationnelle (clés, index, contraintes, relations) est dans `OnModelCreating`.

3. **Seed Data réaliste** :
   - 18 parfums de glaces avec noms, descriptions, prix et options de personnalisation.
   - Insertion conditionnelle via `HasData()` de EF Core.

4. **Configuration ASP.NET Core** :
   - `appsettings.json` pour les paramètres structurés.
   - Pattern `IOptions<T>` pour l'injection de configuration fortement typée dans les services.

#### Découpage en Micro-Étapes Réalisables

- **Action 4.1** : Création des entités de domaine (`User.cs`, `Icecream.cs`, `IcecreamOption.cs`, `Order.cs`, `OrderItem.cs`).
- **Action 4.2** : Implémentation du contexte `Data/AppDbContext.cs` avec configuration Fluent API dans `OnModelCreating`.
- **Action 4.3** : Création de la classe de seed `Data/SeedData.cs` (18 parfums de glaces et 24 options).
- **Action 4.4** : Configuration de la chaîne SQLite dans `appsettings.json` et enregistrement du DbContext dans `Program.cs`.
- **Action 4.5** : Test d'initialisation en direct : exécution de `EnsureCreatedAsync()`, vérification physique de `fullstack.db` et des données insérées.
- **Action 4.6** : Rédaction du livret pédagogique d'étape `Livret/etapes/04_persistance_efcore.tex` (ORM, Fluent API, POCO).
- **Action 4.7** : Relecture, questions/réponses et validation utilisateur.

#### Console d'Observabilité

```
[STARTUP] Base de données SQLite : fullstack.db
[STARTUP] Migration automatique appliquée (EnsureCreated)
[SQL]     INSERT INTO Icecreams (Name, Description, Image, Price) VALUES (@p0, @p1, @p2, @p3)
[STARTUP] Seed Data : 18 parfums et 24 options insérés
```

#### Vérification

```
dotnet run --project FullStackCSharp.Back
→ Le fichier fullstack.db est créé physiquement sur le disque
→ Les 18 parfums sont visibles dans la console via les logs SQL
```

---

### Jalon 5 — Pipeline HTTP, Middleware & Endpoints du Catalogue

**Périmètre** : Backend  
**Concept clé** : *Le pipeline de requêtes ASP.NET Core — chaque requête traverse une chaîne ordonnée de middleware*

#### Ce qui est construit

| Fichier | Rôle |
| :--- | :--- |
| `Program.cs` | Point d'entrée : registration des services (DI), configuration du pipeline middleware, mapping des endpoints |
| `Middleware/GlobalExceptionMiddleware.cs` | Capture toute exception non gérée, journalise l'erreur et renvoie une réponse JSON `500 Internal Server Error` propre |
| `Services/IcecreamService.cs` | Logique métier du catalogue : `GetAllAsync()`, `GetByIdAsync(int id)` |
| `Endpoints/CatalogEndpoints.cs` | Groupe d'endpoints : `GET /api/icecreams` (liste) et `GET /api/icecreams/{id}` (détail avec options) |
| `Endpoints/HealthEndpoints.cs` | `GET /health` — point de terminaison de vérification de santé de l'API |
| `Mapping/IcecreamMapping.cs` | Méthodes d'extension `ToDto()` et `ToDetailDto()` pour transformer les entités en DTOs |

#### Pipeline Middleware — L'Ordre Compte

```
Program.cs — L'ordre d'enregistrement du pipeline détermine l'ordre d'exécution :

app.UseMiddleware<GlobalExceptionMiddleware>();   ← 1. Capture les exceptions
app.UseMiddleware<RequestLoggingMiddleware>();     ← 2. Journalise requête/réponse
app.UseCors("AllowMauiClient");                   ← 3. Autorise les origines cross-domain
app.UseAuthentication();                          ← 4. Valide le token JWT (si présent)
app.UseAuthorization();                           ← 5. Vérifie les autorisations
app.MapCatalogEndpoints();                        ← 6. Route vers les endpoints métier
app.MapHealthEndpoints();
```

#### Concepts Professionnels Enseignés

1. **Injection de Dépendances (DI)** :
   - `IcecreamService` est enregistré dans le conteneur DI avec `builder.Services.AddScoped<IcecreamService>()`.
   - Les endpoints reçoivent le service **par injection de paramètre** — jamais de `new IcecreamService()`.
   - Cycle de vie `Scoped` = une instance par requête HTTP.

2. **Pipeline de Middleware** :
   - Chaque requête HTTP traverse les middleware dans l'ordre d'enregistrement.
   - La réponse remonte dans l'ordre inverse.
   - L'ordre est **critique** : CORS avant Auth, Auth avant Authorization, Exception handler en premier.

3. **Minimal API avec Groupes d'Endpoints** :
   - Les endpoints sont organisés en fichiers dédiés par domaine fonctionnel (`CatalogEndpoints`, `AuthEndpoints`, `OrderEndpoints`).
   - Chaque fichier est une méthode d'extension statique `MapXxxEndpoints(this WebApplication app)`.
   - Pas de Controller MVC : c'est l'approche moderne recommandée par Microsoft pour les APIs légères.

4. **CORS (Cross-Origin Resource Sharing)** :
   - Configuration explicite pour autoriser le client MAUI à communiquer avec l'API.
   - En production, les origines autorisées seraient restreintes.

5. **Gestion d'Erreurs Globale** :
   - `GlobalExceptionMiddleware` encapsule tout le pipeline dans un `try/catch`.
   - Aucun endpoint ne doit gérer ses propres exceptions — le middleware le fait systématiquement.
   - Le client reçoit toujours une réponse JSON structurée, jamais une stack trace brute.

#### Découpage en Micro-Étapes Réalisables

- **Action 5.1** : Création du middleware global de capture d'exceptions (`Middleware/GlobalExceptionMiddleware.cs`).
- **Action 5.2** : Configuration de la stratégie CORS pour autoriser les requêtes du client MAUI.
- **Action 5.3** : Création des méthodes de mapping `Mapping/IcecreamMapping.cs` (Entités vers DTOs).
- **Action 5.4** : Création du service métier `Services/IcecreamService.cs` (`GetAllAsync`, `GetByIdAsync`).
- **Action 5.5** : Exposition des endpoints de catalogue `Endpoints/CatalogEndpoints.cs` et de santé `Endpoints/HealthEndpoints.cs`.
- **Action 5.6** : Test réel par requêtes curl (`/health`, `/api/icecreams`, `/api/icecreams/1`) et observation des requêtes SQL dans la console.
- **Action 5.7** : Rédaction du livret pédagogique d'étape `Livret/etapes/05_pipeline_catalogue.tex` (Pipeline HTTP ordonné, Minimal APIs, DI Scoped).
- **Action 5.8** : Relecture, questions/réponses et validation utilisateur.

#### Console d'Observabilité

```
[HTTP]    → GET /api/icecreams
[SQL]     SELECT i.Id, i.Name, i.Description, i.Image, i.Price FROM Icecreams AS i
[HTTP]    ← 200 OK (18 éléments, 4.2 KB, 12 ms)

[HTTP]    → GET /api/icecreams/5
[SQL]     SELECT ... FROM Icecreams AS i LEFT JOIN IcecreamOptions AS o ON ... WHERE i.Id = @id
[HTTP]    ← 200 OK (1 élément + 3 options, 0.8 KB, 8 ms)

[HTTP]    → GET /api/icecreams/999
[HTTP]    ← 404 Not Found (3 ms)
```

#### Vérification

```bash
curl http://localhost:5227/health                  →  {"status":"healthy"}
curl http://localhost:5227/api/icecreams            →  JSON array de 18 glaces
curl http://localhost:5227/api/icecreams/1          →  JSON détail avec options
curl http://localhost:5227/api/icecreams/999        →  404 Not Found
```

---

### Jalon 6 — Sécurité : Hachage, JWT & Authentification

**Périmètre** : Backend  
**Concept clé** : *Ne jamais stocker un mot de passe en clair — le serveur ne connaît que le hash*

#### Ce qui est construit

| Fichier | Rôle |
| :--- | :--- |
| `Services/PasswordService.cs` | Hachage `HMACSHA512` avec sel aléatoire : `HashPassword(string password)` → `(byte[] hash, byte[] salt)`, `VerifyPassword(string password, byte[] hash, byte[] salt)` → `bool` |
| `Services/TokenService.cs` | Génération de JWT : `GenerateToken(User user)` → `string`. Claims inclus : `sub`, `email`, `name`, `address`. Signature `HmacSha256` avec clé secrète depuis `appsettings.json` |
| `Services/AuthService.cs` | Orchestration : `SignupAsync(SignupRequest)` → crée l'utilisateur, hache le mot de passe, génère le token. `SigninAsync(SigninRequest)` → vérifie le hash, génère le token |
| `Endpoints/AuthEndpoints.cs` | `POST /api/signup` et `POST /api/signin` — endpoints publics (sans `[Authorize]`) |
| `Configuration/JwtSettings.cs` | Classe POCO pour `IOptions<JwtSettings>` : `SecretKey`, `Issuer`, `Audience`, `ExpirationDays` |
| `Extensions/AuthenticationExtensions.cs` | Configuration du middleware `AddAuthentication().AddJwtBearer()` avec validation des paramètres du token |

#### Concepts Professionnels Enseignés

1. **Hachage Cryptographique Salé** :
   - Le mot de passe n'est **jamais** stocké en clair ni chiffré de manière réversible.
   - `HMACSHA512` produit un hash de 64 octets à partir du mot de passe + un sel aléatoire de 128 octets.
   - Le sel est **unique par utilisateur** : deux utilisateurs avec le même mot de passe ont des hash différents.
   - Vérification : on recalcule le hash avec le même sel et on compare octet par octet.

2. **JSON Web Token (JWT)** :
   - Un JWT est composé de 3 parties : `Header.Payload.Signature` encodées en Base64.
   - Le **Header** indique l'algorithme de signature (`HS256`).
   - Le **Payload** contient les *Claims* : identifiant utilisateur, email, nom, date d'expiration.
   - La **Signature** garantit que le token n'a pas été modifié — le serveur la vérifie avec sa clé secrète.
   - Le client stocke le token et l'envoie dans chaque requête protégée via l'en-tête `Authorization: Bearer <token>`.

3. **Configuration Fortement Typée (`IOptions<T>`)** :
   - Les paramètres JWT (`SecretKey`, `ExpirationDays`, etc.) sont dans `appsettings.json`.
   - Ils sont injectés dans `TokenService` via `IOptions<JwtSettings>` — jamais de valeurs codées en dur.

4. **Middleware d'Authentification ASP.NET Core** :
   - `AddAuthentication().AddJwtBearer()` configure la validation automatique du token sur chaque requête.
   - Les endpoints marqués `RequireAuthorization()` rejettent automatiquement les requêtes sans token valide avec `401 Unauthorized`.

#### Découpage en Micro-Étapes Réalisables

- **Action 6.1** : Création du service de hachage `Services/PasswordService.cs` (HMACSHA512 et sel cryptographique aléatoire de 128 octets).
- **Action 6.2** : Création de la classe `Configuration/JwtSettings.cs` et du service de génération `Services/TokenService.cs`.
- **Action 6.3** : Création du service d'orchestration `Services/AuthService.cs` (`SignupAsync`, `SigninAsync`).
- **Action 6.4** : Exposition des endpoints `Endpoints/AuthEndpoints.cs` et câblage de `AddJwtBearer` dans `Program.cs`.
- **Action 6.5** : Test réel par requêtes curl : inscription réussie, connexion valide avec émission du token, rejet 401 sur mot de passe erroné.
- **Action 6.6** : Rédaction du livret pédagogique d'étape `Livret/etapes/06_securite_jwt.tex` (Cryptographie irréversible, tokens sans état, Claims).
- **Action 6.7** : Relecture, questions/réponses et validation utilisateur.

#### Console d'Observabilité

```
[HTTP]    → POST /api/signup  (Name: "Alice", Email: "alice@test.com")
[AUTH]    Génération du sel cryptographique : 128 octets aléatoires
[AUTH]    Hachage HMACSHA512 : mot de passe (6 chars) → hash (64 octets)
[SQL]     INSERT INTO Users (Id, Name, Email, Address, PasswordHash, PasswordSalt) VALUES (...)
[AUTH]    Émission JWT — Claims décodés :
          ┌─────────────────────────────────────────────────┐
          │  sub     : 3f2504e0-4f89-11d3-9a0c-0305e82c3301 │
          │  email   : alice@test.com                        │
          │  name    : Alice                                 │
          │  address : 12 rue des Lilas                      │
          │  exp     : 2026-11-18T02:00:00Z (7 jours)        │
          └─────────────────────────────────────────────────┘
[HTTP]    ← 200 OK (token JWT émis, 0.9 KB, 45 ms)

[HTTP]    → POST /api/signin  (Email: "alice@test.com")
[SQL]     SELECT ... FROM Users WHERE Email = @email
[AUTH]    Vérification du hash : ✓ Mot de passe valide
[AUTH]    Émission JWT — Claims : sub=3f2504e0..., email=alice@test.com
[HTTP]    ← 200 OK (token JWT émis, 18 ms)

[HTTP]    → POST /api/signin  (Email: "alice@test.com", mot de passe erroné)
[AUTH]    Vérification du hash : ✗ Mot de passe invalide
[HTTP]    ← 401 Unauthorized (5 ms)
```

#### Vérification

```bash
# Inscription
curl -X POST http://localhost:5227/api/signup \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@test.com","address":"12 rue des Lilas","password":"Test123"}'
→ {"token":"eyJhbG...","name":"Alice","email":"alice@test.com"}

# Connexion
curl -X POST http://localhost:5227/api/signin \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@test.com","password":"Test123"}'
→ {"token":"eyJhbG...","name":"Alice","email":"alice@test.com"}

# Accès protégé SANS token
curl http://localhost:5227/api/orders/my-orders
→ 401 Unauthorized
```

---

### Jalon 7 — Endpoints Protégés : Commandes & Profil

**Périmètre** : Backend  
**Concept clé** : *Endpoints authentifiés — le serveur extrait l'identité de l'utilisateur depuis le token JWT, pas depuis le corps de la requête*

#### Ce qui est construit

| Fichier | Rôle |
| :--- | :--- |
| `Services/OrderService.cs` | `PlaceOrderAsync(OrderPlaceRequest request, Guid userId)` — validation du montant, insertion transactionnelle, retour de l'identifiant de commande. `GetUserOrdersAsync(Guid userId)` — historique filtré par utilisateur. `GetOrderDetailAsync(long orderId, Guid userId)` — détail d'une commande spécifique |
| `Endpoints/OrderEndpoints.cs` | `POST /api/orders` (créer), `GET /api/orders/my-orders` (historique), `GET /api/orders/{id}` (détail). Tous protégés par `RequireAuthorization()` |
| `Endpoints/ProfileEndpoints.cs` | `POST /api/change-password` — changement de mot de passe sécurisé (vérification ancien + nouveau hash) |
| `Extensions/ClaimsPrincipalExtensions.cs` | Méthode d'extension `GetUserId(this ClaimsPrincipal)` → `Guid` pour extraire proprement l'identité depuis les Claims |
| `Mapping/OrderMapping.cs` | Méthodes de transformation `Order` → `OrderDto`, `Order` → `OrderDetailDto` |

#### Concepts Professionnels Enseignés

1. **Extraction de l'Identité depuis le JWT** :
   - Le `UserId` n'est **jamais** envoyé dans le corps de la requête par le client.
   - Le serveur l'extrait du *Claim* `sub` du token JWT via `HttpContext.User.GetUserId()`.
   - C'est une règle de sécurité fondamentale : le client ne peut pas usurper l'identité d'un autre utilisateur.

2. **Vérification Anti-Fraude des Prix** :
   - Le client envoie un `TotalAmount` dans la commande.
   - Le serveur **recalcule** le total à partir des prix réels stockés en base de données.
   - Si l'écart dépasse un seuil de tolérance (erreurs d'arrondi), la commande est rejetée.
   - C'est une pratique standard dans tout système de e-commerce.

3. **Transaction Relationnelle** :
   - L'insertion d'une commande (`Order`) et de ses lignes d'articles (`OrderItem`) est encapsulée dans une transaction EF Core.
   - Si l'insertion d'un article échoue, toute la commande est annulée (*rollback*) — la base de données ne reste jamais dans un état incohérent.

4. **Changement de Mot de Passe Sécurisé** :
   - L'ancien mot de passe est vérifié avant d'accepter le nouveau.
   - Un **nouveau sel** est généré pour le nouveau hash — on ne réutilise jamais un ancien sel.

#### Découpage en Micro-Étapes Réalisables

- **Action 7.1** : Création de la méthode d'extension `Extensions/ClaimsPrincipalExtensions.cs` pour l'extraction sécurisée du `UserId`.
- **Action 7.2** : Création des méthodes de mapping `Mapping/OrderMapping.cs`.
- **Action 7.3** : Implémentation du service métier `Services/OrderService.cs` (transaction SQL, recalcul anti-fraude, filtrage par utilisateur).
- **Action 7.4** : Exposition des endpoints de commandes protégés `Endpoints/OrderEndpoints.cs` (`POST /api/orders`, `GET /api/orders/my-orders`, `GET /api/orders/{id}`).
- **Action 7.5** : Exposition de l'endpoint de profil `Endpoints/ProfileEndpoints.cs` pour le changement de mot de passe sécurisé.
- **Action 7.6** : Test réel via curl : passage de commande avec token Bearer (HTTP 201), historique filtré, modification de mot de passe.
- **Action 7.7** : Rédaction du livret pédagogique d'étape `Livret/etapes/07_endpoints_proteges.tex` (Routes protégées, transactions ACID, sécurité anti-tampering).
- **Action 7.8** : Relecture, questions/réponses et validation utilisateur.

#### Console d'Observabilité

```
[HTTP]    → POST /api/orders  (Authorization: Bearer eyJhbG...)
[AUTH]    Token JWT validé — UserId: 3f2504e0-4f89-11d3-9a0c-0305e82c3301
[ORDER]   Vérification d'intégrité des prix :
          ┌──────────────────────────────────────────────────────────┐
          │  Article         │ Prix Client │ Prix Base │ Statut     │
          │  Vanille x2      │    5.98 €   │   5.98 €  │  ✓ Valide  │
          │  + Choco Sauce   │    1.50 €   │   1.50 €  │  ✓ Valide  │
          │  Fraise x1       │    3.49 €   │   3.49 €  │  ✓ Valide  │
          │─────────────────────────────────────────────────────────│
          │  Total Client    │   10.97 €                            │
          │  Total Recalculé │   10.97 €    ✓ Concordance parfaite  │
          └──────────────────────────────────────────────────────────┘
[SQL]     BEGIN TRANSACTION
[SQL]     INSERT INTO Orders (Id, UserId, OrderedAt, TotalAmount) VALUES (...)
[SQL]     INSERT INTO OrderItems (OrderId, IcecreamId, Name, UnitPrice, Quantity, Options) VALUES (...)
[SQL]     INSERT INTO OrderItems ...
[SQL]     COMMIT
[HTTP]    ← 201 Created (OrderId: 1, 22 ms)
```

#### Vérification

```bash
# Passage de commande (avec token JWT obtenu au Jalon 6)
curl -X POST http://localhost:5227/api/orders \
  -H "Authorization: Bearer eyJhbG..." \
  -H "Content-Type: application/json" \
  -d '{"items":[{"icecreamId":1,"name":"Vanille","unitPrice":2.99,"quantity":2,"options":["Choco Sauce"]}],"totalAmount":7.48}'
→ 201 Created

# Historique
curl http://localhost:5227/api/orders/my-orders \
  -H "Authorization: Bearer eyJhbG..."
→ [{"id":1,"orderedAt":"2026-11-11T...","totalAmount":7.48,"itemCount":1}]

# Changement de mot de passe
curl -X POST http://localhost:5227/api/change-password \
  -H "Authorization: Bearer eyJhbG..." \
  -H "Content-Type: application/json" \
  -d '{"oldPassword":"Test123","newPassword":"NewPass456"}'
→ 200 OK
```

**→ À ce stade (à la fin de la Phase 2), l'API Backend devient entièrement opérationnelle et testable de manière autonome.**

---

## 4. Phase 3 : Client Mobile .NET MAUI (Jalons 8 à 11)

Le Backend fonctionne. On construit maintenant le client mobile qui va consommer cette API réelle.

---

### Jalon 8 — Structure MAUI, AppShell & Navigation

**Périmètre** : Frontend  
**Concept clé** : *Shell Navigation — le système de routage déclaratif de .NET MAUI*

#### Ce qui est construit

| Fichier | Rôle |
| :--- | :--- |
| `App.xaml` / `App.xaml.cs` | Point d'entrée MAUI, définition des ressources globales (couleurs, styles) |
| `AppShell.xaml` / `AppShell.xaml.cs` | Squelette de navigation : `TabBar` (onglets principaux) et routes enregistrées |
| `MauiProgram.cs` | Configuration DI, enregistrement des services, des ViewModels et des Pages |
| `Pages/OnboardingPage.xaml` | Écran d'accueil initial (avant connexion) |
| `Pages/SigninPage.xaml` | Formulaire de connexion |
| `Pages/SignupPage.xaml` | Formulaire d'inscription |
| `Pages/HomePage.xaml` | Page principale — catalogue de glaces (après connexion) |
| `Pages/DetailsPage.xaml` | Détail et personnalisation d'une glace |
| `Pages/CartPage.xaml` | Panier d'achat |
| `Pages/ProfilePage.xaml` | Profil utilisateur |
| `Pages/MyOrdersPage.xaml` | Historique des commandes |
| `Pages/OrderDetailsPage.xaml` | Détail d'une commande passée |

#### Concepts Professionnels Enseignés

1. **Injection de Dépendances dans MAUI** :
   - `MauiProgram.cs` enregistre chaque Page et chaque ViewModel dans le conteneur DI.
   - Les Pages reçoivent leur ViewModel par injection de constructeur.
   - Les ViewModels reçoivent les services réseau par injection.
   - Cycle de vie : `AddTransient` pour les Pages (recréées à chaque navigation), `AddSingleton` pour les services partagés.

2. **Shell Navigation** :
   - Les onglets principaux (`TabBar`) : Accueil, Panier, Profil.
   - Les pages détachées (`Routing.RegisterRoute`) : Détails, Commandes, Inscription, etc.
   - Navigation par URI : `Shell.Current.GoToAsync("details?id=5")`.
   - Passage de paramètres avec `[QueryProperty]`.

3. **Ressources XAML Globales** :
   - Palette de couleurs centralisée dans `App.xaml`.
   - Styles implicites et explicites pour garantir la cohérence visuelle.
   - 100% vectoriel : les icônes sont des SVG ou des géométries XAML.

#### Découpage en Micro-Étapes Réalisables

- **Action 8.1** : Configuration du conteneur DI et enregistrement des premières pages dans `MauiProgram.cs`.
- **Action 8.2** : Définition des couleurs, pinceaux et styles vectoriels globaux dans `App.xaml`.
- **Action 8.3** : Conception de l'arborescence Shell déclarative dans `AppShell.xaml` (barre d'onglets `TabBar` et routes enfants).
- **Action 8.4** : Création des pages XAML squelettes (`OnboardingPage`, `SigninPage`, `SignupPage`, `HomePage`, `CartPage`, `ProfilePage`, `MyOrdersPage`, `OrderDetailsPage`).
- **Action 8.5** : Test de compilation et de lancement à blanc (`dotnet build FullStackCSharp.Front`).
- **Action 8.6** : Rédaction du livret pédagogique d'étape `Livret/etapes/08_structure_maui_shell.tex` (Architecture MAUI, Shell, styles XAML).
- **Action 8.7** : Relecture, questions/réponses et validation utilisateur.

#### Vérification

```
dotnet build FullStackCSharp.Front
→ Build succeeded
→ L'application démarre, affiche l'OnboardingPage, et la navigation entre les pages fonctionne
```

---

### Jalon 9 — Couche Réseau : HttpClient, Refit & Injection du Token JWT

**Périmètre** : Frontend  
**Concept clé** : *DelegatingHandler — intercepter automatiquement chaque requête HTTP pour y injecter le token JWT*

#### Ce qui est construit

| Fichier | Rôle |
| :--- | :--- |
| `Services/TokenStorageService.cs` | Stockage et récupération du token JWT via `SecureStorage` de MAUI (coffre-fort chiffré natif du système d'exploitation) |
| `Http/AuthHeaderHandler.cs` | `DelegatingHandler` : intercepte chaque requête HTTP sortante et ajoute l'en-tête `Authorization: Bearer <token>` si un token est stocké |
| `Http/ApiContracts/IAuthApi.cs` | Interface Refit : `[Post("/api/signup")]`, `[Post("/api/signin")]`, `[Post("/api/change-password")]` |
| `Http/ApiContracts/ICatalogApi.cs` | Interface Refit : `[Get("/api/icecreams")]`, `[Get("/api/icecreams/{id}")]` |
| `Http/ApiContracts/IOrderApi.cs` | Interface Refit : `[Post("/api/orders")]`, `[Get("/api/orders/my-orders")]`, `[Get("/api/orders/{id}")]` |
| `Extensions/HttpClientExtensions.cs` | Enregistrement dans `MauiProgram.cs` : `AddRefitClient<IAuthApi>()`, configuration du `HttpMessageHandler` pipeline |

#### Concepts Professionnels Enseignés

1. **`IHttpClientFactory`** :
   - Jamais de `new HttpClient()` direct — c'est une fuite de ressources classique (épuisement des sockets).
   - `IHttpClientFactory` gère le cycle de vie des `HttpClient` et le pool de connexions.

2. **`DelegatingHandler` pour le Token JWT** :
   - `AuthHeaderHandler` est un maillon de la chaîne de traitement HTTP.
   - Il lit le token depuis `SecureStorage` et l'ajoute à l'en-tête `Authorization` de **chaque** requête sortante.
   - Les ViewModels n'ont jamais à se soucier de la gestion du token — c'est transparent.

3. **Refit — Client HTTP Déclaratif** :
   - On définit une interface C# avec des attributs `[Get]`, `[Post]`, etc.
   - Refit génère automatiquement l'implémentation à la compilation.
   - Les types de retour et de paramètres utilisent les DTOs de `FullStackCSharp.Shared` — typage fort garanti.

4. **`SecureStorage`** :
   - Le token JWT est stocké dans le coffre-fort chiffré natif de l'OS (Keychain sur iOS, KeyStore sur Android, DPAPI sur Windows).
   - C'est l'approche recommandée par Microsoft pour stocker des données sensibles dans une application MAUI.

#### Découpage en Micro-Étapes Réalisables

- **Action 9.1** : Création du service de stockage sécurisé `Services/TokenStorageService.cs` (`SecureStorage`).
- **Action 9.2** : Création du handler réseau `Http/AuthHeaderHandler.cs` (`DelegatingHandler`).
- **Action 9.3** : Définition des interfaces d'API déclaratives Refit (`IAuthApi.cs`, `ICatalogApi.cs`, `IOrderApi.cs`).
- **Action 9.4** : Enregistrement de `IHttpClientFactory` et des clients Refit dans `MauiProgram.cs`.
- **Action 9.5** : Test de connectivité réseau client-serveur (appel `/health` depuis le client).
- **Action 9.6** : Rédaction du livret pédagogique d'étape `Livret/etapes/09_reseau_refit_jwt.tex` (HttpMessageHandler pipeline, Refit, SecureStorage).
- **Action 9.7** : Relecture, questions/réponses et validation utilisateur.

#### Vérification

```
L'application compile et le pipeline HTTP est fonctionnel.
Le AuthHeaderHandler injecte correctement le token dans chaque requête.
Le serveur reçoit et valide le token — visible dans la console d'observabilité.
```

---

### Jalon 10 — Flux d'Authentification : Onboarding, Connexion, Inscription

**Périmètre** : Frontend (consomme le Backend du Jalon 6)  
**Concept clé** : *MVVM — le ViewModel orchestre la logique, la View ne fait que présenter*

#### Ce qui est construit

| Fichier | Rôle |
| :--- | :--- |
| `ViewModels/OnboardingViewModel.cs` | Navigation vers la page de connexion ou d'inscription |
| `ViewModels/SigninViewModel.cs` | Propriétés observables (`Email`, `Password`, `IsBusy`, `ErrorMessage`), commande `[RelayCommand] SigninAsync()` |
| `ViewModels/SignupViewModel.cs` | Propriétés observables (Name, Email, Address, Password), commande `[RelayCommand] SignupAsync()` |
| `Pages/OnboardingPage.xaml` | Interface d'accueil avec illustration SVG et boutons |
| `Pages/SigninPage.xaml` | Formulaire lié au ViewModel par `{Binding}` |
| `Pages/SignupPage.xaml` | Formulaire lié au ViewModel par `{Binding}` |

#### Concepts Professionnels Enseignés

1. **MVVM avec CommunityToolkit.Mvvm** :
   - `[ObservableProperty]` : génère automatiquement la propriété publique + l'événement `PropertyChanged` depuis un champ privé.
   - `[RelayCommand]` : génère une `ICommand` depuis une méthode async — le bouton XAML se lie à `SigninCommand`.
   - Le ViewModel ne connaît **aucune** classe XAML : il ne manipule que des données et des services.

2. **Data Binding Bidirectionnel** :
   - `<Entry Text="{Binding Email}" />` : ce que l'utilisateur tape dans le champ met à jour la propriété du ViewModel en temps réel.
   - `<Button Command="{Binding SigninCommand}" />` : le clic déclenche la méthode async du ViewModel.
   - `<ActivityIndicator IsRunning="{Binding IsBusy}" />` : l'indicateur de chargement s'active automatiquement pendant l'appel réseau.

3. **Gestion des États de Chargement** :
   - `IsBusy = true` avant l'appel API, `IsBusy = false` après.
   - Le `[RelayCommand]` supporte nativement `CanExecute` qui désactive le bouton pendant le traitement.

4. **Flux de Navigation Post-Authentification** :
   - Connexion réussie → stockage du token dans `SecureStorage` → navigation vers `HomePage`.
   - Connexion échouée → affichage d'un message d'erreur dans le formulaire (pas de crash).

#### Découpage en Micro-Étapes Réalisables

- **Action 10.1** : Implémentation de `ViewModels/OnboardingViewModel.cs` et de la vue d'accueil `Pages/OnboardingPage.xaml`.
- **Action 10.2** : Implémentation de `ViewModels/SignupViewModel.cs` et du formulaire d'inscription `Pages/SignupPage.xaml` avec liaison bidirectionnelle.
- **Action 10.3** : Implémentation de `ViewModels/SigninViewModel.cs` et du formulaire de connexion `Pages/SigninPage.xaml` avec indicateur `IsBusy` et gestion d'erreur.
- **Action 10.4** : Test complet du flux : Inscription $\to$ Connexion $\to$ Stockage JWT $\to$ Redirection vers `HomePage`.
- **Action 10.5** : Rédaction du livret pédagogique d'étape `Livret/etapes/10_flux_authentification.tex` (MVVM, Data Binding, commandes asynchrones).
- **Action 10.6** : Relecture, questions/réponses et validation utilisateur.

#### Vérification

```
1. Lancer le Backend (dotnet run --project FullStackCSharp.Back)
2. Lancer le Frontend (dotnet run --project FullStackCSharp.Front)
3. S'inscrire avec un email/mot de passe → Le token JWT apparaît dans la console backend
4. Se connecter avec les mêmes identifiants → Redirection vers HomePage
5. Entrer un mauvais mot de passe → Message d'erreur affiché, pas de crash
```

---

### Jalon 11 — Catalogue, Détails & Personnalisation Produit

**Périmètre** : Frontend (consomme les endpoints catalogue du Jalon 5)  
**Concept clé** : *CollectionView, DataTemplate & Navigation avec paramètres*

#### Ce qui est construit

| Fichier | Rôle |
| :--- | :--- |
| `ViewModels/HomeViewModel.cs` | Chargement du catalogue via `ICatalogApi.GetAllAsync()`, collection `ObservableCollection<IcecreamDto>` |
| `ViewModels/DetailsViewModel.cs` | Réception de l'id par `[QueryProperty]`, chargement du détail, sélection des options, gestion de la quantité, calcul du sous-total |
| `Pages/HomePage.xaml` | `CollectionView` en grille 2 colonnes avec `DataTemplate` pour chaque carte de glace (illustration SVG, nom, prix) |
| `Pages/DetailsPage.xaml` | Affichage de la glace sélectionnée, liste des options avec cases à cocher, sélecteur de quantité (+/-), bouton « Ajouter au panier » |
| `Controls/IcecreamCard.xaml` | Composant XAML réutilisable pour l'affichage d'une carte de glace dans le catalogue |

#### Concepts Professionnels Enseignés

1. **`CollectionView` et Virtualisation** :
   - `CollectionView` remplace `ListView` dans les applications MAUI modernes.
   - Elle virtualise le rendu : seuls les éléments visibles à l'écran sont réellement instanciés.
   - `ItemsLayout="VerticalGrid, 2"` pour une grille à 2 colonnes.

2. **`DataTemplate` et Liaison de Données** :
   - Chaque cellule du catalogue est décrite par un `DataTemplate` qui se lie aux propriétés du `IcecreamDto`.
   - Le `DataTemplate` est un patron visuel qui s'applique automatiquement à chaque élément de la collection.

3. **Navigation avec Paramètres** :
   - `Shell.Current.GoToAsync($"details?id={icecream.Id}")`.
   - Le ViewModel cible déclare `[QueryProperty(nameof(IcecreamId), "id")]` pour recevoir le paramètre.
   - Le chargement du détail est déclenché dans le setter de la propriété.

4. **Composants XAML Réutilisables** :
   - `IcecreamCard` est un `ContentView` dédié qui encapsule la mise en page d'une carte de glace.
   - Il est réutilisable dans n'importe quelle page sans dupliquer le XAML.

#### Découpage en Micro-Étapes Réalisables

- **Action 11.1** : Conception du composant réutilisable `Controls/IcecreamCard.xaml` (illustration vectorielle, libellé, prix).
- **Action 11.2** : Implémentation de `ViewModels/HomeViewModel.cs` et de la grille `CollectionView` dans `Pages/HomePage.xaml`.
- **Action 11.3** : Implémentation de `ViewModels/DetailsViewModel.cs` avec réception de paramètre `[QueryProperty]` et calcul de sous-total.
- **Action 11.4** : Conception de la vue de détail `Pages/DetailsPage.xaml` (choix des garnitures, portions, bouton d'ajout au panier).
- **Action 11.5** : Test de navigation : sélection d'une glace depuis la grille, affichage des options et vérification du calcul dynamique.
- **Action 11.6** : Rédaction du livret pédagogique d'étape `Livret/etapes/11_catalogue_details.tex` (Virtualisation CollectionView, QueryProperty, DataTemplate).
- **Action 11.7** : Relecture, questions/réponses et validation utilisateur.

#### Vérification

```
1. Lancer Backend + Frontend
2. Se connecter → La HomePage affiche les 18 glaces en grille 2 colonnes
3. Toucher une glace → Navigation vers DetailsPage avec les informations correctes
4. Sélectionner des options, ajuster la quantité → Le sous-total se recalcule en temps réel
```

---

## 5. Phase 4 : Fonctionnalités Transversales & Finalisation (Jalons 12 à 15)

Cette phase complète l'application avec les fonctionnalités qui traversent les deux couches (Front + Back) et implémentent le cycle de vie complet d'une commande.

---

### Jalon 12 — Panier Local (SQLite Client) & Interface CRUD

**Périmètre** : Frontend  
**Concept clé** : *Double persistance — le serveur a SA base SQLite, le client a la SIENNE*

#### Ce qui est construit

| Fichier | Rôle |
| :--- | :--- |
| `Data/CartItemEntity.cs` | Entité SQLite locale : `Id`, `IcecreamId`, `Name`, `UnitPrice`, `Quantity`, `OptionsJson` (options sérialisées) |
| `Services/DatabaseService.cs` | Service `IAsyncDisposable` gérant la connexion SQLite locale (`sqlite-net-pcl`). Méthodes : `AddOrUpdateAsync`, `GetAllAsync`, `RemoveAsync`, `ClearAllAsync` |
| `ViewModels/CartViewModel.cs` | Chargement des articles depuis la base locale, ajout avec détection des doublons (même glace + mêmes options → incrément de quantité), suppression unitaire, vidage complet, calcul du total |
| `Pages/CartPage.xaml` | Liste des articles avec `SwipeView` pour supprimer, affichage du nom, des options, de la quantité et du prix, bouton de vidage intégral avec dialogue de confirmation, bouton « Commander » |

#### Concepts Professionnels Enseignés

1. **Pourquoi deux bases SQLite distinctes ?**
   - La base **serveur** (`fullstack.db` via EF Core) stocke les données centralisées : utilisateurs, catalogue, commandes validées.
   - La base **client** (`cart.db` via `sqlite-net-pcl`) stocke les données locales temporaires : le panier en cours de construction.
   - Le panier survit à la fermeture de l'application, mais n'est jamais synchronisé avec le serveur tant que l'utilisateur ne passe pas commande.
   - C'est le même principe que les sites de e-commerce : le panier est local (cookies/localStorage) jusqu'au checkout.

2. **`sqlite-net-pcl` vs Entity Framework Core** :
   - EF Core est un ORM complet avec migrations, Fluent API, change tracking — adapté au serveur.
   - `sqlite-net-pcl` est un micro-ORM léger avec attributs `[Table]`, `[PrimaryKey]`, `[AutoIncrement]` — adapté au client mobile.
   - Deux outils différents pour deux contextes différents.

3. **Détection de Doublons Intelligente** :
   - Ajouter « Vanille + Sauce Chocolat, quantité 1 » deux fois ne crée pas deux lignes → la quantité passe à 2.
   - Ajouter « Vanille + Sauce Caramel » crée une nouvelle ligne car les options sont différentes.
   - La comparaison se fait sur `IcecreamId` + `OptionsJson` (chaîne JSON triée).

4. **`IAsyncDisposable`** :
   - `DatabaseService` implémente `IAsyncDisposable` pour garantir la fermeture propre de la connexion SQLite.
   - Le conteneur DI de MAUI gère automatiquement le cycle de vie.

#### Découpage en Micro-Étapes Réalisables

- **Action 12.1** : Création du modèle d'entité SQLite local `Data/CartItemEntity.cs`.
- **Action 12.2** : Implémentation du service d'accès aux données local `Services/DatabaseService.cs` (`IAsyncDisposable`).
- **Action 12.3** : Implémentation de `ViewModels/CartViewModel.cs` (algorithme de fusion de doublons, calcul de total, commandes CRUD).
- **Action 12.4** : Conception de `Pages/CartPage.xaml` (affichage des lignes avec `SwipeView`, dialogue de confirmation de vidage).
- **Action 12.5** : Test de persistance locale : ajout d'articles, arrêt forcé de l'application, relance et vérification du panier conservé.
- **Action 12.6** : Rédaction du livret pédagogique d'étape `Livret/etapes/12_panier_sqlite_local.tex` (Stockage hors-ligne, sqlite-net-pcl vs EF Core).
- **Action 12.7** : Relecture, questions/réponses et validation utilisateur.

#### Vérification

```
1. Depuis DetailsPage, ajouter 2 glaces au panier avec des options différentes
2. Naviguer vers CartPage → Les 2 articles sont affichés avec les bons prix
3. Fermer l'application complètement, la rouvrir → Le panier est toujours là
4. Glisser un article vers la gauche (SwipeView) → Suppression avec confirmation
5. Vider le panier → Dialogue de confirmation → Liste vide
```

---

### Jalon 13 — Passage de Commande : Flux Client → Serveur

**Périmètre** : Frontend + Backend  
**Concept clé** : *Le flux transactionnel complet — du bouton « Commander » au HTTP 201 Created*

#### Ce qui est construit

| Fichier | Modifications |
| :--- | :--- |
| `ViewModels/CartViewModel.cs` | Ajout de `PlaceOrderAsync()` : transformation des `CartItemEntity` locaux en `OrderPlaceRequest` (DTO Shared), envoi via `IOrderApi.PlaceOrderAsync()` avec token JWT, vidage du panier local en cas de succès |

#### Flux Complet (ce qui se passe réellement quand l'utilisateur appuie sur « Commander »)

```
CLIENT                                                    SERVEUR
  │                                                          │
  │  1. CartViewModel lit les articles depuis SQLite local    │
  │  2. Transforme CartItemEntity[] → OrderPlaceRequest       │
  │  3. AuthHeaderHandler injecte le token JWT                │
  │  ─── POST /api/orders (JSON + Bearer Token) ───────────► │
  │                                                          │
  │                     4. JWT validé → UserId extrait        │
  │                     5. Prix recalculés depuis la DB       │
  │                     6. BEGIN TRANSACTION                  │
  │                     7. INSERT Order + OrderItems          │
  │                     8. COMMIT                             │
  │                                                          │
  │  ◄──────────────── 201 Created (OrderId: 42) ─────────── │
  │                                                          │
  │  9. Vidage de la base SQLite locale (cart.db)             │
  │  10. Notification toast "Commande validée !"             │
  │  11. Navigation vers la page d'accueil                   │
  │                                                          │
```

#### Gestion d'Erreurs Réaliste

| Situation | Comportement Client | Comportement Serveur |
| :--- | :--- | :--- |
| Token expiré | Reçoit `401 Unauthorized` → Redirige vers la page de connexion | Rejette la requête avant tout traitement |
| Serveur injoignable | Exception réseau capturée → Message « Connexion impossible, réessayez » | — |
| Prix modifié entre-temps | Reçoit `400 Bad Request` → Message « Les prix ont changé, rafraîchissez votre panier » | Détecte l'écart de prix, refuse la commande |
| Commande valide | Reçoit `201 Created` → Vide le panier, affiche le toast | Insère la commande, retourne l'identifiant |

#### Découpage en Micro-Étapes Réalisables

- **Action 13.1** : Implémentation de la méthode `PlaceOrderAsync` dans `ViewModels/CartViewModel.cs` (transformation `CartItemEntity` vers `OrderPlaceRequest`).
- **Action 13.2** : Émission de la requête réseau sécurisée via `IOrderApi.PlaceOrderAsync` avec token JWT injecté automatiquement.
- **Action 13.3** : Prise en charge du statut de succès `201 Created` : appel à `DatabaseService.ClearAllAsync()`, mise à jour du badge et toast de confirmation.
- **Action 13.4** : Gestion des erreurs réseau et codes HTTP (401 session expirée, 400 discordance de tarif).
- **Action 13.5** : Test d'intégration de bout en bout : du clic sur « Commander » à la validation transactionnelle dans la console Kestrel.
- **Action 13.6** : Rédaction du livret pédagogique d'étape `Livret/etapes/13_commande_flux_complet.tex` (Flux transactionnel, intégrité des données, résilience réseau).
- **Action 13.7** : Relecture, questions/réponses et validation utilisateur.

#### Vérification

```
1. Remplir le panier avec 2-3 articles
2. Appuyer sur « Commander »
3. Observer dans la console backend : la vérification anti-fraude des prix, la transaction SQL
4. Le panier se vide côté client
5. Un toast « Commande #42 validée » s'affiche
```

---

### Jalon 14 — Profil Utilisateur, Historique & Détails des Commandes

**Périmètre** : Frontend (consomme les endpoints du Jalon 7)  
**Concept clé** : *Exploitation des Claims JWT côté client et côté serveur pour personnaliser l'expérience*

#### Ce qui est construit

| Fichier | Rôle |
| :--- | :--- |
| `ViewModels/ProfileViewModel.cs` | Lecture des informations utilisateur depuis les Claims du token JWT décodé localement (nom, email, adresse). Génération des initiales pour l'avatar. Commande `SignoutAsync()` : suppression du token de `SecureStorage`, redirection vers l'Onboarding |
| `ViewModels/MyOrdersViewModel.cs` | Chargement de l'historique via `IOrderApi.GetMyOrdersAsync()`, affichage en `ObservableCollection<OrderDto>` |
| `ViewModels/OrderDetailsViewModel.cs` | Chargement du détail d'une commande spécifique via `IOrderApi.GetOrderDetailAsync(id)` |
| `Pages/ProfilePage.xaml` | Avatar circulaire avec initiales (généré en XAML pur), informations utilisateur, bouton de déconnexion, bouton d'accès à l'historique, bouton de changement de mot de passe |
| `Pages/MyOrdersPage.xaml` | `CollectionView` des commandes passées : identifiant, date formatée, montant total, nombre d'articles |
| `Pages/OrderDetailsPage.xaml` | Détail ligne par ligne d'une commande : nom de chaque glace, options choisies, quantité, prix unitaire et montant total |

#### Concepts Professionnels Enseignés

1. **Décodage JWT Côté Client** :
   - Le token JWT peut être décodé côté client (le Payload est du Base64, pas du chiffrement).
   - On en extrait le nom et l'email pour l'affichage du profil **sans** faire un appel API supplémentaire.
   - Attention : le décodage côté client ne remplace pas la validation côté serveur.

2. **Déconnexion (Sign Out)** :
   - Suppression du token de `SecureStorage`.
   - Réinitialisation de la pile de navigation vers `OnboardingPage`.
   - Le `AuthHeaderHandler` n'enverra plus de token → toutes les requêtes protégées retourneront `401`.

3. **Formatage & Présentation des Données** :
   - Dates formatées en français (`OrderedAt.ToString("dd MMMM yyyy à HH:mm", new CultureInfo("fr-FR"))`).
   - Montants en euros avec `ToString("C", new CultureInfo("fr-FR"))`.

#### Découpage en Micro-Étapes Réalisables

- **Action 14.1** : Implémentation de `ViewModels/ProfileViewModel.cs` et de `Pages/ProfilePage.xaml` (décodage Claims local, avatar d'initiales, commande de déconnexion).
- **Action 14.2** : Implémentation de `ViewModels/MyOrdersViewModel.cs` et de la vue d'historique `Pages/MyOrdersPage.xaml`.
- **Action 14.3** : Implémentation de `ViewModels/OrderDetailsViewModel.cs` et de la page détaillée `Pages/OrderDetailsPage.xaml`.
- **Action 14.4** : Test complet : consultation des commandes passées, inspection d'un reçu détaillé et déconnexion avec nettoyage du coffre `SecureStorage`.
- **Action 14.5** : Rédaction du livret pédagogique d'étape `Livret/etapes/14_profil_historique.tex` (Session sans état, extraction de Claims côté client, localisation des devises/dates).
- **Action 14.6** : Relecture, questions/réponses et validation utilisateur.

#### Vérification

```
1. Se connecter → Aller sur l'onglet Profil → Vérifier nom, email, avatar à initiales
2. Passer une commande (Jalon 13) → Aller dans Historique → La commande apparaît
3. Toucher la commande → Le détail ligne par ligne s'affiche correctement
4. Se déconnecter → Retour à l'Onboarding → Impossible d'accéder aux pages protégées
```

---

### Jalon 15 — Composants Avancés : Popup Modale & Badge Natif

**Périmètre** : Frontend  
**Concept clé** : *Étendre .NET MAUI avec CommunityToolkit.Maui et les renderers de plateforme native*

#### Ce qui est construit

| Fichier | Rôle |
| :--- | :--- |
| `Controls/ChangePasswordPopup.xaml` | Popup modale (`<toolkit:Popup>`) avec formulaire de changement de mot de passe : ancien mot de passe, nouveau mot de passe, confirmation |
| `ViewModels/ChangePasswordViewModel.cs` | Validation des champs (nouveau = confirmation, longueur minimale), appel à `IAuthApi.ChangePasswordAsync()`, fermeture du popup en cas de succès |
| `Platforms/Android/Handlers/TabBarBadgeHandler.cs` | Renderer natif Android utilisant `BadgeDrawable` de Material Design pour afficher un compteur dynamique sur l'icône de l'onglet Panier |

#### Concepts Professionnels Enseignés

1. **Popup Modale (CommunityToolkit.Maui)** :
   - `<toolkit:Popup>` est une fenêtre surgissante qui se superpose à la page actuelle sans changer la navigation.
   - Elle possède son propre ViewModel injecté par DI.
   - La fermeture du popup peut retourner un résultat typé à la page appelante via `CloseAsync(result)`.
   - Cas d'usage idéal : formulaires courts, confirmations, saisies rapides.

2. **Badge Natif Android** :
   - .NET MAUI ne fournit pas nativement de badge sur les onglets.
   - On crée un `Handler` personnalisé qui accède à la couche Android native (`Google.Android.Material.Badge.BadgeDrawable`).
   - Le badge se met à jour automatiquement quand le `CartViewModel` notifie un changement du nombre d'articles.
   - Cela démontre la capacité de MAUI à accéder au code natif de chaque plateforme quand l'abstraction cross-platform ne suffit pas.

3. **Validation Côté Client Avant Envoi** :
   - Le bouton « Valider » du popup de changement de mot de passe n'est actif que lorsque toutes les conditions sont remplies (ancien renseigné, nouveau ≥ 6 caractères, confirmation identique).
   - C'est une validation d'ergonomie côté client — la validation de sécurité (vérification de l'ancien mot de passe) reste côté serveur.

#### Découpage en Micro-Étapes Réalisables

- **Action 15.1** : Conception du contrôle de popup modale `Controls/ChangePasswordPopup.xaml` (`<toolkit:Popup>`).
- **Action 15.2** : Implémentation de `ViewModels/ChangePasswordViewModel.cs` avec validation préalable côté client.
- **Action 15.3** : Création du renderer natif Android `Platforms/Android/Handlers/TabBarBadgeHandler.cs` exploitant `BadgeDrawable`.
- **Action 15.4** : Câblage de l'événement réactif entre le nombre d'articles du panier et l'actualisation du badge natif.
- **Action 15.5** : Test final : ouverture du popup de mot de passe, validation, actualisation dynamique du badge d'onglet.
- **Action 15.6** : Rédaction du livret pédagogique d'étape `Livret/etapes/15_composants_avances.tex` (Extension native de MAUI, popups modales réactives).
- **Action 15.7** : Exécution du script Python `Livret/compiler_livret.py` pour consolider tous les chapitres dans `LIVRET.pdf`.
- **Action 15.8** : Revue finale et clôture du projet.

#### Vérification

```
1. Profil → Bouton « Changer le mot de passe » → Le popup s'ouvre en overlay
2. Saisir ancien mot de passe + nouveau + confirmation → Le bouton Valider s'active
3. Valider → Le serveur confirme → Le popup se ferme avec un toast de succès
4. Se déconnecter, se reconnecter avec le nouveau mot de passe → Succès

5. Ajouter des articles au panier → Le badge sur l'onglet Panier affiche le nombre
6. Vider le panier → Le badge disparaît
```

---

## 6. Synthèse des Compétences Professionnelles Acquises

À l'issue de ces 15 jalons, les compétences suivantes sont maîtrisées dans un contexte professionnel réel :

| Domaine | Compétences Concrètes |
| :--- | :--- |
| **Architecture** | Solution multi-projets, séparation Front/Back/Shared, injection de dépendances, cycles de vie `Scoped`/`Transient`/`Singleton` |
| **Backend API** | ASP.NET Core Minimal API, pipeline middleware (ordre critique), groupes d'endpoints, gestion d'erreurs globale, CORS |
| **Persistance Serveur** | Entity Framework Core, Fluent API, Seed Data, transactions relationnelles, mapping Entity → DTO |
| **Sécurité** | Hachage HMACSHA512 avec sel, JWT (Claims, signature, validation), endpoints protégés, extraction d'identité depuis le token |
| **Persistance Client** | `sqlite-net-pcl`, base SQLite embarquée locale, `IAsyncDisposable`, distinction des deux niveaux de stockage |
| **Client Mobile** | .NET MAUI, MVVM avec `CommunityToolkit.Mvvm`, Shell Navigation, `CollectionView`, `DataTemplate`, ressources 100% SVG |
| **Réseau** | `IHttpClientFactory`, Refit (client HTTP déclaratif), `DelegatingHandler` pour injection automatique du JWT, `SecureStorage` |
| **Configuration** | `appsettings.json`, `IOptions<T>`, `Directory.Build.props`, environnements (`Development`/`Production`) |
| **Composants Avancés** | Popups modales (`CommunityToolkit.Maui`), renderers de plateforme native (badge Android), composants XAML réutilisables |
| **Observabilité** | Middleware de journalisation, logs ANSI colorés, traçage SQL en temps réel, décodage JWT pédagogique |

---

## 7. Méthodologie Didactique : Les Micro-Fiches par Action (Approche Ultra-Granulaire)

Pour garantir une assimilation pas-à-pas et un contrôle continu de l'apprentissage :

1. **Une micro-fiche `.tex` par micro-action** :
   - À chaque micro-action technique réalisée, un fichier LaTeX modulaire dédié est créé dans `Livret/etapes/` sous le format `XX_YY_nom_action.tex` (ex: `01_01_creation_solution.tex`, `01_02_creation_shared.tex`, etc.).
   - Ce document ciblé (1 à 2 pages A4) détaille le concept fondamental unique abordé, avec schéma vectoriel TikZ percutant, texte continu fluide et aéré (tableaux strictement réservés aux synthèses comparatives utiles), objectifs observables, erreurs fréquentes et exercice pratique.
2. **Cycle de lecture et validation humaine immédiate** :
   - L'utilisateur lit et analyse la micro-fiche (lecture de 2 minutes).
   - En cas de besoin d'éclaircissement ou d'approfondissement, la micro-fiche est enrichie.
   - Dès validation explicite de l'utilisateur, passage immédiat à la micro-action suivante.
3. **Compilation automatisée via script Python (`Livret/compiler_livret.py`)** :
   - Un script Python assemble au fur et à mesure l'ensemble des micro-fiches validées pour générer le livret complet `Livret/LIVRET.tex` et son rendu compilé `Livret/LIVRET.pdf`.

> **Rappel** : Les micro-fiches ne sont jamais une récitation passive de code. Elles se concentrent sur les **concepts d'ingénierie fondamentaux**, illustrés par des **schémas de flux TikZ**, une **mise en page aérée et non rigide**, des **vérifications concrètes**, des **erreurs fréquentes signalées** et un **exercice de réinvestissement** pour chaque étape.
