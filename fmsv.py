import urllib.request
import json
import os
import subprocess
import sys

print("="*20,"\n\n")
print("__     _        __          \n")
print("/_____/\   /__//_//_/\    /_____/\     /_/\ /_/\   \n")
print("\::::_\/_  \::\| \| \ \   \::::_\/_    \:\ \\ \ \  \n")
print(" \:\/___/\  \:.      \ \   \:\/___/\    \:\ \\ \ \ \n")
print("  \:::._\/   \:.\-/\  \ \   \_::._\:\    \:\_/.:\ \ \n")
print("   \:\ \      \. \  \  \ \    /____\:\    \ ..::/ /\n")
print("    \_\/       \__\/ \__\/    \_____\/     \___/_/ \n")
print("- FmSV - By ZAW -")

print("\n\n","="*20)
input("Press Enter to start...")
print("="*20)
while True :
 server_name = input("server name ?")
 if server_name == "":
    print("// Enter Server name")
 else : 
     break

gamemode = input("gamemode [survival/creative] ?>")
if gamemode =="":
    gamemode="survival"
print(f"gamemode={gamemode}")

maximam_player = input("maximam player ?>")
if maximam_player =="":
    maximam_player="20"
print(f"max-players={maximam_player}")

difficulty = input("server difficulty [easy/normal/hard] ?>")
if difficulty == "":
    difficulty="normal"
print(f"difficulty={difficulty}")

online_mode = input("online mode [true/false] ?>")
if online_mode =="":
    online_mode="true"
print(f"online-mode={online_mode}")

view_distance = input("view-distance [10] ?>")
if view_distance == "":
    view_distance="10"

simulation_distance = input("simulation-distance [10]?>")
if simulation_distance =="":
    simulation_distance ="10"

level_seed = input("level_seed ?>")

hardcore = input("hardcore [true/false] ?>")
if hardcore == "":
    hardcore="false"
print(f"hardcore={online_mode}")

print("\n\nyou can chenge setting in server.properties\n\n")
print("="*20)

print("Checking Java ...\n")
def has_java():
    try:
        subprocess.run(["java", "-version"], capture_output=True, check=True)
        return True
    except:
        return False

def install_java():
    print("-- installing Java --")
    try :
        subprocess.run(["winget", "install", "Microsoft.OpenJDK.17", "--silent", "--accept-package-agreements","--accept-source-agreements"])
    except :
        print("Error in installing Java")

    print("Java installed!")

if not has_java():
    install_java()
else:
    print("-- Java is installed --")

print("\nServer Types:")
print("=" * 35)
server_types = {
    "1": {"name": "Vanilla", "desc": "Official Mojang server"},
    "2": {"name": "Forge", "desc": "Modded server (1.20.4 and below)"},
    "3": {"name": "NeoForge", "desc": "Modern Forge fork (1.20.5+)"},
    "4": {"name": "Fabric", "desc": "Lightweight mod loader"},
    "5": {"name": "Paper", "desc": "High-performance Spigot fork"},
    "6": {"name": "Spigot", "desc": "Bukkit fork with optimizations"},
    "7": {"name": "Bukkit", "desc": "Original plugin server"},
    "8": {"name": "Purpur", "desc": "Paper fork with more features"},
}

for key, value in server_types.items():
    print(f"  {key}. {value['name']:<10} - {value['desc']}")
print("=" * 35)

server_type_choice = input("Choose server type (1-8): ")

if server_type_choice not in server_types:
    print("Invalid choice! Defaulting to Vanilla.")
    server_type_choice = "1"

server_type = server_types[server_type_choice]["name"]
print(f"\nSelected: {server_type}\n")

print("="*20)
snapshow = input("Show Snapshot ? [y/n] ").lower()

if snapshow == "y":
    versiontype = ["release","snapshot"]
else:
    versiontype = ["release"]

how_much = input("how much of the version list(for all enter): ")

if how_much == "":
    how_much = 100000

print("Loading versions...")
url = "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"
try:
    data = json.loads(urllib.request.urlopen(url).read().decode())
except :
    print(f"Error in catching versions ")
    input("Press Enter to exit...")
    sys.exit()

