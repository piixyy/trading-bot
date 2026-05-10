# Binance Futures Testnet Trading Bot

## Overview
This is a simple Python-based CLI trading bot built for Binance Futures Testnet.  
It allows placing both MARKET and LIMIT orders using user input from the command line.

The goal of this project was to create a clean, structured, and reusable application with proper logging and error handling.

---

## Setup Instructions

1. Download or clone this project

2. Install required libraries:
pip install -r requirements.txt

3. Create a `.env` file in the main folder and add your Binance Testnet API keys:
API_KEY=your_api_key
API_SECRET=your_secret_key

---

## How to Run

### Market Order Example
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order Example
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

---

## Features
- Supports both MARKET and LIMIT orders
- Allows BUY and SELL operations
- Takes input through CLI arguments
- Validates user input before placing orders
- Logs API requests, responses, and errors
- Handles exceptions for invalid input and API failures

---

## Logs
All logs are stored in:
logs/bot.log

These logs include:
- Order request details
- API responses
- Error messages (if any)

---

## Assumptions
- The bot is designed to work with Binance Futures Testnet (USDT-M)
- Only basic order types (Market and Limit) are implemented

## Bonus Feature
An enhanced CLI experience has been added.  
Users can now input order details interactively instead of passing command-line arguments.
