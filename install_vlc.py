from pywinauto.application import Application

vlc = Application(backend="win32").start("vlc-3.exe")

vlc.InstallDialog.OKButton.wait('ready',timeout=30).click_input()
vlc.InstallDialog.NextButton.wait('ready', timeout=30).click_input()
vlc.InstallDialog.NextButton.wait('ready', timeout=30).click_input()
vlc.InstallDialog.NextButton.wait('ready', timeout=30).click_input()
vlc.InstallDialog.InstallButton.wait('ready', timeout=300).click_input()
vlc.InstallDialog.FinishButton.wait('ready', timeout=30).click_input()
