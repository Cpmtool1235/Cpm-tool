Current version of the script 
debug_mode = 0
CURRENT_VERSION = """
2.3.10
"""
CURRENT_VERSION=CURRENT_VERSION.replace('\n','')
server_local = "http://127.0.0.1:3000"
server_online = "https://api.topixsb.dev"
mode_server = server_online
"""
-------------------------------------------
MAJOR (Angka Pertama):

Angka ini meningkat ketika ada perubahan yang tidak kompatibel yang mengharuskan 
pengguna untuk memodifikasi kode atau penggunaan mereka yang ada. Misalnya, 
jika suatu fungsi dihapus atau perilakunya berubah secara signifikan, Anda akan 
meningkatkan versi mayor.
-------------------------------------------
MINOR (Angka Kedua):

Angka ini meningkat ketika fitur baru ditambahkan dengan cara yang kompatibel 
dengan versi sebelumnya. Ini berarti bahwa fungsionalitas yang ada tetap tidak 
berubah, tetapi kemampuan atau peningkatan baru diperkenalkan. Misalnya, 
jika fungsi baru ditambahkan tanpa memengaruhi yang sudah ada, Anda akan 
menaikkan versi minor.
-------------------------------------------
PATCH (Angka Ketiga):

Angka ini meningkat ketika perbaikan bug yang kompatibel dengan versi sebelumnya 
diperkenalkan. Ini biasanya merupakan perubahan kecil yang menyelesaikan masalah 
tanpa menambah fitur baru atau merusak fungsionalitas yang ada. Misalnya, 
jika ada bug yang diperbaiki dalam suatu fungsi tetapi antarmuka fungsi tersebut 
tetap sama, Anda akan menaikkan versi patch.
-------------------------------------------
"""



import os,sys,random
import platform
try:
    import httpx
    from colr import color
    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    local_ip = httpx.get('https://api.ipify.org').text
    response = httpx.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    print(f"problem : {e}")
    input("lets Fix it?... Press Enter")
    def is_termux():
        return 'termux' in platform.system().lower()

    if is_termux():
        print("Python is running in Termux.")
        os.system("pkg update && pkg upgrade -y")
        os.system("termux-setup-storage -y")
    else:
        print("Python is running on a Linux PC.")
    os.system("pip install colr")
    os.system("pip install httpx")
    os.system("pip install pystyle")
    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem

VERSION_CHECK_URL = f"{mode_server}/termux-version"

def get_latest_version_info():
    try:
        response = httpx.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None

def download_new_version(download_url, filename):
    response = httpx.get(download_url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)
        
def update_script():
    version_info = get_latest_version_info()
    if not version_info:
        return
    
    latest_version = version_info.get("version")
    download_url = version_info.get("download_url")
    print(download_url)
    print(f"CURRENT_VERSION {CURRENT_VERSION}\nlatest_version {latest_version}\ndownload_url {download_url}")
    if latest_version and download_url:
        if latest_version != CURRENT_VERSION:
            print(f"New version available: {latest_version}")
            print(f"Downloading update... {download_url}")
            download_new_version(download_url, sys.argv[0])
            print("Script updated to the latest version. Please restart the script.")
            exit()
        else:
            print("You already have the latest version.")
    else:
        print("Invalid version information received.")
update_script()


def disp(clrnama):
    clrfirsttime = True
    clrVnama = clrnama.split("[")
    clrdisps = clrVnama[0]
    for clrx in clrVnama:
        if clrfirsttime == False:
            clrcode1 = f"{clrx[0:2]}"
            clrcode2 = f"{clrx[2:4]}"
            clrcode3 = f"{clrx[4:6]}"
            clrcode1 = (int(clrcode1, 16))
            clrcode2 = (int(clrcode2, 16))
            clrcode3 = (int(clrcode3, 16))
            clrhuruf = clrx[7:8]
            clrdisps += color(clrhuruf,
                              fore=(clrcode1,
                                    clrcode2,
                                    clrcode3),
                              back=(0, 0, 0))
        if clrfirsttime:
            clrfirsttime = False

    clrdisps += clrVnama[len(clrVnama)-1][8:len(clrVnama[len(clrVnama)-1])]
    return(clrdisps)

