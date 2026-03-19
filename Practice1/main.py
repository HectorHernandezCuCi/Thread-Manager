import flet as ft

from utils.formats.numbers import format_number_input
from helpers.UI.runBenchmark import run_benchmark

def main(page: ft.Page):
    page.title = "Thread Manager"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0A0E1A"
    page.padding = 0
    page.window_min_width = 450
    page.window_width = 700
    page.window_height = 900

    threads_input = ft.TextField(
        label="Thread Count", 
        value="4", 
        expand=1, 
        border_color="#1E3A5F", 
        keyboard_type=ft.KeyboardType.NUMBER,
        prefix_icon=ft.icons.Icons.NUMBERS,
        on_change=format_number_input
    )
    
    limit_input = ft.TextField(
        label="Range Limit", 
        value="1,000,000", 
        expand=2, 
        border_color="#1E3A5F", 
        keyboard_type=ft.KeyboardType.NUMBER,
        prefix_icon=ft.icons.Icons.LINE_WEIGHT,
        on_change=format_number_input
    )

    progress_bar = ft.ProgressBar(width=None, color="#4FC3F7", visible=False)
    threaded_val_txt = ft.Text("—", size=20, weight="bold", color="#4FC3F7")
    sequential_val_txt = ft.Text("—", size=20, weight="bold", color="#90CAF9")
    thread_time_label = ft.Text("—", size=12)
    seq_time_label = ft.Text("—", size=12)
    speedup_txt = ft.Text("", size=14, weight="bold")
    thread_breakdown_col = ft.Column(spacing=0)

    results_card = ft.Container(
        visible=False,
        content=ft.Column([
            ft.Text("Performance Comparison", size=16, weight="bold"),
            ft.Divider(color="#1A2332"),
            ft.ResponsiveRow([
                ft.Column([
                    ft.Text("Multi-Threaded Sum", size=12, color="#90A4AE"), 
                    threaded_val_txt, 
                    thread_time_label
                ], col=6),
                ft.Column([
                    ft.Text("Sequential Sum", size=12, color="#90A4AE"), 
                    sequential_val_txt, 
                    seq_time_label
                ], col=6),
            ]),
            ft.Container(speedup_txt, alignment=ft.alignment.Alignment.CENTER, padding=15),
            ft.Divider(color="#1A2332"),
            ft.Text("Thread Breakdown", size=14, weight="bold", color="#4FC3F7"),
            thread_breakdown_col
        ]),
        padding=20, 
        border_radius=15, 
        bgcolor="#0D1421", 
        border=ft.border.all(1, "#1E3A5F")
    )

    ui_components = {
        'threads_input': threads_input,
        'limit_input': limit_input,
        'progress_bar': progress_bar,
        'results_card': results_card,
        'threaded_val_txt': threaded_val_txt,
        'sequential_val_txt': sequential_val_txt,
        'thread_time_label': thread_time_label,
        'seq_time_label': seq_time_label,
        'speedup_txt': speedup_txt,
        'thread_breakdown_col': thread_breakdown_col
    }

    btn = ft.ElevatedButton(
        "Run Benchmark", 
        icon=ft.icons.Icons.PLAY_ARROW_ROUNDED, 
        on_click=lambda e: run_benchmark(e, page, ui_components),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20
        )
    )

    ui_components['btn'] = btn

    header = ft.Container(
        content=ft.Row([
            ft.Icon(ft.icons.Icons.MEMORY, color="#4FC3F7", size=30),
            ft.Text("THREAD MANAGER PRO", size=22, weight="bold")
        ]),
        padding=25, 
        bgcolor="#0D1421",
        border=ft.border.only(bottom=ft.border.BorderSide(1, "#1A2332"))
    )

    main_scroll_area = ft.Container(
        expand=True,
        content=ft.Column([
            ft.Text("Configuration", size=14, color="#607D8B", weight="bold"),
            ft.Row([threads_input, limit_input], spacing=10),
            btn,
            progress_bar,
            results_card,
            ft.Container(height=40)
        ], 
        scroll=ft.ScrollMode.ADAPTIVE, 
        spacing=20),
        padding=20
    )

    page.add(header, main_scroll_area)

if __name__ == "__main__":
    ft.app(target=main)