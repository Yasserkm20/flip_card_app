# Ice Breaker Cards App

Welcome to the **Ice Breaker Cards App**! This interactive web application is designed to help you break the ice and spark conversations in a fun and engaging way. The app features 30 unique cards, each with a question or prompt that encourages creativity, storytelling, and self-expression. Simply flip a card to reveal the question and start the conversation!

---

## Features

- **30 Unique Cards**: Each card contains a fun and thought-provoking question or prompt.
- **Flip Animation**: Enjoy a smooth flip animation when revealing the card's content.
- **Responsive Design**: The app is designed to work seamlessly on both desktop and mobile devices.
- **Custom Styling**: Beautifully styled with a blurred background image and modern card design.
- **Session State Management**: The app remembers which cards have been flipped, so you can continue where you left off.

---

## How to Use

1. **Open the App**: Launch the app in your browser.
2. **Flip a Card**: Click the "🧊 أكسر 🧊" button below any card to flip it and reveal the question or prompt.
3. **Answer the Question**: Share your answer with the group or reflect on it individually.
4. **Continue Exploring**: Flip more cards to discover new questions and keep the conversation going!

---

## Installation

To run this app locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Yasserkm20/flip_card_app.git
   cd flip_card_app
   ```

2. **Install Dependencies**:
   Make sure you have Python installed, then install the required dependencies:
   ```bash
   pip install streamlit
   ```

3. **Run the App**:
   Start the app using Streamlit:
   ```bash
   streamlit run flip_card_app.py
   ```

4. **Open in Browser**:
   The app will automatically open in your default web browser. If it doesn't, navigate to `http://localhost:8501`.

---

## Customization

- **Change Questions**: Modify the `cards` list in the code to add or update questions.
- **Update Styling**: Edit the CSS in the `flip_css` variable to customize the app's appearance.
- **Add More Cards**: Increase the number of cards by updating the `st.session_state.flipped_cards` list and adding more entries to the `cards` list.

---

## Technologies Used

- **Streamlit**: A powerful framework for building interactive web apps with Python.
- **HTML/CSS**: Used for styling and creating the flip card effect.
- **Session State**: Manages the state of flipped cards across user interactions.

---

## Contributing

Contributions are welcome! If you'd like to improve the app, feel free to open an issue or submit a pull request. Here are some ideas for contributions:
- Add more cards with new questions.
- Improve the UI/UX design.
- Add support for multiple languages.

---

## Acknowledgments

- **Streamlit**: For making it easy to build and share data apps.
- **Google Fonts**: For providing the Tajawal font used in the app.
- **Unsplash/Image Providers**: For the background image (replace with your own if needed).

---

Enjoy using the **Ice Breaker Cards App**! 🎉