warnasekarang=""
def generate(namax):
    global warnasekarang
    gabungwarna = ""
    contohnama = namax
    # proses memecah huruf di nama
    data = {
        "huruf": "",
        "kodewarna": [255, 0, 0],
        "mode": 1,
        "kodewarnaCPM": ""
    }
    while True:
        while True:
            tanya = random.choice(["merah","kuning","hijau","biru","ungu","pink"])
            if tanya!=warnasekarang:
                warnasekarang = tanya
                break
        if tanya == "merah":
            data["kodewarna"] = [255, 0, 0]
            break
        elif tanya == "kuning":
            data["kodewarna"] = [230, 245, 66]
            break
        elif tanya == "hijau":
            data["kodewarna"] = [0, 255, 0]
            break
        elif tanya == "biru":
            data["kodewarna"] = [0, 0, 255]
            break
        elif tanya == "ungu":
            data["kodewarna"] = [150, 66, 245]
            break
        elif tanya == "pink":
            data["kodewarna"] = [245, 66, 215]
            break
        else:
            print("Harus sesuai pilihan warna ..!")

    for huruf in contohnama:
        while True:
            # print(f"\nmode sekarang : {data['mode']}")
            tambah = 45
            if data["mode"] == 1:
                if data["kodewarna"][1]+tambah <= 255:
                    data["kodewarna"][1] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [255, 255, 0]
            elif data["mode"] == 2:
                if data["kodewarna"][0]-tambah >= 0:
                    data["kodewarna"][0] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 255, 0]
            elif data["mode"] == 3:
                if data["kodewarna"][2]+tambah >= 255:
                    data["kodewarna"][2] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 255, 255]
            elif data["mode"] == 4:
                if data["kodewarna"][1]-tambah >= 0:
                    data["kodewarna"][1] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 0, 255]
            elif data["mode"] == 5:
                if data["kodewarna"][0]+tambah >= 255:
                    data["kodewarna"][0] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [255, 0, 255]
            elif data["mode"] == 6:
                if data["kodewarna"][2]-tambah >= 255:
                    data["kodewarna"][2] -= tambah
                    break
                else:
                    data["mode"] = 1
                    data["kodewarna"] = [255, 0, 0]
        # print(f"{huruf} {data['kodewarna']}")
        gabungwarna += color(huruf,
                             fore=(data["kodewarna"][0],
                                   data["kodewarna"][1],
                                   data["kodewarna"][2]),
                             back=(0, 0, 0))
        kodas = []
        for t in range(3):
            clrcode = hex(data["kodewarna"][t])[2::]
            if len(clrcode) == 1:
                clrcode += "0"
            kodas.append(clrcode)
        data["kodewarnaCPM"] += f"[{kodas[0]}{kodas[1]}{kodas[2]}]{huruf}"
    # print(f"hasil\t:  {disp(data['kodewarnaCPM'])}")
    # print(f"kode\t:  {data['kodewarnaCPM']}")
    return data["kodewarnaCPM"]
def refresh_x():
    import inspect
    kucing_garong = inspect.getfile(inspect.currentframe())
    with open(kucing_garong, 'r') as file:
        gajah_terbang = file.read()
        gajah_duduk = len(gajah_terbang)
    if debug_mode!=1: 
            pass
    return gajah_duduk
pySystem.Clear()
pySystem.Size(80, 40)


text = """
< [ YouTube TopixSB ] > X < [ ₱ⱤØ₲Ɽ₳₥ ฿Ɇ₮₳ ] >"""[1:]

banner = r"""
___ç$$$ç________________
__$$$$$$$_####______####_       YouTube TopixSB
___*$$$$$$ç####___########        
_____*$$$$$$$$$$$##########     ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█
_____$$$$$$$$$$$$$##########    ░▒█░░ ░▀▀▀▄▄ ▒█▀▀▄
______$$$$$$$$$$$$$##########   ░▒█░░ ▒█▄▄▄█ ▒█▄▄█ 
______$$$$$$$$$$_$$$##########
______$$$$$$$$$$##$$$##########
_______$$$$$$$$$_##$$##########
______$$$$$$$$$$___$$#########
_____$_$$$$$$$$$$__$$_########
___$$__$$$$$$$$$$_$$$__######
______$$$$$$$$$$__$$$___#####
______$$$$$$$$$___$$____####
______$$$$$$$$$_________###
______$$$$$$$$__________##
_______$$$$$$___________##
_______$$$$$$______________
_______$$$$$$$$____________
_______$$$$$$$$____________
_______$$$$_$$$$___________
_______$$$$_$$$$___________
_______$$$___$$$$__________
__ççç$$$$$$_çç$$$$__________       
                          
           Car Parking Multiplayer Instant Script
                    LESS THEN 1 MINUTE

                        PRESS ENTER          
"""[1:]


pyAnime.Fade(pyCenter.Center(banner), pyColors.purple_to_red, pyColorate.Vertical, enter=True)

pySystem.Clear()

print("\n"*2    )
print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))
print("\n"*2)


delet=["cpm/pos.py","cpm/__init__.py"]
for psdd in delet:
    if os.path.exists(f"{psdd}") == True:
        os.system(f"rm {psdd}")



