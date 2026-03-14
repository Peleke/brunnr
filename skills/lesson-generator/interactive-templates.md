# Interactive Templates — Copy-Paste Code Blocks

Ready-to-adapt code templates for engagement elements. Referenced by `engagement-patterns.md` for implementation details.

---

## YouTube Video Embed

```python
from IPython.display import YouTubeVideo, display, Markdown

def embed_video(video_id: str, title: str, context: str, start: int = 0) -> None:
    """Embed a YouTube video with contextual introduction.

    Args:
        video_id: YouTube video ID (11 chars after v=)
        title: Video title for the intro text
        context: 1-2 sentences explaining why this video is relevant here
        start: Start time in seconds (0 = beginning)
    """
    display(Markdown(f"---\n\n**Video**: *{title}*\n\n{context}\n"))
    display(YouTubeVideo(video_id, width=720, height=405, start=start))


# Usage:
# embed_video(
#     "lG4VkPoG3ko",
#     "Bayes theorem, the geometry of changing beliefs — 3Blue1Brown",
#     "You just computed a posterior by hand. This video shows the same idea geometrically — "
#     "watch how the rectangle shrinks as evidence arrives."
# )
```

---

## Plotly: Scatter with Hover Context

```python
import plotly.express as px
import plotly.graph_objects as go

def plotly_scatter_with_context(
    x, y, labels, descriptions, title,
    xaxis_title="X", yaxis_title="Y",
    color=None, color_map=None
):
    """Scatter plot where hover shows meaningful context, not just coordinates.

    Args:
        x, y: Data arrays
        labels: Short labels for each point (shown on hover)
        descriptions: Longer descriptions (shown on hover)
        title: Plot title
        color: Optional categorical color column
        color_map: Optional dict mapping categories to hex colors
    """
    import pandas as pd
    df = pd.DataFrame({
        'x': x, 'y': y,
        'label': labels, 'description': descriptions,
        **({"color": color} if color is not None else {})
    })

    fig = px.scatter(
        df, x='x', y='y',
        color='color' if color is not None else None,
        color_discrete_map=color_map,
        hover_data={'label': True, 'description': True, 'x': ':.2f', 'y': ':.2f'},
        title=title
    )
    fig.update_layout(
        template='plotly_white',
        xaxis_title=xaxis_title, yaxis_title=yaxis_title,
        font=dict(size=12),
        hoverlabel=dict(bgcolor="white", font_size=12)
    )
    fig.show()


# Usage (Module 0.1 — salience scores vs intuitive ratings):
# plotly_scatter_with_context(
#     x=salience_scores, y=intuitive_ratings,
#     labels=[f"Entry {i}" for i in range(len(ENTRIES))],
#     descriptions=[e.task[:60] for e in ENTRIES],
#     title="SalienceScorer vs. Intuitive Ratings",
#     xaxis_title="Salience Score", yaxis_title="Intuitive Rating"
# )
```

---

## Plotly: Bar Chart with Hover

```python
def plotly_bar_comparison(
    categories, values_a, values_b,
    label_a="A", label_b="B",
    title="Comparison", yaxis_title="Value",
    colors=("#2196F3", "#FF9800")
):
    """Side-by-side bar chart with hover showing both values."""
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name=label_a, x=categories, y=values_a,
        marker_color=colors[0],
        hovertemplate='%{x}<br>' + label_a + ': %{y:.2f}<extra></extra>'
    ))
    fig.add_trace(go.Bar(
        name=label_b, x=categories, y=values_b,
        marker_color=colors[1],
        hovertemplate='%{x}<br>' + label_b + ': %{y:.2f}<extra></extra>'
    ))
    fig.update_layout(
        barmode='group', template='plotly_white',
        title=title, yaxis_title=yaxis_title,
        font=dict(size=12)
    )
    fig.show()


# Usage (Module 0.2 — P(k) distribution):
# plotly_bar_comparison(
#     categories=[str(k) for k in range(6)],
#     values_a=pmf_values, values_b=cumulative_values,
#     label_a="P(k)", label_b="Cumulative P",
#     title="Binomial Distribution (n=5, p=0.5)"
# )
```

---

## Plotly: 3D Surface

