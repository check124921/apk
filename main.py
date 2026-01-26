from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
class HelloAIPyApp(App):
    def build(self):
        # 设置窗口标题和大小（简单美化）
        Window.title = "AiPy给老板的APK"
        Window.size = (300, 200)
        # 返回一个带彩虹色的标签（用Kivy默认颜色循环）
        return Label(
            text="老板好呀！😊\n这是AiPy做的APK～",
            halign="center",
            valign="middle",
            font_size="24sp",
            color=(0.2, 0.6, 1, 1)  # 温柔蓝
        )
if __name__ == "__main__":
    HelloAIPyApp().run()