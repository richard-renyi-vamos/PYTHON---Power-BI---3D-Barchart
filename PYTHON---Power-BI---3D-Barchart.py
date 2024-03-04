import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'X': [1, 2, 3, 4],
    'Y': [5, 6, 7, 8],
    'Z': [9, 10, 11, 12]
}

df = pd.DataFrame(data)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = df['X']
y = df['Y']
z = df['Z']

# Create 3D bar chart
ax.bar3d(x, y, 0, 1, 1, z, color='skyblue')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Bar Chart')

plt.show()
