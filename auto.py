# ------------------[ AUTO INSTALL ]-------------------#
import os, sys, subprocess, time


def auto_install():
    pkgs = [
        "requests",
        "beautifulsoup4",
        "faker",
        "fake-email",
        "fake-useragent",
    ]
    total = len(pkgs)
    os.system("clear")
    print("\033[1;34m─────────────────────────────────────────────────────\033[1;37m")
    print("INSTALLING MODULES...")
    print("\033[1;34m─────────────────────────────────────────────────────\033[1;32m")
    for i, pkg in enumerate(pkgs, 1):
        pct = int((i / total) * 100)
        bar_len = 20
        filled = int(bar_len * i / total)
        bar = "█" * filled + "░" * (bar_len - filled)
        sys.stdout.write(
            f"\r\033[1;37m[{bar}] \033[1;33m{pct}%\033[1;32m - Installing {pkg}...    "
        )
        sys.stdout.flush()
        subprocess.check_call(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--quiet",
                pkg,
                "--break-system-packages",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    sys.stdout.write(
        "\r\033[1;32m[{0}] \033[1;37m100% - \033[1;32mAll modules installed!\033[0m\n".format(
            "█" * bar_len
        )
    )
    time.sleep(1)
    os.system("clear")


auto_install()

# ------------------[ IMPORT ]-------------------#
import re, json, string, hashlib, random, platform
import requests
import bs4
import faker
import fake_email
from faker import Faker
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as parse
from bs4 import BeautifulSoup as par


# ------------------[ PROXY SERVER ]-------------------#
def load_proxies():
    proxy_url = [
        "https://raw.githubusercontent.com/chandtricker/HTTP/main/http.txt",
        "https://raw.githubusercontent.com/chandtricker/HTTP/main/http_proxies.txt",
    ]
    try:
        response = requests.get(proxy_url)
        if response.status_code == 200:
            return [proxy.strip() for proxy in response.text.splitlines()]
    except requests.exceptions.RequestException:
        pass
    return []


proxies_list = load_proxies()


def get_random_proxy():
    if proxies_list:
        return {"http": random.choice(proxies_list)}
    return None


proxies = get_random_proxy()
# ------------------[ COLORS ]-------------------#
gggg = "\033[8;102m"  # green new coverage prices
rrrr = "\033[8;101m"  # silver new cover words
rrrrrrrr = "\033[32;101m"  # yes you are right
q = "\033[1;30m"  # Gray
w = "\033[1;31m"  # red
e = "\033[1;32m"  # green
r = "\033[1;33m"  # yellow
t = "\033[1;34m"  # blue
y = "\033[1;35m"  # rosy
u = "\033[1;36m"  # Open blue
i = "\033[1;37m"  # white
P = "\x1b[1;97m"  #
M = "\033[1;33m"  #
H = "\033[1;32m"  #
K = "\x1b[1;97m"  #
B = "\x1b[1;96m"  #
U = "\x1b[1;95m"  #
O = "\x1b[1;97m"  #
R = "\x1b[38;5;246m"  #
N = "\x1b[0m"  #
my_color = [P, M, H, K, B, U, O, N, R]
ssn = requests.Session()
boos = random.choice([P, M, H, K, B, U, O, N, R])
orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black = "\033[1;30m"
red = "\x1b[38;5;160m"
green = "\x1b[38;5;46m"
yelloww = "\033[1;33m"
blue = "\033[38;5;6m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m"
abir = random.choice(
    [
        "\x1b[38;5;196m",
        "\x1b[38;5;208m",
        "\033[1;30m",
        "\x1b[38;5;160m",
        "\x1b[38;5;46m",
        "\033[1;33m",
        "\033[38;5;6m",
        "\033[1;35m",
        "\033[1;36m",
        "\033[1;37m",
    ]
)
my_color = [white, blue, green]
warna = random.choice(my_color)
# ------------------[ USER AGENT UA ]-------------------#
from fake_useragent import UserAgent

ua = UserAgent()


def generate_user_agent():
    android_versions = ["9", "10", "11", "12", "13"]
    devices = [
        "Infinix X682C",
        "Redmi Note 9 Pro",
        "V2111 Build/SP1A.210812.003",
        "HLK-AL00 Build/HONORHLK-AL00",
        "ASUS_Z01QD",
        "Redmi 4A Build/MMB29M",
    ]
    browser_engines = [
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",
        "AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/",
    ]
    browsers = ["Mobile Safari/537.36", "UCBrowser/11.4.8.1012 Mobile Safari/537.36"]
    aa = "Mozilla/5.0 (Linux; Android"
    b = random.choice(android_versions)
    c = random.choice(devices)
    d = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    e = random.randint(1, 999)
    f = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    g = random.choice(browser_engines)
    h = random.randint(80, 114)
    i = "0"
    j = random.randint(4200, 5900)
    k = random.randint(40, 150)
    l = random.choice(browsers)
    return f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}"


