# 要爬取的女优（演员）ID列表

ids = [
    "ayuf2",  # 園田みおん
    "aetua",  # 冬愛ことね
    "ay4sm",  # 初川南
    "ayua",  # JULIA
    "aaiqq",  # 水端あさみ
    "aanv6",  # 歌野こころ
    "aycfw",  # 辻本杏
    "j4wq",  # 白石もも
    "aacqo",  # 東条実澪
    "azda2",  # 愛沢有紗
    "affam",  # 本田もも
    "abbeg",  # 栗宮ふたば
    "aacfw",  # 佐野ゆま
    "ayad4",  # 饭冈加奈子
    "aeqqu",  # 逢見リカ
    "ci",  # 一ノ瀬アメリ
    "pyvq",  # 佳山三花
    "azcvi",  # 泷泽萝拉
    "afkv4",  # 斎藤あみり
    "abgvq",  # 小花のん
    "aadt6",  # 小鳥遊もえ
    'aaoa4',  # 小湊よつ葉
    'abbds',  # 山手梨愛
    'ae3so',  # 本庄鈴
    "ae5q6",  # 楓カレン
    'aebe6',  # 七沢みあ
    'aeceq',  # 山岸逢花
    "aabdo",  # 山岸あや花
    'aejdi',  # 明里つむぎ
    'aemco',  # 桜空もも
    'aeyaq',  # 河北彩花
    'afgda',  # 相沢みなみ
    'afnqu',  # 坂道みる
    'aygqk',  # 夏目彩春
    'azjsc',  # 松嶋真麻
    "azhfk",  # 星野景子
    "aaivs",  # 神木麗
    "aalqo",  # 坂井なるは
    "abaew",  # 石川澪
    "abdaa",  # 楓芙愛
    "ae4ee",  # 星宮一花
    "aentc",  # 美谷朱里
    "aaouy",  # 新有菜,新ありな 橋本ありな
    "onba",  # 希志あいの
    "aygdk",  # 希島あいり
    "afib2",  # 水森翠
]

ids = list(set(ids))

# 爬取到第x页的数据，默认-1表爬取所有
recent = -1

# 爬虫名字
actor_spidername = "actors_spider"
works_spidername = "works_spider"
magnet_spidername = "magnet_spider"

# 磁力链接的文件大小区间
# 设置磁力链接文件大小的区间，单位为KB
magnet_file = [2, 10]


def get_actor_ids():
    """
    获取要爬取的女优（演员）ID列表。

    Returns:
        list: 包含女优ID的列表。
    """
    return ids


def get_recent_pages():
    """
    获取爬取的最近页数。

    Returns:
        int: 爬取的最近页数，默认为2。
    """
    return recent


def get_spider_names():
    """
    获取爬虫的名字列表。

    Returns:
        tuple: 包含三个爬虫名字的元组。
    """
    return actor_spidername, works_spidername, magnet_spidername


def get_magnet_file_size_range():
    """
    获取磁力链接文件大小的区间。

    Returns:
        list: 包含文件大小区间的列表
    """
    return magnet_file


if __name__ == "__main__":
    # 调用重新创建表的函数
    pass
