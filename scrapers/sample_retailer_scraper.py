""
Sample retailer scraper implementation.

This module provides a sample implementation of the BaseScraper class
to demonstrate how to create a scraper for a specific e-commerce site.
"""
from typing import Optional, Tuple
import random
from bs4 import BeautifulSoup

from .base_scraper import BaseScraper


class SampleRetailerScraper(BaseScraper):
    """Scraper for a sample e-commerce retailer.
    
    This is a demonstration of how to implement a scraper for a specific
    e-commerce site by extending the BaseScraper class.
    """
    
    def __init__(self):
        """Initialize the sample retailer scraper."""
        super().__init__(base_url="https://example.com")
    
    def get_price(self, url: str) -> Tuple[Optional[str], Optional[str]]:
        """Get the current price and title for a product.
        
        Args:
            url: The product URL
            
        Returns:
            A tuple of (price, title) or (None, None) if not found
        """
        try:
            # Add a random delay to be polite
            self._get_random_delay()
            
            # Make the request
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            # Parse the HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # In a real implementation, you would extract the price and title
            # using appropriate selectors for the target website.
            # This is just a placeholder that returns sample data.
            
            # Example selectors (would be customized for the actual site):
            # price_element = soup.select_one('.price')
            # title_element = soup.select_one('.product-title')
            
            # For demonstration, return sample data
            return "R$ 1.234,56", "Sample Product Title"
            
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None, None
    
    def __str__(self) -> str:
        """Return a string representation of the scraper."""
        return "SampleRetailerScraper for example.com"