def W_ueragent():
    chrome_versions = [(80, 3987, 163), (90, 4430, 212), (100, 4896, 127)]
    webkit_versions = [(537, 36), (537, 36), (537, 36)]
    safari_versions = [500, 600]
    windows_versions = [(10, 0), (10, 1), (11, 0)]
    chrome_version = random.choice(chrome_versions)
    webkit_version = random.choice(webkit_versions)
    safari_version = random.choice(safari_versions)
    windows_version = random.choice(windows_versions)
    is_win64 = random.choice([True, False])
    win64_str = "Win64; x64" if is_win64 else "WOW64"
    user_agent = (
        f"Mozilla/5.0 (Windows NT {windows_version[0]}.{windows_version[1]}; {win64_str}) "
        f"AppleWebKit/{webkit_version[0]}.{webkit_version[1]} (KHTML, like Gecko) "
        f"Chrome/{chrome_version[0]}.{chrome_version[1]}.{chrome_version[2]} Safari/{safari_version}"
    )
    return user_agent


def user_agent():
    devices = [
        "[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 9 Pro;FBSV/10]",
        "[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287519012;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/289140577;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/10]",
        "[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1931;FBSV/10]",
        "[FBAN/FB4A;FBAV/435.0.0.42.112;FBBV/523162189;FBDM/{density=3.0,width=1080,height=2165};FBLC/it_IT;FBRV/526139383;FBCR/TIM;FBMF/OnePlus;FBBD/OnePlus;FBDV/LE2113;FBSV/13]",
        "[FBAN/FB4A;FBAV/221.0.0.48.102;FBBV/154683427;FBDM/{density=2.75,width=1080,height=2030};FBLC/en_GB;FBRV/155327069;FBCR/Banglalink;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 5;FBSV/8.1.0]",
    ]
    prefix = (
        "[FBAN/FB4A;FBAV/"
        + str(random.randint(11, 80))
        + ".0.0."
        + str(random.randint(9, 49))
        + "."
        + str(random.randint(11, 77))
        + ";FBBV/"
        + str(random.randint(11111111, 99999999))
        + ";"
    )
    ua = prefix + random.choice(devices)
    return ua


# ------------------[ FAKE NAME PHILIPPINES ]-------------------#
def fake_philippines():
    first = Faker("en_PH").first_name()
    last = Faker("en_PH").last_name()
    return first, last


# ------------------[ FAKE NAME INDONESIA ]-------------------#
def fake_indonesia():
    first = Faker("id_ID").first_name()
    last = Faker("id_ID").last_name()
    return first, last


# ------------------[ FAKE NAME VIETNAMESE ]-------------------#
def fake_vietnamese():
    first = Faker("vi_VN").first_name()
    last = Faker("vi_VN").last_name()
    return first, last


# ------------------[ DATA EXTRACTOR ]-------------------#
def extractor(data):
    try:
        soup = BeautifulSoup(data, "html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error": str(e)}


# ------------------[ LOCKED/ACTIVE CHECKER ]-------------------#
def lock_checker(uid):
    try:
        response = requests.get(f"https://graph.facebook.com/{uid}/picture?type=normal")
        if "Photoshop" in response.text:
            return "Active"
        else:
            return "Locked"
    except Exception as e:
        pass
        return "Error"


# ------------------[ RANDOM STRING ]-------------------#
def generate_random_string(length):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


# Save to sdcard on Android
folder_path = "/sdcard/AUTO_CREATE_LEO"
if not os.path.exists("/sdcard/"):
    folder_path = "AUTO_CREATE_LEO"
try:
    os.makedirs(folder_path, exist_ok=True)
except:
    pass
# ------------------[ INFORMATION ]-------------------#
try:
    ___sim___ = (
        subprocess.check_output("getprop gsm.operator.alpha", shell=True)
        .decode("utf-8")
        .replace("\n", "")
        .replace(",", "|")
    )
except:
    ___sim___ = "Unknown"

try:
    ___brand___ = (
        subprocess.check_output("getprop ro.product.brand", shell=True)
        .decode("utf-8")
        .replace("\n", "")
    )
except:
    ___brand___ = "Termux"

___bit___ = platform.architecture()[0]

try:
    ___ccc___ = requests.get("http://ip-api.com/json/").json()["country"]
except:
    ___ccc___ = "Unknown"


# ------------------[ ??? ]-------------------#
def p(x):
    print(x)


# ------------------[ SLOW PRINT ]-------------------#
def sp(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)


# ------------------[ CONNECTION MONITOR ]-------------------#
# ------------------[ WHATSAPP CHANNEL ]-------------------#
WHATSAPP_CHANNEL = "https://whatsapp.com/channel/0029Vb8CSZQIt5rolffFX31P"