```python
def plotly_3d_surface(
    X, Y, Z,
    title="Surface Plot",
    xaxis_title="X", yaxis_title="Y", zaxis_title="Z",
    colorscale="Blues", hover_format=".2f"
):
    """Interactive 3D surface with hover showing all three values.

    Args:
        X, Y: 2D meshgrid arrays
        Z: 2D values array (same shape as X, Y)
    """
    fig = go.Figure(data=[go.Surface(
        x=X, y=Y, z=Z,
        colorscale=colorscale,
        hovertemplate=(
            f'{xaxis_title}: %{{x:{hover_format}}}<br>'
            f'{yaxis_title}: %{{y:{hover_format}}}<br>'
            f'{zaxis_title}: %{{z:{hover_format}}}'
            '<extra></extra>'
        )
    )])
    fig.update_layout(
        title=title, template='plotly_white',
        scene=dict(
            xaxis_title=xaxis_title,
            yaxis_title=yaxis_title,
            zaxis_title=zaxis_title,
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
        ),
        font=dict(size=12)
    )
    fig.show()


# Usage (Module 0.1 — linearity vs interaction surface):
# L_grid = np.linspace(0, 1, 30)
# S_grid = np.linspace(0, 1, 30)
# L_mesh, S_mesh = np.meshgrid(L_grid, S_grid)
# Z = 0.4 * L_mesh + 0.4 * S_mesh + 0.2
# plotly_3d_surface(
#     L_mesh, S_mesh, Z,
#     title="Salience Score Surface (Linear Model)",
#     xaxis_title="Linguistic", yaxis_title="Structural", zaxis_title="Score"
# )
```

---

## Plotly: Animated Parameter Sweep

```python
def plotly_animated_sweep(
    param_values, param_name,
    compute_frame_fn,
    x_range, x_label="x", y_label="y",
    title="Parameter Sweep"
):
    """Animated plot that sweeps through parameter values.

    Args:
        param_values: Array of parameter values to sweep through
        param_name: Name of the parameter (shown in slider)
        compute_frame_fn: Function(param_value) -> (x_array, y_array)
        x_range: Tuple (x_min, x_max) for consistent axis
    """
    frames = []
    for pv in param_values:
        x, y = compute_frame_fn(pv)
        frames.append(go.Frame(
            data=[go.Scatter(x=x, y=y, mode='lines', line=dict(width=3, color='#2196F3'))],
            name=f"{param_name}={pv:.2f}"
        ))

    x0, y0 = compute_frame_fn(param_values[0])
    fig = go.Figure(
        data=[go.Scatter(x=x0, y=y0, mode='lines', line=dict(width=3, color='#2196F3'))],
        frames=frames
    )

    fig.update_layout(
        template='plotly_white', title=title,
        xaxis=dict(title=x_label, range=x_range),
        yaxis_title=y_label,
        font=dict(size=12),
        updatemenus=[dict(type="buttons", showactive=False,
            buttons=[
                dict(label="Play", method="animate",
                     args=[None, {"frame": {"duration": 100}, "fromcurrent": True}]),
                dict(label="Pause", method="animate",
                     args=[[None], {"frame": {"duration": 0}, "mode": "immediate"}])
            ])],
        sliders=[dict(
            steps=[dict(args=[[f.name], {"frame": {"duration": 0}, "mode": "immediate"}],
                        method="animate", label=f"{pv:.1f}")
                   for pv, f in zip(param_values, frames)],
            currentvalue=dict(prefix=f"{param_name}: ")
        )]
    )
    fig.show()


# Usage (Module 0.3 — Beta distribution shape sweep):
# from scipy.stats import beta as beta_dist
# x = np.linspace(0, 1, 200)
# alphas = np.linspace(0.5, 10, 20)
# plotly_animated_sweep(
#     alphas, "α",
#     compute_frame_fn=lambda a: (x, beta_dist.pdf(x, a, 3)),
#     x_range=(0, 1), x_label="θ", y_label="PDF",
#     title="Beta(α, β=3) — Watch the Shape Change"
# )
```

---

## ipywidgets: `@interact` Slider

