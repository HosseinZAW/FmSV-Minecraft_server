

# FmSV - Minecraft dedicated Server

> **Fastest & easiest way to run a Minecraft server on Windows and {Linux soon...}**

--
[FA_README](https://github.com/HosseinZAW/FmSV/blob/main/FA_README.md) اموزش فارسی
--

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20(Soon)-lightgrey)

---

## 📋 Table of Contents
- [Features](#-features)
- [Supported Server Types](#-supported-server-types)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
- [Configuration](#-configuration)
- [System Requirements](#-system-requirements)
- [License](#-license)

---

## ✨ Features
- 🚀 **One-click server setup** - No manual configuration needed
- 📦 **8 different server types** - Vanilla, Forge, NeoForge, Fabric, Paper, Spigot, Bukkit, Purpur
- 🔄 **Auto Java installation** - Installs Java 17 if not present
- 🎮 **Interactive version selection** - Browse and choose any Minecraft version
- ⚙️ **Automatic configuration** - Generates `server.properties` and `eula.txt`
- 📝 **Server info tracking** - Creates `.fmsv` metadata file
- 🖥️ **Cross-platform** - Works on Windows and {Linux soon...}

---

## 🎯 Supported Server Types

| # | Server Type | Description |
|---|-------------|-------------|
| 1 | **Vanilla** | Official Mojang server |
| 2 | **Forge** | Modded server (1.20.4 and below) |
| 3 | **NeoForge** | Modern Forge fork (1.20.5+) |
| 4 | **Fabric** | Lightweight mod loader |
| 5 | **Paper** | High-performance Spigot fork |
| 6 | **Spigot** | Bukkit fork with optimizations |
| 7 | **Bukkit** | Original plugin server |
| 8 | **Purpur** | Paper fork with more features |

---

## 📥 Installation

### Windows
1. Download `FmSV.exe` from the [releases page](https://github.com/Hosseinzaw/FmSV/releases)
2. Place the file in your desired directory
3. Double-click to run

### Linux
Soon...

---

## 🚀 How to Use

### Step 1: Run the Program
```bash
open FmSV_1.0.exe  # Windows
```

### Step 2: Configure Server Settings
You'll be prompted to enter:
- **Server name** - Your server's display name
- **Gamemode** - `survival` or `creative` (default: survival)
- **Max players** - Maximum players allowed (default: 20)
- **Difficulty** - `easy`, `normal`, or `hard` (default: normal)
- **Online mode** - `true`/`false` (default: true)
- **View distance** - Render distance in chunks (default: 10)
- **Simulation distance** - Simulation distance in chunks (default: 10)
- **Level seed** - World seed (optional)
- **Hardcore** - `true`/`false` (default: false)

### Step 3: Select Server Type
Choose from 8 available server types (1-8)

### Step 4: Choose Minecraft Version
- View all available versions
- Type the number corresponding to your desired version

### Step 5: Allocate RAM
Specify RAM amount (e.g., `2G`, `4G`, `8G`)

### Step 6: Launch!
- Choose to start the server immediately or later
- If later, run `start.bat` to start your server

---

## ⚙️ Configuration

### Generated Files
After setup, your server directory will contain:

```
📁 your_server_name_Type_Version/
├── server.jar              # Server executable
├── start.bat               # Startup script (Windows)
├── server.properties       # Server configuration
├── eula.txt                # EULA agreement (auto-accepted)
├── fmsv.fmsv              # Server metadata

```

### Server Properties
The following settings are automatically configured:
```properties
max-players=
gamemode=
difficulty=
hardcore=
level-seed=
online-mode=
view-distance=
simulation-distance=
```

---

## 💻 System Requirements

### Minimum Requirements
- **OS**: Windows 10/11 or Linux (Ubuntu 20.04+)
- **RAM**: 2GB minimum (4GB+ recommended)
- **Storage**: 1GB free space
- **Internet**: Required for downloading server files

### Java Requirements
- Java 17 or higher (auto-installed on Windows)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Credits
- **Developer**: ZAW


---


## 🔗 Links
- [GitHub Repository](https://github.com/HosseinZAW/FmSV)
- [Report Bug](https://github.com/HosseinZAW/FmSV/issues)
- [Request Feature](https://github.com/HosseinZAW/FmSV/issues)

---

> **⚠️ Disclaimer**: FmSV is not affiliated with Mojang Studios or Microsoft. Minecraft is a trademark of Mojang Studios.

---

<div align="center">
Made with ❤️ by ZAW
</div>
