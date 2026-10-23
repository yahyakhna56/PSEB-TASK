# Zomato Restaurant Analytics Dashboard

An interactive dashboard built with **Python**, **Pandas**, **Matplotlib**, **Seaborn**, and **Streamlit** to explore restaurant data from the Zomato dataset.

## 🚀 Live Demo

**Open the deployed dashboard:** https://pseb-task-hvtrgtbus2gdw9gfaqso4z.streamlit.app/

## 📊 Features

- Upload the Zomato restaurant CSV directly in the app.
- Filter restaurant records by city and price range.
- View key metrics, including the number of restaurants in the current selection and their average rating.
- Explore three visualizations:
  - Distribution of restaurant ratings
  - Top cities by restaurant count
  - Average rating by price range
- View the dashboard online through Streamlit Community Cloud.

## 🧰 Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit

## 📁 Repository Structure

```text
zomato-restaurant-dashboard/
├── app.py
├── requirements.txt
└── README.md
```

## 💾 Dataset

The dashboard is designed for the **Zomato Restaurant Dataset** CSV file. The dataset is not required to be stored in this GitHub repository: upload the CSV through the sidebar of the live app when prompted.

The app expects columns including:

- `City`
- `Aggregate rating`
- `Price range`
- `Restaurant Name`
- `Votes`

## ▶️ Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/zomato-restaurant-dashboard.git
   cd zomato-restaurant-dashboard
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows:

   ```bash
   .venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the dashboard:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL shown in your terminal, then upload the Zomato CSV using the sidebar.

> Replace `YOUR-USERNAME` in the clone command with your GitHub username and repository URL.

## ☁️ Deployment

This dashboard is deployed using **Streamlit Community Cloud**. The live link is:

https://pseb-task-hvtrgtbus2gdw9gfaqso4z.streamlit.app/

## 📝 Notes

- Restaurants with an aggregate rating of `0` are excluded from average-rating charts because they are generally marked as not rated in this dataset.
- Average ratings and city counts depend on the filters selected in the dashboard.
- Keep the dataset private if it contains any information you do not intend to share publicly.

## 📄 License

No license has been specified for this project. Add a license file if you want to define how others may use, modify, or distribute the code.
