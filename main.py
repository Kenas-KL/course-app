import asynckivy
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivymd.uix.progressindicator import MDCircularProgressIndicator
from kivy.metrics import dp
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogIcon,MDDialogContentContainer, MDDialogSupportingText
from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDList
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivy.lang import Builder
import sqlite3
import webbrowser

Builder.load_string("""
<Main_Screen>:
    md_bg_color: self.theme_cls.backgroundColor
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        type: "medium"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        MDTopAppBarLeadingButtonContainer:
                            MDActionTopAppBarButton:
                                icon: "menu"
                                style: "tonal"
                                on_release: nav_drawer.set_state("toggle")
                        MDTopAppBarTitle:
                            text: "Course App Academia"
                            pos_hint: {"center_x": .5}
                        MDTopAppBarTrailingButtonContainer:
                            MDActionTopAppBarButton:
                                icon: "chat-question-outline"
                                on_press: root.manager.current = 'evaluation_'


#----------------------------------- body ---------------------------------
                    ScrollView:
                        MDList:
                            id: list_parts_course
#---------------------------------------------------------------------------

        MDNavigationDrawer:
            id: nav_drawer
            orientation: 'vertical'
            radius: 0, dp(16), dp(16), 0
            size_hint_x: None
            width: "260dp"
            MDNavigationDrawerMenu:
                MDNavigationDrawerLabel:
                    text: "SPC_Academia"
                    bold: True
                MDNavigationDrawerDivider:
                MDNavigationDrawerItem:
                    on_release: app.to_Facebook()
                    MDNavigationDrawerItemLeadingIcon:
                        icon: "facebook"
                    MDNavigationDrawerItemText:
                        text: "Facebook"
                MDNavigationDrawerItem:
                    on_release: app.to_WhatsApp()
                    MDNavigationDrawerItemLeadingIcon:
                        icon: "whatsapp"
                    MDNavigationDrawerItemText:
                        text: "WhatsApp"
                MDNavigationDrawerItem:
                    on_release: root.manager.current = 'mail_'
                    MDNavigationDrawerItemLeadingIcon:
                        icon: "gmail"
                    MDNavigationDrawerItemText:
                        text: "Mail"
            MDNavigationDrawerMenu:
                MDNavigationDrawerLabel:
                    text: "Autres"
                    bold: True
                MDNavigationDrawerDivider:
                MDNavigationDrawerItem:
                    on_release: app.theme_changed()
                    MDNavigationDrawerItemLeadingIcon:
                        icon: "theme-light-dark"
                    MDNavigationDrawerItemText:
                        text: "Theme"
                MDNavigationDrawerItem:
                    on_release: root.manager.current = 'about_'
                    MDNavigationDrawerItemLeadingIcon:
                        icon: "book-information-variant"
                    MDNavigationDrawerItemText:
                        text: "Apropos"



<Mail_Screen>:
    md_bg_color: self.theme_cls.backgroundColor
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            type: "small"
            MDTopAppBarLeadingButtonContainer:
                MDActionTopAppBarButton:
                    icon: "backburger"
                    on_release: root.manager.current = 'main_'
            MDTopAppBarTitle:
                text: "Mail"

        MDBoxLayout:
            padding: [dp(7),dp(10),dp(7),dp(10)]
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: [5,0,5,0]
                canvas.before:
                    Color:
                        rgba: .5,.5,.5,.5
                    RoundedRectangle:
                        pos: self.width/2 - 150, self.height/2 - 110
                        size: 300, 300
                        source: 'L3.png'
                        radius: [5,5,5,5]
                MDLabel:
                    text: "Ecrivez nous 'info@spc-enterprise.net'"
                    bold: True
                MDTextField:
                    mode: "filled"
                    MDTextFieldLeadingIcon:
                        icon: "email-box"
                    MDTextFieldHintText:
                        text: "Sujet du Message"
                        id: subject
                MDTextField:
                    mode: "filled"
                    MDTextFieldLeadingIcon:
                        icon: "email-newsletter"
                    MDTextFieldHintText:
                        text: "Coprs du message"
                        id: mail
                MDIconButton:
                    icon: 'send'
                    on_release: root.send_mail()
                MDLabel:
                    text: "Ecrivez nous ici sur cet Ecran puis la prochaine fois de puis votre boite Mail. Merci!"
                    halign: "justify"

<EvaluationScreen>:
    md_bg_color: self.theme_cls.backgroundColor
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            type: "small"
            MDTopAppBarLeadingButtonContainer:
                MDActionTopAppBarButton:
                    icon: "backburger"
                    on_release: root.manager.current = 'main_'
            MDTopAppBarTitle:
                text: "Evaluez vous ..."
        MDBoxLayout:
            padding: [dp(7),dp(10),dp(7),dp(10)]
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: [5,0,5,0]
                canvas.before:
                    Color:
                        rgba: .5,.5,.5,.5
                    RoundedRectangle:
                        pos: self.width/2 - 150, self.height/2 - 110
                        size: 300, 300
                        source: 'L3.png'
                        radius: [5,5,5,5]
                MDBoxLayout:
                    size_hint_y: None
                    height: "50dp"
                    padding: [dp(10),0,dp(10),0]
                    spacing: dp(7)
                    canvas.before:
                        Color:
                            rgba: 0,0,0,.2
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [dp(15),dp(15),dp(15),dp(15)]
                    MDLabel:
                        text: 'Score: 0'
                        bold: True
                        halign: 'left'
                    MDLabel:
                        text: 'Meilleur Score: 0'
                        bold: True
                        halign: 'right'
                MDBoxLayout:


<Reading_Screen>:
    md_bg_color: self.theme_cls.backgroundColor
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            type: "small"
            id: title_
            MDTopAppBarLeadingButtonContainer:
                MDActionTopAppBarButton:
                    icon: "backburger"
                    on_press: root.manager.current = 'main_'
                    on_release: root.clear_scroller()
            MDTopAppBarTitle:
                id: title_
                size_hint_x: None
                width: "100dp"
        MDBoxLayout:
            padding: [dp(7),dp(10),dp(7),dp(10)]
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: [5,0,5,0]
                canvas.before:
                    Color:
                        rgba: .5,.5,.5,.3
                    RoundedRectangle:
                        pos: self.width/2 - 150, self.height/2 - 110
                        size: 300, 300
                        source: 'L3.png'
                        radius: [5,5,5,5]
                RelativeLayout:
                    ScrollView:
                        id: scroller
                        do_scroll_x: True
                    RelativeLayout:
                        id: load




<AboutScreen>:
    md_bg_color: self.theme_cls.backgroundColor
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: .5,.5,.5,.5
            RoundedRectangle:
                pos: self.width/2 - 150, self.height/2 - 110
                size: 300, 300
                source: 'L3.png'
                radius: [5,5,5,5]
        MDTopAppBar:
            type: "small"
            MDTopAppBarLeadingButtonContainer:
                MDActionTopAppBarButton:
                    icon: "backburger"
                    on_release: root.manager.current = 'main_'
            MDTopAppBarTitle:
                text: "Apropos"
        BoxLayout:
""")