def c(colr, tex):
    try:
        w = {
            "RED": [255, 0, 0],
            "GREEN": [0, 255, 0],
            "CYAN": [0, 255, 255],
            "YELLOW": [255, 255, 0],
            "GOLD": [255, 223, 0]
        }
        return color(tex,
                     fore=(w[colr.upper()][0],
                           w[colr.upper()][1],
                           w[colr.upper()][2]),
                     back=(0, 0, 0))
    except:
        return tex
def mask_password(password):
    if len(password) <= 3:
        return password
    return password[:3] + '*' * (len(password) - 3)
def heder():
        if Your_Data['username']:
            get_userInfo()
        pySystem.Clear()
        print(f"build : {refresh_x()}\tThis program is in beta and is still being developed")
        versi_tampil = disp(generate(f"Topix SB CPM TOOLS {CURRENT_VERSION}"))
        loc_info = f"  Location\t  : {data_jaringan.get('city')}, {data_jaringan.get('region')}, {data_jaringan.get('country')}"
        loc_info = pyColorate.Horizontal(pyColors.green_to_yellow, loc_info)
        isp_info = f"  ISP     \t  : {data_jaringan.get('org')}"
        isp_info = pyColorate.Horizontal(pyColors.green_to_yellow, isp_info)
        bannerwz = f"""{c("cyan","=====================================================")}
  {versi_tampil} {c("cyan","||")} {c("green","https://carparking.topixsb.dev/")}
{c("cyan","=====================================================")}
{loc_info}
{isp_info}"""
        if Your_Data['email_web']:
            data_client=f"""
  username   : {Your_Data['username']}
  role       : {Your_Data['role']}
  money      : {Your_Data['money']}
  expire_at  : {Your_Data['expire_at']}
  last login : {Your_Data['last_login_date']}"""
            if 'email' in Your_Data:
                data_client+=f"""\n\n  Car Parking Email : {Your_Data["email"]}
  Car Parking Passw : {mask_password(Your_Data["password"])}"""
            
            bannerwz+=pyColorate.Horizontal(pyColors.green_to_yellow, data_client)
        print(bannerwz)

tex="""     IMPORTANT READ

    You must log out of the CPM application first, 
    unless you only want to use the "Inject Rank" and "Instant Rank" features, 
    as these two features do not require you to log out.

    Please refill your cash only at https://carparking.topixsb.dev

"""

print(pyColorate.Horizontal(pyColors.green_to_yellow, pyCenter.XCenter(tex)))



def warnain(text,inpo="",title=""):
    tex = f"""{c("cyan","=====================================================")}"""
    if inpo:
        tex+=f"\n\t\t{pyColorate.Horizontal(pyColors.red_to_purple, inpo)}"
    if title:
        tex+=f"\n\t\t{pyColorate.Horizontal(pyColors.cyan_to_green, title)}"
    tex+=f"""
{pyColorate.Horizontal(pyColors.cyan_to_green, text)}
{c("cyan","=====================================================")}"""
    print(tex)


def send_registration_data(uname, upass):
    url = f"{mode_server}/register-acc"
    
    data = {
        "username": uname,
        "password": upass
    }
    
    try:
        response = httpx.post(url, data=data)
        
        # Pastikan untuk memanggil .json() untuk mendapatkan data JSON
        response_data = response.json()
        return response_data
    except Exception as e:
        return f"An error occurred: {e}"
def send_login_data(uname, upass):
    url = f"{mode_server}/login-acc"
    
    data = {
        "username": uname,
        "password": upass
    }
    
    try:
        response = httpx.post(url, data=data)
        
        # Pastikan untuk memanggil .json() untuk mendapatkan data JSON
        response_data = response.json()
        return response_data
    except Exception as e:
        return f"An error occurred: {e}"

def serper(cit,datanya):
    # URL of the endpoint
    url = f"{mode_server}/app_endpoint"

    # Example data for the New Acc item
    data = {
            "username":Your_Data['username'],
            "item": {
                "name": cit
            },
            "email": Your_Data['email'],
            "password":Your_Data['password'],
        }
    for x in datanya:
        data[x]=datanya[x]
    # Make the request
    response = httpx.post(url, json=data)
    send_login_data(Your_Data['username'],Your_Data['password'])
    return response.json()


