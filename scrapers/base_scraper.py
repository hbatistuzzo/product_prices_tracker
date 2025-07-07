""
Base scraper class for e-commerce price tracking.

This module provides an abstract base class that defines the common interface
for all retailer-specific scrapers.
"""
from abc import ABC, abstractmethod
from typing import Optional, Tuple
import random
import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class BaseScraper(ABC):
    """Abstract base class for e-commerce scrapers."""
    
    # Default headers to mimic a browser
    DEFAULT_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    
    def __init__(self, base_url: str):
        """Initialize the scraper with a base URL.
        
        Args:
            base_url: The base URL of the retailer's website
        """
        self.base_url = base_url
        self.session = self._create_session()
    
    def _create_session(self) -> requests.Session:
        """Create a requests session with retry logic.
        
        Returns:
            Configured requests.Session object
        """
        session = requests.Session()
        
        # Configure retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        
        # Mount the retry strategy to both http and https
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Set default headers
        session.headers.update(self.DEFAULT_HEADERS)
        
        return session
    
    def _get_random_delay(self, min_seconds: float = 1.0, max_seconds: float = 3.0) -> None:
        """Add a random delay between requests to avoid rate limiting."""
        time.sleep(random.uniform(min_seconds, max_seconds))
    
    @abstractmethod
    def get_price(self, url: str) -> Tuple[Optional[str], Optional[str]]:
        """Get the current price and title for a product.
        
        Args:
            url: The product URL
            
        Returns:
            A tuple of (price, title) or (None, None) if not found
        """
        pass
    
    def __repr__(self) -> str:
        """Return a string representation of the scraper."""
        return f"{self.__class__.__name__}(base_url='{self.base_url}')"
