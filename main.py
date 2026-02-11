import flet as ft
import google.generativeai as genai
import os

# DIQQAT: API kalitini shu yerga qo'ying
GOOGLE_AI_KEY = "SIZNING_GEMINI_API_KALITINGIZ"
genai.configure(api_key=GOOGLE_AI_KEY)

def main(page: ft.Page):
    page.title = "EngineerHelperUz AI"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212"
    
    # AI mantiqi
    def get_ai_response(prompt):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            f"Siz professional muhandissiz. Savolga texnik tilda javob bering: {prompt}"
        )
        return response.text

    def on_search(e):
        if not search_box.value: return
        loader.visible = True
        results.controls.clear()
        page.update()
        
        try:
            answer = get_ai_response(search_box.value)
            results.controls.append(ft.Markdown(answer, selectable=True))
        except Exception as ex:
            results.controls.append(ft.Text(f"Xato: {ex}", color="red"))
        
        loader.visible = False
        page.update()

    # UI Elementlari
    search_box = ft.TextField(hint_text="Muhandislik yechimi izlang...", expand=True, border_radius=15)
    loader = ft.ProgressBar(visible=False, color="#2196F3")
    results = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    page.add(
        ft.AppBar(title=ft.Text("EngineerHelperUz"), bgcolor="#1E1E1E"),
        ft.Row([search_box, ft.IconButton(ft.icons.SEARCH, on_click=on_search)]),
        loader,
        results
    )

ft.app(target=main)