# ------------------[ APPROVAL ALERT ]-------------------#
def approval_alert():
    os.system("clear")
    for _ in range(3):
        print("\033[1;32m")
        print("  ╔═══════════════════════════════════════════╗")
        print("  ║     ✅  A P P R O V E D  ✅              ║")
        print("  ║     ✅  A P P R O V E D  ✅              ║")
        print("  ║     ✅  A P P R O V E D  ✅              ║")
        print("  ╚═══════════════════════════════════════════╝")
        print("\033[1;33m")
        print("  ╔═══════════════════════════════════════════╗")
        print("  ║   🔥 CONGRATULATIONS! APPROVED! 🔥      ║")
        print("  ║   🔥 CONGRATULATIONS! APPROVED! 🔥      ║")
        print("  ║   🔥 CONGRATULATIONS! APPROVED! 🔥      ║")
        print("  ╚═══════════════════════════════════════════╝")
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.3)
    print("\033[1;32m")
    print("  ╔═══════════════════════════════════════════╗")
    print("  ║     ✅  A P P R O V E D  ✅              ║")
    print("  ║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║")
    print("  ║  🔥 CONGRATULATIONS! APPROVED! 🔥       ║")
    print("  ║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║")
    print("  ║  ✅ Access Granted! Enjoy the Tool!     ║")
    print("  ╚═══════════════════════════════════════════╝")
    print("\033[1;37m")


# ------------------[ APPROVAL SYSTEM ]-------------------#
def approval():
    os.system("clear")
    print(logo2)
    sp("\033[1;37m━▷ Welcome to LEO TOOL!")
    time.sleep(2)

    os.system("clear")
    print(logo)

    try:
        os.system("git pull > /dev/null 2>&1")
    except:
        pass
    time.sleep(1)

    uuid = str(os.geteuid()) + "DS" + str(os.geteuid())
    id = "MR-LEO-" + "".join(uuid)

    sp("\033[1;39m━▷ You Get Approved for Using Command Paid Tool \033[1;37m")
    print("\n\033[1;39m━▷ Your Key :\u001b[36m " + id)
    time.sleep(0.1)
    print(
        """\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑"""
    )

    try:
        github_urls = [
            "https://raw.githubusercontent.com/Leoafrica/Leo-sys/refs/heads/main/key.txt",
            "https://raw.githubusercontent.com/chandtricker/HTTP/refs/heads/main/http.txt",
            "https://raw.githubusercontent.com/chandtricker/HTTP/main/http_proxies.txt",
        ]

        approved = False
        while not approved:
            any_ok = False
            for url in github_urls:
                try:
                    response = requests.get(url, timeout=10)
                    any_ok = True
                    if response.status_code == 200 and id in response.text:
                        approved = True
                        break
                except:
                    continue
            if not approved and not any_ok:
                wait_conn()
            elif not approved:
                break

        if approved:
            sp("\n\033[1;39m━▷ Congrats! You are approved successfully. Enjoy the tool!")
            approval_alert()
            time.sleep(2)
            return True
        else:
            sp("\n\033[1;39m━▷ Your Key is not approved. Please contact Admin")
            print(f"\n\033[1;33m━▷ Your Generated Key: \033[1;36m{id}")
            time.sleep(0.1)

            print("\n\033[1;31m━▷ To get approval:")
            print("\033[1;32m1. Open WhatsApp Channel")
            print("\033[1;32m2. Send your key in channel response")
            print("\033[1;32m3. Admin will approve within 24 hours")

            choice = input(
                '\n\033[1;33mPress ENTER to open channel or type "exit" to quit: '
            )
            if choice.lower() == "exit":
                exit("\033[1;32m━▷ Thanks for trying CHAND TOOL!")

            print(f"\033[1;32m━▷ Opening WhatsApp Channel...")
            print(f"\033[1;36m")
            print(f"════════════════════════════════════════════════════")
            print(f"   {WHATSAPP_CHANNEL} ")
            print(f"════════════════════════════════════════════════════")
            print(f"\033[1;37m")

            opened = False
            try:
                import webbrowser

                if webbrowser.open(WHATSAPP_CHANNEL):
                    opened = True
            except:
                pass
            if not opened:
                try:
                    subprocess.run(
                        ["termux-open-url", WHATSAPP_CHANNEL],
                        check=True,
                        timeout=5,
                        capture_output=True,
                    )
                    opened = True
                except:
                    pass
            if not opened:
                try:
                    subprocess.run(
                        ["xdg-open", WHATSAPP_CHANNEL],
                        check=True,
                        timeout=5,
                        capture_output=True,
                    )
                    opened = True
                except:
                    pass
            if not opened:
                try:
                    subprocess.run(
                        [
                            "am",
                            "start",
                            "-a",
                            "android.intent.action.VIEW",
                            "-d",
                            WHATSAPP_CHANNEL,
                        ],
                        check=True,
                        timeout=5,
                        capture_output=True,
                    )
                    opened = True
                except:
                    pass

            if opened:
                print(f"\033[1;32m━▷ ✅ WhatsApp Channel opening in browser!")
            else:
                print(
                    f"\033[1;33m━▷ ⚠️  Auto-open failed. Tap the link above or open manually"
                )

            print(f"\033[1;32m━▷ Send this key in channel response: \033[1;36m{id}")

            input("\n\033[1;33mAfter getting approval, press ENTER to check again...")
            return approval()

    except Exception as e:
        print(f"\033[1;31m━▷ Error checking approval: {e}")
        print("\033[1;31m━▷ Please check your internet connection")
        choice = input('\n\033[1;33mPress ENTER to retry or type "exit" to quit: ')
        if choice.lower() == "exit":
            exit("\033[1;32m━▷ Thanks for trying LEO TOOL!")
        return approval()


