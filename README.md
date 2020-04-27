# Keypirinha Plugin: WinSys

A useful [Keypirinha](http://keypirinha.com) plugin with common system and shell commands for Windows 10.

Provides  keywords for system command features such as shutdown, locking the computer,
emptying the recycling bin, as well as shell commands to open the new Windows 10
settings panels and other useful explorer folders (e.g. AppData), etc.


## Download

Downloads can be found at the releases page:
https://github.com/kvnxiao/keypirinha-winsys/releases


## Install

Download the `WinSys.keypirinha-package` file from the release page shown above
and move it to your `InstalledPackage` folder located at:

* `Keypirinha\portable\Profile\InstalledPackages` in **Portable mode**
* **Or** `%APPDATA%\Keypirinha\InstalledPackages` in **Installed mode** (the
  final path would look like
  `C:\Users\%USERNAME%\AppData\Roaming\Keypirinha\InstalledPackages`)


## Usage

Type in a valid keyword to activate the corresponding function:

**System Actions**

|  Keyword |  Description |
|----------|--------------|
|Lock|Locks the computer and brings you to the lock screen|
|Shutdown|Shuts down the computer|
|Restart|Restarts the computer|
|Hibernate|Puts the computer into hibernate mode|
|Sleep|Puts the computer to sleep|
|Logout|Logs out the current user|
|Empty Recycle Bin|Empty the Recycle Bin|

**Explorer Shell Shortcuts**

|  Keyword |  Description |
|----------|--------------|
|Recycle Bin|Opens the Recycle Bin folder|
|AppData|Opens the user's AppData folder|
|LocalAppData|Opens the user's AppData/Local folder|
|LocalLowAppData|Opens the user's AppData/LocalLow folder|
|Desktop|Opens the user's Desktop folder|
|Downloads|Opens the user's Downloads folder|
|Documents|Opens the user's Documents folder|
|Startup|Opens the user's Startup folder|

**Windows Settings Shortcuts (Win10 only)**

|  Keyword |  Description |
|----------|--------------|
|Settings Panel|Opens the Settings application|
|System Settings|Opens the system settings panel|
|Display|Opens the display settings panel|
|Notification & Actions|Opens the notification & actions panel|
|Battery|Opens the battery settings panel|
|Bluetooth & other devices|Opens the Bluetooth & other devices panel|
|Printers & Scanners|Opens the printers & scanners panel|
|Phone & mobile devices|Opens the mobile devices panel|
|Background|Opens the background personalization panel|
|Lock screen|Opens the lock screen personalization panel|
|Date & Time|Opens the date & time panel|
|Region & Language|Opens the region & language panel|
|Accounts|Opens the accounts, email, sync panel|
|Update & Security|Opens the update & security panel|


## Change Log

**1.0.1**
- Added `Startup` keyword as a shell command to open the user's startup menu folder

**1.0.0 - Initial Release**
 - Initial release of the plugin which contains system actions,
  explorer shell shortcuts, and windows settings shortcuts for Windows 10


## License

This package is distributed under the terms of the MIT license.


## Credits

Thanks to polyvertex for Keypirinha.

This plugin was inspired by [psistorm's keypirinha-systemcommands](https://github.com/psistorm/keypirinha-systemcommands).


## Contribute

Feel free to submit a pull request that you may see fit to help improve this plugin. All contributions are welcome!
