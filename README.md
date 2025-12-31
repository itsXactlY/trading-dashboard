# Trading Dashboard 

A full work in progress futuristic, AI-powered trading analytics dashboard that transforms raw CSV data into an immersive, interactive experience.

## Tech Stack

- **Frontend**: Svelte 5, Three.js, TensorFlow.js
- **Backend**: Rust, Actix Web, Apache Arrow
- **AI/ML**: PyTorch, LangChain, Whisper
- **Deployment**: Docker, Terraform, Cloudflare Workers, IPFS

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose
- Node.js (for frontend development)
- Rust (for backend development)
- Python (for AI/ML components)

### Running the Application

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/trading-dashboard.git
   cd trading-dashboard
   ```

2. **Build and Run with Docker**:
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**:
   - Frontend: http://localhost:3000
   - Backend: http://localhost:8080

### Development

#### Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Build and run the backend:
   ```bash
   cargo build --release
   cargo run --release
   ```

#### Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies and run the frontend:
   ```bash
   npm install
   npm run dev
   ```

#### AI Components

1. Navigate to the AI directory:
   ```bash
   cd ai
   ```

2. Install dependencies and run the AI components:
   ```bash
   pip install -r requirements.txt
   python insight_generator.py
   ```

## Deployment

### Docker

The application is containerized using Docker. To deploy:

1. Build the Docker images:
   ```bash
   docker-compose build
   ```

2. Start the containers:
   ```bash
   docker-compose up
   ```

### Terraform

For cloud deployment, use the provided Terraform scripts to provision infrastructure.

## Documentation

- [Architecture Plan](plans/trading_dashboard_architecture.md)
- [UI/UX Plan](plans/trading_dashboard_ui_ux.md)
- [AI/ML Integration Plan](plans/trading_dashboard_ai_ml.md)
- [Deployment Plan](plans/trading_dashboard_deployment.md)

## License

This project is licensed under the MIT License.
