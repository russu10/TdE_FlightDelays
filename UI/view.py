import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._page.title = "FlightDelays"
        self._page.vertical_alignment = ft.MainAxisAlignment.START

        # Titolo (opzionale)
        self._title = ft.Text("FlightDelays", style="headlineMedium", text_align="center")

        # Campo numero minimo compagnie
        self._min_companies = ft.TextField(label="# compagnie minimo", width=200)

        # Dropdown partenza e destinazione
        self._airport_origin = ft.Dropdown(label="Aeroporto di partenza", options=[], width=800)
        self._airport_dest = ft.Dropdown(label="Aeroporto destinazione", options=[], width=800)

        # Pulsanti
        self._analyze_button = ft.ElevatedButton("Analizza aeroporti", width=160,
                                                 on_click=self._controller.trovaAeroporti)
        self._test_button = ft.OutlinedButton("Test Connessione", width=160,
                                              on_click=self._controller.percorso)



        # Layout pulsanti
        self._button_row = ft.Row([self._analyze_button, self._test_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        # Layout finale
        self._page.add(
            self._title,
            ft.Row([self._min_companies], alignment=ft.MainAxisAlignment.START),
            ft.Row([self._airport_origin], alignment=ft.MainAxisAlignment.START),
            ft.Row([self._airport_dest], alignment=ft.MainAxisAlignment.START),
            self._button_row,

        )
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
