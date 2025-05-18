import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def initialize_grid(size, initial_density=0.2):
    """Инициализация сетки с заданной плотностью живых клеток."""
    return np.random.choice([0, 1], size=(size, size), p=[1 - initial_density, initial_density])

def update_grid(grid):
    """Обновление состояния сетки на основе правил игры 'Жизнь'."""
    new_grid = grid.copy()
    rows, cols = grid.shape

    for i in range(rows):
        for j in range(cols):
            # Вычисление количества живых соседей
            total = (grid[i, (j-1)%cols] + grid[i, (j+1)%cols] +
                     grid[(i-1)%rows, j] + grid[(i+1)%rows, j] +
                     grid[(i-1)%rows, (j-1)%cols] + grid[(i-1)%rows, (j+1)%cols] +
                     grid[(i+1)%rows, (j-1)%cols] + grid[(i+1)%rows, (j+1)%cols])

             # Применение модифицированных правил игры 'Жизнь'
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
                elif total == 1:  # Новое правило: выживание при 1 соседе
                    new_grid[i, j] = 1
                elif total == 3:  # Новое правило: смерть при 3 соседях
                    new_grid[i, j] = 0
            else:
                if total == 3 or total == 4:  # Новое правило: рождение при 4 соседях
                    new_grid[i, j] = 1
                    
    return new_grid

def animate_life(grid, iterations=50):
    """Анимация эволюции игры 'Жизнь'."""
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')

    def update(frame):
        nonlocal grid
        grid = update_grid(grid)
        img.set_array(grid)
        return img,

    ani = animation.FuncAnimation(fig, update, frames=iterations, interval=200, blit=True)
    plt.show()

# Инициализация начальной сетки
grid_size = 50
initial_grid = initialize_grid(grid_size, initial_density=0.3)

# Запуск анимации
animate_life(initial_grid, iterations=50)
