# Anything that needs fixing

## qBittorrent incoming connections blocked by MacOS firewall

- Open terminal
-

```Terminal
sudo codesign --force --deep --sign - /Applications/qbittorrent.app
sudo codesign -dvvvv /Applications/qbittorrent.app
sudo codesign --verify -vv  /Applications/qbittorrent.app
```