# ------------------------[ VERSION ]-----------------------#
____Version____ = "\033[1;32mV/1.1"
# ------------------[ LOGO ]-------------------#
logo = f"""\033[1;37mWELCOME TO LEO COMMAND

\033[1;30m
                  ▉▉▉▉
                 ▂▉▉▉▉▂
                \033[1;33m╰▏ ┛┗ ▕╯
                 ╲ 👅 ╱
                 \033[1;32m╱▔╲╱▔╲
               ╱ ╱▏╭╮▕╲ ╲
               ╲ ╲▏╭╮▕╱ ╱       \033[1;31m╷  ╭─╴╭─╮
                \033[1;35m ╲▉▉▉▉╱         \033[1;34m│  ├╴ │ │
                \033[1;34m  ▏╭╮▕          \033[1;32m╰─╴╰─╴╰─╯ 
                \033[1;34m  ▏▏▕▕
                  ▏▏▕▕
                \033[1;31m ╭╰ ╮╭╰ ╮
               \033[1;39mTHE \033[1;35mKING \033[1;36mLEO
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[0;92m
\033[1;31m██╗     ███████╗ ██████╗ 
\033[1;32m██║     ██╔════╝██╔═══██╗
\033[1;33m██║     █████╗  ██║   ██║
\033[1;34m██║     ██╔══╝  ██║   ██║
\033[1;35m███████╗███████╗╚██████╔╝
\033[1;36m╚══════╝╚══════╝ ╚═════╝ 

\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;39m━▷ \033[0;91m𝙊𝙒𝙉𝙀𝙍    \033[1;39m◈✙◈\033[1;33m MR LEO 
\033[1;39m━▷ \033[0;91m𝙎𝘼𝙏𝙐𝙏𝘼𝙎  \033[1;39m◈✙◈ \033[0;92mPAID
\033[1;39m━▷ \033[0;91m𝙑𝙀𝙍𝙎𝙄𝙊𝙉  \033[1;39m◈✙◈ \033[1;37m1.0
\033[1;39m━▷ \033[1;36mFEEL THE POWER OF LEO 
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;39m━▷ LOCATION \033[1;39m◈✙◈ {___ccc___}
\033[1;39m━▷ DEVICE   \033[1;39m◈✙◈ {___brand___}
\033[1;39m━▷ BIT      \033[1;39m◈✙◈ {___bit___}
\033[1;39m━▷ SIM SLOT \033[1;39m◈✙◈ {___sim___}
\033[1;34m─────────────────────────────────────────────────────"""

# ------------------[ LOGO2 ]-------------------#
logo2 = """\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑
\033[1;37mWELCOME TO LEO COMMAND

\033[1;31m╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  
║║║║╣ ║  ║  ║ ║║║║║╣   
╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝  


\033[1;32m╔╦╗╔═╗
 ║ ║ ║
 ╩ ╚═╝


\033[1;33m╦  ╔═╗╔═╗
║  ║╣ ║ ║
╩═╝╚═╝╚═╝


\033[1;35m╔╦╗╔═╗╔═╗╦  
 ║ ║ ║║ ║║  
 ╩ ╚═╝╚═╝╩═╝

 \033[1;31mOWNER \033[1;32mTOOL \033[1;33mOF \033[1;37mMR \033[1;35mLEO 

\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑"""


# ------------------[ LINEX ]-------------------#
def linex():
    print(f"\033[1;34m─────────────────────────────────────────────────────")


# ------------------[ SYSTEM CLEAR ]-------------------#
def clear():
    os.system("clear")
    print(logo)


# ------------------[ LOOP ]-------------------#
loop = 0
lim = 0
tp = 0
cnt = 0
ok = []
cp = []
cps = 0
oks = 0
died = 0
live = 0
uid = []


# ------------------[ MENU CHAND ]-------------------#
# ------------------[ CONNECTION WAIT ]-------------------#
def wait_conn():
    while True:
        for i in range(60, 0, -1):
            sys.stdout.write(f"\r\033[1;31m━▷ Connection Lost! Retrying in {i}s... \033[0m")
            sys.stdout.flush()
            time.sleep(1)
            try:
                requests.get("https://www.google.com", timeout=2)
                sys.stdout.write("\r\033[K\033[1;32m━▷ Connected! Resuming...\033[0m\n")
                return
            except:
                continue

