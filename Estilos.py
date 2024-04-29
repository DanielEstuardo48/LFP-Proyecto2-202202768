from tkinter import ttk

# Establecer el estilo de las pestañas
style = ttk.Style()
style.theme_create("Modern", parent="alt", settings={
    "TNotebook": {"configure": {"background": "#f0f0f0"}},
    "TNotebook.Tab": {
        "configure": {"padding": [10, 5], "background": "#e0e0e0"},
        "map": {"background": [("selected", "#ffffff")],
                "foreground": [("selected", "#000000")],
                "expand": [("selected", [1, 1, 1, 0])]}
    }
})