# TITAN AI Database Migration


Database menggunakan PostgreSQL.


Tables:


## trades

Menyimpan:

- symbol
- entry
- exit
- pnl
- status


## ai_history

Menyimpan:

- AI decision
- confidence
- analysis


## wallet_history

Menyimpan:

- wallet address
- chain
- balance


Migration akan dijalankan ketika backend pertama kali start.