# ------------------[ YOUTUBE CHANNEL ]-------------------#
YOUTUBE_CHANNEL = "https://whatsapp.com/channel/0029Vb8CSZQIt5rolffFX31P"

def open_url(url):
    try:
        import webbrowser
        if webbrowser.open(url):
            return True
    except:
        pass
    try:
        subprocess.run(["termux-open-url", url], check=True, timeout=5, capture_output=True)
        return True
    except:
        pass
    try:
        subprocess.run(["xdg-open", url], check=True, timeout=5, capture_output=True)
        return True
    except:
        pass
    try:
        subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url], check=True, timeout=5, capture_output=True)
        return True
    except:
        pass
    return False

# ------------------[ UID CHECKER ]-------------------#
UID_FOLDER = "ALIVE-UID-LEO"

def uid_checker():
    clear()
    print(" \033[1;32m[\033[1;31m–\033[1;32m] UID CHECKER")
    linex()
    path = input(" \033[1;32m[\033[1;31m–\033[1;32m] ENTER TXT FILE PATH : ").strip()
    if not path:
        print(" \033[1;32m[\033[1;31m–\033[1;32m] \033[1;31mNO FILE SELECTED")
        time.sleep(2)
        menu()
        return
    try:
        with open(path, "r") as f:
            uids = [line.strip() for line in f if line.strip()]
    except:
        print(f" \033[1;32m[\033[1;31m–\033[1;32m] \033[1;31mFILE NOT FOUND: {path}")
        time.sleep(2)
        menu()
        return
    os.makedirs(UID_FOLDER, exist_ok=True)
    live_path = os.path.join(UID_FOLDER, "LIVE-UID.txt")
    death_path = os.path.join(UID_FOLDER, "DEATH-UID.txt")
    live_count = 0
    death_count = 0
    total = len(uids)
    print(f" \033[1;32m[\033[1;31m–\033[1;32m] TOTAL UIDS: \033[1;37m{total}")
    linex()
    for idx, uid in enumerate(uids, 1):
        status = lock_checker(uid)
        if status == "Active":
            live_count += 1
            sys.stdout.write(f"\r\033[1;32m[LIVE] {uid}                    \n")
            sys.stdout.flush()
            with open(live_path, "a") as f:
                f.write(uid + "\n")
        elif status == "Locked":
            death_count += 1
            sys.stdout.write(f"\r\033[1;31m[DEATH] {uid}                    \n")
            sys.stdout.flush()
            with open(death_path, "a") as f:
                f.write(uid + "\n")
        else:
            sys.stdout.write(f"\r\033[1;33m[ERROR] {uid}                    \n")
            sys.stdout.flush()
    linex()
    print(f" \033[1;32m[\033[1;31m–\033[1;32m] ✅ LIVE  : \033[1;32m{live_count}")
    print(f" \033[1;32m[\033[1;31m–\033[1;32m] ❌ DEATH : \033[1;31m{death_count}")
    print(f" \033[1;32m[\033[1;31m–\033[1;32m] \033[1;37mSAVED TO: {UID_FOLDER}/")
    input("\n \033[1;33mPress ENTER to go back...")
    menu()

def menu():
    clear()
    print(" \033[1;32m[\033[1;31m1\033[1;32m] AUTO CREATE FB")
    print(" \033[1;32m[\033[1;31m2\033[1;32m] UID CHECKER")
    print(" \033[1;32m[\033[1;31m3\033[1;32m] SPREAD UID")
    print(" \033[1;32m[\033[1;31m0\033[1;32m] EXIT ")
    linex()
    xd = input(" \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ")
    if xd in ["1", "01"]:
        print("\033[1;32m━▷ Opening YouTube Channel...\033[1;36m")
        print(f"  {YOUTUBE_CHANNEL}")
        open_url(YOUTUBE_CHANNEL)
        time.sleep(1)
        method()
    elif xd in ["2", "02"]:
        print("\033[1;32m━▷ Opening WhatsApp Channel...\033[1;36m")
        print("  https://whatsapp.com/channel/0029Vb8CSZQIt5rolffFX31P")
        open_url("https://whatsapp.com/channel/0029Vb8CSZQIt5rolffFX31P")
        time.sleep(1)
        uid_checker()
    elif xd in ["3", "03"]:
        auto_create_fb_method_3_()
    elif xd in ["0", "00"]:
        exit(" \033[1;32m[\033[1;31m–\033[1;32m] THANKS FOR USE ♥ ")
    else:
        print(
            " \033[1;32m[\033[1;31m–\033[1;32m] \033[1;31mOPTION NOT FOUND IN MENU..."
        )
        time.sleep(1)
        menu()


