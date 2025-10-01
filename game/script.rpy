screen chapter_title(title):
    modal False
    zorder 100
    add "#000000"
    
    vbox:
        align (0.3, 0.5)  # 靠左一点，垂直居中
        spacing 25  # 增加间距
        
        text title:
            size 72
            color "#fcfcfc"
            outlines [(2, "#000000")]
            xalign 0.0  # 文字左对齐
            yoffset -20


label op:
    $ _game_menu_screen = None  # 禁用菜单
    $ renpy.block_rollback()    # 禁用回退
    $ renpy.movie_start_fullscreen("video/op.webm")
    $ renpy.pause(112.0, hard=True)
    $ _game_menu_screen = "game_menu"  # 恢复菜单
    # 回退功能会自动恢复
    menu:
        "直接开始吧":
            "刚才的是别的作品的"
            "好吧其实还参考了别的，不只这个"
            menu:
                "直接开始本作吧":
                    jump prologue

label start:
    menu:
        "看看参考文献":
            "参考了挺多东西的其实"
            "比如说BGM啊，剧情设计啊，场景啊"
            "不过参考文献的作画挺逆天的就是了"
            menu:
                "看看参考文献的OP吧":
                    jump op
                "没什么好看的":
                    menu:
                        "直接开始本作吧":
                            jump prologue
        "直接开始吧":
            jump prologue

