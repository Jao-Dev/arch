config.load_autoconfig(False)


# File handling
config.set("fileselect.handler", "external")
config.set(
    "fileselect.single_file.command",
    ["kitty", "--class", "ranger,ranger", "-e", "ranger", "--choosefile", "{}"],
)
config.set(
    "fileselect.multiple_files.command",
    ["kitty", "--calss", "ranger,ranger", "-e", "ranger", "--choosefiles", "{}"],
)




# Home page
c.url.start_pages = ["https://8bitdash.com/dashboard"]

c.url.searchengines = {
        "DEFAULT": "https://duckduckgo.com/?q={}",
        "yt": "https://www.youtube.com/results?search_query={}",
        "acw": "https://man.archlinux.org/search?q={}",

}

# tema e afins
c.colors.webpage.darkmode.enabled = True


# adblock
c.content.blocking.enabled = True
c.content.blocking.method = "both"

c.content.blocking.adblock.lists = [
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-cookies.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-others.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
    "https://github.com/uBlockOrigin/uAssets/blob/master/filters/experimental.txt",
    "https://github.com/uBlockOrigin/uAssets/blob/master/filters/filters-general.txt",
    "https://github.com/uBlockOrigin/uAssets/blob/master/filters/filters-mobile.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
    "https://github.com/uBlockOrigin/uAssets/blob/master/filters/lan-block.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
    "https://github.com/uBlockOrigin/uAssets/blob/master/filters/privacy-removeparam.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/quick-fixes.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt",
    "https://github.com/uBlockOrigin/uAssets/blob/master/filters/ubo-link-shorteners.txt",
    "https://github.com/uBlockOrigin/uAssets/blob/master/filters/ubol-filters.txt",
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
    "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2022.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2023.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2024.txt",
    "https://github.com/uBlockOrigin/uAssets/blob/master/filters/filters-2025.txt",
    "https://github.com/uBlockOrigin/uAssets/blob/master/filters/filters-2026.txt",
]
