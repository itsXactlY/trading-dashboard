# Dockerfile for the trading dashboard backend
FROM rust:1.60 as builder

WORKDIR /app
COPY backend/Cargo.toml .
COPY backend/src ./src

RUN cargo build --release

FROM debian:bullseye-slim

WORKDIR /app
COPY --from=builder /app/target/release/trading-dashboard-backend .

EXPOSE 8080

CMD ["./trading-dashboard-backend"]