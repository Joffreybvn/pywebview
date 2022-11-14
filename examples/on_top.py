import webview
import time

"""
This example demonstrates how to create a topmost webview window.
"""

def deactivate(window):
    #window starts as on top of and reverts back to normal after 20 seconds
    time.sleep(20)
    window.on_top = False
    window.load_html("<h1>This window is no longer on top of other windows</h1>")


if __name__ == '__main__':
    # Create webview window that stays on top of, all other windows
    window = webview.create_window('Topmost window', html="<h1>This window is on top of other windows</h1>",
                          on_top=True)
    webview.start(deactivate, window)