```python
from ipywidgets import interact, FloatSlider, IntSlider
import matplotlib.pyplot as plt

@interact(
    w_linguistic=FloatSlider(value=0.4, min=0.0, max=1.0, step=0.05, description='w_linguistic'),
    w_structural=FloatSlider(value=0.4, min=0.0, max=1.0, step=0.05, description='w_structural'),
)
def explore_weights(w_linguistic, w_structural):
    """Explore how weight changes affect salience scores."""
    w_outcome = max(0, 1.0 - w_linguistic - w_structural)  # Enforce sum-to-1

    # Recompute scores with new weights (assumes `ENTRIES`, scoring functions exist)
    scores = [
        w_linguistic * linguistic_signal(e.rule, e.agent_output)
        + w_structural * structural_signal(e.rule, e.agent_output)
        + w_outcome * outcome_signal(e)
        for e in ENTRIES
    ]
    intuitive = [e.intuitive_compliance for e in ENTRIES]

    from scipy.stats import spearmanr
    rho, pval = spearmanr(scores, intuitive)

    fig, ax = plt.subplots(figsize=(10, 4))
    x = np.arange(len(ENTRIES))
    ax.bar(x - 0.2, scores, 0.35, label='Salience', color='#2196F3')
    ax.bar(x + 0.2, intuitive, 0.35, label='Intuitive', color='#FF9800')
    ax.set_title(f'Weights: L={w_linguistic:.2f}, S={w_structural:.2f}, O={w_outcome:.2f} | ρ={rho:.3f} (p={pval:.3f})')
    ax.set_ylabel('Score')
    ax.set_xticks(x)
    ax.legend()
    ax.set_ylim(0, 1.2)
    plt.tight_layout()
    plt.show()
```

---

## ipywidgets: Button-Triggered Simulation

```python
import ipywidgets as widgets
from IPython.display import display, clear_output

# Create widgets
n_trials_slider = IntSlider(value=100, min=10, max=1000, step=10, description='Trials:')
p_treatment_slider = FloatSlider(value=0.6, min=0.0, max=1.0, step=0.05, description='P(treatment):')
p_control_slider = FloatSlider(value=0.5, min=0.0, max=1.0, step=0.05, description='P(control):')
run_button = widgets.Button(description='Run Experiment', button_style='primary')
output = widgets.Output()

def run_experiment(b):
    with output:
        clear_output(wait=True)
        n = n_trials_slider.value
        p_t, p_c = p_treatment_slider.value, p_control_slider.value

        treatment = np.random.binomial(1, p_t, n)
        control = np.random.binomial(1, p_c, n)

        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        # Left: cumulative success rates
        t_cumulative = np.cumsum(treatment) / np.arange(1, n+1)
        c_cumulative = np.cumsum(control) / np.arange(1, n+1)
        axes[0].plot(t_cumulative, label=f'Treatment (true p={p_t})', color='#2196F3')
        axes[0].plot(c_cumulative, label=f'Control (true p={p_c})', color='#FF9800')
        axes[0].axhline(y=p_t, color='#2196F3', linestyle='--', alpha=0.3)
        axes[0].axhline(y=p_c, color='#FF9800', linestyle='--', alpha=0.3)
        axes[0].set_xlabel('Trial'); axes[0].set_ylabel('Cumulative Success Rate')
        axes[0].set_title('Convergence Over Time')
        axes[0].legend()

        # Right: final comparison
        axes[1].bar(['Treatment', 'Control'], [treatment.mean(), control.mean()],
                    color=['#2196F3', '#FF9800'])
        axes[1].set_ylabel('Success Rate')
        axes[1].set_title(f'Final: T={treatment.mean():.2%} vs C={control.mean():.2%}')
        axes[1].set_ylim(0, 1)

        plt.tight_layout()
        plt.show()

        diff = treatment.mean() - control.mean()
        print(f"Observed difference: {diff:+.2%}")
        print(f"True difference:     {p_t - p_c:+.2%}")

run_button.on_click(run_experiment)
display(widgets.VBox([n_trials_slider, p_treatment_slider, p_control_slider, run_button, output]))
```

---

## ipywidgets: Constrained Multi-Slider (Weights Sum to 1)

