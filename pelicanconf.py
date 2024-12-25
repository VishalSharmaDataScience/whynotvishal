AUTHOR = 'Vishal Sharma'
SITENAME = 'Why Not, Vishal'
SITEURL = ""


PATH = "content"

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Udna kyu na chahun", "https://open.spotify.com/track/2CfWGWWVeLrmGEPCSGW2m5?si=811dd8006f0f4541"),
    ("Dhun-Echoes of Tuco", "https://open.spotify.com/track/0dwQF1AOpDMVltfT7yhd6Y?si=4e176666e0b84f82"),
    ("Mann Baawre", "https://open.spotify.com/track/2LsVvf5pwMq3DkyEzMOVXX?si=7dd0886a06d3417b")
)

# Social widget
SOCIAL = (
     ('GitHub', 'https://github.com/VishalSharmaDataScience'),
    ('LinkedIn', 'https://www.linkedin.com/in/vishalsharma2204/'),
    ('Instagram', 'https://www.instagram.com/iamvishalssharma'),
    ('YouTube', 'https://www.youtube.com/@VishalSharmaOfficialMusic'),
    ('Spotify','https://open.spotify.com/artist/6shHNESKziBepIXHJHSHPD')

)

# Menu items
MAIN_MENU = True
MENUITEMS = [
    ('Home', f'{SITEURL}/index.html'),
    ('Music', f'{SITEURL}/category/music.html'),
    ('Travel', f'{SITEURL}/category/travel.html'),
    ('Data Science', f'{SITEURL}/category/data-science.html'),
    ('Personal', f'{SITEURL}/category/personal.html'),
    ('About', f'{SITEURL}/pages/about.html'),
    ('Contact', f'{SITEURL}/pages/contact.html'),
]


THEME = "themes/notmyidea"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

# Static pages
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Static paths for custom pages
STATIC_PATHS = ['../images', '../extra', '../static']
EXTRA_PATH_METADATA = {
    '../static/css/main.css': {'path': 'theme/css/main.css'},
    '../static/images/serene_background.webp': {'path': 'theme/images/serene_background.webp'},
    '../static/images/22625946.jpeg': {'path': 'theme/images/22625946.jpeg'},
    '../static/images/logo_album_converted.png': {'path': 'theme/images/logo_album_converted.png'},
    
}

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Basic site info
SITENAME = "Why Not, Vishal"
SITESUBTITLE = "Music, AI/Data Science, Travel, and More"
SITELOGO = "../static/images/logo_album_converted.png"  # Path to your logo image
FAVICON = "/images/favicon.ico"

# Pagination
DEFAULT_PAGINATION = 10
# Theme configuration
COPYRIGHT_YEAR = 2024
BROWSER_COLOR = "#121212"  # Dark background color

DEBUG = True