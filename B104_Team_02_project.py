import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data from a CSV file
data = pd.read_csv('C:\\Users\\racha\\Desktop\\final project\\B104_Team_02_YRBS_data.csv')
dataA = np.array(data)

# Convert 'Drinking' and 'Smoking' columns to numeric, coercing errors to NaN
data['Drinking'] = pd.to_numeric(data['Drinking'], errors='coerce')
data['Smoking'] = pd.to_numeric(data['Smoking'], errors='coerce')

# Check for and handle missing values
print(data.isnull().sum())

# Drop rows with NaN values in 'Drinking' or 'Smoking' columns
data.dropna(subset=['Drinking', 'Smoking'], inplace=True)

# Count the number of times each category occurs 
drinking_counts = data['Drinking'].value_counts().sort_index()
smoking_counts = data['Smoking'].value_counts().sort_index()

# Calculates the percentages for each category
drinking_percentages = (drinking_counts / drinking_counts.sum()) * 100
smoking_percentages = (smoking_counts / smoking_counts.sum()) * 100

# Category labels
drinking_labels = {1: 'Non-Drinker', 2: '1 day', 3: '2 days', 4: '3/5 days', 5: '6/9 days', 6: '10/19 days', 7: '20+ days'}
smoking_labels = {1: 'Non-Smoker', 2: '1 day', 3: '2 days', 4: '3/5 days', 5: '6/9 days', 6: '10/19 days', 7: '20+ days'}

while True:
    # Ask the user which graph they want to see
    print('\nChoose a graph to display:')
    print('1. Bar Chart')
    print('2. Line Chart')
    print('3. Pie Chart')
    print('4. Heat Map')
    print('5. Exit')
    choice = input('Enter your choice (1-5): ')

    if choice == '5':
        print('Goodbye!')
        break

    # Create the figure with two subplots
    fig, (drinking_ax, smoking_ax) = plt.subplots(1, 2, figsize=(14, 6))

    if choice == '1':
        # Bar chart for Drinking
        # f{percent}% shows the percentage value, rounded to one decimal place, followed by a percent sign.
        # ha = horizontal alignment where the txt will be alligned 
        # va = vertical alignmnet where the text will be alligned 
        drinking_ax.bar(drinking_counts.index, drinking_counts.values, color='skyblue')
        drinking_ax.set_title('Drinking Frequency')
        drinking_ax.set_xlabel('Category')
        drinking_ax.set_ylabel('Count')
        drinking_ax.set_xticks(drinking_counts.index)
        drinking_ax.set_xticklabels([drinking_labels.get(i, 'Unknown') for i in drinking_counts.index])

        # Places percentages on the bars
        for i in range(len(drinking_counts)):
            count = drinking_counts.values[i]
            percent = round(drinking_percentages.values[i], 1)
            drinking_ax.text(drinking_counts.index[i], count, f'{percent}%', ha='center', va='bottom')

        # Bar chart for Smoking
        smoking_ax.bar(smoking_counts.index, smoking_counts.values, color='red')
        smoking_ax.set_title('Smoking Frequency')
        smoking_ax.set_xlabel('Category')
        smoking_ax.set_ylabel('Count')
        smoking_ax.set_xticks(smoking_counts.index)
        smoking_ax.set_xticklabels([smoking_labels.get(i, 'Unknown') for i in smoking_counts.index])

        # Places percentages on the bars
        for i in range(len(smoking_counts)):
            count = smoking_counts.values[i]
            percent = round(smoking_percentages.values[i], 1)
            smoking_ax.text(smoking_counts.index[i], count, f'{percent}%', ha='center', va='bottom')

    elif choice == '2':
        # Line chart for Drinking
        drinking_ax.plot(drinking_counts.index, drinking_counts.values, marker='o', color='skyblue')
        drinking_ax.set_title('Drinking Frequency')
        drinking_ax.set_xlabel('Category')
        drinking_ax.set_ylabel('Count')
        drinking_ax.set_xticks(drinking_counts.index)
        drinking_ax.set_xticklabels([drinking_labels.get(i, 'Unknown') for i in drinking_counts.index])

        # Places percentages on the line
        for i in range(len(drinking_counts)):
            count = drinking_counts.values[i]
            percent = round(drinking_percentages.values[i], 1)
            drinking_ax.text(drinking_counts.index[i], count, f'{percent}%', ha='center', va='bottom')

        # Line chart for Smoking
        smoking_ax.plot(smoking_counts.index, smoking_counts.values, marker='o', color='red')
        smoking_ax.set_title('Smoking Frequency')
        smoking_ax.set_xlabel('Category')
        smoking_ax.set_ylabel('Count')
        smoking_ax.set_xticks(smoking_counts.index)
        smoking_ax.set_xticklabels([smoking_labels.get(i, 'Unknown') for i in smoking_counts.index])

        # Places percentages on the line
        for i in range(len(smoking_counts)):
            count = smoking_counts.values[i]
            percent = round(smoking_percentages.values[i], 1)
            smoking_ax.text(smoking_counts.index[i], count, f'{percent}%', ha='center', va='bottom')

    elif choice == '3':
        # Pie chart for Drinking
        wedges, _ = drinking_ax.pie(drinking_percentages, startangle=90, radius=0.8)
        drinking_ax.set_title('Drinking Frequency')
        drinking_legend_labels = [f'{drinking_labels.get(i, 'Unknown')}: {round(drinking_percentages[i], 1)}%' for i in drinking_counts.index]
        drinking_ax.legend(wedges, drinking_legend_labels, title='Percentages', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

        # Pie chart for Smoking
        wedges, _ = smoking_ax.pie(smoking_percentages, startangle=90, radius=0.8)
        smoking_ax.set_title('Smoking Frequency')
        smoking_legend_labels = [f'{smoking_labels.get(i, 'Unknown')}: {round(smoking_percentages[i], 1)}%' for i in smoking_counts.index]
        smoking_ax.legend(wedges, smoking_legend_labels, title='Percentages', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
    
    elif choice == '4':
        # Create a pivot table for the heatmap
        pivot_table = data.pivot_table(index='Smoking', columns='Drinking', aggfunc='size', fill_value=0)

        # Plot the heatmap
        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
        plt.title('Heatmap of Days Smoking vs. Days Drinking')
        plt.xlabel('Days Drinking')
        plt.ylabel('Days Smoking')
        plt.show()
        continue  # Skip the plt.tight_layout() and plt.show() for heatmap

    else:
        print("Invalid choice. Please try again.")
        continue

    # Show the plot
    plt.tight_layout()
    plt.show()