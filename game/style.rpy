################################################################################
## 自定义样式定义
################################################################################

init offset = -1

## 自定义变换用于按钮动画效果
transform button_hover:
    on idle:
        ease 0.2 alpha 0.9 zoom 1.0
    on hover:
        ease 0.2 alpha 1.0 zoom 1.02

transform button_press:
    ease 0.1 zoom 0.98
    ease 0.1 zoom 1.0

## 自定义按钮样式
style custom_button is button:
    background Solid("#4a90e2")
    hover_background Solid("#66a3ff")
    selected_idle_background Solid("#357abd")
    selected_hover_background Solid("#4a90e2")
    padding (20, 12)
    margin (5, 3)

style custom_button_text is button_text:
    color "#ffffff"
    hover_color "#ffffff" 
    selected_color "#ffffff"
    text_align 0.5

## 选项按钮样式
style modern_choice_button is button:
    background Solid("#ffffff")
    hover_background Solid("#4a90e2")
    selected_idle_background Solid("#357abd") 
    selected_hover_background Solid("#4a90e2")
    padding (25, 15)
    margin (8, 5)
    # 添加边框效果
    insensitive_background Solid("#f8f9fa")

style modern_choice_button_text is button_text:
    color "#404040"
    hover_color "#ffffff"
    selected_color "#ffffff"
    insensitive_color "#6c757d"
    text_align 0.5
    size gui.text_size

## 导航按钮样式
style modern_navigation_button is button:
    background Solid("#4a90e2")
    hover_background Solid("#66a3ff")
    selected_idle_background Solid("#357abd")
    selected_hover_background Solid("#4a90e2")
    padding (25, 15)
    margin (8, 6)
    xminimum 220
    yminimum 55

style modern_navigation_button_text is button_text:
    color "#ffffff"
    hover_color "#ffffff"
    selected_color "#ffffff"
    text_align 0.5
    size 28

## 快捷按钮样式
style modern_quick_button is button:
    background Solid("#4a90e2e6")  # 90% opacity
    hover_background Solid("#4a90e2")
    selected_idle_background Solid("#357abd")
    selected_hover_background Solid("#4a90e2")
    padding (15, 8)
    margin (4, 3)
    xminimum 90
    yminimum 40

style modern_quick_button_text is button_text:
    color "#ffffff"
    hover_color "#ffffff"
    selected_color "#ffffff"
    text_align 0.5
    size gui.quick_button_text_size

## 存档按钮样式
style modern_slot_button is button:
    background Solid("#f8f9fa")
    hover_background Solid("#e9ecef")
    selected_idle_background Solid("#dee2e6")
    selected_hover_background Solid("#ced4da")
    padding (12, 10)
    margin (5, 5)

style modern_slot_button_text is button_text:
    color "#495057"
    hover_color "#212529"
    selected_color "#212529"

## 设置按钮样式
style modern_radio_button is button:
    background Solid("#f8f9fa")
    hover_background Solid("#e9ecef")
    selected_idle_background Solid("#4a90e2")
    selected_hover_background Solid("#357abd")
    padding (8, 6)
    margin (2, 2)

style modern_radio_button_text is button_text:
    color "#495057"
    hover_color "#212529"
    selected_color "#ffffff"

style modern_check_button is button:
    background Solid("#f8f9fa")
    hover_background Solid("#e9ecef")
    selected_idle_background Solid("#28a745")
    selected_hover_background Solid("#218838")
    padding (8, 6)
    margin (2, 2)

style modern_check_button_text is button_text:
    color "#495057"
    hover_color "#212529"
    selected_color "#ffffff"

## 确认按钮样式
style modern_confirm_button is button:
    background Solid("#dc3545")
    hover_background Solid("#c82333")
    selected_idle_background Solid("#bd2130")
    selected_hover_background Solid("#b21e2d")
    padding (15, 10)
    margin (5, 3)
    xminimum 120
    yminimum 40

style modern_confirm_button_text is button_text:
    color "#ffffff"
    hover_color "#ffffff"
    selected_color "#ffffff"
    text_align 0.5
    size 24

## 帮助按钮样式
style modern_help_button is button:
    background Solid("#6c757d")
    hover_background Solid("#5a6268")
    selected_idle_background Solid("#495057")
    selected_hover_background Solid("#5a6268")
    padding (12, 8)
    margin (3, 2)

style modern_help_button_text is button_text:
    color "#ffffff"
    hover_color "#ffffff"
    selected_color "#ffffff"

## 页面按钮样式
style modern_page_button is button:
    background Solid("#e9ecef")
    hover_background Solid("#4a90e2")
    selected_idle_background Solid("#357abd")
    selected_hover_background Solid("#4a90e2")
    padding (15, 8)
    margin (3, 2)

style modern_page_button_text is button_text:
    color "#495057"
    hover_color "#ffffff"
    selected_color "#ffffff"
    text_align 0.5
