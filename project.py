import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file
data = pd.read_csv('C:\\Users\\racha\\Desktop\\final project\\final project data.csv')
print(data.head())

# Count the number of occurrences for each category
drinking_counts = data['Drinking'].value_counts().sort_index()
smoking_counts = data['Smoking'].value_counts().sort_index()

# Calculate percentages for each category
drinking_percentages = (drinking_counts / drinking_counts.sum()) * 100
smoking_percentages = (smoking_counts / smoking_counts.sum()) * 100

# Labels for the categories
drinking_labels = {1: 'Non-Drinker', 2: '1 day', 3: '2 days', 4: '3/5 days', 5: '6/9 days', 6: '10/19 days', 7: '20+ days'}
smoking_labels = {1: 'Non-Smoker', 2: '1 day', 3: '2 days', 4: '3/5 days', 5: '6/9 days', 6: '10/19 days', 7: '20+ days'}

while True:
    # Ask the user which graph they want to see
    print("\nChoose a graph to display:")
    print("1. Bar Chart")
    print("2. Line Chart")
    print("3. Pie Chart")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '4':
        print("Goodbye!")
        break

    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    if choice == '1':
        # Bar chart for Drinking
        axes[0].bar(drinking_counts.index, drinking_counts.values, color='skyblue')
        axes[0].set_title('Drinking Frequency')
        axes[0].set_xlabel('Category')
        axes[0].set_ylabel('Count')
        axes[0].set_xticks(drinking_counts.index)
        axes[0].set_xticklabels([drinking_labels[i] for i in drinking_counts.index])

        # Annotate percentages on the bars
        for i in range(len(drinking_counts)):
            count = drinking_counts.values[i]
            percent = drinking_percentages.values[i]
            axes[0].text(drinking_counts.index[i], count, f'{percent:.1f}%', ha='center', va='bottom')

        # Bar chart for Smoking
        axes[1].bar(smoking_counts.index, smoking_counts.values, color='red')
        axes[1].set_title('Smoking Frequency')
        axes[1].set_xlabel('Category')
        axes[1].set_ylabel('Count')
        axes[1].set_xticks(smoking_counts.index)
        axes[1].set_xticklabels([smoking_labels[i] for i in smoking_counts.index])

        # Annotate percentages on the bars
        for i in range(len(smoking_counts)):
            count = smoking_counts.values[i]
            percent = smoking_percentages.values[i]
            axes[1].text(smoking_counts.index[i], count, f'{percent:.1f}%', ha='center', va='bottom')

    elif choice == '2':
        # Line chart for Drinking
        axes[0].plot(drinking_counts.index, drinking_counts.values, marker='o', color='skyblue')
        axes[0].set_title('Drinking Frequency')
        axes[0].set_xlabel('Category')
        axes[0].set_ylabel('Count')
        axes[0].set_xticks(drinking_counts.index)
        axes[0].set_xticklabels([drinking_labels[i] for i in drinking_counts.index])

        # Annotate percentages on the line
        for i in range(len(drinking_counts)):
            count = drinking_counts.values[i]
            percent = drinking_percentages.values[i]
            axes[0].text(drinking_counts.index[i], count, f'{percent:.1f}%', ha='center', va='bottom')

        # Line chart for Smoking
        axes[1].plot(smoking_counts.index, smoking_counts.values, marker='o', color='red')
        axes[1].set_title('Smoking Frequency')
        axes[1].set_xlabel('Category')
        axes[1].set_ylabel('Count')
        axes[1].set_xticks(smoking_counts.index)
        axes[1].set_xticklabels([smoking_labels[i] for i in smoking_counts.index])

        # Annotate percentages on the line
        for i in range(len(smoking_counts)):
            count = smoking_counts.values[i]
            percent = smoking_percentages.values[i]
            axes[1].text(smoking_counts.index[i], count, f'{percent:.1f}%', ha='center', va='bottom')

    elif choice == '3':
        # Pie chart for Drinking
        wedges, _ = axes[0].pie(drinking_percentages, startangle=90, radius=0.8)
        axes[0].set_title('Drinking Frequency')
        drinking_legend_labels = [f"{drinking_labels[i]}: {drinking_percentages[i]:.1f}%" for i in drinking_counts.index]
        axes[0].legend(wedges, drinking_legend_labels, title="Percentages", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        # Pie chart for Smoking
        wedges, _ = axes[1].pie(smoking_percentages, startangle=90, radius=0.8)
        axes[1].set_title('Smoking Frequency')
        smoking_legend_labels = [f"{smoking_labels[i]}: {smoking_percentages[i]:.1f}%" for i in smoking_counts.index]
        axes[1].legend(wedges, smoking_legend_labels, title="Percentages", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    else:
        print("Invalid choice. Please try again.")
        continue

    # Show the plot
    plt.tight_layout()
    plt.show()