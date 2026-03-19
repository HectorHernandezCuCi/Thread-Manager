import time
import threading
import flet as ft
from utils.formats.numbers import get_int
from helpers.validateInputs import validate_inputs
from helpers.calculatePartialSum import calculate_partial_sum
from helpers.UI.buildThreadVisualization import build_thread_visualization

def run_benchmark(e, page, ui):
    error_msg = validate_inputs(ui['threads_input'], ui['limit_input'])
    if error_msg:
        page.snack_bar = ft.SnackBar(ft.Text(error_msg), bgcolor="#FF6B6B")
        page.snack_bar.open = True
        page.update()
        return

    n = get_int(ui['threads_input'])
    limit = get_int(ui['limit_input'])
    
    ui['btn'].disabled = True
    ui['progress_bar'].visible = True
    ui['results_card'].visible = False
    page.update()

    partial_results, times = [0] * n, [0.0] * n
    threads = []
    chunk = limit // n
    
    t_start = time.time()
    for i in range(n):
        start = (i * chunk) + 1
        end = limit if i == n - 1 else (i + 1) * chunk
        t = threading.Thread(target=calculate_partial_sum, args=(start, end, partial_results, i, times))
        threads.append(t)
        t.start()
    for t in threads: t.join()
    t_total = time.time() - t_start

    s_start = time.time()
    seq_sum = sum(range(1, limit + 1))
    s_total = time.time() - s_start

    ui['threaded_val_txt'].value = f"{sum(partial_results):,}"
    ui['sequential_val_txt'].value = f"{seq_sum:,}"
    ui['thread_time_label'].value = f"{t_total*1000:.2f} ms"
    ui['seq_time_label'].value = f"{s_total*1000:.2f} ms"
    
    speedup = s_total / t_total if t_total > 0 else 1
    if speedup > 1:
        ui['speedup_txt'].value = f"Multi-threading is {speedup:.2f}x faster"
        ui['speedup_txt'].color = "#69F0AE"
    else:
        ui['speedup_txt'].value = f"Sequential is {1/speedup:.2f}x faster"
        ui['speedup_txt'].color = "#FF6B6B"

    ui['thread_breakdown_col'].controls = build_thread_visualization(n, limit, partial_results, times)
    
    ui['progress_bar'].visible = False
    ui['results_card'].visible = True
    ui['btn'].disabled = False
    page.update()