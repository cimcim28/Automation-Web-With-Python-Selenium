# Web Automation Testing dengan Python & Selenium

Project ini adalah untuk belajar automation testing menggunakan Python dan Selenium. Saya membuat framework sederhana untuk test website secara otomatis.

## Apa isi project ini?

```
Automation-Web-With-Python-Selenium/
├── configuration/     # File setting dan konfigurasi
├── locators/         # Tempat menyimpan element web
├── pages/            # Class untuk setiap halaman website
├── tests/            # File-file test case
├── utils/            # Function helper
├── conftest.py       # Setting pytest
├── pytest.ini        # Konfigurasi pytest
└── requirements.txt   # List library yang dibutuhkan
```

## Cara menjalankan project

### 1. Install Python
Pastikan Python sudah terinstall di komputer (minimal versi 3.8)

### 2. Clone project ini
```bash
git clone <link-repository>
cd Automation-Web-With-Python-Selenium
```

### 3. Buat virtual environment
```bash
python -m venv venv
```

### 4. Aktifkan virtual environment

**Mac/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 5. Install semua library
```bash
pip install -r requirements.txt
```

## Cara menjalankan test

### Jalankan semua test
```bash
pytest
```

### Jalankan test tertentu
```bash
pytest tests/test_login.py
```

### Jalankan test dengan report HTML
```bash
pytest --html=report.html
```

## Contoh membuat test sederhana

### 1. Buat page object (pages/login_page.py)
```python
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def open_page(self):
        self.driver.get("https://example.com/login")
    
    def input_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)
    
    def input_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
    
    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
```

### 2. Buat test case (tests/test_login.py)
```python
import pytest
from pages.login_page import LoginPage

class TestLogin:
    def setup_method(self):
        # Setup yang dipanggil sebelum setiap test
        self.login_page = LoginPage(self.driver)
    
    def test_login_berhasil(self):
        # Test login dengan data yang benar
        self.login_page.open_page()
        self.login_page.input_username("user123")
        self.login_page.input_password("password123")
        self.login_page.click_login()
        
        # Cek apakah login berhasil
        assert "dashboard" in self.driver.current_url
```

## File-file penting

### requirements.txt
Berisi semua library yang dibutuhkan:
```
selenium==4.15.0
pytest==7.4.0
pytest-html==3.2.0
webdriver-manager==4.0.1
```

### conftest.py
File konfigurasi pytest:
```python
import pytest
from selenium import webdriver

@pytest.fixture
def browser_setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
```

## Tips untuk pemula

1. **Mulai dari yang simple** - buat test login dulu sebelum yang kompleks
2. **Gunakan Page Object Model** - pisahkan element dan action per halaman
3. **Buat assertion yang jelas** - pastikan test bisa detect pass/fail dengan benar
4. **Screenshot saat error** - membantu debugging
5. **Pakai wait** - jangan langsung cari element, tunggu sampai muncul

## Troubleshooting umum

**Error: WebDriver not found**
- Install ChromeDriver atau gunakan webdriver-manager

**Error: Element not found**
- Cek apakah selector benar
- Tambahkan wait/sleep

**Test jalan lambat**
- Coba jalankan headless mode
- Kurangi jumlah test yang jalan bersamaan

## Browser yang didukung
- Chrome (recommended untuk pemula)
- Firefox
- Edge

## Yang akan dipelajari dari project ini
- Automation testing basics
- Selenium WebDriver
- Page Object Model pattern
- Pytest framework
- HTML reporting
- Git version control

---

*Project ini masih dalam tahap pembelajaran, jadi masih banyak yang bisa diperbaiki! 😊*