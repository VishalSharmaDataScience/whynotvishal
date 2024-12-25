AUTHOR = 'Vishal Sharma'
SITENAME = 'Why Not Vishal'
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
    ('Home', '/index.html'),
    ('Music', '/category/music.html'),
    ('Travel', '/category/travel.html'),
    ('Data Science', '/category/data-science.html'),
    ('Personal', '/category/personal.html'),
    ('About', '/pages/about.html'),
]


#THEME = "themes/flex"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

# Static pages
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Static paths for custom pages
STATIC_PATHS = ['images', 'extra', 'static']
EXTRA_PATH_METADATA = {
    'static/custom.css': {'path': 'custom.css'},
}

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Basic site info
SITENAME = "Why Not Vishal"
SITESUBTITLE = "Music, Data Science, Travel, and More"
SITELOGO = "static/images/22625946.jpeg"  # Path to your logo image
FAVICON = "/images/favicon.ico"

# Pagination
DEFAULT_PAGINATION = 10
# Theme configuration
COPYRIGHT_YEAR = 2024
BROWSER_COLOR = "#121212"  # Dark background color

