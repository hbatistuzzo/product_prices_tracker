""
Scraper modules for the E-commerce Price Tracker.

This package contains the base scraper class and implementations
for various e-commerce platforms.
"""

from .base_scraper import BaseScraper
from .sample_retailer_scraper import SampleRetailerScraper

__all__ = ['BaseScraper', 'SampleRetailerScraper']