def get_userInfo():
    # URL of the endpoint
    url = f"{mode_server}/get_UserInfo"

    # Example data for the New Acc item
    data = {
        "user": Your_Data['username']
    }

    try:
        # Make the request with a timeout
        response = httpx.post(url, json=data, timeout=10.0)  # Timeout in seconds
        response.raise_for_status()  # Raise an error for bad responses
        reqreg = response.json()
        Your_Data['role'] = reqreg['role']
        Your_Data['last_login_date'] = reqreg['last_login_date']
        Your_Data['expire_at'] = reqreg['expire_at']
        Your_Data['money'] = reqreg['balance']
    except httpx.TimeoutException:
        print("Request timed out. Please try again later.")
    except httpx.RequestError as e:
        print(f"An error occurred while making the request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

Your_Data = {
    'email_web': None, 
    'expire_at': None, 
    'last_login_date': None, 
    'money': None, 
    'role': None, 
    'username': None
}
req_menu = httpx.get(f"{mode_server}/get_menu")
menu_cpm1 = req_menu.json()
if __name__ == "__main__":
    input("Understand ? ")
    inpo = ""
    while True:
        if not Your_Data['email_web']:
            heder()
            menus="""  [1] Login
  [2] Register
  [q] Exit"""
            warnain(menus,inpo)
            pil = input("  Choice : ")
            heder()
            if pil == "1":
                warnain("  Login TopixSB Account")
                uname = input("  Username : ")
                upass = input("  Password : ")
                reqreg = send_login_data(uname,upass)
                inpo = reqreg['message']
                if reqreg['status']:
                    Your_Data['email_web']=reqreg['data']['email']
                    Your_Data['username']=reqreg['data']['username']
                    Your_Data['password'] = upass
                    Your_Data['identifier'] = reqreg['data']['password']

                    Your_Data['role'] = reqreg['data']['role']
                    Your_Data['last_login_date']=reqreg['data']['last_login_date']
                    Your_Data['expire_at']=reqreg['data']['expire_at']
                    Your_Data['money']=reqreg['data']['money']
            elif pil == "2":
                warnain("  Registration TopixSB Account")
                uname = input("  Username : ")
                upass = input("  Password : ")
                reqreg = send_registration_data(uname,upass)
                inpo = reqreg['message']
            elif pil == "q":
                exit()
        else:
            heder()
            menus="""  [1] CPM 1
  [2] CPM 2
  [q] Exit"""
            warnain(menus,inpo)
            pilawal = input("  Choice : ")
            inpo=""
            heder()
            if pilawal == "1":
                while True:
                    heder()
                    menus1=""
                    for x,v in enumerate(menu_cpm1):
                        if debug_mode==1:
                            menus1+=f"[{v['id_item']}]"
                        if v['status']=="active":
                            menus1+=f"  [{x}] {v['nama_item']}\t\t[{v['harga_item']}]\n"
                        elif v['status']=="maintenance":
                            menus1+=f"  [🔧] {v['nama_item']}\t\t[{v['harga_item']}]\n"
                    menus1+="  [q] Back"
                    warnain(menus1,inpo,title="[ Car Parking Multiplayer v8.8.19.4 ]")
                    pil = input("  Choice : ")
                    inpo=""
                    heder()
                    if pil == "q":
                        break
                    if pil == "":
                        continue
                    if 'email' not in Your_Data:
                        print( f"""{c("cyan","=====================================================")}""")
                        Your_Data['email'] = input("CPM Email : ")
                        Your_Data['password'] = input("CPM Password : ")
                    dat_pil = menu_cpm1[int(pil)]
                    data={}
                    gas=False
                    if dat_pil['id_item'] in [2,3,4,8,9,10,13,14,17]:
                        print( f"""{c("cyan","=====================================================")}""")
                        gas=True
                    else:
                        print( f"""{c("cyan","=====================================================")}""")
                        if dat_pil['id_item']==1:
                            data['customName'] = input("New Name : ")
                        elif dat_pil['id_item']==5:
                            data['customID'] = input("Custom ID : ")
                        elif dat_pil['id_item']==6:
                            data['customIDplus'] = input("Custom ID ++ : ")
                        elif dat_pil['id_item']==7:
                            while True:
                                try:
                                    data['varian'] = int(input("Varian [1 -> 100] : "))
                                    break
                                except:
                                    pass
                        elif dat_pil['id_item']==11:
                            data['hp'] = input("hp : ")
                            data['innerHp'] = input("innerHp : ")
                            data['nm'] = input("nm : ")
                            data['innerNm'] = input("innerNm : ")
                        elif dat_pil['id_item']==[12,15]:
                            data['new_email'] = input("new email : ")
                            data['new_password'] = input("new password : ")
                        elif dat_pil['id_item']==16:
                            data['boost_win'] = input("Win Boost : ")
                        gas=True
                        

                    if gas:
                        reqreg = serper(dat_pil['nama_item'],data)
                        inpo = reqreg['message']
            if pilawal == "2":
                pass
            elif pilawal == "q":
                exit()