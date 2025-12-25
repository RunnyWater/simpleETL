# Simple ETL
> Simple ETL tool that makes ETL process easier, no-code like 

## System Architecture

### Front-end Layer

![Front-end layer](docs/FRONT.jpg)

**React + TypeScript**
- Modern UI with Vite

**Components**
- ETL Configuration UI
- Data Source Selector
- Transformation Builder
- Job Monitor

**State Management**
- TanStack Query (Server)
- Zustand (Client)

---
### Back-end Layer

![Back-end layer](docs/BACK.jpg)

**FastAPI + Python**
- Async REST API

**Core Services**
- ETL Engine
- Data Connectors
- Transformation Logic
- Job Logger

**Data Processing**
- Dual-engine support with **Pandas** and **Polars**

### Desktop Layer 
![Desktop layer](docs/DESKTOP.jpg)

**Electron**
- Cross-platform wrapper

**Main Process**
- Window Management
- Python Process Control
- System Integration
- No-Code Control

**Local Storage**
- electron-store

