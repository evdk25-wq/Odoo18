# Mini CRM Odoo 18

Module Odoo 18 développé comme exercice technique. Il permet de gérer des opportunités commerciales et d’identifier des clients prioritaires.

## Fonctionnalités

- Gestion des opportunités : client, revenu attendu, étape et notes.
- Vues Kanban, liste et formulaire.
- Ajout du statut « Client prioritaire » aux contacts.
- Contrôle métier : un contact doit avoir un numéro de téléphone avant de devenir prioritaire.

## Prérequis

- Docker et Docker Compose

## Lancer le projet

```bash
docker compose up -d
```

Ouvrir ensuite [http://localhost:8069](http://localhost:8069), créer une base de données, puis installer l’application **Mini CRM** depuis le menu Apps.

## Structure

```text
addons/mini_crm/
├── models/       # Modèles Python et logique métier
├── views/        # Vues XML
├── security/     # Droits d'accès
└── __manifest__.py
```

## Version

Testé avec l’image Docker `odoo:18` et PostgreSQL 16.