# ------------------[ AUTO CREATE FACEBOOK METHOD ]-------------------#
def method():
    clear()
    print(" \033[1;32m[\033[1;31m1\033[1;32m] METHOD 1")
    print(" \033[1;32m[\033[1;31m2\033[1;32m] METHOD 2")
    linex()
    xd = input(" \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ")
    if xd in ["1", "01"]:
        auto_create_fb_method_1_()
    elif xd in ["2", "02"]:
        auto_create_fb_method_2_()


# ------------------[ OKS AND CPS AND COOKIE ]-------------------#
def cvt(st, ran):
    try:
        if st == "oks":
            cookie = "c_user=%s;xs=%s;fr=%s;datr=%s;" % (
                ran["c_user"],
                ran["xs"],
                ran["fr"],
                ran["datr"],
            )
        elif st == "cps":
            cookie = "checkpoint=%s;datr=%s;fr=%s;" % (
                ran["checkpoint"],
                ran["datr"],
                ran["fr"],
            )
    except Exception as e:
        cookie = "; ".join([str(x) + "=" + str(y) for x, y in ran])
    return str(cookie)


# ------------------[ METHOD 1 ]-------------------#
def auto_create_fb_method_1_() -> None:
    clear()
    print(" \033[1;32m[\033[1;31m1\033[1;32m] NAME PHILIPPINE")
    print(" \033[1;32m[\033[1;31m2\033[1;32m] NAME INDONESIA")
    print(" \033[1;32m[\033[1;31m3\033[1;32m] NAME VIETNAMESE")
    linex()
    ethan_username = input(" \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ")
    linex()
    print(" \033[1;32m[\033[1;31m1\033[1;32m] AUTO PASSWORD")
    print(" \033[1;32m[\033[1;31m2\033[1;32m] MANUAL PASSWORD")
    linex()
    ethan_password = input(" \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ")
    linex()
    if ethan_password in ["2", "02"]:
        pasw2 = input(" \033[1;32m[\033[1;31m–\033[1;32m] ENTER CUSTOM PASSWORD : ")
        linex()
    clear()
    print(" \033[1;32m[\033[1;31m–\033[1;32m] TOTAL UID  \033[1;33m: \033[1;37m50000")
    print(
        " \033[1;32m[\033[1;31m–\033[1;32m] IF NO RESULT \033[1;33m[\033[1;31mON\033[1;33m/\033[1;31mOFF\033[1;33m] \033[1;32mAIRPLAN MODE"
    )
    linex()
    for make in range(50000):
        global oks, cps
        boos = random.choice([P, M, H, K, B, U, O, N])
        sys.stdout.write(
            f"\r\r\033[1;37m<[{boos}LEO-TRICKER\033[1;37m]<🖤>[{make + 1}|\033[1;32m{oks}\033[1;37m]> "
        )
        sys.stdout.flush()
        # sys.stdout.write(f"\r\r\033[1;37m[CHAND-CREATE] {make+1}\033[1;37m|\033[1;32mOK-:{len(oks)}\033[1;37m");sys.stdout.flush()
        ses = requests.Session()
        response = ses.get(
            url="https://x.facebook.com/reg",
            params={
                "_rdc": "1",
                "_rdr": "",
                "wtsid": "rdr_0t3qOXoIHbMS6isLw",
                "refsrc": "deprecated",
            },
        )
        mts = ses.get("https://x.facebook.com").text
        m_ts = re.search(r'name="m_ts" value="(.*?)"', str(mts)).group(1)
        formula = extractor(response.text)
        if ethan_username in ["1", "01"]:
            firstname, lastname = fake_philippines()
        if ethan_username in ["2", "02"]:
            firstname, lastname = fake_indonesia()
        if ethan_username in ["3", "03"]:
            firstname, lastname = fake_vietnamese()
        domain = random.choice(
            [
                "gmail.com",
                "hotmail.com",
                "outlook.com",
                "yahoo.com",
                "myyahoo.com",
                "protonmail.com",
                "live.com",
                "rocket.com",
            ]
        )
        email2 = (
            f"{firstname.lower()}{lastname.lower()}{random.randint(10, 99)}@{domain}"
        )
        if ethan_password in ["1", "01"]:
            pasw2 = f"{firstname.lower()}{lastname.lower()}"
        # print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] NAME   : {firstname} {lastname}")
        # print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] EMAIL  : {email2}")
        cookies = None
        payload1 = None
        payload2 = {}
        payload3 = {}
        payload3 = {
            "ccp": "2",
            "reg_instance": str(formula["reg_instance"]),
            "submission_request": "true",
            "helper": "",
            "reg_impression_id": str(formula["reg_impression_id"]),
            "ns": "1",
            "zero_header_af_client": "",
            "app_id": "103",
            "logger_id": str(formula["logger_id"]),
            "field_names[0]": "firstname",
            "firstname": firstname,
            "lastname": lastname,
            "field_names[1]": "birthday_wrapper",
            "birthday_day": str(random.randint(1, 28)),
            "birthday_month": str(random.randint(1, 12)),
            "birthday_year": str(random.randint(1992, 2009)),
            "age_step_input": "",
            "did_use_age": "false",
            "field_names[2]": "reg_email__",
            "reg_email__": email2,
            "field_names[3]": "sex",
            "sex": "2",
            "preferred_pronoun": "",
            "custom_gender": "",
            "field_names[4]": "reg_passwd__",
            "name_suggest_elig": "false",
            "was_shown_name_suggestions": "false",
            "did_use_suggested_name": "false",
            "use_custom_gender": "false",
            "guid": "",
            "pre_form_step": "",
            "encpass": "#PWD_BROWSER:0:{}:{}".format(
                str(time.time()).split(".")[0], pasw2
            ),
            "submit": "Sign Up",
            "fb_dtsg": "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",
            "jazoest": str(formula["jazoest"]),
            "lsd": str(formula["lsd"]),
            "__dyn": "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
            "__csr": "",
            "__req": "p",
            "__fmt": "1",
            "__a": "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
            "__user": "0",
        }
        header1 = {
            "Host": "m.facebook.com",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": W_ueragent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "dnt": "1",
            "X-Requested-With": "mark.via.gp",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "dpr": "1.75",
            "viewport-width": "980",
            "sec-ch-ua": '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-ch-ua-platform-version": '""',
            "sec-ch-ua-model": '""',
            "sec-ch-ua-full-version-list": "",
            "sec-ch-prefers-color-scheme": "dark",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        }
        reg_url = "https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1"
        while True:
            try:
                py_submit = ses.post(reg_url, data=payload3, headers=header1, proxies=proxies)
                break
            except:
                wait_conn()
        if "c_user" in py_submit.cookies:
            # first_cok = ses.cookies.get_dict()
            # uid = str(first_cok["c_user"])
            # cookie = (";").join([ "%s=%s" % (key,value) for key,value in ses.cookies.get_dict().items()])
            cok = ";".join([k + "=" + v for k, v in ses.cookies.get_dict().items()])
            uid = re.findall("c_user=(.*?);", cok)[0]
            coki = (
                cvt("oks", ses.cookies.get_dict())
                + "dpr=2;locale=en_US;wd=950x1835;m_page_voice="
                + uid
            )
            print("\r\033[1;32m<[LEO-OK]> " + uid + " | " + pasw2 + "\033[1;37m")
            # print("\033[1;33m<[BISCUT-🍪]> :\033[1;33m "+coki)
            # print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] UID    : {uid}")
            # print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] PASS   : {pasw2}")
            # print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] COOKIE : {coki}")
            # linex()
            file_path_ok = os.path.join(folder_path, "LEO-CREATE-OK.txt")
            file_path_cookies = os.path.join(folder_path, "LEO-CREATE-COOKIE.txt")
            with (
                open(file_path_ok, "a") as file_ok,
                open(file_path_cookies, "a") as file_cookies,
            ):
                file_ok.write(uid + " | " + pasw2 + "\n")
                file_cookies.write(uid + " | " + pasw2 + " |-----> " + coki + "\n")
            oks += 1
        else:
            # print(f" \033[1;32m[\033[1;31m–\033[1;32m] \033[1;31mSUCCESSFULLY CHECKPOINT ID")
            # linex()
            cps += 1


