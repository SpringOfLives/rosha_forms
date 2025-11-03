# Project Name (Replace with your actual project name)

## 💡 Introduction

This project aims to create a dedicated application form website. Currently, Therosha uses Google Forms for their Musical application form, which lacks the desired convenience in areas such as **data storage, user interface (UI), and overall professionalism**. This dedicated application seeks to provide a superior, custom-tailored solution.

---

## 🚀 Getting Started

This guide will help you set up and run the project locally.

### Prerequisites

Before you begin, ensure you have the following tools installed on your system:

1.  **uv** (Python Package Manager)
    * Installation Guide: [https://docs.astral.sh/uv/guides/install-python/](https://docs.astral.sh/uv/guides/install-python/)
2.  **Node.js** (JavaScript Runtime)
    * Installation Guide: [https://nodejs.org/en/download](https://nodejs.org/en/download)
3.  **pnpm** (Fast, Disk Space Efficient Package Manager)
    * Installation Guide: [https://pnpm.io/installation](https://pnpm.io/installation)

### 🛠 Installation & Setup

Once all prerequisites are installed, follow these steps to set up and run the project:

1. **Install Dependencies**
   * Run this command to install both Python and Node.js dependencies automatically:
     ```bash
     make install
     ```
   * This will:
     - Use `uv sync` to install all Python packages defined in `pyproject.toml`.
     - Use `pnpm install` to install all Node.js packages from `pnpm-lock.yaml` and `package.json`.

2. **Apply Database Migrations**
   * Run this command to create and apply all database migrations:
     ```bash
     make migrate
     ```

3. **Create Superuser**
   * Run this command to create an admin account for accessing the Django admin panel:
     ```bash
     make superuser
     ```

4. **Build and Watch CSS**
   * This command builds the project's CSS file and starts a watch mode that continuously monitors for changes:
     ```bash
     make css
     ```
   * **Note:** You should run this command in a separate terminal window as it will run continuously in watch mode.

5. **Run the Server**
   * This command starts the project server:
     ```bash
     make start
     ```

You should now be able to access the application in your web browser!