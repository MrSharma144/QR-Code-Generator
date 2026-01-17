# QR Code Generator for Restaurant Menus

A Django web application that generates QR codes linked to restaurant menus. Users can input a restaurant name and menu URL, and the application creates a scannable QR code image that can be easily shared and accessed.

## Features

- **Simple QR Code Generation**: Generate QR codes with just a restaurant name and menu URL
- **Media Storage**: QR codes are automatically saved to the media folder for easy management
- **User-Friendly Interface**: Clean and intuitive web interface with form validation
- **URL Validation**: Built-in URL validation to ensure correct menu links
- **Flexible Database**: Support for both SQLite (development) and PostgreSQL (production)

## Requirements

- Python 3.8+
- Django 6.0.1
- qrcode library
- Pillow (PIL)
- python-dotenv
- asgiref
- sqlparse
- dj-database-url

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "QR Code"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   # On Windows
   .\env\Scripts\Activate.ps1
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Copy `.env.example` to `.env`
   - Update the following variables:
     ```
     SECRET_KEY=your-secret-key-here
     DEBUG=True
     USE_SQLITE=True
     ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

1. Fill in the restaurant name field
2. Enter the URL of the restaurant's menu
3. Click the submit button
4. The application will generate a QR code and display it
5. Save or share the QR code as needed

## Project Structure

```
QR Code/
├── django_qr/
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   ├── views.py             # Application views
│   ├── forms.py             # Form definitions
│   ├── asgi.py              # ASGI configuration
│   └── wsgi.py              # WSGI configuration
├── templates/
│   ├── generate_qr_code.html    # QR code form template
│   └── qr_code_result.html      # QR code result template
├── media/                   # Generated QR code images
├── env/                     # Virtual environment
├── manage.py                # Django management script
└── db.sqlite3               # SQLite database (development)
```

## Configuration

### Environment Variables

- `SECRET_KEY`: Django secret key (required for production)
- `DEBUG`: Set to `True` for development, `False` for production
- `USE_SQLITE`: Use SQLite for database (`True`/`False`)
- `DATABASE_URL`: PostgreSQL connection URL (if not using SQLite)

### Database

The project supports both SQLite and PostgreSQL:
- **Development**: SQLite (default) - `USE_SQLITE=True`
- **Production**: PostgreSQL - `USE_SQLITE=False` and set `DATABASE_URL`

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the repository.
