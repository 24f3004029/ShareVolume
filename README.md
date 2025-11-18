# ShareVolume

This is **ShareVolume**, a small site built with Flask and frozen to static HTML using [Frozen-Flask].  
It’s deployed on **GitHub Pages**.

## How it works

1. We write the app in Flask (`app.py`) with Jinja2 templates in `templates/`.  
2. We use **Frozen-Flask** to crawl the app and generate static HTML in a `build/` folder.  
3. GitHub Actions (`.github/workflows/deploy.yml`) runs on each push to `main`, builds the static site, and deploys to Pages.

## Local Development

```bash
# Install dependencies
python3 -m pip install -r requirements.txt

# Run dev server
python3 app.py
