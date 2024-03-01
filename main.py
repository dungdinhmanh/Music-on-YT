from ytmusicapi import YTMusic
from flet import *
#from pages.mainpage import MainPage
def main(page: Page):
    container=Container(
        width=500,
        height=500,
        bgcorlor='red',
        border_radius=50
    )
    page.add(container)
app(target=main)