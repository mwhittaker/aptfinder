from typing import List

import sqlite3

from .listing import Listing

class Database:
    def __init__(self, database_file: str) -> None:
        self.database_file = database_file
        self.connection = sqlite3.connect(database_file)
        self.create_relation()

    def create_relation(self) -> None:
        cursor = self.connection.cursor()
        cursor.execute("""
          CREATE TABLE IF NOT EXISTS Listings (
            website text,
            id text,
            url text,
            name text,
            price int,
            distance_to_soda int,
            PRIMARY KEY (website, id)
          );
        """)

    def listing_exists(self, listing: Listing) -> bool:
        cursor = self.connection.cursor()
        bindings = {'website': listing.website, 'id': listing.id}
        cursor.execute("""
          SELECT * FROM
          LISTINGS
          WHERE website = :website AND id = :id;
        """, bindings)
        return cursor.fetchone() is not None

    def insert_listings(self, listings: List[Listing]) -> None:
        cursor = self.connection.cursor()
        bindings = [listing._asdict() for listing in listings]
        cursor.executemany("""
          INSERT OR IGNORE INTO Listings
          VALUES (:website, :id, :url, :name, :price, :distance_to_soda);
        """, bindings)
        self.connection.commit()
