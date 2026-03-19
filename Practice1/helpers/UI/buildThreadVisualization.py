import flet as ft

def build_thread_visualization(n, limit, partial_results, times):
        chunk = limit // n
        max_val = max(partial_results) if partial_results else 1
        colors = ["#4FC3F7", "#81D4FA", "#00E5FF", "#64FFDA", "#B2FF59", "#FFD740", "#FF4081", "#7C4DFF"]
        
        rows = []
        for i in range(n):
            color = colors[i % len(colors)]
            start = (i * chunk) + 1
            end = limit if i == n - 1 else (i + 1) * chunk
            ratio = partial_results[i] / max_val
            
            rows.append(
                ft.Container(
                    content=ft.ResponsiveRow([
                        ft.Text(f"T{i}", size=11, color=color, weight="bold", col={"xs": 2, "sm": 1}),
                        ft.Column([
                            ft.Text(f"{start:,} - {end:,}", size=10, color="#607D8B"),
                            ft.Stack([
                                ft.Container(height=8, bgcolor="#1A2332", border_radius=4),
                                ft.Container(
                                    height=8, 
                                    width=400 * ratio, 
                                    bgcolor=color, 
                                    border_radius=4, 
                                    animate=ft.Animation(600, "easeOut")
                                ),
                            ])
                        ], col={"xs": 6, "sm": 8}),
                        ft.Text(f"{times[i]*1000:.1f}ms", size=10, color="#546E7A", text_align="right", col={"xs": 4, "sm": 3}),
                    ], vertical_alignment="center"),
                    padding=ft.padding.symmetric(vertical=5)
                )
            )
        return rows