versions = [v for v in data["versions"] if v["type"] in versiontype][:int(how_much)]

print("\n" + "=" * 35)
print("    Minecraft Java Versions")
print("=" * 35)
for i, v in enumerate(versions, 1):
    print(f"  {i}. {v['id']}")
print("=" * 35)
print("  0 = Exit")
print("=" * 35)

selected = None
while True:
    try:
        choice = input("Choose: ")
        choice = int(choice)
        
        if choice == 0:
            print("Exiting...")
            sys.exit()
        elif 1 <= choice <= len(versions):
            selected = versions[choice - 1]
            print(f"\nSelected: {selected['id']}")
            break
        else:
            print(f"Enter a number between 1 and {len(versions)}!")
    except ValueError:
        print("Enter a valid number!")

def show_progress(block_num, block_size, total_size):
    if total_size > 0:
        downloaded = block_num * block_size
        percent = min(100, int(downloaded * 100 / total_size))
        filled = int(30 * downloaded / total_size)
        bar = "=" * filled + " " * (30 - filled)
        print(f"\r  [{bar}] {percent}%", end="", flush=True)
        if percent >= 100:
            print()

def download_vanilla(version_id, version_folder):
    print("\nGetting download link...")
    try:
        version_data = json.loads(urllib.request.urlopen(selected["url"]).read().decode())
        download_url = version_data["downloads"]["server"]["url"]
        
        print(f"Downloading Vanilla {version_id}...")
        urllib.request.urlretrieve(download_url, "server.jar", reporthook=show_progress)
        print("Vanilla server downloaded!")
    except Exception as e:
        print(f"Error downloading Vanilla: {e}")
        input("Press Enter to exit...")
        sys.exit()

def download_forge(version_id, version_folder):
    print(f"\nDownloading Forge for {version_id}...")
    
    try:
        forge_url = f"https://files.minecraftforge.net/net/minecraftforge/forge/index_{version_id}.json"
        forge_data = json.loads(urllib.request.urlopen(forge_url).read().decode())
        latest = forge_data.get("latest", {}).get("latest", "latest")
        download_url = forge_data["versions"][latest]["downloads"]["installer"]["url"]
        
        print("Downloading Forge installer...")
        urllib.request.urlretrieve(download_url, "forge-installer.jar", reporthook=show_progress)
        
        print("\nInstalling Forge...")
        subprocess.run(["java", "-jar", "forge-installer.jar", "--installServer"], check=True)
        
        os.remove("forge-installer.jar")
        print("Forge installed successfully!")
    except Exception as e:
        print(f"Error downloading Forge: {e}")
        input("Press Enter to exit...")
        sys.exit()

def download_neoforge(version_id, version_folder):
    print(f"\nDownloading NeoForge for {version_id}...")
    
    try:
        # تلاش با API جدید NeoForge
        neoforge_url = f"https://api.neoforged.net/api/v1/versions/{version_id}"
        data = json.loads(urllib.request.urlopen(neoforge_url).read().decode())
        
        if data and "versions" in data and len(data["versions"]) > 0:
            latest = data["versions"][0]
            download_url = f"https://github.com/neoforged/NeoForge/releases/download/{latest}/neoforge-{latest}-installer.jar"
            
            print("Downloading NeoForge installer...")
            urllib.request.urlretrieve(download_url, "neoforge-installer.jar", reporthook=show_progress)
            
            print("\nInstalling NeoForge...")
            subprocess.run(["java", "-jar", "neoforge-installer.jar", "--installServer"], check=True)
            
            os.remove("neoforge-installer.jar")
            print("NeoForge installed successfully!")
        else:
            print("No NeoForge version found for this Minecraft version!")
            input("Press Enter to exit...")
            sys.exit()
            
    except Exception as e:
        print(f"Error downloading NeoForge: {e}")
        print("Make sure you have internet connection and the version is supported by NeoForge (1.20.5+)")
        input("Press Enter to exit...")
        sys.exit()

