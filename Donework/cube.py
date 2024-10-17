# import matplotlib.pyplot as plt

# # Sample data
# x = [0, 1, 2, 3, 4]
# y = [0, 1, 4, 9, 16]

# # Create a figure and an axes
# fig, ax = plt.subplots()

# # Plot data
# ax.plot(x, y)

# # Show the plot
# plt.show()



import matplotlib.pyplot as plt

# Sample data
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Create a figure and an axes
fig, ax = plt.subplots()

# Plot data
ax.plot(x, y)

# Set labels and title
ax.set_xlabel('X-axis Label')  # Label for the x-axis
ax.set_ylabel('Y-axis Label')  # Label for the y-axis
ax.set_title('Title of the Chart')  # Title of the chart

# Show the plot
plt.show()
