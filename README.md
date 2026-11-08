# SupplyChain AI — Contra portfolio project

A responsive supply-chain intelligence SaaS dashboard built with React, Vite, custom CSS, Lucide icons and Recharts.

## 1. Requirements
- Node.js LTS installed
- VS Code (or another editor)
- Internet connection for installing dependencies and Google Fonts

## 2. Run locally (Windows PowerShell)
1. Extract this folder.
2. Open the `supplychain-ai` folder in VS Code.
3. Open Terminal → New Terminal.
4. Run `npm install`
5. Run `npm run dev`
6. Open the local URL printed by Vite (usually http://localhost:5173).

If PowerShell blocks npm scripts, use Command Prompt in VS Code, or run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in the current PowerShell terminal.

## 3. Project structure
- `index.html` — app entry HTML
- `src/main.jsx` — React entry point
- `src/App.jsx` — navigation, dashboard, inventory, shipments and AI insight views
- `src/styles.css` — responsive visual system and component styling
- `backend/` — optional FastAPI starter API

## 4. What works in this portfolio demo
- Responsive sidebar and mobile navigation
- Overview KPI cards, inventory movement chart and warehouse capacity
- Inventory search, stock status and add-item demo interaction
- Shipment progress list
- AI recommendation examples
- Navigation between dashboard sections

## 5. Important demo honesty
The current data is sample data. The AI insight cards are illustrative rule-based examples, not live AI predictions. The add-item action updates local React state only. Do not describe these as production integrations until the backend, database and real data sources are connected.

## 6. Next development milestones
1. Connect the React frontend to the FastAPI endpoints.
2. Persist products, warehouses and shipments in a database.
3. Add authentication and role-based access.
4. Connect supplier and carrier APIs where available.
5. Implement forecasting with historical demand data and evaluate accuracy.
6. Add tests, loading/error states and deployment.

## 7. Contra case-study suggestion
**Title:** SupplyChain AI — Supply Chain Intelligence Dashboard  
**Role:** Product design, frontend engineering and AI application development  
**Description:** Designed and developed a responsive SaaS dashboard concept for inventory visibility, shipment monitoring and operational insights. The demo includes searchable inventory, warehouse capacity, shipment tracking and clearly labelled sample AI recommendations.