```python
import ipywidgets as widgets
from IPython.display import display, clear_output

w_l_slider = FloatSlider(value=0.4, min=0.0, max=1.0, step=0.05, description='Linguistic:')
w_s_slider = FloatSlider(value=0.4, min=0.0, max=1.0, step=0.05, description='Structural:')
w_o_display = widgets.HTML(value='<b>Outcome: 0.20</b>')
output = widgets.Output()

def on_weight_change(change):
    """Enforce w_l + w_s + w_o = 1 by computing w_o from the other two."""
    w_o = max(0.0, round(1.0 - w_l_slider.value - w_s_slider.value, 2))
    w_o_display.value = f'<b>Outcome: {w_o:.2f}</b>'

    if w_l_slider.value + w_s_slider.value > 1.0:
        w_o_display.value = '<b style="color:red">Outcome: 0.00 (L+S > 1!)</b>'

    with output:
        clear_output(wait=True)
        # Recompute and plot with new weights
        # ... (similar to @interact pattern above)

w_l_slider.observe(on_weight_change, names='value')
w_s_slider.observe(on_weight_change, names='value')

display(widgets.VBox([w_l_slider, w_s_slider, w_o_display, output]))
```

---

## FuncAnimation: Distribution Evolution

```python
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
from scipy.stats import beta as beta_dist

def animate_beta_evolution(observations, alpha_prior=1, beta_prior=1, interval=300):
    """Animate Bayesian updating of a Beta distribution.

    Args:
        observations: List of 0/1 outcomes
        alpha_prior, beta_prior: Prior Beta parameters
        interval: Milliseconds between frames
    """
    x = np.linspace(0, 1, 200)
    fig, ax = plt.subplots(figsize=(10, 5))
    line, = ax.plot(x, beta_dist.pdf(x, alpha_prior, beta_prior), 'b-', lw=2)
    title = ax.set_title('')
    ax.set_xlabel('θ (success probability)')
    ax.set_ylabel('Density')
    ax.set_xlim(0, 1)

    # Compute max y across all frames for stable axis
    a_final = alpha_prior + sum(observations)
    b_final = beta_prior + len(observations) - sum(observations)
    max_y = max(beta_dist.pdf(x, a_final, b_final).max() * 1.1, 4)
    ax.set_ylim(0, max_y)

    def update(frame):
        a = alpha_prior + sum(observations[:frame])
        b = beta_prior + frame - sum(observations[:frame])
        y = beta_dist.pdf(x, a, b)
        line.set_ydata(y)
        successes = sum(observations[:frame])
        title.set_text(
            f'Beta({a}, {b}) | Observations: {frame} | '
            f'Successes: {successes} | Mean: {a/(a+b):.2f}'
        )
        return line, title

    anim = FuncAnimation(fig, update, frames=len(observations)+1, interval=interval, blit=False)
    plt.close(fig)
    return HTML(anim.to_jshtml())


# Usage:
# observations = [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
# animate_beta_evolution(observations, alpha_prior=1, beta_prior=1)
```

---

## FuncAnimation: Convergence Visualization

```python
def animate_convergence(true_value, sample_fn, n_samples=200, interval=50):
    """Animate sample mean converging to true value (Law of Large Numbers).

    Args:
        true_value: The value the sample mean converges to
        sample_fn: Function() -> single sample
        n_samples: Total number of samples
        interval: Milliseconds between frames
    """
    samples = [sample_fn() for _ in range(n_samples)]
    cumulative_means = np.cumsum(samples) / np.arange(1, n_samples + 1)

    fig, ax = plt.subplots(figsize=(10, 5))
    line, = ax.plot([], [], 'b-', lw=1.5)
    ax.axhline(y=true_value, color='red', linestyle='--', alpha=0.7, label=f'True value: {true_value:.2f}')
    ax.set_xlim(0, n_samples)
    ax.set_ylim(true_value - 0.5, true_value + 0.5)
    ax.set_xlabel('Number of samples')
    ax.set_ylabel('Running mean')
    ax.legend()
    title = ax.set_title('')

    def update(frame):
        n = frame + 1
        line.set_data(range(n), cumulative_means[:n])
        title.set_text(f'Sample mean: {cumulative_means[frame]:.4f} | n={n}')
        return line, title

    anim = FuncAnimation(fig, update, frames=n_samples, interval=interval, blit=False)
    plt.close(fig)
    return HTML(anim.to_jshtml())


# Usage:
# animate_convergence(
#     true_value=0.5,
#     sample_fn=lambda: np.random.binomial(1, 0.5),
#     n_samples=200
# )
```

---

## Concept Map: Arc Progress Map

