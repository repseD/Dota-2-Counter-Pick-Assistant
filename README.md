# Expert System for Dota 2 Counter-Pick Assistant

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)](https://docs.python.org/3/library/tkinter.html)
[![Pillow](https://img.shields.io/badge/Image%20Processing-Pillow-red)](https://python-pillow.org/)


### Overview

This is a desktop application built with Python that implements an **expert system** for recommending counter-picks in the popular MOBA game Dota 2. The system uses a decision tree to guide the user through a series of questions about the match state (enemy heroes, player's role, items) and provides a hero recommendation based on the answers.

### Purpose

The main goal of this project is to demonstrate the practical application of expert systems and decision trees for solving complex decision-making problems in a specific domain (esports). It can be used as an educational tool for new players or as a prototype for more complex analytical systems.

### Technologies Used

*   **Python**: The core programming language.
*   **Tkinter**: Standard Python library for creating the graphical user interface (GUI).
*   **Pillow (PIL Fork)**: Library for processing and displaying images of heroes.
*   **Object-Oriented Programming (OOP)**: The project is built using classes and objects.

### How It Works

1.  **Data Structure**: The knowledge base of the expert system is represented as a list of `Node` objects. Each node contains:
    *   A question or final answer (`text`)
    *   An image number for visual representation (`img_num`)
    *   References (indexes) to the next nodes for "Yes" (`to_yes`) and "No" (`to_no`) answers.

2.  **Algorithm**:
    *   The application starts from the root node of the decision tree.
    *   For the current node, it displays a question and an image.
    *   The user answers the question by clicking the "Yes" or "No" button.
    *   Based on the answer, the application navigates to the next corresponding node.
    *   The process continues until a terminal node (a node without `to_yes`/`to_no` links) is reached, where the final hero recommendation is displayed.

3.  **Interface**:
    *   The main window is divided into three parts:
        *   **Left and Right Columns**: Contain buttons for quick navigation to specific questions, allowing the user to start from different scenarios.
        *   **Central Area**: Dynamically displays the current question/answer, image, and navigation buttons.

### Installation and Launch

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/repseD/Dota-2-Counter-Pick-Assistant.git
    cd Dota-2-Counter-Pick-Assistant
    ```

2.  **Create and activate a virtual environment** (recommended):
    ```bash
    python -m venv .venv
    # For Windows (PowerShell)
    .\.venv\Scripts\Activate.ps1
    # For Windows (CMD)
    .\.venv\Scripts\activate.bat
    # For Linux/macOS
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install Pillow
    ```

4.  **Run the application**:
    ```bash
    python main.py
    ```

### Important Note

For the application to work correctly, you need to have image files named `0.png`, `1.png`, `2.png`, etc., in the same directory as the script. These images are used for visual representation of heroes and questions.

---
