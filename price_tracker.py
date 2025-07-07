#!/usr/bin/env python3
"""
E-commerce Price Tracker - Portfolio Version

A demonstration of web scraping and data visualization techniques.
This is a simplified version for portfolio purposes.
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv

# Import base scraper (this would be implemented in a real project)
# from scrapers.base_scraper import BaseScraper

# Configuration
DATA_DIR = Path(__file__).parent / 'data'
DATA_DIR.mkdir(exist_ok=True)

# Sample product configuration (simplified for portfolio)
SAMPLE_PRODUCTS = {
    'sample_product_1': {
        'name': 'Sample Product 1',
        'urls': {
            'retailer_a': 'https://example.com/product/1',
            'retailer_b': 'https://example.com/product/1',
        }
    }
}


def save_price_data(
    product_id: str,
    seller: str,
    price: str,
    title: str,
    url: str
) -> None:
    """Save price data to a CSV file.
    
    Args:
        product_id: Unique identifier for the product
        seller: Name of the seller/retailer
        price: Price as a formatted string
        title: Product title
        url: Product URL
    """
    filename = DATA_DIR / f"{product_id}_prices.csv"
    
    # Create file with headers if it doesn't exist
    if not filename.exists():
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'seller', 'price', 'title', 'url'])
    
    # Append new data
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            seller,
            price,
            title,
            url
        ])


def plot_price_history(product_id: str) -> None:
    """Plot price history for a product.
    
    Args:
        product_id: ID of the product to plot
    """
    filename = DATA_DIR / f"{product_id}_prices.csv"
    
    if not filename.exists():
        print(f"No price data found for {product_id}")
        return
    
    try:
        df = pd.read_csv(filename, parse_dates=['timestamp'])
        
        if df.empty:
            print(f"No price data available for {product_id}")
            return
        
        # Clean and process data
        df = df.sort_values('timestamp')
        
        # Create plot
        plt.figure(figsize=(12, 6))
        
        # Group by seller and plot each one
        for seller, group in df.groupby('seller'):
            plt.plot(
                group['timestamp'],
                group['price'],
                marker='o',
                linestyle='-',
                label=seller.replace('_', ' ').title()
            )
        
        # Customize plot
        plt.title(f'Price History - {SAMPLE_PRODUCTS[product_id]["name"]}')
        plt.xlabel('Date')
        plt.ylabel('Price (BRL)')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save and show plot
        plot_path = DATA_DIR / f"{product_id}_price_history.png"
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Plot saved to {plot_path}")
        
    except Exception as e:
        print(f"Error plotting price history: {e}")


def main() -> None:
    """Main entry point for the price tracker."""
    print("E-commerce Price Tracker - Portfolio Version")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. View sample price history")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == '1':
            # Show sample plot for the first product
            product_id = next(iter(SAMPLE_PRODUCTS))
            plot_price_history(product_id)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
