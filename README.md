# Les Recettes de Chihiro – Projet de site web

## Présentation

« Les Recettes de Chihiro » est une application web permettant de découvrir et de gérer des recettes inspirées du film *Le Voyage de Chihiro* et de l’univers Ghibli.
Le projet combine un frontend Next.js / TypeScript et un backend FastAPI avec une base de données PostgreSQL via Supabase.

## Fonctionnalités principales

### MVP

* Authentification : inscription, connexion, gestion du profil
* Catalogue de recettes : affichage, recherche, filtre par catégorie
* Page recette : ingrédients, instructions, référence au film/série associé
* Ajout de recettes : accessible uniquement aux utilisateurs connectés
* Back-office : gestion des recettes, catégories et utilisateurs (pour admins)

### Fonctionnalités évolutives

* Commentaires et notes sur les recettes
* Favoris utilisateur
* Liste de courses générée à partir de recettes
* Système de recommandations personnalisées
* Dashboard utilisateur et statistiques
* Notifications et classement des recettes
* Support multilingue (FR/EN)

## Stack technique

### Frontend

* Next.js 14+ avec TypeScript
* React Server Components
* TailwindCSS pour le design
* React Query pour la gestion des données

### Backend

* Python 3 + FastAPI
* Pydantic pour la validation
* SQLAlchemy / SQLModel pour les modèles
* Supabase (PostgreSQL) pour la base et l’authentification
* Uvicorn pour le serveur ASGI

### Base de données

* Supabase PostgreSQL
* Tables : users, recipes, categories, comments, favorites, recipe_category
* Auth Supabase + JWT pour sécuriser les endpoints

## Structure du projet

```
backend/
├─ app/
│  ├─ main.py
│  ├─ routers/
│  ├─ schemas/
│  ├─ core/
│  └─ services/
└─ requirements.txt

frontend/
├─ app/ (pages et routes)
├─ components/
├─ lib/ (API utils)
└─ package.json
```

## API (exemples de endpoints)

* `/auth/signup` – inscription utilisateur
* `/auth/login` – connexion utilisateur
* `/recipes` – liste des recettes
* `/recipes/{id}` – détail d’une recette
* `/recipes` POST – ajouter une recette
* `/recipes/{id}` PUT/DELETE – modifier ou supprimer une recette (auth)
* `/categories` – liste ou ajout de catégories (admin)
* `/favorites` – gérer les favoris
* `/comments` – gérer les commentaires et notes

## Améliorations possibles

* Filtrage avancé, multi-langue
* Système de recommandations
* Dashboard utilisateur avec statistiques
* Notifications en temps réel
* Gestion d’images pour chaque recette