# ------------------[ METHOD 2 ]-------------------#
def auto_create_fb_method_2_() -> None:
    clear()
    print(" \033[1;32m[\033[1;31m1\033[1;32m] NAME PHILIPPINE")
    print(" \033[1;32m[\033[1;31m2\033[1;32m] NAME INDONESIA")
    print(" \033[1;32m[\033[1;31m3\033[1;32m] NAME VIETNAMESE")
    linex()
    ethan_username = input(" \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ")
    linex()
    print(" \033[1;32m[\033[1;31m1\033[1;32m] AUTO PASSWORD")
    print(" \033[1;32m[\033[1;31m2\033[1;32m] MANUAL PASSWORD")
    linex()
    ethan_password = input(" \033[1;32m[\033[1;31m–\033[1;32m] CHOOSE : ")
    linex()
    if ethan_password in ["2", "02"]:
        pasw2 = input(" \033[1;32m[\033[1;31m–\033[1;32m] ENTER CUSTOM PASSWORD : ")
        linex()
    for make in range(1000):
        sys.stdout.write(
            f"\r\r\033[1;37m<[{boos}MR-LEO\033[1;37m]<🖤>[{make + 1}|\033[1;32m{len(ok)}\033[1;37m]> "
        )
        sys.stdout.flush()
        ses = requests.Session()
        fake = Faker()
        api_key = "882a8490361da98702bf97a021ddc14d"
        secret = "62f8ce9f74b12f84c123cc23437a4a32"
        gender = random.choice(["M", "F"])
        if ethan_username in ["1", "01"]:
            firstname, lastname = fake_philippines()
        if ethan_username in ["2", "02"]:
            firstname, lastname = fake_indonesia()
        if ethan_username in ["3", "03"]:
            firstname, lastname = fake_vietnamese()
        domain = random.choice(
            [
                "gmail.com",
                "hotmail.com",
                "outlook.com",
                "yahoo.com",
                "myyahoo.com",
                "protonmail.com",
                "live.com",
                "rocket.com",
            ]
        )
        email2 = (
            f"{firstname.lower()}{lastname.lower()}{random.randint(10, 99)}@{domain}"
        )
        if ethan_password in ["1", "01"]:
            pasw2 = f"{firstname.lower()}{lastname.lower()}"
        time.sleep(5)
        print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] NAME   : {firstname} {lastname}")
        print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] EMAIL  : {email2}")
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
        req = {
            "api_key": api_key,
            "attempt_login": True,
            "birthday": birthday.strftime("%Y-%m-%d"),
            "client_country_code": "US",
            "fb_api_caller_class": "com.facebook.registration.protocol.RegisterAccountMethod",
            "fb_api_req_friendly_name": "registerAccount",
            "firstname": firstname,
            "format": "json",
            "gender": gender,
            "lastname": lastname,
            "email": email2,
            "locale": "en_US",
            "method": "user.register",
            "password": pasw2,
            "reg_instance": generate_random_string(32),
            "return_multiple_errors": True,
        }
        headers = {"User-Agent": user_agent()}
        sorted_req = sorted(req.items(), key=lambda x: x[0])
        sig = "".join(f"{k}={v}" for k, v in sorted_req)
        ensig = hashlib.md5((sig + secret).encode()).hexdigest()
        req["sig"] = ensig
        api_url = "https://b-api.facebook.com/method/user.register"
        while True:
            try:
                response = ses.post(api_url, data=req, headers=headers, proxies=proxies)
                break
            except:
                wait_conn()
        reg = response.json()
        uid = reg.get("new_user_id")
        token = reg.get("session_info", {}).get("access_token")
        if uid:
            status = lock_checker(uid)
            if status == "Locked":
                print(
                    f" \033[1;32m[\033[1;31m–\033[1;32m] \033[1;31mSUCCESSFULLY CHECKPOINT ID"
                )
            else:
                print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] UID    : {uid}")
                print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] PASS   : {pasw2}")
                print(f"\r \033[1;32m[\033[1;31m–\033[1;32m] TOKEN  : {token}")
                linex()
                ok.append(uid)
        else:
            print(
                f" \033[1;32m[\033[1;31m–\033[1;32m] \033[1;31mSUCCESSFULLY CHECKPOINT ID"
            )
            linex()