```python
import plotly.graph_objects as go
import networkx as nx

def arc_progress_map(arc_number: int, total_modules: int, current_module: int,
                     module_titles: list[str] = None):
    """Interactive arc progress map showing current position.

    Args:
        arc_number: Arc number (0, 1, 2, ...)
        total_modules: Total modules in this arc
        current_module: 1-indexed current module number
        module_titles: Optional list of module short titles
    """
    if module_titles is None:
        module_titles = [f"Module {arc_number}.{i}" for i in range(1, total_modules + 1)]

    G = nx.DiGraph()
    for i in range(total_modules):
        G.add_node(i, title=module_titles[i])
        if i > 0:
            G.add_edge(i - 1, i)

    # Layout: horizontal chain
    pos = {i: (i * 2, 0) for i in range(total_modules)}

    # Edge traces
    edge_x, edge_y = [], []
    for e0, e1 in G.edges():
        x0, y0 = pos[e0]
        x1, y1 = pos[e1]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y, mode='lines',
        line=dict(width=2, color='#BDBDBD'),
        hoverinfo='none'
    )

    # Node traces — different colors for completed, current, future
    node_x = [pos[i][0] for i in range(total_modules)]
    node_y = [pos[i][1] for i in range(total_modules)]

    colors = []
    sizes = []
    for i in range(total_modules):
        mod_num = i + 1
        if mod_num < current_module:
            colors.append('#4CAF50')  # Completed: green
            sizes.append(30)
        elif mod_num == current_module:
            colors.append('#2196F3')  # Current: blue
            sizes.append(45)
        else:
            colors.append('#E0E0E0')  # Future: gray
            sizes.append(25)

    hover_text = [
        f"<b>{arc_number}.{i+1}: {module_titles[i]}</b><br>"
        f"{'Completed' if i+1 < current_module else 'Current' if i+1 == current_module else 'Upcoming'}"
        for i in range(total_modules)
    ]

    node_trace = go.Scatter(
        x=node_x, y=node_y, mode='markers+text',
        marker=dict(size=sizes, color=colors, line=dict(width=2, color='white')),
        text=[f"{arc_number}.{i+1}" for i in range(total_modules)],
        textposition='top center',
        hovertext=hover_text,
        hoverinfo='text'
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        title=f"Arc {arc_number} Progress — Module {arc_number}.{current_module}",
        template='plotly_white',
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=200,
        margin=dict(l=20, r=20, t=50, b=20),
        font=dict(size=12)
    )
    fig.show()


# Usage:
# ARC_0_MODULES = [
#     "Taste Demo", "Probability & Counting", "Distributions & Beta Priors",
#     "Bayesian Updating", "Hypothesis Testing", "Bootstrap CIs",
#     "Thompson Sampling", "Ship It"
# ]
# arc_progress_map(0, 8, 1, ARC_0_MODULES)  # Module 0.1 is current
```

---

## Combined: Widget + Plotly Live-Updating Chart

```python
import ipywidgets as widgets
import plotly.graph_objects as go
from IPython.display import display, clear_output

slider = FloatSlider(value=0.5, min=0.01, max=0.99, step=0.01, description='P(success):')
output = widgets.Output()

def update_plot(change):
    p = slider.value
    k = np.arange(0, 11)
    from scipy.stats import binom
    pmf = binom.pmf(k, 10, p)

    with output:
        clear_output(wait=True)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=k, y=pmf,
            marker_color=['#E91E63' if v == pmf.max() else '#2196F3' for v in pmf],
            hovertemplate='k=%{x}<br>P(k)=%{y:.4f}<extra></extra>'
        ))
        fig.update_layout(
            title=f'Binomial(n=10, p={p:.2f}) — Mode at k={k[pmf.argmax()]}',
            xaxis_title='k (successes)', yaxis_title='P(k)',
            template='plotly_white', height=350
        )
        fig.show()

slider.observe(update_plot, names='value')
display(widgets.VBox([slider, output]))
update_plot(None)  # Initial render
```

---

## Imports Block (add to Cell 2 of every core notebook)

```python
# Engagement imports — add these alongside existing imports
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import YouTubeVideo, HTML, display, Markdown
from ipywidgets import interact, FloatSlider, IntSlider
import ipywidgets as widgets
```