def download_fabric(version_id, version_folder):
    print(f"\nDownloading Fabric for {version_id}...")
    
    try:
        installer_url = "https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.1/fabric-installer-1.0.1.jar"
        
        print("Downloading Fabric installer...")
        urllib.request.urlretrieve(installer_url, "fabric-installer.jar", reporthook=show_progress)
        
        print("\nInstalling Fabric...")
        subprocess.run(["java", "-jar", "fabric-installer.jar", "server", "-mcversion", version_id, "-downloadMinecraft"], check=True)
        
        os.remove("fabric-installer.jar")
        print("Fabric installed successfully!")
    except Exception as e:
        print(f"Error downloading Fabric: {e}")
        input("Press Enter to exit...")
        sys.exit()

def download_paper(version_id, version_folder):
    print(f"\nDownloading Paper for {version_id}...")
    
    try:
        paper_url = f"https://api.papermc.io/v2/projects/paper/versions/{version_id}/builds"
        data = json.loads(urllib.request.urlopen(paper_url).read().decode())
        latest_build = data["builds"][-1]
        build_number = latest_build["build"]
        
        download_url = f"https://api.papermc.io/v2/projects/paper/versions/{version_id}/builds/{build_number}/downloads/paper-{version_id}-{build_number}.jar"
        
        print(f"Downloading Paper {version_id} build {build_number}...")
        urllib.request.urlretrieve(download_url, "server.jar", reporthook=show_progress)
        print("Paper server downloaded!")
    except Exception as e:
        print(f"Error downloading Paper: {e}")
        input("Press Enter to exit...")
        sys.exit()

def download_spigot(version_id, version_folder):
    print(f"\nDownloading Spigot for {version_id}...")
    
    try:
        print("Downloading BuildTools...")
        buildtools_url = "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"
        urllib.request.urlretrieve(buildtools_url, "BuildTools.jar", reporthook=show_progress)
        
        print("\nBuilding Spigot (this may take a while)...")
        subprocess.run(["java", "-jar", "BuildTools.jar", "--rev", version_id], check=True)
        
        spigot_jar = f"spigot-{version_id}.jar"
        if os.path.exists(spigot_jar):
            os.rename(spigot_jar, "server.jar")
        
        os.remove("BuildTools.jar")
        print("Spigot installed successfully!")
    except Exception as e:
        print(f"Error downloading Spigot: {e}")
        input("Press Enter to exit...")
        sys.exit()

def download_purpur(version_id, version_folder):
    print(f"\nDownloading Purpur for {version_id}...")
    
    try:
        purpur_url = f"https://api.purpurmc.org/v2/purpur/{version_id}"
        data = json.loads(urllib.request.urlopen(purpur_url).read().decode())
        latest_build = data["builds"]["latest"]
        
        download_url = f"https://api.purpurmc.org/v2/purpur/{version_id}/{latest_build}/download"
        
        print(f"Downloading Purpur {version_id} build {latest_build}...")
        urllib.request.urlretrieve(download_url, "server.jar", reporthook=show_progress)
        print("Purpur server downloaded!")
    except Exception as e:
        print(f"Error downloading Purpur: {e}")
        input("Press Enter to exit...")
        sys.exit()

def download_bukkit(version_id, version_folder):
    print(f"\nDownloading Bukkit for {version_id}...")
    download_vanilla(version_id, version_folder)

