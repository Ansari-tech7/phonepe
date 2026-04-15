# ================================
# 📦 IMPORT LIBRARIES
# ================================
from sqlalchemy import create_engine, text

# ================================
# 🔌 DATABASE CONNECTION

import psycopg2
from sqlalchemy import create_engine

# Database credentials
db_user = 'postgres'
db_password = 'ansaris'
db_host = '127.0.0.1'
db_port = '5432'   # or 5432
db_name = 'phonepe'

# Create connection
engine = create_engine(
    f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
)

print("✅ Connected Successfully")

# ================================
# 🧱 CREATE TABLES
# ================================
schema_statements = [

# ------------------ Aggregated User (Device Level) ------------------
"""
CREATE TABLE IF NOT EXISTS aggregated_user (
  state       TEXT NOT NULL,
  year        INT  NOT NULL,
  quarter     INT  NOT NULL,
  brand       TEXT NOT NULL,
  count       BIGINT NOT NULL,
  percentage  NUMERIC(10,6) NOT NULL,
  CONSTRAINT uq_aggregated_user UNIQUE (state, year, quarter, brand)
);
""",

# ------------------ Aggregated User Summary (TOTAL USERS) ------------------
"""
CREATE TABLE IF NOT EXISTS aggregated_user_summary (
  state            TEXT NOT NULL,
  year             INT  NOT NULL,
  quarter          INT  NOT NULL,
  registered_users BIGINT,
  app_opens        BIGINT,
  CONSTRAINT uq_user_summary UNIQUE (state, year, quarter)
);
""",

# ------------------ Aggregated Transaction ------------------
"""
CREATE TABLE IF NOT EXISTS aggregated_transaction (
  state              TEXT NOT NULL,
  year               INT  NOT NULL,
  quarter            INT  NOT NULL,
  transaction_type   TEXT NOT NULL,
  transaction_count  BIGINT NOT NULL,
  transaction_amount NUMERIC(20,2),
  CONSTRAINT uq_aggregated_transaction UNIQUE (state, year, quarter, transaction_type)
);
""",

# ------------------ Aggregated Insurance ------------------
"""
CREATE TABLE IF NOT EXISTS aggregated_insurance (
  state            TEXT NOT NULL,
  year             INT  NOT NULL,
  quarter          INT  NOT NULL,
  insurance_type   TEXT NOT NULL,
  insurance_count  BIGINT NOT NULL,
  insurance_amount NUMERIC(20,2),
  CONSTRAINT uq_aggregated_insurance UNIQUE (state, year, quarter, insurance_type)
);
""",

# ------------------ Map User ------------------
"""
CREATE TABLE IF NOT EXISTS map_user (
  state            TEXT NOT NULL,
  year             INT  NOT NULL,
  quarter          INT  NOT NULL,
  district         TEXT NOT NULL,
  registered_users BIGINT,
  app_opens        BIGINT,
  CONSTRAINT uq_map_user UNIQUE (state, year, quarter, district)
);
""",

# ------------------ Map Transaction ------------------
"""
CREATE TABLE IF NOT EXISTS map_transaction (
  state              TEXT NOT NULL,
  year               INT  NOT NULL,
  quarter            INT  NOT NULL,
  district           TEXT NOT NULL,
  transaction_count  BIGINT,
  transaction_amount NUMERIC(20,2),
  CONSTRAINT uq_map_transaction UNIQUE (state, year, quarter, district)
);
""",

# ------------------ Map Insurance ------------------
"""
CREATE TABLE IF NOT EXISTS map_insurance (
  state            TEXT NOT NULL,
  year             INT  NOT NULL,
  quarter          INT  NOT NULL,
  district         TEXT NOT NULL,
  insurance_count  BIGINT,
  insurance_amount NUMERIC(20,2),
  CONSTRAINT uq_map_insurance UNIQUE (state, year, quarter, district)
);
""",

# ------------------ Top User ------------------
"""
CREATE TABLE IF NOT EXISTS top_user (
  state            TEXT NOT NULL,
  year             INT  NOT NULL,
  quarter          INT  NOT NULL,
  pincode          TEXT NOT NULL,
  registered_users BIGINT,
  CONSTRAINT uq_top_user UNIQUE (state, year, quarter, pincode)
);
""",

# ------------------ Top Transaction ------------------
"""
CREATE TABLE IF NOT EXISTS top_transaction (
  state              TEXT NOT NULL,
  year               INT  NOT NULL,
  quarter            INT  NOT NULL,
  pincode            TEXT NOT NULL,
  transaction_count  BIGINT,
  transaction_amount NUMERIC(20,2),
  CONSTRAINT uq_top_transaction UNIQUE (state, year, quarter, pincode)
);
""",

# ------------------ Top Insurance ------------------
"""
CREATE TABLE IF NOT EXISTS top_insurance (
  state            TEXT NOT NULL,
  year             INT  NOT NULL,
  quarter          INT  NOT NULL,
  pincode          TEXT NOT NULL,
  insurance_count  BIGINT,
  insurance_amount NUMERIC(20,2),
  CONSTRAINT uq_top_insurance UNIQUE (state, year, quarter, pincode)
);
"""
]

# ================================
# ▶️ EXECUTE TABLE CREATION
# ================================
with engine.connect() as conn:
    for stmt in schema_statements:
        conn.execute(text(stmt))
    conn.commit()

print("✅ All tables created successfully!")