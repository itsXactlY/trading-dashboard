use actix_web::{get, post, web, App, HttpServer, Responder};
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
struct Trade {
    date: String,
    chat_name: String,
    creator: String,
    exchanges: String,
    symbol: String,
    status: String,
    leverage: String,
    direction: String,
    last_target: String,
    duration: String,
    signal_gained_profit: String,
    entry_targets_filled: String,
    number_of_filled_entry_targets: String,
    filled_average_entry_price: String,
    number_of_entry_targets: String,
    entry_zone_range: String,
    average_entry_price: String,
    tp1_price: String,
    tp2_price: String,
    tp3_price: String,
    tp4_price: String,
    tp5_price: String,
    tp6_price: String,
    tp7_price: String,
    tp8_price: String,
    tp9_price: String,
    tp10_price: String,
    stop_loss_price: String,
}

#[get("/trades")]
async fn get_trades() -> impl Responder {
    // Placeholder for fetching trades from the database
    web::Json(vec![])
}

#[post("/trades")]
async fn add_trade(trade: web::Json<Trade>) -> impl Responder {
    // Placeholder for adding a trade to the database
    web::Json(trade.0)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(get_trades)
            .service(add_trade)
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}