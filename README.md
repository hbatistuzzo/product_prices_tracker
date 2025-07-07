# E-commerce Price Tracker - Portfolio Version

This is a demonstration version of an e-commerce price tracking system, designed to showcase web scraping and data visualization skills in a portfolio context.

## 🚀 Project Overview

This project demonstrates:

- **Modular Web Scraping**: Clean architecture for scraping multiple e-commerce sites
- **Robust Error Handling**: Graceful handling of network issues and website changes
- **Data Visualization**: Plotting price trends over time
- **Best Practices**: Code organization, type hints, and documentation

## 🛠 Technical Implementation

### Architecture

The project follows a clean architecture with separate components for:

1. **Scrapers**: Each retailer has its own scraper class that extends `BaseScraper`
2. **Data Storage**: Price history is stored in CSV files
3. **Visualization**: Matplotlib is used for generating price trend charts

### Key Components

- `price_tracker.py`: Main application script
- `scrapers/`: Package containing all scraper implementations
  - `base_scraper.py`: Abstract base class for all scrapers
  - `sample_retailer_scraper.py`: Example implementation

## 📦 Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the demo:
   ```bash
   python price_tracker.py
   ```

## 🧠 Learning Points

This project demonstrates:

- Web scraping with error handling and retries
- Object-oriented design with abstract base classes
- Data persistence with CSV files
- Data visualization with Matplotlib
- Python type hints and documentation

## ⚠️ Important Notes

- This is a **demonstration project** only
- The code includes placeholders where actual scraping logic would go
- Always respect website terms of service and robots.txt
- Includes rate limiting to avoid overloading servers

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*This is a portfolio project. The code is provided for educational purposes only.*
