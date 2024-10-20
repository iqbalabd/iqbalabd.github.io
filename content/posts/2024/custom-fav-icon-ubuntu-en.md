Title: Custom Favicon for Scaled Steam Client on Ubuntu 22.04
Slug: custom-steam-favicon-scaling-ubuntu-2204
Lang: en
Date: 2024-10-20 21:30
Modified: 2024-10-20 21:30
Tags: ubuntu 22.04; favicon; desktop;
Status: published
Authors: Iqbal Abdullah
Summary: Create a custom Steam favicon with scaling for 4K monitors on Ubuntu 22.04.

Creating a custom favicon on Ubuntu 22.04 isn't as daunting as it might seem, especially when you're trying to address a specific issue like scaling with a 4K monitor. For instance, if you're using a Dell XPS 9310 and the Steam client appears too small, you can scale it by adding a parameter. Specifically, the `-forcedesktopscaling=X` parameter can be adjusted to your preference. In my case, setting it to `2.5` worked perfectly.

The challenge is ensuring the favicon uses this parameter when launching Steam. The solution is to create a custom desktop entry. Here’s how:

First, copy the existing Steam desktop file to your local applications directory:

```bash
$ cp /usr/share/applications/steam.desktop /home/$HOME/.local/share/applications
$ cd /home/$HOME/.local/share/applications
$ vi steam.desktop
```

Next, edit the file by adding the `-forcedesktopscaling="2.5"` parameter to each line that starts with `Exec=`. It should look something like this:

```
Exec=/usr/games/steam %U -forcedesktopscaling="2.5"
...
...
Exec=/usr/games/steam steam://url/SteamIDControlPage -forcedesktopscaling="2.5"
```

Finally, make the desktop file executable:

```bash
$ chmod a+x steam.desktop
```

Once you've done that, restart your system. This ensures that every time you launch Steam via the favicon, it uses the specified scaling. It's a simple yet effective way to customize your desktop environment to better suit your hardware.

---

References:

- [https://steamcommunity.com/groups/SteamClientBeta/discussions/0/3461605794225862173/?ctp=4](https://steamcommunity.com/groups/SteamClientBeta/discussions/0/3461605794225862173/?ctp=4)
- [https://askubuntu.com/questions/1026528/adding-custom-programs-to-favourites-of-ubuntu-dock/](https://askubuntu.com/questions/1026528/adding-custom-programs-to-favourites-of-ubuntu-dock/)