# ------------------[ METHOD 3 SPREAD UID ]-------------------#
SPREAD_FOLDER = "SPREAD-UID-LEO"


def auto_create_fb_method_3_():
    clear()
    linex()
    print(" \033[1;32m[\033[1;31m–\033[1;32m] SPREAD UID")
    linex()
    path = input(" \033[1;32m[\033[1;31m–\033[1;32m] ENTER TXT FILE PATH : ").strip()
    if not path:
        print(" \033[1;32m[\033[1;31m–\033[1;32m] \033[1;31mNO FILE SELECTED")
        time.sleep(2)
        menu()
        return
    try:
        with open(path, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    except:
        print(f" \033[1;32m[\033[1;31m–\033[1;32m] \033[1;31mFILE NOT FOUND: {path}")
        time.sleep(2)
        menu()
        return
    os.makedirs(SPREAD_FOLDER, exist_ok=True)
    out_path = os.path.join(SPREAD_FOLDER, "SPREAD-UID.txt")
    total = len(lines)
    count = 0
    print(f" \033[1;32m[\033[1;31m–\033[1;32m] TOTAL LINES: \033[1;37m{total}")
    linex()
    with open(out_path, "w") as out:
        for line in lines:
            uid = line.split("|")[0].split(",")[0].split()[0].strip()
            if uid and uid.isdigit():
                out.write(uid + "\n")
                count += 1
                sys.stdout.write(f"\r\033[1;32m[SPREAD] {uid}                    \n")
                sys.stdout.flush()
    linex()
    print(f" \033[1;32m[\033[1;31m–\033[1;32m] ✅ SPREAD: \033[1;37m{count}")
    print(f" \033[1;32m[\033[1;31m–\033[1;32m] \033[1;37mSAVED TO: {SPREAD_FOLDER}/SPREAD-UID.txt")
    input("\n \033[1;33mPress ENTER to go back...")
    menu()


# ------------------[  END  ]-------------------#
if __name__ == "__main__":
    while True:
        try:
            if approval():
                menu()
            else:
                exit("\033[1;31m━▷ Access Denied! Get approval first.")
        except:
            wait_conn()