if selected:
    current_folder = os.getcwd()
    version_folder = os.path.join(current_folder, f"{server_name}_{server_type}_{selected['id']}")
    os.makedirs(version_folder, exist_ok=True)
    os.chdir(version_folder)
    
    download_functions = {
        "Vanilla": download_vanilla,
        "Forge": download_forge,
        "NeoForge": download_neoforge,
        "Fabric": download_fabric,
        "Paper": download_paper,
        "Spigot": download_spigot,
        "Bukkit": download_bukkit,
        "Purpur": download_purpur
    }
    
    download_func = download_functions.get(server_type, download_vanilla)
    download_func(selected["id"], version_folder)
    
    ram = input("\nHow much RAM for server? (2G, 4G ..): ")

    def create_start_bat():
        ramloc = ram if ram else "2G"
        
        jar_file = "server.jar"
        if server_type == "Forge":
            for file in os.listdir():
                if file.startswith("forge-") and file.endswith("-universal.jar"):
                    jar_file = file
                    break
        elif server_type == "NeoForge":
            for file in os.listdir():
                if file.startswith("neoforge-") and file.endswith("-universal.jar"):
                    jar_file = file
                    break
        elif server_type == "Fabric":
            for file in os.listdir():
                if file.startswith("fabric-server-launch.jar"):
                    jar_file = file
                    break

        bat_content = f'''@echo off
title {server_name}_{server_type}_{selected['id']}
echo ========================================
echo   Starting {server_type} Server
echo   Name: {server_name}
echo   Version: {selected['id']}
echo   RAM: {ramloc}
echo ========================================
java -Xmx{ramloc} -Xms{ramloc} -jar {jar_file} nogui
pause
'''
        
        with open("start.bat", "w") as f:
            f.write(bat_content)
        
        print(f"\nstart.bat created in: {os.getcwd()}")
        return os.getcwd()
    
    create_start_bat()

    def accept_eula():
        try:
            os.chdir(version_folder)
            with open("eula.txt", "w") as f:
                f.write("eula=true\n")
            print("EULA accepted automatically")
        except Exception as e:
                print(f"Failed to accept eula: {e}")
    def set_server_setting():
        print("Set server setting")
        try :
            os.chdir(version_folder)
            with open("server.properties","w") as f:
                f.write(f"max-players={maximam_player}\n")
                f.write(f"gamemode={gamemode}\n")
                f.write(f"difficulty={difficulty}\n")
                f.write(f"hardcore={hardcore}\n")
                f.write(f"level-seed={level_seed}\n")
                f.write(f"online-mode={online_mode}\n")
                f.write(f"view-distance={view_distance}")
                f.write(f"simulation-distance={simulation_distance}")
                f.write(f"motd=A Minecraft Server  /by FmSV")
        except Exception as e:
            print(f"Error in set server setting {e}")
    
    def fmsv_file_create():
        os.chdir(version_folder)
        with open("fmsv.fmsv","w") as f:
            f.write(" /$$$$$$$$             /$$$$$$  /$$    /$$\n")
            f.write("| $$_____/            /$$__  $$| $$   | $$\n")
            f.write("| $$    /$$$$$$/$$$$ | $$  \__/| $$   | $$\n")
            f.write("| $$$$$| $$_  $$_  $$|  $$$$$$ |  $$ / $$/\n")
            f.write("| $$__/| $$ \ $$ \ $$ \____  $$ \  $$ $$/ \n")
            f.write("| $$   | $$ | $$ | $$ /$$  \ $$  \  $$$/  \n")
            f.write("| $$   | $$ | $$ | $$|  $$$$$$/   \  $/   \n")
            f.write("|__/   |__/ |__/ |__/ \______/     \_/    \n")
            f.write("                                     by zaw \n\n")
            f.write(f"Name: {server_name}")
            f.write(f"Type: {server_type}\n")
            f.write(f"Version: {selected['id']}\n\n")
            f.write(f"Server fmSV setting :\n\n")
            f.write(f"max-players={maximam_player}\n")
            f.write(f"gamemode={gamemode}\n")
            f.write(f"difficulty={difficulty}\n")
            f.write(f"hardcore={hardcore}\n")
            f.write(f"level-seed={level_seed}\n")
            f.write(f"online-mode={online_mode}\n")
            f.write(f"view-distance={view_distance}\n")
            f.write(f"simulation-distance={simulation_distance}\n")
            f.write(f"motd=A Minecraft Server  /by FmSV")

    print("="*20,"\n")
    print(f"{server_name}\n"
          f"Type: {server_type}\n"
          f"Version: {selected['id']}\n"
          f"RAM: {ram if ram else '2G'}\n"
          f"Directory: {version_folder}\n")
    print("="*20)
    
    if input(f"Do you want to Run {server_name} Now? [y/n] ").lower() == "n":
        accept_eula()
        set_server_setting()
        fmsv_file_create()
        print("You can run start.bat to run the server")
        input("Press enter to exit ...")
    else:
        accept_eula()
        set_server_setting()
        fmsv_file_create()
        os.chdir(version_folder)
        subprocess.run(["start", "start.bat"], shell=True)