Window.size = (320,600)
Window.left = 1040
Window.top = 90


def check_user():
    conn = sqlite3.connect('user_data_base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM User")
    result = cursor.fetchone()[0]
    conn.close()
    return result == 0


class Main_Screen(MDScreen):

    stack = StackLayout()
    title_ = ""
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        connection = sqlite3.connect("user_data_base.db")
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_code TEXT NOT NULL,
            level INT NOT NULL,
            theme TEXT NOT NULL
            )
                ''')
        connection.commit()
        connection.close()

        self.call()

    def call(self):
        async def load_part_course():
            self.parts_course = [
                "1. FONDAMENTAUX DES RESEAUX",
                "2. PROTOCOLE IPV4",
                "3. PROTOCOLE IPV6",
                "4. ROUTAGE ET ROUTEURS",
                "5. SERVICES D'INFRASTRUCTURE",
                "6. COMMUNICATION INTERNET",
                "7. LE CABLAGE",
                "8. LA TECHNOLOGIE VLAN",
                "9. LA TECHNOLOGIE WLAN",
                "10. INTRODUCTION A LA SECURITE DES SYSTEMES D'INFORMATION",
                "11. GESTION D’INFRASTRUCTURE"
            ]
            for _ in range(len(self.parts_course)):
                await asynckivy.sleep(0)
                item = MDListItem(
                    MDListItemHeadlineText(
                        text=self.parts_course[_],font_name='Poppins-Regular.ttf',bold=False
                    ),id = self.parts_course[_]
                )
                item.bind(on_release= self.cal)
                self.ids.list_parts_course.add_widget(item)

        Clock.schedule_once(lambda x: asynckivy.start(load_part_course()))


    def cal(self,instance):
        title = instance.id
        CourseApp.screen_manager.current = 'read_'
        CourseApp.screen_manager.get_screen('read_').set_title(title)

    def open_dialog(self):
        self.user_code = MDTextField(
            MDTextFieldHintText(
                text="Votre Code d'étude"
            ),
        )

        self.dialog = MDDialog(
            MDDialogIcon(
              icon='menu'
            ),
            MDDialogHeadlineText(
                text="Créer un Compte",
                halign="left"
            ),
            MDDialogSupportingText(
                text="Contactez l'equipe Soft Planet Company pour "
                     "Votre Inscription et obtenir ainsi votre compte d'etude"
                     "",
            ),
            MDDialogContentContainer(
                self.user_code,
                spacing=dp(5)
            ),
            MDButton(
                MDButtonText(text="Créer"),
                style="text",
                on_release=self.create_a_account,
            ),
            spacing="8dp",
            padding=[0, 0, 0, 5]

            )

        self.dialog.open()

    def create_a_account(self,instance):
        conn = sqlite3.connect('user_data_base.db')
        cursor = conn.cursor()
        code = self.user_code.text
        if code == "":
            return
        cursor.execute(f"INSERT INTO User (user_code,level,theme) VALUES(?,?,?)",(1,code,"Light"))
        conn.commit()
        conn.close()
        self.load_part_course()
        self.dialog.dismiss()


class Mail_Screen(MDScreen):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def send_mail(self):
        mail = self.ids.mail.text
        destinataire = "info@spc-enterprise.net"
        subject=self.ids.subject.text

        url = f"mailto:{destinataire}?subject={subject}&body={mail} "
        webbrowser.open(url)

class ContenuCours(BoxLayout):
    def __init__(self, content, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'  # Ajustez l'orientation
        self.spacing = dp(15)  # Espacement entre les éléments
        self.size_hint_y = None


        if content.startswith('Image:'):
            path_image = content.split(':')[1].strip()
            img = Image(source=path_image, size_hint=(None,None), width=300,height=300)
            self.add_widget(img)
        else:
            label_ = MDLabel(text=content, halign='justify',size_hint_y=None,font_name='Poppins-Regular.ttf')
            # Ajoutez des propriétés au label si nécessaire
            label_.font_size = 16

            self.add_widget(label_)

class Reading_Screen(MDScreen):
    _title = ""
    break_ = False
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def load_(self):
        self.ids.load.add_widget(
            MDCircularProgressIndicator(
                size_hint=(None, None),
                size=(dp(40), dp(48)),
                pos_hint={'center_x': .5, 'center_y': .6})
        )
        self.ids.load.add_widget(
            MDLabel(
                text="Chargement...",
                halign='center',
                pos_hint={'center_x': .5, 'center_y': .5}
            )
        )

    def set_title(self,title):
        self.load_()
        self.break_ = False
        async def call():
            self.ids.scroller.clear_widgets()
            self.ids.title_.text = (title[3:25]+" ...").lower()
            layout = MDList(size_hint_y=None)
            with open(f"""require\\{title}.txt""", "r", encoding="utf-8") as f:
                for line in f:
                    if self.break_:
                        break
                        # pass
                    await asynckivy.sleep(0)
                    content_ = ContenuCours(line)
                    layout.add_widget(content_)
            self.ids.load.clear_widgets()
            self.ids.scroller.add_widget(layout)
        Clock.schedule_once(lambda x: asynckivy.start(call()))


    def clear_scroller(self):
        self.break_= True
        self.ids.scroller.clear_widgets()

class AboutScreen(MDScreen):
    account_created = True
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


class EvaluationScreen(MDScreen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


class Screen_Manager_(MDScreenManager):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class CourseApp(MDApp):

    screen_manager = None
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Darkgray'

        CourseApp.screen_manager = Screen_Manager_()

        list_screens = [
            Main_Screen(name='main_'),
            Mail_Screen(name='mail_'),
            Reading_Screen(name='read_'),
            AboutScreen(name='about_'),
            EvaluationScreen(name='evaluation_')
        ]

        for screen in list_screens:
            CourseApp.screen_manager.add_widget(screen)

        return CourseApp.screen_manager

    def theme_changed(self):
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'

    def to_WhatsApp(self):
        webbrowser.open('whatsapp://send?phone=+243896667599&text=Bonjour Soft-Planet-Enterprise%20de%20mon%2app')

    def to_Facebook(self):
        webbrowser.open('https://www.facebook.com/profile.php?id=100067415259295')


if __name__ == '__main__':
    CourseApp().run()

