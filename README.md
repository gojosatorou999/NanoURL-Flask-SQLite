# NanoURL 🚀

NanoURL is a premium, lightweight URL shortener built with **Flask** and **SQLite**. It features a modern, glassmorphic UI and robust redirection logic.
 
## ✨ Features
- **Instant Shortening**: Turn long, messy URLs into clean, short links.
- **SQLite Backend**: Efficient data persistence with a local database.
- **Glassmorphism UI**: Beautiful, responsive design with smooth animations.   
- **SEO Optimized**: Meta tags and semantic HTML for better visibility.
 
## 🛠️ Mapping Logic
The core redirection logic follows a simple but effective process:
1. **Input Validation**: Ensures the URL is properly formatted. 
2. **Slug Generation**: A unique 6-character alphanumeric string (slug) is generated using `string.ascii_letters` and `string.digits`.
3. **Database Storage**: The mapping of `{ slug: original_url }` is stored in the `urls` table in `database.db`.
4. **Redirection**: When a user accesses `yourdomain.com/<slug>`, the application:
   - Queries the SQLite database for the provided slug.
   - Retrieves the `original_url`.
   - Performs a 302 redirect to the destination.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Flask

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/NanoURL.git
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000`.

## 📂 Project Structure
- `app.py`: Main Flask application and database initialization.
- `static/css/style.css`: Premium glassmorphism styles.
- `templates/index.html`: Main UI template.
- `database.db`: SQLite database file (created on first run).

---
Built with ❤️ by Antigravity.
